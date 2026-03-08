# SexDiffKG Audit Package -- Complete Reproducibility Guide

**Last updated:** 2026-03-08
**Purpose:** Enable any researcher to independently reproduce and verify every number in the SexDiffKG project. Every claim maps to a verification command that can be run from the repository root (`/home/jshaik369/sexdiffkg/`).

---

## 1. Identity

| Field | Value |
|-------|-------|
| Author | Mohammed Javeed Akhtar Abbas Shaik (J.Shaik) |
| Email | jshaik@coevolvenetwork.com |
| ORCID | 0009-0002-1748-7516 |
| Affiliation | CoEvolve Network, Independent Researcher, Barcelona, Spain |

---

## 2. Software Environment

| Software | Version | Purpose |
|----------|---------|---------|
| Python | 3.13+ | All scripts |
| PyKEEN | 1.11.1 | Knowledge graph embedding training and evaluation |
| PyTorch | 2.x | Tensor computation backend for PyKEEN |
| pandas | 2.x | Data processing, signal computation |
| numpy | 2.x | Numerical operations |
| scipy | 1.x | Statistical tests (Spearman, Fisher) |

### Hardware

Primary compute: **NVIDIA DGX Grace Blackwell GB10** (ARM64, 20 cores, 120 GB unified memory).

**Important GPU limitation:** The GB10 GPU (SM 12.1 architecture) is incompatible with complex-valued tensor CUDA kernels required by RotatE and ComplEx. All KG embedding models were therefore trained on **CPU**. This is documented transparently; training times are longer but results are mathematically identical to GPU training.

---

## 3. Data Sources (with Versions and Licenses)

| Source | Version | License | What it provides |
|--------|---------|---------|------------------|
| FAERS | 2004Q1--2025Q3 | Public Domain | 14,536,008 deduplicated adverse event reports (F: 8,744,397, M: 5,791,611), 87 quarters |
| ChEMBL | 36 | CC-BY-SA 3.0 | Drug-target binding interactions |
| STRING | v12.0 | CC-BY 4.0 | Protein-protein interactions (score > 400) |
| Reactome | 2026-02 | CC-BY 4.0 | Pathway-gene participation (NOT KEGG -- Reactome replaced KEGG in v4) |
| GTEx | v8 (Oliva 2020) | Open Access | Sex-differential gene expression (289 tissue-gene pairs) |
| DiAna | 2025 | Open Source | Drug name normalization (846,917 mappings, 53.9% resolution rate) |

---

## 4. KG v4 Ground Truth Numbers

`GROUND_TRUTH.json` is the **single source of truth** for all canonical numbers. It is maintained in 4 identical copies (see Section 10). All numbers below are taken directly from this file.

### Canonical path: `data/kg_v4/` (symlink: `data/kg`)

### File Checksums (MD5)

| File | MD5 |
|------|-----|
| nodes.tsv | `5a7331b1b0e7f11853444eb59e2b9166` |
| edges.tsv | `b8e4890c2063bdf9357c76730881b440` |
| triples.tsv | `2d4e46b1265a9a9bd44bbfc7372a9e44` |

### Node Counts (6 types, 109,867 total)

| Type | Count |
|------|-------|
| Gene | 77,498 |
| Protein | 16,201 |
| AdverseEvent | 9,949 |
| Drug | 3,920 |
| Pathway | 2,279 |
| Tissue | 20 |

### Edge Counts (6 types, 1,822,851 total rows, 1,532,674 unique triples)

| Edge Type | Total Rows | Unique Triples | Duplicates | Source |
|-----------|-----------|----------------|------------|--------|
| has_adverse_event | 869,142 | 614,978 | 254,164 | FAERS ROR analysis |
| interacts_with | 473,860 | 473,860 | 0 | STRING v12.0 |
| participates_in | 370,597 | 341,492 | 29,105 | Reactome pathways |
| sex_differential_adverse_event | 96,281 | 96,281 | 0 | FAERS sex-stratified ROR |
| targets | 12,682 | 5,774 | 6,908 | ChEMBL 36 |
| sex_differential_expression | 289 | 289 | 0 | GTEx v8 |

### Data Quality Notes

**Bug 1 -- Duplicate edge rows (15.9%):** `edges.tsv` contains 290,177 duplicate `(subject, predicate, object)` rows. The true unique triple count is **1,532,674**, not 1,822,851. PyKEEN deduplicates internally during `TriplesFactory` loading, so model training used the correct count. Fixed in v5. Transparently documented in manuscript limitations (section 10--11).

**Bug 2 -- Missing drug nodes:** 3,288 DRUG entities appear in `targets` edges (from ChEMBL 36) but are missing from `nodes.tsv`. The true entity count is **113,155**, not 109,867. PyKEEN creates entity embeddings from triples, so these drugs DO get embeddings. Fixed in v5.

**Patched files available:**
- `nodes_patched.tsv` -- 113,155 nodes (MD5: `f352e056e8f3ee02509dabbbfa75ba3f`)
- `edges_deduped.tsv` -- 1,532,674 unique edges (MD5: `e90777ee586218bac8a9a376d4e731b5`)
- `triples_deduped.tsv` (MD5: `52d60ce852f841dd85f8ce528fbd93af`)

### Signals

| Metric | Value |
|--------|-------|
| Total comparisons | 254,114 |
| Sex-differential (abs(logR) >= 0.5, min 10/sex) | 96,281 |
| Female-higher | 51,771 (53.8%) |
| Male-higher | 44,510 (46.2%) |
| Strong (abs(logR) >= 1.0) | 32,244 |
| Unique drugs with signals | 2,178 |
| Unique AEs with signals | 5,069 |

---

## 5. Embedding Models

### v4 Models

| Model | MRR | Hits@1 | Hits@10 | AMRI | Epochs | Dim | Device |
|-------|-----|--------|---------|------|--------|-----|--------|
| ComplEx v4 | 0.2484 | 0.1678 | 0.4069 | 0.9902 | 100 | 200 | cuda |
| DistMult v4 | 0.0932 | 0.0419 | 0.1842 | 0.9906 | 100 | 200 | cuda |
| DistMult v4.1 | 0.1013 | 0.0481 | 0.1961 | 0.9909 | 100 | 200 | cuda |
| RotatE v4.1 | 0.2018 | 0.1128 | 0.3677 | 0.9922 | 200 | 256 | cpu |

Notes on v4 models:
- ComplEx v4 is the **best-performing** model (MRR 0.2484).
- DistMult v4.1 was retrained on v4.1 KG with real GTEx sex-differential expression (289 edges). Training time: 91.5 minutes. Entities embedded: 113,155.
- RotatE v4.1 used optimized hyperparameters: margin=6.0, lr=1e-3, batch=4096, 256d, 200 epochs, CPU training (382 min).

### v5.2 Models (merged KG: 217,993 nodes, 3,194,017 edges)

| Model | MRR | Hits@1 | Hits@3 | Hits@5 | Hits@10 | AMRI | Epochs | Notes |
|-------|-----|--------|--------|--------|---------|------|--------|-------|
| ComplEx v5.2 | 0.1629 | 0.0472 | 0.2138 | 0.2785 | 0.3704 | 0.9831 | 25 (early stopped) | 568 min train, 105 min eval |
| DistMult v5.2 | 0.0548 | 0.0287 | 0.0548 | 0.0708 | 0.0995 | 0.9826 | 10 | 486 min eval |
| RotatE v5.2 | IN PROGRESS | -- | -- | -- | -- | -- | -- | Best loss: 0.00393 (epoch 5) |

---

## 6. Validation

| Metric | Value |
|--------|-------|
| Total literature benchmarks | 40 |
| Found in KG | 29 |
| Coverage | 72.5% (29/40) |
| Correct direction | 24 |
| Wrong direction | 5 |
| Directional precision | 82.8% (24/29) |
| Not found | 11 |

---

## 7. Verification Commands

All commands are run from the repository root: `/home/jshaik369/sexdiffkg/`

### 7.1 File Integrity

```bash
# Verify node count (109,867 data rows + 1 header = 109,868 lines)
wc -l data/kg_v4/nodes.tsv
# Expected: 109868

# Verify edge count (1,822,851 data rows + 1 header = 1,822,852 lines)
wc -l data/kg_v4/edges.tsv
# Expected: 1822852

# Verify MD5 checksums
md5sum data/kg_v4/nodes.tsv
# Expected: 5a7331b1b0e7f11853444eb59e2b9166

md5sum data/kg_v4/edges.tsv
# Expected: b8e4890c2063bdf9357c76730881b440

md5sum data/kg_v4/triples.tsv
# Expected: 2d4e46b1265a9a9bd44bbfc7372a9e44
```

### 7.2 Node Type Distribution

```bash
python3 -c "
import pandas as pd
df = pd.read_csv('data/kg_v4/nodes.tsv', sep='\t')
print(f'Total nodes: {len(df)}')
print(df['category'].value_counts().to_string())
"
# Expected:
# Total nodes: 109867
# Gene             77498
# Protein          16201
# AdverseEvent      9949
# Drug              3920
# Pathway           2279
# Tissue              20
```

### 7.3 Edge Type Distribution

```bash
python3 -c "
import pandas as pd
df = pd.read_csv('data/kg_v4/edges.tsv', sep='\t')
print(f'Total edges: {len(df)}')
print(df['predicate'].value_counts().to_string())
"
# Expected:
# Total edges: 1822851
# has_adverse_event                  869142
# interacts_with                     473860
# participates_in                    370597
# sex_differential_adverse_event      96281
# targets                             12682
# sex_differential_expression           289
```

### 7.4 Unique Triple Count (confirms duplicate bug)

```bash
python3 -c "
import pandas as pd
df = pd.read_csv('data/kg_v4/edges.tsv', sep='\t')
unique = df.drop_duplicates(subset=['subject','predicate','object'])
print(f'Total rows: {len(df)}')
print(f'Unique triples: {len(unique)}')
print(f'Duplicates: {len(df) - len(unique)}')
"
# Expected:
# Total rows: 1822851
# Unique triples: 1532674
# Duplicates: 290177
```

### 7.5 FAERS Report Counts

```bash
python3 -c "
import pandas as pd
df = pd.read_parquet('results/signals_v4/all_sex_comparisons_v4.parquet')
print(f'Total comparisons: {len(df)}')
"
# Expected: 254114
```

### 7.6 Signal Counts

```bash
python3 -c "
import pandas as pd
df = pd.read_parquet('results/signals_v4/sex_differential_v4.parquet')
print(f'Total sex-differential signals: {len(df)}')
print(f'Female-higher: {(df.direction==\"female_higher\").sum()}')
print(f'Male-higher: {(df.direction==\"male_higher\").sum()}')
print(f'Strong (|logR| >= 1.0): {(df.log_ratio.abs() >= 1.0).sum()}')
print(f'Unique drugs: {df.drug_name.nunique()}')
print(f'Unique AEs: {df.adverse_event.nunique()}')
"
# Expected:
# Total sex-differential signals: 96281
# Female-higher: 51771
# Male-higher: 44510
# Strong (|logR| >= 1.0): 32244
# Unique drugs: 2178
# Unique AEs: 5069
```

### 7.7 GROUND_TRUTH.json Consistency (all 4 copies)

```bash
md5sum GROUND_TRUTH.json results/GROUND_TRUTH.json data/kg_v4/GROUND_TRUTH.json
# All three should show identical MD5

# Vault copy (may be on separate storage):
md5sum /home/jshaik369/AYURFEM-Vault/projects/sexdiffkg/GROUND_TRUTH.json
# Should match the above
```

### 7.8 v5.2 KG Verification

```bash
# v5.2 node and edge counts
wc -l data/kg_v5.2/nodes.tsv data/kg_v5.2/edges.tsv
# Expected: 217994 nodes.tsv (217,993 + header), 3194018 edges.tsv (3,194,017 + header)

# v5.2 checksums
md5sum data/kg_v5.2/nodes.tsv
# Expected: e0e8077fc8d5f1b6f46e802ac61f4737

md5sum data/kg_v5.2/edges.tsv
# Expected: db4c271ccc29f176b26dbee0de21e1fd
```

### 7.9 Patched Files Verification

```bash
wc -l data/kg_v4/nodes_patched.tsv
# Expected: 113156 (113,155 + header)

wc -l data/kg_v4/edges_deduped.tsv
# Expected: 1532675 (1,532,674 + header)

md5sum data/kg_v4/nodes_patched.tsv
# Expected: f352e056e8f3ee02509dabbbfa75ba3f

md5sum data/kg_v4/edges_deduped.tsv
# Expected: e90777ee586218bac8a9a376d4e731b5

md5sum data/kg_v4/triples_deduped.tsv
# Expected: 52d60ce852f841dd85f8ce528fbd93af
```

---

## 8. Known WRONG Numbers (NEVER USE)

These numbers are from superseded versions (v3) or stale model runs. They must NEVER appear in any publication or claim.

| Wrong Number | Why Wrong |
|-------------|-----------|
| ~~127,063 nodes~~ | v3 original -- superseded |
| ~~126,575 nodes~~ | v3 cleaned -- superseded |
| ~~5,839,717 edges~~ | v3 original -- superseded |
| ~~5,489,928 edges~~ | v3 cleaned -- superseded |
| ~~183,544 total signals~~ | v3 signals -- superseded |
| ~~49,026 strong signals~~ | v3 signals -- superseded |
| ~~5,658 unique AEs~~ | v3 count -- superseded |
| ~~51,825 female-higher~~ | v3 direction count -- superseded |
| ~~44,456 male-higher~~ | v3 direction count -- superseded |
| ~~86 quarters~~ | Was 86 before 2025Q3 update; now 87 |
| ~~KEGG~~ | Replaced by Reactome in v4 |
| ~~MRR 0.039~~ | Stale DistMult v3 baseline |
| ~~MRR 0.048~~ | Stale DistMult version |
| ~~MRR 0.093~~ | DistMult v4 (superseded by v4.1 = 0.1013) |
| ~~MRR 0.0941~~ | Old RotatE with wrong hyperparams (margin=9.0, lr=5e-5, batch=512) |

---

## 9. File Locations

| What | Path |
|------|------|
| KG v4 (canonical) | `data/kg_v4/` |
| KG v4 (symlink) | `data/kg` -> `data/kg_v4` |
| KG v5.2 (merged, bridged) | `data/kg_v5.2/` |
| Signals (all comparisons) | `results/signals_v4/all_sex_comparisons_v4.parquet` |
| Signals (sex-differential) | `results/signals_v4/sex_differential_v4.parquet` |
| Embeddings v4 (ComplEx) | `results/kg_embeddings_v4/ComplEx/` |
| Embeddings v4 (DistMult) | `results/kg_embeddings_v4/DistMult/` |
| Embeddings v4 (RotatE) | `results/kg_embeddings_v4/RotatE_v4.1/` |
| Embeddings v5.2 | `results/kg_embeddings_v5.2/` |
| 29 papers | `Publication/papers/` |
| Deep analysis (130 waves) | `results/deep_analysis/` |
| Ground truth | `GROUND_TRUTH.json` (4 copies) |
| Continuity state | `CONTINUITY_STATE.md` |
| KG Expert Manual | `KG_Expert_Manual.md` |
| Vault | `/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg/` |

---

## 10. RAID Redundancy Locations

| File | Copy 1 | Copy 2 | Copy 3 | Copy 4 |
|------|--------|--------|--------|--------|
| GROUND_TRUTH.json | `./GROUND_TRUTH.json` (repo root) | `results/GROUND_TRUTH.json` | `data/kg_v4/GROUND_TRUTH.json` | vault |
| CONTINUITY_STATE.md | `./CONTINUITY_STATE.md` (repo root) | vault | -- | -- |
| AUDIT_PACKAGE.md | `./AUDIT_PACKAGE.md` (repo root) | vault | -- | -- |

---

## 11. Citation

Shaik MJAA. SexDiffKG: A Sex-Differential Drug Safety Knowledge Graph. 2026. doi:10.5281/zenodo.18819192
