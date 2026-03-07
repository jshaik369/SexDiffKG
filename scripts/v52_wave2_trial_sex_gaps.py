#!/usr/bin/env python3
"""v5.2 Wave 2: Clinical Trial Sex Gaps Analysis

Cross-reference 27K clinical trials from VEDA-KG with sex-differential drug safety signals.
Identify drugs with strong sex-differential signals but NO sex-stratified trials.

This is a direct policy-relevant analysis: which drugs urgently need sex-stratified trials?
Only possible with v5.2 merged KG (VEDA-KG brings clinical trials, SexDiffKG brings safety signals).
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
print("WAVE 2: CLINICAL TRIAL SEX GAPS ANALYSIS")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

# Load edges
print("\n[1/4] Loading v5.2 edges...")
edges = pd.read_csv(f"{V52_DIR}/edges.tsv", sep="\t")

# Get relevant edge subsets
sex_diff = edges[edges["predicate"] == "sex_differential_adverse_event"]
has_ae = edges[edges["predicate"] == "has_adverse_event"]
tests_intervention = edges[edges["predicate"] == "tests_intervention"]
investigates = edges[edges["predicate"] == "investigates"]
treats = edges[edges["predicate"] == "treats"]

print(f"  sex_differential_ae: {len(sex_diff):,}")
print(f"  has_adverse_event: {len(has_ae):,}")
print(f"  tests_intervention: {len(tests_intervention):,}")
print(f"  investigates: {len(investigates):,}")
print(f"  treats: {len(treats):,}")

# === Step 2: Map drugs to their trial coverage ===
print("\n[2/4] Mapping drug-trial coverage...")

# Drug → number of sex-diff AE signals
drug_signal_counts = sex_diff.groupby("subject").size().reset_index(name="n_signals")
drug_signal_counts.columns = ["drug", "n_signals"]

# Drug → number of total AE edges
drug_ae_counts = has_ae.groupby("subject").size().reset_index(name="n_ae")
drug_ae_counts.columns = ["drug", "n_ae"]

# Drug → clinical trials (via tests_intervention)
# tests_intervention: TRIAL → DRUG
trial_drugs = tests_intervention.groupby("object").agg(
    n_trials=("subject", "nunique"),
    trial_ids=("subject", list)
).reset_index()
trial_drugs.columns = ["drug", "n_trials", "trial_ids"]

# Merge
drug_profile = drug_signal_counts.merge(drug_ae_counts, on="drug", how="left")
drug_profile = drug_profile.merge(trial_drugs, on="drug", how="left")
drug_profile["n_trials"] = drug_profile["n_trials"].fillna(0).astype(int)
drug_profile["signal_rate"] = drug_profile["n_signals"] / drug_profile["n_ae"].fillna(1)

# Sort by signals descending
drug_profile = drug_profile.sort_values("n_signals", ascending=False)

print(f"  Drugs with sex-diff signals: {len(drug_profile):,}")
print(f"  Drugs with clinical trials: {(drug_profile['n_trials'] > 0).sum():,}")
print(f"  Drugs with NO trials: {(drug_profile['n_trials'] == 0).sum():,}")

# === Step 3: Identify gaps ===
print("\n[3/4] Identifying drugs needing sex-stratified trials...")

# High-signal, no-trial drugs
gaps = drug_profile[(drug_profile["n_signals"] >= 10) & (drug_profile["n_trials"] == 0)]
gaps = gaps.sort_values("n_signals", ascending=False)

print(f"  Drugs with >=10 sex-diff signals and NO trials: {len(gaps):,}")
print(f"\n  Top 20 drugs urgently needing sex-stratified trials:")
for _, row in gaps.head(20).iterrows():
    drug_name = row["drug"].replace("DRUG:", "")
    print(f"    {drug_name}: {row['n_signals']} sex-diff signals, "
          f"{row['n_ae']} total AEs, "
          f"signal rate: {row['signal_rate']:.1%}")

# High-signal, some-trial drugs (may still lack sex stratification)
covered = drug_profile[(drug_profile["n_signals"] >= 10) & (drug_profile["n_trials"] > 0)]
print(f"\n  Drugs with >=10 sex-diff signals AND trials: {len(covered):,}")
print(f"  Top 10 by signal count (have trials):")
for _, row in covered.head(10).iterrows():
    drug_name = row["drug"].replace("DRUG:", "")
    print(f"    {drug_name}: {row['n_signals']} signals, {row['n_trials']} trials")

# === Step 4: Disease-drug-trial analysis ===
print("\n[4/4] Disease-drug-trial sex gap analysis...")

# What diseases do the high-signal no-trial drugs treat?
drug_diseases = treats[treats["subject"].isin(gaps["drug"])]
disease_counts = drug_diseases.groupby("object").size().sort_values(ascending=False)

print(f"  Diseases treated by gap drugs: {len(disease_counts):,}")
if len(disease_counts) > 0:
    print(f"  Top diseases:")
    for disease, count in disease_counts.head(10).items():
        disease_name = disease.replace("DISEASE:", "")
        print(f"    {disease_name}: {count} gap drugs")

# === Save results ===
results = {
    "analysis": "clinical_trial_sex_gaps",
    "wave": 2,
    "kg_version": "v5.2",
    "timestamp": datetime.now().isoformat(),
    "novelty": "Cross-referencing VEDA-KG clinical trials with SexDiffKG safety signals to identify evidence gaps",
    "summary": {
        "drugs_with_sex_diff_signals": len(drug_profile),
        "drugs_with_trials": int((drug_profile['n_trials'] > 0).sum()),
        "drugs_without_trials": int((drug_profile['n_trials'] == 0).sum()),
        "high_signal_no_trial_drugs": len(gaps),
        "high_signal_with_trial_drugs": len(covered),
    },
    "urgently_need_trials": [],
    "have_trials_high_signals": [],
}

for _, row in gaps.head(50).iterrows():
    results["urgently_need_trials"].append({
        "drug": row["drug"],
        "n_signals": int(row["n_signals"]),
        "n_ae": int(row["n_ae"]) if pd.notna(row["n_ae"]) else 0,
        "signal_rate": round(float(row["signal_rate"]), 3) if pd.notna(row["signal_rate"]) else 0,
    })

for _, row in covered.head(20).iterrows():
    results["have_trials_high_signals"].append({
        "drug": row["drug"],
        "n_signals": int(row["n_signals"]),
        "n_trials": int(row["n_trials"]),
    })

out_path = f"{OUT_DIR}/v52_wave2_trial_sex_gaps.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\n  Results: {out_path}")

# Save full table
table_path = f"{OUT_DIR}/v52_drug_trial_gap_table.tsv"
drug_profile.drop(columns=["trial_ids"], errors="ignore").to_csv(table_path, sep="\t", index=False)
print(f"  Table: {table_path}")

# Generate figure
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    # Left: top 20 gap drugs
    top_gaps = gaps.head(20).copy()
    top_gaps["label"] = top_gaps["drug"].str.replace("DRUG:", "")
    axes[0].barh(range(len(top_gaps)), top_gaps["n_signals"], color="#E53935", alpha=0.8)
    axes[0].set_yticks(range(len(top_gaps)))
    axes[0].set_yticklabels(top_gaps["label"], fontsize=8)
    axes[0].set_xlabel("Sex-Differential Safety Signals")
    axes[0].set_title("Top 20 Drugs Urgently Needing\nSex-Stratified Clinical Trials")
    axes[0].invert_yaxis()

    # Right: signal distribution by trial status
    with_trials = drug_profile[drug_profile["n_trials"] > 0]["n_signals"]
    without_trials = drug_profile[drug_profile["n_trials"] == 0]["n_signals"]

    axes[1].hist(with_trials, bins=50, alpha=0.7, label=f"Has trials (n={len(with_trials)})", color="#2196F3")
    axes[1].hist(without_trials, bins=50, alpha=0.7, label=f"No trials (n={len(without_trials)})", color="#E53935")
    axes[1].set_xlabel("Number of Sex-Differential Signals")
    axes[1].set_ylabel("Number of Drugs")
    axes[1].set_title("Distribution of Sex-Differential Signals\nby Clinical Trial Coverage")
    axes[1].legend()
    axes[1].set_yscale("log")

    plt.suptitle("SexDiffKG v5.2 — Clinical Trial Sex Gap Analysis", fontsize=14, fontweight="bold")
    plt.tight_layout()
    fig_path = f"{FIG_DIR}/v52_wave2_trial_sex_gaps.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"  Figure: {fig_path}")
except Exception as e:
    print(f"  Figure failed: {e}")

print(f"\n{'=' * 70}")
print("WAVE 2 COMPLETE")
print(f"{'=' * 70}")
