# CONTINUITY STATE — SexDiffKG Project
**Last updated:** 2026-03-05 10:47 UTC (Session 12 continued)

## Current Status: v5.2 TRAINING IN PROGRESS

### What Just Happened
1. v4 data quality patch COMPLETE — 3,288 missing drugs added, 290,177 dupes removed
2. v5 repair analysis COMPLETE — found 3 disconnected subgraphs, only 8 name bridges
3. v5.1 LCC extracted but INADEQUATE — only 46.8% v4 preservation
4. **v5.2 bridge build COMPLETE** — 13,167 bridge edges (same_gene + encodes) connected all 3 subgraphs
5. **v5.2 ComplEx training LAUNCHED** — tmux `v52_train`, 5-trial HPO + 500 epoch full training

### v5.2 KG (Current Best Merged)
- **217,993 nodes** (98.7% of v5 entities)
- **3,194,017 edges** (18 relation types)
- **100% v4 preservation** (all 1,532,674 unique v4 triples kept)
- 13 node types, 18 edge types (2 new: same_gene, encodes)
- Path: `data/kg_v5.2/`

### Running Processes
- `tmux v52_train` — ComplEx v5.2 HPO + training (started 10:47 UTC)
- Log: `results/kg_embeddings_v5.2/training.log`

### What To Do Next
1. Monitor v5.2 training (`tmux attach -t v52_train` or `tail -f results/kg_embeddings_v5.2/training.log`)
2. After training completes: compare MRR to v4 baseline (0.2484)
3. If v5.2 MRR competitive: update GROUND_TRUTH, train DistMult + RotatE
4. If v5.2 MRR poor: investigate why, consider regularization or loss function changes
5. Clean up v5.1 directory (superseded by v5.2)
6. Update deep-analysis repo with v5.2 results

### Ground Truth Hierarchy
- v4 canonical: `data/kg_v4/` — GROUND_TRUTH.json (4 copies)
- v4 patched: `data/kg_v4/nodes_patched.tsv`, `edges_deduped.tsv`, `triples_deduped.tsv`
- v5 merged (raw): `data/kg_v5/` — GROUND_TRUTH_v5.json
- v5.1 LCC (deprecated): `data/kg_v5.1/` — 46.8% v4 preservation, SUPERSEDED
- **v5.2 bridged LCC**: `data/kg_v5.2/` — 100% v4 preservation, CURRENT BEST

### Models
| Model | KG | MRR | Hits@10 | AMRI | Status |
|-------|-----|-----|---------|------|--------|
| ComplEx v4 | v4 | 0.2484 | 0.4069 | 0.9902 | BASELINE |
| DistMult v4.1 | v4 | 0.1013 | 0.1961 | 0.9909 | Complete |
| RotatE v4.1 | v4 | 0.2018 | 0.3677 | 0.9922 | Complete |
| ComplEx v5 | v5 | 0.0247 | 0.058 | — | Bad (disconnected graph) |
| DistMult v5 | v5 | 0.0413 | 0.100 | — | Bad (disconnected graph) |
| ComplEx v5.2 | v5.2 | ? | ? | ? | TRAINING |
