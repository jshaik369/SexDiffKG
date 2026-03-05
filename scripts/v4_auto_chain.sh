#!/bin/bash
# Auto-chain: wait for DistMult v4.1, kill CPU RotatE, start GPU RotatE
cd /home/jshaik369/sexdiffkg

echo "$(date): Waiting for DistMult v4.1 to finish..."
while pgrep -f "v4_06_retrain_distmult" > /dev/null 2>&1; do
    sleep 30
done
echo "$(date): DistMult v4.1 complete!"

# Log DistMult results
echo "$(date): DistMult v4.1 results:"
cat results/kg_embeddings/distmult_v41_metrics.json 2>/dev/null

# Kill CPU RotatE
echo "$(date): Killing CPU RotatE..."
pkill -f "v4_05b_train_rotatE" 2>/dev/null
sleep 5

# Start GPU RotatE
echo "$(date): Starting RotatE v4.1 on GPU..."
python3 scripts/v4_07_train_rotatE_gpu.py 2>&1 | tee results/rotatE_v41_gpu_training.log

echo "$(date): RotatE v4.1 GPU complete!"
echo "$(date): Final RotatE results:"
cat results/kg_embeddings/rotatE_v41_gpu_metrics.json 2>/dev/null
