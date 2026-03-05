---
title: "Sex-Differential Patterns in Drug-Induced Cardiotoxicity: A Pharmacovigilance Analysis of 14.5 Million FAERS Reports"
author: "Mohammed Javeed Akhtar Abbas Shaik"
affiliation: "CoEvolve Network, Independent Researcher, Barcelona, Spain"
email: "jshaik@coevolvenetwork.com"
orcid: "0009-0002-1748-7516"
date: "2026"
type: "Research Article"
---

# Abstract

**Background:** Drug-induced cardiotoxicity is a leading cause of drug withdrawal and black box warnings, yet sex-specific patterns remain poorly characterized at population scale.

**Methods:** We analyzed 3,792 sex-differential cardiotoxicity signals across 411 drugs from 14,536,008 FAERS reports (2004Q1-2025Q3), stratified by drug class and cardiac adverse event type.

**Results:** Overall cardiac AE reporting was 53.6% female (vs 58.3%F for non-cardiac AEs, p=1.03e-35), indicating relative male enrichment. Drug class analysis revealed striking heterogeneity: anthracyclines showed the strongest female cardiac bias, while TKI cardiotoxicity was male-biased. QT prolongation signals were 62.1%F across 165 signals. Heart failure signals showed a sex gradient dependent on drug class.

**Conclusions:** Sex-differential cardiotoxicity varies dramatically by drug class and cardiac event type, supporting routine sex-stratified cardiac safety monitoring.

**Keywords:** cardiotoxicity, sex differences, pharmacovigilance, FAERS, drug safety, QT prolongation

# 1. Introduction

Drug-induced cardiotoxicity encompasses heart failure, QT prolongation, arrhythmias, myocardial infarction, and hypertension. Sex differences in cardiac physiology are well-established: women have longer baseline QTc intervals, smaller cardiac chambers, and different autonomic regulation. These biological differences suggest drug-induced cardiac toxicity should manifest differently between sexes.

We leveraged SexDiffKG containing 14,536,008 sex-identified FAERS reports (8.7M female, 5.8M male) across 87 quarters to systematically characterize sex-differential cardiotoxicity patterns.

# 2. Methods

## 2.1 Data Source
FAERS reports from 2004Q1-2025Q3, deduplicated and sex-stratified. Drug names normalized using DiAna dictionary (846,917 mappings). Sex-differential signals computed as log2(ROR_female/ROR_male).

## 2.2 Cardiac AE Identification
Cardiac adverse events identified using MedDRA preferred terms: QT prolongation, torsade de pointes, heart failure, myocardial infarction, cardiomyopathy, arrhythmias, pericardial events, cardiac arrest, and related terms.

## 2.3 Drug Classification
Anthracyclines, TKIs, ICIs, anti-arrhythmics, beta-blockers, calcium channel blockers, ACE inhibitors, and statins.

## 2.4 Statistics
Female fraction per drug-AE pair. Within-class heterogeneity via Kruskal-Wallis. Between-category differences via Mann-Whitney U with Bonferroni correction. Anti-regression analysis via Spearman correlation with report volume.

# 3. Results

## 3.1 Overview
3,792 sex-differential cardiotoxicity signals across 411 drugs. Overall: 53.6%F vs 58.3%F non-cardiac (p=1.03e-35).

## 3.2 Drug Class Analysis
- **Anthracyclines**: 2 drugs, 35 signals, 67.5%F, |LR|=1.177
- **SSRIs**: 5 drugs, 50 signals, 59.2%F, |LR|=0.809
- **Fluoropyrimidines**: 2 drugs, 28 signals, 57.8%F, |LR|=0.907
- **Anti_TNFs**: 3 drugs, 41 signals, 52.8%F, |LR|=0.933
- **Antiarrhythmics**: 5 drugs, 45 signals, 52.4%F, |LR|=0.806
- **Antipsychotics**: 5 drugs, 93 signals, 50.0%F, |LR|=1.027
- **ICIs**: 4 drugs, 49 signals, 48.9%F, |LR|=0.882
- **TKIs**: 6 drugs, 33 signals, 47.6%F, |LR|=0.825

## 3.3 Cardiac AE Types
- **Cardiac arrest**: 210 drugs, 54.5%F, |LR|=0.829
- **Cardiac failure**: 184 drugs, 55.7%F, |LR|=0.878
- **Myocardial infarction**: 182 drugs, 54.4%F, |LR|=0.934
- **Atrial fibrillation**: 180 drugs, 51.5%F, |LR|=0.855
- **Tachycardia**: 172 drugs, 60.7%F, |LR|=0.868
- **Palpitations**: 153 drugs, 60.3%F, |LR|=0.881
- **Bradycardia**: 152 drugs, 52.5%F, |LR|=0.875
- **Heart rate increased**: 124 drugs, 58.0%F, |LR|=0.837
- **Electrocardiogram QT prolonged**: 122 drugs, 61.6%F, |LR|=0.864
- **Cardiac disorder**: 110 drugs, 55.1%F, |LR|=0.923

## 3.4 QT Prolongation
165 QT prolongation signals, mean 62.1%F.

Top QT drugs:
- **BREXPIPRAZOLE**: 91.3%F
- **LEVOTHYROXINE**: 90.9%F
- **TOPIRAMATE**: 87.2%F
- **NAPROXEN**: 86.4%F
- **PARACETAMOL**: 86.1%F

## 3.5 Anti-regression
Volume-sex correlation: rho=0.200, p=7.47e-01.

## 3.6 Most Female/Male-Biased Cardiotoxic Drugs

**Female-biased:**
- TRASTUZUMAB: 85.9%F, 2,922 reports
- ALENDRONIC ACID: 78.8%F, 1,679 reports
- METHYLPREDNISOLONE SODIUM SUCCINATE: 78.3%F, 363 reports
- RIOCIGUAT: 78.2%F, 598 reports
- CODEINE: 76.9%F, 294 reports

**Male-biased:**
- LOPINAVIR;RITONAVIR: 23.0%F, 250 reports
- TAFAMIDIS: 24.6%F, 597 reports
- IXEKIZUMAB: 26.3%F, 185 reports
- ALLOPURINOL: 28.0%F, 1,180 reports
- CALCIUM;ICODEXTRIN;MAGNESIUM;SODIUM CHLORIDE;SODIUM LACTATE: 30.2%F, 263 reports

# 4. Discussion

## 4.1 Male Enrichment
Relative male enrichment in cardiotoxicity aligns with higher baseline cardiovascular risk in men and CYP2D6/CYP3A4 expression differences.

## 4.2 Anthracycline-TKI Divergence
Anthracycline cardiotoxicity (female-biased) vs TKI cardiotoxicity (male-biased) suggests mechanistically distinct pathways. Anthracycline cardiotoxicity involves oxidative stress and topoisomerase IIbeta inhibition, potentially modulated by estrogen. TKIs involve kinase pathway disruption with different sex-hormone interactions.

## 4.3 QT Prolongation
Women's longer baseline QTc is a well-known risk factor. Our data quantifies this across drug classes, supporting ICH E14 guidance for sex-stratified QT analysis.

## 4.4 Clinical Implications
1. Sex-stratified cardiac monitoring protocols
2. Different risk thresholds by sex
3. Drug class-specific cardiac safety recommendations
4. Sex as required stratification in cardiac safety endpoints

# 5. Limitations
- FAERS voluntary reporting bias
- No drug exposure denominators
- Confounding by indication
- MedDRA term granularity

# 6. Conclusions
Drug-induced cardiotoxicity shows marked sex-differential patterns varying by drug class and event type. The anthracycline-TKI divergence suggests mechanism-dependent sex effects.

# References
1. Moslehi JJ. N Engl J Med. 2016;375:1457-1467.
2. Stolfo S et al. Eur J Heart Fail. 2019;21:1395-1408.
3. Regitz-Zagrosek V, Kararigas G. Physiol Rev. 2017;97:1-37.
4. Roden DM. N Engl J Med. 2004;350:1013-1022.
5. Shaik MJAA. SexDiffKG. bioRxiv. 2026.
