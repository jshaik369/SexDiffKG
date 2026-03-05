#!/bin/bash
# Prepare SexDiffKG v4 Zenodo deposit package
# Run from ~/sexdiffkg/
# Author: Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)
# Date: 2026-03-04

set -e
OUTDIR="zenodo/SexDiffKG_v4_deposit"
rm -rf "$OUTDIR"
mkdir -p "$OUTDIR/kg" "$OUTDIR/signals" "$OUTDIR/embeddings" "$OUTDIR/analysis" "$OUTDIR/figures"

echo "=== SexDiffKG v4 Zenodo Deposit ==="
echo "Preparing deposit from canonical data/kg_v4/..."

# KG v4 files (canonical)
echo "[1/7] Copying KG v4 files..."
cp data/kg_v4/nodes.tsv "$OUTDIR/kg/"
cp data/kg_v4/edges.tsv "$OUTDIR/kg/"
cp data/kg_v4/triples.tsv "$OUTDIR/kg/"

# Verify checksums match GROUND_TRUTH
echo "[2/7] Verifying KG checksums..."
NODES_MD5=$(md5sum "$OUTDIR/kg/nodes.tsv" | awk '{print $1}')
EDGES_MD5=$(md5sum "$OUTDIR/kg/edges.tsv" | awk '{print $1}')
TRIPLES_MD5=$(md5sum "$OUTDIR/kg/triples.tsv" | awk '{print $1}')
echo "  nodes.tsv:   $NODES_MD5 (expected: 5a7331b1b0e7f11853444eb59e2b9166)"
echo "  edges.tsv:   $EDGES_MD5 (expected: b8e4890c2063bdf9357c76730881b440)"
echo "  triples.tsv: $TRIPLES_MD5 (expected: 2d4e46b1265a9a9bd44bbfc7372a9e44)"

# Signals v4
echo "[3/7] Copying signal files..."
cp results/signals_v4/sex_differential_signals.parquet "$OUTDIR/signals/" 2>/dev/null ||   cp results/signals_v4/sex_differential.parquet "$OUTDIR/signals/" 2>/dev/null ||   echo "  WARNING: No signal parquet found in results/signals_v4/"

# Embeddings (metrics only, not full model weights)
echo "[4/7] Copying embedding metrics..."
cp results/kg_embeddings/distmult_v41_metrics.json "$OUTDIR/embeddings/" 2>/dev/null || true
cp results/kg_embeddings_v4/complex_v4_metrics.json "$OUTDIR/embeddings/" 2>/dev/null ||   cp results/kg_embeddings/ComplEx_v4/complex_v4_metrics.json "$OUTDIR/embeddings/" 2>/dev/null || true
cp results/kg_embeddings/rotatE_v41_cpu_metrics.json "$OUTDIR/embeddings/" 2>/dev/null || true

# Analysis files
echo "[5/7] Copying analysis files..."
cp results/analysis/sexdiffkg_statistics_v4.json "$OUTDIR/analysis/" 2>/dev/null || true
cp results/analysis/signal_validation_benchmarks.json "$OUTDIR/analysis/" 2>/dev/null || true
cp results/analysis/target_sex_bias.tsv "$OUTDIR/analysis/" 2>/dev/null || true
cp results/analysis/v4_model_comparison_full.json "$OUTDIR/analysis/" 2>/dev/null || true

# Figures
echo "[6/7] Copying figures..."
cp results/figures/*.png "$OUTDIR/figures/" 2>/dev/null || echo "  No PNG figures found"
cp results/figures/*.pdf "$OUTDIR/figures/" 2>/dev/null || echo "  No PDF figures found"

# Ground truth + README
echo "[7/7] Copying ground truth and README..."
cp GROUND_TRUTH.json "$OUTDIR/"
cp LICENSE "$OUTDIR/"

# Create Zenodo README
cat > "$OUTDIR/README.md" << 'README'
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
- **3,441 unique drugs**, **5,658 unique adverse events**

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
README

echo ""
echo "=== Deposit ready at $OUTDIR ==="
echo "Contents:"
find "$OUTDIR" -type f | wc -l
echo "files"
du -sh "$OUTDIR"
echo ""
echo "To create archive: cd zenodo && tar -czf SexDiffKG_v4_deposit.tar.gz SexDiffKG_v4_deposit/"
echo "To upload: https://zenodo.org/uploads/new"
