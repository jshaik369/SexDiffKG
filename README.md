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

**Key finding:** 49,026 drug-adverse event pairs show strong sex-differential signals, with 58.5% biased toward women. Target-level analysis reveals 429 gene targets with sex-biased safety profiles.

## Key Statistics

| Metric | Value |
|--------|-------|
| FAERS reports (deduplicated, M/F) | 14,536,008 |
| Female reports | 8,744,397 (60.2%) |
| Male reports | 5,791,611 (39.8%) |
| Knowledge graph nodes | 127,063 (6 types) |
| Knowledge graph edges | 5,839,717 (6 relations) |
| Strong sex-differential signals | 49,026 |
| Female-biased signals | 28,669 (58.5%) |
| Male-biased signals | 20,357 (41.5%) |
| Gene targets with sex bias | 429 |
| DistMult AMRI | 0.981 |
| Literature validation | 67% (10/15 benchmarks) |

## Data Sources

All data sources are **freely available** and **open access**:

| Source | What | Edges |
|--------|------|------:|
| [FDA FAERS](https://open.fda.gov) | Adverse event reports (2004 Q1 - 2024 Q3) | 4,823,935 |
| [ChEMBL 36](https://www.ebi.ac.uk/chembl/) | Drug-target interactions | 12,682 |
| [STRING v12.0](https://string-db.org) | Protein-protein interactions (score >= 700) | 465,390 |
| [KEGG](https://www.genome.jp/kegg/) | Pathway annotations | 537,605 |
| [UniProt](https://www.uniprot.org) | Protein encoding | 105 |
| [GTEx v10](https://gtexportal.org) | Sex-differential gene expression | — |

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
01_download_faers.py       # Download 87 quarterly FAERS ZIP files from openFDA
02_parse_faers.py          # Parse DEMO, DRUG, REAC tables
03_deduplicate.py          # Deduplicate + filter to M/F only
03b_normalize_drugs.py     # Drug name normalization
04b_fast_signals.py        # Sex-stratified ROR computation via DuckDB
05_molecular_layer.py      # ChEMBL, STRING, KEGG integration
05b_gtex_layer.py          # GTEx sex-differential gene expression
06_build_kg.py             # Knowledge graph assembly
07_train_embeddings.py     # DistMult training via PyKEEN (200d, 100 epochs)
08_validate_v2.py          # Literature benchmark validation
09_cluster_analysis.py     # Drug clustering (K=20, PCA)
14_fix_targets_and_figures.py  # Target analysis + figure generation
generate_v3_final.py       # Manuscript generation
```

## Output Files

```
data/kg/nodes.tsv                    # 127,063 nodes
data/kg/edges.tsv                    # 5,839,717 edges
data/kg/triples.tsv                  # Integer-encoded triples for embedding training
data/kg/entity2id.tsv                # Entity-to-ID mapping
data/kg/relation2id.tsv              # Relation-to-ID mapping
results/signals/sex_differential.parquet    # 183,544 sex-differential signals
results/signals/ror_by_sex.parquet          # Full ROR values
results/kg_embeddings/DistMult/             # Trained model + embeddings
results/analysis/target_sex_bias.tsv        # 429 targets with sex bias
results/figures/                            # 11 publication figures (300 DPI)
```

## Notable Findings

- **HDAC inhibitors** (HDAC1/2/3/6): Exclusively female-biased safety profiles
- **Estrogen receptor drugs** (ESR1): Counterintuitively male-biased safety signals
- **Platelet integrins** (ITGA2B/ITGB3): Exclusively female-biased
- **Drug clustering**: 20 distinct sex-differential safety profile groups across 29,201 drugs

## Reproducibility

- **Hardware:** Tested on NVIDIA DGX with ARM64 GPU and 120GB unified memory
- **Training time:** ~2 hours for DistMult (200d, 100 epochs, CUDA)
- **Total pipeline:** ~8 hours end-to-end
- **Disk space:** ~11 GB for full dataset

## Citation

If you use SexDiffKG in your research, please cite:

```bibtex
@article{akhtarabbas2026sexdiffkg,
  title={SexDiffKG: A Sex-Differential Knowledge Graph Reveals 49,026 Sex-Biased
         Drug Safety Signals from 14.5 Million FDA Reports},
  author={Akhtar Abbas, Mohammed Shaik Javeed},
  journal={bioRxiv},
  year={2026},
  doi={10.1101/2026.709170}
}
```

## License

- **Code:** MIT License
- **Data:** CC-BY 4.0

## Contact

Mohammed Shaik Javeed Akhtar Abbas — Independent Researcher
