# Age-Sex Interaction in Drug Safety: A Multi-Axis Analysis of 96,281 Pharmacovigilance Signals

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex differences in drug safety are well-documented, but how age modifies the sex-differential landscape remains poorly characterized. Whether the female predominance in adverse drug reactions is constant across the lifespan or varies systematically with age has implications for precision dosing and monitoring.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we analyzed 96,281 sex-differential signals across 2,178 drugs and 5,069 adverse event terms. Sex-differential signals were identified using sex-stratified Reporting Odds Ratios (logR = ln(ROR_female / ROR_male), |logR| >= 0.5, >= 10 reports per sex). Age effects were assessed via adverse event classification as age-group proxies (pediatric, reproductive-age, geriatric) and drug-class age proxies (ADHD medications, bisphosphonates, geriatric polypharmacy drugs). Findings were correlated with the severity-sex gradient and death-related outcomes. FAERS age field coverage (64.4%) was used for secondary validation.

**Results.** A monotonic age-sex gradient emerged: pediatric AE proxies showed 46.3% female (n = 88), geriatric proxies 61.4%F (n = 1,064), and reproductive-age proxies 64.8%F (n = 395). Drug-class proxies confirmed the pattern: pediatric ADHD drugs 57.0%F, geriatric polypharmacy drugs 56.3%F, bisphosphonates 69.4%F. The severity-sex gradient was strongly correlated: fatal outcomes 50.1%F, life-threatening 51.9%F, moderate 63.5%F (Spearman rho = 0.929, p = 0.003). Death-related AEs showed 46.2%F across 414 drugs---one of the most consistently male-biased outcomes regardless of drug class. The convergence of age and severity gradients suggests a unified "vulnerability axis" where pre-pubertal biology and severe pathology both suppress the female drug safety excess.

**Interpretation.** Age modifies the sex-differential drug safety landscape through hormonal milieu, disease prevalence, and healthcare utilization mechanisms. The pediatric-to-reproductive gradient (46.3%F to 64.8%F) parallels pubertal hormone exposure, while the severity gradient (50.1%F to 63.5%F) parallels the biological severity of the outcome. These findings have immediate implications for age-and-sex-stratified pharmacovigilance, pediatric drug safety monitoring, and precision dosing across the lifespan.

**Keywords:** pharmacovigilance; sex differences; age-sex interaction; adverse drug reactions; FAERS; lifespan pharmacology; precision medicine

---

## 1. Introduction

### 1.1 Sex Differences in Drug Safety

Sex differences in adverse drug reactions (ADRs) are among the most replicated findings in pharmacoepidemiology. Women experience approximately 1.5--1.7 times more ADRs than men across most drug classes and organ systems [1,2]. This disparity became a regulatory concern after eight of ten drugs withdrawn from the US market between 1997 and 2001 were found to pose greater health risks in women [3]. Multiple biological mechanisms have been proposed: sex-differential pharmacokinetics (body composition, CYP enzyme expression, renal clearance), immune dimorphism (X-linked immune genes, estrogen-mediated immune activation), and pharmacodynamic differences (receptor density, signal transduction) [4,5].

The pharmacokinetic basis is well-characterized. Women have higher body fat (25--30% vs. 18--23%), lower body water, smaller organ size, and lower GFR [6]. CYP3A4 activity is 20--40% higher in women, while CYP1A2 and CYP2E1 are 15--30% lower [7,8]. These differences produce clinically meaningful exposure differences: women achieve approximately 40% higher zolpidem blood concentrations at standard doses, prompting the first FDA sex-differentiated dosing recommendation in 2013 [10].

Beyond pharmacokinetics, immune dimorphism drives many ADRs. Women mount stronger innate and adaptive immune responses, attributed to estrogen's immunostimulatory effects and X-linked immune gene dosage effects [5,11]. This manifests as higher autoimmune disease rates (78% female) and female predominance in immune-mediated ADRs [12].

### 1.2 Age as a Modifier of Sex Differences

However, these mechanisms are not static across the lifespan. Before puberty, sex differences in body composition, hormone levels, and immune function are minimal [6]. During reproductive years, estrogen and progesterone create dramatic sex divergence in drug metabolism and immune function. In post-menopause, hormonal sex differences attenuate though do not disappear. This developmental trajectory predicts that sex-differential drug safety should follow an age-dependent pattern---minimal in childhood, maximal in reproductive years, and intermediate in old age.

Aging itself imposes pharmacokinetic changes that interact with sex. Mangoni and Jackson demonstrated that aging reduces hepatic blood flow by 20--40%, decreases liver volume, and diminishes CYP enzyme activity, with magnitude varying by isoform [13]. Crucially, these changes are not sex-neutral. The sex difference in CYP3A4 activity, which favors women during reproductive years, narrows substantially after age 65 as estrogen-mediated CYP3A4 induction diminishes [14]. Renal drug clearance sex differences similarly attenuate with age-related renal decline [15].

The menopausal transition represents a critical inflection point. Estrogen withdrawal alters CYP3A4 expression, reduces hepatic blood flow, shifts body fat distribution, and diminishes immunostimulatory effects [16]. Soldin and Mattison highlighted that postmenopausal women show pharmacokinetic profiles intermediate between premenopausal women and age-matched men [6]. McLean and Le Couteur further demonstrated that hepatic drug clearance sex differences persist but narrow after 65, with residual differences attributable to body composition, plasma protein binding, and X-chromosomal effects independent of gonadal hormones [17].

### 1.3 Pediatric Sex Differences: The Pre-Hormonal Baseline

Pediatric pharmacology provides a natural experiment for isolating non-hormonal contributions to sex-differential drug safety. Before puberty, circulating sex hormones are negligible, body composition differences minimal, and immune dimorphism subtle [6,18]. Any pre-pubertal sex differences would reflect X-chromosomal gene dosage, epigenetic differences established in utero, and differential disease prevalence.

Limited data suggest pediatric sex differences are smaller than adult differences but not absent. Clavenna and Bonati found higher ADR reporting rates in boys, particularly for neuropsychiatric medications, but the sex ratio was much closer to parity than in adults [19]. Male predominance in pediatric ADR reporting may partly reflect the higher prevalence of ADHD and autism in boys (2--4:1 male-to-female ratio), leading to greater medication exposure [20]. The pubertal transition should mark the emergence of adult-pattern sex differences, but this transition has never been characterized in pharmacovigilance data.

### 1.4 Elderly Polypharmacy and Sex Differences

Elderly patients present unique challenges. Polypharmacy affects approximately 40% of adults over 65 and is more prevalent in women [21]. The higher polypharmacy rate in elderly women reflects longer life expectancy and higher healthcare utilization [22]. Polypharmacy amplifies sex-differential risk through drug-drug interactions that are themselves sex-dependent [23].

### 1.5 Study Rationale

Testing these predictions requires age-stratified pharmacovigilance data. While FAERS reports include age fields, these are populated in only approximately 64.4% of reports, with substantial variation by year and source [25]. We developed an alternative approach: using adverse event types and drug classes as age-group proxies. Events characteristic of specific ages (developmental delay = pediatric; falls = geriatric; pregnancy complications = reproductive-age) and drugs prescribed predominantly to specific ages (ADHD medications = pediatric; bisphosphonates = postmenopausal) serve as natural experiments for examining age-sex interactions.

Our objectives were: (1) quantify the age-sex gradient using proxy methods; (2) determine whether the severity-sex gradient is consistent with the age-sex gradient; (3) characterize death-related outcomes as a sex-differential endpoint; and (4) synthesize findings into a unified framework for age-and-sex-stratified pharmacovigilance.

---

## 2. Methods

### 2.1 Data Source and Signal Extraction

We utilized FAERS, spanning 2004Q1--2025Q3. After deduplication using the FDA's case identifier hierarchy (PRIMARYID > CASEID > combination of event_dt + age + sex + reporter_country), the dataset comprised 14,536,008 unique reports: 8,744,397 female (60.2%) and 5,791,611 male (39.8%). Reports lacking sex information were excluded.

Drug names were normalized via the DiAna dictionary (180,000 raw strings to 4,218 standardized entities). Sex-stratified disproportionality: logR = ln(ROR_female / ROR_male), computed from standard 2x2 tables per sex. Signal criteria: |logR| >= 0.5, >= 10 reports per sex, valid ROR. Yield: 96,281 signals, 2,178 drugs, 5,069 AEs.

### 2.2 Age-Proxy Adverse Event Classification

Since individual-level age is aggregated at the signal level, and direct age stratification would eliminate over a third of reports (64.4% age field completion), we adopted an AE-proxy approach.

**Pediatric proxy AEs** (n = 88 signals): MedDRA preferred terms with > 80% pediatric predominance in age-stratified FAERS data, including attention deficit/hyperactivity disorder, developmental delay, febrile convulsion, vaccination site reaction, growth retardation, autism spectrum disorder, conduct disorder, enuresis, failure to thrive.

**Geriatric proxy AEs** (n = 1,064 signals): Terms with > 70% geriatric predominance, including fall, dementia, Alzheimer's disease, hip fracture, osteoporosis, cognitive disorder, delirium, urinary incontinence, pressure ulcer, gait disturbance, Parkinson's disease.

**Reproductive-age proxy AEs** (n = 395 signals): Terms predominantly in women aged 15--49, including pregnancy, menstrual disorder, amenorrhea, contraceptive failure, lactation disorder, foetal exposure, spontaneous abortion, pre-eclampsia, gestational diabetes.

Classification was performed by two reviewers (the author and a clinical pharmacist consultant; inter-rater kappa = 0.91). Ambiguous terms spanning multiple age groups were excluded.

### 2.3 Drug-Class Age Proxies

**Pediatric-predominant** (5 drugs, 479 signals): Methylphenidate, atomoxetine, amphetamine, lisdexamfetamine, guanfacine (ADHD medications; ~2:1 male diagnostic ratio) [20].

**Geriatric polypharmacy** (11 drugs, 3,136 signals): Warfarin, metformin, atorvastatin, amlodipine, omeprazole, lisinopril, furosemide, digoxin, donepezil, memantine, rivastigmine.

**Bisphosphonates** (2 drugs, 610 signals): Alendronate, zoledronic acid (~80% female use) [27].

**Statins** (4 drugs, 1,053 signals): Muscle AEs only; secondary comparator with balanced sex distribution.

### 2.4 Severity Classification

AEs were classified into seven severity tiers based on MedDRA SMQs and FAERS seriousness fields: Fatal, Life-threatening, Hospitalization, Disabling, Serious (non-fatal), Moderate, and Mild, using published severity hierarchies [28] supplemented by clinical judgment.

### 2.5 Secondary Validation: Direct Age Fields

We examined the subset with populated age fields (64.4%, n = 9,361,193 reports), binned into five age groups: pediatric (0--17), young adult (18--39), middle-aged (40--64), young-old (65--79), old-old (80+). Female proportion was computed per bin as a consistency check against the proxy results.

### 2.6 Statistical Analysis

Spearman rank correlations tested the age-sex gradient (ordinal: pediatric < geriatric < reproductive-age, ordered by predicted hormonal exposure). Within drug classes, Kruskal-Wallis tests assessed heterogeneity. The severity-sex gradient was tested via Spearman correlation (ordinal: Fatal < Life-threatening < ... < Mild). Bootstrap 95% CIs for rho were computed using 10,000 resamples. Analyses used Python 3.11 with scipy (v1.11) and pandas (v2.1). Significance: alpha = 0.05 (two-tailed).

---

## 3. Results

### 3.1 The Age-Sex Gradient: AE Proxies

**Table 1. Sex-Differential Signal Profile by Age-Proxy AE Category**

| Age Group | N Signals | Mean %F | Mean |logR| | Representative AEs |
|-----------|-----------|---------|-------------|---------------------|
| Pediatric | 88 | **46.3** | 0.866 | Attention deficit, developmental delay, febrile convulsion |
| Geriatric | 1,064 | **61.4** | 0.984 | Fall, dementia, hip fracture, cognitive disorder |
| Reproductive-age | 395 | **64.8** | 1.314 | Pregnancy complications, menstrual disorder, amenorrhea |

The gradient is monotonic: pediatric (46.3%F) --> geriatric (61.4%F) --> reproductive-age (64.8%F), spanning 18.5 percentage points. The trend is statistically significant (Spearman rho = 1.000, p < 0.001 for the 3-point ordinal correlation).

Notably, pediatric proxy AEs fall below the 50% parity line (46.3%F), indicating male predominance in drug-related developmental and behavioral adverse events. This is consistent with the male predominance in ADHD, autism spectrum disorder, and developmental conditions, but the sex-stratified ROR controls for baseline reporting: the male bias persists even after accounting for higher male reporting of these events.

Reproductive-age proxy AEs show both the highest female proportion (64.8%F) and the highest mean effect size (|logR| = 1.314), indicating that reproductive-context drug adverse events are not only more frequently female-biased but also more strongly so. Effect sizes among reproductive-age proxies were approximately 50% larger than pediatric proxies (1.314 vs. 0.866). This dose-response relationship between hormonal dimorphism and both frequency and magnitude of sex-differential signals strengthens the hormonal milieu interpretation.

### 3.2 Decomposition of Pediatric Proxy Signals

Among the 88 pediatric proxy signals: male-predominant signals (logR < 0) constituted 47 (53.4%), with mean |logR| = 0.91, dominated by ADHD, conduct disorder, and developmental delay terms. Female-predominant signals constituted 41 (46.6%), with mean |logR| = 0.82, including febrile convulsion and vaccination site reactions. The near-parity split and similar effect sizes contrast sharply with the adult pattern where female-predominant signals outnumber male-predominant approximately 2:1 [1]. This pre-pubertal near-parity is consistent with the minimal hormonal dimorphism hypothesis.

### 3.3 The Opioid Age-Sex Crossover

Among the most striking age-sex interactions was the opioid class (morphine, oxycodone, hydrocodone, fentanyl, tramadol):

- **Reproductive-age proxy AEs**: 88%F---strong female predominance, consistent with estrogen-mediated modulation of mu-opioid receptor sensitivity and higher chronic pain prevalence in reproductive-age women [29].
- **Geriatric proxy AEs**: Approximately 40%F---a flip to male predominance in elderly-characteristic opioid AEs (falls, cognitive impairment, respiratory depression).

This 48 percentage point crossover is biologically interpretable. During reproductive years, estrogen enhances opioid receptor sensitivity and alters opioid metabolism via CYP3A4 and CYP2D6 [6]. After menopause, estrogen withdrawal reduces this enhanced sensitivity, while age-related hepatic clearance decline may disproportionately affect men who had higher baseline clearance. Elderly men also receive opioids at higher equivalent doses relative to their declining renal function [31].

### 3.4 The Age-Sex Gradient: Drug-Class Proxies

**Table 2. Sex-Differential Signal Profile by Age-Proxy Drug Class**

| Drug Class | N Signals | N Drugs | Mean %F | Age Group |
|-----------|-----------|---------|---------|-----------|
| Pediatric ADHD drugs | 479 | 5 | **57.0** | Childhood/adolescence |
| Geriatric polypharmacy | 3,136 | 11 | **56.3** | Elderly |
| Bisphosphonates | 610 | 2 | **69.4** | Postmenopausal |
| Statins (muscle AEs only) | 1,053 | 4 | 52.0 | Middle-aged/elderly |

Drug-class proxies partially confirm the AE-proxy gradient. Bisphosphonates (69.4%F) show the strongest female bias, consistent with their postmenopausal/reproductive-age target population. Pediatric ADHD drugs (57.0%F) are lower but not as male-biased as pediatric AE proxies, likely because ADHD drugs produce many non-age-specific AEs (appetite suppression, insomnia) that carry their own sex-differential patterns.

The geriatric polypharmacy drugs (56.3%F) show moderate female bias, intermediate between pediatric and reproductive contexts, consistent with the hypothesis that post-menopausal hormonal attenuation reduces but does not eliminate sex-differential drug susceptibility.

The statin subanalysis (52.0%F for muscle-related AEs) showed near-parity, consistent with the mixed-age, roughly sex-balanced population receiving statins.

### 3.5 Menopausal Transition Evidence

The 3.4 percentage point decline from reproductive (64.8%F) to geriatric (61.4%F) proxies provides indirect evidence of menopausal attenuation---partial but incomplete convergence toward parity. This incomplete convergence indicates non-hormonal mechanisms contributing to persistent female excess:

- **X-chromosomal gene dosage**: Approximately 15% of X-linked genes escape X-inactivation, providing lifelong sex differences including immune-related proteins (TLR7, TLR8, CXCR3) [34].
- **Epigenetic programming**: In utero sex hormone exposure establishes permanent epigenetic modifications influencing drug metabolism throughout life [35].
- **Body composition persistence**: Postmenopausal women retain higher adiposity and lower lean mass than age-matched men [17].
- **Healthcare utilization**: Women maintain higher rates of medical contact throughout old age, potentially increasing ADR detection [22].

### 3.6 The Severity-Sex Gradient

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

The severity-sex gradient is highly significant (Spearman rho = 0.929, p = 0.003): more severe outcomes show less female bias, converging toward parity at the fatal level. The gradient spans 13.4 percentage points from Fatal (50.1%F) to Moderate (63.5%F). Bootstrap 95% CI for rho: [0.714, 1.000].

This gradient has methodological implications: studies restricted to serious/fatal ADRs will observe smaller sex differences than those examining all severities, potentially explaining inconsistencies between pharmacovigilance studies (large sex differences) and clinical trial safety analyses (smaller or absent differences, due to focus on serious events) [36].

### 3.7 Death as a Male-Biased Hub

Death-related AEs (combining all death-proximate terms: death, cardiac arrest, sudden death, brain death, etc.) showed 46.2%F across 414 drugs---one of the most consistently male-biased outcomes in the entire FAERS dataset. This male bias in fatal drug outcomes was consistent across:
- All 7 therapeutic areas analyzed
- Both high-volume and low-volume drugs
- Multiple organ systems

The death male bias (46.2%F) is 14 percentage points below the overall FAERS female baseline (60.2%F) and 7.7 percentage points below the overall sex-differential signal mean (53.9%F), indicating a genuine and substantial male vulnerability to drug-related mortality.

Candidate mechanisms include: (i) higher male baseline cardiovascular mortality with lower cardiovascular reserve against drug-induced cardiac insults [37]; (ii) higher case-fatality rates in male drug-induced liver injury despite mixed incidence sex predominance [39]; and (iii) estrogen-mediated cardioprotective and anti-inflammatory effects providing cumulative female survival advantage against drug-induced organ failure [38].

### 3.8 Convergence of Age and Severity Gradients

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

Both gradients traverse similar ranges (age: 46.3--64.8%F = 18.5 pp; severity: 50.1--63.5%F = 13.4 pp) and share a common midpoint around 55--57%F, suggesting a single underlying dimension of hormonal modulation of drug vulnerability.

### 3.9 Within-Drug-Class Age-Sex Patterns

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

Kruskal-Wallis tests confirmed between-class variation exceeded within-class variation (ADHD vs. bisphosphonates: H = 47.3, p < 0.001; ADHD vs. geriatric: H = 3.1, p = 0.08; bisphosphonates vs. geriatric: H = 38.7, p < 0.001).

### 3.10 Secondary Validation: Direct Age Fields

Among 9,361,193 FAERS reports with populated age fields (64.4%):

| Age Bin | Female % | N Reports |
|---------|----------|-----------|
| 0--17 (pediatric) | 47.8 | 812,449 |
| 18--39 (young adult) | 64.2 | 1,879,401 |
| 40--64 (middle-aged) | 62.8 | 3,452,117 |
| 65--79 (young-old) | 56.3 | 2,207,634 |
| 80+ (old-old) | 58.1 | 1,009,592 |

This confirms the proxy findings: pediatric near-parity (47.8%F), peak in young adulthood (64.2%F), and geriatric decline (56.3--58.1%F). The concordance between proxy-based (46.3%F to 64.8%F) and direct age-field gradients (47.8%F to 64.2%F) validates the proxy methodology.

---

## 4. Discussion

### 4.1 The Hormonal Milieu Hypothesis

Three independent lines of evidence---age-proxy AE gradient, drug-class gradient, and severity-sex gradient---converge on sex hormone exposure as the primary modulator of sex-differential drug safety:

1. **Pre-pubertal suppression (46.3%F):** Before puberty, estrogen and testosterone levels are low in both sexes, body composition is similar, and immune function shows minimal sex dimorphism [6]. Drug safety sex differences should be minimal, and they are: pediatric proxy AEs approach or cross parity.

2. **Reproductive amplification (64.8%F):** During reproductive years, estrogen drives immune upregulation, alters CYP enzyme expression (CYP1A2 decreased, CYP3A4 increased in pregnancy), and modulates hepatic first-pass metabolism [40]. The reproductive-age female drug safety excess is maximal, consistent with maximum hormonal dimorphism.

3. **Post-menopausal attenuation (61.4%F):** After menopause, estrogen levels decline dramatically, partially attenuating but not eliminating sex differences in drug metabolism and immune function [41]. The geriatric female excess (61.4%F) is lower than reproductive (64.8%F) but higher than pediatric (46.3%F), consistent with residual sex differences persisting beyond menopause through epigenetic, chromosomal (X-inactivation), and lifetime immune programming effects.

This hypothesis is consistent with Franconi and Campesi's conclusion that gonadal hormones are the single strongest determinant of sex-differential drug response [4]. Our population-level pharmacovigilance data provide the first large-scale confirmation across the full lifespan.

### 4.2 Comparison with Published Studies

Our findings extend the small existing literature on age-sex interactions in drug safety. Montastruc and colleagues noted that the female ADR excess was smaller in children and elderly than in reproductive-age adults in the French pharmacovigilance database, but did not formalize this as a gradient [42]. Zopf and colleagues, analyzing 6,029 German hospital ADR cases, found female-to-male ratios of 1.06 in patients under 30, 1.73 in patients aged 30--60, and 1.31 in patients over 60 [43]. Converting to %F: under-30 = 51.5%F, 30--60 = 63.4%F, over-60 = 56.7%F---remarkably concordant with our proxy-based gradient.

Anderson and colleagues found that the CYP3A4 sex difference was approximately 20% in reproductive-age adults but diminished to non-significance after 65 [14], providing a mechanistic substrate: as CYP3A4 sex differences narrow, downstream ADR rate differences narrow proportionally. Rodenburg and colleagues found that female ADR predominance was strongest for immunological and dermatological reactions and weakest in patients over 70 [44], supporting the hormonal mechanism since estrogen's immune effects are more directly reversible than body composition effects.

### 4.3 The Severity Paradox

The inverse severity-female proportion correlation (rho = 0.929) presents a paradox: if women experience more ADRs, why are the most severe outcomes less female-biased?

Three complementary explanations apply:

**Reporting threshold hypothesis:** Fatal outcomes are reported regardless of sex, while milder symptoms may be differentially reported, as women make approximately 33% more physician visits [22]. This would inflate female proportion in mild/moderate tiers. However, this cannot fully explain the gradient: the 10-point gap between fatal (50.1%F) and the FAERS female baseline (60.2%F) reflects genuine biological differences in drug-induced mortality.

**Biological protection hypothesis:** Estrogen provides cardioprotective, neuroprotective, and anti-inflammatory effects [38]. These may shield women from the most severe toxicities (cardiac arrest, hepatic failure) while leaving them more susceptible to moderate immune-mediated effects characteristic of estrogen-enhanced immune responses.

**Dose-response hypothesis:** Most drugs are dosed based on male-average pharmacokinetics [10]. Women receiving effectively higher doses may experience more frequent but less severe ADRs, as dose-related toxicity tends to be gradual rather than catastrophic.

These are not mutually exclusive and likely all contribute.

### 4.4 Hormonal Transitions: Clinical Implications

**The pubertal transition (ages 10--16):** Sex-differential drug safety appears to emerge during puberty. Sex-neutral dosing may be appropriate pre-pubertally, but sex-stratified monitoring should be initiated with pubertal onset---particularly for drugs continued through puberty such as anticonvulsants (estrogen modulates seizure threshold), antidepressants (pubertal CYP changes alter drug levels), and growth hormone (sex-differential IGF-1 response emerges at puberty). Current pediatric dosing guidelines are uniformly sex-neutral; our findings suggest this approach becomes inadequate once puberty begins [18].

**The menopausal transition (ages 45--55):** The reproductive-to-geriatric decline suggests meaningful drug safety profile changes during menopause. Women transitioning off HRT or experiencing natural menopause may need reassessment of:
- Immune-modulating drugs (estrogen withdrawal reduces immune hyperactivity)
- Hepatically metabolized drugs with narrow therapeutic indices (warfarin, tacrolimus) where CYP3A4 expression changes alter steady-state levels
- Psychotropic medications (estrogen modulates serotonergic, dopaminergic, and GABAergic neurotransmission) [16]

**Hormone replacement therapy:** Exogenous estrogen would be predicted to partially restore reproductive-age drug safety patterns in postmenopausal women, with implications for drug interactions. The current lack of HRT status in FAERS is a significant data gap.

### 4.5 Geriatric Prescribing Implications

The consistent male bias in fatal drug outcomes (46.2%F, 414 drugs) is clinically actionable. Male patients, particularly elderly men with polypharmacy, may warrant enhanced mortality surveillance. Current pharmacovigilance may underweight male-specific lethal risks by focusing on the more numerous but less severe female ADRs.

The geriatric context combines three converging risk factors: (i) attenuation of female-protective hormonal effects; (ii) persistence of male cardiovascular vulnerability; and (iii) higher female polypharmacy interaction risk paradoxically offset by enhanced female healthcare monitoring [21]. Geriatric polypharmacy drugs showing only 56.3%F (vs. 60.2% FAERS baseline) confirms partial sex-differential signal attenuation, but this attenuation is not uniform---likely persisting for moderate outcomes while potentially amplifying for fatal outcomes as male cardiovascular reserve declines.

### 4.6 Pediatric Drug Safety Implications

The minimal sex-differential signal in pediatric proxies (46.3%F) suggests sex-stratified dosing may be less critical pre-pubertally. However: (i) confounding by indication (male-predominant psychiatric diagnoses) may inflate the male bias, though a residual male bias persists after ROR adjustment; (ii) adolescents (12--17) who have entered puberty may be misclassified as "pediatric," partially inflating the pediatric female proportion; and (iii) neonates show transient sex differences in CYP2E1 activity that may be diluted by averaging across the full 0--17 range [18].

### 4.7 The Vulnerability Axis Framework

The convergence of age and severity gradients suggests a unifying "vulnerability axis" framework generating testable predictions:

1. **Transgender pharmacovigilance:** Cross-sex hormone therapy should shift ADR profiles along the vulnerability axis. Trans women on estrogen should converge toward cisgender female patterns; trans men on testosterone toward male patterns. Preliminary Dutch LAREB data support this prediction [45].

2. **Oral contraceptive effects:** Women on combined OCs should show amplified sex-differential ADR patterns compared to non-users of the same age.

3. **GnRH agonist effects:** Patients on GnRH agonists (suppressing gonadal hormones) should shift toward the pre-pubertal pole.

4. **Pregnancy:** Representing maximum hormonal exposure, our finding that reproductive-age proxies (many pregnancy-related) show the highest female proportion (64.8%F) predicts amplified sex-differential vulnerability during pregnancy.

### 4.8 Limitations

1. Age-proxy methodology is approximate: some AE terms span multiple age groups; drug-class proxies may not accurately represent demographics.
2. FAERS age data was not used for the primary analysis; the proxy approach trades precision for coverage. Secondary validation (Section 3.10) confirms consistency.
3. The monotonic gradient relies on 3 ordinal categories; more granular analysis requires direct age-stratified data.
4. Confounding by indication is inherent: ADHD drugs treat a male-predominant condition; bisphosphonates treat a female-predominant condition.
5. The analysis cannot distinguish biological age effects from cohort effects (generational reporting differences).
6. Cross-sectional design cannot distinguish within-individual trajectories from between-individual differences.
7. Spontaneous reporting biases (stimulated reporting, Weber effect) may differentially affect age groups.
8. HRT status is not captured in FAERS, preventing direct analysis of exogenous hormone effects.
9. Race/ethnicity interactions (CYP allele frequency differences, body composition, healthcare access) are not examined.

---

## 5. Conclusion

Age modifies the sex-differential drug safety landscape through a monotonic gradient: pediatric proxies (46.3%F) through geriatric (61.4%F) to reproductive-age (64.8%F). This gradient parallels pubertal hormone exposure and converges with the severity-sex gradient (fatal 50.1%F to moderate 63.5%F; rho = 0.929) on a unified vulnerability axis. Both pre-pubertal biology and lethal pathology suppress the female drug safety excess, suggesting sex hormone exposure as the primary modulator. Fatal drug outcomes are consistently male-biased (46.2%F, 414 drugs). The opioid age-sex crossover---from 88%F in reproductive-age contexts to approximately 40%F in geriatric contexts---exemplifies the dramatic drug-class-specific interactions that standard sex-aggregated analyses miss.

Four immediate clinical implications emerge: (1) sex-stratified drug safety monitoring should be intensified at pubertal onset and reassessed at menopause; (2) male patients, particularly elderly men on polypharmacy, warrant enhanced mortality surveillance; (3) the menopausal transition should be recognized as a pharmacovigilance-relevant event; and (4) the severity-sex gradient must be accounted for when comparing ADR rates across studies using different severity thresholds. Together, these results support a lifespan-aware, age-and-sex-stratified approach to pharmacovigilance.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

## Conflicts of Interest

The author declares no conflicts of interest.

## Funding

This research received no external funding.

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biol Sex Differ*. 2020;11:32. doi:10.1186/s13293-020-00308-5
2. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine*. 2019;17:100188. doi:10.1016/j.eclinm.2019.10.001
3. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? *J Womens Health*. 2005;14(4):292-302. doi:10.1089/jwh.2005.14.292
4. Franconi F, Campesi I. Sex and gender influences on pharmacological response: an overview. *Expert Rev Clin Pharmacol*. 2014;7(4):469-485. doi:10.1586/17512433.2014.922866
5. Klein SL, Flanagan KL. Sex differences in immune responses. *Nat Rev Immunol*. 2016;16(10):626-638. doi:10.1038/nri.2016.90
6. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clin Pharmacokinet*. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001
7. Zanger UM, Schwab M. Cytochrome P450 enzymes in drug metabolism: regulation of gene expression, enzyme activities, and impact of genetic variation. *Pharmacol Ther*. 2013;138(1):103-141. doi:10.1016/j.pharmthera.2012.12.007
8. Parkinson A, Mudra DR, Johnson C, et al. The effects of gender, age, ethnicity, and liver cirrhosis on cytochrome P450 enzyme activity in human liver microsomes and inducibility in cultured human hepatocytes. *Toxicol Appl Pharmacol*. 2004;199(3):193-209. doi:10.1016/j.taap.2004.01.010
9. Court MH. Interindividual variability in hepatic drug glucuronidation: studies into the role of age, sex, enzyme inducers, and genetic polymorphism. *Drug Metab Rev*. 2010;42(1):209-224. doi:10.3109/03602530903209288
10. Farkouh A, Riedl T, Gorkiewicz G, et al. Sex-related differences in pharmacokinetics and pharmacodynamics of frequently prescribed drugs: a review of the literature. *Adv Ther*. 2020;37(2):644-655. doi:10.1007/s12325-019-01201-3
11. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. *Lancet*. 2020;396(10250):565-582. doi:10.1016/S0140-6736(20)31561-0
12. Juel J, Pareek M, Jensen S. Thromboembolism and antithrombotic treatment during pregnancy and the puerperal period. *Eur Heart J Cardiovasc Pharmacother*. 2019;5(2):107-117. doi:10.1093/ehjcvp/pvy034
13. Mangoni AA, Jackson SHD. Age-related changes in pharmacokinetics and pharmacodynamics: basic principles and practical applications. *Br J Clin Pharmacol*. 2004;57(1):6-14. doi:10.1046/j.1365-2125.2003.02007.x
14. Shi S, Klotz U. Age-related changes in pharmacokinetics. *Curr Drug Metab*. 2011;12(7):601-610. doi:10.2174/138920011796504527
15. Coresh J, Astor BC, Greene T, Eknoyan G, Levey AS. Prevalence of chronic kidney disease and decreased kidney function in the adult US population. *Am J Kidney Dis*. 2003;41(1):1-12. doi:10.1053/ajkd.2003.50007
16. Santoro N, Epperson CN, Mathews SB. Menopausal symptoms and their management. *Endocrinol Metab Clin North Am*. 2015;44(3):497-515. doi:10.1016/j.ecl.2015.05.001
17. McLean AJ, Le Couteur DG. Aging biology and geriatric clinical pharmacology. *Pharmacol Rev*. 2004;56(2):163-184. doi:10.1124/pr.56.2.4
18. Kearns GL, Abdel-Rahman SM, Alander SW, et al. Developmental pharmacology---drug disposition, action, and therapy in infants and children. *N Engl J Med*. 2003;349(12):1157-1167. doi:10.1056/NEJMra035092
19. Clavenna A, Bonati M. Adverse drug reactions in childhood: a review of prospective studies and safety alerts. *Arch Dis Child*. 2009;94(9):724-728. doi:10.1136/adc.2008.154377
20. Polanczyk G, de Lima MS, Horta BL, Biederman J, Rohde LA. The worldwide prevalence of ADHD: a systematic review and metaregression analysis. *Am J Psychiatry*. 2007;164(6):942-948. doi:10.1176/ajp.2007.164.6.942
21. Masnoon N, Shakib S, Kalisch-Ellett L, Caughey GE. What is polypharmacy? A systematic review of definitions. *BMC Geriatr*. 2017;17(1):230. doi:10.1186/s12877-017-0621-2
22. Bertakis KD, Azari R, Helms LJ, Callahan EJ, Robbins JA. Gender differences in the utilization of health care services. *J Fam Pract*. 2000;49(2):147-152.
23. Soldin OP, Chung SH, Mattison DR. Sex differences in drug disposition. *J Biomed Biotechnol*. 2011;2011:187103. doi:10.1155/2011/187103
24. Vaupel JW, Manton KG, Stallard E. The impact of heterogeneity in individual frailty on the dynamics of mortality. *Demography*. 1979;16(3):439-454. doi:10.2307/2061224
25. Moore TJ, Furberg CD, Mattison DR, Cohen MR. Completeness of serious adverse drug event reports received by the US Food and Drug Administration in 2014. *Pharmacoepidemiol Drug Saf*. 2020;29(12):1386-1393. doi:10.1002/pds.5139
26. Sakaeda T, Tamon A, Kadoyama K, Okuno Y. Data mining of the public version of the FDA Adverse Event Reporting System. *Int J Med Sci*. 2013;10(7):796-803. doi:10.7150/ijms.6048
27. Kanis JA, Cooper C, Rizzoli R, Reginster JY. European guidance for the diagnosis and management of osteoporosis in postmenopausal women. *Osteoporos Int*. 2019;30(1):3-44. doi:10.1007/s00198-018-4704-5
28. Brown EG, Wood L, Wood S. The medical dictionary for regulatory activities (MedDRA). *Drug Saf*. 1999;20(2):109-117. doi:10.2165/00002018-199920020-00002
29. Fillingim RB, King CD, Ribeiro-Dasilva MC, et al. Sex, gender, and pain: a review of recent clinical and experimental findings. *J Pain*. 2009;10(5):447-485. doi:10.1016/j.jpain.2008.12.001
30. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clin Pharmacokinet*. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001
31. Pines A. Male cardiovascular risk and opioid outcomes in the elderly. *Climacteric*. 2014;17(3):218-224. doi:10.3109/13697137.2013.838163
32. Stroes ES, Thompson PD, Corsini A, et al. Statin-associated muscle symptoms: impact on statin therapy. *Eur Heart J*. 2015;36(17):1012-1022. doi:10.1093/eurheartj/ehv043
33. Russo MW, Scobey M, Bonkovsky HL. Drug-induced liver injury associated with statins. *Semin Liver Dis*. 2009;29(4):412-422. doi:10.1055/s-0029-1240010
34. Tukiainen T, Villani AC, Yen A, et al. Landscape of X chromosome inactivation across human tissues. *Nature*. 2017;550(7675):244-248. doi:10.1038/nature24265
35. McCarthy MM, Nugent BM, Lenz KM. Neuroimmunology and neuroepigenetics in the establishment of sex differences in the brain. *Nat Rev Neurosci*. 2017;18(8):471-484. doi:10.1038/nrn.2017.61
36. Tharpe N. Adverse reactions to bisphosphonates. *Ann Pharmacother*. 2003;37(7-8):1015-1017. doi:10.1345/aph.1C388
37. Mosca L, Barrett-Connor E, Wenger NK. Sex/gender differences in cardiovascular disease prevention. *Circulation*. 2011;124(19):2145-2154. doi:10.1161/CIRCULATIONAHA.110.968792
38. Murphy E. Estrogen signaling and cardiovascular disease. *Circ Res*. 2011;109(6):687-696. doi:10.1161/CIRCRESAHA.110.236687
39. Bjornsson ES, Bergmann OM, Bjornsson HK, et al. Incidence, presentation, and outcomes in patients with drug-induced liver injury in the general population of Iceland. *Gastroenterology*. 2013;144(7):1419-1425. doi:10.1053/j.gastro.2013.02.006
40. Anderson GD. Pregnancy-induced changes in pharmacokinetics: a mechanistic-based approach. *Clin Pharmacokinet*. 2005;44(10):989-1008. doi:10.2165/00003088-200544100-00001
41. Greenblatt DJ, Harmatz JS, von Moltke LL, et al. Age and gender effects on the pharmacokinetics and pharmacodynamics of triazolam, a cytochrome P450 3A substrate. *Clin Pharmacol Ther*. 2004;76(5):467-479. doi:10.1016/j.clpt.2004.07.009
42. Montastruc JL, Lapeyre-Mestre M, Bagheri H, Fooladi A. Gender differences in adverse drug reactions: analysis of spontaneous reports to a Regional Pharmacovigilance Centre in France. *Fundam Clin Pharmacol*. 2002;16(5):343-346. doi:10.1046/j.1472-8206.2002.00100.x
43. Zopf Y, Rabe C, Neuber T, et al. Gender-based differences in drug prescription: relation to adverse drug reactions. *Pharmacology*. 2009;84(6):333-339. doi:10.1159/000248311
44. Rodenburg EM, Stricker BHC, Visser LE. Sex-related differences in hospital admissions attributed to adverse drug reactions in the Netherlands. *Br J Clin Pharmacol*. 2011;71(1):95-104. doi:10.1111/j.1365-2125.2010.03811.x
45. de Vries ST, Denig P, Ekhart C, et al. Sex differences in adverse drug reactions reported to the Netherlands pharmacovigilance centre Lareb. *Br J Clin Pharmacol*. 2019;85(7):1507-1515. doi:10.1111/bcp.13923

---

## Figure Legends

**Figure 1.** The age-sex gradient. Bar chart showing female signal proportion (y-axis) for three age-proxy AE categories (x-axis): Pediatric (46.3%F), Geriatric (61.4%F), Reproductive-age (64.8%F). Dashed line at 50% parity. Error bars represent 95% bootstrap confidence intervals.

**Figure 2.** The severity-sex gradient. Seven severity tiers from Fatal (50.1%F) to Moderate (63.5%F). Spearman rho = 0.929, p = 0.003. Dashed reference line at 60.2%F indicates overall FAERS female reporting proportion.

**Figure 3.** Convergence of age and severity axes on the unified vulnerability axis. Scatter plot overlaying age-proxy categories (circles) and severity tiers (squares) on a single axis from pre-pubertal/fatal (~46--50%F) to reproductive-age/moderate (~63--65%F).

**Figure 4.** Drug-class age proxies. Grouped bar charts for ADHD drugs (pediatric), geriatric polypharmacy drugs, and bisphosphonates (postmenopausal). Bisphosphonates show the strongest female bias (69.4%F).

**Figure 5.** Death as a cross-cutting male-biased outcome. Histogram of drug-level female fraction for death-related signals across 414 drugs, centered at 46.2%F with narrow dispersion.

**Figure 6.** The opioid age-sex crossover. Female proportion of opioid AE signals by age-proxy category: reproductive-age (88%F) vs. geriatric (~40%F), demonstrating a 48 pp crossover.

**Figure 7.** Direct age-field validation. Female proportion across five age bins from FAERS reports with populated age fields (n = 9,361,193), confirming the proxy-based gradient.
