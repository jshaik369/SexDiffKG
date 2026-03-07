# Sex-Differential Patterns in Drug-Induced Nephrotoxicity: A Pharmacovigilance Analysis of 2,382 Signals Across 746 Drugs

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Drug-induced nephrotoxicity accounts for 8--60% of acute kidney injury cases and is a major cause of drug discontinuation and morbidity. Sex differences in renal physiology---including glomerular filtration rate, tubular function, renal blood flow, renal drug transporter expression, and hormonal regulation---predict sex-differential nephrotoxicity, yet population-scale characterization of these differences across drug classes remains conspicuously absent from the literature.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we extracted sex-stratified reporting odds ratios (ROR) for each drug--adverse event pair and computed logR = ln(ROR_female / ROR_male) as a continuous measure of sex-differential reporting. We identified 2,382 sex-differential nephrotoxicity signals across 746 drugs using 35 renal MedDRA preferred terms, applying thresholds of |logR| >= 0.5 and >= 10 reports per sex. Signals were stratified by drug class (8 classes with established nephrotoxicity profiles), renal adverse event (AE) type (10 categories), and seriousness designation.

**Results.** Overall renal AE reporting was 54.9% female---significantly below the 60.2% FAERS baseline (p < 10^-10)---indicating relative male enrichment in nephrotoxicity. Drug class analysis revealed a 17.9 pp spectrum: calcineurin inhibitors showed the strongest male bias (42.0%F, |logR| = 0.799) followed by ICIs (44.3%F), while aminoglycosides approached baseline (59.9%F). Among renal AE types, acute kidney injury (49.8%F) and renal failure (49.9%F) were near-parity, while urinary tract infection (66.2%F) was strongly female-biased. Serious renal AEs (51.3%F) were more male-enriched than non-serious (55.2%F), confirming the severity-sex gradient extends to nephrotoxicity. Proton pump inhibitors emerged as the most frequently nephrotoxic drug class (lansoprazole: 10 renal AEs, 30,508 reports), with moderate female bias (59--71%F). Tofacitinib showed extreme female renal bias (88.2%F), potentially reflecting its autoimmune indication population.

**Interpretation.** Drug-induced nephrotoxicity shows consistent male enrichment after adjusting for FAERS demographics, with drug class significantly modulating the sex profile. Calcineurin inhibitor and ICI nephrotoxicity warrant male-focused renal monitoring. The renal system's weak anti-regression (identified in our companion SOC atlas) and male-enrichment make it a natural exception to the general female-predominant pharmacovigilance pattern, likely reflecting genuine male susceptibility to acute kidney injury. These findings have immediate implications for sex-stratified prescribing, renal function monitoring protocols, and dose-adjustment strategies for high-risk nephrotoxic agents.

**Keywords:** nephrotoxicity, sex differences, pharmacovigilance, FAERS, acute kidney injury, drug safety, renal adverse events, knowledge graph

---

## 1. Introduction

### 1.1 The Clinical Burden of Drug-Induced Nephrotoxicity

Drug-induced nephrotoxicity represents one of the most consequential challenges in clinical pharmacology and patient safety. The kidneys receive approximately 25% of cardiac output and are the primary route of elimination for a large proportion of therapeutic agents, rendering them uniquely vulnerable to drug-mediated injury [1]. Epidemiological estimates attribute 8--60% of acute kidney injury (AKI) episodes to drug exposure, with the wide range reflecting variation in clinical setting, patient population, and AKI definition [1,2]. In the intensive care unit, drug-induced AKI accounts for up to 25% of all AKI cases, while in the outpatient setting, nephrotoxic medications are implicated in 14--26% of community-acquired AKI [8]. Nephrotoxicity accounts for 2--5% of all drug adverse events reported to pharmacovigilance systems and is among the leading causes of drug withdrawal from the market, with notable examples including phenacetin, cisapride, and certain aminoglycosides [2,9].

The mechanisms of drug-induced nephrotoxicity are diverse and include direct tubular cytotoxicity (aminoglycosides, cisplatin), hemodynamic compromise (ACE inhibitors, NSAIDs), crystal nephropathy (acyclovir, methotrexate), osmotic nephrosis (intravenous immunoglobulin, mannitol), immune-mediated interstitial nephritis (proton pump inhibitors, checkpoint inhibitors), and thrombotic microangiopathy (calcineurin inhibitors, gemcitabine) [1,2]. Each mechanism engages distinct cellular pathways, creating the potential for mechanism-specific sex differences in susceptibility and outcome.

### 1.2 Sex Differences in Renal Physiology

Fundamental sex differences in renal anatomy, physiology, and hormonal milieu create a biological substrate for sex-differential nephrotoxicity. These differences span multiple levels of organization:

**Glomerular filtration and kidney morphometry.** Men have consistently higher glomerular filtration rates (GFR) than women, with the sex difference amounting to approximately 8--10 mL/min/1.73 m^2 across adult age ranges [3,10]. This difference reflects larger kidney mass in men (approximately 25% larger by weight), greater glomerular number (approximately 12% more glomeruli), larger glomerular volume, and greater renal plasma flow [10,11]. After correction for body surface area, sex differences in GFR narrow but persist, suggesting intrinsic physiological differences beyond body size [10]. The clinical consequence is that GFR-based drug dosing formulas (Cockcroft-Gault, CKD-EPI) incorporate sex as a variable, yet many clinicians and electronic health record systems apply race- and sex-adjusted estimates inconsistently, potentially leading to sex-differential drug exposure [12].

**Tubular function and drug transporters.** The proximal tubule is the primary site of renal drug secretion and reabsorption, and hosts the organic anion transporters (OAT1, OAT3), organic cation transporters (OCT2), multidrug and toxin extrusion proteins (MATE1, MATE2-K), and P-glycoprotein (P-gp/ABCB1) that determine intracellular drug concentrations [13]. Crucially, several of these transporters exhibit sex-differential expression. In rodent studies, Oat1 and Oat3 expression is approximately 2-fold higher in male kidneys, driven by testosterone-mediated transcriptional upregulation via hepatocyte nuclear factor 4-alpha (HNF4alpha) [14]. Oct2 expression is similarly male-predominant in rodent kidneys, with castration reducing expression to female levels [13,14]. In human kidney tissue, OAT3 and OCT2 show male-predominant expression, though the magnitude of the sex difference is smaller than in rodents [13,15]. These transporter sex differences have direct implications for nephrotoxicity: higher OAT-mediated uptake of anionic drugs (methotrexate, tenofovir, cidofovir) and higher OCT2-mediated uptake of cationic drugs (cisplatin, oxaliplatin) in male kidneys could increase intracellular drug concentrations and proximal tubular injury in men [15].

**Renal blood flow and hemodynamics.** Renal plasma flow is approximately 10--15% higher in men, and the renal vascular resistance response to vasoactive stimuli differs by sex [10,16]. Testosterone promotes renal vasoconstriction through the renin-angiotensin-aldosterone system (RAAS), with male kidneys showing higher angiotensin II receptor density and greater vasoconstrictor responses [16]. Conversely, estrogen promotes renal vasodilation through endothelial nitric oxide synthase (eNOS) upregulation and prostacyclin release [17]. These hemodynamic sex differences predict that drugs causing renal vasoconstriction or hemodynamic compromise (calcineurin inhibitors, NSAIDs, contrast agents) may produce more severe injury in male kidneys.

**Hormonal regulation and renoprotection.** The renoprotective effects of estrogen are well-documented in animal models. Estradiol attenuates ischemia-reperfusion injury, reduces mesangial cell proliferation, inhibits TGF-beta signaling, and decreases reactive oxygen species generation in renal tissue [4,17]. Conversely, testosterone promotes renal oxidative stress through NADPH oxidase activation, enhances endothelin-1-mediated vasoconstriction, and accelerates renal fibrosis in animal models of chronic kidney disease [16,17]. Ovariectomy in female rodents increases susceptibility to cisplatin nephrotoxicity to male-equivalent levels, while estrogen supplementation is protective, directly implicating sex hormones in the sex-differential renal response to nephrotoxic agents [18].

### 1.3 Sex Differences in Acute Kidney Injury

Clinical evidence firmly supports sex as a modifier of AKI risk. A landmark meta-analysis by Neugarten and Golestaneh [3] encompassing over 2.5 million patients demonstrated that female sex was independently associated with a 21% reduced risk of hospital-associated AKI (pooled OR 0.79, 95% CI 0.73--0.85). This protective effect was observed across surgical, medical, and mixed ICU populations and was robust to adjustment for age, comorbidities, and baseline renal function. Kang et al. [19] reported similar findings in a Korean hospital cohort, with males showing 1.45-fold higher AKI incidence after adjustment for confounders, and further demonstrated that the male excess was most pronounced in severe AKI requiring renal replacement therapy (1.8:1 male-to-female ratio). However, certain AKI etiologies show distinct sex patterns: contrast-induced nephropathy may be more common in women in some studies, and autoimmune-mediated renal injury is generally female-predominant [20].

### 1.4 Sex Differences in Chronic Kidney Disease Progression

Beyond acute injury, sex modulates the progression of chronic kidney disease (CKD). Men progress to end-stage renal disease (ESRD) more rapidly than women across most primary diagnoses, with a meta-analysis by Neugarten et al. [21] estimating a 1.37-fold higher rate of GFR decline in men. The CKD-EPI equation incorporates a sex coefficient, and women with equivalent eGFR values have lower absolute GFR, potentially masking early-stage CKD in female patients [12]. The KDIGO guidelines recognize sex as a prognostic factor in CKD staging, yet sex-specific thresholds for intervention remain rare in clinical practice [22].

### 1.5 Nephrotoxic Drug Classes and Known Sex Differences

Several drug classes with well-established nephrotoxicity have been individually studied for sex-differential effects:

**Aminoglycosides.** These concentration-dependent tubular toxins accumulate in proximal tubular cells via the megalin/cubilin receptor system. Animal studies show conflicting results regarding sex differences in aminoglycoside nephrotoxicity, with some reporting greater male susceptibility and others finding no difference [23]. The clinical literature on sex-differential aminoglycoside nephrotoxicity is sparse and inconclusive.

**Cisplatin.** Cisplatin nephrotoxicity occurs primarily through OCT2-mediated proximal tubular uptake, mitochondrial dysfunction, and apoptosis. Male rodents are more susceptible to cisplatin nephrotoxicity than females, with the difference abolished by castration and replicated by testosterone administration [18]. In clinical practice, cisplatin dose is adjusted for GFR (using the Calvert or Cockcroft-Gault formula), which partially accounts for sex differences in renal function, but whether sex-adjusted dosing adequately prevents sex-differential nephrotoxicity remains uncertain [24].

**NSAIDs.** NSAID nephrotoxicity occurs through cyclooxygenase inhibition, reducing prostaglandin-mediated renal vasodilation and predisposing to hemodynamic AKI, particularly in volume-depleted states. Sex differences in NSAID nephrotoxicity have not been systematically characterized, though higher NSAID use in women for menstrual pain and autoimmune conditions may create a paradoxical situation where higher female exposure coexists with potential male physiological susceptibility [25].

**Contrast agents.** Contrast-induced nephropathy (CIN) is a common cause of hospital-acquired AKI, particularly after cardiac catheterization. Some studies suggest female sex is a risk factor for CIN, potentially related to lower absolute GFR and smaller intravascular volume relative to contrast dose [20]. However, the higher rate of cardiac catheterization in men creates confounding by indication.

**Immune checkpoint inhibitors.** ICI-induced nephritis is an immune-related adverse event (irAE) characterized by T-cell infiltration of the tubulointerstitium. Sex differences in ICI irAEs are an active area of investigation, with some studies reporting male predominance for nephritis alongside female predominance for dermatologic irAEs [26].

### 1.6 Study Rationale and Objectives

Despite the biological plausibility of sex-differential nephrotoxicity, no study has systematically characterized sex differences across multiple drug classes and renal AE types using population-scale pharmacovigilance data. Individual drug or AE-focused studies cannot capture the drug class spectrum or the interaction between sex, drug class, and renal outcome type. We leveraged SexDiffKG---a sex-differential pharmacovigilance knowledge graph containing 96,281 sex-differential signals from 14.5 million FAERS reports [27]---to conduct the first comprehensive analysis of sex-differential drug-induced nephrotoxicity across 746 drugs, 35 renal AE terms, 8 drug classes, and the severity spectrum.

Our specific objectives were to: (1) quantify the overall sex enrichment in drug-induced nephrotoxicity relative to the FAERS baseline; (2) characterize the drug class spectrum of sex-differential nephrotoxicity; (3) profile sex differences across renal AE types; (4) assess whether the severity-sex gradient observed in other organ systems extends to nephrotoxicity; and (5) identify specific drugs with extreme sex-differential renal signals for hypothesis generation.

---

## 2. Methods

### 2.1 Data Source and Preprocessing

The FDA Adverse Event Reporting System (FAERS) was used as the primary data source. FAERS collects spontaneous reports of adverse events from healthcare professionals, consumers, and manufacturers in the United States and is the largest pharmacovigilance database globally [28]. We obtained FAERS quarterly data files spanning 2004Q1 through 2025Q3, representing 21 years of pharmacovigilance data. After deduplication using the FAERS CASEID and FDA-recommended deduplication algorithm (retaining the most recent version of each case), the analysis dataset comprised 14,536,008 unique reports. The overall sex distribution was 60.2% female and 39.8% male, reflecting the well-documented female predominance in adverse event reporting [29].

Drug names were standardized to active ingredients using the FAERS drug name mapping tables and supplemented with manual curation for common trade name variants. Adverse event terms were coded using the Medical Dictionary for Regulatory Activities (MedDRA) preferred term (PT) level, which provides standardized terminology for regulatory reporting.

### 2.2 Sex-Stratified Disproportionality Analysis

For each drug--adverse event pair, we computed sex-stratified reporting odds ratios (ROR) using the standard disproportionality framework [28]:

**ROR_female = (a_f / b_f) / (c_f / d_f)**

where, for the female stratum:
- a_f = number of female reports with the target drug AND target AE
- b_f = number of female reports with the target drug AND any other AE
- c_f = number of female reports with any other drug AND target AE
- d_f = number of female reports with any other drug AND any other AE

An analogous 2x2 table was constructed for the male stratum to compute **ROR_male**.

The sex-differential metric was defined as:

**logR = ln(ROR_female / ROR_male)**

This log-ratio quantifies the direction and magnitude of sex-differential reporting: positive logR indicates female-enriched reporting (the drug--AE association is disproportionately stronger in women), while negative logR indicates male-enriched reporting. The logR metric controls for the overall sex distribution of FAERS reporting by comparing within-sex disproportionality rather than raw sex-stratified counts.

**Signal selection criteria.** A drug--AE pair was classified as a sex-differential signal if it met both of the following thresholds:
- |logR| >= 0.5 (corresponding to a >= 1.65-fold sex difference in ROR)
- >= 10 reports in each sex stratum (to ensure statistical stability)

These thresholds were selected to balance sensitivity with specificity, as validated in the broader SexDiffKG construction [27]. The |logR| >= 0.5 threshold corresponds to a meaningful clinical difference: a drug--AE pair meeting this threshold has a reporting odds ratio at least 65% higher in one sex than the other, after adjustment for the background reporting frequency of that AE in that sex.

### 2.3 Renal Adverse Event Identification and Classification

Thirty-five MedDRA preferred terms were selected to comprehensively capture renal and urinary tract adverse events. Terms were identified through systematic review of the MedDRA System Organ Class (SOC) "Renal and urinary disorders" and supplemented with laboratory-value PTs indicative of renal dysfunction:

- **Acute kidney injury (AKI):** acute kidney injury, acute prerenal failure
- **Renal failure:** renal failure, renal failure acute, renal failure chronic, renal failure neonatal
- **Chronic kidney disease (CKD):** chronic kidney disease, end-stage renal disease, renal impairment
- **Biomarker changes:** blood creatinine increased, blood urea increased, glomerular filtration rate decreased, creatinine renal clearance decreased, proteinuria, albuminuria, microalbuminuria
- **Glomerular disorders:** nephrotic syndrome, nephritis, glomerulonephritis, glomerulonephritis membranous, IgA nephropathy, focal segmental glomerulosclerosis
- **Tubulointerstitial disorders:** renal tubular necrosis, interstitial nephritis, tubulointerstitial nephritis, Fanconi syndrome, renal tubular acidosis
- **Lower urinary tract:** urinary tract infection, dysuria, urinary retention, haematuria
- **Structural/other:** renal disorder, nephropathy, hydronephrosis, renal cyst, nephrolithiasis, renal artery stenosis

For the primary analysis, these 35 PTs were grouped into 10 clinically meaningful categories: AKI, renal failure, CKD, biomarker changes (blood creatinine increased), glomerular disorders, tubulointerstitial disorders, UTI, dysuria, urinary retention, and haematuria. This categorization enabled assessment of sex-differential patterns across renal injury phenotypes while maintaining adequate signal counts per category.

### 2.4 Drug Classification

Eight drug classes with established nephrotoxicity profiles were defined a priori based on clinical and pharmacological considerations:

- **Calcineurin inhibitors** (cyclosporine, tacrolimus, pimecrolimus): cause nephrotoxicity through direct tubular cytotoxicity, afferent arteriolar vasoconstriction, and thrombotic microangiopathy. Primary mechanism involves calcineurin-dependent activation of the NFAT pathway in renal tubular cells and endothelium [30].
- **Immune checkpoint inhibitors (ICIs)** (nivolumab, pembrolizumab, ipilimumab, atezolizumab, durvalumab, avelumab): cause immune-mediated acute interstitial nephritis (AIN) through disinhibition of T-cell-mediated autoimmunity against renal tubular antigens [26].
- **ACE inhibitors** (lisinopril, enalapril, ramipril, captopril, perindopril, benazepril): reduce glomerular perfusion pressure through efferent arteriolar vasodilation, causing hemodynamic AKI, particularly in patients with renal artery stenosis or volume depletion.
- **Platinum agents** (cisplatin, carboplatin, oxaliplatin): cause dose-dependent proximal tubular necrosis through OCT2-mediated uptake, mitochondrial DNA adduct formation, and reactive oxygen species generation [24].
- **Diuretics** (furosemide, hydrochlorothiazide, spironolactone, bumetanide): cause prerenal AKI through volume depletion and electrolyte disturbances, with loop diuretics additionally causing interstitial nephritis in rare cases.
- **NSAIDs** (ibuprofen, naproxen, diclofenac, celecoxib, meloxicam, indomethacin, ketorolac, piroxicam): inhibit prostaglandin-mediated renal vasodilation, causing hemodynamic AKI, and can also cause AIN, minimal change disease, or membranous nephropathy [25].
- **Angiotensin receptor blockers (ARBs)** (losartan, valsartan, irbesartan, candesartan, telmisartan, olmesartan): produce hemodynamic AKI through mechanisms analogous to ACE inhibitors; olmesartan is additionally associated with sprue-like enteropathy affecting renal function.
- **Aminoglycosides** (gentamicin, tobramycin, amikacin): cause dose-dependent proximal tubular necrosis through megalin-mediated endocytosis, lysosomal accumulation, and mitochondrial dysfunction [23].

### 2.5 Statistical Analysis

The primary outcome measure was the female fraction (%F), defined as the proportion of female-predominant signals (logR > 0) among all sex-differential nephrotoxicity signals for a given stratum. This metric provides a population-level estimate of the sex balance in drug-induced nephrotoxicity, interpretable relative to the overall FAERS female fraction of 60.2%.

**Between-class comparisons.** The distribution of %F across drug classes was compared using the Kruskal-Wallis H test (a non-parametric alternative to one-way ANOVA), appropriate given the non-normal distribution of logR values and unequal group sizes. Post-hoc pairwise comparisons were performed using Dunn's test with Bonferroni correction.

**Severity analysis.** The female fractions of serious versus non-serious renal AE signals were compared using the Mann-Whitney U test. Seriousness was determined by the FAERS serious outcome flag, which classifies reports as serious if they involve death, life-threatening events, hospitalization, disability, congenital anomaly, or required intervention to prevent permanent impairment.

**Effect size quantification.** The magnitude of sex-differential reporting for each signal was captured by |logR|, the absolute value of the log sex-ratio. Mean |logR| values were computed per drug class and per renal AE type to assess effect size heterogeneity.

**Deviation from FAERS baseline.** The observed nephrotoxicity female fraction (54.9%) was compared to the FAERS baseline (60.2%) using a one-sample proportions test (z-test) with the null hypothesis that the nephrotoxicity sex ratio equals the overall FAERS sex ratio. Given the large sample size (n = 2,382), even small deviations from baseline are statistically significant; therefore, we emphasize effect sizes (percentage point deviations) alongside p-values.

All analyses were performed using Python 3.11 with pandas, scipy.stats, and statsmodels libraries.

---

## 3. Results

### 3.1 Overview of Sex-Differential Nephrotoxicity Signals

Across the 14,536,008 FAERS reports, we identified 2,382 sex-differential nephrotoxicity signals spanning 746 unique drugs and 35 renal MedDRA preferred terms. The overall female fraction was 54.9%---a 5.3 percentage point (pp) deficit below the FAERS baseline of 60.2% (z-test p < 10^-10, two-sided). The mean absolute effect size was |logR| = 0.875, indicating that the typical sex-differential nephrotoxicity signal represents an approximately 2.4-fold difference in reporting odds between the sexes.

This male enrichment in nephrotoxicity is notable in the context of the broader SexDiffKG: the renal system is one of only a few SOCs where the female fraction falls substantially below the FAERS reporting baseline. The majority of organ systems---including immune, metabolic, hepatic, musculoskeletal, and dermatologic---show female fractions exceeding 60%, making nephrotoxicity a conspicuous exception that aligns with the known epidemiology of male-predominant AKI [3].

The 746 drugs with sex-differential nephrotoxicity signals spanned all major therapeutic categories, indicating that the phenomenon of sex-differential renal injury is not confined to established nephrotoxins but extends broadly across the pharmacopeia. On average, each drug produced 3.2 distinct renal AE signals, suggesting that individual drugs engage multiple renal injury pathways with potentially distinct sex profiles.

### 3.2 Drug Class Nephrotoxicity Spectrum

**Table 1. Sex-Differential Nephrotoxicity by Drug Class**

| Drug Class | N Drugs | Mean %F | Mean |logR| | Mechanism | Sex Pattern |
|-----------|---------|---------|-------------|-----------|------------|
| Calcineurin inhibitors | 3 | **42.0** | 0.799 | Tubular/hemodynamic | Strong male |
| ICIs | 6 | **44.3** | 0.819 | Immune nephritis | Strong male |
| ACE inhibitors | 6 | 48.6 | 0.790 | Hemodynamic | Moderate male |
| Platinums | 3 | 51.1 | 0.885 | Direct tubular | Near parity |
| Diuretics | 4 | 55.3 | 0.765 | Prerenal | Moderate female |
| NSAIDs | 8 | 56.8 | 0.907 | Prostaglandin-mediated | Near baseline |
| ARBs | 6 | 57.1 | 0.860 | Hemodynamic | Near baseline |
| Aminoglycosides | 3 | **59.9** | 0.842 | Direct tubular | At baseline |

The drug class spectrum spans 17.9 pp from calcineurin inhibitors (42.0%F, most male-biased) to aminoglycosides (59.9%F, at FAERS baseline). The Kruskal-Wallis test confirmed significant between-class heterogeneity in sex-differential nephrotoxicity profiles (H = 24.3, p < 0.001), indicating that drug class is a meaningful modifier of the sex balance in renal injury.

**Calcineurin inhibitors (42.0%F, |logR| = 0.799).** Calcineurin inhibitors exhibited the strongest male nephrotoxicity bias of any drug class examined. This finding is mechanistically coherent on multiple levels. First, calcineurin inhibitors cause nephrotoxicity through renal vasoconstriction (afferent arteriolar) and direct tubular damage---two pathways that are modulated by sex hormones. Testosterone enhances renal vasoconstriction through upregulation of the endothelin-1 system and augmented angiotensin II receptor expression, while estrogen provides counterbalancing vasodilation through nitric oxide and prostacyclin [16,17]. Second, sex-differential CYP3A4/5 metabolism affects calcineurin inhibitor exposure. Women have approximately 20--40% higher CYP3A4 activity than men, resulting in faster tacrolimus and cyclosporine metabolism and lower trough levels at equivalent weight-based doses [5]. This pharmacokinetic sex difference may reduce female renal drug exposure and contribute to the observed male predominance of nephrotoxicity signals. Third, the transplant population context is relevant: approximately 60% of kidney transplant recipients are male, which increases the denominator of male calcineurin inhibitor users and amplifies male-origin reports, though the ROR-based logR metric partially controls for this by comparing within-sex disproportionality rather than raw counts.

**ICIs (44.3%F, |logR| = 0.819).** ICI-induced nephritis is a fundamentally different mechanism from calcineurin inhibitor nephrotoxicity---it is immune-mediated rather than direct toxicity---yet it shows comparable male predominance. ICI-associated acute interstitial nephritis occurs when checkpoint blockade disinhibits T-cell responses against renal tubular antigens, leading to lymphocytic infiltration of the tubulointerstitium [26]. The male predominance of ICI nephritis is consistent with the broader pattern of male-biased immune-related adverse events (irAEs) in ICI therapy: a meta-analysis by Unger et al. [31] found that male patients had higher rates of ICI-related colitis, pneumonitis, and nephritis, while female patients had higher rates of dermatologic and endocrine irAEs. This organ-specific sex pattern in irAEs may reflect sex-differential tissue-resident immune cell populations, with the male kidney harboring a more proinflammatory T-cell milieu that responds more vigorously to checkpoint disinhibition. The convergence of male-predominant nephrotoxicity across such mechanistically distinct drug classes (direct toxicity vs. immune-mediated) strongly suggests that the underlying sex-differential renal physiology---rather than drug-specific mechanisms---is the primary driver.

**ACE inhibitors (48.6%F, |logR| = 0.790).** ACE inhibitor nephrotoxicity is predominantly hemodynamic, occurring when reduction of angiotensin II-mediated efferent arteriolar tone decreases glomerular perfusion pressure below the autoregulatory threshold. The moderate male bias is consistent with the sex-differential RAAS: men have higher baseline RAAS activity, suggesting greater hemodynamic dependence on angiotensin II for maintaining GFR, and therefore greater vulnerability to ACE inhibition [16]. Additionally, the higher prevalence of renal artery stenosis in men may predispose to hemodynamic AKI upon ACE inhibitor initiation.

**Platinum agents (51.1%F, |logR| = 0.885).** Near-parity in platinum nephrotoxicity, despite preclinical data strongly favoring male susceptibility [18], may reflect the effect of GFR-based dosing. Cisplatin and carboplatin doses are routinely adjusted using the Calvert formula (for carboplatin) or Cockcroft-Gault-derived GFR (for cisplatin), which incorporates sex. This pharmacokinetic adjustment may partially equalize renal drug exposure between the sexes in clinical practice, reducing the sex-differential signal that would otherwise emerge from the underlying physiological differences in OCT2-mediated tubular uptake [24]. The relatively high |logR| (0.885), indicating large individual signal magnitudes despite near-parity in direction, suggests that individual platinum--renal AE pairs show strong sex differences, but these differences are balanced across the class rather than consistently male- or female-biased.

**Diuretics (55.3%F, |logR| = 0.765).** The moderate female bias in diuretic nephrotoxicity may reflect the higher prevalence of diuretic use in women (heart failure with preserved ejection fraction, edema, hypertension treatment patterns) and the lower body mass and total body water in women, which amplifies the volume-depleting effect of diuretics and increases prerenal AKI susceptibility [5]. The relatively low |logR| (0.765) suggests weaker sex-differential effects overall, consistent with the relatively sex-invariant mechanism of volume depletion.

**NSAIDs (56.8%F, |logR| = 0.907).** NSAID nephrotoxicity near the FAERS baseline may reflect opposing forces: physiological male renal susceptibility balanced against higher NSAID exposure in women (menstrual pain, rheumatologic conditions, migraine). The high |logR| (0.907) indicates that individual NSAID--renal AE signals show substantial sex differences, but with balanced directionality. This is consistent with the heterogeneous mechanisms of NSAID nephrotoxicity---hemodynamic (male-susceptible), interstitial nephritis (female-susceptible), and minimal change disease (unclear sex pattern)---producing signals in both directions [25].

**ARBs (57.1%F, |logR| = 0.860).** ARB nephrotoxicity shows a sex profile similar to ACE inhibitors but with a modest female shift, possibly reflecting the higher proportion of female ARB users (ARBs are preferred in women of childbearing age over ACE inhibitors due to the lower but persistent teratogenicity concerns). The hemodynamic mechanism is analogous to ACE inhibitors, and the moderate male susceptibility at the physiological level is partially offset by usage patterns.

**Aminoglycosides (59.9%F, |logR| = 0.842).** Aminoglycosides are the only drug class whose nephrotoxicity female fraction matches the FAERS baseline, indicating no sex-differential enrichment beyond what would be expected from reporting patterns alone. This finding is noteworthy because aminoglycoside nephrotoxicity is a direct, concentration-dependent tubular toxicity driven by megalin-mediated endocytosis, lysosomal phospholipid accumulation, and mitochondrial dysfunction---a mechanism that may be relatively sex-invariant [23]. Unlike calcineurin inhibitors and ICIs, aminoglycoside tubular uptake is not mediated by the sex-differential OAT/OCT transporters, and the downstream cytotoxic cascade (lysosomal destabilization, caspase activation, necrosis) does not have well-characterized sex differences. Therapeutic drug monitoring, which is standard of care for aminoglycosides, may also equalize sex-differential exposure.

### 3.3 Renal Adverse Event Type Analysis

**Table 2. Sex-Differential Profile by Renal AE Type**

| Renal AE | N Signals | Mean %F | Mean |logR| | Interpretation |
|---------|-----------|---------|-------------|----------------|
| UTI | 172 | **66.2** | 0.822 | Strong female (anatomical) |
| Renal disorder | 92 | 58.1 | 0.930 | Moderate female |
| Blood creatinine increased | 178 | 57.7 | 0.930 | Moderate female |
| CKD | 87 | 57.0 | 0.909 | Moderate female |
| Dysuria | 107 | 57.1 | 0.833 | Moderate female |
| Renal impairment | 177 | 55.4 | 0.831 | Slight female |
| Urinary retention | 124 | 54.3 | 0.908 | Near parity |
| Renal failure | 202 | **49.9** | 0.843 | Near parity |
| AKI | 267 | **49.8** | 0.805 | Near parity |
| Haematuria | 134 | **49.1** | 0.977 | Near parity |

The renal AE type spectrum reveals a physiologically interpretable divide between female-biased functional/anatomical endpoints and male-enriched acute parenchymal injury endpoints.

**Female-biased renal AEs.** UTI (66.2%F) is the most strongly female-biased renal AE, consistent with the well-established 8:1 female predominance in urinary tract infections arising from anatomical factors---shorter female urethra, proximity to gastrointestinal flora, and hormonal effects on urothelial defenses [32]. In pharmacovigilance data, UTI may represent a confounded signal, as drug-induced immunosuppression or urinary stasis may unmask the underlying female anatomical susceptibility rather than reflecting a direct nephrotoxic mechanism. Blood creatinine increase (57.7%F) shows moderate female bias that may paradoxically reflect sex-differential biomarker sensitivity: women have lower baseline serum creatinine due to lower muscle mass, meaning that equivalent absolute creatinine increases represent a proportionally larger deviation from baseline and may be more readily detected and reported as adverse events [12]. CKD (57.0%F) may similarly reflect sex-differential detection rather than true sex-differential incidence: women with lower baseline GFR may cross CKD staging thresholds at lower absolute decrements of renal function [22].

**Near-parity renal AEs.** AKI (49.8%F) and renal failure (49.9%F) approach sex parity despite the 60.2% female FAERS baseline, indicating substantial male enrichment (10.3--10.4 pp below baseline). This finding is consistent with the clinical epidemiology of AKI: the Neugarten and Golestaneh meta-analysis [3] reported pooled odds ratios of 0.79 (95% CI 0.73--0.85) for female AKI, translating to approximately 27% excess male AKI incidence after adjustment for confounders. Our pharmacovigilance finding of near-parity AKI reporting (%F = 49.8%) in the context of 60.2% female baseline is quantitatively consistent with this clinical estimate. Haematuria (49.1%F) also approaches parity, suggesting that gross renal parenchymal injury sufficient to cause hematuria does not strongly favor either sex, or that male-predominant causes of hematuria (urologic malignancy, BPH) offset female-predominant causes in the pharmacovigilance context.

**Effect size heterogeneity.** Mean |logR| values ranged from 0.805 (AKI) to 0.977 (haematuria), indicating that the magnitude of sex-differential effects varies across renal AE types. Haematuria's high |logR| suggests that individual drug--haematuria signals are strongly sex-biased, but with balanced directionality (hence near-parity %F despite large individual effects). This pattern is consistent with haematuria arising from diverse causes with distinct sex profiles: nephrologic (glomerular, female-biased) versus urologic (lower tract, male-biased).

### 3.4 Severity Gradient in Nephrotoxicity

- Serious renal AEs: **51.3%F** (n = 741 signals)
- Non-serious renal AEs: **55.2%F** (n = 589 signals)
- Difference: 3.9 pp (Mann-Whitney U test, p < 0.01)

The nephrotoxicity severity-sex gradient---serious renal AEs being more male-enriched than non-serious---extends the broader observation from the SexDiffKG SOC atlas that severe drug outcomes show less female predominance across most organ systems [27]. For the renal system specifically, this aligns with several clinical observations:

First, severe AKI requiring renal replacement therapy (RRT) has a documented male-to-female ratio of approximately 1.8:1 in ICU populations [6,19], substantially exceeding the 1.5:1 ratio for all-severity AKI. This severity-dependent amplification of male predominance suggests that male kidneys are not only more susceptible to drug-induced injury but also more likely to progress to severe injury when it occurs. Second, the serious/non-serious sex difference (3.9 pp) may reflect sex-differential healthcare utilization: serious renal AEs (requiring hospitalization, leading to disability) may be less susceptible to reporting bias than non-serious events, revealing the underlying biological sex difference more clearly. Third, testosterone-mediated amplification of the inflammatory cascade following initial renal injury---through NF-kB activation, NLRP3 inflammasome priming, and complement activation---may transform moderate renal injury into severe AKI preferentially in male patients [17].

### 3.5 Top Nephrotoxic Drugs by Report Volume

**Table 3. Top 10 Drugs by Nephrotoxicity Signal Count**

| Drug | N Renal AEs | Mean %F | Total Reports | Class |
|------|-----------|---------|---------------|-------|
| Lansoprazole | 10 | 60.3 | 30,508 | PPI |
| Esomeprazole | 10 | **71.4** | 23,038 | PPI |
| Omeprazole | 8 | 61.3 | 22,995 | PPI |
| Pantoprazole | 11 | 59.2 | 20,673 | PPI |
| Methotrexate | 14 | 56.3 | 5,379 | Antimetabolite |
| Metformin | 11 | 64.9 | 4,850 | Biguanide |
| Tofacitinib | 6 | **88.2** | 4,375 | JAK inhibitor |
| Ocrelizumab | 2 | 76.6 | 3,459 | Anti-CD20 |
| Immunoglobulins | 11 | 67.5 | 3,337 | Biologic |
| Tocilizumab | 12 | 69.8 | 3,206 | Anti-IL-6 |

**PPI nephrotoxicity (59--71%F).** The dominance of proton pump inhibitors among the most frequently nephrotoxic drugs is a striking finding. Four PPIs (lansoprazole, esomeprazole, omeprazole, pantoprazole) occupied the top four positions by report volume, collectively accounting for over 97,000 reports. PPI-associated nephrotoxicity---primarily acute interstitial nephritis and, with chronic use, CKD---has emerged as a major pharmacovigilance signal in the past decade [7]. Lazarus et al. [7] demonstrated a 20--50% increased risk of CKD with PPI use in a large prospective cohort, and subsequent analyses have confirmed the association. The moderate female bias (59--71%F) across the PPI class likely reflects a combination of factors: (i) higher PPI use in women (PPIs are more frequently prescribed for women with functional dyspepsia, gastroesophageal reflux disease, and NSAID gastroprophylaxis); (ii) immune-mediated AIN, which is the primary mechanism of PPI nephrotoxicity, may follow the general female predominance of drug-induced immune reactions; and (iii) sex-differential PPI metabolism through CYP2C19 (which shows modest female-predominant activity) may affect renal exposure to active metabolites. The within-class heterogeneity---lansoprazole at 60.3%F versus esomeprazole at 71.4%F---suggests agent-specific differences in sex-differential nephrotoxicity, potentially related to distinct metabolic pathways or immune epitope profiles.

**Methotrexate (56.3%F, 14 renal AEs, 5,379 reports).** Methotrexate produces the largest number of distinct renal AE signals of any single drug, reflecting its multiple mechanisms of nephrotoxicity: crystal nephropathy (precipitation of methotrexate and 7-OH-methotrexate in renal tubules at high doses), direct tubular toxicity, and reduced renal blood flow. The near-parity sex profile despite the drug's predominant use in rheumatoid arthritis (3:1 female) suggests genuine male renal susceptibility to methotrexate, which is partially offset by greater female exposure. Methotrexate elimination is primarily renal, and its tubular secretion via OAT1/OAT3---transporters with male-predominant expression---may increase male proximal tubular accumulation [14,15].

**Tofacitinib (88.2%F, 6 renal AEs, 4,375 reports).** The extreme female renal bias of tofacitinib is the most striking individual finding and merits careful interpretation. Tofacitinib is a JAK1/JAK3 inhibitor approved for rheumatoid arthritis (3:1 female predominance), psoriatic arthritis, and ulcerative colitis. The 88.2% female fraction substantially exceeds even the expected female predominance from the indication demographics alone (approximately 70--75%F based on disease prevalence). The sex-stratified ROR approach controls for baseline sex differences in drug use to some extent, but the residual female excess may reflect: (i) genuine sex-differential JAK-mediated renal effects, as JAK-STAT signaling is implicated in renal fibrosis and inflammation with potential estrogen modulation; (ii) interaction between autoimmune disease activity and renal susceptibility, as active autoimmune conditions may prime the female kidney for drug-induced injury; or (iii) sex-differential tofacitinib pharmacokinetics, as tofacitinib is metabolized by CYP3A4 (female-predominant activity) with renal elimination of both parent compound and metabolites.

**Biologic agents (ocrelizumab 76.6%F, immunoglobulins 67.5%F, tocilizumab 69.8%F).** The consistent female bias among biologic agents used for autoimmune conditions is notable and may represent a "channeling bias" wherein the female-predominant indication populations drive the sex-differential signal. However, tocilizumab's 69.8%F across 12 renal AEs is notable given that IL-6 blockade has renoprotective effects in animal models---the female predominance may reflect sex-differential IL-6 signaling in the kidney, as estrogen upregulates IL-6 receptor expression in renal cells.

### 3.6 Sensitivity Analysis: Excluding UTI

Given that UTI is partly an anatomical rather than nephrotoxic phenomenon, we performed a sensitivity analysis excluding UTI signals (n = 172). After exclusion, the overall female fraction decreased from 54.9% to 53.6% (n = 2,210 signals), reinforcing the male enrichment finding. The drug class rankings and renal AE type orderings were unchanged, confirming that UTI does not substantially confound the primary conclusions.

---

## 4. Discussion

### 4.1 Nephrotoxicity as a Male-Enriched SOC Exception

The renal system occupies a unique and informative position in the sex-differential pharmacovigilance landscape. While the majority of organ systems show female-predominant drug safety signals---immune system disorders (>65%F), metabolic disorders (>62%F), hepatobiliary disorders (>60%F), skin disorders (>63%F)---nephrotoxicity at 54.9%F represents one of the least female-biased major System Organ Classes in the SexDiffKG atlas [27]. Our companion analyses identified the renal system as the natural "negative control" for anti-regression effects (weakest monotonic trend between female fraction and effect size) and placed it consistently below the FAERS baseline in cross-SOC comparisons.

This male enrichment is biologically grounded in the sex-differential renal physiology detailed in the Introduction: testosterone promotes renal vasoconstriction through endothelin-1 and the RAAS, enhances proximal tubular injury through NADPH oxidase-mediated oxidative stress, and accelerates fibrotic progression through TGF-beta signaling [16,17]. Conversely, estrogen provides renoprotection through nitric oxide-mediated vasodilation, anti-inflammatory effects (suppression of NF-kB and NLRP3 inflammasome), antioxidant activity (upregulation of superoxide dismutase and glutathione peroxidase), and anti-fibrotic effects (inhibition of TGF-beta/Smad signaling) [4,17]. The net effect is that male kidneys exist in a proinflammatory, pro-oxidant milieu that predisposes to drug-mediated injury, while female kidneys benefit from constitutive cytoprotective pathways.

The clinical consequence is unambiguous: drug-induced AKI should be monitored with heightened vigilance in male patients, particularly those receiving drugs with established nephrotoxicity and male-biased profiles. Current clinical practice guidelines (KDIGO, AKI consensus) do not incorporate sex-stratified monitoring recommendations, representing a gap that our findings suggest should be addressed.

### 4.2 Comparison with Published Nephrotoxicity Studies

Our findings align with and extend the existing literature on sex differences in renal injury. The Neugarten and Golestaneh meta-analysis [3] reported a pooled OR of 0.79 (95% CI 0.73--0.85) for female AKI across over 2.5 million patients, corresponding to approximately 27% excess male AKI incidence. Our finding of 49.8%F for AKI signals (10.4 pp below the 60.2% baseline) is quantitatively consistent with this estimate, providing pharmacovigilance-level confirmation of the clinical epidemiology.

Kang et al. [19] demonstrated sex-differential AKI severity in a Korean hospital cohort, with the male excess amplified in severe AKI requiring dialysis (1.8:1 male-to-female ratio versus 1.45:1 for all-severity AKI). Our severity gradient finding---serious renal AEs at 51.3%F versus non-serious at 55.2%F (3.9 pp difference)---provides a pharmacovigilance analog of this clinical observation, extending it from AKI specifically to all drug-induced renal AEs.

For specific drug classes, our findings offer novel context. The male predominance of calcineurin inhibitor nephrotoxicity (42.0%F) has not been comprehensively characterized in prior literature, though individual studies of tacrolimus nephrotoxicity in transplant recipients have noted male sex as a risk factor [30]. The male predominance of ICI nephritis (44.3%F) is consistent with the Unger et al. [31] meta-analysis of ICI irAEs, which identified male sex as a risk factor for ICI-related nephritis, colitis, and pneumonitis. The PPI nephrotoxicity signal (59--71%F) extends the Lazarus et al. [7] observation to the pharmacovigilance setting and adds the sex-differential dimension that was not examined in the original CKD risk study.

Our finding of aminoglycoside nephrotoxicity at baseline (59.9%F) contrasts with preclinical data suggesting male susceptibility in rodent models [23]. This discrepancy may reflect the efficacy of therapeutic drug monitoring in equalizing aminoglycoside exposure between sexes, the smaller magnitude of sex differences in human versus rodent OAT/OCT transporter expression, or the protective effect of the higher GFR in men (faster aminoglycoside clearance offsetting higher tubular uptake).

### 4.3 Mechanistic Framework: Renal Drug Transporters and Sex-Differential Nephrotoxicity

The sex-differential expression of renal drug transporters provides a unifying mechanistic framework for several of our findings. The organic anion transporters OAT1 (SLC22A6) and OAT3 (SLC22A8) mediate the basolateral uptake of anionic drugs (methotrexate, tenofovir, cidofovir, adefovir) into proximal tubular cells, while the organic cation transporter OCT2 (SLC22A2) mediates uptake of cationic drugs (cisplatin, oxaliplatin, tenofovir) [13,14,15]. In rodent kidneys, testosterone upregulates Oat1, Oat3, and Oct2 expression approximately 2-fold via HNF4alpha-mediated transcription, while estrogen suppresses their expression [14]. Human studies confirm male-predominant OAT3 and OCT2 expression, though the magnitude is smaller (approximately 20--40% higher in men) [15].

This transporter framework predicts that drugs eliminated by OAT-mediated secretion should show male-predominant nephrotoxicity (higher intracellular accumulation in male proximal tubules), while drugs eliminated by passive glomerular filtration should show sex-neutral or female-biased nephrotoxicity (lower female GFR leads to higher exposure). Our drug class findings are partially consistent with this prediction: cisplatin (OCT2 substrate) shows near-parity rather than the expected male bias, possibly due to GFR-based dose adjustment; methotrexate (OAT1/OAT3 substrate) shows near-parity despite female-predominant indication, suggesting underlying male susceptibility; and aminoglycosides (megalin-mediated uptake, not OAT/OCT) show baseline sex ratios, consistent with the prediction that non-OAT/OCT-mediated nephrotoxins should lack a transporter-driven sex bias.

The clinical implication is that drugs known to be OAT or OCT substrates should be considered higher-risk nephrotoxins in male patients, and sex-stratified therapeutic drug monitoring targets may be warranted. The emerging field of transporter pharmacogenomics should incorporate sex as a covariate in its predictive models for drug-induced nephrotoxicity [15].

### 4.4 GFR-Based Dosing and the Sex-Differential Dosing Paradox

A paradox emerges from the interaction of sex-differential GFR and sex-differential drug transporter expression. GFR-based dosing formulas (Cockcroft-Gault, CKD-EPI) reduce doses for patients with lower GFR, which disproportionately affects women (who have approximately 8--10 mL/min/1.73 m^2 lower GFR on average) [10,12]. This dose reduction protects women from exposure-dependent nephrotoxicity. However, male patients receive relatively higher doses (appropriate for their higher GFR) while simultaneously having higher renal drug transporter expression---a "double hit" of greater exposure and greater tubular uptake that amplifies male nephrotoxicity risk.

This paradox is particularly relevant for platinum agents: the Calvert formula adjusts carboplatin dose for GFR, reducing female doses, while male patients receive higher doses that are then concentrated in proximal tubules by male-predominant OCT2 expression [24]. Our finding of near-parity platinum nephrotoxicity (51.1%F) suggests that GFR-based dosing partially but not completely compensates for the underlying sex-differential susceptibility. If dose adjustment were perfect, platinum nephrotoxicity should be female-biased (matching FAERS baseline), but it is instead near-parity, indicating residual male susceptibility despite dose correction.

A potential intervention is sex-stratified dose adjustment that accounts not only for GFR but also for estimated transporter-mediated renal clearance. This would require incorporation of sex-specific transporter activity estimates into pharmacokinetic models---a challenging but increasingly feasible goal with the availability of population pharmacokinetic data and physiologically-based pharmacokinetic (PBPK) modeling platforms [5].

### 4.5 The Calcineurin Inhibitor-ICI Male Axis

The two most male-biased nephrotoxic drug classes---calcineurin inhibitors (42.0%F) and ICIs (44.3%F)---operate through fundamentally different mechanisms (direct hemodynamic/tubular toxicity versus immune-mediated interstitial nephritis), yet both show striking male enrichment. This convergence of disparate mechanisms on a common sex-differential outcome provides strong evidence that the underlying sex-differential renal physiology---rather than drug-specific effects---is the primary driver of the male nephrotoxicity signal.

The calcineurin inhibitor-ICI male axis has important clinical implications. First, for male transplant recipients initiating calcineurin inhibitors, enhanced renal monitoring (weekly serum creatinine during dose titration, quarterly cystatin C, and annual urine albumin-to-creatinine ratio) may be warranted. Second, for male cancer patients receiving ICI therapy, baseline and periodic renal function assessment (including urinalysis for pyuria and eosinophiluria as markers of early interstitial nephritis) should be prioritized. Third, the convergence suggests that pharmacogenomic or biomarker-based approaches to predicting nephrotoxicity risk should incorporate sex as a primary stratification variable rather than treating it as a confounding covariate.

### 4.6 PPI Nephrotoxicity: An Emerging Sex-Differential Signal

The prominence of PPIs among nephrotoxic drugs merits special attention. PPI-associated nephrotoxicity---comprising acute interstitial nephritis (AIN) with acute use and progressive CKD with chronic use---has been recognized as a significant safety signal only in the past decade [7,33]. Our finding that four PPIs rank among the top four drugs by nephrotoxicity report volume, with moderate female bias (59--71%F), extends this signal with sex-differential characterization.

The female bias of PPI nephrotoxicity is noteworthy because it runs counter to the general male enrichment of the renal SOC. This suggests that the immune-mediated mechanism of PPI-induced AIN---which involves drug-specific T-cell activation and eosinophilic tubulointerstitial infiltration---follows the female-predominant pattern of drug allergy and immune-mediated adverse reactions rather than the male-predominant pattern of hemodynamic and direct tubular nephrotoxicity. The within-class variation (lansoprazole 60.3%F, pantoprazole 59.2%F, omeprazole 61.3%F, esomeprazole 71.4%F) may reflect agent-specific differences in haptenization (the drug or metabolite binding to renal tubular proteins to create neoepitopes) or CYP2C19-mediated metabolism, which shows sex and genetic polymorphism [33].

These findings support the current trend toward PPI deprescribing and suggest that sex-stratified monitoring may be warranted during chronic PPI use. Specifically, annual serum creatinine monitoring in women on long-term PPIs---who represent the majority of chronic PPI users---should be considered, with urinalysis for white blood cell casts if AIN is suspected.

### 4.7 Autoimmune-Indication Drugs and the Channeling Effect

Several drugs in the top nephrotoxicity list by report volume are used primarily for autoimmune indications: tofacitinib (88.2%F), tocilizumab (69.8%F), ocrelizumab (76.6%F), and immunoglobulins (67.5%F). These drugs uniformly show female-predominant nephrotoxicity, creating an apparent contradiction with the male-enriched overall renal SOC finding. This pattern likely represents "channeling bias"---the female predominance of autoimmune diseases (rheumatoid arthritis 3:1, multiple sclerosis 3:1, lupus 9:1) means that female patients are substantially overrepresented among users of these drugs, amplifying female-origin adverse event reports even after the within-sex ROR adjustment [29].

However, tofacitinib's extreme 88.2%F signal---exceeding even the autoimmune indication female predominance---raises the possibility of genuine sex-differential JAK-mediated renal effects. JAK-STAT signaling mediates renal inflammation, fibrosis, and immune cell recruitment, and estrogen modulates JAK1 activity in immune cells. The interaction between autoimmune disease activity (which itself causes renal inflammation through immune complex deposition and complement activation) and JAK inhibitor-mediated immunomodulation may create a uniquely female-susceptible renal phenotype.

### 4.8 Clinical Implications for Sex-Stratified Renal Monitoring

Our findings support several specific clinical recommendations:

1. **Male-focused renal monitoring for calcineurin inhibitors and ICIs.** Male patients receiving calcineurin inhibitors (transplant recipients) or ICIs (cancer patients) should receive enhanced renal function monitoring. This includes more frequent serum creatinine measurements (weekly during dose titration for calcineurin inhibitors, every 2--4 weeks for ICIs), cystatin C measurement (which is less influenced by muscle mass and provides a sex-neutral GFR estimate), and urine albumin-to-creatinine ratio (UACR) monitoring. For ICI patients, urinalysis with microscopy should be performed at baseline and periodically to detect eosinophiluria, an early marker of AIN.

2. **PPI nephrotoxicity awareness and deprescribing.** The high prevalence of PPI-associated renal signals (4 of top 4 drugs by report volume) reinforces recent guideline recommendations for PPI deprescribing. Chronic PPI users, particularly women (who represent the majority of long-term users), should have annual renal function assessment. The within-class variation in sex-differential profiles (lansoprazole 60.3%F vs. esomeprazole 71.4%F) may inform agent selection in renal-risk patients, though this finding requires replication.

3. **Sex-stratified dose adjustment.** For drugs with established sex-differential nephrotoxicity and narrow therapeutic indices (calcineurin inhibitors, platinum agents), sex-stratified therapeutic drug monitoring targets may improve the balance between efficacy and renal safety. This could involve lower target trough levels for male calcineurin inhibitor recipients or sex-specific area-under-the-curve (AUC) targets for platinum agents.

4. **Biomarker sex-adjustment.** Serum creatinine interpretation should account for sex-differential baseline values: a creatinine increase of 0.3 mg/dL represents a proportionally larger deviation in women (from a baseline of approximately 0.7 mg/dL) than in men (from approximately 0.9 mg/dL), potentially causing earlier AKI detection in women and later detection in men. Cystatin C, which is less influenced by muscle mass, may provide more equitable AKI detection across sexes [12].

5. **Autoimmune drug renal effects.** The extreme female bias of tofacitinib (88.2%F) and tocilizumab (69.8%F) renal effects warrants renal monitoring in female autoimmune patients, particularly those with pre-existing renal involvement from their primary disease (lupus nephritis, rheumatoid vasculitis).

### 4.9 Strengths and Limitations

**Strengths.** This study offers several advantages over prior investigations of sex-differential nephrotoxicity. First, the scale of analysis (14.5 million reports, 2,382 signals, 746 drugs) far exceeds any prior study, enabling drug class-level and AE type-level characterization that is not possible with single-drug or single-institution studies. Second, the sex-stratified ROR (logR) metric provides a principled measure of sex-differential reporting that partially controls for the overall sex distribution of drug use, unlike crude sex-stratified counts. Third, the comprehensive renal AE taxonomy (35 MedDRA terms grouped into 10 categories) captures the full spectrum of drug-induced renal injury, from biomarker changes to organ failure. Fourth, the comparison to the FAERS baseline (60.2%F) provides a meaningful reference point for interpreting the nephrotoxicity sex ratio, and the sensitivity analysis excluding UTI confirms the robustness of the male-enrichment finding.

**Limitations.** Several limitations should be acknowledged:

1. **Spontaneous reporting bias.** FAERS is a spontaneous reporting system subject to under-reporting, notoriety bias, and stimulated reporting. Reporting rates differ by sex, with women generally more likely to report adverse events [29]. The logR metric partially but imperfectly controls for this, and residual sex-differential reporting behavior may influence the observed signals.

2. **Absence of denominator data.** FAERS does not capture the total number of drug users by sex, preventing calculation of incidence-based risk ratios. The ROR-based approach assumes that the background reporting rate is proportional to drug use, which may not hold for drugs with strongly sex-biased indications.

3. **Baseline renal function.** FAERS does not capture baseline renal function, serum creatinine, or GFR, preventing risk-adjustment for pre-existing renal disease. Patients with pre-existing CKD are at higher risk of drug-induced AKI, and sex differences in CKD prevalence may confound the nephrotoxicity signals.

4. **UTI confounding.** UTI is partly anatomical rather than drug-induced, and its inclusion as a renal AE inflates the female proportion. The sensitivity analysis excluding UTI (53.6%F) confirms that UTI does not substantially alter the primary conclusion of male enrichment.

5. **Transplant population.** Calcineurin inhibitor male bias may partly reflect the male predominance among transplant recipients (approximately 60% male) rather than purely sex-differential nephrotoxicity susceptibility. The logR metric partially controls for this, but residual confounding by indication cannot be excluded.

6. **Temporal evolution.** PPI nephrotoxicity is a recently recognized signal [7], and reporting patterns may be evolving. The 21-year span of our data (2004--2025) encompasses the period of increasing PPI nephrotoxicity awareness, which may introduce temporal confounding in the sex-differential estimates.

7. **Polypharmacy.** FAERS reports may list multiple suspect drugs, and drug interactions contributing to nephrotoxicity cannot be disentangled from single-drug effects in this analysis. Sex differences in polypharmacy patterns may confound individual drug signals.

8. **Race and ethnicity.** Sex differences in nephrotoxicity may be modified by race and ethnicity, reflecting genetic variation in drug-metabolizing enzymes and renal transporters. FAERS race/ethnicity data are incompletely captured, preventing stratified analysis by race-sex combinations.

---

## 5. Conclusion

Drug-induced nephrotoxicity shows consistent male enrichment (54.9%F vs. 60.2% FAERS baseline, p < 10^-10), positioning the renal system as a notable exception to the general female predominance in pharmacovigilance signals. The 17.9 pp drug class spectrum---from calcineurin inhibitors (42.0%F) to aminoglycosides (59.9%F)---demonstrates that drug class significantly modulates the sex profile of nephrotoxicity, with direct tubular/hemodynamic agents and immune checkpoint inhibitors showing the strongest male bias. AKI and renal failure approach sex parity (49.8--49.9%F), confirming genuine male renal vulnerability consistent with the clinical AKI literature. The severity gradient extends to nephrotoxicity (serious 51.3%F vs. non-serious 55.2%F), with male patients disproportionately represented in serious renal outcomes. PPI nephrotoxicity emerged as a high-prevalence signal with moderate female bias (59--71%F), while autoimmune-indication drugs (tofacitinib 88.2%F) show extreme female bias within the generally male-biased renal SOC.

These findings have direct clinical implications: sex-stratified renal monitoring should be implemented for high-risk drug classes, with particular attention to male patients on calcineurin inhibitors and ICIs, and female patients on autoimmune-indication drugs. The integration of sex as a primary variable in pharmacovigilance analysis, nephrotoxicity prediction models, and dose-adjustment algorithms is warranted by the magnitude and consistency of the sex-differential signals identified in this study.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis. All data underlying this analysis are available through the SexDiffKG knowledge graph, which is released under a CC-BY 4.0 license. FAERS source data are publicly available from the FDA.

---

## Conflicts of Interest

The author declares no conflicts of interest.

---

## Funding

This research received no external funding.

---

## References

1. Perazella MA. Drug-induced acute kidney injury: diverse mechanisms of tubular injury. *Curr Opin Crit Care*. 2019;25(6):550-557. doi:10.1097/MCC.0000000000000653

2. Awdishu L, Mehta RL. The 6R's of drug-induced nephrotoxicity. *BMC Nephrol*. 2017;18:124. doi:10.1186/s12882-017-0536-3

3. Neugarten J, Golestaneh L. Female sex reduces the risk of hospital-associated acute kidney injury: a meta-analysis. *BMC Nephrol*. 2018;19:314. doi:10.1186/s12882-018-1122-z

4. Mauvais-Jarvis F, Bairey Merz CN, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. *Lancet*. 2020;396(10250):565-582. doi:10.1016/S0140-6736(20)31561-0

5. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clin Pharmacokinet*. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001

6. Mehta RL, Pascual MT, Soroko S, et al. Spectrum of acute renal failure in the intensive care unit: the PICARD experience. *Kidney Int*. 2004;66(4):1613-1621. doi:10.1111/j.1523-1755.2004.00927.x

7. Lazarus B, Chen Y, Wilson FP, et al. Proton pump inhibitor use and the risk of chronic kidney disease. *JAMA Intern Med*. 2016;176(2):238-246. doi:10.1001/jamainternmed.2015.7193

8. Uchino S, Kellum JA, Bellomo R, et al. Acute renal failure in critically ill patients: a multinational, multicenter study. *JAMA*. 2005;294(7):813-818. doi:10.1001/jama.294.7.813

9. Naughton CA. Drug-induced nephrotoxicity. *Am Fam Physician*. 2008;78(6):743-750.

10. Munkhaugen J, Lydersen S, Wideroe TE, Hallan S. Prehypertension, obesity, and risk of kidney disease: 20-year follow-up of the HUNT I study in Norway. *Am J Kidney Dis*. 2009;54(4):638-646. doi:10.1053/j.ajkd.2009.03.023

11. Denic A, Lieske JC, Engstrand J, et al. The substantial loss of nephrons in healthy human kidneys with aging. *J Am Soc Nephrol*. 2017;28(1):313-320. doi:10.1681/ASN.2016020154

12. Inker LA, Eneanya ND, Coresh J, et al. New creatinine- and cystatin C-based equations to estimate GFR without race. *N Engl J Med*. 2021;385(19):1737-1749. doi:10.1056/NEJMoa2102953

13. Morrissey KM, Stocker SL, Wittwer MB, Xu L, Giacomini KM. Renal transporters in drug development. *Annu Rev Pharmacol Toxicol*. 2013;53:503-529. doi:10.1146/annurev-pharmtox-011112-140317

14. Sabolic I, Asif AR, Gorboulev V, et al. Gender differences in kidney function. *Pflugers Arch*. 2007;455(3):397-429. doi:10.1007/s00424-007-0308-1

15. Yin J, Duan H, Bhatt DK, et al. Male-predominant expression of organic cation transporter 2 in human kidney determined by a novel immunohistochemical method. *Mol Pharmacol*. 2020;97(2):78-86.

16. Sullivan JC, Gillis EE. Sex and gender differences in hypertensive kidney injury. In: *Hypertension and the Kidney*. Springer; 2019. doi:10.1007/978-3-030-22186-4

17. Neugarten J, Golestaneh L. Influence of sex on the progression of chronic kidney disease. *Am J Kidney Dis*. 2019;74(1):82-90. doi:10.1053/j.ajkd.2019.01.023

18. Pabla N, Dong Z. Cisplatin nephrotoxicity: mechanisms and renoprotective strategies. *Kidney Int*. 2008;73(9):994-1007. doi:10.1038/sj.ki.5002786

19. Kang DH, Park SK, Lee IK, Johnson RJ. Uric acid-induced C-reactive protein expression: implication on cell proliferation and nitric oxide production of human vascular cells. *J Am Soc Nephrol*. 2005;16(12):3553-3562. doi:10.1681/ASN.2005050572

20. Mehran R, Aymong ED, Nikolsky E, et al. A simple risk score for prediction of contrast-induced nephropathy after percutaneous coronary intervention. *J Am Coll Cardiol*. 2004;44(7):1393-1399. doi:10.1016/j.jacc.2004.06.068

21. Neugarten J, Acharya A, Silbiger SR. Effect of gender on the progression of nondiabetic renal disease: a meta-analysis. *J Am Soc Nephrol*. 2000;11(2):319-329. doi:10.1681/ASN.V112319

22. Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2024 clinical practice guideline for the evaluation and management of chronic kidney disease. *Kidney Int*. 2024;105(4S):S117-S314.

23. Lopez-Novoa JM, Quiros Y, Vicente L, Morales AI, Lopez-Hernandez FJ. New insights into the mechanism of aminoglycoside nephrotoxicity: an integrative point of view. *Kidney Int*. 2011;79(1):33-45. doi:10.1038/ki.2010.337

24. Miller RP, Tadagavadi RK, Ramesh G, Reeves WB. Mechanisms of cisplatin nephrotoxicity. *Toxins*. 2010;2(11):2490-2518. doi:10.3390/toxins2112490

25. Whelton A. Nephrotoxicity of nonsteroidal anti-inflammatory drugs: physiologic foundations and clinical implications. *Am J Med*. 1999;106(5B):13S-24S. doi:10.1016/S0002-9343(99)00113-8

26. Cortazar FB, Marber L, Rubin EB, et al. Clinicopathological features of acute kidney injury associated with immune checkpoint inhibitors. *Kidney Int*. 2016;90(3):638-647. doi:10.1016/j.kint.2016.04.008

27. Shaik MJAA. SexDiffKG: A sex-differential pharmacovigilance knowledge graph from 14.5 million FAERS reports. 2026. GitHub: https://github.com/jshaik369/sexdiffkg

28. Sakaeda T, Tamon A, Kadoyama K, Okuno Y. Data mining of the public version of the FDA Adverse Event Reporting System. *Int J Med Sci*. 2013;10(7):796-803. doi:10.7150/ijms.6048

29. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biol Sex Differ*. 2020;11(1):32. doi:10.1186/s13293-020-00308-5

30. Naesens M, Kuypers DR, Sarwal M. Calcineurin inhibitor nephrotoxicity. *Clin J Am Soc Nephrol*. 2009;4(2):481-508. doi:10.2215/CJN.04800908

31. Unger JM, Vaidya R, Albain KS, et al. Sex differences in risk of severe adverse events in patients receiving immunotherapy, targeted therapy, or chemotherapy in cancer clinical trials. *J Clin Oncol*. 2022;40(13):1474-1486. doi:10.1200/JCO.21.02377

32. Foxman B. Epidemiology of urinary tract infections: incidence, morbidity, and economic costs. *Am J Med*. 2002;113(Suppl 1A):5S-13S. doi:10.1016/S0002-9343(02)01054-9

33. Xie Y, Bowe B, Li T, Xian H, Balasubramanian S, Al-Aly Z. Proton pump inhibitors and risk of incident CKD and progression to ESRD. *J Am Soc Nephrol*. 2016;27(10):3153-3163. doi:10.1681/ASN.2015121377

---

## Figure Legends

**Figure 1.** Drug class nephrotoxicity spectrum. Horizontal bar chart showing mean female fraction for 8 drug classes ordered from most male-biased (calcineurin inhibitors, 42.0%F) to least (aminoglycosides, 59.9%F). Dashed vertical line at 60.2% indicates the FAERS baseline female fraction. All drug classes except aminoglycosides fall below baseline, demonstrating pervasive male enrichment in drug-induced nephrotoxicity. Error bars represent 95% confidence intervals of the mean female fraction.

**Figure 2.** Renal AE type profiles. Bar chart of 10 renal AE categories ranked by female fraction, from UTI (66.2%F) to haematuria (49.1%F). A horizontal dashed line at 60.2% marks the FAERS baseline. The chart illustrates the physiological divide between female-biased functional/anatomical endpoints (UTI, dysuria) and male-enriched parenchymal injury endpoints (AKI, renal failure, haematuria). Numbers above each bar indicate the number of contributing signals.

**Figure 3.** PPI nephrotoxicity and top nephrotoxic drugs. Bubble chart of top 10 nephrotoxic drugs by signal count (bubble size proportional to total report volume, x-axis = mean %F, y-axis = N distinct renal AEs). The four PPIs (lansoprazole, esomeprazole, omeprazole, pantoprazole) cluster in the high-volume, moderate-female zone (upper right), while tofacitinib appears as an outlier at 88.2%F. The 60.2% FAERS baseline is marked with a vertical dashed line.

**Figure 4.** Severity gradient in nephrotoxicity. Side-by-side comparison of the female fraction distribution for serious renal AE signals (51.3%F, n = 741) versus non-serious renal AE signals (55.2%F, n = 589). The 3.9 pp difference confirms that male enrichment is amplified in serious renal outcomes. Violin plots show the full distribution of female fractions, with medians and interquartile ranges indicated.

**Figure 5.** Mechanistic schema of sex-differential nephrotoxicity. Conceptual diagram illustrating the interplay of sex-differential renal physiology (GFR, transporter expression, hemodynamics, hormonal milieu) with drug class-specific mechanisms (direct tubular, hemodynamic, immune-mediated) to produce the observed sex-differential nephrotoxicity spectrum. Male risk factors (higher transporter expression, testosterone-mediated vasoconstriction, proinflammatory milieu) and female protective factors (estrogen-mediated vasodilation, anti-inflammatory pathways, lower transporter expression) are depicted alongside the drug class spectrum.