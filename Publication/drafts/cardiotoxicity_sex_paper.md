# Sex-Differential Patterns in Drug-Induced Cardiotoxicity: A Comprehensive Analysis of 3,792 Signals From 14.5 Million FAERS Reports

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Drug-induced cardiotoxicity is a leading cause of drug withdrawal and black box warnings, yet sex-specific patterns across drug classes and cardiac event types remain poorly characterized at population scale. Foundational work by Makkar et al. (1993) established that women constitute the majority of Torsades de Pointes (TdP) cases, and subsequent electrophysiological research has confirmed sex differences in cardiac repolarization, but comprehensive pharmacovigilance-scale mapping of sex-differential cardiotoxicity across drug mechanisms has not been performed.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we identified 3,792 sex-differential cardiotoxicity signals across 411 drugs. Cardiac adverse events were classified using 35 MedDRA preferred terms organized into 10 functional categories. Sex-differential signals were defined using sex-stratified reporting odds ratios (ROR) with a log-ratio threshold (|logR| >= 0.5, >= 10 reports per sex). Signals were stratified by drug class (8 major classes), cardiac adverse event type (10 categories), severity, and molecular target. Anti-regression and reporter bias analyses were performed.

**Results.** Overall cardiac AE reporting was 53.6% female (vs. 58.3%F for non-cardiac AEs; p = 1.03 x 10^-35), indicating relative male enrichment. Drug class analysis revealed a 19.9 percentage-point spectrum: anthracyclines showed the strongest female cardiac bias (67.5%F, mean |logR| = 1.177) while TKIs showed the strongest male bias (47.6%F). Within cardiac AE types, tachycardia (60.7%F) and QT prolongation (61.6%F) showed female predominance, while atrial fibrillation (51.5%F) and bradycardia (52.5%F) approached parity. The anthracycline-TKI divergence (19.9 pp) suggests mechanism-dependent sex effects: oxidative stress pathways (anthracyclines) produce female-biased cardiotoxicity while kinase inhibition pathways (TKIs) produce male-biased patterns. Among individual drugs, trastuzumab showed the strongest female cardiac bias (85.9%F), while lopinavir/ritonavir showed the strongest male bias (23.0%F). QT prolongation showed consistent female predominance (62.1%F, 165 signals), with extreme female bias for brexpiprazole (91.3%F), levothyroxine (90.9%F), and topiramate (87.2%F).

**Interpretation.** Drug-induced cardiotoxicity exhibits a structured sex-differential landscape determined by both drug mechanism and cardiac event type. The anthracycline-TKI divergence demonstrates that cardiotoxicity pathways are not uniformly sex-biased. QT prolongation is robustly female-biased, consistent with women's longer baseline QTc intervals. These findings support sex-stratified cardiac safety monitoring in clinical practice and drug development.

**Keywords:** cardiotoxicity, sex differences, pharmacovigilance, FAERS, QT prolongation, anthracyclines, tyrosine kinase inhibitors, Torsades de Pointes, reporting odds ratio, adverse drug reactions

---

## 1. Introduction

### 1.1 Drug-Induced Cardiotoxicity as a Regulatory and Clinical Problem

Drug-induced cardiotoxicity remains a critical challenge in pharmacovigilance, accounting for approximately 45% of post-market drug withdrawals in the United States [1]. Cardiovascular adverse events---including heart failure, QT prolongation, arrhythmias, myocardial infarction, and hypertension---affect therapeutic decision-making across oncology, psychiatry, metabolic disease, and infectious disease. The withdrawal of cisapride, terfenadine, and rofecoxib due to cardiovascular toxicity illustrates the scale of this problem: billions of dollars in development costs lost and millions of patients exposed to unrecognized cardiac risk before signals emerged in post-marketing surveillance [1,2]. The regulatory response has been substantial---the ICH E14 guideline mandating thorough QT studies for all new molecular entities was a direct consequence of drug-induced arrhythmia withdrawals---yet cardiovascular toxicity continues to account for the largest fraction of safety-related drug attrition [3].

The scope of drug-induced cardiotoxicity extends far beyond the traditionally recognized high-risk classes. While anthracycline cardiomyopathy and antiarrhythmic proarrhythmia have been studied for decades, the expanding landscape of targeted cancer therapies, immunotherapies, and psychiatric medications has introduced novel mechanisms of cardiac injury that are incompletely characterized [4,5]. Immune checkpoint inhibitor myocarditis, tyrosine kinase inhibitor hypertension, and proteasome inhibitor cardiomyopathy represent mechanistically distinct forms of cardiotoxicity that may have different sex-differential profiles. A comprehensive mapping of sex differences across these diverse mechanisms has not been performed.

### 1.2 Sex Differences in Cardiac Electrophysiology

Sex differences in cardiac physiology are well-established and provide a biological foundation for sex-differential cardiotoxicity. The seminal study by Makkar et al. (1993) analyzed 332 cases of drug-induced TdP and found that women constituted approximately 70% of cases, establishing for the first time at population scale that drug-induced arrhythmia risk is fundamentally sex-dimorphic [6]. This observation has been replicated in multiple subsequent analyses and remains one of the most robust sex differences in all of clinical pharmacology.

The electrophysiological basis for this female TdP susceptibility is now well understood. Women have longer baseline QTc intervals (approximately 10--20 ms longer than age-matched men), reflecting sex differences in cardiac repolarization reserve [7,8]. This difference emerges at puberty and persists through the lifespan, implicating gonadal hormones as primary mediators. Roden (2004) provided a comprehensive mechanistic framework for drug-induced QT prolongation, emphasizing that the human ether-a-go-go-related gene (hERG) potassium channel (KCNH2/Kv11.1) is the primary molecular target for drug-induced repolarization delay, and that sex differences in hERG expression and regulation contribute to the female QT vulnerability [3]. Specifically, testosterone enhances the repolarizing IKr current, providing men with greater repolarization reserve to buffer the effects of hERG-blocking drugs, while estrogen has the opposite effect, reducing IKr and narrowing the safety margin in women.

Beyond the QTc interval, women have smaller cardiac chambers, lower cardiac output, higher resting heart rates, and different autonomic regulation compared to men [7,8]. Estrogen modulates L-type calcium channel (ICaL) function and potassium channel expression, directly affecting repolarization and arrhythmia susceptibility [3,9]. These physiological differences predict that drug-induced cardiac toxicity should manifest differently between sexes---not only for QT-related events but across the entire spectrum of cardiac adverse events.

### 1.3 Torsades de Pointes: The Paradigmatic Sex-Differential Cardiac Event

TdP represents the most dangerous manifestation of drug-induced QT prolongation and carries a mortality rate of 10--17% even with appropriate treatment [3,6]. The female predominance in TdP first documented by Makkar et al. has been confirmed in multiple settings: analysis of the FDA Adverse Event Reporting System, European pharmacovigilance databases, and hospital-based surveillance all demonstrate a 2:1 to 3:1 female-to-male ratio for drug-induced TdP [6,10]. This sex difference is not explained by differential drug exposure alone; even after adjusting for prescribing patterns, women maintain a higher risk per unit exposure for most QT-prolonging drugs.

The clinical consequences of this sex difference are substantial. More than 50 drugs on the international market carry QT prolongation warnings, and several therapeutic classes---including antipsychotics, antibiotics (fluoroquinolones, macrolides), antiemetics (ondansetron, domperidone), and antiarrhythmics---contain multiple agents with QT liability [3]. For women taking these medications, the cumulative QT-prolongation burden is higher, and the threshold for clinically significant arrhythmia is lower. Despite this, sex-stratified QT monitoring is not consistently implemented in clinical practice, and thorough QT study designs do not always include adequate power for sex-stratified analysis.

### 1.4 Sex Differences in Non-QT Cardiotoxicity

While QT prolongation represents the best-characterized sex difference in drug-induced cardiotoxicity, evidence is accumulating for sex-differential patterns in other forms of cardiac injury. In oncology, anthracycline-induced cardiomyopathy---the classic type I cardiotoxicity---shows complex sex-differential patterns. Some studies suggest greater female vulnerability to anthracycline heart failure, potentially mediated by sex differences in oxidative stress handling and mitochondrial function [11,12]. Mosca et al. (2011) provided a landmark review of sex differences in cardiovascular disease more broadly, emphasizing that the historical underrepresentation of women in cardiovascular trials has led to a systematic knowledge gap regarding sex-specific cardiovascular risk, including drug-induced risk [13].

Cardiovascular sex differences extend to drug metabolism. Women have lower expression of several cytochrome P450 enzymes relevant to cardiovascular drug metabolism, including CYP3A4 (which metabolizes many hERG-blocking drugs) and CYP2D6 [14,15]. Women also have lower glomerular filtration rates and different body composition (higher fat-to-lean ratio), affecting the pharmacokinetics of renally cleared and lipophilic cardiac drugs. Zucker and Prendergast (2020) demonstrated that these pharmacokinetic sex differences predict a substantial fraction of the sex disparity in adverse drug reactions overall, including cardiovascular events [15].

### 1.5 Knowledge Gap and Study Rationale

Despite these biological predictions, systematic characterization of sex-differential cardiotoxicity across drug classes and cardiac event types has been limited. Individual studies have documented QT prolongation risks in women [3,6], anthracycline cardiotoxicity differences [11], and immune checkpoint inhibitor myocarditis sex patterns [5], but no comprehensive mapping across the cardiovascular pharmacovigilance landscape has been reported. The existing literature is fragmented by drug class, cardiac event type, and study design, preventing a unified understanding of how sex modifies drug-induced cardiac risk across mechanisms.

We leveraged SexDiffKG---a knowledge graph integrating 14.5 million FAERS reports with molecular target data from ChEMBL 36---to systematically characterize sex-differential cardiotoxicity across drug classes, cardiac event types, and molecular mechanisms. This study addresses three specific questions: (1) Does the magnitude and direction of sex-differential cardiotoxicity vary by drug mechanism? (2) Is the female predominance in QT prolongation consistent across therapeutic classes? (3) Does cardiac AE severity modify the sex-differential pattern?

---

## 2. Methods

### 2.1 Data Source and Report Processing

The FDA Adverse Event Reporting System (FAERS) was used as the primary data source. FAERS is a spontaneous reporting database that captures post-marketing safety reports submitted by healthcare professionals, consumers, and manufacturers to the US Food and Drug Administration. We analyzed quarterly data files from 2004Q1 through 2025Q3, encompassing 86 quarterly data releases.

Report-level deduplication was performed using a validated algorithm based on exact matching of case identifiers, with subsequent fuzzy matching on patient demographics (age, sex, country) and reporter type to eliminate redundant case reports. After deduplication, the analysis dataset comprised 14,536,008 unique adverse event reports. Sex distribution was 8,744,397 female reports (60.2%) and 5,791,611 male reports (39.8%). Reports with missing or ambiguous sex designation were excluded.

Drug name standardization was performed using the Drug Information Association (DiAna) dictionary, mapping reported drug names to active ingredients and resolving brand name variants, misspellings, and combination product nomenclature. This standardization yielded 3,247 unique drug entities for analysis.

### 2.2 Sex-Stratified Reporting Odds Ratio (ROR)

For each drug-adverse event (drug-AE) pair, sex-stratified reporting odds ratios (ROR) were computed separately for female and male report populations. The ROR is a standard disproportionality measure in pharmacovigilance, analogous to the odds ratio in case-control studies, and is defined as:

**ROR_female = (a_f / b_f) / (c_f / d_f)**

where, within the female report population:
- a_f = reports of the drug with the AE of interest
- b_f = reports of the drug without the AE of interest
- c_f = reports of other drugs with the AE of interest
- d_f = reports of other drugs without the AE of interest

An analogous computation was performed for **ROR_male** within the male report population.

The sex-differential measure was defined as the natural logarithm of the ROR ratio:

**logR = ln(ROR_female / ROR_male)**

A positive logR indicates female-biased disproportionality (the drug-AE association is stronger in women), while a negative logR indicates male-biased disproportionality. This measure is symmetric around zero and additive on the log scale, enabling comparison across drug-AE pairs with different baseline reporting rates.

Sex-differential signals were defined using two thresholds applied simultaneously:
- **Effect size threshold:** |logR| >= 0.5 (corresponding to an ROR ratio of >= 1.65 or <= 0.61)
- **Minimum count threshold:** >= 10 reports per sex for the drug-AE pair

These thresholds were selected to balance signal detection sensitivity against false positive control. The |logR| >= 0.5 threshold is more conservative than the commonly used |logR| >= 0.2 (minimal relevant difference) and more permissive than |logR| >= 1.0 (strong signal). Sensitivity analyses at |logR| >= 0.3 and |logR| >= 0.7 were performed to assess robustness.

### 2.3 Female Fraction Computation

For descriptive reporting, sex-differential patterns were summarized using the female fraction (%F), defined as:

**%F = (N_female_reports / (N_female_reports + N_male_reports)) x 100**

This metric was computed at the signal level (per drug-AE pair), at the drug level (aggregating across cardiac AE types), and at the drug class level (aggregating across drugs within a class). The female fraction provides an intuitive interpretation: values above 50% indicate female predominance, while values below 50% indicate male predominance. The overall FAERS female reporting fraction of 60.2% serves as the population-level baseline; cardiac AE female fractions below this value indicate relative male enrichment compared to the general reporting population.

### 2.4 Cardiac Adverse Event Identification and Classification

Cardiac adverse events were identified using 35 MedDRA preferred terms (PTs) selected based on the MedDRA Standardised MedDRA Queries (SMQs) for cardiac-related adverse events, supplemented by expert clinical review to ensure comprehensive coverage. The selected PTs were organized into 10 functional categories based on pathophysiological mechanism:

1. **QT prolongation / repolarization:** Electrocardiogram QT prolonged, Long QT syndrome, Torsade de pointes
2. **Heart failure:** Cardiac failure, Cardiac failure acute, Cardiac failure chronic, Cardiac failure congestive, Left ventricular dysfunction, Ejection fraction decreased
3. **Myocardial infarction / ischemia:** Myocardial infarction, Acute myocardial infarction, Myocardial ischaemia, ST segment elevation myocardial infarction (STEMI), Non-ST segment elevation myocardial infarction (NSTEMI)
4. **Cardiomyopathy:** Cardiomyopathy, Dilated cardiomyopathy, Hypertrophic cardiomyopathy, Drug-related cardiomyopathy, Stress cardiomyopathy (takotsubo)
5. **Arrhythmia (supraventricular):** Atrial fibrillation, Atrial flutter, Supraventricular tachycardia
6. **Arrhythmia (ventricular):** Ventricular tachycardia, Ventricular fibrillation
7. **Rate disturbance:** Tachycardia, Bradycardia, Heart rate increased, Palpitations, Sinus tachycardia
8. **Cardiac arrest:** Cardiac arrest, Cardio-respiratory arrest
9. **Pericardial events:** Pericarditis, Pericardial effusion, Cardiac tamponade
10. **General cardiac disorder:** Cardiac disorder, Cardiomegaly, Myocarditis

This classification framework ensures that signals are analyzed both at the individual PT level and at the functional category level, enabling identification of patterns that may not be apparent from individual-term analysis alone.

### 2.5 Drug Classification

Eight major drug classes with known cardiotoxicity profiles were selected for mechanism-stratified analysis:

- **Anthracyclines** (n=2): doxorubicin, epirubicin. Mechanism: oxidative stress via reactive oxygen species generation and topoisomerase IIbeta (Top2B) inhibition in cardiomyocytes, leading to irreversible cardiomyocyte death (Type I cardiotoxicity).
- **Tyrosine kinase inhibitors (TKIs)** (n=6): sunitinib, sorafenib, imatinib, dasatinib, pazopanib, ponatinib. Mechanism: off-target inhibition of cardioprotective kinase pathways (VEGFR, PDGFR, ABL, c-Kit), leading to cardiomyocyte dysfunction and impaired angiogenesis (Type II cardiotoxicity with additional vascular effects).
- **Immune checkpoint inhibitors (ICIs)** (n=4): nivolumab, pembrolizumab, ipilimumab, atezolizumab. Mechanism: immune-mediated myocarditis via T-cell infiltration of cardiac tissue following disruption of peripheral tolerance.
- **Antiarrhythmics** (n=5): amiodarone, flecainide, sotalol, propafenone, dronedarone. Mechanism: direct modulation of cardiac ion channels (sodium, potassium, calcium), with proarrhythmic potential through excessive conduction slowing or repolarization prolongation.
- **Selective serotonin reuptake inhibitors (SSRIs)** (n=5): sertraline, citalopram, escitalopram, fluoxetine, paroxetine. Mechanism: serotonergic effects on cardiac 5-HT receptors, hERG potassium channel blockade (particularly citalopram/escitalopram), and QT prolongation.
- **Fluoropyrimidines** (n=2): 5-fluorouracil, capecitabine. Mechanism: coronary vasospasm via endothelin-1 upregulation and nitric oxide depletion, leading to myocardial ischemia.
- **Anti-TNF agents** (n=3): infliximab, adalimumab, etanercept. Mechanism: modulation of TNF-alpha signaling in cardiac tissue, with paradoxical worsening of heart failure in patients with pre-existing ventricular dysfunction.
- **Antipsychotics** (n=5): haloperidol, olanzapine, risperidone, quetiapine, clozapine. Mechanism: multiple pathways including hERG blockade (QT prolongation), metabolic syndrome induction (weight gain, dyslipidemia, insulin resistance), autonomic dysregulation, and direct myocardial effects.

### 2.6 Statistical Analysis

Female fraction (%F) was computed per drug-AE pair and aggregated by drug class using the arithmetic mean. Between-class differences in female fraction were assessed via the Kruskal-Wallis test (nonparametric one-way ANOVA), with post-hoc pairwise comparisons using the Dunn test with Bonferroni correction. Within-class heterogeneity was quantified by the range and standard deviation of female fraction across signals within each class.

Anti-regression analysis was performed to assess whether sex-differential signals were robust to reporting volume. Signals were stratified into quintiles of total report count (N_female + N_male), and Spearman rank correlation between report volume quintile and |logR| was computed. A significant negative correlation would indicate that signals attenuate with increasing evidence (suggesting instability), while null or positive correlation indicates robustness.

Comparison of cardiac vs. non-cardiac AE female fractions was assessed using a chi-squared test with Yates' continuity correction. Severity-stratified analysis compared serious vs. non-serious cardiac signals using the Mann-Whitney U test. All statistical analyses were performed using Python 3.11 with SciPy 1.11 and statsmodels 0.14. Effect sizes were reported as mean absolute log-ratio |logR|, which quantifies the magnitude of sex-differential disproportionality regardless of direction.

### 2.7 Sensitivity and Bias Analyses

Three sensitivity analyses were conducted: (1) varying the |logR| threshold from 0.3 to 0.7 to assess threshold dependence, (2) restricting to reports from healthcare professionals (excluding consumer reports) to assess reporter bias, and (3) stratifying by 5-year time periods (2004--2008, 2009--2013, 2014--2018, 2019--2025) to assess temporal stability of sex-differential patterns.

Reporter bias was assessed by comparing the female fraction across reporter types (physician, pharmacist, consumer, other). A significant interaction between reporter type and sex-differential signal direction would suggest that reporting behavior, rather than biological susceptibility, drives the observed sex differences.

---

## 3. Results

### 3.1 Overview

A total of 3,792 sex-differential cardiotoxicity signals were identified across 411 drugs. Overall cardiac AEs were 53.6% female, significantly lower than non-cardiac AEs at 58.3% female (p = 1.03 x 10^-35), indicating relative male enrichment in cardiac drug toxicity. This 4.7 percentage-point gap between cardiac and non-cardiac AEs is highly significant given the large sample size and indicates that the male cardiovascular disease burden partially offsets the general female overrepresentation in FAERS reporting.

Of the 3,792 signals, 2,184 (57.6%) were female-biased (logR > 0.5) and 1,608 (42.4%) were male-biased (logR < -0.5). The mean |logR| across all cardiac signals was 0.873, corresponding to an average ROR ratio of approximately 2.4:1 between the more-affected and less-affected sex. This indicates that when sex-differential cardiac signals exist, they are of substantial magnitude---not marginal statistical artifacts.

### 3.2 Drug Class Cardiotoxicity Spectrum

**Table 1. Sex-Differential Cardiac Signal Profiles by Drug Class**

| Drug Class | N Drugs | N Signals | Mean %F | Mean |logR| | Mechanism |
|-----------|---------|-----------|---------|-------------|-----------|
| Anthracyclines | 2 | 35 | **67.5** | 1.177 | Oxidative stress, Top2B |
| SSRIs | 5 | 50 | 59.2 | 0.809 | Serotonergic, hERG |
| Fluoropyrimidines | 2 | 28 | 57.8 | 0.907 | Coronary vasospasm |
| Anti-TNFs | 3 | 41 | 52.8 | 0.933 | Inflammatory, immune |
| Antiarrhythmics | 5 | 45 | 52.4 | 0.806 | Ion channel modulation |
| Antipsychotics | 5 | 93 | 50.0 | 1.027 | Metabolic, hERG, autonomic |
| ICIs | 4 | 49 | 48.9 | 0.882 | Immune-mediated myocarditis |
| TKIs | 6 | 33 | **47.6** | 0.825 | Kinase inhibition |

The spectrum spans 19.9 percentage points from TKIs (47.6%F, male-biased) to anthracyclines (67.5%F, female-biased). Kruskal-Wallis test confirmed significant between-class heterogeneity (p < 0.001).

The drug class spectrum reveals a clear ordering by mechanism. Classes that produce cardiotoxicity through oxidative stress or serotonergic pathways (anthracyclines, SSRIs) show female predominance, consistent with sex differences in oxidative stress handling and serotonergic receptor expression. Classes that produce cardiotoxicity through structural/vascular mechanisms (TKIs, ICIs) show male predominance or near-parity, consistent with the higher male burden of hypertension, atherosclerotic disease, and cardiac remodeling. Classes with mixed mechanisms (antipsychotics, antiarrhythmics) show intermediate female fractions, reflecting the offsetting contributions of female-biased QT effects and male-biased metabolic/structural effects.

### 3.3 The Anthracycline-TKI Divergence

The most striking finding is the mechanistic divergence between anthracyclines (67.5%F) and TKIs (47.6%F)---the two major classes of oncology-associated cardiotoxicity:

**Anthracyclines (67.5%F):** Doxorubicin and epirubicin produce cardiotoxicity primarily through reactive oxygen species (ROS) generation and topoisomerase IIbeta (Top2B) inhibition in cardiomyocytes. Estrogen modulates oxidative stress responses through upregulation of antioxidant enzymes (SOD, catalase) and mitochondrial protection [9]. Paradoxically, the protective effect of estrogen in normal cardiac physiology may increase susceptibility to anthracycline-specific oxidative damage through altered mitochondrial handling of doxorubicin-iron complexes. The mean |logR| of 1.177 (the highest of any class) indicates not just more frequent female signals but stronger effect sizes.

The anthracycline female bias has clinical context beyond the pharmacovigilance signal. Anthracyclines are the cornerstone of breast cancer chemotherapy, a disease that is overwhelmingly female. However, the sex-stratified ROR methodology accounts for differential prescribing: the signal reflects that, among women exposed to anthracyclines, the cardiac toxicity reporting rate is disproportionately elevated relative to women's overall reporting rate for non-cardiac events. This finding is consistent with preclinical data showing that female cardiomyocytes exhibit greater susceptibility to doxorubicin-induced apoptosis in vitro, mediated through estrogen receptor beta signaling in mitochondria [11,12].

**TKIs (47.6%F):** Tyrosine kinase inhibitors produce cardiotoxicity through off-target kinase inhibition (VEGFR, PDGFR, c-Kit) affecting cardiomyocyte survival, angiogenesis, and myocardial repair. Male predominance in TKI cardiotoxicity may reflect sex-differential expression of kinase targets in cardiac tissue and testosterone-mediated effects on VEGFR signaling [16]. The male bias in TKI cardiotoxicity is consistent with higher male rates of hypertension and cardiac remodeling. Additionally, several TKIs (sunitinib, sorafenib) produce cardiotoxicity partly through hypertension, a condition with higher male prevalence and severity, which may amplify the male-biased signal.

This divergence has direct clinical implications: a female patient receiving anthracycline-based chemotherapy faces different cardiac risk dynamics than a female patient receiving TKI therapy. Class-specific rather than class-agnostic sex-adjusted monitoring is warranted.

### 3.4 Cardiac AE Type Analysis

**Table 2. Sex-Differential Profiles by Cardiac AE Type**

| Cardiac AE | N Drugs | Mean %F | Mean |logR| | Sex Pattern |
|-----------|---------|---------|-------------|-------------|
| QT prolongation (ECG) | 122 | **61.6** | 0.864 | Strong female |
| Tachycardia | 172 | **60.7** | 0.868 | Strong female |
| Palpitations | 153 | **60.3** | 0.881 | Moderate female |
| Heart rate increased | 124 | 58.0 | 0.837 | Moderate female |
| Cardiac failure | 184 | 55.7 | 0.878 | Slight female |
| Cardiac disorder | 110 | 55.1 | 0.923 | Slight female |
| Myocardial infarction | 182 | 54.4 | 0.934 | Near parity |
| Cardiac arrest | 210 | 54.5 | 0.829 | Near parity |
| Bradycardia | 152 | 52.5 | 0.875 | Near parity |
| Atrial fibrillation | 180 | **51.5** | 0.855 | Near parity |

The cardiac AE spectrum reveals a clear physiological pattern that aligns with known sex differences in cardiac electrophysiology and structure:

**Rate-related events (female-biased):** Tachycardia (60.7%F), palpitations (60.3%F), and heart rate increase (58.0%F) show consistent female predominance. These events involve autonomic regulation and adrenergic sensitivity, both of which are sex-dimorphic. Women have higher resting heart rates and greater heart rate variability, potentially increasing susceptibility to rate-related drug effects. The female predominance in drug-induced tachycardia is consistent with epidemiological data showing that inappropriate sinus tachycardia and postural orthostatic tachycardia syndrome (POTS) are both strongly female-predominant conditions [7,8].

**Repolarization events (female-biased):** QT prolongation (61.6%F) is robustly female-biased, consistent with women's longer baseline QTc intervals and greater sensitivity to hERG channel-blocking drugs [3,6]. The 61.6% female proportion across 122 drugs represents a pharmacovigilance-scale confirmation of the ICH E14 recommendation for sex-stratified QT analysis. This finding validates and extends the observation of Makkar et al. (1993) from hospital-based TdP case series to the entire FAERS reporting population across more than a hundred drugs.

**Structural events (near-parity):** Myocardial infarction (54.4%F), cardiac arrest (54.5%F), and atrial fibrillation (51.5%F) approach sex parity. These events involve structural cardiac pathology where sex differences in underlying disease (higher male MI rates, higher male AFib prevalence) partially offset sex-differential drug susceptibility. The near-parity finding for atrial fibrillation is particularly notable, as this arrhythmia has a well-documented 1.5:1 male predominance in the general population [13]; the fact that drug-induced AFib signals reach 51.5%F (slight female excess relative to the background AFib sex ratio) suggests that drugs may preferentially trigger AFib in women relative to their lower baseline risk.

**Heart failure (moderate female bias):** Cardiac failure at 55.7%F occupies an intermediate position. This reflects the convergence of female-biased mechanisms (anthracycline cardiotoxicity, takotsubo cardiomyopathy) and male-biased mechanisms (TKI cardiotoxicity, ischemic cardiomyopathy). The moderate female bias in drug-induced heart failure contrasts with the general population, where heart failure with preserved ejection fraction (HFpEF) is female-predominant while heart failure with reduced ejection fraction (HFrEF) is male-predominant [8].

### 3.5 QT Prolongation Deep Dive

Among 165 QT prolongation signals (combining "Electrocardiogram QT prolonged" and "Torsade de pointes"), the overall female proportion was 62.1%. Individual drug profiles revealed extreme heterogeneity:

**Top Female-Biased QT Drugs:**
- Brexpiprazole: 91.3%F (atypical antipsychotic)
- Levothyroxine: 90.9%F (thyroid hormone)
- Topiramate: 87.2%F (antiepileptic)
- Naproxen: 86.4%F (NSAID)
- Paracetamol: 86.1%F (analgesic)

The extreme female QT bias for brexpiprazole (91.3%F) is clinically significant: this drug is increasingly prescribed for major depressive disorder, which affects women at twice the rate of men. The combination of female-predominant prescribing and female-biased QT toxicity creates a compounded risk that warrants enhanced ECG monitoring in female patients. Brexpiprazole is a partial agonist at dopamine D2 and serotonin 5-HT1A receptors with antagonist activity at 5-HT2A receptors; its QT liability likely arises from hERG channel interaction at therapeutic concentrations, and the near-exclusive female QT signal suggests that the drug's QT effect operates near the threshold where female repolarization reserve is insufficient but male reserve remains adequate.

Levothyroxine QT prolongation (90.9%F) likely reflects thyrotoxicosis-related QT effects, with women being 5--8 times more likely to have thyroid disorders. However, the sex-stratified ROR controls for this baseline: the signal indicates that even accounting for the higher female levothyroxine use, female QT susceptibility is disproportionately elevated. This is consistent with the known interaction between thyroid hormones and cardiac ion channel expression: thyroid hormone excess increases ICaL current density and decreases IKr, exacerbating the repolarization vulnerability that is already greater in women [3].

The finding that paracetamol (86.1%F) and naproxen (86.4%F) produce female-biased QT signals is unexpected and has not been previously reported. Both drugs are available over-the-counter and are among the most widely used medications globally. While neither drug is considered a primary QT-prolonging agent, their potential for QT effects at supratherapeutic doses or in the context of polypharmacy warrants further investigation, particularly in female patients.

### 3.6 Drug-Specific Cardiotoxicity Profiles

#### 3.6.1 Most Female-Biased Cardiotoxic Drugs

**Table 3. Most Female-Biased Cardiotoxic Drugs**

| Drug | %F | N Reports | Drug Class | Key Cardiac AEs |
|------|-----|-----------|-----------|-----------------|
| Trastuzumab | 85.9 | 2,922 | Anti-HER2 | Heart failure, LVEF decrease |
| Alendronic acid | 78.8 | 1,679 | Bisphosphonate | Atrial fibrillation |
| Methylprednisolone | 78.3 | 363 | Corticosteroid | Arrhythmia, cardiac arrest |
| Riociguat | 78.2 | 598 | sGC stimulator | Hypotension, syncope |
| Codeine | 76.9 | 294 | Opioid | QT prolongation, bradycardia |

**Trastuzumab (85.9%F, n=2,922).** Trastuzumab's extreme female cardiac bias reflects the Reproductive Paradox: used almost exclusively for female breast cancer, the rare male patients show disproportionately lower cardiac events after sex-stratification. This is consistent with estrogen's complex role in HER2-mediated cardiac signaling. HER2 (ErbB2) is expressed in adult cardiomyocytes where it plays a protective role through neuregulin-1 signaling; trastuzumab-mediated HER2 inhibition disrupts this cardioprotective pathway. The sex difference may reflect higher myocardial HER2 expression in women or estrogen-dependent amplification of neuregulin-HER2 signaling that, when blocked, produces greater cardiac dysfunction. The large report count (2,922) provides high confidence in this signal.

**Alendronic acid (78.8%F, n=1,679).** The bisphosphonate-atrial fibrillation link has been debated since the 2007 finding from the Women's Health Initiative. Our data confirm a strong female bias in bisphosphonate-associated cardiac events, consistent with the fact that osteoporosis (the primary indication) is 4:1 female-predominant. The cardiac mechanism may involve calcium homeostasis disruption or inflammatory activation of atrial substrate.

**Codeine (76.9%F, n=294).** Codeine's female-biased cardiotoxicity likely reflects CYP2D6-mediated bioactivation to morphine, which has QT-prolonging effects. Women have been reported to have altered CYP2D6 activity profiles, and the female-biased codeine signal may identify a pharmacogenomic-sex interaction worthy of further investigation.

#### 3.6.2 Most Male-Biased Cardiotoxic Drugs

**Table 4. Most Male-Biased Cardiotoxic Drugs**

| Drug | %F | N Reports | Drug Class | Key Cardiac AEs |
|------|-----|-----------|-----------|-----------------|
| Lopinavir/ritonavir | 23.0 | 250 | Antiviral (HIV) | QT prolongation, MI |
| Tafamidis | 24.6 | 597 | TTR stabilizer | Cardiac failure |
| Ixekizumab | 26.3 | 185 | Anti-IL-17 | MI, cardiac failure |
| Allopurinol | 28.0 | 1,180 | Xanthine oxidase inhibitor | Cardiac arrest, MI |
| Icodextrin combination | 30.2 | 263 | Peritoneal dialysis | Cardiac failure |

**Lopinavir/ritonavir (23.0%F, n=250).** The extreme male bias reflects the HIV treatment population demographics (approximately 75% male globally) combined with the cardiovascular comorbidity burden of HIV. Ritonavir is a potent CYP3A4 inhibitor that can elevate plasma levels of co-administered drugs with QT liability. The male cardiac bias is consistent with the higher cardiovascular disease burden in HIV-positive men and the interaction between antiretroviral metabolic toxicity (dyslipidemia, insulin resistance) and male-pattern cardiovascular risk.

**Tafamidis (24.6%F, n=597).** Tafamidis's male bias is expected: transthyretin cardiac amyloidosis (ATTR-CM) predominantly affects older men. Wild-type ATTR-CM has an estimated 25:1 to 50:1 male predominance in diagnosed cases, making this one of the most sex-skewed cardiovascular conditions [17]. The 24.6%F signal likely represents the small proportion of hereditary ATTR (which has a less extreme sex ratio) combined with increasing female diagnosis as awareness grows.

**Allopurinol (28.0%F, n=1,180).** Allopurinol's male cardiac bias aligns with gout's 3:1 male predominance and the cardiovascular comorbidity burden in gout patients. Hyperuricemia is an independent cardiovascular risk factor, and the co-occurrence of gout with metabolic syndrome, hypertension, and chronic kidney disease creates a high-risk male population. The large report count (1,180) provides strong statistical support for this signal.

### 3.7 Severity Gradient in Cardiac AEs

Serious cardiac AEs showed greater male enrichment than non-serious:
- Serious cardiac AEs: 51.3%F (n = 1,892)
- Non-serious cardiac AEs: 55.8%F (n = 1,900)
- Difference: 4.5 pp (p < 0.001)

This aligns with the broader severity-sex gradient: the most severe drug outcomes are less female-biased, with fatal cardiac events approaching or crossing parity. The severity gradient has multiple potential explanations: (1) men may have more severe underlying cardiovascular disease at the time of drug exposure, predisposing to more severe drug-induced events; (2) reporting behavior may differ---men may be less likely to report non-severe cardiac symptoms, inflating female representation in the non-serious stratum; (3) biological sex differences in cardiac reserve and compensatory mechanisms may allow women to tolerate subclinical cardiotoxicity that progresses to severe events more frequently in men.

### 3.8 Anti-Regression and Temporal Stability

Anti-regression analysis showed no significant correlation between report volume quintile and |logR| (Spearman rho = -0.03, p = 0.41), indicating that sex-differential cardiac signals are not attenuated by increasing evidence and are therefore robust rather than artifactual.

Temporal analysis across four time periods showed stable sex-differential patterns for QT prolongation (%F range: 60.3--63.1% across periods) and anthracycline cardiotoxicity (%F range: 65.8--69.2%). The TKI male bias showed slight attenuation over time (from 45.2%F in 2004--2008 to 49.1%F in 2019--2025), potentially reflecting the evolving TKI landscape with newer agents having different selectivity profiles.

---

## 4. Discussion

### 4.1 Mechanism-Dependent Sex-Differential Cardiotoxicity

The central finding---the anthracycline-TKI divergence of 19.9 pp---establishes that drug-induced cardiotoxicity is not uniformly sex-biased but depends on the molecular mechanism of cardiac injury. This has three implications:

First, sex-stratified cardiac monitoring protocols should be mechanism-specific. Anthracycline-treated female patients may warrant more aggressive echocardiographic surveillance for heart failure, while TKI-treated male patients may warrant enhanced blood pressure and cardiac remodeling monitoring.

Second, preclinical cardiac safety assessment should include sex as a biological variable in mechanism-relevant assays. In vitro hERG channel studies (QT risk) should use female-derived cardiomyocytes; oxidative stress assays (anthracycline risk) should include estrogen-modulated conditions.

Third, clinical trial design for cardiotoxicity endpoints should pre-specify sex-stratified analysis. The FDA's 2022 guidance on diversity in clinical trials should be extended to mandate sex-stratified cardiac safety reporting.

The mechanism-dependent nature of the sex-differential pattern has implications for the development of cardioprotective strategies. Dexrazoxane, the only FDA-approved cardioprotectant for anthracycline therapy, chelates iron and reduces oxidative stress---the very pathway that shows the strongest female bias in our analysis. Whether dexrazoxane's cardioprotective efficacy differs by sex has not been systematically studied but is predicted by our findings. Similarly, the development of cardioprotective interventions for TKI-associated cardiotoxicity (e.g., neuregulin-1, beta-blockers, ACE inhibitors) should consider whether the male-biased risk profile implies different optimal strategies for men versus women.

### 4.2 QT Prolongation as a Validated Sex-Differential Signal

The consistent female predominance of QT prolongation (61.6%F across 122 drugs) represents the largest pharmacovigilance-scale validation of women's known QT susceptibility. The ICH E14 guideline recommends sex-stratified QT analysis in thorough QT studies, but implementation remains inconsistent [10]. Our finding that QT female bias persists across antipsychotics, antiarrhythmics, SSRIs, NSAIDs, and even analgesics demonstrates the universality of this sex difference and the clinical importance of compliance with E14 guidance.

The molecular basis for female QT vulnerability centers on the hERG potassium channel (encoded by KCNH2). Roden (2004) established the "repolarization reserve" framework, in which multiple repolarizing currents (IKr, IKs, IK1) provide redundant safety margin against excessive action potential prolongation [3]. Women have lower IKr current density than men, partly due to testosterone-mediated transcriptional upregulation of KCNH2 in males, resulting in reduced repolarization reserve. When a drug blocks hERG (even partially), the remaining repolarization reserve in women may be insufficient to prevent QT prolongation, while men retain adequate reserve. This molecular model predicts that drugs with weak hERG affinity should show minimal sex differences in QT prolongation (both sexes retain adequate reserve), while drugs with moderate hERG affinity should show the largest sex differences (women below threshold, men above). Our data are consistent with this prediction: the most extreme female QT signals (brexpiprazole 91.3%F, levothyroxine 90.9%F) are for drugs not traditionally classified as high-risk QT prolongers, suggesting that their moderate hERG effects operate precisely in the "sex-divergent" zone of repolarization reserve.

Estrogen exerts direct effects on cardiac ion channels that compound the baseline sex difference. Estrogen enhances the L-type calcium current (ICaL), which prolongs the plateau phase of the cardiac action potential, and inhibits IKr, further reducing repolarization reserve [3,9]. These effects are mediated through both genomic (estrogen receptor-mediated transcription) and non-genomic (rapid membrane signaling) pathways. The clinical relevance is demonstrated by the observation that TdP risk in women varies with the menstrual cycle, with greatest QT prolongation occurring during the luteal phase when estrogen and progesterone levels are highest [6]. Our population-level data cannot capture menstrual cycle effects, but the robust 61.6%F QT signal across 122 drugs is consistent with a persistent, hormone-mediated female vulnerability.

### 4.3 Comparison with Prior Literature

Our findings extend and contextualize several landmark observations in the sex-and-cardiotoxicity literature.

**Makkar et al. (1993)** reported that women constituted approximately 70% of drug-induced TdP cases in a review of 332 published case reports across multiple drugs [6]. Our finding of 62.1%F across 165 QT/TdP signals from 14.5 million FAERS reports provides a population-scale replication with a somewhat lower female proportion (62.1% vs. 70%). The attenuation likely reflects the broader signal definition (including QT prolongation without TdP) and the larger, less selected population (FAERS vs. published case reports, which may over-report dramatic TdP presentations in women).

**Roden (2004)** proposed the "repolarization reserve" hypothesis to explain both the female QT vulnerability and the multi-drug nature of QT prolongation risk [3]. Our data provide strong pharmacovigilance support for this model: the universality of female QT predominance across 122 drugs with diverse primary pharmacology (antipsychotics, thyroid hormones, NSAIDs, antiepileptics) is precisely what the repolarization reserve model predicts. If female QT vulnerability were drug-specific rather than host-specific, we would expect heterogeneous sex ratios across drug classes; instead, the consistent 60--65%F range confirms a host-mediated (i.e., sex-physiological) mechanism.

**Mosca et al. (2011)** identified systematic gaps in the recognition and management of cardiovascular disease in women, including underdiagnosis, undertreatment, and underrepresentation in clinical trials [13]. Our finding that cardiac AEs are 53.6%F (below the 60.2% female FAERS baseline) is consistent with Mosca's framework: relative to their representation in the reporting system, women are underrepresented in cardiac AE signals, suggesting either biological protection (men have more cardiac events per drug exposure) or systematic underrecognition of drug-induced cardiotoxicity in women. The severity gradient (serious cardiac AEs at 51.3%F vs. non-serious at 55.8%F) supports the underrecognition hypothesis: women's cardiac symptoms may be dismissed as non-serious more often than men's.

**Zucker and Prendergast (2020)** demonstrated that sex differences in pharmacokinetics (lower CYP3A4 activity, lower renal clearance, higher fat-to-lean ratio in women) predict a substantial fraction of sex-differential adverse drug reactions [15]. For cardiotoxicity specifically, pharmacokinetic sex differences amplify pharmacodynamic sex differences: women not only have greater QT sensitivity per unit drug concentration but may also achieve higher drug concentrations at equivalent doses. This "double hit" model---pharmacokinetic overexposure plus pharmacodynamic hypersensitivity---explains why the female QT predominance is so robust across drug classes.

### 4.4 The Antipsychotic Paradox

Antipsychotics showed exactly 50.0%F cardiac signals (perfect parity) despite being among the strongest QT-prolonging drug classes. This paradox resolves when examining the within-class cardiac AE profile: QT prolongation is female-biased as expected, but metabolic cardiotoxicity (weight gain, insulin resistance, atherosclerosis) is male-biased, creating an aggregate near-parity. This underscores the inadequacy of class-level sex analysis without AE-type stratification.

The antipsychotic metabolic syndrome pathway is increasingly recognized as a major driver of cardiovascular morbidity in psychiatric patients. Olanzapine and clozapine carry the highest metabolic risk among antipsychotics, producing significant weight gain, dyslipidemia, and hyperglycemia. While women may gain more weight on antipsychotics in absolute terms, the cardiovascular consequences (myocardial infarction, cardiac failure) are more frequently reported in men, potentially reflecting the higher male baseline cardiovascular risk and the synergistic interaction between antipsychotic metabolic effects and male-pattern visceral adiposity.

### 4.5 Implications for Cardiac CYP Expression and Drug Metabolism

Sex differences in hepatic drug metabolism are well-characterized [14,15], but emerging evidence suggests that local cardiac metabolism may also contribute to sex-differential cardiotoxicity. The human heart expresses several CYP enzymes, including CYP2J2, CYP2C8, and CYP1B1, which metabolize arachidonic acid to cardioprotective epoxyeicosatrienoic acids (EETs). CYP1B1 expression in cardiac tissue is estrogen-regulated and shows sex-differential activity, with implications for local drug metabolism within the myocardium.

For anthracyclines specifically, cardiac CYP-mediated metabolism of doxorubicin to its cardiotoxic metabolite doxorubicinol may differ by sex, potentially contributing to the female-biased anthracycline cardiotoxicity observed in our data. The interplay between hepatic clearance (which determines systemic drug exposure) and local cardiac metabolism (which determines intramyocardial drug activation) creates a complex sex-differential pharmacology that is not captured by standard pharmacokinetic studies measuring only plasma drug levels.

### 4.6 Regulatory and Clinical Implications

The structured sex-differential landscape of drug-induced cardiotoxicity has several regulatory implications:

**ICH E14 compliance.** Our data provide the strongest pharmacovigilance evidence to date supporting the ICH E14 recommendation for sex-stratified QT analysis. The consistent 61.6%F QT signal across 122 drugs demonstrates that sex-stratified analysis is not merely a statistical nicety but a clinical necessity. Regulatory agencies should strengthen enforcement of sex-stratified QT reporting in thorough QT studies and consider requiring sex-specific QT thresholds for regulatory decisions.

**Drug labeling.** The drug-specific sex profiles identified in this study (e.g., brexpiprazole 91.3%F for QT, trastuzumab 85.9%F for heart failure) could inform sex-specific warnings in drug labeling. Current FDA-approved labeling rarely includes sex-specific cardiac risk information; our data suggest that for drugs with extreme sex-differential signals, sex-specific guidance would be warranted.

**Clinical trial design.** The mechanism-dependent sex-differential pattern argues against a one-size-fits-all approach to cardiac safety monitoring in clinical trials. Anthracycline trials should ensure adequate female enrollment and power for sex-stratified heart failure analysis; TKI trials should similarly ensure adequate male enrollment for hypertension and cardiac remodeling endpoints.

**Clinical practice.** At the bedside, the clinical message is actionable: when prescribing hERG-blocking drugs to women, lower QT monitoring thresholds should be considered; when prescribing anthracyclines to women, enhanced echocardiographic surveillance is supported by this population-scale evidence; when prescribing TKIs to men, blood pressure and cardiac function monitoring should be heightened.

### 4.7 Limitations

1. FAERS voluntary reporting may undercount male cardiac events (men less likely to report non-fatal cardiac symptoms).
2. No drug exposure denominators available in FAERS; relative risk cannot be calculated. The sex-stratified ROR approach mitigates but does not eliminate confounding by differential prescribing.
3. Confounding by indication is inevitable: drugs used predominantly by one sex will show indication-correlated cardiac patterns. The sex-stratified ROR design controls for sex-differential baseline reporting rates but cannot fully separate drug effects from disease effects.
4. Cardiac AE terms overlap between structural and functional categories; some signals contribute to multiple AE type analyses.
5. The analysis spans 2004--2025; temporal changes in prescribing patterns and reporting behavior may affect aggregate results.
6. MedDRA coding imprecision may misclassify some cardiac events, particularly distinguishing between primary and secondary cardiac effects.
7. The FAERS population is predominantly from the United States and may not fully represent global sex-differential patterns, particularly for populations with different genetic backgrounds (e.g., CYP2D6 polymorphism frequencies).
8. Reporter bias remains a concern: women may be more likely to seek medical attention for cardiac symptoms, and healthcare providers may be more alert to cardiac effects in women for certain drug classes (e.g., anthracyclines). Our reporter-type sensitivity analysis partially addresses but does not eliminate this concern.

---

## 5. Conclusion

Drug-induced cardiotoxicity exhibits a structured sex-differential landscape shaped by drug mechanism and cardiac event type. The anthracycline-TKI divergence (19.9 pp) demonstrates mechanism-dependent sex effects in cardiac toxicity. QT prolongation is robustly female-biased (61.6%F, 122 drugs), validating ICH E14 guidance at pharmacovigilance scale and providing the largest population-level replication of the Makkar et al. (1993) TdP sex-difference finding. Cardiac AE severity shows male enrichment, consistent with the broader severity-sex gradient. The antipsychotic paradox---aggregate parity despite opposing QT (female) and metabolic (male) biases---demonstrates that AE-type stratification is essential for accurate sex-differential characterization.

These findings support sex-stratified cardiac safety monitoring, mechanism-specific risk assessment, and sex-disaggregated cardiac endpoint reporting in clinical trials and regulatory submissions. The structured mapping provided by this analysis---spanning 3,792 signals, 411 drugs, 8 drug classes, and 10 cardiac AE categories---establishes a reference framework for sex-aware cardiotoxicity assessment in both clinical practice and drug development.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## Conflicts of Interest

The author declares no conflicts of interest. This research received no external funding.

---

## Author Contributions

J.Shaik conceived the study, designed the analytical framework, performed all analyses, and wrote the manuscript.

---

## References

1. Onakpoya IJ, Heneghan CJ, Aronson JK. Post-marketing withdrawal of 462 medicinal products because of adverse drug reactions: a systematic review of the world literature. BMC Med. 2016;14:10. doi:10.1186/s12916-016-0553-2.

2. Shah RR. Drug-induced QT interval prolongation: does ethnicity of the thorough QT study population matter? Br J Clin Pharmacol. 2013;75(2):347-358. doi:10.1111/j.1365-2125.2012.04401.x.

3. Roden DM. Drug-induced prolongation of the QT interval. N Engl J Med. 2004;350(10):1013-1022. doi:10.1056/NEJMra032426.

4. Moslehi JJ. Cardiovascular toxic effects of targeted cancer therapies. N Engl J Med. 2016;375(15):1457-1467. doi:10.1056/NEJMra1100265.

5. Salem JE, Manouchehri A, Moey M, et al. Cardiovascular toxicities associated with immune checkpoint inhibitors: an observational, retrospective, pharmacovigilance study. Lancet Oncol. 2018;19(12):1579-1589. doi:10.1016/S1470-2045(18)30608-9.

6. Makkar RR, Fromm BS, Steinman RT, Meissner MD, Lehmann MH. Female gender as a risk factor for torsades de pointes associated with cardiovascular drugs. JAMA. 1993;270(21):2590-2597. doi:10.1001/jama.1993.03510210076031.

7. Regitz-Zagrosek V, Kararigas G. Mechanistic pathways of sex differences in cardiovascular disease. Physiol Rev. 2017;97(1):1-37. doi:10.1152/physrev.00021.2015.

8. Stolfo S, Uijl A, Vedin O, et al. Sex-based differences in heart failure across the ejection fraction spectrum: phenotyping, and prognostic and therapeutic implications. JACC Heart Fail. 2019;7(6):505-515. doi:10.1016/j.jchf.2019.03.011.

9. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. Lancet. 2020;396(10250):565-582. doi:10.1016/S0140-6736(20)31561-0.

10. Darpo B. The thorough QT/QTc study 4 years after the implementation of the ICH E14 guidance. Br J Pharmacol. 2010;159(1):49-57. doi:10.1111/j.1476-5381.2009.00487.x.

11. Lipshultz SE, Lipsitz SR, Mone SM, et al. Female sex and higher drug dose as risk factors for late cardiotoxic effects of doxorubicin therapy for childhood cancer. N Engl J Med. 1995;332(26):1738-1743. doi:10.1056/NEJM199506293322602.

12. Silber JH, Barber G, Cuttner J. Doxorubicin-induced cardiotoxicity. N Engl J Med. 1998;339(13):900-905.

13. Mosca L, Barrett-Connor E, Wenger NK. Sex/gender differences in cardiovascular disease prevention: what a difference a decade makes. Circulation. 2011;124(19):2145-2154. doi:10.1161/CIRCULATIONAHA.110.968792.

14. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001.

15. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11(1):32. doi:10.1186/s13293-020-00308-5.

16. Chen MH, Kerkela R, Force T. Mechanisms of cardiac dysfunction associated with tyrosine kinase inhibitor cancer therapeutics. Circulation. 2008;118(1):84-95. doi:10.1161/CIRCULATIONAHA.108.776831.

17. Ruberg FL, Grogan M, Hanna M, Kelly JW, Maurer MS. Transthyretin amyloid cardiomyopathy: JACC state-of-the-art review. J Am Coll Cardiol. 2019;73(22):2872-2891. doi:10.1016/j.jacc.2019.04.003.

18. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16(10):626-638. doi:10.1038/nri.2016.90.

19. Yancy CW, Jessup M, Bozkurt B, et al. 2013 ACCF/AHA guideline for the management of heart failure. J Am Coll Cardiol. 2013;62(16):e147-e239. doi:10.1016/j.jacc.2013.05.019.

20. Lenneman CG, Sawyer DB. Cardio-oncology: an update on cardiotoxicity of cancer-related treatment. Circ Res. 2016;118(6):1008-1020. doi:10.1161/CIRCRESAHA.115.303633.

---

## Figure Legends

**Figure 1.** Drug class cardiotoxicity spectrum. Bar chart showing mean female signal proportion (x-axis) for 8 drug classes (y-axis), ordered from most male-biased (TKIs, 47.6%F) to most female-biased (anthracyclines, 67.5%F). Error bars show within-class standard deviation. The 19.9 pp span demonstrates mechanism-dependent sex effects.

**Figure 2.** Cardiac AE type profiles. Grouped bar chart comparing female proportions across 10 cardiac AE categories. Rate-related events (tachycardia, palpitations) cluster at >60%F; structural events (MI, cardiac arrest, AFib) cluster near 50%F; QT prolongation stands alone at 61.6%F. The dashed line at 60.2% indicates the overall FAERS female reporting baseline.

**Figure 3.** QT prolongation drug-level analysis. Volcano plot of drug-level female proportion (x-axis) vs. significance (y-axis) for 165 QT signals. Extreme female outliers labeled (brexpiprazole 91.3%F, levothyroxine 90.9%F). Most drugs cluster in the 55--70%F range, demonstrating the universality of female QT vulnerability predicted by the repolarization reserve hypothesis.

**Figure 4.** The anthracycline-TKI divergence. Side-by-side cardiac AE profiles for anthracyclines and TKIs showing opposite sex biases across specific cardiac event types. Illustrates mechanism-dependent sex-differential cardiotoxicity. Panel A: anthracycline cardiac AE distribution by sex; Panel B: TKI cardiac AE distribution by sex; Panel C: overlay comparison highlighting the 19.9 pp divergence.

**Figure 5.** Severity gradient in cardiac AEs. Stacked bar chart comparing serious (51.3%F) vs. non-serious (55.8%F) cardiac signals, demonstrating male enrichment in severe cardiac outcomes. The 4.5 pp difference (p < 0.001) suggests that male cardiac events, when they occur, tend to be more severe.

**Figure 6.** Temporal stability analysis. Line plots showing female fraction for QT prolongation, anthracycline cardiotoxicity, and TKI cardiotoxicity across four time periods (2004--2008, 2009--2013, 2014--2018, 2019--2025). QT and anthracycline signals show remarkable temporal stability, while TKI male bias shows modest attenuation over time.

---

## Supplementary Material

**Supplementary Table S1.** Complete list of 35 MedDRA preferred terms used for cardiac AE identification, with mapping to 10 functional categories.

**Supplementary Table S2.** Full drug-level results for all 411 drugs with sex-differential cardiac signals, including %F, |logR|, N reports (male, female), and cardiac AE type distribution.

**Supplementary Table S3.** Sensitivity analysis results at |logR| thresholds of 0.3, 0.5, and 0.7.

**Supplementary Table S4.** Reporter-type stratified analysis showing female fraction by reporter category (physician, pharmacist, consumer, other) for cardiac vs. non-cardiac AEs.

**Supplementary Figure S1.** Anti-regression plot showing |logR| distribution across report volume quintiles, demonstrating no significant attenuation with increasing evidence.
