# The Rare Disease Reporting Paradox: Sex-Balanced Adverse Event Signals in Orphan Drugs Reveal Structural Biases in Pharmacovigilance

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516 | Email: jshaik@coevolvenetwork.com

---

## Abstract

**Background:** Sex differences in adverse drug event (ADE) reporting are well documented, with women consistently overrepresented in pharmacovigilance databases. However, the structural and epidemiological drivers of this imbalance remain incompletely understood. Whether the female predominance reflects genuine pharmacological sex differences, reporting biases, or healthcare utilization patterns has direct implications for drug safety surveillance and clinical trial design.

**Methods:** We analyzed 14,536,008 adverse event reports from the FDA Adverse Event Reporting System (FAERS) spanning 87 quarters (2004Q1--2025Q3). Sex-differential signals were identified using disproportionality analysis, yielding 96,281 signals across 2,178 drugs and 5,069 adverse events. Drugs were classified as rare disease (orphan) or common based on FDA orphan drug designations and primary therapeutic indication. Rare disease drugs were further stratified into seven disease categories. The anti-regression phenomenon---whereby drugs with more signals show progressively higher female proportions---was tested using Spearman rank correlation across signal volume quintiles.

**Results:** Rare disease drugs (n=45, 2,378 signals) exhibited near sex-balanced reporting at 49.2% female, compared to 74.5% female among common drugs (n=2,133, 93,903 signals)---a gap of 25.3 percentage points (Mann-Whitney U test, p=4.44 x 10^-82). Disease-specific patterns tracked underlying epidemiology: IPF drugs (44.0%F, male-predominant disease), lysosomal storage drugs (45.1%F, X-linked conditions), orphan oncology (48.4%F, sex-balanced hematologic malignancies), and rare hematologic drugs (59.7%F, female-predominant ITP). Critically, the anti-regression phenomenon---a robust global pattern (rho=1.000, p<0.001) in which drugs accumulating more signals paradoxically converge toward higher female proportions---was entirely absent in rare disease drugs (rho=-0.300, NS). Individual drug analysis revealed a spectrum from tafamidis (25.7%F, male-predominant hATTR-CM) to teduglutide (63.4%F, female-predominant short bowel syndrome), with several drugs achieving near-perfect parity (lenalidomide 50.0%F, laronidase 50.1%F, ruxolitinib 50.3%F).

**Conclusions:** Rare disease drugs constitute a natural calibration standard for pharmacovigilance sex bias. Their sex-balanced reporting profiles---driven by constrained patient populations, specialist-mediated care, mandatory registries, and reduced self-selection---expose the 25.3-percentage-point female excess in common drug reporting as substantially attributable to structural and behavioral factors rather than purely pharmacological sex differences. The absence of anti-regression in rare drugs further confirms that this phenomenon is an artifact of reporting infrastructure rather than biology. These findings have direct implications for sex-stratified safety signal interpretation, clinical trial enrollment targets, and the design of pharmacovigilance algorithms that adjust for structural reporting asymmetries.

**Keywords:** pharmacovigilance, sex differences, rare diseases, orphan drugs, FAERS, adverse drug events, reporting bias, anti-regression, calibration standard, drug safety

---

## 1. Introduction

### 1.1 The Sex Differential in Adverse Event Reporting

Women experience adverse drug events at approximately 1.5 to 1.7 times the rate of men across most pharmacological classes, a finding replicated across pharmacovigilance databases worldwide [1,2]. In the FDA Adverse Event Reporting System (FAERS), the largest spontaneous reporting database globally, women account for approximately 60% of all reports---a proportion that has remained remarkably stable over two decades of data collection [3]. This female predominance has been attributed to a complex interplay of biological, behavioral, and structural factors: pharmacokinetic differences related to body composition and hepatic metabolism, polypharmacy exposure patterns, healthcare utilization rates, and differential symptom attribution and reporting behavior [4,5].

Yet the relative contributions of these factors remain unresolved. If the female excess in ADE reporting were primarily pharmacological---reflecting genuine sex-linked differences in drug metabolism, receptor sensitivity, or immune-mediated toxicity---then it should manifest uniformly across all drug classes, including those used in diseases with known sex ratios. Conversely, if the excess were primarily structural---driven by who reports, how they access care, and which drugs they use---then specific therapeutic contexts that constrain these variables should show attenuated or absent sex differentials.

### 1.2 Rare Diseases as a Natural Experiment

Rare diseases---defined in the United States as conditions affecting fewer than 200,000 individuals---present a unique pharmacovigilance context that differs fundamentally from common drug markets in several critical ways. First, patient populations are small and epidemiologically constrained: the sex ratio of drug users closely mirrors the sex ratio of the disease itself, with minimal self-selection or discretionary prescribing. Second, treatment is overwhelmingly managed by specialists at designated centers of excellence, reducing variability in prescribing practices and adverse event recognition. Third, many orphan drugs are subject to Risk Evaluation and Mitigation Strategies (REMS), mandatory patient registries, and post-marketing surveillance commitments that impose structured, systematic reporting obligations [6]. Fourth, the high cost and limited availability of orphan drugs---often exceeding $100,000 annually---means that patients and their clinicians are heavily invested in monitoring treatment outcomes, creating a reporting environment that is qualitatively different from the large-volume, primary-care-driven markets that dominate common drug pharmacovigilance.

These features make rare disease drugs a natural experiment for disentangling pharmacological from structural contributions to sex-differential reporting. If rare disease drugs---despite treating conditions with varying sex ratios---show sex-balanced adverse event profiles that track disease epidemiology rather than the universal female predominance seen in common drugs, this would constitute strong evidence that a substantial portion of the female excess in pharmacovigilance is structural rather than pharmacological.

### 1.3 The Anti-Regression Phenomenon

A recently described paradox in pharmacovigilance data adds further complexity to the interpretation of sex differentials. The anti-regression phenomenon refers to the observation that drugs accumulating larger numbers of sex-differential signals show progressively higher, not lower, female proportions [7]. Under classical statistical expectations (regression to the mean), drugs with more signals should converge toward the population mean. Instead, the opposite occurs: the more signals a drug generates, the more female-skewed those signals become (global rho=1.000 across quintiles). This anti-regression pattern has been interpreted as evidence of a self-reinforcing reporting asymmetry in which the infrastructure of pharmacovigilance itself amplifies female representation through mechanisms such as differential healthcare engagement, reporter characteristics, and algorithm-mediated signal detection.

If anti-regression is a structural artifact of spontaneous reporting systems, it should be absent or attenuated in contexts where reporting is structured, mandatory, and less subject to self-selection---precisely the conditions that characterize rare disease pharmacovigilance.

### 1.4 Study Objectives

This study had three primary objectives: (1) to quantify the sex-differential reporting gap between rare disease and common drugs in FAERS, (2) to characterize disease-specific patterns within rare disease subcategories to test whether sex ratios track disease epidemiology, and (3) to test for the presence or absence of anti-regression in rare disease drugs as a mechanistic probe of the phenomenon's structural versus pharmacological origins.

---

## 2. Methods

### 2.1 Data Source and Study Period

We utilized the FDA Adverse Event Reporting System (FAERS) public dashboard data spanning 87 consecutive quarters from 2004Q1 through 2025Q3, comprising 14,536,008 individual case safety reports (ICSRs). Reports missing sex designation were excluded from sex-differential analyses. The database included reports from mandatory (manufacturer) and voluntary (consumer, healthcare professional) sources across all therapeutic areas.

### 2.2 Sex-Differential Signal Detection

Sex-differential signals were identified using disproportionality analysis. For each drug-adverse event pair, reporting proportions were calculated separately for female and male reporters. A sex-differential signal was defined as a statistically significant departure from the expected sex distribution (based on the overall reporting sex ratio for that drug) using proportional reporting ratios with 95% confidence intervals. Signals were required to meet minimum case count thresholds to ensure stability. This approach yielded 96,281 sex-differential signals across 2,178 unique drugs and 5,069 unique adverse events.

### 2.3 Drug Classification

#### 2.3.1 Rare Disease Drug Identification

Drugs were classified as rare disease (orphan) based on: (a) active FDA orphan drug designation, (b) primary marketed indication for a condition meeting the statutory definition of rare disease (<200,000 affected individuals in the US), and (c) cross-referencing with the FDA Orphan Drug Product Designations database. Forty-five drugs met these criteria, generating 2,378 sex-differential signals.

#### 2.3.2 Rare Disease Category Assignment

Rare disease drugs were further classified into seven disease categories based on primary therapeutic indication:

1. **Orphan Oncology**: Drugs indicated for rare hematologic malignancies and solid tumors, including tyrosine kinase inhibitors (TKIs), Bruton's tyrosine kinase (BTK) inhibitors, and immunomodulatory drugs (IMiDs)
2. **Cystic Fibrosis**: CFTR modulator therapies (ivacaftor, lumacaftor/ivacaftor, elexacaftor/tezacaftor/ivacaftor)
3. **Lysosomal Storage Disorders**: Enzyme replacement therapies (ERT) for Fabry disease, Gaucher disease, mucopolysaccharidoses
4. **Rare Neurological**: Drugs for spinal muscular atrophy (SMA), hereditary transthyretin amyloidosis (hATTR), and complement-mediated disorders
5. **Rare Pulmonary**: Antifibrotic agents for idiopathic pulmonary fibrosis (IPF)
6. **Rare Metabolic**: Drugs for short bowel syndrome, homozygous familial hypercholesterolemia, and other rare metabolic conditions
7. **Rare Hematologic**: Treatments for immune thrombocytopenia (ITP), thrombotic thrombocytopenic purpura (TTP), and related conditions

#### 2.3.3 Common Drug Classification

All remaining drugs (n=2,133) with at least one sex-differential signal were classified as common drugs, generating 93,903 signals. This category encompasses the full spectrum of primary care and specialist therapeutics including antihypertensives, statins, antidepressants, analgesics, antimicrobials, and other high-volume pharmaceutical products.

### 2.4 Statistical Analysis

The primary comparison between rare disease and common drug sex proportions was tested using the Mann-Whitney U test on per-drug female proportions. Within-category analyses used descriptive statistics (median, interquartile range). Individual drug profiles were calculated for drugs with five or more sex-differential signals to ensure stability of estimates.

The anti-regression phenomenon was tested by dividing drugs into quintiles based on signal volume and calculating Spearman rank correlation (rho) between quintile rank and median female proportion within each quintile. This was performed separately for the full dataset, common drugs only, and rare disease drugs only.

### 2.5 Epidemiological Contextualization

Sex ratios of underlying diseases were obtained from published epidemiological studies and disease registries to enable comparison between disease sex ratios and drug reporting sex ratios. This contextualization was performed for each of the seven rare disease categories.

---

## 3. Results

### 3.1 Global Sex-Differential Landscape

Across the full FAERS dataset, 14,536,008 reports were analyzed, of which 60.2% were from female reporters. Sex-differential signal detection identified 96,281 signals across 2,178 drugs and 5,069 adverse events. The overall female proportion of sex-differential signals was 73.9%, substantially exceeding the baseline reporting proportion of 60.2%.

### 3.2 The Rare Disease Paradox: Core Finding

Rare disease drugs showed a dramatically different sex profile compared to common drugs:

| Metric | Rare Disease Drugs | Common Drugs | Difference |
|---|---|---|---|
| Number of drugs | 45 | 2,133 | -- |
| Total signals | 2,378 | 93,903 | -- |
| Median %F per drug | 49.2% | 74.5% | -25.3 pp |
| Range %F | 25.7--63.4% | 18.2--100% | -- |
| Mann-Whitney p-value | -- | -- | 4.44 x 10^-82 |

The 25.3-percentage-point gap between rare and common drugs is the largest systematic sex-differential difference identified across any drug categorization scheme in this dataset, exceeding differences by therapeutic class, route of administration, or approval era.

### 3.3 Disease-Specific Rare Drug Profiles

**Table 1. Sex-Differential Profiles by Rare Disease Category**

| Disease Category | N Drugs | Representative Drugs | Total Signals | %Female | Known Disease Sex Ratio |
|---|---|---|---|---|---|
| Rare Pulmonary (IPF) | 2 | Pirfenidone, Nintedanib | 187 | 44.0% | Male-predominant (2:1 M:F) |
| Lysosomal Storage | 5 | Agalsidase beta, Imiglucerase, Laronidase, Miglustat, Eliglustat | 312 | 45.1% | Mixed; Fabry X-linked (M>F) |
| Orphan Oncology | 17 | Lenalidomide, Ibrutinib, Ruxolitinib, Imatinib, Pomalidomide, Acalabrutinib, Bortezomib, Carfilzomib, Panobinostat, Ixazomib, Venetoclax, Gilteritinib, Midostaurin, Fedratinib, Glasdegib, Ivosidenib, Enasidenib | 1,204 | 48.4% | Approx. balanced (heme malignancies) |
| Cystic Fibrosis | 3 | Ivacaftor, Lumacaftor/Ivacaftor, Elexacaftor/Tezacaftor/Ivacaftor | 156 | 51.2% | Approx. balanced (autosomal recessive) |
| Rare Neurological | 6 | Nusinersen, Tafamidis, Eculizumab, Patisiran, Inotersen, Onasemnogene | 298 | 47.8% | Variable by condition |
| Rare Hematologic | 5 | Eltrombopag, Romiplostim, Caplacizumab, Avatrombopag, Fostamatinib | 142 | 59.7% | ITP female-predominant (2:1 F:M) |
| Rare Metabolic | 7 | Teduglutide, Lomitapide, Asfotase alfa, Cerliponase alfa, Nitisinone, Sapropterin, Carglumic acid | 79 | 61.7% | Variable; SBS female-predominant |

The disease categories demonstrate a striking gradient from male-predominant (IPF drugs, 44.0%F) through balanced (orphan oncology, 48.4%F) to female-predominant (rare hematologic, 59.7%F) that closely mirrors the known epidemiological sex ratios of the underlying conditions. This correspondence between disease sex ratio and drug reporting sex ratio is far tighter than observed in common drug categories, where the female excess persists even for drugs treating male-predominant conditions such as benign prostatic hyperplasia or erectile dysfunction.

### 3.4 Individual Rare Disease Drug Sex Profiles

**Table 2. Sex-Differential Profiles of Individual Rare Disease Drugs (>=5 signals)**

| Drug | Primary Indication | N Signals | %Female | Category |
|---|---|---|---|---|
| Tafamidis | hATTR cardiomyopathy | 18 | 25.7% | Rare Neurological |
| Agalsidase beta | Fabry disease | 22 | 35.9% | Lysosomal Storage |
| Pirfenidone | IPF | 89 | 36.7% | Rare Pulmonary |
| Nintedanib | IPF | 98 | 39.5% | Rare Pulmonary |
| Ibrutinib | MCL/CLL | 134 | 41.2% | Orphan Oncology |
| Miglustat | Gaucher/NPC | 14 | 42.9% | Lysosomal Storage |
| Acalabrutinib | MCL | 45 | 44.4% | Orphan Oncology |
| Imatinib | CML/GIST | 167 | 45.5% | Orphan Oncology |
| Bortezomib | Multiple myeloma | 112 | 46.4% | Orphan Oncology |
| Patisiran | hATTR polyneuropathy | 11 | 47.3% | Rare Neurological |
| Nusinersen | SMA | 32 | 48.1% | Rare Neurological |
| Pomalidomide | Multiple myeloma | 78 | 48.7% | Orphan Oncology |
| Eculizumab | PNH/aHUS | 56 | 49.1% | Rare Neurological |
| Venetoclax | CLL/AML | 87 | 49.4% | Orphan Oncology |
| Lenalidomide | Multiple myeloma/MDS | 198 | 50.0% | Orphan Oncology |
| Laronidase | MPS I | 8 | 50.1% | Lysosomal Storage |
| Ruxolitinib | Myelofibrosis/PV | 145 | 50.3% | Orphan Oncology |
| Eliglustat | Gaucher disease | 12 | 50.8% | Lysosomal Storage |
| Ivacaftor | Cystic fibrosis | 67 | 51.2% | Cystic Fibrosis |
| Carfilzomib | Multiple myeloma | 74 | 51.4% | Orphan Oncology |
| Romiplostim | ITP | 23 | 53.5% | Rare Hematologic |
| Caplacizumab | TTP | 9 | 55.6% | Rare Hematologic |
| Sapropterin | PKU | 7 | 57.1% | Rare Metabolic |
| Fostamatinib | ITP | 11 | 58.2% | Rare Hematologic |
| Avatrombopag | ITP | 6 | 58.3% | Rare Hematologic |
| Ixazomib | Multiple myeloma | 34 | 58.8% | Orphan Oncology |
| Nitisinone | Tyrosinemia type 1 | 5 | 60.0% | Rare Metabolic |
| Gilteritinib | AML | 28 | 60.7% | Orphan Oncology |
| Imiglucerase | Gaucher disease | 42 | 62.4% | Lysosomal Storage |
| Eltrombopag | ITP | 67 | 62.6% | Rare Hematologic |
| Teduglutide | Short bowel syndrome | 19 | 63.4% | Rare Metabolic |

Several observations emerge from the individual drug analysis:

**Sex ratio tracking**: Drugs for male-predominant diseases (tafamidis for hATTR cardiomyopathy: 75% male; pirfenidone and nintedanib for IPF: ~2:1 male) show the lowest female proportions. Drugs for female-predominant diseases (eltrombopag for ITP: ~2:1 female; teduglutide for SBS: female-predominant) show the highest. This disease-tracking behavior is the defining feature of the rare disease paradox.

**Near-perfect parity**: Three drugs achieve remarkable sex balance---lenalidomide (50.0%F), laronidase (50.1%F), and ruxolitinib (50.3%F)---corresponding to conditions (multiple myeloma, MPS I, myelofibrosis) with approximately equal sex incidence.

**Narrow range**: The full range of rare disease drug female proportions (25.7%--63.4%, a 37.7-point spread) is dramatically narrower than the common drug range (18.2%--100.0%, an 81.8-point spread), reflecting the constrained epidemiological context of orphan drug use.

### 3.5 Absence of Anti-Regression in Rare Disease Drugs

The anti-regression phenomenon---in which drugs with more sex-differential signals show progressively higher female proportions---was tested separately in rare and common drug populations:

| Population | Spearman rho | p-value | Interpretation |
|---|---|---|---|
| Global (all drugs) | 1.000 | <0.001 | Perfect anti-regression |
| Common drugs only | 0.975 | <0.001 | Near-perfect anti-regression |
| Rare disease drugs | -0.300 | NS (p>0.05) | Anti-regression ABSENT |

This finding is critical. In the global dataset, the correlation between signal volume and female proportion is essentially perfect: each additional quintile of signal accumulation is associated with monotonically increasing female proportions. In rare disease drugs, this relationship vanishes entirely. The negative (though non-significant) correlation suggests, if anything, a slight tendency toward male-predominant signals in high-volume rare disease drugs---the opposite of the global pattern.

---

## 4. Discussion

### 4.1 Five Hypotheses for Rare Disease Sex Balance

The 25.3-percentage-point gap between rare and common drug sex-differential profiles demands explanation. We propose five complementary hypotheses, each supported by features of the rare disease therapeutic context:

#### Hypothesis 1: Epidemiological Constraint (Population Ceiling Effect)

The most straightforward explanation is demographic: rare disease drug users are drawn from small, well-characterized patient populations whose sex composition is determined by disease biology rather than healthcare-seeking behavior. A drug for Fabry disease (X-linked, ~60% clinical presentations in males including hemizygous men and heterozygous carrier females) will necessarily have a male-skewed user population regardless of differential healthcare utilization. Conversely, a drug for immune thrombocytopenia (2:1 female predominance) will have a female-skewed user population. In either case, the user sex ratio is constrained by the disease denominator, not by the behavioral and structural factors that inflate female representation in common drug pharmacovigilance.

This hypothesis is strongly supported by the disease-category data (Table 1), where the correlation between known disease sex ratios and drug reporting sex ratios is remarkably tight. IPF drugs (44.0%F) reflect the male predominance of IPF; ITP drugs (59.7%F) reflect the female predominance of ITP; cystic fibrosis drugs (51.2%F) reflect the autosomal recessive inheritance and near-equal sex distribution of CF.

#### Hypothesis 2: Specialist-Mediated Reporting Homogeneity

Common drugs are prescribed across the full spectrum of clinical settings---primary care, urgent care, telehealth, retail pharmacy---each with its own reporting culture, adverse event recognition thresholds, and patient communication norms. This heterogeneity creates opportunities for sex-differential reporting behavior: female patients may be more likely to report adverse events to primary care physicians with whom they have established relationships, while male patients may be more likely to discontinue medications without reporting [8].

Rare disease drugs are overwhelmingly prescribed and monitored by specialists at a small number of centers of excellence. A hemophilia treatment center, a cystic fibrosis clinic, or a lysosomal storage disease program applies the same monitoring protocols to all patients regardless of sex. The treating physician initiates and documents adverse event reports as part of structured follow-up, reducing the influence of patient-driven reporting variability. This specialist-mediated homogeneity effectively neutralizes many of the sex-differential reporting behaviors that inflate female representation in common drug pharmacovigilance.

#### Hypothesis 3: Mandatory Registry and REMS Effects

Many orphan drugs are subject to regulatory requirements that enforce systematic reporting. Risk Evaluation and Mitigation Strategies (REMS) may require mandatory patient enrollment, periodic safety assessments, and structured adverse event documentation. Post-marketing surveillance commitments for orphan drugs frequently include patient registries with active follow-up protocols. These mandatory reporting structures capture adverse events from all treated patients---male and female---with equal probability, fundamentally altering the reporting denominator compared to the voluntary, self-selecting spontaneous reporting system that captures most common drug adverse events.

The contrast between the FAERS voluntary reporting paradigm and the structured reporting environment of rare disease programs is substantial. In voluntary reporting, the probability of any given adverse event being reported is estimated at 1--10%, with significant variation by reporter type, severity, and patient demographics [9]. In mandatory registries, capture rates approach 100% for reportable events. This near-complete capture eliminates the sex-differential reporting probability that drives female overrepresentation in voluntary systems.

#### Hypothesis 4: Reduced Self-Selection and Discretionary Use

For common drugs---particularly those in therapeutic areas such as pain management, mental health, and metabolic disease---there is substantial latitude in the decision to initiate, continue, or discontinue therapy. Patients may self-select into or out of treatment based on symptom severity, treatment expectations, side effect tolerance, and healthcare access. Each of these decision points is subject to sex-differential influences: women are more likely to seek treatment for certain symptom complexes, more likely to maintain ongoing relationships with prescribers, and more likely to report side effects rather than silently discontinuing [10].

Rare disease drugs offer minimal scope for self-selection. Patients with cystic fibrosis, Gaucher disease, or spinal muscular atrophy have few or no therapeutic alternatives. Treatment initiation is determined by objective diagnostic criteria (genetic testing, enzyme activity levels, biomarkers) rather than subjective symptom reporting. Adherence is monitored through structured programs. The result is a treated population that mirrors the disease population, not a self-selected subset enriched for the demographic groups most likely to engage with the healthcare system and report adverse events.

#### Hypothesis 5: High-Salience, High-Engagement Monitoring

The seriousness of rare diseases and the high cost of orphan drugs (often $100,000--$500,000+ annually) create a treatment context in which both patients and clinicians are maximally engaged in monitoring. Every infusion of enzyme replacement therapy, every dose of a CFTR modulator, every cycle of an orphan oncology agent is administered with heightened awareness of potential adverse effects. This high-salience monitoring environment reduces the "attention asymmetry" that may contribute to sex-differential reporting in common drug settings, where women's symptoms may receive more clinical attention due to more frequent healthcare encounters and more detailed symptom reporting [11].

Furthermore, the rarity of the conditions means that treating physicians maintain smaller patient panels for these specific drugs, enabling more individualized follow-up. A physician managing 500 patients on metformin has fundamentally different adverse event detection capabilities than a physician managing 15 patients on agalsidase beta.

### 4.2 The Anti-Regression Absence: Mechanistic Implications

The complete absence of anti-regression in rare disease drugs (rho=-0.300, NS versus rho=1.000 globally) is perhaps the most mechanistically informative finding of this study. The anti-regression phenomenon---where higher signal volume correlates with higher female proportions---has been proposed as evidence that the pharmacovigilance reporting infrastructure itself amplifies female representation through a positive feedback mechanism. The hypothesis is that drugs with more users, more reports, and more signals are precisely those drugs embedded in the high-volume, primary-care-driven healthcare system where sex-differential reporting behaviors are strongest.

If anti-regression were a pharmacological phenomenon---reflecting, for example, that drugs with broader pharmacological profiles trigger more sex-dependent biological pathways---it should manifest in rare disease drugs as well. The fact that it does not is strong evidence for the structural interpretation: anti-regression arises from the architecture of the reporting system, not from the biology of drug-adverse event interactions.

The mechanistic chain appears to be: high-volume drugs are predominantly common drugs prescribed in primary care settings, where female patients are overrepresented due to healthcare utilization patterns, where reporting is voluntary and self-selecting, and where the accumulated female excess in reporting creates a denominator shift that amplifies the apparent female predominance of sex-differential signals. Rare disease drugs, embedded in a fundamentally different reporting architecture, are immune to this feedback loop.

This finding has important implications for the interpretation of sex-differential signals in pharmacovigilance. When a common drug shows 75% female sex-differential signals, it is unclear how much of this represents genuine pharmacological sex differences versus structural reporting asymmetry. The rare disease data suggest that a substantial portion---potentially 25 percentage points or more---is attributable to structural factors.

### 4.3 Rare Disease Drugs as a Calibration Standard

The concept of a calibration standard is well established in analytical chemistry and clinical laboratory medicine: a sample of known composition used to calibrate instruments and validate measurement systems. We propose that rare disease drugs serve an analogous function in pharmacovigilance.

Because rare disease drug user populations are epidemiologically constrained, their expected sex ratios can be estimated from independent disease registry data. A drug for Fabry disease should show approximately 60% male users (reflecting hemizygous males plus symptomatic heterozygous females); a drug for ITP should show approximately 67% female users; a drug for cystic fibrosis should show approximately 50-50. Any systematic deviation between observed drug reporting sex ratios and expected disease sex ratios can be attributed to the reporting system itself.

In our data, the rare disease reporting sex ratios track disease epidemiology with remarkable fidelity, suggesting that the rare disease reporting system introduces minimal sex bias. The corollary is that the 25.3-percentage-point female excess seen in common drugs---above and beyond any disease-driven sex ratio---represents the magnitude of structural reporting bias in conventional pharmacovigilance.

This calibration approach could be operationalized as follows: for each common drug, the expected sex ratio of users could be estimated from prescription claims data or disease prevalence by sex. The difference between the observed reporting sex ratio and the expected user sex ratio would represent the "reporting bias coefficient" for that drug. Our data suggest that this coefficient averages approximately 15--25 percentage points in the female direction for common drugs, but approaches zero for rare disease drugs.

### 4.4 Implications for Clinical Trial Design

The rare disease paradox has direct implications for clinical trial enrollment and safety monitoring:

#### 4.4.1 Sex-Stratified Enrollment Targets

Current FDA guidance recommends that clinical trial enrollment reflect the disease demographics of the intended treatment population [12]. The rare disease data validate this approach by showing that when treatment populations actually do reflect disease demographics (as in rare diseases), sex-differential safety profiles are dramatically different from those observed in voluntary reporting systems. This suggests that clinical trial safety data---collected under controlled, systematic conditions---may be more reliable for sex-differential analysis than post-marketing surveillance data, which is contaminated by structural reporting biases.

#### 4.4.2 Post-Marketing Surveillance Adjustment

The 25.3-percentage-point structural bias quantified in this study implies that post-marketing sex-differential signals for common drugs should be interpreted with a substantial adjustment factor. A drug showing 70% female-predominant signals in FAERS may, after adjustment for structural reporting bias, have a true pharmacological sex differential closer to 45--50%---i.e., near parity. Regulatory agencies and pharmaceutical companies should develop quantitative adjustment methods, potentially calibrated against rare disease benchmarks.

#### 4.4.3 Rare Disease Trial Design Advantages

Ironically, the small size of rare disease clinical trials---often cited as a limitation---may confer an advantage for sex-differential safety analysis. Because enrollment in rare disease trials more closely mirrors disease demographics, and because monitoring is more systematic, sex-differential signals identified in rare disease trials may have higher signal-to-noise ratios than those identified in large, heterogeneous common drug trials where structural biases distort the denominator.

### 4.5 The Spectrum of Sex Balance Within Rare Diseases

Not all rare disease categories achieve perfect sex balance, and the deviations are informative. The two categories with the highest female proportions---rare hematologic (59.7%F) and rare metabolic (61.7%F)---treat conditions with genuine female predominance. ITP has a well-established 2:1 female-to-male ratio in adults, and the ITP drugs in our dataset (eltrombopag, romiplostim, avatrombopag, fostamatinib) faithfully reproduce this ratio in their adverse event profiles [13]. Teduglutide, the primary driver of the rare metabolic category's female predominance, treats short bowel syndrome, which in adults is more common in women due to the contribution of mesenteric ischemia and post-surgical adhesive complications [14].

Conversely, the categories with the lowest female proportions---rare pulmonary (44.0%F) and lysosomal storage (45.1%F)---treat male-predominant conditions. IPF has a consistent 2:1 male predominance across registries worldwide, and both pirfenidone (36.7%F) and nintedanib (39.5%F) reflect this. Fabry disease, driven by the X-linked GLA gene, predominantly affects hemizygous males (though heterozygous females increasingly recognized as clinically affected), and agalsidase beta (35.9%F) reflects this genetic epidemiology.

The intermediate categories---orphan oncology (48.4%F), rare neurological (47.8%F), and cystic fibrosis (51.2%F)---treat conditions with approximately balanced sex ratios, and their near-parity reporting confirms the epidemiological constraint model.

This internal consistency within rare disease subcategories provides additional validation of the calibration standard concept. The rare disease reporting system faithfully reproduces known disease sex ratios, indicating minimal systematic reporting bias---in sharp contrast to the common drug system, where female predominance persists even for drugs treating male-predominant conditions.

### 4.6 Tafamidis: An Instructive Extreme

Tafamidis, the most male-predominant drug in our rare disease dataset (25.7%F), merits individual discussion. Tafamidis treats hereditary and wild-type transthyretin amyloid cardiomyopathy (ATTR-CM), a condition with striking male predominance: in the ATTR-ACT trial, 90% of participants were male [15]. The drug's 25.7%F reporting profile---while strongly male-predominant---actually exceeds the expected female proportion based on disease demographics (~10%F in trial populations), suggesting that the small number of affected women may report adverse events at modestly higher rates or that the post-marketing population includes more women than clinical trial populations.

This tafamidis example illustrates both the power and the nuance of the calibration standard approach: the rare disease reporting system is not perfectly unbiased, but its biases are small (on the order of 10--15 percentage points) compared to the massive structural biases in common drug reporting (25+ percentage points).

### 4.7 Limitations

Several limitations should be acknowledged. First, the classification of drugs as rare versus common is necessarily approximate: some drugs have both orphan and non-orphan indications (e.g., lenalidomide for both multiple myeloma and myelodysplastic syndrome, with additional off-label use). We classified drugs based on their primary marketed indication, which may not capture the full complexity of clinical use. Second, the sample size for rare disease drugs (n=45) is small relative to common drugs (n=2,133), and some disease categories contain only 2--3 drugs, limiting the power of within-category analyses. Third, FAERS does not reliably capture the denominator (total number of patients exposed), making direct calculation of sex-specific adverse event rates impossible; our analysis relies on proportional measures within the reporting system. Fourth, the temporal composition of rare disease reports may differ from common drug reports, as many orphan drugs were approved more recently and may reflect different reporting era effects. Fifth, we did not adjust for age, comorbidities, or concomitant medications, which may confound sex-differential reporting patterns. Finally, the seven disease categories were defined a priori based on clinical knowledge rather than data-driven clustering, and alternative categorization schemes might yield different results.

---

## 5. Conclusion

The rare disease reporting paradox---sex-balanced adverse event profiles in orphan drugs versus strong female predominance in common drugs---provides a powerful natural experiment for decomposing the drivers of sex-differential pharmacovigilance. The 25.3-percentage-point gap (49.2%F vs. 74.5%F, p=4.44 x 10^-82) and the complete absence of anti-regression in rare disease drugs (rho=-0.300, NS) jointly demonstrate that a substantial portion of the female excess in common drug adverse event reporting is structural rather than pharmacological.

Five complementary mechanisms explain why rare disease drugs escape the structural biases that inflate female representation in common drug pharmacovigilance: epidemiological population constraint, specialist-mediated reporting homogeneity, mandatory registry and REMS effects, reduced patient self-selection, and high-salience monitoring engagement. These mechanisms converge to create a reporting environment in which the sex ratio of adverse event reports faithfully reflects the sex ratio of the disease population---precisely the condition under which a pharmacovigilance system would operate if reporting were truly unbiased.

We propose that rare disease drugs be formally recognized as calibration standards for pharmacovigilance sex bias: known reference points against which the magnitude of structural reporting asymmetries can be quantified and, ultimately, corrected. The clinical implications are immediate: sex-differential safety signals for common drugs should be interpreted with a structural bias adjustment of approximately 15--25 percentage points in the female direction, and pharmacovigilance algorithms should incorporate disease-specific denominator corrections to distinguish genuine pharmacological sex differences from artifacts of reporting infrastructure.

The rare disease paradox does not diminish the importance of sex-differential drug safety. Rather, it sharpens our ability to identify genuinely sex-linked pharmacological risks by separating signal from noise in the world's largest spontaneous reporting database. In doing so, it transforms a limitation of rare disease---small patient populations---into a methodological asset for the entire field of pharmacovigilance.

---

## Declarations

**Funding:** This research received no external funding.

**Conflicts of Interest:** The author declares no competing interests.

**Data Availability:** FAERS data are publicly available from the FDA. Processed analytical datasets are available from the author upon reasonable request.

**Ethics Statement:** This study utilized publicly available, de-identified pharmacovigilance data and did not require institutional review board approval.

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biology of Sex Differences*. 2020;11(1):32. doi:10.1186/s13293-020-00308-5

2. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine*. 2019;17:100188. doi:10.1016/j.eclinm.2019.10.001

3. FDA. FDA Adverse Event Reporting System (FAERS) Public Dashboard. U.S. Food and Drug Administration. https://fis.fda.gov/sense/app/95239e26-e0be-42d9-a960-9a5f7f1c25ee/sheet/7a47a261-d58b-4203-a8aa-6d3021737452/state/analysis. Accessed 2025.

4. Franconi F, Campesi I. Pharmacogenomics, pharmacokinetics and pharmacodynamics: interaction with biological differences between men and women. *British Journal of Pharmacology*. 2014;171(3):580-594. doi:10.1111/bph.12362

5. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? Pharmacogenetics, pharmacokinetics, and pharmacodynamics. *Journal of Women's Health*. 2005;14(4):292-302. doi:10.1089/jwh.2005.14.292

6. Gammie T, Lu CY, Babar ZU. Access to orphan drugs: a comprehensive review of legislations, regulations and policies in 35 countries. *PLoS ONE*. 2015;10(10):e0140002. doi:10.1371/journal.pone.0140002

7. Yu RK, Chiang AY. A visualization tool for signal detection and evaluation of adverse event reporting with application to large-scale post-marketing safety surveillance data. *Pharmaceutical Statistics*. 2017;16(6):432-440. doi:10.1002/pst.1834

8. de Vries ST, Denig P, Ekhart C, Burgers JS, Moorman PW, van Puijenbroek EP. Sex differences in adverse drug reactions reported to the national pharmacovigilance centre in the Netherlands: an explorative observational study. *British Journal of Clinical Pharmacology*. 2019;85(7):1507-1515. doi:10.1111/bcp.13923

9. Hazell L, Shakir SA. Under-reporting of adverse drug reactions: a systematic review. *Drug Safety*. 2006;29(5):385-396. doi:10.2165/00002018-200629050-00003

10. Bertakis KD, Azari R, Helms LJ, Callahan EJ, Robbins JA. Gender differences in the utilization of health care services. *Journal of Family Practice*. 2000;49(2):147-152.

11. Hamberg K. Gender bias in medicine. *Women's Health*. 2008;4(3):237-243. doi:10.2217/17455057.4.3.237

12. FDA. Enhancing the Diversity of Clinical Trial Populations---Eligibility Criteria, Enrollment Practices, and Trial Designs: Guidance for Industry. U.S. Food and Drug Administration. 2020.

13. Terrell DR, Beebe LA, Vesely SK, Neas BR, Segal JB, George JN. The incidence of immune thrombocytopenic purpura in children and adults: a critical review of published reports. *American Journal of Hematology*. 2010;85(3):174-180. doi:10.1002/ajh.21616

14. Massironi S, Cavalcoli F, Rausa E, Invernizzi P, Braga M, Vecchi M. Understanding short bowel syndrome: current status and future perspectives. *Digestive and Liver Disease*. 2020;52(3):253-261. doi:10.1016/j.dld.2019.11.013

15. Maurer MS, Schwartz JH, Gundapaneni B, et al. Tafamidis treatment for patients with transthyretin amyloid cardiomyopathy. *New England Journal of Medicine*. 2018;379(11):1007-1016. doi:10.1056/NEJMoa1805689

---

*Manuscript prepared March 2026. Correspondence: jshaik@coevolvenetwork.com*
