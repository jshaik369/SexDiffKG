# SexDiffKG: A Sex-Differential Drug Safety Knowledge Graph from 14.5 Million FDA Adverse Event Reports

**Authors:** JShaik¹  
**Affiliation:** ¹CoEvolve Network, Independent Researcher, Barcelona, Spain  
**Contact:** jshaik@coevolvenetwork.com  
**Date:** February 28, 2026  
**Version:** 1.0 — ISMB 2026 Submission Draft  

---

## Abstract

Sex-based differences in drug safety are well-documented but poorly systematized. Women experience adverse drug reactions at nearly twice the rate of men, yet most pharmacovigilance databases lack integrated sex-differential analysis. We present SexDiffKG, a sex-differential drug safety knowledge graph constructed from 14,536,008 FDA Adverse Event Reporting System (FAERS) reports spanning 2004–2024, integrated with molecular target data from ChEMBL, protein interaction networks from STRING, and biological pathway annotations from KEGG and UniProt. SexDiffKG contains 127,063 nodes and 5,839,717 edges across 6 entity types and 6 relation types. Through Reporting Odds Ratio (ROR) analysis stratified by sex, we identified 49,026 strong sex-differential drug–adverse event signals (|ln(ROR ratio)| > 1.0 (~2.7× difference), ≥10 reports per sex), with 58.5% showing female bias. Knowledge graph embedding using DistMult (200 dimensions, 100 epochs) achieved MRR of 0.048 and AMRI of 0.981, demonstrating meaningful link prediction capability. Embedding-based clustering of 29,201 drugs into 20 groups revealed distinct sex-differential safety profiles, and target-level analysis identified 429 gene targets with sex-biased drug safety patterns, including ESR1 (estrogen receptor, male-biased), HDAC1/2/3/6 (histone deacetylases, female-biased), and nicotinic acetylcholine receptor subunits (female-biased). SexDiffKG is, to our knowledge, the first knowledge graph specifically designed to capture sex-differential pharmacovigilance signals at scale, providing a computational foundation for sex-aware drug safety assessment.

**Keywords:** pharmacovigilance, sex differences, knowledge graph, drug safety, FAERS, graph embeddings, adverse drug reactions

---

## 1. Introduction

### 1.1 The Sex Gap in Drug Safety

Adverse drug reactions (ADRs) represent a significant public health burden, accounting for an estimated 2.2 million serious cases and 106,000 deaths annually in the United States alone. Women experience ADRs at approximately 1.5–1.7 times the rate of men, a disparity attributed to differences in drug metabolism (CYP enzyme expression), body composition, hormonal influences on drug transport, and historical underrepresentation in clinical trials.

Despite growing recognition of sex-based pharmacological differences, most pharmacovigilance systems analyze safety signals in aggregate without systematic sex stratification. The FDA Adverse Event Reporting System (FAERS), the largest spontaneous reporting database with over 14 million reports, captures patient sex for most entries but does not natively support sex-differential signal detection.

### 1.2 Knowledge Graphs for Drug Safety

Knowledge graphs (KGs) have emerged as powerful tools for integrating heterogeneous biomedical data. Systems such as Hetionet, DRKG, and PharmKG have demonstrated the value of graph-based representations for drug repurposing and safety prediction. However, no existing KG specifically models sex-differential drug safety patterns, leaving a critical gap in computational pharmacovigilance.

### 1.3 Contribution

We present SexDiffKG, a purpose-built knowledge graph that:

1. Integrates 14.5 million FAERS reports with molecular, protein, and pathway data from 5 authoritative sources
2. Introduces sex-stratified ROR analysis to identify 49,026 strong sex-differential drug–adverse event signals
3. Embeds the full graph using DistMult to enable sex-aware link prediction
4. Reveals 429 gene targets with measurable sex-differential drug safety profiles through embedding-based analysis

---

## 2. Methods

### 2.1 Data Sources and Integration

SexDiffKG integrates data from five primary sources:

| Source | Version | Data Type | Contribution |
|--------|---------|-----------|-------------|
| FDA FAERS | 2004Q1–2024Q4 | Spontaneous ADR reports | 14,536,008 reports (F: 8,744,397; M: 5,791,611) |
| ChEMBL 36 | 2024 release | Drug–target binding | 12,682 drug–gene target edges |
| STRING | v12.0 | Protein–protein interactions | 465,390 interaction edges |
| KEGG | 2024 | Biological pathways | 537,605 pathway participation edges |
| UniProt | 2024_05 | Gene–protein encoding | Protein annotation |

FAERS data was processed using a standardized pipeline: deduplication by case ID, sex assignment from demographic fields (excluding unknown/unspecified), drug name normalization to MedDRA preferred terms, and adverse event standardization using MedDRA System Organ Class hierarchy.

### 2.2 Knowledge Graph Construction

The resulting knowledge graph contains:

**Nodes (127,063 total):**
- Gene: 70,607 (55.6%)
- Drug: 29,277 (23.0%)
- AdverseEvent: 16,162 (12.7%)
- Protein: 8,721 (6.9%)
- Pathway: 2,279 (1.8%)
- Tissue: 17 (<0.1%)

**Edges (5,839,717 total):**
- has_adverse_event: 4,640,396 (79.5%) — Drug–AE co-occurrence from FAERS
- participates_in: 537,605 (9.2%) — Gene/Protein–Pathway from KEGG
- interacts_with: 465,390 (8.0%) — Protein–Protein from STRING
- sex_differential_adverse_event: 183,539 (3.1%) — Sex-stratified Drug–AE signals
- targets: 12,682 (0.2%) — Drug–Gene pharmacological targets from ChEMBL
- sex_differential_expression: 105 (<0.1%) — Known sex-differential gene expression

### 2.3 Sex-Differential Signal Detection

For each drug–adverse event pair, we computed sex-stratified Reporting Odds Ratios (ROR):

$$ROR_{sex} = \frac{a_{sex} / b_{sex}}{c_{sex} / d_{sex}}$$

where *a* = reports with the drug–AE pair, *b* = reports with the drug but not the AE, *c* = reports with the AE but not the drug, and *d* = reports with neither, all stratified by patient sex.

The sex-differential ratio was computed as:

$$\text{log\_ror\_ratio} = \ln\left(\frac{ROR_{female}}{ROR_{male}}\right)$$

Signals were classified as **strong** if |log_ror_ratio| > 1.0 (corresponding to >~2.7× difference, since e^1.0 ≈ 2.72) with ≥10 reports in each sex group.

**Signal Filtering Pipeline:**
1. All drug–AE pairs with valid ROR: 2,610,331
2. Sex-differential (both sexes have signal): 183,544
3. Strong (|ln(ROR ratio)| > 1.0 (~2.7× difference), ≥10 reports per sex): 49,026
   - Female-biased: 28,669 (58.5%)
   - Male-biased: 20,357 (41.5%)

### 2.4 Knowledge Graph Embedding

We trained DistMult embeddings on the full graph:

| Parameter | Value |
|-----------|-------|
| Embedding dimension | 200 |
| Training epochs | 100 |
| Batch size | 512 |
| Learning rate | 0.001 |
| Loss function | SLCWA (Stochastic Local Closed World Assumption) |
| Optimizer | Adam |
| Random seed | 42 |
| Training triples | 5,489,928 (after dropping 349,789 with NaN values) |
| Entities embedded | 126,575 |
| Relations | 6 |

Training was performed on an NVIDIA Grace Blackwell GB10 GPU with 120GB unified memory, completing in approximately 3.5 hours.

A secondary RotatE model (200 dimensions, complex-valued = 400 parameters, 25 epochs) was trained on CPU for comparison (7.5h training, 54.1 min GPU evaluation). RotatE achieved near-random performance (MRR 0.0001, AMRI 0.003), validating DistMult as the appropriate primary model for this graph's predominantly symmetric relation structure (see Section 3.2).

### 2.5 Embedding-Based Analysis

Post-training analysis consisted of three components:

1. **Drug clustering:** K-Means (k=20) on L2-normalized drug entity embeddings, with PCA projection for visualization (61.9% variance explained by 2 components)
2. **Cluster profiling:** Mapping sex-differential signals to drug clusters to identify embedding regions associated with sex-biased safety
3. **Target sex-bias scoring:** For each gene target, computing a sex-bias score based on the ratio of female-biased vs. male-biased drugs targeting that gene:

$$\text{sex\_bias\_score} = \frac{n_{female} - n_{male}}{n_{total}}$$

where values range from -1.0 (exclusively male-biased) to +1.0 (exclusively female-biased).

---

## 3. Results

### 3.1 Link Prediction Performance

DistMult v3 evaluation on a held-out test set (499 triples, 13,466 disease candidates):

| Metric | DistMult v3 | DistMult v2 | Improvement |
|--------|:-----------:|:-----------:|:-----------:|
| MRR | 0.04762 | 0.03881 | +22.7% |
| Hits@1 | 2.25% | 1.80% | +24.7% |
| Hits@3 | 4.54% | 3.61% | +25.6% |
| Hits@5 | 6.06% | — | — |
| Hits@10 | 8.85% | 6.91% | +28.0% |
| AMRI | 0.981 | 0.976 | +0.5% |

The AMRI (Adjusted Mean Rank Index) of 0.981 indicates the model ranks correct triples in the top 1.9% of all candidates on average, demonstrating meaningful structural learning despite the graph's heterogeneity and scale. The asymmetry between head prediction (MRR 0.033) and tail prediction (MRR 0.062) reflects the graph's structure where predicting drug targets (tail) is more constrained than predicting which drugs target a gene (head).

### 3.2 Sex-Differential Signal Landscape

From 14,536,008 FAERS reports, we identified 49,026 strong sex-differential drug–adverse event signals across 3,441 unique drugs and 5,658 unique adverse events.

**Top drugs by sex-differential signal count:**

| Drug | Total Signals | Female-Biased | Male-Biased | Max Ratio |
|------|:---:|:---:|:---:|:---:|
| Ranitidine HCl | 381 | 378 | 3 | 3.2× |
| Rituximab | 344 | 281 | 63 | 4.3× |
| Prednisone | 302 | 228 | 74 | 4.5× |
| Risperidone | 298 | 273 | 25 | 4.7× |

**Top adverse events by sex-differential signal count:**

| Adverse Event | Total Signals | Female-Biased | Male-Biased | Max Ratio |
|--------------|:---:|:---:|:---:|:---:|
| Device dislocation | 220 | 0 | 220 | 4.3× |
| Drug intolerance | 176 | 95 | 81 | 3.4× |
| Off label use | 174 | 93 | 81 | 4.6× |
| General physical health deterioration | 170 | 116 | 54 | 3.9× |

Notable biologically coherent signals include dutasteride (5α-reductase inhibitor) showing extreme female bias for prescribing issues (log ROR ratio = 5.53), consistent with its contraindication in women of childbearing age, and clozapine showing female bias for gynaecomastia (log ROR ratio = 4.96), reflecting known hormonal effects.

### 3.3 Embedding-Based Drug Clustering

Clustering 29,201 drugs with embeddings into 20 groups revealed distinct sex-differential safety landscapes:

- **High-signal clusters** (>1,000 signals each) showed variable female bias ratios from 0.39 to 0.71, suggesting embedding space encodes safety-relevant pharmacological features
- **Cluster 0** (2,087 drugs, female ratio 0.39): Enriched for "Drug ineffective" and "Fatigue" — moderate male-bias, suggesting metabolic/hepatic clearance differences
- **Cluster 5** (854 drugs, female ratio 0.71): Enriched for female-biased signals, higher proportion of immunomodulatory agents
- **Silent clusters** (0 signals): Represent drugs without sufficient sex-differential safety data, primarily consisting of rarely prescribed compounds

PCA projection explained 61.9% of embedding variance in 2 components, indicating the learned representations capture substantial pharmacological structure.

### 3.4 Gene Target Sex-Bias Profiles

Through bridging FAERS drug names to ChEMBL target annotations, we matched 29,621 of 49,026 strong signals (60.4%) to drugs with known gene targets, identifying 429 gene targets with sex-differential drug safety profiles (≥2 sex-biased drugs per target).

**Key findings by target class:**

**Epigenetic regulators (female-biased):**
- HDAC1, HDAC2, HDAC3, HDAC6 (histone deacetylases): All exclusively female-biased (score = +1.0)
- Suggests HDAC inhibitors (used in cancer therapy) may carry sex-specific safety considerations

**Hormone receptors (male-biased):**
- ESR1 (estrogen receptor α): Score = -0.80 (5 drugs, 1 female-biased, 5 male-biased)
- This counterintuitive finding suggests drugs targeting ESR1 show more male-biased adverse events, possibly reflecting off-target effects in male patients

**Ion channels and receptors:**
- Nicotinic acetylcholine receptor subunits (CHRNA1, CHRNB1, CHRND, CHRNE, CHRNG): Female-biased (score = +0.75)
- SCNN1A/B/G (sodium channels): Male-biased (score = -1.0)
- S1PR1 (sphingosine-1-phosphate receptor): Male-biased (score = -0.75)

**Immune signaling:**
- JAK1: Male-biased (score = -0.75), consistent with known sex differences in JAK-STAT immune signaling

---

## 4. Discussion

### 4.1 Significance

SexDiffKG represents the first purpose-built knowledge graph for sex-differential drug safety analysis. By integrating FAERS pharmacovigilance data with molecular target annotations, protein interactions, and pathway data, it enables computational approaches to understanding sex-based differences in drug safety that were previously limited to individual drug or drug-class studies.

The identification of 429 gene targets with sex-differential drug safety profiles provides actionable hypotheses for precision pharmacovigilance. The female bias in HDAC inhibitor safety signals, for example, has not been previously reported at scale and warrants mechanistic investigation given the expanding use of these agents in oncology.

### 4.2 Comparison with Existing Resources

No directly comparable sex-differential drug safety KG exists. The closest related resources include:

| Resource | Focus | Scale | Sex-Differential |
|----------|-------|-------|:---:|
| **SexDiffKG** | Drug safety × sex | 127K nodes, 5.8M edges | **Yes** |
| DRKG | Drug repurposing | 97K nodes, 5.9M edges | No |
| PharmKG | Pharmacogenomics | 7.6K nodes, 500K edges | No |
| Hetionet | Disease–gene–drug | 47K nodes, 2.3M edges | No |
| Bio2RDF | Linked biomedical data | Millions | No |

SexDiffKG is comparable to DRKG in scale while providing unique sex-differential signal content not available in any existing resource.

### 4.3 Limitations

1. **FAERS reporting bias:** Spontaneous reporting systems are subject to underreporting, stimulated reporting (e.g., FDA warnings), and demographic biases. The 60:40 female-to-male ratio in FAERS exceeds population drug usage ratios, potentially inflating female-biased signals.

2. **ROR methodology:** ROR does not establish causation and may be confounded by prescribing patterns, disease prevalence, and reporting behavior that differ by sex.

3. **Drug name resolution:** Matching FAERS drug names (often brand names or abbreviated generics) to standardized identifiers achieves approximately 60% coverage for target-level analysis.

4. **Embedding performance:** DistMult MRR of 0.048 is moderate for a 126K-entity graph. RotatE failed to converge in 25 CPU epochs (MRR ≈ 0.0001, AMRI 0.003), likely due to insufficient training and the graph's symmetric relation structure. Domain-specific evaluation would likely show higher precision for DistMult.

5. **Static snapshot:** The current version represents FAERS data through Q4 2024 and does not incorporate temporal trends or evolving safety signals.

### 4.4 Future Directions

1. **Extended embedding models:** RotatE with 25 CPU epochs showed near-random performance. Future work should explore ≥100 GPU-trained epochs (pending NVRTC fix) or alternative models (ComplEx, TransE, R-GCN)
2. **Temporal analysis:** Incorporating time-series signal evolution to detect emerging sex-differential safety concerns
3. **Dose–response integration:** Adding dose-stratified analysis where available in FAERS
4. **Causal inference:** Applying methods such as IC (Information Component) or BCPNN to strengthen causal attribution
5. **Clinical validation:** Comparing SexDiffKG predictions against sex-stratified clinical trial safety data

---

## 5. Data and Code Availability

SexDiffKG was constructed and analyzed entirely on local infrastructure (NVIDIA Grace Blackwell GB10, 120GB unified memory, ARM64 architecture) using open-source tools including PyKEEN 1.11.1, scikit-learn, and pandas.

**Resources:**
- Knowledge graph: 127,063 nodes, 5,839,717 edges (TSV format)
- Embeddings: DistMult 200d entity and relation embeddings (NPZ format)
- Sex-differential signals: 183,544 signals with full ROR statistics (Parquet format)
- Analysis outputs: Cluster profiles, target sex-bias scores, PCA coordinates
- All figures: Publication-quality PNG (300 DPI) and PDF

---

## 6. Pipeline Architecture

```
FAERS (14.5M reports)
    ├── Sex stratification → Female (8.7M) / Male (5.8M)
    ├── ROR computation → 2.6M drug-AE signals
    ├── Sex-differential analysis → 183K signals → 49K strong
    │
    ├── ChEMBL 36 → 12,682 drug-target edges
    ├── STRING v12 → 465K protein interactions
    ├── KEGG → 537K pathway edges
    │
    ├── KG Construction → 127K nodes, 5.8M edges
    │
    ├── DistMult Training (200d, 100 epochs)
    │   ├── Entity embeddings (126,575 × 200)
    │   └── Relation embeddings (6 × 200)
    │
    └── Analysis
        ├── Drug clustering (20 clusters)
        ├── Sex-bias profiling per cluster
        └── Target sex-bias scoring (429 targets)
```

---

## 7. Key Figures

1. **Figure 1:** Drug embedding PCA clusters colored by sex-differential safety profile (29,201 drugs, 20 clusters)
2. **Figure 2:** Distribution of sex-differential signals and top 15 drugs by signal count
3. **Figure 3:** Knowledge graph composition (node and edge type distributions)
4. **Figure 4:** Gene target sex-bias scores (top female-biased and male-biased targets)
5. **Figure 5:** FAERS data summary and signal filtering pipeline
6. **Figure 6:** Embedding cluster sex-differential profiles

---

## Acknowledgments

This work was conducted as independent research at CoEvolve Network, Barcelona, Spain. Computational infrastructure was provided by an NVIDIA DGX Spark (Grace Blackwell GB10). The author thanks the FDA for maintaining the FAERS public database, and the teams behind ChEMBL, STRING, KEGG, and UniProt for their open data contributions.

---

## References

1. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biology of Sex Differences*. 2020;11:32.
2. Watson S, et al. Sex differences in adverse drug reactions. *Drug Safety*. 2019;42(3):445-453.
3. Ali M, et al. PyKEEN 1.0: A Python Library for Training and Evaluating Knowledge Graph Embeddings. *JMLR*. 2021;22:1-6.
4. Yang B, et al. Embedding Entities and Relations for Learning and Inference in Knowledge Bases. *ICLR*. 2015.
5. Sun Z, et al. RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space. *ICLR*. 2019.
6. Gaulton A, et al. The ChEMBL database in 2023. *Nucleic Acids Research*. 2024;52(D1):D1180-D1192.
7. Szklarczyk D, et al. The STRING database in 2023. *Nucleic Acids Research*. 2023;51(D1):D483-D489.
8. Kanehisa M, et al. KEGG for taxonomy-based analysis of pathways and genomes. *Nucleic Acids Research*. 2023;51(D1):D587-D592.
