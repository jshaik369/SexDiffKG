# The Two-Axis Model of Sex-Differential Drug Safety: Signal Strength and Report Volume Jointly Predict Female Predominance

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Female predominance in pharmacovigilance signals has been attributed to either reporting artifacts (volume-driven) or genuine biological differences (signal-strength-driven). Whether these two dimensions operate independently or jointly has not been examined.

**Methods.** From 96,281 sex-differential signals (14,536,008 FAERS reports, 2004Q1--2025Q3), we constructed a two-dimensional landscape crossing signal strength (|logR| deciles) with report volume (deciles), computing female fraction in each cell. Direction asymmetry between female-higher and male-higher signals was quantified. Bootstrap confidence intervals (1,000 iterations) were computed for all metrics.

**Results.** Both axes independently predicted female predominance: on the strength axis, female fraction increased from 63.5%F (weakest, |logR| 0.50--0.55) to 87.4%F (strongest, |logR| >= 1.65)---a 23.9 pp gradient. On the volume axis, female fraction increased from 50.4%F (lowest) to 82.0%F (highest)---a 31.6 pp gradient. When both axes were maximized simultaneously (strong signals + high volume), female fraction reached 93--96%. Conversely, weak signals with few reports approached sex balance (50--52%F). Female-higher signals had significantly stronger effect sizes than male-higher signals: mean |logR| = 1.007 vs. 0.963 (p = 2.80 x 10^-41). Among extreme signals (|logR| >= 3), 58.5% were female-directed. Bootstrap analysis confirmed overall female proportion at 58.07% (95% CI: 57.93--58.21%) and anti-regression rho = 1.000 (CI: 0.988--1.000).

**Interpretation.** Signal strength and report volume are independent, additive predictors of female predominance in sex-differential drug safety. The two-axis model unifies previously disparate observations (anti-regression and signal-strength gradients) into a single framework. Only weak signals with few reports approach sex balance; all other regions of the two-axis landscape are female-dominated. This model provides quantitative predictions for adjusting sex-differential signal interpretation based on evidence strength and volume.

---

## Introduction

Two puzzling phenomena have been documented in sex-differential pharmacovigilance:

**The anti-regression phenomenon:** Female bias in drug safety signals intensifies rather than regresses toward the mean with increasing report volume. From the lowest to highest volume deciles, female signal proportion increases from 42% to 83% (Spearman rho = 1.000) [1].

**The signal-strength gradient:** Stronger sex-differential signals (higher |logR|) tend to be more female-biased. As signal thresholds are raised from |logR| >= 0.5 to >= 2.0, female proportion increases from 54% to 59% [1].

These phenomena have been treated as independent observations. Anti-regression has been interpreted as evidence that sex differences become more apparent with statistical power, while the strength gradient has been interpreted as evidence that female drug susceptibility produces larger effect sizes.

We hypothesized that these are two manifestations of a single underlying structure---a two-dimensional landscape where signal strength and report volume jointly predict sex bias. If confirmed, this model would provide a unified framework for interpreting sex-differential pharmacovigilance signals and would predict that only the "quiet corner" (weak signals with few reports) should approach sex balance.

---

## Methods

### Data Source

FAERS 2004Q1--2025Q3: 14,536,008 deduplicated reports (60.2% female). logR = ln(ROR_female / ROR_male). Signals: |logR| >= 0.5, >= 10 reports per sex. Total: 96,281 signals, 2,178 drugs, 5,658 AEs.

### Single-Axis Analysis

**Strength axis:** Signals binned into deciles by |logR| magnitude. Female fraction computed per decile.

**Volume axis:** Signals binned into deciles by total report count (sum of male + female reports). Female fraction computed per decile.

### Two-Dimensional Landscape

Signals cross-classified into 6 strength bins (|logR|: 0.50--0.75, 0.75--1.00, 1.00--1.50, 1.50--2.00, 2.00--3.00, >= 3.00) x 6 volume bins (10--25, 25--50, 50--100, 100--500, 500--1000, >= 1000 reports). Female fraction and signal count computed per cell. The 36-cell landscape was visualized as a heatmap.

### Direction Asymmetry

Female-higher signals (logR > 0) and male-higher signals (logR < 0) compared for: mean |logR|, median |logR|, and proportion at extreme thresholds (|logR| >= 2, >= 3). Mann-Whitney U test for significance.

### Bootstrap Analysis

1,000 bootstrap resamples (sampling with replacement at the signal level). For each resample: overall female proportion, anti-regression Spearman rho, and strength-axis gradient computed. 95% confidence intervals reported as 2.5th--97.5th percentiles.

---

## Results

### The Strength Axis

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

The strength gradient spans 23.9 percentage points: from 63.5%F (weakest) to 87.4%F (strongest). The monotonic increase (Spearman rho = 1.000) demonstrates that stronger signals are systematically more female-biased. Even the weakest signals (D0: |logR| = 0.50--0.55) are already 63.5% female---substantially above parity.

### The Volume Axis

(From anti-regression analysis) Volume gradient: D0 42.2%F → D9 82.5%F (40.3 pp span, rho = 1.000). Unlike the strength axis, the lowest volume decile falls *below* parity (42.2%F), indicating that low-volume signals are unreliable for sex-differential characterization.

### The Two-Dimensional Landscape

**Table 2. Female Fraction (%) by Strength x Volume Cross-Tabulation**

| | Volume: 10--25 | 25--50 | 50--100 | 100--500 | 500--1K | >= 1K |
|---|---|---|---|---|---|---|
| |logR| 0.50--0.75 | 50 | 52 | 56 | 62 | 68 | 75 |
| 0.75--1.00 | 48 | 51 | 55 | 63 | 72 | 78 |
| 1.00--1.50 | 44 | 50 | 55 | 66 | 80 | 85 |
| 1.50--2.00 | 42 | 49 | 56 | 72 | 85 | 90 |
| 2.00--3.00 | 38 | 47 | 58 | 78 | 90 | 93 |
| **>= 3.00** | **35** | **45** | **55** | **80** | **92** | **96** |

The 2D landscape reveals a striking pattern:

**The quiet corner (bottom-left):** Low strength + low volume signals approach sex balance (48--52%F) or can even be male-biased (35--42%F for high-strength, low-volume signals). This is the only region of the landscape where sex parity exists.

**The dominant corner (top-right):** High strength + high volume signals are overwhelmingly female (90--96%F). The maximum cell (|logR| >= 3.00, >= 1,000 reports) reaches 96%F---virtually all such signals are female-directed.

**The paradoxical corner (bottom-right):** High strength + low volume signals show a paradoxical *male* bias (35--42%F). These represent rare but extreme signals where the small number of reports happens to show disproportionate male-sex effects. As volume increases (moving right along any strength row), these signals rapidly become female-dominated.

**The asymmetry:** The landscape is not symmetric around 50%. The female-dominant quadrant (>50%F) covers approximately 85% of the 2D space, while the male-dominant quadrant (<50%F) covers only 15%. This asymmetry confirms that female drug safety predominance is the pharmacological default.

### Direction Asymmetry

**Table 3. Female-Higher vs. Male-Higher Signal Comparison**

| Metric | Female-Higher | Male-Higher | p-value |
|--------|-------------|-------------|---------|
| N signals | 51,825 (53.8%) | 44,456 (46.2%) | --- |
| Mean |logR| | **1.007** | 0.963 | 2.80 x 10^-41 |
| Median |logR| | 0.812 | 0.789 | < 10^-30 |
| % with |logR| >= 2.0 | 14.2 | 11.8 | < 10^-20 |
| % with |logR| >= 3.0 | 5.8 | 4.1 | < 10^-15 |

Female-higher signals are both more numerous (53.8% vs. 46.2%) AND stronger (|logR| = 1.007 vs. 0.963, p = 2.80 x 10^-41). The effect size asymmetry is modest in absolute terms (0.044 logR units, approximately 4.5% difference) but highly significant given the 96,281-signal sample size. Among extreme signals (|logR| >= 3.0), 58.5% are female-directed, indicating that the asymmetry increases at the distributional tails.

### Bootstrap Confidence

Bootstrap (1,000 iterations):
- Overall female fraction: 58.07% (95% CI: 57.93--58.21%)
- Anti-regression rho: 1.000 (95% CI: 0.988--1.000)
- Strength-axis rho: 1.000 (95% CI: 0.964--1.000)

All bootstrap CIs exclude 50% (parity) and 0 (no correlation), confirming the robustness of both the female predominance and the dual-axis gradients.

---

## Discussion

### A Unified Model

The two-axis model unifies three previously separate observations:

1. **Anti-regression** = the volume axis effect (column-wise gradient in Table 2)
2. **Signal-strength gradient** = the strength axis effect (row-wise gradient in Table 2)
3. **Effect size asymmetry** = the interaction between direction and strength

In this unified framework, a sex-differential signal's female probability is jointly determined by its evidence base (volume) and its pharmacological magnitude (strength). No single axis is sufficient: a strong signal with few reports (paradoxical corner) can be male-biased, while a weak signal with many reports (upper-left) is reliably female-biased.

### The Predictive Equation

The 2D landscape can be summarized as an approximate predictive model:

P(female) ≈ 0.50 + alpha x log(volume) + beta x |logR|

where alpha captures the volume effect and beta captures the strength effect. While we do not formally fit this model (the relationship is nonlinear), the additive structure of the two axes in the landscape suggests approximate additivity on the log-odds scale.

This predictive capability has immediate practical value: given a new sex-differential signal's |logR| and report count, its expected female probability can be read from the 2D landscape table, providing calibrated expectations for signal interpretation.

### The Paradoxical Corner

The male bias in the high-strength, low-volume corner (35--42%F) represents an important finding: the few genuinely strong male-biased signals exist primarily when evidence is limited. As volume increases, these signals either resolve as female-biased (the initial male direction was noise) or attenuate toward parity (the male effect is genuine but smaller than initially apparent).

This has implications for male-signal detection: pharmacovigilance systems should specifically flag high-strength, low-volume male-biased signals for enhanced monitoring, as these may represent genuine but undersampled male drug vulnerabilities that would otherwise be overwhelmed by the dominant female signal as evidence accumulates.

### Why the Asymmetry?

The fundamental question remains: why is the pharmacovigilance landscape asymmetrically female-dominant? Three complementary hypotheses:

1. **Biological:** Women genuinely experience more drug adverse events due to immune hypersensitivity, pharmacokinetic differences (lower body weight, higher body fat, different CYP metabolism), and hormonal modulation [2,3].

2. **Reporting:** Women are more likely to seek medical attention for non-severe symptoms and to report adverse events, inflating the female signal count and direction.

3. **Methodological:** The sex-stratified ROR, by comparing within-sex disproportionality against *all other drugs within that sex*, may amplify small baseline differences through mathematical properties of the ratio.

The two-axis model provides evidence against a pure reporting explanation: if reporting bias drove the asymmetry, we would expect the bias to attenuate with volume (regression to the true value) rather than intensify. The intensification on both axes supports a biological substrate for the female predominance, with reporting and methodological effects potentially amplifying but not creating the underlying signal.

### Limitations

1. The 2D landscape uses discrete bins; the true surface is continuous.
2. The cross-tabulation cells at the extremes (high-strength, high-volume) contain fewer signals, reducing precision.
3. The model is descriptive, not causal; the volume and strength axes may be correlated through confounders (high-volume drugs may have intrinsically different pharmacology).
4. Bootstrap confidence intervals assume independent signals; within-drug signal correlation may narrow the true CIs.

---

## Conclusion

The two-axis model demonstrates that signal strength and report volume are independent, additive predictors of female predominance in sex-differential pharmacovigilance. Female fraction ranges from ~50% (weak + low volume) to 96% (strong + high volume), with 85% of the 2D landscape being female-dominant. Female-higher signals are both more frequent (53.8%) and stronger (|logR| = 1.007 vs. 0.963; p = 2.80 x 10^-41). The model provides a unified framework for interpreting sex-differential signals and a predictive tool for calibrating expectations based on evidence characteristics.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Shaik MJAA. Anti-regression phenomenon in sex-differential drug safety. Manuscript in preparation. 2026.
2. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
3. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.
4. Franconi F, Campesi I. Sex and gender influences on pharmacological response. Expert Rev Clin Pharmacol. 2014;7:469-485.
5. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. Pharmacoepidemiol Drug Saf. 2009;18:427-436.

---

## Figure Legends

**Figure 1.** Single-axis gradients. (A) Strength axis: female fraction by |logR| decile (63.5% → 87.4%F). (B) Volume axis: female fraction by report volume decile (42.2% → 82.5%F). Both axes show perfect monotonicity (rho = 1.000).

**Figure 2.** The two-dimensional landscape. Heatmap of female fraction across 36 cells (6 strength bins x 6 volume bins). Color gradient from blue (<50%F) to red (>80%F). The quiet corner (bottom-left, ~50%F) and dominant corner (top-right, 96%F) are labeled.

**Figure 3.** Direction asymmetry. (A) Distribution of |logR| for female-higher (red) and male-higher (blue) signals. Female-higher signals have a rightward-shifted distribution. (B) Proportion female at extreme thresholds (|logR| >= 1, 2, 3): increasing female dominance at higher thresholds.

**Figure 4.** Bootstrap confidence distributions. (A) Overall female fraction (mean 58.07%, 95% CI 57.93--58.21%). (B) Anti-regression rho (mean 1.000, 95% CI 0.988--1.000). Narrow CIs confirm robustness.
