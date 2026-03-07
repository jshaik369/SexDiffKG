#!/usr/bin/env python3
"""v5.2 Wave 3: PPI Network Sex Bias Propagation

Uses v5.2 bridges to trace: drug → target gene → ENSG → ENSP → PPI neighbors
Propagates sex-bias scores through the STRING PPI network to find "sex-bias hubs".

Novel: Which proteins are central to sex-biased drug safety networks?
Only possible with v5.2 bridges (PPI subgraph was disconnected in v5).
"""
import os
import json
import numpy as np
import pandas as pd
from datetime import datetime
from collections import defaultdict

BASE = "/home/jshaik369/sexdiffkg"
V52_DIR = f"{BASE}/data/kg_v5.2"
OUT_DIR = "/tmp/sexdiffkg-deep-analysis/results"
FIG_DIR = "/tmp/sexdiffkg-deep-analysis/figures"

print("=" * 70)
print("WAVE 3: PPI NETWORK SEX BIAS PROPAGATION")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

# Load edges
print("\n[1/5] Loading v5.2 edges...")
edges = pd.read_csv(f"{V52_DIR}/edges.tsv", sep="\t")

sex_diff = edges[edges["predicate"] == "sex_differential_adverse_event"]
targets = edges[edges["predicate"] == "targets"]  # DRUG → GENE:target_name
same_gene = edges[edges["predicate"] == "same_gene"]  # GENE:target_name → GENE:ENSG
encodes = edges[edges["predicate"] == "encodes"]  # GENE:ENSG → PROTEIN:ENSP
ppi = edges[edges["predicate"] == "interacts_with"]  # PROTEIN ↔ PROTEIN

print(f"  sex_differential_ae: {len(sex_diff):,}")
print(f"  targets: {len(targets):,}")
print(f"  same_gene: {len(same_gene):,}")
print(f"  encodes: {len(encodes):,}")
print(f"  interacts_with (PPI): {len(ppi):,}")

# === Step 2: Compute drug sex-bias scores ===
print("\n[2/5] Computing drug sex-bias scores...")

# Count signals per drug
drug_n_signals = sex_diff.groupby("subject").size().to_dict()

# Get drug → target genes → ENSG → ENSP chain
drug_to_targets = defaultdict(set)
for _, row in targets.iterrows():
    drug_to_targets[row["subject"]].add(row["object"])

target_to_ensg = defaultdict(set)
for _, row in same_gene.iterrows():
    target_to_ensg[row["subject"]].add(row["object"])

ensg_to_ensp = defaultdict(set)
for _, row in encodes.iterrows():
    ensg_to_ensp[row["subject"]].add(row["object"])

# Build: protein → sex-bias score (sum of signals from drugs targeting that protein)
protein_bias_score = defaultdict(float)
protein_drug_count = defaultdict(int)
protein_drug_list = defaultdict(set)

for drug, target_genes in drug_to_targets.items():
    n_signals = drug_n_signals.get(drug, 0)
    if n_signals == 0:
        continue

    for tg in target_genes:
        for ensg in target_to_ensg.get(tg, set()):
            for ensp in ensg_to_ensp.get(ensg, set()):
                protein_bias_score[ensp] += n_signals
                protein_drug_count[ensp] += 1
                protein_drug_list[ensp].add(drug)

print(f"  Proteins with direct drug sex-bias: {len(protein_bias_score):,}")

# === Step 3: Build PPI adjacency and propagate ===
print("\n[3/5] Building PPI network and propagating sex-bias scores...")

# Build adjacency
ppi_adj = defaultdict(set)
for _, row in ppi.iterrows():
    ppi_adj[row["subject"]].add(row["object"])
    ppi_adj[row["object"]].add(row["subject"])

print(f"  PPI network: {len(ppi_adj):,} proteins, {len(ppi):,} interactions")

# Propagate: for each protein, add fraction of neighbor scores (1-hop)
propagated_score = {}
for protein in ppi_adj:
    # Direct score
    direct = protein_bias_score.get(protein, 0)
    # Neighbor contribution (average of neighbor direct scores)
    neighbors = ppi_adj[protein]
    if neighbors:
        neighbor_scores = [protein_bias_score.get(n, 0) for n in neighbors]
        neighbor_avg = np.mean(neighbor_scores) if neighbor_scores else 0
    else:
        neighbor_avg = 0
    # Combined: direct + 0.5 * neighbor average
    propagated_score[protein] = direct + 0.5 * neighbor_avg

# Find hubs: proteins with high propagated score AND high degree
hub_df = pd.DataFrame([
    {
        "protein": p,
        "propagated_score": propagated_score.get(p, 0),
        "direct_score": protein_bias_score.get(p, 0),
        "degree": len(ppi_adj.get(p, set())),
        "n_drugs": protein_drug_count.get(p, 0),
        "drugs": list(protein_drug_list.get(p, set()))[:10],
    }
    for p in set(list(propagated_score.keys()) + list(protein_bias_score.keys()))
]).sort_values("propagated_score", ascending=False)

# Filter to meaningful hubs
hubs = hub_df[(hub_df["propagated_score"] > 0) & (hub_df["degree"] >= 5)]
print(f"  Sex-bias hub proteins (score>0, degree>=5): {len(hubs):,}")

# === Step 4: Load protein names ===
print("\n[4/5] Loading protein annotations...")

# Try to get protein names from STRING aliases
aliases_path = f"{BASE}/data/raw/string/9606.protein.aliases.v12.0.txt.gz"
protein_names = {}
try:
    import gzip
    with gzip.open(aliases_path, "rt") as f:
        next(f)  # skip header
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 3:
                ensp = "PROTEIN:" + parts[0].replace("9606.", "")
                if "BioMart_HUGO" in parts[2] or "Ensembl_HGNC" in parts[2]:
                    if ensp not in protein_names:
                        protein_names[ensp] = parts[1]
    print(f"  Loaded {len(protein_names):,} protein gene symbol annotations")
except:
    print("  Could not load protein aliases")

hubs["gene_symbol"] = hubs["protein"].map(protein_names)

print(f"\n  Top 20 sex-bias hub proteins:")
for _, row in hubs.head(20).iterrows():
    symbol = row.get("gene_symbol", "") or ""
    print(f"    {row['protein']} ({symbol}): score={row['propagated_score']:.0f}, "
          f"degree={row['degree']}, drugs={row['n_drugs']}")

# === Step 5: Save results ===
print("\n[5/5] Saving results...")

results = {
    "analysis": "ppi_sex_bias_propagation",
    "wave": 3,
    "kg_version": "v5.2",
    "timestamp": datetime.now().isoformat(),
    "novelty": "Sex-bias score propagation through STRING PPI network via v5.2 bridges",
    "summary": {
        "proteins_with_direct_bias": len(protein_bias_score),
        "ppi_proteins": len(ppi_adj),
        "ppi_interactions": len(ppi),
        "sex_bias_hubs": len(hubs),
    },
    "top_hubs": [],
}

for _, row in hubs.head(50).iterrows():
    results["top_hubs"].append({
        "protein": row["protein"],
        "gene_symbol": row.get("gene_symbol") or None,
        "propagated_score": round(float(row["propagated_score"]), 1),
        "direct_score": round(float(row["direct_score"]), 1),
        "degree": int(row["degree"]),
        "n_drugs": int(row["n_drugs"]),
    })

out_path = f"{OUT_DIR}/v52_wave3_ppi_sex_bias.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"  Results: {out_path}")

# Save full hub table
table_path = f"{OUT_DIR}/v52_ppi_sex_bias_hubs.tsv"
hubs.drop(columns=["drugs"]).head(200).to_csv(table_path, sep="\t", index=False)
print(f"  Table: {table_path}")

# Generate figure
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    top30 = hubs.head(30).copy()
    top30["label"] = top30["gene_symbol"].fillna(top30["protein"].str.replace("PROTEIN:", "").str[:15])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))

    # Left: top 30 hub proteins by propagated score
    colors = ["#E53935" if s > 0 else "#2196F3" for s in top30["direct_score"]]
    ax1.barh(range(len(top30)), top30["propagated_score"], color=colors, alpha=0.8)
    ax1.set_yticks(range(len(top30)))
    ax1.set_yticklabels(top30["label"], fontsize=8)
    ax1.set_xlabel("Sex-Bias Propagated Score")
    ax1.set_title("Top 30 Sex-Bias Hub Proteins\n(Direct + PPI Neighbor Propagation)")
    ax1.invert_yaxis()

    # Right: score vs degree scatter
    sample = hubs.head(500)
    ax2.scatter(sample["degree"], sample["propagated_score"],
                alpha=0.5, c=np.log1p(sample["direct_score"]), cmap="Reds", s=20)
    ax2.set_xlabel("PPI Degree (number of interactions)")
    ax2.set_ylabel("Propagated Sex-Bias Score")
    ax2.set_title("PPI Hub Degree vs Sex-Bias Score")
    # Label top 5
    for _, row in hubs.head(5).iterrows():
        label = row.get("gene_symbol") or row["protein"].replace("PROTEIN:", "")[:10]
        ax2.annotate(label, (row["degree"], row["propagated_score"]),
                     fontsize=7, ha="center")

    plt.suptitle("SexDiffKG v5.2 — PPI Sex-Bias Propagation", fontsize=14, fontweight="bold")
    plt.tight_layout()
    fig_path = f"{FIG_DIR}/v52_wave3_ppi_sex_bias.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"  Figure: {fig_path}")
except Exception as e:
    print(f"  Figure failed: {e}")

print(f"\n{'=' * 70}")
print("WAVE 3 COMPLETE")
print(f"{'=' * 70}")
