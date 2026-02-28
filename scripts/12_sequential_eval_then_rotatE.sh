#!/bin/bash
# Sequential: DistMult eval → RotatE training (both need GPU)
# Uses python3.13 which has PyKEEN 1.11.1 + CUDA
# Follows Engineering_Protocols.md — no resource conflicts

set -e
cd /home/jshaik369/sexdiffkg

# Ensure output dirs exist
mkdir -p results/kg_embeddings/RotatE

echo "=== PHASE 1: DistMult v3 Evaluation ==="
echo "Started: $(date)"
python3.13 scripts/10_eval_distmult_v3.py 2>&1 | tee results/kg_embeddings/distmult_v3_eval.log
echo "DistMult eval finished: $(date)"

echo ""
echo "=== PHASE 2: RotatE v3 GPU Training ==="
echo "Started: $(date)"
python3.13 scripts/11_train_rotatE_v3_gpu.py 2>&1 | tee results/kg_embeddings/RotatE/rotatE_v3_train.log
echo "RotatE training finished: $(date)"

echo ""
echo "=== ALL COMPLETE ==="
echo "Finished: $(date)"
