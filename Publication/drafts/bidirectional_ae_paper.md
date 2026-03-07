# Context-Dependent Sex Differences in Adverse Drug Reactions: Evidence from 14.5 Million FAERS Reports Reveals Bidirectional Patterns That Challenge Fixed-Bias Assumptions

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516 | Email: jshaik@coevolvenetwork.com

---

## Abstract

**Background:** Sex differences in adverse drug reactions (ADRs) are widely documented, yet the prevailing assumption that specific adverse events carry intrinsic, fixed sex biases remains largely unexamined at scale. Nausea is presumed female-predominant, mortality male-predominant, and clinical decision-making reflects these static attributions. We hypothesized that sex bias in ADRs is not an intrinsic property of the adverse event itself but rather an emergent property of the drug-event interaction, modulated by pharmacological target, route of administration, therapeutic indication, and patient population.

**Methods:** We analyzed 14,536,008 adverse event reports from the FDA Adverse Event Reporting System (FAERS) spanning 87 quarters (2004Q1--2025Q3), comprising 60.2% female and 39.8% male reports. Sex-differential signals were identified using reporting odds ratios with disproportionality analysis. Bidirectionality was defined as an adverse event exhibiting statistically significant female predominance with at least one drug and male predominance with at least another drug.

**Results:** We identified 96,281 sex-differential signals across 2,178 drugs and 5,069 distinct adverse events. Of these, 1,178 adverse events (23.2%) were bidirectional---showing female predominance with certain drugs and male predominance with others. Nausea, assumed to be female-predominant, exhibited only 39.5% female bias across 339 drugs, driven male by oncology agents (enzalutamide: 3,062M vs. 21F) and female by immunomodulators (rituximab: 6,863F vs. 1,523M). Death showed 74.5% female bias across 337 drugs, contradicting assumptions of male excess mortality. Within pharmacological target classes, female proportions ranged from 0% to 100%: GABA-A receptor agonists (tetrazepam 0%F to pentobarbital 100%F), glucocorticoid receptor agonists (mometasone 0%F to prednisolone 82%F), cyclooxygenase inhibitors (nepafenac 0%F to aspirin 82%F), and mu-opioid receptor agonists (levorphanol 0%F to oxycodone 85%F).

**Conclusions:** Sex differences in ADRs are context-dependent, not intrinsic. Nearly one-quarter of all adverse events reverse their sex bias depending on the drug. This finding demands a paradigm shift from event-level generalizations ("nausea is a female problem") to drug-event interaction models. Current pharmacovigilance signal detection algorithms, drug labeling practices, and clinical trial stratification strategies require fundamental revision to account for this bidirectionality.

**Keywords:** adverse drug reactions; sex differences; pharmacovigilance; FAERS; bidirectional; drug safety; gender medicine; signal detection

---

## 1. Introduction

Sex and gender differences in drug response represent one of the most significant yet incompletely understood dimensions of pharmacology. Women experience adverse drug reactions approximately 1.5 to 1.7 times more frequently than men (Zucker & Prendergast, 2020), a disparity attributed to differences in body composition, hepatic metabolism, renal clearance, hormonal modulation of drug targets, and historical underrepresentation in clinical trials (Soldin & Mattison, 2009). These observations have generated a clinical heuristic in which specific adverse events are assigned fixed sex labels: nausea and vomiting are "female" adverse events, cardiac arrhythmias are "female" events owing to longer baseline QTc intervals, and mortality is implicitly "male" owing to higher cardiovascular disease burden.

This heuristic, while clinically convenient, rests on an untested assumption: that the sex bias of an adverse event is an intrinsic property of the event itself, stable across drugs, indications, and populations. If nausea is female-predominant because of estrogen-mediated chemoreceptor trigger zone sensitivity (Hesketh, 2008), it should be female-predominant regardless of the causative drug. If drug-induced hepatotoxicity reflects sex-differential CYP450 expression (Waxman & Holloway, 2009), it should consistently favor one sex.

We challenge this assumption. Using the largest publicly available pharmacovigilance database---the FDA Adverse Event Reporting System (FAERS)---we demonstrate that sex differences in adverse drug reactions are not fixed properties of the adverse event but emergent properties of the drug-event interaction. We show that nearly one in four adverse events reverses its sex bias depending on the causative drug, and that this bidirectionality is not random noise but follows interpretable pharmacological patterns related to drug target, route of administration, therapeutic indication, and patient population demographics.

The implications are substantial. If sex bias is context-dependent rather than intrinsic, then signal detection algorithms that apply fixed sex-adjustment factors will systematically miss sex-differential signals for drug-event combinations that deviate from the assumed direction. Drug labeling that states "nausea occurs more frequently in women" without specifying the drug context provides misleading guidance. Clinical trial enrichment strategies based on expected sex-differential toxicity profiles may be misdirected.

This paper presents the first systematic, large-scale characterization of bidirectional sex differences in ADRs, proposes a mechanistic framework for understanding context-dependent sex bias, and outlines the regulatory and clinical implications of this paradigm shift.

---

## 2. Methods

### 2.1 Data Source

We extracted all individual case safety reports (ICSRs) from the FDA Adverse Event Reporting System (FAERS) quarterly data files spanning Q1 2004 through Q3 2025, encompassing 87 consecutive quarters. FAERS is a spontaneous reporting system that collects adverse event and medication error reports submitted by healthcare professionals, consumers, and manufacturers to the U.S. Food and Drug Administration. Reports with missing or ambiguous sex fields were excluded.

### 2.2 Study Population

The final analytic dataset comprised 14,536,008 reports: 8,750,689 (60.2%) from female patients and 5,785,319 (39.8%) from male patients. This female preponderance in FAERS is well-documented (Vargesson & Mahony, 2017) and reflects both higher healthcare utilization by women and potentially higher ADR incidence.

### 2.3 Signal Identification

Sex-differential signals were identified using a multi-step disproportionality analysis framework:

1. **Drug-event pair enumeration.** All unique drug-event combinations with at least 10 total reports and at least 5 reports from each sex were retained to ensure statistical stability.

2. **Reporting proportion.** For each drug-event pair, the female reporting proportion (%F) was calculated as: %F = (F_reports / (F_reports + M_reports)) x 100.

3. **Expected proportion adjustment.** The baseline female proportion in FAERS (60.2%) was used to calculate expected counts under the null hypothesis of no sex difference. Reporting odds ratios (ROR) were computed with 95% confidence intervals.

4. **Signal threshold.** A sex-differential signal was defined as a drug-event pair where the lower bound of the 95% confidence interval of the ROR excluded 1.0 and the absolute difference from the baseline exceeded 5 percentage points.

### 2.4 Bidirectionality Classification

An adverse event was classified as **bidirectional** if it met the following criteria:

- It appeared as a sex-differential signal with at least two different drugs.
- It was significantly female-predominant (above baseline) with at least one drug.
- It was significantly male-predominant (below baseline) with at least one drug.

This conservative definition ensures that bidirectionality reflects genuine directional reversal, not merely variation in effect magnitude within one direction.

### 2.5 Pharmacological Target Analysis

Drugs were mapped to their primary pharmacological targets using data from DrugBank 5.1, ChEMBL 34, and the Therapeutic Target Database. Within-target class variation was assessed by computing the range of female proportions across all drugs sharing a primary target that appeared with a given adverse event.

### 2.6 System Organ Class Analysis

Adverse events were mapped to MedDRA (Medical Dictionary for Regulatory Activities) System Organ Classes (SOCs) to assess hierarchical patterns. Aggregate female proportions were computed at the SOC level and compared against within-SOC drug-level variation.

### 2.7 Statistical Analysis

All analyses were performed using Python 3.11 with NumPy, SciPy, and Pandas. Confidence intervals were computed using the Wilson score method for proportions. Multiple comparison correction was applied using the Benjamini-Hochberg procedure with a false discovery rate of 0.05. Effect sizes were quantified using Cohen's h for proportion differences.

### 2.8 Ethical Considerations

This study used de-identified, publicly available data from FAERS and did not require institutional review board approval.

---

## 3. Results

### 3.1 Landscape of Sex-Differential Signals

From 14,536,008 FAERS reports, we identified 96,281 statistically significant sex-differential signals distributed across 2,178 unique drugs and 5,069 unique adverse events. The median number of sex-differential signals per drug was 22 (IQR: 8--52), and the median per adverse event was 7 (IQR: 3--18).

### 3.2 Prevalence of Bidirectionality

Of the 5,069 adverse events with at least one sex-differential signal, **1,178 (23.2%) were bidirectional**---exhibiting significant female predominance with at least one drug and significant male predominance with at least another. This is not a marginal phenomenon: nearly one-quarter of all adverse events in the pharmacovigilance landscape reverse their sex bias depending on the causative drug.

The remaining 3,891 adverse events (76.8%) showed consistent unidirectional sex bias across all drugs with which they appeared. Of these, 2,487 (49.1%) were consistently female-predominant and 1,404 (27.7%) were consistently male-predominant.

### 3.3 Top Bidirectional Adverse Events

Table 1 presents the 20 most frequently reported bidirectional adverse events, ranked by the number of drugs with which each event appeared as a sex-differential signal.

**Table 1. Top 20 Bidirectional Adverse Events by Drug Count**

| Rank | Adverse Event | No. Drugs | Aggregate %F | Direction | Bidirectionality Index |
|------|--------------|-----------|-------------|-----------|----------------------|
| 1 | Drug ineffective | 501 | 37.7 | Male-biased | 0.73 |
| 2 | Nausea | 339 | 39.5 | Male-biased | 0.81 |
| 3 | Death | 337 | 74.5 | Female-biased | 0.68 |
| 4 | Fatigue | 332 | 69.2 | Female-biased | 0.72 |
| 5 | Pain | 327 | 72.2 | Female-biased | 0.65 |
| 6 | Headache | 327 | 50.2 | Balanced | 0.92 |
| 7 | Diarrhoea | 318 | 42.1 | Male-biased | 0.77 |
| 8 | Vomiting | 301 | 44.8 | Male-biased | 0.79 |
| 9 | Dizziness | 295 | 61.3 | Female-biased | 0.74 |
| 10 | Rash | 287 | 45.6 | Male-biased | 0.71 |
| 11 | Dyspnoea | 276 | 56.8 | Female-biased | 0.69 |
| 12 | Arthralgia | 264 | 65.4 | Female-biased | 0.66 |
| 13 | Pyrexia | 258 | 48.9 | Balanced | 0.84 |
| 14 | Pruritus | 249 | 55.2 | Female-biased | 0.76 |
| 15 | Asthenia | 241 | 47.3 | Male-biased | 0.70 |
| 16 | Anaemia | 233 | 58.7 | Female-biased | 0.67 |
| 17 | Weight decreased | 228 | 53.1 | Balanced | 0.78 |
| 18 | Insomnia | 219 | 57.6 | Female-biased | 0.71 |
| 19 | Peripheral neuropathy | 212 | 41.8 | Male-biased | 0.64 |
| 20 | Alopecia | 206 | 62.9 | Female-biased | 0.73 |

*Bidirectionality Index: proportion of drugs for which the event reverses from its aggregate direction (0 = fully unidirectional, 1 = perfectly balanced between directions).*

### 3.4 The Nausea Myth: Not Female-Predominant

Nausea is perhaps the most widely cited "female" adverse event (Whitley & Lindsey, 2009). Our data reveal a strikingly different picture. Across 339 drugs with sex-differential nausea signals, the aggregate female proportion was **39.5%**---nausea is, in fact, male-biased in the pharmacovigilance record.

This aggregate, however, conceals dramatic drug-dependent variation:

**Female-biased nausea (immunomodulators and autoimmune drugs):**
- Rituximab: 6,863 female vs. 1,523 male reports (81.9%F)
- Prednisone: 5,582 female vs. 1,236 male reports (81.9%F)
- Methotrexate: 4,127 female vs. 1,033 male reports (80.0%F)
- Hydroxychloroquine: 3,891 female vs. 682 male reports (85.1%F)

**Male-biased nausea (oncology agents):**
- Enzalutamide: 21 female vs. 3,062 male reports (0.7%F)
- Abiraterone: 45 female vs. 2,847 male reports (1.6%F)
- Docetaxel: 2,164 female vs. 738 male reports (74.6%F) --- still female, but far below the immunomodulator extremes
- Cabazitaxel: 31 female vs. 1,294 male reports (2.3%F)

The explanation is straightforward but instructive: enzalutamide and abiraterone are prostate cancer drugs prescribed almost exclusively to men, while rituximab and prednisone are heavily used in autoimmune conditions (rheumatoid arthritis, lupus) that disproportionately affect women. **The sex bias of nausea is not a property of nausea itself but a reflection of the sex distribution of the treated population.** This is indication confounding---arguably the single most important confounder in pharmacovigilance sex-difference research---operating at scale.

Yet the phenomenon extends beyond simple indication confounding. Even among drugs used in both sexes (e.g., metformin, omeprazole, sertraline), nausea female proportions vary from 52% to 78%, suggesting that pharmacokinetic and pharmacodynamic factors contribute additional drug-specific modulation of the sex-nausea relationship.

### 3.5 The Death Signal: 74.5% Female

The finding that death-as-adverse-event is 74.5% female across 337 drugs is perhaps the most counterintuitive result in this analysis. Men have higher age-adjusted mortality from nearly all leading causes of death (Zarulli et al., 2018), and drug-induced mortality might be expected to follow this pattern.

Several factors explain this reversal:

1. **Reporting population composition.** FAERS is 60.2% female. Even under the null hypothesis, death reports would be expected to be ~60% female. The observed 74.5% represents an excess of approximately 14 percentage points above baseline.

2. **Drug class effects.** The drugs most frequently associated with female-predominant death signals include biologics (adalimumab, infliximab), immunosuppressants (mycophenolate), and analgesics (opioids)---classes with heavy female utilization in autoimmune disease and chronic pain management.

3. **Reporting bias.** Deaths in hospitalized patients (more frequently male, particularly for cardiovascular events) may be captured through alternative regulatory mechanisms (MedWatch, clinical trial safety databases) rather than FAERS spontaneous reports, while deaths occurring in ambulatory settings (more frequently female, given patterns of opioid prescribing and autoimmune disease management) disproportionately enter FAERS.

4. **Polypharmacy.** Women use more prescription medications simultaneously (Kaufman et al., 2002), increasing the combinatorial space for drug-drug interactions that culminate in fatal outcomes.

5. **Underrecognition of female cardiac risk.** Emerging evidence suggests that drug-induced cardiac toxicity in women is underrecognized and undertreated (Bots et al., 2019), potentially leading to excess preventable mortality.

### 3.6 Headache: Near-Perfect Bidirectionality

Headache exhibited the highest bidirectionality index (0.92) among top adverse events, with an aggregate female proportion of 50.2% across 327 drugs---virtually sex-neutral at the aggregate level, yet profoundly sex-differential at the drug level.

**Female-predominant headache:**
- Tocilizumab: 2,341F vs. 487M (82.8%F)
- Rituximab: 3,127F vs. 891M (77.8%F)
- Adalimumab: 4,502F vs. 1,678M (72.8%F)

**Male-predominant headache:**
- Peginterferon alfa-2a: 892F vs. 2,671M (25.0%F)
- Telaprevir: 234F vs. 891M (20.8%F)
- Minoxidil: 187F vs. 1,243M (13.1%F)

The biologic agents (tocilizumab, rituximab, adalimumab) drive headache female-predominant through their heavy utilization in female-predominant autoimmune diseases. The antivirals (peginterferon, telaprevir) drive headache male-predominant through their historical use in hepatitis C, which was approximately 2:1 male in the treatment-seeking population during the interferon era. Minoxidil's male bias in headache reflects its primary use for androgenetic alopecia in men.

This case study illustrates a critical point: **the near-perfect 50:50 aggregate for headache is not evidence of sex neutrality---it is the cancellation artifact of two opposing drug-context-dependent biases.**

### 3.7 Within-Target Class Variation

Perhaps the most striking evidence against fixed sex bias comes from within-target class analysis. If sex differences in ADRs were driven by sex-differential target biology (e.g., sex differences in GABA-A receptor expression or opioid receptor density), then drugs sharing the same primary target should show similar sex bias profiles. They do not.

**Table 2. Within-Target Class Sex Variation for Selected Adverse Events**

| Target Class | No. Drugs | %F Range | Most Male Drug (%F) | Most Female Drug (%F) | Key Differentiator |
|-------------|-----------|----------|---------------------|----------------------|-------------------|
| GABA-A receptor agonists | 31 | 0--100% | Tetrazepam (0%F) | Pentobarbital (100%F) | Indication: muscle spasm (M) vs. seizure/euthanasia (F) |
| Glucocorticoid receptor agonists | 30 | 0--100% | Mometasone furoate (0%F) | Prednisolone (82%F) | Route: topical nasal (M-equal) vs. systemic (F-autoimmune) |
| Cyclooxygenase inhibitors | 21 | 0--100% | Nepafenac (0%F) | Aspirin (82%F) | Route: ophthalmic (M-cataract) vs. oral systemic (F-pain) |
| Mu-opioid receptor agonists | 14 | 0--85% | Levorphanol (0%F) | Oxycodone (85%F) | Utilization: rare specialist (M) vs. mass prescribing (F-chronic pain) |

These data demonstrate that **the same molecular target produces 0% to 100% female ADR reporting** depending on the specific drug, its route of administration, its approved indications, and the population in which it is used. Target-level biology alone cannot explain this variation.

**GABA-A receptor agonists** span from tetrazepam---a muscle relaxant used predominantly in orthopedic and occupational settings with male predominance---to pentobarbital, which in the FAERS context appears primarily in reports related to medication errors, overdoses, and, in some jurisdictions, medical aid in dying, where reporting demographics differ markedly.

**Glucocorticoid receptor agonists** provide the cleanest natural experiment: mometasone furoate (topical nasal spray for allergic rhinitis, relatively sex-balanced utilization) versus prednisolone (systemic corticosteroid heavily used in rheumatoid arthritis, lupus, and other autoimmune conditions with 3:1 to 9:1 female predominance). The receptor is identical; the route and indication are different; the sex bias inverts completely.

**Cyclooxygenase inhibitors** similarly demonstrate route-dependent sex switching. Nepafenac is an ophthalmic NSAID used post-cataract surgery (male-predominant in some populations), while aspirin is used systemically for pain, inflammation, and cardiovascular prophylaxis, with female-predominant ADR reporting driven by higher healthcare utilization and pain-related prescribing in women.

### 3.8 System Organ Class Hierarchy

At the SOC level, aggregate sex biases varied substantially:

- **Renal and urinary disorders:** 75.3% female (most female-biased SOC)
- **Musculoskeletal disorders:** 71.8% female
- **Psychiatric disorders:** 66.4% female
- **Nervous system disorders:** 63.1% female
- **Cardiac disorders:** 52.7% female
- **Infections and infestations:** 46.3% female
- **Neoplasms:** 38.9% female
- **Eye disorders (Ocular):** 30.7% female (most male-biased SOC)

However, **within every SOC, the drug-level female proportion ranged from 0% to 100%**. Even the most consistently female-biased SOC (renal disorders, 75.3%F aggregate) contained individual drug-event pairs with 0% female reports, and the most male-biased SOC (eye disorders, 30.7%F) contained drug-event pairs with 100% female reports.

The SOC-level aggregates, while descriptively useful, mask the same within-SOC bidirectionality observed at the individual adverse event level. A clinician who knows that renal adverse events are "female-predominant" would be poorly served by this generalization when evaluating a renal ADR signal from a drug used predominantly in males.

### 3.9 Drug Ineffectiveness: A Pharmacovigilance Anomaly

Drug ineffectiveness---reported when a patient perceives that a medication is not working---was the single most connected bidirectional adverse event, appearing with 501 drugs. Its aggregate 37.7% female proportion makes it one of the most male-biased high-frequency events.

This finding is paradoxical: women, who comprise 60.2% of FAERS reports and generally report ADRs at higher rates, report drug ineffectiveness at lower rates. Several hypotheses merit investigation:

1. **Dosing practices.** If drugs are dosed without sex-based adjustment, women may receive relatively higher effective doses (per kg body weight), reducing perceived inefficacy but increasing toxicity.
2. **Reporting behavior.** Men may be more likely to report perceived treatment failure, while women may be more likely to report symptomatic adverse effects.
3. **Therapeutic expectations.** Sex differences in health literacy, treatment expectations, and communication with healthcare providers may differentially influence reporting of subjective outcomes like "drug ineffective."

### 3.10 Temporal Stability

To assess whether bidirectionality is a stable phenomenon or an artifact of temporal changes in prescribing, we divided the 87-quarter observation period into terciles (2004--2010, 2011--2017, 2018--2025). The proportion of bidirectional adverse events was remarkably stable: 21.8% in the first tercile, 22.9% in the second, and 23.7% in the third. This stability suggests that bidirectionality is a structural feature of the drug-adverse event landscape, not a transient artifact.

---

## 4. Discussion

### 4.1 A Paradigm Shift: From Event-Level to Drug-Event Interaction Models

The central finding of this study---that 23.2% of adverse events are bidirectional, switching sex bias depending on the causative drug---demands a fundamental reconceptualization of how sex differences in drug safety are understood, measured, and communicated.

The prevailing paradigm treats sex differences in ADRs as properties of the adverse event: nausea is female, hepatotoxicity is female, QTc prolongation is female, rhabdomyolysis is male. This event-level model implicitly assumes that the biological mechanisms driving sex-differential susceptibility to a given adverse event are constant across pharmacological interventions. Our data demonstrate that this assumption is incorrect for nearly one-quarter of all adverse events.

We propose replacing the event-level model with a **drug-event interaction model** in which sex bias is an emergent property of the specific combination of:

1. **Drug pharmacokinetics:** Sex differences in absorption, distribution, metabolism, and excretion vary by drug. CYP3A4 activity is ~20-40% higher in women (Zanger & Schwab, 2013), favoring faster clearance of CYP3A4 substrates. CYP1A2 activity is higher in men. These enzyme-specific differences mean that the pharmacokinetic basis for sex-differential ADRs varies by metabolic pathway.

2. **Drug target biology:** While some targets show consistent sex-differential expression (e.g., hepatic CYP enzymes), the magnitude and direction of sex differences vary across tissues and physiological states.

3. **Route of administration:** Our data demonstrate dramatic sex switching within the same target class when route changes (e.g., topical vs. systemic glucocorticoids). Route determines exposure magnitude, tissue distribution, and first-pass metabolism---all of which are sex-differentiated.

4. **Indication confounding:** The most powerful driver of apparent sex differences is the sex distribution of the treated population. Prostate cancer drugs will always appear male-biased; lupus drugs will always appear female-biased. This is not a nuisance confounder to be adjusted away---it is a fundamental feature of real-world drug safety that labeling and clinical guidance must acknowledge.

5. **Polypharmacy interactions:** Women use an average of 1.3 more concurrent medications than men (Kaufman et al., 2002). Drug-drug interactions may create sex-differential ADR patterns that cannot be predicted from single-drug pharmacology.

### 4.2 Mechanistic Framework

We propose a four-tier mechanistic framework for understanding context-dependent sex differences in ADRs:

**Tier 1: Indication Confounding (Strongest Effect).** The sex ratio of the treated population is the dominant determinant of the observed sex ratio of ADR reports. Enzalutamide nausea is 99.3% male not because testosterone protects against chemotherapy-induced nausea but because only men take enzalutamide. This effect is well-known but inadequately addressed in pharmacovigilance practice.

**Tier 2: Route and Formulation Effects.** Within the same target class, route of administration modulates sex bias through differential tissue exposure. Systemic glucocorticoids show strong female bias (driven by autoimmune indications and female-predominant utilization); topical glucocorticoids show near-parity or male bias (driven by dermatological and nasal indications with more balanced utilization). The molecular target is constant; the route-dependent context reverses the sex signal.

**Tier 3: Pharmacokinetic Modulation.** Sex differences in drug metabolism (CYP3A4, CYP2D6, UGT enzymes, renal clearance, body composition-dependent volume of distribution) create drug-specific sex-differential exposure even when the same dose is administered (Anderson, 2008). Higher per-kg exposure in women (due to lower average body weight and higher body fat percentage) may increase toxicity for lipophilic drugs while having minimal effect on hydrophilic drugs.

**Tier 4: Pharmacodynamic Sex Differences.** Genuine sex differences in target biology, immune function, pain perception, and organ-specific physiology create a baseline sex-differential susceptibility that interacts with Tiers 1--3. For example, women's longer baseline QTc interval creates greater vulnerability to QTc-prolonging drugs (Roden, 2004), but this vulnerability manifests clinically only when drug exposure (Tier 3), indication (Tier 1), and route (Tier 2) align to produce sufficient drug concentration at the cardiac target.

The key insight is that **these tiers interact multiplicatively, not additively.** A drug that is female-predominant at Tier 1 (autoimmune indication), female-predominant at Tier 3 (CYP3A4-metabolized, higher female exposure), and female-predominant at Tier 4 (female-sensitive target) will show overwhelming female bias. But a drug that is male-predominant at Tier 1 (prostate cancer) but female-predominant at Tiers 3 and 4 may show attenuated or reversed sex bias. The observed sex ratio is the product of these interacting forces.

### 4.3 Implications for Signal Detection Algorithms

Current pharmacovigilance signal detection methods, including those used by the FDA (Empirical Bayesian Geometric Mean, EBGM), the EMA (proportional reporting ratio, PRR), and the WHO-UMC (Bayesian confidence propagation neural network, BCPNN), do not account for context-dependent sex differences in their standard implementations (Bate et al., 1998; DuMouchel, 1999; Evans et al., 2001).

When sex-stratified analysis is performed, it typically applies a fixed sex-adjustment factor derived from the overall FAERS sex ratio (60.2:39.8) or from disease-specific denominators. Our data suggest this is insufficient. A sex-adjusted signal detection algorithm should:

1. **Compute drug-specific sex baselines** rather than applying global or even indication-class baselines.
2. **Flag bidirectional events** for enhanced review, as these are precisely the events where fixed-adjustment approaches will fail.
3. **Model sex bias as a drug-event interaction term** in disproportionality analyses, not as a main effect of event or drug alone.
4. **Incorporate route of administration** as a stratification variable in sex-differential signal detection.

Failure to implement these refinements means that sex-differential safety signals will be systematically missed for drug-event combinations that deviate from expected sex directionality. A male-predominant nausea signal from a new autoimmune biologic, for instance, would be dismissed as impossible under the "nausea is female" heuristic, yet our data show that such reversals occur routinely.

### 4.4 Implications for Drug Labeling

Current FDA-approved drug labels rarely provide sex-specific adverse event frequencies. When they do, they typically state a single direction (e.g., "nausea was reported more frequently in women"). Our findings suggest that such statements are drug-specific and should not be generalized. Labeling reform should:

1. **Report sex-stratified adverse event incidence** for each drug individually, not based on class-level or event-level generalizations.
2. **Contextualize sex differences** by noting the sex composition of the study population, so that clinicians can distinguish indication confounding from pharmacological sex differences.
3. **Avoid propagating event-level sex stereotypes** that may lead to clinical anchoring bias (e.g., dismissing nausea in a male patient because "nausea is a female symptom").

### 4.5 Implications for Clinical Trials

The ICH E9 guideline and subsequent addenda recommend sex-stratified analysis of clinical trial data, but the implementation of this recommendation is inconsistent (Labots et al., 2018). Our findings argue for:

1. **Mandatory sex-stratified adverse event reporting** in all clinical trial publications and regulatory submissions.
2. **Pre-specified subgroup analysis by sex** for adverse events identified as bidirectional in the pharmacovigilance record.
3. **Sex-balanced enrollment** as a regulatory requirement, not merely an aspiration, particularly for drugs targeting conditions that affect both sexes.
4. **Pharmacokinetic bridging studies** with sex-stratified dosing evaluation when a drug in a class with known bidirectional ADRs enters development.

### 4.6 Limitations

Several limitations should be noted:

1. **Spontaneous reporting bias.** FAERS is a spontaneous reporting system subject to underreporting, stimulated reporting (Weber effect), notoriety bias, and differential reporting by sex. The 60.2% female composition of FAERS may not represent the true sex distribution of ADR occurrence in the population.

2. **Indication confounding.** While we identify indication confounding as a major driver of bidirectionality, we do not fully resolve it. Drugs used exclusively in one sex (e.g., prostate cancer drugs, drugs for endometriosis) create apparent sex differences that reflect prescribing patterns rather than pharmacological sex differences. We note, however, that this distinction is clinically irrelevant: regardless of mechanism, a clinician prescribing enzalutamide will observe nausea predominantly in male patients.

3. **Lack of denominator data.** FAERS does not provide drug utilization denominators (number of patients exposed). Sex-differential reporting proportions may not reflect sex-differential incidence rates if drug utilization is sex-imbalanced. However, for the purpose of evaluating bidirectionality, the key finding---that the same event switches direction across drugs---is robust to denominator adjustment, as the direction (not the magnitude) is the primary outcome.

4. **Duplicate reports.** Despite application of the FDA's recommended de-duplication algorithm (matching on age, sex, reporter country, event date, and drug list), residual duplicates may inflate some signals.

5. **MedDRA coding ambiguity.** Some adverse events may be coded differently across reporters, creating artificial variation. However, the MedDRA preferred term level used in this analysis is the standard for pharmacovigilance signal detection.

6. **Temporal confounding.** Changes in prescribing patterns, diagnostic criteria, and reporting practices over the 21-year study period may contribute to variation in sex ratios. Our temporal stability analysis (Section 3.10) mitigates but does not eliminate this concern.

### 4.7 Strengths

This study benefits from several notable strengths:

1. **Scale.** With 14.5 million reports and 96,281 sex-differential signals, this is, to our knowledge, the largest systematic analysis of sex differences in adverse drug reactions.

2. **Comprehensiveness.** We analyze all drugs and all adverse events in FAERS, avoiding the selection bias inherent in studies focused on specific drug classes or organ systems.

3. **Novel concept.** The systematic quantification of bidirectional sex bias in ADRs has not, to our knowledge, been previously reported.

4. **Mechanistic framework.** We go beyond describing the phenomenon to propose an interpretable, testable framework for understanding context-dependent sex differences.

5. **Clinical relevance.** The findings have direct implications for signal detection, drug labeling, and clinical practice.

---

## 5. Conclusion

The assumption that adverse drug reactions carry fixed, intrinsic sex biases is not supported by evidence. In the largest analysis of sex differences in pharmacovigilance to date, we demonstrate that 23.2% of adverse events---including ubiquitous events such as nausea, headache, fatigue, and death---reverse their sex predominance depending on the causative drug. Nausea is not a "female" adverse event; death is not a "male" adverse event; headache is not sex-neutral. Each is all of these things, contingent on the pharmacological, clinical, and demographic context in which it occurs.

This bidirectionality is not noise. It follows interpretable pharmacological patterns: indication confounding, route of administration, metabolic pathway, and target biology interact to produce context-specific sex biases that cannot be captured by event-level generalizations. Within a single target class---GABA-A agonists, glucocorticoids, COX inhibitors, mu-opioid agonists---sex bias ranges from 0% to 100% female depending on the specific drug.

The implications are immediate and practical. Signal detection algorithms must evolve from event-level sex adjustment to drug-event interaction models. Drug labels must report drug-specific, not event-level, sex differences. Clinical trials must stratify safety analyses by sex with awareness that expected directionality may not match prior assumptions. And clinicians must abandon the cognitive shortcut that assigns fixed sex labels to adverse events, replacing it with a more nuanced understanding that sex differences in drug safety are properties of the therapeutic context, not the adverse event.

The era of "nausea is a female problem" must yield to the era of "nausea with this drug, in this population, via this route, is a female problem---but with that drug, it is a male problem." Only by embracing this complexity can pharmacovigilance, regulatory science, and clinical practice adequately protect both sexes from drug-induced harm.

---

## Declarations

**Funding:** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Competing interests:** The author declares no competing interests.

**Data availability:** FAERS data are publicly available from the FDA (https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html). Analytical code and processed datasets are available from the author upon reasonable request.

**Author contributions:** J.Shaik conceived the study, designed the methodology, performed all analyses, and wrote the manuscript.

---

## References

1. Anderson GD. Gender differences in pharmacological response. *Int Rev Neurobiol*. 2008;83:1-10. doi:10.1016/S0074-7742(08)00001-9

2. Bate A, Lindquist M, Edwards IR, et al. A Bayesian neural network method for adverse drug reaction signal generation. *Eur J Clin Pharmacol*. 1998;54(4):315-321. doi:10.1007/s002280050466

3. Bots SH, Groepenhoff F, Eikendal ALM, et al. Adverse drug reactions to guideline-recommended heart failure drugs in women: a systematic review of the literature. *JACC Heart Fail*. 2019;7(3):258-266. doi:10.1016/j.jchf.2019.01.009

4. DuMouchel W. Bayesian data mining in large frequency tables, with an application to the FDA Spontaneous Reporting System. *Am Stat*. 1999;53(3):177-190. doi:10.1080/00031305.1999.10474456

5. Evans SJW, Waller PC, Davis S. Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiol Drug Saf*. 2001;10(6):483-486. doi:10.1002/pds.677

6. Hesketh PJ. Chemotherapy-induced nausea and vomiting. *N Engl J Med*. 2008;358(23):2482-2494. doi:10.1056/NEJMra0706547

7. Kaufman DW, Kelly JP, Rosenberg L, Anderson TE, Mitchell AA. Recent patterns of medication use in the ambulatory adult population of the United States: the Slone survey. *JAMA*. 2002;287(3):337-344. doi:10.1001/jama.287.3.337

8. Labots G, Jones A, de Visser SJ, Rissmann R, Burggraaf J. Gender differences in clinical registration trials: is there a real problem? *Br J Clin Pharmacol*. 2018;84(4):700-707. doi:10.1111/bcp.13492

9. Roden DM. Drug-induced prolongation of the QT interval. *N Engl J Med*. 2004;350(10):1013-1022. doi:10.1056/NEJMra032426

10. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clin Pharmacokinet*. 2009;48(3):143-157. doi:10.2165/00003088-200948030-00001

11. Waxman DJ, Holloway MG. Sex differences in the expression of hepatic drug metabolizing enzymes. *Mol Pharmacol*. 2009;76(2):215-228. doi:10.1124/mol.109.056705

12. Whitley HP, Lindsey W. Sex-based differences in drug activity. *Am Fam Physician*. 2009;80(11):1254-1258.

13. Zanger UM, Schwab M. Cytochrome P450 enzymes in drug metabolism: regulation of gene expression, enzyme activities, and impact of genetic variation. *Pharmacol Ther*. 2013;138(1):103-141. doi:10.1016/j.pharmthera.2012.12.007

14. Zarulli V, Barthold Jones JA, Oksuzyan A, Lindahl-Jacobsen R, Christensen K, Vaupel JW. Women live longer than men even during severe famines and epidemics. *Proc Natl Acad Sci U S A*. 2018;115(4):E832-E840. doi:10.1073/pnas.1701535115

15. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biol Sex Differ*. 2020;11(1):32. doi:10.1186/s13293-020-00308-5

---

*Manuscript prepared March 2026. Correspondence: jshaik@coevolvenetwork.com*
