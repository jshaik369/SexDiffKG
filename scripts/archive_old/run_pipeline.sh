#!/bin/bash
# SexDiffKG Pipeline Runner
# Waits for FAERS download to complete, then runs parse → dedup → signals
# Usage: nohup bash scripts/run_pipeline.sh > logs/pipeline.log 2>&1 &

set -e
cd /home/jshaik369/sexdiffkg

LOG="logs/pipeline_$(date +%Y%m%d_%H%M%S).log"
exec > >(tee -a "$LOG") 2>&1

echo "=== SexDiffKG Pipeline Started: $(date) ==="

# Step 1: Wait for download to complete
echo "[$(date)] Waiting for FAERS download to complete..."
while pgrep -f "01_download_faers" > /dev/null 2>&1; do
    COUNT=$(ls /media/jshaik369/cen8tb/sexdiffkg_data/raw_faers/*.zip 2>/dev/null | wc -l)
    SIZE=$(du -sh /media/jshaik369/cen8tb/sexdiffkg_data/raw_faers/ 2>/dev/null | cut -f1)
    echo "[$(date)] Download in progress: $COUNT files, $SIZE"
    sleep 60
done
echo "[$(date)] Download complete!"

# Refresh symlinks
echo "[$(date)] Creating symlinks..."
for f in /media/jshaik369/cen8tb/sexdiffkg_data/raw_faers/*.zip; do
    ln -sf "$f" data/raw/faers/ 2>/dev/null
done
TOTAL=$(ls data/raw/faers/*.zip 2>/dev/null | wc -l)
echo "[$(date)] $TOTAL ZIP files linked"

# Step 2: Parse FAERS
echo "[$(date)] Starting FAERS parsing..."
python3 scripts/02_parse_faers.py --input-dir data/raw/faers --output-dir data/processed/faers
echo "[$(date)] Parsing complete!"

# Step 3: Deduplicate
echo "[$(date)] Starting deduplication..."
python3 scripts/03_deduplicate.py --input-dir data/processed/faers --output-dir data/processed/faers_clean
echo "[$(date)] Deduplication complete!"

# Step 4: Drug normalization  
echo "[$(date)] Starting drug name normalization..."
python3 scripts/03b_normalize_drugs.py --input-dir data/processed/faers_clean --output-dir data/processed/faers_clean
echo "[$(date)] Drug normalization complete!"

# Step 5: Compute signals
echo "[$(date)] Computing sex-stratified signals..."
python3 scripts/04_compute_signals.py --input-dir data/processed/faers_clean --output-dir results/signals
echo "[$(date)] Signal computation complete!"

# Step 6: Build KG
echo "[$(date)] Building knowledge graph..."
python3 scripts/06_build_kg.py
echo "[$(date)] KG built!"

# Step 7: Train embeddings
echo "[$(date)] Training graph embeddings..."
python3 scripts/07_train_embeddings.py
echo "[$(date)] Embeddings trained!"

echo "=== SexDiffKG Pipeline Complete: $(date) ==="
echo "Check results in: results/signals/ and results/kg_embeddings/"

# Step 8: Validate against benchmarks
echo "[$(date)] Running benchmark validation..."
python3 scripts/08_validate.py --signals-dir results/signals --output-dir results/validation
echo "[$(date)] Validation complete!"

echo "=== Full SexDiffKG Pipeline FINISHED: $(date) ==="
