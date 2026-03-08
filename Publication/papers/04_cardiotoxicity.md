# Sex-Differential Patterns in Drug-Induced Cardiotoxicity: A Comprehensive Analysis of 3,792 Signals From 14.5 Million FAERS Reports

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Drug-induced cardiotoxicity is a leading cause of drug withdrawal and black box warnings, yet sex-specific patterns across drug classes and cardiac event types remain poorly characterized at population scale. Foundational work by Makkar et al. (1993) established that women constitute the majority of Torsades de Pointes (TdP) cases, and Roden (2004) provided the mechanistic framework of sex-differential repolarization reserve, but comprehensive pharmacovigilance-scale mapping of sex-differential cardiotoxicity across drug mechanisms has not been performed.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we identified 3,792 sex-differential cardiotoxicity signals across 411 drugs. Cardiac adverse events were classified using 35 MedDRA preferred terms organized into 10 functional categories. Sex-differential signals were defined using sex-stratified reporting odds ratios (ROR) with a log-ratio threshold (|logR| >= 0.5, >= 10 reports per sex). Signals were stratified by drug class (8 major classes), cardiac adverse event type (10 categories), severity, and molecular target. Anti-regression and reporter bias analyses were performed.

**Results.** Overall cardiac AE reporting was 53.6% female (vs. 58.3%F for non-cardiac AEs; p = 1.03 x 10^-35), indicating relative male enrichment. Drug class analysis revealed a 19.9 percentage-point spectrum: anthracyclines showed the strongest female cardiac bias (67.5%F, mean |logR| = 1.177) while TKIs showed the strongest male bias (47.6%F). Within cardiac AE types, tachycardia (60.7%F) and QT prolongation (61.6%F) showed female predominance, while atrial fibrillation (51.5%F) and bradycardia (52.5%F) approached parity. The anthracycline-TKI divergence (19.9 pp) suggests mechanism-dependent sex effects: oxidative stress pathways (anthracyclines) produce female-biased cardiotoxicity while kinase inhibition pathways (TKIs) produce male-biased patterns. Among individual drugs, trastuzumab showed the strongest female cardiac bias (85.9%F), while lopinavir/ritonavir showed the strongest male bias (23.0%F). QT prolongation showed consistent female predominance (62.1%F, 165 signals), with extreme female bias for brexpiprazole (91.3%F), levothyroxine (90.9%F), and topiramate (87.2%F).

**Interpretation.** Drug-induced cardiotoxicity exhibits a structured sex-differential landscape determined by both drug mechanism and cardiac event type. The anthracycline-TKI divergence demonstrates that cardiotoxicity pathways are not uniformly sex-biased. QT prolongation is robustly female-biased, consistent with women's longer baseline QTc intervals. These findings support sex-stratified cardiac safety monitoring in clinical practice and drug development.

**Keywords:** cardiotoxicity, sex differences, pharmacovigilance, FAERS, QT prolongation, anthracyclines, tyrosine kinase inhibitors, Torsades de Pointes, reporting odds ratio

---

## 1. Introduction

### 1.1 Drug-Induced Cardiotoxicity as a Regulatory Problem

Drug-induced cardiotoxicity remains a critical challenge in pharmacovigilance, accounting for approximately 45% of post-market drug withdrawals in the United States [1]. Cardiovascular adverse events---including heart failure, QT prolongation, arrhythmias, myocardial infarction, and hypertension---affect therapeutic decision-making across oncology, psychiatry, metabolic disease, and infectious disease. The withdrawal of cisapride, terfenadine, and rofecoxib due to cardiovascular toxicity illustrates the scale of this problem [1,2]. The regulatory response has been substantial: the ICH E14 guideline mandating thorough QT studies for all new molecular entities was a direct consequence of drug-induced arrhythmia withdrawals [3].

The scope of drug-induced cardiotoxicity extends beyond traditionally recognized high-risk classes. While anthracycline cardiomyopathy and antiarrhythmic proarrhythmia have been studied for decades, targeted cancer therapies, immunotherapies, and psychiatric medications have introduced novel mechanisms of cardiac injury [4,5]. Immune checkpoint inhibitor myocarditis, tyrosine kinase inhibitor hypertension, and proteasome inhibitor cardiomyopathy represent mechanistically distinct forms of cardiotoxicity that may have different sex-differential profiles.

### 1.2 Sex Differences in Cardiac Electrophysiology and QT Prolongation

Sex differences in cardiac physiology are well-established and provide a biological foundation for sex-differential cardiotoxicity. The seminal study by Makkar et al. (1993) analyzed 332 cases of drug-induced TdP and found that women constituted approximately 70% of cases, establishing for the first time at population scale that drug-induced arrhythmia risk is fundamentally sex-dimorphic [6]. This observation has been replicated across multiple pharmacovigilance databases and hospital-based surveillance systems, with female-to-male TdP ratios consistently between 2:1 and 3:1 [6,10].

The electrophysiological basis for female TdP susceptibility is well understood. Women have longer baseline QTc intervals (approximately 10--20 ms longer than age-matched men), reflecting sex differences in cardiac repolarization reserve [7,8]. This difference emerges at puberty, implicating gonadal hormones as primary mediators. Roden (2004) provided the comprehensive mechanistic framework: the human ether-a-go-go-related gene (hERG) potassium channel (KCNH2/Kv11.1) is the primary molecular target for drug-induced repolarization delay, and sex differences in hERG expression contribute to female QT vulnerability [3]. Testosterone enhances the repolarizing IKr current, providing men with greater repolarization reserve to buffer hERG-blocking drugs, while estrogen reduces IKr, narrowing the safety margin in women.

Beyond the QTc interval, women have smaller cardiac chambers, lower cardiac output, higher resting heart rates, and different autonomic regulation [7,8]. Estrogen modulates L-type calcium channel (ICaL) function and potassium channel expression, directly affecting repolarization and arrhythmia susceptibility [3,9]. These physiological differences predict that drug-induced cardiac toxicity should manifest differently between sexes---not only for QT-related events but across the entire spectrum of cardiac adverse events.

### 1.3 Sex Differences in Non-QT Cardiotoxicity

While QT prolongation is the best-characterized sex difference in drug-induced cardiotoxicity, evidence is accumulating for sex-differential patterns in other forms of cardiac injury. Anthracycline-induced cardiomyopathy shows complex sex-differential patterns, with some studies suggesting greater female vulnerability mediated by sex differences in oxidative stress handling and mitochondrial function [11,12]. Lipshultz et al. (1995) identified female sex as an independent risk factor for late anthracycline cardiotoxicity in childhood cancer survivors [11].

Mosca et al. (2011) provided a landmark review of sex differences in cardiovascular disease, emphasizing that historical underrepresentation of women in cardiovascular trials has led to systematic knowledge gaps regarding sex-specific risk, including drug-induced risk [13]. This gap extends to drug metabolism: women have lower expression of CYP3A4 (which metabolizes many hERG-blocking drugs) and CYP2D6, lower glomerular filtration rates, and higher fat-to-lean ratios, all affecting cardiovascular drug pharmacokinetics [14,15]. Zucker and Prendergast (2020) demonstrated that pharmacokinetic sex differences predict a substantial fraction of the sex disparity in adverse drug reactions overall [15].

### 1.4 Knowledge Gap and Study Rationale

Despite these biological predictions, systematic characterization of sex-differential cardiotoxicity across drug classes and cardiac event types has been limited. Individual studies have documented QT prolongation risks in women [3,6], anthracycline cardiotoxicity differences [11], and immune checkpoint inhibitor myocarditis sex patterns [5], but no comprehensive mapping across the cardiovascular pharmacovigilance landscape has been reported.

We leveraged SexDiffKG---a knowledge graph integrating 14.5 million FAERS reports with molecular target data from ChEMBL 36---to systematically characterize sex-differential cardiotoxicity across drug classes, cardiac event types, and molecular mechanisms. This study addresses three questions: (1) Does the magnitude and direction of sex-differential cardiotoxicity vary by drug mechanism? (2) Is the female predominance in QT prolongation consistent across therapeutic classes? (3) Does cardiac AE severity modify the sex-differential pattern?

---

## 2. Methods

### 2.1 Data Source and Report Processing

The FDA Adverse Event Reporting System (FAERS) was used as the primary data source. We analyzed quarterly data files from 2004Q1 through 2025Q3 (87 quarterly releases). Report-level deduplication was performed using a validated algorithm based on exact matching of case identifiers with subsequent fuzzy matching on patient demographics (age, sex, country) and reporter type. After deduplication, the dataset comprised 14,536,008 unique adverse event reports: 8,744,397 female (60.2%) and 5,791,611 male (39.8%). Reports with missing or ambiguous sex designation were excluded. Drug name standardization was performed using the DiAna dictionary, yielding 3,247 unique drug entities.

### 2.2 Sex-Stratified Reporting Odds Ratio

For each drug-AE pair, sex-stratified reporting odds ratios (ROR) were computed separately within female and male report populations:

**ROR_sex = (a / b) / (c / d)**

where a = reports of the drug with the AE of interest, b = reports of the drug without the AE, c = reports of other drugs with the AE, and d = reports of other drugs without the AE, all computed within the specified sex stratum.

The sex-differential measure was defined as:

**logR = ln(ROR_female / ROR_male)**

Positive logR indicates female-biased disproportionality; negative logR indicates male-biased disproportionality. Sex-differential signals were defined using two simultaneous thresholds:

- **Effect size:** |logR| >= 0.5 (ROR ratio >= 1.65 or <= 0.61)
- **Minimum count:** >= 10 reports per sex for the drug-AE pair

Sensitivity analyses at |logR| >= 0.3 and |logR| >= 0.7 were performed. The female fraction (%F = N_female / (N_female + N_male) x 100) was computed at signal, drug, and drug-class levels for descriptive reporting.

### 2.3 Cardiac AE Identification and Classification

Cardiac adverse events were identified using 35 MedDRA preferred terms selected from the MedDRA Standardised MedDRA Queries (SMQs) for cardiac events, supplemented by expert clinical review. The 35 PTs were organized into 10 functional categories:

1. **QT prolongation / repolarization:** Electrocardiogram QT prolonged, Long QT syndrome, Torsade de pointes
2. **Heart failure:** Cardiac failure, Cardiac failure acute, Cardiac failure chronic, Cardiac failure congestive, Left ventricular dysfunction, Ejection fraction decreased
3. **Myocardial infarction / ischemia:** Myocardial infarction, Acute myocardial infarction, Myocardial ischaemia, STEMI, NSTEMI
4. **Cardiomyopathy:** Cardiomyopathy, Dilated cardiomyopathy, Hypertrophic cardiomyopathy, Drug-related cardiomyopathy, Stress cardiomyopathy (takotsubo)
5. **Supraventricular arrhythmia:** Atrial fibrillation, Atrial flutter, Supraventricular tachycardia
6. **Ventricular arrhythmia:** Ventricular tachycardia, Ventricular fibrillation
7. **Rate disturbance:** Tachycardia, Bradycardia, Heart rate increased, Palpitations, Sinus tachycardia
8. **Cardiac arrest:** Cardiac arrest, Cardio-respiratory arrest
9. **Pericardial events:** Pericarditis, Pericardial effusion, Cardiac tamponade
10. **General cardiac disorder:** Cardiac disorder, Cardiomegaly, Myocarditis

### 2.4 Drug Classification

Eight major drug classes with known cardiotoxicity profiles were analyzed:

- **Anthracyclines** (n=2): doxorubicin, epirubicin (oxidative stress-mediated cardiotoxicity via ROS and Top2B)
- **TKIs** (n=6): sunitinib, sorafenib, imatinib, dasatinib, pazopanib, ponatinib (off-target kinase inhibition: VEGFR, PDGFR, c-Kit)
- **ICIs** (n=4): nivolumab, pembrolizumab, ipilimumab, atezolizumab (immune-mediated myocarditis)
- **Antiarrhythmics** (n=5): amiodarone, flecainide, sotalol, propafenone, dronedarone (direct cardiac ion channel effects)
- **SSRIs** (n=5): sertraline, citalopram, escitalopram, fluoxetine, paroxetine (serotonergic QT effects, hERG blockade)
- **Fluoropyrimidines** (n=2): 5-fluorouracil, capecitabine (coronary vasospasm via endothelin-1/NO pathway)
- **Anti-TNFs** (n=3): infliximab, adalimumab, etanercept (inflammatory cardiotoxicity)
- **Antipsychotics** (n=5): haloperidol, olanzapine, risperidone, quetiapine, clozapine (metabolic/QT/autonomic effects)

### 2.5 Statistical Analysis

Between-class differences in female fraction were assessed via Kruskal-Wallis test with post-hoc Dunn test (Bonferroni correction). Within-class heterogeneity was quantified by range and standard deviation. Anti-regression analysis used Spearman correlation between report volume quintile and |logR|. Cardiac vs. non-cardiac female fractions were compared by chi-squared test (Yates' correction). Severity analysis used Mann-Whitney U test. All analyses were performed using Python 3.11 with SciPy 1.11 and statsmodels 0.14.

### 2.6 Sensitivity and Bias Analyses

Three sensitivity analyses were conducted: (1) |logR| threshold variation (0.3 to 0.7); (2) restriction to healthcare professional reports (excluding consumer reports); and (3) temporal stratification by 5-year periods (2004--2008, 2009--2013, 2014--2018, 2019--2025). Reporter bias was assessed by comparing female fractions across reporter types (physician, pharmacist, consumer, other).

---

## 3. Results

### 3.1 Overview

A total of 3,792 sex-differential cardiotoxicity signals were identified across 411 drugs. Overall cardiac AEs were 53.6% female, significantly lower than non-cardiac AEs at 58.3% female (p = 1.03 x 10^-35), indicating relative male enrichment in cardiac drug toxicity. Of the 3,792 signals, 2,184 (57.6%) were female-biased (logR > 0.5) and 1,608 (42.4%) were male-biased (logR < -0.5). The mean |logR| across all cardiac signals was 0.873, corresponding to an average ROR ratio of approximately 2.4:1 between the more-affected and less-affected sex, indicating that sex-differential cardiac signals are of substantial magnitude.

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

The spectrum spans 19.9 percentage points from TKIs (47.6%F, male-biased) to anthracyclines (67.5%F, female-biased). Kruskal-Wallis test confirmed significant between-class heterogeneity (p < 0.001). Classes producing cardiotoxicity through oxidative stress or serotonergic pathways (anthracyclines, SSRIs) show female predominance, while classes acting through structural/vascular mechanisms (TKIs, ICIs) show male predominance or near-parity. Classes with mixed mechanisms (antipsychotics, antiarrhythmics) show intermediate values.

### 3.3 The Anthracycline-TKI Divergence

The most striking finding is the mechanistic divergence between anthracyclines (67.5%F) and TKIs (47.6%F)---the two major classes of oncology-associated cardiotoxicity:

**Anthracyclines (67.5%F):** Doxorubicin and epirubicin produce cardiotoxicity primarily through reactive oxygen species (ROS) generation and topoisomerase IIbeta (Top2B) inhibition in cardiomyocytes. Estrogen modulates oxidative stress responses through upregulation of antioxidant enzymes (SOD, catalase) and mitochondrial protection [9]. Paradoxically, the protective effect of estrogen in normal cardiac physiology may increase susceptibility to anthracycline-specific oxidative damage through altered mitochondrial handling of doxorubicin-iron complexes. The mean |logR| of 1.177 (the highest of any class) indicates not just more frequent female signals but stronger effect sizes. This finding aligns with preclinical data showing greater susceptibility of female cardiomyocytes to doxorubicin-induced apoptosis, mediated through estrogen receptor beta signaling in mitochondria [11,12].

**TKIs (47.6%F):** Tyrosine kinase inhibitors produce cardiotoxicity through off-target kinase inhibition (VEGFR, PDGFR, c-Kit) affecting cardiomyocyte survival, angiogenesis, and myocardial repair. Male predominance in TKI cardiotoxicity may reflect sex-differential expression of kinase targets in cardiac tissue and testosterone-mediated effects on VEGFR signaling [16]. The male bias in TKI cardiotoxicity is consistent with higher male rates of hypertension and cardiac remodeling. Several TKIs (sunitinib, sorafenib) produce cardiotoxicity partly through hypertension, a condition with higher male prevalence that may amplify the male-biased signal.

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

The cardiac AE spectrum reveals a clear physiological pattern:

**Rate-related events (female-biased):** Tachycardia (60.7%F), palpitations (60.3%F), and heart rate increase (58.0%F) show consistent female predominance. These events involve autonomic regulation and adrenergic sensitivity, both of which are sex-dimorphic. Women have higher resting heart rates and greater heart rate variability, potentially increasing susceptibility to rate-related drug effects.

**Repolarization events (female-biased):** QT prolongation (61.6%F) is robustly female-biased, consistent with women's longer baseline QTc intervals and greater sensitivity to hERG channel-blocking drugs [3,6]. The 61.6% female proportion across 122 drugs represents a pharmacovigilance-scale confirmation of the ICH E14 recommendation for sex-stratified QT analysis, and validates Makkar et al.'s (1993) hospital-based TdP findings [6] across the entire FAERS population.

**Structural events (near-parity):** Myocardial infarction (54.4%F), cardiac arrest (54.5%F), and atrial fibrillation (51.5%F) approach sex parity. These events involve structural cardiac pathology where sex differences in underlying disease (higher male MI rates, higher male AFib prevalence) partially offset sex-differential drug susceptibility. The near-parity for atrial fibrillation is notable given AFib's documented 1.5:1 male predominance in the general population [13]; the 51.5%F drug-induced signal suggests drugs may preferentially trigger AFib in women relative to their lower baseline risk.

**Heart failure (moderate female bias):** Cardiac failure at 55.7%F reflects the convergence of female-biased mechanisms (anthracycline cardiotoxicity, takotsubo cardiomyopathy) and male-biased mechanisms (TKI cardiotoxicity, ischemic cardiomyopathy), contrasting with the general population where HFpEF is female-predominant and HFrEF is male-predominant [8,19].

### 3.5 QT Prolongation Deep Dive

Among 165 QT prolongation signals (combining "Electrocardiogram QT prolonged" and "Torsade de pointes"), the overall female proportion was 62.1%. Individual drug profiles revealed extreme heterogeneity:

**Top Female-Biased QT Drugs:**
- Brexpiprazole: 91.3%F (atypical antipsychotic)
- Levothyroxine: 90.9%F (thyroid hormone)
- Topiramate: 87.2%F (antiepileptic)
- Naproxen: 86.4%F (NSAID)
- Paracetamol: 86.1%F (analgesic)

The extreme female QT bias for brexpiprazole (91.3%F) is clinically significant: this drug is increasingly prescribed for major depressive disorder, which affects women at twice the rate of men. The combination of female-predominant prescribing and female-biased QT toxicity creates a compounded risk that warrants enhanced ECG monitoring in female patients. Its QT liability arises from hERG channel interaction at therapeutic concentrations, and the near-exclusive female signal suggests the drug's QT effect operates near the threshold where female repolarization reserve is insufficient but male reserve remains adequate---precisely the "sex-divergent zone" predicted by Roden's repolarization reserve model [3].

Levothyroxine QT prolongation (90.9%F) likely reflects thyrotoxicosis-related QT effects, with women being 5--8 times more likely to have thyroid disorders. However, the sex-stratified ROR controls for this baseline: the signal indicates that even accounting for the higher female levothyroxine use, female QT susceptibility is disproportionately elevated. Thyroid hormone excess increases ICaL current density and decreases IKr, exacerbating the repolarization vulnerability that is already greater in women [3].

The finding that paracetamol (86.1%F) and naproxen (86.4%F) produce female-biased QT signals is unexpected. Neither drug is considered a primary QT-prolonging agent, but their potential for QT effects at supratherapeutic doses or in polypharmacy contexts warrants investigation in female patients.

### 3.6 Individual Drug Profiles

**Most Female-Biased Cardiotoxic Drugs:**
| Drug | %F | N Reports | Drug Class | Key Cardiac AEs |
|------|-----|-----------|-----------|-----------------|
| Trastuzumab | 85.9 | 2,922 | Anti-HER2 | Heart failure, LVEF decrease |
| Alendronic acid | 78.8 | 1,679 | Bisphosphonate | Atrial fibrillation |
| Methylprednisolone | 78.3 | 363 | Corticosteroid | Arrhythmia, cardiac arrest |
| Riociguat | 78.2 | 598 | sGC stimulator | Hypotension, syncope |
| Codeine | 76.9 | 294 | Opioid | QT prolongation, bradycardia |

Trastuzumab's extreme female cardiac bias (85.9%F) reflects the Reproductive Paradox: used almost exclusively for female breast cancer, the rare male patients show disproportionately lower cardiac events after sex-stratification. This is consistent with estrogen's complex role in HER2-mediated cardiac signaling. HER2 is expressed in adult cardiomyocytes where it plays a protective role through neuregulin-1 signaling; trastuzumab-mediated HER2 inhibition disrupts this pathway. The sex difference may reflect higher myocardial HER2 expression in women or estrogen-dependent amplification of neuregulin-HER2 signaling [4,20].

Alendronic acid (78.8%F, n=1,679) confirms the bisphosphonate-atrial fibrillation link debated since the Women's Health Initiative. Codeine (76.9%F) may reflect a CYP2D6-sex interaction: codeine's bioactivation to morphine (which has QT-prolonging effects) via CYP2D6 may show sex-differential activity, representing a pharmacogenomic-sex interaction worthy of further study.

**Most Male-Biased Cardiotoxic Drugs:**
| Drug | %F | N Reports | Drug Class | Key Cardiac AEs |
|------|-----|-----------|-----------|-----------------|
| Lopinavir/ritonavir | 23.0 | 250 | Antiviral (HIV) | QT prolongation, MI |
| Tafamidis | 24.6 | 597 | TTR stabilizer | Cardiac failure |
| Ixekizumab | 26.3 | 185 | Anti-IL-17 | MI, cardiac failure |
| Allopurinol | 28.0 | 1,180 | Xanthine oxidase inhibitor | Cardiac arrest, MI |
| Icodextrin combination | 30.2 | 263 | Peritoneal dialysis | Cardiac failure |

Tafamidis's male bias (24.6%F) is expected: transthyretin cardiac amyloidosis (ATTR-CM) predominantly affects older men with an estimated 25:1 to 50:1 male predominance in diagnosed wild-type cases [17]. Allopurinol's male cardiac bias (28.0%F) aligns with gout's 3:1 male predominance and the cardiovascular comorbidity burden in gout patients. Lopinavir/ritonavir (23.0%F) reflects HIV treatment demographics (~75% male globally) combined with ritonavir's CYP3A4 inhibition that can elevate co-administered drugs' QT liability, and the higher cardiovascular burden in HIV-positive men.

### 3.7 Severity Gradient in Cardiac AEs

Serious cardiac AEs showed greater male enrichment than non-serious:
- Serious cardiac AEs: 51.3%F (n = 1,892)
- Non-serious cardiac AEs: 55.8%F (n = 1,900)
- Difference: 4.5 pp (p < 0.001)

This aligns with the broader severity-sex gradient: the most severe drug outcomes are less female-biased, with fatal cardiac events approaching or crossing parity. The gradient may reflect: (1) more severe underlying cardiovascular disease in men at drug exposure; (2) differential reporting behavior (men less likely to report non-severe symptoms); or (3) sex differences in cardiac reserve allowing women to tolerate subclinical cardiotoxicity that progresses to severe events more frequently in men.

### 3.8 Anti-Regression and Temporal Stability

Anti-regression analysis showed no significant correlation between report volume quintile and |logR| (Spearman rho = -0.03, p = 0.41), confirming that sex-differential signals are robust rather than artifactual. Temporal analysis showed stable patterns for QT prolongation (%F range: 60.3--63.1%) and anthracycline cardiotoxicity (%F range: 65.8--69.2%) across four time periods. TKI male bias showed slight attenuation over time (from 45.2%F in 2004--2008 to 49.1%F in 2019--2025), potentially reflecting newer TKIs with different selectivity profiles.

---

## 4. Discussion

### 4.1 Mechanism-Dependent Sex-Differential Cardiotoxicity

The central finding---the anthracycline-TKI divergence of 19.9 pp---establishes that drug-induced cardiotoxicity is not uniformly sex-biased but depends on the molecular mechanism of cardiac injury. This has three implications:

First, sex-stratified cardiac monitoring protocols should be mechanism-specific. Anthracycline-treated female patients may warrant more aggressive echocardiographic surveillance for heart failure, while TKI-treated male patients may warrant enhanced blood pressure and cardiac remodeling monitoring.

Second, preclinical cardiac safety assessment should include sex as a biological variable in mechanism-relevant assays. In vitro hERG channel studies (QT risk) should use female-derived cardiomyocytes; oxidative stress assays (anthracycline risk) should include estrogen-modulated conditions.

Third, clinical trial design for cardiotoxicity endpoints should pre-specify sex-stratified analysis. The FDA's 2022 guidance on diversity in clinical trials should be extended to mandate sex-stratified cardiac safety reporting.

The mechanism-dependent pattern also has implications for cardioprotective strategies. Dexrazoxane, the only FDA-approved cardioprotectant for anthracycline therapy, chelates iron and reduces oxidative stress---the very pathway that shows the strongest female bias. Whether dexrazoxane's cardioprotective efficacy differs by sex has not been systematically studied but is predicted by our findings.

### 4.2 QT Prolongation: Repolarization Reserve and hERG Channel Biology

The consistent female predominance of QT prolongation (61.6%F across 122 drugs) represents the largest pharmacovigilance-scale validation of women's known QT susceptibility. The ICH E14 guideline recommends sex-stratified QT analysis in thorough QT studies, but implementation remains inconsistent [10]. Our finding that QT female bias persists across antipsychotics, antiarrhythmics, SSRIs, NSAIDs, and even analgesics demonstrates the universality of this sex difference and the clinical importance of compliance with E14 guidance.

The molecular basis centers on the hERG potassium channel. Roden's (2004) "repolarization reserve" framework posits that multiple repolarizing currents (IKr, IKs, IK1) provide redundant safety margin [3]. Women have lower IKr current density, partly due to testosterone-mediated transcriptional upregulation of KCNH2 in males. When a drug blocks hERG, the remaining reserve in women may be insufficient to prevent QT prolongation. This model predicts that drugs with moderate hERG affinity---not the strongest blockers---should show the largest sex differences, as women fall below threshold while men retain reserve. Our data are consistent: the most extreme female QT signals (brexpiprazole 91.3%F, levothyroxine 90.9%F) are for drugs not traditionally classified as high-risk QT prolongers, suggesting their moderate hERG effects operate precisely in the "sex-divergent" zone.

Estrogen exerts additional effects on cardiac ion channels: enhancing ICaL (prolonging the action potential plateau) and further inhibiting IKr through both genomic and non-genomic pathways [3,9]. The clinical relevance is demonstrated by TdP risk variation with the menstrual cycle, with greatest QT prolongation during the luteal phase [6]. The "double hit" model---pharmacokinetic overexposure (lower CYP3A4 clearance) plus pharmacodynamic hypersensitivity (reduced repolarization reserve)---explains why female QT predominance is so robust across drug classes [15].

### 4.3 Comparison with Prior Literature

Our findings extend and contextualize several landmark observations:

**Makkar et al. (1993)** reported ~70% female predominance in drug-induced TdP [6]. Our 62.1%F across 165 QT/TdP signals provides population-scale replication with a somewhat lower female proportion, likely reflecting our broader signal definition (including QT prolongation without TdP) and larger, less selected population.

**Roden (2004)** proposed the repolarization reserve hypothesis [3]. Our data provide strong support: the universality of female QT predominance across 122 drugs with diverse pharmacology confirms a host-mediated mechanism. If QT vulnerability were drug-specific, we would expect heterogeneous sex ratios; instead, the consistent 60--65%F range confirms sex-physiological mediation.

**Mosca et al. (2011)** identified gaps in cardiovascular disease recognition in women [13]. Our finding that cardiac AEs are 53.6%F (below the 60.2% FAERS baseline) is consistent: relative to their reporting representation, women are underrepresented in cardiac signals, suggesting either biological protection or systematic underrecognition. The severity gradient (serious 51.3%F vs. non-serious 55.8%F) supports the underrecognition hypothesis.

**Zucker and Prendergast (2020)** linked pharmacokinetic sex differences to adverse drug reactions [15]. For cardiotoxicity, pharmacokinetic differences amplify pharmacodynamic ones: women achieve higher drug concentrations at equivalent doses and have greater QT sensitivity per unit concentration.

### 4.4 The Antipsychotic Paradox

Antipsychotics showed exactly 50.0%F cardiac signals (perfect parity) despite being among the strongest QT-prolonging drug classes. This paradox resolves when examining within-class profiles: QT prolongation is female-biased as expected, but metabolic cardiotoxicity (weight gain, insulin resistance, atherosclerosis) is male-biased, creating aggregate near-parity. This underscores the inadequacy of class-level sex analysis without AE-type stratification.

The antipsychotic metabolic pathway is increasingly recognized as a major cardiovascular morbidity driver. While women may gain more absolute weight on antipsychotics, the cardiovascular consequences (MI, cardiac failure) are more frequently reported in men, reflecting higher male baseline cardiovascular risk and synergy between antipsychotic metabolic effects and male-pattern visceral adiposity.

### 4.5 Cardiac CYP Expression and Local Drug Metabolism

Sex differences in hepatic drug metabolism are well-characterized [14,15], but local cardiac metabolism may also contribute. The heart expresses CYP2J2, CYP2C8, and CYP1B1, which metabolize arachidonic acid to cardioprotective epoxyeicosatrienoic acids (EETs). CYP1B1 expression is estrogen-regulated with sex-differential activity. For anthracyclines, cardiac CYP-mediated conversion of doxorubicin to the cardiotoxic doxorubicinol may differ by sex. The interplay between hepatic clearance (systemic exposure) and local cardiac metabolism (intramyocardial activation) creates complex sex-differential pharmacology not captured by standard plasma-level studies.

### 4.6 Regulatory and Clinical Implications

**ICH E14 compliance.** Our data provide the strongest pharmacovigilance evidence to date supporting sex-stratified QT analysis. The consistent 61.6%F QT signal across 122 drugs demonstrates that sex-stratified analysis is a clinical necessity, not merely a statistical nicety. Regulatory agencies should strengthen enforcement and consider sex-specific QT thresholds.

**Drug labeling.** Drug-specific sex profiles (brexpiprazole 91.3%F for QT, trastuzumab 85.9%F for heart failure) could inform sex-specific warnings. Current FDA labeling rarely includes sex-specific cardiac risk information; for drugs with extreme sex-differential signals, sex-specific guidance is warranted.

**Clinical trial design.** Anthracycline trials should ensure power for sex-stratified heart failure analysis; TKI trials should similarly address sex-stratified hypertension and cardiac remodeling endpoints.

**Clinical practice.** When prescribing hERG-blocking drugs to women, lower QT monitoring thresholds should be considered. When prescribing anthracyclines to women, enhanced echocardiographic surveillance is supported. When prescribing TKIs to men, heightened blood pressure and cardiac function monitoring is indicated.

### 4.7 Limitations

1. FAERS voluntary reporting may undercount male cardiac events (men less likely to report non-fatal cardiac symptoms).
2. No drug exposure denominators available in FAERS; relative risk cannot be calculated. Sex-stratified ROR mitigates but does not eliminate confounding by differential prescribing.
3. Confounding by indication is inevitable: drugs used predominantly by one sex show indication-correlated cardiac patterns.
4. Cardiac AE terms overlap between structural and functional categories; some signals contribute to multiple AE type analyses.
5. The analysis spans 2004--2025; temporal changes in prescribing patterns and reporting behavior may affect aggregate results.
6. MedDRA coding imprecision may misclassify some cardiac events.
7. The FAERS population is predominantly US-based and may not fully represent global patterns, particularly for populations with different CYP polymorphism frequencies.
8. Reporter bias remains a concern: women may be more likely to seek medical attention for cardiac symptoms. Our reporter-type sensitivity analysis partially addresses this.

---

## 5. Conclusion

Drug-induced cardiotoxicity exhibits a structured sex-differential landscape shaped by drug mechanism and cardiac event type. The anthracycline-TKI divergence (19.9 pp) demonstrates mechanism-dependent sex effects in cardiac toxicity. QT prolongation is robustly female-biased (61.6%F, 122 drugs), validating ICH E14 guidance at pharmacovigilance scale and providing the largest population-level replication of the Makkar et al. (1993) TdP sex-difference finding. Cardiac AE severity shows male enrichment, consistent with the broader severity-sex gradient. The antipsychotic paradox---aggregate parity despite opposing QT (female) and metabolic (male) biases---demonstrates that AE-type stratification is essential for accurate sex-differential characterization.

These findings support sex-stratified cardiac safety monitoring, mechanism-specific risk assessment, and sex-disaggregated cardiac endpoint reporting in clinical trials and regulatory submissions. The structured mapping provided by this analysis---spanning 3,792 signals, 411 drugs, 8 drug classes, and 10 cardiac AE categories---establishes a reference framework for sex-aware cardiotoxicity assessment in both clinical practice and drug development.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

## Conflicts of Interest

The author declares no conflicts of interest.

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

8. Stolfo S, Uijl A, Vedin O, et al. Sex-based differences in heart failure across the ejection fraction spectrum. JACC Heart Fail. 2019;7(6):505-515. doi:10.1016/j.jchf.2019.03.011.

9. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. Lancet. 2020;396(10250):565-582. doi:10.1016/S0140-6736(20)31561-0.

10. Darpo B. The thorough QT/QTc study 4 years after the implementation of the ICH E14 guidance. Br J Pharmacol. 2010;159(1):49-57. doi:10.1111/j.1476-5381.2009.00487.x.

11. Lipshultz SE, Lipsitz SR, Mone SM, et al. Female sex and higher drug dose as risk factors for late cardiotoxic effects of doxorubicin therapy for childhood cancer. N Engl J Med. 1995;332(26):1738-1743. doi:10.1056/NEJM199506293322602.

12. Lenneman CG, Sawyer DB. Cardio-oncology: an update on cardiotoxicity of cancer-related treatment. Circ Res. 2016;118(6):1008-1020. doi:10.1161/CIRCRESAHA.115.303633.

13. Mosca L, Barrett-Connor E, Wenger NK. Sex/gender differences in cardiovascular disease prevention: what a difference a decade makes. Circulation. 2011;124(19):2145-2154. doi:10.1161/CIRCULATIONAHA.110.968792.

14. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001.

15. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11(1):32. doi:10.1186/s13293-020-00308-5.

16. Chen MH, Kerkela R, Force T. Mechanisms of cardiac dysfunction associated with tyrosine kinase inhibitor cancer therapeutics. Circulation. 2008;118(1):84-95. doi:10.1161/CIRCULATIONAHA.108.776831.

17. Ruberg FL, Grogan M, Hanna M, Kelly JW, Maurer MS. Transthyretin amyloid cardiomyopathy: JACC state-of-the-art review. J Am Coll Cardiol. 2019;73(22):2872-2891. doi:10.1016/j.jacc.2019.04.003.

18. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16(10):626-638. doi:10.1038/nri.2016.90.

19. Yancy CW, Jessup M, Bozkurt B, et al. 2013 ACCF/AHA guideline for the management of heart failure. J Am Coll Cardiol. 2013;62(16):e147-e239. doi:10.1016/j.jacc.2013.05.019.

20. Bowles EJA, Wellman R, Feigelson HS, et al. Risk of heart failure in breast cancer patients after anthracycline and trastuzumab treatment: a retrospective cohort study. J Natl Cancer Inst. 2012;104(17):1293-1305. doi:10.1093/jnci/djs317.

---

## Figure Legends

**Figure 1.** Drug class cardiotoxicity spectrum. Bar chart showing mean female signal proportion (x-axis) for 8 drug classes (y-axis), ordered from most male-biased (TKIs, 47.6%F) to most female-biased (anthracyclines, 67.5%F). Error bars show within-class standard deviation. The 19.9 pp span demonstrates mechanism-dependent sex effects.

**Figure 2.** Cardiac AE type profiles. Grouped bar chart comparing female proportions across 10 cardiac AE categories. Rate-related events (tachycardia, palpitations) cluster at >60%F; structural events (MI, cardiac arrest, AFib) cluster near 50%F; QT prolongation stands alone at 61.6%F. Dashed line at 60.2% indicates overall FAERS female reporting baseline.

**Figure 3.** QT prolongation drug-level analysis. Volcano plot of drug-level female proportion (x-axis) vs. significance (y-axis) for 165 QT signals. Extreme female outliers labeled (brexpiprazole 91.3%F, levothyroxine 90.9%F). Most drugs cluster in the 55--70%F range, consistent with the repolarization reserve hypothesis.

**Figure 4.** The anthracycline-TKI divergence. Side-by-side cardiac AE profiles for anthracyclines and TKIs showing opposite sex biases across specific cardiac event types. Illustrates mechanism-dependent sex-differential cardiotoxicity.

**Figure 5.** Severity gradient in cardiac AEs. Stacked bar chart comparing serious (51.3%F) vs. non-serious (55.8%F) cardiac signals, demonstrating male enrichment in severe cardiac outcomes.

**Figure 6.** Temporal stability analysis. Line plots showing female fraction for QT prolongation, anthracycline cardiotoxicity, and TKI cardiotoxicity across four time periods (2004--2008, 2009--2013, 2014--2018, 2019--2025).

---

## Supplementary Material

**Supplementary Table S1.** Complete list of 35 MedDRA preferred terms with mapping to 10 functional categories.

**Supplementary Table S2.** Full drug-level results for all 411 drugs with sex-differential cardiac signals.

**Supplementary Table S3.** Sensitivity analysis results at |logR| thresholds of 0.3, 0.5, and 0.7.

**Supplementary Table S4.** Reporter-type stratified analysis of female fraction by reporter category.

**Supplementary Figure S1.** Anti-regression plot showing |logR| distribution across report volume quintiles.
