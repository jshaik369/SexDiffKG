#!/bin/bash
# SexDiffKG Pipeline v3 - restart from dedup (parse already done)

set -euo pipefail
cd ~/sexdiffkg
LOG=logs/pipeline_v3.log

log() { echo "[$(date)] $1" | tee -a "$LOG"; }

log "=== SexDiffKG Pipeline v3 starting (from dedup) ==="

# Step 2: Deduplicate
log "Step 2: Deduplicating..."
python3 scripts/03_deduplicate.py --input-dir data/processed/faers --output-dir data/processed/faers_clean 2>&1 | tee -a "$LOG"
log "Dedup complete!"
ls -lh data/processed/faers_clean/*.parquet 2>&1 | tee -a "$LOG"

# Step 3: Normalize drug names
log "Step 3: Normalizing drug names..."
python3 scripts/03b_normalize_drugs.py --input-dir data/processed/faers_clean --output-dir data/processed/faers_clean 2>&1 | tee -a "$LOG"
log "Normalization complete!"

# Step 4: Compute sex-stratified signals
log "Step 4: Computing sex-stratified signals..."
python3 scripts/04_compute_signals.py --input-dir data/processed/faers_clean --output-dir results/signals 2>&1 | tee -a "$LOG"
log "Signals complete!"
ls -lh results/signals/*.parquet 2>&1 | tee -a "$LOG"

# Step 5: Build knowledge graph
log "Step 5: Building SexDiffKG..."
python3 scripts/06_build_kg.py --data-dir data --output-dir data/kg 2>&1 | tee -a "$LOG"
log "KG build complete!"
ls -lh data/kg/*.tsv 2>&1 | tee -a "$LOG"

# Step 6: Train embeddings
log "Step 6: Training graph embeddings..."
python3 scripts/07_train_embeddings.py --kg-dir data/kg --output-dir results/kg_embeddings 2>&1 | tee -a "$LOG"
log "Embeddings complete!"

# Step 7: Validate
log "Step 7: Running benchmark validation..."
python3 scripts/08_validate.py --signals-dir results/signals --output-dir results/validation 2>&1 | tee -a "$LOG"
log "Validation complete!"

log "=== SexDiffKG Pipeline v3 ALL DONE ==="
