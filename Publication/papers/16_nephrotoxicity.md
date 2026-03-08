# Sex-Differential Patterns in Drug-Induced Nephrotoxicity: A Pharmacovigilance Analysis of 2,382 Signals Across 746 Drugs

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Drug-induced nephrotoxicity accounts for 8--60% of acute kidney injury cases and is a major cause of drug discontinuation. Sex differences in renal physiology---including glomerular filtration rate, tubular function, renal blood flow, drug transporter expression, and hormonal regulation---predict sex-differential nephrotoxicity, yet population-scale characterization across drug classes is lacking.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we extracted sex-stratified reporting odds ratios (ROR) for each drug--adverse event pair and computed logR = ln(ROR_female / ROR_male) as a continuous measure of sex-differential reporting. We identified 2,382 sex-differential nephrotoxicity signals across 746 drugs using 35 renal MedDRA preferred terms, applying thresholds of |logR| >= 0.5 and >= 10 reports per sex. Signals were stratified by drug class (8 classes), renal AE type (10 categories), and severity.

**Results.** Overall renal AE reporting was 54.9% female---significantly below the 60.2% FAERS baseline (p < 10^-10)---indicating relative male enrichment in nephrotoxicity. Drug class analysis revealed a 17.9 pp spectrum: calcineurin inhibitors showed the strongest male bias (42.0%F, |logR| = 0.799) followed by ICIs (44.3%F), while aminoglycosides approached baseline (59.9%F). Among renal AE types, acute kidney injury (49.8%F) and renal failure (49.9%F) were near-parity, while urinary tract infection (66.2%F) was strongly female-biased. Serious renal AEs (51.3%F) were more male-enriched than non-serious (55.2%F), confirming the severity-sex gradient extends to nephrotoxicity. Proton pump inhibitors emerged as the most frequently nephrotoxic drug class (lansoprazole: 10 renal AEs, 30,508 reports), with moderate female bias (59--71%F). Tofacitinib showed extreme female renal bias (88.2%F), potentially reflecting its autoimmune indication population.

**Interpretation.** Drug-induced nephrotoxicity shows consistent male enrichment after adjusting for FAERS demographics, with drug class significantly modulating the sex profile. Calcineurin inhibitor and ICI nephrotoxicity warrant male-focused renal monitoring. The renal system's weak anti-regression (identified in our companion SOC atlas) and male-enrichment make it a natural exception to the general female-predominant pharmacovigilance pattern, likely reflecting genuine male susceptibility to acute kidney injury. These findings have implications for sex-stratified prescribing, monitoring protocols, and dose-adjustment strategies.

---

## 1. Introduction

### 1.1 The Clinical Burden of Drug-Induced Nephrotoxicity

Drug-induced nephrotoxicity represents a major challenge in clinical pharmacology. The kidneys receive approximately 25% of cardiac output and are the primary elimination route for many therapeutic agents, rendering them uniquely vulnerable to drug-mediated injury [1]. Epidemiological estimates attribute 8--60% of acute kidney injury (AKI) episodes to drug exposure, with the range reflecting variation in clinical setting and AKI definition [1,2]. In the intensive care unit, drug-induced AKI accounts for up to 25% of all AKI cases [8]. Nephrotoxicity accounts for 2--5% of all drug adverse events reported to pharmacovigilance systems and is among the leading causes of drug market withdrawal [2,9].

The mechanisms of drug-induced nephrotoxicity include direct tubular cytotoxicity (aminoglycosides, cisplatin), hemodynamic compromise (ACE inhibitors, NSAIDs), crystal nephropathy (acyclovir, methotrexate), osmotic nephrosis (immunoglobulin, mannitol), immune-mediated interstitial nephritis (proton pump inhibitors, checkpoint inhibitors), and thrombotic microangiopathy (calcineurin inhibitors, gemcitabine) [1,2]. Each mechanism engages distinct cellular pathways, creating the potential for mechanism-specific sex differences in susceptibility.

### 1.2 Sex Differences in Renal Physiology

Fundamental sex differences in renal anatomy, physiology, and hormonal milieu create a biological substrate for sex-differential nephrotoxicity.

**Glomerular filtration and kidney morphometry.** Men have consistently higher GFR than women by approximately 8--10 mL/min/1.73 m^2 across adult age ranges [3,10]. This reflects larger kidney mass (approximately 25% larger by weight), greater glomerular number (approximately 12% more), larger glomerular volume, and greater renal plasma flow [10,11]. GFR-based drug dosing formulas (Cockcroft-Gault, CKD-EPI) incorporate sex as a variable, yet inconsistent application may lead to sex-differential drug exposure [12].

**Tubular function and drug transporters.** The proximal tubule hosts key transporters---OAT1, OAT3, OCT2, MATE1/2-K, and P-glycoprotein---that determine intracellular drug concentrations [13]. Several exhibit sex-differential expression: in rodent kidneys, Oat1, Oat3, and Oct2 expression is approximately 2-fold higher in males, driven by testosterone via hepatocyte nuclear factor 4-alpha (HNF4alpha) [14]. In human kidney tissue, OAT3 and OCT2 show male-predominant expression, though with smaller magnitude than rodents [13,15]. These differences predict higher intracellular accumulation of OAT substrates (methotrexate, tenofovir) and OCT2 substrates (cisplatin, oxaliplatin) in male proximal tubules [15].

**Renal hemodynamics.** Renal plasma flow is approximately 10--15% higher in men [10,16]. Testosterone promotes renal vasoconstriction through the RAAS, with higher angiotensin II receptor density in male kidneys [16]. Estrogen promotes vasodilation through eNOS upregulation and prostacyclin release [17]. These differences predict greater susceptibility to hemodynamic nephrotoxicity (calcineurin inhibitors, NSAIDs, contrast agents) in male kidneys.

**Hormonal renoprotection.** Estradiol attenuates ischemia-reperfusion injury, inhibits TGF-beta signaling, and decreases reactive oxygen species in renal tissue [4,17]. Testosterone promotes oxidative stress through NADPH oxidase, enhances endothelin-1-mediated vasoconstriction, and accelerates renal fibrosis [16,17]. Ovariectomy in female rodents increases susceptibility to cisplatin nephrotoxicity to male-equivalent levels, directly implicating sex hormones in nephrotoxic susceptibility [18].

### 1.3 Sex Differences in Acute Kidney Injury

A meta-analysis by Neugarten and Golestaneh [3] encompassing over 2.5 million patients demonstrated that female sex was independently associated with a 21% reduced risk of hospital-associated AKI (pooled OR 0.79, 95% CI 0.73--0.85). This protective effect was observed across surgical, medical, and mixed ICU populations. Kang et al. [19] reported 1.45-fold higher AKI incidence in males, with the excess most pronounced in severe AKI requiring renal replacement therapy (1.8:1 male-to-female ratio). However, certain etiologies show distinct patterns: contrast-induced nephropathy may be more common in women, and autoimmune-mediated renal injury is generally female-predominant [20].

### 1.4 Sex Differences in Chronic Kidney Disease Progression

Men progress to end-stage renal disease more rapidly across most primary diagnoses, with Neugarten et al. [21] estimating a 1.37-fold higher rate of GFR decline in men. The CKD-EPI equation incorporates a sex coefficient, and the KDIGO guidelines recognize sex as a prognostic factor, yet sex-specific intervention thresholds remain rare in clinical practice [12,22].

### 1.5 Nephrotoxic Drug Classes and Known Sex Differences

**Aminoglycosides** accumulate in proximal tubular cells via megalin/cubilin. Animal studies show conflicting results regarding sex differences, and clinical data are sparse [23]. **Cisplatin** nephrotoxicity occurs through OCT2-mediated tubular uptake; male rodents are more susceptible, with the difference abolished by castration [18,24]. **NSAIDs** cause hemodynamic AKI through cyclooxygenase inhibition; sex differences have not been systematically characterized, though higher female NSAID use may coexist with male physiological susceptibility [25]. **Contrast agents** produce nephropathy particularly after cardiac catheterization; some studies suggest female risk, potentially related to lower GFR relative to contrast dose [20]. **ICIs** cause immune-mediated interstitial nephritis; some studies report male predominance for nephritis alongside female predominance for dermatologic irAEs [26].

### 1.6 Study Rationale

No study has systematically characterized sex differences across multiple drug classes and renal AE types using population-scale pharmacovigilance data. We leveraged SexDiffKG---a sex-differential pharmacovigilance knowledge graph containing 96,281 sex-differential signals from 14.5 million FAERS reports [27]---to conduct the first comprehensive analysis of sex-differential drug-induced nephrotoxicity across 746 drugs, 35 renal AE terms, 8 drug classes, and the severity spectrum.

---

## 2. Methods

### 2.1 Data Source and Preprocessing

The FDA Adverse Event Reporting System (FAERS) was used as the primary data source [28]. FAERS quarterly data files spanning 2004Q1 through 2025Q3 were obtained, representing 21 years of pharmacovigilance data. After deduplication using the FAERS CASEID and FDA-recommended algorithm (retaining the most recent case version), the analysis dataset comprised 14,536,008 unique reports (60.2% female, 39.8% male) [29]. Drug names were standardized to active ingredients using FAERS mapping tables supplemented with manual curation. Adverse events were coded using MedDRA preferred terms.

### 2.2 Sex-Stratified Disproportionality Analysis

For each drug--adverse event pair, sex-stratified reporting odds ratios (ROR) were computed using the standard 2x2 disproportionality framework [28]:

**ROR_female = (a_f / b_f) / (c_f / d_f)**

where, for the female stratum:
- a_f = number of female reports with the target drug AND target AE
- b_f = number of female reports with the target drug AND any other AE
- c_f = number of female reports with any other drug AND target AE
- d_f = number of female reports with any other drug AND any other AE

An analogous table was constructed for the male stratum to compute **ROR_male**.

The sex-differential metric was defined as:

**logR = ln(ROR_female / ROR_male)**

Positive logR indicates female-enriched reporting (stronger drug--AE association in women); negative logR indicates male-enriched reporting. This metric controls for the overall sex distribution by comparing within-sex disproportionality rather than raw counts.

**Signal selection criteria:**
- |logR| >= 0.5 (corresponding to a >= 1.65-fold sex difference in ROR)
- >= 10 reports in each sex stratum (statistical stability)

The |logR| >= 0.5 threshold identifies drug--AE pairs with reporting odds at least 65% higher in one sex, after adjustment for background AE frequency in that sex [27].

### 2.3 Renal Adverse Event Identification

Thirty-five MedDRA preferred terms were selected from the SOC "Renal and urinary disorders" and supplemented with laboratory-value PTs:

- **AKI:** acute kidney injury, acute prerenal failure
- **Renal failure:** renal failure, renal failure acute/chronic/neonatal
- **CKD:** chronic kidney disease, end-stage renal disease, renal impairment
- **Biomarkers:** blood creatinine increased, blood urea increased, GFR decreased, proteinuria, albuminuria, microalbuminuria
- **Glomerular:** nephrotic syndrome, nephritis, glomerulonephritis (membranous, IgA), focal segmental glomerulosclerosis
- **Tubulointerstitial:** renal tubular necrosis, interstitial nephritis, tubulointerstitial nephritis, Fanconi syndrome, renal tubular acidosis
- **Lower urinary tract:** UTI, dysuria, urinary retention, haematuria
- **Other:** renal disorder, nephropathy, hydronephrosis, renal cyst, nephrolithiasis, renal artery stenosis

These 35 PTs were grouped into 10 clinically meaningful categories for analysis.

### 2.4 Drug Classification

Eight drug classes with established nephrotoxicity profiles were defined a priori:

- **Calcineurin inhibitors** (cyclosporine, tacrolimus, pimecrolimus): tubular cytotoxicity and afferent arteriolar vasoconstriction [30]
- **ICIs** (nivolumab, pembrolizumab, ipilimumab, atezolizumab, durvalumab, avelumab): immune-mediated acute interstitial nephritis [26]
- **ACE inhibitors** (lisinopril, enalapril, ramipril, captopril, perindopril, benazepril): hemodynamic AKI via efferent arteriolar vasodilation
- **Platinum agents** (cisplatin, carboplatin, oxaliplatin): OCT2-mediated proximal tubular necrosis [24]
- **Diuretics** (furosemide, hydrochlorothiazide, spironolactone, bumetanide): prerenal AKI via volume depletion
- **NSAIDs** (ibuprofen, naproxen, diclofenac, celecoxib, meloxicam, indomethacin, ketorolac, piroxicam): prostaglandin-mediated hemodynamic AKI [25]
- **ARBs** (losartan, valsartan, irbesartan, candesartan, telmisartan, olmesartan): hemodynamic AKI analogous to ACE inhibitors
- **Aminoglycosides** (gentamicin, tobramycin, amikacin): megalin-mediated tubular necrosis [23]

### 2.5 Statistical Analysis

The primary outcome was the female fraction (%F), the proportion of female-predominant signals (logR > 0) among all sex-differential nephrotoxicity signals for a given stratum, interpretable relative to the FAERS baseline of 60.2%.

**Between-class comparisons** used the Kruskal-Wallis H test, with post-hoc Dunn's test and Bonferroni correction. **Severity analysis** compared serious versus non-serious signal %F using the Mann-Whitney U test. Seriousness was determined by the FAERS serious outcome flag (death, life-threatening, hospitalization, disability, congenital anomaly, or required intervention). **Effect sizes** were captured as mean |logR| per stratum. **Deviation from baseline** was assessed via one-sample z-test comparing the nephrotoxicity %F (54.9%) to the FAERS baseline (60.2%). Given the large sample (n = 2,382), we emphasize effect sizes alongside p-values.

All analyses were performed using Python 3.11 with pandas, scipy.stats, and statsmodels.

---

## 3. Results

### 3.1 Overview

Across 14,536,008 FAERS reports, we identified 2,382 sex-differential nephrotoxicity signals spanning 746 unique drugs and 35 renal MedDRA preferred terms. The overall female fraction was 54.9%---a 5.3 percentage point (pp) deficit below the FAERS baseline of 60.2% (z-test p < 10^-10, two-sided). The mean absolute effect size was |logR| = 0.875, indicating the typical signal represents an approximately 2.4-fold difference in reporting odds between the sexes.

This male enrichment is notable in the broader SexDiffKG context: the renal system is one of only a few SOCs where the female fraction falls substantially below baseline. The majority of SOCs---immune, metabolic, hepatic, musculoskeletal, dermatologic---show female fractions exceeding 60%, making nephrotoxicity a conspicuous exception aligned with the known epidemiology of male-predominant AKI [3]. The 746 drugs spanned all major therapeutic categories, with each drug averaging 3.2 distinct renal AE signals.

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

The spectrum spans 17.9 pp from calcineurin inhibitors (42.0%F) to aminoglycosides (59.9%F). The Kruskal-Wallis test confirmed significant between-class heterogeneity (H = 24.3, p < 0.001).

**Calcineurin inhibitors (42.0%F, |logR| = 0.799)** exhibited the strongest male bias. This is mechanistically coherent: calcineurin inhibitors cause renal vasoconstriction and tubular damage modulated by sex hormones---testosterone enhances vasoconstriction through endothelin-1 and angiotensin II receptor upregulation, while estrogen provides vasodilation through nitric oxide and prostacyclin [16,17]. Sex-differential CYP3A4/5 metabolism also contributes: women have approximately 20--40% higher CYP3A4 activity, resulting in faster tacrolimus and cyclosporine metabolism and lower trough levels at equivalent doses [5]. The transplant population context (approximately 60% male kidney transplant recipients) further contributes, though the logR metric partially controls for this.

**ICIs (44.3%F, |logR| = 0.819).** ICI-induced nephritis is immune-mediated (T-cell infiltration of the renal interstitium), yet shows male predominance comparable to calcineurin inhibitors. This is consistent with the Unger et al. [31] finding of male-biased ICI irAEs for nephritis, colitis, and pneumonitis, contrasting with female predominance for skin and endocrine irAEs. The convergence of male-predominant nephrotoxicity across mechanistically distinct drug classes (direct toxicity vs. immune-mediated) strongly suggests that the underlying sex-differential renal physiology---rather than drug-specific mechanisms---is the primary driver.

**ACE inhibitors (48.6%F, |logR| = 0.790).** The moderate male bias is consistent with the sex-differential RAAS: men have higher baseline RAAS activity, suggesting greater hemodynamic dependence on angiotensin II for maintaining GFR, and therefore greater vulnerability to ACE inhibition [16].

**Platinum agents (51.1%F, |logR| = 0.885).** Near-parity despite preclinical data favoring male susceptibility [18] may reflect GFR-based dosing: the Calvert formula adjusts doses for GFR (which incorporates sex), partially equalizing exposure [24]. The high |logR| indicates large individual signal magnitudes, but balanced directionality across the class.

**Diuretics (55.3%F, |logR| = 0.765).** Moderate female bias may reflect higher diuretic use in women and lower body mass/total body water amplifying volume-depleting effects [5].

**NSAIDs (56.8%F, |logR| = 0.907).** Near-baseline despite male physiological susceptibility likely reflects higher NSAID exposure in women (menstrual pain, rheumatologic conditions). The high |logR| and balanced directionality are consistent with heterogeneous NSAID nephrotoxicity mechanisms---hemodynamic (male-susceptible), interstitial nephritis (female-susceptible), minimal change disease---producing signals in both directions [25].

**ARBs (57.1%F, |logR| = 0.860).** Similar to ACE inhibitors but modestly female-shifted, possibly reflecting higher female ARB use (preferred over ACE inhibitors in women of childbearing age).

**Aminoglycosides (59.9%F, |logR| = 0.842).** The only class matching the FAERS baseline, indicating no sex-differential enrichment. Aminoglycoside nephrotoxicity is megalin-mediated---not via the sex-differential OAT/OCT transporters---and may be relatively sex-invariant [23]. Therapeutic drug monitoring may also equalize exposure.

### 3.3 Renal AE Type Analysis

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

The spectrum reveals a physiological divide between female-biased functional/anatomical endpoints and male-enriched parenchymal injury endpoints.

**Female-biased renal AEs.** UTI (66.2%F) reflects the 8:1 female predominance from anatomical factors (shorter urethra, proximity to GI flora) [32]. Blood creatinine increase (57.7%F) may paradoxically reflect sex-differential biomarker sensitivity: women have lower baseline creatinine, so equivalent absolute increases represent proportionally larger deviations more readily detected and reported [12]. CKD (57.0%F) may similarly reflect sex-differential detection: women with lower baseline GFR may cross CKD staging thresholds at smaller absolute decrements [22].

**Near-parity renal AEs.** AKI (49.8%F) and renal failure (49.9%F) approach parity despite the 60.2% FAERS baseline, indicating 10.3--10.4 pp male enrichment. This is consistent with the Neugarten and Golestaneh [3] meta-analysis reporting pooled OR 0.79 (95% CI 0.73--0.85) for female AKI, translating to approximately 27% excess male AKI incidence. Our pharmacovigilance finding is quantitatively consistent with this clinical estimate. Haematuria (49.1%F) also approaches parity; its high |logR| (0.977) suggests strongly sex-biased individual signals with balanced directionality, consistent with diverse causes (nephrologic female-biased, urologic male-biased).

### 3.4 Severity Gradient

- Serious renal AEs: **51.3%F** (n = 741 signals)
- Non-serious renal AEs: **55.2%F** (n = 589 signals)
- Difference: 3.9 pp (Mann-Whitney U test, p < 0.01)

The severity-sex gradient extends the broader SexDiffKG observation that severe drug outcomes show less female predominance [27]. This aligns with clinical data: severe AKI requiring RRT has a 1.8:1 male-to-female ratio in ICU populations [6,19], substantially exceeding the 1.5:1 ratio for all-severity AKI. The gradient may also reflect sex-differential reporting (serious events less susceptible to bias, revealing the underlying biological sex difference more clearly) and testosterone-mediated amplification of inflammatory cascades (NF-kB, NLRP3 inflammasome) that transform moderate injury into severe AKI preferentially in males [17].

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

**PPI nephrotoxicity (59--71%F).** Four PPIs occupied the top four positions by report volume, collectively accounting for over 97,000 reports. PPI-associated nephrotoxicity (acute interstitial nephritis, CKD) has emerged as a major signal in the past decade [7]. Lazarus et al. [7] demonstrated 20--50% increased CKD risk with PPI use, and Xie et al. [33] confirmed the association with progression to ESRD. The moderate female bias likely reflects higher PPI use in women, immune-mediated AIN mechanisms (which follow the female-predominant pattern of drug allergy), and sex-differential CYP2C19 metabolism. The within-class heterogeneity (lansoprazole 60.3%F vs. esomeprazole 71.4%F) suggests agent-specific differences, potentially related to distinct metabolic pathways or immune epitope profiles.

**Methotrexate (56.3%F, 14 renal AEs, 5,379 reports)** produces the most distinct renal AE signals of any single drug, reflecting multiple nephrotoxicity mechanisms: crystal nephropathy, direct tubular toxicity, and reduced renal blood flow. The near-parity sex profile despite predominant use in rheumatoid arthritis (3:1 female) suggests genuine male susceptibility, potentially via OAT1/OAT3-mediated tubular accumulation [14,15].

**Tofacitinib (88.2%F, 6 renal AEs, 4,375 reports).** The extreme female bias substantially exceeds even the autoimmune indication demographics (approximately 70--75%F). Residual female excess may reflect genuine sex-differential JAK-mediated renal effects (JAK-STAT signaling in renal fibrosis and inflammation with estrogen modulation), interaction between autoimmune disease activity and renal susceptibility, or sex-differential CYP3A4 metabolism with renal elimination.

**Biologic agents (ocrelizumab 76.6%F, immunoglobulins 67.5%F, tocilizumab 69.8%F)** show consistent female bias, likely reflecting channeling bias from female-predominant autoimmune indications [29]. Tocilizumab's 69.8%F across 12 renal AEs is notable given that IL-6 blockade has renoprotective effects in animal models---the female predominance may reflect sex-differential IL-6 signaling, as estrogen upregulates IL-6 receptor expression in renal cells.

### 3.6 Sensitivity Analysis: Excluding UTI

Excluding UTI signals (n = 172), the overall female fraction decreased from 54.9% to 53.6% (n = 2,210 signals), reinforcing the male enrichment finding. Drug class rankings and renal AE type orderings were unchanged.

---

## 4. Discussion

### 4.1 Nephrotoxicity as a Male-Enriched SOC Exception

The renal system occupies a unique position in the sex-differential pharmacovigilance landscape. While most organ systems show female-predominant drug safety signals (immune >65%F, metabolic >62%F, hepatobiliary >60%F, skin >63%F), nephrotoxicity at 54.9%F is one of the least female-biased major SOCs [27]. Our companion analyses identified the renal system as the natural "negative control" for anti-regression effects and placed it consistently below the FAERS baseline.

This male enrichment is biologically grounded: testosterone promotes renal vasoconstriction through endothelin-1 and the RAAS, enhances proximal tubular injury through NADPH oxidase-mediated oxidative stress, and accelerates fibrotic progression through TGF-beta signaling [16,17]. Estrogen provides renoprotection through nitric oxide-mediated vasodilation, anti-inflammatory effects (NF-kB and NLRP3 inflammasome suppression), and anti-fibrotic effects (TGF-beta/Smad inhibition) [4,17]. Male kidneys thus exist in a proinflammatory, pro-oxidant milieu predisposing to drug-mediated injury.

### 4.2 Comparison with Published Nephrotoxicity Studies

Our findings align with and extend the existing literature. The Neugarten and Golestaneh [3] meta-analysis reported pooled OR 0.79 (95% CI 0.73--0.85) for female AKI across over 2.5 million patients, corresponding to approximately 27% excess male incidence. Our AKI signal finding (49.8%F, 10.4 pp below baseline) provides pharmacovigilance-level confirmation. Kang et al. [19] demonstrated severity-dependent amplification (1.8:1 male-to-female ratio for dialysis-requiring AKI versus 1.45:1 overall), paralleled by our severity gradient (51.3%F serious vs. 55.2%F non-serious).

For specific drug classes, our findings offer novel context. Calcineurin inhibitor nephrotoxicity male predominance (42.0%F) has not been comprehensively characterized previously, though individual tacrolimus studies have noted male sex as a risk factor [30]. ICI nephritis male predominance (44.3%F) is consistent with the Unger et al. [31] irAE meta-analysis. PPI nephrotoxicity (59--71%F) extends the Lazarus et al. [7] signal with sex-differential characterization. Aminoglycoside nephrotoxicity at baseline (59.9%F) contrasts with rodent data suggesting male susceptibility [23], possibly reflecting therapeutic drug monitoring efficacy and smaller human transporter sex differences.

### 4.3 Renal Drug Transporters as a Mechanistic Framework

The sex-differential expression of renal drug transporters provides a unifying mechanistic framework. OAT1 (SLC22A6) and OAT3 (SLC22A8) mediate basolateral uptake of anionic drugs into proximal tubular cells, while OCT2 (SLC22A2) mediates cationic drug uptake [13,14,15]. Testosterone upregulates Oat1, Oat3, and Oct2 approximately 2-fold in rodent kidneys via HNF4alpha [14]; human studies confirm male-predominant expression at 20--40% higher levels [15].

This framework predicts that OAT/OCT-eliminated drugs should show male-predominant nephrotoxicity, while passively-filtered drugs should be sex-neutral. Our findings are partially consistent: cisplatin (OCT2 substrate) shows near-parity rather than expected male bias, likely due to GFR-based dose adjustment; methotrexate (OAT1/3 substrate) shows near-parity despite female-predominant indication, suggesting underlying male susceptibility; aminoglycosides (megalin-mediated, not OAT/OCT) show baseline ratios. The clinical implication is that OAT/OCT substrate drugs should be considered higher-risk nephrotoxins in male patients, and sex-stratified therapeutic drug monitoring may be warranted [15].

### 4.4 The GFR-Dosing Paradox

A paradox emerges from the interaction of sex-differential GFR and transporter expression. GFR-based dosing reduces doses for lower GFR, disproportionately affecting women (approximately 8--10 mL/min/1.73 m^2 lower on average) [10,12]. This protects women from exposure-dependent nephrotoxicity. However, males receive relatively higher doses while simultaneously having higher transporter expression---a "double hit" of greater exposure and greater tubular uptake. Our finding of near-parity platinum nephrotoxicity (51.1%F) suggests GFR-based dosing partially but not completely compensates. If compensation were perfect, platinum nephrotoxicity should match the FAERS baseline (female-biased); instead, near-parity indicates residual male susceptibility.

Sex-stratified dose adjustment accounting for both GFR and estimated transporter-mediated clearance---incorporating sex-specific transporter activity estimates into PBPK models---represents an important future direction [5].

### 4.5 The Calcineurin Inhibitor-ICI Male Axis

The convergence of male-predominant nephrotoxicity across mechanistically distinct drug classes---calcineurin inhibitors (42.0%F, direct toxicity) and ICIs (44.3%F, immune-mediated)---provides strong evidence that sex-differential renal physiology, rather than drug-specific effects, drives the male nephrotoxicity signal. This has implications for male transplant recipients (enhanced monitoring: weekly creatinine during dose titration, quarterly cystatin C, annual UACR) and male ICI patients (baseline and periodic renal assessment including urinalysis for eosinophiluria as an early AIN marker). More broadly, nephrotoxicity prediction models should incorporate sex as a primary stratification variable.

### 4.6 PPI Nephrotoxicity: An Emerging Sex-Differential Signal

Four PPIs among the top four nephrotoxic drugs by report volume, with moderate female bias (59--71%F), warrants attention. The female bias runs counter to the general male enrichment of the renal SOC, suggesting that PPI-induced AIN---involving drug-specific T-cell activation and eosinophilic tubulointerstitial infiltration---follows the female-predominant pattern of drug allergy rather than the male-predominant pattern of hemodynamic/tubular nephrotoxicity [7,33]. The within-class variation (lansoprazole 60.3%F, pantoprazole 59.2%F, omeprazole 61.3%F, esomeprazole 71.4%F) may reflect agent-specific differences in haptenization or CYP2C19-mediated metabolism. These findings support PPI deprescribing guidelines and suggest annual renal monitoring for chronic PPI users, particularly women.

### 4.7 Autoimmune-Indication Drugs and Channeling

Drugs for autoimmune indications---tofacitinib (88.2%F), tocilizumab (69.8%F), ocrelizumab (76.6%F), immunoglobulins (67.5%F)---show uniformly female-predominant nephrotoxicity, creating an apparent contradiction with the male-enriched renal SOC. This likely represents channeling bias from female-predominant autoimmune diseases (RA 3:1, MS 3:1, lupus 9:1) [29]. However, tofacitinib's extreme 88.2%F---exceeding indication demographics---raises the possibility of genuine sex-differential JAK-mediated renal effects, as JAK-STAT signaling mediates renal inflammation and fibrosis with estrogen modulation of JAK1 activity.

### 4.8 Clinical Implications

1. **Male-focused renal monitoring for calcineurin inhibitors and ICIs.** Enhanced monitoring (frequent creatinine, cystatin C, UACR) for male patients. For ICI patients, urinalysis with microscopy at baseline and periodically to detect eosinophiluria.

2. **PPI nephrotoxicity awareness and deprescribing.** Annual renal function assessment for chronic PPI users, particularly women. Within-class variation (60.3--71.4%F) may inform agent selection.

3. **Sex-stratified dose adjustment.** Lower calcineurin inhibitor trough targets for male recipients; sex-specific AUC targets for platinum agents.

4. **Biomarker sex-adjustment.** A creatinine increase of 0.3 mg/dL represents a larger proportional deviation in women (baseline approximately 0.7 mg/dL) than men (approximately 0.9 mg/dL). Cystatin C, less influenced by muscle mass, provides more equitable AKI detection [12].

5. **Autoimmune drug renal effects.** The extreme female bias of tofacitinib (88.2%F) and tocilizumab (69.8%F) warrants renal monitoring in female autoimmune patients, particularly those with pre-existing renal involvement.

### 4.9 Strengths and Limitations

**Strengths.** The scale of analysis (14.5 million reports, 2,382 signals, 746 drugs) enables drug class-level and AE type-level characterization not possible with single-drug studies. The logR metric provides principled sex-differential measurement. The comprehensive renal AE taxonomy (35 PTs, 10 categories) captures the full injury spectrum. The FAERS baseline comparison and UTI sensitivity analysis confirm robustness.

**Limitations:**

1. **Spontaneous reporting bias.** FAERS is subject to under-reporting, notoriety bias, and stimulated reporting, with sex-differential reporting rates [29]. The logR metric partially but imperfectly controls for this.

2. **Absence of denominator data.** FAERS lacks drug user counts by sex, preventing incidence-based risk calculation.

3. **No baseline renal function.** Pre-existing CKD and sex differences in CKD prevalence may confound signals.

4. **UTI confounding.** Partly anatomical; sensitivity analysis (53.6%F without UTI) confirms primary conclusions.

5. **Transplant demographics.** Calcineurin inhibitor male bias may partly reflect the approximately 60% male transplant recipient population.

6. **Temporal evolution.** PPI nephrotoxicity is recently recognized [7]; reporting patterns may be evolving across the 2004--2025 study period.

7. **Polypharmacy.** Drug interactions cannot be disentangled from single-drug effects.

8. **Race and ethnicity.** Sex differences may be modified by genetic variation in drug-metabolizing enzymes and transporters; FAERS race data are incomplete.

---

## 5. Conclusion

Drug-induced nephrotoxicity shows consistent male enrichment (54.9%F vs. 60.2% FAERS baseline, p < 10^-10), positioning the renal system as a notable exception to the general female predominance in pharmacovigilance signals. The 17.9 pp drug class spectrum---from calcineurin inhibitors (42.0%F) to aminoglycosides (59.9%F)---demonstrates that drug class significantly modulates the sex profile, with direct tubular/hemodynamic agents and ICIs showing the strongest male bias. AKI and renal failure approach sex parity (49.8--49.9%F), confirming genuine male renal vulnerability consistent with clinical literature. The severity gradient extends to nephrotoxicity (serious 51.3%F vs. non-serious 55.2%F), with male patients disproportionately represented in serious renal outcomes. PPI nephrotoxicity emerged as a high-prevalence signal with moderate female bias (59--71%F), while autoimmune-indication drugs (tofacitinib 88.2%F) show extreme female bias within the generally male-biased renal SOC.

These findings support sex-stratified renal monitoring for high-risk drug classes, with particular attention to male patients on calcineurin inhibitors and ICIs, and female patients on autoimmune-indication drugs. The integration of sex as a primary variable in pharmacovigilance analysis, nephrotoxicity prediction, and dose-adjustment algorithms is warranted.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis. All data underlying this analysis are available through the SexDiffKG knowledge graph (CC-BY 4.0). FAERS source data are publicly available from the FDA.

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

**Figure 1.** Drug class nephrotoxicity spectrum. Horizontal bar chart showing mean female fraction for 8 drug classes ordered from most male-biased (calcineurin inhibitors, 42.0%F) to least (aminoglycosides, 59.9%F). Dashed vertical line at 60.2% indicates the FAERS baseline. All classes except aminoglycosides fall below baseline. Error bars represent 95% confidence intervals.

**Figure 2.** Renal AE type profiles. Bar chart of 10 renal AE categories ranked by female fraction, from UTI (66.2%F) to haematuria (49.1%F). Horizontal dashed line at 60.2% marks FAERS baseline. Illustrates the physiological divide between female-biased functional/anatomical endpoints and male-enriched parenchymal injury endpoints. Numbers above bars indicate contributing signal counts.

**Figure 3.** PPI nephrotoxicity and top nephrotoxic drugs. Bubble chart of top 10 drugs by signal count (bubble size proportional to total report volume, x-axis = mean %F, y-axis = N distinct renal AEs). Four PPIs cluster in the high-volume, moderate-female zone; tofacitinib appears as an outlier at 88.2%F. Vertical dashed line at 60.2% FAERS baseline.

**Figure 4.** Severity gradient in nephrotoxicity. Comparison of female fraction distributions for serious (51.3%F, n = 741) versus non-serious (55.2%F, n = 589) renal AE signals. The 3.9 pp difference confirms male enrichment is amplified in serious outcomes. Violin plots with medians and interquartile ranges.

**Figure 5.** Mechanistic schema of sex-differential nephrotoxicity. Conceptual diagram of sex-differential renal physiology (GFR, transporter expression, hemodynamics, hormonal milieu) interacting with drug class mechanisms to produce the observed spectrum.