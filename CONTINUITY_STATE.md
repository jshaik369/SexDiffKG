# SexDiffKG v5.2 Continuity State

## Updated: 2026-03-08T15:45Z

## Current Status: AUDIT-PROOF — RotatE v5.2 EVALUATION IN PROGRESS

### Embedding Training Status:
- **ComplEx v5.2 DONE**: MRR 0.1629, Hits@1 4.72%, Hits@10 37.0%, AMRI 0.983 (epoch 25, early stopped)
- **DistMult v5.2 DONE**: MRR 0.0548, Hits@1 2.87%, Hits@10 9.95%, AMRI 0.983 (epoch 10, eval 485 min)
- **RotatE v5.2 IN PROGRESS**: PID 408479, ~42h elapsed, epoch 5 evaluation (~27h/~28h estimated)
  - Process: R state, 1107% CPU, 15.7 GB RSS, 50 threads
  - Training loss: 0.176 → 0.0549 → 0.0142 → 0.00535 → 0.00393 (epochs 1-5)
  - Checkpoint: rotate_v52_checkpoint.pt (1.0 GB), mtime 1772876649 (Mar 7 10:44)
  - DGX monitor: PID 2813207 checking every 5 min
  - After eval: epochs 6-10 training (~6h48m), then next eval cycle
  - Estimated completion: Mar 13-16 (6-10 total eval cycles, 23h each)

### Publication Status: 29 PAPERS — ALL AUDITED ✓
Total: 1.31 MB across 29 papers (all >= 35 KB)
- Git: Publication/papers/01-29_*.md (commit d778a7a)
- All numbers verified against GROUND_TRUTH.json (Mar 8 audit)
- Fixes applied: 5,658→5,069 AEs (24 files), F/M counts (4 files), quarters 86→87 (3 files)

### GitHub Pushes (Session 20):
- d778a7a: 29 audited papers
- 328a990: v5.2 KG data + embeddings via Git LFS (921 MB)
- 5b78498: Publishing strategy v2 + medRxiv checklist
- be20435: v5.1 gitignore
- a8f6f36: GROUND_TRUTH.json ComplEx v5.2 exact metrics

### Zenodo Deposit: READY FOR UPLOAD
- Archive: zenodo/SexDiffKG_v4_deposit.tar.gz (274 MB, 48 files)
- Contains: KG (nodes/edges/triples), signals (96,281 + 32,244 strong), 
  ComplEx model (181 MB), DistMult model (87 MB), figures, validation, GROUND_TRUTH.json
- User action required: Upload via Zenodo web UI

### GROUND_TRUTH.json: CURRENT ✓
- 4 copies synced (md5: all match)
- ComplEx v5.2 exact metrics filled (hits_at_1 was null → 0.0472)
- Last verified: 2026-03-08T15:30

### What to Do Next:
1. Monitor RotatE v5.2 (eval should complete ~Mar 8 17:00, then epochs 6-10)
2. When RotatE completes: extract results → update GROUND_TRUTH → commit → push
3. Upload Zenodo deposit (user action)
4. Submit medRxiv preprint (user action)
5. Begin journal submissions per publishing_strategy.md timeline

### Critical Files:
| File | Status |
|------|--------|
| GROUND_TRUTH.json (4 copies) | CURRENT ✓ |
| Publication/papers/ (29 files) | AUDITED ✓ |
| Publication/publishing_strategy.md | UPDATED v2 ✓ |
| Publication/medrxiv_submission_checklist.md | NEW ✓ |
| zenodo/SexDiffKG_v4_deposit.tar.gz | READY (274 MB) ✓ |
| data/kg_v5.2/ | IN GITHUB (LFS) ✓ |
| results/kg_embeddings_v5.2/ | ComplEx+DistMult DONE, RotatE IN PROGRESS |
