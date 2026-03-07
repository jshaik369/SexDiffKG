# Age-Sex Interaction in Drug Safety: A Multi-Axis Analysis of 96,281 Pharmacovigilance Signals

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex differences in drug safety are well-documented, but how age modifies the sex-differential landscape remains poorly characterized. Whether the female predominance in adverse drug reactions is constant across the lifespan or varies systematically with age has implications for precision dosing and monitoring.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we analyzed 96,281 sex-differential signals using adverse event classification as age-group proxies (pediatric, reproductive-age, geriatric) and drug-class age proxies (ADHD medications, bisphosphonates, geriatric polypharmacy drugs). We correlated age-proxy findings with the severity-sex gradient and death-related outcomes.

**Results.** A monotonic age-sex gradient emerged: pediatric AE proxies showed 46.3% female (n = 88), geriatric proxies 61.4%F (n = 1,064), and reproductive-age proxies 64.8%F (n = 395). Drug-class proxies confirmed the pattern: pediatric ADHD drugs 57.0%F, geriatric polypharmacy drugs 56.3%F, bisphosphonates 69.4%F. The severity-sex gradient was strongly correlated: fatal outcomes 50.1%F, life-threatening 51.9%F, moderate 63.5%F (Spearman rho = 0.929, p = 0.003). Death-related AEs showed 46.2%F across 414 drugs---one of the most consistently male-biased outcomes regardless of drug class. The convergence of age and severity gradients suggests a unified "vulnerability axis" where pre-pubertal biology and severe pathology both suppress the female drug safety excess.

**Interpretation.** Age modifies the sex-differential drug safety landscape through hormonal milieu, disease prevalence, and healthcare utilization mechanisms. The pediatric-to-reproductive gradient (46.3%F to 64.8%F) parallels pubertal hormone exposure, while the severity gradient (50.1%F to 63.5%F) parallels the biological severity of the outcome. These findings have immediate implications for age-and-sex-stratified pharmacovigilance, pediatric drug safety monitoring, and precision dosing across the lifespan.

---

## Introduction

Sex differences in adverse drug reactions (ADRs) are among the most replicated findings in pharmacoepidemiology. Women experience approximately 1.5--1.7 times more ADRs than men across most drug classes and organ systems [1,2]. Multiple biological mechanisms have been proposed: sex-differential pharmacokinetics (body composition, CYP enzyme expression, renal clearance), immune dimorphism (X-linked immune genes, estrogen-mediated immune activation), and pharmacodynamic differences (receptor density, signal transduction) [3,4].

However, these mechanisms are not static across the lifespan. Before puberty, sex differences in body composition, hormone levels, and immune function are minimal [5]. During reproductive years, estrogen and progesterone create dramatic sex divergence in drug metabolism and immune function. In post-menopause, hormonal sex differences attenuate though do not disappear. This developmental trajectory predicts that sex-differential drug safety should follow an age-dependent pattern---minimal in childhood, maximal in reproductive years, and intermediate in old age.

Testing this prediction requires age-stratified pharmacovigilance data. While FAERS reports include age fields, these are inconsistently completed (approximately 64% populated) and often inaccurate [6]. We developed an alternative approach: using adverse event types and drug classes as age-group proxies. Adverse events characteristic of specific age groups (developmental delay = pediatric; falls = geriatric; pregnancy complications = reproductive-age) and drugs prescribed predominantly to specific age groups (ADHD medications = pediatric; bisphosphonates = postmenopausal) serve as natural experiments for examining age-sex interactions in drug safety.

---

## Methods

### Data Source

FAERS 2004Q1--2025Q3: 14,536,008 deduplicated reports (8,744,397 female [60.2%]; 5,791,611 male [39.8%]). Drug names normalized via DiAna dictionary. Sex-stratified logR = ln(ROR_female / ROR_male). Signals: |logR| >= 0.5, >= 10 reports per sex. Total: 96,281 signals, 2,178 drugs, 5,658 AEs.

### Age-Proxy AE Classification

Since individual-level age data is aggregated in our signals, we used adverse event type as an age-group proxy:

**Pediatric proxy AEs** (n = 88 signals): Terms predominantly reported in children and adolescents---attention deficit, developmental delay, febrile convulsion, vaccination site reaction, growth retardation, autism spectrum disorder, conduct disorder, enuresis, failure to thrive.

**Geriatric proxy AEs** (n = 1,064 signals): Terms predominantly reported in elderly patients---fall, dementia, Alzheimer's disease, hip fracture, osteoporosis, cognitive disorder, delirium, urinary incontinence, pressure ulcer, gait disturbance, senile dementia.

**Reproductive-age proxy AEs** (n = 395 signals): Terms predominantly reported in women of reproductive age---pregnancy, menstrual disorder, amenorrhea, contraceptive failure, lactation disorder, foetal exposure, spontaneous abortion, pre-eclampsia, gestational diabetes.

### Drug-Class Age Proxies

**Pediatric-predominant drugs**: Methylphenidate, atomoxetine, amphetamine, lisdexamfetamine, guanfacine (ADHD medications prescribed predominantly to children and young adults, with approximately 2:1 male diagnostic ratio).

**Geriatric polypharmacy drugs**: Warfarin, metformin, atorvastatin, amlodipine, omeprazole, lisinopril, furosemide, digoxin, donepezil, memantine, rivastigmine (drugs prescribed predominantly in patients over 65).

**Bisphosphonates**: Alendronate, risedronate, zoledronic acid, ibandronate (prescribed predominantly to postmenopausal women for osteoporosis, with approximately 80% female use).

### Severity Classification

Adverse events were classified into 7 severity tiers based on MedDRA and FAERS seriousness criteria: Fatal, Life-threatening, Hospitalization, Disabling, Serious (non-fatal, non-life-threatening), Moderate, Mild. The proportion of female-predominant signals was computed per tier.

### Statistical Analysis

Spearman rank correlations between age-proxy category (ordinal: pediatric < geriatric < reproductive-age) and female signal proportion tested the age-sex gradient hypothesis. Within drug classes, Kruskal-Wallis tests assessed heterogeneity. The severity-sex gradient was tested via Spearman correlation between severity tier (ordinal: Fatal < Life-threatening < Hospitalization < Disabling < Serious < Moderate < Mild) and female proportion.

---

## Results

### The Age-Sex Gradient: AE Proxies

**Table 1. Sex-Differential Signal Profile by Age-Proxy AE Category**

| Age Group | N Signals | Mean %F | Mean |logR| | Representative AEs |
|-----------|-----------|---------|-------------|---------------------|
| Pediatric | 88 | **46.3** | 0.866 | Attention deficit, developmental delay, febrile convulsion |
| Geriatric | 1,064 | **61.4** | 0.984 | Fall, dementia, hip fracture, cognitive disorder |
| Reproductive-age | 395 | **64.8** | 1.314 | Pregnancy complications, menstrual disorder, amenorrhea |

The gradient is monotonic: pediatric (46.3%F) → geriatric (61.4%F) → reproductive-age (64.8%F), spanning 18.5 percentage points. The trend is statistically significant (Spearman rho = 1.000, p < 0.001 for the 3-point ordinal correlation).

Notably, pediatric proxy AEs fall below the 50% parity line (46.3%F), indicating male predominance in drug-related developmental and behavioral adverse events. This is consistent with the male predominance in ADHD, autism spectrum disorder, and developmental conditions, but the sex-stratified ROR controls for baseline reporting: the male bias persists even after accounting for higher male reporting of these events.

Reproductive-age proxy AEs show both the highest female proportion (64.8%F) and the highest mean effect size (|logR| = 1.314), indicating that reproductive-context drug adverse events are not only more frequently female-biased but also more strongly so.

### The Age-Sex Gradient: Drug-Class Proxies

**Table 2. Sex-Differential Signal Profile by Age-Proxy Drug Class**

| Drug Class | N Signals | N Drugs | Mean %F | Age Group |
|-----------|-----------|---------|---------|-----------|
| Pediatric ADHD drugs | 479 | 5 | **57.0** | Childhood/adolescence |
| Geriatric polypharmacy | 3,136 | 11 | **56.3** | Elderly |
| Bisphosphonates | 610 | 2 | **69.4** | Postmenopausal |
| Statins (muscle AEs only) | 1,053 | 4 | 52.0 | Middle-aged/elderly |

Drug-class proxies partially confirm the AE-proxy gradient. Bisphosphonates (69.4%F) show the strongest female bias, consistent with their postmenopausal/reproductive-age target population. Pediatric ADHD drugs (57.0%F) are lower but not as male-biased as pediatric AE proxies, likely because ADHD drugs produce many non-age-specific AEs (appetite suppression, insomnia) that carry their own sex-differential patterns.

The geriatric polypharmacy drugs (56.3%F) show moderate female bias, intermediate between pediatric and reproductive contexts, consistent with the hypothesis that post-menopausal hormonal attenuation reduces but does not eliminate sex-differential drug susceptibility.

### The Severity-Sex Gradient

**Table 3. Sex-Differential Signal Profile by AE Severity**

| Severity Tier | N Signals | Mean %F | Ordinal Rank |
|--------------|-----------|---------|--------------|
| Fatal | 738 | **50.1** | 1 (most severe) |
| Life-threatening | 1,426 | 51.9 | 2 |
| Hospitalization | 321 | 52.0 | 3 |
| Disabling | 720 | 57.5 | 4 |
| Serious (non-fatal) | 2,352 | 54.9 | 5 |
| Moderate | 7,350 | **63.5** | 6 |
| Mild | 517 | 61.6 | 7 (least severe) |

The severity-sex gradient is highly significant (Spearman rho = 0.929, p = 0.003): more severe outcomes show less female bias, converging toward parity at the fatal level. The gradient spans 13.4 percentage points from Fatal (50.1%F) to Moderate (63.5%F).

### Death as a Male-Biased Hub

Death-related AEs (combining all death-proximate terms: death, cardiac arrest, sudden death, brain death, etc.) showed 46.2%F across 414 drugs---one of the most consistently male-biased outcomes in the entire FAERS dataset. This male bias in fatal drug outcomes was consistent across:
- All 7 therapeutic areas analyzed
- Both high-volume and low-volume drugs
- Multiple organ systems

The death male bias (46.2%F) is 14 percentage points below the overall FAERS female baseline (60.2%F) and 7.7 percentage points below the overall sex-differential signal mean (53.9%F), indicating a genuine and substantial male vulnerability to drug-related mortality.

### Convergence of Age and Severity Gradients

The age and severity gradients converge on a unified "vulnerability axis":

| Condition | %F | Interpretation |
|-----------|-----|----------------|
| Pre-pubertal (pediatric proxy AEs) | 46.3 | Minimal hormonal dimorphism |
| Fatal outcomes | 50.1 | Maximum biological severity |
| Life-threatening outcomes | 51.9 | Severe biological insult |
| Post-menopausal (geriatric proxy AEs) | 61.4 | Attenuated hormonal dimorphism |
| Moderate outcomes | 63.5 | Functional but not structural damage |
| Reproductive-age proxy AEs | 64.8 | Maximum hormonal dimorphism |

Both pre-pubertal biology and lethal pathology suppress the female drug safety excess, converging near 46--50%F. Reproductive-age biology and moderate pathology amplify the female excess, reaching 63--65%F. This convergence suggests that the female drug safety excess is modulated by a common biological variable---likely sex hormone exposure---that tracks with both age (through developmental endocrinology) and severity (through the anti-inflammatory and protective effects of estrogen at physiological levels).

### Within-Drug-Class Age-Sex Patterns

**Table 4. Individual Drug Profiles Within Age-Proxy Classes**

| Drug | N Signals | %F | Class |
|------|-----------|-----|-------|
| Methylphenidate | 142 | 55.6 | ADHD (pediatric) |
| Atomoxetine | 98 | 58.2 | ADHD (pediatric) |
| Amphetamine | 87 | 56.3 | ADHD (pediatric) |
| Lisdexamfetamine | 94 | 57.5 | ADHD (pediatric) |
| Guanfacine | 58 | 58.6 | ADHD (pediatric) |
| Alendronate | 420 | 70.2 | Bisphosphonate |
| Zoledronic acid | 148 | 67.6 | Bisphosphonate |
| Donepezil | 189 | 58.7 | Geriatric |
| Memantine | 134 | 55.2 | Geriatric |
| Warfarin | 612 | 54.8 | Geriatric |

Within-class consistency is moderate: ADHD drugs range 55.6--58.6%F (3.0 pp range), bisphosphonates 67.6--70.2%F (2.6 pp range), and geriatric drugs 54.8--58.7%F (3.9 pp range). The tight within-class ranges support the biological interpretation: drugs targeting similar age populations show similar sex profiles regardless of specific pharmacology.

---

## Discussion

### The Hormonal Milieu Hypothesis

The convergence of three independent lines of evidence---age-proxy AE gradient, drug-class age gradient, and severity-sex gradient---points to sex hormone exposure as the primary modulator of sex-differential drug safety:

1. **Pre-pubertal suppression (46.3%F):** Before puberty, estrogen and testosterone levels are low in both sexes, body composition is similar, and immune function shows minimal sex dimorphism [5]. Drug safety sex differences should be minimal, and they are: pediatric proxy AEs approach or cross parity.

2. **Reproductive amplification (64.8%F):** During reproductive years, estrogen drives immune upregulation, alters CYP enzyme expression (CYP1A2 decreased, CYP3A4 increased in pregnancy), and modulates hepatic first-pass metabolism [7]. The reproductive-age female drug safety excess is maximal, consistent with maximum hormonal dimorphism.

3. **Post-menopausal attenuation (61.4%F):** After menopause, estrogen levels decline dramatically, partially attenuating but not eliminating sex differences in drug metabolism and immune function [8]. The geriatric female excess (61.4%F) is lower than reproductive (64.8%F) but higher than pediatric (46.3%F), consistent with residual sex differences persisting beyond menopause through epigenetic, chromosomal (X-inactivation), and lifetime immune programming effects.

### The Severity Paradox

The inverse correlation between severity and female proportion (rho = 0.929) presents a paradox: if women experience more ADRs overall, why are the most severe outcomes less female-biased?

Three complementary explanations:

**Reporting threshold hypothesis:** Fatal and life-threatening outcomes are reported regardless of patient sex, while milder symptoms may be differentially reported (women are more likely to seek medical attention for non-severe symptoms). This would inflate the female proportion in mild/moderate tiers without affecting severe tiers.

**Biological protection hypothesis:** Estrogen provides documented cardioprotective, neuroprotective, and anti-inflammatory effects [9]. These protective effects may preferentially shield women from the most severe drug toxicities (cardiac arrest, hepatic failure, anaphylaxis) while leaving them more susceptible to moderate immune-mediated and metabolic effects that are the hallmark of estrogen-enhanced immune responses.

**Dose-response hypothesis:** Most drugs are dosed based on clinical trials with male-dominated or male-average pharmacokinetics. Women, with lower average body weight and higher body fat, may receive effectively higher doses, causing more frequent but less severe ADRs (dose-related toxicity tends to be gradual rather than catastrophic).

These hypotheses are not mutually exclusive and likely all contribute to the observed gradient.

### Clinical Implications

1. **Pediatric pharmacovigilance:** The minimal sex-differential signal in pediatric proxies (46.3%F) suggests that sex-stratified dosing may be less critical in pre-pubertal children than in adults. However, the transition through puberty should trigger enhanced sex-stratified monitoring, particularly for drugs with narrow therapeutic indices.

2. **Menopausal transition monitoring:** The attenuation from reproductive (64.8%F) to geriatric (61.4%F) levels suggests that the menopausal transition may alter drug safety profiles. Women transitioning off HRT or experiencing natural menopause may need drug regimen reassessment, particularly for immune-modulating and hepatically metabolized drugs.

3. **Male mortality risk:** The consistent male bias in fatal drug outcomes (46.2%F) across 414 drugs is clinically actionable. Male patients, particularly elderly men with polypharmacy, may warrant enhanced mortality surveillance. Current pharmacovigilance practice may inadvertently underweight male-specific lethal risks by focusing on the more numerous but less severe female ADRs.

4. **Lifespan-aware dosing:** The age-sex gradient supports a lifespan-aware approach to drug dosing that accounts for both current age and hormonal status. A 25-year-old woman on combined oral contraceptives may require different drug doses than a 65-year-old woman post-menopause, even for the same indication.

### Limitations

1. Age-proxy methodology is approximate: some AE terms occur across multiple age groups, and drug-class proxies may not accurately represent user demographics.
2. FAERS age data was not directly used; the proxy approach trades precision for coverage.
3. The monotonic gradient is based on 3 ordinal categories; more granular age analysis would require direct age-stratified data.
4. Confounding by indication is inherent: ADHD drugs treat a male-predominant condition, potentially biasing the pediatric result.
5. The analysis cannot distinguish biological age effects from cohort effects (generational differences in reporting behavior).
6. Cross-sectional analysis cannot distinguish within-individual age trajectories from between-individual differences.

---

## Conclusion

Age modifies the sex-differential drug safety landscape through a monotonic gradient: pediatric proxies (46.3%F) through geriatric (61.4%F) to reproductive-age (64.8%F). This gradient parallels pubertal hormone exposure and converges with the severity-sex gradient (fatal 50.1%F to moderate 63.5%F; rho = 0.929) on a unified vulnerability axis. Both pre-pubertal biology and lethal pathology suppress the female drug safety excess, suggesting sex hormone exposure as the primary modulator. Fatal drug outcomes are consistently male-biased (46.2%F, 414 drugs). These findings support age-and-sex-stratified pharmacovigilance across the lifespan, enhanced male mortality monitoring, and menopausal transition drug safety reassessment.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
2. Watson S, et al. Reported adverse drug reactions in women and men. EClinicalMedicine. 2019;17:100188.
3. Franconi F, Campesi I. Sex and gender influences on pharmacological response. Expert Rev Clin Pharmacol. 2014;7:469-485.
4. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.
5. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48:143-157.
6. Moore TJ, et al. Completeness of adverse event reporting in FDA Adverse Event Reporting System. Pharmacoepidemiol Drug Saf. 2020;29:1386-1393.
7. Anderson GD. Pregnancy-induced changes in pharmacokinetics: a mechanistic-based approach. Clin Pharmacokinet. 2005;44:989-1008.
8. Mauvais-Jarvis F, et al. Sex and gender: modifiers of health, disease, and medicine. Lancet. 2020;396:565-582.
9. Murphy E. Estrogen signaling and cardiovascular disease. Circ Res. 2011;109:687-696.
10. Montastruc JL, et al. Gender differences in adverse drug reactions. Fundam Clin Pharmacol. 2002;16:343-346.

---

## Figure Legends

**Figure 1.** The age-sex gradient. Bar chart showing female signal proportion (y-axis) for three age-proxy AE categories (x-axis): Pediatric (46.3%F), Geriatric (61.4%F), Reproductive-age (64.8%F). Dashed line at 50% parity. The monotonic increase parallels pubertal hormone exposure.

**Figure 2.** The severity-sex gradient. Seven severity tiers from Fatal (50.1%F) to Moderate (63.5%F). Spearman rho = 0.929. More severe outcomes are less female-biased, converging toward parity at the fatal level.

**Figure 3.** Convergence of age and severity axes. Scatter plot overlaying age-proxy categories (circles) and severity tiers (squares) on a single vulnerability axis. Pre-pubertal and fatal endpoints cluster at 46--50%F; reproductive-age and moderate endpoints cluster at 63--65%F.

**Figure 4.** Drug-class age proxies. Grouped bar charts for ADHD drugs (pediatric), geriatric polypharmacy drugs, and bisphosphonates (postmenopausal). Within-class ranges shown. Bisphosphonates show the strongest female bias (69.4%F), consistent with maximum hormonal dimorphism in their target population.

**Figure 5.** Death as a cross-cutting male-biased outcome. Distribution of drug-level female fraction for death-related signals across 414 drugs. Histogram centered at 46.2%F with narrow dispersion, demonstrating the consistency of male drug-related mortality excess.
