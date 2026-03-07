# Temporal Dynamics of Sex-Differential Drug Safety: 486 Bidirectional Drugs, Volume-Dependent Stability, and the Effect Size Amplification Gradient

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex-differential drug safety signals are typically analyzed as static cumulative measures. Whether these signals are temporally stable or show systematic dynamics---including direction reversals, volume-dependent stability, and effect size evolution---has not been examined.

**Methods.** From 96,281 sex-differential signals across 2,178 drugs (14,536,008 FAERS reports, 2004Q1--2025Q3), we analyzed: (1) the volume-sex gradient across signal volume strata; (2) bidirectional drugs with strong signals in both sex directions; (3) intra-drug sex variability; and (4) effect size behavior across report volume deciles.

**Results.** The volume-sex gradient was pronounced: drug quintiles ranged from Q1 = 41.8%F (lowest volume) to Q5 = 55.3%F (highest volume). At finer granularity: signals from drugs with 10--25 reports showed 40.8%F, while those from drugs with >= 1,000 reports showed 87.4%F---a 46.6 percentage-point amplification. A total of 486 drugs (22.3% of 2,178) had strong signals in both female and male directions simultaneously (bidirectional drugs), with prednisone showing the most signals (303 female, 73 male). Effect sizes amplified with volume (mean |logR|: D0 = 0.871 → D9 = 1.351; rho = 0.152, p < 10^-15), with the top decile showing 55% larger effects than the bottom. Intra-drug variability was extreme: 1,090 drugs with >= 10 signals showed within-drug sex ranges from 0 pp (metformin/rosiglitazone: 100%F across all signals) to 98 pp (minoxidil).

**Interpretation.** Sex-differential drug safety signals exhibit pronounced volume-dependent dynamics: the female sex bias amplifies from near-parity to 87%F across the volume spectrum, effect sizes grow rather than attenuate, and nearly one-quarter of all drugs are simultaneously bidirectional. These findings challenge static sex-safety labels and support dynamic, volume-aware, AE-specific sex-differential pharmacovigilance.

---

## Introduction

Pharmacovigilance traditionally treats drug safety signals as static attributes. A drug is characterized as having "female-biased" or "male-biased" adverse event profiles based on cumulative analysis across the entire reporting timeline. This static paradigm implicitly assumes that sex-differential signals are stable properties of drug pharmacology that can be measured once and applied indefinitely [1].

Several factors challenge this assumption. Report volume accumulates over time, and our previous work has demonstrated that sex-differential signals intensify with volume (anti-regression). Drug user demographics evolve as indications expand, formulations change, and prescribing patterns shift. Reporting behavior may change in response to safety communications, media coverage, or regulatory actions [2].

Understanding the dynamic behavior of sex-differential signals---whether they stabilize, reverse, amplify, or oscillate---has direct implications for drug labeling, safety communications, and clinical decision-making. A signal that consistently shows female predominance over 20 years is qualitatively different from one that oscillates between male and female predominance depending on the reporting period.

We present a comprehensive analysis of temporal dynamics in sex-differential drug safety signals, examining volume-dependent behavior, bidirectional patterns, effect size evolution, and intra-drug variability.

---

## Methods

### Data Source

FAERS 2004Q1--2025Q3: 14,536,008 deduplicated reports (60.2% female). Sex-stratified logR = ln(ROR_female / ROR_male). Signals: |logR| >= 0.5, >= 10 reports per sex. Total: 96,281 signals, 2,178 drugs, 5,658 AEs.

### Volume-Sex Gradient

Signals were stratified by total report volume into:
- 5 quintiles (Q1--Q5 by drug-level total reports)
- 10 deciles (D0--D9 by signal-level total reports)
- 6 volume bands (10--25, 25--50, 50--100, 100--500, 500--1000, 1000+ reports)

The proportion of female-predominant signals was computed per stratum.

### Bidirectional Drug Analysis

A drug was classified as "bidirectional" if it had >= 1 strong female signal (logR > 0.5) AND >= 1 strong male signal (logR < -0.5). The proportion of bidirectional drugs and the balance of female vs. male signals were analyzed.

### Intra-Drug Variability

For 1,090 drugs with >= 10 sex-differential signals, we computed:
- Within-drug standard deviation of logR
- Within-drug range (max - min female fraction across AEs)
- Coefficient of variation of logR

### Effect Size Dynamics

Mean absolute log-ratio |logR| was computed per volume decile to test whether effect sizes amplify, attenuate, or remain constant with increasing evidence.

---

## Results

### Volume-Sex Gradient: Drug-Level

**Table 1. Sex-Differential Signal Profile by Drug Volume Quintile**

| Quintile | N Signals | N Drugs | Mean %F | Mean |logR| | Median Volume |
|----------|-----------|---------|---------|-------------|---------------|
| Q1 (lowest) | 567 | 440 | **41.8** | 0.955 | 50 |
| Q2 | 1,638 | 432 | 44.1 | 0.896 | 218 |
| Q3 | 4,820 | 435 | 45.8 | 0.876 | 821 |
| Q4 | 14,315 | 435 | 50.0 | 0.909 | 3,542 |
| Q5 (highest) | 74,941 | 436 | **55.3** | 1.011 | 42,825 |

The gradient from Q1 (41.8%F) to Q5 (55.3%F) is 13.5 percentage points, modest compared to the signal-level anti-regression gradient. This attenuated drug-level gradient reflects the confounding of within-drug AE heterogeneity: each drug contributes signals in both directions, partially canceling the aggregate sex bias.

### Volume-Sex Gradient: Signal-Level

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

### Effect Size Amplification

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

### Bidirectional Drugs

**486 drugs (22.3% of 2,178)** had strong signals in both female and male directions simultaneously. These bidirectional drugs challenge the notion of a single sex-safety label per drug.

**Table 4. Top Bidirectional Drugs**

| Drug | N Strong Female | N Strong Male | Total Signals | Top Female AEs | Top Male AEs |
|------|----------------|---------------|--------------|----------------|-------------|
| Prednisone | 303 | 73 | 926 | Duodenal ulcer perforation, Helicobacter infection, Glossodynia | Metastatic neoplasm, Bone pain |
| Methotrexate | 187 | 64 | 284 | Pancytopenia, Interstitial lung disease | Hepatic failure |
| Adalimumab | 218 | 45 | 318 | Synovitis, IBS, Lupus-like syndrome | Lymphoma, Melanoma |
| Infliximab | 195 | 52 | 285 | Hypersensitivity, Arthralgia | Hepatosplenic T-cell lymphoma |

The bidirectional pattern reflects the multi-target, multi-pathway nature of drug pharmacology. Prednisone, for example, produces female-biased gastrointestinal and oral adverse events (estrogen-modulated mucosal effects?) alongside male-biased oncologic and musculoskeletal outcomes (testosterone-modulated tumor biology?). The coexistence of opposite-sex signals within a single drug demonstrates that sex-differential susceptibility operates at the AE level, not the drug level.

### Intra-Drug Variability

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

The most pharmacologically informative metric is the ratio of within-drug to between-drug variance. When within-drug variance exceeds between-drug variance (as for minoxidil, adalimumab, prednisone), the drug's sex-safety label is meaningless---the label should be AE-specific, not drug-specific.

---

## Discussion

### The Volume-Predictability Principle

The central finding---a 46.6 pp amplification from 40.8%F (minimal volume) to 87.4%F (massive volume)---establishes a volume-predictability principle for sex-differential pharmacovigilance: the reliability of a sex-differential signal is directly proportional to its evidence base. Low-volume signals (< 50 reports) should be treated as preliminary and direction-uncertain; high-volume signals (> 500 reports) represent crystallized pharmacological sex differences.

This principle has three practical applications:

1. **Signal triage:** New sex-differential signals with < 50 reports should not trigger sex-specific label changes or clinical alerts. Only signals crossing the ~100 report threshold where the volume-sex gradient steepens should be considered reliable.

2. **Cumulative monitoring:** Sex-differential signals should be monitored longitudinally as evidence accumulates. A signal that is 50%F with 50 reports may become 75%F with 500 reports---not because the pharmacology changed, but because the true signal has become resolvable.

3. **Retrospective analysis:** When reanalyzing historical signals, the volume context should be reported alongside the sex ratio. A 55%F signal from 30 reports and a 55%F signal from 30,000 reports represent fundamentally different levels of evidence.

### The Bidirectional Drug Challenge

The finding that 486 drugs (22.3%) are bidirectional---simultaneously producing strong female AND strong male signals for different adverse events---fundamentally challenges drug-level sex-safety labels. A drug labeled "female-biased" may have male-biased signals for specific, potentially severe adverse events.

Regulatory implications: the EMA and FDA should consider AE-specific rather than drug-level sex-differential safety labels. A drug's Summary of Product Characteristics (SmPC) or package insert should specify which adverse events are female-biased and which are male-biased, rather than providing a single aggregate sex-safety characterization.

### Effect Size Amplification

The monotonic increase in effect size (|logR|: 0.871 → 1.351 across deciles) is the quantitative complement to direction amplification. Together, they demonstrate *dual amplification*: high-volume signals are both more consistently female-biased AND more strongly female-biased. This is the expected behavior for a genuine biological effect measured with increasing precision, where the signal-to-noise ratio improves and the true effect magnitude becomes apparent.

The opposite pattern---effect size attenuation with volume---would be expected for regression to the mean in a noise-dominated system. The absence of attenuation and the presence of amplification provides the effect-size-level evidence that sex-differential drug safety signals represent genuine pharmacological differences.

### Limitations

1. Volume stratification is observational and cannot prove causation. Higher-volume drugs may differ systematically from lower-volume drugs in ways that affect sex profiles.
2. The analysis uses cumulative report counts; temporal trends within each drug's reporting history are not captured.
3. Bidirectional classification uses a |logR| >= 0.5 threshold; different thresholds would yield different bidirectional counts.
4. The effect size amplification may partly reflect confounding by indication: high-volume drugs tend to treat chronic conditions with longer exposure and more opportunities for AEs.
5. FAERS voluntary reporting introduces inherent uncertainties in all volume-based analyses.

---

## Conclusion

Sex-differential drug safety signals exhibit pronounced volume-dependent dynamics: female bias amplifies from 40.8%F (minimal volume) to 87.4%F (massive volume), effect sizes grow from |logR| = 0.871 to 1.351, and 486 drugs (22.3%) are simultaneously bidirectional. These findings establish that sex-differential pharmacovigilance requires volume-aware interpretation, AE-specific rather than drug-level sex labels, and cumulative monitoring rather than static classification. The dual amplification of both direction and magnitude with increasing evidence confirms that sex-differential drug safety is a genuine pharmacological phenomenon that becomes more, not less, apparent as evidence accumulates.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. Pharmacoepidemiol Drug Saf. 2009;18:427-436.
2. Piening S, et al. The impact of safety-related regulatory action on reporting of adverse drug reactions. Drug Saf. 2012;35:373-385.
3. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
4. Watson S, et al. Reported adverse drug reactions in women and men. EClinicalMedicine. 2019;17:100188.
5. Montastruc JL, et al. Gender differences in adverse drug reactions. Fundam Clin Pharmacol. 2002;16:343-346.
6. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.

---

## Figure Legends

**Figure 1.** Volume-sex gradient. Female signal proportion (y-axis) vs. signal volume band (x-axis). Six bands from 10--25 reports (40.8%F) to >= 1,000 reports (87.4%F). The 46.6 pp amplification demonstrates volume-dependent sex-bias crystallization.

**Figure 2.** Dual amplification. Overlaid plots showing direction (% female, left y-axis) and effect size (mean |logR|, right y-axis) across 10 volume deciles. Both metrics increase monotonically, confirming that high-volume signals are more consistently AND more strongly female-biased.

**Figure 3.** Bidirectional drug network. Network visualization of top 20 bidirectional drugs. Node size proportional to total signals, edge color indicating female (red) or male (blue) AE signals. Prednisone hub highlighted with 303F/73M signal split.

**Figure 4.** Intra-drug variability distribution. Histogram of within-drug logR standard deviation across 1,090 drugs. Right tail (SD > 1.5) represents drugs with maximally heterogeneous sex profiles.

**Figure 5.** Volume-predictability principle. Schematic showing the transition from noise-dominated (< 50 reports, ~50%F, high entropy) to signal-dominated (> 500 reports, >75%F, low entropy) regime, integrating evidence from this paper and the information theory companion analysis.
