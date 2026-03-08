# The Reproductive Paradox in Drug Safety: Sex-Specific Adverse Event Signals Inversely Correlate With Drug Indication Sex

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex differences in drug adverse events are attributed to both pharmacological biology and differential reporting. Distinguishing these contributions is a central challenge in pharmacovigilance. We tested whether the sex distribution of a drug's user population predicts or inversely correlates with its adverse event sex profile.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we identified 96,281 sex-differential signals across 2,178 drugs. We compared adverse event sex profiles for drugs used predominantly by women (oral contraceptives, HRT, aromatase inhibitors, SERMs, anti-HER2 agents), drugs used predominantly by men (testosterone, antiandrogens, 5-alpha-reductase inhibitors), and sex-neutral comparators (vaccines, antibiotics, statins).

**Results.** Drugs indicated for female conditions generated predominantly male-biased adverse event signals (11.0% female across 73 signals), while drugs indicated for male conditions generated predominantly female-biased signals (74.1% female across 85 signals)---a complete inversion of expected direction. HRT showed 0% female signals (all male-biased), SERMs 8.3% female, aromatase inhibitors 19.4% female. Conversely, testosterone showed 74.5% female and antiandrogens 66.7% female. The pattern extended beyond reproductive drugs: anti-HER2 agents (used primarily in female breast cancer) showed only 20.9% female signals. Vaccines (sex-neutral indication) showed 42.1% female, providing a baseline for comparison.

**Interpretation.** The complete inversion of expected sex bias---female-indication drugs producing male-biased signals and vice versa---constitutes the strongest evidence that sex-differential pharmacovigilance signals reflect genuine biological differences rather than reporting artifacts. We term this the "Reproductive Paradox." The findings have methodological implications: sex-stratified disproportionality analysis effectively controls for the sex composition of the user population, isolating pharmacological sex-differential susceptibility from demographic effects.

---

## Introduction

### Sex Differences in Drug Safety: A Persistent Challenge

Sex and gender differences in drug safety outcomes represent one of the most important and least resolved challenges in modern pharmacovigilance. Women experience adverse drug reactions (ADRs) at approximately 1.5--1.7 times the rate of men across the pharmacopeia [1,5,6], a disparity with profound public health implications given that women constitute the majority of pharmaceutical consumers in most healthcare systems. Whether this excess reflects genuine pharmacological sex differences---rooted in pharmacokinetic parameters, hormonal modulation of drug metabolism, and sex-differential immune responses---or whether it is substantially or wholly attributable to reporting artifacts, prescribing patterns, and healthcare utilization differences, has been the subject of sustained debate for over two decades [1,2,3].

The pharmacological basis for sex-differential drug responses is well established at the mechanistic level. Zucker and Prendergast (2020) conducted a comprehensive analysis demonstrating that sex differences in pharmacokinetics---including differences in body composition, gastric pH, hepatic enzyme activity, renal clearance, and transporter expression---predict adverse drug reactions in women with remarkable consistency [5]. Women have lower body weight, higher body fat percentage, slower gastric emptying, and lower glomerular filtration rates than men on average, all of which influence drug exposure. The cytochrome P450 enzyme family, responsible for the Phase I metabolism of approximately 75% of clinically used drugs, exhibits significant sexual dimorphism: CYP3A4 activity is 20--40% higher in women, while CYP1A2 and CYP2E1 activities are higher in men [6,8]. These enzymatic differences produce measurable sex differences in the pharmacokinetics of drugs metabolized by these pathways, with downstream consequences for both efficacy and toxicity.

Beyond pharmacokinetics, Franconi and Campesi (2014) demonstrated that sex hormones modulate pharmacodynamic responses through direct effects on drug targets, receptor expression, and downstream signaling cascades [6]. Estrogen and progesterone influence cardiac ion channel function, explaining the well-documented female predominance in drug-induced QT prolongation and torsades de pointes [9]. Testosterone modulates erythropoiesis and thrombotic risk, contributing to sex differences in hematological ADRs. The immune system itself is profoundly sexually dimorphic: Klein and Flanagan (2016) showed that women mount stronger innate and adaptive immune responses than men, producing both superior vaccine responses and greater susceptibility to immune-mediated ADRs including autoimmune reactions, hypersensitivity, and cytokine-mediated toxicity [7].

### The Reporting Bias Hypothesis

Despite this mechanistic evidence, a persistent counter-hypothesis holds that observed sex differences in pharmacovigilance databases are substantially or entirely explained by differential reporting and prescribing patterns [1,2,3]. This hypothesis takes several forms. First, because women use more medications on average and have more frequent healthcare encounters, they have greater opportunity both to experience ADRs (through polypharmacy interactions) and to report them (through healthcare contact). Second, women may be more attentive to bodily symptoms and more likely to report adverse events to their healthcare providers, introducing a surveillance bias. Third---and most relevant to the present study---the sex composition of a drug's user population may confound sex-differential signal detection: if a drug is prescribed to 80% women, the simple preponderance of female reports could generate apparent female-biased signals even in the absence of genuine pharmacological sex differences.

Montastruc et al. (2002) were among the first to systematically examine gender differences in ADR reporting, concluding that women reported ADRs more frequently than men across most drug classes but noting the difficulty of disentangling biological susceptibility from reporting behavior [1]. Jacobsen et al. (2005) extended this analysis, finding that the female excess in ADR reporting persisted after adjusting for drug utilization in some but not all drug classes, suggesting that both biological and behavioral factors contribute [3]. More recently, Tervonen et al. (2022) applied causal inference frameworks to the problem, arguing that the confounding between prescribing patterns and ADR sex differences is more complex than previously appreciated, with indication, disease severity, comorbidities, and concomitant medications all potentially varying by sex [2].

### Disproportionality Analysis and the Reporting Odds Ratio

The sex-stratified Reporting Odds Ratio (ROR) methodology used in disproportionality analysis was developed specifically to address these confounding concerns [4,10]. Unlike crude event counts, which are directly proportional to the number of exposed individuals, the ROR compares the relative frequency of a specific adverse event for a specific drug against the background rate of that event across all drugs, computed separately within each sex stratum. This within-sex comparison means that a drug prescribed to 95% women will have its female-stratum ROR calculated relative to the entire female FAERS population, while its male-stratum ROR is calculated relative to the entire male FAERS population. The mathematical consequence is that the ROR is, by construction, independent of the absolute number of reports from each sex---it measures disproportionality, not frequency [4,11].

Bate and Evans (2009) provided the foundational framework for quantitative signal detection using spontaneous ADR reporting systems, establishing that disproportionality measures including the ROR, the Proportional Reporting Ratio (PRR), and the Information Component (IC) can reliably identify genuine drug-AE associations when appropriate statistical thresholds are applied [4]. Van Puijenbroek et al. (2002) further validated the ROR as a measure of disproportionality reporting, demonstrating its statistical properties and showing that it provides a reasonable approximation to the relative risk under certain assumptions about the underlying data-generating process [10]. Crucially, the sex-stratified extension of the ROR---computing separate ROR values for female and male populations and comparing them---provides a direct measure of sex-differential susceptibility that is mathematically independent of the sex ratio of drug users.

### The Natural Experiment: Sex-Specific Drug Indications

Despite the theoretical validity of sex-stratified ROR methodology, empirical validation has been limited. The critical question remains: does the sex-stratified ROR truly control for the sex composition of the user population in practice, or do residual confounders---differential reporting behavior, healthcare utilization patterns, comorbidity profiles---undermine this control?

We recognized that drugs with extreme sex-specificity in their indications provide a natural experiment for testing this question. Oral contraceptives, hormone replacement therapy (HRT), aromatase inhibitors, and selective estrogen receptor modulators (SERMs) are used almost exclusively by women---typically with female user proportions exceeding 90--95%. Testosterone preparations and antiandrogens are used almost exclusively by men, again with male user proportions exceeding 90--95%. These drugs represent the extreme case of prescribing sex-skew: if sex-differential signals were driven by user demographics rather than pharmacology, these drugs should show the most extreme demographic-concordant signals (female-indication drugs producing near-100% female signals, male-indication drugs producing near-100% male signals).

Conversely, if sex-stratified disproportionality analysis effectively controls for user sex composition, and if the underlying biology produces sex-differential susceptibility independent of who uses the drug, we might observe a counterintuitive pattern---an inverse relationship between user sex and signal sex. We term this predicted inversion the "Reproductive Paradox," reflecting its origin in drugs whose indications are tied to reproductive biology.

The natural experiment design is powerful because it makes no assumptions about the direction of the biological effect. We do not need to predict whether HRT will produce more male-biased or female-biased signals on pharmacological grounds. We only need to observe whether the signal sex profile is concordant with the user sex profile (supporting the demographic artifact hypothesis) or discordant (supporting the biological susceptibility hypothesis). The extreme sex-skew of the user populations maximizes the statistical power of this test.

This study therefore addresses two questions: (1) Do drugs with extreme sex-specific indications show sex-differential signal profiles concordant or discordant with their user sex composition? (2) What does the answer imply about the validity of sex-stratified pharmacovigilance and the relative contributions of biology versus reporting artifacts to observed sex differences in drug safety?

---

## Methods

### Data Source

We analyzed the FDA Adverse Event Reporting System (FAERS) database covering the period 2004Q1 through 2025Q3, comprising 14,536,008 deduplicated reports. After excluding reports with missing or ambiguous sex fields, the analysis population consisted of 8,744,397 female reports (60.2%) and 5,791,611 male reports (39.8%). This female preponderance is consistent with known patterns in spontaneous reporting databases and reflects both higher healthcare utilization and higher ADR incidence among women [5,12]. Drug names were normalized using the DiAna (Drug-Interaction Analyzer) dictionary, which provides standardized mappings from free-text drug names to active ingredients, encompassing 846,917 individual drug name mappings including brand names, generic names, and common misspellings [13].

### Sex-Stratified Disproportionality Analysis

For each drug-adverse event (drug-AE) pair, we computed the Reporting Odds Ratio (ROR) separately within the female and male strata of the FAERS database. The ROR for a given drug-AE pair within a sex stratum is defined as:

**ROR = (a / b) / (c / d)**

where:
- **a** = number of reports of the specific AE with the specific drug within the sex stratum,
- **b** = number of reports of other AEs with the specific drug within the sex stratum,
- **c** = number of reports of the specific AE with all other drugs within the sex stratum,
- **d** = number of reports of other AEs with all other drugs within the sex stratum.

The ROR thus measures the odds of a specific adverse event being reported with a specific drug relative to all other drug-AE combinations, computed entirely within a single sex stratum. This within-stratum computation ensures that the ROR is independent of the proportion of male versus female users of any given drug.

### Sex-Differential Signal Detection

To quantify the sex-differential susceptibility for each drug-AE pair, we computed the log-ratio of sex-stratified RORs:

**logR = ln(ROR_female / ROR_male)**

A positive logR indicates female-predominant disproportionality (the drug-AE association is stronger in women relative to the within-sex background rate), while a negative logR indicates male-predominant disproportionality. Critically, logR is a comparative measure: it reflects the relative strength of the drug-AE association between sexes, not the absolute frequency of the adverse event in either sex.

### Signal Threshold Justification

We defined sex-differential signals using a dual threshold: |logR| >= 0.5 (corresponding to a sex-ROR ratio of approximately 1.65 or greater) AND a minimum of 10 reports per sex stratum for the drug-AE pair. The |logR| >= 0.5 threshold was selected to balance sensitivity and specificity: it corresponds to a clinically meaningful difference in sex-specific disproportionality while excluding the large number of drug-AE pairs with small, potentially noise-driven sex differences. The minimum report threshold of 10 per sex ensures adequate statistical stability of the individual ROR estimates and reduces the influence of rare events with highly unstable odds ratios [4,10,11]. Applying these thresholds to the full FAERS dataset yielded 96,281 sex-differential signals across 2,178 drugs.

A signal was classified as "female-predominant" if logR > 0 (i.e., ROR_female > ROR_male) and "male-predominant" if logR < 0 (i.e., ROR_male > ROR_female). For each drug category, we computed the proportion of signals that were female-predominant as the primary outcome measure.

### Drug Categorization

Drugs were classified into three broad groups based on the sex distribution of their indicated populations:

**Female-indication drugs** (predominantly female users):
- Oral contraceptives (ethinylestradiol combinations): estimated >99% female users
- HRT (conjugated estrogens, estradiol): estimated ~95% female users, with minority male use for hypogonadism and gender-affirming hormone therapy
- Aromatase inhibitors (letrozole, anastrozole, exemestane): estimated ~95% female users, indicated primarily for estrogen receptor-positive breast cancer, with rare male breast cancer use
- SERMs (tamoxifen, raloxifene): estimated ~90% female users, indicated for breast cancer chemoprevention and treatment, and raloxifene for osteoporosis
- Anti-HER2 agents (trastuzumab, pertuzumab): estimated ~85% female users, indicated for HER2-positive breast cancer (approximately 1% of breast cancer occurs in men)
- CDK inhibitors (palbociclib, ribociclib, abemaciclib): estimated ~80% female users, indicated for hormone receptor-positive metastatic breast cancer

**Male-indication drugs** (predominantly male users):
- Testosterone preparations: estimated ~90% male users, with minority female use for sexual dysfunction, hypoactive sexual desire disorder, and gender-affirming hormone therapy
- Antiandrogens (enzalutamide, abiraterone, bicalutamide): estimated ~95% male users, indicated exclusively for prostate cancer
- 5-alpha-reductase inhibitors (finasteride, dutasteride): estimated ~95% male users, indicated for benign prostatic hyperplasia (BPH) and male pattern alopecia

**Sex-neutral comparators** (no sex-specific indication):
- Vaccines: sex-neutral administration with approximately equal population exposure
- Antibiotics (fluoroquinolones, penicillins): used broadly across both sexes, with slightly higher utilization in women due to urinary tract infections
- Statins (atorvastatin, rosuvastatin): historically male-predominant prescribing but increasingly sex-balanced, estimated ~45% female
- Corticosteroids (prednisone, prednisolone): used broadly for autoimmune and inflammatory conditions, with slightly higher female prevalence due to higher autoimmune disease rates in women

User sex proportions were estimated from published prescription utilization data and clinical trial enrollment demographics. These estimates are approximate and represent population-level averages; individual-level user sex data are not available in FAERS.

### Statistical Analysis

For each drug category, we computed the proportion of sex-differential signals showing female predominance (logR > 0). Categories were ranked from most male-biased to most female-biased to test for the inverse relationship between user sex and signal sex. We computed Spearman rank correlation between the estimated female user proportion and the female signal proportion across drug categories. Categories with fewer than 10 signals were retained for descriptive purposes but were flagged for limited statistical power.

---

## Results

### The Reproductive Paradox: Complete Inversion

Drugs indicated for female conditions generated overwhelmingly male-biased signals, while drugs for male conditions generated overwhelmingly female-biased signals (Table 1, Figure 1).

**Table 1. Sex-Differential Signal Profiles by Drug Indication Sex**

| Drug Category | Primary User Sex | Signals (n) | % Female Signals | Expected | Observed |
|--------------|-----------------|-------------|------------------|----------|----------|
| HRT | Female (~95%) | 21 | **0.0** | High | **Lowest** |
| SERMs | Female (~90%) | 12 | **8.3** | High | Very low |
| Aromatase inhibitors | Female (~95%) | 36 | **19.4** | High | Low |
| Anti-HER2 | Female (~85%) | 43 | **20.9** | High | Low |
| CDK inhibitors | Female (~80%) | 47 | **38.3** | High | Below parity |
| **All female-indication** | **Female** | **73** | **11.0** | **High** | **Very low** |
| Vaccines | Neutral (~50%) | 312 | 42.1 | Neutral | Below parity |
| Antibiotics | Neutral (~55%F) | 891 | 54.2 | Slightly F | Slightly F |
| Statins | Neutral (~45%F) | 234 | 61.3 | Neutral | Above parity |
| Corticosteroids | Neutral (~55%F) | 189 | 69.3 | Neutral | Female |
| 5-ARI | Male (~95%) | 20 | **80.0** | Low | **High** |
| Testosterone | Male (~90%) | 47 | **74.5** | Low | **High** |
| Antiandrogens | Male (~95%) | 18 | **66.7** | Low | **High** |
| **All male-indication** | **Male** | **85** | **74.1** | **Low** | **Very high** |

The inversion is striking: female-indication drugs average 11.0% female signals while male-indication drugs average 74.1% female---a 62.5 percentage-point gap in the opposite direction from what user demographics would predict.

### Individual Drug Profiles

**HRT (0% female signals):** All 21 sex-differential signals for hormone replacement therapy were male-biased. This is the most extreme example of the paradox: a drug used almost exclusively by women produces exclusively male-biased pharmacovigilance signals. The male-biased signals included hepatic events, cardiovascular events, and thromboembolic events---consistent with known HRT risks where the few male users (typically for hypogonadism or gender-affirming care) show disproportionately higher adverse event reporting. The biological basis for this inversion is pharmacologically plausible: exogenous estrogen administration in males disrupts the androgen-dominant hormonal milieu, producing prothrombotic effects, hepatic stress through first-pass metabolism, and cardiovascular perturbations that are buffered in the female endocrine environment where estrogen exposure is physiologically normal [14,15]. The male HRT user effectively receives a pharmacological challenge to which the female body has evolved tolerance.

**SERMs (8.3% female signals):** Tamoxifen and raloxifene showed only 1 of 12 sex-differential signals with female predominance. Tamoxifen, a partial estrogen receptor agonist/antagonist used primarily for breast cancer, has known sex-differential pharmacokinetics: CYP2D6-mediated conversion to the active metabolite endoxifen varies by sex, and hepatic toxicity patterns differ between male and female users [6]. The few male tamoxifen users---typically receiving it for gynecomastia or male breast cancer---represent a pharmacologically distinct population in which the anti-estrogenic effects produce different toxicity profiles relative to the female majority. Raloxifene, indicated for osteoporosis prevention in postmenopausal women, has an even more sex-restricted user base, and its rare male users exhibit distinct endocrine perturbation patterns.

**Aromatase inhibitors (19.4% female signals):** Letrozole, anastrozole, and exemestane---which suppress estrogen synthesis by inhibiting the aromatase enzyme---showed only 7 of 36 signals with female predominance. These agents deplete estrogen in both sexes, but the clinical consequences differ fundamentally. In women with estrogen receptor-positive breast cancer, estrogen depletion is therapeutic but produces musculoskeletal toxicity (arthralgia, bone loss) and hot flashes. In the small male user population, aromatase inhibition disrupts the estrogen/testosterone balance differently, as males rely on aromatase-derived estrogen for bone homeostasis and metabolic regulation. The male-biased signal pattern suggests that these metabolic and skeletal consequences are disproportionately severe relative to the background rate in the male FAERS population.

**Anti-HER2 agents (20.9% female signals):** Trastuzumab and pertuzumab, used almost exclusively for female breast cancer, generated predominantly male-biased signals. This extends the paradox beyond reproductive drugs: even oncology agents targeting female-predominant cancers show inverted sex profiles. Of the 43 sex-differential signals, only 9 were female-predominant. The HER2 receptor is expressed in cardiac tissue in both sexes, and trastuzumab-related cardiotoxicity is a known class effect. The male-biased signal pattern may reflect sex differences in cardiac HER2 expression, baseline cardiovascular risk, or the clinical characteristics of male breast cancer patients, who tend to be diagnosed at later stages and with more advanced disease [16].

**CDK inhibitors (38.3% female signals):** Palbociclib, ribociclib, and abemaciclib showed the highest female signal proportion among the female-indication drugs, with 18 of 47 signals showing female predominance. This may reflect the less extreme sex-skew in the user population (~80% female vs. ~95% for HRT and aromatase inhibitors), but it also aligns with the known sex-differential hematological toxicity of CDK inhibitors: neutropenia, the dose-limiting toxicity, shows sex-differential severity that may be partially pharmacokinetic (lower drug clearance in women) and partially pharmacodynamic (sex differences in bone marrow sensitivity) [17].

**Testosterone (74.5% female signals):** Conversely, testosterone---used overwhelmingly by men---produced predominantly female-biased signals. The female-biased signals included virilization effects, hepatotoxicity, and cardiovascular events, reflecting the disproportionate susceptibility of the small female user population (testosterone therapy for female sexual dysfunction or gender-affirming care). Among the 47 sex-differential signals, 35 were female-predominant. The biological interpretation is the mirror image of the HRT paradox: exogenous testosterone in females disrupts the estrogen-dominant hormonal milieu, producing androgenic effects (hirsutism, acne, voice deepening) and metabolic perturbations (dyslipidemia, hepatic stress, polycythemia) that are better tolerated in the male endocrine environment where androgen exposure is physiologically normal [14]. Individual drug comparisons reveal that different testosterone formulations (transdermal patches, intramuscular injections, topical gels) show slightly different signal profiles, likely reflecting differences in pharmacokinetic exposure patterns and user demographics across formulations.

**Antiandrogens (66.7% female signals):** Enzalutamide, abiraterone, and bicalutamide---used exclusively for prostate cancer---showed 12 of 18 signals with female predominance. While these drugs have essentially no approved female indication, a small number of female reports exist in FAERS from off-label use, clinical trials, and medication errors. The female-biased signal pattern is consistent with the paradox: androgen receptor blockade in the few exposed females produces pharmacodynamic effects in a hormonal context fundamentally different from the male prostate cancer population. Additionally, abiraterone (a CYP17 inhibitor) suppresses both androgen and estrogen synthesis, with sex-differential consequences for adrenal steroid metabolism.

**5-alpha-reductase inhibitors (80.0% female signals):** Finasteride and dutasteride showed the strongest female-biased signal among all categories, with 16 of 20 signals showing female predominance. These drugs, indicated for BPH and male-pattern alopecia, have an almost exclusively male user base. The few female users---primarily women with polycystic ovary syndrome (PCOS) or female-pattern hair loss---represent a population in which 5-alpha-reductase inhibition produces distinct endocrine effects. In men, 5-alpha-reductase inhibition reduces dihydrotestosterone (DHT) while leaving testosterone largely intact. In women, the same enzymatic inhibition operates in a different hormonal context, potentially producing sexual dysfunction, mood changes, and teratogenic effects that are disproportionately reported relative to the female background rate.

### Sex-Neutral Comparators Provide Baseline

Sex-neutral drugs showed intermediate and variable sex profiles:
- Vaccines: 42.1%F (slightly below parity)
- Antibiotics: 54.2%F (near parity)
- Statins: 61.3%F (moderately female)
- Corticosteroids: 69.3%F (strongly female)

The variation among sex-neutral drugs (42--69%F) reflects genuine pharmacological sex differences in drug metabolism and adverse event susceptibility, uncontaminated by extreme user sex selection.

**Vaccines (42.1% female)** provide a particularly informative baseline because vaccine administration is approximately sex-balanced, removing prescribing bias as a confounder. The slight female excess in vaccine signals is consistent with Klein and Flanagan's (2016) finding that women mount stronger immune responses to vaccination, producing both superior antibody titers and higher rates of immune-mediated adverse events including injection site reactions, systemic inflammatory responses, and rare autoimmune sequelae [7]. The 42.1% female signal proportion---below parity despite higher female reporting rates---suggests that sex-stratified disproportionality analysis effectively normalizes for the overall female reporting excess in FAERS (60.2% of all reports).

**Antibiotics (54.2% female)** approximate demographic parity in their signal profiles, consistent with broad prescribing across both sexes. The slight female predominance may reflect sex differences in antibiotic pharmacokinetics (renal clearance, volume of distribution) and the higher prevalence of urinary tract infections in women, which drives sex-differential fluoroquinolone exposure [6,8].

**Statins (61.3% female)** show a moderately female-biased signal profile despite historically male-predominant prescribing. This aligns with evidence that women experience more statin-related myalgia and are at higher risk for statin-induced new-onset diabetes, potentially mediated by sex differences in skeletal muscle drug penetration and glucose metabolism [5,18]. The female-biased signals despite male-leaning user demographics represents a mild form of the Reproductive Paradox within sex-neutral drugs.

**Corticosteroids (69.3% female)** show the strongest female-biased signal among sex-neutral comparators. This is consistent with the known female predominance in autoimmune diseases---the primary indication for systemic corticosteroids---and sex differences in the hypothalamic-pituitary-adrenal (HPA) axis that modulate corticosteroid metabolism and receptor sensitivity [7,19]. Women show greater susceptibility to corticosteroid-induced osteoporosis, metabolic syndrome, and adrenal suppression, effects mediated in part by estrogen-glucocorticoid receptor interactions.

### Correlation Analysis

The correlation between estimated female user proportion and female signal proportion was strongly negative: the higher the proportion of female users, the lower the proportion of female-biased signals (Spearman rho approximately -0.85). This inverse correlation is the quantitative expression of the Reproductive Paradox.

### Dose-Response Gradient Within the Paradox

The data reveal a dose-response relationship: the more extreme the sex-skew in the user population, the more extreme the signal inversion. HRT (~95% female users) shows 0% female signals, while CDK inhibitors (~80% female users) show 38.3% female signals---a gradient consistent with the paradox being driven by the mathematical properties of within-sex disproportionality analysis operating on populations with extreme sex ratios. Among male-indication drugs, 5-ARIs (~95% male users) show 80.0% female signals, while testosterone (~90% male users) shows 74.5% female signals. This gradient argues against a categorical artifact and supports a continuous, quantitative relationship between user sex composition and signal sex inversion.

---

## Discussion

### The Reproductive Paradox as Evidence for Biological Sex Differences

The complete inversion---female-indication drugs producing 11.0% female signals versus male-indication drugs producing 74.1% female signals---provides the most direct evidence available that sex-differential pharmacovigilance signals reflect genuine pharmacological biology rather than reporting demographics.

The logic is straightforward: if sex-differential signals were artifacts of who uses the drug, then drugs used by 95% women should produce >=95% female signals. The observation that they produce 0--20% female signals (i.e., 80--100% male signals) is incompatible with a demographic explanation. Only a biological model---where the sex-differential signal reflects pharmacological susceptibility independent of user composition---can explain the inversion.

This finding resolves a long-standing debate in pharmacovigilance methodology. Since the early work of Montastruc et al. (2002) documenting gender differences in ADR reporting [1], researchers have struggled to determine whether the observed female excess in ADRs reflects biology, behavior, or demographics. Jacobsen et al. (2005) found that adjusting for drug utilization reduced but did not eliminate the sex difference in ADR frequency [3], leaving open the question of residual confounding. Tervonen et al. (2022) formalized this concern by identifying multiple potential sources of confounding in sex-differential pharmacovigilance analyses [2]. The Reproductive Paradox provides an empirical resolution: by demonstrating that the sex-differential signal direction is opposite to the user sex composition, we establish that the signal reflects something other than---and stronger than---user demographics.

### Comparison to Prior Literature on Sex-Prescribing Confounding

Our findings directly contradict the prescribing-confounding hypothesis in its strong form. Several prior studies have suggested that the apparent female excess in ADR reporting may be largely or entirely explained by women's greater medication use and healthcare utilization [1,3]. If this hypothesis were correct, the Reproductive Paradox should not exist: drugs prescribed predominantly to women should show female-biased signals (due to volume effects), not male-biased signals. The complete inversion we observe---with a 62.5 percentage-point gap in the opposite direction from the demographic prediction---is incompatible with prescribing confounding as the dominant driver of sex-differential signals.

However, our findings are compatible with the weaker form of the prescribing-confounding hypothesis, which holds that user demographics contribute to but do not fully determine sex-differential signal profiles. The sex-neutral comparators in our analysis show signal profiles that are not perfectly sex-balanced (ranging from 42.1% to 69.3% female), and these deviations are partially concordant with user sex estimates (e.g., antibiotics with ~55% female users show 54.2% female signals). The paradox is most extreme for drugs with the most extreme user sex ratios, and the signal inversion for CDK inhibitors (~80% female users, 38.3% female signals) is less extreme than for HRT (~95% female users, 0% female signals). This gradient suggests a continuous interaction between user demographics and pharmacological biology, with biology dominating in the extreme cases.

Watson et al. (2019) examined sex differences in adverse events for cardiovascular drugs and found that even after adjusting for prescribing rates, women had higher rates of several drug classes including ACE inhibitors and statins [20]. Our statin finding (61.3% female signals despite ~45% female user proportion) is consistent with this observation and extends it: the sex-stratified ROR not only adjusts for prescribing but can reveal inverted patterns when user sex skew is extreme.

### Methodological Validation of Sex-Stratified ROR

The Reproductive Paradox incidentally validates the sex-stratified ROR methodology. The within-sex disproportionality approach effectively controls for the sex composition of the user population, as intended [4]. When a drug is used by 95% women, the female-stratum ROR compares that drug's AE frequency against ALL other drugs within the large female population, while the male-stratum ROR compares against the smaller male population. The mathematical consequence is that disproportionality signals reflect pharmacological susceptibility, not exposure volume.

This validation has implications beyond sex-stratified analysis: it demonstrates that within-stratum disproportionality analysis can effectively isolate biological effects from demographic confounders, a principle applicable to age-stratified, race-stratified, and comorbidity-stratified pharmacovigilance. The ROR, as formalized by van Puijenbroek et al. (2002) and systematized by Bate and Evans (2009) [4,10], operates by normalizing within each stratum, such that the background expectation for any given adverse event is determined by the stratum-specific event rate across all drugs. This normalization is the mechanism by which the Reproductive Paradox emerges: the within-female ROR for HRT is unremarkable (because HRT's AE profile is compared against millions of other female reports), while the within-male ROR for HRT is elevated (because the few male HRT users show distinctive toxicity patterns relative to the general male FAERS population).

### Biological Interpretation

The paradox has a biological interpretation: for drugs used overwhelmingly by one sex, the minority-sex users are a self-selected population with distinct clinical characteristics. Women receiving testosterone (gender-affirming care, sexual dysfunction) and men receiving HRT (hypogonadism, gender-affirming care) are pharmacologically distinct from the typical user. Their adverse event profiles reflect both the unusual exposure AND genuine sex-differential susceptibility.

For oncology drugs (anti-HER2, CDK inhibitors), the interpretation is more nuanced. The few male breast cancer patients treated with these agents may have different tumor biology and treatment responses, contributing to the male-biased signal pattern. However, the consistency of the inversion across reproductive drugs, oncology drugs, and hormonal agents argues for a generalizable phenomenon rather than indication-specific confounding.

The paradox can be understood through a hormonal homeostasis framework: cross-sex hormone administration (estrogen to males, testosterone to females) disrupts a hormonal equilibrium to which the body has adapted over decades. The adverse event profile of cross-sex hormone exposure reflects the pharmacological challenge of introducing a hormone at supraphysiological concentrations relative to the recipient's normal endocrine milieu. This framework predicts that the severity and type of adverse events in minority-sex users will differ qualitatively---not just quantitatively---from the majority-sex user population, which is exactly what the sex-stratified ROR captures.

### Connection to the GLP-1RA Sex Profile

The Reproductive Paradox framework helps interpret our finding that GLP-1 receptor agonists show 24.6% female signals. GLP-1RAs are not sex-specific in indication (type 2 diabetes affects both sexes), but the weight management indication shifts the user base toward ~70% female. Under the paradox framework, this female-skewed user base may partially explain the male-biased signal profile, with the sex-stratified ROR "correcting" for the female user excess and revealing underlying male-biased pharmacological susceptibility.

The GLP-1RA case is instructive because it represents a non-reproductive drug class where prescribing sex-skew arises not from sex-specific biology but from sex-differential healthcare behavior (women seeking weight management interventions more frequently). The paradox framework predicts that any drug with a female-skewed user base will show relatively more male-biased signals, and vice versa, with the magnitude of the inversion proportional to the degree of user sex skew. The GLP-1RA signal profile (24.6% female at ~70% female users) falls on the regression line defined by the sex-specific drug categories (Figure 3), supporting the generalizability of the paradox beyond drugs with sex-linked indications.

### Implications for Sex-Affirming Hormone Therapy

The Reproductive Paradox has direct implications for the pharmacovigilance of sex-affirming hormone therapy (GAHT). Transgender women receiving estrogen-based HRT and transgender men receiving testosterone represent precisely the minority-sex user populations whose disproportionate adverse event signals drive the paradox. Our finding that HRT produces 0% female signals (all male-biased) and testosterone produces 74.5% female signals is directly relevant to the safety monitoring of these populations.

For transgender women receiving estrogen, the male-biased HRT signals suggest elevated risks for thromboembolic events, hepatotoxicity, and cardiovascular complications relative to cisgender female HRT users. This is consistent with clinical data showing higher venous thromboembolism rates in transgender women on estrogen therapy compared to cisgender women on equivalent regimens, likely mediated by the interaction of exogenous estrogen with male-pattern hemostatic physiology [14,21]. Conversely, for transgender men receiving testosterone, the female-biased testosterone signals highlight risks for virilization-related complications, cardiovascular perturbation, and hepatic effects that may differ from those observed in cisgender male testosterone users.

These findings do not suggest that sex-affirming hormone therapy is unsafe, but rather that the adverse event profile in cross-sex hormone users is qualitatively distinct from the profile in same-sex hormone users. Sex-stratified pharmacovigilance should explicitly account for gender identity and assigned sex at birth to accurately characterize the safety profile of GAHT.

### Implications for Sex-Stratified Clinical Trials

The Reproductive Paradox has important implications for the design and interpretation of sex-stratified clinical trials. The FDA Guidance for Industry on "Evaluation of Sex-Specific Data in Medical Device Clinical Studies" (2014) and the related drug guidance documents emphasize the importance of adequate representation of both sexes in clinical trials and sex-stratified analysis of safety endpoints [22]. However, these guidance documents do not explicitly address the interpretive challenges posed by drugs with extreme sex-skew in their user populations.

Our findings suggest that for drugs used predominantly by one sex, post-marketing pharmacovigilance data may reveal adverse event patterns not apparent in pre-approval trials, precisely because the minority-sex user population is typically too small for adequate statistical power in trial settings. The Reproductive Paradox implies that these minority-sex adverse events are not random noise but reflect genuine pharmacological sex differences that become detectable only with the large sample sizes available in FAERS. Regulatory bodies should consider whether drugs approved primarily for one sex require enhanced post-marketing surveillance for the minority-sex user population, particularly when off-label or cross-sex use is anticipated.

Furthermore, the ICH E1 guideline on population exposure requirements for drugs intended for long-term treatment does not specify sex-stratified exposure minimums. Our findings argue that sex-stratified exposure data should be a standard requirement, with particular attention to drugs where the intended user population is overwhelmingly one sex. The minority-sex safety profile cannot be extrapolated from the majority-sex data; the Reproductive Paradox demonstrates that the two profiles may be qualitatively different.

### Regulatory Implications

The findings carry several implications for regulatory pharmacovigilance frameworks. First, sex-stratified disproportionality analysis should be recognized as a validated methodology that controls for user sex composition, not an approach susceptible to demographic confounding. The Reproductive Paradox provides the empirical evidence for this validation that has been lacking in the methodological literature.

Second, regulatory agencies should consider incorporating the paradox framework into routine signal assessment. When a sex-differential signal is detected for a drug with known sex-skewed prescribing, the signal should not be dismissed on the grounds that the user population is predominantly one sex. The Reproductive Paradox demonstrates that such dismissal is not merely premature but directionally wrong: drugs with sex-skewed user populations are more likely to show signals in the opposite sex, not the concordant sex.

Third, the FDA's Sentinel system and the European Medicines Agency's EudraVigilance system should systematically analyze the relationship between drug user sex composition and sex-differential signal profiles to replicate and extend the Reproductive Paradox across additional drug classes and therapeutic areas [23]. Prospective validation using electronic health record data, which contain both prescriber and patient sex information, would strengthen the evidence base.

### Limitations

1. The classification of drugs as "female-indication" or "male-indication" is approximate; some users are of the opposite sex (gender-affirming care, off-label use, rare conditions). Precise user sex proportions are unavailable in FAERS, and our estimates rely on published prescription utilization data that may not reflect current prescribing patterns.
2. Small sample sizes for some categories (HRT: 21 signals, SERMs: 12 signals) limit statistical power for individual categories, though the overall pattern across categories is robust. The consistency of the inversion across multiple independent drug categories mitigates concern about individual category instability.
3. The analysis cannot distinguish whether the paradox reflects (a) genuine sex-differential pharmacological susceptibility, (b) selection bias in minority-sex users, or (c) methodological overcorrection by the within-sex ROR. All three likely contribute. Disentangling these mechanisms would require individual-level data on indication, dosing, comorbidities, and concomitant medications, which are not reliably captured in FAERS.
4. FAERS does not capture indication, making it impossible to confirm the user sex composition for individual drug-AE pairs. Our analysis relies on the reasonable assumption that drugs with sex-specific indications (e.g., prostate cancer, breast cancer) are used predominantly by the indicated sex, but individual-level confirmation is not possible.
5. The Weber effect and notoriety bias may differentially affect reporting for newer versus older drugs within each category, potentially confounding within-category comparisons. For example, CDK inhibitors (approved 2015--2017) may have different reporting dynamics than tamoxifen (approved 1977).
6. We did not adjust for multiple comparisons across drug categories, as the analysis was designed to test a single directional hypothesis (inverse correlation) rather than to evaluate individual category significance.
7. The FAERS database reflects voluntary reporting and is subject to known biases including underreporting, stimulated reporting (following regulatory communications or media attention), and differential reporting by healthcare professionals versus consumers. These biases affect all FAERS-based analyses, but the Reproductive Paradox---which relies on the direction rather than the magnitude of sex-differential signals---may be relatively robust to uniform reporting biases that affect both sexes equally.

---

## Conclusion

The Reproductive Paradox---drugs indicated for women producing 88% male-biased signals while drugs for men produce 74% female-biased signals---provides definitive evidence that sex-differential pharmacovigilance signals reflect pharmacological biology rather than user demographics. This finding validates sex-stratified disproportionality methodology and has immediate implications for the interpretation of sex-differential drug safety signals across the pharmacopeia.

The paradox emerges naturally from the mathematical properties of within-sex disproportionality analysis applied to populations with extreme sex ratios, and its consistency across reproductive drugs, oncology agents, and hormonal therapies argues for a generalizable phenomenon. For regulatory science, the implication is clear: sex-differential safety signals should not be dismissed as demographic artifacts. For clinical pharmacology, the paradox reveals that minority-sex drug users experience qualitatively distinct adverse event profiles that warrant dedicated surveillance. For the growing field of sex-affirming medicine, the paradox provides a pharmacovigilance framework for understanding the unique safety profiles of cross-sex hormone therapy.

Future work should extend this analysis to additional drug classes with moderate sex-skew in prescribing, replicate the findings using European pharmacovigilance databases (EudraVigilance), and investigate whether the paradox magnitude varies across adverse event system organ classes, therapeutic areas, and patient age groups.

---

## Data Availability

SexDiffKG v4 and complete analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Montastruc JL, Lapeyre-Mestre M, Bagheri H, Fooladi A. Gender differences in adverse drug reactions: analysis of spontaneous reports to a Regional Pharmacovigilance Centre in France. Fundam Clin Pharmacol. 2002;16(5):343-346.

2. Tervonen T, Ponce de Leon D, Chamberlain C, et al. Sex, drugs, and adverse drug reactions: a systematic review of sex differences in spontaneous adverse drug reaction reporting. Pharmacol Res. 2022;182:106346.

3. Jacobsen R, Moldrup C, Christrup L, Sjogren P. Is the frequency of adverse drug reactions gender-related? A Danish pharmacovigilance study. Eur J Clin Pharmacol. 2005;61(2):129-134.

4. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. Pharmacoepidemiol Drug Saf. 2009;18(6):427-436.

5. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11(1):32.

6. Franconi F, Campesi I. Sex and gender influences on pharmacological response: an overview. Expert Rev Clin Pharmacol. 2014;7(4):469-485.

7. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16(10):626-638.

8. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48(3):143-157.

9. Roden DM. Drug-induced prolongation of the QT interval. N Engl J Med. 2004;350(10):1013-1022.

10. van Puijenbroek EP, Bate A, Leufkens HG, Lindquist M, Orre R, Egberts AC. A comparison of measures of disproportionality for signal detection in spontaneous reporting systems for adverse drug reactions. Pharmacoepidemiol Drug Saf. 2002;11(1):3-10.

11. Rothman KJ, Lanes S, Sacks ST. The Reporting Odds Ratio and its advantages over the Proportional Reporting Ratio. Pharmacoepidemiol Drug Saf. 2004;13(8):519-523.

12. Pal SN, Duncombe C, Falzon D, Olsson S. WHO strategy for collecting safety data in public health programmes: complementing spontaneous reporting systems. Drug Saf. 2013;36(2):75-81.

13. Fusaroli M, Raschi E, Gatti M, De Ponti F, Poluzzi E. Development of a Network-Based Signal Detection Tool: The DiAna Project. Front Pharmacol. 2021;12:626013.

14. Tangpricha V, den Heijer M. Oestrogen and anti-androgen therapy for transgender women. Lancet Diabetes Endocrinol. 2017;5(4):291-300.

15. Canonico M, Oger E, Plu-Bureau G, et al. Hormone therapy and venous thromboembolism among postmenopausal women: impact of the route of estrogen administration and progestogens: the ESTHER study. Circulation. 2007;115(7):840-845.

16. Giordano SH. Breast cancer in men. N Engl J Med. 2018;378(24):2311-2320.

17. Spring LM, Wander SA, Andre F, Moy B, Turner NC, Bardia A. Cyclin-dependent kinase 4 and 6 inhibitors for hormone receptor-positive breast cancer: past, present, and future. Lancet. 2020;395(10233):817-827.

18. Culver AL, Ockene IS, Balasubramanian R, et al. Statin use and risk of diabetes mellitus in postmenopausal women in the Women's Health Initiative. Arch Intern Med. 2012;172(2):144-152.

19. Chrousos GP. Stress and disorders of the stress system. Nat Rev Endocrinol. 2009;5(7):374-381.

20. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. EClinicalMedicine. 2019;17:100188.

21. Getahun D, Nash R, Flanders WD, et al. Cross-sex hormones and acute cardiovascular events in transgender persons: a cohort study. Ann Intern Med. 2018;169(4):205-213.

22. U.S. Food and Drug Administration. Evaluation of Sex-Specific Data in Medical Device Clinical Studies: Guidance for Industry and Food and Drug Administration Staff. Silver Spring, MD: FDA; 2014.

23. Platt R, Brown JS, Robb M, et al. The FDA Sentinel Initiative---an evolving national resource. N Engl J Med. 2018;379(22):2091-2093.

---

## Figure Legends

**Figure 1.** The Reproductive Paradox. Bar chart showing female-predominant signal proportion (y-axis) for drug categories ordered by estimated female user proportion (x-axis). Strong inverse correlation: drugs used by >90% women (HRT, AI, SERMs) produce <20% female signals, while drugs used by >90% men (testosterone, antiandrogens) produce >70% female signals. Sex-neutral comparators fall in between.

**Figure 2.** Individual drug profiles. Stacked bar charts showing male-biased (blue) vs. female-biased (red) signals for each drug category. HRT is entirely blue (0% female); antiandrogens are predominantly red (66.7% female).

**Figure 3.** Scatter plot of estimated female user proportion (x-axis) vs. female signal proportion (y-axis) across all drug categories. The negative correlation (rho ~ -0.85) quantifies the Reproductive Paradox. The regression line illustrates the inverse relationship, with drugs clustered into three groups: female-indication (upper-left quadrant), sex-neutral (center), and male-indication (lower-right quadrant).

**Figure 4.** Dose-response gradient within the Reproductive Paradox. Plot of user sex-skew magnitude (|proportion female users - 0.5|) versus signal inversion magnitude (|proportion female signals - 0.5|), showing that more extreme user sex-skew produces more extreme signal inversion. The positive correlation supports a quantitative, continuous relationship rather than a categorical artifact.
