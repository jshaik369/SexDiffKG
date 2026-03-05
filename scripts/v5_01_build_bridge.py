#!/usr/bin/env python3
"""
v5_01_build_bridge.py — Build 5 identifier bridges between SexDiffKG and VEDA-KG
Bridges: Gene, Protein, Drug, AE, Pathway
Output: data/bridge/*.tsv
"""
import pandas as pd
import numpy as np
import os
import gzip
import json
import sqlite3
from collections import defaultdict
from datetime import datetime

base = "/home/jshaik369/sexdiffkg"
veda = "/home/jshaik369/veda-kg"
bridge_dir = f"{base}/data/bridge"
os.makedirs(bridge_dir, exist_ok=True)

log = []
def logprint(msg):
    print(msg)
    log.append(msg)

logprint(f"=== SexDiffKG ↔ VEDA-KG Bridge Builder ===")
logprint(f"Started: {datetime.now().isoformat()}")

# ============================================================
# 1. LOAD SEXDIFFKG NODES
# ============================================================
logprint("\n--- Loading SexDiffKG v4 nodes ---")
sexdiff_nodes = pd.read_csv(f"{base}/data/kg_v4/nodes.tsv", sep='\t')
logprint(f"Total nodes: {len(sexdiff_nodes):,}")
for cat, cnt in sexdiff_nodes['category'].value_counts().items():
    logprint(f"  {cat}: {cnt:,}")

# Extract by type
sdkg_genes = sexdiff_nodes[sexdiff_nodes['category'] == 'Gene']['id'].tolist()
sdkg_proteins = sexdiff_nodes[sexdiff_nodes['category'] == 'Protein']['id'].tolist()
sdkg_drugs = sexdiff_nodes[sexdiff_nodes['category'] == 'Drug']['id'].tolist()
sdkg_aes = sexdiff_nodes[sexdiff_nodes['category'] == 'AdverseEvent']['id'].tolist()
sdkg_pathways = sexdiff_nodes[sexdiff_nodes['category'] == 'Pathway']['id'].tolist()

# ============================================================
# 2. LOAD VEDA-KG NODES (from CSV exports, not empty SQLite)
# ============================================================
logprint("\n--- Loading VEDA-KG nodes ---")
veda_nodes = pd.read_csv(f"{veda}/data/exports/neo4j_nodes.csv")
logprint(f"Total VEDA nodes: {len(veda_nodes):,}")
logprint(f"Columns: {veda_nodes.columns.tolist()}")
# Column names: node_id:ID, label, type:LABEL, confidence:float
veda_type_col = 'type:LABEL'
veda_id_col = 'node_id:ID'
veda_name_col = 'label'
for vtype, cnt in veda_nodes[veda_type_col].value_counts().items():
    logprint(f"  {vtype}: {cnt:,}")

# ============================================================
# 3. LOAD BRIDGE RESOURCES
# ============================================================
logprint("\n--- Loading bridge resources ---")

# 3a. drug_targets.parquet — THE primary bridge
dt = pd.read_parquet(f"{base}/data/processed/molecular/drug_targets.parquet")
logprint(f"drug_targets.parquet: {len(dt):,} rows, {dt['target_name'].nunique()} unique targets, {dt['drug_name'].nunique()} unique drugs")

# 3b. id_mappings.parquet — UniProt crossref
idmap = pd.read_parquet(f"{base}/data/processed/molecular/id_mappings.parquet")
logprint(f"id_mappings.parquet: {len(idmap):,} rows")

# 3c. UniProt KEGG mapping from idmapping.dat.gz
logprint("Loading UniProt → KEGG mapping from HUMAN_9606_idmapping.dat.gz...")
uniprot_to_kegg = {}
kegg_to_gene = {}
gene_to_kegg = {}
idmap_path = f"{base}/data/raw/uniprot/HUMAN_9606_idmapping.dat.gz"
if os.path.exists(idmap_path):
    with gzip.open(idmap_path, 'rt') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 3:
                uniprot_id, db, val = parts
                if db == 'KEGG':
                    uniprot_to_kegg[uniprot_id] = val
                elif db == 'Gene_Name':
                    # Map gene name to UniProt for later KEGG lookup
                    if val not in gene_to_kegg:
                        gene_to_kegg[val] = uniprot_id
    logprint(f"  UniProt→KEGG: {len(uniprot_to_kegg):,} mappings")
    logprint(f"  Gene_Name→UniProt: {len(gene_to_kegg):,} mappings")
else:
    logprint(f"  WARNING: {idmap_path} not found")

# ============================================================
# 4. BUILD GENE BRIDGE
# ============================================================
logprint("\n--- Building Gene Bridge ---")

# SexDiffKG genes use format: "GENE:TargetName" where TargetName is a descriptive name
# drug_targets.parquet maps target_name → gene_symbol
# UniProt idmapping maps gene_symbol → KEGG hsa:ID

# Build target_name → gene_symbol map
target_to_gene = {}
for _, row in dt.drop_duplicates(subset=['target_name', 'gene_symbol']).iterrows():
    if pd.notna(row['target_name']) and pd.notna(row['gene_symbol']):
        tn = row['target_name']
        gs = row['gene_symbol']
        target_to_gene[tn] = gs

# VEDA genes use format: "GENE:hsa:XXXX"
veda_genes = veda_nodes[veda_nodes[veda_type_col] == 'GENE']
logprint(f"VEDA GENE nodes: {len(veda_genes):,}")

# Build gene_symbol → KEGG ID map
gene_symbol_to_kegg = {}
for gene_sym, uniprot_id in gene_to_kegg.items():
    if uniprot_id in uniprot_to_kegg:
        kegg_id = uniprot_to_kegg[uniprot_id]
        gene_symbol_to_kegg[gene_sym] = kegg_id

logprint(f"gene_symbol→KEGG: {len(gene_symbol_to_kegg):,} mappings")

# Also build a reverse map from KEGG to gene_symbol for VEDA→SexDiffKG matching
kegg_to_gene_symbol = {v: k for k, v in gene_symbol_to_kegg.items()}

# Build gene bridge
gene_bridges = []
# Path 1: SexDiffKG gene name → drug_targets target_name → gene_symbol → KEGG
for gene_id in sdkg_genes:
    gene_name = gene_id.replace("GENE:", "")
    # Check if this gene name is a target_name in drug_targets
    if gene_name in target_to_gene:
        gs = target_to_gene[gene_name]
        kegg_id = gene_symbol_to_kegg.get(gs)
        veda_id = f"GENE:{kegg_id}" if kegg_id else None
        gene_bridges.append({
            'sexdiffkg_id': gene_id,
            'veda_id': veda_id,
            'gene_symbol': gs,
            'kegg_id': kegg_id,
            'bridge_method': 'drug_targets→gene_symbol→KEGG'
        })

# Path 2: For SexDiffKG genes NOT in drug_targets, try direct gene_symbol match
# Many SexDiffKG gene IDs ARE the gene symbol (from STRING/Reactome)
matched_ids = {b['sexdiffkg_id'] for b in gene_bridges}
for gene_id in sdkg_genes:
    if gene_id in matched_ids:
        continue
    gene_name = gene_id.replace("GENE:", "")
    # Try as gene symbol directly
    kegg_id = gene_symbol_to_kegg.get(gene_name)
    if kegg_id:
        gene_bridges.append({
            'sexdiffkg_id': gene_id,
            'veda_id': f"GENE:{kegg_id}",
            'gene_symbol': gene_name,
            'kegg_id': kegg_id,
            'bridge_method': 'direct_gene_symbol→KEGG'
        })

gene_df = pd.DataFrame(gene_bridges)
gene_matched = gene_df[gene_df['veda_id'].notna()]
logprint(f"Gene bridge: {len(gene_matched):,} matched / {len(sdkg_genes):,} SexDiffKG genes ({100*len(gene_matched)/max(1,len(sdkg_genes)):.1f}%)")
gene_df.to_csv(f"{bridge_dir}/gene_bridge.tsv", sep='\t', index=False)

# ============================================================
# 5. BUILD PROTEIN BRIDGE
# ============================================================
logprint("\n--- Building Protein Bridge ---")

# SexDiffKG proteins: "PROTEIN:ENSP00000378426" format (Ensembl protein IDs)
# VEDA proteins: "PROTEIN:string:9606.ENSP00000378426" (STRING format)
# Bridge: prepend "9606." to ENSP ID

veda_proteins = veda_nodes[veda_nodes[veda_type_col] == 'PROTEIN']
logprint(f"VEDA PROTEIN nodes: {len(veda_proteins):,}")

# Build set of VEDA protein IDs for quick lookup
veda_protein_ids = set(veda_proteins[veda_id_col].tolist())

protein_bridges = []
for prot_id in sdkg_proteins:
    prot_name = prot_id.replace("PROTEIN:", "")
    # Try STRING format
    string_id = f"PROTEIN:string:9606.{prot_name}"
    if string_id in veda_protein_ids:
        protein_bridges.append({
            'sexdiffkg_id': prot_id,
            'veda_id': string_id,
            'bridge_method': 'ENSP→STRING_prefix'
        })
    else:
        # Try UniProt mapping via id_mappings.parquet
        match = idmap[idmap['string_id'] == f"9606.{prot_name}"]
        if len(match) > 0:
            uniprot_id = match.iloc[0]['uniprot_id']
            veda_uniprot = f"PROTEIN:uniprot:{uniprot_id}"
            if veda_uniprot in veda_protein_ids:
                protein_bridges.append({
                    'sexdiffkg_id': prot_id,
                    'veda_id': veda_uniprot,
                    'bridge_method': 'ENSP→UniProt'
                })
            else:
                protein_bridges.append({
                    'sexdiffkg_id': prot_id,
                    'veda_id': None,
                    'bridge_method': 'no_match'
                })
        else:
            protein_bridges.append({
                'sexdiffkg_id': prot_id,
                'veda_id': None,
                'bridge_method': 'no_match'
            })

prot_df = pd.DataFrame(protein_bridges)
prot_matched = prot_df[prot_df['veda_id'].notna()]
logprint(f"Protein bridge: {len(prot_matched):,} matched / {len(sdkg_proteins):,} SexDiffKG proteins ({100*len(prot_matched)/max(1,len(sdkg_proteins)):.1f}%)")
prot_df.to_csv(f"{bridge_dir}/protein_bridge.tsv", sep='\t', index=False)

# ============================================================
# 6. BUILD DRUG BRIDGE
# ============================================================
logprint("\n--- Building Drug Bridge ---")

veda_drugs = veda_nodes[veda_nodes[veda_type_col] == 'DRUG']
veda_compounds = veda_nodes[veda_nodes[veda_type_col] == 'COMPOUND']
logprint(f"VEDA DRUG nodes: {len(veda_drugs):,}")
logprint(f"VEDA COMPOUND nodes: {len(veda_compounds):,}")

# Get VEDA drug/compound names for matching
id_col = veda_id_col
name_col = veda_name_col

# Build VEDA drug name lookup (case-insensitive)
veda_drug_lookup = {}
for _, row in veda_drugs.iterrows():
    vid = str(row[id_col])
    vname = str(row[name_col]).upper().strip() if pd.notna(row[name_col]) else ''
    # Also extract name from ID (e.g., "DRUG:clinicaltrials:aspirin" -> "aspirin")
    id_name = vid.split(':')[-1].upper().strip()
    veda_drug_lookup[vname] = vid
    veda_drug_lookup[id_name] = vid

for _, row in veda_compounds.iterrows():
    vid = str(row[id_col])
    vname = str(row[name_col]).upper().strip() if pd.notna(row[name_col]) else ''
    id_name = vid.split(':')[-1].upper().strip()
    veda_drug_lookup[vname] = vid
    veda_drug_lookup[id_name] = vid

# Also use ChEMBL synonyms from drug_targets.parquet
chembl_drug_map = {}
for _, row in dt.drop_duplicates(subset=['drug_name', 'chembl_id']).iterrows():
    if pd.notna(row['drug_name']) and pd.notna(row['chembl_id']):
        chembl_drug_map[row['drug_name'].upper()] = row['chembl_id']

drug_bridges = []
for drug_id in sdkg_drugs:
    drug_name = drug_id.replace("DRUG:", "").upper().strip()
    
    # Method 1: Direct name match
    veda_match = veda_drug_lookup.get(drug_name)
    if veda_match:
        drug_bridges.append({
            'sexdiffkg_id': drug_id,
            'veda_id': veda_match,
            'bridge_method': 'name_match'
        })
        continue
    
    # Method 2: ChEMBL ID match
    chembl_id = chembl_drug_map.get(drug_name)
    if chembl_id:
        compound_id = f"COMPOUND:chembl:{chembl_id}"
        if compound_id in veda_drug_lookup.values():
            drug_bridges.append({
                'sexdiffkg_id': drug_id,
                'veda_id': compound_id,
                'bridge_method': 'chembl_id'
            })
            continue
    
    # No match
    drug_bridges.append({
        'sexdiffkg_id': drug_id,
        'veda_id': None,
        'bridge_method': 'no_match'
    })

drug_df = pd.DataFrame(drug_bridges)
drug_matched = drug_df[drug_df['veda_id'].notna()]
logprint(f"Drug bridge: {len(drug_matched):,} matched / {len(sdkg_drugs):,} SexDiffKG drugs ({100*len(drug_matched)/max(1,len(sdkg_drugs)):.1f}%)")
drug_df.to_csv(f"{bridge_dir}/drug_bridge.tsv", sep='\t', index=False)

# ============================================================
# 7. BUILD AE BRIDGE
# ============================================================
logprint("\n--- Building AE Bridge ---")

veda_aes = veda_nodes[veda_nodes[veda_type_col] == 'ADVERSE_EVENT']
logprint(f"VEDA ADVERSE_EVENT nodes: {len(veda_aes):,}")

# Build VEDA AE name lookup (case-insensitive)
veda_ae_lookup = {}
for _, row in veda_aes.iterrows():
    vid = str(row[veda_id_col])
    # Extract AE name from ID (e.g., "ADVERSE_EVENT:faers:nausea" -> "nausea")
    ae_name = vid.split(':')[-1].upper().strip()
    veda_ae_lookup[ae_name] = vid

ae_bridges = []
for ae_id in sdkg_aes:
    ae_name = ae_id.replace("AE:", "").upper().strip()
    veda_match = veda_ae_lookup.get(ae_name)
    ae_bridges.append({
        'sexdiffkg_id': ae_id,
        'veda_id': veda_match,
        'bridge_method': 'name_match' if veda_match else 'no_match'
    })

ae_df = pd.DataFrame(ae_bridges)
ae_matched = ae_df[ae_df['veda_id'].notna()]
logprint(f"AE bridge: {len(ae_matched):,} matched / {len(sdkg_aes):,} SexDiffKG AEs ({100*len(ae_matched)/max(1,len(sdkg_aes)):.1f}%)")
ae_df.to_csv(f"{bridge_dir}/ae_bridge.tsv", sep='\t', index=False)

# ============================================================
# 8. PATHWAY BRIDGE (no direct mapping — both kept)
# ============================================================
logprint("\n--- Pathway Bridge ---")
logprint(f"SexDiffKG pathways (Reactome): {len(sdkg_pathways):,}")
veda_pathways = veda_nodes[veda_nodes[veda_type_col] == 'PATHWAY']
logprint(f"VEDA pathways (KEGG): {len(veda_pathways):,}")
logprint("No direct bridge (different ontologies). Both pathway sets will be kept in merged KG.")

# ============================================================
# 9. SUMMARY REPORT
# ============================================================
logprint("\n=== BRIDGE SUMMARY ===")
summary = {
    'timestamp': datetime.now().isoformat(),
    'gene_bridge': {
        'total_sexdiffkg': len(sdkg_genes),
        'matched': len(gene_matched),
        'coverage_pct': round(100*len(gene_matched)/max(1,len(sdkg_genes)), 1),
        'methods': gene_df['bridge_method'].value_counts().to_dict() if len(gene_df) > 0 else {}
    },
    'protein_bridge': {
        'total_sexdiffkg': len(sdkg_proteins),
        'matched': len(prot_matched),
        'coverage_pct': round(100*len(prot_matched)/max(1,len(sdkg_proteins)), 1),
        'methods': prot_df['bridge_method'].value_counts().to_dict() if len(prot_df) > 0 else {}
    },
    'drug_bridge': {
        'total_sexdiffkg': len(sdkg_drugs),
        'matched': len(drug_matched),
        'coverage_pct': round(100*len(drug_matched)/max(1,len(sdkg_drugs)), 1),
        'methods': drug_df['bridge_method'].value_counts().to_dict() if len(drug_df) > 0 else {}
    },
    'ae_bridge': {
        'total_sexdiffkg': len(sdkg_aes),
        'matched': len(ae_matched),
        'coverage_pct': round(100*len(ae_matched)/max(1,len(sdkg_aes)), 1)
    },
    'pathway_bridge': {
        'sexdiffkg_reactome': len(sdkg_pathways),
        'veda_kegg': len(veda_pathways),
        'note': 'No direct mapping — both pathway sets kept'
    },
    'veda_total_nodes': len(veda_nodes),
    'sexdiffkg_total_nodes': len(sexdiff_nodes)
}

for bridge_name in ['gene_bridge', 'protein_bridge', 'drug_bridge', 'ae_bridge']:
    b = summary[bridge_name]
    logprint(f"  {bridge_name}: {b['matched']:,}/{b['total_sexdiffkg']:,} ({b['coverage_pct']}%)")

with open(f"{bridge_dir}/bridge_summary.json", 'w') as f:
    json.dump(summary, f, indent=2)

logprint(f"\nBridge files saved to: {bridge_dir}/")
logprint(f"Completed: {datetime.now().isoformat()}")

# Save log
with open(f"{bridge_dir}/bridge_build.log", 'w') as f:
    f.write('\n'.join(log))
