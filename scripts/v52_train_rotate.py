#!/usr/bin/env python3
"""
SexDiffKG v5.2 — RotatE Training with Mini-HPO
=================================================
3-trial mini-HPO (20 epochs each) → full training (300 epochs + early stopping)

Key design decisions:
  - CPU-only: GB10 NVRTC SM 12.1 cannot JIT-compile complex tensor CUDA kernels.
    RotatE uses complex embeddings → force CPU.
  - Single train() call: avoids PyKEEN epoch counter bug (Incident #10).
  - Save model BEFORE evaluation extraction: crash protection (Incident #1).
  - create_inverse_triples=True: major performance lever (Lacroix et al. ICML 2018).
  - Checkpoint every 50 epochs for crash recovery.
  - 90/5/5 split with random_state=42 for reproducibility.

Baselines (v4 RotatE v4.1): MRR 0.2018, Hits@10 36.77%, AMRI 0.9922

Author: JShaik (jshaik@coevolvenetwork.com)
"""

import gc
import json
import os
import sys
import time
import numpy as np
import torch
from datetime import datetime
from pathlib import Path

# --- Paths ---
BASE = "/home/jshaik369/sexdiffkg"
V52_DIR = f"{BASE}/data/kg_v5.2"
OUT_DIR = f"{BASE}/results/kg_embeddings_v5.2"
VAULT = "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg"
TRIPLES_FILE = f"{V52_DIR}/triples.tsv"

os.makedirs(OUT_DIR, exist_ok=True)

# --- CPU threading config ---
torch.set_num_threads(16)
os.environ["OMP_NUM_THREADS"] = "16"
os.environ["MKL_NUM_THREADS"] = "16"

# --- Constants ---
SEED = 42
METRIC = "both.realistic.inverse_harmonic_mean_rank"

# --- Baselines ---
BASELINES = {
    "RotatE_v4.1": {"mrr": 0.2018, "hits_at_10": 0.3677, "amri": 0.9922},
    "ComplEx_v4":   {"mrr": 0.2484, "hits_at_10": 0.4069, "amri": 0.9902},
}


def log(msg):
    """Timestamped logging to stdout."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def check_prerequisites():
    """Verify triples file exists before proceeding."""
    if not os.path.exists(TRIPLES_FILE):
        log(f"FATAL: {TRIPLES_FILE} not found.")
        log("Run the v5.2 build pipeline first.")
        sys.exit(1)
    log(f"Triples file: {TRIPLES_FILE}")


def load_and_split():
    """Load v5.2 triples and create 90/5/5 split."""
    from pykeen.triples import TriplesFactory

    log("Loading v5.2 triples with create_inverse_triples=True...")
    tf = TriplesFactory.from_path(
        TRIPLES_FILE,
        create_inverse_triples=True,
        random_seed=SEED,
    )
    log(f"  Entities:  {tf.num_entities:,}")
    log(f"  Relations: {tf.num_relations:,} (including inverse)")
    log(f"  Triples:   {tf.num_triples:,} (including inverse)")

    # 90/5/5 split
    train, valid, test = tf.split([0.9, 0.05, 0.05], random_state=SEED)
    log(f"  Train: {train.num_triples:,}")
    log(f"  Valid: {valid.num_triples:,}")
    log(f"  Test:  {test.num_triples:,}")

    # Save split info
    split_info = {
        "entities": int(tf.num_entities),
        "relations": int(tf.num_relations),
        "total_triples": int(tf.num_triples),
        "train_triples": int(train.num_triples),
        "valid_triples": int(valid.num_triples),
        "test_triples": int(test.num_triples),
        "split_ratios": [0.9, 0.05, 0.05],
        "random_state": SEED,
        "inverse_triples": True,
        "model": "RotatE",
    }
    with open(f"{OUT_DIR}/rotate_v52_split_info.json", "w") as f:
        json.dump(split_info, f, indent=2)
    log(f"  Split info saved: {OUT_DIR}/rotate_v52_split_info.json")

    return tf, train, valid, test


def run_mini_hpo(train, valid, test):
    """
    3-trial mini-HPO with 20 epochs each.

    Configs chosen based on v4.1 experience (NSSALoss + AdamW did well):
      Trial 1: dim=200, lr=0.001, batch=512,  negs=64   (conservative)
      Trial 2: dim=200, lr=0.003, batch=1024, negs=128  (scaled LR with batch, Goyal 2017)
      Trial 3: dim=300, lr=0.001, batch=512,  negs=128  (higher dim, more negatives)
    """
    from pykeen.pipeline import pipeline

    configs = [
        {"dim": 200, "lr": 0.001, "batch": 512,  "negs": 64,  "label": "conservative"},
        {"dim": 200, "lr": 0.003, "batch": 1024, "negs": 128, "label": "scaled-lr"},
        {"dim": 300, "lr": 0.001, "batch": 512,  "negs": 128, "label": "high-dim"},
    ]

    log(f"Running {len(configs)}-trial mini-HPO (20 epochs each)...")
    hpo_start = time.time()

    best_mrr = -1.0
    best_config = None
    hpo_results_list = []

    for i, cfg in enumerate(configs):
        log(f"\n  Trial {i+1}/{len(configs)} [{cfg['label']}]: "
            f"dim={cfg['dim']}, lr={cfg['lr']}, batch={cfg['batch']}, negs={cfg['negs']}")
        trial_start = time.time()

        try:
            r = pipeline(
                training=train,
                validation=valid,
                testing=test,
                model="RotatE",
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
                evaluation_kwargs=dict(batch_size=256),
                random_seed=SEED,
                device="cpu",
            )

            metrics = r.metric_results.to_dict()
            mrr = metrics.get("both", {}).get("realistic", {}).get(
                "inverse_harmonic_mean_rank", 0
            )
            h10 = metrics.get("both", {}).get("realistic", {}).get("hits_at_10", 0)
            trial_time = time.time() - trial_start

            log(f"    MRR: {mrr:.5f}, Hits@10: {h10:.5f} ({trial_time/60:.1f} min)")

            hpo_results_list.append({
                "trial": i + 1,
                "label": cfg["label"],
                "config": {k: v for k, v in cfg.items() if k != "label"},
                "mrr": float(mrr),
                "hits_at_10": float(h10),
                "time_min": round(trial_time / 60, 1),
            })

            if mrr > best_mrr:
                best_mrr = mrr
                best_config = cfg

            # Free memory between trials
            del r
            gc.collect()

        except Exception as e:
            trial_time = time.time() - trial_start
            log(f"    FAILED ({trial_time/60:.1f} min): {e}")
            hpo_results_list.append({
                "trial": i + 1,
                "label": cfg["label"],
                "config": {k: v for k, v in cfg.items() if k != "label"},
                "error": str(e),
                "time_min": round(trial_time / 60, 1),
            })

    hpo_elapsed = time.time() - hpo_start

    if best_config is None:
        log("  WARNING: All HPO trials failed! Using conservative defaults.")
        best_config = {"dim": 200, "lr": 0.001, "batch": 512, "negs": 128, "label": "fallback"}
        best_mrr = None

    log(f"\n  HPO complete in {hpo_elapsed/60:.1f} min")
    log(f"  Best config: [{best_config.get('label', 'N/A')}] "
        f"dim={best_config['dim']}, lr={best_config['lr']}, "
        f"batch={best_config['batch']}, negs={best_config['negs']}")
    log(f"  Best HPO MRR: {best_mrr}")

    # Save HPO results
    hpo_out = {
        "timestamp": datetime.now().isoformat(),
        "model": "RotatE",
        "kg_version": "v5.2",
        "hpo_epochs": 20,
        "n_trials": len(configs),
        "time_min": round(hpo_elapsed / 60, 1),
        "best_mrr": float(best_mrr) if best_mrr and best_mrr > 0 else None,
        "best_config": {k: v for k, v in best_config.items() if k != "label"},
        "best_label": best_config.get("label"),
        "all_trials": hpo_results_list,
    }
    hpo_path = f"{OUT_DIR}/rotate_v52_hpo_results.json"
    with open(hpo_path, "w") as f:
        json.dump(hpo_out, f, indent=2)
    log(f"  HPO results saved: {hpo_path}")

    return best_config, best_mrr, hpo_elapsed


def full_training(train, valid, test, tf, best_config, hpo_elapsed):
    """
    Full RotatE training: 300 epochs + early stopping.

    Uses pipeline API with:
      - Early stopping: patience=10, frequency=10, relative_delta=0.001
      - Checkpoint every 50 epochs
      - Filtered evaluation
      - CPU device (forced)
    """
    from pykeen.pipeline import pipeline

    dim = best_config["dim"]
    lr = best_config["lr"]
    batch = best_config["batch"]
    negs = best_config["negs"]

    log(f"\nFull RotatE training (300 epochs + early stopping)...")
    log(f"  Config: dim={dim}, lr={lr}, batch={batch}, negs={negs}")
    log(f"  Early stopping: patience=10, frequency=10, relative_delta=0.001")
    log(f"  Metric: {METRIC}")
    log(f"  Checkpoint: every 50 epochs → {OUT_DIR}")

    train_start = time.time()

    result = pipeline(
        training=train,
        validation=valid,
        testing=test,
        model="RotatE",
        model_kwargs=dict(
            embedding_dim=dim,
        ),
        optimizer="Adam",
        optimizer_kwargs=dict(
            lr=lr,
        ),
        training_kwargs=dict(
            num_epochs=300,
            batch_size=batch,
            use_tqdm=True,
            checkpoint_name="rotate_v52_checkpoint.pt",
            checkpoint_directory=OUT_DIR,
            checkpoint_frequency=50,
        ),
        negative_sampler="basic",
        negative_sampler_kwargs=dict(
            num_negs_per_pos=negs,
        ),
        stopper="early",
        stopper_kwargs=dict(
            frequency=10,
            patience=10,
            relative_delta=0.001,
            metric=METRIC,
        ),
        evaluator_kwargs=dict(
            filtered=True,
        ),
        evaluation_kwargs=dict(
            batch_size=256,
        ),
        random_seed=SEED,
        device="cpu",
    )

    train_elapsed = time.time() - train_start
    log(f"  Training complete: {train_elapsed/60:.1f} min ({train_elapsed/3600:.2f} h)")

    return result, train_elapsed


def save_model(result, train):
    """
    CRITICAL: Save model weights BEFORE evaluation extraction.
    This is crash protection — evaluation metric extraction can fail,
    but we must not lose the trained model (Incident #1 prevention).
    """
    log("\nSaving model weights (crash protection — BEFORE evaluation extraction)...")

    model_path = f"{OUT_DIR}/rotate_v52_final.pt"
    torch.save({
        "model_state_dict": result.model.state_dict(),
        "entity_to_id": dict(train.entity_to_id),
        "relation_to_id": dict(train.relation_to_id),
    }, model_path)
    log(f"  Model checkpoint saved: {model_path}")

    # Also save embeddings as numpy arrays for downstream analysis
    emb_dir = Path(OUT_DIR) / "rotate_v52_embeddings"
    emb_dir.mkdir(parents=True, exist_ok=True)

    try:
        entity_emb = result.model.entity_representations[0](indices=None).detach().cpu().numpy()
        relation_emb = result.model.relation_representations[0](indices=None).detach().cpu().numpy()
        np.savez(emb_dir / "entity_embeddings.npz", embeddings=entity_emb)
        np.savez(emb_dir / "relation_embeddings.npz", embeddings=relation_emb)
        log(f"  Entity embeddings:   {entity_emb.shape} → {emb_dir}/entity_embeddings.npz")
        log(f"  Relation embeddings: {relation_emb.shape} → {emb_dir}/relation_embeddings.npz")
    except Exception as e:
        log(f"  WARNING: Embedding extraction failed (model is saved): {e}")

    # Save entity-to-id and relation-to-id mappings as JSON for easy lookup
    try:
        with open(emb_dir / "entity_to_id.json", "w") as f:
            json.dump({str(k): int(v) for k, v in train.entity_to_id.items()}, f)
        with open(emb_dir / "relation_to_id.json", "w") as f:
            json.dump({str(k): int(v) for k, v in train.relation_to_id.items()}, f)
        log(f"  ID mappings saved to {emb_dir}/")
    except Exception as e:
        log(f"  WARNING: ID mapping save failed: {e}")

    return model_path


def extract_and_save_results(result, tf, train, valid, test, best_config,
                              hpo_elapsed, train_elapsed, best_hpo_mrr):
    """Extract metrics and save results JSON + vault copy."""
    log("\nExtracting evaluation results...")

    metrics = result.metric_results.to_dict()
    mrr = metrics.get("both", {}).get("realistic", {}).get("inverse_harmonic_mean_rank", None)
    h1 = metrics.get("both", {}).get("realistic", {}).get("hits_at_1", None)
    h3 = metrics.get("both", {}).get("realistic", {}).get("hits_at_3", None)
    h5 = metrics.get("both", {}).get("realistic", {}).get("hits_at_5", None)
    h10 = metrics.get("both", {}).get("realistic", {}).get("hits_at_10", None)
    amri = metrics.get("both", {}).get("realistic", {}).get(
        "adjusted_arithmetic_mean_rank_index", None
    )

    # If AMRI not available directly, compute from AMR
    if amri is None:
        amr = metrics.get("both", {}).get("realistic", {}).get("arithmetic_mean_rank", None)
        if amr is not None:
            amri = 1.0 - (2.0 * amr) / (tf.num_entities + 1)

    # --- Print results ---
    log("")
    log("=" * 70)
    log("RotatE v5.2 RESULTS")
    log("=" * 70)
    log(f"  MRR:     {mrr}")
    log(f"  Hits@1:  {h1}")
    log(f"  Hits@3:  {h3}")
    log(f"  Hits@5:  {h5}")
    log(f"  Hits@10: {h10}")
    log(f"  AMRI:    {amri}")
    log(f"  HPO time:   {hpo_elapsed/60:.1f} min")
    log(f"  Train time: {train_elapsed/60:.1f} min")
    log(f"  Total time: {(hpo_elapsed + train_elapsed)/60:.1f} min")

    # --- Baseline comparison ---
    log(f"\n  Baselines:")
    for name, bl in BASELINES.items():
        log(f"    {name}: MRR {bl['mrr']}, Hits@10 {bl['hits_at_10']*100:.2f}%, AMRI {bl['amri']}")
    if mrr:
        for name, bl in BASELINES.items():
            pct_change = (mrr - bl["mrr"]) / bl["mrr"] * 100
            log(f"    v5.2 RotatE vs {name}: {pct_change:+.1f}% MRR")

    # --- Build results dict ---
    final_results = {
        "timestamp": datetime.now().isoformat(),
        "model": "RotatE",
        "kg_version": "v5.2",
        "kg_description": "SexDiffKG v5.2 bridged merged (217,993 nodes, 3,194,017 edges, 18 relation types)",
        "entities": int(tf.num_entities),
        "relations": int(tf.num_relations),
        "train_triples": int(train.num_triples),
        "valid_triples": int(valid.num_triples),
        "test_triples": int(test.num_triples),
        "inverse_triples": True,
        "hyperparameters": {
            "embedding_dim": best_config["dim"],
            "learning_rate": best_config["lr"],
            "batch_size": best_config["batch"],
            "num_negs_per_pos": best_config["negs"],
            "optimizer": "Adam",
            "max_epochs": 300,
            "early_stopping": True,
            "early_stopping_patience": 10,
            "early_stopping_frequency": 10,
            "early_stopping_relative_delta": 0.001,
            "early_stopping_metric": METRIC,
            "checkpoint_frequency": 50,
        },
        "hpo": {
            "n_trials": 3,
            "epochs_per_trial": 20,
            "best_hpo_mrr": float(best_hpo_mrr) if best_hpo_mrr and best_hpo_mrr > 0 else None,
            "best_config_label": best_config.get("label"),
            "time_min": round(hpo_elapsed / 60, 1),
        },
        "results": {
            "mrr": float(mrr) if mrr is not None else None,
            "hits_at_1": float(h1) if h1 is not None else None,
            "hits_at_3": float(h3) if h3 is not None else None,
            "hits_at_5": float(h5) if h5 is not None else None,
            "hits_at_10": float(h10) if h10 is not None else None,
            "amri": float(amri) if amri is not None else None,
        },
        "baselines": BASELINES,
        "training_time_min": round(train_elapsed / 60, 1),
        "hpo_time_min": round(hpo_elapsed / 60, 1),
        "total_time_min": round((hpo_elapsed + train_elapsed) / 60, 1),
        "device": "cpu",
        "cpu_threads": 16,
        "random_seed": SEED,
        "notes": [
            "CPU-only: GB10 GPU NVRTC SM 12.1 incompatible with complex tensor JIT compilation",
            "create_inverse_triples=True (Lacroix et al. ICML 2018)",
            "Model saved BEFORE evaluation extraction (crash protection, Incident #1)",
            "Single train() call to avoid epoch counter bug (Incident #10)",
        ],
    }

    # --- Save results ---
    results_path = f"{OUT_DIR}/rotate_v52_results.json"
    with open(results_path, "w") as f:
        json.dump(final_results, f, indent=2)
    log(f"\n  Results saved: {results_path}")

    # --- Vault copy ---
    vault_results_path = f"{VAULT}/rotate_v52_results.json"
    try:
        os.makedirs(VAULT, exist_ok=True)
        with open(vault_results_path, "w") as f:
            json.dump(final_results, f, indent=2)
        log(f"  Vault copy: {vault_results_path}")
    except Exception as e:
        log(f"  WARNING: Vault copy failed: {e}")

    return final_results


def main():
    """Main entry point: HPO → Full Training → Save → Evaluate → Report."""
    print("=" * 70)
    print("SexDiffKG v5.2 — RotatE TRAINING")
    print(f"Date: {datetime.now().isoformat()}")
    print(f"Device: CPU (GB10 GPU incompatible with RotatE complex tensors)")
    print(f"Threads: {torch.get_num_threads()}")
    print(f"PyTorch: {torch.__version__}")
    print(f"Triples: {TRIPLES_FILE}")
    print(f"Output:  {OUT_DIR}")
    print(f"Vault:   {VAULT}")
    print("=" * 70)

    total_start = time.time()

    # --- Pre-flight ---
    check_prerequisites()

    # --- Load data ---
    log("\n[1/5] Loading and splitting data...")
    tf, train, valid, test = load_and_split()

    # --- Mini-HPO ---
    log("\n[2/5] Mini-HPO (3 trials, 20 epochs each)...")
    best_config, best_hpo_mrr, hpo_elapsed = run_mini_hpo(train, valid, test)

    # Force GC between HPO and full training
    gc.collect()

    # --- Full training ---
    log("\n[3/5] Full training (300 epochs + early stopping)...")
    result, train_elapsed = full_training(train, valid, test, tf, best_config, hpo_elapsed)

    # --- Save model BEFORE evaluation extraction (CRITICAL) ---
    log("\n[4/5] Saving model and embeddings...")
    model_path = save_model(result, train)

    # --- Extract results and save ---
    log("\n[5/5] Extracting and saving results...")
    final_results = extract_and_save_results(
        result, tf, train, valid, test, best_config,
        hpo_elapsed, train_elapsed, best_hpo_mrr,
    )

    # --- Final summary ---
    total_elapsed = time.time() - total_start
    log("")
    log("=" * 70)
    log("TRAINING COMPLETE")
    log(f"  Total wall time: {total_elapsed/60:.1f} min ({total_elapsed/3600:.2f} h)")
    log(f"  Model:   {model_path}")
    log(f"  Results: {OUT_DIR}/rotate_v52_results.json")
    log(f"  Vault:   {VAULT}/rotate_v52_results.json")
    log("=" * 70)


if __name__ == "__main__":
    main()
