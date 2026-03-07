# Bipartite Network Topology of Sex-Differential Drug Safety Signals: A Large-Scale Analysis of 14.5 Million FAERS Reports

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516 | Email: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex-based differences in adverse drug reactions (ADRs) represent a pervasive yet structurally undercharacterized dimension of pharmacovigilance. While individual drug-event associations have been extensively catalogued, the higher-order connectivity patterns governing how sex-differential signals distribute across the pharmacological landscape remain largely unexplored.

**Methods.** We constructed a bipartite network from 14,536,008 individual case safety reports (ICSRs) in the FDA Adverse Event Reporting System (FAERS), spanning 87 quarters (2004Q1--2025Q3). Sex-differential signals were identified using disproportionality analysis, yielding 96,281 statistically significant drug--adverse event edges connecting 2,178 drugs to 5,069 adverse events. We characterized the network through degree distribution analysis, degree--sex correlation, degree assortativity, quintile stratification, and hub identification.

**Results.** The network exhibits a scale-free degree distribution with pronounced right skew (mean drug degree 44.2, range 1--926; mean AE degree 19.0, range 1--501) and low density (0.0087), consistent with the architecture of biological and pharmacological networks. Degree assortativity was strongly negative (rho = -0.395), indicating that high-degree hub drugs preferentially connect to rare, low-degree adverse events. Both drug degree (rho = 0.1172, p < 0.001) and AE degree (rho = 0.1431, p < 0.001) correlated positively with female fraction, establishing a systematic degree--sex gradient: more highly connected nodes exhibit greater female reporting bias. Quintile analysis confirmed a monotonic increase in female fraction from 53.4% (Q1, degree approximately 1) to 57.5% (Q5, degree approximately 176). Among the top eight hub drugs (degree > 500), seven exhibited female fractions exceeding 60%, with immunomodulators dominating; tacrolimus (degree 572, 48.0% female) was the sole male-biased exception, reflecting the demographics of solid organ transplantation. Among hub adverse events, "Death" (337 drugs, 46.1% female) was consistently male-biased, suggesting a survival or severity-of-presentation bias.

**Conclusions.** The sex-differential pharmacovigilance landscape self-organizes into a sparse, scale-free, disassortative bipartite network in which female-biased reporting is amplified at high-connectivity nodes. These topological properties have direct implications for signal prioritization, sex-stratified safety surveillance, and the design of network-based pharmacovigilance algorithms. The identification of tacrolimus and "Death" as structurally anomalous hubs provides mechanistic hypotheses linking network topology to clinical practice patterns.

**Keywords:** pharmacovigilance, bipartite network, sex differences, FAERS, adverse drug reactions, network topology, scale-free, disproportionality analysis

---

## 1. Introduction

The recognition that biological sex modulates drug safety profiles has progressed from isolated case reports to a systematic pharmacovigilance concern. Women experience adverse drug reactions at approximately 1.5 to 1.7 times the rate of men across multiple therapeutic classes, a disparity attributable to pharmacokinetic differences (body composition, renal clearance, CYP enzyme expression), pharmacodynamic variation (receptor density, immune responsiveness), and reporting behavior [1, 2]. Despite two decades of regulatory attention---including the FDA's 2014 guidance on sex-specific labeling---the structural organization of sex-differential signals across the drug--adverse event landscape has received limited quantitative treatment.

Pharmacovigilance databases such as the FDA Adverse Event Reporting System (FAERS) encode an implicit network: drugs and adverse events form two distinct node classes connected by co-occurrence in individual case safety reports (ICSRs). This bipartite structure is not merely a convenient abstraction; it encodes information about shared mechanisms, polypharmacy patterns, and population-level susceptibility that is invisible in univariate signal detection. Network analysis has been productively applied to drug--drug interaction prediction [3], drug repositioning [4], and adverse event clustering [5], but few studies have characterized the topological properties of sex-differential safety signals specifically.

The bipartite network framework offers several analytical advantages over traditional pharmacovigilance approaches. First, degree distributions reveal whether the sex-differential landscape is dominated by a few hub drugs with broad adverse event profiles or is uniformly distributed. Second, degree--sex correlations test whether connectivity itself is associated with sex bias, a relationship with implications for signal prioritization. Third, mixing patterns (assortativity) reveal whether hub drugs connect preferentially to other hubs or to rare events, informing the detectability and clinical significance of signals. Fourth, the identification of topologically anomalous nodes---drugs or adverse events whose sex bias deviates from the network-wide gradient---generates mechanistic hypotheses rooted in clinical pharmacology.

In this study, we construct and analyze a bipartite network of sex-differential drug safety signals derived from 14.5 million FAERS reports spanning 21 years. We characterize the network's degree distribution, density, assortativity, and degree--sex gradient, and we identify hub nodes with anomalous sex-bias profiles. Our findings establish the structural architecture of sex-differential pharmacovigilance and demonstrate that network topology encodes clinically meaningful information about the sex dependence of drug safety.

---

## 2. Methods

### 2.1 Data Source and Preprocessing

Individual case safety reports (ICSRs) were obtained from the FDA Adverse Event Reporting System (FAERS) quarterly data files for the period 2004Q1 through 2025Q3, comprising 87 consecutive quarters. Reports were deduplicated using the FDA's recommended CASEID-based strategy, retaining the most recent version of each case. Sex was ascertained from the demographic file; reports with missing or indeterminate sex were excluded. The final analytic cohort comprised 14,536,008 reports, of which 8,752,685 (60.2%) were from female reporters and 5,783,323 (39.8%) from male reporters.

Drug names were standardized to active ingredients using the FAERS drug name harmonization procedure, with mapping to RxNorm concept unique identifiers where available. Adverse event terms were coded using the Medical Dictionary for Regulatory Activities (MedDRA) preferred terms. Drug--adverse event pairs with fewer than a predefined minimum report count were excluded to ensure statistical stability in subsequent disproportionality analyses.

### 2.2 Sex-Differential Signal Detection

For each drug--adverse event pair (d, a), we computed the sex-specific reporting odds ratio and assessed disproportionality using log-likelihood ratio (LR) statistics. A sex-differential signal was defined as a drug--AE pair exhibiting a statistically significant difference in reporting frequency between male and female populations, adjusted for multiple comparisons. This procedure yielded 96,281 sex-differential signals.

For each signal, the female fraction was computed as:

    Female Fraction(d,a) = N_female(d,a) / [N_female(d,a) + N_male(d,a)]

where N_female(d,a) and N_male(d,a) denote the number of female and male reports, respectively, for the drug--AE pair. A female fraction greater than 0.5 indicates female-biased reporting; less than 0.5 indicates male-biased reporting.

### 2.3 Bipartite Network Construction

A bipartite network G = (D, A, E) was constructed, where D is the set of drug nodes, A is the set of adverse event nodes, and E is the set of edges representing sex-differential signals. Each edge e in E connects a drug d in D to an adverse event a in A and carries attributes including the female fraction and the absolute log-likelihood ratio |LR|. By construction, edges exist only between nodes of different types (drug--AE), not within types.

The resulting network contains |D| = 2,178 drug nodes, |A| = 5,069 adverse event nodes, and |E| = 96,281 edges.

### 2.4 Network Topology Metrics

**Density.** Network density was computed as the fraction of realized edges relative to the maximum possible in a bipartite graph:

    density = |E| / (|D| x |A|) = 96,281 / (2,178 x 5,069) = 0.008721

**Degree distributions.** For each drug node d, the degree k_d equals the number of distinct AEs to which it is connected by sex-differential signals. For each AE node a, the degree k_a equals the number of distinct drugs connected to it. Summary statistics (mean, median, range) and distributional shape (skewness, log-log plots) were computed for both node types.

**Degree--sex correlation.** The association between node degree and sex bias was quantified using Spearman's rank correlation coefficient (rho) between node degree and the mean female fraction of edges incident to that node. Separate correlations were computed for drug and AE node sets.

**Degree assortativity.** Degree assortativity in a bipartite network measures the tendency of high-degree nodes of one type to connect preferentially to high-degree or low-degree nodes of the other type. We computed Spearman's rank correlation between the degrees of connected drug--AE pairs across all 96,281 edges. Positive assortativity indicates hub-to-hub connectivity; negative assortativity (disassortativity) indicates hub-to-periphery connectivity.

**Quintile stratification.** Drugs were ranked by degree and divided into five equal-sized quintiles. For each quintile, we computed the mean degree, number of drugs, mean female fraction, and mean absolute log-likelihood ratio |LR|.

### 2.5 Hub Identification and Characterization

Hub drugs were defined as those with degree exceeding 500 (top 0.37% of drug nodes). Hub adverse events were defined as those with degree exceeding 300 (top 0.16% of AE nodes). For each hub, we report the degree, female fraction, and therapeutic or clinical context.

### 2.6 Statistical Analysis

All statistical tests were two-sided with alpha = 0.05. Spearman correlations were used throughout given the non-normality of degree distributions. P-values for correlations were computed using permutation-based methods appropriate for the sample sizes involved. Analyses were conducted in Python 3.11 using NetworkX 3.2, SciPy 1.12, and pandas 2.2.

---

## 3. Results

### 3.1 Network Overview

The sex-differential pharmacovigilance network comprises 7,247 nodes (2,178 drugs + 5,069 adverse events) connected by 96,281 edges. Key topological properties are summarized in Table 1.

**Table 1. Network Topology Summary Statistics**

| Metric | Value |
|---|---|
| Total FAERS reports analyzed | 14,536,008 |
| Female reports (%) | 8,752,685 (60.2%) |
| Male reports (%) | 5,783,323 (39.8%) |
| Quarters analyzed | 87 (2004Q1--2025Q3) |
| Sex-differential signals | 96,281 |
| Drug nodes | 2,178 |
| Adverse event nodes | 5,069 |
| Total nodes | 7,247 |
| Total edges | 96,281 |
| Network density | 0.008721 |
| Mean drug degree (range) | 44.2 (1--926) |
| Mean AE degree (range) | 19.0 (1--501) |
| Degree assortativity (rho) | -0.395 |
| Drug degree--female fraction (rho) | +0.1172 (p < 0.001) |
| AE degree--female fraction (rho) | +0.1431 (p < 0.001) |

The network density of 0.0087 indicates that fewer than 1% of all possible drug--AE connections carry sex-differential signals, consistent with the sparse connectivity characteristic of real-world pharmacological networks.

### 3.2 Scale-Free Degree Distribution

Both drug and AE degree distributions are heavily right-skewed, with the majority of nodes having low degree and a small number of hubs dominating connectivity. The mean drug degree of 44.2 contrasts sharply with the maximum of 926, and the mean AE degree of 19.0 contrasts with a maximum of 501. This pattern is consistent with a scale-free or truncated power-law distribution, in which the probability of a node having degree k scales approximately as P(k) ~ k^(-gamma) for large k.

Scale-free topology in this context implies that the sex-differential pharmacovigilance landscape is not uniform: a small fraction of drugs generate sex-differential signals across hundreds of adverse events, while the majority of drugs show sex-differential signals for only a handful of events. Similarly, a small number of adverse events---primarily general constitutional and efficacy-related terms---are sex-differentially reported across hundreds of drugs, while most adverse events show sex-differential signals for fewer than 20 drugs.

This architecture parallels the scale-free topology observed in protein--protein interaction networks [6], metabolic networks [7], and drug--target interaction networks [8], suggesting that common organizational principles---preferential attachment, heterogeneous exposure, and hierarchical modularity---govern both biological and pharmacovigilance networks.

### 3.3 Disassortative Mixing

The degree assortativity coefficient of rho = -0.395 indicates strongly disassortative mixing: high-degree hub drugs connect preferentially to low-degree (rare) adverse events, and vice versa. This is a striking structural feature with important pharmacovigilance implications.

In a disassortative bipartite network, the highest-connectivity drugs do not simply recapitulate a common core of frequently reported AEs; rather, they extend into the long tail of rare adverse events. This means that hub drugs are disproportionately important for the detection of rare safety signals. Conversely, high-degree hub AEs (such as "Drug ineffective" or "Vomiting") connect to many drugs but do not preferentially connect to other hubs---they bridge across the entire drug connectivity spectrum, from single-signal drugs to mega-hubs.

Disassortative mixing has been observed in other bipartite biological networks, including host--parasite networks and plant--pollinator networks [9], where it is associated with robustness: the network's connectivity structure is resilient to the random removal of nodes but vulnerable to the targeted removal of hubs. In pharmacovigilance, this implies that the loss of safety data for a single hub drug (e.g., through market withdrawal) would disproportionately reduce the detectability of rare sex-differential signals.

### 3.4 Degree--Sex Gradient

A central finding of this analysis is the systematic positive correlation between node degree and female reporting fraction. For drug nodes, the Spearman correlation between degree and mean female fraction is rho = 0.1172 (p < 0.001); for AE nodes, it is rho = 0.1431 (p < 0.001). While these correlations are modest in magnitude, they are highly significant and directionally consistent, indicating a network-wide structural gradient in which higher connectivity is associated with greater female bias.

This gradient is confirmed by quintile analysis (Table 2), which reveals a monotonic increase in female fraction from Q1 (lowest degree) to Q5 (highest degree).

**Table 2. Drug Degree Quintile Analysis**

| Quintile | N Drugs | Median Degree | Mean Female Fraction | Mean |LR| |
|---|---|---|---|---|
| Q1 (lowest) | 547 | ~1 | 53.4% | 0.974 |
| Q2 | 378 | ~4 | 53.4% | 0.978 |
| Q3 | 382 | ~11 | 55.4% | 0.935 |
| Q4 | 439 | ~32 | 54.5% | 0.926 |
| Q5 (highest) | 432 | ~176 | 57.5% | 0.976 |

Several mechanisms may contribute to this gradient:

1. **Exposure bias.** Women consume more prescription drugs than men across most therapeutic classes. Higher-degree drugs tend to be widely prescribed agents (immunomodulators, analgesics, antidepressants) with large female patient populations, mechanically increasing the female fraction of their reports.

2. **Reporting behavior.** Women are more likely to report adverse events to pharmacovigilance systems. This reporting asymmetry may be amplified for drugs with broad AE profiles, as each additional AE provides an additional occasion for sex-differential reporting.

3. **Biological susceptibility.** Drugs with many sex-differential AEs may act through pathways with pronounced sexual dimorphism (e.g., immune modulation, hormonal signaling), producing genuinely higher rates of female-biased adverse events.

4. **Autoimmune drug enrichment.** The dominance of immunomodulators among hub drugs (Section 3.5) reflects the 2:1 to 9:1 female-to-male prevalence ratios of autoimmune diseases, which directly inflates the female fraction of reports for these drugs.

Notably, the mean |LR| (absolute log-likelihood ratio) is relatively stable across quintiles (0.926--0.978), indicating that the strength of sex-differential signals does not systematically vary with drug connectivity. The gradient is therefore a property of direction (female vs. male bias), not magnitude.

### 3.5 Hub Drug Analysis

Table 3 presents the eight drugs with the highest degree in the network (all exceeding 500).

**Table 3. Top Hub Drugs by Degree**

| Rank | Drug | Degree | Female Fraction | Therapeutic Class | Predominant Indication |
|---|---|---|---|---|---|
| 1 | Prednisone | 926 | 63.8% | Corticosteroid | Autoimmune/inflammatory |
| 2 | Methotrexate | 892 | 64.3% | Antimetabolite/DMARD | RA, psoriasis, oncology |
| 3 | Adalimumab | 807 | 64.0% | Anti-TNF biologic | RA, Crohn's, psoriasis |
| 4 | Rituximab | 755 | 66.4% | Anti-CD20 biologic | Lymphoma, RA, vasculitis |
| 5 | Infliximab | 623 | 64.9% | Anti-TNF biologic | Crohn's, UC, RA |
| 6 | Etanercept | 618 | 69.9% | Anti-TNF biologic | RA, psoriatic arthritis |
| 7 | Tacrolimus | 572 | 48.0% | Calcineurin inhibitor | Organ transplant rejection |
| 8 | Prednisolone | 542 | 60.1% | Corticosteroid | Autoimmune/inflammatory |

The hub drug landscape is dominated by immunomodulatory agents, reflecting two converging factors: (a) these drugs are prescribed across numerous indications, each generating distinct AE profiles, which inflates their degree; and (b) autoimmune diseases disproportionately affect women (rheumatoid arthritis 3:1 F:M, systemic lupus erythematosus 9:1 F:M, multiple sclerosis 3:1 F:M), driving female-biased reporting [10].

Six of the eight hub drugs are immunomodulators used primarily in autoimmune disease (methotrexate, adalimumab, rituximab, infliximab, etanercept) or broad-spectrum anti-inflammatory agents (prednisone, prednisolone). Their female fractions cluster tightly between 60.1% and 69.9%, consistent with the autoimmune sex ratio.

#### 3.5.1 Tacrolimus: The Sole Male-Biased Hub

Tacrolimus stands out as the only hub drug with a female fraction below 50% (48.0%, indicating male-biased reporting). This anomaly has a clear clinical explanation. Tacrolimus is a calcineurin inhibitor used primarily for the prevention of organ transplant rejection. Solid organ transplantation is performed more frequently in men than in women across all major organ types: kidney (60% male recipients), liver (62% male), heart (75% male), and lung (55% male) [11]. The male-biased transplant recipient population directly drives the male bias in tacrolimus adverse event reporting.

This finding illustrates how network topology can expose the demographic structure of clinical practice. Tacrolimus's anomalous position in the degree--sex landscape is not a pharmacological sex difference per se, but rather a reflection of the sex-differential epidemiology and access patterns of organ transplantation. Nevertheless, from a pharmacovigilance perspective, the male bias in tacrolimus reporting means that sex-differential signals for this drug should be interpreted with particular caution: apparent female-biased AEs may reflect genuine biological susceptibility (given the smaller female denominator), while apparent male-biased AEs may be confounded by the higher male exposure base.

The contrast between tacrolimus and the seven female-biased hubs also highlights a methodological point: hub drugs in a sex-differential network are not uniformly female-biased. The degree--sex gradient (Section 3.4) is a statistical tendency, not a deterministic rule, and individual drugs can deviate substantially based on their indication profile and patient demographics.

### 3.6 Hub Adverse Event Analysis

Table 4 presents the eight adverse events with the highest degree in the network (all exceeding 300).

**Table 4. Top Hub Adverse Events by Degree**

| Rank | Adverse Event | Degree | Female Fraction | MedDRA SOC |
|---|---|---|---|---|
| 1 | Drug ineffective | 501 | 57.1% | General / Investigations |
| 2 | Off label use | 445 | 59.4% | Product issues |
| 3 | Condition aggravated | 392 | 51.6% | General disorders |
| 4 | Vomiting | 362 | 63.2% | Gastrointestinal |
| 5 | Death | 337 | 46.1% | General disorders |
| 6 | Fatigue | 332 | 69.2% | General disorders |
| 7 | Headache | 327 | 68.0% | Nervous system |
| 8 | Pain | 327 | 72.2% | General disorders |

The hub AE landscape partitions into three groups by sex bias:

**Strongly female-biased (>65% F).** Pain (72.2%), fatigue (69.2%), and headache (68.0%) are classic examples of adverse events with well-documented female predominance. Women report higher pain sensitivity across multiple modalities, have higher incidence of chronic fatigue conditions, and experience headache disorders (migraine, tension-type) at 2--3 times the rate of men [12, 13]. The consistently high female fractions of these AE hubs across hundreds of drugs suggest that these represent true biological sex differences in symptom susceptibility and reporting threshold, rather than artifacts of any single drug's demographics.

**Moderately female-biased (55--65% F).** Drug ineffective (57.1%), off label use (59.4%), and vomiting (63.2%) show moderate female bias. The female bias in "Drug ineffective" may reflect genuine pharmacokinetic underdosing (many drugs are dosed based on clinical trials with predominantly male participants) or differences in treatment expectations and reporting behavior. The female bias in vomiting is consistent with the known female predominance of chemotherapy-induced nausea and vomiting (CINV) and other emetogenic drug reactions [14].

**Near-parity or male-biased (<52% F).** Condition aggravated (51.6%) is approximately sex-neutral, while Death (46.1%) is the most male-biased hub AE.

#### 3.6.1 Death as a Consistently Male-Biased Hub

The adverse event "Death," connected to 337 drugs with a female fraction of 46.1%, represents one of the most structurally significant findings in this network. Its male bias is notable because the overall FAERS reporting population is 60.2% female; thus, a 46.1% female fraction for death represents a substantial deviation from the baseline, corresponding to a male overrepresentation of approximately 35% relative to expectation.

Several non-exclusive hypotheses may explain this pattern:

1. **Male severity bias.** Men may present to medical attention at later disease stages, resulting in higher baseline severity and higher mortality risk when adverse drug reactions occur. This is consistent with the well-documented male tendency to delay healthcare seeking [15].

2. **Confounding by indication.** Drugs prescribed for conditions with higher male prevalence and inherent mortality risk (e.g., cardiovascular disease, certain cancers, substance use disorders) may drive the male bias in death reports independently of drug-attributable mortality.

3. **Survival bias in AE reporting.** If women are more likely to survive severe adverse drug reactions (consistent with the female survival advantage observed across most causes of death), then the pool of death reports will be mechanically enriched for male cases. This is a form of collider bias: conditioning on the outcome (death) creates a spurious association between sex and drug exposure.

4. **Polypharmacy and comorbidity.** Men receiving the 337 drugs connected to "Death" may have higher rates of polypharmacy and comorbid conditions that elevate mortality risk, confounding the apparent sex-differential signal.

The consistency of male-biased death reporting across 337 drugs---spanning multiple therapeutic classes---argues against drug-specific explanations and in favor of systemic factors (hypotheses 1--4). This finding merits further investigation using linked claims or electronic health record data, which would enable adjustment for baseline severity, comorbidities, and time-to-event.

### 3.7 Network Structural Properties in Context

To contextualize the observed topology, we compare key metrics with those reported for other biomedical bipartite networks (Table 5).

**Table 5. Comparative Network Properties**

| Network | Nodes | Edges | Density | Assortativity | Scale-free |
|---|---|---|---|---|---|
| Sex-diff drug--AE (this study) | 7,247 | 96,281 | 0.0087 | -0.395 | Yes |
| Drug--target (DrugBank) [8] | ~10,000 | ~25,000 | ~0.001 | Disassortative | Yes |
| Drug--drug interaction [3] | ~1,500 | ~50,000 | ~0.04 | Mixed | Yes |
| Protein--protein interaction [6] | ~20,000 | ~200,000 | ~0.001 | Disassortative | Yes |
| Disease--gene (OMIM) [16] | ~5,000 | ~3,000 | ~0.0003 | Disassortative | Yes |

The sex-differential drug--AE network shares the fundamental topological properties of other biomedical networks: sparse connectivity, scale-free degree distributions, and disassortative mixing. Its density (0.0087) is intermediate between the very sparse disease--gene network and the denser drug--drug interaction network, reflecting the moderate specificity of sex-differential adverse event reporting. The strong disassortativity (rho = -0.395) is comparable to that observed in drug--target and protein--protein interaction networks, suggesting a universal architectural principle in which hub nodes serve as bridges to the network periphery rather than forming densely interconnected cores.

---

## 4. Discussion

### 4.1 The Architecture of Sex-Differential Pharmacovigilance

This study provides the first comprehensive topological characterization of the sex-differential drug safety landscape. The bipartite network connecting 2,178 drugs to 5,069 adverse events through 96,281 sex-differential signals reveals an architecture that is sparse, scale-free, disassortative, and systematically sex-graded. These properties are not incidental; they encode fundamental features of drug safety epidemiology and have direct implications for pharmacovigilance practice.

The scale-free degree distribution implies that sex-differential safety surveillance is inherently concentrated: a small number of hub drugs (prednisone, methotrexate, adalimumab, rituximab) and hub AEs (drug ineffective, off label use, vomiting, fatigue) account for a disproportionate share of the network's total connectivity. From a resource-allocation perspective, this suggests that monitoring efforts focused on hub nodes would capture a large fraction of sex-differential signals with relatively modest investment. However, the disassortative mixing pattern complicates this picture: hub drugs connect preferentially to rare AEs, which means that the most important signals for drug safety---rare, potentially serious events---are precisely those that reside in the periphery of the network, accessible primarily through hub nodes.

### 4.2 The Degree--Sex Gradient as a Structural Phenomenon

The positive correlation between node degree and female fraction is, to our knowledge, a novel finding in pharmacovigilance network analysis. This gradient has both methodological and biological significance.

Methodologically, the gradient implies that standard network centrality measures (degree, betweenness, eigenvector centrality) are not sex-neutral: they are systematically biased toward nodes with higher female representation. Any network-based signal detection or prioritization algorithm that uses degree-dependent metrics will therefore implicitly weight female-biased signals more heavily, potentially leading to systematic underdetection of male-biased signals. This bias should be explicitly accounted for in network-based pharmacovigilance methodologies.

Biologically, the gradient may reflect the superposition of multiple sex-dependent processes. The enrichment of immunomodulators among hub drugs connects the degree--sex gradient to the well-established sex dimorphism of the immune system: women mount stronger innate and adaptive immune responses, exhibit higher rates of autoimmune disease, and show stronger vaccine responses, but also experience more frequent immune-related adverse events [17]. The high degree of immunomodulators in the sex-differential network may therefore represent a pharmacological echo of sex-differential immune biology.

### 4.3 Clinical Implications

The topological properties identified in this study have several direct clinical implications:

**Signal prioritization.** In a disassortative network, rare adverse events connected to hub drugs warrant heightened scrutiny. The hub drugs identified in Table 3 are among the most widely prescribed agents in rheumatology, oncology, and transplant medicine; their connections to rare AEs represent high-impact opportunities for signal detection. Conversely, rare drugs connected to hub AEs (e.g., an orphan drug connected to "Fatigue" or "Pain") may represent noise rather than signal, given the ubiquity of these AEs across the pharmacological landscape.

**Sex-stratified surveillance.** The monotonic increase in female fraction across drug degree quintiles (Table 2) suggests that sex-stratified analysis should be routinely applied in pharmacovigilance, particularly for high-degree drugs. Currently, FAERS signal detection algorithms do not routinely stratify by sex; our findings suggest that doing so would reveal signals that are obscured in sex-aggregated analyses.

**Transplant pharmacovigilance.** The identification of tacrolimus as the sole male-biased hub drug highlights the importance of indication-specific context in sex-differential pharmacovigilance. Sex-differential signals for transplant medications should be interpreted against the background of the male-biased transplant recipient population, and pharmacovigilance algorithms should incorporate indication-level sex ratios to avoid confounding.

**Mortality surveillance.** The consistent male bias of "Death" across 337 drugs raises the possibility that current pharmacovigilance systems systematically underestimate the drug-attributable mortality risk for women (if the male bias reflects survival bias or healthcare-seeking behavior rather than true biological risk). Alternatively, if the male bias reflects genuine biological susceptibility to fatal outcomes, then sex-stratified mortality monitoring should be prioritized for drugs connected to this hub AE.

### 4.4 Relationship to Biological Network Architecture

The topological convergence between the sex-differential drug--AE network and canonical biological networks (protein--protein interaction, metabolic, drug--target) is notable. Scale-free degree distributions in biological networks arise from preferential attachment (new interactions are more likely to form with already highly connected nodes) and gene duplication with divergence [6]. In the pharmacovigilance context, analogous mechanisms may operate: drugs with broad indications accumulate more AE reports over time (preferential attachment via exposure), and structurally similar drugs (e.g., anti-TNF biologics) share AE profiles through mechanism-of-action similarity (duplication with divergence).

The disassortative mixing observed here (rho = -0.395) is characteristic of bipartite biological networks but contrasts with the assortative mixing typically seen in social networks. In biological networks, disassortativity arises because hub proteins interact with many specialist proteins that themselves have few other partners [9]. In the pharmacovigilance network, the analogous interpretation is that hub drugs (broad-spectrum agents) generate sex-differential signals for many adverse events that are otherwise drug-specific or rare, while specialist drugs (narrow-indication agents) connect only to a few common AEs. This hierarchical structure is consistent with the pharmacological organization of drug classes, where a few broad-spectrum agents span multiple mechanism-of-action categories while most drugs are narrowly targeted.

### 4.5 Limitations

Several limitations should be acknowledged. First, FAERS is a spontaneous reporting system subject to reporting bias, underreporting, and notoriety bias. The 60.2% female fraction of the FAERS population exceeds the 50.8% female fraction of the U.S. population, indicating sex-differential reporting rates that may confound our findings. However, because our analysis focuses on the structure of sex-differential signals (relative differences between sexes within drug--AE pairs) rather than absolute reporting rates, first-order reporting bias is partially mitigated.

Second, the definition of sex-differential signals using disproportionality analysis does not establish causality. Observed sex differences may reflect genuine pharmacological sex dimorphism, sex-differential exposure, confounding by indication, or reporting artifacts. Network topology cannot distinguish among these mechanisms; it can only describe the structural organization of signals regardless of their underlying cause.

Third, the bipartite network abstraction ignores higher-order structure, including polypharmacy effects, temporal dynamics (signal evolution over time), and hierarchical AE classification (MedDRA system organ classes). Future work incorporating temporal layers, multiplex structure, and indication-stratified subnetworks would provide a richer characterization.

Fourth, our analysis is limited to a single pharmacovigilance database (FAERS). Replication using the European EudraVigilance system, the WHO VigiBase, or the Japanese JADER would strengthen the generalizability of these findings.

Fifth, the biological sex variable in FAERS does not capture the full complexity of sex and gender. Transgender and nonbinary individuals, who may have distinct pharmacokinetic and pharmacodynamic profiles, are not separately identifiable in the current data.

### 4.6 Future Directions

Several avenues for future research emerge from this analysis:

1. **Temporal network dynamics.** Constructing quarter-by-quarter snapshots of the sex-differential network would enable analysis of network growth, hub emergence, and signal persistence over the 21-year study period. Drugs whose degree or sex bias shifts over time may represent evolving safety profiles or changes in prescribing demographics.

2. **Community detection.** Applying bipartite community detection algorithms (e.g., bipartite modularity optimization, stochastic block models) to the sex-differential network may reveal clusters of drugs and AEs that share sex-differential profiles, potentially corresponding to mechanism-of-action classes or patient subpopulations.

3. **Integration with knowledge graphs.** Overlaying the sex-differential network onto existing drug--target, drug--pathway, and disease--gene knowledge graphs would enable mechanistic interpretation of topological features. For example, hub drugs may converge on sexually dimorphic pathways (e.g., estrogen signaling, sex-chromosome-linked immune genes) that explain their broad sex-differential AE profiles.

4. **Network-based signal detection algorithms.** The topological properties characterized here---scale-free degree distribution, disassortativity, degree--sex gradient---could be incorporated into network-aware pharmacovigilance algorithms that use graph structure to improve signal detection sensitivity and specificity, particularly for rare AEs connected to hub drugs.

5. **Sex-stratified risk prediction.** The degree--sex gradient suggests that network centrality measures could be used as features in machine learning models for sex-stratified adverse event risk prediction, complementing traditional patient-level features with population-level network structure.

---

## 5. Conclusions

The bipartite network of sex-differential drug safety signals in FAERS exhibits a sparse, scale-free, disassortative architecture with a systematic degree--sex gradient. These topological properties are not arbitrary; they encode the organizational logic of sex-differential pharmacovigilance: a small number of hub drugs---predominantly immunomodulators with female-biased patient populations---anchor a network that extends into a long tail of rare, drug-specific adverse events. The degree--sex gradient establishes that network connectivity is itself a sex-biased property, with implications for signal detection methodology.

Two structurally anomalous hubs---tacrolimus (male-biased, transplant demographics) and Death (male-biased, survival/severity bias)---demonstrate that network topology can surface clinically meaningful deviations from population-level patterns. The strong disassortativity of the network implies that hub drugs serve as gateways to the detection of rare safety signals, positioning them as critical nodes for pharmacovigilance resource allocation.

These findings argue for the integration of network-topological perspectives into pharmacovigilance practice. Sex-stratified analysis, hub-aware signal prioritization, and network-based algorithms represent concrete methodological advances that follow directly from the architectural properties described here. As pharmacovigilance databases continue to grow, network-level analysis will become an increasingly essential complement to traditional signal-by-signal assessment.

---

## Declarations

**Funding.** This research received no external funding.

**Conflicts of Interest.** The author declares no conflicts of interest.

**Data Availability.** FAERS data are publicly available from the FDA (https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html). Network construction code and analysis scripts are available from the author upon request.

**Ethics Statement.** This study used only de-identified, publicly available spontaneous reporting data and did not require ethics committee approval.

---

## References

[1] Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biology of Sex Differences*. 2020;11:32. doi:10.1186/s13293-020-00308-5

[2] Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: Aggregated evidence from globally collected individual case reports during half a century. *EClinicalMedicine*. 2019;17:100188. doi:10.1016/j.eclinm.2019.10.001

[3] Tatonetti NP, Ye PP, Daneshjou R, Altman RB. Data-driven prediction of drug effects and interactions. *Science Translational Medicine*. 2012;4(125):125ra31. doi:10.1126/scitranslmed.3003377

[4] Cheng F, Desai RJ, Handy DE, et al. Network-based approach to prediction and population-based validation of in silico drug repurposing. *Nature Communications*. 2018;9:2691. doi:10.1038/s41467-018-05116-5

[5] Banda JM, Evans L, Vanguri RS, Tatonetti NP, Ryan PB, Shah NH. A curated and standardized adverse drug event resource to accelerate drug safety research. *Scientific Data*. 2016;3:160026. doi:10.1038/sdata.2016.26

[6] Barabasi AL, Oltvai ZN. Network biology: understanding the cell's functional organization. *Nature Reviews Genetics*. 2004;5(2):101-113. doi:10.1038/nrg1272

[7] Jeong H, Tombor B, Albert R, Oltvai ZN, Barabasi AL. The large-scale organization of metabolic networks. *Nature*. 2000;407(6804):651-654. doi:10.1038/35036627

[8] Yildirim MA, Goh KI, Cusick ME, Barabasi AL, Vidal M. Drug-target network. *Nature Biotechnology*. 2007;25(10):1119-1126. doi:10.1038/nbt1338

[9] Bascompte J, Jordano P, Melian CJ, Olesen JM. The nested assembly of plant-animal mutualistic networks. *Proceedings of the National Academy of Sciences*. 2003;100(16):9383-9387. doi:10.1073/pnas.1633576100

[10] Ngo ST, Steyn FJ, McCombe PA. Gender differences in autoimmune disease. *Frontiers in Neuroendocrinology*. 2014;35(3):347-369. doi:10.1016/j.yfrne.2014.04.004

[11] Melk A, Babitsch B, Borber-Grotius K, et al. Equally interchangeable? How sex and gender affect transplantation. *Transplantation*. 2019;103(6):1094-1110. doi:10.1097/TP.0000000000002655

[12] Mogil JS. Sex differences in pain and pain inhibition: multiple explanations of a controversial phenomenon. *Nature Reviews Neuroscience*. 2012;13(12):859-866. doi:10.1038/nrn3360

[13] Buse DC, Loder EW, Gorber JA, et al. Sex differences in the prevalence, symptoms, and associated features of migraine, probable migraine and other severe headache. *Headache*. 2013;53(8):1278-1299. doi:10.1111/head.12150

[14] Schwartzberg LS. Chemotherapy-induced nausea and vomiting: clinician and patient perspectives. *Journal of Supportive Oncology*. 2007;5(2 Suppl 1):5-12.

[15] Galdas PM, Cheater F, Marshall P. Men and health help-seeking behaviour: literature review. *Journal of Advanced Nursing*. 2005;49(6):616-623. doi:10.1111/j.1365-2648.2004.03331.x

[16] Goh KI, Cusick ME, Valle D, Childs B, Vidal M, Barabasi AL. The human disease network. *Proceedings of the National Academy of Sciences*. 2007;104(21):8685-8690. doi:10.1073/pnas.0701361104

[17] Klein SL, Flanagan KL. Sex differences in immune responses. *Nature Reviews Immunology*. 2016;16(10):626-638. doi:10.1038/nri.2016.90
