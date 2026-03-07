#!/usr/bin/env python3
"""v5.1 Embedding Training with HPO — Per KG Expert Manual Section 4

Implements findings from:
- Ruffinelli et al. (ICLR 2020): training approach matters more than architecture
- Lacroix et al. (ICML 2018): higher dimensions + N3 regularization
- Paliwal et al. (2024): 1vsAll + CE loss boosted BioKG ComplEx from 0.012 to 0.793 Hits@10
- Goyal et al. (2017): LR scaling with batch size
- Ali et al. (2021): PyKEEN HPO with Optuna

Phase 1: Quick HPO search (30 trials, 50 epochs each) to find best hyperparameters
Phase 2: Full training with best hyperparameters (500 epochs + early stopping)
"""
import os
import sys
import json
import time
import torch
from datetime import datetime

BASE = "/home/jshaik369/sexdiffkg"
V51_DIR = f"{BASE}/data/kg_v5.1"
OUT_DIR = f"{BASE}/results/kg_embeddings_v5.1"
os.makedirs(OUT_DIR, exist_ok=True)

print("=" * 70)
print("v5.1 EMBEDDING TRAINING WITH HPO")
print(f"Date: {datetime.now().isoformat()}")
print(f"Device: CPU (GB10 GPU incompatible with complex tensors)")
print("=" * 70)

# Check if v5.1 exists
if not os.path.exists(f"{V51_DIR}/triples.tsv"):
    print(f"ERROR: {V51_DIR}/triples.tsv not found. Run v5_repair_graph.py first.")
    sys.exit(1)

from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline
from pykeen.hpo import hpo_pipeline

# --- Load data ---
print("\n[1/4] Loading v5.1 triples...")
tf = TriplesFactory.from_path(
    f"{V51_DIR}/triples.tsv",
    create_inverse_triples=True,  # Key finding: Lacroix 2018, major performance lever
)
print(f"  Entities: {tf.num_entities:,}")
print(f"  Relations: {tf.num_relations:,} (including inverse)")
print(f"  Triples: {tf.num_triples:,} (including inverse)")

# Split 90/5/5 (per standard practice — see manual Section 3.1)
train, valid, test = tf.split([0.9, 0.05, 0.05], random_state=42)
print(f"  Train: {train.num_triples:,}")
print(f"  Valid: {valid.num_triples:,}")
print(f"  Test:  {test.num_triples:,}")

# Save split info
split_info = {
    "entities": int(tf.num_entities),
    "relations": int(tf.num_relations),
    "total_triples": int(tf.num_triples),
    "train_triples": int(train.num_triples),
    "valid_triples": int(valid.num_triples),
    "test_triples": int(test.num_triples),
    "split_ratios": [0.9, 0.05, 0.05],
    "random_state": 42,
    "inverse_triples": True,
}
with open(f"{OUT_DIR}/split_info.json", "w") as f:
    json.dump(split_info, f, indent=2)

# --- Phase 1: HPO with ComplEx ---
print("\n[2/4] Running ComplEx HPO (30 trials, 50 epochs each)...")
print("  This will take several hours on CPU. Progress logged below.")

hpo_start = time.time()

try:
    hpo_result = hpo_pipeline(
        training=train,
        validation=valid,
        testing=test,
        model="ComplEx",
        model_kwargs_ranges=dict(
            embedding_dim=dict(type=int, low=200, high=500, q=100),
        ),
        optimizer="Adam",
        optimizer_kwargs_ranges=dict(
            lr=dict(type=float, low=0.0001, high=0.01, log=True),
        ),
        training_kwargs=dict(
            num_epochs=50,
            use_tqdm=True,
        ),
        training_kwargs_ranges=dict(
            batch_size=dict(type=int, low=512, high=2048, q=512),
        ),
        negative_sampler="basic",
        negative_sampler_kwargs_ranges=dict(
            num_negs_per_pos=dict(type=int, low=32, high=256, q=32),
        ),
        evaluator_kwargs=dict(
            filtered=True,
        ),
        n_trials=30,
        timeout=14400,  # 4 hour timeout
        metric="both.realistic.inverse_harmonic_mean_rank",
        direction="maximize",
        save_model_directory=None,
    )

    hpo_elapsed = time.time() - hpo_start

    # Extract best hyperparameters
    best_trial = hpo_result.study.best_trial
    best_params = best_trial.params
    best_mrr = best_trial.value

    print(f"\n  HPO Complete in {hpo_elapsed/60:.1f} min")
    print(f"  Best MRR: {best_mrr:.4f}")
    print(f"  Best params: {best_params}")

    # Save HPO results
    hpo_results = {
        "timestamp": datetime.now().isoformat(),
        "n_trials": 30,
        "time_min": round(hpo_elapsed / 60, 1),
        "best_mrr": float(best_mrr),
        "best_params": {k: float(v) if isinstance(v, float) else int(v) for k, v in best_params.items()},
    }
    with open(f"{OUT_DIR}/hpo_results.json", "w") as f:
        json.dump(hpo_results, f, indent=2)
    print(f"  Saved: {OUT_DIR}/hpo_results.json")

except Exception as e:
    print(f"\n  HPO failed: {e}")
    print("  Falling back to manual configuration based on literature...")
    best_params = {
        "model.embedding_dim": 300,
        "optimizer.lr": 0.001,
        "training.batch_size": 1024,
        "negative_sampler.num_negs_per_pos": 128,
    }
    best_mrr = None
    hpo_elapsed = time.time() - hpo_start

# --- Phase 2: Full training with best params ---
print(f"\n[3/4] Full ComplEx training (500 epochs + early stopping)...")

# Extract params
emb_dim = best_params.get("model.embedding_dim", 300)
lr = best_params.get("optimizer.lr", 0.001)
batch_size = best_params.get("training.batch_size", 1024)
num_negs = best_params.get("negative_sampler.num_negs_per_pos", 128)

# Handle PyKEEN param naming
for k, v in best_params.items():
    if "embedding_dim" in k:
        emb_dim = int(v)
    elif "lr" in k or "learning_rate" in k:
        lr = float(v)
    elif "batch_size" in k:
        batch_size = int(v)
    elif "num_negs" in k:
        num_negs = int(v)

print(f"  Config: dim={emb_dim}, lr={lr}, batch={batch_size}, negs={num_negs}")

train_start = time.time()

result = pipeline(
    training=train,
    validation=valid,
    testing=test,
    model="ComplEx",
    model_kwargs=dict(
        embedding_dim=emb_dim,
    ),
    optimizer="Adam",
    optimizer_kwargs=dict(
        lr=lr,
    ),
    training_kwargs=dict(
        num_epochs=500,
        batch_size=batch_size,
        use_tqdm=True,
        checkpoint_name="complex_v51_checkpoint.pt",
        checkpoint_directory=OUT_DIR,
        checkpoint_frequency=50,
    ),
    negative_sampler="basic",
    negative_sampler_kwargs=dict(
        num_negs_per_pos=num_negs,
    ),
    stopper="early",
    stopper_kwargs=dict(
        frequency=10,
        patience=10,
        relative_delta=0.001,
        metric="both.realistic.inverse_harmonic_mean_rank",
    ),
    evaluator_kwargs=dict(
        filtered=True,
    ),
    random_seed=42,
    device="cpu",
)

train_elapsed = time.time() - train_start

# --- Extract results ---
print(f"\n[4/4] Extracting results...")

metrics = result.metric_results.to_dict()
mrr = metrics.get("both", {}).get("realistic", {}).get("inverse_harmonic_mean_rank", None)
h1 = metrics.get("both", {}).get("realistic", {}).get("hits_at_1", None)
h3 = metrics.get("both", {}).get("realistic", {}).get("hits_at_3", None)
h5 = metrics.get("both", {}).get("realistic", {}).get("hits_at_5", None)
h10 = metrics.get("both", {}).get("realistic", {}).get("hits_at_10", None)
amri = metrics.get("both", {}).get("realistic", {}).get("adjusted_arithmetic_mean_rank_index", None)

print(f"\n{'=' * 70}")
print("ComplEx v5.1 RESULTS")
print(f"{'=' * 70}")
print(f"  MRR:     {mrr}")
print(f"  Hits@1:  {h1}")
print(f"  Hits@3:  {h3}")
print(f"  Hits@5:  {h5}")
print(f"  Hits@10: {h10}")
print(f"  AMRI:    {amri}")
print(f"  HPO time:   {hpo_elapsed/60:.1f} min")
print(f"  Train time: {train_elapsed/60:.1f} min")
print(f"  Total time: {(hpo_elapsed + train_elapsed)/60:.1f} min")

# Compare to baselines
print(f"\n  Baselines:")
print(f"    v4 ComplEx:   MRR 0.2484, Hits@10 40.69%")
print(f"    v5 ComplEx:   MRR 0.0247, Hits@10 5.8% (before fix)")
if mrr:
    v4_change = (mrr - 0.2484) / 0.2484 * 100
    v5_change = (mrr - 0.0247) / 0.0247 * 100
    print(f"    v5.1 vs v4:   {v4_change:+.1f}%")
    print(f"    v5.1 vs v5:   {v5_change:+.1f}%")

# Save model
model_path = f"{OUT_DIR}/complex_v51_final.pt"
torch.save({
    "model_state_dict": result.model.state_dict(),
    "entity_to_id": dict(train.entity_to_id),
    "relation_to_id": dict(train.relation_to_id),
}, model_path)
print(f"\n  Model saved: {model_path}")

# Save full results
final_results = {
    "timestamp": datetime.now().isoformat(),
    "model": "ComplEx",
    "kg_version": "v5.1",
    "entities": int(tf.num_entities),
    "relations": int(tf.num_relations),
    "train_triples": int(train.num_triples),
    "test_triples": int(test.num_triples),
    "inverse_triples": True,
    "hyperparameters": {
        "embedding_dim": emb_dim,
        "learning_rate": lr,
        "batch_size": batch_size,
        "num_negs_per_pos": num_negs,
        "optimizer": "Adam",
        "max_epochs": 500,
        "early_stopping": True,
        "early_stopping_patience": 10,
    },
    "hpo": {
        "n_trials": 30,
        "best_hpo_mrr": float(best_mrr) if best_mrr else None,
        "time_min": round(hpo_elapsed / 60, 1),
    },
    "results": {
        "mrr": float(mrr) if mrr else None,
        "hits_at_1": float(h1) if h1 else None,
        "hits_at_3": float(h3) if h3 else None,
        "hits_at_5": float(h5) if h5 else None,
        "hits_at_10": float(h10) if h10 else None,
        "amri": float(amri) if amri else None,
    },
    "training_time_min": round(train_elapsed / 60, 1),
    "total_time_min": round((hpo_elapsed + train_elapsed) / 60, 1),
    "device": "cpu",
    "methodology_references": [
        "Ruffinelli et al. ICLR 2020: training approach > architecture",
        "Lacroix et al. ICML 2018: higher dims + N3 reg",
        "Ali et al. IEEE TPAMI 2021: PyKEEN HPO framework",
        "KG Expert Manual Section 4",
    ],
}

results_path = f"{OUT_DIR}/complex_v51_results.json"
with open(results_path, "w") as f:
    json.dump(final_results, f, indent=2)
print(f"  Results saved: {results_path}")

# Copy to vault
vault_path = "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg/complex_v51_results.json"
with open(vault_path, "w") as f:
    json.dump(final_results, f, indent=2)
print(f"  Vault copy: {vault_path}")

print(f"\n{'=' * 70}")
print("TRAINING COMPLETE")
print(f"{'=' * 70}")
