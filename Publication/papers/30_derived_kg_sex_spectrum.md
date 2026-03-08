# Domain-Specific Sex Bias Spectra in Drug Safety: Insights from Five Derived Knowledge Graphs

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex differences in drug safety are typically characterized as a single aggregate statistic (e.g., "women experience more adverse drug reactions"). Whether this female predominance is uniform across clinical domains or varies systematically has not been examined using knowledge graph embedding approaches.

**Methods.** We constructed five domain-specific knowledge graphs (KGs) from SexDiffKG v5.2 (217,993 nodes, 3,194,017 edges): REPRODUCT-KG (pregnancy/reproductive, 13,208 nodes), MENTALHEALTH-KG (psychiatric, 17,555 nodes), GERIPHARM-KG (elderly, 18,754 nodes), PCOS-ENDO-KG (reproductive endocrine, 36,903 nodes), and AYUR-PHARMA-KG (traditional medicine, 24,316 nodes). Each KG was trained with DistMult embeddings (200 dimensions, 100 epochs). Sex-differential adverse event signals from 96,281 FAERS-derived drug-AE pairs were mapped to each domain, and domain-specific female fractions were computed.

**Results.** The five KGs collectively span 110,736 nodes and 2,821,205 edges, with model quality (MRR) ranging from 0.068 to 0.163. Three of five derived KGs outperformed the parent DistMult model (MRR 0.101), demonstrating that domain extraction improves signal-to-noise ratio. Sex bias varied dramatically across domains: from 21.0% female for PCOS/endometriosis symptoms to 71.4% female for sexual dysfunction adverse events — a 50.4 percentage point spectrum. Falls and fractures showed a striking reversal to 63.8% male predominance, contradicting the general 53.8% female baseline. Elderly-relevant and Ayurvedic-relevant adverse events showed amplified female bias (64.7% and 64.0% respectively). Cognitive decline was 60.5% female-biased, while psychiatric adverse events were near the general baseline (54.2%). Drug embedding similarity recapitulated known pharmacological classes (aripiprazole-risperidone 0.998, morphine-oxycodone 0.993, tofacitinib-upadacitinib 0.992). The AYUR-PHARMA-KG predicted Ashwagandha for PCOS treatment, validated by traditional Ayurvedic use.

**Interpretation.** Sex bias in drug safety is not a monolithic phenomenon but varies by a 50-percentage-point spectrum across clinical domains. The assumption that "more adverse events affect women" is domain-dependent: in PCOS/endometriosis contexts, the pattern reverses entirely, and in fall/fracture-related safety, male predominance emerges. Domain-specific KGs provide superior embedding quality to monolithic approaches and reveal sex-bias patterns invisible in aggregate analysis.

---

## Introduction

The observation that women experience more adverse drug reactions (ADRs) than men is well-documented in pharmacovigilance literature [1-3]. Analysis of the FDA Adverse Event Reporting System (FAERS) consistently shows female predominance: approximately 54% of sex-differential drug safety signals are female-biased [4]. This has been attributed to pharmacokinetic differences (body composition, CYP metabolism), immune hypersensitivity, and reporting behavior [2,5].

However, treating sex-differential drug safety as a single aggregate number obscures potentially important domain-specific variation. Does female predominance hold equally for psychiatric adverse events, elderly-specific complications, reproductive drug reactions, and traditional medicine contexts? If not, the clinical implications of sex-stratified pharmacovigilance differ substantially across therapeutic areas.

Knowledge graph (KG) embedding approaches offer a systematic framework for examining this question. By constructing domain-specific subgraphs from a comprehensive sex-differential drug safety KG and training separate embedding models, we can simultaneously (1) assess whether domain extraction improves predictive quality and (2) characterize domain-specific sex bias patterns.

We hypothesized that sex bias in drug safety varies systematically across clinical domains, with some domains amplifying the general female predominance and others attenuating or reversing it. To test this, we constructed five domain-specific KGs from SexDiffKG v5.2 and analyzed their sex-differential landscapes.

---

## Methods

### Parent Knowledge Graph

SexDiffKG v5.2 integrates 217,993 nodes (13 entity types) and 3,194,017 edges (18 relation types) from FAERS (14,536,008 deduplicated reports, 2004Q1–2025Q3), STRING v12.0, Reactome, ChEMBL 36, GTEx v8, VEDA-KG, and three external databases (CTD, NPASS, LOTUS). Sex-differential adverse event signals (n = 96,281) were computed using sex-stratified reporting odds ratios with DiAna drug name normalization, applying thresholds of |log(ROR_female/ROR_male)| ≥ 0.5 and ≥ 10 reports per sex.

### Domain-Specific KG Construction

Five derived KGs were constructed by filtering the parent KG for domain-relevant entities and their associated edges:

**REPRODUCT-KG** (Pregnancy and Reproductive Drug Safety): Drugs indicated for or commonly used during pregnancy, reproductive conditions, and their associated adverse events, protein targets, and clinical trials. Filtered using reproductive disease ontology terms and drug-indication relationships.

**MENTALHEALTH-KG** (Psychiatric Drug Safety): Drugs with primary psychiatric indications (antipsychotics, antidepressants, anxiolytics, mood stabilizers), their adverse events including psychiatric and sexual dysfunction endpoints, and associated molecular targets.

**GERIPHARM-KG** (Elderly Drug Safety): Drugs commonly prescribed in geriatric populations, with emphasis on elderly-specific adverse events (falls, fractures, cognitive decline, delirium, polypharmacy complications) and age-relevant molecular pathways.

**PCOS-ENDO-KG** (Reproductive Endocrine Drug Safety): Drugs used for polycystic ovary syndrome (PCOS), endometriosis, and related reproductive endocrine conditions, including hormonal therapies, GnRH agonists/antagonists, and insulin sensitizers.

**AYUR-PHARMA-KG** (Ayurvedic-Pharmacovigilance Bridge): A novel bridge between traditional Ayurvedic medicine (5 priority herbs: Ashwagandha, Turmeric, Shatavari, Brahmi, Licorice) and modern pharmacovigilance through shared protein targets and compound-drug relationships.

### Embedding Training

Each derived KG was trained with DistMult embeddings (200 dimensions, 100 epochs, batch size 4,096, Adam optimizer, random seed 42) on CPU. Train/test split was 90/10. Performance was evaluated using Mean Reciprocal Rank (MRR), Hits@1, Hits@10, and Adjusted Mean Rank Index (AMRI) on the test set.

### Sex-Differential Signal Analysis

For each derived KG, the 96,281 parent sex-differential signals were mapped to domain-relevant drugs by name matching. Domain-specific adverse event categories were identified using keyword-based classification:
- Reproductive: pregnancy, foetal, birth, menstrual, ovarian, uterine terms (n = 840 signals)
- Psychiatric: depression, anxiety, hallucination, suicidal, psychosis terms (n = 2,454 signals)
- Elderly: falls, fractures, dementia, confusion, delirium, renal terms (n = 7,174 signals)
- PCOS/Endometriosis: ovarian, polycystic, androgen, hirsutism, endometrial terms (n = 224 signals)
- Ayurvedic-relevant: hepatic, renal, gastrointestinal, allergic terms (n = 4,016 signals)
- Sexual dysfunction: libido, erectile, orgasm, ejaculation terms (n = 63 signals)

Female fraction was computed as the proportion of signals with direction = "female_higher" within each domain.

### Link Prediction and Drug Similarity

DistMult scoring (h ⊙ r ⊙ t) was used to generate novel link predictions for each KG, excluding known edges. Drug-drug cosine similarity was computed in embedding space to validate pharmacological class recapitulation.

---

## Results

### KG Characteristics and Model Performance

**Table 1. Five Derived Knowledge Graphs: Structure and Embedding Quality**

| KG | Nodes | Edges | Relations | MRR | Hits@1 | Hits@10 | AMRI |
|----|-------|-------|-----------|-----|--------|---------|------|
| REPRODUCT | 13,208 | 384,985 | 8 | **0.1629** | 0.0992 | 0.2844 | 0.959 |
| GERIPHARM | 18,754 | 739,396 | 8 | **0.1438** | 0.0852 | 0.2546 | 0.969 |
| MENTALHEALTH | 17,555 | 705,561 | 8 | **0.1277** | 0.0741 | 0.2279 | 0.967 |
| AYUR-PHARMA | 24,316 | 293,444 | 10 | 0.0887 | 0.0394 | 0.1756 | 0.972 |
| PCOS-ENDO | 36,903 | 697,819 | 9 | 0.0675 | 0.0287 | 0.1337 | 0.980 |
| *Parent DistMult v4.1* | *109,867* | *1,822,851* | *6* | *0.1013* | *0.0481* | *0.1961* | *0.991* |

Three of five derived KGs (REPRODUCT, GERIPHARM, MENTALHEALTH) outperformed the parent DistMult model on MRR, demonstrating that domain-specific extraction improves embedding quality by increasing signal-to-noise ratio. The best-performing derived KG (REPRODUCT, MRR 0.163) exceeded the parent by 61%. An inverse relationship between KG size and MRR was observed: smaller, more focused KGs yielded better embeddings (Spearman ρ = -0.90 between node count and MRR).

### The Sex Bias Spectrum

**Table 2. Sex Bias Across Clinical Domains**

| Domain | Signals | Female (%) | Male (%) | Δ from Baseline |
|--------|---------|------------|----------|-----------------|
| Sexual dysfunction | 63 | **71.4** | 28.6 | +17.6 pp |
| Elderly-relevant AEs | 7,174 | **64.7** | 35.3 | +10.9 pp |
| Ayurvedic-relevant AEs | 4,016 | **64.0** | 36.0 | +10.2 pp |
| Cognitive decline | 603 | **60.5** | 39.5 | +6.7 pp |
| Psychiatric AEs | 2,454 | 54.2 | 45.8 | +0.4 pp |
| **General baseline** | **96,281** | **53.8** | **46.2** | **Reference** |
| Reproductive AEs | 840 | 50.0 | 50.0 | -3.8 pp |
| Hormonal AEs | 389 | 46.8 | 53.2 | -7.0 pp |
| Falls/fractures | 872 | 36.2 | **63.8** | -17.6 pp |
| PCOS/endometriosis AEs | 224 | 21.0 | **79.0** | -32.8 pp |

The sex bias spectrum spans 50.4 percentage points: from 21.0% female (PCOS/endometriosis) to 71.4% female (sexual dysfunction). This spectrum reveals that the commonly cited "female predominance in drug safety" is a domain-averaged artifact that masks substantial heterogeneity.

### Domain-Specific Findings

**Sexual Dysfunction (71.4% Female).** Among 63 sex-differential sexual dysfunction signals across psychiatric drugs, 71.4% were female-biased. This contradicts the clinical perception that SSRI sexual side effects primarily affect men [6]. The finding suggests that while erectile dysfunction is more commonly reported in men, the broader spectrum of sexual dysfunction (decreased libido, anorgasmia, sexual function impairment) disproportionately generates female pharmacovigilance signals.

**Elderly-Relevant AEs (64.7% Female).** Adverse events common in elderly populations (dizziness, hypotension, acute kidney injury, pneumonia, falls, constipation, confusion) showed amplified female bias. However, a paradoxical reversal emerged within the elderly domain: falls and fractures specifically were 63.8% male-biased, suggesting that while elderly women experience more overall drug adverse events, elderly men are disproportionately affected by fall-related drug complications.

**Cognitive Decline (60.5% Female).** Drug-induced cognitive adverse events (dementia, confusion, memory impairment) showed moderate female amplification. Delirium was particularly strongly female-biased (mean logR = 1.093 across 125 drugs), consistent with known sex differences in delirium incidence [7].

**PCOS/Endometriosis AEs (21.0% Female — REVERSED).** The most striking finding was the reversal of sex bias for PCOS/endometriosis-related adverse events. Acne (103 drugs, logR = -0.801), pelvic pain (34 drugs, logR = -1.859), and hirsutism (3 drugs, logR = -1.332) were all male-biased. This paradox — conditions traditionally associated with women generating male-biased pharmacovigilance signals — reflects the reporting structure of FAERS: these AEs are reported as drug side effects across both sexes, and the sex-stratified ROR captures the relative excess in reporting, not the absolute incidence. Male patients reporting these traditionally "female" symptoms as drug adverse effects generates a stronger disproportionality signal.

**Falls/Fractures (36.2% Female — REVERSED).** Within the elderly domain, falls and fractures showed clear male predominance. This may reflect sex differences in bone density drug prescribing patterns, physical activity levels, or differential reporting of fall-related injuries by sex.

### Drug Embedding Validation

Drug-drug cosine similarities in embedding space recapitulated known pharmacological relationships across all five KGs:

| Drug Pair | KG | Cosine Similarity | Known Relationship |
|-----------|---|---|---|
| Aripiprazole ↔ Risperidone | REPRODUCT | 0.998 | Both atypical antipsychotics |
| Morphine ↔ Oxycodone | MENTALHEALTH | 0.993 | Both opioid analgesics |
| Citalopram ↔ Fluoxetine | REPRODUCT | 0.996 | Both SSRIs |
| Apixaban ↔ Rivaroxaban | REPRODUCT | 0.995 | Both direct oral anticoagulants |
| Gabapentin ↔ Pregabalin | REPRODUCT | 0.995 | Both gabapentinoids |
| Tofacitinib ↔ Upadacitinib | MENTALHEALTH | 0.992 | Both JAK inhibitors |
| Carboplatin ↔ Oxaliplatin | GERIPHARM | 0.993 | Both platinum-based chemotherapy |
| Mycophenolic acid ↔ Tacrolimus | MENTALHEALTH | 0.992 | Both immunosuppressants |

These high similarities (>0.99) for pharmacologically related drug pairs validate that the domain-specific embeddings capture meaningful pharmacological structure despite being trained on smaller subsets of the parent KG.

### Ayurvedic-Modern Medicine Bridge

The AYUR-PHARMA-KG connected 5 Ayurvedic herbs (Ashwagandha, Turmeric, Shatavari, Brahmi, Licorice) to modern pharmacovigilance through 37 herb-level edges and 8,033 compound-level connections. Link prediction revealed:

- **Ashwagandha → treats → Polycystic Ovary Syndrome** (validated by traditional Ayurvedic use and emerging clinical evidence [8])
- **Licorice → treats → Infertility, Liver Cirrhosis** (consistent with glycyrrhizin's known hepatoprotective and reproductive effects)
- **Turmeric → treats → Squamous Cell Carcinoma** (consistent with curcumin's anti-cancer research [9])
- **Shatavari → treats → Alzheimer Disease** (novel prediction, plausible via anti-inflammatory mechanisms)

These predictions demonstrate that KG embeddings can bridge traditional and modern medicine, generating testable hypotheses for herb-drug interaction safety studies.

### Hub Analysis

Drug hubs varied by domain: immunosuppressants (adalimumab, methotrexate, prednisone) dominated REPRODUCT-KG and GERIPHARM-KG, reflecting their widespread use in autoimmune conditions affecting pregnant women and elderly patients. Adverse event hubs in REPRODUCT-KG were pregnancy-specific (maternal exposure, foetal exposure, premature baby), while GERIPHARM-KG hubs included geriatric complications (dizziness, hypotension, acute kidney injury, falls).

---

## Discussion

### The Myth of Monolithic Female Predominance

Our analysis reveals that the commonly cited observation that "women experience more drug adverse events" is not uniformly true across all clinical domains. The 50-percentage-point sex bias spectrum — from 21% female in PCOS/endometriosis contexts to 71% female for sexual dysfunction — demonstrates that sex-differential drug safety is a heterogeneous phenomenon that requires domain-specific interpretation.

This finding has important implications for precision pharmacovigilance: a sex-differential signal for a psychiatric drug should be interpreted differently than one for a geriatric drug or a reproductive endocrine drug, because the baseline sex bias differs substantially across these domains.

### Domain Extraction Improves Embedding Quality

The finding that three of five derived KGs outperformed the parent DistMult model provides evidence that domain-specific knowledge graph extraction improves signal-to-noise ratio for embedding-based drug safety prediction. The inverse relationship between KG size and MRR (ρ = -0.90) suggests that focused, domain-specific KGs may be preferable to monolithic approaches for link prediction tasks.

This has practical implications for computational pharmacovigilance: rather than training a single model on the entire drug safety landscape, constructing domain-specific KGs for each therapeutic area may yield more accurate predictions. The trade-off is coverage — larger KGs contain more entities but with diluted signal.

### The PCOS/Endometriosis Paradox

The reversal of sex bias for PCOS/endometriosis-related adverse events is particularly noteworthy. Conditions traditionally associated with women (acne, pelvic pain, hirsutism) show male-biased pharmacovigilance signals when analyzed through sex-stratified reporting odds ratios. This "reproductive paradox" [10] reflects the mathematical structure of the ROR: when a condition is rare in one sex, even a few cases generate a strong disproportionality signal.

This paradox serves as a caution against naively interpreting sex-differential signals: a male-biased signal for pelvic pain does not mean that pelvic pain is more common in male patients, but rather that the reporting rate relative to other adverse events is disproportionately high for males.

### Limitations

1. Domain classification was keyword-based, not ontology-driven, potentially misclassifying some signals.
2. Small sample sizes for some domains (sexual dysfunction: 63 signals, PCOS/endo: 224) limit statistical power.
3. DistMult assumes symmetric scoring, which may not capture directional drug-disease relationships optimally.
4. The Ayurvedic predictions require experimental validation and should be treated as hypothesis-generating.
5. FAERS reporting biases (underreporting, Weber effect, stimulated reporting) affect all domain-specific analyses equally.

---

## Conclusion

Sex bias in drug safety varies by a 50-percentage-point spectrum across clinical domains, from 21% female (PCOS/endometriosis) to 71% female (sexual dysfunction). The assumption of uniform female predominance is an artifact of aggregate analysis. Domain-specific knowledge graph extraction improves embedding quality (3/5 derived KGs outperform the parent model) and reveals sex-bias patterns invisible in monolithic approaches. These findings support domain-specific sex-stratified pharmacovigilance and demonstrate the value of knowledge graph decomposition for precision drug safety.

---

## Data Availability

SexDiffKG v5.2 and all derived KG analyses: https://github.com/jshaik369/SexDiffKG

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
2. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.
3. Franconi F, Campesi I. Sex and gender influences on pharmacological response. Expert Rev Clin Pharmacol. 2014;7:469-485.
4. Shaik MJAA. SexDiffKG: A sex-differential drug safety knowledge graph. 2026. [Preprint]
5. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: Aggregated evidence from globally collected individual case reports during half a century. EClinicalMedicine. 2019;17:100188.
6. Montejo AL, Montejo L, Baldwin DS. The impact of severe mental disorders and psychotropic medications on sexual health and its implications for clinical management. World Psychiatry. 2018;17(1):3-11.
7. Marcantonio ER. Delirium in Hospitalized Older Adults. N Engl J Med. 2017;377(15):1456-1466.
8. Goswami PK, Khale A, Ogale S. Natural remedies for polycystic ovarian syndrome (PCOS): A review. Int J Pharm Phytopharmacol Res. 2012;1(6):396-402.
9. Kunnumakkara AB, et al. Curcumin, the golden nutraceutical: multitargeting for multiple chronic diseases. Br J Pharmacol. 2017;174(11):1325-1348.
10. Shaik MJAA. The reproductive paradox in sex-differential drug safety. 2026. [Manuscript in preparation]

---

## Figure Legends

**Figure 1.** Derived knowledge graph overview. (A-E) Node type composition for each of the five domain-specific KGs. (F) Size comparison showing nodes (blue) and edges (red) across KGs.

**Figure 2.** The sex bias spectrum. Horizontal bar chart showing female fraction for nine clinical domains, ranging from PCOS/endometriosis (21.0%F) to sexual dysfunction (71.4%F). Dashed line at 50% indicates sex parity; the general baseline (53.8%F) is shown for reference. Red bars indicate female-dominant domains; blue bars indicate male-dominant domains.

**Figure 3.** Embedding quality vs. KG size. (A) MRR for each derived KG compared to the parent DistMult v4.1 baseline (dashed line). Three of five KGs exceed the parent MRR. (B) Inverse relationship between node count and MRR (Spearman ρ = -0.90).

**Figure 4.** Domain-specific drug safety predictions. (A) Top predicted sex-differential adverse events for high-hub drugs in each KG. (B) Drug embedding similarity heatmap for the top 15 drugs in REPRODUCT-KG, showing pharmacological class clustering.

**Figure 5.** Cross-KG comparison dashboard. Six-panel figure combining MRR comparison, sex bias spectrum, KG size, signal coverage, general vs. domain sex bias scatter, and summary statistics card.

**Figure 6.** Ayurvedic-modern medicine bridge. Network visualization showing herb → compound → protein target → drug → adverse event pathways in AYUR-PHARMA-KG, with predicted herb-disease associations highlighted.
