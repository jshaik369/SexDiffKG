# SexDiffKG Full Systems Inventory — Deep Audit
**Date:** 2026-03-05
**Scope:** All assets across DGX Spark, Mac Mini M2, all drives, GitHub, Zenodo, bioRxiv

---

## 1. HARDWARE TOPOLOGY

### DGX Spark GB10
- **CPU:** 20 ARM Grace cores
- **GPU:** GB10 (NVRTC SM 12.1 — complex tensor CUDA incompatible)
- **NVMe:** 3.7 TB (2.3 TB used, 1.3 TB free, 64%)
- **RAM:** 128 GB unified
- **OS:** Ubuntu-based Linux, CUDA 13.0, Driver 580.126.09
- **SSH:** `ssh dgx` → 10.0.0.2 (Ethernet direct, NOT WiFi)

### Mac Mini M2
- **CPU:** M2 (4 efficiency + 4 performance cores)
- **RAM:** 16 GB unified
- **SSD:** 245 GB (213 GB used, 29 GB free, 87% — CRITICALLY LOW)
- **OS:** macOS Darwin 25.3.0

### External Drives
| Drive | Mount | Host | Size | Used | Free |
|-------|-------|------|------|------|------|
| 28TB Swolfy | /media/jshaik369/28TBSwolfy | DGX | 26 TB | 23 TB (89%) | 3 TB |
| Samsung cen8tb1 | /media/jshaik369/cen8tb1 | DGX | 7.3 TB | 75 GB (2%) | 7.2 TB |
| 5TB Swolfy | /Volumes/5TBSwolfyUT | Mac Mini | 4.5 TB | 133 GB (3%) | 4.4 TB |
| 28TB Swolfy | NOT MOUNTED | Mac Mini | — | — | — |

---

## 2. SEXDIFFKG PROJECT — COMPLETE INVENTORY

### Core Data (DGX: /home/jshaik369/sexdiffkg/)
- **Total size:** 26 GB (data/ 17 GB, results/ 6.9 GB, zenodo/ 2.3 GB)
- **KG v4 (canonical):** 109,867 nodes / 1,822,851 edges / 6 types each
- **FAERS:** 14,536,008 deduplicated reports (8.7M F / 5.8M M), 87 quarters
- **Signals:** 96,281 sex-differential (51,771 F / 44,510 M), 2,178 drugs, 5,069 AEs
- **Drug normalization:** DiAna dictionary, 846,917 mappings, 53.9% resolution
- **Sources:** STRING v12.0, ChEMBL 36, Reactome, GTEx v8

### Models
| Model | MRR | Hits@1 | Hits@10 | AMRI | Status |
|-------|-----|--------|---------|------|--------|
| ComplEx v4 | **0.2484** | 0.1678 | 0.4069 | 0.9902 | BEST |
| RotatE v4.1 | 0.2018 | 0.1128 | 0.3677 | 0.9922 | Complete |
| DistMult v4.1 | 0.1013 | 0.0481 | 0.1961 | 0.9909 | Complete |

### Deep Analysis (100 Waves, 10 Sessions)
- **204** analysis JSONs (3.0 MB)
- **279** publication figures (PNG + PDF, 300 DPI)
- **35** paper drafts
- **Repo:** github.com/jshaik369/sexdiffkg-deep-analysis (79 commits)
- **Location:** /tmp/sexdiffkg-deep-analysis on DGX

### Validation
| Source | Concordance | N |
|--------|-------------|---|
| Literature cross-validation | 92.0% | 11/12 |
| Canada Vigilance | 91.0% | 1,212 signals |
| 40 Literature benchmarks | 82.8% | 24/29 |
| Drug withdrawal | 80.0% | 4/5 |
| Meta-analysis | 76.9% | 10/13 |
| **Composite** | **82.9%** | 4 sources |

### Publication Materials
- 1 complete manuscript (manuscript_scidata_COMPLETE.md, 77.8 KB)
- 35 paper drafts (29 READY, 3 DRAFT, 3 STUB)
- 3 conference abstracts (ISMB, ASHG, NeurIPS)
- 4 cover letters
- Grand Audit Report + Publishing Strategy

### Git Status
- **Main repo:** 831 uncommitted changes (LFS blocks push — edges.tsv/triples.tsv >100MB)
- **Deep analysis repo:** Clean, 79 commits pushed

---

## 3. VEDA-KG PROJECT

**Location:** /home/jshaik369/veda-kg/ (36 GB)
- **155,557 nodes** / **2,124,360 edges**
- **14 node types:** Protein 46K, Compound 38K, ClinicalTrial 27K, Disease 14K, Gene 14K, Drug 9K, AE 3K, Symptom 3K, Intervention 1K, Pathway 369, Guna 20, Rasa 6, Herb 5, Dosha 3
- **15 edge types:** interacts_with 1.9M, investigates 69K, tests_intervention 48K, treats 41K, etc.
- **Data sources:** STRING 1.9M, ClinicalTrials.gov 117K, ChEMBL 77K, KEGG 51K, UniProt 8K, DisGeNET 6K, FAERS 3K
- **Models:** RotatE MRR 0.1199, TransE MRR 0.0453
- **Full ChEMBL 36 database:** 28 GB (already downloaded)
- **Exports:** vedakg.json (459 MB), neo4j CSVs, triples.tsv (181 MB)

### Cross-KG Integration Potential
- **AE overlap:** 93.1% of VEDA-KG AEs exist in SexDiffKG
- **Identifier mismatch (KEY BLOCKER):** VEDA uses KEGG/ChEMBL IDs, SexDiffKG uses gene names/Ensembl
- **DisGeNET:** 82,833 gene-disease associations available in VEDA data
- **Shared ChEMBL 36:** Both KGs use same ChEMBL version

---

## 4. AYURFEM VAULT

**Location:** /home/jshaik369/AYURFEM-Vault/projects/sexdiffkg/
- **181 files**, 11 MB total
- Key files: GROUND_TRUTH.json, CONTINUITY_STATE.md, Lessons_Learned.md, 39+ analysis docs
- Grand audit report and publishing strategy saved (2026-03-05)

---

## 5. GITHUB & EXTERNAL DEPOSITS

### Repositories
| Repo | Commits | Status |
|------|---------|--------|
| jshaik369/SexDiffKG | 9 | **STALE README** — v3 numbers (127K nodes, KEGG, GTEx v10) |
| jshaik369/sexdiffkg-deep-analysis | 79 | Current, all analysis + figures |

### CRITICAL: External Deposits
- **bioRxiv DOI 10.1101/2026.709170:** Returns **404 — NOT DEPOSITED**
- **Zenodo:** **NOT FOUND publicly** despite references
- **ISMB 2026:** Abstract submitted, no acceptance confirmation

---

## 6. DGX STORAGE DEEP DIVE

### NVMe Top Consumers (3.7 TB total)
| Item | Size | Category |
|------|------|----------|
| Steam games | **1.3 TB** | Entertainment |
| Ollama models (8) | 215 GB | AI models |
| LM Studio models | 183 GB | AI models |
| HuggingFace cache (13) | 123 GB | AI models |
| ComfyUI | 40 GB | AI tools |
| VEDA-KG | 36 GB | Research |
| Miniforge3 | 27 GB | Python env |
| SexDiffKG | 26 GB | Research |
| pip cache | 7.8 GB | Cache |
| llama.cpp | 7.1 GB | AI tools |
| pytorch_build | 6.0 GB | Build artifacts |

### 28TB Swolfy Contents (DGX-mounted)
- AYURFEM backups × 10 directories
- ComfyUI_outputs, DGX/, Google/, Edits/
- macmini_backup/, samsung_backup/
- HUMANITY_DATA_2026/

### Samsung 8TB Contents
- AYURFEM_MASTER (33 GB), ayurfem_molecular (32 GB), Ayurfem (7.8 GB)
- sexdiffkg_data (3.2 GB) — raw FAERS staging

---

## 7. MAC MINI INVENTORY

### SSD Usage (245 GB, 87% full)
- Claude Desktop vm_bundles: 7.9 GB
- sexdiffkg_training: 181 MB (RotatE v4.1 model)
- 3 Claude Code skills: ayurfem, knowledge-graph, sexdiffkg
- Ollama running locally (models tunnel to DGX)

### 5TB Drive
- AYURFEM_COMPLETE archive: 11 GB
- Spark fine-tuning data: 2.2 GB
- Mostly empty (4.4 TB free)

---

## 8. RUNNING SERVICES (DGX)

### MCP Agents
- ayurfem_agent.py (port 8765)
- ayurfem_context_agent.py (port 8766)
- jupyter_agent.py (port 9001)

### Docker (7 containers)
- Qdrant (6333), Open-WebUI (8080), SearXNG (8889)
- Perplexica, Meilisearch (7700), Portainer (9443)
- Agent-Zero (ayurfem-agent)

### GPU
- 75°C, 95% utilization
- **Game running:** AVGame-Win64-Shipping.exe using 4 GB VRAM
- ComfyUI: 170 MB VRAM

---

## 9. IDENTIFIED ISSUES (Priority Order)

### CRITICAL
1. **bioRxiv NOT deposited** — DOI badge in README is dead (404)
2. **Zenodo NOT deposited** — No public record despite README badge
3. **Main SexDiffKG README has WRONG v3 numbers** — 127K nodes, KEGG, GTEx v10, DistMult 0.048
4. **831 uncommitted changes in main repo** — LFS needed for >100MB files

### HIGH
5. **Mac Mini SSD 87% full** — Only 29 GB free
6. **GPU running a game** — 4 GB VRAM consumed, 95% utilization
7. **ISMB poster doesn't exist** — Deadline April 9 (35 days)
8. **No actual journal submission started**

### MODERATE
9. **88 broken FAERS symlinks** — cen8tb unmounted for some paths
10. **SSH config discrepancy** — MEMORY.md says WiFi 192.168.1.15, actual is Ethernet 10.0.0.2
11. **28TB drive not mounted on Mac Mini** — was corrupted (ExFAT)
12. **Steam consuming 1.3 TB on DGX NVMe** — research bottleneck potential

### LOW
13. **Duplicate AI model storage** — Ollama + LM Studio + HF cache overlap
14. **pip cache 7.8 GB** — clearable
15. **pytorch_build 6 GB** — clearable
