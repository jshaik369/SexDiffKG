# The Pan-Therapeutic Sex-Differential Drug Safety Spectrum: Within-Class Variation Exceeds Between-Class Differences Across 19 Drug Classes

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex differences in drug adverse events are documented for individual drugs, but systematic comparison across and within therapeutic classes---testing whether mechanism of action predicts sex-differential safety---has not been performed at pharmacovigilance scale. Regulatory agencies routinely issue class-wide safety warnings when a signal emerges for one member of a drug class, yet the validity of extending such class-effect assumptions to sex-differential safety profiles has never been empirically tested across the full therapeutic spectrum.

**Methods.** From 96,281 sex-differential signals across 2,178 drugs (14,536,008 FAERS reports, 2004Q1--2025Q3), we analyzed sex bias patterns across 19 major drug classes spanning cardiovascular, psychiatric, pain, endocrine, anti-infective, autoimmune, dermatological, and ophthalmological therapeutics. Sex-stratified reporting odds ratios (ROR) were computed for each drug-adverse event pair, and the log-ratio logR = ln(ROR_female / ROR_male) was used to classify signals as female-biased (logR > 0.5) or male-biased (logR < -0.5). Within-class variation (max - min %F across drugs in a class) was compared to between-class variation (range of class-level mean %F across all 19 classes).

**Results.** The pan-therapeutic spectrum spanned 68 percentage points: from CGRP migraine agents (83%F) to S1P modulators (15%F). Within-class sex bias variation was extraordinary: atypical antipsychotics showed a 90 pp spread (risperidone 93%F to cariprazine 3%F), triptans 65 pp (sumatriptan 77%F to almotriptan 12%F), anti-CD20 antibodies 60 pp (obinutuzumab 72%F to ofatumumab 12%F), and JAK inhibitors 46 pp (ruxolitinib 70%F to upadacitinib 24%F). DOACs showed the tightest within-class agreement (3 pp, 53--56%F). In 8 of 19 classes, within-class spread exceeded 30 pp, demonstrating that drugs sharing a primary mechanism can show completely opposite sex-bias profiles. Pain therapeutics showed a graded spectrum: CGRP agents (83%F) > NSAIDs (67%F) > opioids (62%F) > cannabinoids (44%F). Cardiovascular drugs spanned 29 pp. Endocrine drugs revealed GLP-1 agonists as female-biased (58%F) with tirzepatide highest (65%F), while SGLT2 inhibitors were near-balanced (48%F).

**Interpretation.** Sex-differential drug safety varies more within therapeutic classes than between them. The extraordinary within-class spreads (up to 90 pp for atypical antipsychotics sharing D2/5-HT2A targets) demonstrate that primary mechanism of action does not determine sex-differential safety. Secondary pharmacology, pharmacokinetics, indication-specific populations, and individual molecular properties drive the within-class divergence. These findings mandate individual-drug rather than class-level sex-differential characterization, with direct implications for regulatory labeling, prescribing guidelines, and clinical trial design.

**Keywords:** sex differences; adverse drug reactions; pharmacovigilance; FAERS; drug safety; class effects; therapeutic spectrum; reporting odds ratio

---

## 1. Introduction

### 1.1 The Class-Effect Paradigm in Drug Safety

The assumption that drugs sharing a mechanism of action share safety profiles underpins class-effect labeling in pharmacovigilance and drug regulation [1]. When one drug in a class produces a safety signal, regulatory agencies often issue class-wide warnings (e.g., TZD class cardiovascular warnings based on rosiglitazone [2], fluoroquinolone class tendon warnings [3], SGLT2 inhibitor amputation warnings initially based on canagliflozin data [4]). This regulatory framework reflects a reasonable pharmacological prior: drugs binding the same primary target activate similar downstream signaling cascades and should, in principle, produce similar adverse event spectra.

The class-effect paradigm has served drug safety well in many contexts. Statins share class-level hepatotoxicity and myopathy risks [5], and ACE inhibitors share class-level angioedema and cough liabilities. However, notable exceptions have challenged class-effect universality: cerivastatin's rhabdomyolysis risk far exceeded that of other statins [6], and rosiglitazone's cardiovascular risk was not shared by pioglitazone [2], demonstrating that individual molecular properties can override class-level pharmacology for specific safety endpoints. This class-effect assumption has not been tested for sex-differential safety: do drugs sharing a primary target also share sex-differential adverse event profiles?

### 1.2 Sex Differences in Drug Safety: Prior Systematic Analyses

Sex differences in adverse drug reactions (ADRs) have emerged as a major concern in pharmacovigilance [7,8]. Women experience approximately 1.5- to 1.7-fold higher rates of ADRs compared to men across multiple studies [9,10], a disparity attributed to pharmacokinetic differences (lower body weight, higher body fat percentage, sex-differential CYP enzyme expression, hormonal modulation of drug metabolism), pharmacodynamic differences (sex-differential receptor expression and signaling), and historically inadequate female representation in clinical trials [11].

Watson et al. (2019) conducted one of the most comprehensive analyses to date, examining sex differences in ADR reporting across 12 major organ systems using the UK Yellow Card pharmacovigilance database [12]. Their study demonstrated that women reported significantly more ADRs across nearly all organ systems, with particularly pronounced differences for skin, gastrointestinal, and neurological reactions. Critically, Watson et al. identified that these differences persisted after adjusting for prescription frequency, suggesting biological rather than purely exposure-driven mechanisms. However, their organ-system-level approach could not resolve whether sex differences arose from class-level or drug-level properties.

Yu et al. (2016) performed a systematic analysis of sex differences in drug efficacy and safety using data from clinical trials and post-marketing surveillance [13]. Their work in *Scientific Reports* highlighted that sex-differential drug responses extended beyond pharmacokinetic differences, implicating sex-dimorphic immune function, hormonal modulation of drug targets, and sex-differential disease biology as contributing mechanisms. These findings underscored the need for sex-stratified pharmacovigilance at scale but did not address within-class variation.

Zucker and Prendergast (2020) provided a landmark review demonstrating that sex differences in pharmacokinetics---particularly in cytochrome P450 enzyme activity, renal clearance, and drug transporter expression---could predict sex-differential ADR patterns [8]. Their analysis of 86 drugs with known sex-differential pharmacokinetics showed that women experienced higher drug exposure for the majority, providing a mechanistic basis for sex-differential safety signals and raising the critical question of whether drugs sharing a primary mechanism but differing in metabolic pathways would show divergent sex-differential profiles.

### 1.3 The ATC Classification System and Its Limitations

The Anatomical Therapeutic Chemical (ATC) classification system, maintained by the WHO Collaborating Centre for Drug Statistics Methodology, provides a hierarchical framework for organizing drugs by therapeutic indication and mechanism of action [14]. At the first level, the ATC system defines 14 main anatomical/pharmacological groups (e.g., A = Alimentary tract, C = Cardiovascular, N = Nervous system), with successive levels specifying therapeutic, pharmacological, and chemical subgroups down to individual substances.

While the ATC system offers a standardized framework, it was not designed to capture modern polypharmacology. For this analysis, we employed a pharmacologically informed classification grouping drugs by primary molecular target rather than ATC code, enabling direct testing of whether shared mechanism predicts shared sex-differential safety.

### 1.4 Competing Hypotheses

Two competing hypotheses predict different outcomes for the relationship between drug mechanism and sex-differential safety:

**The mechanism hypothesis:** If primary target biology determines sex-differential safety (through sex-differential target expression, hormonal modulation of target signaling, or sex-linked downstream pathways), then drugs within a class should show concordant sex profiles, and between-class variation should exceed within-class variation.

**The pharmacokinetic hypothesis:** If individual drug properties (lipophilicity, metabolism pathway, half-life, off-target binding) determine sex-differential safety through sex-differential pharmacokinetics, then within-class variation should be substantial, and mechanism alone should not predict sex profiles.

Prior analyses have examined sex differences for individual drug classes: opioids [15], antidepressants [16], cardiovascular drugs [17], and antipsychotics [18]. However, no study has systematically compared within-class and between-class sex-differential safety variation across the full therapeutic spectrum. We addressed this gap using 96,281 sex-differential signals across 19 drug classes.

---

## 2. Methods

### 2.1 Data Source

We used the U.S. FDA Adverse Event Reporting System (FAERS), the largest publicly available pharmacovigilance database, covering the period 2004Q1 through 2025Q3: 14,536,008 deduplicated reports (60.2% female, 39.8% male). Reports lacking sex designation, with indeterminate sex, or from pediatric populations (age < 18 years) were excluded. Drug names were standardized to active ingredient level using the FAERS drug name mapping pipeline.

### 2.2 Sex-Stratified Disproportionality Analysis

For each drug-adverse event (drug-AE) pair, sex-stratified reporting odds ratios (ROR) were computed independently for female and male populations:

$$
ROR_{sex} = \frac{a_{sex} / b_{sex}}{c_{sex} / d_{sex}}
$$

where $a$ = reports for the specific drug-AE pair, $b$ = reports for the drug with other AEs, $c$ = reports for other drugs with the specific AE, $d$ = reports for other drugs with other AEs, each within the specified sex stratum.

The sex-differential signal metric was:

$$
logR = \ln\left(\frac{ROR_{female}}{ROR_{male}}\right)
$$

Positive logR values indicate female-biased signals (stronger drug-AE association in women); negative values indicate male-biased signals. The logR metric is symmetric around zero and has desirable statistical properties for cross-sex disproportionality comparison [1,19].

### 2.3 Signal Thresholding

Signals required: (1) |logR| >= 0.5 (~1.65-fold ROR difference between sexes); (2) >= 10 reports in each sex stratum. These thresholds yielded 96,281 sex-differential signals across 2,178 drugs and 5,069 unique adverse events.

### 2.4 Female Signal Proportion

For each drug, the female signal proportion (%F) was computed as:

$$
\%F = \frac{N_{female-biased\ signals}}{N_{female-biased\ signals} + N_{male-biased\ signals}} \times 100
$$

Drugs with fewer than 5 total signals were excluded. Values near 100%F indicate female-biased safety concerns; near 0%F indicates male-biased signals; 50%F indicates balanced profiles.

### 2.5 Drug Classification

Drugs were classified into 19 major classes organized by therapeutic area, based on primary molecular target:

**Pain & migraine:** CGRP agents (erenumab, fremanezumab, galcanezumab, rimegepant), triptans (sumatriptan, rizatriptan, almotriptan, eletriptan), NSAIDs (ibuprofen, naproxen, diclofenac, celecoxib, meloxicam, piroxicam, flurbiprofen, indomethacin), opioids (morphine, oxycodone, fentanyl, tramadol, oxymorphone, codeine), cannabinoids (dronabinol, nabilone).

**Cardiovascular:** Beta-blockers (atenolol, metoprolol, carvedilol, bisoprolol), DOACs (rivaroxaban, apixaban, edoxaban), CCBs (amlodipine, diltiazem, nifedipine, nimodipine), antiarrhythmics (amiodarone, flecainide, sotalol), PAH drugs (bosentan, ambrisentan, sildenafil, tadalafil, epoprostenol, iloprost), ARNI (sacubitril/valsartan).

**Psychiatric:** Atypical antipsychotics (risperidone, quetiapine, olanzapine, aripiprazole, clozapine, cariprazine, brexpiprazole), SSRIs (sertraline, fluoxetine, citalopram, escitalopram, paroxetine), ADHD stimulants (methylphenidate, amphetamine, dexamfetamine, lisdexamfetamine, atomoxetine).

**Endocrine & metabolic:** GLP-1 agonists (semaglutide, liraglutide, dulaglutide, exenatide, tirzepatide), SGLT2 inhibitors (dapagliflozin, empagliflozin, canagliflozin), TZDs (pioglitazone, rosiglitazone), osteoporosis drugs (alendronate, risedronate, denosumab, zoledronic acid).

**Anti-infective:** Tetracyclines (doxycycline, minocycline, tetracycline), fluoroquinolones (ciprofloxacin, levofloxacin, moxifloxacin), carbapenems (meropenem, imipenem, ertapenem), HIV antiretrovirals (efavirenz, tenofovir, dolutegravir, darunavir).

**Autoimmune:** Anti-TNFs (infliximab, adalimumab, etanercept, certolizumab, golimumab), JAK inhibitors (tofacitinib, baricitinib, upadacitinib, ruxolitinib), anti-CD20 (rituximab, ocrelizumab, obinutuzumab, ofatumumab).

**Other:** S1P modulators (fingolimod, siponimod, ozanimod), retinoids (isotretinoin, acitretin, adapalene, tretinoin), muscle relaxants (baclofen, dantrolene, cyclobenzaprine, tizanidine).

### 2.6 Variation Metrics

**Between-class variation:** Range of class-level mean %F across all 19 classes.
**Within-class variation:** For each class, max(%F) - min(%F) across individual drugs with >= 5 signals.
**Class consistency:** Coefficient of variation (CV = SD / mean %F) per class.

---

## 3. Results

### 3.1 The Pan-Therapeutic Spectrum

The 19 drug classes spanned a 68 percentage-point range in mean female signal proportion, from CGRP agents (83%F) to S1P modulators (15%F). The overall mean across all 96,281 signals was 53.8%F, reflecting a modest female predominance consistent with higher overall ADR reporting rates in women [8,12].

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

The female-predominant end is anchored by classes for conditions with known female predominance (migraine, osteoporosis) or sex-differential immune biology (autoimmune diseases). The male-predominant end features S1P modulators, whose adverse events (cardiac conduction effects, macular edema) may show sex-differential reporting due to cardiovascular comorbidity patterns.

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

Pain therapeutics exhibited a graded female-to-male spectrum: CGRP agents (83%F) > NSAIDs (67%F) > opioids (62%F) > cannabinoids (44%F). This 39 pp pain therapeutic gradient tracks with receptor pharmacology: CGRP is strongly modulated by estrogen (menstrual migraine [20]), COX enzymes show modest sex differences, opioid mu-receptors are sex-dimorphic [15], and cannabinoid CB1 receptors show male-predominant activation patterns [21].

CGRP agents showed a relatively tight 15 pp spread despite including both monoclonal antibodies (erenumab, fremanezumab, galcanezumab) and a small-molecule receptor antagonist (rimegepant), suggesting that the CGRP pathway's sex biology constrains the sex-differential profile regardless of molecular format. Triptans, by contrast, showed a 65 pp spread despite sharing 5-HT1B/1D agonism: sumatriptan (77%F, metabolized primarily by MAO-A with sex-differential activity) diverged sharply from almotriptan (12%F, metabolized by CYP3A4 and MAO-A). Within opioids, morphine (67%F) differs from oxymorphone (45%F) by 22 pp despite identical mu-receptor primary targets, suggesting that secondary metabolism (CYP2D6 for oxymorphone vs. UGT2B7 for morphine) drives the sex-differential divergence. Cannabinoids (44%F, 8 pp spread) were male-biased, consistent with male-predominant CB1 receptor density and testosterone enhancement of endocannabinoid signaling [21].

#### 3.3.2 Cardiovascular Therapeutics

Cardiovascular drugs spanned a 29 pp range from PAH drugs (71%F) to ARNI (42%F), with remarkable heterogeneity in within-class consistency.

DOACs (55%F, 3 pp spread) showed the tightest within-class agreement in the entire analysis: rivaroxaban, apixaban, and edoxaban clustered at 53--56%F. This consistency likely reflects the relative sex-neutrality of factor Xa as a target and the similar pharmacokinetic profiles across the class. By contrast, beta-blockers showed 20 pp spread (carvedilol 46%F to atenolol 66%F), tracking with receptor selectivity: atenolol (beta-1 selective) versus carvedilol (beta-1/beta-2/alpha-1 non-selective). The alpha-1 adrenergic receptor shows sex-differential vascular expression, and carvedilol's CYP2D6 metabolism introduces additional pharmacokinetic sex divergence versus atenolol's renal elimination.

CCBs (56%F, 43 pp spread) showed the largest cardiovascular within-class spread: nimodipine (28%F) and diltiazem (70%F) diverged by 43 pp despite both targeting L-type calcium channels. This reflects distinct subclasses (dihydropyridine vs. benzothiazepine) with different tissue selectivities and indication contexts (subarachnoid hemorrhage vs. hypertension/angina). PAH drugs (71%F, 16 pp spread) were consistently female-biased, reflecting the 2.3:1 female predominance in PAH [22]. Antiarrhythmics (47%F, 14 pp spread) showed modest within-class variation around a slightly male-biased mean, potentially reflecting competing effects: women's longer baseline QTc and greater drug-induced QT prolongation susceptibility [17] versus male-predominant atrial fibrillation prevalence.

#### 3.3.3 Psychiatric Therapeutics

Psychiatric drugs showed the most extreme within-class variation across all therapeutic areas.

**Atypical antipsychotics (48%F, 90 pp spread).** The 90 pp spread from cariprazine (3%F) to risperidone (93%F) represents the single most striking finding of this analysis. Multiple factors converge: (i) *metabolic pathway divergence*---risperidone is primarily metabolized by CYP2D6 (sex-differential activity [23]) while cariprazine uses CYP3A4; (ii) *indication population differences*---risperidone has significant use in autism spectrum disorder (4:1 male predominance in ASD), while cariprazine is primarily for bipolar depression; (iii) *secondary pharmacology*---risperidone has strong alpha-1 adrenergic and H1 histaminergic antagonism, while cariprazine is a D3 partial agonist with distinct downstream signaling; (iv) *prolactin dynamics*---risperidone is among the strongest prolactin-elevating antipsychotics (producing sex-specific galactorrhea, amenorrhea), while cariprazine has minimal prolactin effects.

SSRIs (58%F, 11 pp spread) showed notably consistent sex-differential profiles, likely reflecting their relatively clean pharmacology (serotonin transporter inhibition with limited off-target effects) and similar pharmacokinetic properties. ADHD stimulants (51 pp spread) diverged from dexamfetamine (15%F) to methylphenidate (78%F), reflecting both mechanistic differences (DAT blockade vs. DAT reversal) and the male-predominant ADHD diagnosis pattern in childhood populations where methylphenidate predominates [18].

#### 3.3.4 Endocrine and Metabolic Therapeutics

GLP-1 agonists (58%F, 15 pp spread) were moderately female-biased, with tirzepatide highest (65%F) and exenatide lowest (50%F). Tirzepatide's higher female bias may relate to its dual GIP/GLP-1 agonism, as GIP receptor signaling shows sex-differential effects on bone metabolism and adipose tissue distribution [24]. The GLP-1 female bias aligns with the 67.1 pp diabetes drug spectrum from TZDs (92%F) to SGLT2 inhibitors (48%F), suggesting that glucose-lowering mechanism influences sex-differential safety independently of glycemic efficacy.

SGLT2 inhibitors (48%F, 10 pp spread) showed near sex-parity with tight within-class consistency, consistent with the renal sodium-glucose cotransporter producing a relatively sex-neutral adverse event profile. Osteoporosis drugs (73%F, 20 pp spread) reflected the overwhelmingly female patient population, with the 20 pp spread possibly reflecting route-of-administration differences (oral vs. subcutaneous vs. intravenous) affecting adverse event types reported.

#### 3.3.5 Anti-Infective Therapeutics

Tetracyclines (68%F, 12 pp spread) were the most female-biased antibiotic class, likely reflecting acne indication (female-predominant treatment-seeking), photosensitivity reactions (female-biased dermatologic AE), and minocycline's female-predominant vestibular toxicity. Fluoroquinolones (54%F, 8 pp spread) showed near sex-parity with tight consistency, perhaps because fluoroquinolone tendinopathy risk factors (age, corticosteroid use) are not strongly sex-linked [3]. Carbapenems (51%F, 7 pp spread) showed the most balanced anti-infective profile, consistent with severe hospital-acquired infection demographics. HIV antiretrovirals (42%F, 18 pp spread) were male-biased, reflecting the historically male-predominant HIV treatment population, with the 18 pp within-class spread reflecting distinct metabolic pathways (CYP2B6 for efavirenz, renal for tenofovir, UGT1A1 for dolutegravir, CYP3A4 for darunavir).

#### 3.3.6 Autoimmune Therapeutics

Anti-TNFs (69%F, 15 pp spread) showed consistently female-biased profiles, reflecting the sex-differential biology of TNF-alpha (estrogen enhances TNF-alpha production [9]) and the female predominance of target indications (rheumatoid arthritis, Crohn's disease). The 15 pp spread across five monoclonal antibodies with different molecular formats (chimeric, fully human, PEGylated Fab, receptor-Fc fusion) was relatively modest, suggesting target biology dominates over antibody-specific properties.

JAK inhibitors (46 pp spread) diverged from upadacitinib (24%F) to ruxolitinib (70%F), reflecting critical differences in JAK isoform selectivity and indication: ruxolitinib (JAK1/2, myelofibrosis---slightly male-predominant) versus tofacitinib (pan-JAK, rheumatoid arthritis---strongly female-predominant) versus upadacitinib (JAK1-selective, rheumatoid arthritis and atopic dermatitis). Anti-CD20 antibodies (60 pp spread) diverged from ofatumumab (12%F) to obinutuzumab (72%F) despite targeting the same cell-surface antigen, reflecting dramatic indication differences: hematological malignancies (obinutuzumab, rituximab) versus multiple sclerosis (ofatumumab, ocrelizumab).

#### 3.3.7 Other Therapeutic Areas

S1P modulators (15%F, 25 pp spread) showed the most male-biased profile across all 19 classes. While multiple sclerosis is 2-3 times more common in women, S1P modulator adverse events (first-dose bradycardia, macular edema, lymphopenia) may be differentially reported due to male-predominant cardiovascular comorbidity. The 25 pp spread reflects S1P receptor subtype selectivity differences (siponimod is S1P1/5-selective; fingolimod is non-selective).

Retinoids (34 pp spread) ranged from acitretin (43%F, psoriasis---sex-balanced) to adapalene (77%F, topical acne---female-predominant treatment-seeking). Muscle relaxants (39 pp spread) ranged from dantrolene (40%F, ryanodine receptor mechanism) to cyclobenzaprine (79%F, central norepinephrine mechanism structurally related to tricyclic antidepressants), making within-class divergence expected given fundamentally different mechanisms grouped under a single therapeutic umbrella.

### 3.4 DOACs: A Model of Within-Class Consistency

DOACs (rivaroxaban, apixaban, edoxaban) show the tightest within-class sex profile: 53--56%F with only 3 pp spread. This consistency suggests that factor Xa inhibition produces a highly reproducible sex-differential safety profile regardless of specific molecular structure. DOACs may serve as a positive control for class-effect sex-differential labeling---the rare case where mechanism truly determines sex profile.

The DOAC consistency contrasts instructively with the antipsychotic 90 pp explosion. DOACs share several consistency-promoting properties: (1) identical molecular target at the same binding site; (2) similar pharmacokinetic profiles (moderate protein binding, dual renal/hepatic clearance); (3) homogeneous primary indication (stroke prevention in atrial fibrillation); (4) target (factor Xa) that is not strongly sex-dimorphic. Antipsychotics lack all four features.

### 3.5 Consistency Classes versus Divergence Classes

The full spectrum of within-class variation reveals a bimodal pattern. "Consistency classes" (spread < 15 pp) include DOACs (3 pp), carbapenems (7 pp), cannabinoids (8 pp), fluoroquinolones (8 pp), SSRIs (11 pp), and tetracyclines (12 pp). These share relatively clean pharmacology, limited indication heterogeneity, and similar within-class pharmacokinetic profiles.

"Divergence classes" (spread > 30 pp) include atypical antipsychotics (90 pp), triptans (65 pp), anti-CD20 (60 pp), ADHD stimulants (51 pp), JAK inhibitors (46 pp), CCBs (43 pp), muscle relaxants (39 pp), and retinoids (34 pp). These are characterized by extensive off-target binding, indication heterogeneity, divergent metabolic pathways, or different drug subclasses grouped under a single mechanistic label.

---

## 4. Discussion

### 4.1 Mechanism Hypothesis: Rejected for Most Classes

The extraordinary within-class variation (up to 90 pp for antipsychotics) definitively rejects the mechanism hypothesis for most drug classes. Drugs sharing primary targets produce diametrically opposite sex-differential safety profiles far more often than concordant profiles. Primary mechanism of action is a poor predictor of sex-differential safety.

Exceptions exist: DOACs (3 pp spread) and SSRIs (11 pp spread) show meaningful within-class consistency, suggesting that some targets do constrain sex-differential safety profiles. The common feature of these consistent classes may be target specificity: DOACs and SSRIs have relatively clean pharmacology with few off-target effects, while antipsychotics and triptans are notoriously "dirty" drugs with extensive off-target binding. This pattern suggests a refined model: **primary mechanism constrains sex-differential safety only when the drug's pharmacological activity is dominated by that primary mechanism.** For polypharmacological drugs, secondary pharmacology, metabolism, and indication context override primary mechanism effects.

### 4.2 Comparison with Watson et al. (2019) EClinicalMedicine

Watson et al. [12] analyzed sex differences in ADR reporting across the UK Yellow Card database and demonstrated that women reported significantly more ADRs across nearly all organ systems. Our findings extend Watson et al. in three critical ways.

First, while Watson et al. focused on aggregate sex differences (the overall female predominance), our analysis reveals that this aggregate pattern conceals enormous drug-level and class-level heterogeneity. The 68 pp between-class range (CGRP agents 83%F to S1P modulators 15%F) shows that "women report more ADRs" is a dramatic oversimplification---for S1P modulators, the reverse is true. Watson et al.'s organ-system-level analysis could not capture this drug-class resolution.

Second, Watson et al. identified skin, gastrointestinal, and neurological reactions as showing the strongest sex differences. Our therapeutic-area analysis complements this by identifying which drug classes drive these organ-system patterns: CGRP agents and NSAIDs likely contribute to neurological and gastrointestinal sex differences, while retinoids and tetracyclines contribute to dermatological differences.

Third, and most critically, Watson et al. did not examine within-class variation. Our finding that within-class variation exceeds between-class variation in 42% of classes demonstrates that drug-level properties are a major---and previously unrecognized---source of sex-differential safety variation that cannot be captured at the organ-system level.

### 4.3 Comparison with Yu et al. (2016) Scientific Reports

Yu et al. [13] emphasized that sex-differential drug responses extend beyond pharmacokinetics to encompass sex-dimorphic immune function, hormonal modulation of drug targets, and sex-differential disease biology. Our findings provide large-scale pharmacovigilance validation of Yu et al.'s framework at the between-class level: the pain therapeutic gradient (CGRP 83%F > NSAIDs 67%F > opioids 62%F > cannabinoids 44%F) directly reflects target-level sex-differential biology, precisely as their framework predicts.

However, the within-class explosions (antipsychotics 90 pp, triptans 65 pp) reveal a critical limitation: target-level sex biology is necessary but not sufficient to predict drug-level sex-differential safety. Two drugs acting on the same sex-dimorphic target can show opposite profiles due to secondary pharmacology, metabolism, and indication context. Our findings extend Yu et al.'s framework by demonstrating that target biology sets the between-class pattern but individual drug properties dominate within-class variation.

### 4.4 Integration with Zucker and Prendergast (2020) Pharmacokinetic Framework

Zucker and Prendergast [8] provided compelling evidence that sex differences in pharmacokinetics predict ADR patterns. Our within-class analysis provides strong support at scale: the most divergent classes (antipsychotics, triptans, ADHD stimulants) are precisely those where within-class metabolic pathway differences are greatest (CYP2D6 vs. CYP3A4 vs. MAO-A), while the most consistent classes (DOACs, SSRIs, carbapenems) share similar metabolic profiles. The Zucker-Prendergast pharmacokinetic framework, applied at the within-class level, explains why mechanism alone is insufficient: even drugs sharing a target diverge dramatically if their disposition differs in sex-differential ways.

### 4.5 Why Some Therapeutic Areas Show Stronger Sex Effects

The 68 pp between-class range is driven by four principal mechanisms:

1. **Disease sex ratio.** Conditions with strongly sex-skewed prevalence (migraine 3:1 female, osteoporosis 4:1 female, PAH 2.3:1 female) drive female-biased safety reporting independent of drug pharmacology. This "denominator effect" is partially but not fully corrected by ROR disproportionality analysis.

2. **Target sex biology.** Molecular targets with sex-differential expression or hormonal modulation produce sex-biased profiles through pharmacodynamic mechanisms. CGRP (estrogen-modulated [20]), serotonin receptors (sex-differential expression), and TNF-alpha (estrogen-enhanced production [9]) directly influence sex-differential safety.

3. **Metabolic pathway sex dimorphism.** Drug classes metabolized by sex-dimorphic CYP enzymes show greater within-class variation than renally eliminated classes. CYP3A4 activity is approximately 20-40% higher in women [7], CYP2D6 shows genotype-dependent sex effects, and CYP1A2 is generally higher in men.

4. **Polypharmacology.** "Dirty" drugs with extensive off-target binding (antipsychotics, triptans) show greater within-class variation than "clean" drugs (DOACs, SSRIs) because each secondary target introduces an independent sex-differential effect.

### 4.6 Drivers of Within-Class Divergence

Four factors explain within-class variation:

1. **CYP metabolism pathway:** Drugs metabolized by different CYP enzymes (CYP2D6 vs. CYP3A4 vs. CYP1A2) achieve different sex-differential tissue concentrations, as CYP expression is sex-dimorphic [23].

2. **Off-target binding:** Secondary receptor affinities with sex-differential consequences (e.g., risperidone's alpha-1 blockade vs. cariprazine's D3 partial agonism) shift the overall sex profile away from what primary mechanism predicts.

3. **Indication populations:** Different indications with different sex ratios within a class (e.g., methylphenidate for ADHD in boys vs. atomoxetine for adult ADHD; ruxolitinib for myelofibrosis vs. tofacitinib for rheumatoid arthritis) modulate the types and sex distribution of adverse events reported.

4. **Physicochemical properties:** Lipophilicity, volume of distribution, and protein binding affect sex-differential tissue exposure independently of target pharmacology. Women's higher average body fat percentage, lower body weight, and different albumin/alpha-1 acid glycoprotein levels introduce sex-differential free drug fractions and tissue distribution.

### 4.7 Implications for Drug Regulation and Clinical Practice

1. **Class-effect sex warnings are invalid.** A sex-differential safety signal for one drug should NOT be extrapolated to other drugs in the same class. The 90 pp antipsychotic spread demonstrates that a sex-safety finding for risperidone carries no predictive value for cariprazine.

2. **Within-class switching requires sex-differential consideration.** Switching between drugs within a class may change sex-differential safety exposure by up to 90 pp. Clinicians should consider individual drug sex-differential profiles when selecting among within-class alternatives.

3. **Trial design must be drug-specific.** Phase III trials should not rely on class-level sex-differential safety assumptions. The FDA's guidance on demographic subgroup analysis [25] should be extended to mandate drug-specific sex-stratified safety analysis.

4. **Drug labeling should include sex-differential profiles.** A standardized sex-differential safety metric should be incorporated into labeling to inform sex-aware prescribing, replacing the current inconsistent and rarely quantitative sex-differential information.

5. **Sex-stratified signal detection should be default.** Routine sex-stratified pharmacovigilance, as performed here, should become standard in databases worldwide.

### 4.8 The Consistency-Divergence Spectrum as a Drug Class Property

Within-class sex-differential consistency is itself a meaningful pharmacological characteristic. High-consistency classes (DOACs, SSRIs, carbapenems) may be amenable to class-level labeling; low-consistency classes (antipsychotics, triptans, anti-CD20) categorically require individual drug characterization. This spectrum correlates with pharmacological target specificity, metabolic homogeneity, and indication consistency---features useful for prospectively predicting sex-stratified data requirements for new drug classes.

### 4.9 Limitations

1. Drug classification is based on primary mechanism; some drugs have multiple mechanisms. Reclassification would alter within-class spreads but not the central finding of extreme within-class divergence.

2. Within-class spread depends on the number of drugs analyzed; larger classes have more opportunity for extreme values. However, the 65 pp triptan spread (4 drugs) and 60 pp anti-CD20 spread (4 drugs) argue against a pure size artifact.

3. Some within-class differences may reflect indication-specific confounding rather than true drug-level differences. Disentangling drug-level from indication-level sex effects requires indication-stratified analyses beyond this study's scope.

4. Reporting patterns may differ across indications within a class. The ROR framework partially mitigates this but residual reporting bias cannot be excluded.

5. The 21-year study period spans changes in prescribing patterns and reporting practices. Drugs marketed for the entire period have different reporting maturity than recently approved drugs.

6. FAERS reflects U.S. reporting patterns. International replication using WHO VigiBase or EudraVigilance would strengthen generalizability.

7. Dose-level analysis was not performed due to incomplete dose information in FAERS; sex-differential safety may vary with dose.

---

## 5. Conclusion

The pan-therapeutic sex-differential spectrum spans 68 pp (CGRP agents 83%F to S1P modulators 15%F), but within-class variation exceeds between-class variation in 42% of classes (8 of 19). The atypical antipsychotic 90 pp spread (risperidone 93%F to cariprazine 3%F) demonstrates that shared primary mechanism does not predict sex-differential safety. Only DOACs (3 pp spread) show the tight within-class consistency expected under the mechanism hypothesis. These findings invalidate class-effect sex-differential safety labeling and mandate individual-drug sex-differential characterization for every approved therapeutic.

These findings carry direct implications for clinical practice and regulation: therapeutic switching decisions must consider drug-level sex-differential profiles, regulatory agencies should require drug-specific sex-stratified safety data, and sex-stratified signal detection should become standard in pharmacovigilance.

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

20. Labastida-Ramirez A, Rubio-Beltran E, Villalon CM, MaassenVanDenBrink A. Gender aspects of CGRP in migraine. Cephalalgia. 2019;39:435-444.

21. Craft RM, Marusich JA, Wiley JL. Sex differences in cannabinoid pharmacology: a reflection of differences in the endocannabinoid system? Life Sci. 2013;92:476-481.

22. Badesch DB, Raskob GE, Elliott CG, et al. Pulmonary arterial hypertension: baseline characteristics from the REVEAL registry. Chest. 2010;137:376-387.

23. Zanger UM, Schwab M. Cytochrome P450 enzymes in drug metabolism: regulation of gene expression, enzyme activities, and impact of genetic variation. Pharmacol Ther. 2013;138:103-141.

24. Campbell JE, Drucker DJ. Pharmacology, physiology, and mechanisms of incretin hormone action. Cell Metab. 2013;17:819-837.

25. U.S. Food and Drug Administration. Collection of race and ethnicity data in clinical trials: guidance for industry. Silver Spring, MD: FDA; 2016.

---

## Figure Legends

**Figure 1.** Pan-therapeutic sex spectrum. Horizontal bar chart of 19 drug classes ranked by mean female signal proportion. CGRP agents (83%F) to S1P modulators (15%F). Error bars show within-class range. Dashed line at 50% parity.

**Figure 2.** Within-class vs. between-class variation. Forest plot showing class mean (diamond) with within-class range (horizontal line) for each of 19 classes. The majority of within-class ranges exceed the interquartile range of class means.

**Figure 3.** The antipsychotic explosion. Individual drug profiles for 7 atypical antipsychotics. Stacked bar showing female (red) and male (blue) signal proportions. Risperidone (93%F) and cariprazine (3%F) anchoring opposite extremes.

**Figure 4.** Pain therapeutic gradient. CGRP agents (83%F) > NSAIDs (67%F) > Opioids (62%F) > Cannabinoids (44%F). Receptor pharmacology annotations for each class.

**Figure 5.** DOACs: the exception. Within-class profile for rivaroxaban, apixaban, and edoxaban showing 3 pp spread---the tightest within-class agreement in the analysis.

**Figure 6.** Consistency-divergence spectrum. Scatter plot of within-class spread (y-axis) versus number of drugs in class (x-axis) for all 19 classes. Labeled points for extreme cases. Horizontal reference line at 30 pp threshold.

---

## Supplementary Materials

**Table S1.** Complete drug-level %F values, signal counts, and CYP metabolism pathways for all drugs across 19 classes.

**Table S2.** Pairwise within-class comparisons for the 10 classes with highest spread.

**Figure S1.** Individual drug %F profiles for all 19 classes with 95% Wilson score confidence intervals.
