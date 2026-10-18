# SexDiffKG

A knowledge graph that links drugs, adverse events, genes, proteins and pathways, with adverse-event reporting from the FDA Adverse Event Reporting System (FAERS) analysed separately for women and men.

> **Status (October 2026): under revision.**
> An independent review of the code found problems with the statistical method used to label drug–event pairs as sex-differential, and with several results reported earlier (embedding scores, a 40-pair literature check, and analyses whose code was not kept).
> Until the revision is finished, treat the sex-difference labels as exploratory. Do not cite results from earlier drafts, abstracts or earlier versions of this README.
> Details and the revision plan: [KNOWN_ISSUES.md](KNOWN_ISSUES.md).

## What is in this repository

| Path | Content |
|------|---------|
| `data/kg_v4/nodes_patched.tsv` | 113,155 nodes (version 4) |
| `data/kg_v4/edges_deduped.tsv`, `triples_deduped.tsv` | 1,532,674 unique edges (version 4) |
| `data/kg_v4/nodes.tsv` | Original node list (109,867; lacks 3,288 drug nodes) |
| `data/kg_v5.2/` | Version 5.2: v4 merged with VEDA-KG data, 217,993 nodes, 3,194,017 edges (edges and triples in Git LFS) |
| `data/external/`, `data/processed/`, `data/reference/` | Lookup tables (SIDER/MedDRA, ATC classes, indications) |
| `GROUND_TRUTH.json` | Reference counts and file checksums |
| `results/signals_v4/` | Summary of the signal computation |
| `results/validation_40_benchmarks_v4.json` | Literature check (see known issues before using) |
| `scripts/` | Code that builds the signals and the graph |

The node and edge files match the MD5 checksums in `GROUND_TRUTH.json`.

### Version 4 contents

| | Count |
|---|---:|
| FAERS reports, deduplicated, sex recorded as female or male (2004 Q1 – 2025 Q3) | 14,536,008 |
| ...female | 8,744,397 (60.2%) |
| ...male | 5,791,611 (39.8%) |
| Drug–event pairs compared (at least 10 reports in each sex) | 254,114 |
| Pairs labelled sex-differential | 96,281 (51,771 higher in women, 44,510 higher in men) |

| Edge type | Unique edges | Source |
|---|---:|---|
| `has_adverse_event` | 614,978 | FAERS |
| `interacts_with` | 473,860 (each interaction stored in both directions) | STRING v12.0, score ≥ 700 |
| `participates_in` | 341,492 | Reactome |
| `sex_differential_adverse_event` | 96,281 | FAERS (see method) |
| `targets` | 5,774 | ChEMBL 36 |
| `sex_differential_expression` | 289 | GTEx v8 |

## Method

1. FAERS quarterly files are parsed. One report is kept per case (the latest version), and only reports with sex recorded as female or male are used. Only primary and secondary suspect drugs are counted.
2. Drug names are normalised with the DiAna dictionary, the FDA active-ingredient field and ChEMBL synonyms. Remaining names are cleaned as text.
3. For each drug–event pair, a reporting odds ratio (ROR) is computed separately within female and within male reports. Pairs need at least 10 reports in each sex.
4. A pair is labelled sex-differential when |ln ROR(female) − ln ROR(male)| ≥ 0.5.
   **This rule has no statistical test, confidence interval or multiple-testing correction, so many labels at low report counts are expected to be noise.** Replacing it is the first item of the revision.
5. Signals are combined with ChEMBL drug targets, STRING interactions, Reactome pathways and GTEx sex-biased expression to form the graph.

### What FAERS can and cannot show

FAERS is a voluntary reporting system. It cannot measure incidence or risk. Reporting depends on who reports, how widely a drug is used, age, indication and co-medication. A difference in reporting between women and men is a question for further study, not evidence of a difference in drug safety. **Nothing here is medical advice.**

## Running the code

The scripts read the project location from the environment variable `SEXDIFFKG_HOME` (default `~/sexdiffkg`).
Raw FAERS files, the DiAna dictionary and the ChEMBL database are not included and must be downloaded separately, so the full pipeline cannot yet be run from this repository alone.

```
pip install -r requirements.txt
```

## Data sources and licences

| Source | Licence |
|---|---|
| [FDA FAERS](https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html) | Public domain |
| [ChEMBL 36](https://www.ebi.ac.uk/chembl/) | CC BY-SA 3.0 |
| [STRING v12.0](https://string-db.org) | CC BY 4.0 |
| [Reactome](https://reactome.org) | CC BY 4.0 |
| [GTEx v8](https://gtexportal.org) | Open access |
| [DiAna](https://github.com/fusarolimichele/DiAna_package) | See source |

Code is released under the MIT licence. Data derived from these sources keep the terms of their sources; check them before reuse.

## Citation

See [CITATION.cff](CITATION.cff) (Zenodo DOI 10.5281/zenodo.18819192).

## Author

Mohammed Javeed Akhtar Abbas Shaik, independent researcher, Barcelona. ORCID [0009-0002-1748-7516](https://orcid.org/0009-0002-1748-7516).
