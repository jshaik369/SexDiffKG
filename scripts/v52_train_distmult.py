#!/usr/bin/env python3
"""v52_train_distmult.py — Train DistMult embeddings on SexDiffKG v5.2

DistMult is simpler than ComplEx (real-valued, no complex tensors).
Benefits from different hyperparams: smaller dims, higher negs, moderate LR.

Phase 1: 3-trial mini-HPO (20 epochs each) to find best config
Phase 2: Full training (300 epochs + early stopping patience=10)

CRITICAL: Save model weights BEFORE evaluation extraction (crash protection).
CPU-only (GB10 GPU incompatible).
"""
import os
import sys
import json
import time
import shutil
import torch
import numpy as np
from datetime import datetime

# ── Paths ──────────────────────────────────────────────────────────────
BASE = "/home/jshaik369/sexdiffkg"
V52_DIR = f"{BASE}/data/kg_v5.2"
OUT_DIR = f"{BASE}/results/kg_embeddings_v5.2"
VAULT = "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg"
os.makedirs(OUT_DIR, exist_ok=True)

TRIPLES_PATH = f"{V52_DIR}/triples.tsv"
RESULTS_JSON = f"{OUT_DIR}/distmult_v52_results.json"
VAULT_JSON = f"{VAULT}/distmult_v52_results.json"
MODEL_PATH = f"{OUT_DIR}/distmult_v52_final.pt"

print("=" * 70)
print("DistMult v5.2 TRAINING")
print(f"Date: {datetime.now().isoformat()}")
print(f"Device: CPU (GB10 GPU incompatible)")
print(f"Torch: {torch.__version__}")
print(f"Triples: {TRIPLES_PATH}")
print(f"Output: {OUT_DIR}")
print("=" * 70)

# ── Validate input ─────────────────────────────────────────────────────
if not os.path.exists(TRIPLES_PATH):
    print(f"ERROR: {TRIPLES_PATH} not found.")
    print("Run the v5.2 bridge/rebuild script first.")
    sys.exit(1)

from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline

# ── [1/5] Load and split data ─────────────────────────────────────────
print("\n[1/5] Loading v5.2 triples...")
tf = TriplesFactory.from_path(
    TRIPLES_PATH,
    create_inverse_triples=True,
)
print(f"  Entities:  {tf.num_entities:,}")
print(f"  Relations: {tf.num_relations:,} (including inverse)")
print(f"  Triples:   {tf.num_triples:,} (including inverse)")

# 90/5/5 split
train, valid, test = tf.split([0.9, 0.05, 0.05], random_state=42)
print(f"  Train: {train.num_triples:,}")
print(f"  Valid: {valid.num_triples:,}")
print(f"  Test:  {test.num_triples:,}")

# Save split info and mappings
split_info = {
    "model": "DistMult",
    "kg_version": "v5.2",
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
with open(f"{OUT_DIR}/distmult_split_info.json", "w") as f:
    json.dump(split_info, f, indent=2)

with open(f"{OUT_DIR}/distmult_entity_to_id.json", "w") as f:
    json.dump(tf.entity_to_id, f)
with open(f"{OUT_DIR}/distmult_relation_to_id.json", "w") as f:
    json.dump(tf.relation_to_id, f)

# ── [2/5] Mini-HPO (3 trials, 20 epochs each) ─────────────────────────
print("\n[2/5] Running DistMult mini-HPO (3 trials, 20 epochs each)...")
print("  DistMult benefits from different hyperparams vs ComplEx:")
print("  - Real-valued embeddings (simpler, faster)")
print("  - Higher neg samples help more")
print("  - Moderate LR works well")

hpo_configs = [
    {"dim": 200, "lr": 0.001, "batch": 1024, "negs": 64},
    {"dim": 300, "lr": 0.001, "batch": 512,  "negs": 128},
    {"dim": 200, "lr": 0.003, "batch": 512,  "negs": 128},
]

best_mrr = -1
best_config = None
hpo_results_list = []
hpo_start = time.time()

for i, cfg in enumerate(hpo_configs):
    print(f"\n  Trial {i+1}/{len(hpo_configs)}: "
          f"dim={cfg['dim']}, lr={cfg['lr']}, "
          f"batch={cfg['batch']}, negs={cfg['negs']}")
    trial_start = time.time()

    try:
        r = pipeline(
            training=train,
            validation=valid,
            testing=test,
            model="DistMult",
            model_kwargs=dict(embedding_dim=cfg["dim"]),
            optimizer="Adam",
            optimizer_kwargs=dict(lr=cfg["lr"]),
            training_kwargs=dict(
                num_epochs=20,
                batch_size=cfg["batch"],
                use_tqdm=True,
            ),
            negative_sampler="basic",
            negative_sampler_kwargs=dict(num_negs_per_pos=cfg["negs"]),
            evaluator_kwargs=dict(filtered=True),
            random_seed=42,
            device="cpu",
        )

        metrics = r.metric_results.to_dict()
        mrr = metrics.get("both", {}).get("realistic", {}).get(
            "inverse_harmonic_mean_rank", 0)
        h10 = metrics.get("both", {}).get("realistic", {}).get(
            "hits_at_10", 0)
        trial_time = time.time() - trial_start

        print(f"    MRR: {mrr:.4f}, Hits@10: {h10:.4f} "
              f"({trial_time/60:.1f} min)")

        hpo_results_list.append({
            "trial": i + 1,
            "config": cfg,
            "mrr": float(mrr),
            "hits_at_10": float(h10),
            "time_min": round(trial_time / 60, 1),
        })

        if mrr > best_mrr:
            best_mrr = mrr
            best_config = cfg

    except Exception as e:
        trial_time = time.time() - trial_start
        print(f"    FAILED: {e}")
        hpo_results_list.append({
            "trial": i + 1,
            "config": cfg,
            "error": str(e),
            "time_min": round(trial_time / 60, 1),
        })

hpo_elapsed = time.time() - hpo_start

if best_config is None:
    print("\n  WARNING: All HPO trials failed! Using safe defaults...")
    best_config = {"dim": 200, "lr": 0.001, "batch": 1024, "negs": 64}
    best_mrr = None

print(f"\n  HPO complete in {hpo_elapsed/60:.1f} min")
print(f"  Best HPO MRR: {best_mrr}")
print(f"  Best config: {best_config}")

# Save HPO results
hpo_out = {
    "timestamp": datetime.now().isoformat(),
    "model": "DistMult",
    "kg_version": "v5.2",
    "n_trials": len(hpo_configs),
    "epochs_per_trial": 20,
    "time_min": round(hpo_elapsed / 60, 1),
    "best_mrr": float(best_mrr) if best_mrr and best_mrr > 0 else None,
    "best_config": best_config,
    "all_trials": hpo_results_list,
}
with open(f"{OUT_DIR}/distmult_hpo_results.json", "w") as f:
    json.dump(hpo_out, f, indent=2)
print(f"  HPO results saved: {OUT_DIR}/distmult_hpo_results.json")

# ── [3/5] Full training (300 epochs + early stopping) ─────────────────
print(f"\n[3/5] Full DistMult training (300 epochs + early stopping)...")
print(f"  Config: dim={best_config['dim']}, lr={best_config['lr']}, "
      f"batch={best_config['batch']}, negs={best_config['negs']}")
print(f"  Early stopping: patience=10, frequency=10, "
      f"relative_delta=0.001")
print(f"  Metric: both.realistic.inverse_harmonic_mean_rank")
print(f"  Checkpoints: every 50 epochs -> {OUT_DIR}/")

train_start = time.time()

result = pipeline(
    training=train,
    validation=valid,
    testing=test,
    model="DistMult",
    model_kwargs=dict(
        embedding_dim=best_config["dim"],
    ),
    optimizer="Adam",
    optimizer_kwargs=dict(
        lr=best_config["lr"],
    ),
    training_kwargs=dict(
        num_epochs=300,
        batch_size=best_config["batch"],
        use_tqdm=True,
        checkpoint_name="distmult_v52_checkpoint.pt",
        checkpoint_directory=OUT_DIR,
        checkpoint_frequency=50,
    ),
    negative_sampler="basic",
    negative_sampler_kwargs=dict(
        num_negs_per_pos=best_config["negs"],
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
print(f"\n  Training complete in {train_elapsed/60:.1f} min")

# ── [4/5] Save model BEFORE evaluation extraction (crash protection) ──
print(f"\n[4/5] Saving model weights (crash protection)...")
torch.save({
    "model_state_dict": result.model.state_dict(),
    "entity_to_id": dict(train.entity_to_id),
    "relation_to_id": dict(train.relation_to_id),
    "best_hpo_config": best_config,
    "kg_version": "v5.2",
    "model_name": "DistMult",
    "timestamp": datetime.now().isoformat(),
}, MODEL_PATH)
print(f"  Model saved: {MODEL_PATH}")

# Also save full pipeline result
result.save_to_directory(f"{OUT_DIR}/distmult_v52_pipeline")
print(f"  Pipeline saved: {OUT_DIR}/distmult_v52_pipeline/")

# ── [5/5] Extract results ─────────────────────────────────────────────
print(f"\n[5/5] Extracting results...")

metrics = result.metric_results.to_dict()
mrr = metrics.get("both", {}).get("realistic", {}).get(
    "inverse_harmonic_mean_rank", None)
h1 = metrics.get("both", {}).get("realistic", {}).get(
    "hits_at_1", None)
h3 = metrics.get("both", {}).get("realistic", {}).get(
    "hits_at_3", None)
h5 = metrics.get("both", {}).get("realistic", {}).get(
    "hits_at_5", None)
h10 = metrics.get("both", {}).get("realistic", {}).get(
    "hits_at_10", None)
amri = metrics.get("both", {}).get("realistic", {}).get(
    "adjusted_arithmetic_mean_rank_index", None)

# Fallback metric extraction if primary keys are None
if mrr is None:
    print("  WARNING: Primary metric keys returned None. Scanning all keys...")
    for side_key, side_val in metrics.items():
        if not isinstance(side_val, dict):
            continue
        for setting_key, setting_val in side_val.items():
            if not isinstance(setting_val, dict):
                continue
            for metric_key, metric_val in setting_val.items():
                if metric_val and isinstance(metric_val, (int, float)):
                    if "harmonic" in metric_key and mrr is None:
                        mrr = metric_val
                    elif "hits_at_1" == metric_key and h1 is None:
                        h1 = metric_val
                    elif "hits_at_3" == metric_key and h3 is None:
                        h3 = metric_val
                    elif "hits_at_5" == metric_key and h5 is None:
                        h5 = metric_val
                    elif "hits_at_10" == metric_key and h10 is None:
                        h10 = metric_val
                    elif "adjusted" in metric_key and "arithmetic" in metric_key and amri is None:
                        amri = metric_val

print(f"\n{'=' * 70}")
print("DistMult v5.2 RESULTS")
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

# ── Baselines comparison ──────────────────────────────────────────────
print(f"\n  Baselines:")
print(f"    DistMult v4.1: MRR 0.1013, Hits@10 19.61%")
print(f"    DistMult v5:   MRR 0.0413, Hits@10 7.78%")
print(f"    ComplEx v4:    MRR 0.2484, Hits@10 40.69%")
if mrr is not None:
    v41_change = (mrr - 0.1013) / 0.1013 * 100
    v5_change = (mrr - 0.0413) / 0.0413 * 100 if 0.0413 > 0 else 0
    print(f"    v5.2 DistMult vs v4.1 DistMult: {v41_change:+.1f}%")
    print(f"    v5.2 DistMult vs v5 DistMult:   {v5_change:+.1f}%")
if h10 is not None:
    h10_pct = h10 * 100
    h10_v41_delta = h10_pct - 19.61
    h10_v5_delta = h10_pct - 7.78
    print(f"    Hits@10 vs v4.1: {h10_v41_delta:+.2f}pp")
    print(f"    Hits@10 vs v5:   {h10_v5_delta:+.2f}pp")

# ── Save full results JSON ────────────────────────────────────────────
final_results = {
    "timestamp": datetime.now().isoformat(),
    "model": "DistMult",
    "kg_version": "v5.2",
    "entities": int(tf.num_entities),
    "relations": int(tf.num_relations),
    "total_triples": int(tf.num_triples),
    "train_triples": int(train.num_triples),
    "valid_triples": int(valid.num_triples),
    "test_triples": int(test.num_triples),
    "inverse_triples": True,
    "split_ratios": [0.9, 0.05, 0.05],
    "hyperparameters": {
        "embedding_dim": best_config["dim"],
        "learning_rate": best_config["lr"],
        "batch_size": best_config["batch"],
        "num_negs_per_pos": best_config["negs"],
        "optimizer": "Adam",
        "negative_sampler": "basic",
        "max_epochs": 300,
        "early_stopping": True,
        "early_stopping_patience": 10,
        "early_stopping_frequency": 10,
        "early_stopping_relative_delta": 0.001,
        "early_stopping_metric": "both.realistic.inverse_harmonic_mean_rank",
        "checkpoint_frequency": 50,
    },
    "hpo": {
        "n_trials": len(hpo_configs),
        "epochs_per_trial": 20,
        "best_hpo_mrr": float(best_mrr) if best_mrr and best_mrr > 0 else None,
        "best_config": best_config,
        "time_min": round(hpo_elapsed / 60, 1),
        "all_trials": hpo_results_list,
    },
    "results": {
        "mrr": float(mrr) if mrr is not None else None,
        "hits_at_1": float(h1) if h1 is not None else None,
        "hits_at_3": float(h3) if h3 is not None else None,
        "hits_at_5": float(h5) if h5 is not None else None,
        "hits_at_10": float(h10) if h10 is not None else None,
        "amri": float(amri) if amri is not None else None,
    },
    "baselines": {
        "distmult_v4.1": {"mrr": 0.1013, "hits_at_10": 0.1961},
        "distmult_v5": {"mrr": 0.0413, "hits_at_10": 0.0778},
        "complex_v4": {"mrr": 0.2484, "hits_at_10": 0.4069},
    },
    "training_time_min": round(train_elapsed / 60, 1),
    "hpo_time_min": round(hpo_elapsed / 60, 1),
    "total_time_min": round((hpo_elapsed + train_elapsed) / 60, 1),
    "device": "cpu",
    "random_seed": 42,
    "torch_version": torch.__version__,
    "model_path": MODEL_PATH,
    "full_metrics": metrics,
}

with open(RESULTS_JSON, "w") as f:
    json.dump(final_results, f, indent=2, default=str)
print(f"\n  Results saved: {RESULTS_JSON}")

# Vault copy
try:
    os.makedirs(os.path.dirname(VAULT_JSON), exist_ok=True)
    with open(VAULT_JSON, "w") as f:
        json.dump(final_results, f, indent=2, default=str)
    print(f"  Vault copy:  {VAULT_JSON}")
except Exception as e:
    print(f"  WARNING: Vault copy failed: {e}")

# ── Extract and save entity embeddings ────────────────────────────────
print("\n  Extracting entity embeddings...")
try:
    model = result.model
    state = model.state_dict()
    # PyKEEN stores entity embeddings under this key
    emb_key = None
    for k in state.keys():
        if "entity" in k and "embedding" in k.lower():
            emb_key = k
            break
    if emb_key is None:
        # Fallback: look for any key with 'entity_representations'
        for k in state.keys():
            if "entity_representations" in k:
                emb_key = k
                break

    if emb_key is not None:
        embeddings = state[emb_key].cpu().numpy()
        emb_path = f"{OUT_DIR}/distmult_entity_embeddings.npy"
        np.save(emb_path, embeddings)
        print(f"  Entity embeddings saved: {emb_path} (shape: {embeddings.shape})")
    else:
        print(f"  WARNING: Could not find entity embedding key in state_dict.")
        print(f"  Available keys: {list(state.keys())}")
except Exception as e:
    print(f"  WARNING: Embedding extraction failed: {e}")

# ── Summary ───────────────────────────────────────────────────────────
print(f"\n{'=' * 70}")
print("TRAINING COMPLETE")
print(f"{'=' * 70}")
print(f"  Model:     DistMult v5.2")
print(f"  MRR:       {mrr}")
print(f"  Hits@10:   {h10}")
print(f"  HPO:       {hpo_elapsed/60:.1f} min ({len(hpo_configs)} trials)")
print(f"  Training:  {train_elapsed/60:.1f} min")
print(f"  Total:     {(hpo_elapsed + train_elapsed)/60:.1f} min")
print(f"  Saved to:  {OUT_DIR}/")
print(f"  Completed: {datetime.now().isoformat()}")
