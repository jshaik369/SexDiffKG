#!/bin/bash
# v5.2 Model Training Chain — runs all models sequentially
# Launch: tmux new-session -d -s v52_chain "bash /home/jshaik369/sexdiffkg/scripts/v52_chain_all_models.sh"

set -e
BASE="/home/jshaik369/sexdiffkg"
LOG_DIR="$BASE/results/kg_embeddings_v5.2"

echo "=========================================="
echo "v5.2 MODEL TRAINING CHAIN"
echo "Started: $(date -Iseconds)"
echo "=========================================="

# Step 1: Validate v5.2 KG first
echo ""
echo "[1/4] Validating v5.2 KG..."
python3 "$BASE/scripts/v52_validate.py" 2>&1 | tee "$LOG_DIR/validation.log"

# Step 2: DistMult training
echo ""
echo "[2/4] Training DistMult v5.2..."
echo "Started: $(date -Iseconds)"
python3 "$BASE/scripts/v52_train_distmult.py" 2>&1 | tee "$LOG_DIR/distmult_training.log"
echo "DistMult done: $(date -Iseconds)"

# Step 3: RotatE training
echo ""
echo "[3/4] Training RotatE v5.2..."
echo "Started: $(date -Iseconds)"
python3 "$BASE/scripts/v52_train_rotate.py" 2>&1 | tee "$LOG_DIR/rotate_training.log"
echo "RotatE done: $(date -Iseconds)"

# Step 4: Summary
echo ""
echo "=========================================="
echo "ALL MODELS COMPLETE"
echo "Finished: $(date -Iseconds)"
echo "=========================================="
echo ""
echo "Results:"
for f in "$LOG_DIR"/*_v52_results.json; do
    echo "  $(basename $f):"
    python3 -c "import json; d=json.load(open('$f')); r=d.get('results',{}); print(f'    MRR: {r.get(\"mrr\",\"N/A\")}, Hits@10: {r.get(\"hits_at_10\",\"N/A\")}')"
done
