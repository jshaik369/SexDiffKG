# SexDiffKG v5.2 Continuity State

## Updated: 2026-03-08T17:30Z

## Current Status: AUDIT-PROOF — RotatE v5.2 EVALUATION IN PROGRESS

### Embedding Training Status:
- **ComplEx v5.2 DONE**: MRR 0.1629, Hits@1 4.72%, Hits@10 37.0%, AMRI 0.983 (epoch 25, early stopped)
- **DistMult v5.2 DONE**: MRR 0.0548, Hits@1 2.87%, Hits@10 9.95%, AMRI 0.983 (epoch 10, eval 485 min)
- **RotatE v5.2 IN PROGRESS**: PID 408479, ~43h elapsed, epoch 5 evaluation (~28-30h estimated)
  - Training loss: 0.176 → 0.0549 → 0.0142 → 0.00535 → 0.00393 (epochs 1-5)
  - Checkpoint: rotate_v52_checkpoint.pt (1.0 GB), mtime 1772876649 (Mar 7 10:44)
  - Evaluation started: Mar 7 12:05 CET (log mtime 1772881536)
  - DistMult eval took 485 min (8h). RotatE ~3.5x slower = ~28h
  - After eval: epochs 6-10 training (~6h48m), then next eval cycle (~28h)
  - Estimated full completion: Mar 13-16 (6-10 total eval cycles)

### Session 21 Work (Mar 8):
- Fixed v3 strong signal artifacts in papers 06, 09, 24:
  - 49,026 → 32,244 (|logR| >= 1.0)
  - 28,669/20,357 → 18,174/14,070 (v4 F/M at |logR| >= 1.0)
  - Fixed confidence tier table in atlas paper
  - Fixed extreme signal labels (proportion-based definition)
- Fixed README: ComplEx v5.2 Hits@1 (0.0975→0.0472), BibTeX key
- Created AUDIT_PACKAGE.md (371 lines, 2 RAID copies)
- Added threshold breakdowns to GROUND_TRUTH.json (all 4 RAID copies)
- Updated AYURFEM skill and knowledge-graph skill (v3 wrong numbers list)
- Git pushes: 103ac9a (paper fixes + audit package), 1cb1d41 (GROUND_TRUTH)

### Publication Status: 29 PAPERS — ALL AUDITED ✓
- Total: 1.31 MB across 29 papers (all >= 35 KB)
- All v3 artifacts purged (49,026, 28,669, 20,357 removed)
- Numbers verified against GROUND_TRUTH.json

### Zenodo Deposit: READY FOR UPLOAD
- Archive: zenodo/SexDiffKG_v4_deposit.tar.gz (274 MB, 48 files)
- User action required

### What to Do Next:
1. Monitor RotatE v5.2 (eval should complete Mar 8-9, then more training cycles)
2. When RotatE completes: extract results → update GROUND_TRUTH → commit → push
3. Upload Zenodo deposit (user action)
4. Submit medRxiv preprint (user action)
5. Begin journal submissions per publishing_strategy.md timeline

### GitHub Commits This Session:
| Commit | Description |
|--------|-------------|
| 103ac9a | Fix v3 strong signal artifacts, add AUDIT_PACKAGE.md |
| 1cb1d41 | Add threshold breakdowns to GROUND_TRUTH.json |
