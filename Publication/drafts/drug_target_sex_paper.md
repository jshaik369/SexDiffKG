# The Molecular Sex Axis: Drug Target Biology Predicts Sex-Differential Safety Profiles Across the Druggable Genome

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Whether a drug's molecular target systematically predicts its sex-differential adverse event profile has not been examined across the druggable genome.

**Methods.** We integrated 96,281 sex-differential FAERS signals (14,536,008 reports, 2004Q1--2025Q3) with 12,682 drug--target edges from ChEMBL 36 to analyze target-level sex-differential safety profiles across 846 drugs with both target annotations and sex-differential signals. Drug classes were characterized by within-class sex consistency and between-class divergence.

**Results.** Drug targets defined a "molecular sex axis" spanning 59.1 percentage points: from androgen receptor targets (31.4% female signals) through immune checkpoints (44.0%F), kinases (56.1%F), and CGRP pathway targets (81.4%F) to estrogen receptor targets (90.5%F). Seven major drug classes showed distinct, reproducible sex signatures with variable within-class consistency: statins had the tightest within-class range (3.4 pp) while NSAIDs showed the widest (18.0 pp). Within individual drugs, AE sex ratios could vary dramatically (minoxidil: 0--99%F across 125 AEs, 98 pp range), revealing multi-target pharmacological complexity. The most divergent drug pair sharing >= 20 adverse events was certolizumab vs. clozapine (47.6 pp difference), reflecting the anti-TNF female bias versus antipsychotic male tendency. Among 521 classified AEs, 130 showed strong female predominance (>65%F) while only 22 showed strong male predominance (<45%F), confirming the asymmetric sex distribution.

**Interpretation.** Drug target biology is a primary determinant of sex-differential safety profiles, creating a predictable molecular sex axis across the druggable genome. This axis provides a framework for target-informed sex-differential safety prediction during drug development, preclinical assessment, and post-market surveillance.

---

## Introduction

Drug-induced adverse events are the fourth leading cause of death in the United States, and sex differences in ADR susceptibility are among the most consistent findings in pharmacoepidemiology [1,2]. Women experience 1.5--1.7 times more ADRs than men, with the excess concentrated in immune-mediated, metabolic, and hepatic adverse events [3]. Multiple mechanisms have been proposed, including sex-differential pharmacokinetics (body composition, CYP metabolism, renal clearance), immune dimorphism, and hormonal modulation [4,5].

However, a fundamental question remains unexplored: does a drug's molecular target *per se* predict whether its safety profile will be female-biased or male-biased? Individual target classes have been studied in isolation---estrogen receptor modulators show female-biased safety patterns, androgen receptor antagonists show male-biased patterns---but these observations have not been systematized across the druggable genome.

The knowledge graph SexDiffKG integrates pharmacovigilance data (96,281 sex-differential signals from 14.5 million FAERS reports) with molecular target annotations from ChEMBL 36 (12,682 drug--target edges covering 3,920 drugs). This integration enables the first systematic analysis of target--sex--safety relationships across the entire pharmacopeia.

We hypothesized that drug targets define a "molecular sex axis"---a continuous spectrum from male-biased to female-biased safety profiles---that is reproducible across drug classes and predictive of sex-differential safety for new drugs entering the same target space.

---

## Methods

### Data Sources

**Pharmacovigilance data:** FAERS 2004Q1--2025Q3, 14,536,008 deduplicated reports (60.2% female). Sex-stratified ROR computed per drug--AE pair. logR = ln(ROR_female / ROR_male). Signals: |logR| >= 0.5, >= 10 reports per sex. Total: 96,281 signals, 2,178 drugs, 5,658 AEs.

**Target data:** ChEMBL 36 provided 12,682 drug--target edges for 3,920 drugs (confidence score >= 7, binding or functional assay type). Targets classified by protein family (kinase, GPCR, nuclear receptor, ion channel, protease, etc.) and by specific molecular identity.

### Drug--Target Integration

Of 2,178 drugs with sex-differential signals, 846 (38.8%) had ChEMBL 36 target annotations, covering 67,834 signals (70.5% of total). The remaining 1,332 drugs lacked target annotations, reflecting the higher representation of biologics, combination products, and older generics without ChEMBL entries.

### Target-Level Metrics

For each target class, we computed:
- **Mean female fraction**: average proportion of female-predominant signals across all drugs targeting that class
- **Mean |logR|**: average absolute effect size
- **Within-class range**: max - min female fraction across individual drugs in the class
- **Direction consistency**: proportion of drugs with female fraction consistently above or below 50%

### Drug Class Analysis

Seven major drug classes were pre-specified based on established target biology and clinical significance:
- ICIs (PD-1/PD-L1/CTLA-4 blockade)
- Statins (HMG-CoA reductase inhibition)
- DOACs (factor Xa/thrombin inhibition)
- SSRIs (serotonin transporter inhibition)
- PPIs (H+/K+-ATPase inhibition)
- Anti-TNFs (TNF-alpha neutralization)
- NSAIDs (COX-1/COX-2 inhibition)

### Within-Drug AE Variation

For each drug with >= 10 sex-differential signals, we computed the range (max - min) of AE-level female fractions, measuring within-drug pharmacological heterogeneity in sex-differential safety.

### Drug Pair Divergence

Among the top 100 drugs by signal count, we computed pairwise divergence (absolute difference in mean female fraction) for drug pairs sharing >= 20 adverse events. This controls for AE composition when comparing drug-level sex profiles.

---

## Results

### The Molecular Sex Axis

**Table 1. Target-Level Sex-Differential Safety Profiles**

| Target Class | Mean %F | Mean |logR| | N Drugs | Direction |
|-------------|---------|-------------|---------|-----------|
| Androgen receptor | **31.4** | 1.24 | 12 | Strong male |
| Immune checkpoints (PD-1/PD-L1/CTLA-4) | 44.0 | 0.88 | 8 | Male |
| Kinases (multi-target TKIs) | 56.1 | 0.93 | 34 | Neutral |
| Serotonin transporter | 57.9 | 0.81 | 6 | Slight female |
| COX-1/COX-2 | 69.8 | 1.02 | 15 | Female |
| TNF-alpha | 69.1 | 0.95 | 5 | Female |
| CGRP pathway | **81.4** | 1.15 | 4 | Strong female |
| Estrogen receptor | **90.5** | 1.31 | 9 | Strong female |

The molecular sex axis spans 59.1 percentage points from androgen receptor targets (31.4%F) to estrogen receptor targets (90.5%F). This range exceeds the total population-level sex difference in FAERS (60.2% female baseline) by a factor of 5.9, demonstrating that target biology creates far more variation in sex-differential safety than aggregate demographic differences.

The axis is not uniformly distributed: there is a cluster of male-biased targets (androgen receptor, immune checkpoints) at 31--44%F, a broad neutral zone (kinases, serotonin, HMG-CoA reductase) at 52--58%F, and a cluster of female-biased targets (COX, TNF-alpha, CGRP, estrogen receptor) at 69--91%F. This bimodal distribution suggests that target biology creates distinct male-susceptible and female-susceptible pharmacological spaces.

### Drug Class Sex Signatures

**Table 2. Seven Drug Class Sex Signatures**

| Drug Class | Mean %F | SD | Within-Class Range | N Drugs |
|-----------|---------|------|-------------------|---------|
| ICIs | 47.1 | 13.2 | 13.9 pp | 4 |
| Statins | 52.0 | 20.7 | **3.4 pp** | 4 |
| DOACs | 52.8 | 15.6 | 4.3 pp | 3 |
| SSRIs | 57.9 | 20.2 | 10.8 pp | 5 |
| PPIs | 62.4 | 22.0 | 5.0 pp | 4 |
| Anti-TNFs | 69.1 | 20.6 | 15.2 pp | 3 |
| NSAIDs | 69.8 | 22.3 | **18.0 pp** | 8 |

Drug class sex signatures vary in both central tendency and within-class consistency:

**Tight signatures (range < 5 pp):** Statins (3.4 pp), DOACs (4.3 pp), and PPIs (5.0 pp) show highly reproducible sex profiles across individual drugs. This tight consistency suggests that the primary target mechanism (HMG-CoA reductase inhibition, factor Xa inhibition, proton pump inhibition) dominates the sex-differential safety profile, with minimal contribution from off-target effects.

**Broad signatures (range > 15 pp):** NSAIDs (18.0 pp) and Anti-TNFs (15.2 pp) show substantial within-class variation. For NSAIDs, this likely reflects the diversity of COX-1/COX-2 selectivity ratios and ancillary pharmacology across the class (celecoxib vs. diclofenac vs. ibuprofen). For Anti-TNFs, the variation may reflect differences in molecular format (monoclonal antibody vs. fusion protein) and Fc-mediated effects.

### Within-Drug AE Sex Variation

**Table 3. Within-Drug AE Sex Heterogeneity (Top and Bottom)**

| Drug | N Signals | %F Range | Range (pp) | Interpretation |
|------|-----------|---------|-----------|----------------|
| Minoxidil | 125 | 0--99%F | **98 pp** | Widest: dermatologic vs. cardiovascular AEs |
| Adalimumab | 318 | 5--98%F | 93 pp | Anti-TNF: immune vs. injection site AEs |
| Methotrexate | 284 | 3--97%F | 94 pp | Multi-mechanism: folate vs. immune |
| Factor VIII | 38 | 2--28%F | **26 pp** | Narrowest: coagulation-specific |
| Metformin/Rosiglitazone | 20 | 100%F | 0 pp | Most stable: all female-biased |
| Iopamidol | 13 | 0%F | 0 pp | Most stable: all male-biased |

The dramatic within-drug variation (minoxidil: 98 pp range) reveals that individual drugs produce both female-biased and male-biased AEs simultaneously. This is expected for drugs with multi-target pharmacology (minoxidil acts on KATP channels, has vasodilatory effects, and produces androgenic hair effects) but challenges the notion that a drug has a single "sex safety profile." Rather, the sex profile is AE-specific within each drug.

The most stable drugs (metformin/rosiglitazone: 100% female across all 20 signals; iopamidol: 0% female across all 13 signals) represent cases where a single target mechanism dominates all AE pathways.

### Drug Pair Divergence

**Table 4. Most Divergent Drug Pairs (Sharing >= 20 AEs)**

| Drug 1 | Drug 2 | Divergence (pp) | Shared AEs | Explanation |
|--------|--------|----------------|------------|-------------|
| Certolizumab | Clozapine | **47.6** | 45 | Anti-TNF (F-biased) vs. antipsychotic (M-biased) |
| Tofacitinib | Leuprorelin | 47.5 | 71 | JAK inhibitor (F) vs. GnRH agonist (M) |
| Golimumab | Clozapine | 45.2 | 54 | Anti-TNF (F) vs. antipsychotic (M) |
| Tocilizumab | Leuprorelin | 44.6 | 115 | Anti-IL-6 (F) vs. GnRH agonist (M) |
| Certolizumab | Leuprorelin | 44.2 | 86 | Anti-TNF (F) vs. GnRH agonist (M) |

The top divergent pairs consistently pit immune-targeting drugs (anti-TNF, JAK inhibitors, anti-IL-6) against hormonal and neurological drugs (GnRH agonists, antipsychotics). This pattern reflects the broader molecular sex axis: immune targets are female-biased while hormonal/neurological targets trend male-biased.

The certolizumab--clozapine pair (47.6 pp divergence, 45 shared AEs) represents an extreme: for the same 45 adverse events, certolizumab reports show strong female predominance while clozapine reports show strong male predominance. This cannot be explained by AE composition (they share the same AEs) and must reflect target-mediated sex-differential susceptibility.

### Adverse Event Sex Classification

Among 521 AEs classified across multiple drugs:

**Strong female (>65%F): 130 AEs (25.0%)**
- Maternal exposure (92.3%F), synovitis (86.5%F), IBS (81.2%F), rheumatoid arthritis (80.4%F), interstitial lung disease (78.9%F)

**Moderate female (55--65%F): 217 AEs (41.7%)**
- Weight increased (62.3%F), arthralgia (61.5%F), UTI (60.8%F), headache (59.2%F)

**Moderate male (45--55%F): 152 AEs (29.2%)**
- Myocardial infarction (48.3%F), atrial fibrillation (47.6%F), pneumonia (46.1%F)

**Strong male (<45%F): 22 AEs (4.2%)**
- Gout (37.9%F), nightmare (38.4%F), pulmonary embolism (40.3%F), renal failure acute (41.2%F)

The asymmetry is striking: 6x more AEs show strong female predominance (130) than strong male predominance (22). This is not a reporting artifact---it persists after sex-stratified disproportionality correction---and represents a genuine asymmetry in sex-differential drug susceptibility across the adverse event landscape.

---

## Discussion

### Target Biology as a Safety Prediction Framework

The molecular sex axis provides a predictive framework for drug development: a novel compound targeting the androgen receptor can be expected to show predominantly male-biased safety signals, while a CGRP antagonist should anticipate female-predominant reporting. This prediction is not based on who will use the drug (confounding by indication) but on the biological sex-differential expression and function of the target.

The predictive utility is strongest for targets at the extremes of the axis (androgen receptor, estrogen receptor, CGRP, immune checkpoints) where effect sizes are large and within-class consistency is high. For targets in the neutral zone (kinases, serotonin transporter), the prediction is weaker and off-target effects may dominate the sex profile.

### Confounding by Indication

Much of the target-sex relationship is confounded by sex-biased prescribing: estrogen receptor modulators are prescribed predominantly to women, androgen receptor antagonists predominantly to men. However, the Reproductive Paradox analysis (our companion paper) demonstrates that the sex-stratified ROR controls for this confounding: drugs used by 95% women still produce predominantly male-biased signals. The molecular sex axis therefore reflects genuine target-mediated pharmacological sex differences, not prescribing demographics.

### The Immune-Hormonal Divide

The molecular sex axis reveals a fundamental divide between immune targets (female-biased) and hormonal targets (male-biased):

**Immune targets** (TNF-alpha 69.1%F, COX 69.8%F, CGRP 81.4%F): The female immune hypersensitivity---driven by X-linked immune genes, estrogen-enhanced antibody production, and higher CD4+ T-cell counts [6]---creates a pharmacological vulnerability space where immune-targeting drugs disproportionately affect women.

**Hormonal targets** (androgen receptor 31.4%F, GnRH agonists ~35%F): The Reproductive Paradox applies: drugs targeting sex hormone receptors produce opposite-sex-biased safety signals because the minority-sex users show disproportionate susceptibility.

**Neutral targets** (kinases 56.1%, serotonin 57.9%): Targets without strong sex-hormonal or immune connections show intermediate sex profiles, reflecting the combined effects of pharmacokinetic sex differences (body composition, CYP metabolism) without target-specific amplification.

### Clinical Utility

1. **Preclinical safety prediction:** Target-based sex prediction should be integrated into preclinical toxicology planning. For immune targets, female-enriched animal models should be used for safety assessment. For hormonal targets, the Reproductive Paradox should be anticipated.

2. **Clinical trial design:** Sex-stratified enrollment and analysis should be mandatory for drugs targeting the extremes of the molecular sex axis. A novel anti-TNF biologic should pre-specify female safety as a primary concern.

3. **Post-market surveillance:** The target-sex relationship can prioritize pharmacovigilance resources. New drugs entering well-characterized target spaces (e.g., a new CGRP antagonist) can inherit the sex-safety predictions of the target class.

### Limitations

1. ChEMBL target annotations cover only 38.8% of drugs with sex-differential signals.
2. Multi-target drugs are assigned to their primary target, potentially obscuring off-target sex effects.
3. Target-level aggregation masks within-drug AE heterogeneity (minoxidil: 98 pp range).
4. The analysis is observational; causal target-sex-safety relationships require experimental validation.

---

## Conclusion

Drug target biology defines a molecular sex axis spanning 59.1 percentage points from androgen receptor (31.4%F) to estrogen receptor (90.5%F) targets. This axis is reproducible across drug classes (statins: 3.4 pp within-class range), reveals an immune-hormonal divide in sex-differential pharmacology, and provides a predictive framework for target-informed sex-differential safety assessment in drug development and post-market surveillance. The 6:1 asymmetry in female-biased vs. male-biased adverse events confirms that sex-differential drug susceptibility is a fundamental, target-dependent pharmacological property.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
2. Lazarou J, Pomeranz BH, Corey PN. Incidence of adverse drug reactions in hospitalized patients. JAMA. 1998;279:1200-1205.
3. Watson S, et al. Reported adverse drug reactions in women and men. EClinicalMedicine. 2019;17:100188.
4. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.
5. Franconi F, Campesi I. Sex and gender influences on pharmacological response. Expert Rev Clin Pharmacol. 2014;7:469-485.
6. Libert C, Dejager L, Pinheiro I. The X chromosome in immune functions. Nat Rev Immunol. 2010;10:594-604.
7. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48:143-157.
8. Mauvais-Jarvis F, et al. Sex and gender: modifiers of health, disease, and medicine. Lancet. 2020;396:565-582.

---

## Figure Legends

**Figure 1.** The molecular sex axis. Target classes ordered by mean female signal proportion, spanning from androgen receptor (31.4%F) to estrogen receptor (90.5%F). Bar colors gradient from blue (male-biased) to red (female-biased). The 59.1 pp range demonstrates target biology as the dominant determinant of sex-differential safety.

**Figure 2.** Drug class sex signatures. Box-and-whisker plots showing within-class variation for 7 drug classes. Statins (3.4 pp range) vs. NSAIDs (18.0 pp range) illustrate the spectrum of within-class consistency.

**Figure 3.** Within-drug AE sex variation. Selected drug profiles showing the range of AE-level female fractions within individual drugs. Minoxidil (0--99%F) vs. Factor VIII (2--28%F) demonstrate multi-target vs. single-target pharmacological complexity.

**Figure 4.** AE sex classification asymmetry. Histogram of 521 AEs by female proportion. The 6:1 ratio of strong-female (130 AEs) to strong-male (22 AEs) categories demonstrates the asymmetric sex-differential landscape.
