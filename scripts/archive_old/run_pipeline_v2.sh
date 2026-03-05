#!/bin/bash
# SexDiffKG Pipeline v2 - post-download, full chain
# Download already complete (87 files, 3.2GB)

set -e
cd ~/sexdiffkg
LOG=logs/pipeline_v2.log

log() { echo "[$(date)] $1" | tee -a "$LOG"; }

log "=== SexDiffKG Pipeline v2 starting ==="
log "Download already complete: $(ls data/raw/faers/*.zip 2>/dev/null | wc -l) files"

# Step 1: Parse
log "Step 1: Parsing FAERS..."
python3 scripts/02_parse_faers.py --input-dir data/raw/faers --output-dir data/processed/faers 2>&1 | tee -a "$LOG"
log "Parse complete! Files: $(ls data/processed/faers/*.parquet 2>/dev/null)"

# Step 2: Deduplicate
log "Step 2: Deduplicating..."
python3 scripts/03_deduplicate.py --input-dir data/processed/faers --output-dir data/processed/faers_clean 2>&1 | tee -a "$LOG"
log "Dedup complete!"

# Step 3: Normalize drug names
log "Step 3: Normalizing drug names..."
python3 scripts/03b_normalize_drugs.py --input-dir data/processed/faers_clean --output-dir data/processed/faers_clean 2>&1 | tee -a "$LOG"
log "Normalization complete!"

# Step 4: Compute sex-stratified signals
log "Step 4: Computing sex-stratified signals..."
python3 scripts/04_compute_signals.py --input-dir data/processed/faers_clean --output-dir results/signals 2>&1 | tee -a "$LOG"
log "Signals complete!"

# Step 5: Build knowledge graph
log "Step 5: Building SexDiffKG..."
python3 scripts/06_build_kg.py --data-dir data --output-dir data/kg 2>&1 | tee -a "$LOG"
log "KG build complete!"

# Step 6: Train embeddings
log "Step 6: Training graph embeddings..."
python3 scripts/07_train_embeddings.py --kg-dir data/kg --output-dir results/kg_embeddings 2>&1 | tee -a "$LOG"
log "Embeddings complete!"

# Step 7: Validate
log "Step 7: Running benchmark validation..."
python3 scripts/08_validate.py --signals-dir results/signals --output-dir results/validation 2>&1 | tee -a "$LOG"
log "Validation complete!"

log "=== SexDiffKG Pipeline v2 COMPLETE ==="
log "Results in: results/signals, data/kg, results/kg_embeddings, results/validation"
