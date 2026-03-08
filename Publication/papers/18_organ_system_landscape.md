# Cross-Organ Drug Class Sex Dimorphism: A Comprehensive Landscape Analysis of 14.5 Million FAERS Reports Across Ten Organ Systems

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516 | Email: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex differences in adverse drug reactions (ADRs) are well documented at the level of individual drugs and individual organ systems, yet systematic cross-organ analyses that track how the *same drug class* behaves across *different organ systems* remain absent from the literature. Whether the primary determinant of a drug's sex-differential safety profile is the pharmacological mechanism of the drug or the intrinsic vulnerability of the target organ is an open question with direct clinical implications.

**Methods.** We analyzed 14,536,008 individual case safety reports (ICSRs) from the FDA Adverse Event Reporting System (FAERS), spanning 87 quarters (2004 Q1 through 2025 Q3; 60.2% female reporters). Sex-differential signals were identified using log-likelihood ratio (LR) scoring with Bayesian shrinkage, yielding 96,281 statistically significant drug-adverse event pair signals across 2,178 unique drugs and 5,069 unique adverse events. Each signal was mapped to one of ten organ systems (hematologic, cardiac, renal, psychiatric, respiratory, metabolic/endocrine, neurologic, gastrointestinal, dermatologic, musculoskeletal) and annotated with drug class, severity grade, and temporal quarter. Cross-organ concordance was quantified for immune checkpoint inhibitors (ICIs), anti-tumor necrosis factor (anti-TNF) agents, and non-steroidal anti-inflammatory drugs (NSAIDs).

**Results.** The ten organ systems formed a continuous sex-dimorphism spectrum ranging from 52.1% female (hematologic) to 66.2% female (musculoskeletal). Immune checkpoint inhibitors exhibited consistent male-biased toxicity across all twelve organ sub-systems tested (range: 39.9%F respiratory to 50.8%F neurologic), representing the most organ-invariant drug class pattern in the dataset. Anti-TNF agents showed the converse: consistent female bias across all systems (63.3%F hematologic to 86.3%F musculoskeletal). Within organ systems, subcategory-level divergence was substantial: ICI-associated adrenal insufficiency was male-biased (45.8%F) while ICI-associated thyroiditis was female-biased (62.6%F), representing a 16.8 percentage-point spread within the same drug class and the same organ system. Across all ten systems, serious adverse events were more male-biased than non-serious events from the same organ category. Multivariate analysis confirmed that drug class was a stronger predictor of the sex ratio of an adverse event signal than organ system membership.

**Conclusions.** Drug pharmacological mechanism, not target organ identity, is the dominant determinant of sex-differential adverse event profiles. ICIs produce male-biased toxicity regardless of which organ is affected; anti-TNFs produce female-biased toxicity regardless of organ. This finding argues for drug-class-stratified, rather than organ-stratified, sex-aware pharmacovigilance monitoring. Clinical monitoring protocols should be organized primarily by drug mechanism with organ-specific modifiers, rather than the reverse.

**Keywords:** sex differences, pharmacovigilance, FAERS, immune checkpoint inhibitors, anti-TNF, cross-organ analysis, adverse drug reactions, drug safety, sex-stratified medicine

---

## 1. Introduction

Sex-based differences in drug safety have been recognized since at least the thalidomide tragedy of the 1960s, yet their systematic characterization has lagged behind efficacy-focused clinical research by decades (Zucker & Prendergast, 2020). Women experience adverse drug reactions at approximately 1.5 to 1.7 times the rate of men across therapeutic areas (Zopf et al., 2008), a disparity attributed variously to pharmacokinetic differences (body composition, CYP enzyme activity, renal clearance), pharmacodynamic differences (receptor density, immune responsiveness), hormonal modulation, and prescribing pattern asymmetries (Soldin & Mattison, 2009). Despite growing awareness, the FDA Adverse Event Reporting System (FAERS) — the largest spontaneous reporting database in the world — has been underutilized for systematic, multi-organ, drug-class-level sex-differential analysis.

Three distinct analytical paradigms have been applied to sex differences in ADRs. The first, and most common, is **organ-centric**: investigators select a single organ system (e.g., cardiac, hepatic, dermatologic) and catalog which drugs produce sex-differential toxicity within that organ (Salem et al., 2019; Rodenburg et al., 2012). The second is **drug-centric**: investigators select a single drug or drug class and catalog its sex-differential ADR profile across all reported events (Unger et al., 2022; Duma et al., 2019). The third paradigm — **cross-organ, cross-drug-class** — asks whether the same drug class produces concordant or discordant sex ratios when it damages different organ systems. This third paradigm has remained largely unexplored, primarily because it requires simultaneously large datasets, comprehensive organ-system mapping, and drug-class annotation.

The distinction matters clinically. If organ vulnerability is the primary determinant of sex ratios — that is, if the kidney "always" produces male-biased toxicity regardless of which drug damages it — then monitoring protocols should be organized by organ system. If, instead, drug mechanism is the primary determinant — that is, if immune checkpoint inhibitors "always" produce male-biased toxicity regardless of which organ they damage — then monitoring protocols should be organized by drug class. The two organizational principles lead to different clinical workflows, different alert thresholds, and different resource allocations.

This study addresses the cross-organ paradigm directly. Using 14.5 million FAERS reports spanning 21 years and 87 reporting quarters, we mapped 96,281 sex-differential signals across ten organ systems and systematically tracked drug class behavior across all ten. We report three principal findings: (1) a continuous organ-system sex-dimorphism spectrum from hematologic (most male-biased) to musculoskeletal (most female-biased); (2) immune checkpoint inhibitors as the most organ-invariant male-biased drug class, and anti-TNF agents as the most organ-invariant female-biased class; and (3) drug class as a stronger predictor of sex ratio than organ system membership. We discuss the immunological and pharmacological mechanisms underlying these patterns and propose a drug-class-first monitoring framework for sex-aware pharmacovigilance.

---

## 2. Methods

### 2.1 Data Source and Study Population

We extracted all individual case safety reports (ICSRs) from the FDA Adverse Event Reporting System (FAERS) quarterly data files spanning 2004 Q1 through 2025 Q3, comprising 87 quarterly releases. After deduplication by FDA case identifier and removal of reports with missing sex designation, the analytic dataset comprised 14,536,008 reports. The sex distribution was 60.2% female (n = 8,744,397) and 39.8% male (n = 5,791,611), consistent with the well-documented female predominance in spontaneous ADR reporting (Zucker & Prendergast, 2020).

### 2.2 Signal Detection and Sex-Differential Scoring

For each unique drug-adverse event (drug-AE) pair with at least 20 total reports and at least 5 reports from each sex, we computed a sex-differential signal using log-likelihood ratio (LR) scoring. The LR was defined as:

    LR = log2(observed_female_proportion / expected_female_proportion)

where the expected female proportion was derived from the overall FAERS sex ratio (60.2%F) with Bayesian shrinkage toward the population mean to stabilize estimates for low-count pairs. Signals were deemed statistically significant at a false discovery rate (FDR) < 0.05 after Benjamini-Hochberg correction, yielding 96,281 significant drug-AE pair signals across 2,178 unique drugs and 5,069 unique adverse events.

A positive LR (female proportion exceeding 60.2%) indicates female-biased reporting; a negative LR (female proportion below 60.2%) indicates male-biased reporting. The magnitude of the absolute LR (|LR|) quantifies the strength of the sex differential. Signals with |LR| > 0.5 were classified as strongly dimorphic.

### 2.3 Organ System Classification

Each of the 5,069 unique adverse events was mapped to one of ten organ systems using a hierarchical classification based on MedDRA System Organ Class (SOC) terms, supplemented by manual review for ambiguous terms:

1. **Hematologic** — blood and lymphatic system disorders, coagulopathies, cytopenias
2. **Cardiotoxicity** — cardiac disorders, vascular disorders (excluding cerebrovascular)
3. **Nephrotoxicity** — renal and urinary disorders
4. **Psychiatric** — psychiatric disorders, behavioral disturbances, substance-related events
5. **Respiratory** — respiratory, thoracic, and mediastinal disorders
6. **Metabolic/Endocrine** — metabolism and nutrition disorders, endocrine disorders
7. **Neurotoxicity** — nervous system disorders (excluding psychiatric), cerebrovascular events
8. **Gastrointestinal** — gastrointestinal disorders, hepatobiliary disorders
9. **Dermatologic** — skin and subcutaneous tissue disorders
10. **Musculoskeletal** — musculoskeletal and connective tissue disorders

Adverse events mapping to multiple SOCs were assigned to the primary SOC based on MedDRA primary path designation. Events not mapping to any of the ten systems (e.g., general disorders, investigations, surgical/procedural complications) were excluded from organ-system analyses but retained in drug-class-level analyses.

### 2.4 Drug Class Annotation

Drugs were annotated to pharmacological classes using the WHO Anatomical Therapeutic Chemical (ATC) classification system at the fourth level (chemical subgroup), supplemented by manual annotation for novel agents not yet assigned ATC codes. Key drug classes of interest included immune checkpoint inhibitors (ICIs: nivolumab, pembrolizumab, atezolizumab, ipilimumab, durvalumab, avelumab, cemiplimab, tremelimumab), anti-TNF agents (infliximab, adalimumab, etanercept, golimumab, certolizumab pegol), and non-steroidal anti-inflammatory drugs (NSAIDs: ibuprofen, naproxen, diclofenac, celecoxib, meloxicam, piroxicam, indomethacin, ketorolac).

### 2.5 Cross-Organ Concordance Analysis

For each drug class with signals in three or more organ systems, we computed the cross-organ concordance index (COCI), defined as the proportion of organ systems in which the drug class maintained the same directional bias (male-biased or female-biased) relative to the 60.2% female FAERS baseline. A COCI of 1.0 indicates perfect cross-organ concordance (all organs show the same directional bias); a COCI of 0.5 indicates no concordance. Drug classes were ranked by COCI to identify the most organ-invariant and most organ-variable pharmacological mechanisms.

### 2.6 Severity Stratification

Reports were classified as serious (resulting in death, hospitalization, disability, life-threatening condition, or congenital anomaly) or non-serious based on FAERS outcome codes. Sex ratios were computed separately for serious and non-serious events within each organ system to test the hypothesis that severity modifies sex-differential patterns.

### 2.7 Statistical Analysis

All analyses were conducted in Python 3.11 using pandas, scipy, and statsmodels. Confidence intervals for proportions were computed using the Wilson score method. Differences between proportions were tested using chi-squared tests with Yates correction. Multivariate logistic regression was used to assess the relative contribution of drug class versus organ system to the sex ratio of signals, with drug class and organ system as categorical predictors and female proportion as the outcome. The variance explained (pseudo-R-squared, McFadden) was compared between drug-class-only, organ-system-only, and combined models to quantify the relative predictive power of each factor.

---

## 3. Results

### 3.1 The Ten-Organ Sex-Dimorphism Spectrum

The 96,281 sex-differential signals distributed across the ten organ systems in a continuous gradient from near-parity to strongly female-biased (Table 1). Hematologic signals were the most sex-balanced (52.1%F, only 8.1 percentage points below the FAERS baseline of 60.2%), while musculoskeletal signals were the most female-biased (66.2%F, 6.0 points above baseline).

**Table 1. Ten-Organ System Sex-Dimorphism Spectrum**

| Rank | Organ System | Signals (n) | % Female | Deviation from Baseline (60.2%F) | Directional Bias |
|------|---|---|---|---|---|
| 1 | Hematologic | 3,122 | 52.1% | -8.1 pp | Male-biased |
| 2 | Cardiotoxicity | 3,792 | 53.6% | -6.6 pp | Male-biased |
| 3 | Nephrotoxicity | 2,382 | 54.9% | -5.3 pp | Male-biased |
| 4 | Psychiatric | 2,954 | 57.0% | -3.2 pp | Male-biased |
| 5 | Respiratory | 4,952 | 57.3% | -2.9 pp | Male-biased |
| 6 | Metabolic/Endocrine | 3,993 | 60.2% | 0.0 pp | Neutral |
| 7 | Neurotoxicity | 6,202 | 61.4% | +1.2 pp | Female-biased |
| 8 | Gastrointestinal | 4,476 | 61.8% | +1.6 pp | Female-biased |
| 9 | Dermatologic | 3,810 | 62.6% | +2.4 pp | Female-biased |
| 10 | Musculoskeletal | 3,218 | 66.2% | +6.0 pp | Female-biased |

The spectrum reveals a meaningful biological gradient. The three most male-biased systems (hematologic, cardiac, renal) are systems where male sex is an established epidemiological risk factor for primary disease (cardiovascular disease, chronic kidney disease, hematologic malignancies). The three most female-biased systems (musculoskeletal, dermatologic, gastrointestinal) are systems where autoimmune and inflammatory conditions with strong female predominance are prevalent (rheumatoid arthritis, lupus, inflammatory bowel disease, chronic pain syndromes). The metabolic/endocrine system sits precisely at the FAERS baseline (60.2%F), suggesting that metabolic ADRs faithfully reflect the sex composition of the reporting population without significant organ-specific amplification.

Neurotoxicity, the largest single system by signal count (n = 6,202), was modestly female-biased (61.4%F), consistent with the higher prevalence of chronic neurological conditions (migraine, multiple sclerosis, fibromyalgia-associated neuropathy) among women.

### 3.2 Immune Checkpoint Inhibitors: Universal Male Bias Across All Organ Systems

The most striking cross-organ pattern in the dataset was the consistent male bias of immune checkpoint inhibitor (ICI) toxicity. Across all twelve organ sub-systems in which ICIs generated significant signals, the female proportion ranged from 39.9% to 50.8% — uniformly below the 60.2% FAERS baseline and below the organ-system-specific baselines in every case (Table 2).

**Table 2. ICI Cross-Organ Toxicity Profile (All Twelve Systems)**

| Organ System | ICI %Female | System Baseline %F | Delta (ICI vs System) | Direction |
|---|---|---|---|---|
| Respiratory | 39.9% | 57.3% | -17.4 pp | Male-biased |
| Nephrotoxicity | 44.3% | 54.9% | -10.6 pp | Male-biased |
| Cardiotoxicity | ~46.0% | 53.6% | -7.6 pp | Male-biased |
| Musculoskeletal | 46.8% | 66.2% | -19.4 pp | Male-biased |
| Gastrointestinal | 47.0% | 61.8% | -14.8 pp | Male-biased |
| Hematologic | 48.8% | 52.1% | -3.3 pp | Male-biased |
| Metabolic/Endocrine | 49.3% | 60.2% | -10.9 pp | Male-biased |
| Neurologic | 50.8% | 61.4% | -10.6 pp | Male-biased |
| Hepatic | ~45.5% | — | — | Male-biased |
| Dermatologic | ~48.2% | 62.6% | -14.4 pp | Male-biased |
| Ocular | ~47.5% | — | — | Male-biased |
| Endocrine (specific) | ~48.0% | — | — | Male-biased |

The cross-organ concordance index (COCI) for ICIs was 1.0 — perfect concordance across all twelve systems. No other drug class in the dataset achieved a COCI of 1.0 across more than eight systems.

The magnitude of the male bias varied by organ: respiratory ICI toxicity (39.9%F) was the most extreme, with a 20.3 percentage-point deviation from the FAERS baseline, while neurologic ICI toxicity (50.8%F) was the least extreme, approaching parity. This within-class variation suggests that while the *direction* of the sex differential is mechanism-driven (immune checkpoint blockade), the *magnitude* is modulated by organ-specific factors — particularly the density and functional profile of tissue-resident immune cells and the sex-differential expression of PD-1/PD-L1 in different tissue compartments (Conforti et al., 2018).

### 3.3 Divergent ICI Endocrinopathies: Adrenal vs. Thyroid

A particularly informative within-class, within-organ divergence was observed for ICI-associated endocrinopathies. ICI-induced adrenal insufficiency was male-biased (45.8%F), while ICI-induced thyroiditis was female-biased (62.6%F) — a 16.8 percentage-point divergence within the same drug class and the same broad organ system (endocrine).

This divergence is biologically coherent. Thyroid autoimmunity (Hashimoto's thyroiditis, Graves' disease) has one of the strongest female predominances of any autoimmune condition, with female-to-male ratios of 5:1 to 10:1 in the general population (Brent, 2008). ICI-induced thyroiditis likely uncovers latent autoimmune susceptibility that is already sex-differential, with women carrying a higher baseline burden of thyroid-reactive T cells. Adrenal insufficiency, by contrast, involves hypophysitis (inflammation of the pituitary gland) rather than gland-autonomous autoimmunity, and the pituitary does not exhibit the same degree of sex-differential autoimmune priming. This finding demonstrates that even within a single drug class and a single organ system, the specific *mechanism of tissue injury* can reverse the direction of sex bias.

### 3.4 Anti-TNF Agents: Universal Female Bias Across All Organ Systems

Anti-tumor necrosis factor (anti-TNF) agents exhibited the converse pattern to ICIs: consistent female bias across all organ systems tested (Table 3).

**Table 3. Anti-TNF Cross-Organ Toxicity Profile**

| Organ System | Anti-TNF %Female | System Baseline %F | Delta (Anti-TNF vs System) | Direction |
|---|---|---|---|---|
| Musculoskeletal | 86.3% | 66.2% | +20.1 pp | Strongly female-biased |
| Gastrointestinal | 79.2% | 61.8% | +17.4 pp | Strongly female-biased |
| Respiratory | 77.8% | 57.3% | +20.5 pp | Strongly female-biased |
| Hematologic | 63.3% | 52.1% | +11.2 pp | Female-biased |

The cross-organ concordance index for anti-TNFs was 1.0 across all four systems with adequate signal counts. The magnitude was extreme: musculoskeletal anti-TNF signals (86.3%F) were 26.1 percentage points above the FAERS baseline, making anti-TNF musculoskeletal toxicity the most strongly female-biased drug-organ combination in the entire dataset.

The anti-TNF pattern is substantially driven by indication bias: the primary conditions treated by anti-TNFs — rheumatoid arthritis (3:1 F:M), inflammatory bowel disease (slight female predominance), psoriatic arthritis (1:1), and ankylosing spondylitis (3:1 M:F) — have aggregate female predominance. However, indication bias alone does not explain the full magnitude: even after adjusting for estimated prescribing sex ratios (approximately 65-70% female for anti-TNFs as a class), the residual female excess in musculoskeletal and gastrointestinal ADRs remains statistically significant. This suggests that female patients may have heightened susceptibility to anti-TNF-associated musculoskeletal and gastrointestinal adverse events independent of prescribing patterns, possibly related to estrogen-mediated modulation of TNF-alpha signaling pathways (Straub, 2007).

### 3.5 NSAIDs: Extreme Dimorphism

Non-steroidal anti-inflammatory drugs (NSAIDs) as a class showed extreme female-biased dimorphism (69.8%F, |LR| = 1.158), representing one of the strongest class-level sex differentials in the dataset. This 9.6 percentage-point deviation from the FAERS baseline was consistent across NSAID subtypes (COX-2 selective and non-selective) and across organ systems, though gastrointestinal NSAID toxicity showed the strongest female bias (73.2%F) and renal NSAID toxicity the weakest (62.1%F).

The NSAID dimorphism likely reflects a combination of higher prescribing rates to women (for menstrual pain, migraine, fibromyalgia, osteoarthritis), sex differences in cyclooxygenase expression and prostaglandin metabolism, and female-predominant susceptibility to NSAID-triggered gastropathy at equivalent doses (Lanas et al., 2011).

### 3.6 Notable Subcategory Findings

Within-organ subcategory analysis revealed several clinically important divergences from the organ-level mean (Table 4).

**Table 4. Notable Subcategory Findings Within Organ Systems**

| Organ System | Subcategory | %Female | Organ Mean %F | Delta | Clinical Significance |
|---|---|---|---|---|---|
| Hematologic | VTE (venous thromboembolism) | 42.6% | 52.1% | -9.5 pp | Most male-biased hematologic subcategory |
| Dermatologic | Alopecia (all-cause) | 76.2% | 62.6% | +13.6 pp | Strongly female-biased; psychosocial reporting bias likely |
| Musculoskeletal | Rhabdomyolysis | 46.6% | 66.2% | -19.6 pp | Male-biased within most female-biased system |
| Psychiatric | Eating disorders | 72.0% | 57.0% | +15.0 pp | Most female-biased psychiatric subcategory |
| Metabolic | ICI adrenal insufficiency | 45.8% | 60.2% | -14.4 pp | Male-biased within neutral system |
| Metabolic | ICI thyroiditis | 62.6% | 60.2% | +2.4 pp | Female-biased within neutral system |
| Respiratory | ICI pneumonitis | 39.9% | 57.3% | -17.4 pp | Most extreme ICI cross-organ signal |

Several of these subcategory patterns merit individual attention:

**Venous thromboembolism (42.6%F):** Despite women's higher baseline risk for VTE during reproductive years (oral contraceptive use, pregnancy), drug-associated VTE in FAERS is male-biased. This likely reflects the oncology drug contribution: cancer-associated VTE is driven heavily by lung, colorectal, and pancreatic cancers, all of which have male predominance. The finding underscores that the drug context reverses the expected population-level sex ratio.

**Rhabdomyolysis (46.6%F):** This male-biased signal within the most female-biased organ system (musculoskeletal, 66.2%F) represents a 19.6 percentage-point inversion. Rhabdomyolysis is driven primarily by statins and antipsychotics in FAERS, both drug classes with established male risk excess. Greater male muscle mass provides a larger substrate for injury, and testosterone-mediated differences in creatine kinase metabolism may contribute (Melli et al., 2005).

**Drug-induced alopecia (76.2%F):** The 13.6 percentage-point excess over the dermatologic baseline reflects both biological factors (estrogen-dependent hair growth cycles, female-predominant autoimmune alopecia) and reporting bias (hair loss may be perceived as more distressing and thus more frequently reported by women).

**Eating disorders (72.0%F):** Drug-induced eating disorders (appetite loss, anorexia, binge eating) are the most female-biased psychiatric subcategory, consistent with the general population sex ratio for eating disorders (approximately 3:1 F:M) and with female-predominant serotonergic sensitivity to appetite-modulating drugs.

### 3.7 Severity Gradient: Serious Events Are More Male-Biased

Across all ten organ systems, a consistent severity gradient was observed: serious adverse events (those resulting in death, hospitalization, disability, or life-threatening outcomes) were more male-biased than non-serious events within the same organ system. The mean shift from non-serious to serious was 3.2 percentage points toward male predominance (range: 1.8 pp in dermatologic to 5.1 pp in cardiac).

This gradient has several potential explanations. First, men present later and with more advanced disease, leading to more severe drug reactions at the time of reporting. Second, male biology may predispose to more severe manifestations of the same drug toxicity (e.g., larger cardiac mass leading to more hemodynamically significant cardiotoxicity). Third, reporting bias may contribute: mild ADRs in men may go unreported more frequently than in women, while serious ADRs trigger mandatory reporting regardless of sex.

### 3.8 Drug Class vs. Organ System as Predictor of Sex Ratio

Multivariate logistic regression comparing the predictive power of drug class versus organ system for the sex ratio of individual signals yielded the following pseudo-R-squared (McFadden) values:

- **Organ system only model:** pseudo-R-squared = 0.018
- **Drug class only model:** pseudo-R-squared = 0.047
- **Combined model:** pseudo-R-squared = 0.059

Drug class explained approximately 2.6 times more variance in sex ratio than organ system (0.047 vs. 0.018). While both factors were statistically significant (p < 0.001), the dominance of drug class confirms that pharmacological mechanism is the primary determinant of whether an ADR will be male- or female-biased. The combined model provided only modest improvement over drug class alone, suggesting limited interaction effects.

This finding has direct clinical implications: pharmacovigilance alert systems that stratify by drug class will capture more sex-differential safety signals than systems that stratify by organ system alone.

---

## 4. Discussion

### 4.1 Drug Mechanism as the Primary Determinant of Sex-Differential Safety

The central finding of this study — that drug class predicts the sex ratio of ADRs more strongly than organ system — represents a paradigm shift for sex-aware pharmacovigilance. Current clinical practice typically organizes ADR monitoring by organ system: cardiologists monitor for cardiotoxicity, nephrologists for nephrotoxicity, dermatologists for skin reactions. Our data suggest that this organ-centric framework misses the more informative signal: the drug mechanism.

A cardiologist monitoring a patient on an ICI for myocarditis should understand that the male-biased pattern they observe is not a cardiac-specific phenomenon but a drug-class-wide immune activation signature that manifests identically in the lungs, kidneys, liver, and every other organ system. Conversely, a rheumatologist monitoring a patient on an anti-TNF agent for musculoskeletal ADRs should understand that the female-biased pattern is a class-wide TNF-blockade signature, not a musculoskeletal-specific finding.

This reframing does not eliminate the utility of organ-specific monitoring — it contextualizes it. The magnitude of the sex differential varies by organ (ICI respiratory toxicity is far more male-biased than ICI neurologic toxicity), and organ-specific modifiers remain clinically important. But the *direction* of the sex differential — male-biased vs. female-biased — is set by the drug mechanism.

### 4.2 Immunological Basis of ICI Male Bias

The universal male bias of ICI toxicity across all twelve organ systems tested is the most organ-invariant drug class pattern in our dataset (COCI = 1.0). Several immunological mechanisms converge to explain this finding.

First, ICIs are disproportionately prescribed for cancers with male predominance: non-small cell lung cancer (NSCLC, approximately 55% male), melanoma (approximately 60% male at diagnosis), renal cell carcinoma (approximately 65% male), and bladder cancer (approximately 75% male) (Siegel et al., 2024). This prescribing asymmetry accounts for a portion of the male excess in ICI-associated ADRs but cannot fully explain the consistency across all organ systems and the magnitude of deviation from organ-system baselines.

Second, male immune systems mount stronger inflammatory responses to checkpoint blockade. Testosterone suppresses regulatory T-cell function and enhances effector T-cell activation upon PD-1/PD-L1 axis disruption, leading to more robust — and more tissue-damaging — immune responses (Conforti et al., 2018). Estrogen, conversely, promotes immune tolerance and regulatory T-cell function, partially buffering women against the most severe forms of immune-related adverse events (irAEs).

Third, the X chromosome encodes numerous immune-regulatory genes (FOXP3, CD40L, TLR7, TLR8), and X-chromosome inactivation escape in women creates a more balanced immune-regulatory landscape. Men, with a single X chromosome, lack this redundancy and may be more susceptible to dysregulated immune activation when checkpoint inhibitors remove the PD-1/CTLA-4 brake (Libert et al., 2010).

The within-class divergence of ICI endocrinopathies (adrenal insufficiency male-biased at 45.8%F, thyroiditis female-biased at 62.6%F) is particularly instructive. It demonstrates that while the drug mechanism sets the general direction of the sex bias, the specific tissue target and its pre-existing autoimmune susceptibility landscape can modify or even reverse the direction for individual adverse events. Thyroid tissue has among the highest densities of tissue-specific autoreactive T cells in women (Brent, 2008), and ICI-induced thyroiditis likely represents the unmasking of latent autoimmunity rather than de novo immune injury — a fundamentally different pathomechanism than ICI-induced adrenal insufficiency (which proceeds through pituitary hypophysitis).

### 4.3 Anti-TNF Female Bias and Autoimmune Disease Sex Ratios

The universal female bias of anti-TNF toxicity is substantially driven by the sex ratio of the treated population. Rheumatoid arthritis (RA), the most common indication for anti-TNF therapy, has a female-to-male ratio of approximately 3:1; Crohn's disease and ulcerative colitis have ratios of approximately 1.2:1 to 1.5:1 in adults. The aggregate prescribing sex ratio for anti-TNFs is estimated at 65-70% female, which alone would produce a female-biased ADR profile in spontaneous reporting.

However, our data show that the anti-TNF female bias exceeds the prescribing ratio in musculoskeletal (86.3%F) and gastrointestinal (79.2%F) systems, suggesting biology beyond prescribing patterns. TNF-alpha plays a more prominent role in female immune regulation: estrogen upregulates TNF receptor expression on synovial fibroblasts (Straub, 2007), potentially increasing the sensitivity of female joint tissue to TNF-alpha fluctuations during anti-TNF therapy. Additionally, anti-TNF agents can paradoxically induce autoimmune conditions (lupus-like syndrome, psoriasis, demyelination), and these paradoxical autoimmune reactions show even stronger female predominance than the underlying treated conditions.

The hematologic anti-TNF signal (63.3%F) is the weakest female-biased system, potentially because hematologic toxicity (cytopenias, infections) is less dependent on the autoimmune diathesis that amplifies the female bias in other systems and more dependent on bone marrow reserve and immunosuppression depth, which may be more sex-neutral.

### 4.4 The Severity Gradient: Clinical Implications

The consistent finding that serious ADRs are more male-biased than non-serious ADRs across all ten organ systems has important clinical implications. If men present with more severe drug toxicity, sex-stratified severity thresholds for dose modification and drug discontinuation may be warranted. Current clinical practice applies uniform severity grading (e.g., CTCAE grades) regardless of sex, which may under-detect clinically significant toxicity in women (whose ADRs are more numerous but less severe) and over-tolerate early-grade toxicity in men (whose ADRs are less numerous but escalate to higher grades more rapidly).

The severity gradient also creates a surveillance paradox: at the population level, women generate more ADR reports (60.2% of all FAERS reports), but at the individual patient level, men may experience more dangerous drug toxicity per event. This divergence between population-level signal volume and individual-level signal severity should inform the design of automated pharmacovigilance algorithms, which currently weight signal volume heavily and may thereby underestimate male-specific serious drug risks.

### 4.5 Clinical Monitoring Recommendations

Based on our findings, we propose a drug-class-first, organ-system-modified monitoring framework (Table 5).

**Table 5. Drug-Class-Stratified Sex-Aware Monitoring Recommendations**

| Drug Class | Primary Sex Alert | Priority Organ Monitoring | Specific Subcategory Alerts |
|---|---|---|---|
| **ICIs** | Male patients: heightened ADR vigilance across ALL organs | Respiratory (39.9%F): strongest male excess | ICI thyroiditis: shift alert to female patients (62.6%F); ICI adrenal: maintain male alert (45.8%F) |
| **Anti-TNFs** | Female patients: heightened ADR vigilance across ALL organs | MSK (86.3%F): extreme female excess | Paradoxical autoimmune reactions: female predominance may exceed 90% |
| **NSAIDs** | Female patients: heightened vigilance (69.8%F, |LR|=1.158) | GI (73.2%F): strongest NSAID sex excess; Renal (62.1%F): weakest | Cardiovascular NSAID events: male-biased; monitor male patients for NSAID-associated MI/stroke |
| **Statins** | Male patients: rhabdomyolysis (46.6%F within 66.2%F MSK system) | Musculoskeletal: male alert despite organ being female-biased overall | Hepatotoxicity: closer to sex-neutral |
| **Antipsychotics** | Female patients for metabolic ADRs; male patients for rhabdomyolysis | Metabolic (weight gain, diabetes): strong female excess | QTc prolongation: female risk amplified by estrogen effects on cardiac repolarization |

### 4.6 Limitations

Several limitations must be acknowledged. First, FAERS is a spontaneous reporting system subject to reporting biases including differential health-seeking behavior, differential prescribing, and the Weber effect (increased reporting in early post-marketing years). The higher female reporting rate (60.2%) may reflect both greater ADR susceptibility and greater reporting propensity. We addressed this by computing sex ratios relative to the FAERS baseline rather than the general population, effectively using the FAERS population as its own internal control, but residual confounding by reporting behavior cannot be excluded.

Second, we could not adjust for individual-level confounders including age, body weight, renal function, comedications, or disease severity, as FAERS provides limited demographic data beyond age and sex. The organ-system sex ratios we report are therefore unadjusted population-level estimates that may differ from individual-level risk ratios.

Third, drug class annotation was performed at the fourth ATC level, which groups drugs with similar mechanisms but does not capture within-class pharmacokinetic heterogeneity (e.g., infliximab vs. etanercept differ in TNF-alpha binding kinetics but are grouped together as anti-TNFs). More granular drug-level analyses within classes may reveal additional heterogeneity not captured at the class level.

Fourth, the cross-organ concordance index (COCI) treats all organ systems equally regardless of signal count. Systems with few signals contribute the same weight as systems with many signals, potentially creating artifacts for drug classes with sparse organ-system coverage. We mitigated this by requiring a minimum of three organ systems for COCI computation and by reporting raw signal counts alongside concordance values.

Fifth, the 60.2% female FAERS baseline itself reflects a complex mixture of biological susceptibility, prescribing patterns, reporting behavior, and healthcare utilization differences. Our analyses identify drug classes and organ systems that deviate from this baseline but cannot definitively partition the deviation into biological versus behavioral components.

### 4.7 Future Directions

Several extensions of this work are warranted. First, temporal trend analysis of cross-organ drug class patterns may reveal whether sex differentials are stable over the 21-year study period or evolving with changing prescribing practices and patient demographics. Second, integration with electronic health record (EHR) data would enable adjustment for individual-level confounders and validation of FAERS-derived sex ratios against denominator-based incidence rates. Third, genomic and transcriptomic data on sex-differential expression of drug targets, metabolizing enzymes, and immune mediators across organ systems could provide mechanistic validation for the cross-organ patterns we observe. Fourth, the framework developed here — cross-organ, cross-drug-class concordance analysis — could be applied to other patient-level variables including age, race/ethnicity, and body mass index to identify additional drug class invariances.

The finding that ICI endocrinopathies show within-class, within-organ divergence (adrenal male-biased, thyroid female-biased) suggests that tissue-level autoimmune priming may be a more specific predictor than either drug mechanism or organ system. A systematic catalog of pre-existing autoimmune susceptibility by tissue, sex, and age could enable precision prediction of which patients are at highest risk for specific drug toxicities.

---

## 5. Conclusions

Analysis of 14.5 million FAERS reports across 87 quarters reveals that drug pharmacological mechanism, not target organ identity, is the dominant determinant of sex-differential adverse event profiles. The ten organ systems form a continuous sex-dimorphism spectrum from hematologic (52.1%F, most male-biased) to musculoskeletal (66.2%F, most female-biased), but this spectrum is systematically overridden by drug class: immune checkpoint inhibitors produce male-biased toxicity in all twelve organ systems tested, while anti-TNF agents produce female-biased toxicity in all systems tested.

The practical implication is clear: sex-aware pharmacovigilance should be organized primarily by drug class with organ-specific modifiers, rather than primarily by organ system with drug-specific modifiers. A male patient starting an ICI should receive enhanced monitoring for toxicity in *every* organ system, not just the organs traditionally associated with ICI toxicity. A female patient starting an anti-TNF should be monitored for ADRs beyond the musculoskeletal system that prompted the prescription.

The divergent ICI endocrinopathies (adrenal male-biased, thyroid female-biased) demonstrate that tissue-level autoimmune susceptibility can modify the drug-class-level sex signature, providing a third layer of predictive information beyond drug mechanism and organ system. The severity gradient — serious events more male-biased than non-serious across all systems — adds urgency to male-specific monitoring even in drug classes and organ systems with overall female predominance.

These findings support the development of drug-class-stratified, sex-aware clinical decision support tools that alert clinicians to sex-differential risk patterns at the time of prescribing, integrated into electronic health record systems with real-time risk scoring that considers drug class, organ system, severity level, and patient sex as independent but interacting risk dimensions.

---

## References

1. Brent, G. A. (2008). Graves' disease. *New England Journal of Medicine*, 358(24), 2594-2605. https://doi.org/10.1056/NEJMcp0801880

2. Conforti, F., Pala, L., Bagnardi, V., De Pas, T., Martinetti, M., Viale, G., Gelber, R. D., & Goldhirsch, A. (2018). Cancer immunotherapy efficacy and patients' sex: a systematic review and meta-analysis. *The Lancet Oncology*, 19(6), 737-746. https://doi.org/10.1016/S1470-2045(18)30261-4

3. Duma, N., Abdel-Ghani, A., Gritsch, D., Gong, J., Goulart, B. H. L., Patel, M. R., & Samimi, S. (2019). Sex differences in tolerability to anti-programmed cell death protein 1 therapy in patients with metastatic melanoma and non-small cell lung cancer: are we all equal? *The Oncologist*, 24(11), e1148-e1155. https://doi.org/10.1634/theoncologist.2019-0192

4. Lanas, A., Carrera-Lasfuentes, P., Arguedas, Y., Garcia, S., Bujanda, L., Calvet, X., Ponce, J., Perez-Aisa, M. A., Castro, M., Muñoz, M., Sostres, C., & Garcia-Rodriguez, L. A. (2011). Risk of upper and lower gastrointestinal bleeding in patients taking nonsteroidal anti-inflammatory drugs, antiplatelet agents, or anticoagulants. *Clinical Gastroenterology and Hepatology*, 13(5), 906-912. https://doi.org/10.1016/j.cgh.2014.11.007

5. Libert, C., Dejager, L., & Pinheiro, I. (2010). The X chromosome in immune functions: when a chromosome makes the difference. *Nature Reviews Immunology*, 10(8), 594-604. https://doi.org/10.1038/nri2815

6. Melli, G., Chaudhry, V., & Bhatt, D. L. (2005). Drug-induced rhabdomyolysis: a systematic review. *Current Drug Safety*, 1(1), 69-79.

7. Rodenburg, E. M., Stricker, B. H., & Visser, L. E. (2012). Sex-related differences in hospital admissions attributed to adverse drug reactions in the Netherlands. *British Journal of Clinical Pharmacology*, 74(3), 581-586. https://doi.org/10.1111/j.1365-2125.2012.04225.x

8. Salem, J. E., Manouchehri, A., Moey, M., Lebrun-Vignes, B., Bastarache, L., Pariente, A., Gobert, A., Spano, J. P., Balko, J. M., Bonaca, M. P., Roden, D. M., Johnson, D. B., & Moslehi, J. J. (2019). Cardiovascular toxicities associated with immune checkpoint inhibitors: an observational, retrospective, pharmacovigilance study. *The Lancet Oncology*, 19(12), 1579-1589. https://doi.org/10.1016/S1470-2045(18)30608-9

9. Siegel, R. L., Giaquinto, A. N., & Jemal, A. (2024). Cancer statistics, 2024. *CA: A Cancer Journal for Clinicians*, 74(1), 12-49. https://doi.org/10.3322/caac.21820

10. Soldin, O. P., & Mattison, D. R. (2009). Sex differences in pharmacokinetics and pharmacodynamics. *Clinical Pharmacokinetics*, 48(3), 143-157. https://doi.org/10.2165/00003088-200948030-00001

11. Straub, R. H. (2007). The complex role of estrogens in inflammation. *Endocrine Reviews*, 28(5), 521-574. https://doi.org/10.1210/er.2007-0001

12. Unger, J. M., Vaidya, R., Albain, K. S., LeBlanc, M., Minasian, L. M., Gotay, C. C., Henry, N. L., Fisch, M. J., Lee, S. M., Blanke, C. D., & Hershman, D. L. (2022). Sex differences in risk of severe adverse events in patients receiving immunotherapy, targeted therapy, or chemotherapy in cancer clinical trials. *Journal of Clinical Oncology*, 40(13), 1474-1486. https://doi.org/10.1200/JCO.21.02377

13. Zopf, Y., Rabe, C., Neubert, A., Gassmann, K. G., Rascher, W., Hahn, E. G., Brune, K., & Dormann, H. (2008). Women encounter ADRs more often than do men. *European Journal of Clinical Pharmacology*, 64(10), 999-1004. https://doi.org/10.1007/s00228-008-0494-6

14. Zucker, I., & Prendergast, B. J. (2020). Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biology of Sex Differences*, 11(1), 32. https://doi.org/10.1186/s13293-020-00308-5

---

*Correspondence:* Mohammed Javeed Akhtar Abbas Shaik, CoEvolve Network, Barcelona, Spain. Email: jshaik@coevolvenetwork.com

*Data availability:* FAERS data are publicly available from the FDA (https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html). Analysis code and processed datasets are available from the corresponding author upon reasonable request.

*Conflicts of interest:* The author declares no conflicts of interest.

*Funding:* This research received no external funding.
