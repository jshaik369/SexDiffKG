#!/usr/bin/env python3
"""Swarm Block D v4: Protein Network Sex Bias Propagation
Fixed: pathway bridge now uses Ensembl ID mappings from drug_targets.parquet
(participates_in uses GENE:ENSG/ENSP/ENST, not descriptive names)
"""
import pandas as pd
import numpy as np
import json
import os
from datetime import datetime
from collections import defaultdict

base = "/home/jshaik369/sexdiffkg"
v5_dir = f"{base}/data/kg_v5"
results_dir = f"{base}/results/analysis"
deep_dir = "/tmp/sexdiffkg-deep-analysis"
os.makedirs(f"{deep_dir}/results", exist_ok=True)
os.makedirs(f"{deep_dir}/figures", exist_ok=True)

print("=== Swarm D v4: Protein Network Sex Bias Propagation ===")
print(f"Started: {datetime.now().isoformat()}\n")

edges = pd.read_csv(f"{v5_dir}/edges.tsv", sep='\t')
nodes = pd.read_csv(f"{v5_dir}/nodes.tsv", sep='\t')

node_name = dict(zip(nodes['id'], nodes['name']))
node_cat = dict(zip(nodes['id'], nodes['category']))

# === Build comprehensive bridges ===
print("--- Building bridges ---")
dt = pd.read_parquet(f"{base}/data/processed/molecular/drug_targets.parquet")

# Bridge 1: descriptive gene name → PROTEIN (for drug→target→protein chain)
gene_to_protein = {}
protein_to_gene = {}
# Bridge 2: Ensembl gene ID → protein bias (for pathway scoring)
ensembl_to_protein = {}  # GENE:ENSG... → PROTEIN:ENSP...
ensp_gene_to_protein = {}  # GENE:ENSP... → PROTEIN:ENSP...

for _, row in dt.iterrows():
    gene_id = f"GENE:{row['target_name']}"
    sid = str(row.get('string_id', ''))
    ensembl = str(row.get('ensembl_gene_id', ''))

    if pd.notna(row.get('string_id')) and 'ENSP' in sid:
        ensp = sid.split('.')[-1] if '.' in sid else sid
        prot_id = f"PROTEIN:{ensp}"
        gene_to_protein[gene_id] = prot_id
        protein_to_gene[prot_id] = gene_id

        # Map Ensembl gene ID to same protein
        if pd.notna(row.get('ensembl_gene_id')) and ensembl.startswith('ENSG'):
            ensembl_to_protein[f"GENE:{ensembl}"] = prot_id

        # Map GENE:ENSP to PROTEIN:ENSP (participates_in uses ENSP as gene IDs too)
        ensp_gene_to_protein[f"GENE:{ensp}"] = prot_id

# Also from encoded_by edges
encoded_by = edges[edges['predicate'] == 'encoded_by']
for _, row in encoded_by.iterrows():
    s_cat = node_cat.get(row['subject'], '')
    o_cat = node_cat.get(row['object'], '')
    if s_cat == 'Protein' and 'Gene' in str(o_cat):
        gene_to_protein[row['object']] = row['subject']
        protein_to_gene[row['subject']] = row['object']
    elif 'Gene' in str(s_cat) and o_cat == 'Protein':
        gene_to_protein[row['subject']] = row['object']
        protein_to_gene[row['object']] = row['subject']

print(f"Gene(name)→Protein: {len(gene_to_protein):,}")
print(f"Gene(ENSG)→Protein: {len(ensembl_to_protein):,}")
print(f"Gene(ENSP)→Protein: {len(ensp_gene_to_protein):,}")

# Combined pathway bridge: any GENE:* → PROTEIN:*
pathway_gene_to_protein = {}
pathway_gene_to_protein.update(gene_to_protein)
pathway_gene_to_protein.update(ensembl_to_protein)
pathway_gene_to_protein.update(ensp_gene_to_protein)
print(f"Combined pathway bridge: {len(pathway_gene_to_protein):,}")

# === PPI network ===
ppi = edges[edges['predicate'] == 'interacts_with']
ppi_adj = defaultdict(set)
for _, row in ppi.iterrows():
    ppi_adj[row['subject']].add(row['object'])
    ppi_adj[row['object']].add(row['subject'])

ppi_proteins = set(ppi_adj.keys())
print(f"Proteins in PPI: {len(ppi_proteins):,}")

# === Drug sex-diff signal counts ===
sexdiff = edges[edges['predicate'] == 'sex_differential_adverse_event']
drug_sexdiff_count = sexdiff.groupby('subject').size().to_dict()

# === Drug→target (gene) → protein mapping ===
targets_edges = edges[edges['predicate'] == 'targets']
drug_proteins = defaultdict(set)
protein_drugs = defaultdict(set)
for _, row in targets_edges.iterrows():
    drug = row['subject']
    gene = row['object']
    protein = gene_to_protein.get(gene)
    if protein and protein in ppi_proteins:
        drug_proteins[drug].add(protein)
        protein_drugs[protein].add(drug)

print(f"Drugs mapped to PPI proteins: {len(drug_proteins):,}")
print(f"PPI proteins targeted by drugs: {len(protein_drugs):,}")

# === Compute drug F-fractions ===
signals = pd.read_parquet(f"{base}/results/signals_v4/sex_differential_v4.parquet")
drug_f_frac = {}
for drug_name, group in signals.groupby('drug_name'):
    drug_key = f"DRUG:{drug_name}"
    n_f = (group['direction'] == 'female_higher').sum()
    n_m = (group['direction'] == 'male_higher').sum()
    if n_f + n_m > 0:
        drug_f_frac[drug_key] = n_f / (n_f + n_m)
print(f"Drugs with F-fraction: {len(drug_f_frac):,}")

# === Protein bias ===
protein_bias = {}
for protein, drugs in protein_drugs.items():
    f_fracs = []
    weights = []
    for drug in drugs:
        if drug in drug_f_frac and drug in drug_sexdiff_count:
            f_fracs.append(drug_f_frac[drug])
            weights.append(drug_sexdiff_count[drug])
    if f_fracs:
        weighted_f = np.average(f_fracs, weights=weights)
        gene = protein_to_gene.get(protein)
        gene_name = node_name.get(gene, '') if gene else ''
        protein_bias[protein] = {
            'f_frac': float(weighted_f),
            'n_drugs': len(f_fracs),
            'total_signals': sum(weights),
            'name': node_name.get(protein, protein),
            'gene_name': gene_name,
        }

print(f"Proteins with direct sex bias: {len(protein_bias):,}")

print("\nTop 20 directly scored proteins:")
sorted_bias = sorted(protein_bias.items(), key=lambda x: -x[1]['total_signals'])
for prot_id, info in sorted_bias[:20]:
    gene = info['gene_name'] or info['name']
    d = 'F' if info['f_frac'] > 0.55 else ('M' if info['f_frac'] < 0.45 else '=')
    print(f"  {gene[:40]:40s} | F%={100*info['f_frac']:5.1f} | {info['n_drugs']:3d} drugs | {info['total_signals']:5d} signals | {d}")

# === 1-hop propagation ===
print("\n--- 1-hop propagation ---")
propagated = {}
for protein in ppi_adj:
    direct = protein_bias.get(protein, {}).get('f_frac')
    n_drugs_direct = protein_bias.get(protein, {}).get('n_drugs', 0)

    neighbor_scores = []
    for neighbor in ppi_adj[protein]:
        if neighbor in protein_bias:
            neighbor_scores.append(protein_bias[neighbor]['f_frac'])

    if direct is not None or neighbor_scores:
        all_scores = []
        if direct is not None:
            all_scores.extend([direct] * 3)
        all_scores.extend(neighbor_scores)
        score = float(np.mean(all_scores))
        confidence = len(neighbor_scores) + (3 if direct is not None else 0)
        propagated[protein] = {
            'score': score,
            'direct': direct,
            'n_scored_neighbors': len(neighbor_scores),
            'n_drugs': n_drugs_direct,
            'degree': len(ppi_adj[protein]),
            'confidence': confidence,
            'name': node_name.get(protein, protein),
        }

print(f"Proteins with propagated scores: {len(propagated):,}")

# Hub analysis
hub_data = []
for prot, info in propagated.items():
    if info['confidence'] < 2:
        continue
    hub_score = abs(info['score'] - 0.5) * np.log1p(info['confidence']) * np.log1p(info['degree'])
    direction = 'female' if info['score'] > 0.55 else ('male' if info['score'] < 0.45 else 'balanced')
    gene = protein_to_gene.get(prot)
    gene_name = node_name.get(gene, '') if gene else ''
    hub_data.append({
        'protein_id': prot,
        'protein_name': info['name'],
        'gene_name': gene_name or info['name'],
        'propagated_f_frac': round(info['score'], 4),
        'direct_score': info['direct'],
        'degree': info['degree'],
        'n_scored_neighbors': info['n_scored_neighbors'],
        'confidence': info['confidence'],
        'hub_score': round(float(hub_score), 4),
        'bias_direction': direction,
    })

hub_df = pd.DataFrame(hub_data).sort_values('hub_score', ascending=False) if hub_data else pd.DataFrame()
print(f"Filtered hubs (conf>=2): {len(hub_df)}")

female_hubs = hub_df[hub_df['bias_direction'] == 'female'] if len(hub_df) > 0 else pd.DataFrame()
male_hubs = hub_df[hub_df['bias_direction'] == 'male'] if len(hub_df) > 0 else pd.DataFrame()
print(f"  Female-biased: {len(female_hubs)}, Male-biased: {len(male_hubs)}")

print("\nTop 15 female-biased hubs:")
for _, row in female_hubs.head(15).iterrows():
    label = row['gene_name'][:40] if row['gene_name'] else row['protein_name'][:40]
    print(f"  {label:40s} | F%={100*row['propagated_f_frac']:.1f} | deg={row['degree']:4d} | conf={row['confidence']:3d}")

print("\nTop 15 male-biased hubs:")
for _, row in male_hubs.head(15).iterrows():
    label = row['gene_name'][:40] if row['gene_name'] else row['protein_name'][:40]
    print(f"  {label:40s} | F%={100*row['propagated_f_frac']:.1f} | deg={row['degree']:4d} | conf={row['confidence']:3d}")

# === Pathway-level aggregation (via Ensembl bridge) ===
print("\n--- Pathway-level sex bias (via Ensembl bridge) ---")

pathway_edges = edges[edges['predicate'] == 'participates_in']
pathway_genes = defaultdict(set)
for _, row in pathway_edges.iterrows():
    if node_cat.get(row['object']) == 'Pathway':
        pathway_genes[row['object']].add(row['subject'])

print(f"Pathways: {len(pathway_genes):,}")

# For each pathway gene, find corresponding protein via ALL bridges
pathway_bias = []
for pathway, genes in pathway_genes.items():
    scores = []
    for gene in genes:
        # Try all bridge types
        protein = pathway_gene_to_protein.get(gene)
        if protein and protein in propagated:
            scores.append(propagated[protein]['score'])
            continue
        # Also try: if gene IS an ENSP id, check PROTEIN:ENSP directly
        gene_suffix = gene.replace('GENE:', '')
        if gene_suffix.startswith('ENSP'):
            prot_id = f"PROTEIN:{gene_suffix}"
            if prot_id in propagated:
                scores.append(propagated[prot_id]['score'])

    if len(scores) >= 3:
        pathway_bias.append({
            'pathway_id': pathway,
            'pathway_name': node_name.get(pathway, pathway),
            'mean_f_frac': round(float(np.mean(scores)), 4),
            'std_f_frac': round(float(np.std(scores)), 4),
            'n_scored_genes': len(scores),
            'n_total_genes': len(genes),
            'coverage_pct': round(100 * len(scores) / len(genes), 1),
            'bias': 'female' if np.mean(scores) > 0.55 else ('male' if np.mean(scores) < 0.45 else 'balanced'),
        })

pw_df = pd.DataFrame(pathway_bias).sort_values('mean_f_frac', ascending=False) if pathway_bias else pd.DataFrame()
print(f"Pathways with sex bias scores: {len(pw_df):,}")

if len(pw_df) > 0:
    f_pw = pw_df[pw_df['bias'] == 'female']
    m_pw = pw_df[pw_df['bias'] == 'male']
    b_pw = pw_df[pw_df['bias'] == 'balanced']
    print(f"  Female-biased: {len(f_pw)}, Male-biased: {len(m_pw)}, Balanced: {len(b_pw)}")

    print("\nTop 15 female-biased pathways:")
    for _, row in pw_df.head(15).iterrows():
        print(f"  {row['pathway_name'][:50]:50s} | F%={100*row['mean_f_frac']:.1f} | {row['n_scored_genes']}/{row['n_total_genes']} genes")

    print("\nTop 15 male-biased pathways:")
    for _, row in pw_df.tail(15).iterrows():
        print(f"  {row['pathway_name'][:50]:50s} | F%={100*row['mean_f_frac']:.1f} | {row['n_scored_genes']}/{row['n_total_genes']} genes")
else:
    print("  No pathways scored — checking bridge coverage...")
    # Diagnostic
    pw_sample = list(pathway_genes.keys())[:3]
    for pw in pw_sample:
        genes = pathway_genes[pw]
        n_bridged = sum(1 for g in genes if pathway_gene_to_protein.get(g) is not None)
        n_direct_ensp = sum(1 for g in genes if f"PROTEIN:{g.replace('GENE:', '')}" in propagated and g.replace('GENE:', '').startswith('ENSP'))
        print(f"  Pathway {pw}: {len(genes)} genes, {n_bridged} bridged, {n_direct_ensp} direct ENSP")
        for g in list(genes)[:5]:
            prot = pathway_gene_to_protein.get(g)
            in_prop = prot in propagated if prot else False
            print(f"    {g} → {prot} → in_propagated: {in_prop}")

# === Save ===
results = {
    'timestamp': datetime.now().isoformat(),
    'version': 'v4',
    'stats': {
        'ppi_proteins': len(ppi_proteins),
        'gene_to_protein_mappings': len(gene_to_protein),
        'ensembl_bridge': len(ensembl_to_protein),
        'ensp_gene_bridge': len(ensp_gene_to_protein),
        'combined_pathway_bridge': len(pathway_gene_to_protein),
        'drugs_mapped_to_ppi': len(drug_proteins),
        'proteins_with_direct_bias': len(protein_bias),
        'proteins_with_propagated': len(propagated),
        'filtered_hubs': len(hub_df),
        'pathways_scored': len(pw_df),
    },
    'top_directly_scored': [{
        'protein': prot_id,
        'gene_name': info['gene_name'],
        'f_frac': info['f_frac'],
        'n_drugs': info['n_drugs'],
        'total_signals': info['total_signals'],
    } for prot_id, info in sorted_bias[:50]],
    'top_hubs': hub_df.head(50).to_dict('records') if len(hub_df) > 0 else [],
    'pathway_bias': {
        'female_biased': pw_df.head(30).to_dict('records') if len(pw_df) > 0 else [],
        'male_biased': pw_df.tail(30).to_dict('records') if len(pw_df) > 0 else [],
    },
}

for path in [f"{results_dir}/ppi_sex_bias_propagation.json", f"{deep_dir}/results/ppi_sex_bias_propagation.json"]:
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, default=str)

# Figure
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(18, 14))
    fig.suptitle('SexDiffKG v5: Protein Network Sex Bias Propagation (v4)', fontsize=14, fontweight='bold')

    # Panel 1: Direct protein bias
    if protein_bias:
        direct_scores = [info['f_frac'] for info in protein_bias.values()]
        axes[0, 0].hist(direct_scores, bins=30, color='#9b59b6', edgecolor='black', alpha=0.7)
        axes[0, 0].axvline(0.5, color='black', linestyle='--', alpha=0.5)
        axes[0, 0].set_xlabel('Female Fraction')
        axes[0, 0].set_ylabel('Count')
        axes[0, 0].set_title(f'Direct Protein Sex Bias (n={len(protein_bias):,})')

    # Panel 2: Top hubs
    if len(hub_df) >= 15:
        top_h = hub_df.head(20)
        colors = ['#e74c3c' if d == 'female' else '#3498db' if d == 'male' else '#95a5a6'
                  for d in top_h['bias_direction']]
        labels = [g[:25] if g else p[:25] for g, p in zip(top_h['gene_name'], top_h['protein_name'])]
        axes[0, 1].barh(range(len(top_h)), top_h['hub_score'].values, color=colors)
        axes[0, 1].set_yticks(range(len(top_h)))
        axes[0, 1].set_yticklabels(labels, fontsize=7)
        axes[0, 1].set_xlabel('Hub Score')
        axes[0, 1].set_title('Top Sex-Bias Protein Hubs')
        axes[0, 1].invert_yaxis()

    # Panel 3: Propagated distribution
    if len(hub_df) > 0:
        axes[1, 0].hist(hub_df['propagated_f_frac'], bins=40, color='#2ecc71', edgecolor='black', alpha=0.7)
        axes[1, 0].axvline(0.5, color='black', linestyle='--', alpha=0.5)
        axes[1, 0].set_xlabel('Propagated Female Fraction')
        axes[1, 0].set_ylabel('Count')
        axes[1, 0].set_title(f'Propagated Bias (conf>=2, n={len(hub_df):,})')

    # Panel 4: Pathway bias
    if len(pw_df) >= 10:
        top_pw = pd.concat([pw_df.head(10), pw_df.tail(10)])
        pw_colors = ['#e74c3c' if f > 0.55 else '#3498db' if f < 0.45 else '#95a5a6'
                     for f in top_pw['mean_f_frac']]
        axes[1, 1].barh(range(len(top_pw)), (top_pw['mean_f_frac'] - 0.5).values, color=pw_colors)
        axes[1, 1].set_yticks(range(len(top_pw)))
        axes[1, 1].set_yticklabels([n[:30] for n in top_pw['pathway_name'].values], fontsize=7)
        axes[1, 1].axvline(0, color='black', linestyle='-', alpha=0.5)
        axes[1, 1].set_xlabel('Sex Bias (F% - 50%)')
        axes[1, 1].set_title(f'Pathway-Level Sex Bias (n={len(pw_df):,})')
        axes[1, 1].invert_yaxis()
    else:
        axes[1, 1].text(0.5, 0.5, f'Pathways scored: {len(pw_df)}\n(Limited bridge coverage)', ha='center', va='center', fontsize=12)
        axes[1, 1].set_title('Pathway-Level Sex Bias')

    plt.tight_layout()
    for fmt in ['png', 'pdf']:
        fig.savefig(f"{deep_dir}/figures/fig267_ppi_sex_bias.{fmt}", dpi=300, bbox_inches='tight')
    plt.close()
    print("\nFigure saved: fig267_ppi_sex_bias")
except Exception as e:
    print(f"Figure error: {e}")

print(f"\nCompleted: {datetime.now().isoformat()}")
