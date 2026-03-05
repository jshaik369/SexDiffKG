#!/usr/bin/env python3
"""Link prediction on v5 merged KG using ComplEx embeddings.

Predicts novel drug-AE, drug-target, and drug-disease associations
from the trained ComplEx v5 model.

Run AFTER ComplEx v5 training completes.
"""
import torch
import json
import os
import numpy as np
from datetime import datetime
from collections import defaultdict

base = "/home/jshaik369/sexdiffkg"
emb_dir = f"{base}/results/kg_embeddings_v5"
out_dir = f"{base}/results/link_predictions_v5"
os.makedirs(out_dir, exist_ok=True)

print("=" * 70)
print("LINK PREDICTION — SexDiffKG v5 (ComplEx)")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

# Load mappings
entity_to_id = json.load(open(f"{emb_dir}/entity_to_id.json"))
relation_to_id = json.load(open(f"{emb_dir}/relation_to_id.json"))
id_to_entity = {v: k for k, v in entity_to_id.items()}
id_to_relation = {v: k for k, v in relation_to_id.items()}

print(f"Entities: {len(entity_to_id):,}")
print(f"Relations: {len(relation_to_id):,}")
print(f"Relation types: {list(relation_to_id.keys())}")

# Load existing triples for filtering
print("\nLoading existing triples...")
existing_triples = set()
triples_path = f"{base}/data/kg_v5/triples.tsv"
with open(triples_path) as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) == 3:
            existing_triples.add(tuple(parts))
print(f"Existing triples: {len(existing_triples):,}")

# Load checkpoint
print("\nLoading ComplEx v5 model...")
checkpoint_path = f"{emb_dir}/complex_v5_checkpoint.pt"
final_path = f"{emb_dir}/complex_v5_final.pt"

# Try final model first, then checkpoint
if os.path.exists(final_path):
    state = torch.load(final_path, map_location='cpu', weights_only=False)
    print(f"Loaded final model: {os.path.getsize(final_path)/1024/1024:.1f} MB")
elif os.path.exists(checkpoint_path):
    state = torch.load(checkpoint_path, map_location='cpu', weights_only=False)
    print(f"Loaded checkpoint: {os.path.getsize(checkpoint_path)/1024/1024:.1f} MB")
    # Extract model state from checkpoint
    if 'model_state_dict' in state:
        state = state['model_state_dict']
else:
    print("ERROR: No model found!")
    exit(1)

# Extract embeddings
if isinstance(state, dict) and 'entity_representations.0._embeddings.weight' in state:
    entity_emb = state['entity_representations.0._embeddings.weight']
    relation_emb = state['relation_representations.0._embeddings.weight']
elif isinstance(state, dict) and 'model_state_dict' in state:
    ms = state['model_state_dict']
    entity_emb = ms['entity_representations.0._embeddings.weight']
    relation_emb = ms['relation_representations.0._embeddings.weight']
else:
    # Try to find embedding keys
    print("Model state keys:")
    for k in sorted(state.keys()) if isinstance(state, dict) else []:
        if isinstance(state[k], torch.Tensor):
            print(f"  {k}: {state[k].shape}")
    # Try common patterns
    for prefix in ['', 'model.']:
        ek = f'{prefix}entity_representations.0._embeddings.weight'
        rk = f'{prefix}relation_representations.0._embeddings.weight'
        if ek in state:
            entity_emb = state[ek]
            relation_emb = state[rk]
            break
    else:
        print("ERROR: Could not find embedding tensors")
        exit(1)

print(f"Entity embeddings: {entity_emb.shape}")
print(f"Relation embeddings: {relation_emb.shape}")

# ComplEx scoring function
def complex_score(head_emb, rel_emb, tail_emb):
    """ComplEx interaction score."""
    # Split into real and imaginary
    re_head, im_head = head_emb.chunk(2, dim=-1)
    re_rel, im_rel = rel_emb.chunk(2, dim=-1)
    re_tail, im_tail = tail_emb.chunk(2, dim=-1)

    # ComplEx scoring
    score = (re_head * re_rel * re_tail +
             re_head * im_rel * im_tail +
             im_head * re_rel * im_tail -
             im_head * im_rel * re_tail).sum(dim=-1)
    return score

# Categorize entities
drugs = {k: v for k, v in entity_to_id.items() if k.startswith('DRUG:')}
aes = {k: v for k, v in entity_to_id.items() if k.startswith('AE:')}
genes = {k: v for k, v in entity_to_id.items() if k.startswith('GENE:')}
proteins = {k: v for k, v in entity_to_id.items() if k.startswith('PROTEIN:')}
diseases = {k: v for k, v in entity_to_id.items() if k.startswith('DISEASE:')}
trials = {k: v for k, v in entity_to_id.items() if k.startswith('TRIAL:')}

print(f"\nEntity categories:")
print(f"  Drugs: {len(drugs):,}")
print(f"  AEs: {len(aes):,}")
print(f"  Genes: {len(genes):,}")
print(f"  Proteins: {len(proteins):,}")
print(f"  Diseases: {len(diseases):,}")
print(f"  Trials: {len(trials):,}")

# Prediction function
def predict_tails(head_name, relation_name, candidate_entities, top_k=50, exclude_existing=True):
    """Predict top-k tail entities for a given head and relation."""
    if head_name not in entity_to_id or relation_name not in relation_to_id:
        return []

    head_id = entity_to_id[head_name]
    rel_id = relation_to_id[relation_name]

    head_e = entity_emb[head_id].unsqueeze(0)
    rel_e = relation_emb[rel_id].unsqueeze(0)

    candidate_ids = list(candidate_entities.values())
    candidate_names = list(candidate_entities.keys())

    tail_e = entity_emb[candidate_ids]

    # Score all candidates
    head_expanded = head_e.expand(len(candidate_ids), -1)
    rel_expanded = rel_e.expand(len(candidate_ids), -1)

    scores = complex_score(head_expanded, rel_expanded, tail_e)

    # Sort by score
    sorted_indices = torch.argsort(scores, descending=True)

    results = []
    for idx in sorted_indices:
        idx = idx.item()
        name = candidate_names[idx]
        score = scores[idx].item()

        # Check if this triple already exists
        triple = (head_name, relation_name, name)
        is_known = triple in existing_triples

        if exclude_existing and is_known:
            continue

        results.append({
            'head': head_name,
            'relation': relation_name,
            'tail': name,
            'score': round(score, 4),
            'known': is_known
        })

        if len(results) >= top_k:
            break

    return results

# === PREDICTION TASKS ===

all_predictions = {}

# 1. Novel drug-AE predictions for high-interest drugs
print("\n" + "=" * 70)
print("1. NOVEL DRUG-AE PREDICTIONS")
print("=" * 70)

focus_drugs = [
    'DRUG:RISPERIDONE', 'DRUG:METFORMIN', 'DRUG:ASPIRIN',
    'DRUG:IBUPROFEN', 'DRUG:ATORVASTATIN', 'DRUG:LISINOPRIL',
    'DRUG:NIVOLUMAB', 'DRUG:PEMBROLIZUMAB', 'DRUG:SEMAGLUTIDE',
    'DRUG:OZEMPIC', 'DRUG:METHOTREXATE', 'DRUG:WARFARIN'
]

ae_relation = None
for r in relation_to_id:
    if 'adverse' in r.lower() or 'ae' in r.lower() or 'has_adverse_event' in r:
        ae_relation = r
        break

if ae_relation:
    drug_ae_predictions = {}
    for drug in focus_drugs:
        if drug in entity_to_id:
            preds = predict_tails(drug, ae_relation, aes, top_k=20)
            if preds:
                drug_ae_predictions[drug] = preds
                print(f"\n{drug} → novel AEs (top 5):")
                for p in preds[:5]:
                    print(f"  {p['tail']}: {p['score']:.4f}")
    all_predictions['drug_ae'] = drug_ae_predictions
else:
    print("No adverse event relation found")

# 2. Novel drug-target predictions
print("\n" + "=" * 70)
print("2. NOVEL DRUG-TARGET PREDICTIONS")
print("=" * 70)

target_relation = None
for r in relation_to_id:
    if 'target' in r.lower() or 'binds' in r.lower():
        target_relation = r
        break

if target_relation:
    drug_target_predictions = {}
    for drug in focus_drugs:
        if drug in entity_to_id:
            # Predict targets (could be genes or proteins)
            gene_preds = predict_tails(drug, target_relation, genes, top_k=10)
            prot_preds = predict_tails(drug, target_relation, proteins, top_k=10)
            preds = sorted(gene_preds + prot_preds, key=lambda x: x['score'], reverse=True)[:10]
            if preds:
                drug_target_predictions[drug] = preds
                print(f"\n{drug} → novel targets (top 3):")
                for p in preds[:3]:
                    print(f"  {p['tail']}: {p['score']:.4f}")
    all_predictions['drug_target'] = drug_target_predictions

# 3. Disease-drug predictions (novel for v5)
print("\n" + "=" * 70)
print("3. DISEASE-DRUG PREDICTIONS (v5 novel)")
print("=" * 70)

treats_relation = None
for r in relation_to_id:
    if 'treats' in r.lower() or 'investigates' in r.lower():
        treats_relation = r
        break

if treats_relation and diseases:
    focus_diseases = []
    for d in diseases:
        if any(kw in d.lower() for kw in ['diabetes', 'cancer', 'heart', 'depression', 'alzheimer']):
            focus_diseases.append(d)
    focus_diseases = focus_diseases[:10]

    disease_drug_predictions = {}
    for disease in focus_diseases:
        preds = predict_tails(disease, treats_relation, drugs, top_k=10)
        if preds:
            disease_drug_predictions[disease] = preds
            print(f"\n{disease} → predicted drugs (top 3):")
            for p in preds[:3]:
                print(f"  {p['tail']}: {p['score']:.4f}")
    all_predictions['disease_drug'] = disease_drug_predictions
else:
    print(f"No treats relation found. Available: {list(relation_to_id.keys())}")

# 4. Sex-differential signal predictions
print("\n" + "=" * 70)
print("4. SEX-DIFFERENTIAL SIGNAL PREDICTIONS")
print("=" * 70)

sex_diff_relation = None
for r in relation_to_id:
    if 'sex_diff' in r.lower():
        sex_diff_relation = r
        break

if sex_diff_relation:
    sex_diff_predictions = {}
    high_interest = ['DRUG:SEMAGLUTIDE', 'DRUG:NIVOLUMAB', 'DRUG:PEMBROLIZUMAB',
                     'DRUG:TRASTUZUMAB', 'DRUG:RITUXIMAB', 'DRUG:DAPAGLIFLOZIN']
    for drug in high_interest:
        if drug in entity_to_id:
            preds = predict_tails(drug, sex_diff_relation, aes, top_k=20)
            if preds:
                sex_diff_predictions[drug] = preds
                print(f"\n{drug} → predicted sex-differential AEs (top 5):")
                for p in preds[:5]:
                    print(f"  {p['tail']}: {p['score']:.4f}")
    all_predictions['sex_differential'] = sex_diff_predictions

# Save all predictions
output = {
    'timestamp': datetime.now().isoformat(),
    'model': 'ComplEx v5',
    'kg': 'SexDiffKG v5 merged',
    'entities': len(entity_to_id),
    'relations': len(relation_to_id),
    'relation_types': list(relation_to_id.keys()),
    'existing_triples': len(existing_triples),
    'predictions': {}
}

for category, preds in all_predictions.items():
    output['predictions'][category] = {}
    for key, pred_list in preds.items():
        output['predictions'][category][key] = pred_list

with open(f"{out_dir}/link_predictions_v5.json", 'w') as f:
    json.dump(output, f, indent=2)

# Summary statistics
total_novel = sum(
    len([p for p in preds_list if not p.get('known', False)])
    for cat_preds in all_predictions.values()
    for preds_list in cat_preds.values()
)

print(f"\n{'=' * 70}")
print(f"SUMMARY")
print(f"Total novel predictions: {total_novel}")
print(f"Categories: {list(all_predictions.keys())}")
print(f"Output: {out_dir}/link_predictions_v5.json")
print(f"{'=' * 70}")
