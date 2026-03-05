#!/usr/bin/env python3
"""v5.2 ALL MODEL TRAINING — Fast, No HPO, Literature-backed Defaults

HPO is infeasible on CPU for 3.2M triples (~26 min/epoch = 65+ hours for 5 trials).
Instead: use literature-backed defaults and train directly with early stopping.

Models: ComplEx, DistMult, RotatE (sequential — all use complex/real tensors on CPU)

Key refs applied:
- Lacroix 2018: inverse triples (already in data), dim 200 sufficient for <250K entities
- Ruffinelli 2020: Adam + early stopping is robust default
- Goyal 2017: batch 1024 with lr 0.001 is safe for KGs this size
"""
import os
import sys
import json
import time
import gc
import torch
import numpy as np
from datetime import datetime

BASE = "/home/jshaik369/sexdiffkg"
V52_DIR = f"{BASE}/data/kg_v5.2"
OUT_DIR = f"{BASE}/results/kg_embeddings_v5.2"
VAULT = "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg"
os.makedirs(OUT_DIR, exist_ok=True)

# Set CPU threads for DGX Grace (20 ARM cores)
torch.set_num_threads(16)
os.environ["OMP_NUM_THREADS"] = "16"
os.environ["MKL_NUM_THREADS"] = "16"

print("=" * 70)
print("v5.2 ALL MODEL TRAINING (Fast Mode)")
print(f"Date: {datetime.now().isoformat()}")
print(f"Device: CPU, {torch.get_num_threads()} threads")
print("=" * 70)

if not os.path.exists(f"{V52_DIR}/triples.tsv"):
    print(f"ERROR: {V52_DIR}/triples.tsv not found.")
    sys.exit(1)

from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline

# === Load data once ===
print("\n[LOAD] Loading v5.2 triples...")
tf = TriplesFactory.from_path(
    f"{V52_DIR}/triples.tsv",
    create_inverse_triples=True,
)
train, valid, test = tf.split([0.9, 0.05, 0.05], random_state=42)
print(f"  Entities: {tf.num_entities:,}, Relations: {tf.num_relations:,}")
print(f"  Train: {train.num_triples:,}, Valid: {valid.num_triples:,}, Test: {test.num_triples:,}")

# Save split info
with open(f"{OUT_DIR}/split_info.json", "w") as f:
    json.dump({
        "entities": int(tf.num_entities),
        "relations": int(tf.num_relations),
        "total_triples": int(tf.num_triples),
        "train": int(train.num_triples),
        "valid": int(valid.num_triples),
        "test": int(test.num_triples),
        "split": [0.9, 0.05, 0.05],
        "random_state": 42,
        "inverse_triples": True,
    }, f, indent=2)

# === Model configs ===
# Literature-backed defaults for ~220K entity heterogeneous biomedical KG
MODELS = [
    {
        "name": "ComplEx",
        "kwargs": {"embedding_dim": 200},
        "max_epochs": 200,
        "batch_size": 1024,
        "lr": 0.001,
        "negs": 64,
        "baselines": {"v4": 0.2484, "v5": 0.0247},
    },
    {
        "name": "DistMult",
        "kwargs": {"embedding_dim": 200},
        "max_epochs": 200,
        "batch_size": 1024,
        "lr": 0.001,
        "negs": 64,
        "baselines": {"v4.1": 0.1013, "v5": 0.0413},
    },
    {
        "name": "RotatE",
        "kwargs": {"embedding_dim": 200},
        "max_epochs": 200,
        "batch_size": 1024,
        "lr": 0.001,
        "negs": 64,
        "baselines": {"v4.1": 0.2018},
    },
]

all_results = {}

for idx, cfg in enumerate(MODELS):
    model_name = cfg["name"]
    print(f"\n{'=' * 70}")
    print(f"[{idx+1}/{len(MODELS)}] TRAINING {model_name}")
    print(f"  dim={cfg['kwargs']['embedding_dim']}, lr={cfg['lr']}, "
          f"batch={cfg['batch_size']}, negs={cfg['negs']}, "
          f"max_epochs={cfg['max_epochs']}")
    print(f"  Started: {datetime.now().isoformat()}")
    print(f"{'=' * 70}")

    model_start = time.time()
    prefix = model_name.lower()

    try:
        result = pipeline(
            training=train,
            validation=valid,
            testing=test,
            model=model_name,
            model_kwargs=cfg["kwargs"],
            optimizer="Adam",
            optimizer_kwargs=dict(lr=cfg["lr"]),
            training_kwargs=dict(
                num_epochs=cfg["max_epochs"],
                batch_size=cfg["batch_size"],
                use_tqdm=True,
                checkpoint_name=f"{prefix}_v52_checkpoint.pt",
                checkpoint_directory=OUT_DIR,
                checkpoint_frequency=25,
            ),
            negative_sampler="basic",
            negative_sampler_kwargs=dict(num_negs_per_pos=cfg["negs"]),
            stopper="early",
            stopper_kwargs=dict(
                frequency=5,
                patience=5,
                relative_delta=0.001,
                metric="both.realistic.inverse_harmonic_mean_rank",
            ),
            evaluator_kwargs=dict(filtered=True),
            random_seed=42,
            device="cpu",
        )

        model_elapsed = time.time() - model_start

        # SAVE MODEL FIRST (crash protection)
        model_path = f"{OUT_DIR}/{prefix}_v52_final.pt"
        torch.save({
            "model_state_dict": result.model.state_dict(),
            "entity_to_id": dict(train.entity_to_id),
            "relation_to_id": dict(train.relation_to_id),
            "config": cfg,
        }, model_path)
        print(f"\n  Model saved: {model_path}")

        # Extract metrics
        metrics = result.metric_results.to_dict()
        mrr = metrics.get("both", {}).get("realistic", {}).get("inverse_harmonic_mean_rank", None)
        h1 = metrics.get("both", {}).get("realistic", {}).get("hits_at_1", None)
        h3 = metrics.get("both", {}).get("realistic", {}).get("hits_at_3", None)
        h5 = metrics.get("both", {}).get("realistic", {}).get("hits_at_5", None)
        h10 = metrics.get("both", {}).get("realistic", {}).get("hits_at_10", None)
        amri = metrics.get("both", {}).get("realistic", {}).get("adjusted_arithmetic_mean_rank_index", None)

        print(f"\n  {model_name} v5.2 RESULTS:")
        print(f"    MRR:     {mrr}")
        print(f"    Hits@1:  {h1}")
        print(f"    Hits@3:  {h3}")
        print(f"    Hits@5:  {h5}")
        print(f"    Hits@10: {h10}")
        print(f"    AMRI:    {amri}")
        print(f"    Time:    {model_elapsed/60:.1f} min")

        # Baseline comparison
        for bname, bval in cfg["baselines"].items():
            if mrr:
                change = (mrr - bval) / bval * 100
                print(f"    vs {bname}: {change:+.1f}%")

        model_results = {
            "timestamp": datetime.now().isoformat(),
            "model": model_name,
            "kg_version": "v5.2",
            "entities": int(tf.num_entities),
            "relations": int(tf.num_relations),
            "train_triples": int(train.num_triples),
            "test_triples": int(test.num_triples),
            "inverse_triples": True,
            "hyperparameters": {
                "embedding_dim": cfg["kwargs"]["embedding_dim"],
                "lr": cfg["lr"],
                "batch_size": cfg["batch_size"],
                "negs": cfg["negs"],
                "optimizer": "Adam",
                "max_epochs": cfg["max_epochs"],
                "early_stopping": True,
                "patience": 5,
                "frequency": 5,
            },
            "results": {
                "mrr": float(mrr) if mrr else None,
                "hits_at_1": float(h1) if h1 else None,
                "hits_at_3": float(h3) if h3 else None,
                "hits_at_5": float(h5) if h5 else None,
                "hits_at_10": float(h10) if h10 else None,
                "amri": float(amri) if amri else None,
            },
            "training_time_min": round(model_elapsed / 60, 1),
            "device": "cpu",
            "baselines": cfg["baselines"],
        }

        # Save per-model results
        rpath = f"{OUT_DIR}/{prefix}_v52_results.json"
        with open(rpath, "w") as f:
            json.dump(model_results, f, indent=2)
        print(f"  Results: {rpath}")

        # Vault copy
        vpath = f"{VAULT}/{prefix}_v52_results.json"
        with open(vpath, "w") as f:
            json.dump(model_results, f, indent=2)
        print(f"  Vault:   {vpath}")

        # Save embeddings
        try:
            state = result.model.state_dict()
            for k, v in state.items():
                if "entity" in k and "embedding" in k.lower():
                    emb = v.cpu().numpy()
                    if np.iscomplexobj(emb):
                        np.savez(f"{OUT_DIR}/{prefix}_embeddings.npz",
                                 real=emb.real, imag=emb.imag)
                    else:
                        np.save(f"{OUT_DIR}/{prefix}_embeddings.npy", emb)
                    print(f"  Embeddings: shape {emb.shape}")
                    break
        except Exception as e:
            print(f"  Embedding extraction warning: {e}")

        all_results[model_name] = model_results

    except Exception as e:
        model_elapsed = time.time() - model_start
        print(f"\n  {model_name} FAILED after {model_elapsed/60:.1f} min: {e}")
        all_results[model_name] = {"error": str(e), "time_min": round(model_elapsed / 60, 1)}

    # Force garbage collection between models
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

# === FINAL SUMMARY ===
print(f"\n{'=' * 70}")
print("ALL MODELS COMPLETE")
print(f"{'=' * 70}")
print(f"\n  {'Model':<12} {'MRR':>8} {'Hits@1':>8} {'Hits@10':>8} {'AMRI':>8} {'Time':>8}")
print(f"  {'-'*12} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")
for name, r in all_results.items():
    if "error" in r:
        print(f"  {name:<12} FAILED: {r['error'][:40]}")
    else:
        res = r["results"]
        print(f"  {name:<12} {res['mrr'] or 0:>8.4f} {res['hits_at_1'] or 0:>8.4f} "
              f"{res['hits_at_10'] or 0:>8.4f} {res['amri'] or 0:>8.4f} "
              f"{r['training_time_min']:>6.0f}m")

# v4 baselines for reference
print(f"\n  v4 Baselines:")
print(f"  {'ComplEx v4':<12} {'0.2484':>8} {'0.1678':>8} {'0.4069':>8} {'0.9902':>8}")
print(f"  {'DistMult v4.1':<12} {'0.1013':>8} {'0.0481':>8} {'0.1961':>8} {'0.9909':>8}")
print(f"  {'RotatE v4.1':<12} {'0.2018':>8} {'0.1128':>8} {'0.3677':>8} {'0.9922':>8}")

# Save combined results
combined_path = f"{OUT_DIR}/all_models_v52_results.json"
with open(combined_path, "w") as f:
    json.dump(all_results, f, indent=2, default=str)
print(f"\n  Combined: {combined_path}")

vault_combined = f"{VAULT}/all_models_v52_results.json"
with open(vault_combined, "w") as f:
    json.dump(all_results, f, indent=2, default=str)
print(f"  Vault:    {vault_combined}")

print(f"\n  Completed: {datetime.now().isoformat()}")
print(f"{'=' * 70}")
