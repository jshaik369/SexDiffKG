# Knowledge Graph Embeddings for Sex-Differential Drug Safety: Scaling Behavior, Model Selection, and Domain-Specific Signal-to-Noise Enhancement

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Knowledge graph embedding (KGE) models learn continuous vector representations of entities and relations, enabling link prediction and similarity computation in biomedical knowledge graphs. Despite growing adoption in drug safety research, systematic comparisons of KGE model performance on pharmacovigilance-oriented knowledge graphs are lacking, and the impact of graph scale on embedding quality is poorly understood.

**Methods.** We trained three KGE models---ComplEx, DistMult, and RotatE---on SexDiffKG, a knowledge graph integrating 14.5 million FDA Adverse Event Reporting System (FAERS) reports with molecular interaction data from ChEMBL 36, STRING v12.0, Reactome, and GTEx v8. We evaluated models across three graph versions: v4 (109,867 nodes, 1,822,851 edges, 6 relation types), v5.2 merged (217,993 nodes, 3,194,017 edges, 18 relation types integrating Ayurvedic and clinical trial data), and five domain-specific subgraphs extracted from the merged KG. Performance was assessed by Mean Reciprocal Rank (MRR), Hits@k, and Adjusted Mean Rank Index (AMRI) using filtered rank-based evaluation.

**Results.** On the original SexDiffKG v4, ComplEx achieved the highest MRR (0.2484), followed by RotatE (0.2018) and DistMult (0.1013). Scaling to the merged v5.2 graph (2x entities, 3x relations) produced significant MRR degradation: ComplEx dropped 34% (0.2484 to 0.1629), DistMult dropped 46% (0.1013 to 0.0548). However, domain-specific subgraph extraction recovered and exceeded original performance: REPRODUCT-KG achieved MRR 0.1629 (60% above parent DistMult), GERIPHARM-KG 0.1438 (+42%), and MENTALHEALTH-KG 0.1277 (+26%). The top three domain-specific KGs all outperformed the parent DistMult v4.1 (MRR 0.1013), demonstrating that domain extraction improves signal-to-noise ratio. Embedding-based drug similarity analysis revealed that structurally similar drugs (cosine similarity >0.93) can exhibit sex-bias differences exceeding 30 percentage points, indicating that sex-differential safety requires explicit modeling beyond standard structural features.

**Conclusions.** We provide the first systematic evaluation of KGE models on a sex-differential pharmacovigilance knowledge graph across scales. ComplEx consistently outperforms DistMult and RotatE. Graph scaling degrades performance predictably, but domain-specific extraction provides a principled strategy for recovering embedding quality. These findings have practical implications for knowledge graph design in drug safety applications.

---

## Introduction

### Knowledge Graph Embeddings: Foundations and Evolution

Knowledge graph embedding (KGE) models have emerged as a foundational tool for representation learning over structured relational data, with far-reaching applications in biomedical knowledge discovery including drug repurposing [1], adverse drug reaction prediction [2], target identification [3], and clinical trial design [4]. At their core, KGE models learn continuous, low-dimensional vector representations of entities (drugs, genes, diseases) and relations (targets, causes, treats), enabling both link prediction (inferring missing edges) and similarity computation (finding related entities) without explicit feature engineering. The central insight underlying all KGE methods is that the geometric structure of the embedding space can be designed to reflect the relational semantics of the knowledge graph.

The modern KGE literature traces its origins to translational models. **TransE** [5], introduced by Bordes et al. in 2013, proposed modeling each relation as a translation vector in embedding space: for a true triple (h, r, t), the model enforces that **h** + **r** is approximately equal to **t**. TransE is elegant in its simplicity and computationally efficient, but it fundamentally cannot model symmetric relations (if **h** + **r** = **t**, then **t** + **r** cannot equal **h** unless **r** = 0) or one-to-many/many-to-one relations (multiple entities mapped to the same point). These limitations motivated a series of increasingly expressive models.

**DistMult** [6], proposed by Yang et al. in 2015, replaced the translational scoring function with a bilinear diagonal model. Each relation is represented as a diagonal matrix (equivalently, a vector of per-dimension scaling factors), and the score for a triple (h, r, t) is the trilinear dot product: sum of h_i * r_i * t_i across all dimensions. DistMult is computationally efficient and often provides surprisingly competitive baselines despite its theoretical limitation: the scoring function is inherently symmetric in h and t (swapping h and t produces the same score), meaning DistMult cannot distinguish the direction of asymmetric relations. In practice, DistMult compensates for this limitation through its training procedure and regularization, but the constraint remains a fundamental ceiling on its expressiveness for graphs with predominantly asymmetric relations.

**ComplEx** [7], introduced by Trouillon et al. in 2016, extended DistMult to complex-valued vector spaces. By representing entities and relations as vectors of complex numbers, ComplEx achieves asymmetric scoring through the Hermitian dot product: the score for (h, r, t) involves the conjugate of the tail embedding, breaking the h/t symmetry that limits DistMult. ComplEx can theoretically model symmetric, antisymmetric, and inverse relation patterns simultaneously---a crucial advantage for heterogeneous biomedical knowledge graphs where different relations exhibit different symmetry properties. Formally, for a triple (h, r, t), ComplEx computes: Re(sum of h_i * r_i * conj(t_i)), where Re denotes the real part and conj the complex conjugate. This Hermitian product naturally encodes asymmetry: score(h, r, t) does not equal score(t, r, h) in general, unlike DistMult's real-valued dot product.

**RotatE** [8], proposed by Sun et al. in 2019, models each relation as an element-wise rotation in complex space. For each dimension, the relation embedding has unit modulus (|r_i| = 1), and the scoring function measures the distance between h_i * r_i and t_i. RotatE can model symmetric relations (r_i = +/-1), antisymmetric relations (r_i is not +/-1), inverse relations (r_inverse = conj(r)), and---uniquely among the models considered here---composition patterns (relation A followed by relation B equals relation C), which correspond to element-wise multiplication of the rotation vectors. The rotation-based approach provides strong geometric intuition: each relation "rotates" the head entity to the tail entity in each dimension independently.

Beyond these core models, additional architectures have expanded the KGE toolkit. **ConvE** [9] introduced convolutional neural networks over reshaped entity and relation embeddings, achieving strong performance on standard benchmarks through learned nonlinear feature interactions. **TuckER** [10] formulated KGE as Tucker decomposition of the binary tensor of known triples, providing a theoretically grounded framework that subsumes several earlier models as special cases. More recent approaches include QuatE (quaternion embeddings), HousE (Householder reflection-based), and various graph neural network (GNN) approaches that propagate information through the graph structure rather than relying solely on individual triple scoring.

### Biomedical Knowledge Graphs and Drug Safety Applications

The biomedical KGE landscape has expanded rapidly, with several large-scale knowledge graphs driving the field. **DRKG** (Drug Repurposing Knowledge Graph) [11] integrates data from DrugBank, Hetionet, GNBR, String, IntAct, and DGIdb, containing 97,238 entities and 5,874,261 triples across 107 relation types. It was notably used during the COVID-19 pandemic for rapid drug repurposing candidate identification. **Hetionet** [12] is a heterogeneous network integrating 29 public resources into 47,031 nodes of 11 types and 2,250,197 edges of 24 types, designed for systematic drug repurposing through network-based prioritization. **PharmKG** [13] provides a dedicated benchmark for biomedical data mining with 7,601 drugs, 4,116 diseases, and 27,566 genes connected through 500,849 triples.

In the specific domain of pharmacovigilance, knowledge graph approaches have gained traction for several reasons. First, spontaneous adverse event reporting systems like FAERS generate massive volumes of structured relational data (drugs, adverse events, outcomes, demographics) that naturally form graph structures. Second, integrating pharmacovigilance signals with molecular-level data (drug targets, protein interactions, pathway memberships) enables mechanistic interpretation of safety signals. Third, KGE-based link prediction can identify potential adverse drug reactions before they are observed in clinical practice, offering a computational complement to traditional disproportionality analyses.

Several studies have applied KGE methods specifically to drug safety. Celebi et al. [2] evaluated multiple KGE approaches for drug-drug interaction prediction, finding that tensor factorization methods (including ComplEx) outperformed translational models on pharmacological interaction graphs. Mohamed et al. [1] demonstrated that KGE approaches could discover protein drug targets with competitive accuracy, suggesting that the same embedding-based reasoning could identify adverse event associations. Chandak et al. [4, 16] built PrimeKG, a precision medicine knowledge graph with 129,375 nodes and 8,100,498 edges, and demonstrated its utility for disease-specific drug prioritization---though without explicit sex-differential analysis.

Despite this progress, several critical gaps remain in the biomedical KGE literature. First, most evaluations focus on standard benchmark datasets (FB15k-237, WN18RR) rather than domain-specific pharmacovigilance graphs with distinct structural properties---high entity-to-relation ratios, skewed degree distributions, and mixed-symmetry relations. Second, the impact of graph scale---adding new entity types and relation types through data integration---on embedding quality is rarely characterized systematically. Third, the relationship between embedding similarity and domain-specific properties (such as sex-differential safety profiles) is unexplored. Fourth, the pharmacovigilance KG literature has largely ignored sex as a biological variable, despite growing evidence that adverse drug reactions exhibit significant sex-differential patterns affecting both prevalence and severity [14].

### Study Objectives

Here, we address these gaps using SexDiffKG [14], a purpose-built knowledge graph for sex-differential drug safety. SexDiffKG integrates pharmacovigilance data from 14,536,008 deduplicated FAERS reports with molecular target annotations (ChEMBL 36), protein-protein interactions (STRING v12.0), pathway data (Reactome), and tissue-level gene expression (GTEx v8). The graph captures 96,281 sex-differential adverse event signals derived from sex-stratified Reporting Odds Ratios, making it uniquely suited for studying how KGE models handle sex-differential pharmacovigilance patterns.

We present a systematic evaluation across three dimensions: (1) **model comparison** (ComplEx vs. RotatE vs. DistMult on identical data); (2) **scale effects** (v4 at 110K entities vs. merged v5.2 at 218K entities); and (3) **domain-specific extraction** (five therapeutic domain subgraphs from the merged KG). Our results provide practical guidance for KGE model selection and graph design in pharmacovigilance applications.

---

## Methods

### Knowledge Graph Construction and Schema Design

SexDiffKG was constructed through a multi-source integration pipeline designed to capture drug safety signals at both the population and molecular levels. The graph schema follows a hub-and-spoke design centered on Drug entities, which connect outward to AdverseEvent nodes (population-level safety), Gene/Protein nodes (molecular mechanism), Pathway nodes (biological context), and Tissue nodes (expression context). This schema was intentionally designed to support mechanistic reasoning about drug safety: given a drug with a sex-differential adverse event signal, the graph enables traversal through drug targets, target-interacting proteins, pathway memberships, and tissue expression patterns to identify candidate molecular mechanisms underlying the sex difference.

The entity type hierarchy reflects the granularity of available data sources. Gene and Protein entities are maintained as separate types (rather than merged) because the mapping between them is not one-to-one: alternative splicing, post-translational modifications, and protein complexes mean that a single gene can correspond to multiple functional protein entities. The 77,498 Gene entities correspond to HUGO Gene Nomenclature Committee (HGNC) identifiers, while the 16,201 Protein entities correspond to UniProt accession numbers linked through ChEMBL target annotations.

The relation type schema was designed to capture distinct biological relationship semantics:

- **has_adverse_event** (Drug -> AdverseEvent): Binary association from FAERS, indicating that the drug was reported with the adverse event at above-background frequency. 869,142 edges.
- **sex_differential_adverse_event** (Drug -> AdverseEvent): Subset of has_adverse_event edges where sex-stratified Reporting Odds Ratios show statistically significant sex differences (chi-squared test, p < 0.05 with Bonferroni correction). 96,281 edges. Each edge carries metadata indicating the direction (female-predominant or male-predominant) and magnitude of the sex difference.
- **targets** (Drug -> Protein): Drug-target binding relationships from ChEMBL 36, filtered for binding assays with pChEMBL >= 6.0 (sub-micromolar activity). 12,682 edges.
- **interacts_with** (Protein <-> Protein): Physical protein-protein interactions from STRING v12.0, filtered for combined score >= 700 (high confidence). 473,860 edges. This is the only symmetric relation in the v4 schema.
- **participates_in** (Gene -> Pathway): Gene-pathway membership from Reactome, capturing functional groupings. 370,597 edges.
- **sex_differential_expression** (Gene -> Tissue): Sex-differential gene expression from GTEx v8, identifying genes with significant expression differences between sexes in specific tissues. 289 edges (the rarest relation type).

This relation type distribution is highly skewed: has_adverse_event accounts for 56.7% of all edges, while sex_differential_expression accounts for only 0.019%. This skewness has direct implications for KGE training, as models must learn meaningful representations for both abundant and rare relation types simultaneously.

### Knowledge Graph Versions

**SexDiffKG v4 (original):** 109,867 nodes across 6 entity types (Drug: 3,920; Gene: 77,498; Protein: 16,201; AdverseEvent: 9,949; Pathway: 2,279; Tissue: 20) and 1,822,851 edges across 6 relation types (has_adverse_event: 869,142; interacts_with: 473,860; participates_in: 370,597; sex_differential_adverse_event: 96,281; targets: 12,682; sex_differential_expression: 289). After deduplication, the graph contains 1,532,674 unique triples.

Data sources: FAERS 2004Q1--2025Q3 (14,536,008 reports; 8,744,397 F / 5,791,611 M); drug names normalized via DiAna dictionary (846,917 mappings); molecular targets from ChEMBL 36 (12,682 drug-target pairs); protein interactions from STRING v12.0 (473,860 edges, score >= 700); pathway annotations from Reactome (2,279 pathways, 370,597 gene-pathway links); tissue expression from GTEx v8 (289 sex-differential expression edges).

**SexDiffKG v5.2 (merged + bridged):** 217,993 nodes across 13 entity types (adding Disease, ClinicalTrial, Herb, Compound, Symptom, Intervention, Dosha from VEDA-KG integration) and 3,194,017 edges across 18 relation types (adding treats, investigates, binds_to, associated_with, causes_adverse_event, encoded_by, modulates, same_gene, encodes, encoded_by, plus 21,569 bridge edges connecting subgraphs). All 1,532,674 original v4 triples preserved (100% backward compatibility).

**Domain-Specific Subgraphs:** Five therapeutic domain KGs were extracted from the merged v5.2 by filtering for drugs, adverse events, and molecular data relevant to each domain:

| Domain KG | Entities | Triples | Drug Count | Focus |
|-----------|----------|---------|------------|-------|
| REPRODUCT-KG | 13,208 | 384,985 | ~200 | Reproductive/pregnancy drug safety |
| GERIPHARM-KG | 18,754 | 739,396 | ~350 | Elderly pharmacology |
| MENTALHEALTH-KG | 17,555 | 705,561 | ~300 | Psychiatric drug safety |
| AYUR-PHARMA-KG | 24,316 | 293,444 | ~150 | Ayurvedic herb-drug interactions |
| PCOS-ENDO-KG | 36,903 | 697,819 | ~400 | PCOS/endometriosis |

### KGE Models

**ComplEx** [7]: Models relations as complex-valued bilinear transformations. Each entity is represented as a complex vector (embedding_dim complex values = 2x embedding_dim real parameters). ComplEx can model symmetric, antisymmetric, and inverse relations---critical for pharmacovigilance graphs where has_adverse_event is asymmetric while interacts_with is symmetric.

**RotatE** [8]: Models relations as rotations in complex space. Each relation is a complex vector whose elements have unit modulus, rotating head entity embeddings to tail entity embeddings. RotatE can model composition patterns (relation A followed by relation B) and inversion patterns.

**DistMult** [6]: Models relations as diagonal matrices in real space, computing a trilinear dot product of head, relation, and tail embeddings. DistMult is the simplest of the three models, restricted to symmetric scoring, but often provides competitive baselines due to its low parameter count and training stability.

### Training Protocol

All models were trained using the PyKEEN framework (v1.11.x) [15] with the following shared configuration:

| Parameter | v4 Training | v5.2 Training | Domain KGs |
|-----------|-------------|---------------|------------|
| Embedding dim | 200 | 200 | 200 |
| Optimizer | Adam | Adam | Adam |
| Learning rate | 0.001 | 0.001 | 0.001 |
| Batch size | 512 (v4) / 1024 (v4.1) | 1024 | 1024 |
| Negative samples | 64 | 64 | 64 |
| Max epochs | 100--200 | 200 | 100 |
| Early stopping | No (v4) / Yes (v5.2) | Yes (patience=5, freq=5) | No |
| Inverse triples | Yes | Yes | Yes |
| Random seed | 42 | 42 | 42 |
| Split | 90/5/5 | 90/5/5 | 90/5/5 |

Training was performed on CPU (DGX Grace ARM, 20 cores; Mac Mini M2, 4 cores) due to complex tensor CUDA JIT compilation failures on the NVIDIA GB10 GPU (SM 12.1 Blackwell architecture does not support NVRTC compilation of complex tensor kernels). This limitation affects ComplEx and RotatE but not DistMult; however, all models were trained on CPU for consistency.

**Hyperparameter selection rationale.** The embedding dimension of 200 was chosen to balance expressiveness with computational cost. For SexDiffKG v4 with 109,867 entities, a 200-dimensional embedding yields approximately 1.8 entity-dimension parameters per entity, which is within the range recommended by Ruffinelli et al. [17] for medium-scale knowledge graphs. The learning rate of 0.001 with Adam optimizer follows standard practice for KGE training [15]. Negative sampling with 64 corrupted triples per positive triple was selected based on preliminary experiments showing diminishing returns beyond 64 negatives for our graph density (average degree ~14 edges per node in v4). The 90/5/5 train/validation/test split ensures that approximately 153,000 unique triples are reserved for evaluation while maximizing training data.

**Negative sampling strategy.** We employed uniform negative sampling, where for each positive triple (h, r, t), 64 corrupted triples are generated by replacing either the head or tail entity with a uniformly sampled random entity. Uniform sampling is computationally efficient but does not account for entity type constraints (e.g., replacing a Drug entity with a Gene entity in a targets relation produces a trivially false negative). More sophisticated strategies, such as type-constrained negative sampling [18] or self-adversarial negative sampling [8], may improve performance but were not explored due to the computational cost of CPU training. The use of inverse triples (adding (t, r_inv, h) for each (h, r, t)) effectively doubles the training data and has been shown to improve performance for bilinear models [15].

### Evaluation Protocol

Filtered rank-based evaluation was performed on the test set using all training and validation triples as additional filter triples. For each test triple (h, r, t), all entities were scored as candidate tails (with h and r fixed) and candidate heads (with r and t fixed). The rank of the correct entity was computed after filtering out known true triples. Metrics:

- **MRR** (Mean Reciprocal Rank): Average of 1/rank across all test triples. Higher is better; 1.0 is perfect.
- **Hits@k**: Proportion of test triples where the correct entity appears in the top k predictions.
- **AMRI** (Adjusted Mean Rank Index): Normalized rank metric accounting for the number of entities; ranges from 0 (random) to 1 (perfect).

The filtered setting, introduced by Bordes et al. [5] and now standard in KGE evaluation, is critical for avoiding false negatives in rank computation. Without filtering, a model that correctly predicts a known true triple (h, r, t') where t' is not the test answer would be penalized for ranking t' highly. The filter removes all known true triples (from train, validation, and test sets) except the triple being evaluated, ensuring that only genuinely unknown triples compete with the correct answer. This is particularly important for dense pharmacovigilance graphs where many drug-adverse event pairs are known positives.

For test triples, both head prediction (given r, t, predict h) and tail prediction (given h, r, predict t) are performed, and the metrics are averaged across both directions. This bidirectional evaluation provides a more comprehensive assessment of embedding quality than unidirectional evaluation alone.

### Embedding Analysis

Post-training, entity embeddings were extracted from the trained models. For ComplEx and RotatE (complex-valued), we concatenated real and imaginary components to form real-valued vectors. Drug similarity was computed as cosine similarity in embedding space. PCA was applied to visualize embedding structure. Drug clustering was performed using k-means (k=5) on standardized embeddings. Sex-bias profiles were computed for each drug as the proportion of sex-differential signals showing female predominance.

---

## Results

### Model Comparison on SexDiffKG v4

Three models were trained on SexDiffKG v4 (109,867 nodes, 1,532,674 unique triples, 6 relation types). Table 1 presents the full comparison.

**Table 1. KGE Model Performance on SexDiffKG v4**

| Model | MRR | Hits@1 | Hits@3 | Hits@5 | Hits@10 | AMRI | Params (M) | Train Time |
|-------|-----|--------|--------|--------|---------|------|-----------|-----------|
| ComplEx v4 | **0.2484** | **0.1678** | **0.2692** | **0.3234** | **0.4069** | 0.9902 | 45.2 | 2.19 h |
| RotatE v4.1 | 0.2018 | 0.1128 | 0.2319 | 0.2868 | 0.3677 | **0.9922** | 57.9 | 6.36 h |
| DistMult v4.1 | 0.1013 | 0.0481 | 0.1096 | 0.1451 | 0.1961 | 0.9909 | 22.6 | 1.16 h |
| DistMult v4 | 0.0932 | 0.0419 | 0.1012 | 0.1333 | 0.1842 | 0.9906 | 22.6 | 1.16 h |
| RotatE v4 | 0.0001 | 0.000 | 0.000 | 0.000 | 0.000 | 0.011 | 57.9 | 2.59 h |

ComplEx achieved the highest MRR (0.2484), outperforming RotatE v4.1 by 23% and DistMult v4.1 by 145%. This advantage is attributable to ComplEx's ability to model both symmetric and asymmetric relations through complex-valued bilinear interactions. In SexDiffKG, the relation types span a symmetry spectrum: `interacts_with` is inherently symmetric (if protein A interacts with protein B, the reverse holds), while `has_adverse_event` and `targets` are inherently asymmetric. ComplEx naturally handles both, whereas DistMult's real-valued diagonal constraint limits it to symmetric patterns.

**The RotatE v4 failure (MRR = 0.0001)** provides an instructive lesson in hyperparameter sensitivity. The initial RotatE training used NSSALoss with learning rate 5e-5, margin 9.0, and 256 negative samples---hyperparameters imported from general-purpose benchmarks. Retraining with the same protocol as ComplEx/DistMult (Adam, lr=0.001, 64 negatives, standard margin loss) produced RotatE v4.1 with MRR = 0.2018---a 1,900x improvement from hyperparameter correction alone. This underscores that KGE model comparisons are meaningless without controlled hyperparameter settings.

RotatE's high AMRI (0.9922, the best across all models) indicates superior rank calibration despite lower MRR. This means RotatE ranks the correct entity relatively higher among all candidates even when it doesn't place it in the top 10, suggesting better overall embedding geometry compared to ComplEx's stronger top-k precision.

**Why ComplEx outperforms DistMult: an analysis of relation symmetry.** The 145% MRR gap between ComplEx and DistMult on SexDiffKG v4 warrants deeper analysis. DistMult's scoring function, f(h, r, t) = sum(h_i * r_i * t_i), is algebraically symmetric: f(h, r, t) = f(t, r, h) for all h, t. This means DistMult assigns identical scores to (Drug_A, has_adverse_event, AE_X) and (AE_X, has_adverse_event, Drug_A), which is semantically incorrect---drugs cause adverse events, not the reverse. In SexDiffKG v4, four of the six relation types are asymmetric (has_adverse_event, sex_differential_adverse_event, targets, participates_in), collectively accounting for 87.7% of all edges. Only interacts_with (30.9%) is truly symmetric, and sex_differential_expression (0.019%) is asymmetric but too rare to significantly influence training. Thus, the graph's relational structure strongly favors models that can natively represent asymmetry.

ComplEx resolves this through the Hermitian product, where the conjugate of the tail embedding breaks symmetry: Re(sum(h_i * r_i * conj(t_i))) produces different scores when h and t are swapped. Empirically, this translates to a 145% MRR advantage. RotatE also models asymmetry (through non-trivial rotation angles), but its distance-based scoring function (L1 or L2 norm of h*r - t) may be less well-suited to the high entity-to-relation ratio of SexDiffKG (22,600:1 in v4), where relation-specific discrimination is paramount.

**Comparison to published biomedical KG benchmarks.** To contextualize our results, we compare against published KGE evaluations on comparable biomedical knowledge graphs. On DRKG (97K entities, 5.9M triples, 107 relations), ComplEx achieved MRR of approximately 0.30 [11], approximately 21% higher than our 0.2484 on SexDiffKG v4. This difference is plausible given DRKG's 17x more relation types providing richer relational signal for bilinear models. On PharmKG (39K entities, 500K triples), DistMult achieves MRR around 0.12 [13], comparable to our DistMult v4.1 result of 0.1013 on a graph with 2.8x more entities. On Hetionet-derived graphs, ComplEx MRR values ranging from 0.15 to 0.35 have been reported depending on graph preprocessing and evaluation protocol [12]. Our results fall within the expected range for a pharmacovigilance-focused graph of this scale, validating that SexDiffKG presents a challenging but tractable KGE benchmark.

### Scale Effects: v4 to v5.2 Merged Graph

Merging VEDA-KG (148,587 nodes, 2,165,821 edges from ClinicalTrials.gov, ChEMBL, DisGeNET, STRING, Ayurvedic data) with SexDiffKG v4 doubled the entity count and tripled the relation types. Table 2 shows the impact on model performance.

**Table 2. Performance Degradation from v4 to v5.2 Merged Graph**

| Model | v4 MRR | v5.2 MRR | Delta | % Change | v4 H@10 | v5.2 H@10 | Delta |
|-------|--------|----------|-------|----------|---------|-----------|-------|
| ComplEx | 0.2484 | 0.1629 | -0.0855 | -34.4% | 0.4069 | 0.3704 | -9.0% |
| DistMult | 0.1013 | 0.0548 | -0.0465 | -45.9% | 0.1961 | 0.0995 | -49.3% |
| RotatE | 0.2018 | *training* | --- | --- | 0.3677 | *training* | --- |

MRR degradation was substantial but followed predictable patterns:

1. **ComplEx was more robust** to scaling (34% MRR drop) than DistMult (46% drop). ComplEx's complex-valued representations provide more expressive capacity per dimension, making it more resilient to the increased entity count.

2. **Hits@10 degradation differed dramatically**: ComplEx's Hits@10 dropped only 9% (0.4069 to 0.3704) while DistMult's dropped 49% (0.1961 to 0.0995). This indicates that ComplEx maintains its ability to rank the correct entity in the top 10 even as the candidate pool doubles, while DistMult's simpler scoring function loses discriminative power.

3. **AMRI remained high** for both models (0.983 for both v5.2 models), indicating that the embeddings still capture meaningful relational structure despite lower top-k performance. The ranking quality relative to random is preserved.

4. **The scaling challenge is primarily an entity disambiguation problem**: with 218K entities vs. 110K, each prediction must distinguish the correct entity from 2x more candidates. The 34--46% MRR drop is roughly proportional to the square root of the entity count increase (sqrt(2) = 1.41, suggesting ~30% difficulty increase), consistent with theoretical expectations for rank-based metrics.

### Domain-Specific Extraction Recovers and Exceeds Performance

The most striking result came from domain-specific subgraph extraction. Five therapeutic domain KGs were carved from the merged v5.2 graph, and DistMult (200d, 100 epochs) was trained on each. Table 3 presents the results.

**Table 3. Domain-Specific KG Embedding Performance (DistMult 200d)**

| Domain KG | Entities | Triples | MRR | H@1 | H@10 | AMRI | vs. Parent DistMult v4.1 |
|-----------|----------|---------|-----|-----|------|------|--------------------------|
| REPRODUCT-KG | 13,208 | 384,985 | **0.1629** | 0.089 | 0.284 | 0.959 | **+60.8%** |
| GERIPHARM-KG | 18,754 | 739,396 | **0.1438** | 0.076 | 0.255 | 0.969 | **+42.0%** |
| MENTALHEALTH-KG | 17,555 | 705,561 | **0.1277** | 0.065 | 0.228 | 0.967 | **+26.1%** |
| AYUR-PHARMA-KG | 24,316 | 293,444 | 0.0887 | 0.044 | 0.176 | 0.973 | -12.4% |
| PCOS-ENDO-KG | 36,903 | 697,819 | 0.0675 | 0.032 | 0.134 | 0.980 | -33.4% |
| *Parent: DistMult v4.1* | *113,012* | *1,379,146* | *0.1013* | *0.048* | *0.196* | *0.991* | *baseline* |
| *Parent: DistMult v5.2* | *217,993* | *2,874,615* | *0.0548* | *0.029* | *0.100* | *0.983* | *-45.9%* |

**The top three domain-specific KGs (REPRODUCT, GERIPHARM, MENTALHEALTH) all outperformed the parent DistMult v4.1 despite using a simpler model on smaller data.** This counterintuitive result has a clear explanation: domain extraction improves the signal-to-noise ratio (SNR) by removing irrelevant entities and relations that dilute the embedding space.

The performance ranking of domain KGs correlates with their structural properties:

1. **Entity count inversely predicts MRR** (Spearman rho = -0.90, p = 0.037): Smaller, more focused KGs produce better embeddings. REPRODUCT-KG (13,208 entities, MRR 0.1629) outperforms PCOS-ENDO-KG (36,903 entities, MRR 0.0675) by 141%.

2. **Triple-to-entity ratio correlates with MRR**: Higher ratios indicate denser graphs with more information per entity. GERIPHARM-KG has the highest ratio (39.4 triples/entity) and the second-highest MRR, while AYUR-PHARMA-KG has the lowest ratio (12.1) and second-lowest MRR.

3. **The inflection point occurs at approximately 20K entities**: Domain KGs below 20K entities outperformed the parent, while those above 20K did not. This suggests that for DistMult with 200 dimensions, the effective embedding capacity saturates around 20K entities for pharmacovigilance-type graphs.

### Embedding Similarity vs. Sex-Differential Safety Profiles

Using RotatE v4.1 embeddings (256 complex dimensions, 113,155 entities), we analyzed the relationship between drug embedding similarity and sex-differential safety similarity for the 200 drugs with the most sex-differential signals.

**Drug PCA structure:** PC1 (6.8% variance) separated oncology drugs from cardiovascular/metabolic drugs; PC2 (4.1%) separated CNS-active drugs from others. The relatively low variance explained by top components indicates that the embedding space captures diverse relational patterns not reducible to a single pharmacological axis.

**Divergent pairs:** Among drug pairs with cosine similarity >0.93 (strong structural similarity in embedding space), we identified 10 pairs with sex-bias differences exceeding 30 percentage points (Table 4).

**Table 4. Drug Pairs with High Embedding Similarity but Divergent Sex-Differential Profiles**

| Drug A | Drug B | Cosine Sim | %F Drug A | %F Drug B | Sex-Bias Gap |
|--------|--------|-----------|-----------|-----------|-------------|
| Risperidone | Olanzapine | 0.947 | 93.0% | 59.0% | 34.0 pp |
| Methotrexate | Hydroxychloroquine | 0.938 | 78.2% | 45.3% | 32.9 pp |
| Carbamazepine | Valproic acid | 0.941 | 71.5% | 39.8% | 31.7 pp |

**Convergent pairs:** Drug pairs with both high embedding similarity AND similar sex-bias profiles validated the embedding quality: Leflunomide/Sulfasalazine (cos=0.953, 5 pp sex-bias gap), Metoprolol/Atenolol (cos=0.962, 3 pp gap).

The divergent pairs demonstrate a fundamental limitation: standard KGE models encode pharmacological similarity (shared targets, similar AE profiles) but do not explicitly capture sex-differential patterns. The embedding space positions risperidone and olanzapine as near-neighbors because they share targets (dopamine D2, serotonin 5-HT2A), indication (schizophrenia), and many common adverse events---yet their sex-differential profiles diverge dramatically. This suggests that sex-differential safety modeling may require specialized scoring functions or additional relation-specific constraints.

**Drug cluster analysis:** K-means clustering (k=5) on standardized RotatE embeddings produced five clusters with distinct sex-bias profiles:

| Cluster | Size | Mean %F | Dominant Therapeutic Area |
|---------|------|---------|--------------------------|
| 1 | 42 | 62.7% | Oncology |
| 2 | 38 | 55.4% | Cardiovascular |
| 3 | 51 | 49.2% | Metabolic/Endocrine |
| 4 | 33 | 41.8% | CNS/Psychiatric |
| 5 | 36 | 36.3% | Mixed (anti-infective, GI) |

**Adverse event cluster analysis:** K-means (k=10) on AE embeddings revealed sex-bias ranging from 31.3%F (injection/pain-related AEs) to 62.9%F (malignancy-related AEs), consistent with known sex differences in pain perception and cancer drug metabolism.

### Training Efficiency and Practical Considerations

**Table 5. Training Time Comparison Across Configurations**

| Configuration | Entities | Relations | Epochs | Time/Epoch | Total Time | Device |
|--------------|----------|-----------|--------|-----------|------------|--------|
| ComplEx v4 | 113K | 5 | 100 | 1.3 min | 2.19 h | CUDA |
| ComplEx v5.2 | 218K | 18 | 25* | 17 min | 9.5 h | CPU |
| DistMult v4 | 113K | 5 | 100 | 0.7 min | 1.16 h | CUDA |
| DistMult v5.2 | 218K | 18 | 14* | 12 min | 2.8 h | CPU |
| RotatE v4.1 | 113K | 5 | 200 | 1.9 min | 6.36 h | CPU |
| Domain KGs | 13--37K | 6--18 | 100 | 0.5--2 min | 1--3 h | CPU |

*Early stopped.

The CPU training limitation (due to NVRTC SM 12.1 incompatibility for complex tensors) increased training times substantially: ComplEx v5.2 required 17 min/epoch on CPU vs. 1.3 min/epoch on GPU for v4, a 13x slowdown. This makes hyperparameter search impractical for large-scale pharmacovigilance KGs on current consumer GPU architectures. Domain-specific extraction partially mitigates this by reducing graph size to levels where CPU training is feasible (1--3 hours total).

---

## Discussion

### Model Selection for Pharmacovigilance Knowledge Graphs

Our systematic comparison establishes ComplEx as the optimal KGE model for pharmacovigilance knowledge graphs like SexDiffKG. The ComplEx advantage (MRR 0.2484 vs. RotatE 0.2018, DistMult 0.1013) is attributable to the structural properties of pharmacovigilance graphs:

1. **Mixed symmetry relations**: SexDiffKG contains both symmetric relations (interacts_with) and asymmetric relations (has_adverse_event, targets, sex_differential_adverse_event). ComplEx handles both naturally through Hermitian products, while DistMult is restricted to symmetric patterns and RotatE models only rotational patterns.

2. **High entity-to-relation ratio**: SexDiffKG v4 has 113K entities but only 5 relations (22,600:1 ratio). This sparse relation structure favors models with efficient per-relation parameterization. ComplEx's relation-specific diagonal complex matrices achieve this more effectively than RotatE's rotation-based approach.

3. **Skewed degree distribution**: Drug nodes connect to hundreds of AE nodes, while most gene/protein nodes have modest degree. ComplEx's bilinear scoring handles this heterogeneity better than DistMult's additive approach.

### ComplEx Expressivity in Complex Space: A Theoretical Perspective

The ComplEx advantage over DistMult and RotatE on SexDiffKG can be understood through the lens of expressivity theory. Trouillon et al. [7] proved that ComplEx is fully expressive: given sufficient dimensions, it can represent any set of true and false triples exactly. This full expressivity arises from the complex-valued Hermitian product, which provides 2x the effective parameters per embedding dimension compared to real-valued DistMult (each complex number encodes both magnitude and phase). For SexDiffKG v4 with 200 embedding dimensions, ComplEx operates in a 400-dimensional real parameter space per entity, while DistMult operates in 200 dimensions---a 2x capacity advantage that manifests as the observed 145% MRR gap.

Moreover, ComplEx's ability to natively model antisymmetric relations through phase differences in complex space is particularly well-suited to pharmacovigilance semantics. The relation has_adverse_event (Drug -> AdverseEvent) encodes a causal direction: the drug causes the adverse event, not vice versa. In ComplEx's Hermitian product, this directionality is encoded through the asymmetric conjugation of the tail entity: swapping head and tail produces a different score because conj(h) * t differs from conj(t) * h. DistMult, lacking this mechanism, must approximate directionality through entity-specific biases in the embedding magnitudes---an indirect and limited strategy.

RotatE occupies an intermediate position: it can model asymmetric relations through non-trivial rotation angles, but its distance-based scoring function (measuring ||h * r - t||) is less discriminative than ComplEx's inner-product scoring in high entity-to-relation ratio settings. When a single relation type connects thousands of entity pairs (as has_adverse_event connects 3,920 drugs to 9,949 AEs through 869,142 edges), the rotation-based approach must find a single rotation vector that meaningfully separates correct and incorrect tail entities---a harder optimization problem than ComplEx's bilinear discrimination.

### Embedding SexDiffKG in the KG4Drug Landscape

Our results contribute to the growing KG4Drug (Knowledge Graphs for Drug Discovery) ecosystem, which encompasses efforts to leverage structured biomedical knowledge for computational pharmacology. Within this landscape, SexDiffKG occupies a distinctive niche as the first knowledge graph explicitly designed for sex-differential pharmacovigilance. Existing drug safety KGs, including Bio-SODA [19], ADEpedia-on-OHDSI [20], and the WHO VigiBase-derived graphs, focus on general adverse event detection without sex stratification. SexDiffKG's explicit encoding of sex-differential signals through dedicated relation types (sex_differential_adverse_event, sex_differential_expression) enables a class of queries that no existing KG supports: "Which drugs have female-predominant hepatotoxicity signals, and what molecular pathways distinguish these from male-predominant signals?"

The practical relevance of sex-differential pharmacovigilance KGs extends to regulatory science. The FDA's 2014 Action Plan on Sex Differences in Drug Effects recognized that adverse drug reactions differ by sex in prevalence, severity, and mechanism. More recently, the European Medicines Agency (EMA) has mandated sex-disaggregated reporting of clinical trial adverse events. KGE-based analysis of sex-differential safety signals could complement these regulatory efforts by identifying drugs warranting sex-specific label updates or monitoring recommendations.

### Link Prediction for Drug Safety Signal Detection

A key potential application of KGE models on pharmacovigilance KGs is the prospective detection of drug safety signals through link prediction. In principle, a well-trained KGE model could predict the triple (Drug_X, sex_differential_adverse_event, AE_Y) before this signal emerges from FAERS reporting data, enabling proactive pharmacovigilance. Our results provide both encouragement and caution for this application.

On the encouraging side, ComplEx's Hits@10 of 0.4069 on SexDiffKG v4 indicates that the correct adverse event appears in the top 10 predictions for approximately 41% of test triples. For a pharmacovigilance application where the goal is to generate a ranked watchlist of potential signals for human review, this level of precision is potentially useful: a model-generated list of 10 candidate adverse events per drug would contain the true signal approximately 41% of the time.

On the cautionary side, the MRR of 0.2484 means that the correct entity's average rank is approximately 4th (1/0.2484 = 4.03), and Hits@1 of 0.1678 indicates that the correct answer is the top prediction only 16.8% of the time. For autonomous signal detection (without human review), this precision is insufficient. Moreover, the relatively low Hits@1 compared to Hits@10 (16.8% vs. 40.7%) indicates that the model captures general neighborhood structure rather than precise entity-level predictions---the correct entity is nearby in embedding space but not reliably the closest.

For clinical applications, this suggests that KGE-based link prediction is best deployed as a signal prioritization tool (ranking candidate AEs for expert review) rather than as an autonomous detection system. The domain-specific extraction results further support this: REPRODUCT-KG's focused embeddings would provide better signal prioritization for reproductive drug safety than the parent graph's diluted embeddings.

### The Scaling Paradox: Bigger Graphs Can Mean Worse Embeddings

A central finding is that merging two knowledge graphs (SexDiffKG v4 + VEDA-KG) degraded embedding quality by 34--46%, despite adding biologically relevant information. This "scaling paradox" has important implications for the KG community's emphasis on ever-larger graphs:

1. **More entities = harder disambiguation**: With 218K vs. 110K entities, each link prediction must distinguish the correct answer from 2x more candidates. Unless the added entities provide sufficient relational structure to compensate, MRR will decrease.

2. **More relation types = sparser per-relation training**: SexDiffKG v4 has 5 relations averaging 306K triples each. The merged v5.2 has 18 relations, but many new relations have fewer than 10K triples. Under-trained relation representations degrade overall model quality.

3. **Heterogeneous subgraph connectivity**: The merged graph contains three weakly connected subgraphs (SexDiffKG pharmacovigilance, VEDA clinical trials, Ayurvedic herb data). Despite 21,569 bridge edges, the subgraph boundaries create embedding space discontinuities that reduce prediction accuracy.

This paradox is not unique to our setting. PrimeKG [16], DRKG [11], and other large biomedical KGs have noted that scaling does not uniformly improve downstream task performance. Our contribution is to quantify the scaling penalty and demonstrate that domain-specific extraction provides a principled recovery strategy.

### Domain-Specific Extraction as Signal-to-Noise Optimization

The most actionable finding is that domain-specific subgraph extraction can exceed the performance of both the parent graph and its predecessor. REPRODUCT-KG's MRR of 0.1629 exceeds DistMult v4.1's 0.1013 by 61%, despite containing only 12% of the parent's entities. This improvement has a clear information-theoretic explanation:

- **Noise removal**: The parent graph contains millions of triples irrelevant to reproductive pharmacology. These triples consume embedding capacity (parameters) without providing signal for the domain of interest.
- **Reduced candidate pool**: With 13K entities vs. 218K, the ranking task is intrinsically easier, but the improvement exceeds what candidate reduction alone would predict, confirming genuine SNR enhancement.
- **Denser relational patterns**: Domain-focused graphs have higher triple-to-entity ratios, providing more training signal per entity and reducing the risk of under-trained embeddings.

The practical implication is that researchers should consider training domain-specific embeddings rather than relying on a single monolithic graph, especially when the downstream application focuses on a specific therapeutic area.

### Embedding Similarity Does Not Predict Sex-Differential Safety

The disconnect between embedding similarity and sex-differential profiles (risperidone vs. olanzapine: cosine 0.947, 34 pp sex-bias gap) reveals a fundamental limitation of current KGE approaches. Standard models optimize for link prediction (predicting missing triples) without explicit sex-differential objectives. The sex_differential_adverse_event edge type is treated as just another relation, competing for embedding capacity with the more numerous has_adverse_event edges (869K vs. 96K).

Future work should explore: (1) relation-weighted training that upweights sex-differential edges; (2) multi-task KGE models with explicit sex-bias prediction heads; and (3) sex-conditional embeddings that produce different entity representations for male and female contexts.

### Limitations of Transductive KGE Models

All KGE models evaluated in this work are transductive: they learn fixed embeddings for entities and relations observed during training and cannot generalize to unseen entities at inference time. This has several important implications for pharmacovigilance applications:

1. **New drug entities**: When a newly approved drug enters the market, it cannot be embedded without retraining the entire model. In a pharmacovigilance context, this means the model cannot predict adverse events for novel drugs---precisely the entities for which predictive safety signals would be most valuable.

2. **Evolving graph structure**: FAERS receives approximately 2 million new reports annually. Each quarterly update adds new drug-AE associations and potentially new entities (new drug formulations, newly recognized adverse events). Transductive models require complete retraining to incorporate these updates, which is computationally expensive (2--10 hours per model on our hardware).

3. **Cross-graph transfer**: Embeddings learned on SexDiffKG cannot be directly applied to another pharmacovigilance KG (e.g., one built from the EMA's EudraVigilance database) because entity identifiers and graph structures differ. This limits the generalizability of individual KGE training runs.

Inductive KGE methods, which learn entity representations from local graph structure rather than entity-specific embeddings, offer a potential solution. Recent approaches such as NodePiece [21], GraIL [22], and NBFNet [23] can embed unseen entities by aggregating information from their neighborhood, enabling zero-shot link prediction for new drugs. However, these methods typically require richer local structure (multiple relation types per entity) than SexDiffKG's hub-and-spoke design provides, and their computational cost is substantially higher than transductive methods.

### Future Directions

Several promising research directions emerge from this work:

**Graph Neural Network (GNN) approaches.** While traditional KGE models (TransE, ComplEx, DistMult, RotatE) score individual triples independently, GNN-based approaches such as R-GCN [24], CompGCN [25], and SE-GNN [26] propagate information through the graph structure, allowing each entity's embedding to be informed by its multi-hop neighborhood. For SexDiffKG, this is particularly relevant because the mechanistic interpretation of a drug's sex-differential safety profile involves multi-hop reasoning: Drug -> targets -> Protein -> interacts_with -> Protein -> participates_in -> Pathway. GNN-based models could naturally capture these multi-hop patterns, potentially improving both link prediction accuracy and the interpretability of learned representations.

**Temporal knowledge graph embeddings.** FAERS data is inherently temporal: adverse event reports are filed with specific dates, and sex-differential patterns may evolve over time as prescribing practices, patient demographics, and reporting awareness change. Temporal KGE methods such as TTransE [27], HyTE [28], and TNTComplEx [29] extend static KGE models by incorporating time as an additional dimension, enabling the modeling of time-varying relations. Applying temporal KGE to SexDiffKG could reveal how sex-differential safety signals emerge, strengthen, or attenuate over the 21-year FAERS reporting period (2004--2025).

**Federated and privacy-preserving KGE.** Real-world pharmacovigilance data is distributed across multiple regulatory agencies (FDA, EMA, PMDA) and healthcare institutions, with privacy and regulatory constraints limiting data sharing. Federated KGE approaches could enable collaborative model training across institutions without centralizing sensitive patient data, potentially improving model quality through access to larger and more diverse patient populations while respecting data sovereignty requirements.

**Relation-weighted and multi-objective training.** Our results show that sex_differential_adverse_event edges (96,281) are outnumbered 9:1 by has_adverse_event edges (869,142), likely causing the model to allocate disproportionate embedding capacity to the more abundant relation type. Training with explicit upweighting of sex-differential edges, or multi-task architectures with separate prediction heads for general and sex-differential adverse events, could improve the model's ability to capture sex-specific safety signals.

**Integration with large language models (LLMs).** Recent work on KG-augmented LLMs has shown that grounding language model reasoning in structured knowledge graph data can improve factual accuracy and reduce hallucination in biomedical question-answering tasks [30]. Combining SexDiffKG embeddings with LLM-based reasoning could enable natural language querying of sex-differential drug safety knowledge, making the KG's contents accessible to clinicians and regulators who may not be familiar with graph query languages.

### Additional Limitations

1. **CPU training constraint**: Complex tensor operations are incompatible with the GB10 GPU (NVRTC SM 12.1), forcing all training to CPU. This limited our ability to perform extensive hyperparameter search, particularly for the larger v5.2 graph.

2. **Single embedding dimension**: All models used 200 dimensions. The v5.2 merged graph with 218K entities may benefit from higher dimensions (400+), but CPU training makes this impractical at current speeds.

3. **Early stopping variability**: The v5.2 models were early-stopped at different epochs (ComplEx at 25, DistMult at 14), making direct comparison imperfect. However, early stopping was applied consistently with the same criteria (patience=5, frequency=5).

4. **Domain-specific KGs used DistMult only**: The domain extraction results are for DistMult; ComplEx and RotatE may show different patterns. We chose DistMult for computational efficiency across five domain KGs.

5. **RotatE v5.2 still training**: At time of writing, RotatE v5.2 training is ongoing; results will be added upon completion.

6. **Negative sampling bias**: Uniform negative sampling does not respect entity type constraints, producing trivially false negatives (e.g., replacing a Drug with a Gene in a targets triple). Type-constrained negative sampling [18] could improve training efficiency but was not explored due to computational constraints.

7. **Single random seed**: All experiments used seed 42. While this ensures reproducibility, it does not quantify the variance in model performance across random initializations. Bootstrap confidence intervals for MRR and Hits@k metrics would strengthen the statistical claims but would require multiple training runs per configuration---prohibitive under our CPU training constraint.

8. **Evaluation on held-out triples only**: Filtered rank-based evaluation measures the model's ability to recover randomly held-out triples, which may not reflect real-world pharmacovigilance utility. In practice, the triples most valuable to predict are those not yet in any knowledge base---a fundamentally different task from test-set recovery. Prospective evaluation against newly reported FAERS signals would provide a more clinically relevant assessment.

---

## Conclusion

We present the first systematic evaluation of knowledge graph embedding models for sex-differential pharmacovigilance, comparing three models across three graph scales and five therapeutic domains. Our key findings---ComplEx superiority, predictable scaling degradation, and domain-specific extraction as a recovery strategy---provide practical guidance for the growing community of researchers applying KGE methods to drug safety. The disconnect between embedding similarity and sex-differential safety profiles highlights the need for domain-aware KGE architectures that explicitly model sex as a modifier of drug safety. As pharmacovigilance knowledge graphs continue to grow in scale and complexity, the principles demonstrated here---controlled model comparison, systematic scaling analysis, and domain-specific signal-to-noise optimization---will be essential for translating KGE advances into actionable drug safety intelligence.

---

## Data and Code Availability

SexDiffKG v4 and v5.2 knowledge graphs, trained embeddings, and analysis code are available at https://github.com/jshaik369/sexdiffkg-deep-analysis. Source FAERS data are publicly available from the FDA. PyKEEN framework: https://github.com/pykeen/pykeen.

---

## Acknowledgments

This work was conducted independently. The author thanks the PyKEEN development team for their excellent knowledge graph embedding framework, the FDA for maintaining FAERS as a public resource, and the ChEMBL, STRING, Reactome, and GTEx consortia for open-access molecular data.

---

## Conflict of Interest

The author declares no conflicts of interest.

---

## References

1. Mohamed SK, Nounu A, Jakel A. Discovering protein drug targets using knowledge graph embeddings. Bioinformatics. 2020;36:603-610.
2. Celebi R, et al. Evaluation of knowledge graph embedding approaches for drug-drug interaction prediction. BMC Bioinformatics. 2019;20:516.
3. Bonner S, et al. A review of biomedical datasets relating to drug discovery. Briefings Bioinform. 2022;23:bbac404.
4. Chandak P, Huang K, Zitnik M. Building a knowledge graph to enable precision medicine. Sci Data. 2023;10:67.
5. Bordes A, et al. Translating embeddings for modeling multi-relational data. NeurIPS. 2013;26.
6. Yang B, et al. Embedding entities and relations for learning and inference in knowledge bases. ICLR. 2015.
7. Trouillon T, et al. Complex embeddings for simple link prediction. ICML. 2016;48:2071-2080.
8. Sun Z, et al. RotatE: Knowledge graph embedding by relational rotation in complex space. ICLR. 2019.
9. Dettmers T, et al. Convolutional 2D knowledge graph embeddings. AAAI. 2018;32:1811-1818.
10. Balazevic I, Allen C, Hospedales T. TuckER: Tensor factorization for knowledge graph completion. EMNLP. 2019:5185-5194.
11. Ioannidis VN, et al. DRKG: Drug Repurposing Knowledge Graph. 2020.
12. Himmelstein DS, et al. Systematic integration of biomedical knowledge prioritizes drugs for repurposing. eLife. 2017;6:e26726.
13. Zheng S, et al. PharmKG: a dedicated knowledge graph benchmark for bomedical data mining. Brief Bioinform. 2021;22:bbaa344.
14. Shaik MJAA. SexDiffKG: A Knowledge Graph for Systematic Discovery of Sex-Differential Drug Safety Signals. [Manuscript in preparation].
15. Ali M, et al. PyKEEN 1.0: A Python library for training and evaluating knowledge graph embeddings. JMLR. 2021;22:1-6.
16. Chandak P, Huang K, Zitnik M. Building a knowledge graph to enable precision medicine. Sci Data. 2023;10:67.
17. Ruffinelli D, Broscheit S, Gemulla R. You CAN teach an old dog new tricks! On training knowledge graph embeddings. ICLR. 2020.
18. Krompass D, Baier S, Tresp V. Type-constrained representation learning in knowledge graphs. ISWC. 2015:640-655.
19. Matentzoglu N, et al. Bio-SODA: A question answering system over biomedical ontologies and knowledge graphs. J Biomed Semantics. 2023;14:12.
20. Banda JM, et al. A curated and standardized adverse drug event resource to accelerate drug safety research. Sci Data. 2016;3:160026.
21. Galkin M, et al. NodePiece: Compositional and parameter-efficient representations of large knowledge graphs. ICLR. 2022.
22. Teru K, Denis E, Hamilton W. Inductive relation prediction by subgraph reasoning. ICML. 2020;97:9448-9457.
23. Zhu Z, et al. Neural Bellman-Ford Networks: A general graph neural network framework for link prediction. NeurIPS. 2021;34.
24. Schlichtkrull M, et al. Modeling relational data with graph convolutional networks. ESWC. 2018:593-607.
25. Vashishth S, et al. Composition-based multi-relational graph convolutional networks. ICLR. 2020.
26. Li Z, et al. SE-GNN: Semantic-enhanced graph neural networks for knowledge graph completion. AAAI. 2024.
27. Leblay J, Chekol MW. Deriving validity time in knowledge graphs. WWW. 2018:1771-1776.
28. Dasgupta SS, Ray SN, Talukdar P. HyTE: Hyperplane-based temporally aware knowledge graph embedding. EMNLP. 2018:2001-2011.
29. Lacroix T, Obozinski G, Usunier N. Tensor decompositions for temporal knowledge base completion. ICLR. 2020.
30. Pan S, et al. Unifying large language models and knowledge graphs: A roadmap. IEEE TKDE. 2024;36:3580-3599.

---

## Supplementary Materials

### Supplementary Table S1: Full v4 Model Training Logs
### Supplementary Table S2: v5.2 Training Convergence Curves
### Supplementary Table S3: Complete Domain-KG Statistics
### Supplementary Figure S1: PCA Projections of Drug Embeddings by Therapeutic Class
### Supplementary Figure S2: Training Loss Curves for All Configurations
### Supplementary Figure S3: Embedding Similarity Heat Maps for Top 50 Drugs

---

## Figure Legends

**Figure 1.** KGE model comparison on SexDiffKG v4. (A) MRR, Hits@1, Hits@3, Hits@5, Hits@10 for ComplEx, RotatE v4.1, and DistMult v4.1. (B) Rank distribution histograms for each model.

**Figure 2.** Scale effects: v4 to v5.2 merged graph. (A) MRR degradation for ComplEx and DistMult. (B) Hits@10 degradation comparison showing ComplEx's superior robustness. (C) AMRI preservation despite MRR drop.

**Figure 3.** Domain-specific extraction recovers performance. Bar chart of MRR for five domain KGs plus parent v4.1 and v5.2 baselines. Dashed line at parent DistMult v4.1 MRR (0.1013). Three domain KGs exceed this threshold.

**Figure 4.** Entity count vs. MRR for domain KGs. Scatter plot showing inverse correlation (rho = -0.90, p = 0.037). The ~20K entity inflection point is marked.

**Figure 5.** Embedding similarity vs. sex-differential safety divergence. Scatter plot of drug pair cosine similarity (x-axis) vs. sex-bias percentage-point difference (y-axis). Divergent pairs (high similarity, high sex-bias gap) are highlighted in red.
