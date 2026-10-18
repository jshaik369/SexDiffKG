# Known issues and revision plan

Found in an independent review of the code and data (October 2026). Listed from most to least important.

## Statistical method
1. **No test for a sex difference.** A pair is labelled sex-differential when |ln ROR(female) − ln ROR(male)| ≥ 0.5 (`scripts/v4_02_compute_signals.py`), with no confidence interval, test or multiple-testing correction. With 10 reports per sex, chance alone crosses this threshold in roughly a quarter of pairs.
2. **Labels where neither sex shows a signal.** The rule compares two RORs even when both are below 1.
3. **Sex-specific terms are included**, for example pregnancy, foetal-exposure and breast-feeding events.

## Data
4. **The same ingredient appears under several drug names** (for example PARACETAMOL and ACETAMINOPHEN; ASPIRIN and ACETYLSALICYLIC ACID; salt forms). This splits drug-level results and inflates the drug count.
5. **Some adverse-event terms appear in two spellings** (for example COUGH and Cough).
6. **The gene, protein and pathway layers use different identifier systems** that do not connect in version 4. Each protein interaction is stored in both directions.
7. **The FDA list of deleted cases is not applied.** The female/male filter runs before deduplication.
8. **The 289 GTEx expression edges** were produced by a script that is not in this repository.
9. `has_adverse_event` means at least 10 reports in one sex, not a disproportionality signal.

## Earlier results (withdrawn pending re-analysis)
10. **Embedding scores** (ComplEx, RotatE, DistMult) were inflated: reverse protein edges and duplicate drug–event edges let test edges be predicted from training edges. Some reported scores have no matching script or result file. The training code has been removed from the current version and remains in the git history.
11. **40-pair literature check (24 of 29 matched):** matching used loose text search and kept the most extreme match. Pairs without a difference were counted as "not found" instead of as failures. One pair was listed twice.
12. **Exploratory analyses, manuscript drafts and abstracts** that were in this repository included numbers that could not be regenerated from code. They have been removed from the current version and remain in the git history.

## Revision plan
- Replace the threshold with an interaction test on ln ROR(female) − ln ROR(male) using both standard errors, with false-discovery-rate control. Require a signal in at least one sex and exclude sex-specific terms.
- Normalise drugs to one ingredient identifier and adverse events to one MedDRA spelling. Apply the FDA deleted-case list.
- Rebuild the graph on unified gene and protein identifiers, with one edge per drug–event pair.
- Re-run the literature check on a fixed list, with exact matching and failures counted.
- Publish every reported number together with the script that produces it.
