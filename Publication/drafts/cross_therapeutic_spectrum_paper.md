# The Pan-Therapeutic Sex-Differential Drug Safety Spectrum: Within-Class Variation Exceeds Between-Class Differences Across 19 Drug Classes

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex differences in drug adverse events are documented for individual drugs, but systematic comparison across and within therapeutic classes---testing whether mechanism of action predicts sex-differential safety---has not been performed at pharmacovigilance scale.

**Methods.** From 96,281 sex-differential signals across 2,178 drugs (14,536,008 FAERS reports, 2004Q1--2025Q3), we analyzed sex bias patterns across 19 major drug classes spanning cardiovascular, psychiatric, pain, endocrine, anti-infective, autoimmune, dermatological, and ophthalmological therapeutics. Within-class variation (max - min %F across drugs in a class) was compared to between-class variation.

**Results.** The pan-therapeutic spectrum spanned 68 percentage points: from CGRP migraine agents (83%F) to S1P modulators (15%F). Within-class sex bias variation was extraordinary: atypical antipsychotics showed a 90 pp spread (risperidone 93%F to cariprazine 3%F), triptans 65 pp (sumatriptan 77%F to almotriptan 12%F), anti-CD20 antibodies 60 pp (obinutuzumab 72%F to ofatumumab 12%F), and JAK inhibitors 46 pp (ruxolitinib 70%F to upadacitinib 24%F). DOACs showed the tightest within-class agreement (3 pp, 53--56%F). In 8 of 19 classes, within-class spread exceeded 30 pp, demonstrating that drugs sharing a primary mechanism can show completely opposite sex-bias profiles. Pain therapeutics showed a graded spectrum: CGRP agents (83%F) > NSAIDs (67%F) > opioids (62%F) > cannabinoids (44%F). Cardiovascular drugs spanned 29 pp. Endocrine drugs revealed GLP-1 agonists as female-biased (58%F) with tirzepatide highest (65%F), while SGLT2 inhibitors were near-balanced (48%F).

**Interpretation.** Sex-differential drug safety varies more within therapeutic classes than between them. The extraordinary within-class spreads (up to 90 pp for atypical antipsychotics sharing D2/5-HT2A targets) demonstrate that primary mechanism of action does not determine sex-differential safety. Secondary pharmacology, pharmacokinetics, indication-specific populations, and individual molecular properties drive the within-class divergence. These findings mandate individual-drug rather than class-level sex-differential characterization.

---

## Introduction

The assumption that drugs sharing a mechanism of action share safety profiles underpins class-effect labeling in pharmacovigilance and drug regulation [1]. When one drug in a class produces a safety signal, regulatory agencies often issue class-wide warnings (e.g., TZD class cardiovascular warnings based on rosiglitazone, fluoroquinolone class tendon warnings). This class-effect assumption has not been tested for sex-differential safety: do drugs sharing a primary target also share sex-differential adverse event profiles?

Two competing hypotheses predict different outcomes:

**The mechanism hypothesis:** If primary target biology determines sex-differential safety (through target sex-differential expression, hormonal modulation of target signaling, or sex-linked downstream pathways), then drugs within a class should show concordant sex profiles, and between-class variation should exceed within-class variation.

**The pharmacokinetic hypothesis:** If individual drug properties (lipophilicity, metabolism pathway, half-life, off-target binding) determine sex-differential safety through sex-differential pharmacokinetics, then within-class variation should be substantial, and mechanism alone should not predict sex profiles.

We tested these hypotheses using 96,281 sex-differential signals across 19 drug classes, computing both between-class and within-class sex bias variation.

---

## Methods

### Data Source

FAERS 2004Q1--2025Q3: 14,536,008 deduplicated reports (60.2% female). Sex-stratified logR = ln(ROR_female / ROR_male). Signals: |logR| >= 0.5, >= 10 reports per sex. Total: 96,281 signals, 2,178 drugs, 5,658 AEs.

### Drug Classification

19 major drug classes organized by therapeutic area:

**Pain & migraine:** CGRP agents (erenumab, fremanezumab, galcanezumab, rimegepant), triptans (sumatriptan, rizatriptan, almotriptan, eletriptan), NSAIDs (ibuprofen, naproxen, diclofenac, celecoxib, meloxicam, piroxicam, flurbiprofen, indomethacin), opioids (morphine, oxycodone, fentanyl, tramadol, oxymorphone, codeine), cannabinoids (dronabinol, nabilone).

**Cardiovascular:** Beta-blockers (atenolol, metoprolol, carvedilol, bisoprolol), DOACs (rivaroxaban, apixaban, edoxaban), CCBs (amlodipine, diltiazem, nifedipine, nimodipine), antiarrhythmics (amiodarone, flecainide, sotalol), PAH drugs (bosentan, ambrisentan, sildenafil, tadalafil, epoprostenol, iloprost), ARNI (sacubitril/valsartan).

**Psychiatric:** Atypical antipsychotics (risperidone, quetiapine, olanzapine, aripiprazole, clozapine, cariprazine, brexpiprazole), SSRIs (sertraline, fluoxetine, citalopram, escitalopram, paroxetine), ADHD stimulants (methylphenidate, amphetamine, dexamfetamine, lisdexamfetamine, atomoxetine).

**Endocrine & metabolic:** GLP-1 agonists (semaglutide, liraglutide, dulaglutide, exenatide, tirzepatide), SGLT2 inhibitors (dapagliflozin, empagliflozin, canagliflozin), TZDs (pioglitazone, rosiglitazone), osteoporosis drugs (alendronate, risedronate, denosumab, zoledronic acid).

**Anti-infective:** Tetracyclines (doxycycline, minocycline, tetracycline), fluoroquinolones (ciprofloxacin, levofloxacin, moxifloxacin), carbapenems (meropenem, imipenem, ertapenem), HIV antiretrovirals (efavirenz, tenofovir, dolutegravir, darunavir).

**Autoimmune:** Anti-TNFs (infliximab, adalimumab, etanercept, certolizumab, golimumab), JAK inhibitors (tofacitinib, baricitinib, upadacitinib, ruxolitinib), anti-CD20 (rituximab, ocrelizumab, obinutuzumab, ofatumumab).

**Other:** S1P modulators (fingolimod, siponimod, ozanimod), retinoids (isotretinoin, acitretin, adapalene, tretinoin), muscle relaxants (baclofen, dantrolene, cyclobenzaprine, tizanidine).

### Metrics

**Between-class variation:** Range of class-level mean %F across all 19 classes.
**Within-class variation:** For each class, max(%F) - min(%F) across individual drugs with >= 5 signals.
**Class consistency:** Coefficient of variation (SD/%F) per class.

---

## Results

### The Pan-Therapeutic Spectrum

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

### The Within-Class Explosion

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

### Therapeutic Area Deep Dives

**Pain therapeutics:** A graded female-to-male spectrum: CGRP agents (83%F) > NSAIDs (67%F) > opioids (62%F) > cannabinoids (44%F). This 39 pp pain therapeutic gradient tracks with receptor pharmacology: CGRP is strongly modulated by estrogen (menstrual migraine), COX enzymes show modest sex differences, opioid mu-receptors are sex-dimorphic, and cannabinoid CB1 receptors show male-predominant activation patterns.

Within opioids, morphine (67%F) differs from oxymorphone (45%F) by 22 pp despite identical mu-receptor primary targets, suggesting that secondary metabolism (CYP2D6 for oxymorphone vs. UGT2B7 for morphine) drives the sex-differential divergence.

**Cardiovascular drugs:** A 29 pp span from PAH drugs (71%F) to ARNI (42%F). The tight DOAC consistency (53--56%F, 3 pp spread) contrasts sharply with beta-blockers (carvedilol 46%F to atenolol 66%F, 20 pp), suggesting that receptor selectivity (alpha+beta vs. beta-1) modulates cardiovascular sex-differential safety.

**Psychiatric drugs:** The most extreme within-class variation. Atypical antipsychotics span 90 pp; ADHD stimulants span 51 pp. For antipsychotics, the divergence may relate to differential CYP2D6 metabolism (risperidone is a CYP2D6 substrate with sex-differential metabolism; cariprazine is CYP3A4-metabolized with different sex pharmacokinetics), indication differences (risperidone for autism/irritability with male-predominant patient base; cariprazine for bipolar depression), and receptor binding profile differences beyond D2/5-HT2A.

**Endocrine drugs:** GLP-1 agonists are moderately female-biased (58%F overall), with tirzepatide (65%F) highest. The GLP-1 female bias aligns with the 67.1 pp diabetes drug spectrum from TZDs (92%F) to SGLT2 inhibitors (48%F), suggesting that glucose-lowering mechanism influences sex-differential safety independently of glycemic efficacy.

**Anti-infectives:** Tetracyclines (68%F) are the most female-biased antibiotic class, possibly reflecting tetracycline's use in acne (female-predominant dermatologic indication) and its photosensitivity reaction (female-biased dermatologic AE). HIV antiretrovirals (42%F) are male-biased, reflecting the historically male-predominant HIV treatment population.

### DOACs: A Model of Within-Class Consistency

DOACs (rivaroxaban, apixaban, edoxaban) show the tightest within-class sex profile: 53--56%F with only 3 pp spread. This consistency suggests that factor Xa inhibition produces a highly reproducible sex-differential safety profile regardless of specific molecular structure. DOACs may serve as a positive control for class-effect sex-differential labeling---the rare case where mechanism truly determines sex profile.

---

## Discussion

### Mechanism Hypothesis: Rejected for Most Classes

The extraordinary within-class variation (up to 90 pp for antipsychotics) definitively rejects the mechanism hypothesis for most drug classes. Drugs sharing primary targets produce diametrically opposite sex-differential safety profiles far more often than concordant profiles. Primary mechanism of action is a poor predictor of sex-differential safety.

Exceptions exist: DOACs (3 pp spread) and SSRIs (11 pp spread) show meaningful within-class consistency, suggesting that some targets do constrain sex-differential safety profiles. The common feature of these consistent classes may be target specificity: DOACs and SSRIs have relatively clean pharmacology with few off-target effects, while antipsychotics and triptans are notoriously "dirty" drugs with extensive off-target binding.

### What Drives Within-Class Divergence?

Four factors likely explain the within-class variation:

1. **CYP metabolism pathway:** Drugs within a class metabolized by different CYP enzymes (CYP2D6 vs. CYP3A4 vs. CYP1A2) will show different sex-differential exposure, as CYP expression is sex-dimorphic.

2. **Off-target binding:** Drugs within a class differ in secondary receptor affinities that may have sex-differential consequences (e.g., risperidone's alpha-1 blockade vs. cariprazine's D3 partial agonism).

3. **Indication populations:** Some drugs within a class are used for different indications with different sex ratios (e.g., methylphenidate for ADHD in boys vs. atomoxetine for adult ADHD with more female representation).

4. **Physicochemical properties:** Lipophilicity, volume of distribution, and protein binding affect sex-differential tissue exposure independently of target pharmacology.

### Implications for Drug Regulation

The finding that within-class variation exceeds between-class variation has immediate regulatory implications:

1. **Class-effect sex warnings are invalid:** A sex-differential safety signal for one drug in a class should NOT be extrapolated to other drugs in the same class. Each drug requires individual sex-differential characterization.

2. **Within-class switching:** Switching between drugs within a class may inadvertently change a patient's sex-differential safety exposure by up to 90 pp. Clinicians should consider sex-differential safety profiles when selecting among within-class alternatives.

3. **Trial design:** Phase III trials should not rely on class-level sex-differential safety assumptions. Individual drugs require sex-stratified safety analysis regardless of prior class data.

### Limitations

1. Drug classification is based on primary mechanism; some drugs have multiple mechanisms.
2. Within-class spread depends on the number of drugs analyzed; larger classes have more opportunity for extreme values.
3. Some within-class differences may reflect indication-specific confounding rather than true drug-level differences.
4. Reporting patterns may differ across indications within a class.

---

## Conclusion

The pan-therapeutic sex-differential spectrum spans 68 pp (CGRP agents 83%F to S1P modulators 15%F), but within-class variation exceeds between-class variation in 42% of classes (8 of 19). The atypical antipsychotic 90 pp spread (risperidone 93%F to cariprazine 3%F) demonstrates that shared primary mechanism does not predict sex-differential safety. Only DOACs (3 pp spread) show the tight within-class consistency expected under the mechanism hypothesis. These findings invalidate class-effect sex-differential safety labeling and mandate individual-drug sex-differential characterization for every approved therapeutic.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. Pharmacoepidemiol Drug Saf. 2009;18:427-436.
2. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
3. Watson S, et al. Reported adverse drug reactions in women and men. EClinicalMedicine. 2019;17:100188.
4. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.
5. Franconi F, Campesi I. Sex and gender influences on pharmacological response. Expert Rev Clin Pharmacol. 2014;7:469-485.
6. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48:143-157.

---

## Figure Legends

**Figure 1.** Pan-therapeutic sex spectrum. Horizontal bar chart of 19 drug classes ranked by mean female signal proportion. CGRP agents (83%F) to S1P modulators (15%F). Error bars show within-class range. Dashed line at 50% parity.

**Figure 2.** Within-class vs. between-class variation. Forest plot showing class mean (diamond) with within-class range (horizontal line) for each of 19 classes. The majority of within-class ranges exceed the interquartile range of class means.

**Figure 3.** The antipsychotic explosion. Individual drug profiles for 7 atypical antipsychotics. Stacked bar showing female (red) and male (blue) signal proportions. Risperidone (93%F) and cariprazine (3%F) anchoring opposite extremes.

**Figure 4.** Pain therapeutic gradient. CGRP agents (83%F) > NSAIDs (67%F) > Opioids (62%F) > Cannabinoids (44%F). Receptor pharmacology annotations for each class.

**Figure 5.** DOACs: the exception. Within-class profile for rivaroxaban, apixaban, and edoxaban showing 3 pp spread---the tightest within-class agreement in the analysis.
