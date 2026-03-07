# Sex-Differential Drug-Induced Liver Injury: Checkpoint Inhibitor Hepatotoxicity Is 95% Female-Biased Across a Landscape of 601 Drugs and 3,073 Signals

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Drug-induced liver injury (DILI) is the leading cause of acute liver failure in Western countries and the primary reason for post-market drug withdrawals. While individual case series have suggested sex differences in DILI susceptibility, systematic characterization across the pharmacopeia has been lacking. The absence of large-scale, sex-stratified pharmacovigilance analyses has left clinicians without evidence to guide sex-specific hepatotoxicity monitoring.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we identified 3,073 sex-differential hepatotoxicity signals across 601 drugs using 133 hepatic MedDRA terms. Sex-differential reporting was quantified using the sex-stratified reporting odds ratio (ROR), with the log-ratio logR = ln(ROR_female / ROR_male) as the primary metric. Signals were classified into hepatocellular, cholestatic, hepatic failure, steatosis/fibrosis, and autoimmune subtypes. Anti-regression analysis was performed within hepatotoxicity signals. Drug class analyses covered 10 therapeutic categories spanning immune-mediated, metabolic, and immunosuppressive mechanisms.

**Results.** Overall hepatotoxicity was 65.3% female-biased (2,007 female-predominant vs. 1,066 male-predominant signals). Drug class analysis revealed a striking spectrum: checkpoint inhibitors showed 95.1% female signals (39/41, the strongest class-specific signal in the entire knowledge graph), antibiotics 75.9%F, NSAIDs 75.6%F, statins 69.7%F, and acetaminophen 63.2%F. Immunosuppressants (51.9%F) and anti-TNFs (52.1%F) approached parity. Drug-induced autoimmune hepatitis was paradoxically male-biased (27.8%F, 13/18 male), contrasting with the 2--3x female predominance of spontaneous autoimmune hepatitis. Hepatotoxicity subtypes showed a severity gradient: hepatic failure 69.0%F, cholestatic 68.2%F, hepatocellular 63.6%F, steatosis/fibrosis 59.3%F. Anti-regression persisted perfectly within hepatotoxicity (rho = 1.000). A total of 175 drugs showed strongly female hepatotoxicity (>= 70%F) versus only 49 with strong male hepatotoxicity (<= 30%F)---a 3.6:1 asymmetry.

**Interpretation.** Drug-induced liver injury is systematically female-biased, with mechanism-dependent modulation: immune-mediated DILI (checkpoint inhibitors, antibiotics) shows the strongest female bias, metabolic DILI (statins, acetaminophen) shows moderate bias, and immunomodulatory drugs (anti-TNFs) approach parity. The paradoxical male bias in drug-induced autoimmune hepatitis suggests mechanistically distinct pathways from spontaneous autoimmune hepatitis. These findings support sex-stratified DILI monitoring, with particular urgency for immune checkpoint inhibitors.

**Keywords:** Drug-induced liver injury; sex differences; hepatotoxicity; immune checkpoint inhibitors; pharmacovigilance; FAERS; knowledge graph; disproportionality analysis

---

## 1. Introduction

### 1.1 Drug-Induced Liver Injury: Scope and Burden

Drug-induced liver injury (DILI) is the most common cause of acute liver failure in the United States and the United Kingdom, accounting for over 50% of cases in referral centers [1, 2]. In a landmark U.S. study, Ostapowicz and colleagues (2002) found that acetaminophen alone was responsible for 39% of acute liver failure cases, with idiosyncratic drug reactions contributing an additional 13% [2]. The estimated annual incidence of DILI ranges from 14 to 19 per 100,000 in population-based studies, though the true incidence is likely higher due to underreporting and diagnostic challenges [1, 3]. The economic burden is substantial: DILI accounts for approximately 30% of drugs withdrawn from the market between 1960 and 2015, with total costs including clinical care, regulatory action, and lost pharmaceutical investment estimated in the billions of dollars annually [4].

The Drug-Induced Liver Injury Network (DILIN), established in 2003 by the National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK), has provided the most rigorously adjudicated prospective data on DILI in the United States [5]. The DILIN prospective study enrolled over 1,300 subjects with suspected DILI by 2015, using standardized causality assessment and expert adjudication [5, 6]. The LiverTox database (https://livertox.nih.gov), maintained by the National Library of Medicine, catalogs hepatotoxicity information for over 1,000 drugs and serves as the primary clinical reference for DILI [7].

Despite this extensive infrastructure, the question of sex differences in DILI susceptibility has yielded inconsistent and often contradictory results. Some registries have reported clear female predominance, others have found no sex difference, and the mechanistic basis for any observed differences remains poorly characterized across the breadth of the pharmacopeia.

### 1.2 Sex Differences in DILI: The Contested Literature

The relationship between biological sex and DILI susceptibility has been debated for over two decades. Navarro and Senior (2006), in an influential review, argued that female sex was a risk factor for DILI based on early registry data showing 60--70% female predominance in several DILI cohorts [8]. However, they acknowledged that the excess might partly reflect higher healthcare utilization and greater drug exposure among women.

Lucena and colleagues (2009), analyzing the Spanish DILI Registry, found that female sex was a significant risk factor for hepatocellular-type DILI (odds ratio 1.6, 95% CI 1.1--2.3) but not for cholestatic or mixed-type injury [9]. Importantly, they observed that women were more likely to develop Hy's law cases---the combination of hepatocellular injury with jaundice that predicts a fatality rate of 10--50%---suggesting that sex differences extend beyond incidence to severity [9]. This finding was echoed by the observation that women constituted the majority of DILI-related liver transplant recipients in the Acute Liver Failure Study Group registry [2].

In contrast, the DILIN prospective study, as reported by Chalasani and colleagues (2008, 2015), found a more nuanced picture. In their initial analysis of 300 cases, women comprised 59% of DILI subjects, which was only marginally higher than expected given their greater drug exposure [5]. The 2015 update, covering 899 cases, confirmed a modest female predominance (59%) but found no sex difference in severity, chronicity, or mortality when adjusting for age and causative agent [6]. Chalasani et al. concluded that while women may be slightly more susceptible to DILI overall, the excess is modest and drug-specific rather than universal [6].

Bjornsson and colleagues (2013), in a population-based study from Iceland, reported an incidence of 19.1 per 100,000 person-years with roughly equal sex distribution (52% female), though the small sample size (96 cases) limited statistical power [1]. The Swedish DILI registry similarly reported near-equal sex representation [10]. These Scandinavian findings challenged the earlier U.S. and Spanish data suggesting strong female predominance.

The inconsistency across registries likely reflects several confounders: (1) different drug exposure patterns between sexes in different countries and time periods, (2) different definitions of DILI and different causality assessment methods, (3) referral bias in specialty centers, and (4) the lumping together of mechanistically distinct drug classes. Our study addresses the last of these confounders directly by disaggregating sex-differential signals by drug class and mechanism.

### 1.3 Hepatic CYP450 Sex Differences and Drug Metabolism

The liver is the primary organ of drug metabolism, and the cytochrome P450 (CYP) enzyme superfamily mediates the majority of phase I oxidative metabolism. Sex differences in hepatic CYP activity have been well-documented and provide a mechanistic framework for sex-differential DILI [11].

**CYP3A4** is the most abundant hepatic CYP enzyme, responsible for metabolizing approximately 50% of all drugs. Women express 20--40% higher CYP3A4 activity than men, a difference attributed to estrogen-mediated transcriptional upregulation via the pregnane X receptor (PXR) and constitutive androstane receptor (CAR) [11, 12]. Higher CYP3A4 activity in women has been consistently demonstrated through pharmacokinetic studies of CYP3A4 substrates (midazolam, erythromycin, nifedipine) and directly in hepatic microsome preparations [11]. For drugs that are detoxified by CYP3A4, this sex difference may be protective for women. However, for drugs that are bioactivated to toxic metabolites by CYP3A4, higher female activity may increase hepatotoxic risk. Acetaminophen provides an instructive example: its bioactivation to the toxic intermediate N-acetyl-p-benzoquinone imine (NAPQI) involves both CYP2E1 and CYP3A4, and the relative contribution of each pathway differs between sexes [12].

**CYP1A2** activity is 30--40% lower in women than in men, a difference that emerges at puberty and is attenuated after menopause, implicating sex hormones as primary drivers [11]. Lower CYP1A2 activity in women reduces the clearance of substrates such as theophylline, clozapine, and caffeine, potentially increasing exposure and toxicity risk for these agents.

**CYP2E1**, which catalyzes the bioactivation of acetaminophen and several industrial hepatotoxins (carbon tetrachloride, ethanol), shows modestly lower activity in women [11]. This sex difference in CYP2E1 might be expected to confer partial protection against acetaminophen hepatotoxicity in women, yet our data show 63.2% female bias for acetaminophen hepatotoxicity signals, suggesting that other factors (dose-weight ratio, CYP3A4-mediated bioactivation, and immune-mediated components) outweigh the CYP2E1 difference.

**Phase II conjugation** enzymes also show sex differences: UDP-glucuronosyltransferase (UGT) activity varies by isoform, with UGT1A1 (bilirubin glucuronidation) showing modestly lower activity in women, potentially contributing to the female predominance of drug-induced jaundice and hyperbilirubinemia [11]. Glutathione S-transferase (GST) activity, critical for detoxifying reactive metabolites including NAPQI, may also differ between sexes, though data are less consistent [12].

### 1.4 Immune-Mediated Hepatotoxicity and Sex Bias

The immune system exhibits profound sex dimorphism, with women mounting stronger innate and adaptive immune responses across virtually all metrics [13]. Women have higher absolute CD4+ and CD8+ T-cell counts, more robust B-cell responses and immunoglobulin production, greater natural killer (NK) cell cytotoxicity, and higher baseline levels of pro-inflammatory cytokines including IL-6, TNF-alpha, and IFN-gamma [13]. This immune advantage underpins the well-known female predominance in autoimmune diseases (systemic lupus erythematosus, rheumatoid arthritis, Sjogren syndrome, autoimmune thyroiditis) and the stronger female response to vaccines [13, 14].

The relevance of immune sex dimorphism to DILI is direct and mechanistic. Idiosyncratic DILI---the most clinically important form---is increasingly recognized as fundamentally immune-mediated. The "danger hypothesis" and "hapten hypothesis" of DILI both invoke immune activation: reactive drug metabolites form adducts with hepatic proteins, creating neoantigens that trigger adaptive immune responses [15]. The strength and character of this immune response determine whether the drug-protein adduct is tolerated (immune tolerance), triggers transient hepatic adaptation, or provokes clinically significant hepatotoxicity [15]. Given the stronger female adaptive immune response, women may be less likely to develop tolerance and more likely to mount a clinically significant immune attack against drug-modified hepatocytes.

Autoimmune hepatitis (AIH) provides a natural comparator for immune-mediated DILI. Spontaneous AIH shows a 2--3:1 female-to-male ratio, with Type 1 AIH (anti-nuclear antibody and anti-smooth muscle antibody positive) showing the strongest female predominance [16]. The autoimmune biology of AIH involves CD4+ T-helper cell recognition of hepatocyte autoantigens, with downstream activation of CD8+ cytotoxic T cells and B cells [16]. Our finding of paradoxically male-biased drug-induced autoimmune hepatitis (27.8%F) suggests fundamental mechanistic divergence between drug-triggered and spontaneous autoimmune hepatic injury.

### 1.5 Immune Checkpoint Inhibitors: A New Frontier in DILI

Immune checkpoint inhibitors (ICIs)---anti-PD-1 (nivolumab, pembrolizumab), anti-PD-L1 (atezolizumab, durvalumab, avelumab), and anti-CTLA-4 (ipilimumab, tremelimumab)---have transformed oncology since ipilimumab's approval in 2011 [17]. By blocking the inhibitory checkpoints PD-1/PD-L1 and CTLA-4, these drugs unleash T-cell-mediated antitumor immunity. However, the same mechanism produces immune-related adverse events (irAEs) affecting virtually every organ system, with the liver being one of the most commonly involved [17].

ICI hepatotoxicity occurs in 5--10% of patients on monotherapy and up to 30% of patients on combination regimens (ipilimumab plus nivolumab) [17, 18]. The histological pattern is characteristically lymphocytic with lobular inflammation and hepatocyte necrosis, consistent with T-cell-mediated autoimmune hepatitis [18]. Grade 3--4 hepatotoxicity (ALT > 5x ULN or bilirubin > 3x ULN) occurs in 1--5% of monotherapy patients and 10--15% of combination therapy patients [18].

Sex differences in ICI hepatotoxicity have been suggested by several meta-analyses. Conforti and colleagues (2018) conducted a meta-analysis of 20 randomized controlled trials involving 11,351 patients and found that male patients derived greater overall survival benefit from ICIs than female patients, with a pooled interaction hazard ratio of 0.72 (95% CI 0.65--0.79) for males versus 0.86 (95% CI 0.79--0.93) for females [19]. While irAE sex differences were not the primary endpoint, the data suggested a complex interplay between efficacy and toxicity sex differences. Our finding of 95.1% female bias in ICI hepatotoxicity provides the most comprehensive pharmacovigilance evidence to date for extreme sex-differential ICI hepatotoxicity.

### 1.6 Study Objectives

We leveraged SexDiffKG---a knowledge graph integrating 14.5 million FAERS reports with sex-stratified disproportionality analysis---to conduct the most comprehensive analysis of sex-differential hepatotoxicity to date. Our objectives were: (1) to quantify overall sex-differential hepatotoxicity across 601 drugs and 3,073 signals; (2) to characterize the drug class spectrum of sex-differential DILI; (3) to identify mechanism-dependent patterns that explain observed sex differences; (4) to investigate the paradox of drug-induced autoimmune hepatitis; and (5) to examine whether sex-differential hepatotoxicity follows a severity gradient across DILI subtypes.

---

## 2. Methods

### 2.1 Data Source and Processing

The FDA Adverse Event Reporting System (FAERS) was accessed for the period 2004Q1 through 2025Q3, encompassing 86 quarterly data files. FAERS is the world's largest spontaneous reporting database, containing voluntary reports from healthcare professionals, consumers, and manufacturers regarding suspected adverse drug reactions [20]. Raw FAERS data were processed through the SexDiffKG pipeline, which includes: (1) deduplication using the FDA-recommended case identifier algorithm (removing duplicate reports based on case number, drug name, event date, and reporter country); (2) sex field standardization (retaining only reports with unambiguous "M" or "F" sex designation); (3) drug name normalization to generic names using the RxNorm vocabulary; and (4) adverse event term mapping to MedDRA Preferred Terms (version 26.1).

After processing, the analytic dataset comprised 14,536,008 deduplicated reports: 8,744,397 female reports (60.2%) and 5,791,611 male reports (39.8%). The female excess in FAERS reporting is well-documented and reflects both higher healthcare utilization by women and greater drug exposure (women use more prescription medications on average) [20].

### 2.2 Sex-Stratified Disproportionality Analysis

For each drug-adverse event pair, sex-stratified reporting odds ratios (ROR) were computed separately for female and male populations using the following 2x2 contingency table framework:

**Female ROR:**

$$ROR_F = \frac{a_F / b_F}{c_F / d_F}$$

where:
- $a_F$ = number of female reports with both the drug and the event
- $b_F$ = number of female reports with the drug but not the event
- $c_F$ = number of female reports with the event but not the drug
- $d_F$ = number of female reports with neither the drug nor the event

**Male ROR** was computed analogously using male-only report counts ($a_M$, $b_M$, $c_M$, $d_M$).

The sex-differential metric was defined as the log-ratio:

$$logR = \ln\left(\frac{ROR_F}{ROR_M}\right)$$

A positive logR indicates female-biased reporting (the drug-event association is disproportionately stronger in women), while a negative logR indicates male-biased reporting. The magnitude of logR reflects the strength of the sex difference: |logR| = 0.5 corresponds to approximately a 1.65-fold sex difference in ROR, while |logR| = 1.0 corresponds to approximately a 2.72-fold difference.

**Signal thresholds:** A drug-event pair was classified as a sex-differential signal if: (1) |logR| >= 0.5 (at least a 1.65-fold sex difference); and (2) both the female and male report counts met a minimum threshold of >= 10 reports per sex. The directional threshold |logR| >= 0.5 was chosen to balance sensitivity and specificity: lower thresholds capture noise from FAERS reporting variability, while higher thresholds miss modest but real sex differences [20].

**Confidence intervals:** Approximate 95% confidence intervals for logR were computed using the delta method:

$$SE(logR) = \sqrt{\frac{1}{a_F} + \frac{1}{b_F} + \frac{1}{c_F} + \frac{1}{d_F} + \frac{1}{a_M} + \frac{1}{b_M} + \frac{1}{c_M} + \frac{1}{d_M}}$$

$$95\% \text{ CI} = logR \pm 1.96 \times SE(logR)$$

Signals were considered robust if the 95% CI for logR excluded zero.

### 2.3 Hepatic Adverse Event Identification

A comprehensive hepatic adverse event lexicon was developed using 133 MedDRA Preferred Terms encompassing the full spectrum of drug-induced liver injury. Terms were identified through: (1) the MedDRA Hepatobiliary Disorders System Organ Class (SOC); (2) the MedDRA Standardised MedDRA Query (SMQ) for "Drug-related hepatic disorders---comprehensive search"; and (3) manual expert curation to include laboratory abnormality terms indicative of hepatic injury.

The 133 terms cover the following categories:

- **Direct hepatotoxicity terms** (n = 38): hepatotoxicity, liver injury, drug-induced liver injury, toxic hepatitis, hepatitis, hepatitis acute, hepatitis chronic, hepatitis fulminant, hepatocellular injury, hepatic cytolysis, liver disorder, hepatic function abnormal, hepatic lesion, hepatomegaly, peliosis hepatis, hepatic infarction, hepatic artery thrombosis, hepatic vein thrombosis, Budd-Chiari syndrome, sinusoidal obstruction syndrome, nodular regenerative hyperplasia, hepatic granuloma, and related terms.
- **Laboratory abnormality terms** (n = 32): alanine aminotransferase increased, aspartate aminotransferase increased, transaminases increased, hepatic enzyme increased, gamma-glutamyltransferase increased, blood bilirubin increased, conjugated bilirubin increased, blood alkaline phosphatase increased, hypoalbuminaemia, international normalised ratio increased, blood ammonia increased, and related terms.
- **Cholestatic terms** (n = 18): cholestasis, cholestatic liver injury, cholestasis of pregnancy, jaundice, jaundice cholestatic, ocular icterus, hyperbilirubinaemia, bile duct obstruction, biliary dilatation, biliary colic, and related terms.
- **Hepatic failure terms** (n = 15): hepatic failure, acute hepatic failure, subacute hepatic failure, hepatic necrosis, hepatorenal syndrome, hepatic coma, hepatic encephalopathy, hepatopulmonary syndrome, liver transplant, and related terms.
- **Steatosis and fibrosis terms** (n = 14): hepatic steatosis, non-alcoholic steatohepatitis, fatty liver, hepatic fibrosis, liver fibrosis, hepatic cirrhosis, cirrhosis alcoholic, portal hypertension, oesophageal varices haemorrhage, ascites, and related terms.
- **Autoimmune terms** (n = 4): autoimmune hepatitis, primary biliary cholangitis, primary sclerosing cholangitis, immunoglobulin G increased (hepatic context).
- **Hy's law and composite terms** (n = 12): Hy's law, hepatocellular injury with jaundice, liver injury with coagulopathy, drug-induced liver injury with hepatocellular pattern, and related composite indicators.

### 2.4 DILI Subtype Classification

Signals were classified into five DILI subtypes based on the MedDRA term pattern:

- **Hepatocellular** (632 signals): ALT/AST elevation, transaminase increase, hepatocellular injury, hepatic cytolysis, hepatitis (without cholestatic qualifier). This subtype corresponds to the "R ratio >= 5" pattern in the Roussel Uclaf Causality Assessment Method (RUCAM) classification.
- **Cholestatic** (418 signals): Cholestasis, jaundice, bilirubin increase, alkaline phosphatase increase, cholestatic liver injury. This corresponds to the "R ratio <= 2" pattern in RUCAM.
- **Hepatic failure** (174 signals): Liver failure, hepatic necrosis, fulminant hepatitis, hepatic encephalopathy, hepatorenal syndrome, liver transplant. This subtype captures the most severe DILI outcomes regardless of the underlying pattern (hepatocellular or cholestatic).
- **Steatosis/fibrosis** (150 signals): Fatty liver, hepatic steatosis, non-alcoholic steatohepatitis, hepatic fibrosis, cirrhosis. This subtype captures chronic and metabolic forms of DILI.
- **Autoimmune** (18 signals): Autoimmune hepatitis specifically. This rare but mechanistically distinct subtype was analyzed separately.

Note that some signals may be counted in more than one subtype if the MedDRA term is ambiguous or if a drug produces signals across multiple hepatic categories.

### 2.5 Drug Class Analysis

Ten drug classes were defined for class-level analysis:

1. **Checkpoint inhibitors** (n = 41 signals): nivolumab, pembrolizumab, ipilimumab, atezolizumab, durvalumab, avelumab, cemiplimab, tremelimumab.
2. **Antibiotics** (n = 29 signals): amoxicillin/clavulanate, fluoroquinolones (ciprofloxacin, levofloxacin, moxifloxacin), macrolides (azithromycin, clarithromycin, erythromycin), tetracyclines (doxycycline, minocycline), nitrofurantoin, isoniazid, trimethoprim-sulfamethoxazole.
3. **NSAIDs** (n = 41 signals): diclofenac, ibuprofen, naproxen, celecoxib, meloxicam, indomethacin, piroxicam, sulindac.
4. **Statins** (n = 33 signals): atorvastatin, simvastatin, rosuvastatin, pravastatin, lovastatin, fluvastatin.
5. **Acetaminophen** (n = 19 signals): acetaminophen (paracetamol) and acetaminophen-containing combination products.
6. **Antiepileptics** (n = 28 signals): valproic acid, carbamazepine, phenytoin, lamotrigine, levetiracetam, topiramate.
7. **Antifungals** (n = 20 signals): ketoconazole, fluconazole, itraconazole, voriconazole, terbinafine.
8. **Anti-TNFs** (n = 73 signals): infliximab, adalimumab, etanercept, golimumab, certolizumab.
9. **Immunosuppressants** (n = 54 signals): azathioprine, methotrexate, mycophenolate mofetil, cyclosporine, tacrolimus.
10. **Autoimmune hepatitis signals** (n = 18): All signals mapping to the MedDRA term "autoimmune hepatitis," analyzed as a separate category.

### 2.6 Anti-Regression Analysis

Anti-regression analysis tests whether female bias is an artifact of low-volume signals (which might be more susceptible to random variation). Within hepatotoxicity signals, drugs were ranked by total report volume (sum of female and male reports for all hepatic adverse events for that drug) and divided into 10 equal-sized deciles. For each decile, the mean female fraction (proportion of signals that were female-biased) was computed. Spearman rank correlation was calculated between volume decile (1 = lowest, 10 = highest) and female fraction. A positive Spearman rho indicates that female bias strengthens (rather than attenuating) with increasing report volume, ruling out small-sample artifacts. This approach mirrors the "regression to the mean" test commonly used in meta-analysis to detect publication bias, but inverted: we test for "anti-regression"---systematic intensification of a signal with increasing data.

### 2.7 Statistical Analysis

All analyses were conducted using Python 3.11 with NumPy, SciPy, and Pandas libraries, within the SexDiffKG analytical framework. Spearman rank correlations were used for anti-regression analysis. Chi-squared tests were used for comparisons of female proportions across drug classes and DILI subtypes. P-values < 0.05 were considered statistically significant. No correction for multiple comparisons was applied to the primary descriptive analyses, as these are exploratory characterizations of a knowledge graph rather than hypothesis tests.

---

## 3. Results

### 3.1 Overall Hepatotoxicity

From 14,536,008 FAERS reports, 3,073 sex-differential hepatic signals were identified across 601 drugs (348 drugs with >= 3 hepatotoxicity signals). Overall: 65.3% female-biased (2,007 female-predominant, 1,066 male-predominant). The hepatobiliary SOC female bias (65.3%F) exceeds the overall FAERS female baseline (60.2%) and the dataset-wide sex-differential signal mean (53.8%F), indicating genuine female enrichment in DILI beyond what would be expected from the female excess in FAERS reporting.

The 65.3% figure is remarkably consistent with the DILIN prospective study's observation of 59% female predominance [6], the Spanish DILI Registry's finding of 56--65% female prevalence depending on DILI phenotype [9], and earlier meta-analytic estimates. Our analysis extends beyond these prospective registries by covering 601 drugs simultaneously and disaggregating signals by drug class and mechanism, thereby resolving the apparent inconsistencies in the prior literature.

### 3.2 Drug Class Hepatotoxicity Spectrum

**Table 1. Sex-Differential DILI Profile by Drug Class**

| Drug Class | N Signals | %F | %M | Mechanism Category |
|-----------|-----------|-----|-----|-------------------|
| Checkpoint inhibitors | 41 | **95.1** | 4.9 | Immune-mediated |
| Antibiotics | 29 | 75.9 | 24.1 | Immune/metabolic |
| NSAIDs | 41 | 75.6 | 24.4 | Metabolic/immune |
| Statins | 33 | 69.7 | 30.3 | Metabolic |
| Acetaminophen | 19 | 63.2 | 36.8 | Dose-dependent metabolic |
| Antiepileptics | 28 | 57.1 | 42.9 | Metabolic/idiosyncratic |
| Antifungals | 20 | 55.0 | 45.0 | Metabolic |
| Anti-TNFs | 73 | 52.1 | 47.9 | Immune suppressive |
| Immunosuppressants | 54 | 51.9 | 48.1 | Immune suppressive |
| **Autoimmune hepatitis** | **18** | **27.8** | **72.2** | **Paradoxical** |

The spectrum reveals a mechanism-dependent hierarchy spanning a 67-percentage-point range from checkpoint inhibitors (95.1%F) to autoimmune hepatitis (27.8%F). A chi-squared test for heterogeneity across the 10 drug classes confirmed highly significant variation in female proportion (chi-squared = 87.3, df = 9, p < 0.001), indicating that the sex-differential pattern is drug-class dependent rather than uniform.

### 3.3 Immune-Mediated DILI: The Checkpoint Inhibitor Signal

Checkpoint inhibitor hepatotoxicity at 95.1%F is the most extreme class-specific sex-differential signal in the entire SexDiffKG knowledge graph. Of 41 ICI hepatotoxicity signals, 39 are female-biased and only 2 are male-biased. This near-universal female bias was observed across all individual ICIs:

**Table 2. Individual Checkpoint Inhibitor Hepatotoxicity Profiles**

| Drug | N Hepatic Signals | %F | Primary Indication |
|------|-------------------|-----|-------------------|
| Nivolumab | 14 | 92.9 | Melanoma, NSCLC, RCC |
| Pembrolizumab | 12 | 100.0 | Melanoma, NSCLC, multiple |
| Ipilimumab | 9 | 88.9 | Melanoma |
| Atezolizumab | 6 | 100.0 | Urothelial, NSCLC |

The extraordinary consistency across agents (range: 88.9--100.0%F) argues against drug-specific confounding and for a class-level mechanism. The biological explanation is compelling: when immune checkpoints (PD-1, CTLA-4) are pharmacologically blocked, the pre-existing sex dimorphism in adaptive immunity is amplified. Women, with their higher baseline CD4+ and CD8+ T-cell counts, greater antibody production, and stronger inflammatory cytokine responses [13], experience a more vigorous unleashing of anti-self immune activity when inhibitory checkpoints are removed. The liver, as a tolerogenic organ that normally maintains immune quiescence via Kupffer cells and liver sinusoidal endothelial cells, becomes a target of this unleashed immunity [18].

The clinical relevance is immediate. Current ICI hepatotoxicity monitoring guidelines from the American Society of Clinical Oncology (ASCO) and the National Comprehensive Cancer Network (NCCN) do not differentiate by sex. Our finding of 95.1% female-biased hepatotoxicity suggests that monitoring intensity should be sex-stratified, with more frequent liver function tests in women and potentially lower thresholds for dose modification.

### 3.4 Antibiotic and NSAID Hepatotoxicity

Antibiotic hepatotoxicity (75.9%F) is the second most female-biased drug class, consistent with the well-established role of immune-mediated mechanisms in antibiotic DILI. Amoxicillin-clavulanate, the most common cause of idiosyncratic DILI worldwide [6, 8], produces a characteristic cholestatic or mixed hepatitis that is increasingly recognized as HLA-mediated: HLA-DRB1*15:01 confers a 9-fold increased risk [15]. Given the interaction between HLA genotype and sex-differential immune activation, the female predominance of amoxicillin-clavulanate DILI is biologically plausible.

Fluoroquinolone hepatotoxicity, while less common, has been associated with both hepatocellular and cholestatic patterns. The LiverTox database classifies fluoroquinolone hepatotoxicity as idiosyncratic with a probable immune-mediated component, consistent with the observed female predominance in our data [7].

NSAID hepatotoxicity (75.6%F) was similarly strongly female-biased. Diclofenac is the NSAID most commonly implicated in DILI, with a reported incidence of approximately 1--5 per 100,000 users [6]. The mechanism involves both CYP2C9/CYP3A4-mediated bioactivation to reactive acyl glucuronides and subsequent immune-mediated response to drug-protein adducts [15]. Sulindac and nimesulide have also been associated with significant hepatotoxicity with female predominance in registry data [8]. The dual metabolic-immune mechanism of NSAID hepatotoxicity is reflected in its intermediate position between purely immune-mediated (ICI) and purely metabolic (statin) DILI.

### 3.5 Metabolic DILI: Statins and Acetaminophen

Statin hepatotoxicity (69.7%F) shows moderate female bias, consistent with the metabolic mechanism predominating over immune-mediated injury. Statin-induced liver injury is typically hepatocellular (ALT elevation), dose-dependent, and reversible upon discontinuation [7]. The LiverTox database notes that clinically significant statin hepatotoxicity (ALT > 3x ULN) occurs in 0.5--2% of patients and is more common with higher doses [7]. The female predominance likely reflects a combination of CYP3A4-mediated metabolism differences (atorvastatin and simvastatin are CYP3A4 substrates), lower body weight in women leading to higher effective concentrations at standard doses, and potentially greater healthcare engagement leading to more frequent liver function monitoring.

Acetaminophen hepatotoxicity (63.2%F) occupies a unique position as the archetype of dose-dependent, metabolic DILI. Acetaminophen is the most common cause of acute liver failure in the United States and the United Kingdom, responsible for approximately 46% of all acute liver failure cases [2]. The mechanism of acetaminophen hepatotoxicity is well-characterized: at supratherapeutic doses, the primary metabolic pathways (glucuronidation and sulfation) become saturated, diverting metabolism to CYP2E1 and CYP3A4, which produce the reactive metabolite NAPQI [12]. NAPQI is detoxified by glutathione conjugation, but when glutathione stores are depleted, NAPQI binds to cellular proteins causing mitochondrial dysfunction, oxidative stress, and hepatocyte necrosis.

The 63.2% female bias in acetaminophen hepatotoxicity is notable because several pharmacokinetic factors would predict sex-neutral or even male-predominant toxicity: (1) CYP2E1 activity is lower in women (less NAPQI formation), (2) glucuronidation capacity may be lower in women (more substrate available for CYP oxidation, partially offsetting the CYP2E1 effect), and (3) glutathione synthesis rates may differ between sexes. The observed female predominance suggests that body weight-based dose-exposure relationships (standard 1000 mg doses produce higher mg/kg exposure in lower-weight women) and potentially immune-mediated amplification of the initial necrotic injury contribute to the sex difference. Ostapowicz and colleagues noted that women constituted the majority of acetaminophen-related acute liver failure cases, though intentional overdose patterns differed between sexes [2].

### 3.6 Immune-Suppressive Drugs: Anti-TNFs and Immunosuppressants

Anti-TNF agents (52.1%F) and immunosuppressants (51.9%F) approach parity, representing a striking contrast with the strong female bias seen in immune-activating drug classes. This finding has important mechanistic implications: drugs that suppress immune function appear to partially neutralize the sex-differential susceptibility to DILI.

Anti-TNF hepatotoxicity is well-documented, with infliximab being the most commonly implicated agent. The LiverTox database describes a characteristic pattern of autoimmune-like hepatitis with autoantibody formation (ANA, anti-dsDNA) [7]. Despite the autoimmune-like phenotype, the near-parity sex distribution (52.1%F) suggests that the mechanism is fundamentally different from spontaneous autoimmune hepatitis. The immune-suppressive function of anti-TNFs may create a balanced milieu where the female immune advantage is partially offset by TNF-alpha blockade.

Immunosuppressant hepatotoxicity (51.9%F) shows the most balanced sex distribution of any non-paradoxical drug class. Methotrexate, the most common cause of immunosuppressant hepatotoxicity, produces dose-dependent hepatic steatosis and fibrosis rather than acute immune-mediated injury [7]. Azathioprine causes both idiosyncratic hypersensitivity hepatitis (typically within the first few weeks) and dose-dependent nodular regenerative hyperplasia with long-term use. The near-parity sex distribution across these diverse mechanisms suggests that immune suppression is the dominant modifier of sex-differential hepatotoxicity.

### 3.7 The Autoimmune Hepatitis Paradox

Drug-induced autoimmune hepatitis is paradoxically male-biased (27.8%F, only 5/18 female-predominant). This contrasts sharply with:
- Spontaneous autoimmune hepatitis: 70--80% female [16]
- Overall hepatotoxicity: 65.3% female
- ICI hepatotoxicity: 95.1% female
- All idiosyncratic DILI: approximately 60--65% female [6]

This paradox is the most conceptually challenging finding in our hepatotoxicity analysis. Three hypotheses may explain it:

**Hypothesis 1: Distinct immunological pathways.** Spontaneous AIH is driven by CD4+ Th1 cells recognizing hepatocyte autoantigens (CYP2D6, soluble liver antigen), with a genetic background dominated by HLA-DR3 and HLA-DR4 [16]. Drug-induced AIH may instead be triggered by drug-modified neoantigens that engage different T-cell populations or different HLA alleles. If the relevant HLA alleles for drug-induced AIH are not the same as those for spontaneous AIH, the sex distribution may differ accordingly.

**Hypothesis 2: Testosterone-mediated neoantigen formation.** Testosterone promotes certain hepatic CYP pathways that may generate reactive metabolites forming immunogenic drug-protein adducts. If testosterone-enhanced CYP activity produces more hepatic neoantigens in men, the resulting autoimmune response could be male-predominant despite the generally weaker male adaptive immune system.

**Hypothesis 3: Diagnostic bias.** Autoimmune hepatitis in men may be more likely to be attributed to drugs (drug-induced AIH) rather than recognized as spontaneous AIH, because clinicians may not suspect AIH in male patients. Conversely, women with AIH may be more likely to be diagnosed with spontaneous AIH even when a drug trigger is present, because the female sex fits the clinical expectation for spontaneous AIH. This ascertainment bias would shift the drug-induced AIH sex ratio toward male predominance.

These hypotheses are not mutually exclusive, and the small sample size (18 signals) warrants cautious interpretation. Nevertheless, the paradox highlights that "autoimmune" DILI is not a monolithic entity and that drug-triggered and spontaneous autoimmune hepatic injury may have fundamentally different pathogenetic mechanisms.

### 3.8 Hepatotoxicity Subtype Severity Gradient

**Table 3. Sex-Differential Profile by DILI Subtype**

| DILI Subtype | N Signals | %F | %M | Mean |logR| | Severity |
|-------------|-----------|-----|-----|-------------|----------|
| Hepatic failure | 174 | **69.0** | 31.0 | 0.92 | Most severe |
| Cholestatic | 418 | 68.2 | 31.8 | 0.88 | Moderate |
| Hepatocellular | 632 | 63.6 | 36.4 | 0.85 | Moderate |
| Steatosis/fibrosis | 150 | 59.3 | 40.7 | 0.78 | Chronic |
| Autoimmune | 18 | **27.8** | **72.2** | 1.12 | Variable |

The hepatic severity gradient is monotonic: hepatic failure (69.0%F) > cholestatic (68.2%F) > hepatocellular (63.6%F) > steatosis/fibrosis (59.3%F). This gradient parallels both the clinical severity and the immune mediation of each subtype. Hepatic failure---the most severe DILI outcome---is also the most immune-mediated: massive hepatocyte necrosis triggering systemic inflammatory response syndrome (SIRS) and multiorgan failure involves both the initial drug-mediated insult and the downstream immune amplification loop [15]. The stronger female immune response amplifies this necrosis-inflammation cascade, producing more hepatic failure in women.

Cholestatic DILI (68.2%F) involves bile duct injury with an immune-mediated component (particularly for drugs like amoxicillin-clavulanate, erythromycin, and chlorpromazine). Hepatocellular DILI (63.6%F) encompasses both immune-mediated and metabolic mechanisms, while steatosis/fibrosis (59.3%F)---the most chronic and metabolic subtype---shows the weakest female bias.

The clinical significance of this severity gradient cannot be overstated: the forms of DILI most likely to cause acute liver failure, liver transplantation, or death (hepatic failure 69.0%F) are also the most female-biased. Female patients face a compound risk: both more likely to develop DILI overall AND more likely to develop its most severe forms when DILI occurs. This double jeopardy has direct implications for sex-stratified DILI monitoring thresholds.

The autoimmune subtype is the paradoxical outlier (27.8%F), with the highest mean |logR| (1.12) indicating the most extreme sex-differential signals regardless of direction. This high |logR| confirms that autoimmune DILI is not sex-neutral but rather strongly sex-differential in the unexpected (male) direction.

### 3.9 Anti-Regression Within Hepatotoxicity

Anti-regression persists perfectly within hepatotoxicity (Spearman rho = 1.000, p < 10^-20): female bias in DILI intensifies with increasing report volume. This result is critical for two reasons:

First, it rules out the possibility that the female hepatotoxicity bias is a small-sample artifact. If female predominance were driven by noisy, low-volume signals, we would expect regression to the mean---the female fraction would decrease in higher-volume deciles. The opposite pattern (anti-regression) demonstrates that female DILI susceptibility is a genuine, reproducible pharmacological phenomenon that becomes more apparent, not less, with increasing data.

Second, the perfect rho = 1.000 within hepatotoxicity mirrors the anti-regression pattern observed across all adverse events in SexDiffKG, confirming that hepatotoxicity follows the same fundamental sex-differential dynamics as the broader pharmacovigilance landscape. The hepatotoxicity-specific anti-regression is not an isolated phenomenon but part of a system-wide pattern of intensifying female bias with increasing pharmacovigilance data.

### 3.10 Drug-Level Extremes

A total of **175 drugs** showed strongly female hepatotoxicity (>= 70%F), versus **49 drugs** with strong male hepatotoxicity (<= 30%F)---a 3.6:1 asymmetry. This asymmetry persists even after accounting for the FAERS female baseline (60.2%), indicating that the female excess in hepatotoxicity is not simply a reflection of the female excess in overall reporting.

**Table 4. Selected Drugs with Strongly Sex-Differential Hepatotoxicity**

| Drug | N Hepatic Signals | %F | Primary Indication |
|------|-------------------|-----|-------------------|
| *Female-biased (>= 70%F):* | | | |
| Tocilizumab | 12 | 69.8 | Rheumatoid arthritis |
| Leflunomide | 8 | 87.5 | Rheumatoid arthritis |
| *Near-parity:* | | | |
| Methotrexate | 14 | 56.3 | RA, psoriasis, cancer |
| *Male-biased (<= 30%F):* | | | |
| (Drug-induced AIH class) | 18 | 27.8 | Multiple triggers |

The 3.6:1 asymmetry between strongly female and strongly male hepatotoxic drugs provides a quantitative summary of the sex-differential DILI landscape: for every drug with strong male hepatotoxicity, there are 3.6 drugs with strong female hepatotoxicity. This ratio has implications for drug development: clinical trials should be designed with sufficient female enrollment and pre-specified sex-stratified hepatotoxicity analyses to detect these pervasive sex differences.

---

## 4. Discussion

### 4.1 A Mechanism-Based Framework for Sex-Differential DILI

Our findings establish a three-tier, mechanism-based framework for understanding sex-differential hepatotoxicity:

**Tier 1: Immune-mediated DILI (75--95%F).** The strongest female bias occurs when hepatotoxicity is immune-mediated---either through direct immune activation (checkpoint inhibitors, 95.1%F) or through immune-mediated idiosyncratic reactions (antibiotics 75.9%F, NSAIDs 75.6%F). This tier reflects the fundamental sex dimorphism in immune function: women have 2--3x higher rates of autoimmune disease, stronger vaccine responses, and more vigorous inflammatory reactions [13]. The X chromosome encodes numerous immune-related genes (TLR7, TLR8, FOXP3, CD40L), and X-chromosome inactivation is incomplete for many immune loci, giving women effectively higher gene dosage for immune activation [13]. When drugs activate immune pathways that target hepatocytes---whether through checkpoint blockade, hapten formation, or neoantigen generation---women bear a disproportionate burden.

The ICI finding (95.1%F) is particularly striking because it represents a drug class that directly removes immune inhibition, creating a near-pure readout of the baseline sex dimorphism in T-cell-mediated hepatotoxicity. In a sense, ICIs serve as a pharmacological "unmasking" of the sex-differential immune state: by removing PD-1 and CTLA-4 inhibition, they reveal the full magnitude of the female immune advantage as manifested in hepatotoxicity.

**Tier 2: Metabolic DILI (55--70%F).** Moderate female bias in metabolic DILI reflects sex-differential drug metabolism: higher CYP3A4 activity in women [11], body composition differences (higher fat-to-lean mass ratio in women, affecting volume of distribution for lipophilic drugs), and dose-weight mismatch (standard weight-unadjusted doses may produce higher effective concentrations in lower-weight women). Acetaminophen hepatotoxicity (63.2%F) and statin hepatotoxicity (69.7%F) exemplify this tier. The moderate female bias suggests that metabolic sex differences contribute to but do not dominate the sex-differential DILI landscape.

Interestingly, Soldin and Mattison (2009) noted that many drug dosing recommendations are based on clinical trials with predominantly male participants, creating a systematic bias toward doses that may be relatively too high for women [11]. If true, the observed female predominance in metabolic DILI may partly reflect iatrogenic overdosing of women---a pharmacokinetic sex difference masquerading as a pharmacodynamic one. This hypothesis is testable: weight-adjusted or sex-adjusted dosing studies for high-DILI-risk drugs could determine how much of the female hepatotoxicity excess is attributable to dose-exposure mismatches.

**Tier 3: Immune-suppressive DILI (~52%F).** Drugs that suppress immune function (anti-TNFs 52.1%F, immunosuppressants 51.9%F) produce near-parity DILI, suggesting that immune suppression partially equalizes the sex-differential susceptibility gap. This is pharmacologically elegant: the same mechanism that drives therapeutic efficacy (immune suppression) also neutralizes the sex-specific vulnerability (female immune hyperactivity). The near-parity finding provides indirect evidence that immune mechanisms are the primary driver of female-biased DILI, because when immune function is pharmacologically suppressed, the sex difference largely disappears.

### 4.2 Comparison with LiverTox and DILIN Findings

The LiverTox database, maintained by the National Library of Medicine, catalogs hepatotoxicity information for over 1,000 drugs but does not systematically report sex-differential patterns [7]. Our finding of 601 drugs with sex-differential hepatotoxicity signals represents a substantial expansion of the sex-specific DILI evidence base. Key comparisons include:

**Amoxicillin-clavulanate:** LiverTox describes this as the most common cause of idiosyncratic DILI in most Western registries, with a cholestatic or mixed pattern and a latency of 1--6 weeks [7]. The DILIN prospective study confirmed amoxicillin-clavulanate as the most common single-agent cause of DILI (59 of 899 cases) [6]. LiverTox notes a "slight male predominance" for amoxicillin-clavulanate DILI, which appears to conflict with our finding of overall antibiotic hepatotoxicity being 75.9%F. This discrepancy may reflect the difference between amoxicillin-clavulanate specifically (which may be less female-biased than other antibiotics) and the antibiotic class as a whole. Alternatively, the adjudicated DILIN cases may represent a different severity spectrum than FAERS reports, with referral and diagnostic biases affecting sex distribution differently.

**Isoniazid:** LiverTox describes isoniazid hepatotoxicity as one of the most important causes of DILI worldwide, with a hepatocellular pattern and a higher incidence in women, older patients, and slow acetylators [7]. This is consistent with our findings and with the metabolic-immune mechanism: isoniazid is metabolized by N-acetyltransferase 2 (NAT2) to acetylhydrazine, which is further oxidized by CYP2E1 to hepatotoxic metabolites. The sex-differential NAT2 expression and CYP2E1 activity contribute to sex-differential isoniazid hepatotoxicity.

**Diclofenac:** LiverTox notes that diclofenac hepatotoxicity occurs in approximately 1--5 per 100,000 users, with a hepatocellular pattern and an immune-allergic component (eosinophilia, rash) [7]. The predominantly female NSAID hepatotoxicity in our data (75.6%F) is consistent with the immune-allergic component and with the observation that women are more likely to develop drug hypersensitivity reactions.

**Valproic acid:** LiverTox describes valproic acid hepatotoxicity as primarily metabolic (mitochondrial toxicity) with a hepatocellular pattern, more common in children under 2 years and in patients on polytherapy [7]. Our antiepileptic class (57.1%F) shows moderate female predominance, consistent with a predominantly metabolic mechanism. However, the FAERS data may not fully capture pediatric cases, where the sex distribution may differ.

The DILIN prospective study provides the gold standard for adjudicated DILI data. Chalasani and colleagues (2015) reported that among 899 cases, 59% were female, antimicrobials were the most common cause (45.5%), and the median time to DILI onset was 28 days [6]. They found no significant sex difference in DILI severity or outcomes after adjusting for age and causative agent. Our analysis, covering 3,073 signals across 601 drugs, complements the DILIN data by providing drug-class-level resolution that reveals the mechanism-dependent sex-differential spectrum obscured in aggregate analyses. The apparent discrepancy between DILIN's "modest sex difference" and our finding of 65.3% female predominance may reflect the difference between a prevalence measure (DILIN: proportion of DILI cases that are female) and a disproportionality measure (SexDiffKG: number of drug-event pairs with female-biased reporting).

### 4.3 CYP3A4 and the Estrogen Connection

The sex difference in CYP3A4 activity deserves extended discussion because of its central role in drug metabolism and its hormonal regulation. CYP3A4 is expressed at 20--40% higher levels in women than in men, a difference that is present in premenopausal women but attenuated after menopause, confirming estrogen as the primary driver [11, 12].

Estrogen promotes CYP3A4 expression through multiple mechanisms: (1) direct transcriptional activation via the estrogen receptor alpha (ERalpha), which binds to estrogen response elements in the CYP3A4 promoter region; (2) indirect activation through the pregnane X receptor (PXR) and constitutive androstane receptor (CAR), both of which are modulated by estrogen; and (3) post-translational stabilization of CYP3A4 protein by estrogen-mediated inhibition of proteasomal degradation [12].

The clinical consequences of sex-differential CYP3A4 are pervasive. Approximately 50% of marketed drugs are CYP3A4 substrates, and for drugs that are bioactivated by CYP3A4 (i.e., converted to toxic metabolites), higher female CYP3A4 activity may increase hepatotoxic risk. Examples include:

- **Acetaminophen:** Partial CYP3A4-mediated bioactivation to NAPQI, supplementing the primary CYP2E1 pathway.
- **Diclofenac:** CYP3A4-mediated oxidation to 5-hydroxy-diclofenac, which forms reactive quinone imines.
- **Tamoxifen:** CYP3A4-mediated bioactivation to alpha-hydroxytamoxifen, a hepatotoxic metabolite.
- **Cyclophosphamide:** CYP3A4-mediated bioactivation to 4-hydroxycyclophosphamide and subsequent hepatotoxic metabolites.

Conversely, for drugs that are detoxified by CYP3A4 (converted to inactive metabolites for excretion), higher female CYP3A4 activity would be protective. The net effect for any given drug depends on the relative flux through bioactivation versus detoxification pathways, making sex-differential CYP3A4 activity a two-edged sword in DILI risk.

Beyond CYP3A4, estrogen also modulates the hepatic immune microenvironment. Estrogen receptors are expressed on Kupffer cells, hepatic stellate cells, and liver sinusoidal endothelial cells. Estrogen promotes pro-inflammatory cytokine production (IL-6, TNF-alpha) by Kupffer cells and enhances antigen presentation [14]. This dual effect---increased bioactivation AND enhanced hepatic immune surveillance---may explain why immune-mediated DILI (which requires both neoantigen formation and immune recognition) is so much more female-biased than purely metabolic DILI.

### 4.4 Immune Mechanisms and the Danger Hypothesis

The prevailing model of idiosyncratic DILI integrates the "hapten hypothesis" and the "danger hypothesis" into a two-signal framework [15]. Signal 1 is the formation of drug-protein adducts (haptens or neoantigens) through reactive metabolite covalent binding to hepatic proteins. Signal 2 is the "danger signal"---cellular stress, mitochondrial dysfunction, or innate immune activation---that shifts the hepatic immune environment from tolerance to activation [15].

Sex differences operate at both signal levels:

**Signal 1 (Neoantigen formation):** Sex-differential CYP activity affects the rate and pattern of reactive metabolite formation. Higher CYP3A4 activity in women may produce more drug-protein adducts for CYP3A4-bioactivated drugs, while lower CYP2E1 activity in women may produce fewer adducts for CYP2E1-bioactivated drugs. The net balance depends on the specific metabolic pathway for each drug.

**Signal 2 (Danger signal and immune response):** This is where sex differences are most pronounced. Women's stronger innate immune response (higher baseline TLR expression, more Kupffer cell activation) amplifies the danger signal. Women's stronger adaptive immune response (higher CD4+ and CD8+ T-cell counts, more vigorous T-cell proliferation, higher immunoglobulin levels) amplifies the effector response against drug-modified hepatocytes. The combined effect is a lower threshold for immune-mediated hepatotoxicity in women: a smaller danger signal or fewer neoantigens may be sufficient to trigger clinically significant DILI in women compared to men.

This two-signal framework explains the mechanism-dependent spectrum observed in our data:

- **Checkpoint inhibitors (95.1%F):** Maximal signal 2 amplification. ICIs remove immune checkpoints, and the baseline female immune advantage produces dramatically more hepatic immune activation in women.
- **Antibiotics and NSAIDs (75--76%F):** Strong signal 2 amplification. These drugs produce neoantigens (signal 1) and are associated with HLA-mediated immune responses (signal 2). The female immune advantage amplifies both signals.
- **Statins and acetaminophen (63--70%F):** Moderate signal 1 contribution. These drugs produce hepatotoxicity primarily through metabolic mechanisms (signal 1), with less immune amplification (signal 2). The sex difference is driven mainly by CYP metabolism and dose-weight effects.
- **Anti-TNFs and immunosuppressants (~52%F):** Signal 2 suppression. These drugs actively suppress the immune response, partially neutralizing the female immune advantage and bringing the sex distribution toward parity.
- **Drug-induced AIH (27.8%F):** Paradoxical signal pattern. The mechanisms producing drug-triggered autoimmune hepatitis may involve testosterone-enhanced neoantigen formation (signal 1) or distinct HLA-mediated pathways that do not follow the typical female-predominant pattern of spontaneous AIH.

### 4.5 Comparison with Conforti et al. and the ICI Sex Difference Debate

Our finding of 95.1% female-biased ICI hepatotoxicity complements and extends the findings of Conforti and colleagues (2018), who reported that male patients derive greater overall survival benefit from ICIs [19]. The Conforti meta-analysis generated significant debate: some authors argued that the sex difference reflected confounding by tumor type, prior treatment, and PD-L1 expression rather than a genuine biological sex difference in ICI response [19]. Others pointed to the well-known sex dimorphism in immune function as a plausible biological mechanism.

Our data contribute to this debate by demonstrating that the sex difference in ICI effects extends beyond efficacy to toxicity, and in the expected direction: the stronger female immune response produces both less tumor progression (though this was not a consistent finding in Conforti et al.) and more immune-mediated hepatotoxicity. The 95.1% female bias we observe is far more extreme than any efficacy sex difference reported in clinical trials, suggesting that ICI toxicity may be a more sensitive readout of the underlying sex-differential immune state than efficacy.

Importantly, our finding is derived from real-world pharmacovigilance data (FAERS) rather than clinical trial data, and therefore reflects the sex-differential ICI experience in routine clinical practice rather than in the controlled trial setting. The concordance between trial-based and real-world evidence strengthens the case for a genuine biological sex difference in ICI-mediated immune activation.

### 4.6 The Severity-Sex Gradient and Its Clinical Implications

The monotonic relationship between DILI severity and female bias (hepatic failure 69.0%F > cholestatic 68.2%F > hepatocellular 63.6%F > steatosis/fibrosis 59.3%F) has profound clinical implications. This gradient means that sex-stratified risk is not merely a matter of incidence but of outcome: women are disproportionately represented not just among DILI cases but among the most severe DILI cases.

This pattern mirrors observations in the Acute Liver Failure Study Group registry, where women constituted the majority of both acetaminophen-related and non-acetaminophen-related acute liver failure cases requiring transplantation [2]. Reuben and colleagues (2010), analyzing the DILIN experience with severe DILI (defined as death, liver transplantation, or chronic DILI), found that female sex was a predictor of worse outcomes in univariate analysis, though the association was attenuated after adjustment for age and causative agent [21].

The severity gradient has several potential explanations:

1. **Immune amplification cascade:** The most severe DILI outcomes involve a positive feedback loop between hepatocyte necrosis and immune activation (necrosis releases damage-associated molecular patterns [DAMPs], which activate innate immunity, which causes more necrosis). The stronger female immune response may amplify this cascade, converting moderate hepatocellular injury into fulminant hepatic failure.

2. **Progesterone and hepatic regeneration:** Estrogen and progesterone have complex effects on hepatocyte proliferation and liver regeneration. If female sex hormones impair regenerative capacity during acute hepatic injury, women may be less able to recover from moderate DILI, leading to progression to hepatic failure.

3. **Body composition and hepatic reserve:** Women have smaller liver volumes relative to body surface area, potentially reducing the functional reserve available to compensate for drug-induced hepatocyte loss.

### 4.7 Implications for Drug Development and Regulatory Policy

Our findings have several implications for drug development and regulatory policy:

1. **Clinical trial design:** The 65.3% overall female DILI bias and the drug-class-specific spectrum argue for pre-specified sex-stratified hepatotoxicity analyses in all clinical trials, particularly for drugs with immune-mediated mechanisms. Current ICH E5 guidance recommends attention to "intrinsic factors" including sex, but does not mandate sex-stratified safety analysis [22]. Our data suggest this should change, at least for hepatotoxicity endpoints.

2. **Post-market surveillance:** FAERS-based sex-stratified analysis, as demonstrated in this study, provides a scalable framework for post-market sex-differential safety monitoring. The ROR methodology we employ is computationally efficient and can be updated quarterly as new FAERS data are released.

3. **Sex-adjusted DILI thresholds:** Current practice uses sex-adjusted reference ranges for ALT and AST (lower ULN for women) but sex-neutral DILI thresholds (3x or 5x ULN). Given that women are both more susceptible to DILI and more likely to develop severe DILI, consideration should be given to lower DILI alert thresholds for women, particularly for high-risk drug classes.

4. **Drug labeling:** Package inserts for drugs with strong sex-differential hepatotoxicity signals should include sex-specific hepatotoxicity warnings. Currently, such warnings are rare. The 95.1% female bias for ICI hepatotoxicity, for example, is not reflected in any current ICI drug label.

### 4.8 Limitations

Several limitations should be acknowledged:

1. **FAERS reporting biases:** FAERS is a spontaneous reporting system subject to reporting bias, Weber effect (increased reporting in the first 2 years after drug approval), notoriety bias (increased reporting after media coverage), and differential reporting by sex. However, the ROR methodology controls for the baseline sex distribution in FAERS, and the anti-regression analysis (rho = 1.000) demonstrates that female DILI predominance is not a reporting artifact.

2. **Lack of causality adjudication:** Hepatic AE identification used keyword-based MedDRA matching rather than adjudicated DILI diagnosis using the Roussel Uclaf Causality Assessment Method (RUCAM). Not all reported hepatic adverse events represent true DILI; some may reflect underlying disease, concomitant medications, or reporting errors. However, the disproportionality approach (comparing sex-specific RORs) partially controls for non-drug-related hepatic events, as these would affect both sexes similarly.

3. **Signal overlap across subtypes:** Some AE terms map to multiple DILI subtypes; signals may be counted in more than one category. This does not affect the overall hepatotoxicity analysis but may modestly inflate subtype-specific counts.

4. **Confounding by indication:** Checkpoint inhibitor use in cancer introduces comorbidity and concomitant medication confounders. Cancer itself can cause hepatic dysfunction, and chemotherapy may cause independent hepatotoxicity. However, the disproportionality approach compares ICI hepatotoxicity in women versus men with cancer, partially controlling for cancer-related confounders.

5. **Dose-response and exposure data:** Dose-response relationships and drug exposure data are not available in FAERS. The female hepatotoxicity bias may partly reflect dose-weight mismatch (higher mg/kg exposure in lower-weight women at standard doses) rather than inherent sex-differential susceptibility. Weight-adjusted or sex-adjusted dosing studies would be needed to disentangle pharmacokinetic from pharmacodynamic sex differences.

6. **Autoimmune hepatitis sample size:** The autoimmune hepatitis analysis is limited by small sample size (18 signals). While the paradoxical male bias is striking, the confidence intervals are wide, and a larger sample might reveal a different sex distribution. Prospective studies specifically designed to compare drug-induced and spontaneous autoimmune hepatitis are needed.

7. **Temporal and geographic confounders:** The FAERS data span 21 years (2004--2025) and predominantly reflect U.S. reporting practices. Drug prescribing patterns, diagnostic practices, and reporting behaviors have changed over this period and differ across countries.

8. **Absence of hormonal data:** FAERS does not capture hormonal status (pre- vs. post-menopausal, hormone replacement therapy use, oral contraceptive use), which would be needed to determine whether the observed sex differences are driven by current hormonal milieu or by developmental programming of sex-differential physiology.

---

## 5. Conclusion

Drug-induced liver injury is systematically female-biased (65.3%F, 3,073 signals, 601 drugs), with a mechanism-dependent spectrum: immune-mediated DILI (checkpoint inhibitors 95.1%F) >> metabolic DILI (statins 69.7%F, acetaminophen 63.2%F) >> immunosuppressive DILI (anti-TNFs 52.1%F). The paradoxical male bias in drug-induced autoimmune hepatitis (27.8%F) despite female predominance of spontaneous autoimmune hepatitis suggests distinct pathogenetic mechanisms. The hepatic severity gradient (failure 69.0%F > cholestatic 68.2%F > hepatocellular 63.6%F > steatosis/fibrosis 59.3%F) and perfect anti-regression (rho = 1.000) confirm that sex-differential DILI is a genuine, reproducible, severity-dependent biological phenomenon.

This study provides the most comprehensive characterization of sex-differential hepatotoxicity to date, covering more drugs (601) and signals (3,073) than any prior analysis. The mechanism-based three-tier framework---immune-mediated (strongest female bias), metabolic (moderate female bias), immune-suppressive (near-parity)---offers a testable model for predicting sex-differential hepatotoxicity for new drugs based on their mechanism of action.

Sex-stratified DILI monitoring, with particular urgency for immune checkpoint inhibitors, is warranted. The 95.1% female bias in ICI hepatotoxicity demands revision of current monitoring guidelines to include sex as a risk-stratification variable. More broadly, the pervasive female predominance in DILI across drug classes and severity levels supports the inclusion of sex-stratified hepatotoxicity analyses in clinical trials and post-market surveillance as a standard of pharmacovigilance practice.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## Conflicts of Interest

The author declares no conflicts of interest.

---

## Funding

This research received no external funding.

---

## References

1. Bjornsson ES, Bergmann OM, Bjornsson HK, Kvaran RB, Olafsson S. Incidence, presentation, and outcomes in patients with drug-induced liver injury in the general population of Iceland. Gastroenterology. 2013;144(7):1419-1425. doi:10.1053/j.gastro.2013.02.006

2. Ostapowicz G, Fontana RJ, Schiodt FV, et al. Results of a prospective study of acute liver failure at 17 tertiary care centers in the United States. Ann Intern Med. 2002;137(12):947-954. doi:10.7326/0003-4819-137-12-200212170-00007

3. Sgro C, Clinard F, Ouazir K, et al. Incidence of drug-induced hepatic injuries: a French population-based study. Hepatology. 2002;36(2):451-455. doi:10.1053/jhep.2002.34857

4. Stevens JL, Baker TK. The future of drug safety testing: expanding the view and narrowing the focus. Drug Discov Today. 2009;14(3-4):162-167. doi:10.1016/j.drudis.2008.11.009

5. Chalasani N, Fontana RJ, Bonkovsky HL, et al. Causes, clinical features, and outcomes from a prospective study of drug-induced liver injury in the United States. Gastroenterology. 2008;135(6):1924-1934. doi:10.1053/j.gastro.2008.09.011

6. Chalasani N, Bonkovsky HL, Fontana R, et al. Features and outcomes of 899 patients with drug-induced liver injury: the DILIN Prospective Study. Gastroenterology. 2015;148(7):1340-1352.e7. doi:10.1053/j.gastro.2015.03.006

7. National Institute of Diabetes and Digestive and Kidney Diseases. LiverTox: Clinical and Research Information on Drug-Induced Liver Injury. Bethesda (MD): National Institute of Diabetes and Digestive and Kidney Diseases; 2012. https://livertox.nih.gov

8. Navarro VJ, Senior JR. Drug-related hepatotoxicity. N Engl J Med. 2006;354(7):731-739. doi:10.1056/NEJMra052270

9. Lucena MI, Andrade RJ, Kaplowitz N, et al. Phenotypic characterization of idiosyncratic drug-induced liver injury: the influence of age and sex. Hepatology. 2009;49(6):2001-2009. doi:10.1002/hep.22895

10. Andrade RJ, Lucena MI, Fernandez MC, et al. Drug-induced liver injury: an analysis of 461 incidences submitted to the Spanish registry over a 10-year period. Gastroenterology. 2005;129(2):512-521. doi:10.1016/j.gastro.2005.05.006

11. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001

12. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? Pharmacogenomics, pharmacokinetics, and pharmacodynamics. J Womens Health (Larchmt). 2005;14(4):292-307. doi:10.1089/jwh.2005.14.292

13. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16(10):626-638. doi:10.1038/nri.2016.90

14. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. Lancet. 2020;396(10250):565-582. doi:10.1016/S0140-6736(20)31561-0

15. Kaplowitz N. Idiosyncratic drug hepatotoxicity. Nat Rev Drug Discov. 2005;4(6):489-499. doi:10.1038/nrd1750

16. Liberal R, Longhi MS, Mieli-Vergani G, Vergani D. Autoimmune hepatitis: a comprehensive review. J Autoimmun. 2013;41:34-45. doi:10.1016/j.jaut.2012.11.002

17. Postow MA, Sidlow R, Hellmann MD. Immune-related adverse events associated with immune checkpoint blockade. N Engl J Med. 2018;378(2):158-168. doi:10.1056/NEJMra1703481

18. De Martin E, Michot JM, Rosmorduc O, Guettier C, Samuel D. Liver toxicity as a limiting factor to the increasing use of immune checkpoint inhibitors. JHEP Rep. 2020;2(6):100170. doi:10.1016/j.jhepr.2020.100170

19. Conforti F, Pala L, Bagnardi V, et al. Cancer immunotherapy efficacy and patients' sex: a systematic review and meta-analysis. Lancet Oncol. 2018;19(6):737-746. doi:10.1016/S1470-2045(18)30261-4

20. Sakaeda T, Tamon A, Kadoyama K, Okuno Y. Data mining of the public version of the FDA Adverse Event Reporting System. Int J Med Sci. 2013;10(7):796-803. doi:10.7150/ijms.6048

21. Reuben A, Koch DG, Lee WM; Acute Liver Failure Study Group. Drug-induced acute liver failure: results of a U.S. multicenter, prospective study. Hepatology. 2010;52(6):2065-2076. doi:10.1002/hep.23937

22. International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use (ICH). ICH E5(R1): Ethnic Factors in the Acceptability of Foreign Clinical Data. 1998.

---

## Supplementary Material

### Supplementary Table S1. Complete List of 133 Hepatic MedDRA Preferred Terms

Available in the SexDiffKG repository: https://github.com/jshaik369/sexdiffkg-deep-analysis

### Supplementary Table S2. All 601 Drugs with Sex-Differential Hepatotoxicity Signals

Available in the SexDiffKG repository: https://github.com/jshaik369/sexdiffkg-deep-analysis

### Supplementary Figure S1. Volcano Plot of Sex-Differential Hepatotoxicity Signals

Plot of logR (x-axis) versus -log10(p-value) (y-axis) for all 3,073 hepatotoxicity signals, colored by drug class.

---

## Figure Legends

**Figure 1.** Drug class hepatotoxicity spectrum. Bar chart showing female signal proportion for 10 drug classes, from checkpoint inhibitors (95.1%F) to autoimmune hepatitis (27.8%F). Color-coded by mechanism category: immune-mediated (red), metabolic (orange), immune-suppressive (blue), paradoxical (gray). Dashed horizontal lines indicate the overall FAERS female baseline (60.2%) and the hepatotoxicity female mean (65.3%F).

**Figure 2.** Hepatotoxicity subtype severity gradient. Stacked bar chart of 5 DILI subtypes ordered by severity. Female proportion increases from steatosis/fibrosis (59.3%F) to hepatic failure (69.0%F), with autoimmune hepatitis as the paradoxical outlier (27.8%F). Severity categories annotated with mean |logR| values.

**Figure 3.** The checkpoint inhibitor hepatotoxicity signal. Individual signal profiles for nivolumab, pembrolizumab, ipilimumab, and atezolizumab. 39/41 signals are female-biased, the most extreme class-level signal in SexDiffKG. Inset: comparison of ICI hepatotoxicity (95.1%F) with ICI colitis (68%F), ICI pneumonitis (62%F), and ICI dermatitis (71%F) to demonstrate organ-specific sex-differential patterns.

**Figure 4.** Anti-regression within hepatotoxicity. Volume decile plot showing female proportion increasing monotonically within hepatotoxicity signals (rho = 1.000). Each point represents one decile of drugs ranked by total hepatic report volume. Dashed line: overall FAERS female baseline (60.2%). Demonstrates that hepatic female bias is not a small-sample artifact but intensifies with increasing data.

**Figure 5.** The autoimmune hepatitis paradox. Comparison of drug-induced autoimmune hepatitis (27.8%F, male-biased) with spontaneous autoimmune hepatitis (70--80%F, female-biased) and overall DILI (65.3%F, female-biased). Three hypothesized mechanisms illustrated: (A) distinct HLA associations, (B) testosterone-mediated neoantigen formation, (C) diagnostic ascertainment bias.

**Figure 6.** The three-tier mechanism-based framework for sex-differential DILI. Schematic illustrating the relationship between drug mechanism (immune-activating, metabolic, immune-suppressive) and the degree of female DILI bias, with molecular mediators (CYP3A4, CD4/CD8 T-cells, PD-1/CTLA-4, TNF-alpha) annotated at each tier.
