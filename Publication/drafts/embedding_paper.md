# Knowledge Graph Embeddings Reveal Hidden Structure in Sex-Differential Drug Safety:
# Structurally Similar Drugs Can Have Dramatically Different Sex-Specific Risk Profiles

## Authors
Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)
CoEvolve Network, Independent Researcher, Barcelona, Spain
ORCID: 0009-0002-1748-7516

## Abstract
Knowledge graph embeddings encode complex relational structures into continuous vector spaces, enabling similarity computation between drugs, adverse events, and biological targets. Using RotatE embeddings (MRR = 0.2018) from SexDiffKG — a knowledge graph integrating 14.5M FAERS reports with molecular interaction data — we demonstrate that embedding similarity captures meaningful pharmacological relationships yet reveals striking divergences in sex-differential safety profiles. Among the top 200 drugs by signal volume, we identify 10 drug pairs with embedding cosine similarity >0.93 yet sex-bias differences exceeding 30 percentage points. The most dramatic example is Risperidone (93% female-biased signals) versus Olanzapine (59% female-biased, cosine = 0.947). Drug clustering based on RotatE embeddings yields 5 clusters with distinct sex profiles: an oncology-enriched cluster (62.7%F) and a mixed-indication cluster (36.3%F). Adverse event embeddings cluster into 10 groups with sex bias ranging from 31.3%F (injection/pain-related) to 62.9%F (malignancy-related). These findings demonstrate that while KG embeddings effectively capture therapeutic similarity, sex-differential safety profiles require explicit modeling beyond standard structural features.

## Key Findings
1. RotatE embeddings: 113,155 entities, 512 dimensions (256 complex)
2. All 3,920 drugs and 9,949 AEs represented in embedding space
3. Drug PCA: PC1 explains 6.8% variance, PC2 explains 4.1%
4. Divergent pairs: Risperidone/Olanzapine (cos=0.947, 34pp sex difference)
5. Convergent pairs: Leflunomide/Sulfasalazine (cos=0.953, 5pp sex difference)
6. Drug cluster sex range: 36.3%F to 62.7%F across 5 clusters
7. AE cluster sex range: 31.3%F to 62.9%F across 10 clusters
