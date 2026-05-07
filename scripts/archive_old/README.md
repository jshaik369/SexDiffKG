# LEGACY — V3 Pipeline (archived)

The scripts in this directory comprise the **v3 SexDiffKG pipeline**. They are kept for historical reference and reproducibility of v3-era analyses, but are **superseded by the v4 pipeline** (top-level `scripts/v4_*.py` and `scripts/v5_*.py`).

## What's here

| Script | Purpose | v4 equivalent |
|---|---|---|
| `01_download_faers.py` | Download FAERS quarterly XML dumps | None — v4 ingests pre-downloaded files. **Still useful** for the download step. |
| `02_parse_faers.py` | Parse FAERS XML → parquet | Subsumed by v4 ingest |
| `03_deduplicate.py` | Deduplicate reports by case ID | Subsumed by v4 ingest |
| `03b_normalize_drugs.py` | Drug-name normalization v3 | `scripts/v4_01_normalize_diana.py` (DiAna-based, faster) |
| `04_compute_signals.py` | Sex-stratified ROR computation v3 | `scripts/v4_02_compute_signals.py` |
| `06_build_kg.py` | KG construction v3 | `scripts/v4_03_build_kg.py` |
| `07*_train_*.py` | Embedding training v3 | `scripts/v4_04_train_distmult.py`, `scripts/v4_05_train_rotatE.py`, `scripts/v5_04_train_complex.py` |

## Why keep them?

1. **The v3 FAERS downloader still works** and the v4 pipeline does not yet ship its own. Use `01_download_faers.py` for the download step, then continue with v4 scripts. See `docs/FAERS_SETUP.md`.
2. **Numbers in the originally-submitted ISMB 2026 abstract were computed with v3.** If you need to reproduce those exact numbers, the v3 scripts are the only way.
3. **Audit trail.** v4 patched and re-derived everything; if a future audit questions "what did v3 actually produce?", the answer is here.

## What NOT to do

- Don't run v3 scripts as part of new analyses — use the top-level v4/v5 scripts.
- Don't expect the v3 numbers to match `GROUND_TRUTH.json`. They won't. The v4 patch corrected several v3 errors (290,177 duplicate edges, 3,288 missing drug nodes).
- Don't compare v3 metrics to v4 metrics directly without the patch context.

## Reference

- `GROUND_TRUTH.json` (top-level, canonical v4 numbers)
- `data/kg_v5/GROUND_TRUTH_v5.json` (v5 numbers)
- `data/archive/kg_v3_cleaned/` and `data/archive/kg_v3_original/` (the v3 KG itself, archived)
- `docs/FAERS_SETUP.md` (current setup walkthrough)
