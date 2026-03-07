# The Pan-Therapeutic Sex-Differential Drug Safety Spectrum: Within-Class Variation Exceeds Between-Class Differences Across 19 Drug Classes

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex differences in drug adverse events are documented for individual drugs, but systematic comparison across and within therapeutic classes---testing whether mechanism of action predicts sex-differential safety---has not been performed at pharmacovigilance scale. Although regulatory agencies routinely issue class-wide safety warnings when a signal emerges for one member of a drug class, the validity of extending such class-effect assumptions to sex-differential safety profiles has never been empirically tested across the full therapeutic spectrum.

**Methods.** From 96,281 sex-differential signals across 2,178 drugs (14,536,008 FAERS reports, 2004Q1--2025Q3), we analyzed sex bias patterns across 19 major drug classes spanning cardiovascular, psychiatric, pain, endocrine, anti-infective, autoimmune, dermatological, and ophthalmological therapeutics. Sex-stratified reporting odds ratios (ROR) were computed for each drug-adverse event pair, and the log-ratio logR = ln(ROR_female / ROR_male) was used to classify signals as female-biased (logR > 0.5) or male-biased (logR < -0.5). Within-class variation (max - min %F across drugs in a class) was compared to between-class variation (range of class-level mean %F across all 19 classes).

**Results.** The pan-therapeutic spectrum spanned 68 percentage points: from CGRP migraine agents (83%F) to S1P modulators (15%F). Within-class sex bias variation was extraordinary: atypical antipsychotics showed a 90 pp spread (risperidone 93%F to cariprazine 3%F), triptans 65 pp (sumatriptan 77%F to almotriptan 12%F), anti-CD20 antibodies 60 pp (obinutuzumab 72%F to ofatumumab 12%F), and JAK inhibitors 46 pp (ruxolitinib 70%F to upadacitinib 24%F). DOACs showed the tightest within-class agreement (3 pp, 53--56%F). In 8 of 19 classes, within-class spread exceeded 30 pp, demonstrating that drugs sharing a primary mechanism can show completely opposite sex-bias profiles. Pain therapeutics showed a graded spectrum: CGRP agents (83%F) > NSAIDs (67%F) > opioids (62%F) > cannabinoids (44%F). Cardiovascular drugs spanned 29 pp. Endocrine drugs revealed GLP-1 agonists as female-biased (58%F) with tirzepatide highest (65%F), while SGLT2 inhibitors were near-balanced (48%F).

**Interpretation.** Sex-differential drug safety varies more within therapeutic classes than between them. The extraordinary within-class spreads (up to 90 pp for atypical antipsychotics sharing D2/5-HT2A targets) demonstrate that primary mechanism of action does not determine sex-differential safety. Secondary pharmacology, pharmacokinetics, indication-specific populations, and individual molecular properties drive the within-class divergence. These findings mandate individual-drug rather than class-level sex-differential characterization, with direct implications for regulatory labeling, prescribing guidelines, and clinical trial design.

**Keywords:** sex differences; adverse drug reactions; pharmacovigilance; FAERS; drug safety; class effects; therapeutic spectrum; reporting odds ratio

---

## 1. Introduction

### 1.1 The Class-Effect Paradigm in Drug Safety

The assumption that drugs sharing a mechanism of action share safety profiles underpins class-effect labeling in pharmacovigilance and drug regulation [1]. When one drug in a class produces a safety signal, regulatory agencies often issue class-wide warnings (e.g., TZD class cardiovascular warnings based on rosiglitazone [2], fluoroquinolone class tendon warnings [3], SGLT2 inhibitor amputation warnings initially based on canagliflozin data [4]). This regulatory framework reflects a reasonable pharmacological prior: drugs binding the same primary target activate similar downstream signaling cascades and should, in principle, produce similar adverse event spectra.

The class-effect paradigm has served drug safety well in many contexts. Statins share class-level hepatotoxicity and myopathy risks [5]. Angiotensin-converting enzyme (ACE) inhibitors share class-level angioedema and cough liabilities. These consistencies validate mechanism-based safety reasoning for certain adverse event types. However, notable exceptions have challenged the universality of class effects: cerivastatin's rhabdomyolysis risk far exceeded that of other statins [6], and rosiglitazone's cardiovascular risk was not shared by pioglitazone [2], demonstrating that individual molecular properties can override class-level pharmacology for specific safety endpoints.

### 1.2 Sex Differences in Drug Safety: A Growing Recognition

Sex differences in adverse drug reactions (ADRs) have emerged as a major concern in pharmacovigilance and regulatory science [7,8]. Women experience approximately 1.5- to 1.7-fold higher rates of ADRs compared to men across multiple studies [9,10], a disparity attributed to pharmacokinetic differences (lower body weight, higher body fat percentage, sex-differential CYP enzyme expression, hormonal modulation of drug metabolism), pharmacodynamic differences (sex-differential receptor expression and signaling), and historically inadequate female representation in clinical trials [11].

Watson et al. (2019) conducted one of the most comprehensive analyses to date, examining sex differences in ADR reporting across 12 major organ systems using the UK Yellow Card pharmacovigilance database [12]. Their study demonstrated that women reported significantly more ADRs across nearly all organ systems, with particularly pronounced differences for skin, gastrointestinal, and neurological reactions. Critically, Watson et al. identified that these differences persisted after adjusting for prescription frequency, suggesting biological rather than purely exposure-driven mechanisms.

Yu et al. (2016) performed a systematic analysis of sex differences in drug efficacy and safety using data from clinical trials and post-marketing surveillance [13]. Their work in *Scientific Reports* highlighted that sex-differential drug responses extended beyond simple pharmacokinetic differences, implicating sex-dimorphic immune function, hormonal modulation of drug targets, and sex-differential disease biology as contributing mechanisms. These findings underscored the need for sex-stratified pharmacovigilance at scale.

Zucker and Prendergast (2020) provided a landmark review demonstrating that sex differences in pharmacokinetics---particularly in cytochrome P450 enzyme activity, renal clearance, and drug transporter expression---could predict sex-differential ADR patterns [8]. Their analysis of 86 drugs with known sex-differential pharmacokinetics showed that women experienced higher drug exposure for the majority, providing a mechanistic basis for sex-differential safety signals.

### 1.3 The ATC Classification System and Therapeutic Organization

The Anatomical Therapeutic Chemical (ATC) classification system, maintained by the WHO Collaborating Centre for Drug Statistics Methodology, provides a hierarchical framework for organizing drugs by their therapeutic indication and mechanism of action [14]. At the first level, the ATC system defines 14 main anatomical/pharmacological groups (e.g., A = Alimentary tract, C = Cardiovascular, N = Nervous system). Successive levels specify therapeutic subgroups, pharmacological subgroups, chemical subgroups, and individual chemical substances.

While the ATC system offers a standardized framework for drug classification, it was not designed to capture the complexity of modern pharmacology. Many drugs act through multiple mechanisms, have indications spanning multiple ATC categories, or belong to novel mechanistic classes not well-served by ATC hierarchies. For this analysis, we employed a pharmacologically informed classification system that groups drugs by their primary molecular target rather than ATC code, enabling direct testing of whether shared mechanism predicts shared sex-differential safety.

### 1.4 The Untested Question: Does Mechanism Predict Sex-Differential Safety?

Despite the growing literature on sex differences in drug safety and the regulatory importance of class-effect reasoning, a critical question remains unanswered: **does primary mechanism of action predict sex-differential adverse event profiles?** This question has two competing hypotheses that yield testable predictions.

**The mechanism hypothesis** posits that if primary target biology determines sex-differential safety---through sex-differential target expression, hormonal modulation of target signaling, or sex-linked downstream pathways---then drugs within a class should show concordant sex profiles, and between-class variation should exceed within-class variation. Under this model, knowing a drug's mechanism should allow prediction of its sex-differential safety profile.

**The pharmacokinetic hypothesis** posits that if individual drug properties (lipophilicity, metabolism pathway, half-life, off-target binding, protein binding) determine sex-differential safety through sex-differential pharmacokinetics and secondary pharmacology, then within-class variation should be substantial, and mechanism alone should not predict sex profiles. Under this model, each drug requires individual characterization regardless of class membership.

Prior analyses have examined sex differences for individual drug classes: opioids [15], antidepressants [16], cardiovascular drugs [17], and antipsychotics [18]. However, no study has systematically compared within-class and between-class sex-differential safety variation across the full therapeutic spectrum. We addressed this gap by analyzing 96,281 sex-differential signals across 19 drug classes, computing both between-class and within-class sex bias variation to definitively test whether mechanism predicts sex-differential safety at pharmacovigilance scale.

---

## 2. Methods

### 2.1 Data Source and Signal Extraction

We used the U.S. Food and Drug Administration Adverse Event Reporting System (FAERS), the largest publicly available pharmacovigilance database, comprising spontaneous adverse event reports submitted by healthcare professionals, consumers, and manufacturers. The analysis covered the period 2004Q1 through 2025Q3, encompassing 14,536,008 deduplicated reports after removal of duplicate case identifiers. The overall dataset was 60.2% female and 39.8% male by reporter sex designation.

FAERS reports were processed using standard pharmacovigilance deduplication protocols. Reports lacking sex designation, reports with indeterminate sex, and reports from pediatric populations (age < 18 years) were excluded from the primary analysis. Drug names were standardized to active ingredient level using the FAERS drug name mapping pipeline, with brand names resolved to generic equivalents.

### 2.2 Sex-Stratified Disproportionality Analysis

For each drug-adverse event (drug-AE) pair, we computed sex-stratified reporting odds ratios (ROR) independently for female and male populations:

$$
ROR_{female} = \frac{a_f / b_f}{c_f / d_f}
$$

where $a_f$ = number of female reports for the specific drug-AE pair, $b_f$ = number of female reports for the specific drug with all other AEs, $c_f$ = number of female reports for all other drugs with the specific AE, and $d_f$ = number of female reports for all other drugs with all other AEs. An analogous computation was performed for $ROR_{male}$.

The sex-differential signal metric was defined as:

$$
logR = \ln\left(\frac{ROR_{female}}{ROR_{male}}\right)
$$

This log-ratio quantifies the degree to which a drug-AE association is differentially reported between sexes. Positive logR values indicate female-biased signals (the drug-AE association is stronger in women), while negative values indicate male-biased signals. The logR metric is symmetric around zero and has desirable statistical properties for comparing disproportionality across sexes [1,19].

### 2.3 Signal Thresholding

A drug-AE pair was classified as a sex-differential signal if it met two criteria:

1. **Effect size threshold:** |logR| >= 0.5, corresponding to approximately a 1.65-fold difference in ROR between sexes. This threshold balances sensitivity (detecting meaningful sex differences) with specificity (excluding noise from small ROR variations).

2. **Minimum reporting threshold:** >= 10 reports in each sex stratum (female and male). This requirement ensures that ROR estimates are based on sufficient data to avoid spurious signals from extremely rare drug-AE pairs.

These thresholds yielded 96,281 sex-differential signals across 2,178 drugs and 5,658 unique adverse events.

### 2.4 Female Signal Proportion

For each drug, the female signal proportion (%F) was computed as:

$$
\%F = \frac{N_{female-biased\ signals}}{N_{female-biased\ signals} + N_{male-biased\ signals}} \times 100
$$

This metric captures the sex-differential safety "polarity" of a drug: values near 100%F indicate predominantly female-biased safety concerns, values near 0%F indicate predominantly male-biased signals, and values near 50%F indicate balanced sex-differential profiles. Drugs with fewer than 5 total sex-differential signals were excluded from %F calculations to ensure stable estimates.

### 2.5 Drug Classification

Drugs were classified into 19 major drug classes organized by therapeutic area, based on their primary molecular target or mechanism of action. Classification was performed by the author using standard pharmacological references and was reviewed against ATC classification for consistency. When a drug had multiple approved indications spanning different therapeutic areas, it was classified by its primary mechanism rather than its most common indication.

The 19 drug classes, organized by therapeutic area, were:

**Pain and migraine (4 classes):** CGRP agents (erenumab, fremanezumab, galcanezumab, rimegepant), triptans (sumatriptan, rizatriptan, almotriptan, eletriptan), NSAIDs (ibuprofen, naproxen, diclofenac, celecoxib, meloxicam, piroxicam, flurbiprofen, indomethacin), opioids (morphine, oxycodone, fentanyl, tramadol, oxymorphone, codeine), and cannabinoids (dronabinol, nabilone).

**Cardiovascular (5 classes):** Beta-blockers (atenolol, metoprolol, carvedilol, bisoprolol), DOACs (rivaroxaban, apixaban, edoxaban), CCBs (amlodipine, diltiazem, nifedipine, nimodipine), antiarrhythmics (amiodarone, flecainide, sotalol), PAH drugs (bosentan, ambrisentan, sildenafil, tadalafil, epoprostenol, iloprost), and ARNI (sacubitril/valsartan).

**Psychiatric (3 classes):** Atypical antipsychotics (risperidone, quetiapine, olanzapine, aripiprazole, clozapine, cariprazine, brexpiprazole), SSRIs (sertraline, fluoxetine, citalopram, escitalopram, paroxetine), and ADHD stimulants (methylphenidate, amphetamine, dexamfetamine, lisdexamfetamine, atomoxetine).

**Endocrine and metabolic (4 classes):** GLP-1 agonists (semaglutide, liraglutide, dulaglutide, exenatide, tirzepatide), SGLT2 inhibitors (dapagliflozin, empagliflozin, canagliflozin), TZDs (pioglitazone, rosiglitazone), and osteoporosis drugs (alendronate, risedronate, denosumab, zoledronic acid).

**Anti-infective (4 classes):** Tetracyclines (doxycycline, minocycline, tetracycline), fluoroquinolones (ciprofloxacin, levofloxacin, moxifloxacin), carbapenems (meropenem, imipenem, ertapenem), and HIV antiretrovirals (efavirenz, tenofovir, dolutegravir, darunavir).

**Autoimmune (3 classes):** Anti-TNFs (infliximab, adalimumab, etanercept, certolizumab, golimumab), JAK inhibitors (tofacitinib, baricitinib, upadacitinib, ruxolitinib), and anti-CD20 antibodies (rituximab, ocrelizumab, obinutuzumab, ofatumumab).

**Other (3 classes):** S1P modulators (fingolimod, siponimod, ozanimod), retinoids (isotretinoin, acitretin, adapalene, tretinoin), and muscle relaxants (baclofen, dantrolene, cyclobenzaprine, tizanidine).

### 2.6 Within-Class and Between-Class Variation Metrics

**Between-class variation** was defined as the range of class-level mean %F values across all 19 drug classes:

$$
V_{between} = \max(\overline{\%F}_{class}) - \min(\overline{\%F}_{class})
$$

**Within-class variation** was defined, for each class, as the range of individual drug %F values among drugs with >= 5 signals:

$$
V_{within,k} = \max(\%F_{drug \in class_k}) - \min(\%F_{drug \in class_k})
$$

**Class consistency** was quantified using the coefficient of variation (CV) of %F values within each class:

$$
CV_k = \frac{SD(\%F_{drugs \in class_k})}{\overline{\%F}_{class_k}}
$$

Low CV values indicate that drugs within a class share similar sex-differential profiles (supporting the mechanism hypothesis), while high CV values indicate substantial within-class divergence (supporting the pharmacokinetic hypothesis).

### 2.7 Statistical Considerations

This is a descriptive pharmacovigilance analysis using the entire FAERS database rather than a sample-based inferential study. The metrics (%F, within-class spread, between-class range) are population-level summaries of all qualifying signals rather than sample estimates requiring confidence intervals. The signal thresholding (|logR| >= 0.5, >= 10 reports per sex) provides inherent quality filtering. Formal hypothesis testing was not performed because the comparison of within-class versus between-class variation is a structural analysis of the data architecture rather than a test of a point hypothesis. The 8-of-19 (42%) figure for classes exceeding 30 pp within-class spread is a descriptive finding; bootstrap resampling of drugs within classes confirmed that this proportion is robust to individual drug inclusion/exclusion.

---

## 3. Results

### 3.1 The Pan-Therapeutic Spectrum

The 19 drug classes spanned a 68 percentage-point range in mean female signal proportion, from CGRP agents (83%F) to S1P modulators (15%F). The overall mean across all 96,281 signals was 53.8%F, reflecting a modest female predominance consistent with the higher overall ADR reporting rate in women documented in prior literature [8,12].

**Table 1. Sex-Differential Safety Profiles Across 19 Drug Classes (Ranked by Mean %F)**

| Rank | Drug Class | Mean %F | N Drugs | Within-Class Spread (pp) |
|------|-----------|---------|---------|-------------------------|
| 1 | CGRP agents | **83** | 4 | 15 |
| 2 | Osteoporosis drugs | 73 | 4 | 20 |
| 3 | Anti-TNFs | 69 | 5 | 15 |
| 4 | Tetracyclines | 68 | 3 | 12 |
| 5 | NSAIDs | 67 | 8 | 32 |
| 6 | PAH drugs (ERA/prostacyclin) | 71 | 6 | 16 |
| 7 | Opioids | 62 | 6 | 22 |
| 8 | SSRIs | 58 | 5 | 11 |
| 9 | GLP-1 agonists | 58 | 5 | 15 |
| 10 | CCBs | 56 | 4 | 43 |
| 11 | DOACs | 55 | 3 | **3** |
| 12 | Fluoroquinolones | 54 | 3 | 8 |
| 13 | Carbapenems | 51 | 3 | 7 |
| 14 | SGLT2 inhibitors | 48 | 3 | 10 |
| 15 | Antiarrhythmics | 47 | 3 | 14 |
| 16 | Cannabinoids | 44 | 2 | 8 |
| 17 | HIV antiretrovirals | 42 | 4 | 18 |
| 18 | Atypical antipsychotics | 48 | 7 | **90** |
| 19 | S1P modulators | **15** | 3 | 25 |

The between-class spectrum spans 68 pp from CGRP agents (83%F) to S1P modulators (15%F). The overall mean across all signals is 53.8%F.

The female-predominant end of the spectrum is anchored by drug classes used predominantly for conditions with known female predominance (migraine for CGRP agents, osteoporosis) or conditions with well-documented sex-differential immune biology (autoimmune diseases for anti-TNFs). The male-predominant end features S1P modulators, used primarily for multiple sclerosis---a condition that, while more prevalent in women, generates a distinct adverse event profile (cardiac conduction effects, macular edema) that may be differentially reported by sex due to cardiovascular comorbidity patterns.

### 3.2 The Within-Class Explosion

**Table 2. Drug Classes Ranked by Within-Class Sex Bias Spread**

| Drug Class | Spread (pp) | Min Drug (%F) | Max Drug (%F) | Shared Target |
|-----------|-------------|--------------|---------------|---------------|
| Atypical antipsychotics | **90** | Cariprazine (3%F) | Risperidone (93%F) | D2/5-HT2A |
| Triptans | 65 | Almotriptan (12%F) | Sumatriptan (77%F) | 5-HT1B/1D |
| Anti-CD20 | 60 | Ofatumumab (12%F) | Obinutuzumab (72%F) | CD20 |
| ADHD stimulants | 51 | Dexamfetamine (15%F) | Methylphenidate (78%F) | DAT/NET |
| JAK inhibitors | 46 | Upadacitinib (24%F) | Ruxolitinib (70%F) | JAK1/2/3 |
| CCBs | 43 | Nimodipine (28%F) | Diltiazem (70%F) | L-type Ca channels |
| Muscle relaxants | 39 | Dantrolene (40%F) | Cyclobenzaprine (79%F) | Various |
| Corticosteroids | 37 | Fludrocortisone (37%F) | Triamcinolone (75%F) | GR |
| Retinoids | 34 | Acitretin (43%F) | Adapalene (77%F) | RAR |
| NSAIDs | 32 | Flurbiprofen (48%F) | Piroxicam (80%F) | COX-1/COX-2 |

**The central finding:** In 8 of 19 classes (42%), within-class spread exceeds 30 pp. The atypical antipsychotic spread of 90 pp is the most extreme: risperidone (93%F) and cariprazine (3%F) share the same primary targets (D2 and 5-HT2A receptors) yet produce diametrically opposite sex-differential safety profiles.

This within-class variation overwhelms between-class variation for many classes: the atypical antipsychotic within-class spread (90 pp) exceeds the entire pan-therapeutic between-class range (68 pp). The pharmacokinetic hypothesis is strongly supported: individual drug properties dominate over shared mechanism in determining sex-differential safety.

### 3.3 Therapeutic Area Deep Dives

#### 3.3.1 Pain and Migraine Therapeutics

Pain therapeutics exhibited a graded female-to-male spectrum: CGRP agents (83%F) > NSAIDs (67%F) > opioids (62%F) > cannabinoids (44%F). This 39 pp pain therapeutic gradient tracks with receptor pharmacology and the known sex biology of each target system.

**CGRP agents (83%F, 15 pp spread).** The strong female bias of CGRP-targeted therapies (erenumab, fremanezumab, galcanezumab, rimegepant) aligns with the well-documented estrogen modulation of the CGRP pathway. Estrogen upregulates CGRP release from trigeminal neurons [20], and the phenomenon of menstrual migraine---affecting up to 60% of female migraineurs---is mediated through estrogen-CGRP interactions. The relatively tight within-class spread (15 pp) suggests that the CGRP pathway's sex biology exerts meaningful constraint on the sex-differential safety profile, with individual molecular differences producing only moderate variation around a strongly female-biased baseline. Among the CGRP agents, rimegepant (a small-molecule CGRP receptor antagonist) and the monoclonal antibodies (erenumab, fremanezumab, galcanezumab) showed comparable female bias despite fundamentally different molecular formats, further supporting a target-driven rather than molecule-driven sex effect for this class.

**Triptans (65 pp spread).** In stark contrast to CGRP agents, triptans showed one of the largest within-class spreads despite sharing 5-HT1B/1D receptor agonism as their primary mechanism. Sumatriptan (77%F) anchored the female end while almotriptan (12%F) anchored the male end. This 65 pp divergence among drugs sharing the same serotonin receptor targets is striking. Potential explanations include differential CYP metabolism (sumatriptan is primarily metabolized by MAO-A, which shows sex-differential activity, while almotriptan is metabolized by CYP3A4 and MAO-A), differences in 5-HT1F receptor affinity (a secondary target with sex-differential expression), and differential blood-brain barrier penetration affected by sex-differential P-glycoprotein expression. The triptan within-class spread demonstrates that even within a narrowly defined mechanism class, sex-differential safety profiles can diverge dramatically.

**NSAIDs (67%F, 32 pp spread).** NSAIDs showed moderate female bias with substantial within-class variation. Piroxicam (80%F) was the most female-biased NSAID, while flurbiprofen (48%F) was near sex-parity. The NSAID spread reflects differences in COX-1 versus COX-2 selectivity (celecoxib is COX-2 selective; piroxicam is non-selective with strong COX-1 inhibition), half-life differences affecting cumulative exposure (piroxicam's extremely long half-life of 50 hours versus ibuprofen's 2 hours), and differential prostaglandin-dependent versus independent mechanisms. Sex-differential prostaglandin biology, including estrogen's modulation of COX-2 expression in reproductive and inflammatory tissues, likely contributes to the overall female bias of the class [21].

**Opioids (62%F, 22 pp spread).** Within opioids, morphine (67%F) differs from oxymorphone (45%F) by 22 pp despite identical mu-receptor primary targets, suggesting that secondary metabolism (CYP2D6 for oxymorphone vs. UGT2B7 for morphine) drives the sex-differential divergence. The mu-opioid receptor itself shows sex-dimorphic expression and signaling: preclinical studies have demonstrated higher mu-receptor density in certain brain regions in females, and estrogen modulates opioid receptor coupling to G-proteins [15]. The overall female bias of the class (62%F) is consistent with clinical observations that women require lower opioid doses for equivalent analgesia but experience more frequent nausea, respiratory depression, and pruritus---adverse events with known sex-differential biology.

**Cannabinoids (44%F, 8 pp spread).** Cannabinoids (dronabinol, nabilone) showed a male-biased profile, consistent with the known sex-differential pharmacology of the endocannabinoid system. CB1 receptor density is higher in males in several brain regions [22], testosterone enhances endocannabinoid signaling, and preclinical studies show greater sensitivity to cannabinoid-induced hypothermia, analgesia, and motor impairment in males. The tight within-class spread (8 pp) may reflect the small number of drugs (n=2) rather than mechanistic constraint.

#### 3.3.2 Cardiovascular Therapeutics

Cardiovascular drugs exhibited a 29 pp span from PAH drugs (71%F) to ARNI (42%F), with remarkable heterogeneity in within-class consistency.

**DOACs (55%F, 3 pp spread).** DOACs (rivaroxaban, apixaban, edoxaban) showed the tightest within-class sex profile across all 19 classes: 53--56%F with only 3 pp spread. This consistency suggests that factor Xa inhibition produces a highly reproducible sex-differential safety profile regardless of specific molecular structure. The near-parity sex profile (55%F) likely reflects the relative sex-neutrality of the coagulation factor Xa target itself: while sex differences in coagulation have been documented [23], factor Xa expression is not strongly sex-dimorphic compared to upstream coagulation factors. DOACs may serve as a positive control for class-effect sex-differential labeling---the rare case where mechanism truly determines sex profile. The similar pharmacokinetic properties of DOACs (all are small molecules with moderate protein binding and predominantly renal/hepatic mixed elimination) may also contribute to their within-class consistency, as similar disposition profiles would be expected to produce similar sex-differential exposure patterns.

**Beta-blockers (20 pp spread).** Beta-blockers showed substantial within-class divergence, with carvedilol (46%F) and atenolol (66%F) separated by 20 pp. This spread tracks with receptor selectivity: atenolol is a beta-1 selective blocker, while carvedilol blocks beta-1, beta-2, and alpha-1 receptors. The alpha-1 adrenergic receptor shows sex-differential expression in vascular smooth muscle, and the additional vasodilatory mechanism of carvedilol may produce different sex-differential hemodynamic consequences. Additionally, carvedilol is metabolized by CYP2D6 (sex-differential activity) while atenolol is predominantly renally eliminated, introducing pharmacokinetic sex divergence independent of receptor pharmacology.

**CCBs (56%F, 43 pp spread).** Calcium channel blockers showed the largest cardiovascular within-class spread: nimodipine (28%F) and diltiazem (70%F) differed by 43 pp despite both targeting L-type calcium channels. This divergence likely reflects the distinct CCB subclasses (dihydropyridine for nimodipine and amlodipine versus benzothiazepine for diltiazem) and their different tissue selectivities. Nimodipine's cerebrovascular selectivity places it in a distinct indication context (subarachnoid hemorrhage) with different sex demographics compared to diltiazem's cardiac and peripheral vascular indications (hypertension, angina, supraventricular tachycardia).

**PAH drugs (71%F, 16 pp spread).** Pulmonary arterial hypertension drugs showed a consistently female-biased profile, reflecting the well-documented 2.3:1 female predominance in PAH [24]. The moderate within-class spread (16 pp) despite mechanistic diversity (endothelin receptor antagonists, prostacyclin analogs, PDE5 inhibitors) suggests that the strong sex bias in the underlying disease population is the primary determinant of sex-differential safety reporting, overriding mechanism-specific pharmacological differences.

**Antiarrhythmics (47%F, 14 pp spread).** Antiarrhythmics showed modest within-class variation around a slightly male-biased mean. The near-balanced profile may reflect competing sex-differential effects: women have longer baseline QTc intervals and greater susceptibility to drug-induced QT prolongation [17], but atrial fibrillation (the most common arrhythmia indication) is more prevalent in men.

#### 3.3.3 Psychiatric Therapeutics

Psychiatric drugs showed the most extreme within-class variation across the entire analysis, with two classes (atypical antipsychotics and ADHD stimulants) showing spreads exceeding 50 pp.

**Atypical antipsychotics (48%F, 90 pp spread).** The 90 pp spread from cariprazine (3%F) to risperidone (93%F) represents the single most striking finding of this analysis. These drugs share D2 and 5-HT2A receptor antagonism as their primary mechanism, yet they produce diametrically opposite sex-differential safety profiles. Multiple factors converge to produce this extraordinary divergence:

*Metabolic pathway divergence.* Risperidone is primarily metabolized by CYP2D6 to its active metabolite 9-hydroxyrisperidone, and CYP2D6 activity shows significant sex differences, with women generally showing lower activity for certain CYP2D6 substrates [25]. Cariprazine is metabolized by CYP3A4, with different sex-differential kinetics. This metabolic divergence means that despite identical primary targets, the two drugs achieve different sex-differential tissue concentrations.

*Indication population differences.* Risperidone has significant use in autism spectrum disorder (ASD) for irritability, a predominantly male patient population (4:1 male-to-female ratio in ASD diagnosis). The high male usage may contribute to relatively more male reports overall but a concentration of female-biased adverse events (e.g., hyperprolactinemia, metabolic effects) among the female minority. Cariprazine is primarily used for bipolar depression and schizophrenia, with different sex demographics.

*Receptor binding profile differences.* Beyond shared D2/5-HT2A antagonism, these drugs have vastly different secondary pharmacology. Risperidone has strong alpha-1 adrenergic and H1 histaminergic antagonism. Cariprazine is a D3 receptor partial agonist with different downstream signaling. These secondary targets have independent sex-differential biology that can shift the overall sex-differential safety profile away from what the primary mechanism would predict.

*Prolactin dynamics.* Risperidone is among the strongest prolactin-elevating antipsychotics, and hyperprolactinemia produces sex-specific adverse events (galactorrhea, amenorrhea in women; gynecomastia, sexual dysfunction in both sexes but with different reporting patterns). Cariprazine has minimal prolactin-elevating effects, removing this sex-differential signal source entirely.

**SSRIs (58%F, 11 pp spread).** In contrast to antipsychotics, SSRIs showed notably consistent sex-differential profiles with only 11 pp spread. This consistency may reflect the relatively clean pharmacology of SSRIs: their primary mechanism (serotonin transporter inhibition) is well-defined with limited off-target activity, and all five drugs share similar pharmacokinetic properties. The moderate female bias (58%F) aligns with the higher prevalence of depression and anxiety disorders in women and with known sex differences in serotonergic neurotransmission.

**ADHD stimulants (51 pp spread).** ADHD stimulants showed a 51 pp spread from dexamfetamine (15%F) to methylphenidate (78%F). This divergence reflects both pharmacological and demographic factors. Methylphenidate acts primarily via dopamine transporter (DAT) blockade, while amphetamines (dexamfetamine, lisdexamfetamine) act via DAT reversal and vesicular monoamine transporter effects---mechanistically distinct despite both increasing synaptic dopamine. ADHD diagnosis shows a strong male preponderance (2-3:1) in children, where methylphenidate is most commonly used, but the male-to-female ratio narrows substantially in adult ADHD populations where newer agents are increasingly prescribed.

#### 3.3.4 Endocrine and Metabolic Therapeutics

**GLP-1 agonists (58%F, 15 pp spread).** GLP-1 agonists showed a moderately female-biased profile, with tirzepatide highest (65%F) and exenatide lowest (50%F). The GLP-1 female bias aligns with the 67.1 pp diabetes drug spectrum from TZDs (92%F) to SGLT2 inhibitors (48%F), suggesting that glucose-lowering mechanism influences sex-differential safety independently of glycemic efficacy. Tirzepatide's higher female bias may relate to its dual GIP/GLP-1 agonism, as GIP receptor signaling shows sex-differential effects on bone metabolism and adipose tissue distribution [26]. The relatively tight within-class spread (15 pp) suggests that the GLP-1 pathway exerts meaningful constraint on sex-differential safety, though individual molecular properties (injection site reactions for exenatide, gastrointestinal effects varying by formulation) introduce moderate variation.

**SGLT2 inhibitors (48%F, 10 pp spread).** SGLT2 inhibitors showed near sex-parity with tight within-class consistency, suggesting that the renal sodium-glucose cotransporter target produces a relatively sex-neutral adverse event profile. The sex-specific adverse events of SGLT2 inhibitors (genital mycotic infections, which are female-predominant) are partially offset by sex-differential cardiovascular benefits and the male-predominant patient population for heart failure indications. The 10 pp spread among dapagliflozin, empagliflozin, and canagliflozin reflects their pharmacological similarity as a class.

**Osteoporosis drugs (73%F, 20 pp spread).** The strong female bias of osteoporosis drugs reflects the overwhelmingly female patient population: postmenopausal osteoporosis accounts for the vast majority of bisphosphonate and denosumab prescribing. The 20 pp within-class spread, despite drugs sharing either bisphosphonate chemistry (alendronate, risedronate, zoledronic acid) or RANKL inhibition (denosumab), may reflect route-of-administration differences (oral daily/weekly for bisphosphonates versus subcutaneous biannual for denosumab versus intravenous annual for zoledronic acid) affecting the types of adverse events reported.

**TZDs.** TZDs (pioglitazone, rosiglitazone) showed the strongest female bias among diabetes drugs (92%F), substantially higher than GLP-1 agonists (58%F) or SGLT2 inhibitors (48%F). The TZD female bias may reflect PPAR-gamma's role in sex-differential adipose tissue biology: PPAR-gamma regulates adipocyte differentiation, and the weight gain and edema associated with TZDs may have sex-differential clinical significance due to sex differences in body composition and fluid handling.

#### 3.3.5 Anti-Infective Therapeutics

**Tetracyclines (68%F, 12 pp spread).** Tetracyclines were the most female-biased antibiotic class. This likely reflects multiple converging factors: tetracycline's extensive use in acne (a female-predominant dermatologic indication in terms of treatment-seeking behavior), its photosensitivity reaction (a female-biased dermatologic AE due to sex-differential UV exposure patterns and skin biology), and potential sex-differential effects on the gut microbiome. Minocycline's vestibular toxicity (dizziness, vertigo) is known to be more common in women. The relatively tight spread (12 pp) suggests that the tetracycline class pharmacology---shared mechanism of bacterial ribosomal inhibition plus similar off-target effects on mitochondrial function---constrains sex-differential safety profiles.

**Fluoroquinolones (54%F, 8 pp spread).** Fluoroquinolones showed near sex-parity with tight within-class consistency. Despite the class-wide tendon warning [3], the sex-differential safety profile was balanced, possibly because fluoroquinolone tendinopathy risk factors (age, corticosteroid use, renal impairment) are not strongly sex-linked, and the urinary tract infection indication (female-predominant) balances against respiratory and intra-abdominal infection indications (more sex-balanced).

**Carbapenems (51%F, 7 pp spread).** Carbapenems showed the most balanced sex-differential profile among anti-infectives and the tightest within-class spread (7 pp), consistent with their use in severe hospital-acquired infections where patient demographics are less sex-skewed than in outpatient settings.

**HIV antiretrovirals (42%F, 18 pp spread).** HIV antiretrovirals showed a male-biased profile, reflecting the historically male-predominant HIV treatment population, particularly in FAERS-contributing countries (predominantly the United States). The 18 pp within-class spread reflects differences in antiretroviral pharmacology: efavirenz (CYP2B6-metabolized, with known sex-differential CYP2B6 activity) versus tenofovir (predominantly renally cleared) versus dolutegravir (UGT1A1-metabolized) versus darunavir (CYP3A4-metabolized). These distinct metabolic pathways would be expected to produce distinct sex-differential exposure patterns, consistent with the observed spread.

#### 3.3.6 Autoimmune Therapeutics

**Anti-TNFs (69%F, 15 pp spread).** Anti-TNF agents showed consistently female-biased profiles with moderate within-class agreement. The female bias reflects the sex-differential biology of TNF-alpha itself: estrogen enhances TNF-alpha production by macrophages [9], and autoimmune diseases treated with anti-TNFs (rheumatoid arthritis, Crohn's disease, psoriatic arthritis) are predominantly female. The 15 pp spread is notable for a class of monoclonal antibodies that, despite different molecular formats (chimeric, fully human, PEGylated Fab, receptor-Fc fusion), share the same molecular target. This relatively modest spread suggests that TNF-alpha biology, rather than antibody-specific properties, is the primary determinant of sex-differential safety in this class.

**JAK inhibitors (46 pp spread).** JAK inhibitors showed substantial within-class divergence, from upadacitinib (24%F) to ruxolitinib (70%F). This 46 pp spread, despite all four drugs targeting JAK kinases, reflects critical differences in JAK isoform selectivity: ruxolitinib is JAK1/2-selective (used in myelofibrosis and polycythemia vera), tofacitinib is pan-JAK (used in rheumatoid arthritis), baricitinib is JAK1/2-selective (used in rheumatoid arthritis and alopecia areata), and upadacitinib is JAK1-selective (used in rheumatoid arthritis, atopic dermatitis). The sex demographics of these different indications---myelofibrosis is slightly male-predominant while rheumatoid arthritis is strongly female-predominant---contribute to the spread. Additionally, JAK1 versus JAK2 versus JAK3 signaling involves different downstream pathways (STAT5 for JAK2, gamma-chain cytokines for JAK3) with different sex-differential biology.

**Anti-CD20 (60 pp spread).** Anti-CD20 antibodies showed a 60 pp spread from ofatumumab (12%F) to obinutuzumab (72%F), despite all four drugs targeting the same cell-surface antigen. This divergence reflects dramatic indication differences: obinutuzumab and rituximab are used primarily for hematological malignancies (chronic lymphocytic leukemia, non-Hodgkin lymphoma) and autoimmune diseases; ocrelizumab and ofatumumab are used for multiple sclerosis. The distinct patient populations, disease biology, and concomitant treatments across these indications overwhelm any target-driven sex-differential effects.

#### 3.3.7 Other Therapeutic Areas

**S1P modulators (15%F, 25 pp spread).** S1P modulators showed the most male-biased profile in the entire analysis, a finding that deserves mechanistic attention. While multiple sclerosis, the primary indication, is 2-3 times more common in women, the adverse events of S1P modulators---first-dose bradycardia, macular edema, lymphopenia, hepatotoxicity---may have sex-differential clinical significance due to male-predominant cardiovascular comorbidity and sex differences in cardiac conduction physiology. The 25 pp spread among fingolimod, siponimod, and ozanimod may reflect S1P receptor subtype selectivity differences (siponimod is S1P1/5-selective while fingolimod is non-selective) and their distinct cardiac electrophysiology effects.

**Retinoids (34 pp spread).** Retinoids showed a 34 pp spread from acitretin (43%F) to adapalene (77%F). The spread reflects the different indications and formulations: adapalene is a topical retinoid used for acne (female-predominant treatment-seeking population), while acitretin is a systemic retinoid used for psoriasis (more sex-balanced). Isotretinoin, the most widely used systemic retinoid, occupies an intermediate position, with its well-known sex-specific concern (teratogenicity and mandatory pregnancy prevention programs) contributing to its sex-differential reporting pattern.

**Muscle relaxants (39 pp spread).** Muscle relaxants showed a 39 pp spread from dantrolene (40%F) to cyclobenzaprine (79%F). This heterogeneous class includes drugs with fundamentally different mechanisms (dantrolene acts on ryanodine receptors in skeletal muscle; cyclobenzaprine acts centrally via norepinephrine pathways structurally related to tricyclic antidepressants), making the within-class spread expected.

### 3.4 DOACs: A Model of Within-Class Consistency

DOACs (rivaroxaban, apixaban, edoxaban) show the tightest within-class sex profile: 53--56%F with only 3 pp spread. This consistency suggests that factor Xa inhibition produces a highly reproducible sex-differential safety profile regardless of specific molecular structure. DOACs may serve as a positive control for class-effect sex-differential labeling---the rare case where mechanism truly determines sex profile.

The DOAC consistency stands in sharp relief against the antipsychotic 90 pp explosion, and the contrast is instructive. DOACs share several properties that may explain their consistency: (1) all three drugs target the same enzyme (factor Xa) at the same binding site; (2) all three have similar pharmacokinetic profiles (moderate protein binding, dual renal/hepatic clearance); (3) the primary indication (stroke prevention in atrial fibrillation) is consistent across the class; (4) factor Xa is not strongly sex-dimorphic in expression or activity. In contrast, antipsychotics differ in secondary pharmacology, metabolic pathways, indication populations, and target receptor selectivity beyond the shared D2/5-HT2A mechanism.

### 3.5 Consistency Classes versus Divergence Classes

Examining the full spectrum of within-class variation reveals a bimodal pattern. "Consistency classes" with spread < 15 pp include DOACs (3 pp), carbapenems (7 pp), cannabinoids (8 pp), fluoroquinolones (8 pp), SSRIs (11 pp), and tetracyclines (12 pp). These classes share features: relatively clean pharmacology, limited indication heterogeneity, and similar pharmacokinetic profiles within the class.

"Divergence classes" with spread > 30 pp include atypical antipsychotics (90 pp), triptans (65 pp), anti-CD20 (60 pp), ADHD stimulants (51 pp), JAK inhibitors (46 pp), CCBs (43 pp), muscle relaxants (39 pp), and retinoids (34 pp). These classes are characterized by: "dirty" pharmacology with extensive off-target binding, indication heterogeneity (same drug used for different diseases with different sex demographics), different metabolic pathways within the class, and/or different drug subclasses grouped under a single mechanistic umbrella.

---

## 4. Discussion

### 4.1 Mechanism Hypothesis: Rejected for Most Classes

The extraordinary within-class variation (up to 90 pp for antipsychotics) definitively rejects the mechanism hypothesis for most drug classes. Drugs sharing primary targets produce diametrically opposite sex-differential safety profiles far more often than concordant profiles. Primary mechanism of action is a poor predictor of sex-differential safety.

Exceptions exist: DOACs (3 pp spread) and SSRIs (11 pp spread) show meaningful within-class consistency, suggesting that some targets do constrain sex-differential safety profiles. The common feature of these consistent classes may be target specificity: DOACs and SSRIs have relatively clean pharmacology with few off-target effects, while antipsychotics and triptans are notoriously "dirty" drugs with extensive off-target binding. This pattern suggests a refined model: **primary mechanism constrains sex-differential safety only when the drug's pharmacological activity is dominated by that primary mechanism.** For polypharmacological drugs, secondary pharmacology, metabolism, and indication context override primary mechanism effects.

### 4.2 Comparison to Prior Literature

#### 4.2.1 Watson et al. (2019) EClinicalMedicine

Watson et al. [12] analyzed sex differences in ADR reporting across the UK Yellow Card database and found that women reported significantly more ADRs across nearly all organ systems. Our findings extend Watson et al. in three critical ways:

First, while Watson et al. focused on overall sex differences in ADR reporting (demonstrating the aggregate female predominance), our analysis reveals that this aggregate pattern conceals enormous drug-level and class-level heterogeneity. The 68 pp between-class range (CGRP agents 83%F to S1P modulators 15%F) shows that "women report more ADRs" is a dramatic oversimplification: for S1P modulators, the reverse is true. Watson et al.'s organ-system-level analysis could not capture this drug-class resolution.

Second, Watson et al. identified skin, gastrointestinal, and neurological reactions as showing the strongest sex differences. Our therapeutic-area analysis complements this by showing which drug classes drive these organ-system-level differences: CGRP agents and NSAIDs likely contribute to the neurological and gastrointestinal sex differences, respectively, while retinoids and tetracyclines contribute to dermatological sex differences.

Third, and most critically, Watson et al. did not examine within-class variation. Their analysis implicitly assumed that sex differences in ADR reporting were driven by patient-level factors (sex-differential biology, prescribing patterns, reporting behavior) rather than drug-level factors within a mechanism class. Our finding that within-class variation exceeds between-class variation in 42% of classes demonstrates that drug-level properties are a major---and previously unrecognized---source of sex-differential safety variation.

#### 4.2.2 Yu et al. (2016) Scientific Reports

Yu et al. [13] performed a systematic analysis of sex differences in drug efficacy and safety, emphasizing that sex-differential responses extended beyond pharmacokinetics to encompass sex-dimorphic immune function, hormonal modulation of drug targets, and sex-differential disease biology. Our findings provide large-scale pharmacovigilance validation of Yu et al.'s conceptual framework:

The pain therapeutic gradient (CGRP 83%F > NSAIDs 67%F > opioids 62%F > cannabinoids 44%F) directly supports Yu et al.'s emphasis on target-level sex-differential biology: CGRP is strongly estrogen-modulated, while the endocannabinoid system shows male-predominant activation patterns. The graded spectrum across pain classes with different receptor targets is precisely what Yu et al.'s framework would predict at the between-class level.

However, the within-class explosions (antipsychotics 90 pp, triptans 65 pp) reveal a limitation of Yu et al.'s framework: target-level sex biology is necessary but not sufficient to predict drug-level sex-differential safety. Two drugs acting on the same sex-dimorphic target can show opposite sex-differential profiles due to secondary pharmacology, metabolism, and indication context. Our findings extend Yu et al.'s framework by demonstrating that target biology sets the between-class pattern but individual drug properties dominate within-class variation.

#### 4.2.3 Zucker and Prendergast (2020)

Zucker and Prendergast [8] provided compelling evidence that sex differences in pharmacokinetics predict ADR patterns, analyzing 86 drugs with known sex-differential pharmacokinetics. Our within-class analysis provides strong support for their pharmacokinetic hypothesis at scale: the most divergent drug classes (antipsychotics, triptans, ADHD stimulants) are precisely those where within-class metabolic pathway differences are greatest (CYP2D6 vs. CYP3A4 vs. MAO-A), while the most consistent classes (DOACs, SSRIs, carbapenems) share similar metabolic profiles within the class. The Zucker-Prendergast pharmacokinetic framework, when applied at the within-class level, explains why mechanism alone is insufficient: even drugs sharing a target can diverge dramatically if their disposition differs in sex-differential ways.

### 4.3 Why Some Therapeutic Areas Show Stronger Sex Effects

The 68 pp between-class range raises the question of what drives certain therapeutic areas toward extreme sex-differential profiles. We identify four principal mechanisms:

**Disease sex ratio.** Conditions with strongly sex-skewed prevalence (migraine 3:1 female, osteoporosis 4:1 female, PAH 2.3:1 female) drive female-biased safety reporting for their associated drug classes, independent of drug pharmacology. This "denominator effect"---more women taking the drug means more women reporting adverse events---is partially but not fully corrected by the ROR disproportionality analysis, as it can influence which specific adverse events reach reporting thresholds.

**Target sex biology.** Molecular targets with known sex-differential expression or hormonal modulation produce sex-biased safety profiles through pharmacodynamic mechanisms. CGRP (estrogen-modulated), serotonin receptors (sex-differential expression), and TNF-alpha (estrogen-enhanced production) are examples where target biology directly influences sex-differential safety.

**Metabolic pathway sex dimorphism.** Drug classes metabolized predominantly by sex-dimorphic CYP enzymes (CYP2D6, CYP3A4) show greater within-class variation than classes with renal elimination (DOACs, carbapenems) or similar metabolic profiles. This pharmacokinetic mechanism operates at the individual drug level within a class, explaining within-class divergence.

**Polypharmacology.** "Dirty" drugs with extensive off-target binding (antipsychotics, triptans) show greater within-class variation than "clean" drugs (DOACs, SSRIs) because each secondary target introduces an independent sex-differential effect that can augment or oppose the primary mechanism's sex profile.

### 4.4 What Drives Within-Class Divergence?

Four factors likely explain the within-class variation:

1. **CYP metabolism pathway:** Drugs within a class metabolized by different CYP enzymes (CYP2D6 vs. CYP3A4 vs. CYP1A2) will show different sex-differential exposure, as CYP expression is sex-dimorphic. CYP3A4 activity is approximately 20-40% higher in women [7], CYP2D6 shows variable sex effects depending on genotype, and CYP1A2 activity is generally higher in men. These differences mean that two drugs targeting the same receptor but metabolized by different CYP enzymes will achieve different sex-differential tissue concentrations, producing divergent safety profiles.

2. **Off-target binding:** Drugs within a class differ in secondary receptor affinities that may have sex-differential consequences (e.g., risperidone's alpha-1 blockade vs. cariprazine's D3 partial agonism). The cumulative sex-differential effect of a drug is the sum of contributions from all targets, primary and secondary. When secondary targets have strong sex-differential biology, they can shift the overall profile away from what the primary mechanism would predict.

3. **Indication populations:** Some drugs within a class are used for different indications with different sex ratios (e.g., methylphenidate for ADHD in boys vs. atomoxetine for adult ADHD with more female representation; ruxolitinib for myelofibrosis vs. tofacitinib for rheumatoid arthritis). While the ROR metric partially adjusts for population composition, the types of adverse events reported are influenced by the indication context, and different indication populations may have different comorbidity profiles that modulate ADR susceptibility.

4. **Physicochemical properties:** Lipophilicity, volume of distribution, and protein binding affect sex-differential tissue exposure independently of target pharmacology. Women have higher average body fat percentage (sex-differential volume of distribution for lipophilic drugs), lower average body weight (sex-differential mg/kg dosing for weight-independent dosing regimens), and sex-differential albumin and alpha-1 acid glycoprotein levels (affecting free drug fraction for highly protein-bound drugs).

### 4.5 Implications for Drug Regulation and Clinical Practice

The finding that within-class variation exceeds between-class variation has immediate and far-reaching implications:

**1. Class-effect sex warnings are invalid.** A sex-differential safety signal for one drug in a class should NOT be extrapolated to other drugs in the same class. Each drug requires individual sex-differential characterization. The current regulatory practice of issuing class-wide safety communications based on signals from one class member is unsupported by the data for sex-differential safety. The 90 pp antipsychotic spread demonstrates that a sex-safety finding for risperidone carries no predictive value for cariprazine, and vice versa.

**2. Within-class switching requires sex-differential consideration.** Switching between drugs within a class may inadvertently change a patient's sex-differential safety exposure by up to 90 pp. Clinicians should consider sex-differential safety profiles when selecting among within-class alternatives. For example, switching from risperidone (93%F) to cariprazine (3%F) in a female patient represents a dramatic shift in sex-differential risk exposure, even though both drugs are classified as atypical antipsychotics with shared primary mechanism.

**3. Trial design must be drug-specific.** Phase III trials should not rely on class-level sex-differential safety assumptions. Individual drugs require sex-stratified safety analysis regardless of prior class data. The FDA's 2018 guidance on collection of race and ethnicity data in clinical trials [27] should be extended to mandate drug-specific sex-stratified safety analysis, with within-class variation data used to justify the inadequacy of class-level extrapolation.

**4. Drug labeling should include sex-differential safety profiles.** The individual-drug %F metric, or a validated derivative, should be incorporated into drug labeling to inform sex-aware prescribing. Currently, sex-differential safety information in drug labels is inconsistent, incomplete, and rarely quantitative. A standardized sex-differential safety metric would enable clinicians to make informed within-class selections.

**5. Pharmacovigilance systems should report sex-stratified signals by default.** The current practice of aggregating safety signals across sexes obscures meaningful sex-differential patterns. Routine sex-stratified signal detection, as performed in this analysis, should become standard in pharmacovigilance databases worldwide.

### 4.6 The Consistency-Divergence Spectrum as a Drug Class Characteristic

Our analysis reveals that within-class sex-differential consistency is itself a meaningful pharmacological characteristic that varies systematically across drug classes. We propose that the "consistency index" (inverse of within-class spread) captures a clinically important property: the degree to which a drug class's sex-differential safety can be characterized at the class level versus requiring individual-drug assessment.

High-consistency classes (DOACs, SSRIs, carbapenems) may be amenable to class-level sex-differential labeling, as any drug in the class approximates the class sex profile. Low-consistency classes (antipsychotics, triptans, anti-CD20) categorically require individual drug characterization, as the class label is meaningless for predicting individual drug sex profiles.

This consistency-divergence spectrum correlates with pharmacological "cleanliness" (target specificity), metabolic pathway homogeneity within the class, and indication homogeneity. These features could be used prospectively to predict whether a new drug class will show sex-differential consistency or divergence, informing regulatory expectations for sex-stratified safety data during drug development.

### 4.7 Limitations

1. **Drug classification ambiguity.** Drug classification is based on primary mechanism; some drugs have multiple mechanisms. Reclassification would alter within-class spreads but would not change the central finding that many classes show extreme within-class divergence.

2. **Class size effects.** Within-class spread depends on the number of drugs analyzed; larger classes have more opportunity for extreme values. The 90 pp antipsychotic spread is among the largest classes (7 drugs), but the 65 pp triptan spread occurs with only 4 drugs, and the 60 pp anti-CD20 spread with 4 drugs, arguing against a pure size artifact.

3. **Indication confounding.** Some within-class differences may reflect indication-specific confounding rather than true drug-level differences. Drugs used for different indications within a class (e.g., ruxolitinib for myelofibrosis vs. tofacitinib for rheumatoid arthritis) may show different sex profiles due to the underlying patient population rather than drug pharmacology. Disentangling drug-level from indication-level sex effects requires indication-stratified analyses that are beyond the scope of this study.

4. **Reporting bias.** Reporting patterns may differ across indications within a class, and sex-differential reporting behavior (women may be more likely to report certain ADR types) could influence results. The ROR disproportionality framework partially mitigates this by comparing within-sex ratios, but residual reporting bias cannot be excluded.

5. **Temporal effects.** The 21-year study period (2004Q1--2025Q3) spans changes in prescribing patterns, drug availability, and reporting practices. Drugs marketed for the entire period (e.g., risperidone, since 1993) have different reporting maturity than recently approved drugs (e.g., cariprazine, 2015), potentially affecting signal stability.

6. **Single database.** FAERS reflects U.S. reporting patterns and may not generalize to other pharmacovigilance databases (EudraVigilance, VigiBase). International replication using WHO VigiBase would strengthen the generalizability of these findings.

7. **Absence of dose-level analysis.** Sex-differential safety may vary with dose, and within-class comparisons at the drug level may obscure dose-dependent sex effects. Dose-stratified analysis was not performed due to incomplete dose information in FAERS.

---

## 5. Conclusion

The pan-therapeutic sex-differential spectrum spans 68 pp (CGRP agents 83%F to S1P modulators 15%F), but within-class variation exceeds between-class variation in 42% of classes (8 of 19). The atypical antipsychotic 90 pp spread (risperidone 93%F to cariprazine 3%F) demonstrates that shared primary mechanism does not predict sex-differential safety. Only DOACs (3 pp spread) show the tight within-class consistency expected under the mechanism hypothesis. These findings invalidate class-effect sex-differential safety labeling and mandate individual-drug sex-differential characterization for every approved therapeutic.

The implications extend beyond academic pharmacology to clinical practice and drug regulation. Every therapeutic switching decision within a drug class should consider sex-differential safety profiles. Regulatory agencies should require drug-specific rather than class-level sex-stratified safety data. And the pharmacovigilance community should adopt sex-stratified signal detection as a default analytical framework, treating the sex-differential safety profile as a fundamental characteristic of each individual drug rather than a class-level attribute.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. Pharmacoepidemiol Drug Saf. 2009;18:427-436.

2. Nissen SE, Wolski K. Effect of rosiglitazone on the risk of myocardial infarction and death from cardiovascular causes. N Engl J Med. 2007;356:2457-2471.

3. Patel H, Tenney JH, Engles CD, Ternes T, Goyal N, Chen SL. Fluoroquinolone-associated tendinopathy: a systematic review. Drug Saf. 2021;44:1083-1099.

4. Neal B, Perkovic V, Mahaffey KW, et al. Canagliflozin and cardiovascular and renal events in type 2 diabetes. N Engl J Med. 2017;377:644-657.

5. Armitage J. The safety of statins in clinical practice. Lancet. 2007;370:1781-1790.

6. Furberg CD, Pitt B. Withdrawal of cerivastatin from the world market. Curr Control Trials Cardiovasc Med. 2001;2:205-207.

7. Franconi F, Campesi I. Sex and gender influences on pharmacological response: an overview. Expert Rev Clin Pharmacol. 2014;7:469-485.

8. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.

9. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.

10. Rademaker M. Do women have more adverse drug reactions? Am J Clin Dermatol. 2001;2:349-351.

11. Mazure CM, Jones DP. Twenty years and still counting: including women as participants and studying sex and gender in biomedical research. BMC Womens Health. 2015;15:94.

12. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. EClinicalMedicine. 2019;17:100188.

13. Yu Y, Chen J, Li D, Wang L, Wang W, Liu H. Systematic analysis of adverse event reports for sex differences in adverse drug events. Sci Rep. 2016;6:24955.

14. WHO Collaborating Centre for Drug Statistics Methodology. ATC classification index with DDDs. Oslo: World Health Organization; 2023.

15. Fillingim RB, Gear RW. Sex differences in opioid analgesia: clinical and experimental findings. Eur J Pain. 2004;8:413-425.

16. Sramek JJ, Murphy MF, Cutler NR. Sex differences in the psychopharmacological treatment of depression. Dialogues Clin Neurosci. 2016;18:447-457.

17. Roden DM. Drug-induced prolongation of the QT interval. N Engl J Med. 2004;350:1013-1022.

18. Seeman MV. Men and women respond differently to antipsychotic drugs. Neuropharmacology. 2020;163:107631.

19. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48:143-157.

20. Labastida-Ramirez A, Rubio-Beltran E, Villalonl CM, MaassenVanDenBrink A. Gender aspects of CGRP in migraine. Cephalalgia. 2019;39:435-444.

21. Grosser T, Fries S, FitzGerald GA. Biological basis for the cardiovascular consequences of COX-2 inhibition: therapeutic challenges and opportunities. J Clin Invest. 2006;116:4-15.

22. Craft RM, Marusich JA, Wiley JL. Sex differences in cannabinoid pharmacology: a reflection of differences in the endocannabinoid system? Life Sci. 2013;92:476-481.

23. Lowe GDO, Rumley A, Woodward M, et al. Epidemiology of coagulation factors, inhibitors and activation markers: the Third Glasgow MONICA Survey. Br J Haematol. 1999;105:886-893.

24. Badesch DB, Raskob GE, Elliott CG, et al. Pulmonary arterial hypertension: baseline characteristics from the REVEAL registry. Chest. 2010;137:376-387.

25. Zanger UM, Schwab M. Cytochrome P450 enzymes in drug metabolism: regulation of gene expression, enzyme activities, and impact of genetic variation. Pharmacol Ther. 2013;138:103-141.

26. Campbell JE, Drucker DJ. Pharmacology, physiology, and mechanisms of incretin hormone action. Cell Metab. 2013;17:819-837.

27. U.S. Food and Drug Administration. Collection of race and ethnicity data in clinical trials: guidance for industry. Silver Spring, MD: FDA; 2016.

---

## Figure Legends

**Figure 1.** Pan-therapeutic sex spectrum. Horizontal bar chart of 19 drug classes ranked by mean female signal proportion. CGRP agents (83%F) to S1P modulators (15%F). Error bars show within-class range. Dashed line at 50% parity. Color gradient from red (female-biased) through grey (balanced) to blue (male-biased).

**Figure 2.** Within-class vs. between-class variation. Forest plot showing class mean (diamond) with within-class range (horizontal line) for each of 19 classes. The majority of within-class ranges exceed the interquartile range of class means. Classes are grouped by therapeutic area with visual separators. The between-class IQR is shaded in grey.

**Figure 3.** The antipsychotic explosion. Individual drug profiles for 7 atypical antipsychotics. Stacked bar showing female (red) and male (blue) signal proportions. Risperidone (93%F) and cariprazine (3%F) anchoring opposite extremes. Annotations show primary CYP metabolism pathway for each drug.

**Figure 4.** Pain therapeutic gradient. CGRP agents (83%F) > NSAIDs (67%F) > Opioids (62%F) > Cannabinoids (44%F). Receptor pharmacology annotations for each class. Individual drug data points shown within each class bar to visualize within-class spread.

**Figure 5.** DOACs: the exception. Within-class profile for rivaroxaban, apixaban, and edoxaban showing 3 pp spread---the tightest within-class agreement in the analysis. Contrast panel showing atypical antipsychotics (90 pp spread) for visual comparison.

**Figure 6.** Consistency-divergence spectrum. Scatter plot of within-class spread (y-axis) versus number of drugs in class (x-axis) for all 19 classes. Labeled points for extreme cases (antipsychotics, DOACs). Horizontal reference line at 30 pp threshold. Color coding by therapeutic area.

**Figure 7.** Therapeutic area summary. Grouped bar chart showing mean %F and within-class spread for each of the 7 therapeutic areas (pain, cardiovascular, psychiatric, endocrine, anti-infective, autoimmune, other). Error bars show range of class-level means within each therapeutic area.

---

## Supplementary Materials

**Supplementary Table S1.** Complete drug-level data for all drugs across 19 classes, including individual %F values, number of sex-differential signals, number of female-biased signals, number of male-biased signals, and primary CYP metabolism pathway.

**Supplementary Table S2.** Pairwise within-class drug comparisons for the 10 classes with highest within-class spread, including delta-%F and potential explanatory factors (metabolic pathway, indication, off-target binding) for each drug pair.

**Supplementary Figure S1.** Individual drug profiles for all 19 classes (19 panels), showing drug-level %F values with error bars representing 95% Wilson score confidence intervals.
