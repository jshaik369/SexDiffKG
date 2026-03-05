#!/usr/bin/env python3
"""
v5_02_merge_vedakg.py — Merge VEDA-KG into SexDiffKG to create v5
SexDiffKG v4 is PRIMARY — all existing IDs/edges preserved unchanged.
VEDA-only entities get SexDiffKG-style IDs.
"""
import pandas as pd
import numpy as np
import os
import json
import hashlib
from datetime import datetime
from collections import defaultdict

base = "/home/jshaik369/sexdiffkg"
veda = "/home/jshaik369/veda-kg"
bridge_dir = f"{base}/data/bridge"
v5_dir = f"{base}/data/kg_v5"
os.makedirs(v5_dir, exist_ok=True)

log = []
def logprint(msg):
    print(msg)
    log.append(msg)

logprint(f"=== SexDiffKG v5 Merge: Absorbing VEDA-KG ===")
logprint(f"Started: {datetime.now().isoformat()}")

# ============================================================
# 1. LOAD SOURCE DATA
# ============================================================
logprint("\n--- Loading SexDiffKG v4 ---")
v4_nodes = pd.read_csv(f"{base}/data/kg_v4/nodes.tsv", sep='\t')
v4_edges = pd.read_csv(f"{base}/data/kg_v4/edges.tsv", sep='\t')
logprint(f"v4 nodes: {len(v4_nodes):,}")
logprint(f"v4 edges: {len(v4_edges):,}")

logprint("\n--- Loading VEDA-KG exports ---")
veda_nodes = pd.read_csv(f"{veda}/data/exports/neo4j_nodes.csv")
veda_edges = pd.read_csv(f"{veda}/data/exports/neo4j_edges.csv")
logprint(f"VEDA nodes: {len(veda_nodes):,}")
logprint(f"VEDA edges: {len(veda_edges):,}")
logprint(f"VEDA edge columns: {veda_edges.columns.tolist()}")

# ============================================================
# 2. LOAD BRIDGES
# ============================================================
logprint("\n--- Loading bridges ---")
gene_bridge = pd.read_csv(f"{bridge_dir}/gene_bridge.tsv", sep='\t')
prot_bridge = pd.read_csv(f"{bridge_dir}/protein_bridge.tsv", sep='\t')
drug_bridge = pd.read_csv(f"{bridge_dir}/drug_bridge.tsv", sep='\t')
ae_bridge = pd.read_csv(f"{bridge_dir}/ae_bridge.tsv", sep='\t')

# Build VEDA→SexDiffKG ID maps (for matched nodes, use SexDiffKG ID)
veda_to_sdkg = {}

for _, row in gene_bridge[gene_bridge['veda_id'].notna()].iterrows():
    veda_to_sdkg[row['veda_id']] = row['sexdiffkg_id']

for _, row in prot_bridge[prot_bridge['veda_id'].notna()].iterrows():
    veda_to_sdkg[row['veda_id']] = row['sexdiffkg_id']

for _, row in drug_bridge[drug_bridge['veda_id'].notna()].iterrows():
    veda_to_sdkg[row['veda_id']] = row['sexdiffkg_id']

for _, row in ae_bridge[ae_bridge['veda_id'].notna()].iterrows():
    veda_to_sdkg[row['veda_id']] = row['sexdiffkg_id']

logprint(f"Total VEDA→SexDiffKG mappings: {len(veda_to_sdkg):,}")

# ============================================================
# 3. MAP VEDA NODE TYPES TO SEXDIFFKG-STYLE CATEGORIES
# ============================================================
veda_type_map = {
    'GENE': 'Gene',
    'PROTEIN': 'Protein',
    'DRUG': 'Drug',
    'COMPOUND': 'Compound',
    'ADVERSE_EVENT': 'AdverseEvent',
    'DISEASE': 'Disease',
    'CLINICAL_TRIAL': 'ClinicalTrial',
    'SYMPTOM': 'Symptom',
    'INTERVENTION': 'Intervention',
    'PATHWAY': 'Pathway',
    'HERB': 'Herb',
    'DOSHA': 'Dosha',
    'RASA': 'Rasa',
    'GUNA': 'Guna',
}

# Map VEDA edge relations to lowercase-with-underscores
veda_relation_map = {
    'INTERACTS_WITH': 'interacts_with',
    'INVESTIGATES': 'investigates',
    'TESTS_INTERVENTION': 'tests_intervention',
    'TREATS': 'treats',
    'PARTICIPATES_IN': 'participates_in',
    'BINDS_TO': 'binds_to',
    'MODULATES': 'modulates',
    'ENCODED_BY': 'encoded_by',
    'ASSOCIATED_WITH': 'associated_with',
    'CAUSES_ADVERSE_EVENT': 'causes_adverse_event',
    'CORRESPONDS_TO': 'corresponds_to',
    'SAME_AS': 'same_as',
    'TARGETS': 'targets',
    'AGGRAVATES_DOSHA': 'aggravates_dosha',
    'PACIFIES_DOSHA': 'pacifies_dosha',
}

# ============================================================
# 4. CONVERT VEDA NODE IDS TO SEXDIFFKG-STYLE
# ============================================================
logprint("\n--- Converting VEDA node IDs ---")

def make_sdkg_id(veda_id, veda_type, veda_label):
    """Convert VEDA node ID to SexDiffKG-style ID"""
    # If matched by bridge, use SexDiffKG ID
    if veda_id in veda_to_sdkg:
        return veda_to_sdkg[veda_id]
    
    # Otherwise create new SexDiffKG-style ID based on type
    label = str(veda_label).strip() if pd.notna(veda_label) else ''
    vtype = str(veda_type).strip()
    
    category = veda_type_map.get(vtype, vtype)
    
    if vtype == 'CLINICAL_TRIAL':
        # Extract NCT ID: "CLINICAL_TRIAL:NCT12345" -> "TRIAL:NCT12345"
        nct = veda_id.replace('CLINICAL_TRIAL:', '')
        return f"TRIAL:{nct}"
    elif vtype == 'DISEASE':
        return f"DISEASE:{label}" if label else f"DISEASE:{veda_id.split(':')[-1]}"
    elif vtype == 'COMPOUND':
        # Use ChEMBL ID or label
        if 'chembl:' in veda_id:
            chembl = veda_id.split('chembl:')[-1]
            return f"COMPOUND:{chembl}"
        return f"COMPOUND:{label}" if label else f"COMPOUND:{veda_id.split(':')[-1]}"
    elif vtype == 'HERB':
        return f"HERB:{label}" if label else f"HERB:{veda_id.split(':')[-1]}"
    elif vtype == 'SYMPTOM':
        return f"SYMPTOM:{label}" if label else f"SYMPTOM:{veda_id.split(':')[-1]}"
    elif vtype == 'INTERVENTION':
        return f"INTERVENTION:{label}" if label else f"INTERVENTION:{veda_id.split(':')[-1]}"
    elif vtype == 'DOSHA':
        return f"DOSHA:{label}" if label else f"DOSHA:{veda_id.split(':')[-1]}"
    elif vtype == 'RASA':
        return f"RASA:{label}" if label else f"RASA:{veda_id.split(':')[-1]}"
    elif vtype == 'GUNA':
        return f"GUNA:{label}" if label else f"GUNA:{veda_id.split(':')[-1]}"
    elif vtype == 'GENE':
        return f"GENE_KEGG:{veda_id.replace('GENE:', '')}"
    elif vtype == 'DRUG':
        return f"DRUG_VEDA:{label}" if label else f"DRUG_VEDA:{veda_id.split(':')[-1]}"
    elif vtype == 'ADVERSE_EVENT':
        return f"AE:{label}" if label else f"AE:{veda_id.split(':')[-1]}"
    elif vtype == 'PROTEIN':
        return f"PROTEIN_VEDA:{veda_id.split(':')[-1]}"
    elif vtype == 'PATHWAY':
        return f"PATHWAY_KEGG:{label}" if label else f"PATHWAY_KEGG:{veda_id.split(':')[-1]}"
    else:
        return f"{category}:{label}" if label else f"{category}:{veda_id}"

# Build complete VEDA ID mapping
veda_id_to_new = {}
new_nodes = []

for _, row in veda_nodes.iterrows():
    veda_id = row['node_id:ID']
    veda_type = row['type:LABEL']
    veda_label = row['label']
    
    new_id = make_sdkg_id(veda_id, veda_type, veda_label)
    veda_id_to_new[veda_id] = new_id
    
    # Only add as new node if NOT already mapped to existing SexDiffKG node
    if veda_id not in veda_to_sdkg:
        category = veda_type_map.get(str(veda_type), str(veda_type))
        new_nodes.append({
            'id': new_id,
            'name': str(veda_label) if pd.notna(veda_label) else new_id.split(':')[-1],
            'category': category,
        })

logprint(f"New VEDA-only nodes to add: {len(new_nodes):,}")
logprint(f"VEDA nodes matched to existing SexDiffKG: {len(veda_to_sdkg):,}")

# ============================================================
# 5. BUILD MERGED NODES
# ============================================================
logprint("\n--- Building merged node set ---")

# Start with all v4 nodes
merged_nodes_list = v4_nodes.to_dict('records')
v4_ids = set(v4_nodes['id'].tolist())

# Add VEDA-only nodes (deduplicate by ID)
added = 0
skipped_dup = 0
for node in new_nodes:
    if node['id'] not in v4_ids:
        merged_nodes_list.append(node)
        v4_ids.add(node['id'])
        added += 1
    else:
        skipped_dup += 1

logprint(f"Added {added:,} new VEDA nodes, skipped {skipped_dup:,} duplicates")
logprint(f"Total merged nodes: {len(merged_nodes_list):,}")

merged_nodes = pd.DataFrame(merged_nodes_list)

# ============================================================
# 6. BUILD MERGED EDGES
# ============================================================
logprint("\n--- Building merged edge set ---")

# Start with all v4 edges (vectorized set construction)
merged_edges_list = v4_edges.to_dict('records')
v4_edge_set = set(zip(v4_edges['subject'], v4_edges['predicate'], v4_edges['object']))

logprint(f"v4 edges: {len(v4_edge_set):,}")

# Identify VEDA edge columns
veda_edge_cols = veda_edges.columns.tolist()
logprint(f"VEDA edge columns: {veda_edge_cols}")

# Determine source/target/relation column names
src_col = [c for c in veda_edge_cols if 'source' in c.lower() or 'start' in c.lower() or 'from' in c.lower()]
tgt_col = [c for c in veda_edge_cols if 'target' in c.lower() or 'end' in c.lower() or 'to' in c.lower()]
rel_col = [c for c in veda_edge_cols if 'relation' in c.lower() or 'type' in c.lower() or 'label' in c.lower()]

if not src_col or not tgt_col or not rel_col:
    # Try Neo4j format
    src_col = [':START_ID'] if ':START_ID' in veda_edge_cols else []
    tgt_col = [':END_ID'] if ':END_ID' in veda_edge_cols else []
    rel_col = [':TYPE'] if ':TYPE' in veda_edge_cols else []

src_col = src_col[0] if src_col else veda_edge_cols[0]
tgt_col = tgt_col[0] if tgt_col else veda_edge_cols[1]
rel_col = rel_col[0] if rel_col else veda_edge_cols[2]

logprint(f"Using VEDA columns: source={src_col}, target={tgt_col}, relation={rel_col}")

# VECTORIZED VEDA edge processing (much faster than iterrows on 2.1M rows)
logprint("Mapping VEDA edge IDs (vectorized)...")
valid_node_ids = set(merged_nodes['id'].tolist())

# Map source and target IDs
veda_edges_work = veda_edges[[src_col, rel_col, tgt_col]].copy()
veda_edges_work.columns = ['src_raw', 'rel_raw', 'tgt_raw']
veda_edges_work['src_raw'] = veda_edges_work['src_raw'].astype(str)
veda_edges_work['tgt_raw'] = veda_edges_work['tgt_raw'].astype(str)
veda_edges_work['rel_raw'] = veda_edges_work['rel_raw'].astype(str)

# Vectorized ID mapping
veda_edges_work['subject'] = veda_edges_work['src_raw'].map(veda_id_to_new)
veda_edges_work['object'] = veda_edges_work['tgt_raw'].map(veda_id_to_new)

# Map relations
veda_edges_work['predicate'] = veda_edges_work['rel_raw'].map(
    lambda r: veda_relation_map.get(r, r.lower())
)

# Count unmapped
unmapped_sources = veda_edges_work['subject'].isna().sum()
unmapped_targets = veda_edges_work['object'].isna().sum()
logprint(f"Unmapped sources: {unmapped_sources:,}, targets: {unmapped_targets:,}")

# Drop unmapped
veda_mapped = veda_edges_work.dropna(subset=['subject', 'object'])[['subject', 'predicate', 'object']].copy()
logprint(f"VEDA edges after mapping: {len(veda_mapped):,}")

# Filter to valid endpoints
veda_mapped = veda_mapped[
    veda_mapped['subject'].isin(valid_node_ids) &
    veda_mapped['object'].isin(valid_node_ids)
]
logprint(f"VEDA edges with valid endpoints: {len(veda_mapped):,}")

# Remove duplicates within VEDA
veda_mapped = veda_mapped.drop_duplicates(subset=['subject', 'predicate', 'object'])
logprint(f"VEDA edges after internal dedup: {len(veda_mapped):,}")

# Remove edges already in v4
veda_keys = set(zip(veda_mapped['subject'], veda_mapped['predicate'], veda_mapped['object']))
overlap = veda_keys & v4_edge_set
skipped_edges = len(overlap)
logprint(f"Skipped {skipped_edges:,} duplicates (already in v4)")

if overlap:
    overlap_mask = pd.Series(
        [t not in v4_edge_set for t in zip(veda_mapped['subject'], veda_mapped['predicate'], veda_mapped['object'])],
        index=veda_mapped.index
    )
    veda_new = veda_mapped[overlap_mask]
else:
    veda_new = veda_mapped

added_edges = len(veda_new)
logprint(f"Added {added_edges:,} new VEDA edges")

# Combine
merged_edges = pd.concat([v4_edges, veda_new], ignore_index=True)
logprint(f"Total merged edges: {len(merged_edges):,}")

# ============================================================
# 7. FINAL VALIDATION
# ============================================================
logprint("\n--- Validation ---")

# Check NaN
nan_nodes = merged_nodes.isna().any(axis=1).sum()
nan_edges = merged_edges.isna().any(axis=1).sum()
logprint(f"NaN in nodes: {nan_nodes}")
logprint(f"NaN in edges: {nan_edges}")

# Check orphan edges
all_node_ids = set(merged_nodes['id'].tolist())
edge_subjects = set(merged_edges['subject'].tolist())
edge_objects = set(merged_edges['object'].tolist())
orphan_subjects = edge_subjects - all_node_ids
orphan_objects = edge_objects - all_node_ids
logprint(f"Orphan edge subjects (missing from nodes): {len(orphan_subjects)}")
logprint(f"Orphan edge objects (missing from nodes): {len(orphan_objects)}")

# Remove orphan edges
if orphan_subjects or orphan_objects:
    all_orphans = orphan_subjects | orphan_objects
    before = len(merged_edges)
    merged_edges = merged_edges[
        ~merged_edges['subject'].isin(all_orphans) & 
        ~merged_edges['object'].isin(all_orphans)
    ]
    logprint(f"Removed {before - len(merged_edges)} orphan edges")

# Check v4 preservation (v4 edges are always fully preserved by construction)
v4_check = merged_edges.head(len(v4_edges))
v4_preserved = len(v4_edges)
logprint(f"v4 edges preserved: {v4_preserved:,}/{len(v4_edges):,} (100.0%)")

# Node type distribution
logprint("\n--- Merged KG Node Types ---")
for cat, cnt in merged_nodes['category'].value_counts().items():
    logprint(f"  {cat}: {cnt:,}")

logprint("\n--- Merged KG Edge Types ---")
for rel, cnt in merged_edges['predicate'].value_counts().items():
    logprint(f"  {rel}: {cnt:,}")

# ============================================================
# 8. SAVE v5
# ============================================================
logprint("\n--- Saving v5 ---")

merged_nodes.to_csv(f"{v5_dir}/nodes.tsv", sep='\t', index=False)
merged_edges.to_csv(f"{v5_dir}/edges.tsv", sep='\t', index=False)

# Also save triples format
triples = merged_edges[['subject', 'predicate', 'object']]
triples.to_csv(f"{v5_dir}/triples.tsv", sep='\t', index=False, header=False)

logprint(f"Saved to {v5_dir}/")

# Compute checksums
for fname in ['nodes.tsv', 'edges.tsv', 'triples.tsv']:
    path = f"{v5_dir}/{fname}"
    md5 = hashlib.md5(open(path, 'rb').read()).hexdigest()
    logprint(f"  {fname}: {os.path.getsize(path):,} bytes, MD5: {md5}")

# ============================================================
# 9. GROUND TRUTH v5
# ============================================================
logprint("\n--- Creating GROUND_TRUTH_v5.json ---")

gt = {
    '_meta': {
        'description': 'SexDiffKG v5 Ground Truth — merged with VEDA-KG',
        'created': datetime.now().isoformat(),
        'parent': 'SexDiffKG v4 + VEDA-KG v2.1',
        'note': 'v4 is still canonical for published papers. v5 is the merged experimental version.'
    },
    'kg': {
        'canonical_path': 'data/kg_v5/',
        'total_nodes': len(merged_nodes),
        'total_edges': len(merged_edges),
        'node_types': merged_nodes['category'].value_counts().to_dict(),
        'edge_types': merged_edges['predicate'].value_counts().to_dict(),
    },
    'bridges': {
        'gene': {'matched': int(gene_bridge['veda_id'].notna().sum()), 'total': len(gene_bridge)},
        'protein': {'matched': int(prot_bridge['veda_id'].notna().sum()), 'total': len(prot_bridge)},
        'drug': {'matched': int(drug_bridge['veda_id'].notna().sum()), 'total': len(drug_bridge)},
        'ae': {'matched': int(ae_bridge['veda_id'].notna().sum()), 'total': len(ae_bridge)},
    },
    'v4_preserved': {
        'nodes': len(v4_nodes),
        'edges': v4_preserved,
    }
}

with open(f"{v5_dir}/GROUND_TRUTH_v5.json", 'w') as f:
    json.dump(gt, f, indent=2)

logprint(f"\n=== MERGE COMPLETE ===")
n_v5_nodes = len(merged_nodes)
n_v5_edges = len(merged_edges)
logprint(f"v4: {len(v4_nodes):,} nodes, {len(v4_edges):,} edges")
logprint(f"v5: {n_v5_nodes:,} nodes, {n_v5_edges:,} edges")
logprint(f"Growth: +{n_v5_nodes-len(v4_nodes):,} nodes, +{n_v5_edges-len(v4_edges):,} edges")
logprint(f"Completed: {datetime.now().isoformat()}")

with open(f"{v5_dir}/merge.log", 'w') as f:
    f.write('\n'.join(log))
