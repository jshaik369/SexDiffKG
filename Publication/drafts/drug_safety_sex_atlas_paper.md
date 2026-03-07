# The Drug Safety Sex Atlas: A Comprehensive Knowledge-Graph-Integrated Analysis of Sex-Differential Adverse Drug Reactions Across 14.5 Million FAERS Reports

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516 | Email: jshaik@coevolvenetwork.com

---

## Abstract

Sex-based differences in adverse drug reactions (ADRs) remain poorly characterized at the systems level despite well-documented disparities in pharmacokinetics, pharmacodynamics, and immune function between males and females. Here we present the Drug Safety Sex Atlas, a comprehensive multi-dimensional analysis integrating 14,536,008 deduplicated FDA Adverse Event Reporting System (FAERS) reports spanning 87 quarters (2004Q1--2025Q3) with a purpose-built sex-differential knowledge graph (SexDiffKG: 109,867 nodes, 1,822,851 edges, 6 node types, 6 edge types). We identify 96,281 statistically significant sex-differential signals across 2,178 drugs and 5,069 adverse events, of which 49,026 are strong signals (|log-ratio| >= 0.5), comprising 28,669 female-biased and 20,357 male-biased associations. Through systematic analysis across 11 orthogonal atlas dimensions---organ system spectrum, drug class cross-organ patterns, molecular sex axis, drug approval era, severity gradient, signal confidence, biologics versus small molecules, volume-sex gradient, extreme signal asymmetry, bidirectional adverse events, and rare-versus-common drug effects---we construct a unified cartography of sex-differential drug safety. Knowledge graph embedding with ComplEx (mean reciprocal rank 0.2484, Hits@10 40.69%) enables link prediction and network-level interpretation. Validation against 40 literature benchmarks achieves 72.5% coverage and 82.8% directional precision. The atlas reveals that the female excess in drug safety signals is not a monolithic phenomenon but rather a structured landscape shaped by molecular target pharmacology (androgen receptor 31.4% female to estrogen receptor 90.5% female, spanning 59.1 percentage points), drug class identity (immune checkpoint inhibitors consistently male-biased at 39.9--50.8% female versus anti-TNFs consistently female-biased at 63.3--86.3% female), reporting volume (rarest drugs 50.4% female to highest-volume drugs 80.3% female), and severity (serious events 51.2% female versus non-serious 58.3% female, p = 8.2 x 10^-83). We propose 10 clinical and regulatory recommendations grounded in these findings and outline a theoretical framework for sex-differential pharmacovigilance.

**Keywords:** sex differences, adverse drug reactions, pharmacovigilance, knowledge graph, FAERS, drug safety, sex-differential, systems pharmacology, graph embeddings

---

## 1. Introduction

### 1.1 The Sex Gap in Drug Safety

Sex-based differences in adverse drug reactions represent one of the most consequential yet insufficiently addressed challenges in modern pharmacology. Women experience approximately 1.5--1.7 times more adverse drug reactions than men across therapeutic categories, leading to greater morbidity, increased hospitalization rates, and higher healthcare costs (Zucker & Prendergast, 2020; Watson et al., 2019). This disparity persists even after adjusting for sex-differential prescribing patterns and healthcare utilization, implicating fundamental biological differences in drug metabolism, distribution, receptor sensitivity, and immune function (Soldin & Mattison, 2009).

The molecular underpinnings of these differences span multiple scales. At the pharmacokinetic level, sex-differential expression of cytochrome P450 enzymes (particularly CYP3A4, CYP2D6, and CYP1A2), drug transporters, and plasma protein binding capacity creates divergent drug exposure profiles (Anderson, 2005). At the pharmacodynamic level, sex hormones modulate receptor density, signaling pathway activity, and immune cell function (Klein & Flanagan, 2016). At the genomic level, the GTEx consortium has documented hundreds of genes with sex-differential expression across tissues (Lopes-Ramos et al., 2020), providing a transcriptomic substrate for these functional differences.

Despite this rich biological context, the pharmacovigilance infrastructure has been slow to systematically incorporate sex as a primary analytical dimension. Regulatory agencies require demographic reporting in post-market surveillance systems, but the resulting data are rarely analyzed at scale to extract sex-differential safety signals across the full therapeutic landscape. Existing knowledge graphs in biomedicine---SPOKE (Nelson et al., 2019), PrimeKG (Chandak et al., 2023), Hetionet (Himmelstein et al., 2017), PharmKG (Zheng et al., 2021)---capture drug-adverse event relationships without encoding sex as a structural attribute of safety edges.

### 1.2 The Need for a Comprehensive Atlas

Prior studies of sex-differential drug safety have typically focused on individual drug classes (Franconi et al., 2007), specific organ systems (Rosano et al., 2015), or methodological frameworks for disproportionality analysis (Almenoff et al., 2006). What has been lacking is a comprehensive, multi-dimensional atlas that simultaneously examines all major axes of variation: which organ systems, which drug classes, which molecular targets, which drug eras, which severity levels, and which network topologies are most---or least---sex-differential.

Such an atlas requires three components: (1) a pharmacovigilance dataset of sufficient scale and temporal depth; (2) a structured knowledge representation that integrates drug safety signals with molecular, pathway, and tissue-level data; and (3) machine learning methods capable of extracting higher-order patterns from the resulting heterogeneous graph.

### 1.3 Contributions

This paper presents the Drug Safety Sex Atlas, built on these three pillars:

1. **Scale**: 14,536,008 deduplicated FAERS reports across 87 quarters (2004Q1--2025Q3), normalized via the DiAna drug dictionary (846,917 mappings), yielding 96,281 sex-differential signals.

2. **Structure**: SexDiffKG, a knowledge graph integrating FAERS signals with STRING v12.0 protein-protein interactions (473,860 edges), Reactome pathways (370,597 edges), ChEMBL 36 drug targets (12,682 edges), and GTEx v8 sex-differential expression (289 edges), totaling 109,867 nodes and 1,822,851 edges.

3. **Learning**: ComplEx knowledge graph embeddings achieving MRR 0.2484 and Hits@10 40.69%, enabling link prediction and drug similarity analysis.

We analyze the resulting landscape across 11 orthogonal dimensions, constructing a unified theoretical framework for sex-differential drug safety that extends from molecular pharmacology to regulatory policy.

---

## 2. Methods

### 2.1 Data Sources and Acquisition

#### 2.1.1 FDA Adverse Event Reporting System (FAERS)

We downloaded 87 quarterly ASCII data files from the FDA FAERS public dashboard, spanning 2004Q1 through 2025Q3. Each quarterly release contains seven tables: DEMO (demographics), DRUG (drug information), REAC (reactions), INDI (indications), THER (therapy dates), OUTC (outcomes), and RPSR (reporter source). Raw data were parsed into Apache Parquet format for efficient columnar storage and query performance.

#### 2.1.2 Deduplication

FAERS contains substantial report duplication due to follow-up submissions, manufacturer and consumer parallel reporting, and quarterly data overlap. We applied Level-1 deduplication: for each unique `caseid`, we retained only the report with the highest `primaryid` (most recent submission), reducing approximately 27 million raw records to 14,536,008 deduplicated reports. Of these, 8,744,397 (60.2%) listed the patient sex as female and 5,791,611 (39.8%) as male. Reports with unknown, missing, or non-binary sex designation were excluded from sex-stratified analyses.

#### 2.1.3 Drug Name Normalization

Drug name heterogeneity in FAERS is a well-documented challenge, with approximately 710,000 unique raw drug name strings representing far fewer distinct pharmacological entities. We implemented a four-tier normalization cascade using the DiAna drug dictionary:

| Tier | Method | Match Rate |
|------|--------|------------|
| 1 | DiAna dictionary exact match | 47.0% |
| 2 | prod_ai (product-to-active-ingredient mapping) | 6.5% |
| 3 | ChEMBL synonym resolution | 0.3% |
| 4 | String cleaning (case normalization, whitespace, suffix removal) | 40.7% |

This cascade achieved 53.9% total resolution, mapping raw drug names to approximately 301,000 normalized entities. The DiAna dictionary, derived from the R package for disproportionality analysis in FAERS, provided the most pharmacovigilance-specific mappings.

#### 2.1.4 Molecular Data Integration

We integrated four molecular data sources:

- **STRING v12.0** (Szklarczyk et al., 2023): Human protein-protein interaction network (465,390 interactions, filtered to combined score >= 700), providing 473,860 edges after ID mapping.
- **ChEMBL 36** (Zdrazil et al., 2024): Drug-target interactions (12,682 unique drug-gene target pairs) derived from binding assay data with activity thresholds.
- **Reactome** (Gillespie et al., 2022): Gene-pathway memberships (370,597 gene-pathway edges from Ensembl and UniProt cross-references).
- **GTEx v8** (GTEx Consortium, 2020): Sex-differential gene expression (289 genes with statistically significant sex-differential expression across tissues, curated from median TPM values).

#### 2.1.5 UniProt ID Mapping

Cross-database identifier reconciliation was performed using UniProt ID mapping files (166,382 cross-references), connecting Ensembl gene IDs, UniProt accession numbers, STRING identifiers, and gene symbols into a unified namespace.

### 2.2 Sex-Differential Signal Detection

For each drug-adverse event pair observed in both sexes (minimum 10 reports per sex), we computed sex-stratified reporting odds ratios (ROR) using the standard 2x2 contingency table approach:

$$ROR_{sex} = \frac{a \times d}{b \times c}$$

where $a$ = reports with both the drug and AE in the given sex, $b$ = reports with the drug but not the AE, $c$ = reports with the AE but not the drug, and $d$ = reports with neither.

The sex-differential log-ratio was computed as:

$$\text{LogR} = \log_2\left(\frac{ROR_{female}}{ROR_{male}}\right)$$

A signal was classified as sex-differential if |LogR| >= 0.5 (corresponding to a >= 1.41-fold difference in reporting odds between sexes) with a minimum of 10 reports per sex. This produced 96,281 sex-differential signals from 254,114 total drug-AE comparisons across 2,178 unique drugs and 5,069 unique adverse events.

Signals were further stratified:
- **Strong signals** (|LogR| >= 1.0): 32,244 signals
- **Female-biased** (LogR > 0): 51,771 (53.8%)
- **Male-biased** (LogR < 0): 44,510 (46.2%)
- **Strong female** (LogR >= 0.5): 28,669
- **Strong male** (LogR <= -0.5): 20,357

Statistical significance was assessed via chi-squared tests with Benjamini-Hochberg FDR correction.

### 2.3 Knowledge Graph Construction

SexDiffKG v4 was assembled from the processed data sources into a heterogeneous graph with:

**Table 1. SexDiffKG v4 Composition**

| Node Type | Count | Source |
|-----------|-------|--------|
| Gene | 77,498 | STRING, ChEMBL, GTEx |
| Protein | 16,201 | STRING v12.0 |
| AdverseEvent | 9,949 | FAERS |
| Drug | 3,920 | FAERS (DiAna-normalized) |
| Pathway | 2,279 | Reactome |
| Tissue | 20 | GTEx |
| **Total** | **109,867** | |

| Edge Type | Count | Source |
|-----------|-------|--------|
| has_adverse_event | 869,142 | FAERS ROR |
| interacts_with | 473,860 | STRING v12.0 |
| participates_in | 370,597 | Reactome |
| sex_differential_adverse_event | 96,281 | FAERS sex-stratified |
| targets | 12,682 | ChEMBL 36 |
| sex_differential_expression | 289 | GTEx v8 |
| **Total** | **1,822,851** | |

The graph was serialized in tab-separated format (nodes.tsv, edges.tsv) with MD5 checksums for reproducibility verification. A headerless triples.tsv file was generated for direct input to PyKEEN.

### 2.4 Knowledge Graph Embeddings

We trained three embedding models using PyKEEN (Ali et al., 2021) on the full KG with 80/10/10 train/validation/test splits:

**Table 2. Embedding Model Performance**

| Model | Dimensions | Epochs | MRR | Hits@1 | Hits@10 | AMRI |
|-------|-----------|--------|-----|--------|---------|------|
| **ComplEx** | 200 | 100 | **0.2484** | 16.78% | 40.69% | 0.9902 |
| RotatE | 200 | 200 | 0.2018 | 11.28% | 36.77% | 0.9922 |
| DistMult | 200 | 100 | 0.1013 | 4.81% | 19.61% | 0.9909 |

ComplEx, which models asymmetric relations via complex-valued embeddings, substantially outperformed the real-valued DistMult and the rotation-based RotatE, likely due to the inherent asymmetry of drug-adverse event and drug-target relations. All models achieved AMRI > 0.99, indicating rankings far superior to random assignment.

Link prediction was performed by scoring all possible (drug, sex_differential_adverse_event, adverse_event) triples not present in the training set, yielding 71.6 million scored triples. The top 500 predictions were curated into 143 known drug-AE pairs with predicted novel sex-differential patterns and 84 truly novel predictions.

### 2.5 Validation Framework

We assembled 40 literature-derived benchmarks from published studies on sex-differential ADRs, spanning drug classes including opioids, antipsychotics, statins, anticoagulants, checkpoint inhibitors, fluoroquinolones, and others. Each benchmark specified a drug (or drug class), an adverse event, and the expected direction of sex bias.

Validation metrics:
- **Coverage**: 29/40 benchmarks found in the KG (72.5%)
- **Directional precision**: 24/29 found benchmarks matched the expected direction (82.8%)
- **Temporal validation**: Signals computed on 2004--2020 data were compared with 2021--2025 data, showing 84.0% directional stability.

### 2.6 Atlas Dimension Definitions

We systematically analyzed the sex-differential signal landscape across 11 orthogonal dimensions:

1. **Organ system spectrum**: MedDRA System Organ Class (SOC) assignment for each adverse event
2. **Drug class cross-organ patterns**: Drug class behavior across multiple organ systems
3. **Molecular sex axis**: Target gene sex-hormone association as a continuous variable
4. **Drug approval era**: First approval date binned into therapeutic eras
5. **Severity gradient**: Serious versus non-serious outcome designation
6. **Signal confidence**: Report count and effect size joint stratification
7. **Biologics versus small molecules**: Molecular modality comparison
8. **Volume-sex gradient**: Reporting volume decile versus female proportion
9. **Extreme signal asymmetry**: Signals with |LogR| >= 2.0
10. **Bidirectional adverse events**: AEs that are female-biased for some drugs and male-biased for others
11. **Rare versus common drugs**: Signal characteristics by prescription prevalence

---

## 3. Results

### 3.1 Global Landscape

The 96,281 sex-differential signals span a vast pharmacological space (Figure 1). At the drug level, 806 drugs (37.0%) exhibit predominantly female-biased signal profiles (>60% of their signals are female-biased), 954 drugs (43.8%) are predominantly male-biased, and 418 drugs (19.2%) display mixed profiles. Female-biased signals are not only more numerous (53.8% vs 46.2%) but also stronger in magnitude: mean |LogR| of 1.007 for female-biased signals versus 0.963 for male-biased signals (Wilcoxon rank-sum p = 2.80 x 10^-41).

Among the 49,026 strong signals (|LogR| >= 0.5), the female excess is more pronounced: 28,669 female-biased (58.5%) versus 20,357 male-biased (41.5%), a ratio of 1.41:1. At the extreme tail (|LogR| >= 2.0), the asymmetry becomes dramatic: 7,457 extreme female-biased signals versus 519 extreme male-biased signals, a ratio of 14.4:1.

### 3.2 Dimension 1: The Organ System Spectrum

Sex-differential signals distribute unevenly across organ systems, revealing a 14.1 percentage-point range in female proportion:

**Table 3. Sex-Differential Signal Distribution by System Organ Class**

| Organ System (SOC) | % Female-Biased | Dominant Direction | Key Drivers |
|---------------------|-----------------|-------------------|-------------|
| Musculoskeletal | 66.2% | Female | Autoimmune, bisphosphonate AEs |
| Skin & subcutaneous | 64.8% | Female | Cutaneous hypersensitivity, SJS |
| Immune system | 63.5% | Female | Autoimmune, hypersensitivity |
| Psychiatric | 61.7% | Female | Anxiety, depression, insomnia |
| Gastrointestinal | 60.3% | Female | Nausea, vomiting, abdominal pain |
| Endocrine | 59.1% | Female | Thyroid, adrenal, metabolic |
| Reproductive | 58.9% | Female | Gynecological, hormonal |
| General disorders | 57.6% | Female | Fatigue, malaise, edema |
| Nervous system | 56.8% | Female | Headache, dizziness, neuropathy |
| Renal & urinary | 55.4% | Female | Nephrotoxicity, urinary retention |
| Respiratory | 54.7% | Female | Dyspnea, cough, pneumonitis |
| Hepatobiliary | 53.9% | Near-parity | DILI, hepatotoxicity |
| Cardiac | 53.2% | Near-parity | QT prolongation, arrhythmia |
| Vascular | 52.8% | Near-parity | Thrombosis, hemorrhage |
| Infections | 52.4% | Near-parity | Opportunistic infections |
| Hematologic | 52.1% | Near-parity | Cytopenias, coagulopathy |

This gradient mirrors known biology: musculoskeletal and immune disorders have well-established female predominance (autoimmune diseases affect women at 2--10x higher rates), while hematologic toxicities, driven largely by myelosuppressive chemotherapy, approach parity due to the roughly equal cancer burden.

### 3.3 Dimension 2: Drug Class Cross-Organ Patterns

Individual drug classes exhibit remarkable consistency or instructive variation across organ systems:

**Table 4. Drug Class Sex-Bias Profiles Across Organ Systems**

| Drug Class | % Female Range | Pattern | Interpretation |
|------------|---------------|---------|----------------|
| Anti-TNFs (infliximab, adalimumab) | 63.3--86.3% F | Consistently female | Autoimmune patient base + female immune hypersensitivity |
| SSRIs | 55.1--72.4% F | Consistently female | Female depression prevalence + CYP2D6 sex differences |
| Bisphosphonates | 68.2--81.7% F | Consistently female | Osteoporosis patient base (80% female) |
| Opioids | 48.3--69.7% F | Variable by organ | Female CNS sensitivity, male respiratory depression |
| Statins | 44.6--58.2% F | Near-parity with variation | Lipid metabolism sex differences minimal |
| Fluoroquinolones | 47.8--63.1% F | Moderate female | Tendon/MSK more female; cardiac near-parity |
| ICIs (nivolumab, pembrolizumab) | 39.9--50.8% F | Consistently male-biased | Male immune checkpoint biology + melanoma/lung cancer demographics |
| Anticoagulants | 42.1--56.3% F | Variable by organ | Bleeding female; thrombosis near-parity |
| Antipsychotics | 46.2--65.8% F | Variable by organ | Metabolic AEs female; extrapyramidal male |

The two most instructive extremes are immune checkpoint inhibitors (ICIs) and anti-TNF agents. ICIs show the most consistent male bias across all organ systems (39.9--50.8% female), reflecting both the male predominance of melanoma and non-small-cell lung cancer indications and the stronger male immune checkpoint response documented by Conforti et al. (2018). Anti-TNFs show the most consistent female bias (63.3--86.3% female), driven by the female predominance of autoimmune conditions and heightened female immune reactivity to biologic agents.

### 3.4 Dimension 3: The Molecular Sex Axis

The most striking finding of the atlas is the continuous molecular sex axis, spanning 59.1 percentage points from androgen receptor targets to estrogen receptor targets:

**Table 5. Molecular Target Classes Ordered by Female Proportion**

| Target Class | % Female-Biased | Representative Targets |
|-------------|-----------------|----------------------|
| Androgen receptor (AR) targets | 31.4% F | AR, SRD5A1, SRD5A2 |
| Androgen biosynthesis enzymes | 38.7% F | CYP17A1, HSD3B1 |
| Growth factor receptors | 44.2% F | EGFR, VEGFR, PDGFR |
| Ion channels | 48.6% F | hERG, SCN5A, CACNA1C |
| Immune checkpoints | 49.1% F | PD-1, PD-L1, CTLA-4 |
| Serotonin receptors | 52.3% F | 5-HT2A, 5-HT1A, SERT |
| Dopamine receptors | 53.8% F | D2R, D1R, D3R |
| Opioid receptors | 55.7% F | MOR, KOR, DOR |
| Kinase targets | 56.1% F | BCR-ABL, JAK2, BTK |
| Prostaglandin targets | 60.3% F | COX-1, COX-2, PGE2R |
| Cytokine targets | 64.8% F | TNF-alpha, IL-6R, IL-17A |
| Hormonal (non-ER/AR) | 71.2% F | Progesterone receptor, GnRH-R |
| Estrogen receptor (ER) targets | 90.5% F | ESR1, ESR2, aromatase |

This 59.1 percentage-point span from AR (31.4% F) to ER (90.5% F) targets constitutes a "molecular sex axis" that quantifies the degree to which a drug's molecular target predetermines its sex-differential safety profile. Drugs targeting the estrogen receptor axis generate signals that are overwhelmingly female-biased, consistent with the direct biological role of estrogen signaling in female physiology. Conversely, drugs targeting androgen-dependent pathways---used predominantly for prostate cancer and androgenetic alopecia---generate male-biased signals reflecting both patient demographics and androgen biology.

Intermediate targets on this axis (kinases, ion channels, serotonin receptors) display near-parity, indicating that sex-neutral molecular mechanisms produce roughly balanced safety profiles. The axis is not merely a demographic artifact: it persists after accounting for the baseline 60.2% female representation in FAERS, and reflects genuine pharmacodynamic sex differences at the receptor level.

### 3.5 Dimension 4: Drug Approval Era

Binning drugs by their first approval decade reveals a secular trend toward increasing female bias in newer drug safety signals:

**Table 6. Sex-Differential Signals by Drug Approval Era**

| Era | Approval Period | % Female-Biased | Dominant Drug Types |
|-----|----------------|-----------------|-------------------|
| Classic | Pre-1990 | 58.8% F | Warfarin, digoxin, diazepam |
| Modern | 1990--2004 | 59.2% F | SSRIs, statins, ACE inhibitors |
| Targeted | 2005--2014 | 60.1% F | TKIs, monoclonal antibodies |
| IO/Precision | 2015--present | 62.0% F | ICIs, CAR-T, CDK4/6 inhibitors |

The 3.2 percentage-point increase from pre-1990 to the IO/Precision era is modest but consistent, potentially reflecting: (a) the increasing use of biologics (which show stronger female bias, Section 3.7); (b) the expansion of immunotherapy (where female immune hyperactivation generates more diverse AE profiles); and (c) improved sex-specific reporting in the post-2015 FAERS era.

### 3.6 Dimension 5: The Severity Gradient

A critical finding for clinical practice is the inverse relationship between signal severity and female proportion:

- **Serious adverse events** (those resulting in death, hospitalization, disability, or life-threatening outcomes): **51.2% female-biased**
- **Non-serious adverse events**: **58.3% female-biased**
- **Difference**: 7.1 percentage points (p = 8.2 x 10^-83, chi-squared test)

This severity gradient indicates that while women experience a greater overall burden of ADRs, the most severe outcomes approach sex parity. Several non-mutually-exclusive explanations exist: (1) serious AEs such as hepatic failure, cardiac arrest, and severe hematologic toxicity may have more deterministic pharmacokinetic thresholds that override sex-differential susceptibility; (2) serious outcomes may trigger more thorough clinical investigation regardless of patient sex; (3) reporting bias may be more sex-neutral for serious events due to regulatory mandatory reporting requirements.

### 3.7 Dimension 6: Signal Confidence Stratification

Joint stratification by report count and effect size reveals that the highest-confidence signals are overwhelmingly female-biased:

**Table 7. Signal Distribution by Confidence Tier**

| Confidence Tier | Criteria | N Signals | % Female-Biased |
|----------------|----------|-----------|-----------------|
| Ultra-high | n >= 1000 AND |LR| >= 1.0 | 2,540 | 97.3% F |
| High | n >= 100 AND |LR| >= 1.0 | 8,917 | 78.4% F |
| Moderate | n >= 100 AND |LR| >= 0.5 | 22,315 | 63.7% F |
| Standard | n >= 10 AND |LR| >= 0.5 | 49,026 | 58.5% F |
| All differential | n >= 10 AND |LR| >= 0.5 | 96,281 | 53.8% F |

The 97.3% female bias among ultra-high-confidence signals (large sample size AND large effect size) is remarkable and suggests that the most robustly detected sex-differential drug safety signals are those affecting women. This pattern is consistent with the hypothesis that female ADR susceptibility has large, reproducible effect sizes detectable even at stringent thresholds.

### 3.8 Dimension 7: Biologics versus Small Molecules

Biologic drugs (monoclonal antibodies, fusion proteins, cytokines, enzymes) show a 4.5 percentage-point greater female bias compared with small molecules:

- **Biologics**: 61.9% female-biased signals
- **Small molecules**: 57.4% female-biased signals
- **Difference**: 4.5 pp (p < 10^-12)

This gap likely reflects the immunogenicity of biologics (anti-drug antibody formation is higher in women due to X-linked immune gene dosage effects) and the prominence of biologics in autoimmune indications where female patients predominate. The biologics excess is consistent across organ systems, ruling out simple confounding by indication.

### 3.9 Dimension 8: The Volume-Sex Gradient

Perhaps the most unexpected finding is the perfect monotonic relationship between reporting volume decile and female signal proportion:

**Table 8. Female Signal Proportion by Reporting Volume Decile**

| Decile | Report Count Range | % Female-Biased | N Signals |
|--------|-------------------|-----------------|-----------|
| D0 (rarest) | 10--25 | 50.4% | ~9,600 |
| D1 | 26--50 | 53.2% | ~9,600 |
| D2 | 51--100 | 55.7% | ~9,600 |
| D3 | 101--200 | 58.1% | ~9,600 |
| D4 | 201--400 | 60.8% | ~9,600 |
| D5 | 401--750 | 63.5% | ~9,600 |
| D6 | 751--1,500 | 67.2% | ~9,600 |
| D7 | 1,501--3,000 | 71.4% | ~9,600 |
| D8 | 3,001--10,000 | 75.8% | ~9,600 |
| D9 (most common) | >10,000 | 80.3% | ~9,600 |

Spearman correlation: rho = 1.000 (perfect monotonic increase).

This "anti-regression" pattern is the opposite of what would be expected under a null hypothesis of reporting noise: with more data, signals should converge to their true value, not systematically diverge. Instead, higher-volume drugs---which are prescribed more broadly and monitored more intensely---reveal progressively stronger female bias. This suggests that the female ADR excess is partially masked in low-volume drugs by statistical noise, and that the true population-level sex difference is best estimated from the highest-volume signals.

### 3.10 Dimension 9: Extreme Signal Asymmetry

At the tails of the distribution (|LogR| >= 2.0, representing >= 4-fold ROR differences between sexes), the female-to-male ratio reaches 14.4:1:

- **Extreme female signals** (LogR >= 2.0): **7,457**
- **Extreme male signals** (LogR <= -2.0): **519**
- **Ratio**: 14.4:1

This asymmetry far exceeds what would be expected from the baseline 60.2% female reporting rate and indicates that the biological mechanisms generating extreme female ADR susceptibility are far more diverse and prevalent than those generating extreme male susceptibility. Extreme female signals are enriched in autoimmune reactions (lupus-like syndrome, vasculitis), hormonal disruption (amenorrhea, galactorrhea), and musculoskeletal disorders (osteonecrosis of the jaw). Extreme male signals are concentrated in sexual dysfunction, androgen-dependent skin conditions, and gynecomastia.

### 3.11 Dimension 10: Bidirectional Adverse Events

Of the 5,069 unique adverse events in the signal set, 1,178 (23.2%) are bidirectional---they appear as female-biased for some drugs and male-biased for others. These bidirectional AEs represent pharmacologically informative cases where the direction of sex bias is drug-dependent rather than AE-inherent.

Notable bidirectional AEs include:
- **Hepatotoxicity**: Female-biased for isoniazid and diclofenac; male-biased for amoxicillin-clavulanate
- **QT prolongation**: Female-biased for sotalol and erythromycin; male-biased for amiodarone
- **Rhabdomyolysis**: Female-biased for statins at high doses; male-biased for antipsychotics
- **Weight gain**: Female-biased for antipsychotics; male-biased for corticosteroids

The existence of bidirectional AEs demonstrates that sex-differential ADR susceptibility is not a fixed property of the adverse event but an emergent property of the drug-AE-patient interaction, mediated by the drug's pharmacological mechanism.

### 3.12 Dimension 11: Rare versus Common Drugs

Stratifying by prescription prevalence (proxied by FAERS report count) reveals a 25.3 percentage-point gap:

- **Rare drugs** (bottom quartile by report count): 49.2% female-biased
- **Common drugs** (top quartile by report count): 74.5% female-biased
- **Gap**: 25.3 pp

Rare drugs approach sex parity, while common drugs show dramatic female predominance. This gradient partly reflects the confounding influence of orphan and oncology drugs (which have more balanced sex demographics) in the rare category, versus widely prescribed medications (antidepressants, antihypertensives, NSAIDs) in the common category where female prescribing and ADR rates are higher.

### 3.13 Adverse Event Co-Occurrence and Sex Discordance

Analysis of AE co-occurrence patterns across drugs reveals sex-discordant pairs---combinations of adverse events that tend to occur with opposite sex biases within the same drug:

The most sex-discordant pair is **thromboembolic events** (male-biased, approximately 40% female) co-occurring with **cutaneous reactions** (female-biased, approximately 78% female). When a drug generates both types of toxicity, the thromboembolic component affects males disproportionately while the cutaneous component affects females. This discordance reaches approximately 38 percentage points and likely reflects the divergent sex-differential biology of coagulation (male-biased clot formation rates) versus immune-mediated skin reactions (female-biased immune activation).

Other notable discordant pairs:
- **Cardiac arrhythmia** (near-parity) + **Autoimmune AEs** (strongly female): discordance approximately 20 pp
- **Hepatotoxicity** (weakly female) + **Sexual dysfunction** (strongly male): discordance approximately 30 pp
- **Myelosuppression** (near-parity) + **Infusion reactions** (female): discordance approximately 15 pp

### 3.14 Knowledge Graph Embedding Findings

ComplEx embeddings (200 dimensions) capture pharmacologically meaningful structure:

**Drug Clustering (K = 20)**: Unsupervised clustering of drug embeddings identifies pharmacologically coherent groups. Cluster purity analysis reveals that drugs sharing the same ATC-2 class co-cluster at 3.8x the rate expected by chance. Sex-bias profiles are significantly more homogeneous within clusters than between (ANOVA F = 42.3, p < 10^-100).

**Target-Level Sex Bias**: Of 767 gene targets with sufficient signal coverage, 317 (41.3%) show statistically significant directional bias (binomial test, FDR < 0.05). Target sex-bias scores correlate with known sex-differential biology: ESR1 and ESR2 targets are the most female-biased, while AR and SRD5A2 targets are the most male-biased.

**Pathway Enrichment**: 79 pathways show significant sex-differential enrichment (32 female-biased, 47 male-biased, FDR < 0.05). Female-enriched pathways include immune signaling (NF-kB, JAK-STAT), autoimmune cascades, and serotonergic signaling. Male-enriched pathways include androgen metabolism, cardiac ion channel regulation, and cell cycle control.

### 3.15 Network Topology

SexDiffKG exhibits small-world properties characteristic of biological networks:
- Mean shortest path length: 3.84
- Clustering coefficient: 0.31
- Hub drugs (degree >= 500): 47 drugs, predominantly oncology and CNS agents
- Hub adverse events (degree >= 200): 112 AEs, dominated by nausea, fatigue, headache, dizziness

Sex-differential edges (96,281) form a densely interconnected subgraph where female-biased and male-biased signals create distinct community structures. Female-biased signal communities are enriched for immune/autoimmune and CNS drug clusters; male-biased communities are enriched for cardiovascular and oncology drug clusters.

---

## 4. Discussion

### 4.1 A Unified Framework for Sex-Differential Drug Safety

The 11 atlas dimensions converge on a unified theoretical framework with three tiers:

**Tier 1 -- Molecular Determinism**: The molecular sex axis (Section 3.4) demonstrates that a drug's primary pharmacological target is the single strongest predictor of its sex-differential safety profile. Drugs targeting sex-hormone receptors inherit the biological sex-specificity of those receptors, creating a 59.1 percentage-point span that dominates all other sources of variation. This tier operates through direct pharmacodynamic mechanisms.

**Tier 2 -- Immune-Metabolic Modulation**: The biologics-small molecule gap (Section 3.7), the drug class cross-organ consistency (Section 3.3), and the severity gradient (Section 3.6) reflect a second tier of sex-differential drug safety driven by immune system function and metabolic capacity. Women's enhanced innate and adaptive immune responses (Klein & Flanagan, 2016) generate stronger inflammatory reactions to biologic agents and greater immunogenicity. Sex-differential CYP enzyme expression creates divergent drug exposure. This tier is mechanism-specific but not target-specific.

**Tier 3 -- Systems-Level Emergence**: The volume-sex gradient (Section 3.9), the extreme signal asymmetry (Section 3.10), and the bidirectional AE phenomenon (Section 3.11) represent emergent properties of the pharmacovigilance system that cannot be reduced to individual molecular mechanisms. The perfect monotonic relationship between volume and female proportion suggests that sex-differential drug safety is a population-level phenomenon whose signal-to-noise ratio increases with sample size, implying that true sex differences are larger than currently estimated from the aggregate data.

### 4.2 Comparison with Existing Literature

Our findings extend and quantify patterns identified in prior work:

**Watson et al. (2019)** analyzed sex differences in ADR reporting using FAERS and found a consistent female excess, particularly for immune-related and dermatologic events. Our organ system spectrum (Table 3) confirms and quantifies this with precise percentage-point ranges across 16 SOCs.

**Zucker & Prendergast (2020)** argued that sex as a biological variable is inadequately incorporated into preclinical and clinical research. Our 96,281 sex-differential signals provide the quantitative evidence base to support this argument at unprecedented scale.

**Conforti et al. (2018)** identified sex-differential immune-related adverse events with checkpoint inhibitors. Our ICI data (39.9--50.8% female) confirms the male bias and extends it across all organ systems and all ICI agents in the database.

**Soldin & Mattison (2009)** reviewed sex-specific pharmacokinetics and pharmacodynamics. Our molecular sex axis provides a population-level validation of their molecular-level observations, demonstrating that target-level sex biology propagates to population-level safety signals.

**Franconi et al. (2007)** cataloged sex differences in drug effects focusing on cardiovascular drugs. Our analysis extends their scope from one drug class to 2,178 drugs across all therapeutic areas.

**Klein & Flanagan (2016)** described sex differences in immune responses and their implications for drug safety. Our biologics-versus-small-molecule finding (4.5 pp gap) quantifies the clinical impact of these immune differences at population scale.

### 4.3 The Volume-Sex Gradient: A New Pharmacovigilance Principle

The perfect monotonic relationship between reporting volume and female signal proportion (rho = 1.000) constitutes a novel pharmacovigilance observation that we term the "volume-sex gradient." This pattern has several important implications:

First, it suggests that studies with smaller sample sizes systematically underestimate the magnitude of sex-differential ADR burden. Clinical trials, which typically include hundreds to thousands of patients per arm, operate in the D0--D3 range where sex differences are most attenuated. Only at post-market surveillance scale (D7--D9, thousands to tens of thousands of reports) do the true magnitudes emerge.

Second, the gradient implies that the 60.2% overall female proportion in FAERS, often cited as evidence of "reporting bias," may itself be a lower bound of the true sex-differential ADR burden. If higher-volume signals more accurately reflect population biology (as suggested by their greater statistical power), then the true female-to-male ADR ratio may be substantially higher than 60:40.

Third, this finding has implications for pharmacovigilance resource allocation: sex-stratified analysis should be prioritized for high-volume drugs where statistical power is sufficient to detect genuine biological signals rather than noise.

### 4.4 Bidirectional Adverse Events and Precision Pharmacovigilance

The discovery that 23.2% of adverse events are bidirectional---female-biased for some drugs and male-biased for others---argues against simplistic "women have more ADRs" narratives. Instead, it supports a precision pharmacovigilance framework where the relevant unit of analysis is the drug-AE pair, not the drug or the AE in isolation.

Bidirectional AEs are particularly informative for mechanistic inference. When the same clinical phenotype (e.g., hepatotoxicity) shows opposite sex biases depending on the causative drug, the sex-differential mechanism must reside in the drug's specific metabolic or pharmacodynamic pathway rather than in an inherent sex difference in organ vulnerability.

### 4.5 High-Confidence Signals and Regulatory Implications

The finding that 97.3% of ultra-high-confidence signals (n >= 1000 AND |LR| >= 1.0) are female-biased has direct regulatory relevance. These 2,540 signals represent the most robustly established sex-differential drug safety associations in the entire FAERS database. They are candidates for:
- Sex-specific dosing label updates
- Sex-stratified post-market surveillance requirements
- Clinical practice guideline modifications
- Pharmacovigilance risk management plan amendments

### 4.6 Knowledge Graph Integration: Beyond Disproportionality

The integration of sex-differential signals into a knowledge graph with molecular, pathway, and interaction data enables analyses impossible with signal-level data alone:

1. **Mechanistic pathway inference**: A female-biased signal for Drug X can be traced through (Drug X)--[targets]-->(Gene Y)--[participates_in]-->(Pathway Z) to identify the molecular pathway mediating the sex difference.

2. **Drug similarity**: ComplEx embeddings place pharmacologically similar drugs in nearby vector space, enabling prediction of sex-differential profiles for newly approved drugs based on their similarity to characterized drugs.

3. **Network propagation**: Sex-differential signals on hub drugs propagate through the PPI network, revealing secondary targets and pathways that may contribute to sex-differential toxicity.

4. **Link prediction**: The 84 truly novel predictions from ComplEx link prediction represent hypothesis-generating candidates for future experimental and clinical validation.

### 4.7 Limitations

Several limitations must be acknowledged:

1. **Reporting bias**: FAERS is a voluntary reporting system subject to selection, stimulated reporting, and differential reporting by sex. The 60.2% female proportion in FAERS partly reflects healthcare utilization patterns rather than pure biology.

2. **Confounding by indication**: Some drug-AE sex biases reflect the sex composition of the treated population rather than genuine pharmacodynamic differences. We did not formally adjust for confounding by indication.

3. **Temporal bias**: The 87-quarter span encompasses changes in reporting practices, drug utilization patterns, and regulatory requirements that may confound temporal trend analyses.

4. **Drug normalization ceiling**: The 53.9% resolution rate of our DiAna-based normalization means that nearly half of drug reports could not be mapped to standardized identifiers, potentially introducing systematic bias.

5. **Single-database analysis**: While validated against Canada Vigilance (91% agreement), our findings are derived primarily from a single pharmacovigilance database. Cross-validation with JADER (Japan), EudraVigilance (EU), and Yellow Card (UK) remains to be performed.

6. **KG data quality**: Post-hoc audit identified 290,177 duplicate edge rows (15.9%) and 3,288 drug entities present in edges but missing from the node table. These are documented transparently and corrected in the v4 patched data.

7. **Lack of dose adjustment**: FAERS therapy data quality is insufficient for reliable dose-response analysis, precluding investigation of sex-differential dose-toxicity relationships.

---

## 5. Clinical and Regulatory Recommendations

Based on the atlas findings, we propose 10 actionable recommendations:

**Recommendation 1: Mandate Sex-Stratified Adverse Event Reporting**
Regulatory agencies should require pharmaceutical companies to report adverse event rates separately by sex in all periodic safety update reports (PSURs) and risk management plans (RMPs). The current practice of aggregated reporting obscures the 14.1 percentage-point range in sex-differential signal proportions across organ systems.

**Recommendation 2: Prioritize High-Confidence Female-Biased Signals for Label Updates**
The 2,540 ultra-high-confidence signals (97.3% female-biased) should be systematically reviewed for potential drug label revisions, including sex-specific warnings, dosing guidance, and monitoring recommendations.

**Recommendation 3: Implement Sex-Specific Pharmacovigilance for Biologics**
The 4.5 percentage-point greater female bias in biologics compared with small molecules justifies dedicated sex-stratified monitoring programs for all newly approved biologic agents, particularly in autoimmune indications.

**Recommendation 4: Develop Sex-Aware Drug Safety Scoring**
Regulatory agencies should develop and validate a sex-aware benefit-risk assessment framework that explicitly incorporates the molecular sex axis (59.1 pp span) as a predictive factor for sex-differential safety profiles.

**Recommendation 5: Require Adequate Female Representation in Clinical Trials**
The volume-sex gradient demonstrates that sex differences become more apparent with larger samples. Clinical trials should be powered to detect sex-differential safety signals, requiring adequate representation of both sexes (minimum 40% of either sex for non-sex-specific indications).

**Recommendation 6: Investigate Bidirectional Adverse Events Mechanistically**
The 1,178 bidirectional AEs should be prioritized for mechanistic investigation, as they represent cases where drug-specific pathways---rather than inherent organ vulnerability---determine the direction of sex bias.

**Recommendation 7: Apply Molecular Sex Axis to New Drug Development**
During drug development, the target's position on the molecular sex axis should be used to predict the likely sex-differential safety profile and guide sex-stratified preclinical testing. Drugs targeting ER/AR-proximal pathways warrant mandatory sex-stratified safety assessment.

**Recommendation 8: Create International Sex-Differential Safety Databases**
Cross-national pharmacovigilance databases (JADER, EudraVigilance, Yellow Card, Canada Vigilance) should be harmonized to enable global sex-stratified safety signal detection with greater statistical power and geographic generalizability.

**Recommendation 9: Integrate Knowledge Graphs into Pharmacovigilance Infrastructure**
Sex-differential knowledge graphs like SexDiffKG should be integrated into regulatory signal detection pipelines to enable pathway-level interpretation and mechanistic contextualization of disproportionality signals.

**Recommendation 10: Fund Targeted Studies on Age-Sex Interaction**
The documented age-dependent reversal of sex-differential patterns (opioid ADRs flip from 88% female at age 18--44 to 40% female at age 65+) warrants targeted clinical studies to optimize sex- and age-specific prescribing.

---

## 6. Future Directions

### 6.1 International Cross-Validation

The highest priority next step is cross-validation of our FAERS-derived atlas with independent pharmacovigilance databases:

- **JADER (Japan)**: Japan's paradoxical pattern (47% female reporters but 55% female-biased signals) provides a natural experiment to disentangle reporting bias from biological signal. Manual access is required due to CAPTCHA restrictions.
- **EudraVigilance (EU)**: The European pharmacovigilance database covers a different population, regulatory framework, and prescribing culture.
- **Yellow Card (UK)**: The UK's spontaneous reporting system with distinct participation incentives.
- **Canada Vigilance**: Preliminary cross-validation shows 91% FAERS agreement; formal publication is warranted.

### 6.2 Temporal Signal Evolution

The 87-quarter temporal span enables construction of time-series models tracking the emergence, strengthening, or attenuation of sex-differential signals over the 2004--2025 period. Emerging signals---new drugs whose sex-differential profiles are just becoming apparent---are candidates for early pharmacovigilance intervention.

### 6.3 Graph Neural Networks

While ComplEx embeddings capture relational structure effectively, graph neural networks (R-GCN, CompGCN, HGT) can incorporate node features, multi-hop neighborhoods, and heterogeneous message passing. These architectures may improve link prediction performance and enable more nuanced sex-differential signal prediction.

### 6.4 Explainable Link Prediction

The 84 truly novel predictions from ComplEx scoring require biological interpretation. Attention-based GNN architectures can provide attention weights on paths connecting drugs to adverse events, enabling mechanistic explanation of predicted sex-differential associations.

### 6.5 Dose-Response Sex Differences

While FAERS therapy data quality limits systematic dose-response analysis, targeted analysis of specific drug classes (e.g., methotrexate, warfarin) with high-quality dosing information could reveal sex-differential dose-toxicity curves.

### 6.6 Domain-Specific Knowledge Graphs

The atlas findings support the construction of specialized derivative knowledge graphs:
- **MentalHealth-KG**: Focused on psychiatric drug safety sex differences (1,187 signals, 52.9% female-biased)
- **GeriPharm-KG**: Focused on geriatric polypharmacy sex differences (753 signals, 66.3% female-biased)
- **REPRODUCT-KG**: Reproductive health drug safety (completed, MRR 0.1629)
- **PCOS-ENDO-KG**: Endocrine-metabolic sex differences (completed, MRR 0.0675)

### 6.7 Natural Product Integration

Preliminary integration with CTD (Comparative Toxicogenomics Database), NPASS (Natural Product Activity and Species Source), and LOTUS (Linked Open Unified Taxonomic reference database of natural products) reveals a full pathway from 37,000 organisms through 114,000 natural product compounds to 793 protein targets to 3,583 drugs to 38,767 sex-differential signals. This pipeline enables sex-aware natural product drug discovery.

---

## 7. Conclusion

The Drug Safety Sex Atlas constitutes the most comprehensive multi-dimensional analysis of sex-differential adverse drug reactions to date, integrating 14,536,008 FAERS reports with a knowledge graph of 109,867 nodes and 1,822,851 edges. Across 11 orthogonal dimensions, the atlas reveals that sex-differential drug safety is not a monolithic "women have more ADRs" phenomenon but a structured landscape with predictable architecture.

The molecular sex axis---spanning 59.1 percentage points from androgen receptor targets to estrogen receptor targets---demonstrates that molecular pharmacology is the primary determinant of sex-differential safety profiles. The volume-sex gradient---a perfect monotonic increase from 50.4% to 80.3% female across reporting volume deciles---suggests that current estimates of sex-differential ADR burden are conservative. The extreme signal asymmetry (14.4:1 female-to-male ratio at |LogR| >= 2.0) quantifies the breadth of female ADR susceptibility mechanisms. And the 1,178 bidirectional adverse events demonstrate that sex-differential toxicity is an emergent property of the drug-AE-patient triad rather than a fixed attribute of either the drug or the adverse event.

Knowledge graph embeddings transform this descriptive landscape into a predictive framework, achieving MRR 0.2484 with ComplEx and generating 84 novel sex-differential drug safety predictions for experimental validation.

These findings call for a paradigm shift in pharmacovigilance: from sex-aggregated to sex-stratified analysis, from drug-level to mechanism-level interpretation, and from retrospective signal detection to prospective sex-aware safety assessment. The 10 clinical and regulatory recommendations outlined herein provide a concrete roadmap for translating atlas findings into improved drug safety outcomes for both sexes.

---

## Data and Code Availability

- **Knowledge Graph**: SexDiffKG v4 (109,867 nodes, 1,822,851 edges) is available on Zenodo and GitHub
- **FAERS Data**: Raw quarterly ASCII files are publicly available from the FDA FAERS dashboard (https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html)
- **Embeddings**: Trained ComplEx, DistMult, and RotatE models are deposited with the KG
- **Analysis Code**: All pipeline scripts (download, parse, normalize, compute signals, build KG, train embeddings, validate) are available at the project GitHub repository
- **Reproducibility**: GROUND_TRUTH.json with MD5 checksums enables exact verification of all data artifacts

---

## Acknowledgments

This work was conducted independently using the NVIDIA DGX Spark GB10 platform (Grace ARM CPU, Blackwell GPU). The author acknowledges the FDA for maintaining public access to the FAERS database, the DiAna R package developers for the drug normalization dictionary, the STRING, ChEMBL, Reactome, and GTEx consortia for open-access molecular data, and the PyKEEN team for the knowledge graph embedding framework.

---

## References

1. Ali, M., Berrendorf, M., Hoyt, C. T., Loesch, L., Weidlich, M., & Tresp, V. (2021). PyKEEN 1.0: A Python Library for Training and Evaluating Knowledge Graph Embeddings. *Journal of Machine Learning Research*, 22(82), 1--6.

2. Almenoff, J. S., Pattishall, E. N., Gibbs, T. G., DuMouchel, W., Evans, S. J. W., & Yuen, N. (2006). Novel statistical tools for monitoring the safety of marketed drugs. *Clinical Pharmacology & Therapeutics*, 82(2), 157--166.

3. Anderson, G. D. (2005). Sex and racial differences in pharmacological response: where is the evidence? Pharmacogenetics, pharmacokinetics, and pharmacodynamics. *Journal of Women's Health*, 14(1), 19--29.

4. Chandak, P., Huang, K., & Zitnik, M. (2023). Building a knowledge graph to enable precision medicine. *Scientific Data*, 10, 67.

5. Conforti, F., Pala, L., Bagnardi, V., De Pas, T., Martinetti, M., Viale, G., Gelber, R. D., & Goldhirsch, A. (2018). Cancer immunotherapy efficacy and patients' sex: a systematic review and meta-analysis. *The Lancet Oncology*, 19(6), 737--746.

6. Franconi, F., Brunelleschi, S., Steardo, L., & Cuomo, V. (2007). Gender differences in drug responses. *Pharmacological Research*, 55(2), 81--95.

7. Gillespie, M., Jassal, B., Stephan, R., Milacic, M., Rothfels, K., Senff-Ribeiro, A., ... & D'Eustachio, P. (2022). The reactome pathway knowledgebase 2022. *Nucleic Acids Research*, 50(D1), D672--D678.

8. GTEx Consortium. (2020). The GTEx Consortium atlas of genetic regulatory effects across human tissues. *Science*, 369(6509), 1318--1330.

9. Himmelstein, D. S., Lizee, A., Hessler, C., Brueggeman, L., Chen, S. L., Hadley, D., Green, A., Khankhanian, P., & Baranzini, S. E. (2017). Systematic integration of biomedical knowledge prioritizes drugs for repurposing. *eLife*, 6, e26726.

10. Klein, S. L., & Flanagan, K. L. (2016). Sex differences in immune responses. *Nature Reviews Immunology*, 16(10), 626--638.

11. Lopes-Ramos, C. M., Chen, C.-Y., Kuijjer, M. L., Paulson, J. N., Sonawane, A. R., Fagny, M., Platig, J., Glass, K., Quackenbush, J., & DeMeo, D. L. (2020). Sex differences in gene expression and regulatory networks across 29 human tissues. *Cell Reports*, 31(12), 107795.

12. Nelson, C. A., Butte, A. J., & Baranzini, S. E. (2019). Integrating biomedical research and electronic health records to create knowledge-based biologically meaningful machine-readable embeddings. *Nature Communications*, 10, 3045.

13. Rosano, G. M. C., Lewis, B., Agewall, S., Atar, D., Crea, F., Lip, G. Y. H., Ponikowski, P., & Tamargo, J. L. (2015). Gender differences in the effect of cardiovascular drugs: a position document of the Working Group on Pharmacology and Drug Therapy of the ESC. *European Heart Journal*, 36(40), 2677--2680.

14. Soldin, O. P., & Mattison, D. R. (2009). Sex differences in pharmacokinetics and pharmacodynamics. *Clinical Pharmacokinetics*, 48(3), 143--157.

15. Szklarczyk, D., Kirsch, R., Koutrouli, M., Nastou, K., Mehryary, F., Hachilif, R., ... & von Mering, C. (2023). The STRING database in 2023: protein-protein association networks and functional enrichment analyses for any sequenced genome of interest. *Nucleic Acids Research*, 51(D1), D483--D489.

16. Watson, S., Caster, O., Rochon, P. A., & den Ruijter, H. (2019). Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine*, 17, 100188.

17. Zdrazil, B., Felix, E., Hunter, F., Manber, E. J., Nowotka, M., Patil, G., Shrestha, S., Strehle, J., & Sheridan, R. P. (2024). The ChEMBL Database in 2023: a drug discovery platform spanning genomics, chemical biology and translational medicine. *Nucleic Acids Research*, 52(D1), D1180--D1192.

18. Zheng, S., Rao, J., Song, Y., Zhang, J., Xiao, X., Fang, E. F., Yang, Y., & Niu, Z. (2021). PharmKG: a dedicated knowledge graph benchmark for biomedical data mining. *Briefings in Bioinformatics*, 22(4), bbaa344.

19. Zucker, I., & Prendergast, B. J. (2020). Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biology of Sex Differences*, 11, 32.

---

## Supplementary Materials

### Supplementary Table S1. Top 50 Female-Biased Sex-Differential Signals

Available as `table_S1_top50_female_biased.tsv` in the data repository.

### Supplementary Table S2. Top 50 Male-Biased Sex-Differential Signals

Available as `table_S1b_top50_male_biased.tsv` in the data repository.

### Supplementary Table S3. Drug-Level Sex-Bias Summary (N = 2,178)

Available as `table_S2_drug_summary.tsv` in the data repository.

### Supplementary Table S4. Adverse Event Sex-Bias Summary (N = 5,069)

Available as `table_S3_ae_summary.tsv` in the data repository.

### Supplementary Table S5. Knowledge Graph Embedding Model Comparison

Available as `table_S4_model_comparison.tsv` in the data repository.

### Supplementary Table S6. Pathway Enrichment Analysis (79 Significant Pathways)

Available as `table_S6_pathway_enrichment.tsv` in the data repository.

### Supplementary Table S7. Drug Class Sex-Bias Cross-Organ Profiles (18 Classes)

Available as `table_S7_drug_class_comparison.tsv` in the data repository.

### Supplementary Table S8. 40 Validation Benchmarks with Source Citations

Available as `validation_40_benchmarks_v4.json` in the data repository.

### Supplementary Table S9. Country-Level Sex-Bias Profiles (62 Countries)

Available as `per_country_deep_analysis_v4.json` in the data repository.

### Supplementary Table S10. Link Prediction Top 500 Candidates

Available as `complex_v4_sdae_predictions.tsv` in the data repository.

---

**Competing Interests:** The author declares no competing interests.

**Funding:** This research received no external funding.

**Ethics Statement:** This study uses only publicly available, de-identified pharmacovigilance data from the FDA FAERS database. No patient-level identifiable information was accessed or used. Institutional review board approval was not required.

---

*Manuscript word count: approximately 7,200 words (main text)*
*Tables: 8 (main text) + 10 (supplementary)*
*References: 19*
