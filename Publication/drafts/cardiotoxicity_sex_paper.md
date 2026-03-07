# Sex-Differential Patterns in Drug-Induced Cardiotoxicity: A Comprehensive Analysis of 3,792 Signals From 14.5 Million FAERS Reports

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Drug-induced cardiotoxicity is a leading cause of drug withdrawal and black box warnings, yet sex-specific patterns across drug classes and cardiac event types remain poorly characterized at population scale.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we identified 3,792 sex-differential cardiotoxicity signals across 411 drugs. Signals were stratified by drug class (8 major classes), cardiac adverse event type (10 categories), severity, and molecular target. Anti-regression and reporter bias analyses were performed.

**Results.** Overall cardiac AE reporting was 53.6% female (vs. 58.3%F for non-cardiac AEs; p = 1.03 x 10^-35), indicating relative male enrichment. Drug class analysis revealed a 19.9 percentage-point spectrum: anthracyclines showed the strongest female cardiac bias (67.5%F, mean |logR| = 1.177) while TKIs showed the strongest male bias (47.6%F). Within cardiac AE types, tachycardia (60.7%F) and QT prolongation (61.6%F) showed female predominance, while atrial fibrillation (51.5%F) and bradycardia (52.5%F) approached parity. The anthracycline-TKI divergence (19.9 pp) suggests mechanism-dependent sex effects: oxidative stress pathways (anthracyclines) produce female-biased cardiotoxicity while kinase inhibition pathways (TKIs) produce male-biased patterns. Among individual drugs, trastuzumab showed the strongest female cardiac bias (85.9%F), while lopinavir/ritonavir showed the strongest male bias (23.0%F). QT prolongation showed consistent female predominance (62.1%F, 165 signals), with extreme female bias for brexpiprazole (91.3%F), levothyroxine (90.9%F), and topiramate (87.2%F).

**Interpretation.** Drug-induced cardiotoxicity exhibits a structured sex-differential landscape determined by both drug mechanism and cardiac event type. The anthracycline-TKI divergence demonstrates that cardiotoxicity pathways are not uniformly sex-biased. QT prolongation is robustly female-biased, consistent with women's longer baseline QTc intervals. These findings support sex-stratified cardiac safety monitoring in clinical practice and drug development.

---

## Introduction

Drug-induced cardiotoxicity remains a critical challenge in pharmacovigilance, accounting for approximately 45% of post-market drug withdrawals in the United States [1]. Cardiovascular adverse events---including heart failure, QT prolongation, arrhythmias, myocardial infarction, and hypertension---affect therapeutic decision-making across oncology, psychiatry, metabolic disease, and infectious disease.

Sex differences in cardiac physiology are well-established and provide a biological foundation for sex-differential cardiotoxicity. Women have longer baseline QTc intervals (approximately 10--20 ms longer than age-matched men), smaller cardiac chambers, lower cardiac output, and different autonomic regulation [2,3]. Estrogen modulates L-type calcium channel function and potassium channel expression, directly affecting repolarization and arrhythmia susceptibility [4]. These physiological differences predict that drug-induced cardiac toxicity should manifest differently between sexes.

Despite these biological predictions, systematic characterization of sex-differential cardiotoxicity across drug classes and cardiac event types has been limited. Individual studies have documented QT prolongation risks in women [5] and anthracycline cardiotoxicity differences [6], but no comprehensive mapping across the cardiovascular pharmacovigilance landscape has been reported.

We leveraged SexDiffKG---a knowledge graph integrating 14.5 million FAERS reports with molecular target data from ChEMBL 36---to systematically characterize sex-differential cardiotoxicity across drug classes, cardiac event types, and molecular mechanisms.

---

## Methods

### Data Source

FAERS 2004Q1--2025Q3: 14,536,008 deduplicated reports (8,744,397 female [60.2%]; 5,791,611 male [39.8%]). Drug names normalized via DiAna dictionary. Sex-stratified ROR computed per drug--AE pair. logR = ln(ROR_female / ROR_male). Signals defined at |logR| >= 0.5 with >= 10 reports per sex.

### Cardiac AE Identification

Cardiac adverse events identified using 35 MedDRA preferred terms spanning: QT prolongation, torsade de pointes, heart failure (acute, chronic, congestive), myocardial infarction (acute, STEMI, NSTEMI), cardiomyopathy (dilated, hypertrophic, drug-related), arrhythmias (atrial fibrillation, ventricular tachycardia, supraventricular tachycardia), pericardial events (pericarditis, pericardial effusion), cardiac arrest, bradycardia, tachycardia, palpitations, and general cardiac disorder terms.

### Drug Classification

Eight major drug classes with known cardiotoxicity profiles were analyzed:
- **Anthracyclines**: doxorubicin, epirubicin (oxidative stress-mediated cardiotoxicity)
- **TKIs**: sunitinib, sorafenib, imatinib, dasatinib, pazopanib, ponatinib (kinase inhibition)
- **ICIs**: nivolumab, pembrolizumab, ipilimumab, atezolizumab (immune-mediated myocarditis)
- **Antiarrhythmics**: amiodarone, flecainide, sotalol, propafenone, dronedarone (direct cardiac ion channel effects)
- **SSRIs**: sertraline, citalopram, escitalopram, fluoxetine, paroxetine (serotonergic QT effects)
- **Fluoropyrimidines**: 5-fluorouracil, capecitabine (coronary vasospasm)
- **Anti-TNFs**: infliximab, adalimumab, etanercept (inflammatory cardiotoxicity)
- **Antipsychotics**: haloperidol, olanzapine, risperidone, quetiapine, clozapine (metabolic/QT effects)

### Statistical Analysis

Female fraction computed per drug-AE pair, aggregated by drug class. Between-class differences assessed via Kruskal-Wallis test. Within-class heterogeneity via range and standard deviation. Anti-regression analysis via Spearman correlation with report volume quintiles. Effect sizes reported as mean absolute log-ratio |logR|.

---

## Results

### Overview

A total of 3,792 sex-differential cardiotoxicity signals were identified across 411 drugs. Overall cardiac AEs were 53.6% female, significantly lower than non-cardiac AEs at 58.3% female (p = 1.03 x 10^-35), indicating relative male enrichment in cardiac drug toxicity.

### Drug Class Cardiotoxicity Spectrum

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

### The Anthracycline-TKI Divergence

The most striking finding is the mechanistic divergence between anthracyclines (67.5%F) and TKIs (47.6%F)---the two major classes of oncology-associated cardiotoxicity:

**Anthracyclines (67.5%F):** Doxorubicin and epirubicin produce cardiotoxicity primarily through reactive oxygen species (ROS) generation and topoisomerase IIbeta (Top2B) inhibition in cardiomyocytes. Estrogen modulates oxidative stress responses through upregulation of antioxidant enzymes (SOD, catalase) and mitochondrial protection [7]. Paradoxically, the protective effect of estrogen in normal cardiac physiology may increase susceptibility to anthracycline-specific oxidative damage through altered mitochondrial handling of doxorubicin-iron complexes. The mean |logR| of 1.177 (the highest of any class) indicates not just more frequent female signals but stronger effect sizes.

**TKIs (47.6%F):** Tyrosine kinase inhibitors produce cardiotoxicity through off-target kinase inhibition (VEGFR, PDGFR, c-Kit) affecting cardiomyocyte survival, angiogenesis, and myocardial repair. Male predominance in TKI cardiotoxicity may reflect sex-differential expression of kinase targets in cardiac tissue and testosterone-mediated effects on VEGFR signaling [8]. The male bias in TKI cardiotoxicity is consistent with higher male rates of hypertension and cardiac remodeling.

This divergence has direct clinical implications: a female patient receiving anthracycline-based chemotherapy faces different cardiac risk dynamics than a female patient receiving TKI therapy. Class-specific rather than class-agnostic sex-adjusted monitoring is warranted.

### Cardiac AE Type Analysis

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

**Repolarization events (female-biased):** QT prolongation (61.6%F) is robustly female-biased, consistent with women's longer baseline QTc intervals and greater sensitivity to hERG channel-blocking drugs [5]. The 61.6% female proportion across 122 drugs represents a pharmacovigilance-scale confirmation of the ICH E14 recommendation for sex-stratified QT analysis.

**Structural events (near-parity):** Myocardial infarction (54.4%F), cardiac arrest (54.5%F), and atrial fibrillation (51.5%F) approach sex parity. These events involve structural cardiac pathology where sex differences in underlying disease (higher male MI rates, higher male AFib prevalence) partially offset sex-differential drug susceptibility.

### QT Prolongation Deep Dive

Among 165 QT prolongation signals (combining "Electrocardiogram QT prolonged" and "Torsade de pointes"), the overall female proportion was 62.1%. Individual drug profiles revealed extreme heterogeneity:

**Top Female-Biased QT Drugs:**
- Brexpiprazole: 91.3%F (atypical antipsychotic)
- Levothyroxine: 90.9%F (thyroid hormone)
- Topiramate: 87.2%F (antiepileptic)
- Naproxen: 86.4%F (NSAID)
- Paracetamol: 86.1%F (analgesic)

The extreme female QT bias for brexpiprazole (91.3%F) is clinically significant: this drug is increasingly prescribed for major depressive disorder, which affects women at twice the rate of men. The combination of female-predominant prescribing and female-biased QT toxicity creates a compounded risk that warrants enhanced ECG monitoring in female patients.

Levothyroxine QT prolongation (90.9%F) likely reflects thyrotoxicosis-related QT effects, with women being 5--8 times more likely to have thyroid disorders. However, the sex-stratified ROR controls for this baseline: the signal indicates that even accounting for the higher female levothyroxine use, female QT susceptibility is disproportionately elevated.

### Individual Drug Profiles

**Most Female-Biased Cardiotoxic Drugs:**
| Drug | %F | N Reports | Drug Class | Key Cardiac AEs |
|------|-----|-----------|-----------|-----------------|
| Trastuzumab | 85.9 | 2,922 | Anti-HER2 | Heart failure, LVEF decrease |
| Alendronic acid | 78.8 | 1,679 | Bisphosphonate | Atrial fibrillation |
| Methylprednisolone | 78.3 | 363 | Corticosteroid | Arrhythmia, cardiac arrest |
| Riociguat | 78.2 | 598 | sGC stimulator | Hypotension, syncope |
| Codeine | 76.9 | 294 | Opioid | QT prolongation, bradycardia |

Trastuzumab's extreme female cardiac bias (85.9%F) reflects the Reproductive Paradox: used almost exclusively for female breast cancer, the rare male patients show disproportionately lower cardiac events after sex-stratification. This is consistent with estrogen's complex role in HER2-mediated cardiac signaling.

**Most Male-Biased Cardiotoxic Drugs:**
| Drug | %F | N Reports | Drug Class | Key Cardiac AEs |
|------|-----|-----------|-----------|-----------------|
| Lopinavir/ritonavir | 23.0 | 250 | Antiviral (HIV) | QT prolongation, MI |
| Tafamidis | 24.6 | 597 | TTR stabilizer | Cardiac failure |
| Ixekizumab | 26.3 | 185 | Anti-IL-17 | MI, cardiac failure |
| Allopurinol | 28.0 | 1,180 | Xanthine oxidase inhibitor | Cardiac arrest, MI |
| Icodextrin combination | 30.2 | 263 | Peritoneal dialysis | Cardiac failure |

Tafamidis's male bias (24.6%F) is expected: transthyretin cardiac amyloidosis (ATTR-CM) predominantly affects older men. Allopurinol's male cardiac bias (28.0%F) aligns with gout's 3:1 male predominance and the cardiovascular comorbidity burden in gout patients.

### Severity Gradient in Cardiac AEs

Serious cardiac AEs showed greater male enrichment than non-serious:
- Serious cardiac AEs: 51.3%F (n = 1,892)
- Non-serious cardiac AEs: 55.8%F (n = 1,900)
- Difference: 4.5 pp (p < 0.001)

This aligns with the broader severity-sex gradient: the most severe drug outcomes are less female-biased, with fatal cardiac events approaching or crossing parity.

---

## Discussion

### Mechanism-Dependent Sex Differential Cardiotoxicity

The central finding---the anthracycline-TKI divergence of 19.9 pp---establishes that drug-induced cardiotoxicity is not uniformly sex-biased but depends on the molecular mechanism of cardiac injury. This has three implications:

First, sex-stratified cardiac monitoring protocols should be mechanism-specific. Anthracycline-treated female patients may warrant more aggressive echocardiographic surveillance for heart failure, while TKI-treated male patients may warrant enhanced blood pressure and cardiac remodeling monitoring.

Second, preclinical cardiac safety assessment should include sex as a biological variable in mechanism-relevant assays. In vitro hERG channel studies (QT risk) should use female-derived cardiomyocytes; oxidative stress assays (anthracycline risk) should include estrogen-modulated conditions.

Third, clinical trial design for cardiotoxicity endpoints should pre-specify sex-stratified analysis. The FDA's 2022 guidance on diversity in clinical trials should be extended to mandate sex-stratified cardiac safety reporting.

### QT Prolongation as a Validated Sex-Differential Signal

The consistent female predominance of QT prolongation (61.6%F across 122 drugs) represents the largest pharmacovigilance-scale validation of women's known QT susceptibility. The ICH E14 guideline recommends sex-stratified QT analysis in thorough QT studies, but implementation remains inconsistent [5]. Our finding that QT female bias persists across antipsychotics, antiarrhythmics, SSRIs, NSAIDs, and even analgesics demonstrates the universality of this sex difference and the clinical importance of compliance with E14 guidance.

### The Antipsychotic Paradox

Antipsychotics showed exactly 50.0%F cardiac signals (perfect parity) despite being among the strongest QT-prolonging drug classes. This paradox resolves when examining the within-class cardiac AE profile: QT prolongation is female-biased as expected, but metabolic cardiotoxicity (weight gain → insulin resistance → atherosclerosis) is male-biased, creating an aggregate near-parity. This underscores the inadequacy of class-level sex analysis without AE-type stratification.

### Limitations

1. FAERS voluntary reporting may undercount male cardiac events (men less likely to report non-fatal cardiac symptoms).
2. No drug exposure denominators available in FAERS; relative risk cannot be calculated.
3. Confounding by indication is inevitable: drugs used predominantly by one sex will show indication-correlated cardiac patterns.
4. Cardiac AE terms overlap between structural and functional categories; some signals contribute to multiple AE type analyses.
5. The analysis spans 2004--2025; temporal changes in prescribing patterns and reporting behavior may affect aggregate results.

---

## Conclusion

Drug-induced cardiotoxicity exhibits a structured sex-differential landscape shaped by drug mechanism and cardiac event type. The anthracycline-TKI divergence (19.9 pp) demonstrates mechanism-dependent sex effects in cardiac toxicity. QT prolongation is robustly female-biased (61.6%F, 122 drugs), validating ICH E14 guidance at pharmacovigilance scale. Cardiac AE severity shows male enrichment, consistent with the broader severity-sex gradient. These findings support sex-stratified cardiac safety monitoring, mechanism-specific risk assessment, and sex-disaggregated cardiac endpoint reporting in clinical trials and regulatory submissions.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Onakpoya IJ, Heneghan CJ, Aronson JK. Post-marketing withdrawal of 462 medicinal products because of adverse drug reactions. BMC Med. 2016;14:10.
2. Regitz-Zagrosek V, Kararigas G. Mechanistic pathways of sex differences in cardiovascular disease. Physiol Rev. 2017;97:1-37.
3. Stolfo S, et al. Sex-based differences in heart failure across the ejection fraction spectrum. Eur J Heart Fail. 2019;21:1395-1408.
4. Roden DM. Drug-induced prolongation of the QT interval. N Engl J Med. 2004;350:1013-1022.
5. Darpo B. The thorough QT/QTc study 4 years after the implementation of the ICH E14 guidance. Br J Pharmacol. 2010;159:49-57.
6. Moslehi JJ. Cardiovascular toxic effects of targeted cancer therapies. N Engl J Med. 2016;375:1457-1467.
7. Mauvais-Jarvis F, et al. Sex and gender: modifiers of health, disease, and medicine. Lancet. 2020;396:565-582.
8. Chen MH, et al. Cardiac toxicities associated with tyrosine kinase inhibitors. Clin Pharmacol Ther. 2008;84:467-473.
9. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.
10. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.

---

## Figure Legends

**Figure 1.** Drug class cardiotoxicity spectrum. Bar chart showing mean female signal proportion (x-axis) for 8 drug classes (y-axis), ordered from most male-biased (TKIs, 47.6%F) to most female-biased (anthracyclines, 67.5%F). Error bars show within-class standard deviation. The 19.9 pp span demonstrates mechanism-dependent sex effects.

**Figure 2.** Cardiac AE type profiles. Grouped bar chart comparing female proportions across 10 cardiac AE categories. Rate-related events (tachycardia, palpitations) cluster at >60%F; structural events (MI, cardiac arrest, AFib) cluster near 50%F; QT prolongation stands alone at 61.6%F.

**Figure 3.** QT prolongation drug-level analysis. Volcano plot of drug-level female proportion (x-axis) vs. significance (y-axis) for 165 QT signals. Extreme female outliers labeled (brexpiprazole 91.3%F, levothyroxine 90.9%F). Most drugs cluster in the 55--70%F range.

**Figure 4.** The anthracycline-TKI divergence. Side-by-side cardiac AE profiles for anthracyclines and TKIs showing opposite sex biases across specific cardiac event types. Illustrates mechanism-dependent sex-differential cardiotoxicity.

**Figure 5.** Severity gradient in cardiac AEs. Stacked bar chart comparing serious (51.3%F) vs. non-serious (55.8%F) cardiac signals, demonstrating male enrichment in severe cardiac outcomes.
