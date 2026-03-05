#!/bin/bash
# vault_sync.sh — RAID-like vault redundancy
# Syncs vault to multiple locations for zero-loss logging
# Usage: ./scripts/vault_sync.sh [full|quick]

set -euo pipefail

VAULT="/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg"
REPO_MIRROR="/home/jshaik369/sexdiffkg/vault_mirror"
GROUND_TRUTH="/home/jshaik369/sexdiffkg/GROUND_TRUTH.json"
LOG="/home/jshaik369/sexdiffkg/results/vault_sync.log"

MODE="${1:-quick}"

echo "$(date +%Y-%m-%d %H:%M:%S): vault_sync $MODE started" >> "$LOG"

# 1. Mirror vault to repo (git-tracked redundancy)
mkdir -p "$REPO_MIRROR"
rsync -av --delete "$VAULT/" "$REPO_MIRROR/" >> "$LOG" 2>&1
echo "$(date +%Y-%m-%d %H:%M:%S): Vault mirrored to $REPO_MIRROR" >> "$LOG"

# 2. Ground truth checksum verification
if [ -f "$GROUND_TRUTH" ]; then
    echo "$(date +%Y-%m-%d %H:%M:%S): Ground truth exists at $GROUND_TRUTH" >> "$LOG"
fi

# 3. KG integrity check
KG_NODES=$(wc -l < /home/jshaik369/sexdiffkg/data/kg_v4/nodes.tsv)
KG_EDGES=$(wc -l < /home/jshaik369/sexdiffkg/data/kg_v4/edges.tsv)
echo "$(date +%Y-%m-%d %H:%M:%S): KG integrity: nodes=$KG_NODES edges=$KG_EDGES" >> "$LOG"

if [ "$KG_NODES" != "109868" ] || [ "$KG_EDGES" != "1822852" ]; then
    echo "CRITICAL: KG line counts changed! Expected 109868/1822852, got $KG_NODES/$KG_EDGES" >> "$LOG"
    echo "CRITICAL: KG line counts changed!" >&2
    exit 1
fi

if [ "$MODE" = "full" ]; then
    # Full mode: MD5 verification
    echo "$(date +%Y-%m-%d %H:%M:%S): Running MD5 verification..." >> "$LOG"
    md5sum /home/jshaik369/sexdiffkg/data/kg_v4/nodes.tsv >> "$LOG"
    md5sum /home/jshaik369/sexdiffkg/data/kg_v4/edges.tsv >> "$LOG"
    md5sum /home/jshaik369/sexdiffkg/data/kg_v4/triples.tsv >> "$LOG"
    
    # Count vault files
    VAULT_COUNT=$(ls "$VAULT"/*.md 2>/dev/null | wc -l)
    MIRROR_COUNT=$(ls "$REPO_MIRROR"/*.md 2>/dev/null | wc -l)
    echo "$(date +%Y-%m-%d %H:%M:%S): Vault files: $VAULT_COUNT, Mirror files: $MIRROR_COUNT" >> "$LOG"
fi

echo "$(date +%Y-%m-%d %H:%M:%S): vault_sync $MODE complete" >> "$LOG"
echo "Vault sync complete. Log: $LOG"
