#!/usr/bin/env python3
"""Train DistMult embeddings on all 5 derived KGs.
Runs sequentially through each KG since CPU-bound.
"""
import torch
import json
import os
import time
import numpy as np
from datetime import datetime
from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline

base = "/home/jshaik369"

DERIVED_KGS = {
    'reproductkg': {
        'name': 'REPRODUCT-KG',
        'path': f'{base}/reproductkg',
        'triples': f'{base}/reproductkg/data/kg/triples.tsv',
        'out': f'{base}/reproductkg/results/embeddings',
    },
    'mentalhealthkg': {
        'name': 'MENTALHEALTH-KG',
        'path': f'{base}/mentalhealthkg',
        'triples': f'{base}/mentalhealthkg/data/kg/triples.tsv',
        'out': f'{base}/mentalhealthkg/results/embeddings',
    },
    'geripharmkg': {
        'name': 'GERIPHARM-KG',
        'path': f'{base}/geripharmkg',
        'triples': f'{base}/geripharmkg/data/kg/triples.tsv',
        'out': f'{base}/geripharmkg/results/embeddings',
    },
    'pcosendokg': {
        'name': 'PCOS-ENDO-KG',
        'path': f'{base}/pcosendokg',
        'triples': f'{base}/pcosendokg/data/kg/triples.tsv',
        'out': f'{base}/pcosendokg/results/embeddings',
    },
    'ayurpharmakg': {
        'name': 'AYUR-PHARMA-KG',
        'path': f'{base}/ayurpharmakg',
        'triples': f'{base}/ayurpharmakg/data/kg/triples.tsv',
        'out': f'{base}/ayurpharmakg/results/embeddings',
    },
}

print("=" * 70)
print("DERIVED KG EMBEDDING TRAINING")
print(f"Date: {datetime.now().isoformat()}")
print(f"KGs: {len(DERIVED_KGS)}")
print("=" * 70)

all_results = {}

for kg_id, config in DERIVED_KGS.items():
    print(f"\n{'=' * 70}")
    print(f"TRAINING: {config['name']}")
    print(f"{'=' * 70}")

    triples_path = config['triples']
    out_dir = config['out']

    if not os.path.exists(triples_path):
        print(f"SKIP: {triples_path} not found")
        continue

    os.makedirs(out_dir, exist_ok=True)

    # Load triples
    print(f"Loading {triples_path}...")
    tf = TriplesFactory.from_path(triples_path, create_inverse_triples=False)
    print(f"  Entities: {tf.num_entities:,}")
    print(f"  Relations: {tf.num_relations:,}")
    print(f"  Triples: {tf.num_triples:,}")

    # Save mappings
    with open(f"{out_dir}/entity_to_id.json", 'w') as f:
        json.dump(tf.entity_to_id, f)
    with open(f"{out_dir}/relation_to_id.json", 'w') as f:
        json.dump(tf.relation_to_id, f)

    # Split
    train, test = tf.split([0.9, 0.1], random_state=42)
    print(f"  Train: {train.num_triples:,} / Test: {test.num_triples:,}")

    # Train DistMult (faster, good baseline)
    start = time.time()
    result = pipeline(
        training=train,
        testing=test,
        model='DistMult',
        model_kwargs=dict(embedding_dim=200),
        training_kwargs=dict(
            num_epochs=100,
            batch_size=4096,
            checkpoint_name=f'{kg_id}_checkpoint.pt',
            checkpoint_directory=out_dir,
            checkpoint_frequency=10,
        ),
        optimizer_kwargs=dict(lr=0.001),
        device='cpu',
        random_seed=42,
    )
    elapsed = time.time() - start

    # Extract metrics
    metrics = result.metric_results.to_dict()
    mrr = metrics.get('both', {}).get('realistic', {}).get('inverse_harmonic_mean_rank', None)
    h1 = metrics.get('both', {}).get('realistic', {}).get('hits_at_1', None)
    h10 = metrics.get('both', {}).get('realistic', {}).get('hits_at_10', None)
    amri = metrics.get('both', {}).get('realistic', {}).get('adjusted_arithmetic_mean_rank_index', None)

    print(f"\n{config['name']} DistMult Results:")
    print(f"  MRR:    {mrr}")
    print(f"  Hits@1: {h1}")
    print(f"  Hits@10: {h10}")
    print(f"  AMRI:   {amri}")
    print(f"  Time:   {elapsed/60:.1f} min")

    # Save model
    model_path = f"{out_dir}/distmult_model.pt"
    torch.save(result.model.state_dict(), model_path)
    print(f"  Model saved: {model_path}")

    # Save results
    kg_results = {
        'timestamp': datetime.now().isoformat(),
        'kg': config['name'],
        'model': 'DistMult',
        'entities': int(tf.num_entities),
        'relations': int(tf.num_relations),
        'triples': int(tf.num_triples),
        'train_triples': int(train.num_triples),
        'test_triples': int(test.num_triples),
        'embedding_dim': 200,
        'epochs': 100,
        'batch_size': 4096,
        'training_time_min': round(elapsed / 60, 1),
        'mrr': float(mrr) if mrr else None,
        'hits_at_1': float(h1) if h1 else None,
        'hits_at_10': float(h10) if h10 else None,
        'amri': float(amri) if amri else None,
    }

    with open(f"{out_dir}/distmult_results.json", 'w') as f:
        json.dump(kg_results, f, indent=2)

    all_results[kg_id] = kg_results

    # Update GROUND_TRUTH.json
    gt_path = f"{config['path']}/GROUND_TRUTH.json"
    if os.path.exists(gt_path):
        with open(gt_path) as f:
            gt = json.load(f)
        gt['embeddings'] = {
            'model': 'DistMult',
            'mrr': float(mrr) if mrr else None,
            'hits_at_10': float(h10) if h10 else None,
            'amri': float(amri) if amri else None,
        }
        with open(gt_path, 'w') as f:
            json.dump(gt, f, indent=2)

# Summary
print(f"\n{'=' * 70}")
print("TRAINING SUMMARY")
print(f"{'=' * 70}")
for kg_id, res in all_results.items():
    print(f"  {res['kg']:20s}: MRR {res['mrr']:.4f}, Hits@10 {res['hits_at_10']*100:.1f}%, "
          f"{res['training_time_min']:.0f} min")

with open(f"{base}/sexdiffkg/results/derived_kg_embeddings_summary.json", 'w') as f:
    json.dump(all_results, f, indent=2)

print(f"\nAll results saved to: {base}/sexdiffkg/results/derived_kg_embeddings_summary.json")
