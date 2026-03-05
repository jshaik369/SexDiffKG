# CONTINUITY_STATE — SexDiffKG Ecosystem
**Last Updated:** 2026-03-05 07:15 UTC (Session 12 final)

## CURRENT STATUS: All Training & Evaluation COMPLETE

### v5 Embedding Results (merged KG: 246,056 nodes, 3,182,843 edges)
| Model | MRR | Hits@10 | AMRI | Eval Time | Note |
|-------|-----|---------|------|-----------|------|
| ComplEx v5 | 0.0247 | 5.8% | 0.929 | 68 min | 50K subset. -90% vs v4 (expected: 2x entities, 3x relations) |
| DistMult v5 | 0.0413 | 7.8% | 0.9884 | 49 min | 50K subset |

### v4 Canonical Model Performance
| Model | MRR | Hits@1 | Hits@10 | AMRI |
|-------|-----|--------|---------|------|
| ComplEx v4 | 0.2484 | 16.78% | 40.69% | 0.9902 |
| RotatE v4.1 | 0.2018 | 11.28% | 36.77% | 0.9922 |
| DistMult v4.1 | 0.1013 | 4.81% | 19.61% | 0.9909 |

### Derived KG Embeddings (ALL 5 COMPLETE, DistMult 200d, 100ep)
| KG | Entities | Triples | MRR | Hits@10 | AMRI | Time |
|----|----------|---------|-----|---------|------|------|
| REPRODUCT-KG | 13,208 | 384,985 | 0.1629 | 28.4% | 0.9588 | 10.6 min |
| GERIPHARM-KG | 18,754 | 739,396 | 0.1438 | 25.5% | 0.9691 | 20.5 min |
| MENTALHEALTH-KG | 17,555 | 705,561 | 0.1277 | 22.8% | 0.9669 | 19.9 min |
| AYUR-PHARMA-KG | 24,316 | 293,444 | 0.0887 | 17.6% | 0.9725 | 11.1 min |
| PCOS-ENDO-KG | 36,903 | 697,819 | 0.0675 | 13.4% | 0.9803 | 25.0 min |

### Completed (Sessions 11-12, Mar 4-5 2026)
1. GitHub push blocker FIXED - 1024 files pushed, all under 100MB
2. README updated: RotatE v4.1 correct metrics, v5 section, derived KGs
3. ISMB 2026 poster: Publication/ISMB2026_poster.png + .pdf
4. Scripts cleanup: 57 archived to scripts/archive_old/, Makefile fixed
5. Vault docs: 14 stale files fixed
6. Link prediction script ready + 550 v5 predictions generated
7. Paper merges: 4 merge operations
8. Manuscript PDF generated
9. bioRxiv badge fixed to "Preprint: In Preparation"
10. ALL 5 derived KG embeddings COMPLETE
11. GROUND_TRUTH.json cleaned - RAID synced (4 copies identical)
12. Vault consistency audit COMPLETE
13. Manuscript audit: 9 discrepancies fixed
14. CITATION.cff created and pushed
15. Paper draft scan: ALL 29 drafts clean
16. ComplEx v5 training + evaluation COMPLETE
17. DistMult v5 training + evaluation COMPLETE
18. Cross-document audit: 7 issues found and fixed
19. Model comparison JSON: all versions + derived KGs
20. Deep-analysis repo: 244 analysis files, 316 figures, pushed

### Phase Status
| Phase | Status | Key Deliverable |
|-------|--------|-----------------|
| 0. Infrastructure | COMPLETE | Drive mount, symlinks, FAERS |
| 2.1 Bridges | COMPLETE | 5 identifier bridges |
| 2.2 Merge | COMPLETE | v5: 246,056 nodes, 3,182,843 edges |
| 2.3 Validate | COMPLETE | 100% v4 preservation, 0 NaN |
| 2.4 Train | COMPLETE | ComplEx v5 + DistMult v5 evaluated |
| 3. Swarms | COMPLETE | 31 waves, 108 JSONs, 121 figures |
| 4. Audit-proof | COMPLETE | FAIR 15/15, repro 97.5%, cascade 91.7% |
| 5. Derived KGs | COMPLETE | 5 KGs built, all embeddings done |
| 6. Publication | IN PROGRESS | README pushed, poster done, PDF done, CITATION.cff done |

### Next Steps (priority order)
1. Upload Zenodo v4 deposit (archive ready, needs user login)
2. Submit medRxiv preprint (manuscript PDF ready, needs user action)
3. Consider higher-capacity v5 training (400d, 200ep) if v5 MRR improvement desired
4. Run full-KG evaluation on GPU when available (CPU 50K subset used for now)
5. Commit remaining results to GitHub repos
6. Staggered journal submissions (Papers A-L)

### GitHub Repos
- **Main**: github.com/jshaik369/SexDiffKG (latest: 735f849)
- **Deep Analysis**: github.com/jshaik369/sexdiffkg-deep-analysis (latest: a8c3093)

### GROUND_TRUTH RAID: All copies verified identical (session 12 audit)

### Recovery Protocol
If starting a new session, read in order:
1. This file (CONTINUITY_STATE.md) - both copies
2. GROUND_TRUTH.json (canonical at sexdiffkg/GROUND_TRUTH.json)
3. GROUND_TRUTH_v5.json (vault)
4. Lessons_Learned.md
5. `tmux ls` on DGX
6. Latest Session_Log in vault
