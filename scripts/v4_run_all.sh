#!/bin/bash
# SexDiffKG v4 Master Pipeline — Full Rebuild
# Runs all steps sequentially with logging
# Launch in tmux: tmux new-session -d -s v4 './scripts/v4_run_all.sh'
set -euo pipefail

cd /home/jshaik369/sexdiffkg
LOGDIR=logs
VAULT=~/AYURFEM-Vault/projects/sexdiffkg
mkdir -p "$LOGDIR" "$VAULT"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
MASTER_LOG="$LOGDIR/v4_master_${TIMESTAMP}.log"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$MASTER_LOG"; }

log "================================================================"
log "SexDiffKG v4 FULL REBUILD — STARTED"
log "================================================================"
log "DGX Spark GB10 | 128GB RAM | Blackwell GPU"
log ""

# Step 1: Drug normalization with DiAna (98.94% coverage)
log "=== STEP 1: Drug Normalization (DiAna) ==="
python3 scripts/v4_01_normalize_diana.py 2>&1 | tee -a "$MASTER_LOG"
log "Step 1 DONE"
log ""

# Step 2: Recompute sex-stratified signals
log "=== STEP 2: Sex-Stratified Signal Computation ==="
python3 scripts/v4_02_compute_signals.py 2>&1 | tee -a "$MASTER_LOG"
log "Step 2 DONE"
log ""

# Step 3: Build KG v4 (Reactome + NaN-free)
log "=== STEP 3: KG v4 Construction ==="
python3 scripts/v4_03_build_kg.py 2>&1 | tee -a "$MASTER_LOG"
log "Step 3 DONE"
log ""

# Step 4a: Train DistMult v4 (GPU, ~6h)
log "=== STEP 4a: DistMult v4 Training (100 epochs, GPU) ==="
python3 scripts/v4_04_train_distmult.py 2>&1 | tee -a "$MASTER_LOG"
log "Step 4a DONE"
log ""

# Step 4b: Train RotatE v4 (CPU training, GPU eval, ~10h)
log "=== STEP 4b: RotatE v4 Training (200 epochs, NSSALoss) ==="
python3 scripts/v4_05_train_rotatE.py 2>&1 | tee -a "$MASTER_LOG"
log "Step 4b DONE"
log ""

# Step 5: Validation (40 benchmarks)
log "=== STEP 5: Validation ==="
python3 scripts/validate_40_benchmarks.py 2>&1 | tee -a "$MASTER_LOG" || true
log "Step 5 DONE"
log ""

# Step 6: Run audit scripts
log "=== STEP 6: Audit Scripts ==="
python3 scripts/audit_reproducibility.py 2>&1 | tee -a "$MASTER_LOG" || true
python3 scripts/audit_data_lineage.py 2>&1 | tee -a "$MASTER_LOG" || true
python3 scripts/verify_numbers.py 2>&1 | tee -a "$MASTER_LOG" || true
log "Step 6 DONE"
log ""

# Summary
log "================================================================"
log "SexDiffKG v4 REBUILD COMPLETE"
log "================================================================"
log "Master log: $MASTER_LOG"
log ""

# Write completion status to vault
python3 -c "
import json, time
from pathlib import Path

vault = Path.home() / 'AYURFEM-Vault/projects/sexdiffkg'
vault.mkdir(parents=True, exist_ok=True)

# Read all v4 summaries
summaries = {}
for f in ['data/processed/faers_clean/drug_normalization_v4_summary.json',
          'results/signals_v4/signal_computation_v4_summary.json',
          'data/kg_v4/kg_v4_summary.json',
          'results/kg_embeddings_v4/DistMult/distmult_v4_summary.json',
          'results/kg_embeddings_v4/RotatE/rotatE_v4_summary.json']:
    p = Path.home() / 'sexdiffkg' / f
    if p.exists():
        with open(p) as fh:
            summaries[p.stem] = json.load(fh)

# Write vault report
report = f'''# SexDiffKG v4 Full Rebuild Report — {time.strftime('%Y-%m-%d %H:%M:%S')}

## Pipeline Version: v4 (DiAna + Reactome + NSSALoss RotatE)

### Drug Normalization (DiAna)
'''
norm = summaries.get('drug_normalization_v4_summary', {})
if norm:
    report += f'''- Total records: {norm.get('total_records', 0):,}
- Raw unique drugs: {norm.get('unique_raw_drugs', 0):,}
- Normalized unique drugs: {norm.get('unique_normalized_drugs', 0):,}
- Reduction: {norm.get('reduction_pct', 0)}%
- DiAna matches: {norm.get('stats', {}).get('diana', 0):,}
- Total mapped: {norm.get('total_mapped_pct', 0)}%
'''

sig = summaries.get('signal_computation_v4_summary', {}).get('results', {})
if sig:
    report += f'''
### Sex-Stratified Signals
- Total signals: {sig.get('total_sex_differential_signals', 0):,}
- Female-higher: {sig.get('female_higher', 0):,}
- Male-higher: {sig.get('male_higher', 0):,}
- Unique drugs: {sig.get('unique_drugs', 0):,}
- Unique AEs: {sig.get('unique_adverse_events', 0):,}
'''

kg = summaries.get('kg_v4_summary', {})
if kg:
    report += f'''
### Knowledge Graph v4
- Nodes: {kg.get('total_nodes', 0):,}
- Edges: {kg.get('total_edges', 0):,}
- Triples (NaN-free): {kg.get('total_triples', 0):,}
- NaN dropped: {kg.get('nan_triples_dropped', 0):,}
- Pathways: {kg.get('data_sources', {}).get('pathways', 'unknown')}
'''

dm = summaries.get('distmult_v4_summary', {})
if dm:
    m = dm.get('metrics', {})
    report += f'''
### DistMult v4 Embeddings
- MRR: {m.get('inverse_harmonic_mean_rank', 0)}
- Hits@10: {m.get('hits_at_10', 0)}
- AMRI: {m.get('amri', 'N/A')}
- Training: {dm.get('training_time_hours', 0)}h on {dm.get('device', 'unknown')}
'''

rt = summaries.get('rotatE_v4_summary', {})
if rt:
    m = rt.get('metrics', {})
    report += f'''
### RotatE v4 Embeddings (FIXED)
- MRR: {m.get('inverse_harmonic_mean_rank', 0)}
- Hits@10: {m.get('hits_at_10', 0)}
- AMRI: {m.get('amri', 'N/A')}
- Training: {rt.get('training_time_hours', 0)}h
- v3 MRR was: {rt.get('v3_comparison', {}).get('v3_mrr', 0.0001)}
'''

report += f'''
---
*Generated by v4_run_all.sh at {time.strftime('%Y-%m-%d %H:%M:%S')}*
'''

(vault / 'v4_Rebuild_Report_{}.md'.format(time.strftime('%Y-%m-%d'))).write_text(report)
print('Vault report written')
" 2>&1 | tee -a "$MASTER_LOG"

log "Vault report written. Pipeline finished."
