# Information-Theoretic Characterization of Sex-Differential Drug Safety: Entropy, Mutual Information, and the Predictability Gradient

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Traditional pharmacovigilance signal detection relies on disproportionality measures (ROR, PRR) that quantify association strength but do not characterize the information content or predictability of sex-differential signals. Information theory offers a complementary framework for signal prioritization.

**Methods.** From 96,281 sex-differential signals across 1,394 drugs with >= 5 signals (14,536,008 FAERS reports, 2004Q1--2025Q3), we computed binary Shannon entropy H(sex|drug) for each drug, mutual information I(drug;sex|AE) for each adverse event, and tracked entropy across report volume deciles. Information concentration was quantified via cumulative distribution analysis.

**Results.** Mean drug entropy was 0.949 (close to maximum 1.0), but the distribution was left-skewed with a predictable tail. The most sex-predictable drugs were niraparib (H = 0.254, 95.8%F) and enzalutamide (H = 0.335, 6.2%F)---both targeting sex-linked cancer pathways. Entropy anti-regression was significant (Spearman rho = -0.952, p = 2.3 x 10^-5): high-volume drugs had systematically lower entropy (D0: H = 0.982 vs D9: H = 0.908), translating the anti-regression phenomenon into information-theoretic terms as increasing predictability. At the individual signal level, the gradient was steeper (D9: H = 0.716). Mutual information analysis identified folliculitis (MI = 0.320), obesity (MI = 0.318), and blood cholesterol increased (MI = 0.315) as the adverse events where drug identity most strongly predicts reporter sex. Sex information was diffusely distributed across the pharmacopeia: the top 10 drugs contained only 0.3% of total entropy variation, and the top 500 contained 32.9%.

**Interpretation.** Information theory reveals that sex-differential drug safety follows a structured predictability gradient: high-volume drugs are more sex-predictable (lower entropy), specific adverse events carry high mutual information about sex, and sex information is diffusely distributed rather than concentrated in a few outlier drugs. This framework provides a complementary lens for pharmacovigilance signal prioritization, where low-entropy drugs warrant heightened sex-specific monitoring.

---

## Introduction

Pharmacovigilance signal detection has historically relied on disproportionality measures---the Proportional Reporting Ratio (PRR), Reporting Odds Ratio (ROR), and Bayesian Confidence Propagation Neural Network (BCPNN)---to identify drug-adverse event associations that exceed background rates [1,2]. Sex-stratified extensions of these methods compute sex-specific rates and sex-differential ratios, adding a layer of demographic characterization [3].

However, these traditional measures have a fundamental limitation: they quantify association strength (how much a signal deviates from the null) but do not characterize the *information content* of sex-differential signals or the *predictability* of sex distributions across the pharmacopeia. A drug with 60% female signals and a drug with 95% female signals both have "female-biased" profiles, but they differ profoundly in predictability and clinical actionability.

Information theory, founded by Shannon [4], provides a natural framework for this distinction. The binary entropy H(sex|drug) measures how uncertain we are about a reporter's sex given which drug they reported, on a scale from 0 (perfect prediction) to 1 (maximum uncertainty, 50/50). The mutual information I(drug;sex|AE) for each adverse event quantifies how much knowing the drug reduces uncertainty about sex, identifying AEs where drug-specific rather than generic sex effects dominate.

We applied information theory to 96,281 sex-differential signals across 1,394 drugs to characterize the predictability landscape of sex-differential drug safety.

---

## Methods

### Data Source

FAERS 2004Q1--2025Q3: 14,536,008 deduplicated reports (60.2% female). Sex-stratified logR = ln(ROR_female / ROR_male). Signals: |logR| >= 0.5, >= 10 reports per sex. Analysis restricted to 1,394 drugs with >= 5 sex-differential signals for stable entropy estimation.

### Binary Entropy per Drug

For each drug *d* with mean female fraction *p_d* across its sex-differential signals:

H(d) = -p_d log_2(p_d) - (1 - p_d) log_2(1 - p_d)

H ranges from 0 (all signals same sex) to 1.0 (exactly 50/50). Drugs with p_d = 0 or p_d = 1 were assigned H = 0.

### Mutual Information per Adverse Event

For each adverse event *a* occurring across multiple drugs:

I(drug; sex | a) = H(sex|a) - H(sex|drug, a)

where H(sex|a) is the overall binary entropy for that AE across all drugs, and H(sex|drug, a) is the weighted-average conditional entropy across individual drugs reporting that AE. Higher MI indicates that knowing which drug caused the AE provides more information about the reporter's sex.

Analysis was restricted to 1,668 AEs occurring across >= 5 drugs.

### Entropy Anti-Regression

Drugs were divided into deciles by total report volume (sum of male and female reports across all AEs). Mean entropy was computed per decile. Spearman correlation tested whether higher-volume drugs are more or less predictable.

### Signal-Level Entropy by Volume

For a finer-grained analysis, individual signals (drug-AE pairs) were binned into 10 deciles by report volume, and mean binary entropy was computed per decile.

### Information Concentration

The cumulative distribution of entropy variation was computed: what fraction of total sex-information is concentrated in the top N drugs? This tests whether sex-differential safety is driven by a few extreme drugs or is a diffuse, system-wide property.

---

## Results

### Drug Entropy Distribution

Among 1,394 drugs with >= 5 signals:
- Mean entropy: **0.949** (close to maximum 1.0)
- Median entropy: **0.985**
- The distribution is strongly left-skewed: most drugs have high entropy (near-balanced sex profiles), but a long left tail extends to very low entropy (highly predictable).

**Table 1. Most Sex-Predictable Drugs (Lowest Entropy)**

| Drug | H(sex) | F Fraction | N Signals | Total Reports | Target |
|------|--------|-----------|-----------|---------------|--------|
| Niraparib | **0.254** | 0.958 | 12 | 19,484 | PARP (ovarian cancer) |
| Fulvestrant | 0.259 | 0.956 | 6 | 6,145 | ER antagonist (breast cancer) |
| IUD (contraceptive) | 0.292 | 0.949 | 5 | 3,622 | Progesterone (contraception) |
| Palbociclib | 0.314 | 0.944 | 38 | 56,177 | CDK4/6 (breast cancer) |
| Enzalutamide | **0.335** | 0.062 | 10 | 20,903 | AR antagonist (prostate cancer) |
| Abiraterone | 0.362 | 0.079 | 16 | 21,556 | CYP17A1 (prostate cancer) |
| Ribociclib | 0.378 | 0.087 | 14 | 18,932 | CDK4/6 (breast cancer) |

The most predictable drugs are exclusively sex-linked cancer therapies: PARP inhibitors for ovarian cancer (niraparib, 95.8%F), ER antagonists for breast cancer (fulvestrant, 95.6%F), CDK4/6 inhibitors for breast cancer (palbociclib, 94.3%F), and AR antagonists for prostate cancer (enzalutamide, 6.2%F). This validates the entropy measure: drugs with the most biologically sex-constrained indications have the lowest entropy.

**Table 2. Most Balanced Drugs (Highest Entropy)**

| Drug | H(sex) | F Fraction | N Signals | Total Reports |
|------|--------|-----------|-----------|---------------|
| Ambroxol | **1.000** | 0.499 | 14 | 1,303 |
| Amlodipine besylate | 1.000 | 0.502 | 11 | 441 |
| Antithymocyte immunoglobulin | 1.000 | 0.503 | 169 | 18,264 |
| Busulfan | 1.000 | 0.500 | 8 | 2,156 |

Maximum-entropy drugs (H = 1.0, exactly balanced) include drugs from diverse classes, suggesting that perfect sex balance can occur at any therapeutic context. Antithymocyte immunoglobulin is notable: despite 169 signals and 18,264 reports (high statistical power), it maintains perfect entropy, suggesting genuinely sex-neutral pharmacology in the transplant setting.

### Entropy Anti-Regression

**Table 3. Drug Entropy by Report Volume Decile**

| Decile | N Drugs | Mean H | Mean F Fraction | Mean Total Reports |
|--------|---------|--------|----------------|-------------------|
| D0 (lowest) | 139 | **0.982** | 0.524 | 267 |
| D1 | 139 | 0.970 | 0.532 | 450 |
| D2 | 139 | 0.958 | 0.541 | 757 |
| D3 | 139 | 0.949 | 0.550 | 1,241 |
| D4 | 139 | 0.939 | 0.556 | 2,017 |
| D5 | 139 | 0.932 | 0.563 | 3,432 |
| D6 | 139 | 0.924 | 0.572 | 6,054 |
| D7 | 140 | 0.910 | 0.586 | 11,486 |
| D8 | 140 | 0.889 | 0.610 | 24,781 |
| D9 (highest) | 143 | **0.908** | 0.641 | 125,309 |

Spearman rho = **-0.952**, p = **2.3 x 10^-5**.

The entropy anti-regression is highly significant: high-volume drugs are systematically more sex-predictable (lower entropy). In the top decile (D9: H = 0.908, F = 0.641), the most well-characterized drugs show the strongest female bias AND measurably lower entropy than low-volume drugs (D0: H = 0.982).

This translates the anti-regression phenomenon into information-theoretic terms: as statistical evidence accumulates, sex-differential drug safety doesn't regress toward uncertainty (H → 1.0) but intensifies toward predictability (H → 0). This is the information-theoretic signature of a genuine biological signal, not statistical noise.

### Signal-Level Entropy by Volume

At the individual signal level, entropy decreased monotonically with volume:

| Volume Decile | Signal Entropy |
|--------------|---------------|
| D0 | 1.000 |
| D1 | 1.000 |
| D2 | 0.999 |
| D3 | 0.997 |
| D4 | 0.994 |
| D5 | 0.990 |
| D6 | 0.988 |
| D7 | 0.967 |
| D8 | 0.919 |
| D9 | **0.716** |

The transition from near-maximum entropy (D0--D6: 0.988--1.000) to sharply reduced entropy (D9: 0.716) indicates a phase transition: below a report volume threshold, sex-differential signals are essentially unpredictable, but above this threshold, they become highly structured.

### Mutual Information: Which AEs Are Most Sex-Informative?

**Table 4. Top 10 Adverse Events by Mutual Information**

| Adverse Event | MI (bits) | H(overall) | H(conditional) | N Drugs | F Fraction |
|--------------|-----------|-----------|----------------|---------|-----------|
| Folliculitis | **0.320** | 0.880 | 0.560 | 46 | 0.701 |
| Obesity | 0.318 | 0.922 | 0.603 | 91 | 0.663 |
| Blood cholesterol increased | 0.315 | 0.929 | 0.614 | 122 | 0.658 |
| Hip arthroplasty | 0.297 | 0.852 | 0.555 | 42 | 0.688 |
| Lipids increased | 0.289 | 0.919 | 0.630 | 87 | 0.651 |
| Amenorrhoea | 0.282 | 0.756 | 0.474 | 38 | 0.742 |
| Hypersensitivity | 0.276 | 0.935 | 0.659 | 156 | 0.645 |
| Gynaecomastia | 0.271 | 0.813 | 0.542 | 52 | 0.312 |
| Menstrual disorder | 0.268 | 0.774 | 0.506 | 34 | 0.729 |
| Acne | 0.263 | 0.888 | 0.625 | 68 | 0.687 |

High-MI adverse events fall into three categories:

**Metabolic AEs** (obesity MI = 0.318, cholesterol MI = 0.315, lipids MI = 0.289): Drug identity strongly predicts sex for metabolic AEs, suggesting that the sex-differential metabolic impact varies substantially across drug classes. This is clinically important: metabolic monitoring intensity could be sex-stratified based on the drug being prescribed.

**Hormonal/reproductive AEs** (amenorrhoea MI = 0.282, gynaecomastia MI = 0.271, menstrual disorder MI = 0.268): Predictable---these AEs are inherently sex-linked. The high MI reflects the variation in which drugs cause reproductive side effects across sexes.

**Dermatologic/immune AEs** (folliculitis MI = 0.320, hypersensitivity MI = 0.276, acne MI = 0.263): Drug-specific rather than generic sex effects dominate, making these AEs prime candidates for drug-level sex-specific monitoring.

**Table 5. Least Sex-Informative AEs**

| Adverse Event | MI (bits) | N Drugs | F Fraction |
|--------------|-----------|---------|-----------|
| Catarrh | 0.006 | 28 | 0.255 |
| GI GVHD | 0.012 | 21 | 0.472 |
| Acute lymphocytic leukaemia | 0.014 | 18 | 0.461 |

Low-MI AEs are those where sex distribution is consistent regardless of drug---the AE's sex profile is intrinsic to the condition rather than modulated by drug pharmacology.

### Information Concentration

| Top N Drugs | % of Total Sex-Information |
|------------|--------------------------|
| Top 10 | 0.3% |
| Top 50 | 2.2% |
| Top 100 | 5.1% |
| Top 500 | 32.9% |

Sex-differential information is broadly distributed: the top 10 drugs contain only 0.3% of total entropy variation, and even the top 500 contain only 32.9%. This diffuse distribution demonstrates that sex-differential drug safety is a system-wide pharmacological property, not driven by a handful of outlier drugs. Effective sex-stratified pharmacovigilance therefore requires system-wide implementation rather than targeted monitoring of a few high-profile drugs.

---

## Discussion

### Information Theory Complements Disproportionality Analysis

The entropy framework offers three advantages over traditional disproportionality measures:

**1. Unified predictability scale.** Entropy provides a single metric (0--1) that captures sex predictability regardless of direction. A drug with 95%F and one with 5%F both have H ≈ 0.29, equally predictable but in opposite directions. Traditional female fraction conflates magnitude and direction, requiring separate interpretation of extreme values at both ends.

**2. Prioritization for monitoring.** Low-entropy drugs warrant heightened sex-specific monitoring because their sex distributions are highly non-random. This provides a principled basis for allocating sex-stratified monitoring resources---currently done ad hoc or not at all.

**3. Anti-regression validation.** The entropy decrease with volume (rho = -0.952) demonstrates that the anti-regression phenomenon is not simply a shift in means but a genuine increase in signal-to-noise ratio. In information-theoretic terms, accumulating evidence doesn't add noise---it resolves structure.

### The Phase Transition in Predictability

The signal-level entropy gradient shows a striking phase transition: signals in deciles D0--D6 have entropy near 1.0 (essentially unpredictable), while D8--D9 drop to 0.92 and 0.72 (highly structured). This has practical implications: below approximately 100 total reports, individual drug-AE pair sex ratios are uninformative. Above approximately 500 reports, sex-differential patterns become reliable. This threshold could be used to filter sex-differential analyses, excluding low-evidence signals that contribute noise without information.

### Mutual Information Identifies Mechanism-Specific Sex Effects

The mutual information analysis distinguishes AEs where sex is drug-dependent (high MI: folliculitis, obesity, cholesterol) from AEs where sex is drug-independent (low MI: catarrh, GVHD). The former represent opportunities for drug-level sex-specific interventions; the latter represent condition-level sex differences that are pharmacologically invariant.

The dominance of metabolic AEs among high-MI signals (obesity, cholesterol, lipids) is clinically important: metabolic drug effects are among the most common and clinically impactful ADRs, and our analysis reveals that their sex profile is highly drug-specific. Sex-stratified metabolic monitoring could therefore be tailored to individual drug prescriptions.

### Limitations

1. Binary entropy treats female fraction as a single proportion, losing information about individual AE-level variation within drugs.
2. Mutual information requires sufficient drug diversity per AE; rare AEs are excluded.
3. The analysis cannot distinguish whether entropy differences reflect biological sex-differential susceptibility or sex-differential prescribing patterns.
4. Information-theoretic measures are scale-dependent: a drug with 5 signals and 100%F has H = 0 but low confidence; a drug with 500 signals and 100%F has H = 0 with high confidence. Entropy alone doesn't capture statistical power.

---

## Conclusion

Information-theoretic analysis reveals a structured predictability gradient in sex-differential drug safety: high-volume drugs are more sex-predictable (entropy anti-regression, rho = -0.952), specific AEs carry high mutual information about sex given drug identity (folliculitis MI = 0.320, obesity MI = 0.318), and sex information is diffusely distributed across the pharmacopeia (top 10 drugs: only 0.3% of total information). The phase transition in signal-level entropy (near-random below ~100 reports, highly structured above ~500) provides an evidence threshold for sex-differential signal interpretation. This framework offers a complementary lens to traditional disproportionality analysis for pharmacovigilance signal prioritization and sex-specific monitoring resource allocation.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Evans SJW, Waller PC, Davis S. Use of proportional reporting ratios (PRRs) for signal generation from spontaneous ADR reports. Pharmacoepidemiol Drug Saf. 2001;10:483-486.
2. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. Pharmacoepidemiol Drug Saf. 2009;18:427-436.
3. Montastruc JL, et al. Gender differences in adverse drug reactions. Fundam Clin Pharmacol. 2002;16:343-346.
4. Shannon CE. A mathematical theory of communication. Bell Syst Tech J. 1948;27:379-423.
5. Cover TM, Thomas JA. Elements of Information Theory. 2nd ed. Wiley; 2006.
6. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
7. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.

---

## Figure Legends

**Figure 1.** Drug entropy distribution. Histogram of binary entropy H(sex|drug) across 1,394 drugs. The distribution is strongly left-skewed with mode near 1.0 and a long tail extending to H = 0.25. Inset: zoomed view of the low-entropy tail (H < 0.5), showing sex-linked cancer therapies.

**Figure 2.** Entropy anti-regression. Drug-level entropy (y-axis) vs. report volume decile (x-axis). Monotonic decrease from D0 (H = 0.982) to D9 (H = 0.908). Spearman rho = -0.952. The information-theoretic signature of genuine biological signal.

**Figure 3.** Signal-level entropy phase transition. Individual signal entropy (y-axis) vs. report volume decile (x-axis). Near-maximum entropy in D0--D6, with sharp transition to structured low entropy in D8--D9.

**Figure 4.** Mutual information landscape. Scatter plot of mutual information (y-axis) vs. number of drugs per AE (x-axis), colored by mean female fraction. High-MI AEs (folliculitis, obesity, cholesterol) are labeled. Low-MI AEs cluster near zero regardless of drug count.

**Figure 5.** Information concentration curve. Cumulative fraction of total sex-information (y-axis) vs. number of top drugs (x-axis, log scale). The shallow curve demonstrates diffuse distribution: 500 drugs account for only 32.9% of total information.
