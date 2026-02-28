# SexDiffKG: A Sex-Stratified Knowledge Graph for Drug Safety Pharmacovigilance

**Author:** JShaik (jshaik@coevolvenetwork.com)  
**Affiliation:** CoEvolve Network, Independent Researcher, Barcelona, Spain  
**Status:** Under preparation 

## Overview

SexDiffKG is the first knowledge graph where biological sex is a structural dimension on every drug-safety edge rather than an optional annotation. It integrates FDA Adverse Event Reporting System (FAERS) pharmacovigilance data with molecular mechanism layers to enable sex-aware drug safety analysis.

## Key Statistics

| Metric | Value |
|--------|-------|
| FAERS quarters | 87 (2004Q1–2025Q3) |
| Raw reports | 23,607,453 |
| After dedup + sex filtering (M/F) | 14,536,008 |
| Drug–AE–sex ROR combinations | 6,887,858 |
| Sex-differential signals | 213,899 |
| KG nodes | 161,551 (6 entity types) |
| KG edges | 8,117,539 (6 relation types) |
| TransE MRR (baseline) | 0.018 |
| Validation recall | 100% (15/15 benchmarks) |
| Directional precision | 53.3% (8/15) |

## Data Sources

- **FAERS**: FDA Adverse Event Reporting System (2004Q1–2025Q3)
- **ChEMBL 36**: Drug–target interactions (12,682 edges)
- **STRING**: Protein–protein interactions (465,390 edges, confidence ≥700)
- **KEGG/Reactome**: Pathway annotations (537,605 edges)
- **GTEx**: Sex-differential gene expression (105 tissue–gene pairs; Oliva et al. 2020)

## Pipeline

The pipeline consists of numbered Python scripts executed sequentially:

```
01_download_faers.py    # Download 87 quarterly FAERS ZIP files
02_parse_faers.py       # Parse DEMO, DRUG, REAC tables; AERS→FAERS normalization
03_deduplicate.py       # Level-1 dedup (latest FDA date per caseid) + sex filter (M/F only)
03b_normalize_drugs.py  # Full RxNorm drug normalization (NOT USED — see Limitations)
04b_fast_signals.py     # Sex-stratified ROR via DuckDB SQL
05_molecular_layer.py   # ChEMBL, STRING, KEGG integration
05b_gtex_layer.py       # GTEx sex-differential expression
06_build_kg.py          # KG assembly (KGX + triple format)
07_train_embeddings.py  # TransE training via PyKEEN
08_validate_v2.py       # Literature benchmark validation
```

## Hardware

- NVIDIA DGX (ARM64)
- CUDA for TransE training (~9 hours for 100 epochs)

## Known Limitations

1. **Drug normalization**: Only case normalization (str.upper + strip) was applied. No RxNorm CUI mapping or trade-to-generic name resolution. A full normalization script (03b_normalize_drugs.py) exists but was not executed in this pipeline run. Drug entities like "LIPITOR" and "ATORVASTATIN" are treated as separate nodes.

2. **Sex filtering**: The 14.5M report count reflects both deduplication AND filtering to female/male-coded cases only. Approximately 4.4M reports with unknown, unspecified, or other sex codes were excluded.

3. **TransE baseline**: MRR of 0.018 is a baseline on a large heterogeneous KG (161K entities). This is consistent with expectations for pharmacovigilance KGs and should not be compared to benchmarks like FB15k-237 (14K entities, MRR ~0.29).

4. **Validation**: 53.3% directional precision. Some mismatches (e.g., trastuzumab) may reflect confounding by differential prescribing patterns rather than true pharmacological sex differences.

5. **RotatE**: Failed on ARM64 GB10 due to unsupported CUDA complex number operations.

## Output Files

```
data/kg/nodes.tsv              # 161,551 nodes
data/kg/edges.tsv              # 8,117,539 edges
data/kg/triples.tsv            # 7,767,750 clean triples
results/signals/ror_by_sex.parquet           # 6,887,858 ROR values
results/signals/sex_differential.parquet     # 213,899 differential signals
results/validation/benchmark_validation_v2.csv  # 15 benchmark results
results/kg_embeddings/TransE/                # Trained model + embeddings
```

## Citation

If you use SexDiffKG, please cite:

> JShaik. SexDiffKG: A Sex-Stratified Knowledge Graph for Drug Safety Pharmacovigilance.

## License

TBD

## Contact

JShaik — jshaik@coevolvenetwork.com
