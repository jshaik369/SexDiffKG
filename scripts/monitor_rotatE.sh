#!/bin/bash
# --- SexDiffKG path config (auto-injected) ---
SEXDIFFKG_HOME="${SEXDIFFKG_HOME:-$HOME/sexdiffkg}"
SEXDIFFKG_VAULT="${SEXDIFFKG_VAULT:-$HOME/AYURFEM-Vault/projects/sexdiffkg}"
export SEXDIFFKG_HOME SEXDIFFKG_VAULT
# --- end SexDiffKG path config ---

# Monitor RotatE training and capture completion
LOG=$SEXDIFFKG_HOME/results/rotatE_v41_cpu_fixed_training.log
METRICS=$SEXDIFFKG_HOME/results/kg_embeddings/rotatE_v41_cpu_metrics.json
VAULT=$SEXDIFFKG_VAULT
MONITOR_LOG=$SEXDIFFKG_HOME/results/rotatE_monitor.log

echo "=== Monitor started $(date) ===" >> $MONITOR_LOG

while true; do
    # Check if metrics file exists (training + eval complete)
    if [ -f "$METRICS" ]; then
        echo "=== TRAINING COMPLETE $(date) ===" >> $MONITOR_LOG
        cat $METRICS >> $MONITOR_LOG
        # Copy metrics to vault
        cp $METRICS $VAULT/RotatE_v41_DGX_metrics.json
        echo "Metrics copied to vault" >> $MONITOR_LOG
        break
    fi
    
    # Extract last epoch info from training log
    LAST_EPOCH=$(grep -oP 'loss=[\d.]+' $LOG 2>/dev/null | tail -1)
    PROGRESS=$(grep -oP '\d+/200' $LOG 2>/dev/null | tail -1)
    echo "[$(date '+%H:%M')] Epoch $PROGRESS $LAST_EPOCH" >> $MONITOR_LOG
    
    sleep 1800  # Check every 30 min
done
