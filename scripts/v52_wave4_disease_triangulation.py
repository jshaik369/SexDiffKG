#!/usr/bin/env python3
"""v5.2 Wave 4: Disease-Drug-Sex Triangulation

For each disease in the merged KG:
1. Find drugs that treat it (treats edges from VEDA)
2. Count sex-differential safety signals for those drugs
3. Identify diseases where treatment drugs show strongest sex bias
4. Cross-reference with disease-pathway associations

Novel: Which diseases have treatment options that are systematically sex-biased in safety?
"""
import os
import json
import pandas as pd
from datetime import datetime
from collections import defaultdict

BASE = "/home/jshaik369/sexdiffkg"
V52_DIR = f"{BASE}/data/kg_v5.2"
OUT_DIR = "/tmp/sexdiffkg-deep-analysis/results"
FIG_DIR = "/tmp/sexdiffkg-deep-analysis/figures"

print("=" * 70)
print("WAVE 4: DISEASE-DRUG-SEX TRIANGULATION")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

# Load edges
edges = pd.read_csv(f"{V52_DIR}/edges.tsv", sep="\t")

treats = edges[edges["predicate"] == "treats"]
sex_diff = edges[edges["predicate"] == "sex_differential_adverse_event"]
investigates = edges[edges["predicate"] == "investigates"]
assoc = edges[edges["predicate"] == "associated_with"]

print(f"  treats: {len(treats):,}")
print(f"  sex_differential_ae: {len(sex_diff):,}")
print(f"  investigates: {len(investigates):,}")
print(f"  associated_with: {len(assoc):,}")

# === Disease → drugs → sex-diff signals ===
print("\n[1/3] Building disease-drug-signal triangulation...")

# Drug → signal count
drug_signals = sex_diff.groupby("subject").size().to_dict()

# Disease → drugs (via treats)
disease_drugs = defaultdict(set)
for _, row in treats.iterrows():
    disease_drugs[row["object"]].add(row["subject"])

# Disease → trials (via investigates)
disease_trials = investigates.groupby("object")["subject"].nunique().to_dict()

# Compute per-disease stats
disease_stats = []
for disease, drugs in disease_drugs.items():
    total_signals = sum(drug_signals.get(d, 0) for d in drugs)
    drugs_with_signals = sum(1 for d in drugs if d in drug_signals)
    n_trials = disease_trials.get(disease, 0)

    if len(drugs) >= 3:  # Only diseases with >=3 treatment drugs
        disease_stats.append({
            "disease": disease,
            "n_drugs": len(drugs),
            "drugs_with_signals": drugs_with_signals,
            "signal_fraction": drugs_with_signals / len(drugs),
            "total_signals": total_signals,
            "avg_signals_per_drug": total_signals / len(drugs) if drugs else 0,
            "n_trials": n_trials,
        })

disease_df = pd.DataFrame(disease_stats).sort_values("total_signals", ascending=False)

print(f"  Diseases with >=3 treatment drugs: {len(disease_df):,}")
print(f"  Diseases where >50% of drugs have sex-diff signals: "
      f"{len(disease_df[disease_df['signal_fraction'] > 0.5]):,}")

print(f"\n  Top 20 diseases by total sex-differential drug safety signals:")
for _, row in disease_df.head(20).iterrows():
    name = row["disease"].replace("DISEASE:", "")[:50]
    print(f"    {name}: {row['total_signals']:,.0f} signals, "
          f"{row['drugs_with_signals']}/{row['n_drugs']} drugs ({row['signal_fraction']:.0%}), "
          f"{row['n_trials']} trials")

# === High signal fraction diseases ===
print(f"\n[2/3] Diseases with highest sex-differential drug signal fraction...")
high_frac = disease_df[disease_df["n_drugs"] >= 5].sort_values("signal_fraction", ascending=False)
print(f"\n  Top 15 by signal fraction (>=5 drugs):")
for _, row in high_frac.head(15).iterrows():
    name = row["disease"].replace("DISEASE:", "")[:50]
    print(f"    {name}: {row['signal_fraction']:.0%} ({row['drugs_with_signals']}/{row['n_drugs']}), "
          f"{row['total_signals']:,.0f} signals")

# === Save ===
print(f"\n[3/3] Saving results...")

results = {
    "analysis": "disease_drug_sex_triangulation",
    "wave": 4,
    "kg_version": "v5.2",
    "timestamp": datetime.now().isoformat(),
    "novelty": "Identifies diseases where treatment drugs systematically show sex-biased safety profiles",
    "summary": {
        "diseases_analyzed": len(disease_df),
        "diseases_high_signal_fraction": int(len(disease_df[disease_df["signal_fraction"] > 0.5])),
    },
    "top_by_signals": [],
    "top_by_fraction": [],
}

for _, row in disease_df.head(30).iterrows():
    results["top_by_signals"].append({
        "disease": row["disease"],
        "n_drugs": int(row["n_drugs"]),
        "drugs_with_signals": int(row["drugs_with_signals"]),
        "signal_fraction": round(float(row["signal_fraction"]), 3),
        "total_signals": int(row["total_signals"]),
        "n_trials": int(row["n_trials"]),
    })

for _, row in high_frac.head(20).iterrows():
    results["top_by_fraction"].append({
        "disease": row["disease"],
        "n_drugs": int(row["n_drugs"]),
        "drugs_with_signals": int(row["drugs_with_signals"]),
        "signal_fraction": round(float(row["signal_fraction"]), 3),
        "total_signals": int(row["total_signals"]),
    })

out_path = f"{OUT_DIR}/v52_wave4_disease_triangulation.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"  Results: {out_path}")

# Figure
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))

    # Left: top 20 by total signals
    top20 = disease_df.head(20).copy()
    top20["label"] = top20["disease"].str.replace("DISEASE:", "").str[:40]
    ax1.barh(range(len(top20)), top20["total_signals"], color="#2196F3", alpha=0.8)
    ax1.set_yticks(range(len(top20)))
    ax1.set_yticklabels(top20["label"], fontsize=7)
    ax1.set_xlabel("Total Sex-Differential Safety Signals")
    ax1.set_title("Top 20 Diseases by Total\nSex-Differential Drug Safety Signals")
    ax1.invert_yaxis()

    # Right: top 20 by signal fraction
    top_frac = high_frac.head(20).copy()
    top_frac["label"] = top_frac["disease"].str.replace("DISEASE:", "").str[:40]
    bars = ax2.barh(range(len(top_frac)), top_frac["signal_fraction"] * 100,
                    color="#E53935", alpha=0.8)
    ax2.set_yticks(range(len(top_frac)))
    ax2.set_yticklabels(top_frac["label"], fontsize=7)
    ax2.set_xlabel("% Treatment Drugs with Sex-Differential Signals")
    ax2.set_title("Diseases with Highest Fraction of\nSex-Biased Treatment Drugs (>=5 drugs)")
    ax2.invert_yaxis()

    plt.suptitle("SexDiffKG v5.2 — Disease-Drug-Sex Triangulation", fontsize=14, fontweight="bold")
    plt.tight_layout()
    fig_path = f"{FIG_DIR}/v52_wave4_disease_triangulation.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"  Figure: {fig_path}")
except Exception as e:
    print(f"  Figure failed: {e}")

print(f"\n{'=' * 70}")
print("WAVE 4 COMPLETE")
print(f"{'=' * 70}")
