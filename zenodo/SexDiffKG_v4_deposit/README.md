# SexDiffKG v4 — Sex-Differential Drug Safety Knowledge Graph

**Version:** 4.0
**Author:** Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)
**ORCID:** 0009-0002-1748-7516
**Affiliation:** CoEvolve Network, Independent Researcher, Barcelona, Spain
**License:** MIT (code), CC-BY 4.0 (data)

## Description

SexDiffKG is the first knowledge graph where biological sex is encoded on every drug-safety edge. It integrates 14,536,008 FDA FAERS adverse event reports (2004 Q1 - 2025 Q3) with molecular interaction networks to reveal sex-differential drug safety patterns at scale.

## Key Statistics

- **109,867 nodes** (6 types: Gene, Protein, AdverseEvent, Drug, Pathway, Tissue)
- **1,822,851 edges** (6 relations)
- **96,281 sex-differential signals** (53.8% female-biased)
- **14,536,008 deduplicated FAERS reports** (8.7M female, 5.8M male)
- **2,178 unique drugs**, **5,069 unique adverse events** (with sex-differential signals)

## Data Sources

| Source | Version | License |
|--------|---------|---------|
| FDA FAERS | 2004Q1-2025Q3 | Public Domain |
| ChEMBL | 36 | CC-BY-SA 3.0 |
| STRING | v12.0 | CC-BY 4.0 |
| Reactome | 2026-02 | CC-BY 4.0 |
| GTEx | v8 (Oliva 2020) | Open Access |

## Embedding Models

| Model | MRR | Hits@10 | AMRI |
|-------|-----|---------|------|
| ComplEx v4 | 0.2484 | 0.4069 | 0.9902 |
| DistMult v4.1 | 0.1013 | 0.1961 | 0.9909 |

## Validation

- 40 literature benchmarks: 72.5% coverage, 82.8% directional precision

## Code

GitHub: https://github.com/jshaik369/SexDiffKG

## Citation

Shaik, M.J.A.A. (2026). SexDiffKG: A Sex-Differential Drug Safety Knowledge Graph from 14.5 Million FDA Adverse Event Reports. bioRxiv, doi:10.1101/2026.709170
