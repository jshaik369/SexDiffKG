#!/usr/bin/env python3
"""v5.2 KG Validation — Per KG Expert Manual Section 1 & 3

Checks:
1. Zero NaN/null in nodes and edges
2. All edge endpoints exist in nodes
3. No duplicate edges
4. All v4 deduplicated edges preserved (100% preservation required)
5. Connected component analysis (LCC should be >95%)
6. Node/edge type distribution
7. Bridge edge verification (same_gene, encodes)
8. MD5 checksums match GROUND_TRUTH_v5.2.json
"""
import os
import sys
import json
import hashlib
import pandas as pd
from datetime import datetime
from collections import deque

BASE = "/home/jshaik369/sexdiffkg"
V52_DIR = f"{BASE}/data/kg_v5.2"
V4_DIR = f"{BASE}/data/kg_v4"
VAULT = "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg"

print("=" * 70)
print("v5.2 KG VALIDATION")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

results = {"timestamp": datetime.now().isoformat(), "checks": {}, "pass": True}

def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    results["checks"][name] = {"status": status, "detail": detail}
    if not condition:
        results["pass"] = False
    print(f"  [{status}] {name}: {detail}")

# Load data
print("\n[1/8] Loading v5.2 data...")
nodes = pd.read_csv(f"{V52_DIR}/nodes.tsv", sep="\t")
edges = pd.read_csv(f"{V52_DIR}/edges.tsv", sep="\t")
print(f"  Nodes: {len(nodes):,}, Edges: {len(edges):,}")

# Check 1: Zero NaN
print("\n[2/8] NaN check...")
nodes_nan = nodes.isnull().sum().sum()
edges_nan = edges[["subject", "predicate", "object"]].isnull().sum().sum()
check("nodes_no_nan", nodes_nan == 0, f"{nodes_nan} NaN values in nodes")
check("edges_no_nan", edges_nan == 0, f"{edges_nan} NaN values in edges")

# Check 2: All endpoints in nodes
print("\n[3/8] Edge endpoint check...")
node_ids = set(nodes["id"])
edge_subjects = set(edges["subject"])
edge_objects = set(edges["object"])
edge_entities = edge_subjects | edge_objects
missing_from_nodes = edge_entities - node_ids
check("all_endpoints_in_nodes", len(missing_from_nodes) == 0,
      f"{len(missing_from_nodes)} entities in edges but not nodes")

# Check 3: No duplicate edges
print("\n[4/8] Duplicate edge check...")
n_dupes = len(edges) - len(edges.drop_duplicates(subset=["subject", "predicate", "object"]))
check("no_duplicate_edges", n_dupes == 0, f"{n_dupes} duplicate edges")

# Check 4: v4 preservation
print("\n[5/8] v4 edge preservation check...")
v4_triples = pd.read_csv(f"{V4_DIR}/triples.tsv", sep="\t", header=None, names=["s", "p", "o"])
v4_deduped = v4_triples.drop_duplicates()
v52_set = set(zip(edges["subject"], edges["predicate"], edges["object"]))
v4_in_v52 = sum(1 for s, p, o in zip(v4_deduped["s"], v4_deduped["p"], v4_deduped["o"])
                if (s, p, o) in v52_set)
pct = v4_in_v52 / len(v4_deduped) * 100
check("v4_100pct_preserved", v4_in_v52 == len(v4_deduped),
      f"{v4_in_v52:,}/{len(v4_deduped):,} ({pct:.1f}%)")

# Check 5: Connected components
print("\n[6/8] Connected component analysis...")
adj = {}
for _, row in edges.iterrows():
    s, o = row["subject"], row["object"]
    if s not in adj: adj[s] = []
    if o not in adj: adj[o] = []
    adj[s].append(o)
    adj[o].append(s)

visited = set()
components = []
for start in adj:
    if start in visited:
        continue
    comp = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        comp.add(node)
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
    components.append(comp)

components.sort(key=len, reverse=True)
lcc_frac = len(components[0]) / len(visited) * 100
check("lcc_gt_95pct", lcc_frac > 95.0,
      f"LCC={len(components[0]):,} nodes ({lcc_frac:.1f}%), {len(components)} components")

orphans = set(nodes["id"]) - set(adj.keys())
check("orphan_count", True, f"{len(orphans):,} orphan nodes (no edges)")

# Check 6: Bridge edges exist
print("\n[7/8] Bridge edge verification...")
same_gene_count = len(edges[edges["predicate"] == "same_gene"])
encodes_count = len(edges[edges["predicate"] == "encodes"])
check("same_gene_bridges", same_gene_count > 0, f"{same_gene_count:,} same_gene edges")
check("encodes_bridges", encodes_count > 0, f"{encodes_count:,} encodes edges")
check("total_bridges", same_gene_count + encodes_count > 10000,
      f"{same_gene_count + encodes_count:,} total bridge edges")

# Check 7: Node and edge type counts
print("\n[8/8] Type distribution...")
cat_counts = nodes["category"].value_counts()
rel_counts = edges["predicate"].value_counts()
check("node_types", cat_counts.shape[0] >= 10,
      f"{cat_counts.shape[0]} node types")
check("edge_types", rel_counts.shape[0] >= 15,
      f"{rel_counts.shape[0]} edge types")

# Check 8: MD5 checksums
def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

gt_path = f"{V52_DIR}/GROUND_TRUTH_v5.2.json"
if os.path.exists(gt_path):
    with open(gt_path) as f:
        gt = json.load(f)
    gt_checksums = gt.get("checksums", {})
    for fname in ["nodes_tsv", "edges_tsv", "triples_tsv"]:
        fpath = f"{V52_DIR}/{fname.replace('_', '.')}"
        actual = md5_file(fpath)
        expected = gt_checksums.get(fname, "")
        check(f"md5_{fname}", actual == expected,
              f"{'match' if actual == expected else f'MISMATCH: {actual} vs {expected}'}")

# Summary
print(f"\n{'=' * 70}")
n_pass = sum(1 for c in results["checks"].values() if c["status"] == "PASS")
n_fail = sum(1 for c in results["checks"].values() if c["status"] == "FAIL")
n_total = len(results["checks"])
print(f"VALIDATION: {n_pass}/{n_total} PASS, {n_fail}/{n_total} FAIL")
print(f"Overall: {'PASS' if results['pass'] else 'FAIL'}")
print(f"{'=' * 70}")

# Node type summary
print(f"\nNode types ({cat_counts.shape[0]}):")
for cat, count in cat_counts.items():
    print(f"  {cat}: {count:,}")

print(f"\nEdge types ({rel_counts.shape[0]}):")
for rel, count in rel_counts.items():
    print(f"  {rel}: {count:,}")

# Save
out_path = f"{V52_DIR}/validation_report.json"
results["node_counts"] = {k: int(v) for k, v in cat_counts.items()}
results["edge_counts"] = {k: int(v) for k, v in rel_counts.items()}
results["summary"] = {"pass": n_pass, "fail": n_fail, "total": n_total}
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nReport saved: {out_path}")

vault_path = f"{VAULT}/v52_validation_report.json"
with open(vault_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"Vault copy: {vault_path}")
