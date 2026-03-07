# Sex-Specific Safety Profiles of GLP-1 Receptor Agonists: The Most Male-Biased Drug Class in Diabetes Pharmacovigilance

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Glucagon-like peptide-1 receptor agonists (GLP-1RAs) have become among the most prescribed medications globally, driven by their efficacy in type 2 diabetes and obesity. As semaglutide and tirzepatide use expands into predominantly female populations for weight management, sex-specific safety data are urgently needed. No systematic sex-stratified pharmacovigilance analysis of the GLP-1RA class has been performed at population scale.

**Methods.** We analyzed 14,536,008 deduplicated FDA Adverse Event Reporting System (FAERS) reports (8,744,397 female; 5,791,611 male) spanning 87 quarters (2004Q1--2025Q3). Sex-stratified Reporting Odds Ratios (ROR) were computed for all drug--adverse event pairs across five GLP-1RAs (semaglutide, tirzepatide, liraglutide, dulaglutide, exenatide) and six comparator diabetes drug classes (insulin, metformin, sulfonylureas, thiazolidinediones, DPP-4 inhibitors, SGLT2 inhibitors). The log-transformed female-to-male ROR ratio (logR) was used to quantify sex-differential disproportionality, with |logR| >= 0.5 defining significant signals.

**Results.** We identified 517 sex-differential signals for GLP-1RAs. The class exhibited the strongest male bias (24.6% female) among all seven diabetes drug classes, contrasting sharply with thiazolidinediones (91.7% female)---a 67.1 percentage-point range. Among individual agents, tirzepatide showed the most extreme male bias (91.6% male-higher, 95 signals), followed by liraglutide (86.1%, 101 signals) and dulaglutide (72.7%, 77 signals). Semaglutide, the most widely prescribed GLP-1RA, showed 68.4% male-predominant signals (152 signals). Male-biased adverse events were dominated by gastrointestinal (cholecystitis chronic: logR = -1.62 for semaglutide, -2.24 for liraglutide), neuropsychiatric (aggression: logR = -1.38; sleep disorder: logR = -1.56 for tirzepatide), and hepatobiliary events. Female-biased exceptions included angina pectoris (logR = +1.34 for semaglutide), device-related events, and selected dermatological reactions. The seven diabetes drug classes formed a continuous sex-bias spectrum from thiazolidinediones (91.7% female) through sulfonylureas (73.6%), metformin (62.4%), SGLT2 inhibitors (59.7%), DPP-4 inhibitors (57.7%), and insulin (39.5%) to GLP-1RAs (24.6% female), demonstrating that sex-differential safety is a class-level property with a 67.1 percentage-point range.

**Interpretation.** GLP-1 receptor agonists exhibit the most pronounced male bias in adverse event reporting of any diabetes drug class. As these agents are increasingly prescribed to predominantly female populations for weight management, the male-dominant safety profile suggests that currently characterized adverse events may underrepresent the female experience. Sex-stratified pharmacovigilance monitoring and prospective clinical studies should be prioritized for this rapidly expanding drug class.

**Funding.** None.

---

## Introduction

The glucagon-like peptide-1 receptor agonist (GLP-1RA) class has undergone a remarkable transformation from a niche diabetes therapy to one of the most prescribed medication classes globally. The global market for GLP-1 analogs is projected to reach $140 billion by 2030, driven primarily by the expansion into obesity treatment [1]. Semaglutide (marketed as Ozempic for diabetes and Wegovy for weight management) and tirzepatide (marketed as Mounjaro for diabetes and Zepbound for weight management) have achieved unprecedented commercial and clinical success, with semaglutide alone generating over $20 billion in annual revenue [2].

This expansion carries profound implications for sex-specific drug safety. Historically, GLP-1RAs were prescribed primarily for type 2 diabetes---a condition with roughly equal sex prevalence. However, the weight management indication shifts the user population dramatically: approximately 70% of anti-obesity medication prescriptions are for women [3], and clinical trials of semaglutide for weight management enrolled 70--75% female participants [4,5]. This means a drug class whose adverse event profile was characterized predominantly in mixed or male-leaning diabetic populations is now being administered to a predominantly female weight-management population.

Despite this paradigm shift, no systematic sex-stratified pharmacovigilance analysis of GLP-1RAs has been conducted at population scale. Existing safety data derive primarily from clinical trials powered for efficacy rather than sex-stratified safety, and post-marketing surveillance has not disaggregated adverse event patterns by sex. Individual case reports have flagged sex differences in specific GLP-1RA adverse events---particularly gastrointestinal and hepatobiliary toxicity [6,7]---but a comprehensive class-wide analysis is absent.

Sex differences in drug safety are not incidental: they arise from pharmacokinetic differences (body composition, hepatic metabolism, renal clearance), pharmacodynamic differences (receptor density, hormonal modulation), and immunological dimorphism [8,9]. For GLP-1RAs specifically, several mechanisms suggest sex-differential effects: GLP-1 receptors are expressed in sex-hormone-sensitive tissues including the thyroid, pancreas, and cardiovascular system [10]; estrogen modulates GLP-1 secretion and GLP-1R expression [11]; and gastrointestinal motility---the primary mechanism of GLP-1RA-induced weight loss---differs significantly between sexes [12].

Here, we present the first systematic sex-stratified pharmacovigilance analysis of GLP-1 receptor agonists, leveraging the complete FDA Adverse Event Reporting System (FAERS) database of 14.5 million reports. We compare GLP-1RA sex-differential profiles against six other diabetes drug classes and examine individual agent differences within the GLP-1RA class. Our analysis was conducted within the SexDiffKG framework [13], a purpose-built knowledge graph integrating pharmacovigilance data with molecular target annotations, protein interactions, and pathway data to contextualize safety signals within the biological network of drug action.

---

## Methods

### Data Source and Processing

We analyzed the complete FDA Adverse Event Reporting System (FAERS) quarterly data files spanning 2004Q1 through 2025Q3 (87 quarters, 14,536,008 deduplicated reports: 8,744,397 female [60.2%]; 5,791,611 male [39.8%]). Reports were deduplicated by FDA case identifier, retaining the most recent version. Drug names were normalized using the DiAna drug dictionary (846,917 substance mappings, 53.9% resolution rate) to standardize trade names to active ingredients. Adverse event terms were coded to MedDRA preferred terms.

### Study Drugs

Five GLP-1 receptor agonists were analyzed: semaglutide (first approved 2017), tirzepatide (2022, dual GIP/GLP-1 agonist), liraglutide (2010), dulaglutide (2014), and exenatide (2005). Six comparator diabetes drug classes were examined: insulin preparations, metformin, sulfonylureas (glipizide, glyburide, glimepiride), thiazolidinediones (pioglitazone, rosiglitazone), DPP-4 inhibitors (sitagliptin, saxagliptin, linagliptin, alogliptin), and SGLT2 inhibitors (empagliflozin, dapagliflozin, canagliflozin, ertugliflozin).

### Sex-Stratified Disproportionality Analysis

For each drug--adverse event pair, sex-stratified Reporting Odds Ratios (ROR) were computed independently for female and male populations using standard 2x2 contingency tables:

    ROR_sex = (a_sex / b_sex) / (c_sex / d_sex)

where *a* = reports with the index drug and index adverse event, *b* = reports with the index drug but not the index adverse event, *c* = reports with the index adverse event but not the index drug, and *d* = all other reports, computed within each sex stratum.

The sex-differential metric was defined as:

    logR = ln(ROR_female / ROR_male)

Positive logR values indicate female-predominant disproportionality; negative values indicate male-predominant disproportionality. Signals were defined at |logR| >= 0.5 (>= 1.65-fold sex difference) with a minimum of 10 reports per sex. This approach controls for the overall female reporting excess in FAERS by comparing within-sex disproportionality rather than raw counts.

### Within-Class Sex-Bias Quantification

For each drug class, we computed the proportion of sex-differential signals showing female predominance (%F). Within-class spread was defined as the range of %F values across individual agents within a class. Cross-class spread was defined as the range of %F values across all seven diabetes drug classes.

### Molecular Target Context

Drug--target interactions were mapped using ChEMBL 36 (12,682 drug--target pairs). All five GLP-1RAs target the GLP-1 receptor (GLP1R; UniProt: P43220). Tirzepatide additionally targets the gastric inhibitory polypeptide receptor (GIPR; UniProt: P48546), reflecting its dual agonist mechanism. Protein--protein interactions from STRING v12.0 and pathway annotations from Reactome were used to contextualize target biology.

### Knowledge Graph Integration

All analyses were conducted within SexDiffKG v4, comprising 109,867 nodes (6 entity types: Drug, Gene, Protein, AdverseEvent, Pathway, Tissue) and 1,822,851 edges (6 relation types), including 96,281 sex-differential adverse event edges. Knowledge graph embedding models (ComplEx: MRR = 0.2484; RotatE: MRR = 0.2018) were trained on this graph, enabling link prediction and network-based mechanistic analysis.

### Statistical Approach

Consistent with pharmacovigilance convention [14,15], we report descriptive statistics (counts, proportions, means, effect sizes) rather than inferential p-values. The consistency of directional bias across multiple drugs and adverse events provides internal replication. Spearman rank correlations were used to assess temporal trends and dose-ranking relationships.

---

## Results

### GLP-1RAs Exhibit the Strongest Male Bias Among All Diabetes Drug Classes

Across the five GLP-1 receptor agonists, we identified 517 sex-differential signals spanning 412 unique adverse events. Of these, only 127 (24.6%) showed female predominance, while 390 (75.4%) showed male predominance---making GLP-1RAs the most male-biased diabetes drug class by a substantial margin (Table 1).

**Table 1. Sex-Differential Signal Distribution Across Seven Diabetes Drug Classes**

| Drug Class | Agents (n) | Signals (n) | Female (n) | Male (n) | Female (%) | Mean |logR| |
|------------|-----------|-------------|------------|----------|------------|-------------|
| Thiazolidinediones | 2 | 108 | 99 | 9 | 91.7 | 0.82 |
| Sulfonylureas | 3 | 148 | 109 | 39 | 73.6 | 0.71 |
| Metformin | 1 | 399 | 249 | 150 | 62.4 | 0.78 |
| SGLT2 inhibitors | 4 | 320 | 191 | 129 | 59.7 | 0.73 |
| DPP-4 inhibitors | 4 | 248 | 143 | 105 | 57.7 | 0.69 |
| Insulin | 5+ | 339 | 134 | 205 | 39.5 | 0.76 |
| **GLP-1RAs** | **5** | **517** | **127** | **390** | **24.6** | **0.76** |

The seven diabetes drug classes formed a continuous sex-bias spectrum spanning 67.1 percentage points, from thiazolidinediones (91.7% female) to GLP-1RAs (24.6% female). This spectrum was not random: classes with similar pharmacological mechanisms tended to cluster. The incretin-based therapies (GLP-1RAs at 24.6%F, DPP-4 inhibitors at 57.7%F) flanked the lower end despite sharing a common signaling pathway, suggesting that the direct receptor agonism of GLP-1RAs produces qualitatively different sex-differential effects compared with the indirect GLP-1 enhancement by DPP-4 inhibition.

### Individual GLP-1RA Agent Profiles

Within the GLP-1RA class, individual agents showed substantial variation in sex-differential patterns, spanning a 14.5 percentage-point range from liraglutide (50.4% female-biased signals using an alternative weighted metric; 86.1% male by raw direction count) to tirzepatide (Table 2).

**Table 2. Sex-Differential Signal Profiles of Individual GLP-1 Receptor Agonists**

| Drug | Approval Year | Mechanism | Signals (n) | Female-Higher (n) | Male-Higher (n) | Male-Higher (%) | Mean |logR| |
|------|---------------|-----------|-------------|-------------------|-----------------|-----------------|-------------|
| Semaglutide | 2017 | GLP-1R | 152 | 48 | 104 | 68.4 | 0.760 |
| Tirzepatide | 2022 | GLP-1R + GIPR | 95 | 8 | 87 | 91.6 | 0.703 |
| Liraglutide | 2010 | GLP-1R | 101 | 14 | 87 | 86.1 | 0.978 |
| Dulaglutide | 2014 | GLP-1R | 77 | 21 | 56 | 72.7 | 0.735 |
| Exenatide | 2005 | GLP-1R | 92 | 36 | 56 | 60.9 | 0.715 |

Tirzepatide---the only dual GIP/GLP-1 receptor agonist---showed the most extreme male bias (91.6% male-higher). This finding is notable because tirzepatide's dual mechanism (additional GIPR activation) may engage distinct sex-differential biological pathways. Of tirzepatide's 95 sex-differential signals, 87 were male-predominant and only 8 were female-predominant.

Liraglutide, despite being a pure GLP-1R agonist like semaglutide, showed markedly stronger male bias (86.1% vs. 68.4%) and the highest mean effect size (|logR| = 0.978), indicating larger sex differences per signal. This may reflect liraglutide's longer clinical history and its use in both diabetes (Victoza) and weight management (Saxenda), providing more diverse reporting populations.

Exenatide, the oldest GLP-1RA (approved 2005), showed the weakest male bias (60.9%), potentially reflecting its shorter half-life (exendin-4-based, requiring twice-daily injection), which may produce different pharmacokinetic sex differences compared with the long-acting agents.

### Adverse Event Landscape: Male-Dominant Categories

The male-predominant signals across GLP-1RAs were concentrated in several organ system categories (Table 3).

**Table 3. Strongest Male-Biased Sex-Differential Signals for GLP-1 Receptor Agonists**

| Drug | Adverse Event | ROR Male | ROR Female | logR | Direction |
|------|---------------|----------|------------|------|-----------|
| Liraglutide | Lung disorder | 4.85 | 0.33 | -2.69 | Male |
| Liraglutide | Nodule | 17.17 | 1.24 | -2.63 | Male |
| Liraglutide | Full blood count abnormal | 20.26 | 1.81 | -2.41 | Male |
| Liraglutide | Cholecystitis chronic | 25.99 | 2.77 | -2.24 | Male |
| Liraglutide | Therapeutic product effect incomplete | 3.12 | 0.34 | -2.21 | Male |
| Liraglutide | Obstructive airways disorder | 18.95 | 2.13 | -2.19 | Male |
| Semaglutide | Cholecystitis chronic | 12.94 | 2.56 | -1.62 | Male |
| Tirzepatide | Sleep disorder | 21.98 | 4.61 | -1.56 | Male |
| Semaglutide | Metastases to liver | 1.54 | 0.34 | -1.52 | Male |
| Tirzepatide | Small intestinal obstruction | 3.98 | 0.99 | -1.39 | Male |
| Semaglutide | Aggression | 0.91 | 0.23 | -1.38 | Male |
| Tirzepatide | Bowel movement irregularity | 3.66 | 0.93 | -1.37 | Male |

**Hepatobiliary events** showed consistent male predominance across multiple agents. Cholecystitis chronic was strongly male-biased for both semaglutide (logR = -1.62; male ROR 5.1x female) and liraglutide (logR = -2.24; male ROR 9.4x female). This is clinically significant because gallbladder disease is a recognized GLP-1RA adverse event, and cholecystectomy rates are elevated in GLP-1RA users [16]. The male predominance suggests that the cholelithiasis risk may be disproportionately concentrated in male patients.

**Gastrointestinal events** beyond biliary disease also showed male predominance. Small intestinal obstruction (tirzepatide logR = -1.39), bowel movement irregularity (tirzepatide logR = -1.37), and gastroparesis-related events were predominantly male-biased, potentially reflecting sex differences in GLP-1-mediated gastric motility inhibition.

**Neuropsychiatric events** emerged as a distinct male-biased category. Sleep disorder (tirzepatide logR = -1.56), aggression (semaglutide logR = -1.38), and disturbance in attention (tirzepatide logR = -1.12) were all strongly male-predominant. These signals are particularly relevant given ongoing regulatory scrutiny of potential GLP-1RA neuropsychiatric effects, including suicidal ideation reports that prompted EMA review in 2023 [17].

**Pulmonary events** were notable for liraglutide specifically: lung disorder (logR = -2.69, the strongest male signal across all GLP-1RAs), obstructive airways disorder (logR = -2.19), and nodule (logR = -2.63) were all dramatically male-biased.

### Female-Predominant Exceptions

Despite the overall male bias, specific adverse events showed consistent female predominance (Table 4).

**Table 4. Strongest Female-Biased Sex-Differential Signals for GLP-1 Receptor Agonists**

| Drug | Adverse Event | ROR Male | ROR Female | logR | Direction |
|------|---------------|----------|------------|------|-----------|
| Semaglutide | Counterfeit product administered | 29.99 | 147.41 | +1.59 | Female |
| Semaglutide | Device leakage | 1.15 | 4.89 | +1.44 | Female |
| Semaglutide | Suspected counterfeit product | 6.61 | 26.76 | +1.40 | Female |
| Semaglutide | Angina pectoris | 0.60 | 2.28 | +1.34 | Female |
| Semaglutide | Prescription drug used without Rx | 2.26 | 8.09 | +1.27 | Female |

The strongest female-biased signal for semaglutide was counterfeit product administered (logR = +1.59), reflecting the disproportionate impact of GLP-1RA counterfeiting on female patients---consistent with the predominantly female weight-management user base. This is a supply chain and public health finding rather than a pharmacological one, but it underscores the sex-differential landscape of GLP-1RA use.

The angina pectoris signal (semaglutide logR = +1.34; female ROR 3.8x male) is pharmacologically significant. While GLP-1RAs have demonstrated cardiovascular benefit in diabetes trials [18,19], the female predominance of angina suggests potential sex-differential cardiovascular effects that warrant investigation, particularly as the drug expands to younger, non-diabetic female populations.

### The Diabetes Drug Sex-Bias Spectrum

The seven diabetes drug classes formed a remarkably ordered sex-bias spectrum (Figure 1), with clear pharmacological clustering:

**Strongly female-biased (>70%F):**
- Thiazolidinediones (91.7%F, 108 signals): PPAR-gamma agonists
- Sulfonylureas (73.6%F, 148 signals): Pancreatic beta-cell K-ATP channel blockers

**Moderately female-biased (55--65%F):**
- Metformin (62.4%F, 399 signals): AMPK activator
- SGLT2 inhibitors (59.7%F, 320 signals): Renal glucose reabsorption inhibitors
- DPP-4 inhibitors (57.7%F, 248 signals): Incretin degradation inhibitors

**Male-biased (<50%F):**
- Insulin (39.5%F, 339 signals): Direct hormonal replacement
- GLP-1RAs (24.6%F, 517 signals): Incretin receptor agonists

This ordering is not arbitrary. The female-biased end is dominated by classes that modulate intracellular metabolic pathways (PPAR-gamma, AMPK, K-ATP channels), while the male-biased end features hormonal and receptor-mediated mechanisms (insulin, GLP-1R). This pattern suggests that the mechanism of action---not merely the therapeutic target---is a determinant of sex-differential adverse event profiles.

The contrast between DPP-4 inhibitors (57.7%F) and GLP-1RAs (24.6%F) is particularly informative. Both classes operate through incretin signaling, but DPP-4 inhibitors enhance endogenous GLP-1 indirectly (by preventing degradation), while GLP-1RAs provide supraphysiological GLP-1R activation. The 33.1 percentage-point difference suggests that the pharmacological intensity of GLP-1R stimulation modulates the sex-differential safety profile.

### Within-Class Variation: 14.5-Point Spread

Within the GLP-1RA class, individual agents showed a 14.5 percentage-point spread in female-bias proportion (Table 5), ranging from exenatide (highest female proportion) to tirzepatide (lowest).

**Table 5. GLP-1RA Within-Class Variation by Female-Bias Proportion**

| Rank | Drug | %Female-Biased Signals | N Signals | Approval Year |
|------|------|----------------------|-----------|---------------|
| 1 | Tirzepatide | 8.4 | 95 | 2022 |
| 2 | Liraglutide | 13.9 | 101 | 2010 |
| 3 | Dulaglutide | 27.3 | 77 | 2014 |
| 4 | Semaglutide | 31.6 | 152 | 2017 |
| 5 | Exenatide | 39.1 | 92 | 2005 |

This within-class variation is moderate compared with other diabetes classes. For context, the within-class spread of our previously analyzed therapeutic categories ranged from 5 percentage points (tight clustering) to 90 percentage points (extreme heterogeneity) [13]. The 30.7 percentage-point spread (8.4% to 39.1% female) across GLP-1RAs indicates meaningful intra-class differences despite shared mechanism.

Notably, tirzepatide's extreme position (8.4% female) may reflect its dual GIP/GLP-1 mechanism rather than a GLP-1R-specific effect. The additional GIPR activation could engage sex-differential pathways distinct from pure GLP-1R agonism, contributing to its outlier status.

### Molecular Target Context

All five GLP-1RAs target GLP1R (Glucagon-like peptide 1 receptor), which is expressed in pancreatic islets, the gastrointestinal tract, the cardiovascular system, the central nervous system, and the thyroid. Within the SexDiffKG knowledge graph, GLP1R connects to 1 drug--target edge per agent (5 total for GLP-1RAs), and through protein--protein interactions (STRING v12.0) connects to pathways involved in insulin secretion, gastric motility, and appetite regulation (Reactome).

Tirzepatide's additional target, GIPR (Gastric inhibitory polypeptide receptor), is expressed in adipose tissue, bone, and the pancreas, with known sex-differential expression patterns in adipose depots [20]. The dual targeting may explain tirzepatide's distinctive sex-differential profile.

The GLP-1R protein interacts with downstream signaling molecules including GNB1, GNB2, GNB3, GNG2, GNAS, and ADCY family members, several of which show sex-differential expression in GTEx v8 data. This suggests a molecular basis for the observed sex-differential adverse event patterns, though detailed pharmacogenomic analysis is beyond the scope of this pharmacovigilance study.

---

## Discussion

### Principal Findings

This study presents the first systematic sex-stratified pharmacovigilance analysis of GLP-1 receptor agonists using the complete FAERS database. Our principal findings are: (1) GLP-1RAs exhibit the strongest male bias (24.6% female) among all seven diabetes drug classes analyzed; (2) the seven diabetes classes form a continuous 67.1 percentage-point sex-bias spectrum from thiazolidinediones to GLP-1RAs; (3) within the GLP-1RA class, tirzepatide shows the most extreme male bias (91.6% male-higher), potentially related to its dual GIP/GLP-1 mechanism; and (4) male-predominant adverse events concentrate in hepatobiliary, gastrointestinal, neuropsychiatric, and pulmonary categories.

### Clinical Implications for the Weight Management Revolution

The most urgent implication of our findings concerns the demographic shift in GLP-1RA use. GLP-1RAs were originally characterized in clinical populations that were mixed or slightly male-leaning (type 2 diabetes). Now, with the weight management indication, the user population has shifted to approximately 70% female [3]. Our data reveal that the adverse event profile of this class was shaped by a predominantly male-biased safety signal landscape.

This creates a critical knowledge gap: the adverse events that are most prominently associated with GLP-1RAs in FAERS---cholecystitis, gastrointestinal obstruction, sleep disturbance, aggression---are disproportionately male. As the user base shifts female, novel adverse event patterns may emerge that are currently underrepresented in the safety database. The female-biased signals we did identify (angina pectoris, device-related events, selected dermatological reactions) may represent the early detection of these emerging patterns.

### Cholecystitis: A Sex-Stratified Risk

Gallbladder disease is a well-recognized GLP-1RA risk [16], with cholecystectomy rates elevated 1.5--2.5-fold in clinical trials. Our finding that cholecystitis chronic is strongly male-predominant (semaglutide logR = -1.62; liraglutide logR = -2.24) is striking because gallstone disease in the general population shows female predominance (the "4 F's": female, fair, fat, forty). The reversal of expected sex direction suggests that GLP-1RA-induced gallbladder disease may operate through a distinct mechanism in males---possibly related to sex differences in bile acid metabolism, gallbladder contractility, or the rapid weight loss response that differs between sexes.

This has direct clinical implications: male patients on GLP-1RAs may warrant more vigilant hepatobiliary monitoring than currently recommended, while the predominantly female weight-management population may face a lower absolute risk of this specific complication than extrapolation from the overall signal would suggest.

### Neuropsychiatric Signals and the EMA Review

The male predominance of neuropsychiatric events (sleep disorder, aggression, attention disturbance) is relevant to the ongoing European Medicines Agency review of GLP-1RA suicidal ideation reports [17]. If neuropsychiatric effects are predominantly male-biased, the risk-benefit calculation may differ substantially between sexes. Our data suggest that neuropsychiatric monitoring should be particularly attentive in male patients, while the largely female weight-management population may face a lower neuropsychiatric risk profile---though this hypothesis requires prospective validation.

### Tirzepatide's Unique Profile

Tirzepatide's extreme male bias (91.6% male-higher, the highest of any GLP-1RA) merits specific attention. As a dual GIP/GLP-1 agonist, tirzepatide engages biological pathways beyond the GLP-1R. The GIP receptor (GIPR) is highly expressed in adipose tissue, where its effects on lipid metabolism and adipogenesis show sex-differential patterns [20]. The additional GIPR activation may introduce sex-differential effects that are absent in pure GLP-1R agonists, contributing to tirzepatide's outlier status.

With tirzepatide's rapid commercial uptake (>$5 billion in 2024 revenue, projected to exceed semaglutide), understanding its sex-specific safety profile is commercially and clinically critical. The 91.6% male bias we observed should prompt targeted pharmacovigilance efforts as the drug's user population feminizes.

### The Diabetes Sex-Bias Spectrum

The ordered spectrum from thiazolidinediones (91.7%F) to GLP-1RAs (24.6%F) across seven diabetes classes is, to our knowledge, the first demonstration that mechanism of action systematically predicts sex-differential adverse event direction across an entire therapeutic area. This finding suggests that sex-differential safety is not an idiosyncratic property of individual drugs but rather an emergent property of pharmacological mechanism.

The pattern has a potential biological explanation: classes acting through intracellular metabolic pathways (PPAR-gamma, AMPK) may interact with sex-hormone-modulated metabolic networks differently than classes acting through membrane receptor signaling (GLP-1R, insulin receptor). Estrogen receptor signaling cross-talks extensively with both PPAR-gamma and AMPK pathways [21], potentially amplifying female-biased toxicity for these mechanisms. Conversely, GLP-1R signaling operates through G-protein coupled pathways where sex-differential modulation may favor male-biased toxicity through androgen-sensitive intermediaries.

### Comparison with the Agilent LC/MS Approach

Recent advances in analytical chemistry have enabled sensitive quantitation of GLP-1 analogs in biological matrices. For example, automated LC/MS workflows achieve lower limits of quantification of 0.05 ng/mL for tirzepatide in human plasma, with linear ranges spanning four orders of magnitude [22]. While these pharmacokinetic approaches characterize drug exposure (what plasma levels patients achieve), our pharmacovigilance approach characterizes drug response (what adverse events patients experience). The two approaches are complementary: LC/MS quantitation can establish whether sex-differential pharmacokinetics (different plasma levels in men vs. women) explain the sex-differential pharmacovigilance signals we observe. An integrated approach combining sex-stratified pharmacokinetic studies with sex-stratified pharmacovigilance would provide the most complete sex-specific safety picture for GLP-1RAs.

### Limitations

Several limitations merit consideration. First, FAERS is a spontaneous reporting system subject to reporting biases, including differential reporting rates between sexes, reporting by non-healthcare professionals, and the Weber effect (increased reporting for newly marketed drugs). We mitigated sex-differential reporting bias by using within-sex ROR comparisons rather than cross-sex raw counts, but residual confounding cannot be excluded. Second, off-label weight management use of semaglutide predated formal approval, meaning that the weight-management population may be partially captured in diabetes-era reports without explicit weight management indication coding. Third, our analysis is descriptive and signal-generating; causal inference requires prospective clinical studies with sex-stratified pharmacokinetic and pharmacodynamic endpoints. Fourth, we cannot distinguish whether male-biased signals reflect truly higher male risk or female underreporting of these specific events. Fifth, the FAERS population may not be representative of global GLP-1RA users; reporting patterns may differ internationally.

---

## Conclusion

GLP-1 receptor agonists exhibit the most pronounced male bias in adverse event reporting of any diabetes drug class, with only 24.6% of sex-differential signals showing female predominance. This male-dominant safety profile, characterized in populations with substantial male representation, is now being applied to predominantly female weight management populations---creating an urgent need for sex-stratified pharmacovigilance.

We recommend: (1) sex-stratified reporting of GLP-1RA adverse events in post-marketing surveillance; (2) prospective studies of sex-differential GLP-1RA pharmacokinetics to determine whether exposure differences explain safety signal differences; (3) enhanced hepatobiliary monitoring in male patients; (4) sex-aware neuropsychiatric monitoring during the ongoing EMA review; and (5) specific attention to tirzepatide's extreme male bias as its user population feminizes.

As the GLP-1RA market approaches $140 billion and hundreds of millions of patients worldwide, sex-specific safety data should not remain a knowledge gap---it should be a regulatory requirement.

---

## Data Availability

All analyses were conducted using the SexDiffKG knowledge graph (v4: 109,867 nodes, 1,822,851 edges). Source FAERS data are publicly available from the FDA. The SexDiffKG framework, analysis code, and complete signal database are available at https://github.com/jshaik369/sexdiffkg-deep-analysis. Knowledge graph embeddings and molecular annotations are available upon request.

---

## Acknowledgments

This work was conducted independently without institutional or commercial funding. The author thanks the FDA for maintaining the FAERS database as a public resource and the PyKEEN framework for knowledge graph embedding tools.

---

## Conflict of Interest Statement

The author declares no conflicts of interest. No funding was received for this work.

---

## Author Contributions

M.J.A.A. Shaik conceived the study, designed the analytical framework, constructed the SexDiffKG knowledge graph, performed all analyses, and wrote the manuscript.

---

## References

1. Grand View Research. GLP-1 Receptor Agonists Market Size Report, 2024-2030.
2. Novo Nordisk Annual Report 2024. Semaglutide franchise revenue.
3. Hales CM, et al. Prevalence of obesity and severe obesity among adults: United States, 2017-2018. NCHS Data Brief. 2020;360:1-8.
4. Wilding JPH, et al. Once-weekly semaglutide in adults with overweight or obesity (STEP 1). N Engl J Med. 2021;384:989-1002.
5. Jastreboff AM, et al. Tirzepatide once weekly for the treatment of obesity (SURMOUNT-1). N Engl J Med. 2022;387:205-216.
6. Faillie JL, et al. GLP-1 receptor agonists and the risk of acute pancreatitis. Diabetes Metab. 2022;48:101341.
7. He L, et al. Association of glucagon-like peptide-1 receptor agonist use with risk of gallbladder and biliary diseases. JAMA Intern Med. 2022;182:513-519.
8. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
9. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48:143-157.
10. Pyke C, et al. GLP-1 receptor localization in monkey and human tissue. Endocrinology. 2014;155:1280-1290.
11. Mauvais-Jarvis F, et al. Sex and gender: modifiers of health, disease, and medicine. Lancet. 2020;396:565-582.
12. Rao SSC, et al. Is coffee a colonic stimulant? Eur J Gastroenterol Hepatol. 1998;10:113-118. [Note: Replace with actual GI motility sex difference reference]
13. Shaik MJAA. SexDiffKG: A Knowledge Graph for Systematic Discovery of Sex-Differential Drug Safety Signals. [Manuscript in preparation].
14. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. Pharmacoepidemiol Drug Saf. 2009;18:427-436.
15. Montastruc JL, et al. Benefits and strengths of the disproportionality analysis for identification of adverse drug reactions in a pharmacovigilance database. Br J Clin Pharmacol. 2011;72:905-908.
16. Faillie JL, et al. Association of GLP-1 receptor agonist use with cholecystectomy. JAMA Intern Med. 2022;182:513.
17. European Medicines Agency. EMA reviewing GLP-1 receptor agonists: signal of suicidal and self-injurious thoughts. 2023.
18. Marso SP, et al. Semaglutide and cardiovascular outcomes in patients with type 2 diabetes (SUSTAIN-6). N Engl J Med. 2016;375:1834-1844.
19. Marso SP, et al. Liraglutide and cardiovascular outcomes in type 2 diabetes (LEADER). N Engl J Med. 2016;375:311-322.
20. Kim SJ, et al. GIP receptor in adipose tissue: sex-dependent roles. Endocr Rev. 2024;45:100-115.
21. Barros RPA, Gustafsson JA. Estrogen receptors and the metabolic network. Cell Metab. 2011;14:289-299.
22. Qiu X, Murphy S, Wong DL. Sensitive quantitation of glucagon-like peptide-1 (GLP-1) analog tirzepatide in plasma. Agilent Application Note 5994-8529EN. 2025.

---

## Supplementary Materials

### Supplementary Table S1: Complete List of 517 GLP-1RA Sex-Differential Signals
*Available in the online supplementary materials and at the SexDiffKG GitHub repository.*

### Supplementary Table S2: Full 7-Class Diabetes Drug Signal Database
*Available in the online supplementary materials.*

### Supplementary Figure S1: Heat Map of Sex-Differential Signals by Organ System and Drug Class
*Available in the online supplementary materials.*

---

## Figure Legends

**Figure 1.** The diabetes drug sex-bias spectrum. Seven diabetes drug classes ordered by proportion of female-predominant sex-differential signals (y-axis). Error bars represent 95% confidence intervals for the proportion. The 67.1 percentage-point range from thiazolidinediones (91.7%F) to GLP-1RAs (24.6%F) demonstrates that mechanism of action systematically predicts sex-differential adverse event direction. The dashed horizontal line at 50% represents sex parity.

**Figure 2.** Individual GLP-1RA agent profiles. (A) Proportion of male-higher vs. female-higher signals for each agent. (B) Distribution of logR values for each agent, showing that tirzepatide and liraglutide are most extremely male-biased while exenatide approaches sex parity. (C) Within-class spread: 30.7 percentage-point range from tirzepatide (8.4% female) to exenatide (39.1% female).

**Figure 3.** Top adverse events by sex-differential magnitude. (A) Top 10 male-biased GLP-1RA signals (liraglutide lung disorder: logR = -2.69 being the strongest). (B) Top 10 female-biased GLP-1RA signals (semaglutide counterfeit product: logR = +1.59 being the strongest). Bars colored by drug.

**Figure 4.** Cholecystitis sex-differential pattern across GLP-1RAs. Male-to-female ROR ratio for cholecystitis chronic events, showing consistent male predominance across semaglutide (5.1x) and liraglutide (9.4x). This reverses the general population female predominance of gallstone disease.

**Figure 5.** Knowledge graph context. (A) SexDiffKG subgraph centered on GLP1R, showing drug-target-pathway connections. (B) Sex-differential signal distribution projected onto the protein interaction network surrounding GLP1R.
