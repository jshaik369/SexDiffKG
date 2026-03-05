#!/bin/bash
# Monitor RotatE training and capture completion
LOG=/home/jshaik369/sexdiffkg/results/rotatE_v41_cpu_fixed_training.log
METRICS=/home/jshaik369/sexdiffkg/results/kg_embeddings/rotatE_v41_cpu_metrics.json
VAULT=/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg
MONITOR_LOG=/home/jshaik369/sexdiffkg/results/rotatE_monitor.log

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
