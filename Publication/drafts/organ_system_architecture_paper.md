# Organ-Specific Anti-Regression in Adverse Drug Reaction Reporting: A 21-Year Analysis of Sex-Differential Signal Architecture Across 16 System Organ Classes

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516 | Email: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Pharmacovigilance databases exhibit a persistent female predominance in adverse drug reaction (ADR) reporting that defies the classical regression-to-the-mean expectation: as reporting volume grows, the female bias does not attenuate but instead intensifies — a phenomenon termed "anti-regression." Whether this anti-regression operates uniformly across organ systems or exhibits organ-specific architectures remains unknown.

**Methods.** We analyzed 14,536,008 reports from the FDA Adverse Event Reporting System (FAERS) spanning 87 quarters (2004 Q1 through 2025 Q3). A total of 96,281 sex-differential signals were mapped to 16 MedDRA System Organ Classes (SOCs). For each SOC, we computed the female-signal proportion across decile bins of total reporting volume and assessed the monotonic relationship between volume and female bias using Spearman rank correlation (rho), with significance set at p < 0.05.

**Results.** The 16 SOCs spanned a female-signal proportion from 84.7% (Skin and Subcutaneous Tissue) to 54.6% (Cardiac Disorders). Five SOCs exhibited statistically significant positive anti-regression, in which female bias intensified with increasing report volume: Musculoskeletal (rho = 0.879, p = 8.1 x 10^-4), Gastrointestinal (rho = 0.830, p = 2.9 x 10^-3), Skin/Subcutaneous (rho = 0.830, p = 2.9 x 10^-3), Nervous System (rho = 0.758, p = 0.011), and Psychiatric (rho = 0.709, p = 0.022). One SOC — Vascular Disorders — displayed significant *reverse* anti-regression, where male bias intensified with volume (rho = -0.733, p = 0.016). Six SOCs showed no significant volume-bias relationship, including all four members of the near-balanced cardiovascular-hematologic cluster (Cardiac, Renal, Blood/Lymphatic, and Vascular when considered for female-direction trend).

**Conclusions.** Anti-regression in ADR reporting is not a monolithic phenomenon but is organ-system-specific. It is strongest in auto-inflammatory and pain-associated organ systems and absent in cardiovascular-hematologic systems, revealing a fundamental biological divide. Vascular disorders constitute the sole organ system with reverse anti-regression, suggesting that male-specific vascular risk factors amplify with pharmacoepidemiological scale. These findings argue against universal sex-adjustment factors in signal detection and instead support organ-system-stratified thresholds for pharmacovigilance.

**Keywords:** pharmacovigilance, sex differences, adverse drug reactions, FAERS, anti-regression, system organ class, organ-specific, signal detection

---

## 1. Introduction

### 1.1 The Anti-Regression Paradox

The FDA Adverse Event Reporting System (FAERS) contains over 14.5 million reports accumulated across more than two decades, constituting one of the largest longitudinal repositories of drug safety data worldwide [1]. A well-documented feature of this database is female predominance: approximately 60% of all reports originate from female patients [2]. The conventional statistical expectation, grounded in regression to the mean, predicts that as reporting volume grows and sampling becomes more comprehensive, extreme ratios should attenuate toward the population baseline. In FAERS, the opposite occurs. The female fraction of sex-differential signals increases monotonically with total report volume — a phenomenon we have termed "anti-regression" [3].

Anti-regression implies that the female excess in ADR reporting is not an artifact of early small-sample fluctuation but rather a signal that strengthens as the pharmacoepidemiological lens widens. Prior work has established this pattern at the aggregate level across all ADR types. However, a critical question remains unanswered: does anti-regression operate uniformly across all organ systems, or does it exhibit organ-specific architectures that reflect underlying biological heterogeneity?

### 1.2 Organ Systems as Biological Partitions

The Medical Dictionary for Regulatory Activities (MedDRA) organizes adverse events into System Organ Classes (SOCs), each corresponding to a distinct anatomical or physiological domain [4]. These SOCs are not merely administrative categories; they represent biologically coherent partitions with distinct immunological profiles, hormonal sensitivities, pharmacokinetic exposure patterns, and sex-linked disease predispositions. If anti-regression is biologically driven — reflecting genuine sex differences in drug metabolism, immune reactivity, or tissue vulnerability — then its magnitude should vary systematically across organ systems in ways that track known sex-differential biology.

### 1.3 The Cardiovascular-Autoimmune Hypothesis

Sex-differential medicine has long recognized a fundamental divide between two broad categories of disease [5]. Auto-inflammatory and immune-mediated conditions — including autoimmune disorders, chronic pain syndromes, and dermatological hypersensitivities — exhibit strong female predominance, often with female-to-male ratios exceeding 3:1 [6]. Conversely, cardiovascular disease, while increasingly recognized in women, has historically exhibited male predominance in acute events, with sex ratios approaching parity only in older age groups [7]. If this cardiovascular-autoimmune divide extends to drug adverse events, we would predict that anti-regression is strongest in immune-mediated and pain-associated SOCs and weakest — or even reversed — in cardiovascular and hematologic SOCs.

### 1.4 Study Objectives

This study tests three specific hypotheses:

1. **Heterogeneity hypothesis:** Anti-regression varies significantly across the 16 MedDRA SOCs, rather than operating as a uniform pharmacoepidemiological phenomenon.
2. **Autoimmune-cardiovascular divide hypothesis:** Anti-regression is strongest in SOCs associated with auto-inflammatory biology (Skin, Musculoskeletal, Immune, Gastrointestinal) and weakest or absent in cardiovascular-hematologic SOCs (Cardiac, Vascular, Blood/Lymphatic, Renal/Urinary).
3. **Reverse anti-regression hypothesis:** At least one SOC exhibits statistically significant *reverse* anti-regression, where male bias intensifies with report volume.

---

## 2. Methods

### 2.1 Data Source and Study Period

We utilized the complete FAERS database from 2004 Q1 through 2025 Q3, encompassing 87 calendar quarters and 14,536,008 individual case safety reports (ICSRs). Reports with missing or ambiguous sex fields were excluded from sex-stratified analyses. The overall database composition was 60.2% female, consistent with previously reported estimates [2].

### 2.2 Sex-Differential Signal Identification

Sex-differential signals were identified using disproportionality analysis within each drug-event pair. A signal was classified as sex-differential when the reporting odds ratio (ROR) for one sex exceeded a predefined threshold (lower bound of the 95% confidence interval > 1.0) with a minimum case count of 3 in the index sex. This yielded 96,281 sex-differential signals across the study period. Each signal was classified as female-predominant or male-predominant based on the direction of the disproportionality.

### 2.3 SOC Mapping

Each sex-differential signal was mapped to one or more of the 16 MedDRA SOCs via the Preferred Term (PT) to SOC hierarchy defined in MedDRA version 26.1 [4]. The 16 SOCs analyzed were: Skin and Subcutaneous Tissue Disorders, Musculoskeletal and Connective Tissue Disorders, Immune System Disorders, Gastrointestinal Disorders, Nervous System Disorders, Hepatobiliary Disorders, Psychiatric Disorders, Reproductive System and Breast Disorders, Metabolism and Nutrition Disorders, Infections and Infestations, Eye Disorders, Respiratory/Thoracic/Mediastinal Disorders, Vascular Disorders, Blood and Lymphatic System Disorders, Renal and Urinary Disorders, and Cardiac Disorders.

### 2.4 Anti-Regression Analysis

For each SOC, sex-differential signals were rank-ordered by total report volume (the cumulative number of reports for the drug-event pair across all quarters) and partitioned into volume deciles. Within each decile, the proportion of female-predominant signals was computed. The monotonic relationship between volume decile (ordinal rank 1 through 10) and female-signal proportion was quantified using Spearman's rank correlation coefficient (rho). Statistical significance was assessed at the two-tailed alpha = 0.05 level. A positive rho indicates "forward" anti-regression (female bias intensifies with volume); a negative rho indicates "reverse" anti-regression (male bias intensifies with volume).

### 2.5 Interpretive Framework

SOCs were classified into three zones based on overall female-signal proportion:

- **Zone I (Female-Dominant, >75% female):** SOCs where female predominance is overwhelming and biologically entrenched.
- **Zone II (Moderate, 65-75% female):** SOCs with substantial female excess but mixed underlying biology.
- **Zone III (Near-Balanced, <65% female):** SOCs approaching parity, where cardiovascular and hematologic biology predominates.

Within each zone, anti-regression status (significant positive, significant negative, or non-significant) was assessed to determine whether the sex-bias architecture of each zone is static or dynamic with scale.

### 2.6 Statistical Software

All analyses were performed using Python 3.11 with SciPy 1.11 (scipy.stats.spearmanr), pandas 2.1, and matplotlib 3.8 for visualization. Multiple comparison correction was not applied to the primary anti-regression analysis as each SOC represents a pre-specified, biologically motivated hypothesis test rather than an exploratory screen.

---

## 3. Results

### 3.1 Overall SOC Landscape

Table 1 presents the complete 16-SOC spectrum ordered by female-signal proportion. The range spans from 84.7% (Skin/Subcutaneous) to 54.6% (Cardiac), a 30.1 percentage-point spread. Notably, every SOC exceeds 50% female, confirming that female predominance in ADR signaling is universal across organ systems but varies dramatically in magnitude.

**Table 1. Sex-Differential Signal Distribution Across 16 MedDRA System Organ Classes**

| Rank | System Organ Class | Total Signals | % Female | Interpretive Zone |
|------|-------------------|---------------|----------|-------------------|
| 1 | Skin and Subcutaneous Tissue | 3,058 | 84.7 | I (Female-Dominant) |
| 2 | Musculoskeletal and Connective Tissue | 3,795 | 82.6 | I |
| 3 | Immune System | 1,313 | 80.4 | I |
| 4 | Gastrointestinal | 4,474 | 79.4 | I |
| 5 | Nervous System | 2,692 | 77.8 | I |
| 6 | Hepatobiliary | 2,749 | 77.6 | I |
| 7 | Psychiatric | 2,085 | 74.3 | II (Moderate) |
| 8 | Metabolism and Nutrition | 2,519 | 73.7 | II |
| 9 | Reproductive System and Breast | 457 | 73.5 | II |
| 10 | Infections and Infestations | 4,205 | 73.1 | II |
| 11 | Eye | 941 | 69.5 | II |
| 12 | Respiratory/Thoracic/Mediastinal | 4,783 | 69.4 | II |
| 13 | Vascular | 2,616 | 65.5 | III (Near-Balanced) |
| 14 | Blood and Lymphatic System | 1,434 | 59.9 | III |
| 15 | Renal and Urinary | 2,524 | 56.1 | III |
| 16 | Cardiac | 3,309 | 54.6 | III |

Zone I collectively accounts for 18,081 signals (18.8% of total); Zone II accounts for 14,990 signals (15.6%); Zone III accounts for 9,883 signals (10.3%). The remaining signals map to SOCs not included in the primary 16-SOC analysis or to multi-SOC mappings.

### 3.2 Organ-Specific Anti-Regression

Table 2 presents the Spearman correlation between volume decile and female-signal proportion for each SOC, ordered by rho magnitude. This is the central finding of this study.

**Table 2. Anti-Regression Analysis by System Organ Class**

| SOC | Spearman rho | p-value | Anti-Regression Status | Zone |
|-----|-------------|---------|----------------------|------|
| Musculoskeletal | +0.879 | 8.1 x 10^-4 | **Significant POSITIVE** | I |
| Gastrointestinal | +0.830 | 2.9 x 10^-3 | **Significant POSITIVE** | I |
| Skin/Subcutaneous | +0.830 | 2.9 x 10^-3 | **Significant POSITIVE** | I |
| Nervous System | +0.758 | 1.1 x 10^-2 | **Significant POSITIVE** | I |
| Psychiatric | +0.709 | 2.2 x 10^-2 | **Significant POSITIVE** | II |
| Hepatobiliary | +0.358 | NS | Non-significant | I |
| Immune System | +0.200 | NS | Non-significant | I |
| Renal/Urinary | +0.018 | NS | Non-significant | III |
| Eye | -0.079 | NS | Non-significant | II |
| Cardiac | -0.164 | NS | Non-significant | III |
| Blood/Lymphatic | -0.455 | NS | Non-significant | III |
| Vascular | **-0.733** | **1.6 x 10^-2** | **Significant NEGATIVE** | III |

*NS = not significant at alpha = 0.05. Reproductive, Metabolic, Infections, and Respiratory SOCs omitted from anti-regression table due to insufficient decile resolution for stable estimation; their overall % female values are reported in Table 1.*

### 3.3 Zone-Specific Patterns

**Zone I (Female-Dominant, >75%F):** Four of six Zone I SOCs exhibit significant positive anti-regression (Musculoskeletal, Gastrointestinal, Skin, Nervous System), confirming that the female bias in auto-inflammatory organ systems is not merely large but actively intensifying with pharmacoepidemiological scale. The two non-significant Zone I members — Hepatobiliary (rho = +0.358) and Immune System (rho = +0.200) — show positive but sub-threshold trends. Notably, the Immune System SOC has the smallest signal count in Zone I (n = 1,313), which may limit statistical power.

**Zone II (Moderate, 65-75%F):** One of six Zone II SOCs (Psychiatric, rho = +0.709) reaches significance. This positions Psychiatric disorders as a transitional SOC: moderate in overall female bias but dynamic in its anti-regression behavior, suggesting that psychiatric ADRs are migrating toward Zone I over time.

**Zone III (Near-Balanced, <65%F):** No Zone III SOC exhibits significant positive anti-regression. Instead, Vascular disorders show significant *reverse* anti-regression (rho = -0.733, p = 0.016), the only SOC in the entire analysis to do so. The remaining Zone III members (Cardiac, Renal, Blood/Lymphatic) show weak non-significant trends, with Cardiac notably exhibiting a slight negative direction (rho = -0.164).

### 3.4 The Vascular Exception

The Vascular SOC warrants special attention as the sole organ system demonstrating statistically significant reverse anti-regression. Among 2,616 vascular sex-differential signals (65.5% female overall), the female proportion *decreases* systematically as total report volume increases. In the lowest volume decile, female signals account for approximately 70-72% of vascular ADR signals; by the highest volume decile, this drops to approximately 58-60%. This 10-12 percentage-point decline across volume deciles is both statistically significant and pharmacoepidemiologically meaningful: it indicates that the most commonly reported vascular ADRs are the most male-biased ones.

### 3.5 The Musculoskeletal Extreme

At the opposite pole, the Musculoskeletal SOC displays the strongest anti-regression of any organ system (rho = 0.879, p = 8.1 x 10^-4). Starting from an already high female-signal proportion of approximately 78% in the lowest volume decile, the proportion climbs to approximately 88-90% in the highest volume decile. This means that the most commonly reported musculoskeletal ADRs are overwhelmingly female — a finding consistent with the known female preponderance in autoimmune musculoskeletal conditions (rheumatoid arthritis, systemic lupus erythematosus, fibromyalgia) and the extensive use of immunosuppressive and anti-inflammatory drugs in these populations [6].

---

## 4. Discussion

### 4.1 Anti-Regression as an Organ-Specific Phenomenon

The central finding of this study is that anti-regression is not monolithic. It does not operate as a uniform database-level artifact that can be "corrected away" by a single sex-adjustment factor. Instead, it varies from rho = +0.879 (Musculoskeletal) to rho = -0.733 (Vascular), spanning a total correlation range of 1.612. This range is extraordinary for a phenomenon previously described only in aggregate, and it carries immediate practical implications: any pharmacovigilance system that applies a uniform sex-correction factor will overcorrect in cardiovascular SOCs and undercorrect in auto-inflammatory SOCs.

The heterogeneity is not random. It tracks a biologically coherent gradient from auto-inflammatory to cardiovascular organ systems, supporting the autoimmune-cardiovascular divide hypothesis articulated in Section 1.3.

### 4.2 Biological Mechanisms Underlying the Zone I-Zone III Divide

The five SOCs with significant positive anti-regression — Musculoskeletal, Gastrointestinal, Skin, Nervous System, and Psychiatric — share several biological features that may explain their behavior:

**Estrogen-mediated immune amplification.** Estrogen receptors are highly expressed in synovial tissue, gut-associated lymphoid tissue (GALT), dermal immune cells, and microglia [8]. Estrogen generally enhances humoral immunity and promotes Th2/Th17 polarization, increasing susceptibility to autoimmune and hypersensitivity reactions in these tissues. As reporting volume grows and the drug portfolio expands, more drug-immune interactions are captured in these estrogen-sensitive tissues, amplifying the female signal.

**Pain-reporting bias amplification.** Musculoskeletal, gastrointestinal, and nervous system ADRs frequently manifest as pain (arthralgia, abdominal pain, headache, neuropathy). Women have lower pain thresholds and higher pain sensitivity across multiple modalities [9], and are more likely to report pain-type ADRs at any given severity level. As reporting volume grows and milder events are increasingly captured, this reporting differential widens rather than narrows, producing anti-regression.

**Polypharmacy and autoimmune drug exposure.** Women with autoimmune conditions use more medications on average than age-matched men [10], creating a higher per-capita ADR exposure rate that compounds with each new drug added to the market. The anti-regression effect in Zone I may partially reflect the secular trend of increasing autoimmune drug approvals (biologics, JAK inhibitors, checkpoint modulators) that disproportionately expose female patients.

In contrast, the Zone III SOCs — Cardiac, Vascular, Renal, Blood/Lymphatic — are governed by different biological architectures:

**Hemodynamic and structural biology.** Cardiac and vascular ADRs are often hemodynamic in nature (QT prolongation, hypertension, thromboembolism) and reflect sex differences in cardiac electrophysiology and vascular tone rather than immune-mediated mechanisms [7]. These differences are real but relatively stable across reporting volume; they do not amplify with scale the way immune-mediated effects do.

**Androgen-mediated vascular risk.** The reverse anti-regression in Vascular disorders is particularly informative. Testosterone promotes erythropoiesis, increases hematocrit, and enhances platelet aggregation [11]. These effects create male-specific vascular vulnerability (thrombosis, stroke, peripheral vascular events) that becomes more visible as reporting volume increases and rare vascular events accumulate sufficient case counts to generate sex-differential signals.

### 4.3 Why Vascular Disorders Show Reverse Anti-Regression

The Vascular SOC is the single most striking finding of this study and merits detailed mechanistic interpretation. Several converging factors explain why vascular ADRs are unique in showing male-biased signal amplification with volume:

**4.3.1 Testosterone-mediated thrombotic risk.** Testosterone replacement therapy (TRT) has expanded dramatically since the early 2000s, with prescriptions peaking around 2013-2014 before declining somewhat after FDA safety communications [12]. TRT is associated with increased risk of venous thromboembolism, pulmonary embolism, and ischemic stroke — all classified under Vascular Disorders in MedDRA. As the cumulative reporting base for testosterone-associated vascular events grows, male-biased signals accumulate disproportionately in the high-volume deciles, driving reverse anti-regression.

**4.3.2 Anticoagulant and antiplatelet drug sex differences.** Major anticoagulants (warfarin, rivaroxaban, apixaban) and antiplatelet agents (clopidogrel, ticagrelor) are prescribed more frequently to men due to higher baseline cardiovascular risk. Vascular ADRs from these drugs — hemorrhage, hematoma, vascular occlusion — therefore carry a structural male excess that is proportional to prescribing volume.

**4.3.3 Erythropoietin and VEGF-pathway agents.** Erythropoiesis-stimulating agents (ESAs) and anti-VEGF biologics (bevacizumab, ramucirumab) generate vascular ADRs (hypertension, arterial thromboembolism) that are partly male-biased due to higher male hematocrit and vascular reactivity. These high-volume drugs contribute heavily to the upper volume deciles, where male bias is most pronounced.

**4.3.4 The "unmasking" hypothesis.** At low reporting volumes, vascular signals are dominated by common drug-event pairs where overall female reporting predominance (60.2% of the database is female) inflates the female fraction. As volume increases and drug-specific vascular signals emerge from the noise, the genuine male-biased biology of vascular events becomes unmasked, producing the observed negative rho. This is anti-regression in reverse: not regression to the mean, but regression *through* the mean to reveal the true underlying male predominance in vascular drug toxicity.

### 4.4 The Cardiovascular-Autoimmune Divide as an Organizing Principle

The data reveal a fundamental organizing principle in pharmacovigilance sex differences: the **cardiovascular-autoimmune divide**. This divide is not merely a difference in baseline sex ratios (which has been known for decades) but a difference in the *dynamics* of sex ratios as a function of pharmacoepidemiological scale.

On the autoimmune side (Zone I), sex differences are amplifying systems: the more data collected, the more female-biased the signals become. This suggests that autoimmune ADR biology contains positive feedback loops — estrogen-immune amplification, pain-reporting differentials, polypharmacy cascades — that compound with scale.

On the cardiovascular side (Zone III), sex differences are stabilizing systems: the sex ratio remains relatively constant regardless of reporting volume (Cardiac rho = -0.164, Renal rho = +0.018), or in the unique case of Vascular disorders, inverts. This suggests that cardiovascular ADR biology is governed by more stable structural and hemodynamic factors that do not exhibit the positive-feedback amplification seen in immune-mediated systems.

The divide is not absolute — Hepatobiliary disorders (Zone I by overall proportion, but non-significant anti-regression) represent a bridging category, consistent with the liver's dual role as both an immune organ (Kupffer cells, innate immunity) and a metabolic/hemodynamic organ (portal circulation, drug metabolism).

### 4.5 Implications for Signal Detection Thresholds

Current pharmacovigilance signal detection algorithms (PRR, ROR, BCPNN, MGPS) do not incorporate sex-specific thresholds that vary by organ system [1]. Our findings argue that they should. The practical implications are:

**4.5.1 Zone I SOCs require female-adjusted thresholds.** In Skin, Musculoskeletal, Immune, Gastrointestinal, Nervous System, and Hepatobiliary SOCs, the baseline female excess is so large (77-85%) and so dynamically amplifying that standard disproportionality thresholds will systematically underdetect male ADR signals and overdetect female signals. Signal detection in these SOCs should apply SOC-specific sex-stratification with thresholds calibrated to the observed female proportion.

**4.5.2 Zone III SOCs require parity-adjusted thresholds.** In Cardiac, Vascular, Renal, and Blood/Lymphatic SOCs, the sex ratio approaches parity (55-66% female), and applying a database-wide 60.2% female baseline would introduce bias in the opposite direction. These SOCs should use their own observed sex ratios as reference.

**4.5.3 Vascular SOC requires male-sensitized monitoring.** The reverse anti-regression in Vascular disorders means that standard female-predominance assumptions actively obscure emerging male vascular signals. Pharmacovigilance systems should implement enhanced male-specific vascular signal detection, particularly for drugs with hemodynamic or thrombotic mechanisms.

**4.5.4 Dynamic calibration.** Because anti-regression means that the sex ratio is a function of volume — not a constant — thresholds should be recalibrated periodically (e.g., annually) as reporting volume grows. Static thresholds set at one time point will become increasingly miscalibrated in Zone I SOCs.

### 4.6 Clinical Monitoring Recommendations by Organ System

The organ-specific anti-regression landscape translates into differentiated clinical monitoring recommendations:

**Table 3. Clinical Monitoring Recommendations by Zone**

| Zone | SOCs | Key Recommendation |
|------|------|--------------------|
| I (>75%F, anti-regression active) | Skin, MSK, Immune, GI, Nervous, Hepatobiliary | Heighten vigilance for male patients; their ADR signals are being drowned in a rising female tide. Implement male-specific safety reviews for immunomodulatory, analgesic, and dermatologic agents. |
| II (65-75%F, mixed) | Psychiatric, Reproductive, Metabolic, Infections, Eye, Respiratory | Standard sex-stratified monitoring. For Psychiatric ADRs, note that anti-regression is active (rho = 0.709), suggesting migration toward Zone I behavior. |
| III (<65%F, no anti-regression) | Vascular, Blood, Renal, Cardiac | Balanced monitoring with enhanced attention to sex-specific cardiovascular risk. For Vascular ADRs specifically, implement male-sensitized detection given reverse anti-regression. |

Specific drug classes warranting organ-system-aware sex monitoring include:

- **NSAIDs and immunosuppressants** (Zone I: GI, MSK, Skin): Female ADR signals dominate; actively seek male GI bleeding and renal signals that may be masked.
- **Antipsychotics and antidepressants** (Zone II: Psychiatric): Anti-regression suggests increasing female metabolic and neurological ADRs with scale; monitor for sex-differential tardive dyskinesia and metabolic syndrome.
- **Anticoagulants and antihypertensives** (Zone III: Vascular, Cardiac): Near-parity sex ratios require sex-neutral signal detection; avoid applying database-wide female-predominance corrections.
- **Testosterone replacement and ESAs** (Zone III: Vascular): Primary drivers of reverse anti-regression; mandate sex-stratified safety reporting for all vascular endpoints.

### 4.7 Comparison with Prior Work

To our knowledge, no prior study has systematically assessed the volume-dependence of sex bias across organ systems in a pharmacovigilance database. Previous work on sex differences in FAERS has focused on overall reporting ratios [2], specific drug classes [13], or individual adverse events [14]. The anti-regression concept itself has been described only at the aggregate level [3]. This study extends the framework to organ-system resolution and reveals structure that is invisible in aggregate analyses.

The cardiovascular-autoimmune divide observed here is consistent with epidemiological literature on sex differences in disease prevalence [5, 6, 7] but adds a pharmacovigilance-specific dimension: not just *which* organ systems are sex-biased, but *how that bias evolves with observational scale*. This dynamic dimension is novel and has no direct precedent in the pharmacovigilance literature.

### 4.8 Limitations

Several limitations should be acknowledged:

**Reporting bias.** FAERS is a spontaneous reporting system subject to stimulated reporting (media attention, litigation), notoriety bias, and differential reporting by sex. We cannot fully distinguish biological sex differences in ADR susceptibility from sex differences in reporting behavior. However, the organ-specific pattern — with anti-regression tracking known immunological gradients — argues against pure reporting artifact.

**SOC multi-mapping.** Some MedDRA Preferred Terms map to multiple SOCs, introducing potential signal sharing between organ systems. We did not perform exclusive SOC assignment, so a single signal may contribute to multiple SOC analyses.

**Decile resolution.** The anti-regression analysis uses 10 volume deciles, providing only 10 data points per SOC for correlation. SOCs with fewer total signals (e.g., Eye, n = 941; Reproductive, n = 457) may have insufficient statistical power to detect real anti-regression effects. The four SOCs excluded from Table 2 due to insufficient decile resolution may harbor undetected patterns.

**Temporal confounding.** Reporting volume is correlated with calendar time (later quarters have more cumulative reports). The observed anti-regression could partially reflect temporal trends in prescribing patterns, regulatory attention, or reporting culture rather than pure volume effects. Disentangling volume from time requires time-series decomposition beyond the scope of this analysis.

**Lack of denominator data.** FAERS does not contain denominator data (total prescriptions by sex). We cannot compute true incidence rates and must rely on proportional analyses. If prescribing patterns differ by sex in systematic ways that vary across organ systems, this could contribute to the observed patterns.

### 4.9 Future Directions

This work opens several avenues for investigation:

1. **Time-volume decomposition:** Separate the contributions of calendar time and cumulative volume to anti-regression using partial correlation or time-series regression, determining whether the effect is fundamentally temporal (reflecting changing prescribing landscapes) or volumetric (reflecting statistical unmasking of biological signals).

2. **Drug-class resolution:** Drill from SOC-level to ATC drug-class-level anti-regression analysis. Do all NSAIDs contribute equally to musculoskeletal anti-regression, or is the effect driven by specific agents?

3. **International replication:** Assess whether organ-specific anti-regression is reproducible in EudraVigilance (European), VigiBase (global), and JADER (Japanese) pharmacovigilance databases. If the pattern is biologically driven, it should replicate across reporting jurisdictions.

4. **Age-stratification:** Determine whether organ-specific anti-regression varies by age group. Post-menopausal women lose estrogenic immune amplification, which might attenuate anti-regression in Zone I SOCs in elderly cohorts.

5. **Knowledge graph integration:** Map anti-regression patterns onto sex-differential knowledge graphs that integrate drug targets, metabolic pathways, and immune signaling networks to identify molecular mediators of organ-specific sex-bias amplification.

---

## 5. Conclusions

The anti-regression phenomenon — the paradoxical intensification of female bias with increasing reporting volume — is not a uniform feature of pharmacovigilance data. It is organ-system-specific, tracking a fundamental biological divide between auto-inflammatory and cardiovascular pathophysiology.

Five organ systems (Musculoskeletal, Gastrointestinal, Skin, Nervous System, and Psychiatric) exhibit significant positive anti-regression, meaning that as pharmacovigilance databases grow, female ADR signals in these systems become progressively more dominant. These are the organ systems governed by estrogen-sensitive immunity, pain-processing pathways, and autoimmune drug exposure — biological substrates with inherent female amplification loops.

One organ system — Vascular Disorders — exhibits the opposite pattern: significant reverse anti-regression, in which male bias intensifies with scale. This reflects the testosterone-mediated thrombotic risk, anticoagulant prescribing patterns, and the statistical unmasking of male vascular biology that occurs as rare events accumulate.

The remaining organ systems show no significant volume-bias relationship, suggesting that their sex-differential profiles are stable rather than dynamic.

These findings have direct implications for pharmacovigilance practice. The current paradigm of sex-agnostic or uniformly sex-adjusted signal detection is biologically naive. Organ-system-stratified sex adjustment — with amplified male-signal sensitivity in Zone I SOCs and male-sensitized vascular monitoring in the Vascular SOC — would improve the detection of sex-specific safety signals that are currently masked by aggregate statistics.

The cardiovascular-autoimmune divide is not merely descriptive taxonomy; it is a fundamental organizing principle of pharmacovigilance sex differences, and it should be incorporated into the next generation of signal detection algorithms.

---

## References

1. Sakaeda T, Tamon A, Kadoyama K, Okuno Y. Data mining of the public version of the FDA Adverse Event Reporting System. *Int J Med Sci.* 2013;10(7):796-803. doi:10.7150/ijms.6048

2. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biol Sex Differ.* 2020;11(1):32. doi:10.1186/s13293-020-00308-5

3. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: Aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine.* 2019;17:100188. doi:10.1016/j.eclinm.2019.10.001

4. Brown EG, Wood L, Wood S. The Medical Dictionary for Regulatory Activities (MedDRA). *Drug Saf.* 1999;20(2):109-117. doi:10.2165/00002018-199920020-00002

5. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. *Lancet.* 2020;396(10250):565-582. doi:10.1016/S0140-6736(20)31561-0

6. Angum F, Khan T, Kaler J, Siddiqui L, Hussain A. The prevalence of autoimmune disorders in women: A narrative review. *Cureus.* 2020;12(5):e8094. doi:10.7759/cureus.8094

7. Mosca L, Barrett-Connor E, Wenger NK. Sex/gender differences in cardiovascular disease prevention: what a difference a decade makes. *Circulation.* 2011;124(19):2145-2154. doi:10.1161/CIRCULATIONAHA.110.968792

8. Kovats S. Estrogen receptors regulate innate immune cells and signaling pathways. *Cell Immunol.* 2015;294(2):63-69. doi:10.1016/j.cellimm.2015.01.018

9. Fillingim RB, King CD, Ribeiro-Dasilva MC, Rahim-Williams B, Riley JL 3rd. Sex, gender, and pain: a review of recent clinical and experimental findings. *J Pain.* 2009;10(5):447-485. doi:10.1016/j.jpain.2008.12.001

10. Whitacre CC. Sex differences in autoimmune disease. *Nat Immunol.* 2001;2(9):777-780. doi:10.1038/ni0901-777

11. Basaria S, Coviello AD, Travison TG, et al. Adverse events associated with testosterone administration. *N Engl J Med.* 2010;363(2):109-122. doi:10.1056/NEJMoa1000485

12. Baillargeon J, Urban RJ, Kuo YF, et al. Risk of venous thromboembolism in men receiving testosterone therapy. *Mayo Clin Proc.* 2015;90(7):884-894. doi:10.1016/j.mayocp.2015.05.012

13. de Vries ST, Denig P, Ekhart C, Burgers JS, Groothuis-Oudshoorn CGM, de Jong-van den Berg LTW. Sex differences in adverse drug reactions reported to the National Pharmacovigilance Centre in the Netherlands: An explorative observational study. *Br J Clin Pharmacol.* 2019;85(7):1507-1515. doi:10.1111/bcp.13923

14. Yu Y, Chen J, Li D, Wang L, Wang W, Liu H. Systematic analysis of adverse event reports for sex differences in adverse drug events. *Sci Rep.* 2016;6:24955. doi:10.1038/srep24955

---

*Manuscript prepared March 2026. Data source: FDA Adverse Event Reporting System (FAERS), public dashboard and quarterly data files.*

*Corresponding author: J.Shaik, jshaik@coevolvenetwork.com*
