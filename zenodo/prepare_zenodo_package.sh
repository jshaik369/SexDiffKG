#!/bin/bash
# Prepare SexDiffKG Zenodo deposit package
# Run from ~/sexdiffkg/

set -e
OUTDIR="zenodo/SexDiffKG_v3_deposit"
mkdir -p "$OUTDIR/kg" "$OUTDIR/signals" "$OUTDIR/embeddings" "$OUTDIR/analysis" "$OUTDIR/figures"

echo "Copying KG files..."
cp data/kg/nodes.tsv "$OUTDIR/kg/"
cp data/kg/edges.tsv "$OUTDIR/kg/"
cp data/kg/entity2id.tsv "$OUTDIR/kg/"
cp data/kg/relation2id.tsv "$OUTDIR/kg/"
cp data/kg/triples.tsv "$OUTDIR/kg/"

echo "Copying signal files..."
cp results/signals/sex_differential.parquet "$OUTDIR/signals/"

echo "Copying DistMult embeddings..."
cp results/kg_embeddings/DistMult/embeddings/entity_embeddings.npz "$OUTDIR/embeddings/"
cp results/kg_embeddings/DistMult/embeddings/relation_embeddings.npz "$OUTDIR/embeddings/"

echo "Copying analysis files..."
cp results/analysis/sexdiffkg_statistics.json "$OUTDIR/analysis/"
cp results/analysis/target_sex_bias.tsv "$OUTDIR/analysis/"
cp results/analysis/signal_validation_benchmarks.json "$OUTDIR/analysis/"
cp results/analysis/top_female_biased_signals.tsv "$OUTDIR/analysis/"
cp results/analysis/top_male_biased_signals.tsv "$OUTDIR/analysis/"

echo "Copying figures..."
cp results/figures/*.png "$OUTDIR/figures/" 2>/dev/null || echo "No PNG figures found"

echo "Copying README..."
cp zenodo/README_ZENODO.md "$OUTDIR/README.md"

echo "Creating compressed archive..."
cd zenodo
tar -czf SexDiffKG_v3_deposit.tar.gz SexDiffKG_v3_deposit/
ls -lh SexDiffKG_v3_deposit.tar.gz

echo ""
echo "Done! Upload SexDiffKG_v3_deposit.tar.gz to Zenodo."
echo "Zenodo upload: https://zenodo.org/uploads/new"
