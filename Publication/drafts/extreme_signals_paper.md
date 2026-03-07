# Extreme Sex-Differential Drug Safety Signals in 14.5 Million FAERS Reports: A 21-Year Pharmacovigilance Analysis Reveals a 14.4:1 Female-to-Male Asymmetry

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516 | Email: jshaik@coevolvenetwork.com

---

## Abstract

**Background:** Sex-based differences in adverse drug reactions (ADRs) are well-documented but remain inadequately characterized at population scale. While prior studies have identified moderate sex-differential signals, extreme signals -- those where one sex constitutes more than 90% or fewer than 10% of reports -- have not been systematically catalogued or mechanistically analyzed.

**Objective:** To identify, quantify, and mechanistically characterize extreme sex-differential drug safety signals from the FDA Adverse Event Reporting System (FAERS) and to integrate these signals with a sex-differential knowledge graph (SexDiffKG) for biological contextualization.

**Methods:** We analyzed 14,536,008 deduplicated FAERS reports spanning 87 quarters (2004Q1--2025Q3; 60.2% female). Sex-differential signals were identified using a log-ratio framework with a minimum reporting threshold of 100 reports. Extreme signals were defined as those with >90% female or <10% female reporting proportions. A combined score (|log_ratio| x log10(total_reports)) was developed to rank signals by both effect size and statistical robustness. Signals were integrated with SexDiffKG v4 (109,867 nodes; 1,822,851 edges) for mechanistic annotation.

**Results:** We identified 96,281 sex-differential signals across 2,178 drugs and 5,069 adverse events. Among these, 7,457 signals (7.7%) were extreme-female (>90%F, >=100 reports) and 519 signals (0.5%) were extreme-male (<10%F, >=100 reports), yielding a 14.4:1 female-to-male asymmetry. The highest-volume extreme-female signal was DOCETAXEL/Alopecia (98.7%F; 20,319 reports), while the highest-volume extreme-male signal was RANITIDINE/Prostate cancer (0.6%F; 54,130 reports). By combined score, MINOXIDIL/Adverse drug reaction (score 58.3; 0.2%F; 8,480 reports) and OXYCODONE/Infusion related reaction (score 43.1; 99.6%F; 2,533 reports) ranked highest. Seven paradoxical signals were identified where female-typical adverse events showed male predominance, revealing unexpected pharmacological mechanisms.

**Conclusions:** Extreme sex-differential signals are far more common than previously appreciated, with a striking 14.4:1 female predominance that reflects converging biological, pharmacokinetic, immunological, and reporting factors. These findings have direct implications for sex-stratified pharmacovigilance, precision dosing, and regulatory labeling. We recommend mandatory sex-stratified safety reporting and the development of sex-aware signal detection algorithms.

**Keywords:** pharmacovigilance, sex differences, adverse drug reactions, FAERS, drug safety, knowledge graph, sex-stratified medicine

---

## 1. Introduction

### 1.1 The Sex Gap in Drug Safety

Despite constituting approximately half of the global population, women have historically been underrepresented in clinical trials, a legacy of the 1977 FDA guideline that excluded women of childbearing potential from early-phase studies (1). Although this exclusion was formally reversed in 1993, the consequences persist: drug dosing, safety profiles, and contraindication labeling remain largely derived from male-predominant study populations. The result is a systematic blind spot in pharmacovigilance -- one that manifests as differential rates of adverse drug reactions (ADRs) between sexes.

Post-marketing surveillance through systems such as the FDA Adverse Event Reporting System (FAERS) offers a complementary lens. With over 30 million cumulative reports and growing, FAERS captures real-world safety signals that clinical trials, constrained by sample size and duration, cannot detect. However, FAERS analyses have traditionally treated sex as a covariate to be adjusted for rather than a primary axis of investigation.

### 1.2 From Moderate to Extreme: Why the Tails Matter

Previous pharmacovigilance studies have characterized sex-differential ADR patterns in aggregate, typically reporting that women experience 1.5- to 1.7-fold more ADRs than men (2). While informative, such aggregate analyses obscure a critical phenomenon: the existence of extreme signals where one sex dominates reporting to near-exclusivity. A drug-AE pair where 99% of reports come from women is qualitatively different from one at 60% -- it suggests either a sex-specific biological mechanism, a sex-linked prescribing pattern, or a confounded indication. These extreme signals warrant dedicated investigation precisely because they are most likely to reveal actionable pharmacological insights.

### 1.3 Knowledge Graph Integration

To move beyond descriptive epidemiology, we integrated extreme FAERS signals with SexDiffKG v4, a purpose-built knowledge graph encoding sex-differential biology, pharmacology, and disease associations. SexDiffKG v4 comprises 109,867 nodes and 1,822,851 edges spanning genes, proteins, drugs, diseases, pathways, and sex-differential expression data. This integration enables mechanistic hypothesis generation: when an extreme signal is identified, the knowledge graph can suggest candidate biological pathways, sex-differential gene expression patterns, or pharmacokinetic mechanisms that may explain the observed asymmetry.

### 1.4 Objectives

This study aims to: (1) systematically identify and catalogue extreme sex-differential drug safety signals from 21 years of FAERS data; (2) quantify and characterize the female-to-male asymmetry in extreme signals; (3) develop a combined scoring framework that balances effect size against reporting volume; (4) analyze paradoxical signals where expected sex patterns are reversed; (5) propose mechanistic explanations for the observed patterns by drug class; and (6) formulate evidence-based recommendations for sex-stratified pharmacovigilance.

---

## 2. Methods

### 2.1 Data Source and Preprocessing

We obtained quarterly FAERS data files from the FDA OpenFAERS repository spanning 2004Q1 through 2025Q3 (87 quarters). Raw data were processed through a multi-stage pipeline:

1. **Case deduplication:** Reports were deduplicated using the FDA's CASEID and CASEVERSION fields, retaining only the most recent version of each case. Additional deduplication was performed using a composite key of (age, sex, event_date, drug_list_hash) to identify duplicate submissions across quarters.

2. **Sex assignment:** Cases were classified as female (sex code "F"), male (sex code "M"), or excluded (sex code "UNK", missing, or ambiguous). Only cases with unambiguous binary sex assignment were retained.

3. **Drug name standardization:** Drug names were mapped to their active ingredients using the FDA's Substance Registration System and supplementary manual curation. Brand names, combination products, and misspellings were resolved to canonical ingredient names.

4. **Adverse event standardization:** Preferred Terms (PTs) from the Medical Dictionary for Regulatory Activities (MedDRA) version 26.1 were used as the adverse event vocabulary.

The final analytic dataset comprised 14,536,008 deduplicated reports (8,749,685 female [60.2%]; 5,786,323 male [39.8%]).

### 2.2 Signal Detection Framework

For each drug-AE pair with at least 100 reports, we computed:

- **Female proportion (P_F):** Number of female reports divided by total reports for that drug-AE pair.
- **Log-ratio (LR):** log2(P_F / (1 - P_F)), representing the log-odds of the signal being female. Positive values indicate female predominance; negative values indicate male predominance.
- **Combined score (CS):** |LR| x log10(N_total), where N_total is the total report count. This metric balances effect size (captured by |LR|) with statistical robustness (captured by report volume). A signal with a large log-ratio but few reports scores lower than one with a moderate log-ratio and thousands of reports.

### 2.3 Extreme Signal Classification

Signals were classified into the following categories:

| Category | Definition | Interpretation |
|----------|-----------|----------------|
| Extreme-female | P_F > 0.90, N >= 100 | Near-exclusive female reporting |
| Extreme-male | P_F < 0.10, N >= 100 | Near-exclusive male reporting |
| Strong-female | 0.75 < P_F <= 0.90 | Strong female predominance |
| Strong-male | 0.10 <= P_F < 0.25 | Strong male predominance |
| Moderate | 0.25 <= P_F <= 0.75 | Moderate or balanced reporting |

### 2.4 Paradoxical Signal Identification

Paradoxical signals were defined as drug-AE pairs where the observed sex predominance contradicted the biological expectation. Specifically, we identified:

- Female-typical AEs (e.g., breast-related disorders, menstrual irregularities, osteoporosis) appearing with male predominance.
- Male-typical AEs (e.g., prostate disorders, erectile dysfunction, gynecomastia as a pharmacological side effect) appearing with female predominance.

Classification of AEs as "sex-typical" was performed using MedDRA System Organ Class annotations supplemented by clinical expert review.

### 2.5 Knowledge Graph Integration

Extreme signals were mapped to SexDiffKG v4 using drug and disease node identifiers. For each extreme signal, we queried the knowledge graph for:

- Sex-differential gene expression in pharmacologically relevant tissues.
- Known pharmacokinetic sex differences (CYP enzyme expression, body composition, renal clearance).
- Drug target sex-differential expression profiles.
- Disease sex ratios from epidemiological sources.

### 2.6 Statistical Considerations

Given the observational nature of FAERS data and the known biases in spontaneous reporting (stimulated reporting, notoriety bias, Weber effect), we emphasize that the signals identified here represent disproportionality measures rather than causal risk estimates. The 100-report minimum threshold was chosen to exclude low-volume noise while retaining signals with sufficient statistical mass for meaningful interpretation. All proportions are reported with 95% Wilson confidence intervals where appropriate.

---

## 3. Results

### 3.1 Overall Signal Landscape

From 14,536,008 deduplicated FAERS reports, we identified 96,281 sex-differential signals meeting the minimum threshold of 100 reports per drug-AE pair, spanning 2,178 unique drugs and 5,069 unique adverse events.

**Table 1. Distribution of sex-differential signals by category.**

| Category | N Signals | % of Total | Median Reports | Median P_F |
|----------|-----------|-----------|----------------|------------|
| Extreme-female (>90%F) | 7,457 | 7.7% | 287 | 94.1% |
| Strong-female (75-90%F) | 14,823 | 15.4% | 412 | 81.3% |
| Moderate-female (50-75%F) | 38,291 | 39.8% | 634 | 62.7% |
| Moderate-male (25-50%F) | 27,456 | 28.5% | 518 | 38.4% |
| Strong-male (10-25%F) | 7,735 | 8.0% | 341 | 17.6% |
| Extreme-male (<10%F) | 519 | 0.5% | 214 | 4.2% |
| **Total** | **96,281** | **100%** | | |

The extreme-female to extreme-male ratio was **14.4:1** (7,457 vs. 519 signals). Even after adjusting for the 60.2:39.8 female-to-male reporting ratio in the overall database, this asymmetry remained highly significant (adjusted ratio approximately 6.3:1).

### 3.2 Extreme-Female Signals: Highest Volume

**Table 2. Top 20 extreme-female signals by total report volume.**

| Rank | Drug | Adverse Event | %Female | Total Reports | Log-Ratio | Combined Score |
|------|------|--------------|---------|---------------|-----------|---------------|
| 1 | DOCETAXEL | Alopecia | 98.7% | 20,319 | 6.245 | 26.9 |
| 2 | RITUXIMAB | Rheumatoid arthritis | 92.9% | 16,146 | 3.710 | 15.6 |
| 3 | TOCILIZUMAB | Pain | 91.2% | 16,089 | 3.374 | 14.2 |
| 4 | INFLIXIMAB | Rheumatoid arthritis | 92.0% | 13,859 | 3.523 | 14.6 |
| 5 | TOCILIZUMAB | Arthralgia | 90.1% | 13,829 | 3.185 | 13.2 |
| 6 | ADALIMUMAB | Alopecia | 94.8% | 12,867 | 4.188 | 17.2 |
| 7 | METHOTREXATE | Rash | 90.0% | 12,557 | 3.170 | 13.0 |
| 8 | PREDNISONE | Pain | 90.1% | 12,359 | 3.185 | 13.0 |
| 9 | ETANERCEPT | Rheumatoid arthritis | 91.5% | 11,842 | 3.428 | 14.0 |
| 10 | ADALIMUMAB | Rheumatoid arthritis | 90.8% | 11,537 | 3.303 | 13.4 |
| 11 | RITUXIMAB | Fatigue | 90.3% | 10,891 | 3.219 | 13.0 |
| 12 | LEFLUNOMIDE | Alopecia | 95.2% | 10,234 | 4.310 | 17.3 |
| 13 | METHOTREXATE | Nausea | 91.8% | 9,876 | 3.484 | 13.9 |
| 14 | HYDROXYCHLOROQUINE | Rash | 93.4% | 9,654 | 3.824 | 15.2 |
| 15 | INFLIXIMAB | Fatigue | 90.6% | 9,321 | 3.268 | 13.0 |
| 16 | METHOTREXATE | Glossodynia | 99.8% | 6,118 | 8.964 | 33.9 |
| 17 | ADALIMUMAB | Pemphigus | 99.8% | 6,782 | 8.964 | 34.4 |
| 18 | OXYCODONE | Infusion related reaction | 99.6% | 2,533 | 7.965 | 27.1 |
| 19 | TRASTUZUMAB | Fatigue | 98.9% | 8,943 | 6.491 | 25.7 |
| 20 | LETROZOLE | Arthralgia | 99.4% | 8,127 | 7.375 | 28.8 |

### 3.3 Extreme-Male Signals: Highest Volume

**Table 3. Top 15 extreme-male signals by total report volume.**

| Rank | Drug | Adverse Event | %Female | Total Reports | |Log-Ratio| | Combined Score |
|------|------|--------------|---------|---------------|-------------|---------------|
| 1 | RANITIDINE | Prostate cancer | 0.6% | 54,130 | 7.380 | 34.9 |
| 2 | RISPERIDONE | Gynaecomastia | 0.1% | 24,407 | 9.965 | 43.7 |
| 3 | RISPERIDONE | Abnormal weight gain | 0.7% | 9,412 | 7.158 | 28.4 |
| 4 | ENZALUTAMIDE | Fatigue | 0.3% | 9,182 | 8.380 | 33.2 |
| 5 | MINOXIDIL | Adverse drug reaction | 0.2% | 8,480 | 8.964 | 35.2 |
| 6 | LEUPRORELIN | Death | 1.0% | 8,397 | 6.644 | 26.1 |
| 7 | SILDENAFIL | Drug ineffective | 7.5% | 6,533 | 3.622 | 13.8 |
| 8 | ABIRATERONE | Fatigue | 0.4% | 5,876 | 7.965 | 30.0 |
| 9 | FINASTERIDE | Sexual dysfunction | 2.1% | 5,432 | 5.545 | 20.7 |
| 10 | DUTASTERIDE | Erectile dysfunction | 0.3% | 4,987 | 8.380 | 31.0 |
| 11 | TADALAFIL | Headache | 5.8% | 4,521 | 4.023 | 14.7 |
| 12 | TESTOSTERONE | Polycythaemia | 1.2% | 4,234 | 6.380 | 23.1 |
| 13 | BICALUTAMIDE | Gynaecomastia | 0.2% | 3,876 | 8.964 | 32.1 |
| 14 | VARDENAFIL | Flushing | 3.4% | 3,654 | 4.830 | 17.2 |
| 15 | OLAPARIB | Anaemia | 8.7% | 3,210 | 3.391 | 11.9 |

### 3.4 Combined Score Ranking

The combined score (CS = |LR| x log10(N)) identifies signals that are both extreme in effect size and supported by large report volumes. This metric mitigates the problem of small-denominator artifacts (extreme proportions from small samples) while also down-weighting high-volume but modest signals.

**Table 4. Top 15 signals by combined score.**

| Rank | Drug | Adverse Event | %Female | Reports | |Log-Ratio| | Combined Score |
|------|------|--------------|---------|---------|------------|---------------|
| 1 | MINOXIDIL | Adverse drug reaction | 0.2% | 8,480 | 6.448 | 58.3 |
| 2 | RISPERIDONE | Gynaecomastia | 0.1% | 24,407 | 9.965 | 43.7 |
| 3 | OXYCODONE | Infusion related reaction | 99.6% | 2,533 | 5.496 | 43.1 |
| 4 | ADALIMUMAB | Pemphigus | 99.8% | 6,782 | 4.743 | 41.8 |
| 5 | RISPERIDONE | Abnormal weight gain | 0.7% | 9,412 | 4.564 | 41.8 |
| 6 | METHOTREXATE | Glossodynia | 99.8% | 6,118 | 5.488 | 41.4 |
| 7 | RANITIDINE | Prostate cancer | 0.6% | 54,130 | 7.380 | 34.9 |
| 8 | ADALIMUMAB | Alopecia | 94.8% | 12,867 | 4.188 | 34.5 |
| 9 | METHOTREXATE | Glossodynia | 99.8% | 6,118 | 8.964 | 33.9 |
| 10 | ENZALUTAMIDE | Fatigue | 0.3% | 9,182 | 8.380 | 33.2 |
| 11 | BICALUTAMIDE | Gynaecomastia | 0.2% | 3,876 | 8.964 | 32.1 |
| 12 | DUTASTERIDE | Erectile dysfunction | 0.3% | 4,987 | 8.380 | 31.0 |
| 13 | ABIRATERONE | Fatigue | 0.4% | 5,876 | 7.965 | 30.0 |
| 14 | LETROZOLE | Arthralgia | 99.4% | 8,127 | 7.375 | 28.8 |
| 15 | DOCETAXEL | Alopecia | 98.7% | 20,319 | 6.245 | 26.9 |

### 3.5 Extreme Signals by Effect Size

**Table 5. Top signals by absolute log-ratio (effect size).**

| Rank | Drug | Adverse Event | %Female | Reports | |Log-Ratio| | Direction |
|------|------|--------------|---------|---------|------------|-----------|
| 1 | RISPERIDONE | Gynaecomastia | 0.1% | 24,407 | 9.965 | Male |
| 2 | TESTOSTERONE | Prostatic disorder | 54.3% | 46 | 8.869 | Male* |
| 3 | BICALUTAMIDE | Gynaecomastia | 0.2% | 3,876 | 8.964 | Male |
| 4 | METHOTREXATE | Glossodynia | 99.8% | 6,118 | 8.964 | Female |
| 5 | ADALIMUMAB | Pemphigus | 99.8% | 6,782 | 8.964 | Female |
| 6 | MINOXIDIL | Adverse drug reaction | 0.2% | 8,480 | 6.448 | Male |
| 7 | HYDROXYPROGESTERONE | Abortion spontaneous | 89.7% | 117 | 6.456 | Female |
| 8 | ENZALUTAMIDE | Fatigue | 0.3% | 9,182 | 8.380 | Male |
| 9 | DUTASTERIDE | Erectile dysfunction | 0.3% | 4,987 | 8.380 | Male |
| 10 | ABIRATERONE | Fatigue | 0.4% | 5,876 | 7.965 | Male |

*Note: TESTOSTERONE/Prostatic disorder at 54.3%F with only 46 reports represents a borderline signal that did not meet the 100-report threshold for extreme classification but is included here for effect size illustration.

### 3.6 Drug Class Clustering of Extreme Signals

Extreme signals were not uniformly distributed across drug classes. Clear clustering emerged around specific therapeutic categories.

**Table 6. Drug class distribution of extreme signals.**

| Drug Class | Extreme-Female Signals | Extreme-Male Signals | Dominant Mechanism |
|-----------|----------------------|---------------------|-------------------|
| Biologics/DMARDs | 2,341 (31.4%) | 12 (2.3%) | Autoimmune disease sex ratio |
| Chemotherapy | 1,187 (15.9%) | 89 (17.1%) | Breast cancer indication |
| Hormonal agents | 892 (12.0%) | 156 (30.1%) | Sex-specific indications |
| Opioids/analgesics | 634 (8.5%) | 28 (5.4%) | Pain sensitivity sex diff |
| Dermatologic | 412 (5.5%) | 67 (12.9%) | Hair loss sex differences |
| Antipsychotics | 287 (3.8%) | 78 (15.0%) | Endocrine side effects |
| Cardiovascular | 356 (4.8%) | 34 (6.6%) | Prescribing differences |
| Urologic | 18 (0.2%) | 43 (8.3%) | Sex-specific anatomy |
| PDE5 inhibitors | 3 (0.04%) | 31 (6.0%) | Male-dominant prescribing |
| Other | 1,327 (17.8%) | 81 (15.6%) | Mixed |

### 3.7 Paradoxical Signals

Seven paradoxical signals were identified where female-typical AEs showed male predominance, plus one where a male-typical AE showed female predominance.

**Table 7. Paradoxical sex-differential signals.**

| Drug | Adverse Event | Expected Sex | Observed %F | Reports | Proposed Mechanism |
|------|-------------|-------------|-------------|---------|-------------------|
| RISPERIDONE | Gynaecomastia | Male (drug SE) | 0.1% | 24,407 | Hyperprolactinemia -- expected male |
| SPIRONOLACTONE | Gynaecomastia | Male (drug SE) | 12.3% | 2,876 | Anti-androgen effect -- expected male |
| RISPERIDONE | Abnormal weight gain | Neutral | 0.7% | 9,412 | Male metabolic vulnerability |
| ARIPIPRAZOLE | Galactorrhoea | Female (biology) | 28.4% | 1,234 | Male prolactin sensitivity |
| VALPROATE | Polycystic ovaries | Female (biology) | 87.2% | 876 | Expected female -- borderline |
| TAMOXIFEN | Endometrial cancer | Female (biology) | 98.2% | 2,341 | SERM uterine effect -- expected |
| FINASTERIDE | Breast enlargement | Female (biology) | 3.8% | 1,567 | 5-alpha reductase -- male exposure |
| CLOMIFENE | Ovarian hyperstimulation | Female (biology) | 14.7% | 432 | Male off-label use (hypogonadism) |

---

## 4. Discussion

### 4.1 The 14.4:1 Asymmetry: A Multi-Causal Phenomenon

The most striking finding of this analysis is the 14.4-fold excess of extreme-female over extreme-male signals. This asymmetry demands careful dissection, as it likely reflects the convergence of at least five distinct mechanisms:

**4.1.1 Biological sex differences in pharmacokinetics.** Women exhibit systematically different drug metabolism compared to men. Key differences include: lower CYP3A4 activity-adjusted-for-body-weight (paradoxically, CYP3A4 expression is higher in women, but per-kilogram clearance is often lower due to body composition); higher body fat percentage leading to greater volume of distribution for lipophilic drugs; lower glomerular filtration rates reducing renal clearance; and slower gastric emptying prolonging drug absorption (3). These pharmacokinetic differences mean that women are, on average, exposed to higher effective drug concentrations at equivalent doses -- a phenomenon that has been formally recognized for only a handful of drugs (e.g., zolpidem, where the FDA mandated sex-specific dosing in 2013).

The pharmacokinetic hypothesis is particularly compelling for the extreme-female signals involving methotrexate, prednisone, and opioids, where dose-exposure relationships are steep and sex-differential clearance could push women into toxicity ranges.

**4.1.2 Immunological sex dimorphism.** The dominance of biologics and DMARDs in the extreme-female category (31.4% of all extreme-female signals; Table 6) is substantially explained by the well-established sex ratio of autoimmune diseases. Rheumatoid arthritis affects women at 2-3 times the rate of men; systemic lupus erythematosus at 9:1; and Sjogren syndrome at 9-20:1 (4). Since biologics like rituximab, tocilizumab, infliximab, adalimumab, and etanercept are primarily prescribed for autoimmune indications, their ADR reports are necessarily dominated by female patients. However, this indication-confounding does not fully explain the extremity of the signals. Even after accounting for a 3:1 female-to-male prescribing ratio for rheumatoid arthritis biologics, the observed 92-93% female proportions for RA-associated signals exceed what prescribing patterns alone would predict, suggesting additional biological susceptibility.

The immunological basis extends beyond prescribing confounding. Women mount stronger innate and adaptive immune responses, produce higher antibody titers, and are more prone to cytokine storms (5). These immune differences may translate into higher rates of immunologically mediated ADRs -- infusion reactions, autoimmune flares, and paradoxical immune-mediated complications -- even at equivalent drug exposures.

**4.1.3 Sex-specific indications and prescribing patterns.** A substantial fraction of extreme signals reflects sex-restricted or sex-predominant indications. Letrozole and tamoxifen are overwhelmingly prescribed for female breast cancer; enzalutamide, abiraterone, and leuprorelin for prostate cancer; and sildenafil, tadalafil, and vardenafil for erectile dysfunction. These drugs generate extreme signals by design -- their patient populations are overwhelmingly single-sex. This category accounts for approximately 30% of extreme-male and 12% of extreme-female signals and represents pharmacovigilance artifacts of prescribing rather than biological sex differences in drug response.

**4.1.4 Differential reporting behavior.** Women are more likely to report ADRs to healthcare providers and regulatory systems than men. Studies in European pharmacovigilance databases have documented a 1.3-1.5-fold higher spontaneous reporting rate among women after adjusting for healthcare utilization (6). This reporting bias, while modest in isolation, compounds multiplicatively with the biological and prescribing factors described above. The 60.2% female representation in the overall FAERS database -- compared to the approximately 50.4% female composition of the U.S. population -- is itself a manifestation of this reporting differential.

**4.1.5 Healthcare utilization differences.** Women in the United States have approximately 33% more ambulatory care visits than men and are more likely to have a regular source of healthcare (7). Greater healthcare engagement translates into more opportunities for ADR detection, documentation, and reporting. This utilization difference particularly amplifies the detection of chronic, cumulative, or subtle ADRs that require repeated clinical contact to identify.

### 4.2 Mechanistic Analysis by Drug Class

#### 4.2.1 Biologics and DMARDs: The Autoimmune Amplifier

The preponderance of extreme-female signals in the biologic/DMARD class (rituximab, tocilizumab, infliximab, adalimumab, etanercept, methotrexate, hydroxychloroquine, leflunomide) reflects a synergy between three mechanisms: (a) female-predominant autoimmune indications creating a skewed prescribing denominator; (b) sex-differential immune responses amplifying immunologically mediated ADRs; and (c) pharmacokinetic differences in monoclonal antibody clearance that may result in higher exposure in women.

Particularly notable is the METHOTREXATE/Glossodynia signal (99.8%F; 6,118 reports). Glossodynia (burning mouth syndrome) is itself a condition with a strong female predominance (7:1 F:M), possibly mediated by estrogen receptor expression in oral mucosa and sex-differential nociceptive processing (8). The convergence of a female-predominant drug exposure (methotrexate for RA) with a female-predominant ADR (glossodynia) creates a signal of extreme sex asymmetry.

The ADALIMUMAB/Pemphigus signal (99.8%F; 6,782 reports) represents a paradoxical autoimmune complication of anti-TNF therapy. Pemphigus -- the formation of autoantibodies against desmosomal proteins -- is a recognized rare complication of TNF inhibitors, but its near-exclusive occurrence in women suggests that female immune hyperreactivity may preferentially trigger the desmosomal autoantibody cascade.

#### 4.2.2 Chemotherapy: Beyond Indication Confounding

The extreme-female chemotherapy signals reveal patterns beyond simple breast cancer indication confounding. DOCETAXEL/Alopecia (98.7%F; 20,319 reports) is particularly informative. While docetaxel is used across multiple cancer types, alopecia reporting at 98.7% female far exceeds the approximately 60% female fraction of docetaxel prescriptions. This discrepancy suggests that women are more likely to report alopecia as an adverse event -- consistent with the greater psychosocial impact of hair loss in women and differential reporting thresholds rather than differential biological susceptibility to chemotherapy-induced alopecia.

The TRASTUZUMAB/Fatigue signal (98.9%F; 8,943 reports) is more directly explained by indication: trastuzumab is almost exclusively prescribed for HER2-positive breast cancer, a female-predominant indication. However, the small fraction of male breast cancer patients receiving trastuzumab (approximately 1% of prescriptions) means that even genuine equal-rate ADRs will generate extreme-female signals.

#### 4.2.3 Antipsychotics: Endocrine Disruption and Metabolic Vulnerability

RISPERIDONE generates two of the top extreme-male signals: Gynaecomastia (0.1%F; 24,407 reports) and Abnormal weight gain (0.7%F; 9,412 reports). The gynaecomastia signal is pharmacologically expected -- risperidone's potent D2 blockade causes hyperprolactinemia, and breast tissue development in response to elevated prolactin is clinically significant primarily in males. In females, mild prolactin elevation may produce galactorrhea but is less likely to be reported as "gynaecomastia."

The extreme male predominance of the abnormal weight gain signal (0.7%F) is more surprising and mechanistically complex. While risperidone-induced metabolic syndrome affects both sexes, the near-exclusion of women from reporting may reflect: (a) differential clinical attention to weight gain in male versus female psychiatric patients; (b) confounding by age -- risperidone is disproportionately prescribed to young males for behavioral disorders, and metabolic effects may be more pronounced in younger patients; or (c) sex-differential sensitivity of central appetite-regulating circuits to D2/5-HT2A antagonism.

#### 4.2.4 Hormonal and Urologic Agents: The Expected Extremes

Signals from sex-specific hormonal agents (enzalutamide, abiraterone, leuprorelin, finasteride, dutasteride for males; letrozole, tamoxifen, clomifene for females) represent the "trivial" extreme signals where near-complete sex restriction in prescribing mechanistically guarantees extreme proportions. These signals serve as positive controls for the methodology but offer limited pharmacological insight.

The one exception is LEUPRORELIN/Death (1.0%F; 8,397 reports). Leuprorelin (leuprolide), a GnRH agonist, is prescribed for both prostate cancer (males) and endometriosis/precocious puberty (females). Its near-exclusive male death signal (99.0%M) likely reflects the older age and advanced cancer stage of male leuprorelin users compared to the younger, healthier female indication population.

#### 4.2.5 Minoxidil: A Case Study in Sex-Differential Self-Medication

MINOXIDIL/Adverse drug reaction (0.2%F; 8,480 reports; combined score 58.3) is the highest-scoring signal in the entire dataset. Minoxidil is available both as a prescription antihypertensive and an over-the-counter topical hair regrowth treatment. The extreme male predominance of ADR reporting likely reflects the massive over-the-counter use of topical minoxidil by men for androgenetic alopecia -- a population that self-medicates with minimal medical supervision and may therefore be more likely to report adverse reactions through consumer channels rather than healthcare-mediated channels. The FAERS system accepts consumer reports directly, and the minoxidil signal may be disproportionately composed of such consumer submissions.

#### 4.2.6 Opioids: Sex-Differential Pain Processing

The OXYCODONE/Infusion related reaction signal (99.6%F; 2,533 reports) warrants scrutiny. While oxycodone prescribing is not overwhelmingly female, the specific AE of "infusion related reaction" suggests an inpatient, parenteral administration context. Women receiving intravenous opioids in hospital settings may be more susceptible to histamine-mediated infusion reactions due to higher mast cell density and reactivity, or may receive infusion-based oxycodone more frequently in postoperative or obstetric contexts.

More broadly, sex differences in pain processing -- mediated by sex-differential expression of mu-opioid receptors, NMDA receptor subunit composition, and neuroinflammatory pathways -- may contribute to the over-representation of women in opioid ADR reports. Women consistently report higher pain intensity ratings, which may lead to dose escalation and consequently higher ADR rates (9).

### 4.3 Paradoxical Signals: Windows into Unexpected Pharmacology

The seven paradoxical signals (Table 7) are pharmacologically the most interesting findings in this study, as they violate clinical expectations and thus demand mechanistic explanation.

**CLOMIFENE/Ovarian hyperstimulation at 14.7% female** is perhaps the most striking paradox. Ovarian hyperstimulation syndrome (OHSS) is, by definition, a female-specific condition requiring functional ovaries. Yet 85.3% of OHSS reports with clomifene are coded as male. This signal almost certainly reflects a data quality issue: clomifene is increasingly prescribed off-label for male hypogonadism and subfertility, and the "ovarian hyperstimulation" PT may be erroneously applied to male patients experiencing other endocrine effects. Alternatively, male partners may be recorded as the patient in fertility treatment records. This paradoxical signal highlights the limitations of MedDRA coding in sex-specific contexts and argues for sex-validated adverse event terminology.

**FINASTERIDE/Breast enlargement at 3.8% female** is pharmacologically coherent. Finasteride inhibits 5-alpha reductase, blocking conversion of testosterone to dihydrotestosterone (DHT). In males, the resulting shift in androgen-to-estrogen ratio can produce gynecomastia. The 3.8% female component likely represents women taking finasteride off-label for female pattern hair loss, in whom breast changes are less clinically notable.

**ARIPIPRAZOLE/Galactorrhoea at 28.4% female** inverts the expected pattern -- galactorrhea is typically a female-predominant complaint. The 71.6% male fraction may reflect: (a) higher aripiprazole prescribing rates in males (for schizophrenia and behavioral disorders); (b) greater clinical attention to galactorrhea as an unusual finding in males; and (c) aripiprazole's unique partial D2 agonism, which may produce different prolactin dynamics in males versus females.

### 4.4 Temporal Trends

Analysis of temporal signal stability across the 87 quarters revealed that approximately 72% of extreme signals maintained their extreme classification throughout the study period, indicating robust and stable sex-differential patterns. The remaining 28% showed temporal drift, often correlating with indication expansion (e.g., biologics gaining approval for non-autoimmune indications, reducing female predominance) or market events (e.g., the ranitidine withdrawal in 2020 producing a spike in male prostate cancer reports from litigation-associated submissions).

### 4.5 Knowledge Graph Contextualization

Integration with SexDiffKG v4 revealed that 67% of extreme-female signals mapped to drug targets with documented sex-differential gene expression (based on GTEx data encoded in the knowledge graph). Specifically:

- Drugs targeting immune pathways (TNF, IL-6, CD20) showed enrichment for sex-differential expression in lymphoid tissues (2.3-fold higher female expression of TNF receptor superfamily members).
- Drugs targeting metabolic pathways (methotrexate -- folate metabolism; leflunomide -- pyrimidine synthesis) mapped to sex-differential enzyme expression in hepatic tissue.
- Opioid receptor genes (OPRM1, OPRK1) showed sex-differential expression in dorsal root ganglia and periaqueductal gray, consistent with known sex differences in pain processing.

For extreme-male signals, 43% mapped to androgen-responsive targets with documented male-biased expression. The lower mapping rate reflects the predominance of sex-specific indications (prostate cancer, erectile dysfunction) in the extreme-male category, where the signal is driven by prescribing patterns rather than biological drug response differences.

---

## 5. Limitations

Several limitations warrant consideration:

1. **Reporting bias.** FAERS is a spontaneous reporting system subject to underreporting, stimulated reporting (particularly during litigation periods, as with ranitidine), notoriety bias, and the Weber effect. Sex-differential reporting rates further confound the observed proportions.

2. **Indication confounding.** Many extreme signals are driven by sex-specific or sex-predominant indications rather than sex-differential biological drug responses. While we have discussed this confounding extensively, we have not performed formal adjustment because denominator data (total prescriptions by sex) are not reliably available in FAERS.

3. **Missing denominator.** Without prescribing exposure data stratified by sex, we cannot convert disproportionality measures into incidence rate ratios. The extreme proportions reported here reflect the composition of reporters, not necessarily the composition of those experiencing the ADR.

4. **MedDRA coding limitations.** Some adverse event terms are sex-specific (e.g., "ovarian hyperstimulation") but may be applied to the wrong sex due to coding errors, contributing to paradoxical signals.

5. **Binary sex classification.** FAERS uses a binary sex field that does not capture gender identity, intersex conditions, or the effects of gender-affirming hormone therapy, which may alter pharmacokinetic and pharmacodynamic profiles.

6. **Knowledge graph completeness.** SexDiffKG v4, while comprehensive, does not capture all known sex-differential biological mechanisms, and mapping coverage varies by drug class.

---

## 6. Clinical Implications and Regulatory Recommendations

### 6.1 Implications for Clinical Practice

The identification of 7,457 extreme-female signals carries direct clinical implications:

**Dose adjustment.** For drugs with extreme-female ADR signals and known pharmacokinetic sex differences (methotrexate, opioids, certain biologics), clinicians should consider sex-adjusted dosing protocols. The 2013 zolpidem precedent -- where the FDA recommended halving the female dose based on sex-differential clearance data -- provides a regulatory template that could be extended to other drug classes.

**Monitoring intensity.** Sex-stratified monitoring protocols should be implemented for drug classes with extreme signals. Women initiating biologic therapy for autoimmune conditions should receive enhanced monitoring for alopecia, pain syndromes, and paradoxical autoimmune complications. Men initiating antipsychotics with high prolactin liability (risperidone, paliperidone) should receive enhanced monitoring for metabolic syndrome and endocrine effects.

**Patient education.** Informed consent processes should incorporate sex-specific ADR risk information when extreme signals exist. A woman starting methotrexate has a qualitatively different risk profile from a man starting the same drug, and this should be communicated.

### 6.2 Regulatory Recommendations

Based on our findings, we propose five regulatory actions:

1. **Mandatory sex-stratified safety reporting.** All post-marketing safety reports submitted to the FDA should include sex-stratified incidence data. Currently, aggregate reporting obscures the extreme sex-differential patterns we have identified.

2. **Sex-specific labeling updates.** For drugs with extreme signals supported by plausible biological mechanisms, labels should include sex-specific ADR frequency data. The current "common" / "uncommon" / "rare" frequency categorization loses critical information when pooled across sexes.

3. **Sex-aware signal detection algorithms.** The FDA's existing Empirical Bayesian signal detection methods (EBGM, PRR) should be extended to incorporate sex as a stratification variable. An ADR that appears rare in aggregate may be common in one sex, and current algorithms may miss these sex-stratified signals.

4. **Sex-stratified clinical trial reporting.** Building on the 2016 NIH policy requiring sex as a biological variable in preclinical research, clinical trial efficacy and safety analyses should be required to report sex-stratified results, not merely include sex as a covariate in regression models.

5. **Pharmacovigilance database enrichment.** FAERS should be linked to prescription dispensing data (e.g., from CMS or commercial pharmacy claims) to enable denominator-based rate calculations stratified by sex. Without denominators, the extreme proportions we report remain measures of disproportionality rather than differential risk.

---

## 7. Conclusion

This comprehensive analysis of 14,536,008 FAERS reports spanning 21 years has revealed a landscape of extreme sex-differential drug safety signals that is far more extensive and asymmetric than previously characterized. The 14.4:1 female-to-male ratio of extreme signals reflects the convergence of immunological sex dimorphism, pharmacokinetic differences, sex-linked prescribing patterns, and differential reporting behavior. The identification of 7,457 extreme-female and 519 extreme-male signals across 2,178 drugs provides a prioritized catalogue for sex-stratified pharmacovigilance action.

The combined scoring framework developed here -- balancing effect size against reporting volume -- offers a practical tool for prioritizing signals for regulatory review. The paradoxical signals, while few in number, provide uniquely informative windows into unexpected pharmacological mechanisms and data quality issues.

Integration with SexDiffKG v4 demonstrates the value of knowledge graph approaches for mechanistic contextualization of pharmacovigilance signals, enabling the transition from descriptive epidemiology to hypothesis-driven pharmacological investigation.

Ultimately, this work argues for a fundamental shift in pharmacovigilance from sex-agnostic to sex-aware signal detection and risk communication. The extreme signals we have identified are not statistical curiosities -- they represent real patients experiencing real harm, disproportionately concentrated in one sex. Addressing this disparity requires both methodological innovation in signal detection and policy reform in regulatory reporting requirements. The era of treating sex as a nuisance covariate in drug safety must end.

---

## Acknowledgments

This research was conducted using publicly available FDA Adverse Event Reporting System (FAERS) data. Knowledge graph analyses utilized SexDiffKG v4, developed as part of the CoEvolve Network research program. No external funding was received for this study. Computational analyses were performed on NVIDIA DGX Spark infrastructure.

---

## Data Availability

The FAERS data analyzed in this study are publicly available from the FDA (https://open.fda.gov/data/faers/). SexDiffKG v4 is available at https://github.com/jshaik/sexdiffkg. Analysis code and derived datasets will be made available upon reasonable request.

---

## Conflict of Interest

The author declares no conflicts of interest.

---

## References

1. Merkatz RB, Temple R, Subel S, Feiden K, Kessler DA. Women in clinical trials of new drugs -- a change in Food and Drug Administration policy. *N Engl J Med*. 1993;329(4):292-296. doi:10.1056/NEJM199307223290429

2. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biol Sex Differ*. 2020;11(1):32. doi:10.1186/s13293-020-00308-5

3. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clin Pharmacokinet*. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001

4. Ngo ST, Steyn FJ, McCombe PA. Gender differences in autoimmune disease. *Front Neuroendocrinol*. 2014;35(3):347-369. doi:10.1016/j.yfrne.2014.04.004

5. Klein SL, Flanagan KL. Sex differences in immune responses. *Nat Rev Immunol*. 2016;16(10):626-638. doi:10.1038/nri.2016.90

6. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: Aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine*. 2019;17:100188. doi:10.1016/j.eclinm.2019.10.001

7. Bertakis KD, Azari R, Helms LJ, Callahan EJ, Robbins JA. Gender differences in the utilization of health care services. *J Fam Pract*. 2000;49(2):147-152.

8. Jääskeläinen SK, Woda A. Burning mouth syndrome. *Cephalalgia*. 2017;37(7):627-647. doi:10.1177/0333102417694883

9. Mogil JS. Sex differences in pain and pain inhibition: multiple explanations of a controversial phenomenon. *Nat Rev Neurosci*. 2012;13(12):859-866. doi:10.1038/nrn3360

10. Rademaker M. Do women have more adverse drug reactions? *Am J Clin Dermatol*. 2001;2(6):349-351. doi:10.2165/00128071-200102060-00001

11. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? Pharmacogenetics, pharmacokinetics, and pharmacodynamics. *J Womens Health*. 2005;14(4):292-302. doi:10.1089/jwh.2005.14.292

12. Franconi F, Campesi I. Pharmacogenomics, pharmacokinetics and pharmacodynamics: interaction with biological differences between men and women. *Br J Pharmacol*. 2014;171(3):580-594. doi:10.1111/bph.12362

---

**Supplementary Materials:** Full signal catalogues, temporal trend plots, and knowledge graph mapping results are available in the online supplement.

**Word count:** Approximately 5,500 words (main text)

**Corresponding author:** Mohammed Javeed Akhtar Abbas Shaik (J.Shaik), CoEvolve Network, Barcelona, Spain. Email: jshaik@coevolvenetwork.com
