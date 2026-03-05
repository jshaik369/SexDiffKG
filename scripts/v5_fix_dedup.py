#!/usr/bin/env python3
"""Fix v5: deduplicate edges, verify v4 preservation, update ground truth"""
import pandas as pd
import json
import hashlib
import os
from datetime import datetime

base = "/home/jshaik369/sexdiffkg"
v4_dir = f"{base}/data/kg_v4"
v5_dir = f"{base}/data/kg_v5"

print("=== v5 Edge Deduplication Fix ===\n")

# Load
v4_edges = pd.read_csv(f"{v4_dir}/edges.tsv", sep='\t')
v5_nodes = pd.read_csv(f"{v5_dir}/nodes.tsv", sep='\t')
v5_edges = pd.read_csv(f"{v5_dir}/edges.tsv", sep='\t')

print(f"v4 edges (file): {len(v4_edges):,}")
print(f"v4 unique triples: {v4_edges.drop_duplicates().shape[0]:,}")
print(f"v5 edges before dedup: {len(v5_edges):,}")

# Deduplicate
v5_dedup = v5_edges.drop_duplicates(subset=['subject', 'predicate', 'object'])
removed = len(v5_edges) - len(v5_dedup)
print(f"v5 edges after dedup: {len(v5_dedup):,} (removed {removed:,})")

# Now verify ALL v4 unique edges are present
v4_unique = v4_edges.drop_duplicates(subset=['subject', 'predicate', 'object'])
v4_set = set(zip(v4_unique['subject'], v4_unique['predicate'], v4_unique['object']))
v5_set = set(zip(v5_dedup['subject'], v5_dedup['predicate'], v5_dedup['object']))

missing = v4_set - v5_set
print(f"\nv4 unique triples: {len(v4_set):,}")
print(f"v4 in v5: {len(v4_set & v5_set):,}")
print(f"Missing: {len(missing):,}")

if missing:
    # These were orphan-removed in merge. Re-add them.
    print("Re-adding missing v4 edges...")
    missing_rows = []
    for s, p, o in missing:
        missing_rows.append({'subject': s, 'predicate': p, 'object': o})
    missing_df = pd.DataFrame(missing_rows)
    v5_dedup = pd.concat([v5_dedup, missing_df], ignore_index=True)
    print(f"v5 after re-add: {len(v5_dedup):,}")

    # Also add any missing nodes for these edges
    all_node_ids = set(v5_nodes['id'].tolist())
    edge_nodes = set(v5_dedup['subject'].tolist()) | set(v5_dedup['object'].tolist())
    new_node_ids = edge_nodes - all_node_ids
    if new_node_ids:
        print(f"Adding {len(new_node_ids)} missing endpoint nodes...")
        # These should all be v4 nodes
        v4_nodes = pd.read_csv(f"{v4_dir}/nodes.tsv", sep='\t')
        v4_node_map = dict(zip(v4_nodes['id'], zip(v4_nodes['name'], v4_nodes['category'])))
        new_rows = []
        for nid in new_node_ids:
            if nid in v4_node_map:
                name, cat = v4_node_map[nid]
                new_rows.append({'id': nid, 'name': name, 'category': cat})
            else:
                new_rows.append({'id': nid, 'name': nid.split(':')[-1], 'category': 'Unknown'})
        v5_nodes = pd.concat([v5_nodes, pd.DataFrame(new_rows)], ignore_index=True)

# Final dedup check
final_dup = v5_dedup.duplicated(subset=['subject', 'predicate', 'object']).sum()
print(f"Final duplicate check: {final_dup}")

# Verify no orphans
node_ids = set(v5_nodes['id'].tolist())
orphan_s = set(v5_dedup['subject'].tolist()) - node_ids
orphan_o = set(v5_dedup['object'].tolist()) - node_ids
print(f"Orphan subjects: {len(orphan_s)}")
print(f"Orphan objects: {len(orphan_o)}")

# Save
print(f"\nSaving cleaned v5...")
v5_nodes.to_csv(f"{v5_dir}/nodes.tsv", sep='\t', index=False)
v5_dedup.to_csv(f"{v5_dir}/edges.tsv", sep='\t', index=False)
triples = v5_dedup[['subject', 'predicate', 'object']]
triples.to_csv(f"{v5_dir}/triples.tsv", sep='\t', index=False, header=False)

# Checksums
for fname in ['nodes.tsv', 'edges.tsv', 'triples.tsv']:
    path = f"{v5_dir}/{fname}"
    md5 = hashlib.md5(open(path, 'rb').read()).hexdigest()
    print(f"  {fname}: {os.path.getsize(path):,} bytes, MD5: {md5}")

# Update ground truth
gt = {
    '_meta': {
        'description': 'SexDiffKG v5 Ground Truth — merged with VEDA-KG (deduped)',
        'created': datetime.now().isoformat(),
        'parent': 'SexDiffKG v4 + VEDA-KG v2.1',
        'note': 'v4 is still canonical for published papers. v5 is the merged version.',
        'dedup_note': 'All edges deduplicated. v4 edges fully preserved.'
    },
    'kg': {
        'canonical_path': 'data/kg_v5/',
        'total_nodes': int(len(v5_nodes)),
        'total_edges': int(len(v5_dedup)),
        'node_types': {k: int(v) for k, v in v5_nodes['category'].value_counts().items()},
        'edge_types': {k: int(v) for k, v in v5_dedup['predicate'].value_counts().items()},
    },
    'v4_preserved': {
        'nodes': int(len(pd.read_csv(f"{v4_dir}/nodes.tsv", sep='\t'))),
        'edges_unique': int(len(v4_set)),
        'in_v5': int(len(v4_set & set(zip(v5_dedup['subject'], v5_dedup['predicate'], v5_dedup['object'])))),
    },
    'checksums': {}
}

for fname in ['nodes.tsv', 'edges.tsv', 'triples.tsv']:
    path = f"{v5_dir}/{fname}"
    gt['checksums'][fname] = hashlib.md5(open(path, 'rb').read()).hexdigest()

with open(f"{v5_dir}/GROUND_TRUTH_v5.json", 'w') as f:
    json.dump(gt, f, indent=2)

# RAID copies
import shutil
shutil.copy(f"{v5_dir}/GROUND_TRUTH_v5.json", f"{base}/results/GROUND_TRUTH_v5.json")
shutil.copy(f"{v5_dir}/GROUND_TRUTH_v5.json", "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg/GROUND_TRUTH_v5.json")

print(f"\n=== FIX COMPLETE ===")
print(f"Nodes: {len(v5_nodes):,}")
print(f"Edges: {len(v5_dedup):,}")
print(f"Node types: {v5_nodes['category'].nunique()}")
print(f"Edge types: {v5_dedup['predicate'].nunique()}")
print(f"v4 preservation: 100%")
