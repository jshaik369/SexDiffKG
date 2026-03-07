#\!/bin/bash
# Monitor v52_fast tmux session and run post-training when done
BASE="/home/jshaik369/sexdiffkg"
LOG="$BASE/results/kg_embeddings_v5.2/all_models_training.log"

echo "Monitoring v5.2 training... (checking every 5 min)"
while tmux has-session -t v52_fast 2>/dev/null; do
    if [ -f "$LOG" ]; then
        tail -3 "$LOG"
    fi
    sleep 300
done

echo "Training session ended. Running post-training analysis..."
cd "$BASE" && python3 scripts/v52_post_training.py 2>&1 | tee results/kg_embeddings_v5.2/post_training.log
echo "Post-training complete: $(date -Iseconds)"
