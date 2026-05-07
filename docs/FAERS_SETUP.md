# FAERS Setup — Step-by-Step

This document walks through setting up the FDA Adverse Event Reporting System (FAERS) data feed used by SexDiffKG. The reviewer of BOSC submission #536 specifically asked for a clearer walkthrough; this is that document.

## 0. Prerequisites

- Python 3.10+
- ~50 GB free disk for raw quarterly XML/JSON dumps; ~5 GB for parsed parquet output.
- `requirements.txt` installed (`pip install -r requirements.txt`).
- `SEXDIFFKG_HOME` env var set, or accept the default `~/sexdiffkg`.

## 1. Choose a date range

FAERS is published quarterly. Current SexDiffKG ground truth covers **2004Q1 through 2025Q3** (87 quarters, 14,536,008 deduplicated reports). To start fresh, edit `config.yaml`:

```yaml
faers:
  quarter_start: "2004Q1"
  quarter_end:   "2025Q3"
  raw_dir: data/raw/faers
```

## 2. Download

Two paths, depending on what you need:

### 2a. Direct XML dumps (canonical, large)

Download the official quarterly XML dumps from FDA:
- URL pattern: `https://fis.fda.gov/content/Exports/faers_xml_YYYYQN.zip` (e.g. `faers_xml_2025Q3.zip`)
- Index: <https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html>

Each ZIP contains DEMO, DRUG, REAC, OUTC, RPSR, THER, INDI files. Extract into `$SEXDIFFKG_HOME/data/raw/faers/<quarter>/`.

### 2b. openFDA JSON (smaller, easier)

`https://api.fda.gov/drug/event.json` exposes the same data via JSON. Useful for prototyping:

```bash
# Single quarter, one drug, one adverse event:
curl 'https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:"aspirin"+AND+receivedate:[20250701+TO+20250930]&limit=100'
```

**Heads up**: openFDA throttles at 1,000 requests/day without a key, 120,000/day with one. For the full 14.5M-report ingest, use the direct XML dumps (2a). openFDA is fine for ad-hoc validation.

### 2c. Convenience script

The project provides `scripts/01_download_faers.py` (for the v3 pipeline) under `scripts/archive_old/`. The v4 pipeline ingests pre-downloaded files directly — it does not include a downloader. Until a v4 downloader is written, **use the v3 script for the download step**; it produces files that v4 can consume.

```bash
# v3 downloader (from archive_old/), produces $SEXDIFFKG_HOME/data/raw/faers/
python3 scripts/archive_old/01_download_faers.py
```

## 3. Parse + deduplicate

```bash
# v3 pipeline (also works for v4 ingest):
python3 scripts/archive_old/02_parse_faers.py
python3 scripts/archive_old/03_deduplicate.py
```

Parsing produces parquet files in `$SEXDIFFKG_HOME/data/processed/faers/`. Deduplication is by case ID; reports with the same ID across quarters are kept once (latest report wins).

Expected output after dedup (full 2004Q1–2025Q3 range):
- `reports_dedup.parquet` — 14,536,008 rows
- Female: 8,744,397
- Male: 5,791,611

These numbers must match `GROUND_TRUTH.json/faers/total_reports_deduplicated`. If they don't, your ingest is incomplete; do not proceed to KG construction.

## 4. Drug-name normalization

```bash
python3 scripts/archive_old/03b_normalize_drugs.py            # legacy v3
# OR, faster v4 normalization with DiAna:
python3 scripts/v4_01_normalize_diana.py
```

DiAna provides 47% match rate by drug-name standardization. See `drug_normalization.log` for per-source resolution stats.

## 5. Compute sex-differential signals

```bash
python3 scripts/v4_02_compute_signals.py
```

Output: `$SEXDIFFKG_HOME/results/signals_v4/sex_differential_v4.parquet` with columns:
`drug_name, adverse_event, ror_female, ror_male, n_female, n_male, log_ratio, direction`.

Expected: 254,114 total comparisons → 96,281 sex-differential → 32,244 strong (|log_ratio| > 1).

## 6. Build the knowledge graph

```bash
python3 scripts/v4_03_build_kg.py
```

Produces `$SEXDIFFKG_HOME/data/kg_v4/{nodes.tsv, edges.tsv, triples.tsv}`. Final patched counts are 113,155 entities / 1,532,674 unique triples.

## 7. Train embeddings

```bash
# DistMult (fast, ~1 hour on GPU):
python3 scripts/v4_04_train_distmult.py

# RotatE (slower, ~6 hours on CPU):
python3 scripts/v4_05_train_rotatE.py

# ComplEx (best v4 model):
python3 scripts/v5_04_train_complex.py
```

Results land in `$SEXDIFFKG_HOME/results/models_v4/`. Compare against `GROUND_TRUTH.json/models/*` for expected MRR / Hits@10 / AMRI.

## 8. Verify

```bash
python3 scripts/audit_proof_verification.py
```

This re-derives every number in `GROUND_TRUTH.json` from raw data and produces `audit_proof_report.json` with PASS/FAIL per claim. Investigate any FAIL.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| "Permission denied" on raw files | Downloaded to wrong directory | Set `SEXDIFFKG_HOME` correctly |
| Report counts off by ~5% | One quarter missing | Check `data/raw/faers/` for gaps |
| openFDA 429 errors | Rate limited | Get an API key, or fall back to XML dumps |
| Embedding MRR wildly different from ground truth | Wrong KG version active | Check `config.yaml/kg/active_version` |
| Hardcoded path errors | Old script | Pull latest from `cleanup/ismb-poster-prep` (or main once merged) |
