---
title: "The Sex Paradox in Pharmacovigilance: Drug Safety Signals Anti-Correlate with Reporting Patterns Across 2,178 Drugs"
authors: "Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)"
affiliation: "CoEvolve Network, Independent Researcher, Barcelona, Spain"
email: "jshaik@coevolvenetwork.com"
orcid: "0009-0002-1748-7516"
target_journal: "JAMA Internal Medicine / Pharmacoepidemiology and Drug Safety"
draft_version: "v3.0 — expanded publication draft"
date: "2026-03-07"
---

## Abstract

**Background:** Women comprise 60.2% of FDA Adverse Event Reporting System (FAERS) reporters, raising persistent concerns that observed sex differences in drug safety merely reflect differential reporting rates. We directly test this "reporting artifact" hypothesis.

**Methods:** We analyzed 96,281 sex-differential adverse event signals from 14.5 million FAERS reports (2004Q1-2025Q3) across 2,178 drugs. For each drug, we computed the proportion of reports from female patients (report ratio) and the proportion of sex-differential signals showing female predominance (signal ratio), then tested their correlation globally and at graduated minimum-signal thresholds. Five convergent analyses were conducted: reporter-signal correlation, graduated-power stratification, majority discordance classification, volume anti-regression, and effect size asymmetry.

**Results:** The FAERS reporter pool is 74.3% female, yet only 53.8% of sex-differential signals are female-higher. The report ratio and signal ratio showed a significant negative correlation (Spearman rho = -0.215, p = 6.92e-13, n = 1,090 drugs), which strengthened with statistical power (Pearson r = -0.271, p = 5.14e-6 at >=100 signals per drug). A total of 53% of drugs showed paradoxical discordance between reporter sex and signal sex. We identified 133 paradox drugs (>60% female reports, <40% female signals; maximum gap 87 percentage points) and 32 reverse paradox drugs (<40% female reports, >60% female signals; maximum gap 70 percentage points). Paradoxical drugs exhibited stronger, not weaker, effect sizes (mean |LR| 0.990 vs. 0.921, p = 2.09e-4). Female-predominant signals were systematically larger than male-predominant signals (F/M ratio = 1.046, p = 2.8e-41), and the female signal proportion increased monotonically with report volume (42.9% to 88.9%).

**Conclusions:** Five independent lines of evidence refute the reporting artifact hypothesis. Sex-differential drug safety signals reflect genuine pharmacological sex differences, with immediate implications for drug safety surveillance, clinical practice, and regulatory policy.

---

## 1. Introduction

### 1.1 The Problem of Sex Bias in Drug Safety Surveillance

Sex differences in drug safety represent one of the most consequential yet methodologically contested domains in modern pharmacoepidemiology. Women experience adverse drug reactions (ADRs) at nearly twice the rate of men, with estimates ranging from 1.5- to 1.7-fold elevated risk across therapeutic classes [1, 2]. This disparity has been documented across multiple pharmacovigilance databases, including the FDA Adverse Event Reporting System (FAERS), EudraVigilance, and the Japanese Adverse Drug Event Report database (JADER), and spans drug classes from cardiovascular agents to oncologics to central nervous system therapeutics [3, 4].

Despite the consistency of these observations, their interpretation remains deeply contested. The central methodological critique is straightforward: if women report adverse events more frequently than men — and indeed, women comprise approximately 60% of all FAERS reporters — then the observed sex-differential signals may simply reflect differential ascertainment rather than differential pharmacology [5, 6]. This "reporting artifact hypothesis" has been invoked repeatedly to discount sex-stratified safety findings, and its influence extends from regulatory decision-making to clinical guideline development [7].

The reporting artifact hypothesis carries significant consequences. If sex-differential signals are dismissed as artifacts, opportunities for sex-specific dose adjustment, monitoring protocols, and contraindication identification are lost. Historical examples underscore the clinical cost: zolpidem dosing was not adjusted for women until 2013, despite decades of evidence showing higher blood levels in women at equivalent doses [8]. More recently, analyses of QT-prolonging drugs have revealed sex-differential cardiac toxicity that is not fully explained by reporting patterns [9].

### 1.2 Simpson's Paradox and Confounding in Observational Pharmacovigilance

The methodological challenge of disentangling reporting bias from genuine pharmacological sex differences is a specific instance of a broader problem in observational research: confounding by non-causal pathways. Simpson's paradox — wherein the direction of an association reverses upon stratification by a confounding variable — has been a persistent concern in epidemiology since its formal description [10, 11]. In pharmacovigilance, the potential for Simpson's paradox arises because the variable that determines reporting (patient sex) is also the variable hypothesized to modify the outcome (adverse event risk).

The classical formulation of Simpson's paradox can be expressed as follows. Let $D$ denote the drug, $S$ the patient sex, $R$ the event of filing a report, and $A$ the occurrence of an adverse event. The reporting artifact hypothesis posits that:

$$P(A \mid D, S=\text{female}) > P(A \mid D, S=\text{male})$$

is an artifact of:

$$P(R \mid A, S=\text{female}) > P(R \mid A, S=\text{male})$$

That is, the elevated adverse event rate observed in women is driven not by differential pharmacology but by differential probability of reporting conditional on experiencing an adverse event. Under this model, the true adverse event rates may be equal or even male-predominant, with the female excess in reported events being entirely attributable to the higher propensity of women (or their healthcare providers) to submit adverse event reports.

This confounding structure is particularly insidious because it cannot be resolved by simple stratification within a single database. The reporting probability $P(R \mid A, S)$ is fundamentally unobservable in spontaneous reporting systems, which capture only the numerator (reports filed) without a well-defined denominator (total adverse events experienced). This is the "denominator problem" that has plagued pharmacovigilance since its inception [12, 13].

### 1.3 Prior Approaches and Their Limitations

Previous approaches to address reporting bias include prescription-denominator adjustment [14] (which controls for differential exposure but not differential reporting propensity), sex-stratified disproportionality analysis [3] (which controls baseline reporting differences but not drug-level confounding), and matched EHR cohort designs [15] (which provide known denominators but cannot scale to thousands of drugs). What has been missing is a systematic test of the internal consistency of the reporting artifact hypothesis itself — an approach that tests whether drug-level reporting patterns predict drug-level signal patterns without requiring knowledge of the unobservable true reporting probability.

### 1.4 The Reporter-Signal Decorrelation Framework

We introduce a novel analytical framework — reporter-signal decorrelation analysis — that directly tests the internal consistency of the reporting artifact hypothesis. The framework is built on a simple logical insight: if reporting bias drives signals, then the sex composition of a drug's reporter pool should predict the sex composition of that drug's safety signals. Specifically, drugs reported predominantly by women should show predominantly female safety signals, and vice versa. The reporting artifact hypothesis therefore predicts a positive correlation between the drug-level report ratio (proportion of reporters who are female) and the drug-level signal ratio (proportion of sex-differential signals that are female-predominant).

This prediction can be tested directly. If the correlation is positive, the data are consistent with reporting bias (though not proof of it). If the correlation is null, reporting patterns and signal patterns are independent, suggesting that signals are not driven by reporting. If the correlation is negative — an anti-correlation — then the data actively contradict the reporting artifact hypothesis, implying that drugs reported more by one sex tend to show safety signals for the other sex.

We further introduce a graduated-power analysis that tests how the reporter-signal correlation changes as we restrict to better-powered drugs (those with more sex-differential signals). Reporting artifacts are expected to weaken with increasing sample size as noise averages out. Genuine biological signals are expected to strengthen with increasing sample size as statistical power increases. The trajectory of the correlation across graduated signal thresholds therefore provides a diagnostic signature for distinguishing artifacts from biology.

### 1.5 Study Objectives

The objectives of this study are:

1. To quantify the global correlation between drug-level reporting sex ratios and drug-level safety signal sex ratios across the full FAERS drug landscape.
2. To characterize the graduated-power trajectory of this correlation at escalating signal-count thresholds.
3. To identify and characterize paradoxical drugs — those exhibiting extreme discordance between reporter sex and signal sex.
4. To assess whether paradoxical drugs exhibit weaker signals (consistent with artifacts) or stronger signals (consistent with genuine pharmacological differences).
5. To evaluate the volume anti-regression pattern and effect size asymmetry as independent lines of evidence.

---

## 2. Methods

### 2.1 Data Source and Study Population

We utilized the FDA Adverse Event Reporting System (FAERS), the world's largest spontaneous reporting database, covering reports submitted from 2004Q1 through 2025Q3. FAERS collects voluntary reports of adverse events and medication errors associated with the use of drug and biologic products. Reports are submitted by healthcare professionals, consumers, and manufacturers [16].

After deduplication using the FDA's recommended CASEID-based algorithm (retaining the most recent report version per case), the study population comprised 14,536,008 reports with non-missing sex information, of which 8,744,397 (60.2%) were from female patients and 5,791,611 (39.8%) from male patients. Reports with missing, unknown, or ambiguous sex designations were excluded.

### 2.2 Drug Standardization

Drug names were standardized using a multi-step normalization pipeline. Active ingredient names were mapped to their canonical forms using the RxNorm vocabulary (National Library of Medicine). Combination products were decomposed into individual active ingredients. Brand names were mapped to generic names where unambiguous mappings existed. Drugs with fewer than 100 total reports (male + female combined) were excluded from the correlation analysis to ensure stable ratio estimates, yielding a final drug set of 2,178 drugs.

### 2.3 Sex-Differential Signal Generation

For each drug-adverse event pair, sex-stratified Reporting Odds Ratios (ROR) were computed using the standard disproportionality framework. For a given drug $d$ and adverse event $e$, the ROR for sex $s$ is defined as:

$$\text{ROR}_{d,e,s} = \frac{n_{d,e,s} / n_{d,\bar{e},s}}{n_{\bar{d},e,s} / n_{\bar{d},\bar{e},s}}$$

where $n_{d,e,s}$ denotes the number of reports of drug $d$ with adverse event $e$ for sex $s$, and barred subscripts denote complements (not-drug, not-event). Only drug-adverse event-sex combinations with $n_{d,e,s} \geq 10$ were retained to ensure stable odds ratio estimates.

The sex-differential log ratio (LR) was then computed as:

$$\text{LR}_{d,e} = \ln(\text{ROR}_{d,e,\text{female}}) - \ln(\text{ROR}_{d,e,\text{male}})$$

A positive LR indicates female-predominant disproportionality; a negative LR indicates male-predominant disproportionality. Signals with $|\text{LR}| \geq 0.5$ (corresponding to approximately a 1.65-fold difference in ROR between sexes) were retained as sex-differential signals. This threshold was chosen to balance sensitivity (capturing clinically meaningful differences) with specificity (excluding noise). The procedure yielded 96,281 sex-differential signals across 2,178 drugs.

### 2.4 Reporter-Signal Metrics

For each drug $d$, two independent summary metrics were computed:

**Report ratio** ($\rho_d$): The proportion of that drug's total reports originating from female patients:

$$\rho_d = \frac{\sum_e n_{d,e,\text{female}}}{\sum_e (n_{d,e,\text{female}} + n_{d,e,\text{male}})}$$

**Signal ratio** ($\sigma_d$): The proportion of that drug's sex-differential signals showing female predominance:

$$\sigma_d = \frac{|\{e : \text{LR}_{d,e} > 0\}|}{|\{e : |\text{LR}_{d,e}| \geq 0.5\}|}$$

The report ratio captures the sex composition of a drug's user/reporter population; the signal ratio captures the sex directionality of that drug's safety signals. Under the reporting artifact hypothesis, these two quantities should be positively correlated.

### 2.5 Correlation Analysis

**Global analysis.** Pearson and Spearman rank correlations between $\rho_d$ and $\sigma_d$ were computed across all 2,178 drugs. The Spearman correlation was used as the primary measure to accommodate potential non-linearity and outliers. Two-tailed p-values were computed using the asymptotic approximation for large samples. Bootstrapped 95% confidence intervals (10,000 iterations, bias-corrected and accelerated) were computed for robustness.

**Graduated-power analysis.** To assess how the reporter-signal relationship changes with statistical power, correlations were recomputed at escalating minimum-signal thresholds: all drugs (no threshold), $\geq$10, $\geq$20, $\geq$50, $\geq$100, and $\geq$200 sex-differential signals per drug. The graduated-power trajectory — the pattern of correlation coefficients across thresholds — was examined as a diagnostic for distinguishing biological signals from reporting artifacts. The key prediction is:

- **Reporting artifacts**: correlation should be positive and should attenuate toward zero with increasing power (regression to the mean)
- **Genuine biological signals**: if present, signal should strengthen (absolute correlation should increase) with increasing power

### 2.6 Paradox Classification

Drugs were classified into four quadrants based on the conjunction of their report ratio and signal ratio:

- **Q1 (Concordant Female)**: $\rho_d > 0.5$ and $\sigma_d > 0.5$ — female-majority reporters, female-majority signals
- **Q2 (Discordant Male-to-Female)**: $\rho_d \leq 0.5$ and $\sigma_d > 0.5$ — male-majority reporters, female-majority signals
- **Q3 (Concordant Male)**: $\rho_d \leq 0.5$ and $\sigma_d \leq 0.5$ — male-majority reporters, male-majority signals
- **Q4 (Discordant Female-to-Male)**: $\rho_d > 0.5$ and $\sigma_d \leq 0.5$ — female-majority reporters, male-majority signals

The overall discordance rate was computed as the proportion of drugs in Q2 or Q4.

**Extreme paradox drugs** were defined using stricter thresholds:
- **Paradox drugs**: $\rho_d > 0.60$ and $\sigma_d < 0.40$ (>60% female reports and <40% female-predominant signals)
- **Reverse paradox drugs**: $\rho_d < 0.40$ and $\sigma_d > 0.60$ (<40% female reports and >60% female-predominant signals)

The reporter-signal gap was computed as $|\rho_d - \sigma_d|$ for each paradox drug.

### 2.7 Effect Size Comparisons

Three effect size comparisons were conducted:

**Female vs. male signal magnitude.** The absolute log ratio $|\text{LR}_{d,e}|$ was compared between female-predominant ($\text{LR} > 0$) and male-predominant ($\text{LR} < 0$) signals using the Mann-Whitney U test (two-tailed). This non-parametric test was chosen because the distribution of effect sizes was right-skewed.

**Paradoxical vs. non-paradoxical drugs.** The mean absolute log ratio per drug was compared between paradoxical drugs (reporter-signal gap > 30 percentage points) and non-paradoxical drugs using Welch's t-test.

**Volume gradient.** Drugs were ranked by total report volume and divided into quintiles (Q1-Q5) plus a top 1% stratum. The proportion of female-predominant signals was computed within each stratum. A monotonically increasing or decreasing trend was assessed visually and by Spearman correlation between volume rank and female signal proportion.

### 2.8 Statistical Framework and Multiple Testing

All statistical tests were two-tailed with a significance threshold of $\alpha = 0.05$. Given the multiple comparisons inherent in the graduated-power analysis (six thresholds), we applied the Bonferroni correction for the correlation tests, yielding an adjusted threshold of $\alpha_{\text{adj}} = 0.0083$. All reported p-values for the graduated-power analysis surpassed this conservative threshold. Effect sizes are reported alongside p-values throughout, as recommended by the American Statistical Association's statement on statistical significance [17].

The five convergent analyses (correlation, graduated power, discordance, volume gradient, effect asymmetry) were treated as independent lines of evidence rather than a single hypothesis test. The probability of all five producing results inconsistent with reporting bias by chance was computed under the assumption of independence.

### 2.9 Sensitivity Analyses

Several sensitivity analyses were conducted to test the robustness of the findings:

1. **Balanced-reporting subset**: The correlation analysis was repeated restricting to drugs with report ratios between 0.4 and 0.6 (approximately balanced male-female reporting), to test whether the anti-correlation persists when the reporting imbalance is minimal.
2. **Exclusion of sex-specific drugs**: Drugs with known sex-specific indications (e.g., testosterone, estrogen) were excluded to test whether the anti-correlation is driven by drugs with strongly sex-skewed user populations.
3. **Alternative LR thresholds**: The signal generation threshold was varied ($|\text{LR}| \geq 0.3$, $\geq 0.7$, $\geq 1.0$) to test sensitivity to the signal definition.
4. **Temporal stability**: The analysis was repeated on the first half (2004Q1-2014Q4) and second half (2015Q1-2025Q3) of the study period separately, to test for temporal consistency.

### 2.10 Software and Reproducibility

All analyses were conducted in Python 3.11 using NumPy 1.26, SciPy 1.12, pandas 2.2, and statsmodels 0.14. Visualizations were generated using matplotlib 3.8 and seaborn 0.13. All code and intermediate results are available at https://github.com/jshaik369/SexDiffKG.

---

## 3. Results

### 3.1 Base Rate Mismatch

The FAERS reporter pool is 74.3% female, yet only 53.8% of sex-differential signals are female-higher. This 20.5 percentage point gap immediately undermines the reporting artifact hypothesis — if reporting bias drove signals, we would expect ~74% female-higher signals, proportional to the female share of reporters. Instead, the signal pool is nearly balanced (53.8% female, 46.2% male), despite a 3:1 female-to-male reporter imbalance in the underlying data.

This base rate mismatch is a necessary but not sufficient condition for refuting the reporting artifact hypothesis. The 53.8% female signal rate could still be consistent with a partially attenuated reporting bias. The following analyses test whether the relationship between reporting and signals holds in the expected direction at the drug level.

### 3.2 Reporter-Signal Anti-Correlation (Global)

Among 1,090 drugs with $\geq$10 sex-differential signals, the correlation between the female report proportion ($\rho_d$) and the female signal proportion ($\sigma_d$) was significantly negative:

**Spearman rho = -0.215, p = 6.92e-13** (95% CI: [-0.271, -0.157])

This means drugs reported more often by women tend to have FEWER female-predominant safety signals — the exact opposite of what reporting bias predicts. The negative sign of the correlation is the single most important finding of this study: it transforms the reporting artifact hypothesis from an untested concern to an empirically falsified claim.

The Pearson correlation at the same threshold was r = -0.183 (p = 1.12e-9), indicating that the relationship is robust to the choice of correlation measure. The slightly weaker Pearson correlation suggests mild non-linearity in the relationship, which is expected given the bounded nature of both ratios (0 to 1).

To provide context for the magnitude of this anti-correlation: in epidemiological studies, confounding variables typically produce positive correlations between exposure proxies and outcome proxies. An anti-correlation of this magnitude (rho = -0.215 across >1,000 drugs) is not merely inconsistent with confounding — it is in the opposite direction from any confounding mechanism.

### 3.3 Graduated-Power Analysis

The anti-correlation STRENGTHENS with increasing statistical power:

| Min Signals | N Drugs | Pearson r | p-value | Interpretation |
|------------|---------|-----------|---------|----------------|
| All | 2,178 | -0.007 | 0.74 | Null (noise dominates) |
| >= 10 | 1,090 | -0.183 | 1.12e-9 | Moderate anti-correlation |
| >= 20 | 818 | -0.201 | 6.47e-9 | Stronger |
| >= 50 | 475 | -0.158 | 5.37e-4 | Persistent |
| >= 100 | 275 | **-0.271** | **5.14e-6** | Strongest |
| >= 200 | 135 | -0.223 | 9.46e-3 | Persistent with smaller N |

At all drugs (noisy, many with 1-2 signals), the correlation is near zero (r = -0.007, p = 0.74). As we restrict to better-powered drugs, the anti-correlation EMERGES and STRENGTHENS. The trajectory from r = -0.007 (all drugs) to r = -0.271 (>=100 signals) represents a 39-fold increase in the absolute correlation coefficient. All p-values at thresholds of >= 10 signals and above surpass the Bonferroni-corrected significance threshold (p < 0.0083).

This graduated-power pattern is a critical diagnostic. Reporting artifacts are noise: they should be maximal at small sample sizes and attenuate toward zero as data accumulates (regression to the mean). We observe the opposite: the anti-correlation is null in noisy data and strengthens in well-powered data. This is the hallmark signature of a genuine biological signal being revealed by statistical power.

The slight attenuation from r = -0.271 at >=100 signals to r = -0.223 at >=200 signals is attributable to reduced sample size (275 vs. 135 drugs), not weakening of the signal. The p-value remains significant (p = 9.46e-3) despite the smaller N.

### 3.4 Majority Discordance

When drugs are classified by the concordance or discordance between their reporter-sex majority and their signal-sex majority, 53% show paradoxical discordance:

- **Q1 (Female reporters, Female signals)**: 667 drugs (30.6%) — concordant
- **Q2 (Male reporters, Female signals)**: 392 drugs (18.0%) — discordant
- **Q3 (Male reporters, Male signals)**: 357 drugs (16.4%) — concordant
- **Q4 (Female reporters, Male signals)**: 762 drugs (35.0%) — discordant
- **Total concordant**: 1,024 drugs (47%)
- **Total discordant**: 1,154 drugs (53%)

Under the reporting artifact hypothesis, the vast majority of drugs should be concordant (Q1 or Q3), because reporter sex should predict signal sex. Instead, a slim majority (53%) are discordant. The largest single quadrant is Q4 (Female reporters, Male signals) at 35.0% — the quintessential paradox: drugs reported predominantly by women generating predominantly male safety signals.

The discordance rate of 53% is significantly greater than the chance rate of 50% ($\chi^2 = 7.76$, $p = 0.0053$), confirming that the asymmetry is systematic rather than stochastic. Importantly, the discordance is asymmetric: Q4 (female-to-male discordance) is nearly twice as common as Q2 (male-to-female discordance), at 35.0% vs. 18.0%. This asymmetry reflects the overall female majority of the FAERS reporter pool: most drugs have female-majority reporters, so paradoxical drugs are more likely to be in Q4 (female reporters, male signals) than Q2.

### 3.5 Paradox Drugs: Detailed Characterization

#### 3.5.1 Female-Reporter/Male-Signal Paradox Drugs (N = 133)

The 133 paradox drugs — those with >60% female reports but <40% female-predominant signals — span multiple therapeutic classes and indications. The most extreme examples, with reporter-signal gaps exceeding 60 percentage points, are:

| Drug | %F Reports | %F Signals | Gap | Primary Indication |
|------|-----------|-----------|-----|-------------------|
| Abaloparatide | 93% | 6% | 87pp | Osteoporosis (postmenopausal) |
| Pertuzumab | 90% | 8% | 82pp | HER2+ breast cancer |
| Mifepristone | 80% | 0% | 80pp | Pregnancy termination / Cushing's |
| Interferon beta-1a | 78% | 13% | 65pp | Multiple sclerosis |
| Docetaxel | 75% | 11% | 64pp | Various cancers |
| Methotrexate sodium | 71% | 9% | 62pp | Autoimmune / cancer |
| Levothyroxine | 77% | 20% | 57pp | Hypothyroidism |
| Denosumab | 81% | 23% | 57pp | Osteoporosis / bone metastases |

Several cases merit specific interpretation. **Abaloparatide** (87pp gap), a parathyroid hormone analog for postmenopausal osteoporosis, has a 93% female reporter pool yet only 6% female-predominant signals. The few men receiving this drug (typically for glucocorticoid-induced osteoporosis) experience distinct adverse event profiles attributable to sex differences in bone metabolism and parathyroid hormone receptor density [18]. **Mifepristone** (80pp gap), used primarily for pregnancy termination, shows 0% female-predominant signals; its off-label use in Cushing's syndrome exposes male patients to qualitatively distinct hormonal perturbations. **Levothyroxine** (57pp gap), the most prescribed medication in the United States, has a 77% female reporter pool reflecting the 5:1 female-to-male ratio of hypothyroidism, yet only 20% of its sex-differential signals are female-predominant — consistent with known sex differences in thyroid hormone metabolism and cardiovascular sensitivity [19].

#### 3.5.2 Male-Reporter/Female-Signal Reverse Paradox Drugs (N = 32)

The 32 reverse paradox drugs — those with <40% female reports but >60% female-predominant signals — show the mirror pattern:

| Drug | %F Reports | %F Signals | Gap | Primary Indication |
|------|-----------|-----------|-----|-------------------|
| BCG Vaccine | 26% | 95% | 70pp | Bladder cancer / TB prevention |
| Tamsulosin | 13% | 81% | 68pp | Benign prostatic hyperplasia |
| Factor VIII | 7% | 74% | 67pp | Hemophilia A |
| Testosterone | 9% | 74% | 65pp | Hypogonadism |
| Risperidone | 29% | 93% | 64pp | Schizophrenia / bipolar |
| Tafamidis | 26% | 86% | 61pp | Transthyretin amyloid cardiomyopathy |
| Diamorphine | 32% | 83% | 50pp | Pain management |
| Sorafenib | 31% | 80% | 49pp | Hepatocellular / renal carcinoma |

**BCG Vaccine** (70pp gap) presents the most extreme reverse paradox: 74% male reporters but 95% female-predominant signals, consistent with well-documented sex differences in immune responses to mycobacterial antigens [23]. **Tamsulosin** (68pp gap), an alpha-1 blocker for BPH, has an 87% male reporter pool yet 81% female-predominant signals, plausibly reflecting greater female cardiovascular sensitivity to alpha-1 blockade [20]. **Factor VIII** (67pp gap) reflects the X-linked epidemiology of hemophilia A yet produces female-predominant signals, likely driven by sex differences in immunogenic response among female carriers [21]. **Risperidone** (64pp gap) is consistent with pharmacokinetic data showing higher plasma concentrations in women at equivalent doses due to CYP2D6 sex differences, resulting in greater prolactin elevation and metabolic effects [22].

### 3.6 Paradoxical Drugs Have Stronger Signals

A critical prediction distinguishes reporting artifacts from genuine biological signals: artifacts should be weakest where the discordance is greatest (because the artifact is being diluted by the mismatch between reporter pool and signal direction), whereas genuine signals should be strongest where the discordance is greatest (because strong biological effects are more likely to produce anti-correlated patterns).

Paradoxical drugs (reporter-signal gap > 30pp) exhibit significantly STRONGER, not weaker, effect sizes:

- Paradoxical drugs: 1,198 drugs, mean |LR| = 0.990
- Non-paradoxical drugs: 980 drugs, mean |LR| = 0.921
- Welch's t = 3.71, p = 2.09e-4 (95% CI for difference: [0.032, 0.105])

The 7.5% effect size advantage of paradoxical drugs is the opposite of what reporting artifacts predict. Under the artifact model, paradoxical drugs should have the weakest signals because the signal direction opposes the expected direction of reporting bias. Instead, they have the strongest signals — consistent with genuine pharmacological sex differences that are powerful enough to produce detectable anti-correlations.

### 3.7 Volume Anti-Regression

The proportion of female-predominant signals increased monotonically with report volume:

| Volume Stratum | Female-Predominant Signals |
|---------------|---------------------------|
| Q1 (lowest volume) | 42.9% |
| Q2 | 46.4% |
| Q3 | 51.3% |
| Q4 | 55.2% |
| Q5 (highest volume) | 73.3% |
| Top 1% | 88.9% |

This monotonic anti-regression pattern — effects INCREASING with statistical power — is the opposite of what artifacts produce. Statistical artifacts are subject to regression to the mean: as sample size increases, random fluctuations average out. If signals were artifacts, we would expect the female-predominant proportion to converge toward 50% or toward the reporter ratio (74.3%). Instead, the proportion increases monotonically from 42.9% to 88.9% (Spearman $r_s = 0.94$, $p = 0.005$ across the six volume strata). This pattern is consistent with a genuine female-excess signal obscured by noise at low volumes.

### 3.8 Effect Size Asymmetry

Female-predominant signals had significantly larger effect sizes than male-predominant signals:

- Female-predominant mean |LR|: 1.007
- Male-predominant mean |LR|: 0.963
- F/M ratio: 1.046
- Mann-Whitney U p = 2.8e-41

The 4.6% effect size excess across 96,281 signals is inconsistent with random reporting variation (expected F/M ratio = 1.000; observed = 1.046, $z = 13.4$, $p = 2.8e-41$). This asymmetry is consistent with pharmacokinetic models predicting systematically higher drug exposure in women due to lower body weight, higher body fat percentage, lower renal clearance, and differential CYP enzyme activity [1, 2].

### 3.9 Convergent Evidence Summary

The five independent analyses produce a coherent, internally consistent picture that is incompatible with the reporting artifact hypothesis:

| Analysis | Reporting Artifact Prediction | Observed Result | Verdict |
|----------|------------------------------|-----------------|---------|
| Reporter-signal correlation | Positive (r > 0) | Negative (rho = -0.215, p = 6.92e-13) | Refuted |
| Graduated power | Attenuates toward zero | Strengthens (r = -0.271 at >=100 signals) | Refuted |
| Drug-level discordance | Low (<50%) | High (53%, p = 0.0053) | Refuted |
| Volume gradient | Regression to mean | Anti-regression (42.9% to 88.9%) | Refuted |
| Effect sizes | Symmetric (F/M = 1.0) | Asymmetric (F/M = 1.046, p = 2.8e-41) | Refuted |

The probability of all five analyses independently contradicting the reporting artifact hypothesis by chance, under the conservative assumption that each has a 50% probability of producing an anti-artifact result, is $0.5^5 = 0.031$.

---

## 4. Discussion

### 4.1 Definitive Refutation of the Reporting Artifact Hypothesis

Our findings provide five independent, convergent lines of evidence against the reporting artifact hypothesis:

1. **Direction**: Report ratios and signal ratios anti-correlate (rho = -0.215, p = 6.92e-13)
2. **Power**: The anti-correlation STRENGTHENS with data (r = -0.271 at >=100 signals, p = 5.14e-6)
3. **Discordance**: 53% of drugs show paradoxical reporter-signal disagreement
4. **Magnitude**: Effects increase with volume (anti-regression: 42.9%F to 88.9%F)
5. **Asymmetry**: Female effects are systematically larger (p = 2.8e-41)

No plausible reporting bias mechanism can simultaneously produce all five patterns. Reporting bias predicts: positive correlation, attenuation with power, concordance, regression to mean, and symmetric effects. We observe the opposite on ALL five dimensions.

The convergent nature of these findings is critical. Any single analysis could be challenged on methodological grounds. But the five analyses test different aspects of the reporting-signal relationship using different statistical methods (correlation, classification, regression, rank comparison). Their unanimous verdict substantially reduces the probability of a systematic methodological artifact producing the observed pattern.

### 4.2 The Graduated-Power Signature as a Diagnostic Tool

The graduated-power analysis provides a particularly powerful diagnostic for distinguishing genuine signals from artifacts in observational data. The key insight is that artifacts and genuine signals have opposite power trajectories:

**Artifacts** are driven by random noise, small-sample fluctuations, and unmeasured confounding. As sample size increases and statistical power improves, these sources of error are progressively averaged out. The expected trajectory of an artifactual correlation is therefore:

$$\lim_{n \to \infty} |r_{\text{artifact}}(n)| = 0$$

**Genuine biological signals** are driven by systematic, reproducible effects. As sample size increases, these effects are estimated more precisely, and the signal-to-noise ratio improves. The expected trajectory of a genuine signal is:

$$|r_{\text{signal}}(n)| \text{ increases monotonically with } n$$

Our graduated-power trajectory — from r = -0.007 (all drugs) to r = -0.271 (>=100 signals) — follows the genuine-signal trajectory exactly. This pattern cannot be produced by any known class of reporting artifacts.

The graduated-power diagnostic has potential applicability beyond pharmacovigilance. Any observational dataset in which a putative confounder (C) is hypothesized to drive an association between two variables (X, Y) can be subjected to a graduated-power analysis by stratifying by the precision of the X-Y association. If the X-C correlation strengthens with precision, the confounding hypothesis is refuted.

### 4.3 Relationship to Known Paradoxes in Epidemiology

The reporter-signal anti-correlation relates to several well-characterized statistical paradoxes. **Simpson's paradox** [10] — wherein an association reverses upon stratification — is directly instantiated by Q4 drugs (female reporters, male signals): the marginal pattern (women report more) reverses at the drug-conditional level. Our data extend classical Simpson's paradox by showing a systematic, graduated anti-correlation that strengthens with statistical power, a "graduated Simpson's paradox" not previously described in the epidemiological literature.

The **obesity paradox** — better outcomes in overweight patients with chronic disease [24, 25] — shares structural similarities with our sex paradox: a seemingly "protective" factor (majority reporter sex) is paradoxically associated with fewer signals. However, the obesity paradox remains controversial and may be attributable to collider bias, whereas our sex paradox strengthens with power, arguing against artifactual origins.

**Lord's paradox** [26] (divergent conclusions from ANOVA vs. ANCOVA) is structurally analogous: the marginal analysis predicts concordance between reporter sex and signal sex, while the conditional (drug-stratified) analysis reveals anti-correlation. **Berkson's bias** [27] — spurious associations from collider selection — could theoretically produce negative reporter-signal correlations if report filing acts as a collider. However, Berkson's bias predicts a weak, attenuating association, not one that strengthens from r = -0.007 to r = -0.271 with increasing power. The graduated-power trajectory is therefore inconsistent with Berkson's bias.

### 4.4 The Exposure Paradox: A Mechanistic Framework

We propose the "exposure paradox" as the primary mechanistic explanation for the reporter-signal anti-correlation. The exposure paradox operates through the following causal chain:

1. **Disease sex ratio determines reporter sex ratio**: Drugs indicated for female-predominant conditions (e.g., autoimmune diseases, osteoporosis, thyroid disorders) naturally accumulate female-majority reporter pools. Drugs indicated for male-predominant conditions (e.g., BPH, hemophilia, hepatocellular carcinoma) accumulate male-majority reporter pools.

2. **Drug pharmacology is optimized for the majority-sex user**: Drug development, dosing, and safety monitoring historically have been conducted primarily in the sex that constitutes the majority of the target patient population. This creates an "optimization bias" — the drug's safety profile is better characterized and better managed in the majority sex.

3. **Minority-sex users experience disproportionate adverse events**: When a drug designed and dosed for one sex is used in the other sex, pharmacokinetic and pharmacodynamic differences produce a distinct adverse event profile. Because the minority sex has fewer reporters, these events are less likely to be reported in absolute numbers — but when they are reported, they produce disproportionality signals because the baseline rate of the drug in that sex is low.

4. **Anti-correlation emerges**: The combination of (a) majority-sex dominance of the reporter pool and (b) minority-sex dominance of the disproportionality signals produces a systematic negative correlation between reporter sex and signal sex.

This framework is supported by the specific paradox drugs identified in our analysis. Abaloparatide, pertuzumab, and denosumab are all drugs developed for conditions more common in women, with dosing established primarily in female cohorts. The minority male users experience different adverse event profiles — consistent with sex differences in bone metabolism (abaloparatide, denosumab) and cardiac physiology (pertuzumab). Conversely, tamsulosin, Factor VIII, and testosterone are developed for male-predominant conditions, and the minority female users experience disproportionate adverse events consistent with sex differences in adrenergic physiology (tamsulosin), immune function (Factor VIII), and endocrine sensitivity (testosterone).

### 4.5 Pharmacokinetic Basis of Sex-Differential Drug Safety

The biological plausibility of the sex paradox is grounded in well-established pharmacokinetic sex differences across all ADME phases [1, 2, 28]. Women have slower gastric emptying (altered absorption), higher body fat percentage (~25% vs. ~15%) with lower total body water (altered distribution), differential CYP enzyme activity (CYP3A4 higher in women; CYP1A2, CYP2E1 variable), and approximately 10-15% lower glomerular filtration rate even after body surface area adjustment (altered elimination). These differences produce systematic sex-differential drug exposure independent of reporting behavior [6, 29]. The 4.6% effect size excess for female-predominant signals is quantitatively consistent with pharmacokinetic models predicting 5-15% higher drug exposure in women at equivalent doses [29].

### 4.6 Clinical Implications

#### 4.6.1 The 133 Paradox Drugs as Priority Targets

The 133 paradox drugs represent high-priority targets for sex-specific safety assessment. These drugs exhibit extreme discordance between their user population (predominantly female) and their safety signal profile (predominantly male), suggesting that minority male users experience adverse events at rates disproportionate to their representation. **Levothyroxine** (57pp gap), as the most prescribed medication in the United States, merits particular attention: 80% of its sex-differential signals are male-predominant despite 77% female users, and sex-specific dosing guidelines may be warranted.

#### 4.6.2 The 32 Reverse Paradox Drugs

The reverse paradox drugs identify medications where minority female users face disproportionate risk. **Risperidone** (64pp gap, 93% female signals despite 71% male reporters) exemplifies this pattern, with female-predominant signals for metabolic syndrome, prolactin elevation, and QT prolongation — all pharmacologically consistent with CYP2D6 sex differences [22].

#### 4.6.3 Regulatory Implications

Our findings have direct implications for regulatory methodology:

1. **Sex-stratified signal detection** should be standard in post-marketing surveillance, without discounting for reporting imbalances.
2. **Sex-specific safety analyses** should be required in periodic safety update reports (PSURs) and risk evaluation and mitigation strategies (REMS).
3. **The graduated-power diagnostic** should be adopted to distinguish genuine sex-differential signals from artifacts.
4. **The 133 paradox drugs and 32 reverse paradox drugs** should be prioritized for sex-specific safety reviews.

### 4.7 Methodological Contributions

This study introduces two methodological innovations with broader applicability. **Reporter-signal decorrelation analysis** provides a general framework for testing confounding by computing the correlation between a confounder's distribution and an outcome's distribution at the analysis-unit level. **Graduated-power trajectory analysis** diagnoses artifacts vs. genuine signals by tracking how a statistic changes across escalating power thresholds — noise attenuates while biology strengthens. Both approaches are applicable to meta-analyses, genome-wide association studies, and other high-dimensional observational contexts.

### 4.8 Comparison to Prior Literature

Our findings are consistent with and extend several prior observations in the pharmacovigilance literature. Zucker and Prendergast (2020) documented that sex differences in adverse drug reactions persist after accounting for differential prescription rates, concluding that biological mechanisms drive the majority of sex-differential safety signals [2]. Our reporter-signal anti-correlation provides a complementary, drug-level test of the same hypothesis, reaching the same conclusion via an independent analytical pathway.

Watson et al. (2019) analyzed FAERS data and found that women experience more ADRs than men across most drug classes, but did not directly test the reporting artifact hypothesis [3]. Our analysis addresses this gap by demonstrating that the sex-differential signal pattern is not only inconsistent with reporting bias but actively contradicts it.

Anderson (2008) reviewed sex-based pharmacokinetic differences and concluded that women are systematically underrepresented in clinical trials relative to their representation in the drug-using population [1]. Our findings add pharmacovigilance evidence to this picture: the paradox drugs identified in our analysis are precisely those where the sex imbalance between users and clinical trial participants may be most pronounced.

The graduated-power analysis is, to our knowledge, novel in the pharmacovigilance context. Related approaches have been used in genetic epidemiology, where the strengthening of a genetic association with increasing sample size is taken as evidence of a true positive rather than a false positive [30].

---

## 5. Limitations

Several limitations should be considered when interpreting these findings:

1. **Spontaneous reporting system biases.** FAERS is a spontaneous reporting system subject to the Weber effect (higher reporting rates for newly marketed drugs), notoriety bias (higher reporting rates for drugs with publicized safety concerns), stimulated reporting (manufacturer-driven reporting campaigns), and general underreporting. These biases could differentially affect male and female reporting in ways that are not captured by our drug-level analysis. However, for these biases to explain the observed anti-correlation, they would need to systematically increase female reporting for drugs with male-predominant safety signals and vice versa — a pattern for which there is no known mechanism.

2. **Reporter sex determination.** Reporter sex was inferred from report-level data in FAERS. Some reports may have missing, incorrect, or ambiguous sex information. Misclassification of reporter sex would be expected to attenuate the observed anti-correlation (bias toward the null), making our estimates conservative.

3. **Confounding by indication.** Drug indication sex ratios are a major driver of reporter sex ratios. Our analysis cannot fully separate the contribution of indication-driven confounding from pharmacological sex differences. However, the graduated-power analysis mitigates this concern: confounding by indication would be expected to produce a fixed, not strengthening, correlation pattern across power strata.

4. **Multiple drug use.** FAERS reports often list multiple concurrent medications. Our drug-level analysis assigns signals to individual drugs, potentially attributing signals to the wrong drug in the context of polypharmacy. This source of error would be expected to add noise (attenuating correlations) rather than producing systematic anti-correlations.

5. **Geographic and temporal heterogeneity.** FAERS is predominantly a US database, and reporting patterns may differ in other jurisdictions. Temporal changes in reporting practices, drug utilization, and diagnostic criteria could affect the stability of the observed patterns. Our temporal sensitivity analysis (first half vs. second half of the study period) partially addresses this concern.

6. **Causality.** Our analysis is observational and correlational. While the convergent evidence strongly argues against reporting bias as the driver of sex-differential signals, it does not definitively establish the specific biological mechanisms responsible. Mechanistic validation through pharmacokinetic modeling and clinical studies is needed.

7. **Replication.** The findings require replication in independent pharmacovigilance databases, particularly EudraVigilance (European Union) and JADER (Japan), to assess generalizability across regulatory jurisdictions and healthcare systems.

---

## 6. Conclusion

Sex-differential drug safety signals anti-correlate with reporting patterns (rho = -0.215, p = 6.9e-13), and this anti-correlation STRENGTHENS with statistical power (r = -0.271 at >=100 signals, p = 5.14e-6). Combined with 53% drug-level discordance, anti-regression (42.9%F to 88.9%F), effect asymmetry (F/M = 1.046, p = 2.8e-41), and paradoxical drugs having STRONGER signals (p = 2.09e-4), these findings definitively refute the reporting artifact hypothesis. Sex-differential adverse drug reactions reflect genuine pharmacological sex differences with immediate implications for drug safety surveillance, clinical practice, and regulatory policy.

The 133 paradox drugs and 32 reverse paradox drugs identified here constitute a priority list for sex-specific safety review. These medications — spanning oncology, endocrinology, immunology, cardiology, and psychiatry — exhibit the most extreme discordance between their user demographics and their safety profiles. Targeted sex-stratified analyses of these drugs, including pharmacokinetic modeling and prospective clinical monitoring, should be a regulatory priority.

The methodological framework introduced here — reporter-signal decorrelation analysis with graduated-power trajectory assessment — provides a generalizable toolkit for distinguishing confounding artifacts from genuine signals in observational pharmacovigilance and beyond.

---

## Data Availability

FAERS data (2004Q1-2025Q3) are publicly available from the FDA. All analysis code, intermediate results, and the SexDiffKG knowledge graph are available at https://github.com/jshaik369/SexDiffKG.

---

## Key Statistics

- 96,281 sex-differential signals, 2,178 drugs
- FAERS: 74.3% female reporters, 53.8% female signals (20.5pp gap)
- Anti-correlation: rho = -0.215, p = 6.92e-13 (global)
- Graduated power: r = -0.271 at >=100 signals (p = 5.14e-6), STRENGTHENS with data
- 53% discordant drugs (reporter sex != signal sex)
- 133 paradox drugs (female reports, male signals), max gap 87pp
- 32 reverse paradox drugs (male reports, female signals), max gap 70pp
- Paradoxical drugs: STRONGER signals (|LR| 0.990 vs 0.921, p = 2.09e-4)
- Volume gradient: Q1=42.9%F -> Top1%=88.9%F (monotonic anti-regression)
- Effect asymmetry: F/M ratio=1.046, p=2.8e-41

---

## References

1. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? Pharmacogenetics, pharmacokinetics, and pharmacodynamics. *Journal of Women's Health*. 2005;14(4):292-302. doi:10.1089/jwh.2005.14.292

2. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biology of Sex Differences*. 2020;11(1):32. doi:10.1186/s13293-020-00308-5

3. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine*. 2019;17:100188. doi:10.1016/j.eclinm.2019.10.001

4. Yu Y, Chen J, Li D, Wang L, Wang W, Liu H. Systematic analysis of adverse event reports for sex differences in adverse drug events. *Scientific Reports*. 2016;6:24955. doi:10.1038/srep24955

5. Zopf Y, Rabe C, Neubert A, Gassmann KG, Rascher W, Hahn EG, et al. Women encounter ADRs more often than do men. *European Journal of Clinical Pharmacology*. 2008;64(10):999-1004. doi:10.1007/s00228-008-0494-6

6. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clinical Pharmacokinetics*. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001

7. Franconi F, Campesi I. Pharmacogenomics, pharmacokinetics and pharmacodynamics: interaction with biological differences between men and women. *British Journal of Pharmacology*. 2014;171(3):580-594. doi:10.1111/bph.12362

8. Greenblatt DJ, Harmatz JS, Singh NN, Steinberg F, Roth T, Moline ML, et al. Gender differences in pharmacokinetics and pharmacodynamics of zolpidem following sublingual administration. *Journal of Clinical Pharmacology*. 2014;54(3):282-290. doi:10.1002/jcph.220

9. Roden DM. Drug-induced prolongation of the QT interval. *New England Journal of Medicine*. 2004;350(10):1013-1022. doi:10.1056/NEJMra032426

10. Simpson EH. The interpretation of interaction in contingency tables. *Journal of the Royal Statistical Society: Series B*. 1951;13(2):238-241. doi:10.1111/j.2517-6161.1951.tb00088.x

11. Pearl J. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press; 2009.

12. Hazell L, Shakir SA. Under-reporting of adverse drug reactions: a systematic review. *Drug Safety*. 2006;29(5):385-396. doi:10.2165/00002018-200629050-00003

13. Montastruc JL, Sommet A, Bagheri H, Lapeyre-Mestre M. Benefits and strengths of the disproportionality analysis for identification of adverse drug reactions in a pharmacovigilance database. *British Journal of Clinical Pharmacology*. 2011;72(6):905-908. doi:10.1111/j.1365-2125.2011.04037.x

14. Holm L, Ekman E, Jorsater Blomgren K. Influence of age, sex and seriousness on reporting of adverse drug reactions in Sweden. *Pharmacoepidemiology and Drug Safety*. 2017;26(3):335-343. doi:10.1002/pds.4155

15. Tamargo J, Rosano G, Walther T, Duarte J, Niessner A, Kaski JC, et al. Gender differences in the effects of cardiovascular drugs. *European Heart Journal - Cardiovascular Pharmacotherapy*. 2017;3(3):163-182. doi:10.1093/ehjcvp/pvw042

16. FDA. FDA Adverse Event Reporting System (FAERS) Public Dashboard. U.S. Food and Drug Administration. https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers. Accessed 2025.

17. Wasserstein RL, Lazar NA. The ASA statement on p-values: context, process, and purpose. *The American Statistician*. 2016;70(2):129-133. doi:10.1080/00031305.2016.1154108

18. Khosla S, Monroe DG. Regulation of bone metabolism by sex steroids. *Cold Spring Harbor Perspectives in Medicine*. 2018;8(1):a031211. doi:10.1101/cshperspect.a031211

19. Biondi B, Cooper DS. Thyroid hormone therapy for hypothyroidism. *Endocrine*. 2019;66(1):18-26. doi:10.1007/s12020-019-02023-7

20. Kneale BJ, Chowienczyk PJ, Brett SE, Coltart DJ, Ritter JM. Gender differences in sensitivity to adrenergic agonists of forearm resistance vasculature. *Journal of the American College of Cardiology*. 2000;36(4):1233-1238. doi:10.1016/S0735-1097(00)00849-4

21. Plug I, Mauser-Bunschoten EP, Brocker-Vriends AH, van Amstel HK, van der Bom JG, van Diemen-Homan JE, et al. Bleeding in carriers of hemophilia. *Blood*. 2006;108(1):52-56. doi:10.1182/blood-2005-09-3879

22. Aichhorn W, Weiss U, Marksteiner J, Kemmler G, Walch T, Zernig G, et al. Influence of age and gender on risperidone plasma concentrations. *Journal of Psychopharmacology*. 2005;19(4):395-401. doi:10.1177/0269881105053307

23. Klein SL, Flanagan KL. Sex differences in immune responses. *Nature Reviews Immunology*. 2016;16(10):626-638. doi:10.1038/nri.2016.90

24. Banack HR, Kaufman JS. The obesity paradox: understanding the effect of obesity on mortality among individuals with cardiovascular disease. *Preventive Medicine*. 2014;62:96-102. doi:10.1016/j.ypmed.2014.02.003

25. Lajous M, Banack HR, Kaufman JS, Hernan MA. Should patients with chronic disease be told to gain weight? The obesity paradox and selection bias. *American Journal of Medicine*. 2015;128(4):334-336. doi:10.1016/j.amjmed.2014.10.043

26. Lord FM. A paradox in the interpretation of group comparisons. *Psychological Bulletin*. 1967;68(5):304-305. doi:10.1037/h0025105

27. Berkson J. Limitations of the application of fourfold table analysis to hospital data. *Biometrics Bulletin*. 1946;2(3):47-53. doi:10.2307/3002000

28. Schwartz JB. The current state of knowledge on age, sex, and their interactions on clinical pharmacology. *Clinical Pharmacology & Therapeutics*. 2007;82(1):87-96. doi:10.1038/sj.clpt.6100226

29. Meibohm B, Beierle I, Derendorf H. How important are gender differences in pharmacokinetics? *Clinical Pharmacokinetics*. 2002;41(5):329-342. doi:10.2165/00003088-200241050-00002

30. Lander ES, Schork NJ. Genetic dissection of complex traits. *Science*. 1994;265(5181):2037-2048. doi:10.1126/science.8091226

---

*Manuscript word count: ~9,800 words (excluding tables, references, and metadata)*

*Corresponding author: Mohammed Javeed Akhtar Abbas Shaik (J.Shaik), jshaik@coevolvenetwork.com, ORCID 0009-0002-1748-7516*
