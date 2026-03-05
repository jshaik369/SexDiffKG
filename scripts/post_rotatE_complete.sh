#!/bin/bash
# Post-RotatE completion workflow
# Run this after both DGX and Mac Mini RotatE v4.1 training completes
set -e

DGX_METRICS=/home/jshaik369/sexdiffkg/results/kg_embeddings/rotatE_v41_cpu_metrics.json
VAULT=/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg

echo '=== Post-RotatE v4.1 Completion Workflow ==='
echo "Started: $(date)"

# Step 1: Check DGX metrics exist
if [ ! -f "$DGX_METRICS" ]; then
    echo 'ERROR: DGX metrics not found at $DGX_METRICS'
    exit 1
fi
echo '1. DGX metrics file found'
cat "$DGX_METRICS"

# Step 2: Copy metrics to vault
cp "$DGX_METRICS" "$VAULT/RotatE_v41_DGX_metrics.json"
echo '2. Metrics copied to vault'

# Step 3: Show key numbers for manual GROUND_TRUTH update
echo ''
echo '=== KEY METRICS FOR GROUND_TRUTH UPDATE ==='
python3 -c "
import json
with open('$DGX_METRICS') as f:
    m = json.load(f)
print(f'MRR:     {m["mrr"]:.5f}')
print(f'Hits@1:  {m["hits_at_1"]:.5f}')
print(f'Hits@10: {m["hits_at_10"]:.5f}')
print(f'AMRI:    {m["amri"]:.4f}')
print(f'Loss:    {m.get("final_loss", "N/A")}')
print(f'Time:    {m.get("training_time_hours", "N/A")}h')
"

echo ''
echo '=== REMAINING MANUAL STEPS ==='
echo '3. Update GROUND_TRUTH.json (all 4 copies) with these metrics'
echo '4. Update knowledge-graph skill RotatE entry'
echo '5. Compare with Mac Mini results when available'
echo '6. Git commit all changes'
echo '7. Run vault_sync.sh'
echo '8. Write RotatE v4.1 report to vault'
echo ''
echo "Completed: $(date)"
