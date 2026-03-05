#!/usr/bin/env python3
"""v5_04_train_complex.py — Train ComplEx embeddings on SexDiffKG v5
CPU-only (GB10 GPU incompatible with complex tensor kernels).
"""
import os
import json
import time
import torch
import numpy as np
from datetime import datetime

base = "/home/jshaik369/sexdiffkg"
v5_dir = f"{base}/data/kg_v5"
out_dir = f"{base}/results/kg_embeddings_v5"
os.makedirs(out_dir, exist_ok=True)

print(f"=== ComplEx Training on SexDiffKG v5 ===")
print(f"Started: {datetime.now().isoformat()}")
print(f"Device: CPU (GB10 GPU incompatible with complex tensors)")
print(f"Torch: {torch.__version__}")

# Force CPU
device = 'cpu'

# Load triples
print("\nLoading triples...")
from pykeen.triples import TriplesFactory

tf = TriplesFactory.from_path(
    f"{v5_dir}/triples.tsv",
    create_inverse_triples=False,
)
print(f"Entities: {tf.num_entities:,}")
print(f"Relations: {tf.num_relations:,}")
print(f"Triples: {tf.num_triples:,}")

# Train/test split (80/20, same seed as v4 for comparability)
train, test = tf.split([0.8, 0.2], random_state=42)
print(f"Train: {train.num_triples:,}")
print(f"Test: {test.num_triples:,}")

# Save entity/relation mappings
with open(f"{out_dir}/entity_to_id.json", 'w') as f:
    json.dump(tf.entity_to_id, f)
with open(f"{out_dir}/relation_to_id.json", 'w') as f:
    json.dump(tf.relation_to_id, f)

# Train ComplEx
print(f"\nTraining ComplEx (200d, 100 epochs)...")
from pykeen.pipeline import pipeline

start = time.time()
result = pipeline(
    training=train,
    testing=test,
    model='ComplEx',
    model_kwargs={'embedding_dim': 200},
    optimizer='Adam',
    optimizer_kwargs={'lr': 0.001},
    training_kwargs={
        'num_epochs': 100,
        'batch_size': 4096,
        'checkpoint_name': 'complex_v5_checkpoint.pt',
        'checkpoint_directory': out_dir,
        'checkpoint_frequency': 10,
    },
    evaluator_kwargs={'batch_size': 2048},
    random_seed=42,
    device=device,
)
elapsed = time.time() - start

print(f"\nTraining completed in {elapsed/60:.1f} minutes")

# Save model
print("Saving model...")
result.save_to_directory(out_dir)

# Extract metrics
metrics = result.metric_results.to_dict()
mrr = metrics.get('both', {}).get('realistic', {}).get('inverse_harmonic_mean_rank', 0)
h1 = metrics.get('both', {}).get('realistic', {}).get('hits_at_1', 0)
h10 = metrics.get('both', {}).get('realistic', {}).get('hits_at_10', 0)
amri = metrics.get('both', {}).get('realistic', {}).get('adjusted_arithmetic_mean_rank_index', 0)

# Try alternate metric keys if needed
if mrr == 0:
    for k, v in metrics.items():
        if isinstance(v, dict):
            for k2, v2 in v.items():
                if isinstance(v2, dict):
                    for k3, v3 in v2.items():
                        if 'harmonic' in k3 and v3 > 0:
                            mrr = v3
                        elif 'hits_at_1' in k3 and v3 > 0:
                            h1 = v3
                        elif 'hits_at_10' in k3 and v3 > 0:
                            h10 = v3
                        elif 'adjusted' in k3 and 'arithmetic' in k3 and v3 > 0:
                            amri = v3

print(f"\n=== Results ===")
print(f"MRR:     {mrr:.4f}")
print(f"Hits@1:  {h1:.4f}")
print(f"Hits@10: {h10:.4f}")
print(f"AMRI:    {amri:.4f}")
print(f"Time:    {elapsed/60:.1f} min")

# Compare with v4
v4_mrr = 0.2484
print(f"\nv4 ComplEx MRR: {v4_mrr:.4f}")
print(f"v5 ComplEx MRR: {mrr:.4f}")
print(f"Delta: {mrr - v4_mrr:+.4f}")

# Save summary
summary = {
    'model': 'ComplEx',
    'version': 'v5',
    'embedding_dim': 200,
    'epochs': 100,
    'entities': tf.num_entities,
    'relations': tf.num_relations,
    'triples': tf.num_triples,
    'train_triples': train.num_triples,
    'test_triples': test.num_triples,
    'mrr': float(mrr),
    'hits_at_1': float(h1),
    'hits_at_10': float(h10),
    'amri': float(amri),
    'training_time_minutes': round(elapsed/60, 1),
    'v4_comparison': {
        'v4_mrr': v4_mrr,
        'delta': round(float(mrr) - v4_mrr, 4),
    },
    'device': device,
    'timestamp': datetime.now().isoformat(),
    'random_seed': 42,
    'full_metrics': metrics,
}

with open(f"{out_dir}/training_summary.json", 'w') as f:
    json.dump(summary, f, indent=2, default=str)

# Extract embeddings
print("\nExtracting embeddings...")
model = result.model
state = model.state_dict()
emb_key = [k for k in state.keys() if 'entity' in k and 'embedding' in k.lower()][0]
embeddings = state[emb_key].cpu().numpy()
np.save(f"{out_dir}/entity_embeddings.npy", embeddings)
print(f"Saved entity embeddings: {embeddings.shape}")

print(f"\nCompleted: {datetime.now().isoformat()}")
print(f"Results saved to: {out_dir}/")
