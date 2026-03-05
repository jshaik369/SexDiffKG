#!/usr/bin/env python3
"""v4 Data Quality Patch — Per KG Expert Manual Section 10.1

Fixes:
1. Add 3,288 missing DRUG entities to nodes.tsv (drugs in edges but not in nodes)
2. Create edges_deduped.tsv (1,532,674 unique triples)
3. Create triples_deduped.tsv
4. Update GROUND_TRUTH.json with patched counts
5. Verify MD5 of original files unchanged (preserve v4 canonical)

Does NOT modify original edges.tsv or triples.tsv — those are preserved for reproducibility.
"""
import os
import sys
import json
import hashlib
from datetime import datetime

BASE = "/home/jshaik369/sexdiffkg"
KG_DIR = f"{BASE}/data/kg_v4"
GT_PATHS = [
    f"{BASE}/GROUND_TRUTH.json",
    f"{BASE}/data/kg_v4/GROUND_TRUTH.json",
    f"{BASE}/results/GROUND_TRUTH.json",
    "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg/GROUND_TRUTH.json",
]

print("=" * 70)
print("v4 DATA QUALITY PATCH")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

# --- Step 1: Read current data ---
print("\n[1/6] Reading current data...")
import pandas as pd

nodes = pd.read_csv(f"{KG_DIR}/nodes.tsv", sep="\t")
edges = pd.read_csv(f"{KG_DIR}/edges.tsv", sep="\t")

print(f"  nodes.tsv: {len(nodes):,} rows, columns: {list(nodes.columns)}")
print(f"  edges.tsv: {len(edges):,} rows, columns: {list(edges.columns)}")

# --- Step 2: Find missing drug nodes ---
print("\n[2/6] Finding entities in edges but missing from nodes...")
node_ids = set(nodes["id"])
edge_subjects = set(edges["subject"])
edge_objects = set(edges["object"])
edge_entities = edge_subjects | edge_objects
missing = edge_entities - node_ids
print(f"  Node IDs in nodes.tsv: {len(node_ids):,}")
print(f"  Unique entities in edges: {len(edge_entities):,}")
print(f"  Missing from nodes.tsv: {len(missing):,}")

# Categorize missing entities
categories = {}
for m in missing:
    prefix = m.split(":")[0] if ":" in m else "UNKNOWN"
    categories[prefix] = categories.get(prefix, 0) + 1
print(f"  Missing by category: {categories}")

# --- Step 3: Add missing nodes ---
print("\n[3/6] Adding missing nodes to nodes.tsv...")
new_rows = []
for entity_id in sorted(missing):
    prefix = entity_id.split(":")[0] if ":" in entity_id else "Unknown"
    # Extract name from ID (after first colon)
    name = entity_id.split(":", 1)[1] if ":" in entity_id else entity_id
    # Map prefix to category
    cat_map = {"DRUG": "Drug", "GENE": "Gene", "PROTEIN": "Protein",
               "AE": "AdverseEvent", "PATHWAY": "Pathway", "TISSUE": "Tissue"}
    category = cat_map.get(prefix, prefix)
    new_rows.append({"id": entity_id, "name": name, "category": category})

new_nodes_df = pd.DataFrame(new_rows)
patched_nodes = pd.concat([nodes, new_nodes_df], ignore_index=True)
patched_nodes = patched_nodes.drop_duplicates(subset=["id"])
patched_nodes = patched_nodes.sort_values("id").reset_index(drop=True)

print(f"  Added {len(new_rows):,} new nodes")
print(f"  Patched nodes.tsv: {len(patched_nodes):,} rows")

# Verify all edge entities now exist
patched_ids = set(patched_nodes["id"])
still_missing = edge_entities - patched_ids
assert len(still_missing) == 0, f"Still missing {len(still_missing)} entities!"
print(f"  Verification: 0 missing entities (PASS)")

# Save patched nodes
patched_nodes_path = f"{KG_DIR}/nodes_patched.tsv"
patched_nodes.to_csv(patched_nodes_path, sep="\t", index=False)
print(f"  Saved: {patched_nodes_path}")

# Category breakdown
cat_counts = patched_nodes["category"].value_counts()
print(f"\n  Patched node categories:")
for cat, count in cat_counts.items():
    print(f"    {cat}: {count:,}")

# --- Step 4: Deduplicate edges ---
print("\n[4/6] Deduplicating edges...")
edges_deduped = edges.drop_duplicates(subset=["subject", "predicate", "object"])
n_dupes = len(edges) - len(edges_deduped)
print(f"  Original edges: {len(edges):,}")
print(f"  Duplicates removed: {n_dupes:,}")
print(f"  Unique triples: {len(edges_deduped):,}")

# Save deduped edges
deduped_edges_path = f"{KG_DIR}/edges_deduped.tsv"
edges_deduped.to_csv(deduped_edges_path, sep="\t", index=False)
print(f"  Saved: {deduped_edges_path}")

# Create deduped triples (subject\tpredicate\tobject only)
deduped_triples_path = f"{KG_DIR}/triples_deduped.tsv"
edges_deduped[["subject", "predicate", "object"]].to_csv(
    deduped_triples_path, sep="\t", index=False, header=False
)
print(f"  Saved: {deduped_triples_path}")

# --- Step 5: Compute MD5 checksums ---
print("\n[5/6] Computing checksums...")

def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

checksums = {
    "nodes_original": md5_file(f"{KG_DIR}/nodes.tsv"),
    "edges_original": md5_file(f"{KG_DIR}/edges.tsv"),
    "triples_original": md5_file(f"{KG_DIR}/triples.tsv"),
    "nodes_patched": md5_file(patched_nodes_path),
    "edges_deduped": md5_file(deduped_edges_path),
    "triples_deduped": md5_file(deduped_triples_path),
}
for name, md5 in checksums.items():
    print(f"  {name}: {md5}")

# Verify originals unchanged
assert checksums["nodes_original"] == "5a7331b1b0e7f11853444eb59e2b9166", "nodes.tsv MD5 CHANGED!"
assert checksums["edges_original"] == "b8e4890c2063bdf9357c76730881b440", "edges.tsv MD5 CHANGED!"
assert checksums["triples_original"] == "2d4e46b1265a9a9bd44bbfc7372a9e44", "triples.tsv MD5 CHANGED!"
print("  Original file integrity: VERIFIED (all 3 MD5 match)")

# --- Step 6: Update GROUND_TRUTH.json ---
print("\n[6/6] Updating GROUND_TRUTH.json...")

for gt_path in GT_PATHS:
    if not os.path.exists(gt_path):
        print(f"  SKIP (not found): {gt_path}")
        continue
    with open(gt_path) as f:
        gt = json.load(f)

    # Add patched data section
    gt["v4_patched"] = {
        "date": datetime.now().isoformat(),
        "nodes_patched": int(len(patched_nodes)),
        "nodes_added": len(new_rows),
        "edges_deduped": int(len(edges_deduped)),
        "duplicates_removed": n_dupes,
        "true_entity_count": int(len(edge_entities)),
        "checksums": {
            "nodes_patched_tsv": checksums["nodes_patched"],
            "edges_deduped_tsv": checksums["edges_deduped"],
            "triples_deduped_tsv": checksums["triples_deduped"],
        },
        "category_counts_patched": {k: int(v) for k, v in cat_counts.items()},
    }

    with open(gt_path, "w") as f:
        json.dump(gt, f, indent=2)
    print(f"  Updated: {gt_path}")

# --- Summary ---
print(f"\n{'=' * 70}")
print("v4 PATCH COMPLETE")
print(f"{'=' * 70}")
print(f"  Original nodes: {len(nodes):,} -> Patched: {len(patched_nodes):,} (+{len(new_rows):,})")
print(f"  Original edges: {len(edges):,} -> Deduped: {len(edges_deduped):,} (-{n_dupes:,})")
print(f"  Original files PRESERVED (MD5 verified)")
print(f"  New files: nodes_patched.tsv, edges_deduped.tsv, triples_deduped.tsv")
print(f"  GROUND_TRUTH.json updated in {len([p for p in GT_PATHS if os.path.exists(p)])} locations")
