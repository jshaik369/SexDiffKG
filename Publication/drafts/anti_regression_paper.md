# Sex-Differential Drug Safety Signals Exhibit Systematic Anti-Regression:
# Higher Report Volumes Amplify Rather Than Dilute Sex Differences

## Authors
Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)
CoEvolve Network, Independent Researcher, Barcelona, Spain
ORCID: 0009-0002-1748-7516

## Abstract
Conventional pharmacovigilance assumes that sex-differential adverse event reporting ratios converge toward population baselines as report volumes increase, following regression to the mean. Using 14.5 million FAERS reports spanning 87 quarters (2004Q1-2025Q3), we demonstrate the opposite: sex-differential drug safety signals exhibit systematic "anti-regression" where female bias monotonically increases from 42.2% (lowest volume decile) to 82.5% (highest volume decile). Simultaneously, effect sizes strengthen from mean |log-ratio| = 0.87 to 1.35. This phenomenon persists across all 23 MedDRA System Organ Classes and is robust to multiple threshold sensitivities (53.8%F at |LR|≥0.5 → 59.4%F at |LR|≥2.0). We further show that female-higher signals carry statistically significantly stronger effect sizes (mean |LR| = 1.007 vs 0.963, p = 3.07×10⁻³⁷). These findings challenge fundamental assumptions in pharmacovigilance and suggest that sex-differential drug responses represent genuine biological signals that are amplified, not diluted, by increased clinical exposure.

## Introduction
Regression to the mean is a statistical cornerstone in signal detection. When early reports suggest a drug-adverse event association differs by sex, the default assumption is that this apparent sex difference will diminish as more data accumulates. This assumption underlies current pharmacovigilance practice where initial sex-skewed signals are often deprioritized as likely artifacts of small sample sizes.

We challenge this assumption using the largest sex-stratified pharmacovigilance analysis to date.

## Methods
### Data Source
- FDA Adverse Event Reporting System (FAERS): 14,536,008 deduplicated reports
- 8,744,397 female reports, 5,791,611 male reports
- 87 quarters from 2004Q1 through 2025Q3
- Drug name normalization: DiAna dictionary (846,917 mappings, 53.9% resolution)

### Signal Detection
- Reporting Odds Ratios (ROR) computed separately for each sex
- Log-ratio of sex-specific RORs as effect size measure
- Minimum 500 total reports, significance threshold |LR| ≥ 0.5
- 96,281 sex-differential signals across 2,178 drugs and 5,069 adverse events

### Anti-Regression Analysis
- Report volume decile stratification (10 equal-frequency bins)
- Mean |log-ratio| and female-higher percentage per decile
- Threshold sensitivity analysis at |LR| cutoffs from 0.5 to 3.0
- Wilcoxon rank-sum and KS tests for distributional differences

## Results
### The Anti-Regression Phenomenon
Report volume decile analysis reveals a striking monotonic pattern:
- D0 (lowest volume): 42.2% female-higher, mean |LR| = 0.8708
- D5 (median): 51.5% female-higher, mean |LR| = 0.9364
- D9 (highest volume): 82.5% female-higher, mean |LR| = 1.3513

This represents a 40.3 percentage point increase in female bias and a 55.2% increase in effect size from the lowest to highest volume decile.

### Female Signals Are Stronger
Female-higher signals (N=51,771) exhibit significantly greater effect sizes than male-higher signals (N=44,510):
- Female mean |LR| = 1.0072 vs Male mean |LR| = 0.9631
- t-test: t = 12.76, p = 3.07 × 10⁻³⁷
- KS-test: D = 0.039, p = 1.42 × 10⁻³¹

### Severity Amplification
The female bias is most pronounced in serious adverse events:
- Serious AEs: 65.6% female-higher (N=2,701)
- Moderate AEs: 53.5% female-higher (N=90,147)
- Mild AEs: 52.6% female-higher (N=3,433)

### Threshold Robustness
Female bias increases with stronger effect size thresholds:
- |LR| ≥ 0.5: 53.8%F (all 96,281 signals)
- |LR| ≥ 1.0: 56.4%F (32,244 signals)
- |LR| ≥ 2.0: 59.4%F (5,467 signals)
- |LR| ≥ 3.0: 58.5%F (1,028 signals)

### Power Law Distribution
Signal distribution follows a power law with significant inequality:
- Top 1% of drugs account for 12.5% of all signals
- Top 1% of AEs account for 14.5% of all signals
- Drug signal Gini coefficient: 0.746
- AE signal Gini coefficient: 0.750

## Discussion
The anti-regression phenomenon represents a fundamental challenge to current pharmacovigilance assumptions. Rather than converging toward sex-neutral baselines with increased data, sex-differential safety signals become MORE pronounced with greater clinical exposure. This suggests these signals reflect genuine sex-dependent pharmacology — including differences in drug metabolism (CYP enzyme expression), body composition (fat distribution, organ size), immune function, and hormonal milieu — rather than statistical artifacts.

The finding that serious adverse events show the strongest female bias (65.6%F) has immediate clinical implications, suggesting that current drug safety monitoring may systematically under-detect female-specific risks for life-threatening reactions.

## Clinical Implications
1. Early sex-differential signals should be amplified, not discounted, in pharmacovigilance
2. Drugs with emerging female-biased safety signals warrant enhanced female-specific monitoring
3. Clinical trial sex-stratified analysis should be mandatory given persistent biological differences
4. 82.5% female bias in highest-volume signals indicates systematic under-recognition of female drug risks
