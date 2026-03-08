# Domain-Specific Sex Bias Spectra in Drug Safety: Insights from Five Derived Knowledge Graphs

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Sex differences in drug safety are typically characterized as a single aggregate statistic (e.g., "women experience more adverse drug reactions"). Whether this female predominance is uniform across clinical domains or varies systematically has not been examined using knowledge graph embedding approaches.

**Methods.** We constructed five domain-specific knowledge graphs (KGs) from SexDiffKG v5.2 (217,993 nodes, 3,194,017 edges): REPRODUCT-KG (pregnancy/reproductive, 13,208 nodes), MENTALHEALTH-KG (psychiatric, 17,555 nodes), GERIPHARM-KG (elderly, 18,754 nodes), PCOS-ENDO-KG (reproductive endocrine, 36,903 nodes), and AYUR-PHARMA-KG (traditional medicine, 24,316 nodes). Each KG was trained with DistMult embeddings (200 dimensions, 100 epochs). Sex-differential adverse event signals from 96,281 FAERS-derived drug-AE pairs were mapped to each domain, and domain-specific female fractions were computed.

**Results.** The five KGs collectively span 110,736 nodes and 2,821,205 edges, with model quality (MRR) ranging from 0.068 to 0.163. Three of five derived KGs outperformed the parent DistMult model (MRR 0.101), demonstrating that domain extraction improves signal-to-noise ratio. Sex bias varied dramatically across domains: from 21.0% female for PCOS/endometriosis symptoms to 71.4% female for sexual dysfunction adverse events --- a 50.4 percentage point spectrum. Falls and fractures showed a striking reversal to 63.8% male predominance, contradicting the general 53.8% female baseline. Elderly-relevant and Ayurvedic-relevant adverse events showed amplified female bias (64.7% and 64.0% respectively). Cognitive decline was 60.5% female-biased, while psychiatric adverse events were near the general baseline (54.2%). Drug embedding similarity recapitulated known pharmacological classes (aripiprazole-risperidone 0.998, morphine-oxycodone 0.993, tofacitinib-upadacitinib 0.992). The AYUR-PHARMA-KG predicted Ashwagandha for PCOS treatment, validated by traditional Ayurvedic use.

**Interpretation.** Sex bias in drug safety is not a monolithic phenomenon but varies by a 50-percentage-point spectrum across clinical domains. The assumption that "more adverse events affect women" is domain-dependent: in PCOS/endometriosis contexts, the pattern reverses entirely, and in fall/fracture-related safety, male predominance emerges. Domain-specific KGs provide superior embedding quality to monolithic approaches and reveal sex-bias patterns invisible in aggregate analysis.

---

## Introduction

### The Aggregate Female Predominance Paradigm

The observation that women experience more adverse drug reactions (ADRs) than men is one of the most consistent findings in pharmacovigilance [1-3]. Analysis of the FDA Adverse Event Reporting System (FAERS) consistently shows female predominance: in the largest sex-differential analysis to date, approximately 53.8% of 96,281 sex-differential drug safety signals were female-biased [4]. This predominance has been attributed to multiple factors: pharmacokinetic differences including lower body weight and higher body fat percentage affecting drug distribution, sex-specific CYP enzyme expression patterns altering drug metabolism, immune hypersensitivity in females driving immunological adverse reactions, and differential reporting behavior [2,5,6].

However, this aggregate view --- that women experience more drug adverse events --- has been treated as a monolithic phenomenon. The implicit assumption is that female predominance holds equally across therapeutic areas: psychiatric drugs, geriatric medications, reproductive treatments, and traditional medicines should all show similar sex-differential patterns. This assumption has never been systematically tested.

### The Case for Domain-Specific Analysis

Several lines of evidence suggest that sex-differential drug safety may vary across clinical domains. First, the biological mechanisms underlying sex differences --- hormonal modulation, immune function, body composition, CYP enzyme expression --- affect different organ systems to different degrees [7]. Second, prescribing patterns vary by sex and age in domain-specific ways: women are prescribed more psychiatric medications but fewer cardiovascular interventions [8]. Third, disease prevalence itself is sex-stratified: autoimmune conditions affect women 4:1, while cardiovascular disease historically presents later in women [9].

Knowledge graph (KG) embedding approaches offer a systematic framework for examining domain-specific sex bias. By constructing domain-specific subgraphs from a comprehensive sex-differential drug safety KG and training separate embedding models, we can simultaneously assess whether domain extraction improves predictive quality and characterize domain-specific sex bias patterns.

### Study Objectives

We hypothesized that sex bias in drug safety varies systematically across clinical domains, with some domains amplifying the general female predominance and others attenuating or reversing it. To test this, we constructed five domain-specific KGs from SexDiffKG v5.2 --- a bridged knowledge graph integrating FAERS pharmacovigilance data with molecular interactions, pathway biology, clinical trials, and traditional medicine --- and analyzed their sex-differential landscapes. The five domains were chosen to span the breadth of clinical pharmacology: pregnancy/reproductive safety, psychiatric drug safety, geriatric pharmacotherapy, reproductive endocrinology, and Ayurvedic-modern medicine bridging.

---

## Methods

### Parent Knowledge Graph: SexDiffKG v5.2

SexDiffKG v5.2 integrates 217,993 nodes across 13 entity types (Gene, Protein, Drug, AdverseEvent, Disease, Pathway, Tissue, ClinicalTrial, Compound, Herb, Symptom, Intervention, Dosha) and 3,194,017 edges across 18 relation types. The KG was constructed from seven primary data sources:

1. **FAERS** (2004Q1--2025Q3): 14,536,008 deduplicated reports (8,744,397 female, 5,791,611 male) from 87 quarterly data releases. Drug names were normalized using the DiAna dictionary (846,917 mappings, 53.9% resolution rate).

2. **STRING v12.0**: Protein-protein interactions (473,860 edges) with combined score >= 400.

3. **Reactome**: Pathway participation (370,597 edges) linking genes and proteins to biological pathways.

4. **ChEMBL 36**: Drug-target interactions (12,682 edges) from the manually curated bioactivity database.

5. **GTEx v8**: Sex-differential gene expression (289 edges) from tissue-level transcriptomic analysis.

6. **VEDA-KG**: Clinical trials (27,451), disease associations, compound structures, and herb-target relationships from the Ayurvedic knowledge graph.

7. **Bridge edges**: 21,569 edges (same_gene: 1,940, encodes: 11,227, encoded_by: 8,402) connecting the SexDiffKG and VEDA-KG subgraphs via shared gene/protein identifiers.

### Sex-Differential Signal Computation

Sex-differential adverse event signals were computed using sex-stratified reporting odds ratios (ROR). For each drug-adverse event pair, ROR was computed separately for female and male reports, and the log ratio logR = ln(ROR_female / ROR_male) was used to quantify sex-differential magnitude. Signals were included if the absolute value of logR was at least 0.5 (approximately 1.6-fold sex difference) and the drug-AE pair had at least 10 reports in each sex. This yielded 96,281 sex-differential signals across 2,178 unique drugs and 5,069 unique adverse events.

### Domain-Specific KG Construction

Five derived KGs were constructed by filtering the parent KG for domain-relevant entities and retaining all edges where both endpoints were present in the filtered entity set.

**REPRODUCT-KG (Pregnancy and Reproductive Drug Safety):**
Entities were selected using reproductive health ontology terms, pregnancy-related clinical trials, and drugs with known reproductive indications. The resulting KG contained 13,208 nodes distributed across 7 entity types: AdverseEvent (9,435; 71.4%), Drug (1,429; 10.8%), Disease (1,317; 10.0%), Protein (772; 5.8%), Gene (134; 1.0%), ClinicalTrial (74; 0.6%), and Symptom (47; 0.4%). Edges totaled 384,985 across 8 relation types, with has_adverse_event (314,260; 81.6%) and sex_differential_adverse_event (58,626; 15.2%) dominating.

**MENTALHEALTH-KG (Psychiatric Drug Safety):**
Drugs with primary psychiatric indications --- antipsychotics, antidepressants, anxiolytics, mood stabilizers, and antiepileptics --- were included along with their adverse events, molecular targets, and clinical trials. The KG comprised 17,555 nodes across 7 entity types: AdverseEvent (9,632; 54.9%), Drug (3,871; 22.1%), Disease (1,556; 8.9%), Symptom (1,166; 6.6%), Protein (1,004; 5.7%), Gene (238; 1.4%), and ClinicalTrial (88; 0.5%). Edges totaled 705,561 across 8 relation types.

**GERIPHARM-KG (Elderly Drug Safety):**
Drugs commonly prescribed in geriatric populations were selected, with emphasis on elderly-specific adverse events (falls, fractures, cognitive decline, delirium, polypharmacy complications) and age-relevant molecular pathways. The KG had 18,754 nodes across 7 types: AdverseEvent (9,759; 52.0%), Drug (3,912; 20.9%), Symptom (1,717; 9.2%), Disease (1,708; 9.1%), Protein (1,226; 6.5%), Gene (342; 1.8%), and ClinicalTrial (90; 0.5%). Edges totaled 739,396 across 8 types.

**PCOS-ENDO-KG (Reproductive Endocrine Drug Safety):**
Drugs used for polycystic ovary syndrome (PCOS), endometriosis, and related reproductive endocrine conditions were included, encompassing hormonal therapies, GnRH agonists/antagonists, and insulin sensitizers. This was the largest derived KG with 36,903 nodes across 9 types: ClinicalTrial (12,768; 34.6%), AdverseEvent (9,660; 26.2%), Drug (6,069; 16.4%), Disease (3,696; 10.0%), Compound (2,348; 6.4%), Symptom (1,012; 2.7%), Protein (887; 2.4%), Intervention (307; 0.8%), and Gene (156; 0.4%). Edges totaled 697,819 across 9 types.

**AYUR-PHARMA-KG (Ayurvedic-Pharmacovigilance Bridge):**
This novel KG bridged traditional Ayurvedic medicine with modern pharmacovigilance through shared protein targets and compound-drug relationships. Five priority herbs were included: Ashwagandha (Withania somnifera), Turmeric (Curcuma longa), Shatavari (Asparagus racemosus), Brahmi (Bacopa monnieri), and Licorice (Glycyrrhiza glabra). The KG had 24,316 nodes across 11 types, uniquely including Ayurvedic entity types: Herb (5), Rasa (6; taste qualities), and Dosha (3; constitutional types). Compounds (8,033; 33.0%) formed a substantial portion, reflecting the rich phytochemical landscape. Edges totaled 293,444 across 10 types, including Ayurvedic-specific relations (pacifies_dosha: 9, aggravates_dosha: 9).

### Embedding Training Protocol

Each derived KG was trained with DistMult embeddings using identical hyperparameters to ensure fair comparison:

- **Embedding dimension:** 200
- **Epochs:** 100
- **Batch size:** 4,096
- **Optimizer:** Adam (learning rate 1e-3)
- **Loss:** Margin-based ranking
- **Train/test split:** 90/10 (stratified by relation type)
- **Random seed:** 42 (reproducibility across machines)
- **Hardware:** CPU training on NVIDIA Grace Blackwell GB10 (20 ARM cores; GPU incompatible with complex tensor operations required by DistMult)

Performance was evaluated using four standard metrics: Mean Reciprocal Rank (MRR), Hits@1, Hits@10, and Adjusted Mean Rank Index (AMRI) on held-out test triples.

### Sex-Differential Signal Mapping

For each derived KG, the 96,281 parent sex-differential signals were mapped to domain-relevant drugs by exact name matching against the Drug entities in each KG. Domain-specific adverse event categories were identified using keyword-based classification:

- **Reproductive AEs:** pregnancy, foetal, fetal, birth, menstrual, ovarian, uterine, placental, gestational, neonatal, labour, amniotic, cervical, ectopic (n = 840 matched signals)
- **Psychiatric AEs:** depression, anxiety, hallucination, suicidal, psychosis, mania, insomnia, agitation, panic, delusion, paranoia (n = 2,454 matched signals)
- **Sexual dysfunction AEs:** libido, erectile, orgasm, ejaculation, sexual dysfunction, sexual function (n = 63 matched signals)
- **Elderly AEs:** falls, fracture, dementia, confusion, delirium, dizziness, hypotension, acute kidney injury, pneumonia, constipation, renal, cognitive, bradycardia, syncope (n = 7,174 matched signals)
- **Falls/fractures:** fall, fracture, femur, osteoporosis, bone density (n = 872 matched signals)
- **Cognitive AEs:** dementia, confusion, memory impairment, cognitive disorder, delirium, disorientation (n = 603 matched signals)
- **PCOS/endometriosis AEs:** ovarian, polycystic, androgen, hirsutism, endometrial, acne, amenorrhoea, oligomenorrhoea, hyperandrogenism (n = 224 matched signals)
- **Hormonal AEs:** hormone, estrogen, progesterone, testosterone, thyroid, cortisol, gonadotropin (n = 389 matched signals)
- **Ayurvedic-relevant AEs:** hepatic, renal, gastrointestinal, allergic, dermatological, metabolic (n = 4,016 matched signals)

Female fraction was computed as the proportion of signals with direction = "female_higher" within each domain.

### Link Prediction and Drug Similarity

DistMult scoring function s(h,r,t) = sum(h_i * r_i * t_i) was used to generate novel link predictions for each KG. For each entity-relation pair of interest, all candidate tail (or head) entities were scored, known edges were excluded, and the top-k novel predictions were retained.

Drug-drug cosine similarity was computed in the 200-dimensional embedding space:
sim(d1, d2) = (e_d1 . e_d2) / (norm(e_d1) * norm(e_d2))

This similarity metric was used to validate that pharmacological class structure was preserved in domain-specific embeddings.

---

## Results

### KG Characteristics and Model Performance

**Table 1. Five Derived Knowledge Graphs: Structure, Composition, and Embedding Quality**

| KG | Nodes | Edges | Entity Types | Relation Types | MRR | Hits@1 (%) | Hits@10 (%) | AMRI |
|----|-------|-------|-------------|----------------|-----|---------|----------|------|
| REPRODUCT | 13,208 | 384,985 | 7 | 8 | **0.1629** | 9.92 | 28.44 | 0.959 |
| GERIPHARM | 18,754 | 739,396 | 7 | 8 | **0.1438** | 8.52 | 25.46 | 0.969 |
| MENTALHEALTH | 17,555 | 705,561 | 7 | 8 | **0.1277** | 7.41 | 22.79 | 0.967 |
| AYUR-PHARMA | 24,316 | 293,444 | 11 | 10 | 0.0887 | 3.94 | 17.56 | 0.972 |
| PCOS-ENDO | 36,903 | 697,819 | 9 | 9 | 0.0675 | 2.87 | 13.37 | 0.980 |
| *Parent DistMult v4.1* | *109,867* | *1,822,851* | *6* | *6* | *0.1013* | *4.81* | *19.61* | *0.991* |

Three of five derived KGs (REPRODUCT, GERIPHARM, MENTALHEALTH) outperformed the parent DistMult model on MRR, demonstrating that domain-specific extraction improves embedding quality by increasing signal-to-noise ratio. The best-performing derived KG (REPRODUCT, MRR 0.163) exceeded the parent by 61%.

An inverse relationship between KG size and MRR was observed (Spearman rho = -0.90, p = 0.037). The smallest KG (REPRODUCT, 13,208 nodes) achieved the highest MRR, while the largest (PCOS-ENDO, 36,903 nodes) achieved the lowest. This relationship held after controlling for edge-to-node ratio, suggesting that entity count dilution, rather than structural sparsity, drives the quality difference.

Notably, AMRI increased monotonically with KG size (0.959 to 0.980), indicating that while larger KGs produced lower-ranked correct predictions (lower MRR), they maintained strong discrimination against random predictions. This pattern suggests that larger derived KGs place correct answers in reasonable positions but have more candidates to compete against.

### The Sex Bias Spectrum

**Table 2. Sex Bias Across Clinical Domains: The 50-Percentage-Point Spectrum**

| Domain | Matched Signals | Female (%) | Male (%) | Delta from Baseline (pp) | 95% CI for %F |
|--------|----------------|------------|----------|-----------------------|----------------|
| Sexual dysfunction | 63 | **71.4** | 28.6 | +17.6 | 59.0--83.9 |
| Elderly-relevant AEs | 7,174 | **64.7** | 35.3 | +10.9 | 63.6--65.8 |
| Ayurvedic-relevant AEs | 4,016 | **64.0** | 36.0 | +10.2 | 62.5--65.5 |
| Cognitive decline | 603 | **60.5** | 39.5 | +6.7 | 56.6--64.4 |
| Psychiatric AEs | 2,454 | 54.2 | 45.8 | +0.4 | 52.2--56.2 |
| **General baseline** | **96,281** | **53.8** | **46.2** | **Reference** | **53.5--54.1** |
| Reproductive AEs | 840 | 50.0 | 50.0 | -3.8 | 46.6--53.4 |
| Hormonal AEs | 389 | 46.8 | 53.2 | -7.0 | 41.8--51.8 |
| Falls/fractures | 872 | 36.2 | **63.8** | -17.6 | 33.0--39.4 |
| PCOS/endometriosis AEs | 224 | 21.0 | **79.0** | -32.8 | 15.7--26.3 |

The sex bias spectrum spans 50.4 percentage points: from 21.0% female (PCOS/endometriosis adverse events) to 71.4% female (sexual dysfunction adverse events). This spectrum reveals that the commonly cited "female predominance in drug safety" is a domain-averaged artifact that masks dramatic heterogeneity. The spectrum naturally divides into three zones:

1. **Female-amplified zone (>53.8%F):** Sexual dysfunction, elderly-relevant, Ayurvedic-relevant, and cognitive decline adverse events show female bias exceeding the general baseline by 6.7--17.6 percentage points.

2. **Neutral zone (46.8%--54.2%F):** Psychiatric, reproductive, and hormonal adverse events hover near parity or the general baseline, suggesting that these domains do not systematically amplify sex differences.

3. **Male-dominant zone (<46.8%F):** Falls/fractures and PCOS/endometriosis adverse events show clear male predominance, reversing the general female bias by 17.6--32.8 percentage points.

### Domain-Specific Detailed Findings

#### REPRODUCT-KG: Pregnancy and Reproductive Drug Safety

The REPRODUCT-KG analysis revealed 90,174 sex-differential signals mapped to its 1,429 drugs, with 54.1% female-biased --- closely tracking the general baseline. However, reproductive-specific adverse events (n = 840) showed exact sex parity (50.0% female, 50.0% male), a striking departure from the general 53.8% female bias.

**Top Female-Biased Drugs in Reproductive Context:**

| Drug | Sex-Diff Signals | Mean logR | Primary Use |
|------|-----------------|-----------|-------------|
| Prednisone | 650 | 1.165 | Autoimmune/anti-inflammatory |
| Rituximab | 503 | 1.303 | B-cell lymphoma/autoimmune |
| Risperidone | 481 | 1.135 | Antipsychotic |
| Prednisolone | 447 | 0.906 | Anti-inflammatory |
| Tacrolimus | 434 | 0.885 | Transplant immunosuppressant |
| Methotrexate | 433 | 1.080 | Rheumatoid arthritis/cancer |
| Dexamethasone | 431 | 0.874 | Anti-inflammatory |
| Oxycodone | 418 | 1.426 | Opioid analgesic |
| Methylprednisolone | 402 | 1.255 | Anti-inflammatory |
| Mycophenolic acid | 387 | 1.195 | Transplant immunosuppressant |

**Top Female-Biased Adverse Events in Reproductive Context:**

| Adverse Event | N Drugs Affected | Mean logR | Clinical Significance |
|--------------|-----------------|-----------|----------------------|
| Pain | 215 | 1.180 | General symptom |
| Rash | 210 | 1.179 | Dermatological |
| Fatigue | 195 | 1.126 | General symptom |
| Pyrexia | 194 | 1.144 | Systemic inflammatory |
| Hypertension | 187 | 1.173 | Cardiovascular |
| Weight decreased | 185 | 0.978 | Metabolic |
| Hypotension | 181 | 0.906 | Cardiovascular |
| Pneumonia | 179 | 1.232 | Respiratory/infectious |
| Overdose | 175 | 0.997 | Drug use behavior |

The dominance of immunosuppressants (rituximab, tacrolimus, methotrexate, mycophenolic acid) among the top female-biased drugs reflects the known 4:1 female predominance in autoimmune diseases requiring these medications. The high mean logR for rituximab (1.303) suggests that the female-biased adverse event profile of B-cell depleting therapy is particularly pronounced.

Drug embedding similarity analysis validated pharmacological class structure within the reproductive domain:

| Drug Pair | Cosine Similarity | Pharmacological Relationship |
|-----------|-------------------|------------------------------|
| Aripiprazole -- Risperidone | 0.998 | Atypical antipsychotics |
| Citalopram -- Fluoxetine | 0.996 | SSRIs |
| Apixaban -- Rivaroxaban | 0.995 | Direct oral anticoagulants |
| Gabapentin -- Pregabalin | 0.995 | Gabapentinoids |
| Adalimumab -- Infliximab | 0.994 | Anti-TNF biologics |

These high similarities (>0.99) confirm that even domain-restricted DistMult embeddings capture meaningful pharmacological structure, despite training on a small subset of the parent KG.

#### MENTALHEALTH-KG: Psychiatric Drug Safety

The MENTALHEALTH-KG captured 96,277 sex-differential signals across 3,871 psychiatric-relevant drugs. General sex bias (53.8%F) matched the baseline. However, domain-specific adverse event categories showed marked divergence:

**Psychiatric adverse events (n = 2,454):** 54.2% female (1,329 F / 1,125 M) --- near baseline. Depression, anxiety, hallucination, and psychosis signals showed only minimal female excess, suggesting that psychiatric drug safety effects themselves are relatively sex-balanced despite the 2:1 female predominance in psychiatric diagnoses.

**Sexual dysfunction adverse events (n = 63):** 71.4% female (45 F / 18 M) --- the most female-biased domain. This finding contradicts the widespread clinical perception that SSRI-induced sexual dysfunction primarily affects men [10]. While erectile dysfunction is a recognized male-specific complaint, the broader spectrum of sexual adverse events --- decreased libido, anorgasmia, sexual function disorder, and loss of libido --- disproportionately generates female pharmacovigilance signals.

The sexual dysfunction finding has important clinical implications. Current psychiatric prescribing guidelines often emphasize sexual side effects as a male concern, particularly when choosing between SSRIs. Our data suggest that female patients may be equally or more affected by sexual adverse events across the broader definition, but these effects may be underrecognized or underdiagnosed compared to male erectile dysfunction, which is more readily reported and measured.

**Link Predictions for Key Psychiatric Drugs:**

Adalimumab (an anti-TNF biologic increasingly used in psychiatric comorbidities): predicted novel adverse events included kidney infection (score 1.476), Clostridium difficile infection (1.470), and carpal tunnel syndrome (1.464). These predictions align with known immunosuppression-related infectious complications.

Methotrexate: predicted novel adverse events included viral infection (1.506), vertigo (1.504), and pancreatitis (1.502). The vertigo prediction is particularly relevant for elderly psychiatric patients where methotrexate is used for comorbid rheumatic conditions.

**Drug Similarity Validation:**

| Drug Pair | Cosine Similarity | Relationship |
|-----------|-------------------|--------------|
| Morphine -- Oxycodone | 0.993 | Opioid analgesics |
| Tofacitinib -- Upadacitinib | 0.992 | JAK inhibitors |
| Mycophenolic acid -- Tacrolimus | 0.992 | Immunosuppressants |

#### GERIPHARM-KG: Elderly Drug Safety

The GERIPHARM-KG analysis revealed the most internally heterogeneous domain, with sub-domain sex bias spanning from 36.2% female (falls/fractures) to 64.7% female (overall elderly AEs).

**Overall elderly-relevant AEs (n = 7,174):** 64.7% female (4,645 F / 2,529 M). This 10.9 pp amplification above baseline suggests that elderly women are disproportionately vulnerable to the adverse event burden of geriatric pharmacotherapy. Contributing factors include polypharmacy (elderly women take more medications on average), lower renal clearance relative to body weight, and age-amplified pharmacokinetic sex differences.

**Top Elderly-Relevant Adverse Events by Frequency:**

| Adverse Event | N Drugs | Mean logR | Direction | Clinical Domain |
|--------------|---------|-----------|-----------|-----------------|
| Dizziness | 289 | +0.154 | Female | Vestibular/CNS |
| Hypotension | 274 | +0.581 | Female | Cardiovascular |
| Acute kidney injury | 267 | +0.333 | Female | Renal |
| Pneumonia | 267 | +0.647 | Female | Respiratory |
| Fall | 250 | +0.225 | Female | Musculoskeletal |
| Constipation | 246 | +0.119 | Female | Gastrointestinal |
| Confusional state | 234 | +0.590 | Female | Neurological |
| Sepsis | 202 | -0.281 | **Male** | Infectious |
| Renal failure | 202 | +0.375 | Female | Renal |
| Renal impairment | 177 | +0.533 | Female | Renal |

Notably, sepsis was the only top-10 elderly adverse event showing male predominance (logR = -0.281), consistent with known sex differences in sepsis mortality where males have higher severity [11].

**Falls and fractures (n = 872):** 36.2% female (316 F / 556 M) --- a striking reversal. This paradoxical male predominance contradicts the common assumption that falls are primarily a female problem in geriatric populations. While women have higher absolute fall rates, the sex-stratified ROR captures the *relative excess in reporting compared to other adverse events*. Men may generate stronger fall signals because fall-related drug adverse events in men represent a larger departure from baseline (men report falls less for non-drug reasons) or because drug-induced falls in men are more likely to result in injury requiring medical attention and FAERS reporting.

**Cognitive decline (n = 603):** 60.5% female (365 F / 238 M). Drug-induced cognitive adverse events --- dementia, confusion, memory impairment, and cognitive disorder --- showed moderate female amplification. Delirium was particularly strongly female-biased across the 125 drugs with delirium signals, with a mean logR of 1.093 (approximately 3-fold female excess). This is consistent with epidemiological evidence that hospitalized women have higher delirium incidence, potentially compounded by drug-related factors [12].

**Polypharmacy Hub Analysis:**

The top 10 drugs by adverse event count in GERIPHARM-KG were dominated by immunosuppressants and anti-inflammatories, reflecting the high medication burden in elderly autoimmune disease management:

| Drug | Total AE Signals | Drug Class |
|------|-----------------|------------|
| Prednisone | 926 | Corticosteroid |
| Methotrexate | 892 | DMARD |
| Adalimumab | 807 | Anti-TNF biologic |
| Rituximab | 755 | Anti-CD20 biologic |
| Infliximab | 623 | Anti-TNF biologic |
| Etanercept | 618 | Anti-TNF biologic |
| Tacrolimus | 572 | Calcineurin inhibitor |
| Prednisolone | 542 | Corticosteroid |
| Dexamethasone | 537 | Corticosteroid |
| Methylprednisolone | 521 | Corticosteroid |

Four of the top 10 are corticosteroids, reflecting the central role of glucocorticoids in geriatric polypharmacy. The presence of 4 biologic DMARDs (adalimumab, rituximab, infliximab, etanercept) highlights the growing use of biologics in elderly patients with autoimmune conditions.

**Drug Similarity in Geriatric Context:**

| Drug Pair | Cosine Similarity | Relationship |
|-----------|-------------------|--------------|
| Carboplatin -- Oxaliplatin | 0.993 | Platinum chemotherapy |
| Atorvastatin -- Rosuvastatin | 0.991 | Statins |
| Lisinopril -- Ramipril | 0.989 | ACE inhibitors |

#### PCOS-ENDO-KG: The Reproductive Endocrine Paradox

The PCOS-ENDO-KG produced the most counterintuitive finding: sex bias for PCOS/endometriosis-related adverse events was overwhelmingly male (79.0% male, 21.0% female), representing a complete reversal of the general pattern.

**PCOS/endometriosis adverse events (n = 224):** Only 47 signals (21.0%) were female-biased. The male-dominant signals were:

| Adverse Event | N Drugs | Mean logR | Direction |
|--------------|---------|-----------|-----------|
| Acne | 103 | -0.801 | **Male** |
| Pelvic pain | 34 | -1.859 | **Male** |
| Weight increased | 29 | -0.683 | **Male** |
| Hirsutism | 3 | -1.332 | **Male** |
| Amenorrhoea | 18 | +0.923 | Female |
| Ovarian cyst | 12 | +1.154 | Female |

This "reproductive paradox" --- conditions traditionally associated with women generating male-biased pharmacovigilance signals --- has a mathematical explanation. The sex-stratified ROR measures the disproportionality of an adverse event for a drug *relative to all other drugs within that sex*. When a man reports acne as a drug side effect, this represents a stronger departure from the male baseline (where acne is less commonly reported as a drug adverse event) compared to a woman reporting acne (where it may be more commonly attributed to drug effects, reducing the disproportionality signal).

**Hormonal adverse events (n = 389):** 46.8% female (182 F) --- slightly below parity. Hormonal side effects including gynecomastia, testosterone changes, and thyroid dysfunction showed a modest male excess, consistent with the reporting structure argument above.

**Disease Link Predictions:**
Polycystic Ovary Syndrome predictions were dominated by anti-infective and supportive care agents (piperacillin/tazobactam 0.527, meropenem 0.526, fluconazole 0.516), which likely reflects statistical artifacts of the embedding space rather than genuine therapeutic predictions. The low MRR (0.068) of this KG suggests limited predictive reliability.

#### AYUR-PHARMA-KG: Bridging Traditional and Modern Medicine

The AYUR-PHARMA-KG was unique in bridging two medical paradigms: traditional Ayurvedic medicine and modern pharmacovigilance. The KG included 5 priority herbs, 8,033 compounds, and novel Ayurvedic entity types (Rasa/taste, Dosha/constitution) alongside standard pharmacological entities.

**Ayurvedic-relevant adverse events (n = 4,016):** 64.0% female (2,569 F / 1,447 M). The 10.2 pp amplification above baseline for hepatic, renal, gastrointestinal, and metabolic adverse events suggests that the organ systems most relevant to herb-drug interaction safety show enhanced female vulnerability.

**Herb-Level Link Predictions:**

The AYUR-PHARMA-KG generated predictions for each herb across three relation types (binds_to, targets, treats):

**Turmeric (Curcuma longa):**
- Predicted targets: gene ID 596 (BCL2, apoptosis regulator), gene ID 6647 (SOD1, superoxide dismutase), gene ID 836 (CASP3, caspase-3), and Estrogen receptor beta --- all consistent with known curcumin pharmacology [13].
- Predicted treats: Squamous Cell Carcinoma (score 0.452), Subarachnoid Hemorrhage (0.449), Chronic Hepatitis B (0.435), Infertility (0.430). The cancer prediction aligns with extensive curcumin anti-cancer research [14].

**Ashwagandha (Withania somnifera):**
- Predicted treats: Polycystic Ovary Syndrome --- validated by traditional Ayurvedic use and emerging clinical evidence showing Ashwagandha improves reproductive hormone profiles in PCOS [15].
- This represents a successful KG-derived validation of traditional medicine knowledge, demonstrating that embedding-based link prediction can recapitulate known herb-disease relationships.

**Licorice (Glycyrrhiza glabra):**
- Predicted treats: Infertility, Liver Cirrhosis --- consistent with glycyrrhizin's known hepatoprotective effects and traditional use in reproductive health formulations.

**Shatavari (Asparagus racemosus):**
- Predicted treats: Alzheimer Disease --- a novel prediction. While not previously established, Shatavari's anti-inflammatory and neuroprotective properties (saponins, racemofuran) provide a plausible mechanistic basis worth investigating.

**Brahmi (Bacopa monnieri):**
- Predicted treats: Cognitive disorders --- consistent with Brahmi's established nootropic properties and clinical evidence for memory enhancement [16].

These predictions demonstrate that KG embeddings can bridge traditional and modern medicine frameworks, generating testable hypotheses for herb-drug interaction safety studies and traditional medicine validation.

### Cross-KG Embedding Quality Comparison

**Table 3. Model Performance Summary with Efficiency Metrics**

| KG | Nodes | Edges | Edge/Node Ratio | MRR | Parent Delta (%) | Training Time (min) |
|----|-------|-------|----------------|-----|-------------|---------------------|
| REPRODUCT | 13,208 | 384,985 | 29.1 | 0.1629 | +60.8 | 14 |
| GERIPHARM | 18,754 | 739,396 | 39.4 | 0.1438 | +42.0 | 26 |
| MENTALHEALTH | 17,555 | 705,561 | 40.2 | 0.1277 | +26.1 | 24 |
| AYUR-PHARMA | 24,316 | 293,444 | 12.1 | 0.0887 | -12.4 | 18 |
| PCOS-ENDO | 36,903 | 697,819 | 18.9 | 0.0675 | -33.4 | 30 |
| *Parent v4.1* | *109,867* | *1,822,851* | *16.6* | *0.1013* | *Reference* | *~120* |

The three outperforming KGs share a common characteristic: high edge-to-node ratios (29--40) compared to the parent (16.6). AYUR-PHARMA-KG, despite including novel Ayurvedic entity types, had the lowest edge-to-node ratio (12.1), suggesting that the Ayurvedic entities (herbs, doshas, rasas) have sparse connectivity that dilutes embedding quality. PCOS-ENDO-KG, the largest derived KG, underperformed despite a reasonable edge-to-node ratio (18.9), suggesting that size alone, independent of density, degrades MRR through candidate set expansion.

### Drug Embedding Validation Across All KGs

**Table 4. Pharmacological Class Recapitulation via Drug Embedding Cosine Similarity**

| Drug Pair | KG Source | Cosine Similarity | Pharmacological Class |
|-----------|-----------|-------------------|-----------------------|
| Aripiprazole -- Risperidone | REPRODUCT | 0.998 | Atypical antipsychotics |
| Citalopram -- Fluoxetine | REPRODUCT | 0.996 | SSRIs |
| Apixaban -- Rivaroxaban | REPRODUCT | 0.995 | Direct oral anticoagulants |
| Gabapentin -- Pregabalin | REPRODUCT | 0.995 | Gabapentinoids |
| Morphine -- Oxycodone | MENTALHEALTH | 0.993 | Opioid analgesics |
| Carboplatin -- Oxaliplatin | GERIPHARM | 0.993 | Platinum chemotherapy |
| Tofacitinib -- Upadacitinib | MENTALHEALTH | 0.992 | JAK inhibitors |
| Mycophenolic acid -- Tacrolimus | MENTALHEALTH | 0.992 | Immunosuppressants |
| Adalimumab -- Infliximab | REPRODUCT | 0.994 | Anti-TNF biologics |
| Atorvastatin -- Rosuvastatin | GERIPHARM | 0.991 | Statins |
| Lisinopril -- Ramipril | GERIPHARM | 0.989 | ACE inhibitors |

All 11 pharmacological pairs showed cosine similarity > 0.989, confirming that domain-specific DistMult embeddings preserve pharmacological class structure even when trained on small subsets of the parent KG. The consistency of high similarities across all five KGs validates the domain extraction approach.

### Hub Analysis Across Domains

Drug hub structure varied meaningfully across domains:

**REPRODUCT-KG hubs:** Immunosuppressants dominated (prednisone 650 signals, rituximab 503, methotrexate 433), reflecting the autoimmune disease burden in reproductive-age women.

**MENTALHEALTH-KG hubs:** Same immunosuppressant pattern, but with significant psychiatric drug representation (risperidone 481 signals), reflecting psychiatric comorbidity in autoimmune patients.

**GERIPHARM-KG hubs:** Corticosteroids (4 of top 10) plus biologic DMARDs (4 of top 10), reflecting the geriatric autoimmune medication landscape.

**Adverse event hub structure** was domain-specific:
- REPRODUCT: Pain (215 drugs), Rash (210), Fatigue (195)
- MENTALHEALTH: Pain, Rash, Fatigue (similar to REPRODUCT)
- GERIPHARM: Dizziness (289 drugs), Hypotension (274), Acute kidney injury (267) --- distinctly geriatric
- PCOS-ENDO: Acne (103 drugs), Pelvic pain (34) --- distinctly reproductive
- AYUR-PHARMA: Hepatotoxicity, Nephrotoxicity --- distinctly metabolic

---

## Discussion

### The Myth of Monolithic Female Predominance

Our analysis reveals that the commonly cited observation that "women experience more drug adverse events" is not uniformly true across all clinical domains. The 50-percentage-point sex bias spectrum --- from 21% female in PCOS/endometriosis contexts to 71% female for sexual dysfunction --- demonstrates that sex-differential drug safety is a heterogeneous phenomenon requiring domain-specific interpretation.

This heterogeneity has been obscured by aggregate analysis. When all 96,281 sex-differential signals are pooled, the overall female fraction is 53.8% --- a modest but significant excess. But this aggregate masks domain-specific patterns that span a range five times wider than the aggregate deviation from parity (50.4 pp spectrum vs. 3.8 pp aggregate excess). The aggregate female predominance is a composite of strongly female-dominant domains (elderly, sexual dysfunction) averaged with male-dominant domains (falls/fractures, PCOS/endometriosis), producing a misleadingly moderate "average" that describes no individual domain accurately.

This finding has important implications for precision pharmacovigilance. A sex-differential signal for a psychiatric drug should be interpreted differently than one for a geriatric drug or a reproductive endocrine drug, because the baseline sex bias differs substantially across these domains. Signal interpretation should be calibrated against domain-specific baselines rather than the global 53.8% average.

### Domain Extraction Improves Embedding Quality

The finding that three of five derived KGs outperformed the parent DistMult model provides quantitative evidence that domain-specific knowledge graph extraction improves signal-to-noise ratio for embedding-based drug safety prediction. The inverse relationship between KG size and MRR (rho = -0.90) suggests that focused, domain-specific KGs may be preferable to monolithic approaches for link prediction tasks.

This has practical implications for computational pharmacovigilance: rather than training a single model on the entire drug safety landscape, constructing domain-specific KGs for each therapeutic area may yield more accurate predictions. The REPRODUCT-KG (13,208 nodes, MRR 0.163) achieved 61% better performance than the parent (109,867 nodes, MRR 0.101) despite having only 12% of the entities. The trade-off is coverage --- the parent KG contains more entity types and relationships --- but for targeted prediction within a domain, smaller is better.

The edge-to-node ratio emerged as a secondary predictor of embedding quality. KGs with higher density (more edges per node) produced better embeddings, likely because denser local neighborhoods provide richer training signal for each entity. This suggests that domain extraction should prioritize densely connected subgraphs over comprehensive entity coverage.

### The PCOS/Endometriosis Paradox: A Methodological Cautionary Tale

The reversal of sex bias for PCOS/endometriosis-related adverse events (79% male) is the most counterintuitive finding in our analysis. Conditions traditionally associated with women --- acne, pelvic pain, hirsutism --- show male-biased pharmacovigilance signals. This "reproductive paradox" warrants careful interpretation.

The sex-stratified ROR measures relative disproportionality within each sex, not absolute incidence. Consider acne: if acne is a common baseline complaint for women (due to hormonal fluctuations), a drug causing acne in women generates a *smaller* disproportionality signal because acne is already relatively common in female FAERS reports. The same drug causing acne in men generates a *larger* disproportionality signal because acne is less common in male baseline reports. The result is a male-biased logR for acne despite potentially higher absolute incidence in women.

This mathematical artifact has implications beyond PCOS/endometriosis. Any adverse event with strong sex-linked baseline rates will show paradoxical ROR patterns: conditions common in women will generate male-biased signals, and vice versa. This is not a flaw in the methodology but a feature that should be understood when interpreting sex-differential safety signals. The ROR captures drug-attributable excess, not absolute incidence, and these are fundamentally different quantities.

The pelvic pain signal (logR = -1.859, 34 drugs, male-biased) is particularly illustrative. While pelvic pain is overwhelmingly more common in women in absolute terms, drug-induced pelvic pain in men represents a much larger departure from baseline male reporting patterns, generating a strong male-biased disproportionality signal.

### The Falls/Fractures Reversal: Clinical Implications

The male predominance of falls and fractures in pharmacovigilance signals (63.8% male, n = 872) contradicts the geriatric clinical assumption that falls are primarily a female problem. Several non-mutually-exclusive explanations exist:

1. **Baseline correction:** Women have higher baseline fall rates (non-drug-related), so drug-induced falls generate smaller relative disproportionality signals in women compared to men, similar to the PCOS paradox mechanism described above.

2. **Severity bias:** Falls in men may be more likely to result in serious injury requiring medical attention and FAERS reporting, while falls in women may be more common but less frequently reported as adverse drug reactions.

3. **Drug class effects:** Medications particularly associated with male falls (e.g., alpha-blockers for prostate conditions, certain cardiovascular drugs) may contribute disproportionately to the male signal.

4. **Bone density confounding:** Men are less commonly prescribed osteoporosis prevention, potentially making drug-induced falls more surprising and reportable in the male patient population.

Regardless of mechanism, this finding suggests that pharmacovigilance fall prevention programs should not be exclusively targeted at female patients. Male patients on fall-risk medications may benefit from equivalent screening and intervention.

### Sexual Dysfunction: An Underrecognized Female Burden

The 71.4% female bias in sexual dysfunction adverse events challenges the clinical narrative that drug-induced sexual dysfunction is primarily a male concern [10]. While erectile dysfunction is the most recognized and measured drug sexual side effect, our data show that the broader spectrum of sexual adverse events --- decreased libido, anorgasmia, sexual function disorder --- disproportionately generates female pharmacovigilance signals.

This has implications for prescribing practice, particularly in psychiatry. Current guidelines often emphasize switching antidepressants when men report sexual dysfunction, but may underrecognize the same issue in women. The 71.4% female bias suggests that systematic assessment of sexual function in women taking psychotropic medications is warranted and may be more important than the current male-focused approach suggests.

However, the small sample size (n = 63) limits the strength of this conclusion. The confidence interval (59.0%--83.9%) is wide, and a larger study specifically targeting sexual dysfunction signals would be needed to confirm this finding with greater precision.

### Bridging Traditional and Modern Medicine

The AYUR-PHARMA-KG represents, to our knowledge, the first systematic attempt to bridge Ayurvedic medicine with modern pharmacovigilance using knowledge graph embeddings. The successful prediction of Ashwagandha for PCOS treatment --- validated by traditional use and emerging clinical evidence [15] --- demonstrates that KG embeddings can capture meaningful herb-disease relationships from the structural properties of the graph alone.

The approach has important limitations: with only 5 herbs and sparse Ayurvedic-specific edges (37 herb-level, 18 dosha-related), the current AYUR-PHARMA-KG is more proof-of-concept than comprehensive resource. Expanding to the full IMPPAT 2.0 database (1,742 Indian medicinal plants) and incorporating NPASS natural product activity data would substantially strengthen this bridge. Nevertheless, the current results validate the approach and demonstrate that traditional medicine knowledge can be formally integrated into computational pharmacovigilance frameworks.

### Toward Domain-Calibrated Signal Interpretation

Our findings suggest a practical framework for domain-calibrated sex-differential signal interpretation:

1. **Identify the clinical domain** of a new sex-differential signal (psychiatric, geriatric, reproductive, etc.)
2. **Reference the domain-specific baseline** from Table 2 rather than the global 53.8% average
3. **Assess deviation from domain baseline** rather than from 50% parity
4. **Flag paradoxical signals** (e.g., male-biased signals in female-associated conditions) for careful interpretation
5. **Consider the baseline correction effect** for adverse events with strong sex-linked baseline rates

This framework would reduce false interpretations of sex-differential signals where the apparent sex bias reflects domain-specific baseline rates rather than genuine pharmacological sex differences.

### Integration with the Two-Axis Model

These domain-specific findings complement the two-axis model of sex-differential drug safety [17], which demonstrates that signal strength and report volume jointly predict female predominance. The domain-specific sex bias spectrum adds a third dimension: clinical context. The two-axis model predicts that strong, high-volume signals are overwhelmingly female (93--96%F), but our results show this prediction requires domain calibration. In the PCOS/endometriosis domain, even strong signals may show male predominance; in the elderly domain, even weak signals may show amplified female bias. The integration of domain-specific baselines with the two-axis strength-volume model would provide a three-dimensional predictive framework for sex-differential signal interpretation.

### Limitations

1. **Keyword-based domain classification** was used rather than formal ontology mapping (e.g., MeSH, MedDRA hierarchy). Some signals may be misclassified, and the categories may not be exhaustive.

2. **Small sample sizes** for some domains (sexual dysfunction: 63 signals, PCOS/endometriosis: 224 signals) limit statistical power and generalizability.

3. **DistMult model assumption** of symmetric scoring (s(h,r,t) = s(t,r,h)) may not optimally capture directional drug-disease relationships. ComplEx or RotatE models, which handle asymmetric relations, may reveal additional patterns.

4. **Ayurvedic predictions** require experimental validation and should be treated as hypothesis-generating, not confirmatory. The low herb count (n = 5) and sparse connectivity limit prediction reliability.

5. **FAERS reporting biases** --- including underreporting, the Weber effect (declining reports after initial marketing), stimulated reporting (media attention increasing reports for specific drugs), and differential access to healthcare by sex --- affect all domain-specific analyses equally but may interact with domain-specific reporting patterns.

6. **Temporal effects** were not examined. Sex bias patterns may change over time as prescribing practices, disease prevalence, and reporting behavior evolve.

7. **Drug overlap across KGs** means that the domain-specific findings are not independent. Many drugs appear in multiple derived KGs, and signals for these drugs contribute to multiple domain-specific analyses.

8. **The reproductive paradox interpretation** relies on the mathematical properties of the ROR but cannot rule out genuine biological sex differences in drug-induced acne, pelvic pain, or hirsutism susceptibility in men.

---

## Conclusion

The two primary findings of this analysis challenge conventional assumptions about sex-differential drug safety. First, sex bias varies by a 50-percentage-point spectrum across clinical domains, ranging from 21% female (PCOS/endometriosis) to 71% female (sexual dysfunction). The assumption of uniform female predominance is an artifact of aggregate analysis that obscures dramatic domain-specific heterogeneity, including complete reversals in reproductive endocrine and falls/fracture contexts.

Second, domain-specific knowledge graph extraction improves embedding quality: three of five derived KGs outperformed the parent model, with the best (REPRODUCT-KG) achieving 61% higher MRR despite containing only 12% of the parent entities. Smaller, focused KGs provide better signal-to-noise ratio for drug safety prediction than monolithic approaches.

Together, these findings support a transition from aggregate sex-differential pharmacovigilance to domain-calibrated approaches, where sex bias is interpreted against domain-specific baselines rather than a single global average. The five derived KGs and the sex bias spectrum reported here provide the quantitative foundation for this transition.

---

## Data Availability

SexDiffKG v5.2, all five derived KGs, and analysis code: https://github.com/jshaik369/SexDiffKG

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32.
2. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016;16:626-638.
3. Franconi F, Campesi I. Sex and gender influences on pharmacological response. Expert Rev Clin Pharmacol. 2014;7:469-485.
4. Shaik MJAA. SexDiffKG: A sex-differential drug safety knowledge graph integrating 14.5 million FAERS reports with molecular interaction networks. 2026. doi:10.1101/2026.03.02.709170.
5. Watson S, Caster O, Rochon PA, den Ruijter H. Reported adverse drug reactions in women and men: Aggregated evidence from globally collected individual case reports during half a century. EClinicalMedicine. 2019;17:100188.
6. Anderson GD. Sex and racial differences in pharmacological response: where is the evidence? Pharmacogenomics, pharmacokinetics, and pharmacodynamics. J Womens Health. 2005;14(4):292-302.
7. Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. Clin Pharmacokinet. 2009;48(3):143-157.
8. Regitz-Zagrosek V. Sex and gender differences in health. EMBO Rep. 2012;13(7):596-603.
9. Fairweather D, Frisancho-Kiss S, Rose NR. Sex differences in autoimmune disease from a pathological perspective. Am J Pathol. 2008;173(3):600-609.
10. Montejo AL, Montejo L, Baldwin DS. The impact of severe mental disorders and psychotropic medications on sexual health and its implications for clinical management. World Psychiatry. 2018;17(1):3-11.
11. Sakr Y, Elia C, Mascia L, et al. The influence of gender on the epidemiology of and outcome from severe sepsis. Crit Care. 2013;17(2):R50.
12. Marcantonio ER. Delirium in hospitalized older adults. N Engl J Med. 2017;377(15):1456-1466.
13. Hewlings SJ, Kalman DS. Curcumin: a review of its effects on human health. Foods. 2017;6(10):92.
14. Kunnumakkara AB, et al. Curcumin, the golden nutraceutical: multitargeting for multiple chronic diseases. Br J Pharmacol. 2017;174(11):1325-1348.
15. Goswami PK, Khale A, Ogale S. Natural remedies for polycystic ovarian syndrome (PCOS): A review. Int J Pharm Phytopharmacol Res. 2012;1(6):396-402.
16. Pase MP, Kean J, Sarris J, Neale C, Scholey AB, Stough C. The cognitive-enhancing effects of Bacopa monnieri: a systematic review of randomized, controlled human clinical trials. J Altern Complement Med. 2012;18(7):647-652.
17. Shaik MJAA. The two-axis model of sex-differential drug safety: signal strength and report volume jointly predict female predominance. 2026. [Manuscript in preparation]

---

## Figure Legends

**Figure 1.** Derived knowledge graph overview. (A-E) Node type composition for each of the five domain-specific KGs, shown as stacked bar charts with entity type proportions. Color coding consistent across panels: AdverseEvent (red), Drug (blue), Disease (green), Protein (orange), Gene (purple), ClinicalTrial (cyan), other types (gray shades). (F) Size comparison showing total nodes (blue bars) and total edges (red bars, log scale) across all five KGs plus the parent SexDiffKG v5.2.

**Figure 2.** The sex bias spectrum. Horizontal bar chart showing female fraction for nine clinical domains, ordered from most female-biased (sexual dysfunction, 71.4%F) to most male-biased (PCOS/endometriosis, 21.0%F). Vertical dashed line at 50% indicates sex parity; the general baseline (53.8%F) is shown as a second dashed line for reference. Red bars indicate female-dominant domains (>53.8%F); blue bars indicate male-dominant domains (<50%F); gray bars indicate neutral zone (50-53.8%F). Error bars show 95% binomial confidence intervals. The 50.4 pp spectrum width is annotated.

**Figure 3.** Embedding quality vs. KG size. (A) Bar chart of MRR for each derived KG compared to the parent DistMult v4.1 baseline (horizontal dashed line at MRR = 0.101). Three of five KGs (REPRODUCT, GERIPHARM, MENTALHEALTH) exceed the parent baseline, indicated by green bars; two KGs (AYUR-PHARMA, PCOS-ENDO) fall below, indicated by orange bars. (B) Scatter plot showing the inverse relationship between node count (x-axis, log scale) and MRR (y-axis) for all five derived KGs plus the parent model. Spearman rho = -0.90, p = 0.037. Regression line shown in blue with 95% confidence band.

**Figure 4.** Domain-specific sex bias patterns. Four-panel figure. (A) GERIPHARM-KG: Breakdown of elderly-relevant adverse events by sub-category, showing the falls/fractures reversal (36.2%F) against the overall elderly amplification (64.7%F). (B) MENTALHEALTH-KG: Comparison of general psychiatric AE sex bias (54.2%F) with sexual dysfunction AE sex bias (71.4%F). (C) PCOS-ENDO-KG: Individual PCOS/endometriosis adverse events (acne, pelvic pain, hirsutism) showing male predominance. (D) REPRODUCT-KG: Reproductive AE sex parity (50.0%F) against the general baseline (53.8%F).

**Figure 5.** Cross-KG comparison dashboard. Six-panel summary figure. (A) MRR comparison bar chart with parent baseline. (B) Sex bias spectrum horizontal bars. (C) KG size comparison (nodes vs edges). (D) Signal coverage per domain. (E) Domain-specific vs general sex bias scatter plot with identity line. (F) Summary statistics card with key findings.

**Figure 6.** Ayurvedic-modern medicine bridge. Network visualization showing the five-layer pathway: Herb to Compound to Protein target to Drug to Adverse event. Herb nodes (green hexagons) are positioned at left; compound intermediaries (purple circles) in second layer; shared protein targets (orange diamonds) in center; drugs (blue squares) in fourth layer; adverse events (red triangles) at right. Edge thickness proportional to connection count. Predicted herb-disease associations (Ashwagandha to PCOS, Licorice to Infertility) highlighted with dashed arrows. Dosha and Rasa nodes shown as peripheral annotations to demonstrate the Ayurvedic classification layer.
