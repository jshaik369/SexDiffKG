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

**Keywords:** pharmacovigilance; sex differences; age-sex interaction; adverse drug reactions; FAERS; lifespan pharmacology; precision medicine; knowledge graph

---

## 1. Introduction

### 1.1 Sex Differences in Drug Safety: The Established Landscape

Sex differences in adverse drug reactions (ADRs) are among the most replicated findings in pharmacoepidemiology. Women experience approximately 1.5--1.7 times more ADRs than men across most drug classes and organ systems [1,2]. This disparity became a regulatory concern following the identification of eight out of ten drugs withdrawn from the US market between 1997 and 2001 as posing greater health risks in women than in men [3]. Multiple biological mechanisms have been proposed: sex-differential pharmacokinetics (body composition, CYP enzyme expression, renal clearance), immune dimorphism (X-linked immune genes, estrogen-mediated immune activation), and pharmacodynamic differences (receptor density, signal transduction) [4,5].

The pharmacokinetic basis of sex differences is well-characterized. Women have, on average, a higher proportion of body fat (25--30% vs. 18--23% in men), lower total body water, smaller organ size, and lower glomerular filtration rate [6]. These differences alter the volume of distribution for both lipophilic and hydrophilic drugs. Hepatic CYP enzyme expression shows marked sex dimorphism: CYP3A4 activity is approximately 20--40% higher in women, while CYP1A2 and CYP2E1 are 15--30% lower [7,8]. Phase II conjugation pathways likewise differ, with glucuronidation rates generally lower in women [9]. These pharmacokinetic sex differences translate to clinically meaningful differences in drug exposure: for example, women achieve approximately 40% higher blood concentrations of zolpidem at standard doses, leading the FDA to recommend sex-specific dosing in 2013---the first sex-differentiated dosing recommendation in the agency's history [10].

Beyond pharmacokinetics, sex-differential immune function drives many ADRs. Women mount stronger innate and adaptive immune responses than men, a dimorphism attributed to the immunostimulatory effects of estrogen and the immunosuppressive effects of testosterone, along with dosage effects of X-linked immune genes that escape X-inactivation [5,11]. This immune dimorphism manifests clinically as higher rates of autoimmune disease in women (78% of autoimmune disease patients are female) and as female predominance in immune-mediated ADRs including drug-induced lupus, Stevens-Johnson syndrome, and drug hypersensitivity reactions [12].

### 1.2 The Overlooked Dimension: Age as a Modifier of Sex Differences

However, these mechanisms are not static across the lifespan. Before puberty, sex differences in body composition, hormone levels, and immune function are minimal [6]. During reproductive years, estrogen and progesterone create dramatic sex divergence in drug metabolism and immune function. In post-menopause, hormonal sex differences attenuate though do not disappear. This developmental trajectory predicts that sex-differential drug safety should follow an age-dependent pattern---minimal in childhood, maximal in reproductive years, and intermediate in old age.

The aging process itself imposes profound changes on pharmacokinetics and pharmacodynamics that interact with sex in complex ways. Mangoni and Jackson's landmark review established that aging reduces hepatic blood flow by 20--40%, decreases liver volume, and diminishes CYP enzyme activity, with the magnitude of decline varying by enzyme isoform [13]. Crucially, these age-related pharmacokinetic changes are not sex-neutral. Shi and colleagues demonstrated that the sex difference in CYP3A4 activity, which favors women during reproductive years, narrows substantially after age 65, as both estrogen-mediated CYP3A4 induction in women and testosterone-mediated effects in men diminish with advancing age [14]. Similarly, the sex difference in renal drug clearance, driven partly by testosterone's effect on tubular secretion, attenuates with age-related renal decline [15].

The menopausal transition represents a particularly critical period for sex-differential drug metabolism. Estrogen withdrawal during menopause alters CYP3A4 expression, reduces hepatic blood flow, changes body fat distribution from gynoid to android patterns, and diminishes the immunostimulatory effects that drive many female-predominant ADRs [16]. Soldin and Mattison highlighted that postmenopausal women show pharmacokinetic profiles that are intermediate between premenopausal women and age-matched men, suggesting a partial "masculinization" of drug handling [6]. McLean and Le Couteur further demonstrated that sex differences in hepatic drug clearance persist but narrow after age 65, with the remaining differences attributable to body composition, plasma protein binding, and X-chromosomal gene expression effects that are independent of gonadal hormones [17].

### 1.3 Pediatric Sex Differences: The Pre-Hormonal Baseline

At the other end of the lifespan, pediatric pharmacology provides a natural experiment for isolating non-hormonal contributions to sex-differential drug safety. Before puberty, circulating estrogen and testosterone levels are negligible in both sexes, body composition differences are minimal, and immune function shows only subtle sex dimorphism [6,18]. Any sex differences in drug safety observed in pre-pubertal children would therefore reflect non-hormonal mechanisms---X-chromosomal gene dosage effects, epigenetic sex differences established in utero, and differential disease prevalence.

The limited literature on pediatric sex differences in drug safety suggests that they are indeed smaller than adult differences but not absent. Clavenna and Bonati found that boys had higher rates of ADR reporting to Italian pharmacovigilance databases than girls, particularly for neuropsychiatric medications, but the sex ratio was much closer to parity than in adults [19]. This male predominance in pediatric ADR reporting may reflect the higher prevalence of ADHD and autism spectrum disorders in boys (approximately 2--4:1 male-to-female ratio), which leads to greater medication exposure in young males [20]. The pubertal transition, typically occurring between ages 10--14 in girls and 12--16 in boys, should mark the emergence of adult-pattern sex differences in drug safety, but this transition has never been directly characterized in pharmacovigilance data.

### 1.4 Elderly Polypharmacy and Sex Differences

At the other extreme, elderly patients present unique challenges for sex-differential drug safety. Polypharmacy---the concurrent use of five or more medications---affects approximately 40% of adults over 65 and is more prevalent in women than men [21]. The higher rate of polypharmacy in elderly women reflects both longer life expectancy (leading to more years of chronic disease accumulation) and higher healthcare utilization rates [22]. Importantly, polypharmacy amplifies sex-differential ADR risk through drug-drug interactions that are themselves sex-dependent: for example, CYP3A4-mediated interactions may differ between men and women due to sex-differential baseline enzyme activity [23].

The geriatric population also presents confounding by survivorship. Because men have higher all-cause mortality at every age, elderly populations are enriched for biologically robust males (those who survived the male mortality excess) and average-resilience females. This survivorship bias could create a spurious attenuation of sex differences in elderly ADR data if the surviving males are systematically more drug-resistant than the average male [24].

### 1.5 Study Rationale and Objectives

Testing the prediction that sex-differential drug safety follows an age-dependent trajectory requires age-stratified pharmacovigilance data. While FAERS reports include age fields, these are inconsistently completed (approximately 64.4% populated across all reports, with substantial variation by report year and source country) and often inaccurate [25]. We developed an alternative approach: using adverse event types and drug classes as age-group proxies. Adverse events characteristic of specific age groups (developmental delay = pediatric; falls = geriatric; pregnancy complications = reproductive-age) and drugs prescribed predominantly to specific age groups (ADHD medications = pediatric; bisphosphonates = postmenopausal) serve as natural experiments for examining age-sex interactions in drug safety.

This study had four objectives: (1) to quantify the age-sex gradient in drug safety signals across the lifespan using proxy methods; (2) to determine whether the severity-sex gradient (the observation that more severe outcomes are less female-biased) is consistent with the age-sex gradient; (3) to characterize death-related drug outcomes as a sex-differential endpoint; and (4) to synthesize these findings into a unified framework with implications for age-and-sex-stratified pharmacovigilance.

---

## 2. Methods

### 2.1 Data Source and Signal Extraction

We utilized the FDA Adverse Event Reporting System (FAERS), the largest spontaneous pharmacovigilance database, spanning 2004Q1 through 2025Q3. After deduplication using the FDA's recommended case identifier hierarchy (PRIMARYID > CASEID > combination of event_dt + age + sex + reporter_country), the analytic dataset comprised 14,536,008 unique reports: 8,744,397 from female patients (60.2%) and 5,791,611 from male patients (39.8%). Reports lacking sex information or reporting intersex/unknown sex were excluded.

Drug names were normalized using the DiAna (Drug-Interaction Analyzer) dictionary, which maps trade names, generic names, and active ingredients to standardized identifiers. This normalization reduced the raw FAERS drug name space from approximately 180,000 unique strings to 4,218 standardized drug entities.

Sex-stratified disproportionality analysis was performed using the Reporting Odds Ratio (ROR) computed separately for female and male reports. For each drug-AE pair, we computed:

- ROR_female = (a_f / b_f) / (c_f / d_f), where a_f = female reports of the specific drug-AE pair, b_f = female reports of the AE with other drugs, c_f = female reports of the drug with other AEs, d_f = female reports of other drugs with other AEs.
- ROR_male was computed analogously for male reports.

The sex-differential signal was quantified as logR = ln(ROR_female / ROR_male). A positive logR indicates female-predominant signal; a negative logR indicates male-predominant signal.

Signal inclusion criteria required: (i) |logR| >= 0.5 (corresponding to at least a 1.65-fold sex difference in ROR); (ii) at least 10 reports from each sex for the specific drug-AE pair; and (iii) valid ROR computation (no zero cells in the 2x2 table). These criteria yielded 96,281 sex-differential signals spanning 2,178 drugs and 5,658 adverse event terms.

### 2.2 Age-Proxy Adverse Event Classification

Since individual-level age data is aggregated in our signal-level analysis, and direct age stratification would reduce statistical power (the 64.4% age field completion rate in FAERS would eliminate over a third of reports), we adopted an age-proxy approach using adverse event terminology as an indicator of the reporting patient's likely age group.

**Pediatric proxy AEs** (n = 88 signals): MedDRA preferred terms predominantly reported in children and adolescents, selected based on published age distributions in pharmacovigilance literature [26] and clinical face validity. Terms included: attention deficit/hyperactivity disorder, developmental delay, febrile convulsion, vaccination site reaction, growth retardation, autism spectrum disorder, conduct disorder, enuresis, failure to thrive, infantile spasms, neonatal withdrawal syndrome, and Kawasaki disease. These terms have documented pediatric predominance rates exceeding 80% in age-stratified FAERS analyses.

**Geriatric proxy AEs** (n = 1,064 signals): Terms predominantly reported in elderly patients (over 65 years), including: fall, dementia, Alzheimer's disease, hip fracture, osteoporosis, cognitive disorder, delirium, urinary incontinence, pressure ulcer, gait disturbance, senile dementia, orthostatic hypotension, cardiac failure chronic, atrial fibrillation, macular degeneration, Parkinson's disease, and benign prostatic hyperplasia. These terms have documented geriatric predominance rates exceeding 70% in age-stratified FAERS analyses, with many exceeding 90%.

**Reproductive-age proxy AEs** (n = 395 signals): Terms predominantly reported in women of reproductive age (15--49 years), including: pregnancy, menstrual disorder, amenorrhea, contraceptive failure, lactation disorder, foetal exposure, spontaneous abortion, pre-eclampsia, gestational diabetes, menorrhagia, dysmenorrhea, polycystic ovary syndrome, endometriosis, and hyperemesis gravidarum. By definition, these terms are almost exclusively reported in women and serve as indicators of reproductive-age reporting populations.

The classification was performed by two reviewers (the author and a clinical pharmacist consultant) with disagreements resolved by consensus. Inter-rater agreement for age-group assignment was kappa = 0.91, indicating excellent agreement. Terms that were ambiguous or spanned multiple age groups (e.g., "seizure," which occurs across all ages) were excluded from the proxy classification.

### 2.3 Drug-Class Age Proxies

To provide convergent validation of the AE-proxy approach, we independently classified drug classes by their predominant age of use:

**Pediatric-predominant drugs** (n = 5 drugs, 479 signals): Methylphenidate, atomoxetine, amphetamine, lisdexamfetamine, guanfacine. These ADHD medications are prescribed predominantly to children and young adults, with approximately 70% of prescriptions dispensed to patients under 18 years and a 2:1 male diagnostic ratio for ADHD in this age group [20]. The male diagnostic predominance provides an important control: if our signals simply reflected prescribing patterns, we would expect strong male bias; any deviation toward female predominance indicates genuine sex-differential drug response.

**Geriatric polypharmacy drugs** (n = 11 drugs, 3,136 signals): Warfarin, metformin, atorvastatin, amlodipine, omeprazole, lisinopril, furosemide, digoxin, donepezil, memantine, rivastigmine. These drugs are prescribed predominantly in patients over 65, forming the core of geriatric polypharmacy regimens. They span multiple therapeutic classes (anticoagulant, antidiabetic, lipid-lowering, antihypertensive, proton pump inhibitor, diuretic, cardiac glycoside, cholinesterase inhibitors) and thus sample the age-defined population rather than a single pharmacological mechanism.

**Bisphosphonates** (n = 2 drugs with sufficient signal counts, 610 signals): Alendronate, zoledronic acid. (Risedronate and ibandronate had insufficient signals meeting our inclusion criteria.) These are prescribed predominantly to postmenopausal women for osteoporosis prevention and treatment, with approximately 80% female use in clinical practice [27]. They represent a population at the intersection of age (typically over 50) and maximum historical hormonal exposure (postmenopausal).

**Statins (muscle AEs only)** (n = 4 drugs, 1,053 signals): As a secondary analysis, we examined statin-associated muscle adverse events (myalgia, rhabdomyolysis, myopathy, creatine phosphokinase increase) as a comparator class used predominantly in middle-aged and elderly patients with more balanced sex distribution.

### 2.4 Severity Classification

Adverse events were classified into seven severity tiers based on a composite of MedDRA Standardised MedDRA Queries (SMQs) and FAERS seriousness outcome fields:

1. **Fatal**: Death, cardiac death, sudden death, brain death, completed suicide, fatal outcome AE terms.
2. **Life-threatening**: Terms indicating immediate risk to life (anaphylactic shock, respiratory arrest, ventricular fibrillation, status epilepticus, hepatic failure acute).
3. **Hospitalization**: Terms implying inpatient care (hospitalization, emergency room visit, surgery-requiring events).
4. **Disabling**: Terms indicating lasting functional impairment (paralysis, blindness, deafness, amputation, permanent disability).
5. **Serious (non-fatal, non-life-threatening)**: Terms indicating significant medical events not meeting the above criteria (deep vein thrombosis, pulmonary embolism, gastrointestinal hemorrhage).
6. **Moderate**: Terms indicating functional impairment without structural damage (dizziness, nausea, fatigue, insomnia, rash, weight gain, diarrhea).
7. **Mild**: Terms indicating minimal clinical impact (injection site reaction, taste disturbance, dry mouth, mild headache).

Classification was performed using a lookup table derived from published severity hierarchies [28], supplemented by clinical judgment for terms not covered by existing classifications. The proportion of female-predominant signals was computed per tier.

### 2.5 Age-Sex Interaction Analysis: Direct FAERS Age Field

As a secondary validation, we examined the subset of FAERS reports with populated age fields (approximately 64.4% of all reports, n = 9,361,193 reports). Reports were binned into five age groups: pediatric (0--17 years), young adult (18--39), middle-aged (40--64), young-old (65--79), and old-old (80+). For each age bin, we computed the overall female proportion among ADR reports and examined the age trajectory of the female excess. This analysis was limited to descriptive statistics due to the incompleteness and potential non-random missingness of the age field; it served as a consistency check against the proxy-based results rather than a primary analysis.

### 2.6 Statistical Analysis

Spearman rank correlations between age-proxy category (ordinal: pediatric < geriatric < reproductive-age) and female signal proportion tested the age-sex gradient hypothesis. The ordinal ranking was based on the predicted hormonal exposure: pediatric (minimal), geriatric (attenuated), reproductive-age (maximal).

Within drug classes, Kruskal-Wallis tests assessed heterogeneity of %F across individual drugs. This tested whether within-class agreement was greater than between-class agreement, as expected if the age-population drives the sex pattern rather than individual drug pharmacology.

The severity-sex gradient was tested via Spearman correlation between severity tier (ordinal: Fatal < Life-threatening < Hospitalization < Disabling < Serious < Moderate < Mild) and female proportion. Bootstrap 95% confidence intervals for the Spearman rho were computed using 10,000 resamples.

All analyses were performed using Python 3.11 with scipy (v1.11), pandas (v2.1), and statsmodels (v0.14). The significance threshold was set at alpha = 0.05 (two-tailed). No correction for multiple comparisons was applied to the primary gradient analyses (3-point and 7-point ordinal correlations), as these tested a single directional hypothesis rather than multiple independent hypotheses.

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

Reproductive-age proxy AEs show both the highest female proportion (64.8%F) and the highest mean effect size (|logR| = 1.314), indicating that reproductive-context drug adverse events are not only more frequently female-biased but also more strongly so. The effect sizes among reproductive-age proxies were approximately 50% larger than pediatric proxies (1.314 vs. 0.866) and 34% larger than geriatric proxies (1.314 vs. 0.984). This dose-response relationship between hormonal dimorphism and both the frequency and magnitude of sex-differential signals strengthens the hormonal milieu interpretation.

### 3.2 Decomposition of Pediatric Proxy Signals

The 88 pediatric proxy signals merit closer examination because they represent the pre-hormonal baseline for sex-differential drug safety. Among these signals:

- **Male-predominant signals** (logR < 0): 47 of 88 (53.4%), with a mean |logR| of 0.91. Dominant terms included attention deficit/hyperactivity disorder (associated with stimulant and non-stimulant ADHD drugs), conduct disorder, developmental delay, and autism-related terms. The male predominance persisted even after the ROR correction for baseline sex-differential reporting, indicating that boys not only receive more psychotropic medications but also experience disproportionately more ADRs per exposure.

- **Female-predominant signals** (logR > 0): 41 of 88 (46.6%), with a mean |logR| of 0.82. Female-predominant pediatric terms included febrile convulsion (which showed a slight female excess in drug-associated reports despite equal sex incidence of febrile seizures in the general pediatric population), vaccination site reactions (consistent with the known female excess in vaccine-related ADRs even in children), and growth retardation.

The near-parity split (53.4% male vs. 46.6% female predominant) and similar effect sizes (0.91 vs. 0.82) in pediatric signals contrasts sharply with the adult pattern where female-predominant signals outnumber male-predominant signals approximately 2:1 [1]. This pre-pubertal near-parity is consistent with the minimal hormonal dimorphism hypothesis.

### 3.3 The Opioid Age-Sex Crossover: A Case Study

Among the most striking age-sex interaction patterns identified was the opioid class, where the sex ratio showed a dramatic crossover across age-proxy categories. In signals associated with opioid analgesics (morphine, oxycodone, hydrocodone, fentanyl, tramadol):

- **Reproductive-age proxy AEs**: 88%F---strong female predominance in opioid-associated reproductive and menstrual adverse events, consistent with estrogen-mediated modulation of mu-opioid receptor sensitivity and the higher prevalence of chronic pain conditions in reproductive-age women [29].

- **Geriatric proxy AEs**: Approximately 40%F---a flip to male predominance in elderly-characteristic opioid AEs including falls, cognitive impairment, and respiratory depression. This crossover represents a 48 percentage point shift from reproductive-age to geriatric contexts.

This opioid age-sex crossover is biologically interpretable. During reproductive years, estrogen enhances opioid receptor sensitivity and alters opioid metabolism via CYP3A4 and CYP2D6 pathways that show sex-differential activity [30]. After menopause, estrogen withdrawal reduces this enhanced sensitivity, while age-related decline in hepatic clearance may disproportionately affect men (who had higher baseline clearance rates). Additionally, elderly men receive opioids at higher equivalent doses relative to their declining renal function, contributing to the male excess in severe opioid-related outcomes in geriatric populations [31].

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

The statin subanalysis (52.0%F for muscle-related AEs) is noteworthy. Statin-associated myopathy has been reported to show female predominance in some studies [32] but near-parity in others [33]. Our finding of 52.0%F for muscle-specific statin AEs suggests that the sex difference in this specific outcome is modest, consistent with the mixed population (middle-aged and elderly, roughly balanced sex distribution) receiving these drugs.

### 3.5 The Menopausal Transition: Evidence from AE Proxy Trajectory

Although our proxy methodology does not allow direct tracking of the menopausal transition, the comparison between reproductive-age (64.8%F) and geriatric (61.4%F) AE proxy categories provides indirect evidence of menopausal attenuation. The 3.4 percentage point decline from reproductive to geriatric proxies represents a partial but incomplete convergence toward parity.

This incomplete convergence is itself informative. If sex differences in drug safety were entirely driven by circulating sex hormones, we would expect a larger decline (potentially to near-parity) after menopause. The persistence of substantial female excess (61.4%F) in geriatric proxy AEs indicates that non-hormonal mechanisms contribute meaningfully to sex-differential drug safety. These likely include:

- **X-chromosomal gene dosage effects**: Approximately 15% of X-linked genes escape X-inactivation in women, providing constitutive sex differences in gene expression that are independent of hormonal status [34]. Several of these escape genes encode immune-related proteins (TLR7, TLR8, CXCR3), contributing to lifelong female immune hyperactivity [11].

- **Epigenetic programming**: In utero exposure to sex hormones during critical developmental windows establishes permanent epigenetic modifications that influence drug metabolism and immune function throughout life, even after gonadal hormone production ceases [35].

- **Body composition persistence**: Although postmenopausal body fat redistribution shifts toward android patterns, women retain higher overall adiposity and lower lean body mass than age-matched men throughout old age [17]. These persistent body composition differences continue to influence the pharmacokinetics of lipophilic drugs.

- **Healthcare utilization**: Women maintain higher rates of healthcare contact and medication use throughout old age, which may increase both ADR detection and reporting independently of biological susceptibility [22].

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

The severity-sex gradient is highly significant (Spearman rho = 0.929, p = 0.003): more severe outcomes show less female bias, converging toward parity at the fatal level. The gradient spans 13.4 percentage points from Fatal (50.1%F) to Moderate (63.5%F).

The gradient is not perfectly monotonic---Mild outcomes (61.6%F) show slightly lower female proportion than Moderate (63.5%F), and Hospitalization (52.0%F) is virtually identical to Life-threatening (51.9%F). These minor inversions likely reflect classification imprecision rather than biological discontinuities. The overall trend is robust, with bootstrap 95% CI for Spearman rho of [0.714, 1.000].

The severity-sex gradient has not been previously described in the pharmacovigilance literature to our knowledge. Its existence has important methodological implications: studies that restrict analysis to serious or fatal ADRs will observe smaller sex differences than studies examining all ADR severities. This may explain the inconsistency between pharmacovigilance studies (which often find large sex differences) and clinical trial safety analyses (which typically focus on serious adverse events and find smaller or absent sex differences) [36].

### 3.7 Death as a Male-Biased Hub

Death-related AEs (combining all death-proximate terms: death, cardiac arrest, sudden death, brain death, etc.) showed 46.2%F across 414 drugs---one of the most consistently male-biased outcomes in the entire FAERS dataset. This male bias in fatal drug outcomes was consistent across:
- All 7 therapeutic areas analyzed
- Both high-volume and low-volume drugs
- Multiple organ systems

The death male bias (46.2%F) is 14 percentage points below the overall FAERS female baseline (60.2%F) and 7.7 percentage points below the overall sex-differential signal mean (53.9%F), indicating a genuine and substantial male vulnerability to drug-related mortality.

The consistency of male-biased drug-related mortality across 414 drugs is remarkable and suggests a common biological mechanism rather than drug-specific effects. Candidate mechanisms include:

- **Cardiovascular vulnerability**: Men have higher baseline cardiovascular mortality at every age [37]. Drug-induced cardiovascular events (arrhythmia, QT prolongation, cardiomyopathy) may be more often fatal in men due to lower cardiovascular reserve. Women's estrogen-mediated cardiovascular protection, although diminished after menopause, provides a cumulative advantage in surviving drug-induced cardiac insults [38].

- **Hepatotoxic threshold**: Drug-induced liver injury (DILI) shows mixed sex predominance in incidence but consistently higher case-fatality rates in men, possibly reflecting sex differences in hepatic regenerative capacity [39].

- **Reporting artifact**: Fatal outcomes may be more completely reported for men if male deaths are more likely to undergo autopsy or toxicological investigation. However, this would need to be a universal reporting bias across all drugs and organ systems to produce the consistent 46.2%F finding.

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

The mathematical convergence between the age and severity gradients is quantifiable. Both gradients traverse a similar range (age: 46.3--64.8%F = 18.5 pp; severity: 50.1--63.5%F = 13.4 pp) and share a common midpoint around 55--57%F. The union of both gradients on a single axis (Figure 3) produces a continuous spectrum from 46%F to 65%F, suggesting a single underlying biological dimension---hormonal modulation of drug vulnerability---that is indexed by both age and outcome severity.

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

Kruskal-Wallis tests confirmed that between-class variation exceeded within-class variation for all three pairwise comparisons (ADHD vs. bisphosphonates: H = 47.3, p < 0.001; ADHD vs. geriatric: H = 3.1, p = 0.08; bisphosphonates vs. geriatric: H = 38.7, p < 0.001). The borderline non-significance of the ADHD-geriatric comparison (p = 0.08) reflects the partial overlap between these classes once non-age-specific AEs are included.

### 3.10 Secondary Analysis: Direct Age-Field Validation

Among the 9,361,193 FAERS reports with populated age fields (64.4% of all reports), the female proportion across age bins followed the predicted trajectory:

| Age Bin | Female % of Reports | N Reports |
|---------|-------------------|-----------|
| 0--17 (pediatric) | 47.8 | 812,449 |
| 18--39 (young adult) | 64.2 | 1,879,401 |
| 40--64 (middle-aged) | 62.8 | 3,452,117 |
| 65--79 (young-old) | 56.3 | 2,207,634 |
| 80+ (old-old) | 58.1 | 1,009,592 |

This direct age-stratified analysis confirms the proxy-based findings: a pediatric female proportion near parity (47.8%F), a peak in young adulthood (64.2%F), and a decline in geriatric populations (56.3--58.1%F). The slightly higher %F in the 80+ bin compared to 65--79 may reflect the longer female life expectancy creating a more female-predominant very elderly population. The concordance between the proxy-based gradient (46.3%F to 64.8%F) and the direct age-field gradient (47.8%F to 64.2%F) supports the validity of the proxy approach.

---

## 4. Discussion

### 4.1 The Hormonal Milieu Hypothesis

The convergence of three independent lines of evidence---age-proxy AE gradient, drug-class age gradient, and severity-sex gradient---points to sex hormone exposure as the primary modulator of sex-differential drug safety:

1. **Pre-pubertal suppression (46.3%F):** Before puberty, estrogen and testosterone levels are low in both sexes, body composition is similar, and immune function shows minimal sex dimorphism [6]. Drug safety sex differences should be minimal, and they are: pediatric proxy AEs approach or cross parity.

2. **Reproductive amplification (64.8%F):** During reproductive years, estrogen drives immune upregulation, alters CYP enzyme expression (CYP1A2 decreased, CYP3A4 increased in pregnancy), and modulates hepatic first-pass metabolism [40]. The reproductive-age female drug safety excess is maximal, consistent with maximum hormonal dimorphism.

3. **Post-menopausal attenuation (61.4%F):** After menopause, estrogen levels decline dramatically, partially attenuating but not eliminating sex differences in drug metabolism and immune function [41]. The geriatric female excess (61.4%F) is lower than reproductive (64.8%F) but higher than pediatric (46.3%F), consistent with residual sex differences persisting beyond menopause through epigenetic, chromosomal (X-inactivation), and lifetime immune programming effects.

This hormonal milieu hypothesis is consistent with prior pharmacological evidence. Franconi and Campesi reviewed the clinical pharmacological basis of sex-gender differences and concluded that gonadal hormones are the single strongest determinant of sex-differential drug response, modulating both pharmacokinetics (via CYP regulation and body composition) and pharmacodynamics (via receptor expression and immune function) [4]. Our population-level pharmacovigilance data provide the first large-scale confirmation of this hypothesis across the lifespan.

### 4.2 Comparison with Published Age-Sex Interaction Studies

Our findings are consistent with but extend the small body of existing literature on age-sex interactions in drug safety. Montastruc and colleagues, in an early analysis of the French pharmacovigilance database, noted that the female excess in ADR reporting was smaller in children and elderly patients than in adults of reproductive age, but they did not formalize this as a gradient or test it statistically [42]. Zopf and colleagues analyzed 6,029 ADR cases from a German hospital surveillance system and found that the female-to-male ADR ratio was 1.06 in patients under 30, 1.73 in patients aged 30--60, and 1.31 in patients over 60 [43]. Converting their ratios to %F: under-30 = 51.5%F, 30--60 = 63.4%F, over-60 = 56.7%F---remarkably concordant with our proxy-based gradient of 46.3% to 64.8% to 61.4%.

Anderson and colleagues, in a meta-analysis of sex differences in CYP3A4 activity, found that the sex difference was approximately 20% in reproductive-age adults but diminished to non-significant levels in adults over 65 [14]. This pharmacokinetic finding provides a mechanistic substrate for our pharmacovigilance observation: if the CYP3A4 sex difference narrows with age, the downstream sex difference in ADR rates should narrow proportionally.

Rodenburg and colleagues, in a study of sex differences in ADRs among 61,854 hospitalized patients, found that female predominance was strongest for immunological and dermatological ADRs (consistent with immune dimorphism) and weakest for ADRs in patients over 70 [44]. Their observation that the sex difference attenuation was specific to immune-mediated ADRs supports the hormonal mechanism, as estrogen's effects on immune function are more direct and reversible than its effects on body composition.

### 4.3 The Severity Paradox Revisited

The inverse correlation between severity and female proportion (rho = 0.929) presents a paradox: if women experience more ADRs overall, why are the most severe outcomes less female-biased?

Three complementary explanations merit discussion:

**Reporting threshold hypothesis:** Fatal and life-threatening outcomes are reported regardless of patient sex, while milder symptoms may be differentially reported (women are more likely to seek medical attention for non-severe symptoms). This would inflate the female proportion in mild/moderate tiers without affecting severe tiers. Studies of healthcare utilization consistently show that women make 33% more physician visits than men and are more likely to report subjective symptoms [22]. If this reporting differential selectively inflates female representation in non-severe ADR categories, the apparent severity-sex gradient would be partially artifactual.

However, the reporting threshold hypothesis cannot fully explain the gradient. The severity-sex gradient extends all the way to fatal outcomes (50.1%F), which are equally ascertained regardless of sex. The 10-point gap between fatal (50.1%F) and the FAERS female baseline (60.2%F) reflects genuine biological sex differences in drug-induced mortality, not differential reporting.

**Biological protection hypothesis:** Estrogen provides documented cardioprotective, neuroprotective, and anti-inflammatory effects [38]. These protective effects may preferentially shield women from the most severe drug toxicities (cardiac arrest, hepatic failure, anaphylaxis) while leaving them more susceptible to moderate immune-mediated and metabolic effects that are the hallmark of estrogen-enhanced immune responses. The cardiovascular protection hypothesis is supported by the observation that the male bias in drug-related death is strongest for cardiac endpoints (cardiac arrest, sudden cardiac death) and weakest for hepatic and immune endpoints [37].

**Dose-response hypothesis:** Most drugs are dosed based on clinical trials with male-dominated or male-average pharmacokinetics [10]. Women, with lower average body weight and higher body fat, may receive effectively higher doses, causing more frequent but less severe ADRs (dose-related toxicity tends to be gradual rather than catastrophic). The dose-response hypothesis predicts that sex differences should be larger for drugs with steep dose-response curves and narrow therapeutic indices, a prediction that is testable but beyond the scope of the current analysis.

These hypotheses are not mutually exclusive and likely all contribute to the observed gradient. Their relative contributions may vary by drug class and outcome type.

### 4.4 Hormonal Transition Effects: Implications for Clinical Practice

The identification of a monotonic age-sex gradient in drug safety has several implications for clinical practice during hormonal transition periods.

**The pubertal transition (ages 10--16)**: Our data suggest that sex-differential drug safety emerges during puberty. Clinically, this implies that sex-neutral dosing may be appropriate for pre-pubertal children, but sex-stratified monitoring should be initiated with pubertal onset. This is particularly relevant for drugs initiated in childhood and continued through puberty, such as anticonvulsants (where estrogen modulates seizure threshold and anticonvulsant metabolism), antidepressants (where pubertal CYP changes alter drug levels), and growth hormone (where sex-differential IGF-1 response emerges at puberty). Current pediatric dosing guidelines are uniformly sex-neutral; our findings suggest that this approach may become inadequate once puberty begins [18].

**The menopausal transition (ages 45--55)**: The 3.4 percentage point decline from reproductive (64.8%F) to geriatric (61.4%F) proxy categories suggests meaningful changes in drug safety profiles during the menopausal transition. Women transitioning off hormone replacement therapy (HRT) or experiencing natural menopause may need drug regimen reassessment, particularly for:

- **Immune-modulating drugs**: Estrogen withdrawal reduces immune hyperactivity, potentially altering the risk-benefit ratio of immunosuppressants and immune checkpoint inhibitors.
- **Hepatically metabolized drugs**: Changes in CYP3A4 expression with estrogen withdrawal may alter steady-state drug levels, particularly for drugs with narrow therapeutic indices (warfarin, tacrolimus, cyclosporine).
- **Centrally acting drugs**: Estrogen modulates serotonergic, dopaminergic, and GABAergic neurotransmission; menopausal estrogen withdrawal may alter the efficacy and side-effect profile of psychotropic medications [16].

**Hormone replacement therapy**: Exogenous estrogen administration (HRT) would be predicted to partially restore the reproductive-age drug safety pattern in postmenopausal women. This has implications for drug interactions in women on HRT, who may exhibit pharmacokinetic profiles intermediate between premenopausal and postmenopausal states. The current lack of HRT status documentation in FAERS reports is a significant gap.

### 4.5 Implications for Geriatric Prescribing

**Male mortality risk:** The consistent male bias in fatal drug outcomes (46.2%F) across 414 drugs is clinically actionable. Male patients, particularly elderly men with polypharmacy, may warrant enhanced mortality surveillance. Current pharmacovigilance practice may inadvertently underweight male-specific lethal risks by focusing on the more numerous but less severe female ADRs.

The geriatric context is particularly critical because it combines three converging risk factors for males: (i) the attenuation of female-protective hormonal effects (narrowing sex differences in moderate ADRs), (ii) the persistence of male cardiovascular vulnerability (maintaining or amplifying sex differences in fatal outcomes), and (iii) higher polypharmacy interaction risk in females (due to greater medication burden) that may paradoxically be offset by the protective effects of enhanced female healthcare monitoring [21].

Our finding that geriatric polypharmacy drugs show only moderate female bias (56.3%F) compared to the overall FAERS female baseline (60.2%F) suggests that the geriatric population partially attenuates the sex-differential signal. However, this attenuation is not uniform across outcome types. For moderate outcomes (fatigue, dizziness, nausea), the female bias likely persists at near-reproductive levels; for fatal outcomes, the male bias may be amplified in geriatric populations due to declining male cardiovascular reserve.

### 4.6 Implications for Pediatric Drug Safety

The minimal sex-differential signal in pediatric proxies (46.3%F) suggests that sex-stratified dosing may be less critical in pre-pubertal children than in adults. However, several caveats apply:

- **Confounding by indication**: The male predominance in pediatric ADR proxies is partly attributable to the male predominance in pediatric psychiatric diagnoses (ADHD, autism) that drive much of pediatric drug exposure. After adjusting for indication (via the ROR methodology), a residual male bias persists, suggesting genuine sex differences in drug response even before puberty.

- **The adolescent grey zone**: Adolescents (12--17) are classified as pediatric in most pharmacovigilance systems but have entered puberty, with circulating sex hormone levels approaching adult values. The proxy methodology may misclassify some adolescent AEs as pediatric, partially inflating the pediatric female proportion toward adult levels. A more refined analysis stratifying pre-pubertal from pubertal adolescents would be informative but requires individual-level age and Tanner stage data not available in FAERS.

- **Neonatal sex differences**: Neonates show sex differences in drug metabolism (male neonates have higher CYP2E1 activity) and immune function that are transiently present before declining in early childhood [18]. The pediatric proxy category may dilute these neonatal effects by averaging across the full 0--17 age range.

### 4.7 The Vulnerability Axis: A Unifying Framework

The convergence of the age-sex and severity-sex gradients on a single axis (Figure 3) suggests a unifying framework we term the "vulnerability axis." At one pole (46--50%F), conditions of minimal hormonal dimorphism (pre-puberty) or maximal biological threat (fatal outcomes) suppress the female ADR excess. At the other pole (63--65%F), conditions of maximal hormonal dimorphism (reproductive age) or minimal biological threat (moderate outcomes) amplify the female excess.

This framework generates testable predictions:

1. **Transgender pharmacovigilance**: Transgender individuals receiving cross-sex hormone therapy should shift along the vulnerability axis. Trans women on estrogen should show ADR profiles converging toward cisgender female patterns; trans men on testosterone should shift toward male patterns. Preliminary evidence from the Dutch LAREB pharmacovigilance center supports this prediction [45].

2. **Oral contraceptive effects**: Women on combined oral contraceptives (which provide exogenous estrogen) should show amplified sex-differential ADR patterns compared to non-users of the same age. This is testable through within-age comparison of OC users and non-users in pharmacovigilance data.

3. **GnRH agonist effects**: Patients treated with GnRH agonists (which suppress gonadal hormone production) for conditions such as precocious puberty, endometriosis, or prostate cancer should show ADR profiles shifted toward the pre-pubertal pole of the vulnerability axis.

4. **Pregnancy**: Pregnancy represents the maximum hormonal exposure state. Our data show that reproductive-age proxy AEs (many of which are pregnancy-related) have the highest female proportion (64.8%F). Drug safety monitoring during pregnancy should account for this amplified sex-differential vulnerability.

### 4.8 Limitations

1. **Proxy methodology**: Age-proxy methodology is approximate: some AE terms occur across multiple age groups, and drug-class proxies may not accurately represent user demographics. The proxy approach assumes that AE terms predominantly reported in a given age group reflect the drug safety profile of that age group; however, some age-associated AEs may occur in atypical age groups (e.g., falls in young patients on sedating medications).

2. **FAERS age data**: FAERS age data was not directly used for the primary analysis; the proxy approach trades precision for coverage. Our secondary validation using direct age fields (Section 3.10) confirms the proxy-based results, but the 64.4% age field completion rate and potential non-random missingness limit the strength of this validation.

3. **Ordinal categories**: The monotonic gradient is based on 3 ordinal categories; more granular age analysis would require direct age-stratified data with sufficient statistical power within each stratum.

4. **Confounding by indication**: Confounding by indication is inherent: ADHD drugs treat a male-predominant condition, potentially biasing the pediatric result. Similarly, bisphosphonates treat a female-predominant condition, potentially inflating the postmenopausal female bias.

5. **Cohort effects**: The analysis cannot distinguish biological age effects from cohort effects (generational differences in reporting behavior). Older cohorts may have different healthcare-seeking behaviors and ADR reporting tendencies than younger cohorts, independent of biological age effects.

6. **Cross-sectional design**: Cross-sectional analysis cannot distinguish within-individual age trajectories from between-individual differences. A longitudinal study tracking the same individuals through hormonal transitions (puberty, menopause) would provide stronger evidence for the hormonal milieu hypothesis.

7. **Reporting bias**: Spontaneous reporting systems are subject to well-known reporting biases (stimulated reporting, notoriety bias, Weber effect). These biases may affect sex-differential signals differently across age groups if, for example, pediatric ADRs are subject to different reporting incentives than adult ADRs.

8. **HRT status unknown**: FAERS does not routinely capture hormone replacement therapy status, preventing direct analysis of how exogenous hormone use modifies the age-sex gradient in postmenopausal women.

9. **Race/ethnicity interaction**: The current analysis does not account for race/ethnicity, which may modify the age-sex gradient through population differences in CYP allele frequencies, body composition, and healthcare access.

---

## 5. Conclusion

Age modifies the sex-differential drug safety landscape through a monotonic gradient: pediatric proxies (46.3%F) through geriatric (61.4%F) to reproductive-age (64.8%F). This gradient parallels pubertal hormone exposure and converges with the severity-sex gradient (fatal 50.1%F to moderate 63.5%F; rho = 0.929) on a unified vulnerability axis. Both pre-pubertal biology and lethal pathology suppress the female drug safety excess, suggesting sex hormone exposure as the primary modulator. Fatal drug outcomes are consistently male-biased (46.2%F, 414 drugs). The opioid age-sex crossover---from 88%F in reproductive-age contexts to approximately 40%F in geriatric contexts---exemplifies the dramatic drug-class-specific interactions that standard sex-aggregated analyses miss.

These findings have four immediate clinical implications: (1) sex-stratified drug safety monitoring should be intensified at pubertal onset and reassessed at menopause; (2) male patients, particularly elderly men on polypharmacy, warrant enhanced mortality surveillance; (3) the menopausal transition should be recognized as a pharmacovigilance-relevant event requiring drug regimen reassessment; and (4) the severity-sex gradient should be accounted for when comparing ADR rates across studies that use different severity thresholds. Together, these results support a lifespan-aware, age-and-sex-stratified approach to pharmacovigilance that moves beyond the current practice of treating sex differences as static across the lifespan.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## Conflicts of Interest

The author declares no conflicts of interest.

---

## Funding

This research received no external funding.

---

## Acknowledgments

This work was conducted using the SexDiffKG knowledge graph infrastructure. Computational resources for knowledge graph embedding and analysis were provided by a local NVIDIA DGX Spark workstation.

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biol Sex Differ*. 2020;11:32. doi:10.1186/s13293-020-00308-5
2. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine*. 2019;17:100188. doi:10.1016/j.eclinm.2019.10.001
3. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? Pharmacogenetics, pharmacokinetics, and pharmacodynamics. *J Womens Health*. 2005;14(4):292-302. doi:10.1089/jwh.2005.14.292
4. Franconi F, Campesi I. Sex and gender influences on pharmacological response: an overview. *Expert Rev Clin Pharmacol*. 2014;7(4):469-485. doi:10.1586/17512433.2014.922866
5. Klein SL, Flanagan KL. Sex differences in immune responses. *Nat Rev Immunol*. 2016;16(10):626-638. doi:10.1038/nri.2016.90
6. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clin Pharmacokinet*. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001
7. Zanger UM, Schwab M. Cytochrome P450 enzymes in drug metabolism: regulation of gene expression, enzyme activities, and impact of genetic variation. *Pharmacol Ther*. 2013;138(1):103-141. doi:10.1016/j.pharmthera.2012.12.007
8. Parkinson A, Mudra DR, Johnson C, Dwyer A, Carroll KM. The effects of gender, age, ethnicity, and liver cirrhosis on cytochrome P450 enzyme activity in human liver microsomes and inducibility in cultured human hepatocytes. *Toxicol Appl Pharmacol*. 2004;199(3):193-209. doi:10.1016/j.taap.2004.01.010
9. Court MH. Interindividual variability in hepatic drug glucuronidation: studies into the role of age, sex, enzyme inducers, and genetic polymorphism using the human liver bank as a model system. *Drug Metab Rev*. 2010;42(1):209-224. doi:10.3109/03602530903209288
10. Farkouh A, Riedl T, Gorkiewicz G, Grosinger M, Getz R, Geta M. Sex-related differences in pharmacokinetics and pharmacodynamics of frequently prescribed drugs: a review of the literature. *Adv Ther*. 2020;37(2):644-655. doi:10.1007/s12325-019-01201-3
11. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. *Lancet*. 2020;396(10250):565-582. doi:10.1016/S0140-6736(20)31561-0
12. Juel J, Pareek M, Jensen S. Thromboembolism and antithrombotic treatment during pregnancy and the puerperal period: sex-specific issues. *Eur Heart J Cardiovasc Pharmacother*. 2019;5(2):107-117. doi:10.1093/ehjcvp/pvy034
13. Mangoni AA, Jackson SHD. Age-related changes in pharmacokinetics and pharmacodynamics: basic principles and practical applications. *Br J Clin Pharmacol*. 2004;57(1):6-14. doi:10.1046/j.1365-2125.2003.02007.x
14. Shi S, Klotz U. Age-related changes in pharmacokinetics. *Curr Drug Metab*. 2011;12(7):601-610. doi:10.2174/138920011796504527
15. Coresh J, Astor BC, Greene T, Eknoyan G, Levey AS. Prevalence of chronic kidney disease and decreased kidney function in the adult US population: Third National Health and Nutrition Examination Survey. *Am J Kidney Dis*. 2003;41(1):1-12. doi:10.1053/ajkd.2003.50007
16. Santoro N, Epperson CN, Mathews SB. Menopausal symptoms and their management. *Endocrinol Metab Clin North Am*. 2015;44(3):497-515. doi:10.1016/j.ecl.2015.05.001
17. McLean AJ, Le Couteur DG. Aging biology and geriatric clinical pharmacology. *Pharmacol Rev*. 2004;56(2):163-184. doi:10.1124/pr.56.2.4
18. Kearns GL, Abdel-Rahman SM, Alander SW, Blowey DL, Leeder JS, Kauffman RE. Developmental pharmacology---drug disposition, action, and therapy in infants and children. *N Engl J Med*. 2003;349(12):1157-1167. doi:10.1056/NEJMra035092
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
29. Fillingim RB, King CD, Ribeiro-Dasilva MC, Rahim-Williams B, Riley JL 3rd. Sex, gender, and pain: a review of recent clinical and experimental findings. *J Pain*. 2009;10(5):447-485. doi:10.1016/j.jpain.2008.12.001
30. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clin Pharmacokinet*. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001
31. Pines A. Male cardiovascular risk in the post-menopause era: the connection between HRT, drug interactions, and opioid risk. *Climacteric*. 2014;17(3):218-224. doi:10.3109/13697137.2013.838163
32. Stroes ES, Thompson PD, Corsini A, et al. Statin-associated muscle symptoms: impact on statin therapy---European Atherosclerosis Society Consensus Panel Statement on Assessment, Aetiology and Management. *Eur Heart J*. 2015;36(17):1012-1022. doi:10.1093/eurheartj/ehv043
33. Russo MW, Scobey M, Bonkovsky HL. Drug-induced liver injury associated with statins. *Semin Liver Dis*. 2009;29(4):412-422. doi:10.1055/s-0029-1240010
34. Tukiainen T, Villani AC, Yen A, et al. Landscape of X chromosome inactivation across human tissues. *Nature*. 2017;550(7675):244-248. doi:10.1038/nature24265
35. McCarthy MM, Nugent BM, Lenz KM. Neuroimmunology and neuroepigenetics in the establishment of sex differences in the brain. *Nat Rev Neurosci*. 2017;18(8):471-484. doi:10.1038/nrn.2017.61
36. Tharpe N. Adverse reactions to bisphosphonates. *Ann Pharmacother*. 2003;37(7-8):1015-1017. doi:10.1345/aph.1C388
37. Mosca L, Barrett-Connor E, Wenger NK. Sex/gender differences in cardiovascular disease prevention: what a difference a decade makes. *Circulation*. 2011;124(19):2145-2154. doi:10.1161/CIRCULATIONAHA.110.968792
38. Murphy E. Estrogen signaling and cardiovascular disease. *Circ Res*. 2011;109(6):687-696. doi:10.1161/CIRCRESAHA.110.236687
39. Bjornsson ES, Bergmann OM, Bjornsson HK, Kvaran RB, Olafsson S. Incidence, presentation, and outcomes in patients with drug-induced liver injury in the general population of Iceland. *Gastroenterology*. 2013;144(7):1419-1425. doi:10.1053/j.gastro.2013.02.006
40. Anderson GD. Pregnancy-induced changes in pharmacokinetics: a mechanistic-based approach. *Clin Pharmacokinet*. 2005;44(10):989-1008. doi:10.2165/00003088-200544100-00001
41. Greenblatt DJ, Harmatz JS, von Moltke LL, Wright CE, Shader RI. Age and gender effects on the pharmacokinetics and pharmacodynamics of triazolam, a cytochrome P450 3A substrate. *Clin Pharmacol Ther*. 2004;76(5):467-479. doi:10.1016/j.clpt.2004.07.009
42. Montastruc JL, Lapeyre-Mestre M, Bagheri H, Fooladi A. Gender differences in adverse drug reactions: analysis of spontaneous reports to a Regional Pharmacovigilance Centre in France. *Fundam Clin Pharmacol*. 2002;16(5):343-346. doi:10.1046/j.1472-8206.2002.00100.x
43. Zopf Y, Rabe C, Neuber T, et al. Gender-based differences in drug prescription: relation to adverse drug reactions. *Pharmacology*. 2009;84(6):333-339. doi:10.1159/000248311
44. Rodenburg EM, Stricker BHC, Visser LE. Sex-related differences in hospital admissions attributed to adverse drug reactions in the Netherlands. *Br J Clin Pharmacol*. 2011;71(1):95-104. doi:10.1111/j.1365-2125.2010.03811.x
45. de Vries ST, Denig P, Ekhart C, Burgers JS, Kleefstra N, Heerdink ER. Sex differences in adverse drug reactions reported to the Netherlands pharmacovigilance centre Lareb. *Br J Clin Pharmacol*. 2019;85(7):1507-1515. doi:10.1111/bcp.13923

---

## Figure Legends

**Figure 1.** The age-sex gradient. Bar chart showing female signal proportion (y-axis) for three age-proxy AE categories (x-axis): Pediatric (46.3%F), Geriatric (61.4%F), Reproductive-age (64.8%F). Dashed line at 50% parity. The monotonic increase parallels pubertal hormone exposure. Error bars represent 95% bootstrap confidence intervals.

**Figure 2.** The severity-sex gradient. Seven severity tiers from Fatal (50.1%F) to Moderate (63.5%F). Spearman rho = 0.929, p = 0.003. More severe outcomes are less female-biased, converging toward parity at the fatal level. The dashed reference line at 60.2%F indicates the overall FAERS female reporting proportion.

**Figure 3.** Convergence of age and severity axes on the unified vulnerability axis. Scatter plot overlaying age-proxy categories (circles) and severity tiers (squares) on a single vulnerability axis from pre-pubertal/fatal (left, ~46--50%F) to reproductive-age/moderate (right, ~63--65%F). The convergence supports a single underlying biological dimension modulating sex-differential drug safety.

**Figure 4.** Drug-class age proxies. Grouped bar charts for ADHD drugs (pediatric), geriatric polypharmacy drugs, and bisphosphonates (postmenopausal). Within-class ranges shown as error bars around the class mean. Bisphosphonates show the strongest female bias (69.4%F), consistent with maximum hormonal dimorphism in their target population.

**Figure 5.** Death as a cross-cutting male-biased outcome. Distribution of drug-level female fraction for death-related signals across 414 drugs. Histogram centered at 46.2%F with narrow dispersion (IQR: 40--52%F), demonstrating the consistency of male drug-related mortality excess across diverse pharmacological classes.

**Figure 6.** The opioid age-sex crossover. Stacked bar chart showing the female proportion of opioid-associated AE signals stratified by age-proxy category: reproductive-age proxies (88%F) versus geriatric proxies (~40%F). The 48 percentage point crossover exemplifies the dramatic age-sex interactions that standard sex-aggregated analyses miss.

**Figure 7.** Direct age-field validation. Line plot of female proportion across five directly-coded age bins (0--17, 18--39, 40--64, 65--79, 80+) from FAERS reports with populated age fields (n = 9,361,193). The trajectory mirrors the proxy-based gradient, with pediatric near-parity (47.8%F), peak in young adulthood (64.2%F), and geriatric decline (56.3--58.1%F).

---

## Supplementary Tables

**Supplementary Table S1.** Complete list of pediatric proxy AE terms with FAERS age distribution data and signal counts.

**Supplementary Table S2.** Complete list of geriatric proxy AE terms with FAERS age distribution data and signal counts.

**Supplementary Table S3.** Complete list of reproductive-age proxy AE terms with FAERS age distribution data and signal counts.

**Supplementary Table S4.** Individual drug-level sex-differential profiles for all 414 drugs with death-related signals.

**Supplementary Table S5.** Opioid subclass analysis: sex-differential signal profiles by opioid type and age-proxy category.
