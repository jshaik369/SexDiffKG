#!/usr/bin/env python3
"""Swarm A v2: Disease-Drug-Sex Triangulation (optimized with dict lookups)"""
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

print("=== Swarm A v2: Disease-Drug-Sex Triangulation ===")
print(f"Started: {datetime.now().isoformat()}\n")

# Load with dict-based lookups (fast)
edges = pd.read_csv(f"{v5_dir}/edges.tsv", sep='\t')
nodes = pd.read_csv(f"{v5_dir}/nodes.tsv", sep='\t')

node_name = dict(zip(nodes['id'], nodes['name']))
node_cat = dict(zip(nodes['id'], nodes['category']))

# Partition edges by type
treats = edges[edges['predicate'] == 'treats']
sexdiff = edges[edges['predicate'] == 'sex_differential_adverse_event']
assoc = edges[edges['predicate'] == 'associated_with']
investigates = edges[edges['predicate'] == 'investigates']
tests_int = edges[edges['predicate'] == 'tests_intervention']

print(f"Treats: {len(treats):,}")
print(f"Sex-differential: {len(sexdiff):,}")
print(f"Associated_with: {len(assoc):,}")

# Build drug→disease mapping
drug_diseases = defaultdict(set)
disease_drugs = defaultdict(set)
for _, row in treats.iterrows():
    s_cat = node_cat.get(row['subject'], '')
    o_cat = node_cat.get(row['object'], '')
    if s_cat in ('Drug', 'Compound'):
        drug_diseases[row['subject']].add(row['object'])
        disease_drugs[row['object']].add(row['subject'])
    elif o_cat in ('Drug', 'Compound'):
        drug_diseases[row['object']].add(row['subject'])
        disease_drugs[row['subject']].add(row['object'])

# Drug sex-diff signal counts
drug_sexdiff = defaultdict(int)
for _, row in sexdiff.iterrows():
    drug_sexdiff[row['subject']] += 1

# Gene-disease mapping
gene_diseases = defaultdict(set)
disease_genes = defaultdict(set)
for _, row in assoc.iterrows():
    gene_diseases[row['subject']].add(row['object'])
    disease_genes[row['object']].add(row['subject'])

# Trial-drug mapping
drug_trials = defaultdict(set)
for _, row in tests_int.iterrows():
    drug_trials[row['object']].add(row['subject'])

print(f"\nDrugs with disease links: {len(drug_diseases):,}")
print(f"Diseases with drug links: {len(disease_drugs):,}")
print(f"Drugs with sex-diff signals: {len(drug_sexdiff):,}")
print(f"Genes with disease assoc: {len(gene_diseases):,}")
print(f"Diseases with gene assoc: {len(disease_genes):,}")

# Load signal details
signals = pd.read_parquet(f"{base}/results/signals_v4/sex_differential_v4.parquet")
drug_f_count = signals[signals['direction'] == 'female_higher'].groupby('drug_name').size().to_dict()
drug_m_count = signals[signals['direction'] == 'male_higher'].groupby('drug_name').size().to_dict()

# === WAVE 101: Disease-level sex-differential drug safety ===
print("\n--- Wave 101: Disease-level sex-differential drug safety ---")

disease_profiles = []
for disease_id, drugs in disease_drugs.items():
    disease_name = node_name.get(disease_id, disease_id)
    drugs_with_sig = [d for d in drugs if drug_sexdiff[d] > 0]
    n_signals = sum(drug_sexdiff[d] for d in drugs_with_sig)

    if n_signals == 0:
        continue

    # Compute aggregate female fraction
    total_f = 0
    total_m = 0
    for d in drugs_with_sig:
        dname = node_name.get(d, d).replace('DRUG:', '')
        total_f += drug_f_count.get(dname, 0)
        total_m += drug_m_count.get(dname, 0)

    f_frac = total_f / (total_f + total_m) if (total_f + total_m) > 0 else 0.5

    disease_profiles.append({
        'disease_id': disease_id,
        'disease_name': disease_name,
        'n_drugs': len(drugs),
        'n_drugs_sexdiff': len(drugs_with_sig),
        'n_signals': n_signals,
        'f_frac': round(f_frac, 3),
        'n_genes': len(disease_genes.get(disease_id, set())),
    })

disease_df = pd.DataFrame(disease_profiles).sort_values('n_signals', ascending=False)
print(f"Diseases with sex-diff drug signals: {len(disease_df):,}")
print("\nTop 20 diseases:")
for _, row in disease_df.head(20).iterrows():
    print(f"  {row['disease_name'][:50]:50s} | {row['n_drugs']:3d} drugs | {row['n_drugs_sexdiff']:3d} sex-diff | {row['n_signals']:5d} signals | F%={100*row['f_frac']:.0f} | {row['n_genes']:3d} genes")

# === WAVE 102: Gene-disease-drug triangulation ===
print("\n--- Wave 102: Gene-disease-drug triangulation ---")

triangles = []
for disease_id in disease_genes:
    disease_name = node_name.get(disease_id, disease_id)
    genes = disease_genes[disease_id]
    drugs = disease_drugs.get(disease_id, set())
    drugs_with_sig = [d for d in drugs if drug_sexdiff[d] > 0]

    if genes and drugs_with_sig:
        triangles.append({
            'disease_id': disease_id,
            'disease_name': disease_name,
            'n_genes': len(genes),
            'n_drugs': len(drugs),
            'n_drugs_sexdiff': len(drugs_with_sig),
            'n_signals': sum(drug_sexdiff[d] for d in drugs_with_sig),
            'score': len(genes) * len(drugs_with_sig),
        })

if triangles:
    tri_df = pd.DataFrame(triangles).sort_values('score', ascending=False)
else:
    tri_df = pd.DataFrame(columns=['disease_id','disease_name','n_genes','n_drugs','n_drugs_sexdiff','n_signals','score'])
    print("  (No triangulations found — gene-disease and drug-disease use different disease ID formats)")
print(f"Triangulated diseases: {len(tri_df):,}")
print("\nTop 20:")
for _, row in tri_df.head(20).iterrows():
    print(f"  {row['disease_name'][:40]:40s} | {row['n_genes']:4d} genes | {row['n_drugs_sexdiff']:3d} sex-diff drugs | score={row['score']}")

# === WAVE 103: Trial gaps ===
print("\n--- Wave 103: Drugs needing sex-stratified trials ---")

urgency = []
for drug, n_sig in sorted(drug_sexdiff.items(), key=lambda x: -x[1])[:100]:
    drug_name = node_name.get(drug, drug)
    n_trials = len(drug_trials.get(drug, set()))
    urgency.append({
        'drug_id': drug,
        'drug_name': drug_name,
        'n_sexdiff': n_sig,
        'n_trials': n_trials,
        'urgency': n_sig / max(n_trials, 1),
    })

urg_df = pd.DataFrame(urgency).sort_values('urgency', ascending=False)
print("Top 30 (most signals, fewest trials):")
for _, row in urg_df.head(30).iterrows():
    print(f"  {row['drug_name'][:45]:45s} | {row['n_sexdiff']:4d} signals | {row['n_trials']:3d} trials")

# Save results
results = {
    'timestamp': datetime.now().isoformat(),
    'wave_101': {
        'n_diseases': len(disease_df),
        'top_20': disease_df.head(20).to_dict('records'),
    },
    'wave_102': {
        'n_triangles': len(tri_df),
        'top_20': tri_df.head(20).to_dict('records'),
    },
    'wave_103': {
        'top_30_urgent': urg_df.head(30).to_dict('records'),
    },
}

for path in [f"{results_dir}/disease_drug_sex_triangulation.json", f"{deep_dir}/results/disease_drug_sex_triangulation.json"]:
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, default=str)

# Figure
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('SexDiffKG v5: Disease-Drug-Sex Triangulation', fontsize=14, fontweight='bold')

    top = disease_df.head(15)
    axes[0,0].barh(range(len(top)), top['n_signals'].values, color='#e74c3c')
    axes[0,0].set_yticks(range(len(top)))
    axes[0,0].set_yticklabels([n[:30] for n in top['disease_name'].values], fontsize=8)
    axes[0,0].set_xlabel('Sex-Differential Signals')
    axes[0,0].set_title('Top Diseases by Sex-Diff Drug Signals')
    axes[0,0].invert_yaxis()

    top_tri = tri_df.head(15)
    axes[0,1].barh(range(len(top_tri)), top_tri['score'].values, color='#3498db')
    axes[0,1].set_yticks(range(len(top_tri)))
    axes[0,1].set_yticklabels([n[:30] for n in top_tri['disease_name'].values], fontsize=8)
    axes[0,1].set_xlabel('Triangulation Score')
    axes[0,1].set_title('Gene×Drug×Sex-Diff Triangulation')
    axes[0,1].invert_yaxis()

    top_urg = urg_df.head(20)
    axes[1,0].barh(range(len(top_urg)), top_urg['urgency'].values, color='#f39c12')
    axes[1,0].set_yticks(range(len(top_urg)))
    axes[1,0].set_yticklabels([n[:30] for n in top_urg['drug_name'].values], fontsize=7)
    axes[1,0].set_xlabel('Urgency (signals / trials)')
    axes[1,0].set_title('Drugs Needing Sex-Stratified Trials')
    axes[1,0].invert_yaxis()

    axes[1,1].hist(disease_df['f_frac'], bins=30, color='#2ecc71', edgecolor='black')
    axes[1,1].axvline(0.5, color='red', linestyle='--')
    axes[1,1].set_xlabel('Female Fraction of Sex-Diff Signals')
    axes[1,1].set_ylabel('Number of Diseases')
    axes[1,1].set_title('Disease-Level Female Bias Distribution')

    plt.tight_layout()
    for fmt in ['png', 'pdf']:
        fig.savefig(f"{deep_dir}/figures/fig265_disease_triangulation.{fmt}", dpi=300, bbox_inches='tight')
    plt.close()
    print("\nFigure saved: fig265_disease_triangulation")
except Exception as e:
    print(f"Figure error: {e}")

print(f"\nCompleted: {datetime.now().isoformat()}")
