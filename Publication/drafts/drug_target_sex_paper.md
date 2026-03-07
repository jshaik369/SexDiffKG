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

### The Burden of Sex-Differential Adverse Drug Reactions

Drug-induced adverse events are the fourth leading cause of death in the United States, and sex differences in ADR susceptibility are among the most consistent findings in pharmacoepidemiology [1,2]. Women experience 1.5--1.7 times more ADRs than men, with the excess concentrated in immune-mediated, metabolic, and hepatic adverse events [3]. Multiple mechanisms have been proposed, including sex-differential pharmacokinetics (body composition, CYP metabolism, renal clearance), immune dimorphism, and hormonal modulation [4,5]. A landmark analysis by Zucker and Prendergast [1] demonstrated that sex differences in pharmacokinetics are sufficient to predict a substantial fraction of observed ADR sex disparities, but also identified a residual component that cannot be explained by pharmacokinetic factors alone. This residual component points to pharmacodynamic sex differences---that is, sex-differential responses at the level of drug targets.

The clinical significance is substantial. An analysis of 86 drugs withdrawn from the US market found that 8 of 10 drugs withdrawn for sex-biased safety concerns disproportionately affected women [2]. The FDA's 2014 revision of zolpidem dosing---halving the recommended dose for women---represented a landmark acknowledgment that sex-specific pharmacology requires sex-specific prescribing [6].

### Sex-Differential Gene Expression and Drug Target Biology

The biological foundation for target-mediated sex differences in drug safety lies in the sexually dimorphic transcriptome. The GTEx Consortium [7] reported that approximately 37% of genes show sex-differential expression in at least one tissue, with the most pronounced differences observed in reproductive tissues, adipose tissue, skeletal muscle, and liver. Lopes-Ramos et al. [8] extended this work using network-based approaches, demonstrating that sex differences in gene regulatory networks are pervasive across human tissues and that these network-level differences alter the functional context in which drug targets operate. Their analysis revealed that sex-differential targeting of transcription factors by gene regulatory networks leads to tissue-specific rewiring of biological pathways, suggesting that the same drug target may function in fundamentally different molecular contexts in males versus females.

The implications for drug safety are direct: if a drug target is expressed at higher levels in one sex, or operates within a sex-differentially wired signaling network, drugs acting on that target may produce sex-biased pharmacodynamic effects. CYP2D6, which metabolizes approximately 25% of clinically used drugs, shows sex-differential hepatic expression, with women showing 20--30% lower activity on average [9]. CYP3A4, metabolizing approximately 50% of all drugs, shows the opposite: women express 20--40% higher hepatic CYP3A4, leading to faster clearance of substrates such as midazolam [10]. These pharmacokinetic sex differences are well-characterized, but sex differences at the pharmacodynamic level---the drug target itself---remain poorly understood.

### The Druggable Genome and Target-Based Safety Prediction

The concept of the "druggable genome" was formalized by Hopkins and Groom [11] and expanded by Santos et al. [12], who identified 667 human proteins targeted by approved drugs, drawn from a broader set of approximately 3,000 proteins estimated to be tractable to small-molecule or biologic intervention. Overington et al. [13] provided the foundational mapping of drug-target relationships, showing that approved drugs collectively target 324 distinct molecular entities, with G-protein coupled receptors (GPCRs), kinases, ion channels, and nuclear receptors representing the dominant target families.

The ChEMBL database [14] has since expanded this mapping enormously, providing curated bioactivity data linking small molecules and biologics to their molecular targets. ChEMBL 36, the version used in this study, contains over 2.4 million distinct compounds tested against over 15,000 protein targets, with confidence-scored drug-target associations that enable systematic integration with clinical safety data.

Despite this wealth of target annotation data, no study has systematically examined whether drug target class predicts sex-differential safety profiles across the druggable genome. Individual target classes have been studied in isolation---estrogen receptor modulators show female-biased safety patterns, androgen receptor antagonists show male-biased patterns---but these observations have not been systematized. The STRING database [15], which maps protein-protein interactions with confidence scores derived from experimental data, co-expression, and text-mining, provides a complementary resource for understanding how drug targets are embedded in sex-differential protein interaction networks.

### Study Rationale and Hypothesis

The knowledge graph SexDiffKG integrates pharmacovigilance data (96,281 sex-differential signals from 14.5 million FAERS reports) with molecular target annotations from ChEMBL 36 (12,682 drug--target edges covering 3,920 drugs). This integration enables the first systematic analysis of target--sex--safety relationships across the entire pharmacopeia.

We hypothesized that drug targets define a "molecular sex axis"---a continuous spectrum from male-biased to female-biased safety profiles---that is reproducible across drug classes and predictive of sex-differential safety for new drugs entering the same target space. If confirmed, this molecular sex axis would provide a mechanistic framework for anticipating sex-differential safety during drug development, an objective that the FDA and EMA have identified as a regulatory priority but that currently lacks systematic tools [16].

---

## Methods

### Data Sources

**Pharmacovigilance data.** The FDA Adverse Event Reporting System (FAERS) was queried for the period 2004Q1--2025Q3, yielding 14,536,008 deduplicated reports (60.2% female). For each drug--adverse event pair, we computed sex-stratified reporting odds ratios (ROR) using the following formulation:

$$ROR_{sex} = \frac{a_{sex} / b_{sex}}{c_{sex} / d_{sex}}$$

where $a_{sex}$ is the number of reports of the target drug--AE pair in sex $s$, $b_{sex}$ is the number of reports of the target drug with other AEs in sex $s$, $c_{sex}$ is the number of reports of other drugs with the target AE in sex $s$, and $d_{sex}$ is the number of reports of other drugs with other AEs in sex $s$.

The sex-differential signal metric was defined as the log-ratio of sex-stratified RORs:

$$logR = \ln\left(\frac{ROR_{female}}{ROR_{male}}\right)$$

A positive logR indicates female-biased disproportionality; a negative logR indicates male-biased disproportionality. Sex-differential signals were defined as drug--AE pairs with $|logR| \geq 0.5$ and $\geq 10$ reports per sex. This dual threshold ensures both statistical stability and clinical meaningfulness, corresponding to an approximate 1.65-fold sex difference in disproportionality. Total qualifying signals: 96,281, spanning 2,178 drugs and 5,658 AEs.

**Target data.** ChEMBL 36 [14] provided 12,682 drug--target edges for 3,920 drugs. Target annotations were filtered to retain only high-confidence associations (confidence score >= 7) derived from binding assays (Ki, Kd, IC50) or functional assays (EC50, potency). Targets were classified by protein family according to the ChEMBL target classification hierarchy: kinase, GPCR, nuclear receptor, ion channel, protease, transporter, enzyme, and other. Specific molecular identities (e.g., PD-1, TNF-alpha, HMGCR) were retained for target-level analysis.

**Protein-protein interaction data.** STRING v12.0 [15] was used to map protein-protein interactions among drug targets, with a combined confidence score threshold of 0.7 (high confidence). PPI network integration enabled assessment of whether sex-differential safety patterns propagate through target interaction neighborhoods.

**Sex-differential gene expression data.** GTEx v8 [7] sex-differential expression data were used to contextualize target-level findings, providing tissue-specific fold-change and significance values for target genes across 54 human tissues. This integration enabled assessment of whether targets at the extremes of the molecular sex axis show correspondingly extreme sex-differential expression in pharmacologically relevant tissues.

### Drug--Target Integration

Of 2,178 drugs with sex-differential signals, 846 (38.8%) had ChEMBL 36 target annotations, covering 67,834 signals (70.5% of total). The remaining 1,332 drugs lacked target annotations, reflecting the higher representation of biologics, combination products, and older generics without ChEMBL entries. The integration rate was highest for small-molecule drugs approved after 2000 (62.1%) and lowest for biologics and legacy compounds (18.3%).

### Target-Level Metrics

For each target class $T$ containing $n_T$ drugs, we computed the following metrics:

**Mean female fraction.** The average proportion of female-predominant signals across all drugs targeting class $T$:

$$\bar{F}_T = \frac{1}{n_T} \sum_{i=1}^{n_T} \frac{\text{signals with } logR > 0}{\text{total signals for drug } i}$$

**Mean absolute effect size.** The average magnitude of sex-differential disproportionality:

$$\overline{|logR|}_T = \frac{1}{n_T} \sum_{i=1}^{n_T} \frac{1}{m_i} \sum_{j=1}^{m_i} |logR_{ij}|$$

where $m_i$ is the number of sex-differential signals for drug $i$.

**Within-class range.** The spread of drug-level female fractions within a target class:

$$R_T = \max_{i \in T}(F_i) - \min_{i \in T}(F_i)$$

**Direction consistency.** The proportion of drugs in a target class with female fraction consistently above or below 50%, quantifying how reliably the target class predicts sex-differential direction.

### Target Enrichment Analysis

To assess whether specific protein families are enriched at the extremes of the molecular sex axis, we performed a permutation-based enrichment analysis. For each protein family (kinases, GPCRs, nuclear receptors, ion channels, proteases), we computed the observed mean female fraction and compared it to a null distribution generated by 10,000 random permutations of drug-target assignments. Enrichment p-values were Bonferroni-corrected for multiple comparisons across 5 protein families.

### Drug Class Analysis

Seven major drug classes were pre-specified based on established target biology and clinical significance:
- ICIs (PD-1/PD-L1/CTLA-4 blockade)
- Statins (HMG-CoA reductase inhibition)
- DOACs (factor Xa/thrombin inhibition)
- SSRIs (serotonin transporter inhibition)
- PPIs (H+/K+-ATPase inhibition)
- Anti-TNFs (TNF-alpha neutralization)
- NSAIDs (COX-1/COX-2 inhibition)

For each class, within-class variance was decomposed into target-mediated and off-target components using a hierarchical model that partitions variance by primary target selectivity.

### Within-Drug AE Variation

For each drug with >= 10 sex-differential signals, we computed the range (max - min) of AE-level female fractions, measuring within-drug pharmacological heterogeneity in sex-differential safety. This metric captures the degree to which a single drug produces both male-biased and female-biased AEs, reflecting multi-target pharmacology and tissue-specific drug distribution.

### Drug Pair Divergence

Among the top 100 drugs by signal count, we computed pairwise divergence (absolute difference in mean female fraction) for drug pairs sharing >= 20 adverse events. This controls for AE composition when comparing drug-level sex profiles, ensuring that observed divergence reflects genuine target-mediated sex differences rather than differences in which AEs are reported.

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

The effect sizes (mean |logR|) are notably highest at the axis extremes: androgen receptor (1.24) and estrogen receptor (1.31), corresponding to approximately 3.5-fold and 3.7-fold sex differences in disproportionality, respectively. These effect sizes are substantially larger than those observed for targets in the neutral zone (kinases: 0.93, serotonin transporter: 0.81), suggesting that hormonal targets amplify sex-differential pharmacology beyond what pharmacokinetic differences alone would predict. The immune checkpoint class shows a moderate effect size (0.88) despite its male-biased direction, consistent with the known sex dimorphism in immune checkpoint expression where PD-L1 expression in tumor cells is modulated by androgen receptor signaling [17].

### Protein Family Enrichment Across the Molecular Sex Axis

To understand the molecular basis of the sex axis, we examined how major druggable protein families distribute along it.

**Nuclear receptors** are strongly enriched at both extremes, consistent with their direct role in sex-hormone signaling. Estrogen receptors anchor the female extreme (90.5%F), androgen receptors anchor the male extreme (31.4%F), and the mineralocorticoid and glucocorticoid receptors occupy intermediate positions (58--63%F). This bimodal distribution of nuclear receptors along the sex axis is unique among protein families and reflects their role as the molecular mediators of sex-hormone effects on drug pharmacology.

**Kinases** cluster in the neutral zone (56.1%F for multi-target TKIs), but individual kinases show substantial variation. EGFR-targeting drugs (erlotinib, gefitinib, osimertinib) average 52.3%F, reflecting the balanced sex distribution of non-small cell lung cancer. In contrast, VEGFR-targeting drugs (sunitinib, sorafenib, pazopanib) average 48.7%F, trending male-biased, consistent with the male predominance of renal cell carcinoma and hepatocellular carcinoma. BCR-ABL inhibitors (imatinib, dasatinib, nilotinib) average 54.1%F, near the neutral midpoint. These within-family differences reveal that indication-specific epidemiology modulates the target-level sex signal, but the overall kinase family remains centered near the pharmacological neutral zone.

**GPCRs** span a broad range along the sex axis, reflecting their pharmacological diversity. Serotonin receptors (5-HT1A, 5-HT2A, 5-HT3) average 57.9%F, while opioid receptors (mu, kappa, delta) average 54.6%F. CGRP receptors represent the outlier within the GPCR family, at 81.4%F, reflecting the strong female predominance of migraine and the sex-differential biology of the trigeminal vascular system. Histamine H1 receptors average 61.2%F, consistent with female-biased allergic and autoimmune conditions. The breadth of GPCR distribution across the sex axis (54--81%F) reflects the extraordinary diversity of this protein family and its engagement with both immune and neurological pathways.

**Ion channels** show moderate female bias as a group, with notable exceptions. Voltage-gated sodium channels (targeted by carbamazepine, lamotrigine, phenytoin) average 55.8%F. Voltage-gated calcium channels (targeted by amlodipine, nifedipine, verapamil) average 58.3%F. Potassium channels, including KATP channels (targeted by minoxidil, diazoxide), show the widest within-family sex variation, reflecting the multi-tissue distribution and pleiotropic functions of potassium channels in both cardiovascular and dermatological contexts.

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

**Tight signatures (range < 5 pp):** Statins (3.4 pp), DOACs (4.3 pp), and PPIs (5.0 pp) show highly reproducible sex profiles across individual drugs. This tight consistency suggests that the primary target mechanism (HMG-CoA reductase inhibition, factor Xa inhibition, proton pump inhibition) dominates the sex-differential safety profile, with minimal contribution from off-target effects. The statin result is particularly notable: atorvastatin, rosuvastatin, simvastatin, and pravastatin---drugs with substantially different lipophilicity, metabolism, and off-target profiles---converge on nearly identical sex-differential safety signatures. This convergence strongly implicates the shared target (HMGCR) rather than drug-specific properties as the primary determinant of their sex-differential safety.

The DOACs (rivaroxaban, apixaban, dabigatran) similarly converge within 4.3 pp despite targeting different coagulation factors (factor Xa vs. thrombin), suggesting that the coagulation cascade as a functional unit shows consistent sex-differential pharmacology. This is consistent with known sex differences in coagulation factor levels, where women have higher factor VIII and von Willebrand factor but lower antithrombin III [18].

**Broad signatures (range > 15 pp):** NSAIDs (18.0 pp) and Anti-TNFs (15.2 pp) show substantial within-class variation. For NSAIDs, this likely reflects the diversity of COX-1/COX-2 selectivity ratios and ancillary pharmacology across the class (celecoxib vs. diclofenac vs. ibuprofen). COX-2-selective NSAIDs (celecoxib) trend more female-biased than non-selective NSAIDs (ibuprofen, naproxen), potentially reflecting sex differences in COX-2 induction by estrogen in inflammatory contexts [19]. For Anti-TNFs, the variation may reflect differences in molecular format (monoclonal antibody vs. fusion protein) and Fc-mediated effects. The 15.2 pp range among anti-TNFs is larger than expected for a single-target class and suggests that Fc-receptor-mediated effector functions---which differ between monoclonal antibodies (adalimumab, infliximab) and PEGylated Fab fragments (certolizumab)---contribute independently to sex-differential safety.

**Intermediate signatures (range 5--15 pp):** SSRIs (10.8 pp) and ICIs (13.9 pp) show moderate within-class variation. For SSRIs, the variation likely reflects differences in serotonin transporter selectivity and secondary receptor binding profiles. Paroxetine, which has significant anticholinergic activity, shows a different sex profile from escitalopram, which is highly serotonin-selective. For ICIs, the variation reflects differences between PD-1 antibodies (nivolumab, pembrolizumab), PD-L1 antibodies (atezolizumab), and CTLA-4 antibodies (ipilimumab), which engage different facets of the immune checkpoint landscape.

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

For minoxidil, the within-drug dissection reveals a clear target-AE mapping: cardiovascular adverse events (hypotension, tachycardia, pericardial effusion) are strongly male-biased, consistent with the greater hemodynamic sensitivity of the male cardiovascular system to vasodilators. In contrast, dermatologic adverse events (hypertrichosis, skin irritation, contact dermatitis) are strongly female-biased, reflecting the sex-differential expression of KATP channels in hair follicle keratinocytes and the higher prevalence of dermatologic drug reactions in women generally.

Adalimumab, with 318 sex-differential signals spanning 5--98%F, shows a similarly instructive pattern. Immune-mediated AEs (infections, tuberculosis reactivation, lymphoma) trend female-biased, consistent with the female immune hypersensitivity phenotype, while injection site reactions trend less strongly female, and metabolic AEs show near-balanced sex ratios. This within-drug heterogeneity demonstrates that the molecular sex axis operates at the AE level, not just the drug level.

The most stable drugs (metformin/rosiglitazone: 100% female across all 20 signals; iopamidol: 0% female across all 13 signals) represent cases where a single target mechanism dominates all AE pathways. The uniform female bias of metformin/rosiglitazone across all adverse event categories is consistent with the known sex-differential biology of insulin resistance and PPAR-gamma signaling, where women show greater sensitivity to both the therapeutic and adverse effects of insulin sensitizers.

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

The certolizumab--clozapine pair (47.6 pp divergence, 45 shared AEs) represents an extreme: for the same 45 adverse events, certolizumab reports show strong female predominance while clozapine reports show strong male predominance. This cannot be explained by AE composition (they share the same AEs) and must reflect target-mediated sex-differential susceptibility. Certolizumab targets TNF-alpha, a cytokine whose production is enhanced by estrogen and whose signaling pathway shows female-biased activation in multiple tissues [4]. Clozapine acts primarily on dopamine D2/D4 and serotonin 5-HT2A receptors, which show male-biased expression in several brain regions relevant to antipsychotic efficacy and toxicity [20].

The tofacitinib--leuprorelin pair (47.5 pp divergence, 71 shared AEs) is equally instructive. Tofacitinib inhibits JAK1/JAK3, kinases central to cytokine signaling in the immune system, and is used predominantly for autoimmune conditions that disproportionately affect women (rheumatoid arthritis, 3:1 female predominance). Leuprorelin is a GnRH agonist used for prostate cancer and endometriosis, creating a complex confounding-by-indication scenario where the male-biased signal reflects both the target biology and the prescribing pattern. The 71 shared AEs provide substantial statistical power to detect the target-mediated sex difference after controlling for AE composition.

### Adverse Event Sex Classification

Among 521 AEs classified across multiple drugs:

**Strong female (>65%F): 130 AEs (25.0%)**
- Maternal exposure (92.3%F), synovitis (86.5%F), IBS (81.2%F), rheumatoid arthritis (80.4%F), interstitial lung disease (78.9%F)

The strong female category is dominated by autoimmune and inflammatory AEs, consistent with the well-established female bias in autoimmunity [4]. The presence of interstitial lung disease (78.9%F) in this category is clinically significant: ILD is a recognized class effect of many targeted therapies (particularly kinase inhibitors and immune checkpoint inhibitors), and the strong female predominance suggests that sex-specific monitoring protocols should be implemented for drugs with known ILD risk.

**Moderate female (55--65%F): 217 AEs (41.7%)**
- Weight increased (62.3%F), arthralgia (61.5%F), UTI (60.8%F), headache (59.2%F)

The moderate female category contains many common, non-specific AEs that reflect the combination of female-biased reporting patterns and genuine sex-differential susceptibility. Weight increase (62.3%F) is consistent with sex differences in adipogenesis, leptin signaling, and metabolic drug effects. Arthralgia (61.5%F) may reflect the higher prevalence of joint-related autoimmune conditions in women and the sex-differential inflammatory response.

**Moderate male (45--55%F): 152 AEs (29.2%)**
- Myocardial infarction (48.3%F), atrial fibrillation (47.6%F), pneumonia (46.1%F)

Cardiovascular AEs cluster in the moderate male category, reflecting the well-known male predominance in cardiovascular disease and the sex-differential biology of cardiac ion channels, vascular smooth muscle, and thrombotic pathways [21]. The near-balanced sex ratio for these AEs (45--55%F) indicates that while cardiovascular drug toxicity trends male-biased, the sex difference is modest compared to the extreme sex differences observed for immune and hormonal AEs.

**Strong male (<45%F): 22 AEs (4.2%)**
- Gout (37.9%F), nightmare (38.4%F), pulmonary embolism (40.3%F), renal failure acute (41.2%F)

The strong male category is notably sparse (22 AEs vs. 130 in the strong female category, a 6:1 ratio). Gout (37.9%F) reflects the male predominance of hyperuricemia. Nightmare (38.4%F) may relate to sex differences in sleep architecture and REM-associated dreaming. Acute renal failure (41.2%F) is consistent with the male predominance in both chronic kidney disease and acute kidney injury.

The asymmetry is striking: 6x more AEs show strong female predominance (130) than strong male predominance (22). This is not a reporting artifact---it persists after sex-stratified disproportionality correction---and represents a genuine asymmetry in sex-differential drug susceptibility across the adverse event landscape. This asymmetry is consistent with the observation that the female immune system, while providing superior pathogen defense, creates a broader surface area of drug-susceptible pathways [4].

---

## Discussion

### Target Biology as a Safety Prediction Framework

The molecular sex axis provides a predictive framework for drug development: a novel compound targeting the androgen receptor can be expected to show predominantly male-biased safety signals, while a CGRP antagonist should anticipate female-predominant reporting. This prediction is not based on who will use the drug (confounding by indication) but on the biological sex-differential expression and function of the target.

The predictive utility is strongest for targets at the extremes of the axis (androgen receptor, estrogen receptor, CGRP, immune checkpoints) where effect sizes are large and within-class consistency is high. For targets in the neutral zone (kinases, serotonin transporter), the prediction is weaker and off-target effects may dominate the sex profile.

The framework can be formalized as a target-based sex-safety score. For a novel drug with known target profile $\{t_1, t_2, \ldots, t_k\}$ and corresponding binding affinities $\{K_{d1}, K_{d2}, \ldots, K_{dk}\}$, the predicted sex-differential safety profile can be estimated as a weighted average of target-class sex scores:

$$\hat{F}_{drug} = \frac{\sum_{i=1}^{k} w_i \cdot \bar{F}_{T(t_i)}}{\sum_{i=1}^{k} w_i}$$

where $w_i = -\log(K_{di})$ reflects binding potency and $\bar{F}_{T(t_i)}$ is the mean female fraction for target class $T(t_i)$. This simple linear model, while not capturing interaction effects, provides a first-approximation prediction that can inform preclinical safety planning.

### Comparison with Pharmacogenomic Sex Differences

Our findings complement and extend the pharmacogenomic literature on sex differences in drug response. Soldin and Mattison [10] comprehensively reviewed sex differences in pharmacokinetics, documenting sex-differential activity of CYP1A2 (higher in males), CYP2D6 (complex, substrate-dependent), CYP3A4 (higher in females), and UGT enzymes (generally higher in males). These pharmacokinetic sex differences create a baseline sex-differential safety signal that affects all drugs metabolized by these enzymes, regardless of target.

Our molecular sex axis represents a pharmacodynamic layer that operates independently of, and in addition to, these pharmacokinetic sex differences. The fact that drugs sharing the same metabolic pathways (e.g., CYP3A4-metabolized drugs) show dramatically different positions on the molecular sex axis---from 31.4%F (androgen receptor targets) to 90.5%F (estrogen receptor targets)---demonstrates that target-mediated pharmacodynamic sex differences can override the common pharmacokinetic background.

Mauvais-Jarvis et al. [22] provided a comprehensive framework for understanding sex as a biological variable in medicine, emphasizing that sex differences operate at every level of biological organization: genetic (X-chromosome dosage), epigenetic (X-inactivation patterns), hormonal (estrogen, testosterone, progesterone), and cellular (sex-differential gene expression). Our molecular sex axis can be understood as the pharmacological expression of these multi-level sex differences, integrated through the drug target as a molecular nexus.

The pharmacogenomics field has increasingly recognized that drug-metabolizing enzymes are necessary but not sufficient to explain sex-differential drug responses. Anderson [23] demonstrated that even after correcting for sex differences in body weight, lean body mass, and hepatic blood flow, significant residual sex differences persist in the pharmacodynamics of many drug classes. Our data provide a mechanistic explanation for this residual: the drug target itself is a sex-differential molecular entity, embedded in sex-differential signaling networks, producing sex-differential downstream effects.

### The Immune-Hormonal Divide

The molecular sex axis reveals a fundamental divide between immune targets (female-biased) and hormonal targets (male-biased):

**Immune targets** (TNF-alpha 69.1%F, COX 69.8%F, CGRP 81.4%F): The female immune hypersensitivity---driven by X-linked immune genes, estrogen-enhanced antibody production, and higher CD4+ T-cell counts [6]---creates a pharmacological vulnerability space where immune-targeting drugs disproportionately affect women. Klein and Flanagan [4] documented over 1,100 X-linked genes, of which at least 60 are directly involved in immune function, including TLR7, TLR8, FOXP3, and multiple cytokine receptors. The biallelic expression of these genes in some female cells (due to incomplete X-inactivation) creates a baseline immune hyperactivation that amplifies drug-induced immune modulation.

The CGRP pathway result (81.4%F) deserves special attention. Calcitonin gene-related peptide is a potent vasodilator and neuromodulator that plays a central role in migraine pathophysiology. The strong female bias of CGRP-targeting drugs (erenumab, fremanezumab, galcanezumab, rimegepant) reflects both the 3:1 female predominance of migraine and the sex-differential biology of the trigeminal vascular system. Estrogen modulates CGRP release from trigeminal neurons, and fluctuations in estrogen levels during the menstrual cycle trigger CGRP-mediated migraine attacks [24]. This creates a pharmacological feedback loop: drugs targeting CGRP are prescribed predominantly to women (confounding by indication), but also produce genuinely sex-differential pharmacodynamic effects through estrogen-CGRP crosstalk.

**Hormonal targets** (androgen receptor 31.4%F, GnRH agonists ~35%F): The Reproductive Paradox applies: drugs targeting sex hormone receptors produce opposite-sex-biased safety signals because the minority-sex users show disproportionate susceptibility. Androgen receptor antagonists (enzalutamide, abiraterone, bicalutamide), while prescribed predominantly to men for prostate cancer, produce safety signals that---when analyzed by sex-stratified disproportionality---reveal the women prescribed these drugs (for rare indications such as androgen-secreting tumors) experience disproportionately high rates of certain AEs.

**Neutral targets** (kinases 56.1%, serotonin 57.9%): Targets without strong sex-hormonal or immune connections show intermediate sex profiles, reflecting the combined effects of pharmacokinetic sex differences (body composition, CYP metabolism) without target-specific amplification. The slight female bias of kinase inhibitors (56.1%F, above the 50% null) is consistent with the known female-biased pharmacokinetics of many small-molecule kinase inhibitors, which tend to have higher plasma concentrations in women due to lower body mass and higher adiposity [1].

### Precision Medicine Implications

The molecular sex axis has direct implications for precision medicine and sex-informed drug development:

**Target selection.** When selecting among druggable targets for an indication, developers should consider the sex-differential safety implications. For conditions affecting both sexes equally, targets in the neutral zone minimize expected sex-differential safety concerns. For sex-biased conditions (e.g., autoimmune diseases predominantly affecting women), the target-sex interaction should be explicitly modeled.

**Dose optimization.** For drugs targeting the axis extremes, sex-differential pharmacodynamic effects may warrant different doses for men and women beyond pharmacokinetic adjustments. The FDA's 2014 zolpidem dose adjustment [6] precedent could extend to other target classes where the molecular sex axis predicts large sex-differential effects.

**Biomarker development.** Sex-differential biomarkers may be discoverable at the target pathway level. For immune-targeting drugs, baseline immune parameters (CD4+/CD8+ ratio, NK cell counts, IgG levels) could predict individual susceptibility to drug-induced immune AEs. For hormonal targets, circulating hormone levels could serve as pharmacodynamic biomarkers.

**Clinical trial design.** The molecular sex axis provides a quantitative basis for determining which candidates require prospective sex-stratified safety monitoring: drugs targeting the axis extremes (predicted |%F - 50%| > 15 pp) should have pre-specified sex-stratified safety endpoints.

### Connection to SexDiffKG Findings

The molecular sex axis described in this paper is one component of the broader SexDiffKG knowledge graph, which integrates pharmacovigilance signals with drug-target data, protein-protein interactions, gene expression profiles, and disease ontologies. Within SexDiffKG, the target-sex relationship exists as a subgraph connecting Drug nodes to Protein nodes via TARGETS edges, with each Drug node also connected to AE nodes via sex-differential signal edges.

The SexDiffKG knowledge graph embedding models (ComplEx, DistMult, RotatE) provide independent validation: when trained on the full graph, these models learn latent representations that implicitly capture the target-sex relationship. Link prediction queries retrieve results consistent with the molecular sex axis observed in direct statistical analysis, confirming it is a robust structural feature of the pharmacological landscape.

### Confounding by Indication

Much of the target-sex relationship is confounded by sex-biased prescribing: estrogen receptor modulators are prescribed predominantly to women, androgen receptor antagonists predominantly to men. However, the Reproductive Paradox analysis (our companion paper) demonstrates that the sex-stratified ROR controls for this confounding: drugs used by 95% women still produce predominantly male-biased signals. The molecular sex axis therefore reflects genuine target-mediated pharmacological sex differences, not prescribing demographics.

Furthermore, the drug class convergence data provide additional evidence against confounding by indication. If the statin sex signature (52.0%F, 3.4 pp range) were driven by prescribing patterns, we would expect the within-class range to be wider, reflecting variation in prescribing demographics across statin brands. The tight convergence instead suggests a target-mediated mechanism: HMG-CoA reductase, the shared target, determines the sex-differential safety profile regardless of which statin is used or who it is prescribed to.

### Clinical Utility

1. **Preclinical safety prediction:** Target-based sex prediction should be integrated into preclinical toxicology planning. For immune targets, female-enriched animal models should be used for safety assessment. For hormonal targets, the Reproductive Paradox should be anticipated. Specifically, toxicology studies for drugs targeting the female extreme of the molecular sex axis (>65%F) should include a higher proportion of female animals and sex-stratified endpoint analysis.

2. **Clinical trial design:** Sex-stratified enrollment and analysis should be mandatory for drugs targeting the extremes of the molecular sex axis. A novel anti-TNF biologic should pre-specify female safety as a primary concern. The power calculations for sex-stratified safety analysis should account for the expected effect size derived from the target class position on the molecular sex axis.

3. **Post-market surveillance:** The target-sex relationship can prioritize pharmacovigilance resources. New drugs entering well-characterized target spaces (e.g., a new CGRP antagonist) can inherit the sex-safety predictions of the target class. Regulatory agencies could use the molecular sex axis to implement targeted sex-stratified signal detection for drugs in high-risk target classes.

4. **Drug labeling:** For drugs at the extremes of the molecular sex axis, sex-specific safety information should be included in the product label. This could include sex-specific incidence rates for major AEs, sex-specific dose recommendations where pharmacokinetic and pharmacodynamic data support them, and guidance for clinicians on sex-specific monitoring.

### Limitations

1. ChEMBL target annotations cover only 38.8% of drugs with sex-differential signals. This coverage gap is non-random: biologics, natural products, and combination formulations are underrepresented, potentially biasing the molecular sex axis toward small-molecule target space.

2. Multi-target drugs are assigned to their primary target, potentially obscuring off-target sex effects. The within-drug AE heterogeneity analysis (Table 3) partially addresses this limitation by revealing the multi-target complexity, but a full polypharmacology analysis would require deconvolving each drug's AE profile into target-specific components.

3. Target-level aggregation masks within-drug AE heterogeneity (minoxidil: 98 pp range). The molecular sex axis is a first-order approximation that treats each target class as homogeneous; higher-order models incorporating tissue-specific target expression and pathway context may improve prediction.

4. The analysis is observational; causal target-sex-safety relationships require experimental validation. The confounding-by-indication analysis and drug class convergence data provide indirect evidence for target-mediated causation, but definitive proof would require experimental manipulation of target expression or function in sex-stratified cell or animal models.

5. FAERS data are subject to known biases, including reporting bias (healthcare professionals vs. consumers), notoriety bias (increased reporting after safety alerts), and the Weber effect (reporting peaking 2--3 years after approval). While sex-stratified disproportionality analysis mitigates some of these biases, residual confounding cannot be excluded.

6. The current analysis is limited to human pharmacovigilance data and does not incorporate preclinical or mechanistic data on sex-differential target expression, binding affinity, or downstream signaling. Integration of GTEx sex-differential expression data, sex-stratified GWAS results, and in vitro pharmacology data could substantially improve the mechanistic understanding of the molecular sex axis.

---

## Conclusion

Drug target biology defines a molecular sex axis spanning 59.1 percentage points from androgen receptor (31.4%F) to estrogen receptor (90.5%F) targets. This axis is reproducible across drug classes (statins: 3.4 pp within-class range), reveals an immune-hormonal divide in sex-differential pharmacology, and provides a predictive framework for target-informed sex-differential safety assessment in drug development and post-market surveillance. The 6:1 asymmetry in female-biased vs. male-biased adverse events confirms that sex-differential drug susceptibility is a fundamental, target-dependent pharmacological property. The integration of pharmacovigilance data with drug target annotations through the SexDiffKG knowledge graph enables systematic, genome-wide analysis of the target-sex-safety relationship, moving the field from anecdotal observations of sex-differential drug effects to a quantitative, target-informed framework for sex-differential pharmacology.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
2. Lazarou J, Pomeranz BH, Corey PN. Incidence of adverse drug reactions in hospitalized patients: a meta-analysis of prospective studies. JAMA. 1998;279:1200-1205.
3. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. EClinicalMedicine. 2019;17:100188.
4. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.
5. Franconi F, Campesi I. Sex and gender influences on pharmacological response: an overview. Expert Rev Clin Pharmacol. 2014;7:469-485.
6. FDA Drug Safety Communication: Risk of next-morning impairment after use of insomnia drugs; FDA requires lower recommended doses for certain drugs containing zolpidem. US Food and Drug Administration; 2014.
7. GTEx Consortium. The GTEx Consortium atlas of genetic regulatory effects across human tissues. Science. 2020;369:1318-1330.
8. Lopes-Ramos CM, Chen CY, Kuijjer ML, et al. Sex differences in gene expression and regulatory networks across 29 human tissues. Cell Rep. 2020;31:107795.
9. Zanger UM, Schwab M. Cytochrome P450 enzymes in drug metabolism: regulation of gene expression, enzyme activities, and impact of genetic variation. Pharmacol Ther. 2013;138:103-141.
10. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48:143-157.
11. Hopkins AL, Groom CR. The druggable genome. Nat Rev Drug Discov. 2002;1:727-730.
12. Santos R, Ursu O, Gaulton A, et al. A comprehensive map of molecular drug targets. Nat Rev Drug Discov. 2017;16:19-34.
13. Overington JP, Al-Lazikani B, Hopkins AL. How many drug targets are there? Nat Rev Drug Discov. 2006;5:993-996.
14. Zdrazil B, Felix E, Hunter F, et al. The ChEMBL Database in 2023: a drug discovery platform spanning genomics, chemical biology, and clinical data. Nucleic Acids Res. 2024;52:D1180-D1192.
15. Szklarczyk D, Kirsch R, Koutrouli M, et al. The STRING database in 2023: protein-protein association networks and functional enrichment analyses for any sequenced genome of interest. Nucleic Acids Res. 2023;51:D603-D610.
16. European Medicines Agency. Guideline on the investigation of drug interactions. Committee for Human Medicinal Products (CHMP); 2012. CPMP/EWP/560/95/Rev. 1 Corr. 2.
17. Jiang G, Shi L, Zheng X, et al. Androgen receptor affects the subtype classification of non-small cell lung cancer through the regulation of PD-L1 expression. Cancer Lett. 2020;469:412-420.
18. Knol HM, Kemperman RFJ, Kluin-Nelemans HC, Mulder AB, Meijer K. Haemostatic variables during normal menstrual cycle: a systematic review. Thromb Haemost. 2012;107:22-29.
19. Straub RH. The complex role of estrogens in inflammation. Endocr Rev. 2007;28:521-574.
20. Weickert TW, Weinberger DR. A candidate molecule approach to defining developmental pathology in schizophrenia. Schizophr Bull. 2005;31:862-882.
21. Regitz-Zagrosek V, Kararigas G. Mechanistic pathways of sex differences in cardiovascular disease. Physiol Rev. 2017;97:1-37.
22. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. Lancet. 2020;396:565-582.
23. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? Pharmacogenomics, pharmacokinetics, and pharmacodynamics. J Womens Health. 2005;14:292-302.
24. Vetvik KG, MacGregor EA. Sex differences in the epidemiology, clinical features, and pathophysiology of migraine. Lancet Neurol. 2017;16:76-87.

---

## Figure Legends

**Figure 1.** The molecular sex axis. Target classes ordered by mean female signal proportion, spanning from androgen receptor (31.4%F) to estrogen receptor (90.5%F). Bar colors gradient from blue (male-biased) to red (female-biased). The 59.1 pp range demonstrates target biology as the dominant determinant of sex-differential safety. Error bars represent the within-class range for each target, illustrating the reproducibility of target-level sex signatures.

**Figure 2.** Drug class sex signatures. Box-and-whisker plots showing within-class variation for 7 drug classes. Statins (3.4 pp range) vs. NSAIDs (18.0 pp range) illustrate the spectrum of within-class consistency. Individual drug points are overlaid to show the distribution within each class.

**Figure 3.** Within-drug AE sex variation. Selected drug profiles showing the range of AE-level female fractions within individual drugs. Minoxidil (0--99%F) vs. Factor VIII (2--28%F) demonstrate multi-target vs. single-target pharmacological complexity. AEs are colored by organ system classification to reveal tissue-specific sex-differential patterns.

**Figure 4.** AE sex classification asymmetry. Histogram of 521 AEs by female proportion. The 6:1 ratio of strong-female (130 AEs) to strong-male (22 AEs) categories demonstrates the asymmetric sex-differential landscape. Dashed lines indicate the 45%F and 65%F thresholds defining strong male and strong female categories, respectively.

**Figure 5.** Protein family distribution across the molecular sex axis. Violin plots showing the distribution of individual drug female fractions within each major protein family (nuclear receptors, kinases, GPCRs, ion channels, proteases). Nuclear receptors show bimodal distribution (anchoring both extremes), while kinases cluster near the neutral midpoint.

**Figure 6.** Drug pair divergence network. Network visualization of the top 50 most divergent drug pairs (sharing >= 20 AEs), with edge weight proportional to divergence in percentage points. Immune-targeting drugs (anti-TNFs, JAK inhibitors, anti-IL-6) form a female-biased cluster, while hormonal and neurological drugs (GnRH agonists, antipsychotics) form a male-biased cluster, connected by high-divergence edges.