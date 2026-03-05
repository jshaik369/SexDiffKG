# CONTINUITY_STATE — SexDiffKG Ecosystem
**Last Updated:** 2026-03-05 04:35 UTC

## CURRENT STATUS: Training Chain Running Autonomously

### Training Active
- **ComplEx v5**: Training in tmux complex_v5 (loss ~0.050, well converged)
- **Auto-chain**: tmux auto_chain_v5 — monitoring ComplEx, will start DistMult v5 evaluation + training
- **Derived KG chain**: tmux derived_chain — training 5 derived KG embeddings sequentially
- **DistMult v5**: Script ready at scripts/v5_05_train_distmult.py, queued after ComplEx v5

### Derived KG Embeddings (Running)
- REPRODUCT-KG: **COMPLETE** — MRR 0.1629, Hits@10 28.4%, AMRI 0.9588 (10.6 min)
- MENTALHEALTH-KG: **COMPLETE** — MRR 0.1277, Hits@10 22.8%, AMRI 0.9669 (19.9 min)
- GERIPHARM-KG: **IN PROGRESS** (739,396 triples, training)
- PCOS-ENDO-KG: Queued (697,819 triples)
- AYUR-PHARMA-KG: Queued (293,444 triples)

### Completed This Session (Session 11)
1. GitHub push blocker FIXED — 1024 files pushed, all under 100MB
2. README updated: RotatE v4.1 correct metrics, v5 section, derived KGs, script list
3. ISMB 2026 poster generated: Publication/ISMB2026_poster.png + .pdf
4. Scripts cleanup: 57 archived to scripts/archive_old/, Makefile fixed
5. Vault docs: 14 stale files fixed (Pipeline_Status, Numbers_Truth_Table, ISMB, etc.)
6. Link prediction script ready: scripts/v5_06_link_prediction.py
7. Paper merges: 4 merge operations (severity, anti-regression, sex paradox, hepatotoxicity)
8. Manuscript PDF generated: Publication/SexDiffKG_Manuscript.pdf
9. bioRxiv badge fixed to "Preprint: In Preparation"
10. Derived KG embeddings training started (2/5 complete)
11. GROUND_TRUTH.json cleaned — duplicate RotatE_v41 entry archived
12. Vault consistency audit in progress

### Phase Status
| Phase | Status | Key Deliverable |
|-------|--------|-----------------|
| 0. Infrastructure | COMPLETE | Drive mount, symlinks, FAERS |
| 2.1 Bridges | COMPLETE | 5 identifier bridges |
| 2.2 Merge | COMPLETE | v5: 246,056 nodes, 3,182,843 edges |
| 2.3 Validate | COMPLETE | 100% v4 preservation, 0 NaN |
| 2.4 Train | IN PROGRESS | ComplEx v5 running, DistMult queued |
| 3. Swarms | COMPLETE | 31 waves, 108 JSONs, 121 figures |
| 4. Audit-proof | COMPLETE | FAIR 15/15, repro 97.5%, cascade 91.7% |
| 5. Derived KGs | IN PROGRESS | 5 KGs built, embeddings 2/5 done |
| 6. Publication | IN PROGRESS | README pushed, poster done, PDF done |

### Next Steps (in priority order)
1. Wait for ComplEx v5 → auto-chain evaluates + starts DistMult v5
2. Wait for all 5 derived KG embeddings to complete
3. Run link predictions on v5 KG (automatic via derived_chain)
4. Update GROUND_TRUTH_v5 with ComplEx v5 metrics
5. Commit remaining results to repos
6. Submit bioRxiv/medRxiv preprint (manuscript PDF ready)
7. Upload Zenodo v4 deposit

### GitHub Repos
- **Main**: github.com/jshaik369/SexDiffKG — PUSHED (c45ae35)
- **Deep Analysis**: github.com/jshaik369/sexdiffkg-deep-analysis — up to date

### Derived KGs (v0.1)
| KG | Nodes | Edges | Triples | Embeddings |
|----|-------|-------|---------|------------|
| REPRODUCT-KG | 22,403 | 1,116,735 | 384,985 | MRR 0.1629 |
| MENTALHEALTH-KG | 20,851 | 762,389 | 705,561 | MRR 0.1277 |
| GERIPHARM-KG | 18,754 | 739,396 | 739,396 | Training... |
| PCOS-ENDO-KG | 36,903 | 697,819 | 697,819 | Queued |
| AYUR-PHARMA-KG | 24,316 | 293,444 | 293,444 | Queued |

### Model Performance (v4 canonical)
| Model | MRR | Hits@10 | AMRI |
|-------|-----|---------|------|
| ComplEx v4 | 0.2484 | 40.69% | 0.9902 |
| RotatE v4.1 | 0.2018 | 36.77% | 0.9922 |
| DistMult v4.1 | 0.1013 | 19.61% | 0.9909 |

### GROUND_TRUTH.json RAID: 4 copies verified identical (cleaned session 11)
