#!/usr/bin/env python3
"""Train DistMult on v5 merged KG.
Run AFTER ComplEx v5 finishes (they share CPU resources).
DistMult is simpler than ComplEx — uses real embeddings, no complex tensors.
Should train faster and serve as comparison baseline.
"""
import torch
import json
import os
import time
import numpy as np
from datetime import datetime
from pykeen.triples import TriplesFactory
from pykeen.models import DistMult
from pykeen.training import SLCWATrainingLoop
from pykeen.losses import MarginRankingLoss
from pykeen.evaluation import RankBasedEvaluator
from pykeen.pipeline import pipeline

base = "/home/jshaik369/sexdiffkg"
triples_path = f"{base}/data/kg_v5/triples.tsv"
out_dir = f"{base}/results/kg_embeddings_v5_distmult"
os.makedirs(out_dir, exist_ok=True)

print("=" * 70)
print("DistMult v5 TRAINING")
print(f"Date: {datetime.now().isoformat()}")
print(f"Triples: {triples_path}")
print(f"Output: {out_dir}")
print("=" * 70)

# Load triples
print("\nLoading triples...")
tf = TriplesFactory.from_path(
    triples_path,
    create_inverse_triples=False,
)
print(f"Entities: {tf.num_entities:,}")
print(f"Relations: {tf.num_relations:,}")
print(f"Triples: {tf.num_triples:,}")

# Save mappings
with open(f"{out_dir}/entity_to_id.json", 'w') as f:
    json.dump(tf.entity_to_id, f)
with open(f"{out_dir}/relation_to_id.json", 'w') as f:
    json.dump(tf.relation_to_id, f)

# Train/test split
train, test = tf.split([0.9, 0.1], random_state=42)
print(f"Train: {train.num_triples:,}")
print(f"Test: {test.num_triples:,}")

# Train
print("\nStarting DistMult training...")
start = time.time()

result = pipeline(
    training=train,
    testing=test,
    model='DistMult',
    model_kwargs=dict(
        embedding_dim=200,
    ),
    training_kwargs=dict(
        num_epochs=100,
        batch_size=4096,
        checkpoint_name='distmult_v5_checkpoint.pt',
        checkpoint_directory=out_dir,
        checkpoint_frequency=6,
    ),
    optimizer_kwargs=dict(lr=0.001),
    device='cpu',
    random_seed=42,
)

elapsed = time.time() - start
print(f"\nTraining complete in {elapsed/60:.1f} minutes")

# Extract metrics
metrics = result.metric_results.to_dict()
mrr = metrics.get('both', {}).get('realistic', {}).get('inverse_harmonic_mean_rank', None)
h1 = metrics.get('both', {}).get('realistic', {}).get('hits_at_1', None)
h10 = metrics.get('both', {}).get('realistic', {}).get('hits_at_10', None)
amri = metrics.get('both', {}).get('realistic', {}).get('adjusted_arithmetic_mean_rank_index', None)

print(f"\nDistMult v5 Results:")
print(f"  MRR:    {mrr}")
print(f"  Hits@1: {h1}")
print(f"  Hits@10: {h10}")
print(f"  AMRI:   {amri}")

# Save model
model_path = f"{out_dir}/distmult_v5_final.pt"
torch.save(result.model.state_dict(), model_path)
print(f"Model saved: {model_path}")

# Save results
results = {
    'timestamp': datetime.now().isoformat(),
    'model': 'DistMult v5',
    'kg': 'SexDiffKG v5 merged',
    'entities': int(tf.num_entities),
    'relations': int(tf.num_relations),
    'triples': int(tf.num_triples),
    'train_triples': int(train.num_triples),
    'test_triples': int(test.num_triples),
    'embedding_dim': 200,
    'epochs': 100,
    'batch_size': 4096,
    'lr': 0.001,
    'training_time_min': round(elapsed / 60, 1),
    'mrr': float(mrr) if mrr else None,
    'hits_at_1': float(h1) if h1 else None,
    'hits_at_10': float(h10) if h10 else None,
    'amri': float(amri) if amri else None,
}

with open(f"{out_dir}/distmult_v5_results.json", 'w') as f:
    json.dump(results, f, indent=2)

# Compare with v4
print(f"\n{'=' * 70}")
print("COMPARISON WITH v4:")
print(f"  DistMult v4.1: MRR 0.1013, Hits@10 19.61%")
print(f"  DistMult v5:   MRR {mrr:.4f}, Hits@10 {h10*100:.2f}%")
print(f"  ComplEx v4:    MRR 0.2484, Hits@10 40.69%")
print(f"{'=' * 70}")
