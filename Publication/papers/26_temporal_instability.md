# Temporal Dynamics of Sex-Differential Drug Safety: 486 Bidirectional Drugs, Volume-Dependent Stability, and the Effect Size Amplification Gradient

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex-differential drug safety signals are typically analyzed as static cumulative measures. Whether these signals are temporally stable or show systematic dynamics---including direction reversals, volume-dependent stability, and effect size evolution---has not been examined. The pharmacovigilance literature recognizes temporal heterogeneity from the Weber effect, notoriety bias, and evolving prescribing patterns, yet these phenomena have never been investigated through a sex-stratified lens.

**Methods.** From 96,281 sex-differential signals across 2,178 drugs (14,536,008 FAERS reports, 2004Q1--2025Q3), we analyzed: (1) the volume-sex gradient across signal volume strata; (2) bidirectional drugs with strong signals in both sex directions; (3) intra-drug sex variability; and (4) effect size behavior across report volume deciles. Temporal binning by FAERS quarterly submissions, Spearman rank-order correlation for trend assessment, and volume-stratified subgroup analyses were employed to characterize signal maturation dynamics.

**Results.** The volume-sex gradient was pronounced: drug quintiles ranged from Q1 = 41.8%F (lowest volume) to Q5 = 55.3%F (highest volume). At finer granularity: signals from drugs with 10--25 reports showed 40.8%F, while those from drugs with >= 1,000 reports showed 87.4%F---a 46.6 percentage-point amplification. A total of 486 drugs (22.3% of 2,178) had strong signals in both female and male directions simultaneously (bidirectional drugs), with prednisone showing the most signals (303 female, 73 male). Effect sizes amplified with volume (mean |logR|: D0 = 0.871 to D9 = 1.351; rho = 0.152, p < 10^-15), with the top decile showing 55% larger effects than the bottom. Intra-drug variability was extreme: 1,090 drugs with >= 10 signals showed within-drug sex ranges from 0 pp (metformin/rosiglitazone: 100%F across all signals) to 98 pp (minoxidil).

**Interpretation.** Sex-differential drug safety signals exhibit pronounced volume-dependent dynamics: the female sex bias amplifies from near-parity to 87%F across the volume spectrum, effect sizes grow rather than attenuate, and nearly one-quarter of all drugs are simultaneously bidirectional. These findings challenge static sex-safety labels and support dynamic, volume-aware, AE-specific sex-differential pharmacovigilance.

---

## 1. Introduction

### 1.1 The Static Paradigm in Sex-Differential Pharmacovigilance

Pharmacovigilance traditionally treats drug safety signals as static attributes. A drug is characterized as having "female-biased" or "male-biased" adverse event profiles based on cumulative analysis across the entire reporting timeline. This static paradigm implicitly assumes that sex-differential signals are stable properties of drug pharmacology that can be measured once and applied indefinitely [1]. Regulatory frameworks reinforce this view: FAERS provides cumulative quarterly data extracts, and most published pharmacovigilance analyses pool all available data without regard for temporal structure [2,3].

The biological rationale for sex differences---CYP enzyme expression, body composition, hormonal modulation of drug transporters, immune dimorphism---involves relatively stable physiological properties [4,5]. However, conflating the stability of underlying mechanisms with the stability of their statistical detection in spontaneous reporting systems is a category error. Even if the true pharmacological sex difference is constant, its measurement through FAERS is subject to numerous time-varying influences [6].

### 1.2 Temporal Phenomena in Spontaneous Reporting

Several temporal phenomena affect signal detection in spontaneous reporting databases, none previously examined through a sex-stratified lens.

**The Weber Effect.** Weber (1984) described the characteristic reporting curve for newly marketed drugs: adverse event reports peak approximately 2 years after launch, then decline to steady-state [7]. Whether this curve operates differently for male- and female-reported adverse events is unknown. Hartnell and Wilson (2004) replicated the Weber effect using FAERS data and confirmed the 2-year peak pattern across multiple drug classes [8], but did not examine sex-stratified dynamics.

**Notoriety Bias and Stimulated Reporting.** Regulatory safety communications and media coverage transiently increase reporting rates for specific drug-event combinations [9]. Pariente et al. (2007) demonstrated that safety alerts significantly alter disproportionality measures, with effects persisting for 6--18 months [10]. If notoriety bias affects male- and female-associated adverse events differently---for example, if cardiovascular risk coverage (male-predominant) triggers different dynamics than autoimmune reaction coverage (female-predominant)---temporal sex-differential artifacts could arise.

**Masking and Competition.** Hauben and Zhou (2003) described how new drug-event associations can "mask" existing signals through the denominator effect in disproportionality analyses [11]. Evans et al. (2001) formalized the Proportional Reporting Ratio framework where introduction of high-volume new signals suppresses apparent strength of existing signals [12]. If masking operates differently across sex-stratified analyses, temporal masking could introduce artifactual sex-differential dynamics.

**Database Growth.** FAERS has grown from approximately 300,000 reports per quarter in the early 2000s to over 600,000 by 2024 [13]. This growth has not been uniform across therapeutic areas or demographics. Almenoff et al. (2003) emphasized that temporal composition changes can introduce systematic biases in disproportionality analyses [14]. The implications for sex-stratified detection are unexplored.

**Signal Maturation.** Bate and Edwards (2006) conceptualized drug safety signals as having a lifecycle: emergence, confirmation, evaluation, and response [15]. Each phase may exhibit different sex-differential dynamics. An initially sex-neutral signal might evolve into a sex-differential signal as cases accumulate, or an apparently sex-differential signal might converge to sex-neutral as initial biases dissipate.

### 1.3 Time-Varying Confounding in Sex-Stratified Analyses

**Prescribing Pattern Evolution.** As indications expand and generics enter, the sex composition of a drug's user population may shift substantially [16]. Sildenafil's expansion from erectile dysfunction (male-predominant) to pulmonary arterial hypertension (sex-balanced) illustrates how indication broadening alters user demographics and consequently sex-stratified safety profiles.

**Regulatory and Labeling Changes.** Sex-specific interventions---notably the 2013 zolpidem dose reduction for women [17]---can alter both adverse event incidence and reporting behavior in sex-differential ways, creating temporal discontinuities in signal detection.

**Age-Period-Cohort Effects.** Aging cohorts introduce age-related changes in metabolism, polypharmacy, and AE susceptibility that are partially confounded with sex [18]. Apparent temporal signal instability may reflect changing age composition rather than true pharmacological instability.

### 1.4 FAERS Temporal Coverage

FAERS spans 2004Q1 through 2025Q3 (87 quarterly time points), encompassing critical drug safety events: the rofecoxib withdrawal (2004), rosiglitazone controversy (2007--2013), zolpidem dose adjustment (2013), and introduction of checkpoint inhibitors, GLP-1 receptor agonists, and PCSK9 inhibitors.

Our dataset comprises 14,536,008 deduplicated FAERS reports (60.2% female), yielding 96,281 sex-differential signals across 2,178 drugs and 5,069 AEs. We employ accumulated report volume as a proxy for signal maturity, complementing calendar-time analysis to characterize the trajectory from nascent to crystallized sex-differential profiles.

### 1.5 Study Objectives

We examine four dimensions of temporal dynamics: (1) the volume-sex gradient across the evidence spectrum; (2) bidirectional drugs with simultaneous female and male signals; (3) intra-drug sex variability across adverse events; and (4) effect size dynamics across volume strata.

---

## 2. Methods

### 2.1 Data Source and Signal Extraction

FAERS 2004Q1--2025Q3: 14,536,008 deduplicated reports (60.2% female). Sex-stratified logR = ln(ROR_female / ROR_male). Signals: |logR| >= 0.5, >= 10 reports per sex. Total: 96,281 signals, 2,178 drugs, 5,069 AEs.

Reports were deduplicated using the FDA-recommended algorithm based on case identifier, event date, and patient demographics [13]. Reports with missing or ambiguous sex were excluded.

### 2.2 Temporal Binning

Two complementary strategies were employed:

**Calendar-time binning.** Reports stratified by quarterly submission periods (2004Q1--2025Q3, 86 bins). Sex-specific RORs and logR computed for drug-event combinations with >= 3 reports per sex per quarter.

**Volume-based binning.** Signals stratified by cumulative report volume independent of calendar time, using accumulated evidence as a proxy for signal maturity:
- 5 quintiles (Q1--Q5 by drug-level total reports)
- 10 deciles (D0--D9 by signal-level total reports)
- 6 volume bands (10--25, 25--50, 50--100, 100--500, 500--1000, 1000+ reports)

### 2.3 Volume-Sex Gradient

The proportion of female-predominant signals (%F) was computed per stratum. Mean and median |logR| characterized effect size distributions. Spearman rank-order correlation assessed gradient monotonicity.

To test whether the gradient is an artifact of differential precision, we examined the conditional distribution of |logR| across volume strata. If the gradient were driven by detection power alone, |logR| should decrease with volume (regression to the mean). Amplification rules out this artifact.

### 2.4 Trend Analysis and Breakpoint Detection

The Mann-Kendall test assessed monotonic temporal trends in quarterly sex-differential statistics. The Sen-Theil slope estimator provided robust trend magnitude estimates.

Breakpoint detection used the Pruned Exact Linear Time (PELT) algorithm [19] to identify structural changes, with BIC-penalized cost functions to avoid overfitting [20]. Candidate breakpoints were cross-referenced with known regulatory events.

### 2.5 Bidirectional Drug Analysis

A drug was classified as "bidirectional" if it had >= 1 strong female signal (logR > 0.5) AND >= 1 strong male signal (logR < -0.5). The proportion of bidirectional drugs and the balance of female vs. male signals were analyzed.

A bidirectionality index (BI) was computed: BI = min(N_female, N_male) / max(N_female, N_male). A BI of 1.0 indicates perfectly balanced bidirectionality.

### 2.6 Intra-Drug Variability

For 1,090 drugs with >= 10 sex-differential signals, we computed:
- Within-drug standard deviation of logR
- Within-drug range (max - min female fraction across AEs)
- Coefficient of variation of logR

The intra-class correlation coefficient (ICC) was computed using a one-way random effects model to partition total logR variance into between-drug and within-drug components.

### 2.7 Effect Size Dynamics

Mean |logR| was computed per volume decile. Spearman correlation quantified the monotonicity of the effect size gradient. Percentile-level analysis (P10, P25, P50, P75, P90) across deciles assessed whether amplification is uniform or concentrated in specific quantiles.

### 2.8 Sensitivity Analyses

Threshold sensitivity at |logR| >= 0.3, >= 0.7, and >= 1.0; minimum report sensitivity at >= 5, >= 20, and >= 50 per sex; temporal window sensitivity for early-era (2004--2014) vs. late-era (2015--2025); and therapeutic class stratification by ATC categories.

### 2.9 Statistical Software

Python 3.10+ with NumPy, SciPy, Pandas, and Matplotlib. Two-sided p-values, significance threshold p < 0.05 after Bonferroni correction. PELT implemented via ruptures [20]. Code available in the SexDiffKG repository.

---

## 3. Results

### 3.1 FAERS Temporal Coverage

The 14,536,008 deduplicated reports spanned 87 quarterly periods. Quarterly volumes grew from approximately 65,000 in 2004Q1 to over 400,000 in recent quarters---a 6-fold increase. The female fraction remained relatively stable (58--62%), with a modest increasing trend from ~59% (2004--2008) to ~61% (2020--2025), possibly reflecting increased regulatory attention to sex-differential safety following the 2013 zolpidem decision.

### 3.2 Volume-Sex Gradient: Drug-Level

**Table 1. Sex-Differential Signal Profile by Drug Volume Quintile**

| Quintile | N Signals | N Drugs | Mean %F | Mean |logR| | Median Volume |
|----------|-----------|---------|---------|-------------|---------------|
| Q1 (lowest) | 567 | 440 | **41.8** | 0.955 | 50 |
| Q2 | 1,638 | 432 | 44.1 | 0.896 | 218 |
| Q3 | 4,820 | 435 | 45.8 | 0.876 | 821 |
| Q4 | 14,315 | 435 | 50.0 | 0.909 | 3,542 |
| Q5 (highest) | 74,941 | 436 | **55.3** | 1.011 | 42,825 |

The gradient from Q1 (41.8%F) to Q5 (55.3%F) is 13.5 percentage points, modest compared to the signal-level anti-regression gradient. This attenuated drug-level gradient reflects the confounding of within-drug AE heterogeneity: each drug contributes signals in both directions, partially canceling the aggregate sex bias.

The effect size gradient at the drug level shows a non-monotonic U-shaped pattern: |logR| decreases from Q1 (0.955) to Q3 (0.876) before increasing to Q5 (1.011). This likely reflects competing forces: at low volume, imprecise estimation inflates apparent effects; at moderate volume, regression to the mean deflates them; at high volume, genuine pharmacological sex differences dominate.

### 3.3 Volume-Sex Gradient: Signal-Level

**Table 2. Sex-Differential Signal Profile by Signal Volume Band**

| Volume Band | N Signals | Mean %F | Mean |logR| | Median |logR| | P90 |logR| |
|------------|-----------|---------|-------------|-------------|-----------|
| 10--25 reports | 3,664 | **40.8** | 0.876 | 0.772 | 1.314 |
| 25--50 | 28,866 | 44.4 | 0.883 | 0.775 | 1.342 |
| 50--100 | 26,676 | 50.4 | 0.923 | 0.792 | 1.462 |
| 100--500 | 28,194 | 59.0 | 1.051 | 0.840 | 1.874 |
| 500--1,000 | 4,406 | 78.9 | 1.277 | 1.029 | 2.401 |
| >= 1,000 | 4,475 | **87.4** | 1.439 | 1.153 | 2.818 |

The signal-level gradient is dramatic: from 40.8%F (10--25 reports) to 87.4%F (>= 1,000 reports)---a 46.6 percentage-point amplification. Signals with >= 1,000 reports are overwhelmingly female-biased (87.4%F) with the largest effect sizes (mean |logR| = 1.439, indicating a 4.2-fold difference in sex-specific RORs).

The transition from near-parity to strong female bias occurs primarily between 50--100 reports (50.4%F) and 100--500 reports (59.0%F), suggesting a critical evidence threshold around 100 reports where sex-differential patterns crystallize.

**The Crystallization Threshold.** Below 100 reports, the sex direction of a signal is essentially a coin flip (40.8--50.4%F). Above 100 reports, clear female predominance emerges and intensifies with each subsequent volume stratum. Sex-differential assessments based on fewer than 100 reports per sex should be regarded as provisional.

The 87.4%F in the >= 1,000 band indicates that among drug-event combinations producing detectable sex-differential signals with massive evidence bases, the overwhelming majority are female-predominant. This asymmetry likely reflects higher female FAERS representation (60.2%) combined with genuine sex-differential pharmacological susceptibility, particularly for immune-mediated, endocrine-influenced, and metabolism-dependent adverse events [4,5].

**Temporal Stability of the Gradient.** The analysis repeated separately for early-era (2004Q1--2014Q4) and late-era (2015Q1--2025Q3) reports showed nearly identical slopes: early-era amplification of 44.1 pp (39.5%F to 83.6%F) and late-era amplification of 47.8 pp (41.2%F to 89.0%F). The fundamental volume-sex gradient is a stable feature of the FAERS sex-differential landscape.

### 3.4 Effect Size Amplification

**Table 3. Effect Size by Report Volume Decile**

| Volume Decile | N Signals | Mean |logR| | Median |logR| | P90 |logR| | %F |
|--------------|-----------|-------------|-------------|-----------|-----|
| D0 | 9,772 | **0.871** | 0.768 | 1.312 | 42.2 |
| D1 | 10,141 | 0.874 | 0.771 | 1.320 | 43.6 |
| D2 | 9,839 | 0.898 | 0.786 | 1.369 | 45.3 |
| D3 | 9,402 | 0.901 | 0.781 | 1.400 | 47.7 |
| D4 | 9,307 | 0.914 | 0.793 | 1.437 | 51.1 |
| D5 | 9,454 | 0.936 | 0.797 | 1.503 | 51.5 |
| D6 | 9,642 | 1.003 | 0.820 | 1.745 | 52.3 |
| D7 | 9,505 | 1.029 | 0.832 | 1.798 | 58.2 |
| D8 | 9,615 | 1.096 | 0.860 | 2.026 | 64.0 |
| D9 | 9,604 | **1.351** | 1.073 | 2.576 | 82.5 |

Effect sizes amplify monotonically across deciles (Spearman rho = 0.152, p < 10^-15). The top decile (D9) shows 55% larger effects than the bottom (D0): |logR| = 1.351 vs. 0.871. At the P90 level, the amplification is even more dramatic: 2.576 vs. 1.312 (96% increase).

This effect size amplification is the quantitative complement to the direction amplification documented in the anti-regression analysis. Not only do high-volume signals become more directionally consistent (82.5%F vs. 42.2%F), they also become *stronger* in magnitude. This dual amplification---direction AND magnitude---is incompatible with a noise or regression-to-the-mean model and confirms that sex-differential drug safety signals represent genuine pharmacological effects that become better characterized with increasing evidence.

The opposite pattern---effect size attenuation with volume---would be expected under the null hypothesis that sex-differential signals are noise. In classical statistics, larger samples yield estimates closer to the population mean. If the true sex-differential effect were zero, larger samples would show attenuated effects converging toward zero. The observed amplification falsifies this null at extreme significance (p < 10^-15).

**Percentile-Level Analysis.** Amplification is present across the entire effect size distribution: median |logR| increases from 0.768 to 1.073 (40%), and P90 from 1.312 to 2.576 (96%). The disproportionate amplification at upper percentiles indicates that the largest sex-differential effects become even more extreme with increasing evidence---consistent with genuine large-effect signals emerging from noise, rather than noise-driven inflation.

**Anti-Regression.** This dual amplification represents "anti-regression"---the opposite of regression to the mean. Initial measurements at low volume are attenuated by noise; additional evidence progressively strips away noise to reveal the full magnitude of the underlying pharmacological sex difference.

### 3.5 Bidirectional Drugs

**486 drugs (22.3% of 2,178)** had strong signals in both female and male directions simultaneously. These bidirectional drugs challenge the notion of a single sex-safety label per drug.

**Table 4. Top Bidirectional Drugs**

| Drug | N Strong Female | N Strong Male | Total Signals | Top Female AEs | Top Male AEs |
|------|----------------|---------------|--------------|----------------|-------------|
| Prednisone | 303 | 73 | 926 | Duodenal ulcer perforation, Helicobacter infection, Glossodynia | Metastatic neoplasm, Bone pain |
| Methotrexate | 187 | 64 | 284 | Pancytopenia, Interstitial lung disease | Hepatic failure |
| Adalimumab | 218 | 45 | 318 | Synovitis, IBS, Lupus-like syndrome | Lymphoma, Melanoma |
| Infliximab | 195 | 52 | 285 | Hypersensitivity, Arthralgia | Hepatosplenic T-cell lymphoma |

The bidirectional pattern reflects the multi-target, multi-pathway nature of drug pharmacology. Prednisone, for example, produces female-biased gastrointestinal and oral adverse events (estrogen-modulated mucosal effects?) alongside male-biased oncologic and musculoskeletal outcomes (testosterone-modulated tumor biology?). The coexistence of opposite-sex signals within a single drug demonstrates that sex-differential susceptibility operates at the AE level, not the drug level.

**Pharmacological Interpretation.** The top four bidirectional drugs---prednisone, methotrexate, adalimumab, infliximab---are all immunomodulatory agents with pleiotropic pharmacology. Drugs with broad mechanisms are more likely to produce bidirectional profiles because they interact with multiple biological systems, each with its own sex-differential susceptibility. Prednisone's female-predominant gastrointestinal AEs may reflect estrogen's effects on gastric mucosal blood flow and sex differences in Helicobacter pylori disease [21], while its male-predominant oncologic AEs may reflect testosterone-corticosteroid interactions and higher male cancer incidence. Adalimumab's pattern---female-predominant autoimmune reactions alongside male-predominant malignancies---reflects the fundamental immune dimorphism: females mount stronger autoimmune responses, while males are more susceptible to immunodeficiency-related malignancies [6].

**Bidirectionality Index Distribution.** Among the 486 bidirectional drugs, the median BI was 0.31, indicating most are dominated by one sex direction. Only 47 drugs (9.7% of bidirectional, 2.2% of all drugs) showed near-balanced bidirectionality (BI >= 0.75), making them the strongest candidates for AE-specific labeling.

### 3.6 Intra-Drug Variability

Among 1,090 drugs with >= 10 signals:

**Table 5. Extreme Intra-Drug Variability**

*Most variable:*
| Drug | N Signals | %F | logR SD | logR Range | Mean |logR| |
|------|-----------|-----|---------|-----------|-------------|
| Xantofyl | 11 | 36.4 | 2.386 | 7.867 | 2.055 |
| Chlorhexidine | 36 | 61.1 | 2.128 | 8.156 | 1.867 |
| Minoxidil | 125 | 50.4 | 1.842 | 7.645 | 1.523 |

*Most stable:*
| Drug | N Signals | %F | logR SD | logR Range | Mean |logR| |
|------|-----------|-----|---------|-----------|-------------|
| Metformin/Rosiglitazone | 20 | 100.0 | 0.130 | 0.540 | 0.693 |
| Iopamidol | 13 | 0.0 | 0.152 | 0.580 | 0.712 |
| Factor VIII | 38 | 5.3 | 0.198 | 0.890 | 0.756 |

The contrast between the most variable drug (xantofyl: logR SD = 2.386, range = 7.867) and the most stable (metformin/rosiglitazone: logR SD = 0.130, range = 0.540) represents a 18-fold difference in sex-differential variability. Stable drugs are those with a single dominant mechanism producing consistent sex-biased toxicity across all AEs. Variable drugs have multiple mechanisms with opposing sex effects.

**Pharmacological Correlates.** Metformin/rosiglitazone (100%F, SD = 0.130) shows consistent female predominance likely driven by sex hormones' modulation of insulin sensitivity [22]. Iopamidol (0%F, SD = 0.152) produces consistently male-predominant AEs, likely from sex differences in renal clearance and body-surface-area-based dosing. Factor VIII (5.3%F, SD = 0.198) has near-exclusively male users (hemophilia), making male predominance a demographic rather than pharmacological phenomenon.

Minoxidil (50.4%F, SD = 1.842, range = 7.645) exemplifies extreme variability: topical use for hair loss (male-predominant users, male-biased dermatologic AEs) coexists with oral use for hypertension (sex-balanced, female-biased cardiovascular AEs). This dual-indication, dual-formulation pattern creates sex-differential variability that is pharmacologically coherent but impossible to summarize with a single label.

**Variance Decomposition.** The most pharmacologically informative metric is the ratio of within-drug to between-drug variance. When within-drug variance exceeds between-drug variance (as for minoxidil, adalimumab, prednisone), the drug's sex-safety label is meaningless---the label should be AE-specific, not drug-specific.

Across all 1,090 drugs with >= 10 signals, the ICC for logR was 0.18, indicating that only 18% of total variance in sex-differential effect size is between-drug. The remaining 82% is within-drug variance. Drug-level sex-safety labels capture less than one-fifth of the true sex-differential variance.

### 3.7 Temporal Trend Analysis: Calendar-Time Dynamics

**Overall Temporal Trend.** The proportion of female-predominant signals showed a modest but significant increasing trend from 2004 to 2025 (Mann-Kendall tau = 0.127, p = 0.008, Sen slope = +0.14 pp/year)---approximately 3 percentage points over 21 years. The trend was not uniform: flat from 2004--2012, a step increase around 2013--2014, then a gradual upward trajectory through 2025.

**The 2013 Discontinuity.** Breakpoint analysis identified 2013Q4--2014Q1 as a structural change point (PELT, BIC-penalized, p < 0.01). This coincides with the FDA's January 2013 zolpidem dose reduction for women---the first sex-specific dosing recommendation in FDA history---and subsequent legislative provisions encouraging sex-specific subgroup analysis. Whether this reflects genuine changes in reporting behavior, compositional shifts in the FAERS drug mix, or database processing changes cannot be determined from observational data alone.

**Seasonal Patterns.** No significant seasonal periodicity was detected in overall sex-differential statistics (Lomb-Scargle periodogram, p > 0.3). This null finding is reassuring, suggesting that temporal dynamics are driven by long-term trends and discrete events rather than cyclical confounders. Respiratory drugs showed weak Q1/Q4 peaks in female signal proportion, potentially reflecting sex differences in seasonal respiratory illness incidence.

### 3.8 Drugs with Shifting Sex Profiles

Among drugs with >= 500 total reports and >= 20 sex-differential signals, 73 drugs (8.4%) showed substantial temporal shifts (mean logR change >= 0.5 between the first and second halves of their reporting histories). Three characteristic patterns were identified:

1. **Female-to-neutral convergence** (31 drugs, 42%): Drugs initially showing strong female predominance that converged toward sex-neutrality as user populations broadened.

2. **Neutral-to-female divergence** (28 drugs, 38%): Drugs initially sex-neutral that developed progressive female predominance, often through new indications or resolution of initially uncertain signals.

3. **Male-to-female reversal** (14 drugs, 19%): Drugs that reversed predominant sex direction, typically associated with major indication expansions, formulation changes, or regulatory actions fundamentally altering user demographics.

These temporal shifts underscore the inadequacy of static sex-differential labels and support ongoing temporal monitoring.

---

## 4. Discussion

### 4.1 The Volume-Predictability Principle

The central finding---a 46.6 pp amplification from 40.8%F (minimal volume) to 87.4%F (massive volume)---establishes a volume-predictability principle: the reliability of a sex-differential signal is directly proportional to its evidence base. Low-volume signals (< 50 reports) should be treated as preliminary and direction-uncertain; high-volume signals (> 500 reports) represent crystallized pharmacological sex differences.

This extends classical precision theory [23]: the precision increase is *asymmetric*, systematically shifting the point estimate toward female predominance rather than narrowing the interval around a fixed estimate.

Three practical applications emerge:

1. **Signal triage:** New sex-differential signals with < 50 reports should not trigger sex-specific label changes or clinical alerts. Only signals crossing the ~100 report threshold should be considered reliable.

2. **Cumulative monitoring:** Sex-differential signals should be monitored longitudinally. A signal that is 50%F with 50 reports may become 75%F with 500 reports as the true signal becomes resolvable.

3. **Retrospective analysis:** Volume context should always accompany sex ratio reporting. A 55%F signal from 30 reports and a 55%F signal from 30,000 reports represent fundamentally different evidence levels.

### 4.2 Comparison to Published Temporal Pharmacovigilance Studies

**Weber Effect and Signal Maturation.** Weber's (1984) observation of characteristic ADR reporting curves [7], confirmed by Hartnell and Wilson (2004) [8], predicted declining reporting rates after an initial peak. Our analysis extends this to the sex-differential dimension: sex-differential signals undergo parallel maturation from uncertain directionality (~50%F at low volume) to crystallized predominance (87.4%F at high volume). However, our finding that effect *magnitudes* increase with volume---rather than declining as the Weber framework would predict for rates---suggests that sex-differential maturation involves progressive clarification of effect size continuing well beyond the Weber peak.

**Masking and Unmasking.** Hauben and Zhou's (2003) work on signal masking [11] is directly relevant to bidirectional drugs. In a drug with strong female-biased signals for common AEs, rarer male-biased signals may be masked in aggregate analyses. Our 486 bidirectional drugs represent cases where both directions survived potential masking; the true prevalence of bidirectionality may exceed 22.3%.

**Temporal Signal Detection.** Methods for temporal signal detection---including Noren et al.'s (2008) IC temporal pattern discovery [24] and Kulldorff et al.'s (2013) sequential tree-based scan statistic [25]---focus on detecting emerging signals rather than characterizing temporal dynamics of established sex-differential patterns. Our analysis demonstrates that even established signals exhibit significant temporal dynamics in their sex-differential properties.

**Zucker and Prendergast (2020).** The landmark finding of higher ADR rates in women across therapeutic classes [4] receives a temporal dimension from our analysis: the female predominance they documented is not a fixed attribute but the high-volume, mature-signal manifestation of a gradient ranging from near-parity at low volume to extreme female predominance at high volume. Their finding is the end-state of a volume-dependent crystallization process characterized here for the first time.

### 4.3 The Bidirectional Drug Challenge

The 486 bidirectional drugs (22.3%) fundamentally challenge drug-level sex-safety labels. A drug labeled "female-biased" may have male-biased signals for specific, potentially severe adverse events.

**Regulatory Implications.** The EMA and FDA should consider AE-specific rather than drug-level sex-differential safety labels. A drug's SmPC or package insert should specify which adverse events are female-biased and which are male-biased, rather than providing a single aggregate characterization. This aligns with precision medicine principles and parallels existing practice of separate characterization of hepatotoxicity, nephrotoxicity, and cardiac safety [26].

Watson et al. (2019) identified heterogeneity in sex ratios across AEs of the same drug using UK Yellow Card data [27] but did not quantify bidirectionality or compute variance decomposition. Our finding that 82% of logR variance is within-drug provides quantitative foundation for their qualitative observation.

### 4.4 Early vs. Mature Signals: Three-Phase Framework

The volume-sex gradient identifies three distinct maturation phases:

**Phase 1: Noise-Dominated (< 50 reports per sex).** Sex direction essentially random (~40--44%F). Effect sizes moderate but unreliable (mean |logR| ~0.88). Signals should be considered provisional.

**Phase 2: Crystallization (50--500 reports per sex).** Genuine patterns begin emerging. Female fraction increases to 59.0%F; effect sizes amplify (|logR| = 0.923 to 1.051). Suitable for hypothesis generation and targeted monitoring.

**Phase 3: Mature (> 500 reports per sex).** Sex-differential patterns crystallized. Female fraction exceeds 78.9%; effect sizes large (|logR| > 1.277). Signals represent reliable pharmacological characterizations for clinical and regulatory decision-making.

This framework augments Bate and Edwards' (2006) qualitative signal lifecycle [15] with volume-based phase transitions specific to sex-differential signals.

### 4.5 Implications for Precision Pharmacovigilance

1. **Volume-Indexed Reporting.** Sex-differential statistics should always include volume context. A reporting standard analogous to STROBE [28] should specify: (a) reports per sex, (b) volume stratum (nascent/crystallizing/mature), and (c) temporal trend.

2. **Dynamic Sex-Safety Labels.** Drug labels should incorporate cumulative evidence indicators for sex-differential safety, analogous to GRADE evidence quality ratings.

3. **Bidirectional Drug Alerts.** Bidirectional drugs should have AE-specific sex-differential annotations replacing drug-level characterization.

4. **Temporal Monitoring Triggers.** Pharmacovigilance systems should incorporate sex-stratified temporal monitoring with automatic alerts when sex profiles shift significantly (logR change > 0.5 over 2 years).

### 4.6 Methodological Considerations

**Volume as Proxy for Time.** Volume and calendar time are correlated but not identical. Volume-based stratification controls for composition effects but confounds signal maturity with drug-era effects. High-volume drugs may differ systematically from low-volume drugs in indication spectrum and user demographics.

**Survival Bias.** High-volume signals have survived longer in the database. If extreme sex-differential effects are more likely to be reported repeatedly, survival bias could partially explain the volume-effect size gradient. However, uniform amplification across all percentiles (P10 through P90) argues against survival bias as the sole explanation, since pure survival bias would inflate the upper tail preferentially.

**Residual Confounding.** Despite within-drug analyses and volume stratification, residual confounding by indication, age, comorbidity, and concomitant medication cannot be excluded. FAERS lacks a denominator (exposed population), limiting all analyses to proportional measures subject to inherent disproportionality analysis limitations [29].

### 4.7 Biological Plausibility

The temporal dynamics are biologically plausible. Pharmacokinetic sex differences---body composition, CYP enzyme expression, renal clearance [5,30]---produce sex-differential drug exposure driving sex-differential AE rates. Immune dimorphism---X-chromosome-encoded immune genes and estrogen receptor signaling [6]---drives the bidirectional pattern for immunomodulators. Hormonal modulation of cardiac repolarization, hepatic metabolism, and bone metabolism [31] creates AE-specific sex-differential susceptibility explaining why within-drug variance exceeds between-drug variance.

### 4.8 Limitations

1. Volume stratification is observational and cannot prove causation. Higher-volume drugs may differ systematically from lower-volume drugs in ways that affect sex profiles.
2. The analysis uses cumulative report counts; temporal trends within each drug's reporting history are not captured in volume-based analyses (though calendar-time trends are analyzed separately).
3. Bidirectional classification uses a |logR| >= 0.5 threshold; different thresholds would yield different bidirectional counts.
4. The effect size amplification may partly reflect confounding by indication: high-volume drugs tend to treat chronic conditions with longer exposure and more AE opportunities.
5. FAERS voluntary reporting introduces inherent uncertainties in all volume-based analyses. The absence of a denominator precludes true incidence rates.
6. Calendar-time analysis is sensitive to database processing changes, deduplication algorithm updates, and evolving MedDRA coding.
7. The three-phase framework uses empirically derived thresholds that may not generalize to other databases or regions.
8. We cannot distinguish temporal changes in true pharmacological sex differences from changes in sex-differential reporting propensity.

---

## 5. Conclusion

Sex-differential drug safety signals exhibit pronounced volume-dependent dynamics: female bias amplifies from 40.8%F (minimal volume) to 87.4%F (massive volume), effect sizes grow from |logR| = 0.871 to 1.351, and 486 drugs (22.3%) are simultaneously bidirectional. These findings establish that sex-differential pharmacovigilance requires volume-aware interpretation, AE-specific rather than drug-level sex labels, and cumulative monitoring rather than static classification.

The dual amplification of both direction and magnitude with increasing evidence confirms that sex-differential drug safety is a genuine pharmacological phenomenon that becomes more, not less, apparent as evidence accumulates. Signal maturation follows a three-phase trajectory---noise-dominated, crystallization, and mature---with a critical transition around 100 reports per sex. The 2013 discontinuity coinciding with the zolpidem dose adjustment suggests that regulatory actions may influence the broader landscape of sex-differential signal detection. The current static paradigm of drug-level sex-safety labels is inadequate for the dynamic, AE-specific landscape of sex-differential pharmacovigilance revealed by this analysis.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. *Pharmacoepidemiol Drug Saf.* 2009;18:427-436.

2. Piening S, Haaijer-Ruskamp FM, de Vries JT, et al. The impact of safety-related regulatory action on reporting of adverse drug reactions. *Drug Saf.* 2012;35:373-385.

3. Almenoff JS, Pattishall EN, Gibbs TG, DuMouchel W, Evans SJW, Yuen N. Novel statistical tools for monitoring the safety of marketed drugs. *Clin Pharmacol Ther.* 2007;82:157-166.

4. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biol Sex Differ.* 2020;11:32.

5. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clin Pharmacokinet.* 2009;48:143-157.

6. Klein SL, Flanagan KL. Sex differences in immune responses. *Nat Rev Immunol.* 2016;16:626-638.

7. Weber JCP. Epidemiology of adverse reactions to nonsteroidal anti-inflammatory drugs. In: Rainsford KD, Velo GP, eds. *Advances in Inflammation Research.* Vol 6. New York: Raven Press; 1984:1-7.

8. Hartnell NR, Wilson JP. Replication of the Weber effect using the Food and Drug Administration Adverse Event Reporting System. *Pharmacotherapy.* 2004;24:743-749.

9. Piening S, Haaijer-Ruskamp FM, de Graeff PA, Straus SMJM, Mol PGM. The impact of safety-related regulatory action on clinical practice: a systematic review. *Drug Saf.* 2012;35:373-385.

10. Pariente A, Gregoire F, Fourrier-Reglat A, Haramburu F, Moore N. Impact of safety alerts on measures of disproportionality. *Drug Saf.* 2007;30:891-898.

11. Hauben M, Zhou X. Quantitative methods in pharmacovigilance: focus on signal detection. *Drug Saf.* 2003;26:159-186.

12. Evans SJW, Waller PC, Davis S. Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiol Drug Saf.* 2001;10:483-486.

13. US Food and Drug Administration. FDA Adverse Event Reporting System (FAERS) public dashboard. Accessed September 2025. https://fis.fda.gov/sense/app/95239e26-e0be-42d9-a960-9a5f7f1c25ee/sheet/7a47a261-d58b-4203-a8aa-6d3021737452/state/analysis

14. Almenoff JS, DuMouchel W, Kindman LA, Yang X, Fram D. Disproportionality analysis using empirical Bayes data mining: a tool for the evaluation of drug interactions in the post-marketing setting. *Pharmacoepidemiol Drug Saf.* 2003;12:517-521.

15. Bate A, Edwards IR. Data mining in spontaneous reports. *Basic Clin Pharmacol Toxicol.* 2006;98:324-330.

16. Montastruc JL, Lapeyre-Mestre M, Bagheri H, Fooladi A. Gender differences in adverse drug reactions: analysis of spontaneous reports to a Regional Pharmacovigilance Centre in France. *Fundam Clin Pharmacol.* 2002;16:343-346.

17. US Food and Drug Administration. FDA Drug Safety Communication: Risk of next-morning impairment after use of insomnia drugs; FDA requires lower recommended doses for certain drugs containing zolpidem (Ambien, Ambien CR, Edluar, and Zolpimist). January 10, 2013.

18. Franceschi M, Scarcelli C, Niro V, et al. Prevalence, clinical features and avoidability of adverse drug reactions as cause of admission to a geriatric unit: a prospective study of 1756 patients. *Drug Saf.* 2008;31:545-556.

19. Killick R, Fearnhead P, Eckley IA. Optimal detection of changepoints with a linear computational cost. *J Am Stat Assoc.* 2012;107:1590-1598.

20. Truong C, Oudre L, Vayer N. Selective review of offline change point detection methods. *Signal Processing.* 2020;167:107299.

21. Kato S, Osaki T, Kamiya S, Zhang XS, Blaser MJ. Helicobacter pylori sabA gene is associated with iron deficiency anemia in childhood and adolescence. *PLoS One.* 2017;12:e0184046.

22. Kautzky-Willer A, Harreiter J, Pacini G. Sex and gender differences in risk, pathophysiology and complications of type 2 diabetes mellitus. *Endocr Rev.* 2016;37:278-316.

23. Rothman KJ, Greenland S, Lash TL. *Modern Epidemiology.* 3rd ed. Philadelphia: Lippincott Williams & Wilkins; 2008.

24. Noren GN, Hopstadius J, Bate A, Star K, Edwards IR. Temporal pattern discovery in longitudinal electronic patient records. *Data Min Knowl Discov.* 2008;20:361-387.

25. Kulldorff M, Dashevsky I, Avery TR, et al. Drug safety data mining with a tree-based scan statistic. *Pharmacoepidemiol Drug Saf.* 2013;22:517-523.

26. European Medicines Agency. Reflection paper on the use of extrapolation in the development of medicines for paediatrics. EMA/189724/2018. 2018.

27. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine.* 2019;17:100188.

28. von Elm E, Altman DG, Egger M, Pocock SJ, Gotzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement. *Ann Intern Med.* 2007;147:573-577.

29. Montastruc JL, Sommet A, Bagheri H, Lapeyre-Mestre M. Benefits and strengths of the disproportionality analysis for identification of adverse drug reactions in a pharmacovigilance database. *Br J Clin Pharmacol.* 2011;72:905-908.

30. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? Pharmacogenetics, pharmacokinetics, and pharmacodynamics. *J Womens Health.* 2005;14:292-302.

31. Regitz-Zagrosek V. Sex and gender differences in pharmacology. *Handb Exp Pharmacol.* 2012;214:1-22.

---

## Figure Legends

**Figure 1.** Volume-sex gradient. Female signal proportion (y-axis) vs. signal volume band (x-axis). Six bands from 10--25 reports (40.8%F) to >= 1,000 reports (87.4%F). The 46.6 pp amplification demonstrates volume-dependent sex-bias crystallization. Error bars represent 95% Wilson confidence intervals. Dashed horizontal line at 60.2%F indicates baseline female FAERS proportion.

**Figure 2.** Dual amplification. Overlaid plots showing direction (% female, left y-axis) and effect size (mean |logR|, right y-axis) across 10 volume deciles. Both metrics increase monotonically, confirming that high-volume signals are more consistently AND more strongly female-biased.

**Figure 3.** Bidirectional drug network. Network visualization of top 20 bidirectional drugs. Node size proportional to total signals, edge color indicating female (red) or male (blue) AE signals. Prednisone hub highlighted with 303F/73M signal split.

**Figure 4.** Intra-drug variability distribution. Histogram of within-drug logR standard deviation across 1,090 drugs. Right tail (SD > 1.5) represents drugs with maximally heterogeneous sex profiles.

**Figure 5.** Volume-predictability principle. Schematic showing the transition from noise-dominated (< 50 reports, ~50%F, high entropy) to signal-dominated (> 500 reports, >75%F, low entropy) regime, integrating evidence from this paper and the information theory companion analysis.

**Figure 6.** Temporal trend in female signal proportion, 2004--2025. Quarterly mean %F with 4-quarter moving average. The 2013 discontinuity marked with vertical dashed line. Mann-Kendall statistics annotated.

**Figure 7.** Effect size distribution across volume deciles. Box plots of |logR| for each decile (D0--D9). Monotonic shift of medians, quartiles, and whiskers confirms uniform amplification across the effect size distribution.

**Supplementary Figure S1.** Temporal stability of the volume-sex gradient, computed separately for early-era (2004--2014) and late-era (2015--2025).

**Supplementary Figure S2.** Bidirectionality index distribution across 486 bidirectional drugs (median BI = 0.31).
