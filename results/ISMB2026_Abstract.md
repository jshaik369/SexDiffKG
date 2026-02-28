# ISMB 2026 Abstract Submission

**Submission Type:** Talk/Poster  
**Deadline:** April 9, 2026  
**Conference:** July 12-16, 2026, Washington, DC, USA  

---

## Title

SexDiffKG: A Sex-Differential Drug Safety Knowledge Graph from 14.5 Million FDA Adverse Event Reports

## Authors

JShaik¹

## Affiliations

¹CoEvolve Network, Independent Researcher, Barcelona, Spain

## Abstract (250 words)

Sex-based differences in adverse drug reactions remain poorly systematized despite women experiencing ADRs at 1.5–1.7× the rate of men. We present SexDiffKG, a purpose-built knowledge graph integrating 14,536,008 FDA Adverse Event Reporting System (FAERS) reports (F: 8,744,397; M: 5,791,611) with drug–target data from ChEMBL 36, protein interactions from STRING v12, and pathway annotations from KEGG. The resulting graph contains 127,063 nodes across 6 entity types (Gene, Drug, AdverseEvent, Protein, Pathway, Tissue) and 5,839,717 edges across 6 relation types.

Through sex-stratified Reporting Odds Ratio analysis, we identified 183,544 sex-differential drug–adverse event signals, of which 49,026 are strong (>2.7× ratio, ≥10 reports per sex), with 58.5% showing female bias. DistMult knowledge graph embeddings (200d, 100 epochs) achieved MRR 0.048 and AMRI 0.981 on link prediction, demonstrating meaningful structural learning across the heterogeneous graph.

Embedding-based analysis revealed three key findings: (1) K-Means clustering of 29,201 drug embeddings into 20 groups identified clusters with distinct sex-differential safety profiles; (2) bridging FAERS signals to ChEMBL targets identified 429 gene targets with sex-biased drug safety patterns; (3) biologically coherent sex-differential targets emerged, including HDAC1/2/3/6 (female-biased), ESR1 (male-biased, score −0.80), nicotinic receptor subunits (female-biased), and JAK1 (male-biased), providing mechanistic hypotheses for sex-specific pharmacovigilance.

SexDiffKG is the first knowledge graph designed for sex-differential drug safety analysis at scale, offering a computational foundation for precision pharmacovigilance. All data was processed on sovereign local infrastructure (NVIDIA GB10, ARM64).

## Keywords

pharmacovigilance, sex differences, knowledge graph, FAERS, drug safety, graph embeddings

## Contact

jshaik@coevolvenetwork.com
