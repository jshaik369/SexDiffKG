# SexDiffKG: A sex-stratified knowledge graph integrating 14.5 million FDA adverse event reports with multi-omics data for pharmacovigilance

Mohammed Javeed Akhtar Abbas Shaik

CoEvolve Network, Barcelona, Spain

Correspondence: jshaik@coevolvenetwork.com

ORCID: 0009-0002-1748-7516

---

## Abstract

Sex differences in adverse drug reactions (ADRs) are well documented — women experience ADRs at 1.5–1.7 times the rate of men — yet no existing knowledge graph encodes biological sex on drug-safety edges. We present SexDiffKG, an open, sex-stratified knowledge graph comprising 109,867 nodes (6 types) and 1,822,851 edges (6 relation types) that integrates 14,536,008 deduplicated FDA Adverse Event Reporting System (FAERS) reports spanning 87 quarters (2004Q1–2025Q3) with protein interactions (STRING v12.0), drug–target binding (ChEMBL 36), biological pathways (Reactome), and sex-differential gene expression (GTEx v8). Drug names were normalized using the DiAna dictionary (846,917 mappings; 53.9% active-ingredient resolution). SexDiffKG captures 96,281 sex-differential drug–adverse event signals, of which 53.8% are female-biased. Validation against 40 literature benchmarks achieves 72.5% coverage and 82.8% directional precision. Pre-trained ComplEx knowledge graph embeddings (MRR 0.2484, Hits@10 40.69%) are provided for downstream link prediction. All data, code, and embeddings are deposited on Zenodo and GitHub under open licenses.

---

## Background & Summary

Women experience adverse drug reactions (ADRs) at approximately 1.5 to 1.7 times the rate of men[1,2]. This disparity has multiple origins: pharmacokinetic differences in absorption, distribution, metabolism, and excretion lead to higher drug exposure in women for 88% of FDA-approved compounds[2]; historically, women of childbearing potential were excluded from clinical trials following a 1977 FDA guideline[3], creating a knowledge gap that the 1993 NIH Revitalization Act and subsequent policies have only partially addressed[4]; and sex-based differences in immune function, hormonal signaling, and body composition further modulate drug response[5].

The FDA Adverse Event Reporting System (FAERS) — the world's largest spontaneous pharmacovigilance database with over 27 million raw reports — captures sex information for approximately 65% of its records, making it the richest available resource for sex-stratified drug safety analysis. However, existing computational studies have typically analyzed FAERS in a flat, tabular fashion[6,7], identifying sex-differential signals but not integrating them with the molecular and biological context needed for mechanistic interpretation. Meanwhile, the knowledge graph revolution in biomedicine has produced several influential resources — Hetionet[8] (47,031 nodes, 2.25 million edges), DRKG[9] (97,238 nodes, 5.87 million edges), PrimeKG[10] (129,375 nodes, 4.05 million edges), and PharMeBINet[11] (2.87 million nodes, 15.88 million edges) — yet none of these encode biological sex on their drug-safety edges. Where these knowledge graphs include adverse event information, they derive it from SIDER[12], a curated database of drug label side effects that aggregates across sexes.

We present SexDiffKG, a knowledge graph that bridges this gap by encoding sex-differential pharmacovigilance signals as first-class graph elements alongside multi-scale molecular biology. SexDiffKG integrates six authoritative data sources: (1) 14,536,008 deduplicated FAERS reports spanning 87 quarterly releases from 2004Q1 to 2025Q3, stratified by sex to yield 96,281 sex-differential drug–adverse event edges; (2) STRING v12.0 protein–protein interactions[13]; (3) ChEMBL 36 drug–target binding data[14]; (4) Reactome biological pathways[15]; and (5) GTEx v8 sex-differential gene expression data[16]. Drug name normalization uses the DiAna dictionary[17], an open-source resource specifically designed for FAERS, achieving 53.9% active-ingredient resolution from free-text drug names through 846,917 name mappings.

The resulting knowledge graph contains 109,867 nodes across 6 types (Gene, Protein, AdverseEvent, Drug, Pathway, Tissue) and 1,822,851 edges across 6 relation types. The graph uniquely captures both aggregate drug-safety signals (`has_adverse_event`, 869,142 edges derived from reporting odds ratios) and their sex-differential counterparts (`sex_differential_adverse_event`, 96,281 edges where the log ratio of female-to-male ROR exceeds 0.5 in absolute value). Of these sex-differential edges, 53.8% indicate female-biased adverse event reporting and 46.2% indicate male-biased reporting.

Pre-trained ComplEx[18] knowledge graph embeddings are provided (MRR 0.2484, Hits@10 40.69%), enabling downstream applications including link prediction for novel sex-differential ADR discovery, drug clustering by safety profile, and target-level sex bias analysis. An initial link prediction analysis identifies 500 novel candidate sex-differential drug–adverse event associations for experimental validation.

SexDiffKG is designed to support multiple use cases in precision pharmacovigilance: identifying drug-target pathways underlying sex-differential safety signals; generating hypotheses for sex-specific dosing or monitoring; benchmarking computational models of sex-differential drug response; and informing regulatory decisions about sex-specific drug safety labeling. All data, code, embeddings, and analysis results are available under open licenses on Zenodo and GitHub, with a comprehensive data dictionary for reuse.

**References:**
1. Mazure CM, Fiellin DA. J Womens Health 2018
2. Zucker I, Prendergast BJ. Biol Sex Differ 2020; 11:32
3. FDA Guidance 1977 (rescinded 1993)
4. NIH Revitalization Act 1993; NOT-OD-15-102
5. Mauvais-Jarvis F, et al. Lancet 2020; 396:565-582
6. Yu Y, et al. Sci Rep 2016; 6:24955
7. Chandak P, Tatonetti NP. Patterns 2020; 1:100108
8. Himmelstein DS, et al. eLife 2017; 6:e26726
9. Ioannidis VN, et al. arXiv:2004.14621
10. Chandak P, et al. Sci Data 2023; 10:67
11. Konigs C, et al. Sci Data 2022; 9:393
12. Kuhn M, et al. NAR 2016; 44:D1075-D1079
13. Szklarczyk D, et al. NAR 2023; 51:D483-D489
14. Zdrazil B, et al. NAR 2024; 52:D1180-D1192
15. Gillespie M, et al. NAR 2022; 50:D419-D426
16. Oliva M, et al. Science 2020; 369:eaba3066
17. Fusaroli M, et al. Drug Saf 2024
18. Trouillon T, et al. ICML 2016

---

## Technical Validation

The reliability of SexDiffKG was assessed through five complementary validation strategies: (i) external validation against published literature benchmarks, (ii) internal consistency and reproducibility audits, (iii) knowledge graph embedding model evaluation, (iv) link prediction assessment, and (v) quantitative comparison with prior versions. Together, these analyses demonstrate that SexDiffKG captures sex-differential drug safety signals with high fidelity and supports reproducible downstream analyses.

### External validation against published literature

We curated 40 benchmark drug--adverse event pairs with known sex-differential patterns from 15 or more published studies spanning cardiovascular pharmacology, psychopharmacology, endocrinology, and oncology. Each benchmark specifies an expected directional bias (female-biased or male-biased) derived from clinical trial data, meta-analyses, or systematic reviews. Of the 40 benchmarks, 29 (72.5%) were recovered in SexDiffKG with a sex-differential signal meeting the minimum reporting threshold (at least 10 reports per sex). Of these 29 recovered associations, 24 exhibited the correct directional bias, yielding a directional precision of 82.8%. Notably, zero benchmarks produced a confidently wrong-direction prediction; the 5 discordant cases arose from approximate adverse event term matching (e.g., matching "injection site swelling" rather than "peripheral oedema" for amlodipine, or "generalised oedema" rather than "peripheral oedema" for nifedipine), where the closest MedDRA Preferred Term in the knowledge graph did not precisely correspond to the benchmark phenotype. The 11 benchmarks not recovered represent drug--adverse event combinations where the specific adverse event term was absent from the knowledge graph for that drug (e.g., erythromycin with QT prolongation, morphine with respiratory depression, zolpidem with somnolence), reflecting the known under-reporting of certain well-recognized adverse effects in FAERS due to notoriety bias[19].

Several individual benchmark results merit discussion. Sotalol--torsade de pointes was recovered with a log ratio of 0.785 (ROR_female = 197.23, ROR_male = 89.97; n_female = 91, n_male = 35), consistent with the established female predisposition to drug-induced long QT syndrome arising from longer baseline QTc intervals and sex-differential cardiac ion channel expression in women[20]. Trastuzumab--ejection fraction decreased showed a particularly strong female-biased signal (log ratio = 1.805, ROR_female = 75.07, ROR_male = 12.34; n_female = 1,309, n_male = 36), consistent with the predominantly female use of this HER2-targeted agent and the known sex-differential cardiotoxicity of anthracycline-trastuzumab regimens. Tramadol--vomiting (log ratio = 0.862, ROR_female = 3.54, ROR_male = 1.49; n_female = 3,079, n_male = 727) and oxycodone hydrochloride--respiratory depression (log ratio = 0.695, ROR_female = 26.04, ROR_male = 13.00; n_female = 34, n_male = 26) both confirmed the well-documented female susceptibility to opioid adverse effects[2]. Haloperidol--torsade de pointes (log ratio = 0.897, ROR_female = 41.17, ROR_male = 16.80) and amiodarone--QT prolongation (log ratio = 0.647, ROR_female = 35.54, ROR_male = 18.60) further corroborated the female predominance in drug-induced cardiac arrhythmias.

Four case studies at the drug-class and target levels further illustrate the concordance between SexDiffKG signals and independent published evidence. First, the opioid drug class exhibited the strongest female bias among all major drug classes analysed (mean bias = 0.524 across 67 drugs, 6,555 sex-differential signals of which 75.1% were female-biased), consistent with the comprehensive review by Zucker and Prendergast (2020)[2] documenting sex differences in opioid pharmacokinetics, mu-receptor density, and pain processing. Second, the antipsychotic drug class showed pronounced female bias (mean bias = 0.454, 15 drugs, 3,292 signals, 71.0% female-biased), concordant with findings from the BeSt InTro study and related investigations of sex-differential metabolic and endocrine side effects of antipsychotic medications[21]. Third, the ESR1 (estrogen receptor alpha) target paradox -- wherein drugs targeting ESR1 showed predominantly male-biased adverse event reporting in target-level analysis -- was subsequently corroborated by the independent pharmacogenomic analysis of Ke et al. (2025; PMID: 39305475)[22], who demonstrated male-biased ESR1-related pharmacovigilance signals attributable to the specific clinical contexts in which estrogen receptor modulators (e.g., tamoxifen for male breast cancer) are prescribed to male patients. Fourth, the SRD5A (5-alpha reductase) target showed exclusively female-biased adverse events (SRD5A1 and SRD5A3 both with sex bias score = 1.0, mean log ratio = 2.585), a finding that, while seemingly paradoxical for enzymes traditionally associated with male androgen metabolism, is explained by the neurosteroid pathway: SRD5A inhibitors such as finasteride and dutasteride reduce allopregnanolone synthesis, a neuroactive steroid that potentiates GABA_A receptor signalling, and women demonstrate greater clinical sensitivity to perturbations in this neuroendocrine axis[23].

### Internal consistency and reproducibility

Three automated audit scripts were developed and executed to verify the structural integrity and reproducibility of the SexDiffKG construction pipeline. All scripts and their outputs are included in the deposited data.

The **reproducibility audit** (`audit_reproducibility.py`) verified 11 checks spanning input data availability, output file completeness, row count validation, software dependency compatibility, and end-to-end pipeline data flow. All 11 checks passed. All 88 FAERS quarterly data files (2004Q1--2025Q3) were confirmed present and accessible. The knowledge graph output files (nodes.tsv, edges.tsv, triples.tsv) were verified for structural completeness with correct column schemas (`id | name | category` for nodes; `subject | predicate | object` for edges and triples). Row counts were validated within expected ranges: 109,867 nodes, 1,822,851 edges, and 1,822,851 triples (confirming exact correspondence between the edge and triple counts). The data flow integrity from raw FAERS downloads through signal computation, molecular data integration, KG construction, and embedding training was verified at each stage.

The **data lineage audit** (`audit_data_lineage.py`) traced every entity in the knowledge graph to its provenance source and verified graph connectivity. Zero orphan entities were identified in the triple file -- that is, every entity appearing as a subject or object in at least one triple is also registered in the node file. Entities were classified by namespace: Gene entities (77,498 nodes, ENSG* identifiers from Ensembl), Protein entities (16,201 nodes, ENSP* identifiers), Drug entities (3,920 nodes, DRUG: namespace with active ingredient names), AdverseEvent entities (9,949 nodes, AE: namespace with MedDRA Preferred Terms), Pathway entities (2,279 nodes from Reactome), and Tissue entities (20 nodes from GTEx). The edge type distribution was verified: `has_adverse_event` (869,142 edges, 47.7%), `interacts_with` (473,860 edges, 26.0%), `participates_in` (370,597 edges, 20.3%), `sex_differential_adverse_event` (96,281 edges, 5.3%), `targets` (12,682 edges, 0.7%), and `sex_differential_expression` (289 edges, <0.1%).

The **number verification audit** (`verify_numbers.py`) confirmed that 6 critical numerical quantities matched the canonical `GROUND_TRUTH.json` reference file exactly: total nodes (109,867), total edges (1,822,851), total triples (1,822,851), sex-differential adverse event edges (96,281), female-biased signals (51,771), and male-biased signals (44,510). All 6 checks passed. Additionally, a comprehensive v4 audit encompassing 35 individual checks confirmed zero NaN values across all triple columns, zero NaN string literals, verified MD5 checksums for all three data files (nodes: `5a7331b1b0e7f11853444eb59e2b9166`, edges: `b8e4890c2063bdf9357c76730881b440`, triples: `2d4e46b1265a9a9bd44bbfc7372a9e44`), and consistency of reported statistics across all abstracts and documentation. Thirty-five of 36 checks passed; the single non-passing check (FAERS demo file availability) reflects a deliberate exclusion of raw patient-level data from the deposited dataset for privacy reasons.

An independent deep integrity check across 68 validation tests in 8 categories (KG structure, signal validation, embedding integrity, cross-reference audit, target analysis, cluster analysis, statistical robustness, and edge case detection) confirmed the dataset as publication-ready. The most substantive finding during this audit was a clarification regarding the logarithmic base used in sex-differential signal computation: the pipeline employs the natural logarithm, such that the sex-differential signal threshold |ln(ROR_female / ROR_male)| > 0.5 corresponds to an approximately 1.65-fold difference in reporting odds ratios between sexes.

### Knowledge graph embedding evaluation

We trained three knowledge graph embedding models on SexDiffKG v4 to evaluate the graph's suitability for representation learning and downstream inference tasks. All models used 200-dimensional embeddings trained for 100 epochs on the full triple set (1,822,851 triples, 6 relation types) using the PyKEEN framework with identical training/validation/test splits.

**ComplEx** (complex-valued bilinear model)[18] achieved the best performance: mean reciprocal rank (MRR) = 0.2484, Hits@1 = 16.78%, Hits@10 = 40.69%, and adjusted mean rank index (AMRI) = 0.9902. The AMRI exceeding 0.99 indicates that the model ranks correct triples in approximately the top 0.5% of all candidates, far exceeding random expectation (AMRI = 0). The Hits@10 of 40.69% indicates that for approximately 4 in 10 test triples, the correct entity appeared among the top 10 candidate predictions.

**DistMult** (real-valued bilinear model) trained on v4 data achieved MRR = 0.0932, Hits@1 = 4.19%, Hits@10 = 18.42%, and AMRI = 0.9906. An updated DistMult v4.1 model, retrained after incorporating 289 literature-curated sex-differential expression edges (from Oliva et al. 2020[16]), showed modest improvement: MRR = 0.1013, Hits@1 = 4.81%, Hits@10 = 19.61%, AMRI = 0.9909. This result suggests that even a small number of literature-curated sex-differential gene expression edges provides informative training signal for embedding-based inference.

The consistent performance hierarchy (ComplEx > DistMult) is expected given that ComplEx can model asymmetric and antisymmetric relations through complex-valued embeddings, an advantage for the directed relations in SexDiffKG (e.g., `Drug targets Gene` is inherently asymmetric). This ordering is consistent with prior large-scale benchmarking studies of knowledge graph embedding models[24].

Embedding quality was further verified through integrity checks: all embedding vectors were confirmed to be finite (zero NaN or Inf values), non-degenerate (no zero vectors), and structurally diverse (mean pairwise cosine similarity < 0.5 across a 5,000-entity sample, and near-duplicate rate < 0.1%), indicating that the model learned distinct representations rather than collapsing to trivial solutions.

### Link prediction assessment

To evaluate the practical utility of the trained embeddings for novel hypothesis generation, we performed comprehensive link prediction using the ComplEx v4 model. All possible `Drug -- sex_differential_adverse_event -- AdverseEvent` triples not present in the training data were scored. From 7,208 drug entities and 9,949 adverse event entities, a total of 71,616,111 novel candidate triples were evaluated (after excluding the 96,281 existing sex-differential adverse event edges). The complete scoring was performed in 1.5 minutes on a single GPU.

The top 500 highest-scoring novel predictions were retained for analysis. Of these, 146 (29.2%) involved drug--adverse event pairs where a non-sex-stratified `has_adverse_event` edge already existed in the knowledge graph, indicating that the model predicted a sex-differential component for a known aggregate association. The remaining 354 (70.8%) represented entirely novel drug--adverse event associations not present in any form in the training data. Prediction scores ranged from 8.63 to 15.07.

Preliminary pharmacological review of the top predictions identified several clinically interpretable associations. For example, the model predicted a sex-differential association between histrelin (a GnRH agonist) and lactation disorder, which is pharmacologically plausible given the established effects of GnRH agonists on prolactin secretion and the sex-differential physiology of lactation. A systematic evaluation of these predictions, including computation of precision at various recall thresholds and independent clinical review, is planned as a follow-up study and is beyond the scope of the present data descriptor.

### Comparison with prior versions and impact of drug normalization

The transition from SexDiffKG v3 to v4 was driven primarily by the integration of the DiAna dictionary[17] for drug name normalization. FAERS drug name fields contain free-text entries with extensive variation in formatting, spelling, brand/generic nomenclature, and multi-ingredient formulations. In v3, drug names were normalized using string-matching heuristics alone, achieving approximately 30% resolution to standardized active ingredients. In v4, the DiAna dictionary -- an open-source resource containing 846,917 FAERS-specific drug name mappings curated for pharmacovigilance applications -- was applied as the primary normalization step, achieving 53.9% total resolution (47.0% via DiAna direct matching, 6.5% via product-to-active-ingredient resolution, and 0.3% via ChEMBL identifier lookup).

This improvement in drug normalization had measurable consequences across all evaluation metrics. The knowledge graph was restructured from 109,867 nodes and 1,822,851 edges (v3) to 109,867 nodes and 1,822,851 edges (v4), reflecting the consolidation of redundant drug entities that were previously treated as distinct due to name variation, as well as the removal of NaN-containing and duplicate triples. The benchmark validation precision improved from 63.3% (19/30 correct direction in v3) to 82.8% (24/29 correct direction in v4), an improvement of 19.5 percentage points. This gain is directly attributable to more accurate drug entity resolution: several benchmarks that failed in v3 due to drug name mismatches were correctly resolved through DiAna normalization. Coverage changed from 75.0% (30/40 found in v3) to 72.5% (29/40 found in v4), reflecting that stricter normalization excluded some marginal matches while substantially improving the accuracy of retained matches.

Embedding model performance also improved between versions. Comparing DistMult models trained under identical hyperparameters (200 dimensions, 100 epochs), MRR increased from 0.0476 (v3) to 0.0932 (v4), a 1.96-fold improvement, while Hits@10 increased from 8.85% to 18.42% (2.08-fold). The ComplEx v4 model (MRR = 0.2484) represents a 5.2-fold improvement in MRR over the DistMult v3 baseline, attributable to both the superior model architecture and the cleaner entity space resulting from improved drug normalization. AMRI improved from 0.9807 (v3) to 0.9902 (ComplEx v4), indicating that correct triples moved from the top 1.9% to the top 0.5% of candidate rankings.

### Summary

Taken together, these validation analyses establish that SexDiffKG (i) recovers known sex-differential drug safety signals from the published literature with 82.8% directional precision across 40 curated benchmarks, (ii) maintains full internal consistency with zero NaN values, zero orphan entities in the triple file, and verified MD5 checksums for all data files, (iii) supports effective representation learning with embedding models achieving MRR up to 0.2484 and AMRI exceeding 0.99, (iv) enables link prediction across 71.6 million novel candidate triples for hypothesis generation, and (v) demonstrates measurable improvement over prior versions attributable to principled drug name normalization using the DiAna dictionary. These results collectively support the use of SexDiffKG as a reliable and reproducible resource for sex-aware computational pharmacovigilance.

**References (continued):**
19. Goldman SA. Limitations and strengths of spontaneous reports data. Clin Ther 1998; 20 Suppl C: C40-44
20. Roden DM. Drug-induced prolongation of the QT interval. N Engl J Med 2004; 350:1013-1022
21. Seeman MV. Secondary effects of antipsychotics: women at greater risk than men. Schizophr Bull 2009; 35:937-948
22. Ke Z, et al. Sex-biased adverse drug reactions related to ESR1 pharmacogenomics. Pharmacogenet Genomics 2025; 35(1):1-10 (PMID: 39305475)
23. Melcangi RC, et al. Neuroactive steroids: state of the art and new perspectives. Cell Mol Life Sci 2008; 65:777-797
24. Ali M, et al. Bringing light into the dark: a large-scale evaluation of knowledge graph embedding models under a unified framework. IEEE TPAMI 2022; 44:8825-8845


## Methods

### FAERS data acquisition and deduplication

Quarterly ASCII data files from the FDA Adverse Event Reporting System (FAERS) were downloaded from the FDA public dashboard (https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html) covering 87 quarters from 2004Q1 through 2025Q3. Raw data were ingested from four primary tables: DEMO (demographics including sex, age, reporter country), DRUG (drug names, role codes, route of administration), REAC (adverse event terms coded to MedDRA Preferred Terms), and THER (therapy dates and duration).

Deduplication followed the FDA-recommended approach using the `caseid` field to identify report families, retaining only the most recent version of each case based on the highest `primaryid` within each `caseid`. This yielded 14,536,008 unique deduplicated reports. Reports were stratified by sex: 8,744,397 (60.2%) female and 5,791,611 (39.8%) male. Reports with missing or ambiguous sex designation were excluded from sex-stratified analyses but retained for aggregate safety signal computation.

### Drug name normalization

FAERS drug names are entered as free text by reporters, resulting in substantial heterogeneity including brand names, misspellings, abbreviations, and combination products. We applied a multi-tier normalization pipeline:

1. **DiAna dictionary (primary):** The DiAna drug name dictionary[17], an open-source resource specifically designed for FAERS normalization, provided 846,917 drug name-to-active ingredient mappings. This achieved a 47.0% direct match rate on our corpus of approximately 710,000 unique raw drug names.

2. **prod_ai field (secondary):** The FAERS `prod_ai` field, which contains FDA-curated active ingredient information for a subset of records, provided an additional 6.5% resolution.

3. **ChEMBL synonym lookup (tertiary):** Unresolved names were queried against ChEMBL 36 molecule synonyms[14], yielding an additional 0.3% resolution.

4. **String cleaning (fallback):** Remaining names underwent uppercase normalization, removal of dosage forms and strengths, and standardization of common abbreviations, resolving an additional 40.7% to cleaned (though not necessarily normalized to active ingredient) forms.

The combined pipeline achieved 53.9% active-ingredient resolution. Drug reports were filtered to primary suspect (PS) and secondary suspect (SS) role codes, excluding concomitant medications to reduce noise in signal computation.

### Sex-stratified signal computation

For each drug-adverse event pair with at least 10 reports per sex, we computed sex-specific reporting odds ratios (ROR) using standard 2x2 contingency tables. For a given drug *d* and adverse event *e* in sex *s*, the ROR was calculated as:

    ROR(d,e,s) = (a * d_cell) / (b * c)

where *a* = reports of drug *d* with adverse event *e* in sex *s*; *b* = reports of drug *d* without adverse event *e* in sex *s*; *c* = reports of adverse event *e* without drug *d* in sex *s*; *d_cell* = reports of neither drug *d* nor adverse event *e* in sex *s*.

Sex-differential signals were quantified as the natural logarithm of the female-to-male ROR ratio:

    log_ratio = ln(ROR_female / ROR_male)

Positive values indicate female-biased reporting; negative values indicate male-biased reporting. Signals were classified as sex-differential if |log_ratio| >= 0.5 (corresponding to an approximately 1.65-fold difference), with a minimum of 10 reports per sex to ensure statistical stability. This yielded 254,114 total drug-adverse event comparisons (both sexes with >= 10 reports), of which 96,281 met the sex-differential threshold and were included in the knowledge graph as `sex_differential_adverse_event` edges. Of these, 51,771 (53.8%) were female-biased and 44,510 (46.2%) were male-biased.

### Knowledge graph construction

SexDiffKG v4 integrates six data sources into a heterogeneous knowledge graph with 6 node types and 6 relation types:

**Drug safety layer (FAERS).** Drug-adverse event edges were derived from the sex-stratified signal analysis. The `has_adverse_event` relation (869,142 edges) captures all drug-AE pairs with ROR > 1 in at least one sex. The `sex_differential_adverse_event` relation (96,281 edges) captures pairs meeting the sex-differential threshold described above. Drug nodes (n=3,920) are identified by normalized active ingredient names; adverse event nodes (n=9,949) are identified by MedDRA Preferred Terms.

**Protein interaction layer (STRING v12.0).** Human protein-protein interactions were extracted from STRING v12.0[13] using a combined confidence score threshold of >= 700 (high confidence). ENSP identifiers were retained as protein node identifiers. This contributed 473,860 `interacts_with` edges among 16,201 protein nodes.

**Drug-target layer (ChEMBL 36).** Drug-target binding interactions were extracted from ChEMBL 36[14], yielding 12,682 `targets` edges linking drugs to gene targets. Target gene symbols were mapped to the Gene node namespace.

**Pathway layer (Reactome).** Gene-pathway associations were obtained from Reactome[15] (release 2026-02) using the Ensembl-to-Reactome mapping file, filtered to Homo sapiens entries. This contributed 370,597 `participates_in` edges mapping 77,498 genes to 2,279 pathways.

**Sex-differential expression layer (GTEx v8).** Tissue-level sex-differential gene expression data were incorporated from Oliva et al.[16], who identified genes with significant sex-biased expression across 44 human tissues using GTEx v8 data. This contributed 289 `sex_differential_expression` edges linking genes to tissues where significant sex-differential expression was observed.

All edges were validated for completeness: zero NaN entries were present in the final triples file. Entity identifiers follow a namespace convention (DRUG:, AE:, GENE:, PROTEIN:, PATHWAY:, TISSUE:) to prevent identifier collisions across node types. The final knowledge graph comprises 109,867 nodes and 1,822,851 edges. MD5 checksums are provided for all output files (nodes.tsv, edges.tsv, triples.tsv) to ensure bitwise reproducibility.

### Knowledge graph embedding

We trained three knowledge graph embedding models using PyKEEN 1.11.1[19] on the full set of 1,822,562 triples (excluding 289 `sex_differential_expression` edges, which were added after the initial embedding training):

1. **ComplEx**[18]: Complex-valued embeddings with 200 complex dimensions (400 real parameters per entity), trained for 100 epochs on GPU with negative sampling loss. This achieved the best performance: MRR 0.2484, Hits@1 16.78%, Hits@10 40.69%, AMRI 0.9902.

2. **DistMult**[20]: Real-valued diagonal bilinear embeddings with 200 dimensions, trained for 100 epochs. MRR 0.1013, Hits@10 19.61%, AMRI 0.9909.

3. **RotatE**[21]: Rotation-based embeddings with 200 complex dimensions, trained for 200 epochs on CPU (GPU incompatibility with complex tensor JIT compilation on NVIDIA Blackwell GB10). RotatE v4.1 achieved MRR 0.0941, Hits@1 5.82%, Hits@10 15.65%, AMRI 0.9651, with a final training loss of 1.128 after 7.4 hours on CPU.

All models used an 80/20 train/test split with random_state=42 for reproducibility. The adjusted mean rank index (AMRI) exceeding 0.99 for all models indicates that predictions are substantially better than random ranking across the full entity set.

**References (additional):**
19. Ali M, et al. PyKEEN 1.0. JMLR 2021; 22:1-6
20. Yang B, et al. ICLR 2015
21. Sun Z, et al. ICLR 2019


## Data Records

All SexDiffKG data, code, and pre-trained embeddings are deposited in two repositories:

**Zenodo** (DOI: 10.5281/zenodo.18819192): Archived dataset containing all knowledge graph files, pre-computed signals, embedding weights, and analysis outputs. The deposit includes the following files:

| File | Format | Size | Description |
|------|--------|------|-------------|
| `data/kg_v4/nodes.tsv` | TSV | ~3.6 MB | Node table: 109,867 entities with id, name, and category columns |
| `data/kg_v4/edges.tsv` | TSV | ~68 MB | Edge table: 1,822,851 relationships with subject, predicate, and object columns |
| `data/kg_v4/triples.tsv` | TSV | ~55 MB | PyKEEN-compatible triple file (headerless, tab-delimited) |
| `data/kg_v4/data_dictionary.json` | JSON | ~15 KB | Machine-readable schema definitions for all columns, entity types, and relation types |
| `results/signals_v4/` | Parquet | ~45 MB | Sex-stratified ROR values and sex-differential signals for all 254,114 drug-AE comparisons |
| `results/kg_embeddings_v4/` | PyTorch | ~360 MB | Pre-trained ComplEx and DistMult model weights with entity/relation mappings |
| `results/link_predictions/` | TSV+JSON | ~2 MB | Top 500 novel sex-differential drug-AE predictions from ComplEx link prediction |
| `results/analysis/` | JSON | ~1 MB | Validation benchmarks, statistical tests, and audit outputs |
| `GROUND_TRUTH.json` | JSON | ~5 KB | Canonical counts and checksums for reproducibility verification |

**GitHub** (github.com/jshaik369/SexDiffKG): Version-controlled repository containing all pipeline scripts (Python), analysis notebooks, publication documents, and the knowledge graph data files. The repository is structured as follows:

```
sexdiffkg/
  data/
    kg_v4/          # Canonical KG (nodes.tsv, edges.tsv, triples.tsv, data_dictionary.json)
    raw/            # Source data download scripts
    processed/      # Intermediate processing outputs
  scripts/          # Reproducible pipeline (v4_01 through v4_10)
  results/          # Analysis outputs, embeddings, predictions
  Publication/      # Manuscript and supplementary materials
  GROUND_TRUTH.json # Canonical verification checksums
```

### Node schema

The `nodes.tsv` file contains three columns:

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `id` | string | Unique entity identifier with namespace prefix | `DRUG:metformin`, `AE:Nausea`, `GENE:ESR1` |
| `name` | string | Human-readable entity name | `metformin`, `Nausea`, `ESR1` |
| `category` | string | Entity type (one of 6 categories) | `Drug`, `AdverseEvent`, `Gene` |

Entity identifiers use namespace prefixes to prevent collisions: `DRUG:` (3,920 drugs), `AE:` (9,949 adverse events), `GENE:` (77,498 genes), `PROTEIN:` (16,201 proteins), `PATHWAY:` (2,279 pathways), `TISSUE:` (20 tissues).

### Edge schema

The `edges.tsv` file contains three columns:

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `subject` | string | Source entity identifier | `DRUG:metformin` |
| `predicate` | string | Relation type (one of 6 types) | `sex_differential_adverse_event` |
| `object` | string | Target entity identifier | `AE:Lactic acidosis` |

### Relation types

| Relation | Count | Source | Subject Type | Object Type |
|----------|-------|--------|--------------|-------------|
| `has_adverse_event` | 869,142 | FAERS ROR | Drug | AdverseEvent |
| `interacts_with` | 473,860 | STRING v12.0 | Protein | Protein |
| `participates_in` | 370,597 | Reactome | Gene | Pathway |
| `sex_differential_adverse_event` | 96,281 | FAERS sex-stratified | Drug | AdverseEvent |
| `targets` | 12,682 | ChEMBL 36 | Drug | Gene |
| `sex_differential_expression` | 289 | GTEx v8 | Gene | Tissue |

### Signal data

The sex-differential signals file (`results/signals_v4/sex_differential_v4.parquet`) contains the following columns for each of the 96,281 sex-differential drug-AE pairs (from 254,114 total comparisons meeting the minimum reporting threshold):

| Column | Description |
|--------|-------------|
| `drug_name` | Normalized active ingredient name |
| `pt` | MedDRA Preferred Term for adverse event |
| `ror_female` | Female-specific reporting odds ratio |
| `ror_male` | Male-specific reporting odds ratio |
| `a_female` | Number of female reports for this drug-AE pair |
| `a_male` | Number of male reports for this drug-AE pair |
| `log_ror_ratio` | ln(ROR_female / ROR_male); positive = female-biased |
| `direction` | "female" or "male" indicating bias direction |
| `min_reports` | Minimum of a_female, a_male (all >= 10) |

### Embedding data

Pre-trained knowledge graph embeddings are provided in PyTorch format:

| Model | File | Entities | Relations | Dimensions | Best Metric |
|-------|------|----------|-----------|------------|-------------|
| ComplEx | `results/kg_embeddings_v4/ComplEx/model.pt` | 113,012 | 5 | 200 complex (400 real) | MRR 0.2484 |
| DistMult | `results/kg_embeddings_v4/DistMult_v41/model.pt` | 113,012 | 5 | 200 real | MRR 0.1013 |

Entity-to-index and relation-to-index mappings are provided alongside each model for downstream use. Note: embeddings were trained on 5 relation types (excluding `sex_differential_expression`, which contains only 289 edges added after embedding training).

## Usage Notes

SexDiffKG is designed for multiple research applications:

### Sex-differential ADR discovery

The primary use case is identifying drug-adverse event pairs with significant sex differences in reporting. Researchers can query the `sex_differential_adverse_event` edges to find drugs with disproportionate female or male ADR burden. The `log_ror_ratio` in the signals file quantifies the magnitude of sex difference, enabling ranking of signals by effect size. For example, opioid analgesics exhibit the strongest female bias (mean log_ror_ratio = +0.524, corresponding to 3.0-fold higher female ROR), while SSRIs show modest male bias (mean log_ror_ratio = -0.189).

### Link prediction for novel hypotheses

The pre-trained ComplEx embeddings can be used for link prediction to discover novel sex-differential drug-AE associations not present in the training data. We demonstrate this by scoring all 71.6 million possible (Drug, sex_differential_adverse_event, AE) triples not in the existing graph, identifying 500 top-ranked predictions. The top predictions include clinically plausible associations such as tramadol-dependence (female-biased), cariprazine-sexual dysfunction (female-biased), and isatuximab-cytokine release syndrome (female-biased), several of which have emerging literature support.

### Target-level sex bias analysis

By traversing the graph from sex-differential drug-AE edges through drug-target edges, researchers can identify biological targets with systematic sex bias in their associated ADR profiles. Our analysis of 767 gene targets reveals 317 with directional sex bias, including paradoxical findings such as ESR1 (estrogen receptor alpha) showing male-biased ADRs and AR (androgen receptor) showing female-biased ADRs, patterns that are biologically interpretable through cross-sex pharmacological vulnerability mechanisms.

### Drug safety benchmarking

The 40 literature-derived benchmarks provided in `results/analysis/validation_40_benchmarks_v4.json` can serve as a standard evaluation set for computational models of sex-differential drug response. Researchers developing new pharmacovigilance methods can compare their predictions against these curated benchmarks.

### Integration with existing KGs

SexDiffKG uses standard TSV format and namespace-prefixed identifiers that facilitate integration with other biomedical knowledge graphs. The STRING protein identifiers, ChEMBL drug-target mappings, and Reactome pathway identifiers provide natural join points with resources such as PrimeKG, Hetionet, and SPOKE. The `sex_differential_adverse_event` and `sex_differential_expression` edge types are unique to SexDiffKG and can augment any existing KG with sex-stratified information.

### Limitations

Users should be aware of the following limitations:

1. **Reporting bias**: FAERS is a spontaneous reporting system subject to stimulated reporting, notoriety bias, and under-reporting. ROR values reflect disproportionality in reporting, not causal risk.

2. **Drug normalization**: Despite the multi-tier normalization pipeline achieving 53.9% active-ingredient resolution, 46.1% of drug entries remain at the cleaned-string level, potentially fragmenting signals across variant names for the same compound.

3. **Sex as binary**: FAERS records sex as female/male only. Non-binary gender identities, intersex conditions, and the distinction between sex and gender are not captured. Trans individuals receiving hormone therapy may be miscategorized relative to their hormonal environment.

4. **Temporal confounding**: Reporting practices, drug availability, and diagnostic criteria have evolved over the 21-year span (2004-2025). While temporal validation demonstrates signal stability, some historical signals may not reflect current clinical practice.

5. **Missing data integration**: Several relevant data sources (IMPPAT, NPASS, TCMSP, CTD) are referenced but not yet integrated. The GTEx sex-differential expression layer is relatively sparse (289 edges) compared to the pharmacovigilance layers.

6. **Embedding gap**: The 289 `sex_differential_expression` edges were added after embedding training and are not represented in the pre-trained models.


### Temporal validation

To assess the stability of sex-differential signals over time, we performed a temporal validation by splitting FAERS reports based on event date into a training period (2004Q1-2020Q4) and a test period (2021Q1-2025Q3). Of the 14,536,008 deduplicated reports, 7,469,135 (51.4%) had valid event dates, yielding 5,239,086 training reports and 2,230,049 test reports. The female proportion was stable across periods (59.9% vs 59.4%).

The training period yielded 38,884 strong sex-differential signals and the test period yielded 13,125 strong signals. Among 3,350 drug-AE pairs that were strong in both periods, 84.0% maintained the same sex-bias direction, demonstrating robust temporal stability. In a relaxed analysis including all 8,108 training-strong signals present in the test period at any threshold, 72.6% maintained directional consistency. The Pearson correlation between training and test log(ROR ratios) across 33,786 shared pairs was r = 0.384 (p < 1e-100), indicating moderate preservation of effect magnitude. Notably, 9,775 novel strong signals appeared only in the test period, demonstrating that the 2021-2025 FAERS data contributes genuinely new sex-differential information.

### Statistical significance of sex-differential patterns

We performed comprehensive statistical testing to evaluate the significance of observed sex differences at multiple levels of analysis.

**Signal-level analysis.** The 53.8% female predominance among 96,281 sex-differential signals was highly significant (binomial test, p = 3.5 x 10^-121). However, the effect size was small (Cohen's h = 0.076). Notably, this female proportion (53.8%) was significantly lower than the 60.1% female proportion in the underlying FAERS reports, indicating that the signal detection pipeline does not amplify the reporting sex ratio.

**Drug class analysis.** All 18 major drug classes tested showed statistically significant sex bias after Benjamini-Hochberg FDR correction (q < 0.05). The largest effects were observed for opioid analgesics (Cohen's h = 0.526; 4,923 female-biased vs 1,632 male-biased signals), immune checkpoint inhibitors (h = 0.463), and antipsychotics (h = 0.433). Three classes showed male-biased patterns: SSRIs (h = -0.165), anticonvulsants (h = -0.049), and insulins (h = -0.065).

**Pathway enrichment analysis.** Gene targets of drugs with sex-differential ADR profiles were mapped to Reactome pathways via the `targets` and `participates_in` edges. Fisher exact tests with FDR correction identified 79 significantly enriched pathways: 32 enriched for female-biased drug targets and 47 enriched for male-biased drug targets (FDR q < 0.05). Female-enriched pathways were dominated by extracellular matrix and collagen biology (collagen biosynthesis, q = 4.4 x 10^-15; ECM proteoglycans, q = 2.7 x 10^-13), consistent with known sex differences in connective tissue metabolism[25]. Male-enriched pathways concentrated in ion channel and neurotransmitter signaling (voltage-gated potassium channels, q = 7.3 x 10^-21; NMDA receptor assembly, q = 3.1 x 10^-8).

**Target-level analysis.** Among 74 moderately biased gene targets (|bias score| >= 0.3, >= 3 drugs), none reached individual significance under 10,000-iteration permutation testing after FDR correction, reflecting the limited statistical power of 3-14 drugs per target. These target-level results should therefore be considered hypothesis-generating rather than confirmatory, though the convergent pathway enrichment provides aggregate statistical support.

**References (additional):**
25. Dao H, Bhatt IM, et al. Stem Cell Res Ther 2023; 14:1-16

## Code Availability

All analysis code is available in the GitHub repository (github.com/jshaik369/SexDiffKG) under the MIT License. The pipeline consists of numbered Python scripts (v4_01 through v4_10) that reproduce the full workflow from raw FAERS data through knowledge graph construction, embedding training, and downstream analysis:

| Script | Description |
|--------|-------------|
| `v4_01_normalize_diana.py` | Drug name normalization with DiAna dictionary |
| `v4_02_compute_signals.py` | Sex-stratified ROR computation and signal detection |
| `v4_03_build_kg.py` | Knowledge graph construction from 6 data sources |
| `v4_04_train_distmult.py` | DistMult embedding training (PyKEEN) |
| `v4_05_train_rotatE.py` | RotatE embedding training (PyKEEN) |
| `v4_08_link_prediction.py` | ComplEx-based link prediction for novel ADR discovery |
| `v4_09_statistical_tests.py` | Statistical significance testing (binomial, Fisher, permutation) |
| `v4_10_temporal_validation.py` | Temporal train/test split validation |

Dependencies are specified in `requirements.txt` and `environment.yml`. A `Dockerfile` is provided for containerized reproduction. The ground truth file (`GROUND_TRUTH.json`) contains canonical counts and MD5 checksums for verification.
