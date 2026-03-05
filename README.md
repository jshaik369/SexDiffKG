# SexDiffKG

**A Sex-Differential Knowledge Graph for Drug Safety from 14.5 Million FDA Adverse Event Reports**

[![bioRxiv](https://img.shields.io/badge/bioRxiv-2026.709170-b31b1b.svg)](https://doi.org/10.1101/2026.709170)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Data: CC-BY 4.0](https://img.shields.io/badge/Data-CC--BY%204.0-green.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED.svg)](Dockerfile)

---

## Overview

SexDiffKG is the first knowledge graph where **biological sex is encoded on every drug-safety edge**. It integrates 14.5 million FDA FAERS adverse event reports with molecular interaction networks to reveal sex-differential drug safety patterns at scale.

**Key finding:** 96,281 drug-adverse event pairs show sex-differential signals, with 53.8% biased toward women. Signal validation against 40 literature benchmarks achieves 82.8% directional precision.

## Key Statistics

| Metric | Value |
|--------|-------|
| FAERS reports (deduplicated, M/F) | 14,536,008 |
| Female reports | 8,744,397 (60.2%) |
| Male reports | 5,791,611 (39.8%) |
| FAERS quarters | 87 (2004 Q1 - 2025 Q3) |
| Knowledge graph nodes | 109,867 (6 types) |
| Knowledge graph edges | 1,822,851 (6 relations) |
| Sex-differential signals | 96,281 |
| Female-biased signals | 51,771 (53.8%) |
| Male-biased signals | 44,510 (46.2%) |
| Unique drugs (normalized) | 2,178 |
| Unique adverse events | 5,069 |
| Best embedding MRR (ComplEx v4) | 0.2484 |
| Best embedding Hits@10 (ComplEx v4) | 0.4069 |
| Best embedding AMRI (ComplEx v4) | 0.9902 |
| Literature validation | 72.5% coverage, 82.8% precision (40 benchmarks) |

## Data Sources

All data sources are **freely available** and **open access**:

| Source | What | License | Edges |
|--------|------|---------|------:|
| [FDA FAERS](https://open.fda.gov) | Adverse event reports (2004 Q1 - 2025 Q3) | Public Domain | 869,142 |
| [ChEMBL 36](https://www.ebi.ac.uk/chembl/) | Drug-target interactions | CC-BY-SA 3.0 | 12,682 |
| [STRING v12.0](https://string-db.org) | Protein-protein interactions (score >= 700) | CC-BY 4.0 | 473,860 |
| [Reactome](https://reactome.org) | Pathway annotations | CC-BY 4.0 | 370,597 |
| [GTEx v8](https://gtexportal.org) | Sex-differential gene expression (Oliva et al. 2020) | Open Access | 289 |

## Drug Normalization

SexDiffKG v4 introduces a 4-tier drug normalization pipeline:

1. **DiAna dictionary** (47.0%): 846,917 FAERS drug name mappings from [DiAna](https://github.com/fusarolimichele/DiAna_package)
2. **prod_ai field** (6.5%): FDA product active ingredient
3. **ChEMBL synonyms** (0.3%): Cross-reference against ChEMBL 36
4. **String cleaning** (40.7%): Uppercase + special character removal

Total active-ingredient resolution: **53.9%**, reducing 710K raw drug names to 301K normalized entries.

## Quick Start

### Option 1: Conda

```bash
git clone https://github.com/jshaik369/SexDiffKG.git
cd SexDiffKG
conda env create -f environment.yml
conda activate sexdiffkg
```

### Option 2: Docker

```bash
docker build -t sexdiffkg .
docker run -it sexdiffkg
```

### Option 3: pip

```bash
pip install -r requirements.txt
```

## Pipeline

The pipeline consists of numbered Python scripts in `scripts/`:

```
v4_01_normalize_diana.py        # 4-tier drug normalization (DiAna + prod_ai + ChEMBL + raw)
v4_02_compute_signals.py        # Sex-stratified ROR computation via DuckDB (16 threads)
v4_03_build_kg.py               # KG assembly (FAERS + ChEMBL + STRING + Reactome + GTEx)
v4_04_train_distmult.py         # DistMult training (PyKEEN, 200d, 100 epochs)
v4_05_train_rotatE.py           # RotatE training (PyKEEN, 200d, 200 epochs)
v4_06_retrain_distmult_v41.py   # DistMult v4.1 (NSSALoss, 100 epochs)
v4_07d_train_rotatE_cpu_fixed.py # RotatE v4.1 CPU (200 epochs)
validate_40_benchmarks_v4.py    # Literature benchmark validation (40 drug-AE pairs)
v5_01_build_bridge.py           # VEDA-KG identifier bridges
v5_02_merge_vedakg.py           # Merge VEDA-KG into SexDiffKG v5
v5_03_validate_merge.py         # v5 merge validation
v5_04_train_complex.py          # ComplEx v5 training on merged KG
v5_05_train_distmult.py         # DistMult v5 training on merged KG
```

## Output Files

```
data/kg_v4/nodes.tsv                          # 109,867 nodes
data/kg_v4/edges.tsv                          # 1,822,851 edges
data/kg_v4/triples.tsv                        # NaN-free triples for embedding training
results/signals_v4/sex_differential_v4.parquet # 96,281 sex-differential signals
results/kg_embeddings/                         # Trained models + embeddings
results/validation_40_benchmarks_v4.json       # Validation results
results/analysis/sexdiffkg_statistics.json     # Canonical ground truth statistics
```

## SexDiffKG v5 — Merged with VEDA-KG

v5 absorbs [VEDA-KG](https://github.com/jshaik369/veda-kg) (Ayurvedic + clinical trial data):

| Metric | v4 | v5 |
|--------|-----|-----|
| Nodes | 109,867 | 246,056 |
| Edges | 1,822,851 | 3,182,843 |
| Node types | 6 | 16 |
| Edge types | 6 | 18 |

All 1,532,674 unique v4 triples preserved (100%). 1,650,169 new edges from VEDA sources (DisGeNET, ClinicalTrials.gov, ChEMBL mechanisms, KEGG pathways).

### Derived Knowledge Graphs

| Project | Nodes | Edges | Focus |
|---------|-------|-------|-------|
| REPRODUCT-KG | 22,403 | 1,116,735 | Pregnancy drug safety |
| MENTALHEALTH-KG | 20,851 | 762,389 | Psychiatric drug safety |
| GERIPHARM-KG | 18,754 | 739,396 | Elderly drug safety |
| PCOS-ENDO-KG | 36,903 | 697,819 | PCOS/endometriosis + GLP-1 |
| AYUR-PHARMA-KG | 24,316 | 293,444 | Ayurvedic pharmacovigilance |

## Notable Findings

- **HDAC inhibitors** (HDAC1/2/3/6): Exclusively female-biased safety profiles
- **Estrogen receptor drugs** (ESR1): Counterintuitively male-biased safety signals
- **Platelet integrins** (ITGA2B/ITGB3): Exclusively female-biased
- **Validation precision**: 82.8% directional precision on 40 literature benchmarks

## Knowledge Graph Embeddings

Three embedding models trained on SexDiffKG v4 (1,822,851 triples):

| Model | MRR | Hits@1 | Hits@10 | AMRI | Epochs | Device |
|-------|-----|--------|---------|------|--------|--------|
| **ComplEx v4** | **0.2484** | **0.1678** | **0.4069** | **0.9902** | 100 | CPU |
| DistMult v4.1 | 0.1013 | 0.0481 | 0.1961 | 0.9909 | 100 | CPU |
| DistMult v4 | 0.0932 | 0.0419 | 0.1842 | 0.9906 | 100 | CPU |
| RotatE v4.1 | 0.2018 | 0.1128 | 0.3677 | 0.9922 | 200 | CPU |

ComplEx achieves 2.45x higher MRR than DistMult, making it the recommended model for downstream link prediction tasks.

## Reproducibility

- **Hardware:** Tested on NVIDIA DGX Spark (Grace Blackwell, 128GB unified memory)
- **Training time:** ~2 hours for ComplEx/DistMult (200d, 100 epochs, CPU)
- **Total pipeline:** ~6 hours end-to-end
- **Disk space:** ~11 GB for full dataset

## Citation

If you use SexDiffKG in your research, please cite:

```bibtex
@article{akhtarabbas2026sexdiffkg,
  title={SexDiffKG: A Sex-Differential Knowledge Graph for Drug Safety
         from 14.5 Million FDA Adverse Event Reports},
  author={Shaik, Mohammed Javeed Akhtar Abbas},
  journal={bioRxiv},
  year={2026},
  doi={10.1101/2026.709170}
}
```

## License

- **Code:** MIT License
- **Data:** CC-BY 4.0

## Author

**Mohammed Javeed Akhtar Abbas Shaik**
ORCID: [0009-0002-1748-7516](https://orcid.org/0009-0002-1748-7516)
Email: jshaik@coevolvenetwork.com
Affiliation: CoEvolve Network, Independent Researcher, Barcelona, Spain
