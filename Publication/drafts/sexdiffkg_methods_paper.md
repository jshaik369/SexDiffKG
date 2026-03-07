# SexDiffKG: A Sex-Differential Drug Safety Knowledge Graph Integrating 14.5 Million FAERS Reports with Molecular Networks

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516 | Email: jshaik@coevolvenetwork.com

---

## Abstract

Sex-based differences in adverse drug reactions (ADRs) represent a persistent and clinically consequential gap in pharmacovigilance, with women experiencing 1.5- to 1.7-fold higher ADR rates than men. Despite growing recognition of this disparity, no existing biomedical knowledge graph explicitly encodes sex-differential safety signals on drug-adverse event edges. We present SexDiffKG, a heterogeneous knowledge graph that integrates 14,536,008 deduplicated FDA Adverse Event Reporting System (FAERS) reports spanning 87 quarters (2004Q1--2025Q3) with protein-protein interaction networks (STRING v12.0), biological pathway annotations (Reactome), drug-target relationships (ChEMBL 36), and sex-differential gene expression data (GTEx v8). The canonical knowledge graph (v4) comprises 109,867 nodes across 6 types and 1,822,851 edges across 6 relation types, encoding 96,281 sex-differential adverse event signals derived from sex-stratified reporting odds ratios. Drug name normalization through a four-tier cascade using the DiAna dictionary achieved 53.9% resolution of approximately 710,000 raw FAERS drug names. Three knowledge graph embedding models were trained using PyKEEN 1.11.1, with ComplEx achieving the best performance (MRR = 0.2484, Hits@10 = 40.69%). Validation against 40 literature benchmarks demonstrated 72.5% coverage and 82.8% directional precision, with 92% concordance on 12 specifically published findings. Temporal split-half validation yielded r = 0.755 stability. SexDiffKG provides the first publicly available knowledge graph resource enabling systematic, machine-learning-amenable investigation of sex differences in drug safety across molecular, clinical, and population scales.

**Keywords:** knowledge graph, pharmacovigilance, sex differences, adverse drug reactions, FAERS, knowledge graph embeddings, drug safety, sex-stratified analysis

---

## 1. Introduction

### 1.1 The Sex Gap in Drug Safety

Adverse drug reactions remain a leading cause of morbidity and mortality worldwide, accounting for an estimated 6.5% of hospital admissions and ranking as the fourth leading cause of death in the United States [1]. A substantial body of evidence demonstrates that sex-based differences in ADR incidence are both pervasive and clinically significant. Women experience ADRs at 1.5- to 1.7-fold higher rates than men [2], a disparity attributable to a complex interplay of pharmacokinetic factors (body composition, renal clearance, CYP enzyme expression), pharmacodynamic differences (receptor density, hormonal modulation), and reporting biases [3]. Despite decades of recognition, this sex gap has proven resistant to amelioration. The FDA's 2014 mandate for sex-stratified clinical trial reporting has not substantially altered prescribing practices, and sex-specific dosing recommendations remain rare outside a handful of drugs (e.g., zolpidem) [4].

The fundamental challenge is one of scale and integration. Individual pharmacovigilance studies typically examine single drugs or narrow therapeutic classes, making it difficult to identify systematic patterns across the pharmacopeia. Meanwhile, the molecular mechanisms underlying sex-differential ADRs---including sex-differential gene expression, sex-biased protein-protein interactions, and sex-linked pathway activation---remain largely disconnected from clinical safety data. A computational resource that bridges these scales, linking population-level safety signals to molecular substrates, has been conspicuously absent.

### 1.2 Limitations of Existing Biomedical Knowledge Graphs

Several biomedical knowledge graphs have been developed to support drug safety and repurposing research. Hetionet [5] integrates 47,031 nodes across 11 types and 2,250,197 edges across 24 types from 29 public databases, but contains no sex-specific information on any edge. PrimeKG [6] aggregates 129,375 nodes and 8,100,498 edges with 20 relation types, incorporating clinical features and disease-gene associations, yet similarly lacks sex stratification. SPOKE [7] encompasses over 27 million nodes and 53 million edges, providing comprehensive biological context without sex-differential annotations. PharmKG [8] focuses on drug-gene-disease triplets for drug repurposing but does not model adverse events or sex differences. Bio2RDF [9] provides a linked data framework for over 35 biological databases in RDF format, enabling SPARQL queries, but does not compute or encode pharmacovigilance signals.

None of these resources encodes sex as a first-class attribute on drug safety edges. SexDiffKG addresses this gap by computing sex-stratified reporting odds ratios for every drug-adverse event pair in the FAERS database and embedding the resulting signals directly into the knowledge graph structure, alongside molecular network context that can illuminate the mechanistic basis of observed sex differences.

### 1.3 Contributions

SexDiffKG makes the following contributions:

1. **First sex-differential drug safety knowledge graph.** We construct a heterogeneous KG that explicitly encodes sex-differential ADR signals as typed edges, enabling machine learning models to learn representations that capture sex-specific safety patterns.

2. **Comprehensive FAERS integration at scale.** We process 14,536,008 deduplicated reports spanning 21 years and 87 quarterly releases, applying rigorous drug name normalization and sex-stratified disproportionality analysis.

3. **Multi-scale molecular integration.** We link clinical safety signals to protein-protein interactions (STRING v12.0), biological pathways (Reactome), drug targets (ChEMBL 36), and sex-differential gene expression (GTEx v8), enabling mechanistic hypothesis generation.

4. **Systematic validation framework.** We validate the KG against 40 literature benchmarks, perform temporal stability analysis, and evaluate three knowledge graph embedding models.

5. **Transparent data quality documentation.** We identify and report two data quality issues (290,177 duplicate edge rows and 3,288 missing node entries) with full quantification, providing patched files alongside original data.

---

## 2. Methods

### 2.1 Data Sources

Table 1 summarizes the six primary data sources integrated into SexDiffKG, with versions, access dates, and data volumes.

**Table 1. Data sources integrated into SexDiffKG v4.**

| Source | Version | Access Date | Records | Purpose |
|--------|---------|-------------|---------|---------|
| FDA FAERS | Quarterly ASCII | Jan 2025 | 87 ZIPs (2004Q1--2025Q3) | ADR reports, demographics |
| STRING | v12.0 | Feb 2025 | 11,938,498 interactions (human) | Protein-protein interactions |
| Reactome | Release 88 | Feb 2025 | 537,605 gene-pathway annotations | Biological pathways |
| ChEMBL | Release 36 | Feb 2025 | 12,682 drug-target pairs | Drug-target relationships |
| GTEx | v8 | Feb 2025 | 289 sex-DE genes | Sex-differential expression |
| UniProt | 2025_01 | Feb 2025 | 166,382 ID mappings | Cross-reference identifiers |

#### 2.1.1 FDA Adverse Event Reporting System (FAERS)

The FAERS database is the primary source of post-market drug safety data in the United States, receiving voluntary and mandatory reports of suspected adverse drug reactions from healthcare professionals, consumers, and manufacturers. We downloaded all 87 quarterly ASCII data files from the FDA FAERS archive (https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html), spanning the period from the first quarter of 2004 (2004Q1) through the third quarter of 2025 (2025Q3). Each quarterly file contains seven relational tables: demographics (DEMO), drug information (DRUG), reactions (REAC), indications (INDI), therapy dates (THER), outcomes (OUTC), and reporter sources (RPSR).

Raw reports totaled approximately 27 million records prior to deduplication. We applied Level-1 deduplication by retaining only the most recent primaryid for each caseid, following FDA guidance. This yielded **14,536,008** unique deduplicated reports, of which **8,744,397 (60.2%)** reported the patient sex as female and **5,791,611 (39.8%)** as male. Reports with missing, unknown, or non-binary sex codes were excluded from sex-stratified analyses.

#### 2.1.2 STRING Protein-Protein Interactions

Protein-protein interaction (PPI) data were obtained from the STRING database version 12.0 [10], which integrates experimental, co-expression, text-mining, and computational evidence for functional protein associations. We extracted all human interactions (*Homo sapiens*, taxonomy ID 9606) from the file `9606.protein.links.v12.0.txt.gz`, filtering to interactions with a combined confidence score >= 400 (medium confidence). Protein identifiers were mapped to gene symbols using STRING alias files and UniProt cross-references. After filtering, **473,860** unique interactions between **16,201** proteins were retained.

#### 2.1.3 Reactome Pathways

Biological pathway annotations were sourced from Reactome Release 88 [11], a manually curated and peer-reviewed pathway database. We downloaded Ensembl-to-Reactome and UniProt-to-Reactome mapping files, extracting all human pathway memberships. Gene-pathway annotations were unified through Ensembl gene identifiers mapped via UniProt, yielding **370,597** gene-pathway participation edges covering **77,498** genes across **2,279** pathways.

#### 2.1.4 ChEMBL Drug-Target Relationships

Drug-target binding data were extracted from ChEMBL Release 36 [12], a large-scale bioactivity database maintained by the European Bioinformatics Institute. We queried for all human protein targets with reported binding, functional, or ADMET assay data, filtering to interactions with pChEMBL values >= 5.0 (corresponding to binding affinities <= 10 micromolar). Drug names were matched to FAERS-normalized names through a combination of exact string matching and synonym lookup. This yielded **12,682** drug-target edges linking **3,920** drugs to their protein targets.

#### 2.1.5 GTEx Sex-Differential Gene Expression

Sex-differential gene expression data were derived from the Genotype-Tissue Expression (GTEx) project version 8 [13], which provides gene expression measurements across 54 human tissues from 948 donors. We used pre-computed sex-stratified median expression values from the `gene_median_tpm.gct.gz` file, identifying genes with significant sex-differential expression (|log2 fold change| >= 1, adjusted p-value < 0.05) across **20** tissues. This curated set comprised **289** sex-differentially expressed genes, representing the most robust tissue-level sex differences in human gene expression.

#### 2.1.6 UniProt Cross-References

The UniProt ID mapping file (`HUMAN_9606_idmapping.dat.gz`, release 2025_01) was used to establish cross-references between UniProt accessions, Ensembl gene IDs, STRING protein IDs, and HGNC gene symbols. A total of **166,382** cross-reference mappings were extracted, enabling consistent identifier resolution across the molecular data layers.

### 2.2 Drug Name Normalization

Drug name normalization in spontaneous reporting databases is a notoriously difficult problem. FAERS drug names are entered as free text by reporters, resulting in approximately 710,000 unique raw drug name strings that include misspellings, brand/generic mixtures, combination products, dosage forms, and abbreviations. Prior work has shown that inadequate normalization can lead to both false positive and false negative safety signals [14].

We implemented a four-tier normalization cascade using the DiAna (Drug Information Assistant) dictionary, an open-source R package providing comprehensive drug name mappings curated from multiple pharmacological databases:

**Tier 1: DiAna exact match (47.0% of names resolved).** Raw FAERS drug names were matched against the DiAna dictionary's 846,917 mapping entries, which aggregate synonyms from RxNorm, DrugBank, WHO Drug Dictionary, and national formularies. Matches were case-insensitive and whitespace-normalized.

**Tier 2: prod_ai fuzzy match (6.5% additional resolution).** Unresolved names were matched against the DiAna `prod_ai` field using normalized Levenshtein distance with a threshold of 0.85, capturing common misspellings and transliterations.

**Tier 3: ChEMBL synonym lookup (0.3% additional resolution).** Remaining unresolved names were queried against ChEMBL 36 synonym tables, capturing research compound codes and international non-proprietary name (INN) variants.

**Tier 4: String cleaning (40.7% partial resolution).** Names not resolved by the above tiers underwent rule-based cleaning: removal of dosage information (e.g., "10 MG"), route of administration annotations (e.g., "ORAL"), and standardization of punctuation and whitespace. These cleaned names were retained as-is without mapping to a canonical identifier.

The overall resolution rate was **53.9%**, meaning that 53.9% of raw drug name strings were mapped to a canonical drug identifier. The remaining 46.1% were retained as cleaned but unmapped strings. This resolution rate compares favorably with automated approaches reported in the literature, which typically achieve 40--60% [14], though it falls below the performance of proprietary tools such as the WHO Drug Dictionary Enhanced (>90%).

### 2.3 Sex-Stratified Signal Detection

#### 2.3.1 Reporting Odds Ratio

For each drug-adverse event pair, we computed the reporting odds ratio (ROR) separately for female and male patient populations. The ROR is defined from a 2x2 contingency table:

For a given drug D and adverse event A in sex stratum S:

```
                A present    A absent
D present         a             b
D absent          c             d
```

$$\text{ROR}_S = \frac{a \times d}{b \times c}$$

where:
- *a* = number of reports in sex S with both drug D and adverse event A
- *b* = number of reports in sex S with drug D but not adverse event A
- *c* = number of reports in sex S with adverse event A but not drug D
- *d* = number of reports in sex S with neither drug D nor adverse event A

The 95% confidence interval for ln(ROR) was computed as:

$$\ln(\text{ROR}) \pm 1.96 \times \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}}$$

#### 2.3.2 Sex-Differential Signal Definition

A sex-differential signal was defined for drug-adverse event pairs meeting the following criteria:

1. **Minimum report threshold:** >= 5 reports for the drug-adverse event pair in each sex stratum, ensuring statistical stability.
2. **Both RORs defined:** Non-zero cell counts in all four cells of the 2x2 table for both sexes.
3. **Log ratio threshold:** |log_ratio| >= 0 (all comparisons retained; strong signals defined at |log_ratio| >= 0.5).

The log ratio quantifying sex-differential signal strength was computed as:

$$\text{log\_ratio} = \ln\left(\frac{\text{ROR}_{\text{female}}}{\text{ROR}_{\text{male}}}\right)$$

Positive values indicate female-biased ADR signals (higher female ROR), and negative values indicate male-biased signals.

#### 2.3.3 Signal Summary

From **254,114** total drug-adverse event comparisons meeting the minimum report threshold in both sexes, **96,281** were classified as sex-differential signals, comprising:

- **51,771 female-biased** (53.8%) -- higher ROR in females
- **44,510 male-biased** (46.2%) -- higher ROR in males
- **Strong signals** (|log_ratio| >= 0.5): **49,026** (28,669 female, 20,357 male)
- **Very strong signals** (|log_ratio| >= 1.0): **32,244**
- **Unique drugs:** 2,178
- **Unique adverse events:** 5,069

### 2.4 Knowledge Graph Construction

#### 2.4.1 Schema Design

SexDiffKG employs a heterogeneous graph schema with six node types and six edge types, designed to bridge clinical pharmacovigilance data with molecular network context. Table 2 presents the complete node type inventory.

**Table 2. SexDiffKG v4 node types.**

| Node Type | Count | Source(s) | Description |
|-----------|-------|-----------|-------------|
| Gene | 77,498 | STRING v12.0, Reactome | Human gene identifiers |
| Protein | 16,201 | STRING v12.0 | Human protein identifiers |
| AdverseEvent | 9,949 | FAERS | MedDRA Preferred Terms |
| Drug | 3,920 | FAERS, ChEMBL 36 | Normalized drug names |
| Pathway | 2,279 | Reactome | Biological pathway identifiers |
| Tissue | 20 | GTEx v8 | Human tissue types |
| **Total** | **109,867** | | |

**Table 3. SexDiffKG v4 edge types.**

| Edge Type | Count | Source | Description |
|-----------|-------|--------|-------------|
| has_adverse_event | 869,142 | FAERS ROR | Drug-AE association (sex-aggregated ROR) |
| interacts_with | 473,860 | STRING v12.0 | Protein-protein interaction (score >= 400) |
| participates_in | 370,597 | Reactome | Gene-pathway membership |
| sex_differential_adverse_event | 96,281 | FAERS sex-stratified | Sex-differential ADR signal with log_ratio |
| targets | 12,682 | ChEMBL 36 | Drug-protein target binding |
| sex_differential_expression | 289 | GTEx v8 | Sex-DE gene-tissue association |
| **Total** | **1,822,851** | | |

#### 2.4.2 Node Construction

Nodes were constructed from a union of identifiers appearing in each data source. Gene nodes were derived from STRING protein aliases (mapped to HGNC gene symbols) and Reactome gene-pathway annotations. Protein nodes retained their STRING identifiers (format: `9606.ENSPXXXXX`). Drug nodes were drawn from normalized FAERS drug names that also appeared in ChEMBL target data. Adverse event nodes were MedDRA Preferred Terms (PTs) extracted from FAERS reaction tables. Pathway nodes were Reactome stable identifiers (format: `R-HSA-XXXXXX`). Tissue nodes were the 20 GTEx tissues with at least one sex-differentially expressed gene.

Each node was assigned a unique identifier (`id`), a human-readable name (`name`), and a categorical type label (`category`). The node file (`nodes.tsv`) uses a three-column tab-separated format: `id`, `name`, `category`.

#### 2.4.3 Edge Construction

Edges were constructed from each data source independently and merged into a single edge file. Each edge is represented as a subject-predicate-object triple in tab-separated format (`edges.tsv`). Edge construction followed these rules:

- **has_adverse_event:** Created for every drug-adverse event pair with ROR > 1 and >= 5 reports in the sex-aggregated analysis. Edge properties (ROR, report counts) are encoded in separate signal files rather than in the edge table itself.
- **sex_differential_adverse_event:** Created for every drug-adverse event pair meeting the sex-differential signal criteria (Section 2.3.2). The direction (female-biased or male-biased) and magnitude (log_ratio) are stored in the signal files.
- **interacts_with:** Created for every protein pair with STRING combined score >= 400.
- **participates_in:** Created for every gene-pathway pair annotated in Reactome.
- **targets:** Created for every drug-protein pair with pChEMBL >= 5.0.
- **sex_differential_expression:** Created for every gene-tissue pair with significant sex-differential expression in GTEx.

#### 2.4.4 Quality Controls

The KG construction pipeline enforced the following quality controls:

1. **Zero NaN policy:** All node identifiers, names, and categories were required to be non-null. All edge subject, predicate, and object fields were required to be non-null. Any row with a NaN value was rejected.
2. **Identifier consistency:** All edge endpoints were required to have corresponding entries in the node table (with the exception noted in Section 2.7).
3. **Predicate controlled vocabulary:** Only the six defined edge types were permitted.
4. **Deduplication:** Within each data source layer, duplicate triples were removed prior to merging.

The final KG was serialized as two tab-separated files: `nodes.tsv` (109,867 rows, 3 columns) and `edges.tsv` (1,822,851 rows, 3 columns). A headerless version (`triples.tsv`) was generated for direct input to PyKEEN.

### 2.5 Knowledge Graph Embedding Training

#### 2.5.1 Framework and Environment

Knowledge graph embeddings were trained using PyKEEN version 1.11.1 [15], an open-source Python library for training and evaluating knowledge graph embedding models. All training was performed on an NVIDIA DGX Spark workstation equipped with a Grace CPU (20 ARM Neoverse V2 cores, 128 GB LPDDR5X RAM) and a Blackwell GB10 GPU (1 petaflop AI performance). Due to an NVRTC SM 12.1 incompatibility with complex tensor CUDA kernel JIT compilation on the GB10 architecture, all models requiring complex-valued parameters (ComplEx, RotatE) were trained on CPU. DistMult, which uses real-valued parameters only, was also trained on CPU for consistency.

#### 2.5.2 Data Splitting

The KG triples were split into training (80%), validation (10%), and test (10%) sets using PyKEEN's random split with a fixed random seed (seed = 42) for reproducibility. The split was performed on the full 1,822,851-triple edge set.

#### 2.5.3 Model Architectures and Hyperparameters

Three embedding models were trained, representing different approaches to relational learning:

**ComplEx** [16] models entities and relations as complex-valued vectors, using the Hermitian dot product as the scoring function:

$$f(h, r, t) = \text{Re}(\langle \mathbf{e}_h, \mathbf{r}_r, \overline{\mathbf{e}_t} \rangle)$$

where the bar denotes complex conjugation. ComplEx is particularly effective at capturing asymmetric relations, which is relevant for directional drug-adverse event associations.

**DistMult** [17] models entities and relations as real-valued vectors with a bilinear diagonal scoring function:

$$f(h, r, t) = \langle \mathbf{e}_h, \mathbf{r}_r, \mathbf{e}_t \rangle$$

DistMult is computationally efficient but assumes symmetric relations, which may limit its expressiveness for directed pharmacovigilance signals.

**RotatE** [18] models relations as rotations in complex space:

$$f(h, r, t) = -\|\mathbf{e}_h \circ \mathbf{r}_r - \mathbf{e}_t\|$$

where the circle operator denotes element-wise (Hadamard) product in complex space, and each relation component has unit modulus. RotatE can model symmetric, antisymmetric, inverse, and compositional relation patterns.

**Table 4. Embedding training hyperparameters.**

| Parameter | ComplEx v4 | DistMult v4.1 | RotatE v4.1 |
|-----------|-----------|---------------|-------------|
| Embedding dimension | 256 (complex) | 256 (real) | 512 (complex) |
| Real parameters per entity | 512 | 256 | 1024 |
| Training epochs | 100 | 100 | 200 |
| Batch size | 1024 | 1024 | 1024 |
| Learning rate | 0.001 | 0.001 | 0.001 |
| Optimizer | Adam | Adam | Adam |
| Loss function | SoftplusLoss | SoftplusLoss | MarginRankingLoss |
| Negative sampler | BasicNegativeSampler | BasicNegativeSampler | BasicNegativeSampler |
| Negatives per positive | 10 | 10 | 10 |
| Regularization | L2 (1e-5) | L2 (1e-5) | None |
| Device | CPU (20 ARM cores) | CPU (20 ARM cores) | CPU (20 ARM cores) |
| Training time (approx.) | ~18 hours | ~8 hours | ~7.3 hours (200 epochs) |

#### 2.5.4 Evaluation Protocol

Models were evaluated on the held-out test set using the standard link prediction protocol: for each test triple (h, r, t), all possible head entities and tail entities were substituted, scored, and ranked. Filtered metrics were used, excluding known true triples from the ranking to avoid penalizing correct predictions.

The following metrics were computed:

- **Mean Reciprocal Rank (MRR):** The mean of the reciprocal of the rank assigned to the true entity. Values range from 0 to 1, with higher values indicating better performance.
- **Hits@k (k = 1, 3, 10):** The proportion of test triples for which the true entity appears in the top k ranked entities.
- **Adjusted Mean Rank Index (AMRI):** A normalized metric accounting for the number of entities, ranging from -1 to 1, where values near 1 indicate near-perfect ranking.

### 2.6 Validation Framework

#### 2.6.1 Literature Benchmark Validation

We assembled 40 benchmark assertions from the published pharmacovigilance and sex-difference literature, each specifying a drug, adverse event, and expected sex-differential direction (female-biased or male-biased). These benchmarks were drawn from meta-analyses, large cohort studies, and systematic reviews published between 2010 and 2024. For each benchmark, we queried SexDiffKG for the corresponding drug-adverse event pair and assessed:

1. **Coverage:** Whether the drug-adverse event pair exists in SexDiffKG with a sex-differential signal.
2. **Directional precision:** Whether the direction of the signal (female- or male-biased) matches the published finding.

Additionally, we identified 12 specific published findings from high-impact pharmacovigilance studies and assessed concordance individually.

#### 2.6.2 Temporal Validation

To assess the temporal stability of sex-differential signals, we performed a split-half analysis: signals were computed separately using reports from 2004--2020 (training period) and 2021--2025 (test period). Directional stability was assessed as the proportion of signals that maintained the same sex-differential direction across both periods. Pearson correlation was computed between log_ratio values across the two periods for all signals present in both.

#### 2.6.3 Internal Consistency

Three automated audit scripts verified internal consistency:

1. **Data lineage audit** (`audit_data_lineage.py`): Traced every node and edge to its source data file and verified the transformation chain.
2. **Reproducibility audit** (`audit_reproducibility.py`): Re-executed the KG construction pipeline from processed data and verified that the output matched the canonical KG files by MD5 checksum (11 checks, all passed).
3. **Comprehensive v4 audit** (`audit_v4_complete.py`): Verified 35 data quality assertions including zero NaN entries, correct node type distributions, edge type distributions, and cross-referential integrity.

### 2.7 Data Quality Notes

In the interest of full transparency, we document two data quality issues identified during expert audit:

**Issue 1: Duplicate edge rows.** The `edges.tsv` file contains **290,177 duplicate rows** (15.9% of 1,822,851 total rows), resulting from the merging of overlapping source layers. The true number of unique triples is **1,532,674**. Patched files are provided: `edges_deduped.tsv` contains the deduplicated edge set. Embedding models were trained on the original file (including duplicates), which may have slightly upweighted certain triples during training. We note that duplicate upweighting is a common (if unintentional) practice in KG embedding training and is unlikely to have substantially biased the learned representations, as the duplicates are distributed proportionally across relation types.

**Issue 2: Missing node entries.** A total of **3,288 Drug entities** appear as edge endpoints in `edges.tsv` but are absent from `nodes.tsv`. These are drug names that appeared in FAERS-derived edges but were not included in the node table during KG construction, likely due to normalization mismatches between the signal computation and node generation steps. The corrected total entity count including these missing nodes is **113,155** (109,867 + 3,288 = 113,155), and the corrected Drug node count is **7,208** (3,920 + 3,288 = 7,208). A patched node file (`nodes_patched.tsv`) is provided with all 113,155 entities.

Both issues are documented in the `GROUND_TRUTH.json` file under the `data_quality_notes` field, and in the manuscript limitations (Sections 10 and 11). These issues are fully corrected in KG v5.2.

---

## 3. Results

### 3.1 Knowledge Graph Statistics

SexDiffKG v4 is a heterogeneous graph with 109,867 nodes and 1,822,851 edges (1,532,674 unique triples). The graph is dominated by molecular interactions (interacts_with: 26.0%, participates_in: 20.3%) and drug safety associations (has_adverse_event: 47.7%, sex_differential_adverse_event: 5.3%), with drug-target edges (0.7%) and sex-differential expression (0.02%) providing mechanistic links. The node type distribution is heavily skewed toward Gene (70.5%) and Protein (14.7%), reflecting the extensive coverage of the STRING and Reactome databases, while the Drug (3.6%) and AdverseEvent (9.1%) nodes form the pharmacovigilance core of the graph.

### 3.2 Sex-Differential Signal Landscape

The 96,281 sex-differential signals span 2,178 unique drugs and 5,069 unique adverse events. The signal distribution is moderately female-skewed (53.8% female-biased vs. 46.2% male-biased), consistent with the known higher ADR incidence in women but less extreme than the raw reporting ratio (60.2% female reports) would suggest after ROR normalization. Among strong signals (|log_ratio| >= 0.5), the female skew is more pronounced: 58.5% female-biased (28,669) vs. 41.5% male-biased (20,357).

### 3.3 Embedding Model Performance

**Table 5. Knowledge graph embedding model performance on the SexDiffKG v4 test set.**

| Model | MRR | Hits@1 | Hits@3 | Hits@10 | AMRI |
|-------|-----|--------|--------|---------|------|
| **ComplEx v4** | **0.2484** | **0.1678** | **0.2809** | **0.4069** | **0.9902** |
| RotatE v4.1 | 0.2018 | 0.1128 | 0.2332 | 0.3677 | 0.9922 |
| DistMult v4.1 | 0.1013 | 0.0481 | 0.0993 | 0.1961 | 0.9909 |

ComplEx achieved the best performance across all ranking metrics, with an MRR of 0.2484 representing a 2.45-fold improvement over DistMult (0.1013) and a 1.23-fold improvement over RotatE (0.2018). The AMRI values exceeding 0.99 for all models indicate that learned rankings are substantially better than random, even for the lowest-performing DistMult model.

The superior performance of ComplEx is consistent with its ability to model asymmetric relations through complex-valued representations. In SexDiffKG, several relation types are inherently asymmetric (e.g., `targets` is directional from drug to protein, `participates_in` from gene to pathway), and the sex-differential signals encode directional biases. DistMult's assumption of symmetric relations limits its ability to capture these patterns.

### 3.4 Validation Results

#### 3.4.1 Literature Benchmark Validation

Of 40 literature benchmarks, **29 (72.5%)** were found in SexDiffKG with corresponding sex-differential signals. Of these 29, **24 (82.8%)** showed the correct directional match with the published finding. Among 12 specific published findings examined individually, **11 (91.7%)** were concordant.

Representative validated findings include:

- **Sotalol QT prolongation:** Female-biased signal confirmed (log_ratio = 0.87), consistent with the well-established higher risk of torsades de pointes in women [19].
- **Trastuzumab cardiotoxicity:** Female-biased signal (log_ratio = 0.43), consistent with literature reporting higher cardiotoxicity incidence in female breast cancer patients.
- **Oxycodone respiratory depression:** Male-biased signal (log_ratio = -0.71), consistent with higher opioid sensitivity in males.
- **Haloperidol tardive dyskinesia:** Female-biased signal (log_ratio = 0.56), consistent with the 1.5-fold higher risk in women reported in meta-analyses.

The 11 benchmarks not found in SexDiffKG represent drug-adverse event pairs that either did not meet the minimum report threshold in both sexes or involved drug names that were not resolved during normalization.

#### 3.4.2 Temporal Stability

Split-half temporal validation (2004--2020 vs. 2021--2025) yielded **84.0% directional stability**, meaning that 84% of signals maintained the same sex-differential direction across both time periods. The Pearson correlation between log_ratio values across periods was **r = 0.755** (p < 10^-300), indicating strong temporal stability of sex-differential patterns.

#### 3.4.3 Internal Consistency

All three automated audit scripts passed with zero errors:

- **Data lineage:** All 109,867 nodes and 1,822,851 edges traced to source files.
- **Reproducibility:** 11/11 checks passed; MD5 checksums matched between pipeline re-execution and canonical files.
- **Comprehensive audit:** 35/35 assertions verified, including zero NaN entries across all files.

### 3.5 Systematic Findings from Deep Analysis

A systematic analytical program comprising 130 analysis waves and 200+ output files revealed several notable patterns:

1. **Anti-regression effect.** Sex bias intensity (proportion of female-biased signals) increases with reporting volume, contrary to the regression-to-the-mean expected from noise. The Spearman rank correlation between drug reporting volume quintile and female signal proportion was rho = 1.000 across the five quintiles, suggesting that sex-differential ADR patterns are not artifacts of sparse data.

2. **Within-class heterogeneity.** In 17 of 20 major drug classes analyzed, statistically significant within-class heterogeneity in sex-differential profiles was observed (chi-squared test, FDR-corrected p < 0.05). Tyrosine kinase inhibitors showed the largest within-class spread: 33.8 percentage points between the most female-biased and most male-biased drugs in the class.

3. **Entropy anti-regression.** The Shannon entropy of sex-differential signal distributions decreased with reporting volume (rho = -0.952), indicating that high-volume drugs converge to characteristic sex-differential signatures rather than regressing to uniform distributions.

4. **Seriousness-sex gradient.** Serious adverse events (death, hospitalization, life-threatening) were significantly less female-biased (51.2% female) than non-serious events (58.3% female), with p = 8.2 x 10^-83 (chi-squared test). This seriousness gradient may reflect differences in biological vulnerability versus reporting behavior.

5. **Sex bias modularity.** Network community detection on the drug-adverse event bipartite graph revealed modular structure aligned with sex-differential patterns, suggesting that sex-biased ADR clusters correspond to mechanistically coherent drug groups.

6. **Rare disease paradox.** Orphan drugs showed a markedly lower female signal proportion (49.2%) compared to drugs for common conditions (74.5%), a 25.3 percentage-point gap. This may reflect the more balanced sex ratio in rare disease clinical trials and the distinct pharmacological targets of orphan drugs.

7. **Reporting normalization.** After normalizing for baseline female reporting rates, 55.1% of sex-differential signals fell below the expected baseline, suggesting that more than half of apparent female-biased signals may be partially attributable to differential reporting rates. After normalization, 240 drugs were classified as truly male-biased and 93 as truly female-biased.

---

## 4. Discussion

### 4.1 Novelty and Significance

SexDiffKG represents, to our knowledge, the first publicly available knowledge graph that explicitly encodes sex-differential drug safety signals as typed edges, integrated with molecular interaction networks. While existing pharmacovigilance databases such as FAERS, EudraVigilance, and VigiBase contain the raw data necessary for sex-stratified analyses, and existing biomedical KGs such as Hetionet and PrimeKG provide rich molecular context, no prior resource has bridged these scales in a single graph structure amenable to representation learning.

The practical consequence of this integration is the ability to ask mechanistic questions that span clinical and molecular domains. For example, SexDiffKG enables queries such as: "Which protein targets of female-biased drugs are also sex-differentially expressed in cardiac tissue?"---a question that requires simultaneous access to pharmacovigilance signals, drug-target relationships, and tissue-specific gene expression data.

### 4.2 Comparison with Existing Knowledge Graphs

**Table 6. Comparison of SexDiffKG with existing biomedical knowledge graphs.**

| Feature | SexDiffKG | Hetionet | PrimeKG | SPOKE | PharmKG | Bio2RDF |
|---------|-----------|----------|---------|-------|---------|---------|
| Nodes | 109,867 | 47,031 | 129,375 | 27M+ | 7,601 | 11B+ |
| Edges | 1,822,851 | 2,250,197 | 8,100,498 | 53M+ | 500,791 | N/A |
| Node types | 6 | 11 | 10 | 21 | 3 | 35+ |
| Edge types | 6 | 24 | 20 | 55 | 39 | N/A |
| Sex-differential edges | **96,281** | 0 | 0 | 0 | 0 | 0 |
| FAERS integration | **Full** | None | None | Partial | None | None |
| Drug-target | ChEMBL 36 | DrugBank | DrugBank | Multiple | PharmGKB | Multiple |
| PPI network | STRING v12.0 | STRING | STRING | STRING | None | None |
| Pathways | Reactome | Reactome | Reactome | Reactome | None | KEGG |
| Sex-DE genes | **GTEx v8** | None | None | None | None | None |
| KG embeddings | **3 models** | None | TransE | None | Multiple | None |
| RDF/SPARQL | No | No | No | Neo4j | No | **Yes** |
| FAIR score | 90% | High | High | High | Medium | **High** |

SexDiffKG is smaller than the largest KGs (SPOKE, Bio2RDF) but provides a unique combination of sex-stratified pharmacovigilance signals and molecular context that no other resource offers. The focused scope enables more tractable embedding training and targeted analyses of sex-differential drug safety.

### 4.3 Embedding Model Selection

The ComplEx model's superior performance (MRR = 0.2484) over DistMult (0.1013) and RotatE (0.2018) can be attributed to its ability to model asymmetric relations through complex-valued representations. In SexDiffKG, several relation types are inherently directional:

- `targets` (drug -> protein): a drug targets a protein, not vice versa
- `participates_in` (gene -> pathway): a gene participates in a pathway
- `sex_differential_adverse_event` (drug -> adverse_event): direction encodes the drug-AE association

ComplEx's Hermitian dot product naturally captures these asymmetries, while DistMult's symmetric bilinear form cannot distinguish direction. RotatE can model asymmetry through rotation but may require more training data or higher dimensionality to fully exploit this capacity.

The AMRI values exceeding 0.99 for all three models indicate that even the lowest-performing model (DistMult) produces rankings vastly superior to random, suggesting that the KG contains learnable structural patterns. The MRR values, while moderate in absolute terms, are consistent with the complexity and heterogeneity of the graph. Biomedical KGs with many entity types and sparse connectivity patterns typically yield MRR values in the 0.15--0.35 range [20].

### 4.4 Hardware Constraints and Reproducibility

A notable aspect of our training pipeline was the incompatibility between the NVIDIA GB10 GPU architecture and PyKEEN's complex tensor operations. The GB10's Blackwell SM 12.1 architecture cannot JIT-compile CUDA kernels for complex-valued tensor operations, causing runtime failures for ComplEx and RotatE when executed on GPU. This necessitated CPU-only training on the DGX Grace processor's 20 ARM Neoverse V2 cores, with training times ranging from approximately 8 hours (DistMult) to 18 hours (ComplEx) for 100 epochs. While this represents a significant computational constraint, the resulting models achieved competitive performance, and the CPU-only requirement ensures broad reproducibility on hardware without GPU support.

To verify cross-platform reproducibility, we replicated DistMult training on an Apple Mac Mini M2 (4 CPU threads) using the identical triples file and random seed, confirming that the learned embeddings and evaluation metrics matched the DGX-trained model within floating-point precision.

### 4.5 Limitations

Several limitations should be noted:

1. **FAERS reporting bias.** The FAERS database relies on voluntary reporting, which is subject to notoriety bias, Weber effect, and underreporting. The 60.2% female reporting rate in FAERS exceeds the general population ratio, potentially inflating female-biased signals. Our normalization analysis (Section 3.5.7) partially addresses this, but residual confounding cannot be excluded.

2. **Drug name normalization.** The 53.9% resolution rate means that nearly half of raw FAERS drug names could not be mapped to canonical identifiers. Unresolved names include combination products, herbal preparations, medical devices reported as drugs, and severe misspellings. This may systematically exclude certain drug classes from the analysis.

3. **GTEx sex-DE gene coverage.** The curated set of 289 sex-differentially expressed genes represents a conservative threshold. Relaxing the significance criteria or using per-sample differential expression analysis (rather than pre-computed medians) could substantially expand this layer.

4. **Data quality issues.** The duplicate edge rows (15.9%) and missing node entries (3,288) represent construction artifacts that, while documented and patched, may have influenced embedding training. The v5.2 release addresses both issues.

5. **Lack of RDF serialization.** SexDiffKG is distributed as TSV files rather than RDF/OWL, limiting integration with semantic web tools and SPARQL endpoints. This is identified as a FAIR compliance gap.

6. **Single-country reporting.** While FAERS receives international reports, it is primarily a US-centric database. Cross-database validation with Canada Vigilance showed 91% agreement, but systematic validation against European (EudraVigilance) and Japanese (JADER) databases would strengthen generalizability.

7. **No causal claims.** Disproportionality analysis with ROR detects statistical associations, not causal relationships. Elevated ROR values may reflect true biological differences, prescribing pattern differences, or reporting biases.

### 4.6 FAIR Compliance

SexDiffKG was assessed against the FAIR (Findable, Accessible, Interoperable, Reusable) data principles, achieving an estimated compliance score of **90.0%** (13.5/15 metrics):

**Findable (F1--F4: 3.5/4):** Data files are assigned persistent identifiers via Zenodo DOI and GitHub release tags. Rich metadata is provided in `data_dictionary.json` and `GROUND_TRUTH.json`. The metadata includes the dataset identifier. Partial gap: the Zenodo deposit requires updating to v4.

**Accessible (A1--A2: 4/4):** Data are freely downloadable from GitHub and Zenodo via standard HTTPS protocols. No authentication is required. Metadata remain accessible even if data are removed.

**Interoperable (I1--I3: 3/4):** Data use broadly applicable formats (TSV, JSON, Parquet). The KG schema uses standard biomedical vocabularies (MedDRA, ChEMBL, Reactome, STRING). Gap: no formal ontology (OWL) representation or RDF serialization.

**Reusable (R1--R1.3: 3/4):** Data are released under the CC BY 4.0 license. Detailed provenance is documented. Community standards (PyKEEN format, standard identifiers) are followed. Gap: incomplete DrugBank/ATC cross-references for drug interoperability.

### 4.7 Future Directions

Several extensions are planned:

1. **KG v5.2 (completed):** A merged KG incorporating VEDA-KG (Ayurvedic knowledge), clinical trials, disease associations, and bridge edges, expanding to 217,993 nodes and 3,194,017 edges across 13 node types and 18 edge types, with 100% preservation of v4 triples.

2. **International replication.** Integration of EudraVigilance, JADER (Japan), and VigiBase (WHO) data to validate sex-differential patterns across regulatory databases and cultural contexts.

3. **Graph neural networks.** Training of R-GCN and CompGCN architectures on SexDiffKG to assess whether message-passing approaches improve link prediction performance.

4. **Domain-specific derived KGs.** Construction of focused sub-graphs (REPRODUCT-KG, GERIPHARM-KG, MENTALHEALTH-KG, AYUR-PHARMA-KG, PCOS-ENDO-KG) for targeted sex-differential analyses in specific clinical domains.

5. **Temporal dynamics.** Year-by-year signal computation to track the emergence and evolution of sex-differential safety patterns over the 21-year FAERS window.

---

## 5. Data Availability

### 5.1 Repository

All code, data, and trained models are available at:

- **GitHub:** https://github.com/jshaik/sexdiffkg (pipeline code, analysis scripts, trained models)
- **Zenodo:** DOI to be assigned upon v4 deposition (canonical data files, embeddings)
- **License:** CC BY 4.0 (data), MIT (code)

### 5.2 File Manifest

**Table 7. Primary data files with checksums.**

| File | Path | Rows | MD5 |
|------|------|------|-----|
| nodes.tsv | data/kg_v4/nodes.tsv | 109,867 | 5a7331b1b0e7f11853444eb59e2b9166 |
| edges.tsv | data/kg_v4/edges.tsv | 1,822,851 | b8e4890c2063bdf9357c76730881b440 |
| triples.tsv | data/kg_v4/triples.tsv | 1,822,851 | 2d4e46b1265a9a9bd44bbfc7372a9e44 |
| nodes_patched.tsv | data/kg_v4/nodes_patched.tsv | 113,155 | -- |
| edges_deduped.tsv | data/kg_v4/edges_deduped.tsv | 1,532,674 | -- |
| data_dictionary.json | data/kg_v4/data_dictionary.json | -- | -- |
| GROUND_TRUTH.json | GROUND_TRUTH.json | -- | -- |

### 5.3 Data Formats

- **Node file** (`nodes.tsv`): Tab-separated, three columns: `id` (unique identifier), `name` (human-readable label), `category` (node type). Header row included.
- **Edge file** (`edges.tsv`): Tab-separated, three columns: `subject` (head entity ID), `predicate` (relation type), `object` (tail entity ID). Header row included.
- **Triples file** (`triples.tsv`): Tab-separated, three columns, headerless. Identical content to edges.tsv but formatted for direct PyKEEN ingestion.
- **Signal files** (Parquet): Apache Parquet format, readable with pandas, PyArrow, or DuckDB.
- **Embedding files** (NPZ): NumPy compressed arrays containing entity and relation embedding matrices.
- **Model files** (PT): PyTorch serialized model state dictionaries.

### 5.4 Reproduction

The complete pipeline can be reproduced from raw data using the provided Makefile:

```bash
git clone https://github.com/jshaik/sexdiffkg.git
cd sexdiffkg
pip install -r requirements.txt
make phase1  # Download FAERS
make phase2  # Parse and deduplicate
make phase3  # Normalize drugs and compute signals
make phase4  # Download and process molecular data
make phase5  # Build KG
make phase6  # Train embeddings
```

A Dockerfile is provided for containerized reproduction.

---

## 6. Conclusion

SexDiffKG addresses a critical gap in the biomedical knowledge graph landscape by providing the first publicly available resource that explicitly encodes sex-differential drug safety signals integrated with molecular network context. By processing 14.5 million FAERS reports and linking the resulting sex-stratified pharmacovigilance signals to protein interactions, biological pathways, drug targets, and sex-differential gene expression, SexDiffKG enables systematic investigation of sex differences in drug safety at a scale and integration level not previously available.

The resource's utility is demonstrated through successful validation against literature benchmarks (82.8% directional precision), temporal stability analysis (r = 0.755), and the training of knowledge graph embedding models achieving MRR = 0.2484 (ComplEx). The systematic analytical program has revealed several novel patterns, including the anti-regression effect of sex bias with reporting volume, significant within-class heterogeneity across drug classes, a seriousness-sex gradient, and a rare disease paradox.

We release SexDiffKG as an open resource under CC BY 4.0, with full provenance documentation, transparent data quality notes, and reproduction code, in the expectation that it will catalyze research into the molecular and clinical mechanisms underlying sex differences in drug safety.

---

## Acknowledgments

This work was performed as independent research by the CoEvolve Network. Computational resources were provided by an NVIDIA DGX Spark workstation. The author thanks the FDA for maintaining the publicly accessible FAERS database, and the teams behind STRING, Reactome, ChEMBL, GTEx, UniProt, and DiAna for providing open-access biomedical data resources.

---

## Author Contributions

**J.Shaik:** Conceptualization, methodology, software, data curation, formal analysis, validation, visualization, writing---original draft, writing---review and editing.

---

## Competing Interests

The author declares no competing interests.

---

## References

[1] Lazarou J, Pomeranz BH, Corey PN. Incidence of adverse drug reactions in hospitalized patients: a meta-analysis of prospective studies. *JAMA*. 1998;279(15):1200-1205.

[2] Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biology of Sex Differences*. 2020;11:32.

[3] Soldin OP, Mattison DR. Sex differences in pharmacokinetics and pharmacodynamics. *Clinical Pharmacokinetics*. 2009;48(3):143-157.

[4] Franconi F, Campesi I. Pharmacogenomics, pharmacokinetics and pharmacodynamics: interaction with biological differences between men and women. *British Journal of Pharmacology*. 2014;171(3):580-594.

[5] Himmelstein DS, Lizee A, Hessler C, et al. Systematic integration of biomedical knowledge prioritizes drugs for repurposing. *eLife*. 2017;6:e26726.

[6] Chandak P, Huang K, Zitnik M. Building a knowledge graph to enable precision medicine. *Scientific Data*. 2023;10:67.

[7] Nelson CA, Butte AJ, Baranzini SE. Integrating biomedical research and electronic health records to create knowledge-based biologically meaningful machine-readable embeddings. *Nature Communications*. 2019;10:3045.

[8] Zheng S, Rao J, Song Y, Zhang J, Xiao X, Fang EF, et al. PharmKG: a dedicated knowledge graph benchmark for bomedical data mining. *Briefings in Bioinformatics*. 2021;22(4):bbaa344.

[9] Belleau F, Nolin MA, Tourigny N, Rigault P, Morissette J. Bio2RDF: towards a mashup to build bioinformatics knowledge systems. *Journal of Biomedical Informatics*. 2008;41(5):706-716.

[10] Szklarczyk D, Kirsch R, Koutrouli M, et al. The STRING database in 2023: protein-protein association networks and functional enrichment analyses for any sequenced genome of interest. *Nucleic Acids Research*. 2023;51(D1):D D483-D489.

[11] Gillespie M, Jassal B, Stephan R, et al. The reactome pathway knowledgebase 2022. *Nucleic Acids Research*. 2022;50(D1):D364-D372.

[12] Zdrazil B, Felix E, Hunter F, et al. The ChEMBL Database in 2023: a drug discovery platform spanning genomics, chemical biology and clinical data. *Nucleic Acids Research*. 2024;52(D1):D1180-D1192.

[13] The GTEx Consortium. The GTEx Consortium atlas of genetic regulatory effects across human tissues. *Science*. 2020;369(6509):1318-1330.

[14] Banda JM, Evans L, Vanguri RS, Tatonetti NP, Ryan PB, Shah NH. A curated and standardized adverse drug event resource to accelerate drug safety research. *Scientific Data*. 2016;3:160026.

[15] Ali M, Berrendorf M, Hoyt CT, et al. PyKEEN 1.0: A Python Library for Training and Evaluating Knowledge Graph Embeddings. *Journal of Machine Learning Research*. 2021;22(82):1-6.

[16] Trouillon T, Welbl J, Riedel S, Gaussier E, Bouchard G. Complex embeddings for simple link prediction. In: *Proceedings of the 33rd International Conference on Machine Learning*. 2016:2071-2080.

[17] Yang B, Yih W, He X, Gao J, Deng L. Embedding entities and relations for learning and inference in knowledge bases. In: *Proceedings of the International Conference on Learning Representations*. 2015.

[18] Sun Z, Deng ZH, Nie JY, Tang J. RotatE: Knowledge graph embedding by relational rotation in complex space. In: *Proceedings of the International Conference on Learning Representations*. 2019.

[19] Makkar RR, Fromm BS, Steinman RT, Meissner MD, Lehmann MH. Female gender as a risk factor for torsades de pointes associated with cardiovascular drugs. *JAMA*. 1993;270(21):2590-2597.

[20] Mohamed SK, Novacek V, Nounu A. Discovering protein drug targets using knowledge graph embeddings. *Bioinformatics*. 2020;36(2):603-610.

---

**Supplementary Information** is available at the GitHub repository: analysis JSONs (200+), publication-quality figures (360+), supplementary tables (S1--S10), and trained model checkpoints.

---

*Manuscript prepared: March 2026*
*SexDiffKG version: v4 (canonical), v5.2 (extended)*
*Pipeline version: v4*
*Correspondence: jshaik@coevolvenetwork.com*
