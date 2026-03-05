# CONTINUITY_STATE — SexDiffKG Ecosystem
**Last Updated:** 2026-03-05 05:00 UTC

## CURRENT STATUS: Multiple Training Jobs Running

### Active DGX Processes
- **tmux eval_complex_v5**: ComplEx v5 safe evaluation (50K subset, batch=32, ~65 min)
- **tmux distmult_v5**: DistMult v5 training (epoch ~13/100, ~85 min remaining)
- **tmux derived_chain**: PCOS-ENDO-KG training (epoch ~51/100), then AYUR-PHARMA-KG

### v5 Embedding Training Status
| Model | Status | Notes |
|-------|--------|-------|
| ComplEx v5 | TRAINING COMPLETE, EVALUATING | 100 epochs, loss 0.0486, 220,785 entities, 18 relations. Safe eval running (50K subset). |
| DistMult v5 | TRAINING IN PROGRESS | Epoch 13/100, ~58s/epoch, loss 0.792 |

### Derived KG Embeddings (DistMult 200d, 100ep)
| KG | Entities | Triples | Status | MRR | Hits@10 | AMRI | Time |
|----|----------|---------|--------|-----|---------|------|------|
| REPRODUCT-KG | 13,208 | 384,985 | COMPLETE | 0.1629 | 28.4% | 0.9588 | 10.6 min |
| MENTALHEALTH-KG | 17,555 | 705,561 | COMPLETE | 0.1277 | 22.8% | 0.9669 | 19.9 min |
| GERIPHARM-KG | 18,754 | 739,396 | COMPLETE | 0.1438 | 25.5% | 0.9691 | 20.5 min |
| PCOS-ENDO-KG | ~17K | 697,819 | TRAINING (epoch ~51/100) | -- | -- | -- | -- |
| AYUR-PHARMA-KG | ~11K | 293,444 | QUEUED | -- | -- | -- | -- |

### Completed This Session (Session 11-12)
1. GitHub push blocker FIXED - 1024 files pushed, all under 100MB
2. README updated: RotatE v4.1 correct metrics, v5 section, derived KGs, script list
3. ISMB 2026 poster generated: Publication/ISMB2026_poster.png + .pdf
4. Scripts cleanup: 57 archived to scripts/archive_old/, Makefile fixed
5. Vault docs: 14 stale files fixed (Pipeline_Status, Numbers_Truth_Table, ISMB, etc.)
6. Link prediction script ready: scripts/v5_06_link_prediction.py
7. Paper merges: 4 merge operations (severity, anti-regression, sex paradox, hepatotoxicity)
8. Manuscript PDF generated: Publication/SexDiffKG_Manuscript.pdf
9. bioRxiv badge fixed to "Preprint: In Preparation"
10. Derived KG embeddings: 3/5 COMPLETE, 1 training, 1 queued
11. GROUND_TRUTH.json cleaned - duplicate RotatE_v41 entry archived, RAID synced
12. Vault consistency audit COMPLETE - all issues fixed
13. Manuscript audit: 9 discrepancies found and fixed (RotatE metrics, v3 size, AMRI claims, etc.)
14. CITATION.cff created and pushed to GitHub
15. Paper draft scan: ALL 29 drafts clean (no stale numbers)
16. ISMB abstract AMRI fixed (0.9906->0.9909)
17. Lessons_Learned.md updated with 5 incidents + 2 operational learnings
18. Number verification cascade: 47/48 PASS (1 off-by-1 in triples.tsv)
19. ComplEx v5 training COMPLETE (100 epochs, 2h42m, checkpoint saved)
20. DistMult v5 auto-started via auto_chain_v5.sh
21. ComplEx v5 full evaluation CRASHED (OOM with 637K triples x 220K entities)
22. ComplEx v5 safe evaluation DEPLOYED (50K subset, batch=32)
23. Deep-analysis repo: manuscript + PDF committed (bd90312)

### Phase Status
| Phase | Status | Key Deliverable |
|-------|--------|-----------------|
| 0. Infrastructure | COMPLETE | Drive mount, symlinks, FAERS |
| 2.1 Bridges | COMPLETE | 5 identifier bridges |
| 2.2 Merge | COMPLETE | v5: 246,056 nodes, 3,182,843 edges |
| 2.3 Validate | COMPLETE | 100% v4 preservation, 0 NaN |
| 2.4 Train | IN PROGRESS | ComplEx v5 evaluating, DistMult v5 training |
| 3. Swarms | COMPLETE | 31 waves, 108 JSONs, 121 figures |
| 4. Audit-proof | COMPLETE | FAIR 15/15, repro 97.5%, cascade 91.7% |
| 5. Derived KGs | IN PROGRESS | 5 KGs built, embeddings 3/5 done |
| 6. Publication | IN PROGRESS | README pushed, poster done, PDF done, CITATION.cff done |

### Next Steps (in priority order)
1. Collect ComplEx v5 evaluation results -> update GROUND_TRUTH_v5.json
2. Wait for DistMult v5 to finish -> evaluate -> update GROUND_TRUTH_v5.json
3. Wait for PCOS-ENDO-KG + AYUR-PHARMA-KG -> update derived KG ground truth
4. Run v5 link predictions (script ready: scripts/v5_06_link_prediction.py)
5. Update CONTINUITY_STATE + vault with all final metrics
6. Commit remaining results to GitHub repos
7. Submit bioRxiv/medRxiv preprint (manuscript PDF ready)
8. Upload Zenodo v4 deposit

### GitHub Repos
- **Main**: github.com/jshaik369/SexDiffKG - PUSHED (latest: 23a847a, CITATION.cff)
- **Deep Analysis**: github.com/jshaik369/sexdiffkg-deep-analysis - PUSHED (bd90312)

### Model Performance (v4 canonical)
| Model | MRR | Hits@1 | Hits@10 | AMRI |
|-------|-----|--------|---------|------|
| ComplEx v4 | 0.2484 | 16.78% | 40.69% | 0.9902 |
| RotatE v4.1 | 0.2018 | 11.28% | 36.77% | 0.9922 |
| DistMult v4.1 | 0.1013 | 4.81% | 19.61% | 0.9909 |

### GROUND_TRUTH.json RAID: 4 copies verified identical (session 11)

### Recovery Protocol
If starting a new session, read in order:
1. This file (CONTINUITY_STATE.md) - both copies
2. GROUND_TRUTH.json (canonical at sexdiffkg/GROUND_TRUTH.json)
3. GROUND_TRUTH_v5.json (vault)
4. Lessons_Learned.md
5. `tmux ls` on DGX
6. Latest Session_Log in vault
