# SexDiffKG: Sex-Differential Drug Safety Knowledge Graph

## Dataset Description

SexDiffKG is a sex-stratified knowledge graph integrating 14.5 million FDA FAERS adverse event reports with molecular interaction networks. It contains 127,063 nodes (6 types) and 5,839,717 edges (6 relation types), with 49,026 strong sex-differential drug safety signals.

## Files Included

### Knowledge Graph
- `nodes.tsv` — 127,063 nodes (Gene, Drug, AdverseEvent, Protein, Pathway, Tissue)
- `edges.tsv` — 5,839,717 edges (6 relation types)
- `entity2id.tsv` — Entity to integer ID mapping (for embedding training)
- `relation2id.tsv` — Relation to integer ID mapping
- `triples.tsv` — Integer-encoded triples for embedding training

### Sex-Differential Signals
- `sex_differential.parquet` — 183,544 sex-differential drug-AE signals
- `strong_signals_summary.tsv` — 49,026 strong signals (|ln(ROR ratio)| > 1.0)

### Embeddings
- `entity_embeddings.npz` — DistMult 200d entity embeddings (126,575 entities)
- `relation_embeddings.npz` — DistMult 200d relation embeddings (6 relations)

### Analysis
- `sexdiffkg_statistics.json` — Complete pipeline statistics
- `target_sex_bias.tsv` — 430 gene targets with sex-biased safety patterns
- `signal_validation_benchmarks.json` — Literature validation results

### Figures
- 11 publication-quality figures (300 DPI PNG)

## Data Sources
- FDA FAERS (2004 Q1 - 2024 Q4): open.fda.gov
- ChEMBL 36: chembl.gitbook.io
- STRING v12.0: string-db.org
- KEGG: genome.jp/kegg
- UniProt: uniprot.org
- GTEx v10: gtexportal.org

## Citation

If you use SexDiffKG, please cite:
> Akhtar Abbas, M.S.J. (2026). SexDiffKG: A Sex-Differential Knowledge Graph Reveals 49,026 Sex-Biased Drug Safety Signals from 14.5 Million FDA Reports. bioRxiv. BIORXIV/2026/709170.

## License
CC-BY 4.0

## Code
https://github.com/jshaik369/SexDiffKG
