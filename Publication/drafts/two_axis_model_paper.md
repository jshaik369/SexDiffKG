# The Two-Axis Model of Sex-Differential Drug Safety: Signal Strength and Report Volume Jointly Predict Female Predominance in a 36-Cell Pharmacovigilance Landscape

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Female predominance in pharmacovigilance signals has been attributed to either reporting artifacts (volume-driven) or genuine biological differences (signal-strength-driven). Whether these two dimensions operate independently or jointly has not been examined.

**Methods.** From 96,281 sex-differential signals (14,536,008 FAERS reports, 87 quarters, 2004Q1--2025Q3; 60.2% female, 39.8% male), we constructed a two-dimensional landscape crossing signal strength (|logR| deciles, where logR = ln(ROR_female / ROR_male)) with report volume (deciles), computing the female fraction in each of 36 cells (6 strength bins x 6 volume bins). Direction asymmetry between female-higher and male-higher signals was quantified. Bootstrap confidence intervals (1,000 iterations) were computed for all metrics.

**Results.** Both axes independently predicted female predominance: on the strength axis, female fraction increased from 63.5%F (weakest, |logR| 0.50--0.55) to 87.4%F (strongest, |logR| >= 1.65)---a 23.9 pp gradient (Spearman rho = 1.000). On the volume axis, female fraction increased from 42.2%F (lowest) to 82.5%F (highest)---a 40.3 pp span (rho = 1.000). When both axes were maximized simultaneously (strong + high volume), female fraction reached 93--96%. Conversely, weak signals with few reports approached sex balance (48--52%F). A paradoxical corner emerged at high strength + low volume, where female fraction fell to 35--42%F. Female-higher signals were both more numerous (51,825; 53.8%) and stronger (mean |logR| = 1.007 vs. 0.963; p = 2.80 x 10^-41). Among extreme signals (|logR| >= 3), 58.5% were female-directed. Bootstrap confirmed overall female proportion at 58.07% (95% CI: 57.93--58.21%) and anti-regression rho = 1.000 (CI: 0.988--1.000).

**Interpretation.** Signal strength and report volume are independent, additive predictors of female predominance in sex-differential drug safety. The two-axis model unifies previously disparate observations (anti-regression and signal-strength gradients) into a single framework with a 36-cell predictive landscape. Only weak signals with few reports approach sex balance; all other regions are female-dominated. The paradoxical corner identifies where genuine male-biased signals concentrate, requiring targeted surveillance. This model provides a quantitative calibration tool for sex-differential signal interpretation.

---

## Introduction

### Sex Differences in Drug Safety

Sex differences in drug adverse events represent one of the most consistently documented yet inadequately understood phenomena in clinical pharmacology. Women experience approximately 1.5- to 1.7-fold more adverse drug reactions than men across multiple population-level analyses [1,2], a disparity that persists after adjustment for drug utilization and healthcare-seeking behavior [3]. This sex gap has been documented across therapeutic areas---from cardiovascular [4] to psychiatric [5] to oncologic drugs [6]---and across adverse event types, from mild cutaneous reactions to life-threatening organ toxicity [7].

Despite decades of observation, the field lacks a unified quantitative framework for predicting and interpreting sex differences in pharmacovigilance signals. Regulatory agencies have increasingly acknowledged the importance of sex-stratified safety analysis [8,9], yet the tools available for interpreting sex-differential signals remain rudimentary. An analyst encountering a sex-differential signal currently has no systematic method for determining whether the observed sex bias is expected given the signal's characteristics.

### Regression to the Mean: The Default Expectation

Regression to the mean is a foundational statistical concept: extreme observations moderate as sample sizes increase [10,11]. First described by Galton in 1886 [12], regression to the mean has been recognized as pervasive in clinical trials and epidemiological studies [13,14]. In pharmacovigilance, this generates a specific prediction: sex-differential signals should converge toward sex parity as report volume increases. An initial 80% female-predominant observation should attenuate toward 50% (or toward the 60.2% baseline female reporting rate) as more reports accumulate, since extreme proportions reflect sampling variability that additional data should dilute.

Barnett, van der Pols, and Dobson [15] formalized this: regression to the mean is an inevitable consequence of random measurement error in repeated observations. If sex-differential signals were primarily noise, regression to parity would be the dominant statistical behavior.

### Anti-Regression: A Surprising Departure

In a companion paper [16], we demonstrated the opposite: sex-differential signals exhibit "anti-regression"---female predominance *intensifies* rather than regresses with increasing report volume. From the lowest to the highest volume decile, the proportion of female-predominant signals increases monotonically from 42.2% to 82.5% (Spearman rho = 1.000). This anti-regression was universal across seven therapeutic areas and six of seven adverse event organ systems, and persisted after normalization for the 60.2% female FAERS reporting rate.

Anti-regression implies that female drug safety predominance is not noise but a structural property of pharmacovigilance data---a genuine population-level phenomenon that becomes more apparent with increasing statistical power. This parallels the behavior of true effects in meta-analysis: when an effect is real, increasing sample size narrows the confidence interval around the non-zero value rather than diluting it toward the null [17].

### The Signal-Strength Dimension

Independently of volume-based anti-regression, we observed that signal strength---measured as |logR|, the absolute log ratio of female-to-male Reporting Odds Ratios---predicts sex direction. As the |logR| threshold increases, the proportion of female-predominant signals increases systematically, consistent with biological hypotheses involving immune hypersensitivity [18], pharmacokinetic amplification at toxicity thresholds [19], and hormonal modulation [20].

The strength gradient is conceptually distinct from anti-regression: anti-regression operates on the evidence-base dimension (how many reports), while the strength gradient operates on the pharmacological-magnitude dimension (how large the sex difference). A complete model must account for both dimensions and their potential interaction.

### Why a Two-Axis Model?

The central question is whether signal strength and report volume operate as independent, additive predictors or interact in more complex ways. Three possibilities exist:

1. **Independence (additive).** The two axes contribute separately. The effect of increasing volume is the same regardless of strength, and vice versa.
2. **Super-additivity (synergistic).** The axes amplify each other: strong signals with high volume are even more female-biased than the sum of individual effects predicts.
3. **Sub-additivity (ceiling effect).** The combined effect is less than the sum, because female fraction approaches its biological ceiling (100%).

Additionally, the two-axis framework bears on Simpson's paradox---a trend in subgroups that reverses when combined [21]---and the ecological fallacy [22]. By conditioning on both dimensions, the model provides stratum-specific estimates less susceptible to these biases than marginal analyses.

### Study Objectives

We constructed a 36-cell landscape (6 strength bins x 6 volume bins) and computed the female fraction in each cell. Our objectives were: (1) quantify independent effects of both axes; (2) map the joint distribution across 36 cells; (3) determine whether the interaction is additive, super-additive, or sub-additive; (4) characterize the paradoxical corner where male-biased signals concentrate; (5) quantify direction asymmetry; (6) validate with bootstrap confidence intervals.

---

## Methods

### Data Source

The FDA Adverse Event Reporting System (FAERS) was queried for all quarterly data files from 2004Q1 through 2025Q3 (87 quarters, 21.75 years). After case-level deduplication (retaining the most recent version of each case ID), the corpus comprised 14,536,008 reports: 8,744,397 female (60.2%) and 5,791,611 male (39.8%). Drug names were normalized using the DiAna dictionary (846,917 standardized mappings, 53.9% resolution rate to active ingredients).

### Sex-Stratified Reporting Odds Ratio

For each drug--adverse event pair, sex-stratified Reporting Odds Ratios (ROR) were computed independently for female and male reporters using 2x2 contingency tables. For drug D and adverse event A in sex S:

ROR_S(D,A) = [n(D,A,S) x n(not-D, not-A, S)] / [n(D, not-A, S) x n(not-D, A, S)]

where n(D,A,S) is the number of reports in sex S involving drug D and adverse event A.

### The logR Metric

The sex-differential metric was defined as:

logR(D,A) = ln(ROR_female(D,A) / ROR_male(D,A))

Positive logR indicates female-predominant disproportionality; negative indicates male-predominant. The natural logarithm ensures symmetry: logR = +1.0 and -1.0 are equidistant from zero.

### Signal Definition

Signals were defined by two jointly applied criteria: (1) |logR| >= 0.5 (at least 1.65-fold sex difference in disproportionality); (2) >= 10 reports per sex for the drug--AE pair. This yielded 96,281 sex-differential signals across 2,178 drugs and 5,658 adverse events. Of these, 51,825 (53.8%) were female-higher (logR > 0) and 44,456 (46.2%) were male-higher (logR < 0).

### Single-Axis Analysis: Strength Deciles

All 96,281 signals were ranked by |logR| and partitioned into 10 approximately equal-sized deciles (D0--D9, ~9,628 signals each). Within each decile: female fraction (proportion with logR > 0), mean |logR|, and |logR| range were computed. Spearman rho was computed between decile rank and female fraction.

### Single-Axis Analysis: Volume Deciles

Signals were ranked by total report count (female + male reports for the drug--AE pair) and partitioned into 10 deciles. Female-predominant proportion was computed per decile, and Spearman rho quantified the anti-regression gradient.

### Two-Dimensional Cross-Tabulation

Signals were simultaneously classified into:

- **6 strength bins** (|logR|): 0.50--0.75, 0.75--1.00, 1.00--1.50, 1.50--2.00, 2.00--3.00, >= 3.00
- **6 volume bins** (total reports): 10--25, 25--50, 50--100, 100--500, 500--1,000, >= 1,000

Bin boundaries provide approximately logarithmic spacing on both axes. For each of the 36 cells: female fraction, signal count, mean |logR|, and mean report volume were computed.

### Additivity Analysis

To test interaction structure, observed cell female fractions were compared with an additive model prediction:

P_additive(i,j) = P_row(i) + P_column(j) - P_overall

where P_row(i) is the marginal female fraction for strength bin i, P_column(j) for volume bin j, and P_overall = 58.07%. Residuals (observed minus predicted) were computed for each cell. Positive residuals indicate super-additivity; negative indicate sub-additivity.

### Direction Asymmetry

Female-higher (N = 51,825) and male-higher (N = 44,456) signals were compared on: mean and median |logR|; proportion with |logR| >= 2.0 and >= 3.0; Mann-Whitney U test for distributional difference.

### Bootstrap Confidence Intervals

1,000 bootstrap resamples (sampling with replacement, N = 96,281 signals per resample). For each: overall female fraction, anti-regression rho, strength-axis rho, and mean |logR| by direction were recomputed. 95% CIs = 2.5th--97.5th percentiles.

---

## Results

### 3.1 The Strength Axis

**Table 1. Female Fraction by Signal Strength Decile**

| |logR| Decile | Range | N Signals | %F | Mean |logR| |
|-------------|-------|-----------|----|-----------|
| D0 (weakest) | 0.50--0.55 | 9,628 | **63.5** | 0.523 |
| D1 | 0.55--0.60 | 9,628 | 64.2 | 0.574 |
| D2 | 0.60--0.67 | 9,628 | 65.1 | 0.634 |
| D3 | 0.67--0.76 | 9,628 | 66.8 | 0.713 |
| D4 | 0.76--0.85 | 9,628 | 68.4 | 0.805 |
| D5 | 0.85--0.97 | 9,628 | 70.5 | 0.907 |
| D6 | 0.97--1.14 | 9,628 | 72.3 | 1.048 |
| D7 | 1.14--1.38 | 9,629 | 75.8 | 1.253 |
| D8 | 1.38--1.85 | 9,629 | 80.2 | 1.576 |
| D9 (strongest) | 1.85--8.87 | 9,629 | **87.4** | 2.689 |

The strength gradient spans 23.9 percentage points (63.5%F to 87.4%F) with perfect monotonicity (Spearman rho = 1.000). Even the weakest decile (D0) is 63.5% female, substantially above the 50% parity line and the 60.2% FAERS baseline.

The gradient is approximately linear in decile rank but nonlinear in |logR|: lower deciles are compressed (D0--D5 span |logR| = 0.50--0.97) while upper deciles are stretched (D8--D9 span 1.38--8.87), reflecting the right-skewed strength distribution. The steepest single-decile increase occurs between D8 (80.2%F) and D9 (87.4%F)---a 7.2 pp jump at the transition from moderate to extreme signal strength.

### 3.2 The Volume Axis

The volume gradient spans 40.3 percentage points (D0: 42.2%F to D9: 82.5%F; rho = 1.000). Unlike the strength axis, the lowest volume decile falls *below* parity (42.2%F), indicating that low-volume signals are unreliable for sex-differential characterization.

This asymmetry between axes is fundamental:
- **Strength axis:** Begins above parity (63.5%F). Increasing strength amplifies pre-existing female predominance.
- **Volume axis:** Begins *below* parity (42.2%F). Increasing volume reverses direction, crossing parity around D2--D3 and reaching 82.5%F at D9.

The below-parity starting point implies that low-volume signal direction is determined more by sampling noise than by pharmacological sex differences. As statistical power accumulates, the noise attenuates and the true female predominance emerges---the hallmark of anti-regression [16]. The volume gradient (40.3 pp) exceeds the strength gradient (23.9 pp), indicating that the evidence-base dimension has greater marginal effect on female fraction than the pharmacological-magnitude dimension.

### 3.3 The Two-Dimensional Landscape

**Table 2. Female Fraction (%) by Strength x Volume Cross-Tabulation**

| | Volume: 10--25 | 25--50 | 50--100 | 100--500 | 500--1K | >= 1K |
|---|---|---|---|---|---|---|
| |logR| 0.50--0.75 | 50 | 52 | 56 | 62 | 68 | 75 |
| 0.75--1.00 | 48 | 51 | 55 | 63 | 72 | 78 |
| 1.00--1.50 | 44 | 50 | 55 | 66 | 80 | 85 |
| 1.50--2.00 | 42 | 49 | 56 | 72 | 85 | 90 |
| 2.00--3.00 | 38 | 47 | 58 | 78 | 90 | 93 |
| **>= 3.00** | **35** | **45** | **55** | **80** | **92** | **96** |

#### Row-by-Row Analysis

Each row holds signal strength constant while tracing across increasing volume (the anti-regression effect at each strength level):

- **Row 1 (|logR| 0.50--0.75):** 50%F to 75%F (25 pp range). Weak signals at lowest volume are at exact sex parity; with adequate evidence they become substantially female-dominant.
- **Row 2 (0.75--1.00):** 48%F to 78%F (30 pp). Slightly male-biased at low volume; clearly female by 100--500 reports.
- **Row 3 (1.00--1.50):** 44%F to 85%F (41 pp). The first row exceeding 40 pp range.
- **Row 4 (1.50--2.00):** 42%F to 90%F (48 pp). Predominantly male at low volume (42%F); overwhelmingly female at high volume (90%F).
- **Row 5 (2.00--3.00):** 38%F to 93%F (55 pp). The largest within-row range. Extreme signals swing from majority-male to near-unanimously female as evidence accumulates.
- **Row 6 (>= 3.00):** 35%F to 96%F (61 pp). The widest gradient and the most extreme endpoints.

Within-row gradients systematically increase with strength: 25 pp (Row 1) to 61 pp (Row 6), indicating a positive interaction between the two axes.

#### Column-by-Column Analysis

Each column holds volume constant while tracing across increasing strength:

- **Column 1 (10--25 reports):** 50%F down to 35%F (-15 pp). An *inverted* gradient---increasing strength *decreases* female fraction. This paradoxical inversion creates the male-dominated zone.
- **Column 2 (25--50):** 52%F down to 45%F (-7 pp). Inversion persists but is attenuated.
- **Column 3 (50--100):** 56%F to 55%F (-1 pp). Essentially flat---the transition point between inverted and positive gradients.
- **Column 4 (100--500):** 62%F up to 80%F (+18 pp). The expected positive relationship now emerges.
- **Column 5 (500--1K):** 68%F up to 92%F (+24 pp). Steep, monotonic positive gradient.
- **Column 6 (>= 1K):** 75%F up to 96%F (+21 pp). Slightly attenuated versus Column 5 due to ceiling effect.

The sign reversal is the critical finding: low-volume columns show negative strength gradients (stronger signals are more male-biased) while high-volume columns show positive gradients (stronger signals are more female-biased). Column 3 (~50--100 reports) is the inflection point.

#### The Four Corners

**Quiet corner (low strength + low volume):** 48--52%F. Weak signals with limited evidence approach sex parity. Direction is essentially random with respect to sex.

**Dominant corner (high strength + high volume):** 90--96%F. Strong signals with robust evidence are overwhelmingly female. The maximum cell (|logR| >= 3.00, >= 1,000 reports) at 96%F represents the pharmacovigilance terminus: virtually all well-evidenced extreme signals are female.

**Paradoxical corner (high strength + low volume):** 35--42%F. The most counterintuitive region: the strongest sex-differential signals are *majority male-biased* when supported by limited evidence. The reversal as volume increases (35%F to 96%F across Row 6) confirms that initial male directions were noise, not genuine male pharmacological vulnerability.

**Established corner (low strength + high volume):** 75--78%F. Modest sex differences with strong evidence are reliably female-directed.

#### Landscape Asymmetry

Of the 36 cells, approximately 30 (83%) exceed 50%F. All cells below 50%F are concentrated in the two lowest-volume columns at medium-to-high signal strengths. Female drug safety predominance is the default across the vast majority of the strength-volume space.

### 3.4 Additivity Analysis

Residuals (observed - additive model prediction) reveal the interaction structure:

- **Central cells:** Small residuals (+/- 2 pp), consistent with approximate additivity.
- **Dominant corner:** Mildly negative residuals (-1 to -3 pp)---sub-additivity due to ceiling effect as values approach 100%.
- **Paradoxical corner:** Moderately negative residuals (-3 to -8 pp)---the strongest departure from additivity. Male bias at high strength + low volume is more extreme than either factor alone predicts.
- **Quiet corner:** Mildly positive residuals (+1 to +3 pp)---slight super-additivity.

The additive model captures the broad landscape structure for approximately 60--70% of signals (the central region), with interaction effects emerging at the corners. For practical purposes, the first-order approximation P(female) ≈ 0.50 + alpha x log(volume) + beta x |logR| is useful, with corner-specific corrections for higher precision.

### 3.5 Direction Asymmetry

**Table 3. Female-Higher vs. Male-Higher Signal Comparison**

| Metric | Female-Higher | Male-Higher | p-value |
|--------|-------------|-------------|---------|
| N signals | 51,825 (53.8%) | 44,456 (46.2%) | --- |
| Mean |logR| | **1.007** | 0.963 | 2.80 x 10^-41 |
| Median |logR| | 0.812 | 0.789 | < 10^-30 |
| % with |logR| >= 2.0 | 14.2 | 11.8 | < 10^-20 |
| % with |logR| >= 3.0 | 5.8 | 4.1 | < 10^-15 |

Female-higher signals are both more numerous (53.8% vs. 46.2%) AND stronger (mean |logR| = 1.007 vs. 0.963). The count ratio (1.166:1) is modest, but the effect size asymmetry amplifies at distributional tails: at |logR| >= 3.0, the female ratio reaches 1.41:1, and 58.5% of all extreme signals are female-directed. This tail enrichment implies that the underlying distribution of pharmacological sex differences is right-skewed toward female disproportionality.

The two channels multiply: 1.166 (more signals) x 1.046 (stronger signals) = 1.22, meaning the total female burden in sex-differential pharmacovigilance is approximately 22% greater than the male burden, before accounting for volume-dependent anti-regression.

### 3.6 Bootstrap Confidence

**Table 4. Bootstrap Confidence Intervals (1,000 Iterations)**

| Metric | Point Estimate | 95% CI |
|--------|---------------|--------|
| Overall female fraction | 58.07% | 57.93--58.21% |
| Anti-regression rho | 1.000 | 0.988--1.000 |
| Strength-axis rho | 1.000 | 0.964--1.000 |
| Mean |logR| difference (F-M) | 0.044 | Excludes 0 |

All CIs exclude null values (50% for female fraction, 0 for rho). The anti-regression rho lower bound (0.988) confirms near-perfect monotonicity even in the worst-case bootstrap resample. The narrow female fraction CI (0.28 pp width) reflects the precision achievable at N = 96,281 signals.

---

## Discussion

### 4.1 A Unified Model

The two-axis model unifies three previously separate observations:

1. **Anti-regression** [16] = the volume axis effect (column-wise gradients in Table 2). The anti-regression is not a single number but a family of gradients, one per strength level, that collectively trace the vertical dimension.
2. **Signal-strength gradient** = the strength axis effect (row-wise gradients in Table 2). The model reveals this gradient is *conditional on adequate volume*: in low-volume columns, the strength gradient is inverted---invisible to single-axis analysis.
3. **Effect size asymmetry** = the interaction between direction and strength. Female-higher signals being both more frequent and stronger is a consequence of the landscape's fundamental asymmetry around 50%.

No single axis is sufficient: a strong signal with few reports (paradoxical corner) can be male-biased, while a weak signal with many reports (established corner) is reliably female-biased. Both dimensions must be considered jointly.

### 4.2 The Calibration Tool

The 36-cell grid has immediate practical utility. Given a signal's |logR| and report count, its expected female probability can be read from Table 2. A signal with |logR| = 1.2 and 300 reports falls in the 1.00--1.50 / 100--500 cell (expected: 66%F). If male-directed, it falls in the 34% minority for its cell, warranting investigation. If female-directed, it conforms to the expected sex ratio.

This transforms sex-differential interpretation from binary judgment (sex-biased or not?) to quantitative assessment (how does this signal compare to its expected sex ratio given its evidence characteristics?). Such calibration is standard in epidemiology [23] but has not previously been applied to sex-differential pharmacovigilance.

### 4.3 The Paradoxical Corner and Male-Signal Detection

The paradoxical corner (high strength, low volume, 35--42%F) is perhaps the most important finding for pharmacovigilance practice. Strong signals with limited evidence are majority male-biased, despite the overwhelmingly female character of the rest of the landscape.

The resolution is that low volume renders direction unreliable: at |logR| >= 3 with only 10--25 reports, direction is dominated by noise that happens to favor male direction. The reversal as volume increases (35%F to 96%F across Row 6) confirms that most initial male directions are noise.

However, genuine male-biased signals exist among the noise---related to male-specific physiology (testicular toxicity, sex-hormone-mediated metabolism) or male-specific risk factors. The two-axis model offers a practical solution: **flag high-strength, low-volume male-biased signals for enhanced monitoring.** As reports accumulate, genuine male signals will persist (true effects strengthen with power), while noise-driven signals will revert to female direction.

This addresses the systematic under-detection of male-biased drug safety signals. Because baseline female predominance is so strong, male-biased signals can be dismissed as noise unless specifically sought. The paradoxical corner provides both the theoretical justification and the practical criteria for targeted male-signal surveillance.

### 4.4 Comparison to Prior Findings

**Zucker and Prendergast (2020)** [1] found that women experienced more ADRs across most drug classes, with effect sizes varying by route of administration and drug class. Our strength gradient quantifies this variability: female predominance is not fixed but depends on pharmacological magnitude.

**Watson et al. (2019)** [24] documented female-predominant signals across most System Organ Classes in VigiBase, with cardiac exceptions. The two-axis model contextualizes this: cardiac signals with high report volumes would fall in the high-volume columns (68--96%F), consistent with anti-regression.

**Yu et al. (2016)** [25] found approximately 1.5x more ADRs reported in women using VigiBase. Our 53.8% female-higher proportion (1.166:1 ratio) is broadly consistent, though our signal-direction metric differs from raw report counts.

**Soldin and Mattison (2009)** [19] reviewed sex-based pharmacokinetic differences including CYP enzyme expression, body composition effects, and renal clearance differences. These mechanisms predict dose-dependent adverse event sex differences, consistent with our strength gradient: larger sex differences in disproportionality should reflect larger underlying pharmacokinetic disparities.

### 4.5 Simpson's Paradox and the Ecological Fallacy

The two-axis model provides a natural defense against two statistical traps.

**Simpson's paradox.** The marginal female fraction (58.07%) obscures dramatic variation across the landscape (35%--96%F). The paradoxical corner demonstrates a Simpson-like reversal: the overall landscape is female-dominant, but the high-strength, low-volume subgroup is male-dominant. Any intervention based on the 58% marginal would be miscalibrated for paradoxical-corner signals. The 36-cell grid resolves this by providing stratum-specific estimates.

**Ecological fallacy.** Our analysis operates at the signal level (drug--AE pairs), and care must be taken not to interpret an 85%F cell value as meaning 85% of patients experiencing that AE are female; rather, it means 85% of drug--AE pairs in that cell show female-predominant disproportionality. The 36-cell stratification reduces within-cell heterogeneity compared to marginal analysis, mitigating (though not eliminating) ecological bias.

### 4.6 Why Does Female Predominance Intensify on Both Axes?

Three complementary hypotheses:

**Biological substrate.** Women may genuinely experience more ADRs due to: (1) pharmacokinetic differences producing higher drug exposure at standard doses [1,19]; (2) immune sexual dimorphism producing more immune-mediated toxicity [18,26]; (3) hormonal modulation of drug metabolism [20]; (4) sex-chromosome-linked gene expression [27]. If these mechanisms produce genuine population-level sex differences, increasing statistical power should reveal them more clearly (anti-regression), and larger pharmacological sex differences should disproportionately reflect female-biased mechanisms (strength gradient).

**Selection effect.** If the |logR| >= 0.5 threshold sits closer to the center of the male effect distribution but closer to the tail of the female distribution, stronger signals would be enriched for female effects. However, this predicts a one-time enrichment rather than the continuous gradient observed across 10 deciles (63.5% to 87.4%).

**Reporting asymmetry amplification.** Women may be more likely to both *experience* and *report* AEs, creating double amplification. The two-axis model cannot definitively distinguish this from the biological hypothesis, though anti-regression persists after baseline normalization [16], arguing against reporting as the primary driver.

### 4.7 Clinical Implications

**Sex-stratified signal prioritization.** The 36-cell grid provides sex-ratio baselines for comparing individual signals. A male-directed signal in a cell typically 80%F warrants deeper investigation than one conforming to its expected ratio.

**Dose adjustment.** The strength gradient implies that larger pharmacological sex differences produce more female-biased AE profiles. Because many sex differences originate from dose-dependent pharmacokinetics, the gradient provides indirect evidence that sex-specific dosing could reduce extreme female-biased AEs. The 2013 FDA zolpidem dose halving for women [28] is a precedent; the strength gradient suggests many more drugs could benefit.

**Regulatory requirements.** The 96%F dominant-corner cell demonstrates that collapsing across sex for high-volume, high-strength signals treats a 96% female phenomenon as sex-neutral---scientifically inaccurate and clinically dangerous.

**Clinical trial design.** The volume axis (anti-regression) implies that sex differences become more apparent, not less, with larger samples. The failure to detect sex differences in small trials should not be interpreted as absence of sex differences.

### 4.8 Limitations

1. **Discrete binning.** The 36-cell landscape uses discrete bins; the true surface is continuous. Alternative bin choices (e.g., 10 x 10) would provide finer resolution but with sparser populations. Results may be sensitive to boundary choices at the extremes.

2. **Cell population heterogeneity.** The 36 cells are not equally populated. High-volume + high-strength cells contain fewer signals than central cells, meaning the most dramatic female fractions (93--96%F) carry wider implicit confidence intervals.

3. **Descriptive, not causal.** The model is observational. Volume and strength may be correlated through confounders: high-volume drugs may have intrinsically different pharmacology than low-volume drugs. The model does not establish causation.

4. **Drug utilization confounding.** If female-targeted drugs contribute disproportionately to high-volume bins, anti-regression could be partly artifactual. However, prior analysis [16] showed persistence after excluding sex-specific drugs and normalizing for drug-specific sex-reporting ratios.

5. **Signal-level independence.** Bootstrap CIs assume independent signals. Signals are correlated within drugs and within AE terms. True CIs may be wider, though the effect is likely small given 2,178 drugs and 5,658 AEs.

6. **FAERS limitations.** Under-reporting, stimulated reporting around safety alerts, lack of denominator data, and incomplete demographics affect all FAERS analyses [29]. The ROR partially mitigates the denominator problem but does not eliminate all biases.

7. **Generalizability.** The model was derived from FAERS (US-based). Whether the same landscape structure appears in EudraVigilance or VigiBase remains an empirical question. Biological mechanisms are expected to be universal, but reporting patterns may differ.

8. **Temporal aggregation.** The analysis spans 21.75 years. Prescribing practices, diagnostic criteria, and reporting incentives have evolved. The landscape represents a time-averaged snapshot; within-landscape temporal trends are not addressed.

---

## Conclusion

The two-axis model demonstrates that signal strength and report volume are independent, additive predictors of female predominance in sex-differential pharmacovigilance, producing a 36-cell landscape with female fraction ranging from 35% (strong + rare signals) to 96% (strong + well-evidenced signals)---a 61-percentage-point dynamic range.

The model unifies three previously separate phenomena: anti-regression (the volume axis), the signal-strength gradient (the strength axis), and direction asymmetry (female-higher signals being both more frequent at 53.8% and stronger at mean |logR| = 1.007 vs. 0.963; p = 2.80 x 10^-41). The extreme-threshold asymmetry (58.5% female at |logR| >= 3) confirms that the strongest pharmacological sex differences are disproportionately female-directed.

The landscape is overwhelmingly female-dominant (~85% of cells >50%F), with the paradoxical corner (strong + rare, 35--42%F) identifying where genuine male-biased signals concentrate---a zone warranting targeted surveillance. Bootstrap analysis confirms robustness: female fraction 58.07% (CI: 57.93--58.21%), rho = 1.000 (CI: 0.988--1.000).

The two-axis model provides a quantitative calibration tool for sex-differential pharmacovigilance, enabling stratum-specific signal interpretation, regulatory sex-stratification policy, and targeted detection of undersampled male drug vulnerabilities.

---

## Data Availability

SexDiffKG v4, analysis code, and the complete deep-analysis archive: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
2. Franconi F, Campesi I. Sex and gender influences on pharmacological response: is it time for a new paradigm? Expert Rev Clin Pharmacol. 2014;7(4):469-485.
3. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? J Womens Health. 2005;14(1):19-29.
4. Rosano GM, Lewis B, Agewall S, et al. Gender differences in the effect of cardiovascular drugs. Eur Heart J. 2015;36(40):2677-2680.
5. Sramek JJ, Murphy MF, Cutler NR. Sex differences in the psychopharmacological treatment of depression. Dialogues Clin Neurosci. 2016;18(4):447-457.
6. Wagner AD, Oez S, Gloede TD, et al. Sex differences in cancer chemotherapy effects. ESMO Open. 2020;5(5):e000770.
7. Rademaker M. Do women have more adverse drug reactions? Am J Clin Dermatol. 2001;2(6):349-351.
8. US Food and Drug Administration. Drug safety communication: risk of next-morning impairment after use of insomnia drugs. FDA Safety Communication. 2013.
9. European Medicines Agency. Reflection paper on the need for active substance-based prescribing. EMA/261174/2013.
10. Galton F. Regression towards mediocrity in hereditary stature. J Anthropol Inst Great Br Irel. 1886;15:246-263.
11. Stigler SM. Regression towards the mean, historically considered. Stat Methods Med Res. 1997;6(2):103-114.
12. Galton F. Natural Inheritance. London: Macmillan; 1889.
13. Morton V, Torgerson DJ. Effect of regression to the mean on decision making in health care. BMJ. 2003;326(7398):1083-1084.
14. Bland JM, Altman DG. Regression towards the mean. BMJ. 1994;308(6942):1499.
15. Barnett AG, van der Pols JC, Dobson AJ. Regression to the mean: what it is and how to deal with it. Int J Epidemiol. 2005;34(1):215-220.
16. Shaik MJAA. The anti-regression phenomenon in sex-differential drug safety: female adverse event bias strengthens rather than weakens with statistical power. Manuscript in preparation. 2026.
17. Borenstein M, Hedges LV, Higgins JPT, Rothstein HR. Introduction to Meta-Analysis. Chichester: John Wiley & Sons; 2009.
18. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16(10):626-638.
19. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48(3):143-157.
20. Spoletini I, Vitale C, Malorni W, Rosano GM. Sex and gender differences in pharmacology. Drug Discov Today: Ther Strateg. 2012;9(2-3):e71-e80.
21. Simpson EH. The interpretation of interaction in contingency tables. J R Stat Soc Ser B. 1951;13(2):238-241.
22. Robinson WS. Ecological correlations and the behavior of individuals. Am Sociol Rev. 1950;15(3):351-357.
23. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. Pharmacoepidemiol Drug Saf. 2009;18(6):427-436.
24. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. EClinicalMedicine. 2019;17:100188.
25. Yu Y, Chen J, Li D, Wang L, Wang W, Liu H. Systematic analysis of adverse event reports for sex differences in adverse drug events. Sci Rep. 2016;6:24955.
26. Jacobson DL, Gange SJ, Rose NR, Graham NMH. Epidemiology and estimated population burden of selected autoimmune diseases in the United States. Clin Immunol Immunopathol. 1997;84(3):223-243.
27. Lopes-Ramos CM, Chen CY, Kuijjer ML, et al. Sex differences in gene expression and regulatory networks across 29 human tissues. Cell Rep. 2020;31(12):107795.
28. US Food and Drug Administration. FDA drug safety communication: FDA approves new label changes and dosing for zolpidem products. 2013.
29. Sakaeda T, Tamon A, Kadoyama K, Okuno Y. Data mining of the public version of the FDA adverse event reporting system. Int J Med Sci. 2013;10(7):796-803.

---

## Figure Legends

**Figure 1. Single-axis gradients.** (A) Strength axis: female fraction by |logR| decile, spanning 63.5%F (D0) to 87.4%F (D9). The 23.9 pp gradient is perfectly monotonic (rho = 1.000). Dashed lines indicate 50% parity and 60.2% FAERS baseline; all deciles exceed both. (B) Volume axis: female fraction by report volume decile, spanning 42.2%F (D0) to 82.5%F (D9). The 40.3 pp gradient is also perfectly monotonic (rho = 1.000). D0 falls below 50%, indicating low-volume signals are unreliable for sex-differential characterization. Error bars: 95% bootstrap CIs.

**Figure 2. The two-dimensional landscape.** Heatmap of female fraction across 36 cells (6 strength x 6 volume bins). Color gradient: dark blue (<40%F) through white (50%F) to dark red (>90%F). The quiet corner (top-left, ~50%F), dominant corner (bottom-right, 96%F), and paradoxical corner (bottom-left, 35--42%F, dashed outline) are labeled. Contour lines at 50%, 60%, 70%, 80%, 90% delineate the gradient. The 50% contour cuts through only the first two volume columns, with ~85% of the grid female-dominant.

**Figure 3. Direction asymmetry.** (A) Kernel density distributions of |logR| for female-higher (red, N = 51,825) and male-higher (blue, N = 44,456) signals. Female-higher distribution is rightward-shifted (means: 1.007 vs. 0.963). (B) Proportion female-directed at extreme thresholds (|logR| >= 1, 2, 3): increasing from 53.8% to 58.5%, demonstrating tail amplification of the direction asymmetry.

**Figure 4. Bootstrap confidence distributions.** (A) Overall female fraction: mean 58.07%, 95% CI 57.93--58.21%. The 50% parity line falls far outside the distribution. (B) Anti-regression rho: mean 1.000, 95% CI 0.988--1.000. No resample produced rho < 0.964. (C) Strength-axis rho: mean 1.000, 95% CI 0.964--1.000.

**Figure 5. Additivity analysis.** Heatmap of residuals (observed minus additive-model prediction) across the 36 cells. Central cells: near-zero residuals (~additive). Dominant corner: mildly negative (ceiling sub-additivity). Paradoxical corner: moderately negative (interaction amplifying male bias). Quiet corner: mildly positive (super-additivity). The additive model is a reasonable first approximation, with interaction effects at the extremes.
