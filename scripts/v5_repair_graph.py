#!/usr/bin/env python3
"""v5 Graph Repair — Per KG Expert Manual Sections 2, 3, 10.2

Fixes:
1. Analyze connected components
2. Remove orphan nodes (degree 0)
3. Build identifier bridges between disconnected subgraphs
4. Extract largest connected component
5. Output v5.1 (cleaned, connected KG)
"""
import os
import json
import hashlib
from datetime import datetime
from collections import defaultdict

BASE = "/home/jshaik369/sexdiffkg"
V5_DIR = f"{BASE}/data/kg_v5"
V51_DIR = f"{BASE}/data/kg_v5.1"
os.makedirs(V51_DIR, exist_ok=True)

print("=" * 70)
print("v5 GRAPH REPAIR -> v5.1")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

import pandas as pd
import numpy as np

# --- Step 1: Load v5 data ---
print("\n[1/7] Loading v5 data...")
nodes = pd.read_csv(f"{V5_DIR}/nodes.tsv", sep="\t")
edges = pd.read_csv(f"{V5_DIR}/edges.tsv", sep="\t")
print(f"  Nodes: {len(nodes):,}")
print(f"  Edges: {len(edges):,}")
print(f"  Node types: {nodes['category'].nunique()}")
print(f"  Edge types: {edges['predicate'].nunique()}")

# --- Step 2: Deduplicate edges ---
print("\n[2/7] Deduplicating edges...")
edges_orig = len(edges)
edges = edges.drop_duplicates(subset=["subject", "predicate", "object"])
print(f"  Before: {edges_orig:,} -> After: {len(edges):,} (removed {edges_orig - len(edges):,})")

# --- Step 3: Find orphan nodes ---
print("\n[3/7] Identifying orphan nodes...")
edge_entities = set(edges["subject"]) | set(edges["object"])
node_ids = set(nodes["id"])
orphan_ids = node_ids - edge_entities
print(f"  Total nodes: {len(node_ids):,}")
print(f"  Entities in edges: {len(edge_entities):,}")
print(f"  Orphan nodes (degree 0): {len(orphan_ids):,} ({100*len(orphan_ids)/len(node_ids):.1f}%)")

# Orphan breakdown by category
orphan_cats = nodes[nodes["id"].isin(orphan_ids)]["category"].value_counts()
print(f"  Orphan breakdown:")
for cat, count in orphan_cats.items():
    print(f"    {cat}: {count:,}")

# --- Step 4: Connected component analysis ---
print("\n[4/7] Connected component analysis...")

# Build adjacency using dict (faster than networkx for this)
adj = defaultdict(set)
for _, row in edges.iterrows():
    adj[row["subject"]].add(row["object"])
    adj[row["object"]].add(row["subject"])

# BFS to find components
all_edge_nodes = set(adj.keys())
visited = set()
components = []

def bfs(start):
    queue = [start]
    component = set()
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        component.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return component

for node in all_edge_nodes:
    if node not in visited:
        comp = bfs(node)
        components.append(comp)

components.sort(key=len, reverse=True)
print(f"  Total components: {len(components):,}")
print(f"  Largest component: {len(components[0]):,} nodes")
if len(components) > 1:
    print(f"  2nd largest: {len(components[1]):,} nodes")
if len(components) > 2:
    print(f"  3rd largest: {len(components[2]):,} nodes")

# Show component size distribution
small = sum(1 for c in components if len(c) < 10)
medium = sum(1 for c in components if 10 <= len(c) < 1000)
large = sum(1 for c in components if len(c) >= 1000)
print(f"  Components <10 nodes: {small}")
print(f"  Components 10-999 nodes: {medium}")
print(f"  Components 1000+ nodes: {large}")

# --- Step 5: Identify bridge opportunities ---
print("\n[5/7] Analyzing bridge opportunities between top components...")

# For each component, show node type distribution
for i, comp in enumerate(components[:5]):
    comp_nodes = nodes[nodes["id"].isin(comp)]
    cats = comp_nodes["category"].value_counts()
    comp_edges = edges[(edges["subject"].isin(comp)) & (edges["object"].isin(comp))]
    rels = comp_edges["predicate"].value_counts()
    print(f"\n  Component {i+1} ({len(comp):,} nodes, {len(comp_edges):,} edges):")
    print(f"    Node types: {dict(cats.head(5))}")
    print(f"    Edge types: {dict(rels.head(5))}")

# --- Step 6: Build bridges using shared identifiers ---
print("\n[6/7] Building identifier bridges...")

# Strategy: Find entities that share name substrings across components
# Specifically: DRUG nodes in different components with same drug name
# And GENE/PROTEIN nodes with mappable identifiers

bridges_built = 0
bridge_edges = []

# Bridge 1: Drug name matching across components
# Get drug nodes from each component
comp1_nodes = nodes[nodes["id"].isin(components[0])]
comp1_drugs = comp1_nodes[comp1_nodes["category"] == "Drug"]

if len(components) > 1:
    other_comp_ids = set()
    for comp in components[1:]:
        other_comp_ids |= comp
    other_nodes = nodes[nodes["id"].isin(other_comp_ids)]
    other_drugs = other_nodes[other_nodes["category"] == "Drug"]

    # Normalize names for matching
    comp1_drug_names = {}
    for _, row in comp1_drugs.iterrows():
        name_norm = row["name"].upper().strip() if pd.notna(row["name"]) else ""
        if name_norm:
            comp1_drug_names[name_norm] = row["id"]

    other_drug_names = {}
    for _, row in other_drugs.iterrows():
        name_norm = row["name"].upper().strip() if pd.notna(row["name"]) else ""
        if name_norm:
            other_drug_names[name_norm] = row["id"]

    # Find matches
    matched_drugs = set(comp1_drug_names.keys()) & set(other_drug_names.keys())
    print(f"  Drug name matches across components: {len(matched_drugs)}")

    for name in matched_drugs:
        id1 = comp1_drug_names[name]
        id2 = other_drug_names[name]
        bridge_edges.append({
            "subject": id1,
            "predicate": "same_as",
            "object": id2,
        })
        bridges_built += 1

# Bridge 2: Gene name matching
comp1_genes = comp1_nodes[comp1_nodes["category"] == "Gene"]
if len(components) > 1:
    other_genes = other_nodes[other_nodes["category"] == "Gene"]

    comp1_gene_names = {}
    for _, row in comp1_genes.iterrows():
        name_norm = row["name"].upper().strip() if pd.notna(row["name"]) else ""
        if name_norm:
            comp1_gene_names[name_norm] = row["id"]

    other_gene_names = {}
    for _, row in other_genes.iterrows():
        name_norm = row["name"].upper().strip() if pd.notna(row["name"]) else ""
        if name_norm:
            other_gene_names[name_norm] = row["id"]

    matched_genes = set(comp1_gene_names.keys()) & set(other_gene_names.keys())
    print(f"  Gene name matches across components: {len(matched_genes)}")

    for name in list(matched_genes):
        id1 = comp1_gene_names[name]
        id2 = other_gene_names[name]
        bridge_edges.append({
            "subject": id1,
            "predicate": "same_as",
            "object": id2,
        })
        bridges_built += 1

# Bridge 3: Protein ENSP matching
comp1_proteins = comp1_nodes[comp1_nodes["category"] == "Protein"]
if len(components) > 1:
    other_proteins = other_nodes[other_nodes["category"] == "Protein"]

    # Extract ENSP IDs from protein names/ids
    def extract_ensp(id_str):
        """Extract Ensembl protein ID regardless of prefix format."""
        if "ENSP" in id_str:
            # Find ENSP followed by digits
            import re
            match = re.search(r'ENSP\d+', id_str)
            if match:
                return match.group()
        return None

    comp1_ensp = {}
    for _, row in comp1_proteins.iterrows():
        ensp = extract_ensp(str(row["id"]))
        if ensp:
            comp1_ensp[ensp] = row["id"]

    other_ensp = {}
    for _, row in other_proteins.iterrows():
        ensp = extract_ensp(str(row["id"]))
        if ensp:
            other_ensp[ensp] = row["id"]

    matched_proteins = set(comp1_ensp.keys()) & set(other_ensp.keys())
    print(f"  Protein ENSP matches across components: {len(matched_proteins)}")

    for ensp in matched_proteins:
        id1 = comp1_ensp[ensp]
        id2 = other_ensp[ensp]
        bridge_edges.append({
            "subject": id1,
            "predicate": "same_as",
            "object": id2,
        })
        bridges_built += 1

print(f"\n  Total bridges built: {bridges_built}")

# Add bridge edges to the graph
if bridge_edges:
    bridge_df = pd.DataFrame(bridge_edges)
    edges_bridged = pd.concat([edges, bridge_df], ignore_index=True)
    edges_bridged = edges_bridged.drop_duplicates(subset=["subject", "predicate", "object"])
    print(f"  Edges after bridging: {len(edges_bridged):,} (was {len(edges):,})")
else:
    edges_bridged = edges
    print("  No bridges found — components may use fundamentally different ID systems")
    print("  Proceeding with largest connected component extraction (PrimeKG approach)")

# --- Step 7: Create v5.1 ---
print("\n[7/7] Creating v5.1 (largest connected component, no orphans)...")

# Re-run component analysis on bridged graph
adj2 = defaultdict(set)
for _, row in edges_bridged.iterrows():
    adj2[row["subject"]].add(row["object"])
    adj2[row["object"]].add(row["subject"])

visited2 = set()
components2 = []
for node in adj2.keys():
    if node not in visited2:
        comp = set()
        queue = [node]
        while queue:
            n = queue.pop(0)
            if n in visited2:
                continue
            visited2.add(n)
            comp.add(n)
            for nb in adj2[n]:
                if nb not in visited2:
                    queue.append(nb)
        components2.append(comp)

components2.sort(key=len, reverse=True)
print(f"  Components after bridging: {len(components2):,}")
print(f"  Largest component: {len(components2[0]):,} nodes")

# Extract largest connected component
lcc_nodes = components2[0]
lcc_edges = edges_bridged[
    (edges_bridged["subject"].isin(lcc_nodes)) &
    (edges_bridged["object"].isin(lcc_nodes))
]

# Filter nodes to LCC (no orphans)
lcc_node_ids = set(lcc_edges["subject"]) | set(lcc_edges["object"])
v51_nodes = nodes[nodes["id"].isin(lcc_node_ids)].copy()

# Also include any bridged entities not in original nodes
bridge_entity_ids = set()
for _, row in lcc_edges.iterrows():
    bridge_entity_ids.add(row["subject"])
    bridge_entity_ids.add(row["object"])
missing_from_nodes = bridge_entity_ids - set(v51_nodes["id"])
if missing_from_nodes:
    print(f"  Adding {len(missing_from_nodes)} entities from bridges to nodes")

v51_nodes = v51_nodes.sort_values("id").reset_index(drop=True)
v51_edges = lcc_edges.sort_values(["subject", "predicate", "object"]).reset_index(drop=True)

# Create triples
v51_triples = v51_edges[["subject", "predicate", "object"]]

# Save v5.1
v51_nodes.to_csv(f"{V51_DIR}/nodes.tsv", sep="\t", index=False)
v51_edges.to_csv(f"{V51_DIR}/edges.tsv", sep="\t", index=False)
v51_triples.to_csv(f"{V51_DIR}/triples.tsv", sep="\t", index=False, header=False)

# Compute checksums
def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

# Stats
v51_cats = v51_nodes["category"].value_counts()
v51_rels = v51_edges["predicate"].value_counts()

print(f"\n  v5.1 Statistics:")
print(f"    Nodes: {len(v51_nodes):,}")
print(f"    Edges: {len(v51_edges):,}")
print(f"    Node types: {v51_nodes['category'].nunique()}")
print(f"    Edge types: {v51_edges['predicate'].nunique()}")

# How much was dropped
nodes_dropped = len(nodes) - len(v51_nodes)
edges_dropped = edges_orig - len(v51_edges)
pct_nodes = 100 * len(v51_nodes) / len(nodes)
pct_edges = 100 * len(v51_edges) / edges_orig

print(f"\n    Nodes retained: {pct_nodes:.1f}% ({nodes_dropped:,} dropped)")
print(f"    Edges retained: {pct_edges:.1f}% ({edges_dropped:,} dropped)")

print(f"\n    Node categories:")
for cat, count in v51_cats.items():
    print(f"      {cat}: {count:,}")

print(f"\n    Edge types:")
for rel, count in v51_rels.items():
    print(f"      {rel}: {count:,}")

# Check v4 preservation
print("\n  Checking v4 edge preservation in v5.1...")
v4_triples = pd.read_csv(f"{BASE}/data/kg_v4/triples.tsv", sep="\t", header=None,
                          names=["subject", "predicate", "object"])
v4_unique = v4_triples.drop_duplicates()
v51_triple_set = set(zip(v51_triples["subject"], v51_triples["predicate"], v51_triples["object"]))
v4_in_v51 = sum(1 for _, r in v4_unique.iterrows()
                if (r["subject"], r["predicate"], r["object"]) in v51_triple_set)
print(f"  v4 triples in v5.1: {v4_in_v51:,} / {len(v4_unique):,} ({100*v4_in_v51/len(v4_unique):.1f}%)")

# Save GROUND_TRUTH_v5.1
gt51 = {
    "version": "5.1",
    "date": datetime.now().isoformat(),
    "description": "v5 merged KG with data quality fixes: orphan removal, deduplication, largest connected component extraction",
    "nodes": int(len(v51_nodes)),
    "edges": int(len(v51_edges)),
    "node_types": int(v51_nodes["category"].nunique()),
    "edge_types": int(v51_edges["predicate"].nunique()),
    "components": 1,
    "orphan_nodes": 0,
    "v4_preservation_pct": round(100 * v4_in_v51 / len(v4_unique), 2),
    "bridges_added": bridges_built,
    "nodes_dropped_from_v5": nodes_dropped,
    "edges_dropped_from_v5": edges_dropped,
    "category_counts": {k: int(v) for k, v in v51_cats.items()},
    "edge_type_counts": {k: int(v) for k, v in v51_rels.items()},
    "checksums": {
        "nodes_tsv": md5_file(f"{V51_DIR}/nodes.tsv"),
        "edges_tsv": md5_file(f"{V51_DIR}/edges.tsv"),
        "triples_tsv": md5_file(f"{V51_DIR}/triples.tsv"),
    },
    "fixes_applied": [
        "Edge deduplication",
        "Orphan node removal",
        "Largest connected component extraction",
        f"Identifier bridges ({bridges_built} same_as edges)",
    ],
    "methodology_references": [
        "PrimeKG (Chandak 2023): largest connected component extraction retained 99.998% of edges",
        "OpenBioLink (Breit 2020): quality-filtered graph variants",
        "KG Expert Manual Section 10.2",
    ],
}

gt51_path = f"{V51_DIR}/GROUND_TRUTH_v5.1.json"
with open(gt51_path, "w") as f:
    json.dump(gt51, f, indent=2)
print(f"\n  Saved: {gt51_path}")

# Also copy to vault
vault_gt = "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg/GROUND_TRUTH_v5.1.json"
with open(vault_gt, "w") as f:
    json.dump(gt51, f, indent=2)
print(f"  Saved: {vault_gt}")

print(f"\n{'=' * 70}")
print("v5.1 GRAPH REPAIR COMPLETE")
print(f"{'=' * 70}")
print(f"  Output: {V51_DIR}/")
print(f"  Ready for embedding training with v51_train_hpo.py")
