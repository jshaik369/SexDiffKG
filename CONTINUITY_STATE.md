# CONTINUITY_STATE — SexDiffKG Ecosystem
**Last Updated:** 2026-03-05 03:49 UTC

## CURRENT STATUS: Active Multi-Front Work

### Training Active
- **ComplEx v5**: Epoch ~70/100, loss 0.060, ~30 min remaining (tmux complex_v5)
- **Auto-chain**: tmux auto_chain_v5 — will start DistMult v5 after ComplEx finishes
- **DistMult v5**: Script ready at scripts/v5_05_train_distmult.py

### Completed This Session
1. GitHub push blocker FIXED — 1024 files pushed, all under 100MB
2. README updated: RotatE v4.1 correct metrics, v5 section, derived KGs, script list
3. ISMB 2026 poster generated: Publication/ISMB2026_poster.png + .pdf
4. Scripts cleanup: 57 archived to scripts/archive_old/, Makefile fixed
5. Vault docs: 14 stale files fixed (Pipeline_Status, Numbers_Truth_Table, ISMB, etc.)
6. Link prediction script ready: scripts/v5_06_link_prediction.py
7. Paper merges: 4 merge operations (severity, anti-regression, sex paradox, hepatotoxicity)

### Phase Status
| Phase | Status | Key Deliverable |
|-------|--------|-----------------|
| 0. Infrastructure | COMPLETE | Drive mount, symlinks, FAERS |
| 2.1 Bridges | COMPLETE | 5 identifier bridges |
| 2.2 Merge | COMPLETE | v5: 246,056 nodes, 3,182,843 edges |
| 2.3 Validate | COMPLETE | 100% v4 preservation, 0 NaN |
| 2.4 Train | IN PROGRESS | ComplEx v5 ~70/100, DistMult queued |
| 3. Swarms | COMPLETE | 31 waves, 108 JSONs, 121 figures |
| 4. Audit-proof | COMPLETE | FAIR 15/15, repro 97.5%, cascade 91.7% |
| 5. Derived KGs | COMPLETE | 5 KGs built (v0.1 subgraphs) |
| 6. Publication | IN PROGRESS | README pushed, poster done, papers merging |

### Next Steps (in priority order)
1. Wait for ComplEx v5 to finish → auto-chain starts DistMult v5
2. Run link predictions on v5 KG (scripts/v5_06_link_prediction.py)
3. Commit merged papers to deep-analysis repo
4. Generate PDF from manuscript_scidata_COMPLETE.md
5. Start derived KG embeddings (REPRODUCT-KG, MENTALHEALTH-KG)
6. Submit bioRxiv preprint (check current DOI status)
7. Upload Zenodo v4 deposit

### GitHub Repos
- **Main**: github.com/jshaik369/SexDiffKG — PUSHED (47fe086)
- **Deep Analysis**: github.com/jshaik369/sexdiffkg-deep-analysis — up to date

### Derived KGs (all v0.1)
| KG | Nodes | Edges | Embeddings | Papers |
|----|-------|-------|------------|--------|
| REPRODUCT-KG | 22,403 | 1,116,735 | Not started | Not started |
| MENTALHEALTH-KG | 20,851 | 762,389 | Not started | Not started |
| GERIPHARM-KG | 18,754 | 739,396 | Not started | Not started |
| PCOS-ENDO-KG | 36,903 | 697,819 | Not started | Not started |
| AYUR-PHARMA-KG | 24,316 | 293,444 | Not started | Not started |

### Model Performance (v4 canonical)
| Model | MRR | Hits@10 | AMRI |
|-------|-----|---------|------|
| ComplEx v4 | 0.2484 | 40.69% | 0.9902 |
| RotatE v4.1 | 0.2018 | 36.77% | 0.9922 |
| DistMult v4.1 | 0.1013 | 19.61% | 0.9909 |

### GROUND_TRUTH.json RAID: 4 copies verified identical
