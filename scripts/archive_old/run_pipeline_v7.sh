#!/usr/bin/env bash
set -euo pipefail
cd /home/jshaik369/sexdiffkg

echo "[$(date)] === Pipeline v7: embeddings → validate (KG already built) ==="

echo "[$(date)] Step 6: Training embeddings..."
python3 scripts/07_train_embeddings.py --kg-dir data/kg --output-dir results/kg_embeddings
echo "[$(date)] Embeddings done!"

echo "[$(date)] Step 7: Validation..."
python3 scripts/08_validate.py --kg-dir data/kg --signals-dir results/signals --output-dir results/validation
echo "[$(date)] Validation done!"

echo "[$(date)] === Pipeline v7 COMPLETE ==="
