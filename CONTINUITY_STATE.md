# SexDiffKG v5.2 Continuity State

## Updated: 2026-03-07T14:30Z

## Current Status: ALL 29 PAPERS EXPANDED — RotatE v5.2 TRAINING IN PROGRESS

### Training Status:
- **ComplEx v5.2 DONE**: MRR 0.1629, Hits@10 37.0%, AMRI 0.983, epoch 25 (early stopped)
- **DistMult v5.2 DONE**: MRR 0.0548, Hits@10 9.9%, AMRI 0.9884
- **RotatE v5.2 IN PROGRESS**: PID 408479, ~24h elapsed, epoch 6 evaluation in progress
  - RSS cycling: ~6 GB (training) ↔ ~15 GB (evaluation)
  - Checkpoint at epoch 5: rotate_v52_checkpoint.pt (1.0 GB), saved 10:44 Mar 7
  - Early stopping patience=5, best loss 0.00393 (epoch 5)
  - Log: eval_rotate.log (3.1 MB, tqdm carriage returns)

### Publication Status: ALL 29 PAPERS >= 15 KB
Total manuscript volume: ~890 KB across 29 papers
- Smallest: two_axis_model_paper.md (15.5 KB)
- Largest: drug_safety_sex_atlas_paper.md (56.9 KB)
- Git commit: 60a6575, pushed to GitHub
- All papers in Publication/drafts/

### Paper List (29 papers, all >= 15 KB):
1. drug_safety_sex_atlas_paper.md (56.9 KB) — Capstone atlas
2. comprehensive_methods_paper.md (56.0 KB) — Analytical methods companion
3. sexdiffkg_methods_paper.md (52.4 KB) — KG construction paper
4. clinical_urgency_paper.md (46.0 KB) — 108 urgent signals
5. organ_system_landscape_paper.md (43.5 KB) — Cross-organ drug class effects
6. extreme_signals_paper.md (43.5 KB) — 14.4:1 female:male asymmetry
7. rare_disease_paradox_paper.md (42.8 KB) — Orphan vs common drugs
8. network_topology_paper.md (41.9 KB) — Bipartite drug-AE network
9. bidirectional_ae_paper.md (39.5 KB) — 1,178 context-dependent AEs
10. glp1ra_diabetes_paper.md (37.0 KB) — GLP-1 male bias
11. CPI_irAE_paper.md (36.8 KB) — Checkpoint inhibitor irAEs
12. organ_system_architecture_paper.md (36.2 KB) — SOC anti-regression
13. cardiac_reversal_paper.md (35.2 KB) — Cardiotoxicity sex reversal
14. embedding_paper.md (32.0 KB) — KG embedding methods
15. severity_sex_gradient_paper.md (29.4 KB) — Severity-sex correlation
16. anti_regression_unified_paper.md (27.5 KB) — Anti-regression phenomenon
17. soc_atlas_paper.md (24.6 KB) — 20-SOC atlas
18. regulatory_paper.md (22.1 KB) — Regulatory implications
19. age_sex_interaction_paper.md (21.5 KB) — Age-sex-severity
20. cardiotoxicity_sex_paper.md (20.6 KB) — Cardiotoxicity spectrum
21. information_theory_paper.md (19.1 KB) — Entropy analysis
22. drug_target_sex_paper.md (18.9 KB) — Molecular sex axis
23. hepatotoxicity_paper.md (18.4 KB) — DILI sex patterns
24. temporal_instability_paper.md (17.7 KB) — Volume-sex gradient
25. cross_therapeutic_spectrum_paper.md (17.7 KB) — 68pp pan-therapeutic
26. nephrotoxicity_sex_paper.md (17.0 KB) — Renal male enrichment
27. sex_paradox_paper.md (16.2 KB) — Sex paradox framework
28. reproductive_paradox_paper.md (16.1 KB) — HRT inversion
29. two_axis_model_paper.md (15.5 KB) — Strength x volume 2D

### KG v5.2 (Merged SexDiffKG v4 + VEDA-KG):
- Nodes: 217,993 (13 types)
- Edges: 3,194,017 (18 types)
- Path: data/kg_v5.2/

### Deep Analysis: 130 WAVES COMPLETE
- Total JSON results: ~200+
- Total figures: ~390+
- All pushed to GitHub (deep-analysis repo)

### Next Steps:
1. Wait for RotatE v5.2 to complete (epoch 6+ evaluation, early stopping at patience 5)
2. Extract RotatE embeddings and save results JSON
3. Update GROUND_TRUTH.json with RotatE metrics
4. Push RotatE results to GitHub
5. Begin Zenodo upload preparation
6. medRxiv preprint submission

### External Databases Integrated:
- CTD: 7 files, 3.3GB — 3M human chem-gene interactions
- NPASS 3.0: 8 files, 215MB — 204K natural products
- LOTUS: 5 files, 268MB — 222K compounds, 37K taxa
