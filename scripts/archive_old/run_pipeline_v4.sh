#!/bin/bash
set -euo pipefail
cd ~/sexdiffkg
LOG=logs/pipeline_v4.log
log() { echo "[$(date)] $1" >> "$LOG"; }

log "=== Pipeline v4: normalize → signals → KG → embeddings → validate ==="

# Fast normalize
log "Step 3: Fast local normalization..."
python3 scripts/fast_normalize.py >> "$LOG" 2>&1
log "Normalization done!"

# Signals
log "Step 4: Computing sex-stratified signals..."
python3 scripts/04_compute_signals.py --input-dir data/processed/faers_clean --output-dir results/signals >> "$LOG" 2>&1
log "Signals done!"

# KG build
log "Step 5: Building SexDiffKG..."
python3 scripts/06_build_kg.py --data-dir data --output-dir data/kg >> "$LOG" 2>&1
log "KG build done!"

# Embeddings
log "Step 6: Training embeddings..."
python3 scripts/07_train_embeddings.py --kg-dir data/kg --output-dir results/kg_embeddings >> "$LOG" 2>&1
log "Embeddings done!"

# Validate
log "Step 7: Validation..."
python3 scripts/08_validate.py --signals-dir results/signals --output-dir results/validation >> "$LOG" 2>&1
log "Validation done!"

log "=== Pipeline v4 COMPLETE ==="
