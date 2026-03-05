#!/usr/bin/env python3
"""Swarm Block B (Waves 106-110): Clinical Trial Sex Gaps Analysis
Cross-reference VEDA clinical trials with SexDiffKG drug safety signals.
"""
import pandas as pd
import numpy as np
import json
import os
from datetime import datetime
from collections import defaultdict

base = "/home/jshaik369/sexdiffkg"
v5_dir = f"{base}/data/kg_v5"
results_dir = f"{base}/results/analysis"
deep_dir = "/tmp/sexdiffkg-deep-analysis"
os.makedirs(f"{deep_dir}/results", exist_ok=True)
os.makedirs(f"{deep_dir}/figures", exist_ok=True)

print("=== Swarm B: Clinical Trial Sex Gaps ===")
print(f"Started: {datetime.now().isoformat()}\n")

edges = pd.read_csv(f"{v5_dir}/edges.tsv", sep='\t')
nodes = pd.read_csv(f"{v5_dir}/nodes.tsv", sep='\t')

# Get node lookups
node_name = dict(zip(nodes['id'], nodes['name']))
node_cat = dict(zip(nodes['id'], nodes['category']))

# Trial-related edges
investigates = edges[edges['predicate'] == 'investigates']
tests_intervention = edges[edges['predicate'] == 'tests_intervention']
treats = edges[edges['predicate'] == 'treats']
sexdiff = edges[edges['predicate'] == 'sex_differential_adverse_event']

print(f"Investigates edges: {len(investigates):,}")
print(f"Tests_intervention edges: {len(tests_intervention):,}")
print(f"Treats edges: {len(treats):,}")
print(f"Sex-differential edges: {len(sexdiff):,}")

# Clinical trial nodes
trial_nodes = nodes[nodes['category'] == 'ClinicalTrial']
print(f"Clinical trial nodes: {len(trial_nodes):,}")

# Map trials to drugs/interventions
trial_interventions = defaultdict(set)
for _, row in tests_intervention.iterrows():
    trial_interventions[row['subject']].add(row['object'])

trial_diseases = defaultdict(set)
for _, row in investigates.iterrows():
    trial_diseases[row['subject']].add(row['object'])

# Map drugs to their sex-differential signals
drug_signals = defaultdict(list)
for _, row in sexdiff.iterrows():
    drug_signals[row['subject']].append(row['object'])

print(f"\nTrials with interventions: {len(trial_interventions):,}")
print(f"Trials investigating diseases: {len(trial_diseases):,}")
print(f"Drugs with sex-diff signals: {len(drug_signals):,}")

# === WAVE 106: Match trials to sex-diff drugs ===
print("\n--- Wave 106: Trial-Drug sex-diff matching ---")

trial_sexdiff_match = []
for trial_id, interventions in trial_interventions.items():
    for intervention in interventions:
        if intervention in drug_signals:
            trial_sexdiff_match.append({
                'trial_id': trial_id,
                'trial_name': node_name.get(trial_id, trial_id),
                'drug_id': intervention,
                'drug_name': node_name.get(intervention, intervention),
                'n_sexdiff_signals': len(drug_signals[intervention]),
                'diseases': [node_name.get(d, d) for d in trial_diseases.get(trial_id, set())],
            })

match_df = pd.DataFrame(trial_sexdiff_match)
if len(match_df) > 0:
    match_df = match_df.sort_values('n_sexdiff_signals', ascending=False)
    print(f"Trials testing drugs with sex-diff signals: {match_df['trial_id'].nunique():,}")
    print(f"Drugs matched: {match_df['drug_id'].nunique():,}")
    print("\nTop 20 trial-drug matches by signal count:")
    for _, row in match_df.head(20).iterrows():
        diseases = ', '.join(row['diseases'][:3]) if row['diseases'] else 'unknown'
        print(f"  {row['trial_name'][:30]:30s} | {row['drug_name'][:25]:25s} | {row['n_sexdiff_signals']:4d} signals | {diseases[:30]}")

# === WAVE 107: Therapeutic area analysis ===
print("\n--- Wave 107: Therapeutic area trial coverage ---")

disease_trial_counts = defaultdict(lambda: {'total_trials': 0, 'trials_with_sexdiff_drugs': 0, 'sexdiff_drugs': set()})
for trial_id, diseases in trial_diseases.items():
    interventions = trial_interventions.get(trial_id, set())
    has_sexdiff = any(i in drug_signals for i in interventions)
    sexdiff_drugs = [i for i in interventions if i in drug_signals]

    for disease in diseases:
        disease_trial_counts[disease]['total_trials'] += 1
        if has_sexdiff:
            disease_trial_counts[disease]['trials_with_sexdiff_drugs'] += 1
        for d in sexdiff_drugs:
            disease_trial_counts[disease]['sexdiff_drugs'].add(d)

disease_coverage = []
for disease, info in disease_trial_counts.items():
    disease_coverage.append({
        'disease_id': disease,
        'disease_name': node_name.get(disease, disease),
        'total_trials': info['total_trials'],
        'trials_with_sexdiff_drugs': info['trials_with_sexdiff_drugs'],
        'n_sexdiff_drugs': len(info['sexdiff_drugs']),
        'coverage_frac': info['trials_with_sexdiff_drugs'] / info['total_trials'] if info['total_trials'] > 0 else 0,
    })

cov_df = pd.DataFrame(disease_coverage).sort_values('trials_with_sexdiff_drugs', ascending=False)
print(f"Diseases with trial data: {len(cov_df):,}")
print("\nTop 20 diseases by sex-diff drug trial coverage:")
for _, row in cov_df.head(20).iterrows():
    print(f"  {row['disease_name'][:40]:40s} | {row['total_trials']:4d} trials | {row['trials_with_sexdiff_drugs']:4d} sex-diff | {row['n_sexdiff_drugs']:3d} drugs | {100*row['coverage_frac']:.0f}%")

# === WAVE 108: Most urgent sex-stratification gaps ===
print("\n--- Wave 108: Most urgent sex-stratification needs ---")

# Drugs with many sex-diff signals but few or no trials
all_drugs_in_trials = set()
for trial_id, interventions in trial_interventions.items():
    all_drugs_in_trials.update(interventions)

urgent_gaps = []
for drug, signals in drug_signals.items():
    n_trials = sum(1 for t, intv in trial_interventions.items() if drug in intv)
    urgent_gaps.append({
        'drug_id': drug,
        'drug_name': node_name.get(drug, drug),
        'n_sexdiff_signals': len(signals),
        'n_trials': n_trials,
        'urgency_score': len(signals) / max(n_trials, 1),
    })

gap_df = pd.DataFrame(urgent_gaps).sort_values('urgency_score', ascending=False)
print("Top 30 drugs: high sex-diff signals / low trial coverage:")
for _, row in gap_df.head(30).iterrows():
    print(f"  {row['drug_name'][:40]:40s} | {row['n_sexdiff_signals']:4d} signals | {row['n_trials']:3d} trials | urgency={row['urgency_score']:.1f}")

# Save results
results = {
    'timestamp': datetime.now().isoformat(),
    'summary': {
        'total_trials': len(trial_nodes),
        'trials_with_interventions': len(trial_interventions),
        'trials_matched_to_sexdiff': int(match_df['trial_id'].nunique()) if len(match_df) > 0 else 0,
        'drugs_with_sexdiff_in_trials': int(match_df['drug_id'].nunique()) if len(match_df) > 0 else 0,
        'diseases_with_trial_data': len(cov_df),
    },
    'wave_106_trial_matches': match_df.head(50).to_dict('records') if len(match_df) > 0 else [],
    'wave_107_disease_coverage': cov_df.head(50).to_dict('records'),
    'wave_108_urgent_gaps': gap_df.head(50).to_dict('records'),
}

for path in [f"{results_dir}/clinical_trial_sex_gaps.json", f"{deep_dir}/results/clinical_trial_sex_gaps.json"]:
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, default=str)

# Figure
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(18, 8))
    fig.suptitle('SexDiffKG v5: Clinical Trial Sex-Stratification Gaps', fontsize=14, fontweight='bold')

    # Trial coverage by disease
    top_cov = cov_df.head(15)
    axes[0].barh(range(len(top_cov)), top_cov['trials_with_sexdiff_drugs'].values, color='#2ecc71', label='With sex-diff drugs')
    axes[0].barh(range(len(top_cov)), top_cov['total_trials'].values, alpha=0.3, color='#95a5a6', label='All trials')
    axes[0].set_yticks(range(len(top_cov)))
    axes[0].set_yticklabels([n[:30] for n in top_cov['disease_name'].values], fontsize=8)
    axes[0].set_xlabel('Number of Trials')
    axes[0].set_title('Disease Trial Coverage')
    axes[0].legend(fontsize=8)
    axes[0].invert_yaxis()

    # Urgency scores
    top_gap = gap_df.head(20)
    colors = ['#e74c3c' if t == 0 else '#f39c12' for t in top_gap['n_trials'].values]
    axes[1].barh(range(len(top_gap)), top_gap['urgency_score'].values, color=colors)
    axes[1].set_yticks(range(len(top_gap)))
    axes[1].set_yticklabels([n[:25] for n in top_gap['drug_name'].values], fontsize=7)
    axes[1].set_xlabel('Urgency Score (signals / trials)')
    axes[1].set_title('Sex-Stratification Urgency')
    axes[1].invert_yaxis()

    # Signal vs trial scatter
    axes[2].scatter(gap_df['n_trials'], gap_df['n_sexdiff_signals'], alpha=0.3, s=10, c='#3498db')
    axes[2].set_xlabel('Number of Clinical Trials')
    axes[2].set_ylabel('Sex-Differential Signals')
    axes[2].set_title('Trial Coverage vs Sex-Diff Signals')
    axes[2].set_xscale('symlog')

    plt.tight_layout()
    for fmt in ['png', 'pdf']:
        fig.savefig(f"{deep_dir}/figures/fig266_trial_sex_gaps.{fmt}", dpi=300, bbox_inches='tight')
    plt.close()
    print("\nFigure saved: fig266_trial_sex_gaps")
except Exception as e:
    print(f"Figure error: {e}")

print(f"\nCompleted: {datetime.now().isoformat()}")
