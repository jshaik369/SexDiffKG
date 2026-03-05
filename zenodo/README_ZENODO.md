# SexDiffKG: Sex-Differential Drug Safety Knowledge Graph

## Dataset Description

SexDiffKG is a sex-stratified knowledge graph integrating 14,536,008 FDA FAERS adverse event reports (2004 Q1 - 2025 Q3) with molecular interaction networks. It contains **109,867 nodes** (6 types) and **1,822,851 edges** (6 relation types), with 96,281 sex-differential drug safety signals across 2,178 drugs and 5,069 adverse events.

## Files Included

### Knowledge Graph
- `nodes.tsv` — 109,867 nodes (Gene: 77,498 | Protein: 16,201 | AdverseEvent: 9,949 | Drug: 3,920 | Pathway: 2,279 | Tissue: 20)
- `edges.tsv` — 1,822,851 edges (6 relation types)
- `entity2id.tsv` — Entity to integer ID mapping (for embedding training)
- `relation2id.tsv` — Relation to integer ID mapping
- `triples.tsv` — Integer-encoded triples for embedding training

### Edge Types
| Relation | Count | Source |
|----------|-------|--------|
| has_adverse_event | 869,142 | FAERS ROR |
| interacts_with | 473,860 | STRING v12.0 |
| participates_in | 370,597 | Reactome |
| sex_differential_adverse_event | 96,281 | FAERS sex-stratified |
| targets | 12,682 | ChEMBL 36 |
| sex_differential_expression | 289 | GTEx v8 |

### Sex-Differential Signals
- `sex_differential.parquet` — 96,281 sex-differential drug-AE signals
- `strong_signals_summary.tsv` — Strong signals (|ln(ROR ratio)| > 1.0)

### Embeddings
- `entity_embeddings.npz` — ComplEx 200d entity embeddings (MRR: 0.2484, Hits@10: 40.69%)
- `relation_embeddings.npz` — ComplEx 200d relation embeddings (6 relations)

### Analysis
- `sexdiffkg_statistics.json` — Complete pipeline statistics
- `target_sex_bias.tsv` — Gene targets with sex-biased safety patterns
- `signal_validation_benchmarks.json` — Literature validation (40 benchmarks, 82.8% precision)

### Figures
- Publication-quality figures (300 DPI PNG)

## Data Sources
- FDA FAERS (2004 Q1 - 2025 Q3): 14,536,008 deduplicated reports (8.7M F / 5.8M M, 87 quarters)
- ChEMBL 36: Drug-target interactions (12,682 drug-target pairs)
- STRING v12.0: Protein-protein interactions (473,860 high-confidence edges)
- Reactome: Pathway annotations (2,279 pathways)
- UniProt: Protein information
- GTEx v8: Sex-differential gene expression (289 tissue-gene pairs)
- Drug normalization: DiAna dictionary (846,917 mappings, 53.9% resolution)

## Key Results
- **Severity-sex gradient**: Fatal ADRs are sex-balanced (50.1%F), mild ADRs are 63.5% female (rho=0.93, p=0.003)
- **Anti-regression**: Female signal bias intensifies with statistical power (rho=1.0, p=6.6e-64)
- **14.4-fold asymmetry**: 7,457 female-extreme vs 519 male-extreme sex-differential signals
- **Validation**: 72.5% coverage, 82.8% directional precision (40 literature benchmarks)

## Citation

If you use SexDiffKG, please cite:
> Shaik, M.J.A.A. (2026). SexDiffKG: A Sex-Differential Knowledge Graph Reveals 96,281 Sex-Biased Drug Safety Signals from 14.5 Million FDA Reports.

## License
CC-BY 4.0

## Code
https://github.com/jshaik369/SexDiffKG
