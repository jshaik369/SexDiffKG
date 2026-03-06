# SexDiffKG v5.2 Continuity State

## Updated: 2026-03-06T13:00Z

## Current Status: 130-WAVE MILESTONE — SESSION 16 IN PROGRESS

### Training Status:
- **ComplEx v5.2 DONE**: MRR 0.1629, Hits@10 37.0%, AMRI 0.983, epoch 25 (early stopped)
  - 6.6x improvement over v5 (0.025), 34% below v4 (0.248) — expected for 2x entity KG
  - Recovered from crash (temp dir cleaned during eval). Best weights intact.
- **DistMult v5.2 RESUMING**: From checkpoint epoch 14, best MRR 0.0434 (epoch 10)
  - Running in tmux v52_recover on DGX
- **RotatE v5.2 QUEUED**: After DistMult completes

### KG v5.2 (Merged SexDiffKG v4 + VEDA-KG):
- Nodes: 217,993 (13 types)
- Edges: 3,194,017 (18 types)
- Path: data/kg_v5.2/

### Deep Analysis Progress:
- **130 WAVES** across 16 sessions (121-128 done, 129-130 running)
- Total JSON results: ~130
- Total figures: ~390
- Permanent storage: results/deep_analysis/ (waves 121-128 copied)

### DGX Reboot Recovery (Mar 6, 2026):
- DGX rebooted ~09:00 UTC, /tmp wiped
- ComplEx training was complete, DistMult killed at epoch 14
- Waves 121-128 results were in /tmp — RE-EXECUTED all 10 waves
- Recovery script: /tmp/v52_recover_and_resume.py
- Permanent copy: results/deep_analysis/{results,figures}/

### Session 16: CTD/NPASS/LOTUS Integration (Waves 121-130):
- W121: CTD Chem-Gene Sex-Bias — 577 drugs bridged, phosphorylation=62.4%F, binding=39.1%F
- W122: NPASS NP Target Atlas — 5,516 NPs, PPAR-gamma=93.6%F, ER=0%F
- W123: LOTUS Organism Pathway — 10,248 organisms, marine sponges most F-biased
- W124: CTD Disease Landscape — 1,084 diseases, cancer=63.9%F
- W125: Cross-DB Safety Profile — 873 toxic NPs, Vitis vinifera=443 compounds
- W126: Gene-Mediated Bias — 12,570 genes, ZMAT3=68.5%F high-confidence
- W127: Activity Types — Kd=56.6%F, MIC/Potency male-biased
- W128: Plant Family Atlas — 665 families, Theonellidae=78.3%F
- W129: Disease-NP Opportunities — RUNNING
- W130: Session Summary — QUEUED

### External Databases:
- **CTD**: 7 files, 3.3GB at data/raw/ctd/ — 3M human chem-gene, 109K direct chem-disease
- **NPASS 3.0**: 8 files, 215MB at data/raw/npass/ — 204K NPs, 1.05M activities, 8.8K targets
- **LOTUS**: 5 files, 268MB at data/raw/lotus/ — 222K compounds, 661K pairs, 37K taxa
- **Bridge**: 114K InChIKey overlap (LOTUS-NPASS), 793 UniProt targets, 938 CTD drugs

### Next Steps:
1. Complete waves 129-130
2. DistMult + RotatE training to completion
3. Push results to GitHub
4. Update vault with final training results
5. Phase 1: publication tasks (blocked on user)
