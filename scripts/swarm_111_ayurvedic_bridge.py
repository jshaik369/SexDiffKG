#!/usr/bin/env python3
"""Swarm Block C (Waves 111-115): Ayurvedic-Modern Pharmacovigilance Bridge
Trace paths: Herbs → compounds → drug targets → sex-differential safety signals.
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

print("=== Swarm C: Ayurvedic-Modern Pharmacovigilance Bridge ===")
print(f"Started: {datetime.now().isoformat()}\n")

edges = pd.read_csv(f"{v5_dir}/edges.tsv", sep='\t')
nodes = pd.read_csv(f"{v5_dir}/nodes.tsv", sep='\t')

node_name = dict(zip(nodes['id'], nodes['name']))
node_cat = dict(zip(nodes['id'], nodes['category']))

# Get Ayurvedic entities
herbs = nodes[nodes['category'] == 'Herb']
doshas = nodes[nodes['category'] == 'Dosha']
rasas = nodes[nodes['category'] == 'Rasa']
gunas = nodes[nodes['category'] == 'Guna']
compounds = nodes[nodes['category'] == 'Compound']

print(f"Herbs: {len(herbs)}")
print(f"Doshas: {len(doshas)}")
print(f"Rasas: {len(rasas)}")
print(f"Gunas: {len(gunas)}")
print(f"Compounds: {len(compounds):,}")

# Build adjacency for path tracing
adj = defaultdict(lambda: defaultdict(set))
for _, row in edges.iterrows():
    adj[row['subject']][row['predicate']].add(row['object'])
    adj[row['object']][f"inv_{row['predicate']}"].add(row['subject'])

# === WAVE 111: Herb-compound-target-AE paths ===
print("\n--- Wave 111: Herb→compound→target→AE pathway tracing ---")

herb_paths = []
for _, herb in herbs.iterrows():
    herb_id = herb['id']
    herb_name = herb['name']

    # Find compounds linked to herb
    herb_compounds = set()
    for pred in adj[herb_id]:
        for target in adj[herb_id][pred]:
            if node_cat.get(target) == 'Compound':
                herb_compounds.add(target)

    # Also check inverse
    for pred in adj[herb_id]:
        if pred.startswith('inv_'):
            for source in adj[herb_id][pred]:
                if node_cat.get(source) == 'Compound':
                    herb_compounds.add(source)

    # For each compound, find targets
    for compound in herb_compounds:
        compound_targets = set()
        for pred in ['targets', 'binds_to', 'modulates']:
            compound_targets.update(adj[compound].get(pred, set()))

        # For each target, find drugs targeting it
        for target in compound_targets:
            target_drugs = adj[target].get('inv_targets', set())

            # For each drug, check sex-diff AEs
            for drug in target_drugs:
                sexdiff_aes = adj[drug].get('sex_differential_adverse_event', set())
                if sexdiff_aes:
                    herb_paths.append({
                        'herb': herb_name,
                        'compound': node_name.get(compound, compound),
                        'target': node_name.get(target, target),
                        'drug': node_name.get(drug, drug),
                        'n_sexdiff_aes': len(sexdiff_aes),
                        'sample_aes': [node_name.get(ae, ae) for ae in list(sexdiff_aes)[:5]],
                    })

print(f"Herb→compound→target→drug→AE paths found: {len(herb_paths):,}")
if herb_paths:
    path_df = pd.DataFrame(herb_paths)
    print("\nAll herb-drug-AE connections:")
    for _, row in path_df.iterrows():
        aes = ', '.join(row['sample_aes'][:3])
        print(f"  {row['herb'][:20]:20s} → {row['compound'][:20]:20s} → {row['target'][:20]:20s} → {row['drug'][:20]:20s} | {row['n_sexdiff_aes']} AEs ({aes})")

# === WAVE 112: Dosha-drug-AE connections ===
print("\n--- Wave 112: Dosha-drug connections ---")

dosha_connections = []
for _, dosha in doshas.iterrows():
    dosha_id = dosha['id']
    dosha_name = dosha['name']

    # Compounds that aggravate/pacify this dosha
    aggravates = adj[dosha_id].get('inv_aggravates_dosha', set())
    pacifies = adj[dosha_id].get('inv_pacifies_dosha', set())

    dosha_connections.append({
        'dosha': dosha_name,
        'n_aggravating': len(aggravates),
        'n_pacifying': len(pacifies),
        'aggravating_names': [node_name.get(c, c) for c in list(aggravates)[:10]],
        'pacifying_names': [node_name.get(c, c) for c in list(pacifies)[:10]],
    })
    print(f"  {dosha_name}: {len(aggravates)} aggravating, {len(pacifies)} pacifying compounds")

# === WAVE 113: Compound-target overlap between Ayurvedic and modern drugs ===
print("\n--- Wave 113: Shared targets between Ayurvedic compounds and modern drugs ---")

compound_ids = set(compounds['id'].tolist())
drug_nodes = nodes[nodes['category'] == 'Drug']
drug_ids = set(drug_nodes['id'].tolist())

# Get targets of compounds vs drugs
compound_targets = defaultdict(set)
drug_targets = defaultdict(set)

for pred in ['targets', 'binds_to']:
    for subj in adj:
        if subj in compound_ids:
            compound_targets[subj].update(adj[subj].get(pred, set()))
        elif subj in drug_ids:
            drug_targets[subj].update(adj[subj].get(pred, set()))

all_compound_targets = set()
for targets in compound_targets.values():
    all_compound_targets.update(targets)

all_drug_targets = set()
for targets in drug_targets.values():
    all_drug_targets.update(targets)

shared_targets = all_compound_targets & all_drug_targets
print(f"Unique compound targets: {len(all_compound_targets):,}")
print(f"Unique drug targets: {len(all_drug_targets):,}")
print(f"Shared targets: {len(shared_targets):,}")

if shared_targets:
    print("\nShared targets between Ayurvedic compounds and modern drugs:")
    for t in list(shared_targets)[:20]:
        t_name = node_name.get(t, t)
        # Find compounds and drugs targeting this
        comps = [c for c, ts in compound_targets.items() if t in ts]
        drugs = [d for d, ts in drug_targets.items() if t in ts]
        # Check if any of those drugs have sex-diff signals
        sexdiff_count = sum(len(adj[d].get('sex_differential_adverse_event', set())) for d in drugs)
        print(f"  {t_name[:40]:40s} | {len(comps)} compounds, {len(drugs)} drugs | {sexdiff_count} sex-diff signals")

# Save results
results = {
    'timestamp': datetime.now().isoformat(),
    'ayurvedic_entities': {
        'herbs': len(herbs),
        'doshas': len(doshas),
        'rasas': len(rasas),
        'gunas': len(gunas),
        'compounds': len(compounds),
    },
    'wave_111_herb_paths': herb_paths[:100],
    'wave_112_dosha_connections': dosha_connections,
    'wave_113_shared_targets': {
        'compound_targets': len(all_compound_targets),
        'drug_targets': len(all_drug_targets),
        'shared': len(shared_targets),
        'shared_target_names': [node_name.get(t, t) for t in list(shared_targets)[:50]],
    },
}

for path in [f"{results_dir}/ayurvedic_pharmacovig_bridge.json", f"{deep_dir}/results/ayurvedic_pharmacovig_bridge.json"]:
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, default=str)

print(f"\nCompleted: {datetime.now().isoformat()}")
