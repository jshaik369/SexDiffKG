# SexDiffKG v5.2 Continuity State

## Updated: 2026-03-08T20:00Z

## Current Status: RotatE v5.2 TRAINING EPOCH 6 — Epoch 5 MRR 0.1363

### Embedding Training Status:
- **ComplEx v5.2 DONE**: MRR 0.1629, Hits@1 4.72%, Hits@10 37.0%, AMRI 0.983 (epoch 25, early stopped)
- **DistMult v5.2 DONE**: MRR 0.0548, Hits@1 2.87%, Hits@10 9.95%, AMRI 0.983 (epoch 10, eval 485 min)
- **RotatE v5.2 IN PROGRESS**: PID 408479, ~48h elapsed
  - **Epoch 5 evaluation COMPLETE: MRR 0.1363** (new best, saved model)
  - Evaluation took 102,914s = 28.6 hours (batch_size=32 on CPU)
  - Training loss: 0.176 → 0.0549 → 0.0142 → 0.00535 → 0.00393 (epochs 1-5)
  - Now training epoch 6 (12% at last check, ~82 min/epoch)
  - Next eval at epoch 10: ~6.5h training + ~28.6h eval = ~35h until next result
  - Early stopping: if no improvement over 5 consecutive evals → stops
  - Estimated completion: Mar 13-16 (depending on improvement pattern)

### v5.2 Model Comparison:
| Model | MRR | Hits@10 | vs v4 ComplEx |
|-------|-----|---------|---------------|
| ComplEx v5.2 | 0.1629 | 37.0% | -34.4% |
| RotatE v5.2 (ep5) | 0.1363 | TBD | -45.1% |
| DistMult v5.2 | 0.0548 | 9.9% | -77.9% |

### Session 21 Work (Mar 8, earlier):
- Fixed v3 strong signal artifacts in papers 06, 09, 24
- Fixed README: ComplEx v5.2 Hits@1, BibTeX key
- Created AUDIT_PACKAGE.md (371 lines, 2 RAID copies)
- Created CITATION.cff, FAIR_compliance.md
- Added threshold breakdowns to GROUND_TRUTH.json (all 4 RAID copies)
- Updated skills (AYURFEM + knowledge-graph)
- 5 Git pushes: 103ac9a, 1cb1d41, 38d38b4, 6f4913f, ce31d41

### Session 22 Work (Mar 8, current):
- Confirmed RotatE epoch 5 MRR = 0.1363 (eval took 28.6h)
- Now training epoch 6, next eval ~35h away

### Publication Status: 29 PAPERS — ALL AUDITED ✓
- Total: 1.31 MB across 29 papers (all >= 35 KB)
- All v3 artifacts purged
- Numbers verified against GROUND_TRUTH.json

### What to Do Next:
1. Monitor RotatE v5.2 (next eval ~35h, epoch 10)
2. When RotatE completes all eval cycles: extract final results → update GROUND_TRUTH → commit → push
3. Upload Zenodo deposit (user action required)
4. Submit medRxiv preprint (user action required)
5. Begin journal submissions per publishing_strategy.md timeline
