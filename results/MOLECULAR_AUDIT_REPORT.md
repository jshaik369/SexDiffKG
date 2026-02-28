# SexDiffKG Molecular Audit Report

**Date:** 2026-02-28 17:43:52
**Runtime:** 252.9 seconds
**Method:** Exhaustive (zero sampling) — every node, every edge, every signal, every embedding value

## Verdict: 🟢 ALL CHECKS PASSED

| Category | Count |
|----------|-------|
| Passed | 85 |
| Failed | 0 |
| Warnings | 4 |
| Total | 89 |

## All Checks

| # | Status | Check | Detail |
|---|--------|-------|--------|
| 1 | ✅ PASS | Total node count | 127,063 |
| 2 | ⚠️ WARN | Null node IDs | count=1 (KNOWN: GUCY1B2 protein missing Ensembl ID, excluded from training) |
| 3 | ✅ PASS | Zero empty node IDs |  |
| 4 | ✅ PASS | Zero whitespace-padded node IDs |  |
| 5 | ✅ PASS | Zero duplicate node IDs |  |
| 6 | ✅ PASS | All nodes have valid categories |  |
| 7 | ✅ PASS | Node count Gene=70607 |  |
| 8 | ✅ PASS | Node count Drug=29277 |  |
| 9 | ✅ PASS | Node count AdverseEvent=16162 |  |
| 10 | ✅ PASS | Node count Protein=8721 |  |
| 11 | ✅ PASS | Node count Pathway=2279 |  |
| 12 | ✅ PASS | Node count Tissue=17 |  |
| 13 | ✅ PASS | All Drug IDs follow CHEMBL or DRUG: prefix |  |
| 14 | ✅ PASS | All AE nodes have names |  |
| 15 | ✅ PASS | Nodes file hash | sha256=0eb91b5b2b5cec27 |
| 16 | ✅ PASS | Total edge count | 5,839,717 |
| 17 | ✅ PASS | Zero null predicates |  |
| 18 | ✅ PASS | All predicates are valid |  |
| 19 | ⚠️ WARN | Null edge subjects | count=238075 (all in interacts_with — STRING unresolved) |
| 20 | ⚠️ WARN | Null edge objects | count=238180 (all in interacts_with — STRING unresolved) |
| 21 | ✅ PASS | Zero dangling subjects (all reference valid nodes) |  |
| 22 | ✅ PASS | Zero dangling objects (all reference valid nodes) |  |
| 23 | ✅ PASS | Edge type has_adverse_event=4,640,396 |  |
| 24 | ✅ PASS | Edge type participates_in=537,605 |  |
| 25 | ✅ PASS | Edge type interacts_with=465,390 |  |
| 26 | ✅ PASS | Edge type sex_differential_adverse_event=183,539 |  |
| 27 | ✅ PASS | Edge type targets=12,682 |  |
| 28 | ✅ PASS | Edge type sex_differential_expression=105 |  |
| 29 | ⚠️ WARN | Duplicate edges in edges.tsv | count=1,920,106 (KNOWN: multi-source merge, does NOT affect training) |
| 30 | ✅ PASS | All 'targets' subjects are Drug nodes |  |
| 31 | ✅ PASS | All 'targets' objects are Gene/Protein nodes |  |
| 32 | ✅ PASS | Edges file hash | sha256=bacfdb0017d4b5c2 |
| 33 | ✅ PASS | Sex-differential signal count | 183,544 |
| 34 | ✅ PASS | ALL 183,544 signal ROR ratios mathematically verified (ln base) |  |
| 35 | ✅ PASS | Zero NaN/Inf in ROR ratio calculations |  |
| 36 | ✅ PASS | ALL 183,544 direction labels correct |  |
| 37 | ✅ PASS | Strong signal count | 49,026 |
| 38 | ✅ PASS | Female-biased strong | 28,669 |
| 39 | ✅ PASS | Male-biased strong | 20,357 |
| 40 | ✅ PASS | ALL 49,026 strong signals have ≥10 reports per sex |  |
| 41 | ✅ PASS | Unique drugs | 3,441 |
| 42 | ✅ PASS | Unique AEs | 5,658 |
| 43 | ✅ PASS | Entity embedding shape | (126575, 200) |
| 44 | ✅ PASS | Relation embedding shape | (6, 200) |
| 45 | ✅ PASS | Zero NaN in 25,315,000 entity values |  |
| 46 | ✅ PASS | Zero Inf in 25,315,000 entity values |  |
| 47 | ✅ PASS | Zero NaN in 1,200 relation values |  |
| 48 | ✅ PASS | Zero Inf in 1,200 relation values |  |
| 49 | ✅ PASS | Zero degenerate (zero-norm) embeddings out of 126,575 |  |
| 50 | ✅ PASS | Embedding norm stats | mean=1.0000, std=0.0000, min=1.0000, max=1.0000 |
| 51 | ✅ PASS | Zero near-duplicate drug embeddings (cosine > 0.9999) out of 29,201 |  |
| 52 | ✅ PASS | No embedding collapse | mean |cos_sim|=0.4608 |
| 53 | ✅ PASS | Embedding file hash entity_embeddings.npz | sha256=bf5ed9dab2786f6e |
| 54 | ✅ PASS | Embedding file hash relation_embeddings.npz | sha256=2917b43b39111d4e |
| 55 | ✅ PASS | Re-derived target count matches | both=429 |
| 56 | ✅ PASS | ALL 429 target scores independently verified |  |
| 57 | ✅ PASS | PCA drug count | 29,201 |
| 58 | ✅ PASS | Total drugs across clusters | 29,201 |
| 59 | ✅ PASS | Total signals across clusters | 49,026 |
| 60 | ✅ PASS | All cluster profile math verified |  |
| 61 | ✅ PASS | All 58,402 PCA coordinate values finite |  |
| 62 | ✅ PASS | Raw triples count | 5,839,717 |
| 63 | ✅ PASS | Clean triples (no NaN) | 5,489,928 |
| 64 | ✅ PASS | NaN triples dropped | 349,789 |
| 65 | ✅ PASS | All triples exist in edges file |  |
| 66 | ✅ PASS | Entity count matches embedding rows | both=126,575 |
| 67 | ✅ PASS | sex_diff_AE edges ≈ signals | edges=183,539, signals=183,544 |
| 68 | ✅ PASS | Study contains FAERS total reports=14,536,008 |  |
| 69 | ✅ PASS | Study contains FAERS female reports=8,744,397 |  |
| 70 | ✅ PASS | Study contains FAERS male reports=5,791,611 |  |
| 71 | ✅ PASS | Study contains KG nodes=127,063 |  |
| 72 | ✅ PASS | Study contains KG edges=5,839,717 |  |
| 73 | ✅ PASS | Study contains Strong signals=49,026 |  |
| 74 | ✅ PASS | Study contains Female-biased strong=28,669 |  |
| 75 | ✅ PASS | Study contains Male-biased strong=20,357 |  |
| 76 | ✅ PASS | Study contains Sex-differential signals=183,544 |  |
| 77 | ✅ PASS | Study contains Drugs clustered=29,201 |  |
| 78 | ✅ PASS | Study contains Gene targets=429 |  |
| 79 | ✅ PASS | Study contains MRR=0.04762 |  |
| 80 | ✅ PASS | Study contains Hits@10 (as percentage)=8.85% |  |
| 81 | ✅ PASS | Study contains AMRI=0.981 |  |
| 82 | ✅ PASS | Study contains Unique drugs=3,441 |  |
| 83 | ✅ PASS | Study contains Unique AEs=5,658 |  |
| 84 | ✅ PASS | Study contains ROR signals=2,610,331 |  |
| 85 | ✅ PASS | Study contains Drug-target edges=12,682 |  |
| 86 | ✅ PASS | Study contains PPI edges=465,390 |  |
| 87 | ✅ PASS | Study contains Pathway edges=537,605 |  |
| 88 | ✅ PASS | Study contains Ratio threshold (corrected)=~2.7× |  |
| 89 | ✅ PASS | Study correctly uses ~2.7× threshold (not >2×) |  |

---
*Molecular-level audit: 85 deterministic checks, zero sampling.*
