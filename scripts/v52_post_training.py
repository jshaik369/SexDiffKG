#!/usr/bin/env python3
"""v5.2 Post-Training Analysis — Run after all 3 models finish

1. Load all model results
2. Generate comparison table
3. Run top-k link predictions with best model
4. Generate sex-differential drug safety predictions from merged KG
5. Update GROUND_TRUTH files
6. Log to vault
"""
import os
import sys
import json
import torch
import numpy as np
import pandas as pd
from datetime import datetime

BASE = "/home/jshaik369/sexdiffkg"
V52_DIR = f"{BASE}/data/kg_v5.2"
EMB_DIR = f"{BASE}/results/kg_embeddings_v5.2"
VAULT = "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg"

print("=" * 70)
print("v5.2 POST-TRAINING ANALYSIS")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 70)

# === 1. Load all results ===
print("\n[1/5] Loading model results...")
models = {}
for prefix in ["complex", "distmult", "rotate"]:
    rpath = f"{EMB_DIR}/{prefix}_v52_results.json"
    if os.path.exists(rpath):
        with open(rpath) as f:
            models[prefix] = json.load(f)
        r = models[prefix]["results"]
        print(f"  {prefix}: MRR={r.get('mrr', 'N/A')}, "
              f"Hits@10={r.get('hits_at_10', 'N/A')}, "
              f"Time={models[prefix].get('training_time_min', 'N/A')}min")
    else:
        print(f"  {prefix}: NOT FOUND")

if not models:
    print("ERROR: No model results found. Training may still be in progress.")
    sys.exit(1)

# === 2. Comparison table ===
print("\n[2/5] Model comparison...")
print(f"\n  {'Model':<12} {'MRR':>8} {'H@1':>8} {'H@3':>8} {'H@10':>8} {'AMRI':>8} {'Time':>8}")
print(f"  {'-'*12} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")

# v5.2 models
for name, data in sorted(models.items()):
    r = data["results"]
    t = data.get("training_time_min", 0)
    print(f"  {name+'_v52':<12} "
          f"{r.get('mrr', 0) or 0:>8.4f} "
          f"{r.get('hits_at_1', 0) or 0:>8.4f} "
          f"{r.get('hits_at_3', 0) or 0:>8.4f} "
          f"{r.get('hits_at_10', 0) or 0:>8.4f} "
          f"{r.get('amri', 0) or 0:>8.4f} "
          f"{t:>6.0f}m")

# v4 baselines
print(f"  {'--- v4 ---':<12}")
print(f"  {'complex_v4':<12} {'0.2484':>8} {'0.1678':>8} {'0.1989':>8} {'0.4069':>8} {'0.9902':>8}")
print(f"  {'distmult_v4':<12} {'0.1013':>8} {'0.0481':>8} {'0.0874':>8} {'0.1961':>8} {'0.9909':>8}")
print(f"  {'rotate_v4':<12} {'0.2018':>8} {'0.1128':>8} {'0.1641':>8} {'0.3677':>8} {'0.9922':>8}")

# === 3. Best model link predictions ===
print("\n[3/5] Link predictions with best model...")

best_name = max(models.keys(), key=lambda k: models[k]["results"].get("mrr", 0) or 0)
best_data = models[best_name]
best_mrr = best_data["results"]["mrr"]
print(f"  Best model: {best_name} (MRR={best_mrr:.4f})")

# Only do predictions if MRR is reasonable
if best_mrr and best_mrr > 0.05:
    from pykeen.triples import TriplesFactory
    from pykeen.models import ComplEx, DistMult, RotatE

    # Load model
    model_path = f"{EMB_DIR}/{best_name}_v52_final.pt"
    checkpoint = torch.load(model_path, map_location="cpu", weights_only=False)

    # Reconstruct factory for ID mapping
    tf = TriplesFactory.from_path(
        f"{V52_DIR}/triples.tsv",
        create_inverse_triples=True,
    )

    # Create model
    model_class = {"complex": ComplEx, "distmult": DistMult, "rotate": RotatE}[best_name]
    dim = best_data["hyperparameters"]["embedding_dim"]
    model = model_class(
        triples_factory=tf,
        embedding_dim=dim,
    )
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    # Generate predictions for sex-differential drug-AE queries
    print("  Generating top-10 predictions for sample queries...")

    # Get entity and relation mappings
    eid = tf.entity_to_id
    rid = tf.relation_to_id
    id2e = {v: k for k, v in eid.items()}
    id2r = {v: k for k, v in rid.items()}

    # Sample drugs with known sex-differential signals
    sample_drugs = ["DRUG:RISPERIDONE", "DRUG:METFORMIN", "DRUG:ASPIRIN",
                    "DRUG:WARFARIN", "DRUG:NIVOLUMAB", "DRUG:PEMBROLIZUMAB",
                    "DRUG:ESTRADIOL", "DRUG:TESTOSTERONE"]
    rel = "sex_differential_adverse_event"

    if rel in rid:
        predictions = []
        for drug in sample_drugs:
            if drug not in eid:
                continue
            h_id = torch.tensor([eid[drug]])
            r_id = torch.tensor([rid[rel]])

            with torch.no_grad():
                scores = model.score_t(h_id.unsqueeze(0), r_id.unsqueeze(0))
                top_k = torch.topk(scores.squeeze(), k=10)

            preds = []
            for score, idx in zip(top_k.values.tolist(), top_k.indices.tolist()):
                entity = id2e.get(idx, f"UNK:{idx}")
                if entity.startswith("AE:"):
                    preds.append({"entity": entity, "score": round(score, 4)})

            if preds:
                predictions.append({
                    "drug": drug,
                    "relation": rel,
                    "top_predictions": preds[:5],
                })
                print(f"    {drug} → {rel}:")
                for p in preds[:3]:
                    print(f"      {p['entity']}: {p['score']:.4f}")

        # Save predictions
        pred_path = f"{EMB_DIR}/v52_sample_predictions.json"
        with open(pred_path, "w") as f:
            json.dump({
                "model": best_name,
                "mrr": best_mrr,
                "timestamp": datetime.now().isoformat(),
                "predictions": predictions,
                "warning": f"MRR={best_mrr:.4f} — predictions are {'reliable' if best_mrr > 0.15 else 'exploratory only'}",
            }, f, indent=2)
        print(f"  Predictions saved: {pred_path}")
    else:
        print(f"  Relation '{rel}' not in model — skipping predictions")
else:
    print(f"  MRR too low ({best_mrr}) — skipping predictions")

# === 4. Update GROUND_TRUTH ===
print("\n[4/5] Updating GROUND_TRUTH with v5.2 model results...")
gt_paths = [
    f"{BASE}/GROUND_TRUTH.json",
    f"{BASE}/data/kg_v4/GROUND_TRUTH.json",
    f"{BASE}/results/GROUND_TRUTH.json",
    f"{VAULT}/GROUND_TRUTH.json",
]

v52_model_section = {}
for name, data in models.items():
    r = data["results"]
    v52_model_section[f"{name}_v52"] = {
        "mrr": r.get("mrr"),
        "hits_at_1": r.get("hits_at_1"),
        "hits_at_3": r.get("hits_at_3"),
        "hits_at_10": r.get("hits_at_10"),
        "amri": r.get("amri"),
        "training_time_min": data.get("training_time_min"),
        "embedding_dim": data["hyperparameters"]["embedding_dim"],
    }

for gp in gt_paths:
    if os.path.exists(gp):
        with open(gp) as f:
            gt = json.load(f)
        gt["v52_models"] = v52_model_section
        gt["v52_kg"] = {
            "nodes": 217993,
            "edges": 3194017,
            "node_types": 13,
            "edge_types": 18,
            "bridges": 13167,
            "v4_preservation_pct": 99.995,
        }
        with open(gp, "w") as f:
            json.dump(gt, f, indent=2)
        print(f"  Updated: {gp}")

# === 5. Summary ===
print(f"\n[5/5] Final summary...")

summary = {
    "timestamp": datetime.now().isoformat(),
    "kg_version": "v5.2",
    "models": v52_model_section,
    "best_model": best_name,
    "best_mrr": best_mrr,
    "v4_comparison": {
        "complex": {"v4_mrr": 0.2484, "v52_mrr": models.get("complex", {}).get("results", {}).get("mrr")},
        "distmult": {"v4_mrr": 0.1013, "v52_mrr": models.get("distmult", {}).get("results", {}).get("mrr")},
        "rotate": {"v4_mrr": 0.2018, "v52_mrr": models.get("rotate", {}).get("results", {}).get("mrr")},
    },
}

summary_path = f"{EMB_DIR}/v52_training_summary.json"
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2)
print(f"  Summary: {summary_path}")

vault_summary = f"{VAULT}/v52_training_summary.json"
with open(vault_summary, "w") as f:
    json.dump(summary, f, indent=2)
print(f"  Vault:   {vault_summary}")

print(f"\n{'=' * 70}")
print("POST-TRAINING ANALYSIS COMPLETE")
print(f"{'=' * 70}")
