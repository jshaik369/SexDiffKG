#!/usr/bin/env python3
"""v5.2 Wave 1: Pathway-Connected Sex-Differential Drug Safety Analysis

This analysis is ONLY possible with v5.2 because v5 had disconnected pathway subgraph.
Now that same_gene + encodes bridges connect drugs → genes → proteins → pathways,
we can ask: which Reactome pathways are enriched for sex-differential drug safety?

Pipeline:
1. Load v5.2 edges
2. Trace: drug → targets → gene (target_name) → same_gene → gene (ENSG) → participates_in → pathway
3. For each pathway: count drugs with sex-differential signals, compute sex bias ratio
4. Identify pathways with strongest female/male drug safety bias
"""
import os
import json
import pandas as pd
from datetime import datetime
from collections import Counter, defaultdict

BASE = "/home/jshaik369/sexdiffkg"
V52_DIR = f"{BASE}/data/kg_v5.2"
OUT_DIR = "/tmp/sexdiffkg-deep-analysis/results"
FIG_DIR = "/tmp/sexdiffkg-deep-analysis/figures"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

print("=" * 70)
print("WAVE 1: PATHWAY-CONNECTED SEX-DIFFERENTIAL DRUG SAFETY")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

# Load v5.2 edges
print("\n[1/5] Loading v5.2 edges...")
edges = pd.read_csv(f"{V52_DIR}/edges.tsv", sep="\t")
print(f"  {len(edges):,} edges loaded")

# === Step 2: Build pathway traces ===
print("\n[2/5] Building drug → pathway traces via bridges...")

# Extract edge subsets
targets_edges = edges[edges["predicate"] == "targets"]  # DRUG → GENE:target_name
same_gene_edges = edges[edges["predicate"] == "same_gene"]  # GENE:target_name → GENE:ENSG
participates_edges = edges[edges["predicate"] == "participates_in"]  # GENE:ENSG → PATHWAY
sex_diff_edges = edges[edges["predicate"] == "sex_differential_adverse_event"]  # DRUG → AE

print(f"  targets: {len(targets_edges):,}")
print(f"  same_gene: {len(same_gene_edges):,}")
print(f"  participates_in: {len(participates_edges):,}")
print(f"  sex_differential_ae: {len(sex_diff_edges):,}")

# Build mappings
# drug → gene:target_name
drug_to_target_gene = defaultdict(set)
for _, row in targets_edges.iterrows():
    drug_to_target_gene[row["subject"]].add(row["object"])

# gene:target_name → gene:ENSG
target_to_ensg = defaultdict(set)
for _, row in same_gene_edges.iterrows():
    target_to_ensg[row["subject"]].add(row["object"])

# gene:ENSG → pathway
ensg_to_pathway = defaultdict(set)
for _, row in participates_edges.iterrows():
    ensg_to_pathway[row["subject"]].add(row["object"])

# drug → sex_diff AEs
drug_sex_diff_aes = defaultdict(set)
for _, row in sex_diff_edges.iterrows():
    drug_sex_diff_aes[row["subject"]].add(row["object"])

# Trace: drug → target_gene → ENSG → pathway
drug_to_pathways = {}
drugs_with_pathways = 0
for drug, target_genes in drug_to_target_gene.items():
    pathways = set()
    for tg in target_genes:
        for ensg in target_to_ensg.get(tg, set()):
            for pw in ensg_to_pathway.get(ensg, set()):
                pathways.add(pw)
    if pathways:
        drug_to_pathways[drug] = pathways
        drugs_with_pathways += 1

print(f"\n  Drugs with target edges: {len(drug_to_target_gene):,}")
print(f"  Drugs traceable to pathways: {drugs_with_pathways:,}")
print(f"  Drugs with sex-diff signals: {len(drug_sex_diff_aes):,}")
print(f"  Drugs with BOTH: {len(set(drug_to_pathways.keys()) & set(drug_sex_diff_aes.keys())):,}")

# === Step 3: Pathway enrichment for sex-diff drugs ===
print("\n[3/5] Computing pathway enrichment for sex-differential drugs...")

# For each pathway: count how many drugs have sex-diff signals
pathway_drug_counts = defaultdict(lambda: {"total_drugs": 0, "sexdiff_drugs": 0, "total_signals": 0})

for drug, pathways in drug_to_pathways.items():
    has_sexdiff = drug in drug_sex_diff_aes
    n_signals = len(drug_sex_diff_aes.get(drug, set()))
    for pw in pathways:
        pathway_drug_counts[pw]["total_drugs"] += 1
        if has_sexdiff:
            pathway_drug_counts[pw]["sexdiff_drugs"] += 1
            pathway_drug_counts[pw]["total_signals"] += n_signals

# Convert to DataFrame
pathway_df = pd.DataFrame([
    {"pathway": pw, **counts}
    for pw, counts in pathway_drug_counts.items()
]).sort_values("sexdiff_drugs", ascending=False)

print(f"  Pathways reached: {len(pathway_df):,}")
print(f"  Top pathways by sex-diff drug count:")
for _, row in pathway_df.head(15).iterrows():
    pct = row["sexdiff_drugs"] / row["total_drugs"] * 100 if row["total_drugs"] > 0 else 0
    print(f"    {row['pathway']}: {row['sexdiff_drugs']}/{row['total_drugs']} drugs ({pct:.0f}%), "
          f"{row['total_signals']} signals")

# === Step 4: Load Reactome pathway names ===
print("\n[4/5] Loading Reactome pathway names...")
reactome_path = f"{BASE}/data/raw/reactome/ReactomePathways.txt"
pathway_names = {}
if os.path.exists(reactome_path):
    with open(reactome_path) as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 3 and parts[2] == "Homo sapiens":
                # R-HSA-XXXX → pathway name
                pathway_names[f"PATHWAY:{parts[0]}"] = parts[1]
    print(f"  Loaded {len(pathway_names):,} human pathway names")

# Add names to results
pathway_df["pathway_name"] = pathway_df["pathway"].map(pathway_names)
pathway_df["sexdiff_fraction"] = pathway_df["sexdiff_drugs"] / pathway_df["total_drugs"]

# === Step 5: Save results ===
print("\n[5/5] Saving results...")

# Filter to significant pathways (>= 3 drugs, >= 2 sex-diff)
significant = pathway_df[(pathway_df["total_drugs"] >= 3) & (pathway_df["sexdiff_drugs"] >= 2)]
print(f"  Significant pathways (>=3 drugs, >=2 sex-diff): {len(significant):,}")

results = {
    "analysis": "pathway_sex_differential_enrichment",
    "wave": 1,
    "kg_version": "v5.2",
    "timestamp": datetime.now().isoformat(),
    "novelty": "First analysis connecting drug safety signals to Reactome pathways via identifier bridges (impossible in v5)",
    "summary": {
        "drugs_with_targets": len(drug_to_target_gene),
        "drugs_traceable_to_pathways": drugs_with_pathways,
        "drugs_with_sex_diff_signals": len(drug_sex_diff_aes),
        "drugs_with_both": len(set(drug_to_pathways.keys()) & set(drug_sex_diff_aes.keys())),
        "pathways_reached": len(pathway_df),
        "significant_pathways": len(significant),
    },
    "top_pathways": [],
}

for _, row in significant.head(30).iterrows():
    results["top_pathways"].append({
        "pathway_id": row["pathway"],
        "pathway_name": row.get("pathway_name", "Unknown"),
        "total_drugs": int(row["total_drugs"]),
        "sexdiff_drugs": int(row["sexdiff_drugs"]),
        "sexdiff_fraction": round(float(row["sexdiff_fraction"]), 3),
        "total_signals": int(row["total_signals"]),
    })

out_path = f"{OUT_DIR}/v52_wave1_pathway_sex_analysis.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"  Results: {out_path}")

# Save full pathway table
table_path = f"{OUT_DIR}/v52_pathway_enrichment_table.tsv"
significant.to_csv(table_path, sep="\t", index=False)
print(f"  Table: {table_path}")

# Generate figure
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    top20 = significant.head(20).copy()
    top20["label"] = top20["pathway_name"].fillna(top20["pathway"]).str[:50]

    fig, ax = plt.subplots(figsize=(14, 8))
    bars = ax.barh(range(len(top20)), top20["sexdiff_drugs"], color="#2196F3", alpha=0.8)
    ax.set_yticks(range(len(top20)))
    ax.set_yticklabels(top20["label"], fontsize=8)
    ax.set_xlabel("Drugs with Sex-Differential Safety Signals")
    ax.set_title("Top 20 Reactome Pathways by Sex-Differential Drug Safety\n(SexDiffKG v5.2 — Bridge-Connected Analysis)")
    ax.invert_yaxis()

    # Add count labels
    for i, (idx, row) in enumerate(top20.iterrows()):
        ax.text(row["sexdiff_drugs"] + 0.1, i,
                f"{row['sexdiff_drugs']}/{row['total_drugs']} ({row['sexdiff_fraction']*100:.0f}%)",
                va="center", fontsize=7)

    plt.tight_layout()
    fig_path = f"{FIG_DIR}/v52_wave1_pathway_enrichment.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"  Figure: {fig_path}")
except Exception as e:
    print(f"  Figure generation failed: {e}")

print(f"\n{'=' * 70}")
print("WAVE 1 COMPLETE")
print(f"{'=' * 70}")
