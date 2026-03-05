#!/usr/bin/env python3
"""v5.2 Proper Identifier Bridge + Rebuild — Per KG Expert Manual Section 2

Problem: v5 has 3 disconnected subgraphs because identifiers don't cross-reference:
  Component 1 (pharmacovigilance): DRUG → AE, DRUG → GENE:target_name
  Component 2 (pathways): GENE:ENSG* → PATHWAY:R-HSA*
  Component 3 (PPI): PROTEIN:ENSP* → PROTEIN:ENSP*

Solution: Build bridge edges using mapping files:
  1. drug_targets.parquet: target_name → ensembl_gene_id → string_id (12,682 rows)
  2. id_mappings.parquet: uniprot → gene_symbol → ensembl_gene_id → string_id (166,382 rows)
  3. STRING protein.aliases: ENSP → gene_symbol (comprehensive)

New bridge edge types:
  - same_gene: GENE:target_name → GENE:ENSG* (connects Component 1↔2)
  - encodes: GENE:ENSG* → PROTEIN:ENSP* (connects Component 2↔3)
"""
import os
import sys
import json
import gzip
import time
import hashlib
import numpy as np
import pandas as pd
from datetime import datetime
from collections import Counter

BASE = "/home/jshaik369/sexdiffkg"
V5_DIR = f"{BASE}/data/kg_v5"
V52_DIR = f"{BASE}/data/kg_v5.2"
VAULT = "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg"
os.makedirs(V52_DIR, exist_ok=True)

print("=" * 70)
print("v5.2 IDENTIFIER BRIDGE + REBUILD")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

# === STEP 1: Load v5 data ===
print("\n[1/8] Loading v5 data...")
nodes = pd.read_csv(f"{V5_DIR}/nodes.tsv", sep="\t")
edges = pd.read_csv(f"{V5_DIR}/edges.tsv", sep="\t")
print(f"  v5 nodes: {len(nodes):,} ({nodes['category'].nunique()} types)")
print(f"  v5 edges: {len(edges):,} ({edges['predicate'].nunique()} relations)")

# === STEP 2: Build GENE:target_name → ENSG bridge from drug_targets.parquet ===
print("\n[2/8] Building GENE target_name → ENSG bridge...")
dt = pd.read_parquet(f"{BASE}/data/processed/molecular/drug_targets.parquet")
print(f"  drug_targets.parquet: {len(dt):,} rows")
print(f"  Columns: {list(dt.columns)}")

# Get unique target_name → ensembl_gene_id mappings
gene_bridge_dt = dt[["target_name", "ensembl_gene_id"]].dropna().drop_duplicates()
# Normalize: GENE:target_name → GENE:ENSG*
gene_bridge_dt["source_id"] = "GENE:" + gene_bridge_dt["target_name"]
gene_bridge_dt["target_id"] = "GENE:" + gene_bridge_dt["ensembl_gene_id"]

# Filter to only those that exist in v5 nodes
v5_node_ids = set(nodes["id"])
gene_bridge_dt = gene_bridge_dt[
    gene_bridge_dt["source_id"].isin(v5_node_ids) &
    gene_bridge_dt["target_id"].isin(v5_node_ids)
]
print(f"  Target name → ENSG bridges (both exist in v5): {len(gene_bridge_dt):,}")

# === STEP 3: Build ENSG → ENSP bridge from drug_targets + id_mappings ===
print("\n[3/8] Building GENE:ENSG → PROTEIN:ENSP bridge...")

# From drug_targets: ensembl_gene_id → string_id
ensg_ensp_dt = dt[["ensembl_gene_id", "string_id"]].dropna().drop_duplicates()
# string_id has format 9606.ENSP* — strip the 9606. prefix for our PROTEIN: nodes
ensg_ensp_dt["source_id"] = "GENE:" + ensg_ensp_dt["ensembl_gene_id"]
ensg_ensp_dt["target_id"] = "PROTEIN:" + ensg_ensp_dt["string_id"].str.replace("9606.", "", regex=False)
ensg_ensp_dt = ensg_ensp_dt[
    ensg_ensp_dt["source_id"].isin(v5_node_ids) &
    ensg_ensp_dt["target_id"].isin(v5_node_ids)
]
print(f"  ENSG → ENSP bridges from drug_targets (both exist): {len(ensg_ensp_dt):,}")

# From id_mappings: more ENSG → ENSP mappings
idmap = pd.read_parquet(f"{BASE}/data/processed/molecular/id_mappings.parquet")
print(f"  id_mappings.parquet: {len(idmap):,} rows")
ensg_ensp_idmap = idmap[["ensembl_gene_id", "string_id"]].dropna().drop_duplicates()
ensg_ensp_idmap["source_id"] = "GENE:" + ensg_ensp_idmap["ensembl_gene_id"]
ensg_ensp_idmap["target_id"] = "PROTEIN:" + ensg_ensp_idmap["string_id"].str.replace("9606.", "", regex=False)
ensg_ensp_idmap = ensg_ensp_idmap[
    ensg_ensp_idmap["source_id"].isin(v5_node_ids) &
    ensg_ensp_idmap["target_id"].isin(v5_node_ids)
]
print(f"  ENSG → ENSP bridges from id_mappings (both exist): {len(ensg_ensp_idmap):,}")

# Combine and deduplicate
ensg_ensp_all = pd.concat([
    ensg_ensp_dt[["source_id", "target_id"]],
    ensg_ensp_idmap[["source_id", "target_id"]]
]).drop_duplicates()
print(f"  Combined ENSG → ENSP bridges (deduplicated): {len(ensg_ensp_all):,}")

# === STEP 4: Build gene_symbol bridge using STRING aliases ===
print("\n[4/8] Loading STRING protein aliases for broader bridging...")

# Parse STRING aliases file
aliases_path = f"{BASE}/data/raw/string/9606.protein.aliases.v12.0.txt.gz"
alias_records = []
with gzip.open(aliases_path, "rt") as f:
    header = next(f)  # skip header
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) >= 3:
            string_id = parts[0]  # 9606.ENSP*
            alias = parts[1]
            source = parts[2]
            # We want Ensembl_gene mappings (ENSG*) and gene symbol mappings
            if "Ensembl_gene" in source or "BioMart_HUGO" in source or "Ensembl_HGNC" in source:
                alias_records.append((string_id, alias, source))

aliases_df = pd.DataFrame(alias_records, columns=["string_id", "alias", "source"])
print(f"  STRING aliases (gene-relevant): {len(aliases_df):,}")

# Extract ENSG aliases
ensg_aliases = aliases_df[aliases_df["alias"].str.startswith("ENSG")]
ensg_aliases = ensg_aliases[["string_id", "alias"]].drop_duplicates()
ensg_aliases["source_id"] = "GENE:" + ensg_aliases["alias"]
ensg_aliases["target_id"] = "PROTEIN:" + ensg_aliases["string_id"].str.replace("9606.", "", regex=False)
ensg_aliases = ensg_aliases[
    ensg_aliases["source_id"].isin(v5_node_ids) &
    ensg_aliases["target_id"].isin(v5_node_ids)
]
print(f"  STRING ENSG → ENSP bridges (both exist in v5): {len(ensg_aliases):,}")

# Extract gene symbol aliases for target_name → ENSP bridging
# Gene symbols from STRING
symbol_aliases = aliases_df[
    (aliases_df["source"].str.contains("HUGO|HGNC|BioMart_HUGO")) &
    (~aliases_df["alias"].str.startswith("ENSG"))
].drop_duplicates(subset=["string_id", "alias"])
print(f"  STRING gene symbol aliases: {len(symbol_aliases):,}")

# Also: gene_symbol → target_name mapping from drug_targets
# Build gene_symbol → ENSG from drug_targets and id_mappings
symbol_to_ensg = pd.concat([
    dt[["gene_symbol", "ensembl_gene_id"]].dropna().drop_duplicates(),
    idmap[["gene_symbol", "ensembl_gene_id"]].dropna().drop_duplicates()
]).drop_duplicates()
print(f"  Gene symbol → ENSG mappings: {len(symbol_to_ensg):,}")

# Build target_name → gene_symbol from drug_targets
target_to_symbol = dt[["target_name", "gene_symbol"]].dropna().drop_duplicates()
print(f"  Target name → gene symbol mappings: {len(target_to_symbol):,}")

# Chain: target_name → gene_symbol → ENSG (broader bridge for Component 1↔2)
target_to_ensg = target_to_symbol.merge(symbol_to_ensg, on="gene_symbol", how="inner")
target_to_ensg["source_id"] = "GENE:" + target_to_ensg["target_name"]
target_to_ensg["target_id"] = "GENE:" + target_to_ensg["ensembl_gene_id"]
target_to_ensg = target_to_ensg[
    target_to_ensg["source_id"].isin(v5_node_ids) &
    target_to_ensg["target_id"].isin(v5_node_ids)
][["source_id", "target_id"]].drop_duplicates()
print(f"  Target name → ENSG via gene_symbol (both exist): {len(target_to_ensg):,}")

# === STEP 5: Combine all bridges ===
print("\n[5/8] Combining all bridge edges...")

# Bridge type 1: same_gene (target_name → ENSG)
bridge_same_gene = pd.concat([
    gene_bridge_dt[["source_id", "target_id"]],
    target_to_ensg[["source_id", "target_id"]]
]).drop_duplicates()
bridge_same_gene["predicate"] = "same_gene"
print(f"  same_gene edges (Component 1↔2): {len(bridge_same_gene):,}")

# Bridge type 2: encodes (ENSG → ENSP)
bridge_encodes = pd.concat([
    ensg_ensp_all[["source_id", "target_id"]],
    ensg_aliases[["source_id", "target_id"]]
]).drop_duplicates()
bridge_encodes["predicate"] = "encodes"
print(f"  encodes edges (Component 2↔3): {len(bridge_encodes):,}")

# Create bridge edges DataFrame
bridge_edges = pd.concat([
    bridge_same_gene.rename(columns={"source_id": "subject", "target_id": "object"}),
    bridge_encodes.rename(columns={"source_id": "subject", "target_id": "object"})
])
print(f"  Total bridge edges: {len(bridge_edges):,}")

# === STEP 6: Rebuild v5.2 ===
print("\n[6/8] Rebuilding v5.2 with bridge edges...")

# Combine v5 edges + bridge edges
v52_edges = pd.concat([edges, bridge_edges], ignore_index=True)
v52_edges = v52_edges.drop_duplicates(subset=["subject", "predicate", "object"])
print(f"  v5.2 edges: {len(v52_edges):,} (v5: {len(edges):,} + bridges: {len(bridge_edges):,}, minus dupes)")

# Verify all edge endpoints exist in nodes
edge_entities = set(v52_edges["subject"]) | set(v52_edges["object"])
node_ids = set(nodes["id"])
missing = edge_entities - node_ids
print(f"  Entities in edges but not nodes: {len(missing):,}")

# Use all v5 nodes (don't drop orphans yet — let component analysis decide)
v52_nodes = nodes.copy()

# === STEP 7: Component analysis ===
print("\n[7/8] Component analysis of v5.2...")

# Build adjacency for component analysis
from collections import deque

adj = {}
for _, row in v52_edges.iterrows():
    s, o = row["subject"], row["object"]
    if s not in adj:
        adj[s] = []
    if o not in adj:
        adj[o] = []
    adj[s].append(o)
    adj[o].append(s)

# BFS components
visited = set()
components = []
entity_to_comp = {}

all_entities = set(adj.keys())
print(f"  Entities in edge graph: {len(all_entities):,}")

for start in all_entities:
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
    comp_id = len(components) - 1
    for n in comp:
        entity_to_comp[n] = comp_id

components.sort(key=len, reverse=True)
print(f"  Components: {len(components):,}")

# Show top components
for i, comp in enumerate(components[:5]):
    comp_nodes_df = v52_nodes[v52_nodes["id"].isin(comp)]
    cat_dist = comp_nodes_df["category"].value_counts().to_dict()
    # Get edge types in component
    comp_edges = v52_edges[v52_edges["subject"].isin(comp) | v52_edges["object"].isin(comp)]
    rel_dist = comp_edges["predicate"].value_counts().to_dict()
    print(f"  Component {i+1}: {len(comp):,} nodes")
    print(f"    Categories: {dict(sorted(cat_dist.items(), key=lambda x: -x[1])[:6])}")
    print(f"    Relations: {dict(sorted(rel_dist.items(), key=lambda x: -x[1])[:5])}")

# Check if top 3 v5 components are now connected
if len(components) > 0:
    lcc = components[0]
    orphan_nodes = set(nodes["id"]) - all_entities
    print(f"\n  Largest connected component: {len(lcc):,} nodes")
    print(f"  Orphan nodes (no edges): {len(orphan_nodes):,}")

    # Check v4 edge preservation
    v4_triples_path = f"{BASE}/data/kg_v4/triples.tsv"
    if os.path.exists(v4_triples_path):
        v4_triples = pd.read_csv(v4_triples_path, sep="\t", header=None, names=["s", "p", "o"])
        v52_triple_set = set(zip(v52_edges["subject"], v52_edges["predicate"], v52_edges["object"]))
        v4_in_v52 = sum(1 for s, p, o in zip(v4_triples["s"], v4_triples["p"], v4_triples["o"])
                        if (s, p, o) in v52_triple_set)
        # Use deduplicated v4 count
        v4_deduped = v4_triples.drop_duplicates()
        v4_deduped_in_v52 = sum(1 for s, p, o in zip(v4_deduped["s"], v4_deduped["p"], v4_deduped["o"])
                                 if (s, p, o) in v52_triple_set)
        print(f"  v4 triples in v5.2: {v4_in_v52:,} / {len(v4_triples):,} ({v4_in_v52/len(v4_triples)*100:.1f}%)")
        print(f"  v4 deduped in v5.2: {v4_deduped_in_v52:,} / {len(v4_deduped):,} ({v4_deduped_in_v52/len(v4_deduped)*100:.1f}%)")

# === STEP 8: Extract LCC and save ===
print("\n[8/8] Extracting LCC and saving v5.2...")

# LCC nodes
lcc_nodes = v52_nodes[v52_nodes["id"].isin(lcc)].copy()
# LCC edges (both endpoints in LCC)
lcc_edges = v52_edges[
    v52_edges["subject"].isin(lcc) &
    v52_edges["object"].isin(lcc)
].copy()

print(f"  v5.2 LCC nodes: {len(lcc_nodes):,}")
print(f"  v5.2 LCC edges: {len(lcc_edges):,}")

# Node type breakdown
cat_counts = lcc_nodes["category"].value_counts()
print(f"\n  Node types ({cat_counts.shape[0]}):")
for cat, count in cat_counts.items():
    print(f"    {cat}: {count:,}")

# Edge type breakdown
rel_counts = lcc_edges["predicate"].value_counts()
print(f"\n  Edge types ({rel_counts.shape[0]}):")
for rel, count in rel_counts.items():
    print(f"    {rel}: {count:,}")

# Save
lcc_nodes.to_csv(f"{V52_DIR}/nodes.tsv", sep="\t", index=False)
lcc_edges.to_csv(f"{V52_DIR}/edges.tsv", sep="\t", index=False)
lcc_edges[["subject", "predicate", "object"]].to_csv(
    f"{V52_DIR}/triples.tsv", sep="\t", index=False, header=False
)
print(f"\n  Saved: {V52_DIR}/nodes.tsv")
print(f"  Saved: {V52_DIR}/edges.tsv")
print(f"  Saved: {V52_DIR}/triples.tsv")

# === Ground Truth ===
def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

gt = {
    "version": "v5.2",
    "timestamp": datetime.now().isoformat(),
    "description": "SexDiffKG v5 + VEDA-KG merged, identifier bridges added, LCC extracted",
    "nodes": int(len(lcc_nodes)),
    "edges": int(len(lcc_edges)),
    "node_types": int(cat_counts.shape[0]),
    "edge_types": int(rel_counts.shape[0]),
    "node_type_counts": {k: int(v) for k, v in cat_counts.items()},
    "edge_type_counts": {k: int(v) for k, v in rel_counts.items()},
    "bridges_added": {
        "same_gene": int(len(bridge_same_gene)),
        "encodes": int(len(bridge_encodes)),
        "total": int(len(bridge_edges)),
    },
    "components_before_lcc": int(len(components)),
    "lcc_fraction": round(len(lcc) / len(all_entities), 4),
    "orphan_nodes_removed": int(len(orphan_nodes)),
    "v4_preservation": {
        "v4_deduped_in_v52": int(v4_deduped_in_v52) if 'v4_deduped_in_v52' in dir() else None,
        "v4_deduped_total": int(len(v4_deduped)) if 'v4_deduped' in dir() else None,
    },
    "checksums": {
        "nodes_tsv": md5_file(f"{V52_DIR}/nodes.tsv"),
        "edges_tsv": md5_file(f"{V52_DIR}/edges.tsv"),
        "triples_tsv": md5_file(f"{V52_DIR}/triples.tsv"),
    },
    "data_sources": [
        "SexDiffKG v4 (FAERS, STRING, Reactome, ChEMBL, GTEx)",
        "VEDA-KG v1 (ClinicalTrials.gov, KEGG, DisGeNET, IMPPAT)",
        "drug_targets.parquet (12,682 bridge rows)",
        "id_mappings.parquet (166,382 bridge rows)",
        "STRING 9606.protein.aliases.v12.0 (ENSP→ENSG mapping)",
    ],
}

gt_path = f"{V52_DIR}/GROUND_TRUTH_v5.2.json"
with open(gt_path, "w") as f:
    json.dump(gt, f, indent=2)
print(f"\n  Ground truth: {gt_path}")

# RAID copy to vault
vault_gt = f"{VAULT}/GROUND_TRUTH_v5.2.json"
with open(vault_gt, "w") as f:
    json.dump(gt, f, indent=2)
print(f"  Vault copy: {vault_gt}")

# === Summary ===
print(f"\n{'=' * 70}")
print("v5.2 BUILD COMPLETE")
print(f"{'=' * 70}")
print(f"  Bridges: {len(bridge_same_gene):,} same_gene + {len(bridge_encodes):,} encodes = {len(bridge_edges):,} total")
print(f"  Components: {len(components):,} (LCC: {len(lcc):,} nodes, {len(lcc) / len(all_entities) * 100:.1f}%)")
print(f"  v5.2 LCC: {len(lcc_nodes):,} nodes, {len(lcc_edges):,} edges")
print(f"  Node types: {cat_counts.shape[0]}, Edge types: {rel_counts.shape[0]}")
if 'v4_deduped_in_v52' in dir():
    print(f"  v4 preservation: {v4_deduped_in_v52:,}/{len(v4_deduped):,} ({v4_deduped_in_v52/len(v4_deduped)*100:.1f}%)")
print(f"  Output: {V52_DIR}/")
print(f"{'=' * 70}")
