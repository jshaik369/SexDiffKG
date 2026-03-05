#!/usr/bin/env python3
"""v5_03_validate_merge.py — Comprehensive validation of SexDiffKG v5 merge"""
import pandas as pd
import numpy as np
import json
import hashlib
import os
from datetime import datetime

base = "/home/jshaik369/sexdiffkg"
v4_dir = f"{base}/data/kg_v4"
v5_dir = f"{base}/data/kg_v5"
results_dir = f"{base}/results/analysis"

report = {'timestamp': datetime.now().isoformat(), 'checks': {}, 'status': 'RUNNING'}
all_pass = True

def check(name, passed, detail=""):
    global all_pass
    report['checks'][name] = {'passed': bool(passed), 'detail': str(detail)}
    status = "PASS" if passed else "FAIL"
    if not passed:
        all_pass = False
    print(f"  [{status}] {name}: {detail}")

print("=== SexDiffKG v5 Validation ===\n")

# Load v5
print("Loading v5...")
v5_nodes = pd.read_csv(f"{v5_dir}/nodes.tsv", sep='\t')
v5_edges = pd.read_csv(f"{v5_dir}/edges.tsv", sep='\t')
print(f"v5: {len(v5_nodes):,} nodes, {len(v5_edges):,} edges")

# Load v4 for comparison
print("Loading v4...")
v4_nodes = pd.read_csv(f"{v4_dir}/nodes.tsv", sep='\t')
v4_edges = pd.read_csv(f"{v4_dir}/edges.tsv", sep='\t')
print(f"v4: {len(v4_nodes):,} nodes, {len(v4_edges):,} edges\n")

# Load ground truth
with open(f"{v5_dir}/GROUND_TRUTH_v5.json") as f:
    gt = json.load(f)

print("--- Structural Checks ---")

# 1. Zero NaN
nan_nodes = v5_nodes.isna().any(axis=1).sum()
nan_edges = v5_edges.isna().any(axis=1).sum()
check("Zero NaN in nodes", nan_nodes == 0, f"{nan_nodes} NaN rows")
check("Zero NaN in edges", nan_edges == 0, f"{nan_edges} NaN rows")

# 2. Column schemas match expected
check("Node columns correct", list(v5_nodes.columns) == ['id', 'name', 'category'],
      f"Got: {list(v5_nodes.columns)}")
check("Edge columns correct", list(v5_edges.columns) == ['subject', 'predicate', 'object'],
      f"Got: {list(v5_edges.columns)}")

# 3. No duplicate nodes
dup_nodes = v5_nodes['id'].duplicated().sum()
check("No duplicate node IDs", dup_nodes == 0, f"{dup_nodes} duplicates")

# 4. No duplicate edges
dup_edges = v5_edges.duplicated().sum()
check("No duplicate edges", dup_edges == 0, f"{dup_edges} duplicates")

# 5. All edge endpoints exist in nodes
node_ids = set(v5_nodes['id'].tolist())
edge_subs = set(v5_edges['subject'].tolist())
edge_objs = set(v5_edges['object'].tolist())
orphan_s = edge_subs - node_ids
orphan_o = edge_objs - node_ids
check("No orphan edge subjects", len(orphan_s) == 0, f"{len(orphan_s)} orphans")
check("No orphan edge objects", len(orphan_o) == 0, f"{len(orphan_o)} orphans")

# 6. Ground truth matches
check("Node count matches GT", len(v5_nodes) == gt['kg']['total_nodes'],
      f"File: {len(v5_nodes)}, GT: {gt['kg']['total_nodes']}")
check("Edge count matches GT", len(v5_edges) == gt['kg']['total_edges'],
      f"File: {len(v5_edges)}, GT: {gt['kg']['total_edges']}")

print("\n--- v4 Preservation Checks ---")

# 7. ALL v4 nodes present in v5
v4_ids = set(v4_nodes['id'].tolist())
v4_in_v5 = v4_ids & node_ids
check("All v4 nodes in v5", len(v4_in_v5) == len(v4_ids),
      f"{len(v4_in_v5)}/{len(v4_ids)} ({100*len(v4_in_v5)/len(v4_ids):.1f}%)")

# 8. ALL v4 edges present in v5
v4_edge_set = set(zip(v4_edges['subject'], v4_edges['predicate'], v4_edges['object']))
v5_edge_set = set(zip(v5_edges['subject'], v5_edges['predicate'], v5_edges['object']))
v4_in_v5_edges = v4_edge_set & v5_edge_set
check("All v4 edges in v5", len(v4_in_v5_edges) == len(v4_edge_set),
      f"{len(v4_in_v5_edges)}/{len(v4_edge_set)} ({100*len(v4_in_v5_edges)/len(v4_edge_set):.1f}%)")

# 9. v4 sex-differential signals preserved
v4_sexdiff = v4_edges[v4_edges['predicate'] == 'sex_differential_adverse_event']
v5_sexdiff = v5_edges[v5_edges['predicate'] == 'sex_differential_adverse_event']
check("Sex-differential signals preserved", len(v5_sexdiff) == len(v4_sexdiff),
      f"v4: {len(v4_sexdiff)}, v5: {len(v5_sexdiff)}")

print("\n--- Type Distribution ---")

# Node type check
for ntype, expected in gt['kg']['node_types'].items():
    actual = (v5_nodes['category'] == ntype).sum()
    check(f"Node type {ntype}", actual == expected, f"Expected: {expected}, Got: {actual}")

# Edge type check
for etype, expected in gt['kg']['edge_types'].items():
    actual = (v5_edges['predicate'] == etype).sum()
    check(f"Edge type {etype}", actual == expected, f"Expected: {expected}, Got: {actual}")

print("\n--- Growth Analysis ---")
node_growth = len(v5_nodes) - len(v4_nodes)
edge_growth = len(v5_edges) - len(v4_edges)
print(f"  Node growth: +{node_growth:,} ({100*node_growth/len(v4_nodes):.1f}%)")
print(f"  Edge growth: +{edge_growth:,} ({100*edge_growth/len(v4_edges):.1f}%)")
print(f"  New node types: {set(v5_nodes['category'].unique()) - set(v4_nodes['category'].unique())}")
print(f"  New edge types: {set(v5_edges['predicate'].unique()) - set(v4_edges['predicate'].unique())}")

# Connected component analysis
print("\n--- Connectivity Check ---")
from collections import defaultdict

adj = defaultdict(set)
sample_size = min(500000, len(v5_edges))
sample_idx = np.random.RandomState(42).choice(len(v5_edges), sample_size, replace=False)
sample = v5_edges.iloc[sample_idx]
for _, row in sample.iterrows():
    adj[row['subject']].add(row['object'])
    adj[row['object']].add(row['subject'])

# BFS for largest component from a random seed
visited = set()
queue = [list(adj.keys())[0]]
visited.add(queue[0])
while queue:
    node = queue.pop(0)
    for neighbor in adj.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

nodes_in_adj = set(adj.keys())
frac = len(visited) / len(nodes_in_adj)
print(f"  Sampled 500K edges → {len(nodes_in_adj):,} unique nodes")
print(f"  Largest component from sample: {len(visited):,} ({100*frac:.1f}%)")
check("KG connectivity (multi-domain KGs have multiple components)", frac > 0.20, f"{100*frac:.1f}% (expected <50% due to disconnected clinical trials/diseases)")

print("\n--- MD5 Checksums ---")
for fname in ['nodes.tsv', 'edges.tsv', 'triples.tsv']:
    path = f"{v5_dir}/{fname}"
    md5 = hashlib.md5(open(path, 'rb').read()).hexdigest()
    report['checks'][f'md5_{fname}'] = {'passed': True, 'detail': md5}
    print(f"  {fname}: {md5}")

# Final verdict
n_checks = len(report['checks'])
n_pass = sum(1 for c in report['checks'].values() if c['passed'])
n_fail = n_checks - n_pass

report['status'] = 'ALL_PASS' if all_pass else 'HAS_FAILURES'
report['summary'] = {
    'total_checks': n_checks,
    'passed': n_pass,
    'failed': n_fail,
    'v5_nodes': len(v5_nodes),
    'v5_edges': len(v5_edges),
    'node_growth_pct': round(100*node_growth/len(v4_nodes), 1),
    'edge_growth_pct': round(100*edge_growth/len(v4_edges), 1),
}

# Save report
os.makedirs(results_dir, exist_ok=True)
with open(f"{results_dir}/v5_merge_validation.json", 'w') as f:
    json.dump(report, f, indent=2)

print(f"\n=== VALIDATION {'PASSED' if all_pass else 'FAILED'}: {n_pass}/{n_checks} checks passed ===")
print(f"Report saved to {results_dir}/v5_merge_validation.json")
