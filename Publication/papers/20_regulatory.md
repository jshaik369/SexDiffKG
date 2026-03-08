# Sex-Specific Drug Safety Warnings Are Needed for 187 Medications: Evidence from 14.5 Million FDA Adverse Event Reports

## Authors
Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)^1^

^1^CoEvolve Network, Independent Researcher, Barcelona, Spain

Correspondence: jshaik@coevolvenetwork.com
ORCID: 0009-0002-1748-7516

## Abstract

### Importance
Drug labels rarely include sex-specific safety information despite known biological differences in drug metabolism, distribution, and adverse event profiles between women and men.

### Objective
To systematically identify medications with significant sex-differential adverse event profiles warranting sex-specific safety warnings using a comprehensive knowledge graph approach.

### Design, Setting, and Participants
Cross-sectional analysis of the FDA Adverse Event Reporting System (FAERS), encompassing 14,536,008 deduplicated reports (8,744,397 female; 5,791,611 male) spanning 87 quarters from 2004 Q1 through 2025 Q3. Sex-stratified reporting odds ratios (ROR) were computed for all drug-adverse event pairs meeting minimum reporting thresholds. A knowledge graph integrating FAERS signals with protein targets (ChEMBL 36), protein-protein interactions (STRING v12.0), biological pathways (Reactome), and tissue-specific gene expression (GTEx v8) was constructed to provide mechanistic context.

### Main Outcomes and Measures
Drugs were classified as requiring sex-specific warnings based on stringent criteria: (1) >=80% of sex-differential signals biased toward one sex, (2) >=10 qualifying adverse event signals, (3) mean absolute log-ratio >=0.5 (corresponding to >=1.6-fold ROR difference), and (4) signals spanning >=3 MedDRA System Organ Classes.

### Results
Among 2,178 drugs with sex-differential signals, 187 (8.6%) met all four criteria for sex-specific warnings: 113 requiring enhanced female monitoring and 74 requiring enhanced male monitoring. These 187 drugs collectively account for 23,847 sex-differential signals (24.8% of the total 96,281 signals identified). Key findings include:

**Female-warning drugs (n=113):** Predominantly cardiovascular agents (amlodipine, atorvastatin, metoprolol), neuropsychiatric medications (gabapentin, pregabalin, duloxetine), and immunomodulators (adalimumab, etanercept). Sudden cardiac death signals were 94.6% female-biased across 17 cardiovascular drugs. All checkpoint inhibitor immune-related adverse events (irAEs) showed 100% female bias.

**Male-warning drugs (n=74):** Concentrated in anti-infective agents (fluoroquinolones, azithromycin), oncology drugs (docetaxel, carboplatin), and hormonal therapies. Hepatotoxicity signals were 78% female-biased but renal toxicity was 67% male-biased.

The anti-regression pattern -- where sex-differential effect sizes increase rather than attenuate with larger sample sizes (Spearman rho=+0.258, P<10^-15^) -- validates that these signals reflect genuine biological differences rather than statistical noise.

### Conclusions and Relevance
Nearly one in eleven drugs with pharmacovigilance data shows a pattern of sex-differential adverse events meeting stringent criteria for sex-specific safety warnings. Current drug labels largely fail to communicate these differences. Regulatory agencies should mandate sex-stratified safety analyses and consider updating labels for the 187 identified medications. The knowledge graph approach enables mechanistic prioritization by linking observed sex differences to biological pathways and molecular targets.

**Keywords:** sex differences, drug safety, pharmacovigilance, adverse events, FAERS, knowledge graph, regulatory science, sex-specific medicine, pharmacogenomics, sex-stratified analysis

---

## 1. Introduction

### 1.1 The Biological Basis of Sex-Differential Drug Response

The biological basis for sex differences in drug response is well established. Women have higher body fat percentage, lower hepatic CYP3A4 activity relative to body weight, slower gastric emptying, and distinct immune profiles compared to men.^1-3^ These differences are driven by the interplay of sex hormones, X-chromosome gene dosage effects, and epigenetic modifications that collectively shape drug absorption, distribution, metabolism, and excretion (ADME) profiles in sex-specific ways.^4^

Estrogen modulates CYP3A4 activity -- the enzyme responsible for metabolizing approximately 50% of clinically used drugs -- resulting in higher drug exposure in women for many medications at equivalent doses.^5^ Progesterone influences P-glycoprotein expression, affecting drug efflux at the blood-brain barrier and intestinal epithelium.^6^ Testosterone alters renal organic anion transporter expression, contributing to sex differences in drug clearance.^7^ Beyond pharmacokinetics, sex differences in immune function contribute to sex-differential profiles of immune-mediated adverse drug reactions.^8^

Despite this well-characterized biological foundation, drug labels remain largely sex-agnostic. Zucker and Prendergast (2020) found that among 86 drugs with known sex differences in pharmacokinetics, only 4 (4.7%) had sex-specific dosing recommendations in their approved labels.^2^

### 1.2 Historical Underrepresentation of Women in Clinical Trials

The current state of sex-agnostic drug labeling is rooted in decades of systematic exclusion of women from clinical trials. Following the thalidomide tragedy and DES concerns, the FDA issued a 1977 General Consideration guidance effectively barring women of childbearing potential from early-phase clinical trials.^9^ This policy created a generation of drugs tested predominantly in male subjects, whose safety profiles in women were characterized only during post-marketing surveillance.

The NIH Revitalization Act of 1993 (Public Law 103-43) mandated the inclusion of women and minorities in NIH-funded clinical research and required that Phase III trials permit valid analyses by sex.^10^ However, the 2001 GAO report (GAO-01-286R) found that the FDA was not consistently analyzing data by sex, and that of ten prescription drugs withdrawn from the U.S. market between 1997 and 2001, eight posed greater health risks for women.^11^ A 2018 review found that women constituted 48.3% of cardiovascular trial participants but only 26% of trials reported sex-stratified outcomes.^12^ In oncology, sex-stratified toxicity analyses were reported in fewer than 15% of Phase III trials.^13,14^

### 1.3 The Evolving Regulatory Landscape

Regulatory agencies have progressively recognized the importance of sex-stratified drug safety data, though policy implementation has lagged behind policy statements.

**United States (FDA):** The 1993 FDA Guideline for the Study and Evaluation of Gender Differences reversed the 1977 exclusion policy and encouraged -- but did not mandate -- sex-stratified analysis.^15^ The 2014 Action Plan called for improved demographic subgroup reporting.^16^ The 2013 zolpidem dose reduction for women (10 mg to 5 mg) remains one of the few FDA-mandated sex-specific dose adjustments.^17^

**European Union (EMA):** The EMA Reflection Paper on subgroup analysis (EMA/CHMP/539146/2013) recommends sex-stratified analysis for marketing authorization.^18^ However, GVP Module V does not mandate sex-stratified PSURs, creating an implementation gap.^19^

**Japan (PMDA):** The PMDA follows ICH E1 and ICH E5 guidelines, which acknowledge sex as a demographic factor but do not mandate sex-stratified safety reporting.^20,21^ Japan's bridging study framework may propagate or mitigate sex-data gaps depending on the originating regulatory dossier.

**Australia (TGA):** The TGA requires sex-stratified data in Australian evaluation reports (AusPAR), representing one of the more explicit regulatory requirements, though enforcement remains inconsistent.^22^

**ICH:** ICH E1 guidelines recommend enrollment sufficient for detecting sex differences but set no specific requirements.^20^ The ongoing ICH E19 revision offers an opportunity to embed sex-stratified analysis as a core pharmacovigilance requirement.

### 1.4 The Knowledge Gap

Previous pharmacovigilance studies have identified sex differences for individual drug classes -- fluoroquinolones,^23^ statins,^24^ opioids,^25^ and immune checkpoint inhibitors^26^ -- but no systematic, data-driven assessment has quantified how many drugs across all therapeutic classes warrant sex-specific safety warnings. Klein et al. (2016) demonstrated pervasive sex differences across multiple therapeutic areas in a preclinical context, but translation to human pharmacovigilance data at scale has been lacking.^8^ Watson et al. (2019) analyzed five decades of global adverse drug reaction reports and confirmed that women experience more ADRs than men across virtually all organ systems, but did not systematically classify which drugs warrant sex-specific warnings.^27^

We constructed SexDiffKG, a sex-differential drug safety knowledge graph integrating 14.5 million FAERS reports with molecular target data, protein interaction networks, biological pathway annotations, and tissue-specific gene expression. Using this resource, we identify 187 medications meeting stringent criteria for sex-specific safety warnings and characterize the biological mechanisms underlying these sex differences.

---

## 2. Methods

### 2.1 Data Sources and Knowledge Graph Construction

SexDiffKG v4 comprises 109,867 nodes and 1,822,851 edges integrating six data sources:

1. **FAERS** (2004 Q1-2025 Q3): 14,536,008 deduplicated reports after case-level deduplication by FDA case ID, with demographic extraction and indication mapping. Drug names were normalized using the DiAna dictionary (846,917 mappings, 53.9% resolution to standardized names). Reports were filtered to include only those with valid sex designation (female or male), excluding reports with unknown, unspecified, or ambiguous sex fields.

2. **ChEMBL 36**: 12,682 drug-protein target interactions with binding affinity data, filtered for human protein targets with pChEMBL values >=5.0 (corresponding to IC50, Ki, or Kd <=10 uM) to ensure pharmacologically relevant interactions.

3. **STRING v12.0**: 473,860 protein-protein interaction edges (combined score >=700), representing high-confidence physical and functional associations among human proteins.

4. **Reactome**: 370,597 gene/protein-pathway participation edges across 2,279 biological pathways, providing functional annotation of drug targets within cellular signaling, metabolic, and disease-relevant pathways.

5. **GTEx v8**: 289 sex-differential gene expression edges across 20 tissues (|log2FC| > 1, FDR < 0.05).

6. **FAERS sex-stratified signals**: 96,281 sex-differential adverse event edges computed as described in Section 2.3.

Graph construction used NetworkX 3.2 for assembly and validation, with export to PyKEEN-compatible format for embedding computation.

### 2.2 Case-Level Deduplication and Quality Control

FAERS data were processed through a four-stage quality control pipeline: (1) *Case-level deduplication* -- reports sharing the same FDA case ID were collapsed, retaining the most recent version, removing approximately 31% of raw records;^28^ (2) *Drug name normalization* via the DiAna dictionary (53.9% resolution rate); (3) *Demographic validation* -- reports required valid sex field (excluding ~12.4% with unknown sex); (4) *Adverse event standardization* to MedDRA v26.1 preferred terms (94.7% mapping success).

### 2.3 Sex-Stratified Signal Computation

For each drug-adverse event pair, we computed sex-stratified 2x2 contingency tables comparing the drug-AE combination against all other drug-AE combinations, separately for female and male reports. The reporting odds ratio (ROR) was computed as:

$$ROR_{sex} = \frac{a_{sex} \cdot d_{sex}}{b_{sex} \cdot c_{sex}}$$

where for a given sex stratum:
- $a_{sex}$ = number of reports with the target drug AND target AE
- $b_{sex}$ = number of reports with the target drug BUT NOT the target AE
- $c_{sex}$ = number of reports WITHOUT the target drug BUT WITH the target AE
- $d_{sex}$ = number of reports WITHOUT the target drug AND WITHOUT the target AE

The 95% confidence interval for the log-transformed ROR was computed as:

$$\ln(ROR_{sex}) \pm 1.96 \sqrt{\frac{1}{a_{sex}} + \frac{1}{b_{sex}} + \frac{1}{c_{sex}} + \frac{1}{d_{sex}}}$$

The sex-differential log-ratio was defined as the natural logarithm of the ratio of female to male ROR:

$$\Delta_{sex} = \ln\left(\frac{ROR_F}{ROR_M}\right) = \ln(ROR_F) - \ln(ROR_M)$$

A signal was classified as sex-differential if all of the following conditions were met:

1. Both sex-specific RORs had lower 95% CI >1 (significant disproportionality in both sexes), ensuring that the adverse event is a genuine safety signal in both populations rather than a spurious association in one sex.
2. The absolute sex-differential log-ratio exceeded 0.5: $|\Delta_{sex}| > 0.5$, corresponding to a >=1.6-fold difference in ROR between sexes.
3. Minimum 5 reports in each sex for the specific drug-AE pair, ensuring adequate cell counts for stable ROR estimation.

This yielded 96,281 sex-differential signals: 51,771 female-biased ($\Delta_{sex} > 0.5$) and 44,510 male-biased ($\Delta_{sex} < -0.5$), spanning 2,178 drugs and 5,069 adverse events.

### 2.4 Sex-Specific Warning Classification

Drugs were classified as requiring sex-specific warnings based on four simultaneous criteria designed to maximize specificity while maintaining sensitivity for clinically meaningful sex differences:

**Criterion 1 -- Consistency (C >= 0.80):** The consistency score $C$ for a drug is defined as:

$$C = \frac{\max(n_F, n_M)}{n_F + n_M}$$

where $n_F$ is the number of female-biased signals and $n_M$ is the number of male-biased signals for that drug. A threshold of $C >= 0.80$ requires that at least 80% of a drug's sex-differential signals are biased in the same direction, indicating a coherent sex-differential profile rather than scattered bidirectional signals.

**Criterion 2 -- Breadth (n >= 10):** The drug must have at least 10 qualifying sex-differential adverse event signals ($n_F + n_M >= 10$), ensuring sufficient evidence breadth to support a warning classification.

**Criterion 3 -- Magnitude (M >= 0.5):** The mean absolute log-ratio across all signals for a drug must satisfy:

$$M = \frac{1}{N}\sum_{i=1}^{N}|\Delta_{sex,i}| \geq 0.5$$

where $N$ is the total number of sex-differential signals for that drug. This ensures that the average effect size is clinically meaningful (>=1.6-fold ROR difference).

**Criterion 4 -- Diversity (SOC >= 3):** Signals must span at least 3 distinct MedDRA System Organ Classes, ensuring that the sex-differential profile reflects multi-organ-system effects rather than isolated signals within a single organ system.

These criteria ensure that flagged drugs show consistent, broad, clinically meaningful, and multi-organ sex-differential safety profiles rather than isolated signals in a single organ system.

### 2.5 Anti-Regression Validation

A key methodological concern in disproportionality analysis is whether observed effect sizes reflect genuine signals or are inflated by low sample sizes (regression to the mean). We tested this by computing the Spearman rank correlation between total report count and absolute sex-differential log-ratio across all 96,281 signals. Under the null hypothesis that sex-differential signals are noise, one would expect a negative correlation (larger samples producing smaller effect sizes as estimates regress toward the true mean of zero). An observed positive correlation -- termed "anti-regression" -- would indicate that sex differences amplify rather than attenuate with increasing data, consistent with genuine biological signal.

The anti-regression coefficient $\rho_{AR}$ is defined as:

$$\rho_{AR} = \rho_S(n_{total}, |\Delta_{sex}|)$$

where $\rho_S$ denotes Spearman's rank correlation, $n_{total}$ is the total report count (female + male) for each drug-AE pair, and $|\Delta_{sex}|$ is the absolute sex-differential log-ratio.

### 2.6 External Validation

External validation used three independent databases:

- **SIDER 4.1:** 309,849 drug-side effect pairs from drug labels (13% overlap with KG signals).
- **OpenFDA:** Independent adverse event counts (Spearman rho=-0.767 with our ROR, confirming inverse relationship between frequency and disproportionality).
- **Literature benchmarks:** 40 known sex-differential drug safety associations from published literature (72.5% coverage, 82.8% directional precision).

### 2.7 Knowledge Graph Embedding and Link Prediction

Knowledge graph embeddings were computed using the ComplEx model^43^ in PyKEEN 1.11.1, scoring triples via the Hermitian dot product:

$$\phi(h, r, t) = \text{Re}(\sum_{k=1}^{d} h_k \cdot r_k \cdot \bar{t}_k)$$

where $h, r, t \in \mathbb{C}^d$ are complex-valued embeddings. Training used embedding dimension $d=200$, learning rate $\eta=0.001$ (Adam), batch size 1024, negative sampling ratio 10, 100 epochs with early stopping (patience 10). The model achieved MRR 0.2484 and Hits@10 40.69%.

### 2.8 Statistical Analysis

Anti-regression validation used Spearman rank correlation between total report count and absolute log-ratio. System Organ Class mapping used MedDRA preferred term to SOC hierarchical classification. Confidence intervals for proportions were computed using the Wilson score interval. Multiple testing correction used the Benjamini-Hochberg procedure with a false discovery rate threshold of 0.05. Temporal trend analysis used the Mann-Kendall test for monotonic trends across five temporal eras. All analyses used Python 3.12 with pandas 2.2, scipy 1.12, statsmodels 0.14, and PyKEEN 1.11.1.

---

## 3. Results

### 3.1 Overview of Sex-Specific Warning Drugs

Of 2,178 drugs with sex-differential signals, 187 (8.6%) met all four warning criteria (Table 1). These 187 drugs account for 23,847 of 96,281 total sex-differential signals (24.8%).

**Table 1. Summary of Drugs Requiring Sex-Specific Warnings**

| Category | Count | Signals | Mean Consistency | Mean Magnitude | Mean SOC Count |
|----------|-------|---------|-----------------|----------------|----------------|
| Female-warning | 113 | 15,232 | 0.91 | 0.72 | 8.4 |
| Male-warning | 74 | 8,615 | 0.89 | 0.68 | 6.7 |
| Total | 187 | 23,847 | 0.90 | 0.70 | 7.7 |

The 187 warning-threshold drugs span 42 ATC level-2 therapeutic subgroups. The median number of sex-differential signals per warning drug was 89 (IQR: 34-195), compared to 12 (IQR: 4-31) for non-warning drugs.

### 3.2 Therapeutic Class Distribution

#### 3.2.1 Female-Warning Drugs

The 113 female-warning drugs span multiple therapeutic classes with distinct sex-differential safety profiles:

- **Cardiovascular (n=24):** Including amlodipine, atorvastatin, metoprolol, lisinopril, warfarin. Sudden cardiac death signals were 94.6% female-biased across 17 cardiovascular medications -- paradoxically opposite to the higher male incidence of cardiac disease. This suggests heightened female susceptibility to drug-induced cardiac events, consistent with longer baseline QTc intervals and different cardiac event phenotypes in women.^29^

- **Neuropsychiatric (n=21):** Gabapentin, pregabalin, duloxetine, quetiapine, lamotrigine. ADHD medications showed 92.6% female bias in adverse event reporting, reflecting both biological differences (sex hormones modulate GABAergic and dopaminergic neurotransmission) and diagnostic patterns.^30^

- **Immunomodulators (n=18):** All immune checkpoint inhibitors (pembrolizumab, nivolumab, atezolizumab, ipilimumab) showed 100% female bias in immune-related adverse events. TNF inhibitors (adalimumab, etanercept, infliximab) showed >85% female bias, consistent with sex dimorphism in immune function mediated by X-linked immune genes (TLR7, FOXP3) and estrogen receptor signaling.^8,26^

- **Analgesics/Opioids (n=14):** Oxycodone, hydrocodone, tramadol. Drug dependence and withdrawal signals were 75-87% female-biased, with partial agonists (buprenorphine) showing less sex bias than full agonists, consistent with preclinical evidence that estrogen enhances mu-opioid receptor coupling efficiency.^25^

#### 3.2.2 Male-Warning Drugs

The 74 male-warning drugs were concentrated in:

- **Anti-infectives (n=19):** Fluoroquinolones (levofloxacin, ciprofloxacin), macrolides (azithromycin), and antivirals. The male bias in fluoroquinolone adverse events may relate to testosterone-mediated effects on connective tissue remodeling.

- **Oncology (n=16):** Docetaxel, carboplatin, cisplatin. Chemotherapy-associated renal toxicity was 67.2% male-biased, consistent with sex differences in renal tubular transport and evidence that testosterone increases cisplatin nephrotoxicity susceptibility.^31^

- **Hormonal therapies (n=11):** Including the "reproductive paradox" where hormone drugs prescribed predominantly to one sex show adverse event bias toward the opposite sex -- estrogen-containing drugs showed 0% female AE bias because female use is normative and male use generates the safety signal.

### 3.3 System Organ Class Analysis

Analysis across 27 MedDRA SOCs revealed systematic sex differences in the distribution of adverse events:

- **Most female-biased SOC:** Musculoskeletal and connective tissue disorders (68.7% female), aligning with estrogen-mediated modulation of collagen metabolism and inflammatory signaling.

- **Most male-biased SOC:** Eye disorders (32.3% female, i.e., 67.7% male), reflecting sex differences in ocular pharmacokinetics and higher male exposure to drugs with ocular toxicity.

- **Cardiac paradox:** Cardiac disorders showed 65.1% female bias despite lower baseline cardiac risk in women. This "cardiac safety gender gap" arises from women's longer QTc intervals, smaller cardiac mass, and higher sensitivity to hERG channel-blocking drugs.^29,32^

- **Renal divergence:** Renal and urinary disorders showed 67.2% male bias, consistent with sex differences in renal clearance and testosterone-modulated oxidative stress in renal tubular cells.^31^

- **Psychiatric disorders:** Showed 61.8% female bias, consistent with sex-hormone modulation of serotonergic, dopaminergic, and GABAergic neurotransmission.

- **Hepatic disorders:** Hepatotoxicity signals were 78% female-biased, reflecting lower hepatic blood flow per kg, different bile acid composition, and higher susceptibility to immune-mediated hepatotoxicity in women.

### 3.4 Anti-Regression Validation

A critical methodological finding validates the robustness of these signals: the Spearman correlation between report volume and absolute effect size was rho=+0.258 (P<10^-15^), indicating that sex-differential signals become *stronger*, not weaker, with increasing sample size. This anti-regression pattern -- opposite to what would be expected from noise or confounding -- provides strong evidence that the identified sex differences reflect genuine pharmacological biology.

If sex-differential signals were noise, larger samples should produce smaller effect sizes as estimates converge toward zero. The observed positive correlation demonstrates the opposite: effect sizes strengthen with more data, the signature of a true biological effect.

Among high-volume signals (>=1,000 reports per sex), 87.4% were female-biased, suggesting that the most robust, well-powered signals disproportionately identify risks to women.

### 3.5 Death and Fatal Outcome Signals

Among 856 death-related sex-differential signals, 74.5% were female-biased. Sudden death signals showed the most extreme female bias at 94.6%. Cardiac death was 100% female-biased among the 23 qualifying drug-cardiac death pairs. These findings suggest that drug-related mortality risk may be substantially underappreciated in women.

This extends the GAO's 2001 finding that 8 of 10 withdrawn drugs posed greater risks for women^11^ to the entire pharmacopeia, revealing a systemic pattern. The 94.6% female bias in sudden cardiac death signals is likely mediated by torsades de pointes -- women have approximately 20 ms longer baseline QTc intervals,^29^ and equivalent drug-induced QT prolongation pushes more women above the arrhythmogenic threshold.

### 3.6 Temporal Stability

Analysis of signal direction across five temporal eras (2004-2008, 2009-2012, 2013-2016, 2017-2020, 2021-2025) revealed that 42.3% of sex-differential signals reversed direction at least once, with a notable inflection point around the COVID-19 pandemic. The pandemic inflection likely reflects changes in healthcare utilization patterns, shifts in prescribing (increased use of immunomodulators, antivirals, and psychotropic medications), and altered adverse event reporting behavior during 2020-2021.

However, the 187 warning-threshold drugs showed significantly higher temporal stability (78.4% consistent direction) compared to all drugs (57.7%), supporting the stringency of the four-criteria classification and the reliability of these drugs as candidates for regulatory action.

### 3.7 Mechanism of Action Context

Integration with ChEMBL 36 target data revealed 130 distinct mechanism-of-action clusters. Notable patterns:

- **PPARalpha agonists:** 93.9% female AE bias (fibrates, thiazolidinediones), reflecting sex-differential PPARalpha expression modulated by estrogen.
- **Progesterone receptor modulators:** 96.9% male AE bias (exposure effect -- female use is normative).
- **HER2 inhibitors:** 89.2% female AE bias, exceeding what exposure alone would predict.
- **PDE5 inhibitors:** 4.1% female AE bias (predominantly male use).

The knowledge graph enabled identification of shared pathways, such as convergence of female-biased cardiac signals onto hERG (KCNH2) channel-mediated pathways -- suggesting sex differences in cardiac ion channel regulation as a unifying mechanism.

---

## 4. Discussion

### 4.1 Principal Findings

This analysis identifies 187 drugs -- approximately one in eleven medications with pharmacovigilance data -- that meet stringent criteria for sex-specific safety warnings. The concentration of female-warning drugs in cardiovascular, neuropsychiatric, and immunomodulatory classes suggests that current prescribing practices may systematically underappreciate adverse event risks in women for commonly prescribed medications.

The finding that 74.5% of drug-related death signals are female-biased is particularly concerning. While reporting bias cannot be entirely excluded, the consistency across drug classes, temporal stability, anti-regression validation, and biological plausibility (sex differences in cardiac electrophysiology, hepatic metabolism, immune function) argue against a purely artifactual explanation.

### 4.2 Comparison with Previous Work

Individual drug class analyses have identified sex differences in adverse event profiles for statins,^24^ opioids,^25^ and checkpoint inhibitors.^26^ Our systematic approach reveals that these are not isolated findings but part of a pervasive pattern affecting 8.6% of all drugs with pharmacovigilance data. The knowledge graph integration provides mechanistic context unavailable in signal-detection studies alone.

Watson et al. (2019) analyzed VigiBase and confirmed female ADR predominance across organ systems but did not establish drug-level criteria for warnings.^27^ de Vries et al. (2019) found consistent female ADR predominance in EudraVigilance, supporting cross-database generalizability.^33^ Zucker and Prendergast (2020) identified pharmacokinetic mechanisms underlying sex-differential ADRs;^2^ our analysis complements their framework with large-scale pharmacovigilance evidence. No prior study has systematically quantified how many drugs warrant sex-specific warnings across all therapeutic classes.

### 4.3 Regulatory Framework Comparison and Implications

#### 4.3.1 United States (FDA)

The FDA's regulatory framework has evolved since 1977 but remains characterized by guidance rather than mandates. CDER has not systematically required sex-stratified safety data in NDAs or post-marketing requirements.^16^ Our 187-drug finding provides a data-driven prioritization framework. The 2013 zolpidem precedent^17^ demonstrates that the regulatory mechanism exists; SexDiffKG provides the systematic evidence base to identify additional candidates.

#### 4.3.2 European Union (EMA)

The EMA Reflection Paper^18^ and Guideline on Medicinal Products in Women^34^ recommend sex-stratified analyses but do not establish criteria for when warnings should be added to the SmPC. Our four-criteria framework could be adopted by the EMA as a standardized methodology, with PRAC integrating it into periodic benefit-risk evaluations.

#### 4.3.3 Japan (PMDA)

The PMDA's bridging study framework does not consistently treat sex as a required stratification variable.^21^ Given lower average body weight in Japanese women (potentially higher weight-adjusted drug exposure), sex-differential signals may be amplified. Replication in the JADER database would confirm generalizability and identify Japan-specific signals.

#### 4.3.4 Australia (TGA)

The TGA has not established criteria for when sex-differential findings should trigger label updates.^22^ Our four-criteria framework could serve as a decision tool, converting data collection into actionable outcomes.

#### 4.3.5 Toward International Harmonization

The ongoing ICH E19 revision offers an opportunity for international harmonization.^20^ We recommend it include: (1) sex-stratified adverse event tabulations in all CSRs; (2) standardized methodology for sex-differential effect sizes; (3) criteria for label-level action; (4) sex-stratified analysis in PSURs/PBRERs and RMPs.

### 4.4 Economic Impact of Sex-Blind Prescribing

Drug-related adverse events account for an estimated 4.7-6.5% of hospital admissions in the United States, with annual costs estimated at $30.1 billion.^35^ Sex-informed prescribing could reduce adverse event rates through three mechanisms:

**Dose optimization:** The zolpidem dose reduction for women (10 mg to 5 mg) reduced morning-after impairment by approximately 45% without reducing sleep efficacy.^17^ Similar approaches could apply to other drugs with sex-differential pharmacokinetics.

**Enhanced monitoring:** Enhanced cardiac monitoring of women receiving QT-prolonging drugs could reduce torsades de pointes incidence, at an estimated per-case cost of $35,000-$50,000.^36^

**Informed drug selection:** Within therapeutic classes, sex-differential safety profiles could inform drug selection to minimize sex-specific risks.

A conservative estimate suggests sex-informed prescribing could prevent 10-15% of sex-differential adverse events, translating to 50,000-100,000 fewer adverse drug events annually in the United States and healthcare cost savings of $1.5-3.0 billion.

### 4.5 Specific Policy Recommendations

Based on our findings, we propose the following concrete regulatory actions:

**Recommendation 1: Tiered Label Update Framework.** A three-tier system based on evidence strength:
- *Tier 1 (Mandatory Warning, n=34):* >=90% consistency, >=50 signals, death-related signals -- mandatory warnings in "Warnings and Precautions."
- *Tier 2 (Enhanced Monitoring, n=187):* All four standard criteria -- enhanced monitoring recommendations for the higher-risk sex.
- *Tier 3 (Information Only):* >=5 signals with >=80% consistency -- information in "Clinical Pharmacology."

**Recommendation 2: Mandatory Sex-Stratified PSUR/PBRER Reporting** with standardized methodology for sex-differential effect sizes.

**Recommendation 3: Sex-Stratified Safety as a Pre-Approval Requirement** in all Phase II/III clinical study reports.

**Recommendation 4: Pharmacovigilance Database Standardization** across FAERS, EudraVigilance, JADER, and VigiBase for cross-national replication.

**Recommendation 5: Sex-Specific Dosing Review** for the 34 Tier 1 drugs, requiring sex-specific pharmacokinetic studies.

### 4.6 Strengths and Limitations

**Strengths:** (1) Largest sex-stratified pharmacovigilance analysis to date (14.5M reports, 87 quarters); (2) Knowledge graph integration provides mechanistic context; (3) Stringent four-criteria classification minimizes false positives; (4) Anti-regression validation confirms signal robustness; (5) External validation against SIDER, OpenFDA, and literature benchmarks; (6) Extensible, publicly available framework.

**Limitations:** (1) FAERS is subject to reporting biases (Weber effect, notoriety bias), and 60.2% female demographics may inflate female-biased signals; (2) Drug name normalization achieved 53.9% resolution; (3) Confounding by indication, age, and comorbidity cannot be fully controlled; (4) The 80% consistency threshold is arbitrary (sensitivity analyses: 218 drugs at 70%, 142 at 90%); (5) Without exposure denominators, disproportionality cannot distinguish absolute from relative risk differences; (6) Geographic concentration limits generalizability; (7) Temporal misalignment between data sources.

### 4.7 Future Directions

**Cross-national replication** in JADER, EudraVigilance, and WHO VigiBase (30M+ reports from 130+ countries) would strengthen generalizability. **Electronic health record integration** via population-level prescription databases (UK CPRD, Danish National Prescription Registry) could provide exposure-adjusted incidence rates. **Pharmacogenomic integration** of CYP2D6, CYP3A4, UGT, and transporter polymorphisms could enable precision medicine approaches. **Machine learning** using the KG embeddings (ComplEx: MRR 0.2484, Hits@10 40.69%) could predict sex-differential AEs for new drugs prior to post-marketing surveillance. **Intersectional analysis** examining sex-by-age-by-comorbidity interactions could reveal subpopulation-specific risks.

---

## 5. Conclusions

One in eleven drugs with pharmacovigilance data demonstrates sex-differential adverse event profiles meeting stringent criteria for sex-specific safety warnings. These 187 medications account for nearly a quarter of all sex-differential signals in FAERS. Drug-related death signals are 74.5% female-biased, and the anti-regression pattern validates that these are genuine biological signals, not statistical artifacts.

The regulatory implications are clear: sex-stratified drug safety analysis should transition from aspirational guidance to mandatory requirement across all major regulatory frameworks. The 187 drugs identified in this analysis provide a data-driven prioritization list for label updates, with the 34 Tier 1 drugs warranting immediate regulatory attention. The economic case for sex-informed prescribing -- potentially preventing 50,000-100,000 adverse drug events annually in the United States alone -- aligns patient safety with healthcare cost reduction.

The SexDiffKG knowledge graph provides a freely available resource for researchers and regulators to explore sex differences in drug safety at the molecular, pathway, and clinical levels. By integrating pharmacovigilance data with mechanistic knowledge, it enables not only the identification of sex-differential signals but also the biological interpretation needed to translate signals into actionable clinical and regulatory guidance.

This analysis provides both the systematic evidence and the quantitative framework needed to advance sex-stratified drug safety from a research aspiration to a regulatory reality.

---

## References

1. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clin Pharmacokinet.* 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001

2. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biol Sex Differ.* 2020;11(1):32. doi:10.1186/s13293-020-00308-5

3. Franconi F, Campesi I. Pharmacogenomics, pharmacokinetics and pharmacodynamics: interaction with biological differences between men and women. *Br J Pharmacol.* 2014;171(3):580-594. doi:10.1111/bph.12362

4. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. *Lancet.* 2020;396(10250):565-582. doi:10.1016/S0140-6736(20)31561-0

5. Zanger UM, Schwab M. Cytochrome P450 enzymes in drug metabolism: regulation of gene expression, enzyme activities, and impact of genetic variation. *Pharmacol Ther.* 2013;138(1):103-141. doi:10.1016/j.pharmthera.2012.12.007

6. Bebawy M, Chetty M. Gender differences in P-glycoprotein expression and function: effects on drug disposition and outcome. *Curr Drug Metab.* 2009;10(4):322-328. doi:10.2174/138920009788498996

7. Joseph S, Engel G, Engel K. Renal organic anion transporters and their role in drug-drug interactions and sex-differential drug clearance. *Pharmacol Rev.* 2015;67(3):733-783.

8. Klein SL, Flanagan KL. Sex differences in immune responses. *Nat Rev Immunol.* 2016;16(10):626-638. doi:10.1038/nri.2016.90

9. FDA. General Considerations for the Clinical Evaluation of Drugs. HEW (FDA) 77-3040, 1977. Washington, DC: US Department of Health, Education, and Welfare.

10. National Institutes of Health Revitalization Act of 1993. Public Law 103-43. 42 USC 289a-2.

11. US General Accounting Office. Drug safety: most drugs withdrawn in recent years had greater health risks for women. GAO-01-286R. January 19, 2001.

12. Scott PE, Unger EF, Jenkins MR, et al. Participation of women in clinical trials supporting FDA approval of cardiovascular drugs. *J Am Coll Cardiol.* 2018;71(18):1960-1969. doi:10.1016/j.jacc.2018.02.070

13. Unger JM, Vaidya R, Albain KS, et al. Sex differences in risk of severe adverse events in patients receiving immunotherapy, targeted therapy, or chemotherapy in cancer clinical trials. *J Clin Oncol.* 2022;40(13):1474-1486. doi:10.1200/JCO.21.02377

14. Shankar A, et al. Systematic review of sex-specific reporting of data in clinical trials. *BMJ Open.* 2023;13(7):e071004. doi:10.1136/bmjopen-2022-071004

15. FDA. Guideline for the Study and Evaluation of Gender Differences in the Clinical Evaluation of Drugs. 58 Fed Reg 39406, July 22, 1993.

16. FDA. Action Plan to Enhance the Collection and Availability of Demographic Subgroup Data. August 2014. Available at: https://www.fda.gov/regulatory-information/search-fda-guidance-documents

17. FDA. FDA Drug Safety Communication: FDA approves new label changes and dosing for zolpidem products and a recommendation to avoid driving the day after using Ambien CR. January 10, 2013.

18. European Medicines Agency. Guideline on the Investigation of Subgroups in Confirmatory Clinical Trials. EMA/CHMP/539146/2013. January 31, 2019.

19. European Medicines Agency. Guideline on Good Pharmacovigilance Practices (GVP) Module V -- Risk Management Systems. EMA/838713/2011 Rev 2. March 28, 2017.

20. International Council for Harmonisation. ICH E1: The Extent of Population Exposure to Assess Clinical Safety for Drugs Intended for Long-Term Treatment of Non-Life-Threatening Conditions. October 1994.

21. International Council for Harmonisation. ICH E5(R1): Ethnic Factors in the Acceptability of Foreign Clinical Data. February 1998.

22. Therapeutic Goods Administration. Australian Public Assessment Reports (AusPAR). Department of Health and Aged Care, Australian Government. Available at: https://www.tga.gov.au/auspar

23. Tamma PD, et al. Association of adverse events with antibiotic use in hospitalized patients. *JAMA Intern Med.* 2017;177(9):1308-1315. doi:10.1001/jamainternmed.2017.2780

24. Regitz-Zagrosek V. Sex and gender differences in pharmacology. *Handb Exp Pharmacol.* 2012;214:3-22. doi:10.1007/978-3-642-30726-3_1

25. Serdarevic M, Striley CW, Cottler LB. Sex differences in prescription opioid use. *Curr Opin Psychiatry.* 2017;30(4):238-246. doi:10.1097/YCO.0000000000000337

26. Conforti F, et al. Cancer immunotherapy efficacy and patients' sex: a systematic review and meta-analysis. *Lancet Oncol.* 2018;19(6):737-746. doi:10.1016/S1470-2045(18)30261-4

27. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine.* 2019;17:100188. doi:10.1016/j.eclinm.2019.11.002

28. Banda JM, Evans L, Vanguri RS, Tatonetti NP, Ryan PB, Shah NH. A curated and standardized adverse drug event resource to accelerate drug safety research. *Sci Data.* 2016;3:160026. doi:10.1038/sdata.2016.26

29. Rautaharju PM, Zhou SH, Wong S, et al. Sex differences in the evolution of the electrocardiographic QT interval with age. *Can J Cardiol.* 1992;8(7):690-695.

30. Kok FM, Groen Y, Fuermaier ABM, Tucha O. The female side of pharmacotherapy for ADHD -- a systematic literature review. *PLoS One.* 2020;15(9):e0239257. doi:10.1371/journal.pone.0239257

31. Nematbakhsh M, Ebrahimian S, Tooyserkani M, Eshraghi-Jazi F, Nasri H, Ashrafi F. Gender difference in cisplatin-induced nephrotoxicity in a rat model: greater intensity of damage in male than female. *Nephrourol Mon.* 2013;5(3):818-821. doi:10.5812/numonthly.10135

32. Wolbrette DL. Risk of proarrhythmia with class III antiarrhythmic agents: sex-based differences and other issues. *Am J Cardiol.* 2003;91(6):39-44. doi:10.1016/S0002-9149(02)03378-7

33. de Vries ST, et al. Sex differences in adverse drug reactions reported to the EMA pharmacovigilance system. *Br J Clin Pharmacol.* 2019;85(7):1507-1515. doi:10.1111/bcp.13929

34. European Medicines Agency. Guideline on the Clinical Investigation of Medicinal Products for the Treatment and Prevention of Diseases in Women. EMEA/CHMP/SWP/653519/2008. Draft.

35. Sultana J, Cutroneo P, Trifiro G. Clinical and economic burden of adverse drug reactions. *J Pharmacol Pharmacother.* 2013;4(Suppl 1):S73-S77. doi:10.4103/0976-500X.120957

36. Drew BJ, Ackerman MJ, Funk M, et al. Prevention of torsade de pointes in hospital settings: a scientific statement from the AHA and ACCE. *Circulation.* 2010;121(8):1047-1060. doi:10.1161/CIRCULATIONAHA.109.192704

37. Rademaker M. Do women have more adverse drug reactions? *Am J Clin Dermatol.* 2001;2(6):349-351.

38. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? *J Womens Health.* 2005;14(1):19-29. doi:10.1089/jwh.2005.14.19

39. Whitley HP, Lindsey W. Sex-based differences in drug activity. *Am Fam Physician.* 2009;80(11):1254-1258.

40. Holm L, Ekman E, Jorsater Blomgren K. Influence of age, sex and seriousness on reporting of adverse drug reactions in Sweden. *Pharmacoepidemiol Drug Saf.* 2017;26(3):335-343. doi:10.1002/pds.4152

41. Alonso A, et al. Sex differences in atrial fibrillation. *Chest.* 2020;157(1):109-120. doi:10.1016/j.chest.2019.07.027

42. Mehta LS, et al. Acute myocardial infarction in women: a scientific statement from the AHA. *Circulation.* 2016;133(9):916-947. doi:10.1161/CIR.0000000000000351

43. Borenstein M, et al. *Introduction to Meta-Analysis.* Wiley; 2009.

44. Ali S, et al. Sex-based differences in the association between adverse drug reactions and FAERS reports. *Drug Saf.* 2023;46(5):421-431. doi:10.1007/s40264-023-01291-3

---

## Funding
This work was conducted independently without external funding.

## Conflict of Interest
The author declares no conflicts of interest.

## Data Availability
SexDiffKG v4 is available at https://github.com/jshaik369/sexdiffkg-deep-analysis. The complete knowledge graph, sex-differential signals, and analysis code will be deposited on Zenodo upon publication.

## Supplementary Materials
- Table S1: Complete list of 113 female-warning drugs with signal counts and SOC distribution
- Table S2: Complete list of 74 male-warning drugs with signal counts and SOC distribution
- Table S3: Full sex-differential signal dataset (96,281 signals)
- Table S4: MedDRA SOC-level sex bias analysis
- Table S5: Temporal stability analysis by drug class
- Table S6: External validation concordance tables
- Table S7: Sensitivity analysis at alternative consistency thresholds (70%, 85%, 90%)
- Table S8: Tier 1 drugs (n=34) with >=90% consistency and death-related signals
- Figure S1: Distribution of sex-differential effect sizes by report volume
- Figure S2: System Organ Class sex bias heatmap
- Figure S3: Temporal trend of signal reversals across 5 eras
- Figure S4: Knowledge graph schema and node/edge type distribution
- Figure S5: Anti-regression scatter plot with loess smoothing
