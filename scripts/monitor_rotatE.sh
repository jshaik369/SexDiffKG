#!/bin/bash
# RotatE Training Completion Monitor
LOG="/home/jshaik369/sexdiffkg/results/kg_embeddings/RotatE/rotatE_v3_cpu.log"
NOTIFY="/home/jshaik369/sexdiffkg/ROTATE_TRAINING_COMPLETE.txt"

while true; do
    # Check if training process is still running
    if ! pgrep -f "11c_train_rotatE_v3_cpu.py" > /dev/null; then
        # Training stopped - check if completed or failed
        FINAL_LOSS=$(grep -oP "loss=\K[0-9.]+" "$LOG" | tail -1)
        FINAL_EPOCH=$(grep -oP "\d+(?=/100.*epoch)" "$LOG" | tail -1)
        
        echo "========================================" > "$NOTIFY"
        echo "ROTATЕ TRAINING COMPLETED" >> "$NOTIFY"
        echo "========================================" >> "$NOTIFY"
        echo "Time: $(date)" >> "$NOTIFY"
        echo "Final Epoch: $FINAL_EPOCH/100" >> "$NOTIFY"
        echo "Final Loss: $FINAL_LOSS" >> "$NOTIFY"
        echo "" >> "$NOTIFY"
        echo "Check results in:" >> "$NOTIFY"
        echo "  /home/jshaik369/sexdiffkg/results/kg_embeddings/RotatE/" >> "$NOTIFY"
        echo "========================================" >> "$NOTIFY"
        
        # Also log to main results
        cp "$NOTIFY" /home/jshaik369/sexdiffkg/results/
        
        echo "Training complete notification written to $NOTIFY"
        exit 0
    fi
    
    # Still running - sleep 10 minutes before next check
    sleep 600
done
