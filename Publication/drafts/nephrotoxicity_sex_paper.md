# Sex-Differential Patterns in Drug-Induced Nephrotoxicity: A Pharmacovigilance Analysis of 2,382 Signals Across 746 Drugs

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Drug-induced nephrotoxicity accounts for 8--60% of acute kidney injury cases and is a major cause of drug discontinuation. Sex differences in renal physiology---including glomerular filtration rate, tubular function, renal blood flow, and hormonal regulation---predict sex-differential nephrotoxicity, but population-scale characterization across drug classes is lacking.

**Methods.** From 14,536,008 FAERS reports (2004Q1--2025Q3), we identified 2,382 sex-differential nephrotoxicity signals across 746 drugs using 35 renal MedDRA terms. Signals were stratified by drug class (8 classes), renal AE type (10 categories), and severity.

**Results.** Overall renal AE reporting was 54.9% female---significantly below the 60.2% FAERS baseline (p < 10^-10)---indicating relative male enrichment in nephrotoxicity. Drug class analysis revealed a 17.9 pp spectrum: calcineurin inhibitors showed the strongest male bias (42.0%F, |logR| = 0.799) followed by ICIs (44.3%F), while aminoglycosides approached baseline (59.9%F). Among renal AE types, acute kidney injury (49.8%F) and renal failure (49.9%F) were near-parity, while urinary tract infection (66.2%F) was strongly female-biased. Serious renal AEs (51.3%F) were more male-enriched than non-serious (55.2%F), confirming the severity-sex gradient extends to nephrotoxicity. Proton pump inhibitors emerged as the most frequently nephrotoxic drug class (lansoprazole: 10 renal AEs, 30,508 reports), with moderate female bias (59--71%F). Tofacitinib showed extreme female renal bias (88.2%F), potentially reflecting its autoimmune indication population.

**Interpretation.** Drug-induced nephrotoxicity shows consistent male enrichment after adjusting for FAERS demographics, with drug class significantly modulating the sex profile. Calcineurin inhibitor and ICI nephrotoxicity warrant male-focused renal monitoring. The renal system's weak anti-regression (identified in our companion SOC atlas) and male-enrichment make it a natural exception to the general female-predominant pharmacovigilance pattern, likely reflecting genuine male susceptibility to acute kidney injury.

---

## Introduction

Drug-induced nephrotoxicity represents a significant clinical burden: 8--60% of acute kidney injury (AKI) episodes are attributed to drug exposure, and nephrotoxicity accounts for 2--5% of all drug adverse events reported to pharmacovigilance systems [1]. Multiple drug classes---including aminoglycosides, calcineurin inhibitors, platinum chemotherapy, NSAIDs, and checkpoint inhibitors---are established nephrotoxins with distinct mechanisms of renal injury [2].

Sex differences in renal physiology provide a biological foundation for sex-differential nephrotoxicity. Men have higher glomerular filtration rates (GFR), larger kidneys, and greater renal plasma flow, while women have higher rates of autoimmune-mediated renal conditions [3]. Testosterone promotes renal vasoconstriction and oxidative stress, while estrogen provides renoprotective effects through anti-inflammatory and antioxidant pathways [4]. These opposing hormonal effects predict that male drug users may be more susceptible to certain types of renal injury.

Clinical evidence supports this prediction: men experience AKI at approximately 1.5 times the rate of women in hospital settings [3]. However, systematic characterization of sex-differential nephrotoxicity across drug classes and renal AE types using pharmacovigilance data has not been reported.

We leveraged SexDiffKG---containing 96,281 sex-differential signals from 14.5 million FAERS reports---to conduct the first comprehensive analysis of sex-differential drug-induced nephrotoxicity.

---

## Methods

### Data Source

FAERS 2004Q1--2025Q3: 14,536,008 deduplicated reports (60.2% female). Sex-stratified logR = ln(ROR_female / ROR_male). Signals: |logR| >= 0.5, >= 10 reports per sex.

### Renal AE Identification

35 MedDRA preferred terms were used to identify renal adverse events: acute kidney injury, renal failure (acute/chronic), blood creatinine increased, proteinuria, haematuria, nephrotic syndrome, renal impairment, renal disorder, urinary tract infection, urinary retention, dysuria, chronic kidney disease, interstitial nephritis, renal tubular necrosis, glomerulonephritis, and related terms. Terms were grouped into 10 categories for analysis.

### Drug Classification

Eight drug classes with established nephrotoxicity profiles:
- **Calcineurin inhibitors** (cyclosporine, tacrolimus, pimecrolimus): direct tubular and hemodynamic nephrotoxicity
- **ICIs** (nivolumab, pembrolizumab, ipilimumab, atezolizumab, durvalumab, avelumab): immune-mediated interstitial nephritis
- **ACE inhibitors** (lisinopril, enalapril, ramipril, captopril, perindopril, benazepril): hemodynamic AKI
- **Platinum agents** (cisplatin, carboplatin, oxaliplatin): direct tubular toxicity
- **Diuretics** (furosemide, hydrochlorothiazide, spironolactone, bumetanide): volume-mediated prerenal AKI
- **NSAIDs** (ibuprofen, naproxen, diclofenac, celecoxib, meloxicam, indomethacin, ketorolac, piroxicam): prostaglandin-mediated hemodynamic
- **ARBs** (losartan, valsartan, irbesartan, candesartan, telmisartan, olmesartan): hemodynamic AKI
- **Aminoglycosides** (gentamicin, tobramycin, amikacin): direct tubular toxicity

### Statistical Analysis

Female fraction per signal. Drug class means compared via Kruskal-Wallis test. Severity comparison (serious vs. non-serious) via Mann-Whitney U. Effect sizes as mean |logR|.

---

## Results

### Overview

2,382 sex-differential nephrotoxicity signals across 746 drugs. Overall: 54.9% female (5.3 pp below FAERS baseline of 60.2%; p < 10^-10), mean |logR| = 0.875. The male enrichment in nephrotoxicity is consistent with known higher male AKI rates and represents one of the most pronounced male-biased SOC-level findings in SexDiffKG.

### Drug Class Nephrotoxicity Spectrum

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

The spectrum spans 17.9 pp from calcineurin inhibitors (42.0%F) to aminoglycosides (59.9%F).

**Calcineurin inhibitors (42.0%F):** The strongest male nephrotoxicity bias. Mechanistically, calcineurin inhibitors cause renal vasoconstriction and tubular damage that is modulated by testosterone (which enhances vasoconstriction) and estrogen (which provides vasodilation). Sex-differential CYP3A4/5 metabolism also affects calcineurin inhibitor exposure, with men typically achieving higher trough levels at equivalent doses [5]. Additionally, the transplant population skews male (approximately 60% of kidney transplant recipients are male), contributing to the male-enriched signal.

**ICIs (44.3%F):** ICI-induced nephritis is immune-mediated (T-cell infiltration of renal interstitium), yet shows male predominance. This is consistent with the broader pattern of male-biased immune-related adverse events in ICI therapy, potentially reflecting testosterone-modulated T-cell activation in the renal compartment. The male ICI nephrotoxicity contrasts with the female predominance of ICI skin reactions, illustrating organ-specific sex-differential immune responses.

**Aminoglycosides (59.9%F):** Near-baseline female fraction suggests that aminoglycoside nephrotoxicity---a direct, concentration-dependent tubular toxicity---does not strongly differ by sex after controlling for exposure. This may reflect the relatively sex-invariant mechanism of aminoglycoside-induced mitochondrial dysfunction and oxidative stress in proximal tubular cells.

### Renal AE Type Analysis

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

The renal AE spectrum reveals a physiological divide:

**Female-biased renal AEs:** UTI (66.2%F) is strongly female-biased, reflecting the well-known 8:1 female predominance in urinary tract infections due to anatomical factors (shorter urethra, proximity to GI flora). Blood creatinine increase (57.7%F) and CKD (57.0%F) show moderate female bias, possibly reflecting sex-differential biomarker sensitivity (women have lower baseline creatinine, so increases are more readily detected).

**Near-parity renal AEs:** AKI (49.8%F) and renal failure (49.9%F) approach sex parity despite the female FAERS baseline, indicating genuine male enrichment. This is consistent with hospital-based studies showing 1.5x male AKI rates [3]. Haematuria (49.1%F) is also near-parity, suggesting that gross renal injury does not strongly differ by sex.

### Severity Gradient

- Serious renal AEs: **51.3%F** (n = 741)
- Non-serious renal AEs: **55.2%F** (n = 589)
- Difference: 3.9 pp (p < 0.01)

The nephrotoxicity severity gradient (serious more male-biased) extends the broader observation that severe drug outcomes show less female predominance. For renal outcomes specifically, this aligns with the clinical observation that severe AKI requiring dialysis has a 1.8:1 male predominance [6].

### Top Nephrotoxic Drugs by Report Volume

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

**PPI nephrotoxicity (59--71%F):** Proton pump inhibitors emerged as the most frequently nephrotoxic drug class, with 4 PPIs ranking in the top 4 by report volume. PPI-associated nephrotoxicity (acute interstitial nephritis, CKD) is a relatively recent pharmacovigilance signal [7]. The moderate female bias (59--71%F) is consistent with higher PPI use in women and possibly with immune-mediated renal injury mechanisms that are female-biased.

**Tofacitinib (88.2%F):** The extreme female renal bias likely reflects the drug's autoimmune indication (rheumatoid arthritis: 3:1 female predominance, ulcerative colitis). The sex-stratified ROR partially controls for this, but the residual female excess may reflect genuine sex-differential JAK-mediated renal effects.

---

## Discussion

### Nephrotoxicity as a Male-Enriched SOC Exception

The renal system occupies a unique position in the sex-differential pharmacovigilance landscape. While most organ systems show female-predominant drug safety signals (immune, metabolic, hepatic: all >60%F), nephrotoxicity at 54.9%F represents one of the least female-biased major SOCs. Our companion analyses identified renal as the natural "negative control" for anti-regression (weakest monotonic trend) and the SOC atlas placed it below the FAERS baseline.

This male enrichment is biologically grounded: testosterone promotes renal vasoconstriction, proximal tubular injury, and oxidative stress, while estrogen provides renoprotection through nitric oxide-mediated vasodilation and anti-inflammatory pathways [4]. The clinical consequence is that drug-induced AKI should be monitored with heightened vigilance in male patients, particularly those receiving calcineurin inhibitors or ICIs.

### The Calcineurin Inhibitor-ICI Male Axis

The two most male-biased nephrotoxic drug classes (calcineurin inhibitors: 42.0%F, ICIs: 44.3%F) operate through fundamentally different mechanisms (direct toxicity vs. immune-mediated), yet both show strong male enrichment. This convergence suggests that renal male vulnerability is mechanism-independent and likely reflects the underlying sex-differential renal physiology rather than drug-specific effects.

### Clinical Implications

1. **Male-focused renal monitoring:** Calcineurin inhibitor and ICI patients who are male should receive enhanced renal function monitoring (more frequent creatinine, cystatin C, and urine albumin testing).
2. **PPI nephrotoxicity awareness:** The high prevalence of PPI-associated renal signals (4 of top 4 drugs) supports recent guideline recommendations for PPI deprescribing and renal monitoring during chronic PPI use.
3. **Autoimmune drug renal effects:** The extreme female bias of tofacitinib (88.2%F) and tocilizumab (69.8%F) renal effects suggests that autoimmune-indication drugs produce female-biased nephrotoxicity even in a generally male-biased SOC, likely through immune-mediated interstitial nephritis.

### Limitations

1. FAERS does not capture baseline renal function or drug exposure, preventing risk-adjusted analysis.
2. UTI as a "renal AE" may inflate female proportion (UTI is partly anatomical, not drug-induced).
3. Calcineurin inhibitor male bias may partly reflect transplant population demographics.
4. PPI nephrotoxicity is a recently recognized signal; reporting patterns may be evolving.

---

## Conclusion

Drug-induced nephrotoxicity shows consistent male enrichment (54.9%F vs. 60.2% baseline), with a 17.9 pp drug class spectrum from calcineurin inhibitors (42.0%F) to aminoglycosides (59.9%F). AKI and renal failure approach sex parity (49.8--49.9%F), confirming genuine male renal vulnerability. The severity gradient extends to nephrotoxicity (serious 51.3%F vs. non-serious 55.2%F). These findings support sex-stratified renal monitoring, with particular attention to male patients on calcineurin inhibitors and ICIs.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Perazella MA. Drug-induced acute kidney injury: diverse mechanisms of tubular injury. Curr Opin Crit Care. 2019;25:550-557.
2. Awdishu L, Mehta RL. The 6R's of drug-induced nephrotoxicity. BMC Nephrol. 2017;18:124.
3. Neugarten J, Golestaneh L. Female sex reduces the risk of hospital-associated acute kidney injury. J Am Soc Nephrol. 2018;29:2481-2488.
4. Mauvais-Jarvis F, et al. Sex and gender: modifiers of health, disease, and medicine. Lancet. 2020;396:565-582.
5. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48:143-157.
6. Mehta RL, et al. Spectrum of acute renal failure in the intensive care unit. Kidney Int. 2004;66:1613-1621.
7. Lazarus B, et al. Proton pump inhibitor use and the risk of chronic kidney disease. JAMA Intern Med. 2016;176:238-246.

---

## Figure Legends

**Figure 1.** Drug class nephrotoxicity spectrum. Horizontal bar chart showing mean female fraction for 8 drug classes. Calcineurin inhibitors (42.0%F) to aminoglycosides (59.9%F). Dashed line at 60.2% (FAERS baseline). All classes except aminoglycosides fall below baseline.

**Figure 2.** Renal AE type profiles. Bar chart of 10 renal AE categories ranked by female fraction. UTI (66.2%F) is the outlier; AKI (49.8%F), renal failure (49.9%F), and haematuria (49.1%F) approach parity.

**Figure 3.** PPI nephrotoxicity. Bubble chart of top 10 nephrotoxic drugs (bubble size = report volume, x-axis = %F, y-axis = N renal AEs). Four PPIs cluster in the high-volume, moderate-female zone.

**Figure 4.** Severity gradient in nephrotoxicity. Comparison of serious (51.3%F) vs. non-serious (55.2%F) renal signals, confirming male enrichment in severe renal outcomes.
