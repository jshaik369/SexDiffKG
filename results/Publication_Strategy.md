# SexDiffKG — Master Publication Strategy

**Goal:** Global recognition for the first sex-differential drug safety knowledge graph  
**Author:** JShaik, CoEvolve Network, Barcelona  
**Created:** February 28, 2026  

---

## Phase 1: IMMEDIATE (March 2026)

### 1.1 bioRxiv Preprint
- **Category:** Pharmacology and Toxicology (secondary: Bioinformatics)
- **Status:** Ready to submit
- **Action:** Submit full study (SexDiffKG_Study_ISMB2026.md → formatted PDF)
- **Turnaround:** 2-3 days to online posting
- **Purpose:** Establish priority, get feedback, citable immediately

### 1.2 Bio-IT World Innovative Practices Award
- **Deadline:** March 2, 2026
- **Conference:** May 19-21, 2026, Boston
- **Action:** Submit application highlighting sovereign AI infrastructure + KG innovation
- **URL:** https://www.bio-itworld.com/award

---

## Phase 2: CONFERENCES (March-May 2026)

### 2.1 ISMB 2026 ★★★★★
- **Deadline:** April 9, 2026
- **Conference:** July 12-16, Washington DC
- **Format:** 250-word abstract + optional 2-page PDF
- **Status:** Abstract DRAFTED (ISMB2026_Abstract.md)
- **Submission type:** Talk/poster

### 2.2 BOSC 2026 (co-located with ISMB)
- **Deadline:** April 9, 2026
- **Conference:** July 14-15, Washington DC
- **Focus:** Open-source tools + reproducible research
- **Action:** Submit same abstract, emphasize open methodology

### 2.3 ASHG 2026
- **Deadline:** May 18, 2026
- **Conference:** October 20-24, Montréal
- **Focus:** 430 gene targets with sex-biased drug safety profiles
- **Angle:** Human genetics meets pharmacovigilance

### 2.4 NeurIPS 2026
- **Deadline:** May 15, 2026
- **Conference:** December 6-12, Sydney
- **Focus:** DistMult/RotatE embeddings, representation learning for drug safety
- **Angle:** ML methodology for heterogeneous biomedical KGs

### 2.5 ESWC 2026
- **Conference:** May 10-14, Dubrovnik
- **Focus:** Knowledge graph construction and embeddings
- **Check deadline:** Resources Track

### 2.6 KGC 2026
- **Conference:** May 4-8, Cornell Tech NYC
- **Focus:** Applied knowledge graphs
- **Check deadline**

---

## Phase 3: JOURNAL SUBMISSIONS (April-June 2026)

### Tier 1: Primary Target Journals

| Journal | IF | Focus | Article Type |
|---------|---:|-------|-------------|
| **Drug Safety** | 3.8 | Pharmacovigilance | Research article |
| **Biology of Sex Differences** | 5.1 | Sex/gender medicine | Research article |
| **Briefings in Bioinformatics** | 7.97 | Methods + applications | Research article |
| **Scientific Data** | 6.9 | Data descriptor | Data Descriptor |

**Strategy:** Submit simultaneously to non-overlapping audiences:
- Drug Safety → pharmacovigilance community
- Biology of Sex Differences → sex/gender medicine community  
- Scientific Data → database/resource users

### Tier 2: High-Impact Options

| Journal | IF | Why |
|---------|---:|-----|
| Nature Communications | 15.7 | Broad impact, precision medicine angle |
| Cell Systems | 7.7 | Systems pharmacology |
| Nucleic Acids Research | 16.4 | Database/resource paper |

### Tier 3: Solid Coverage

| Journal | IF | Why |
|---------|---:|-----|
| Pharmacoepidemiology and Drug Safety | 2.4 | ISPE official journal |
| Clinical Pharmacology & Therapeutics | 5.3 | Translational pharma |
| PLOS Computational Biology | 3.5 | Methods + open access |
| BMC Bioinformatics | 3.3 | Detailed methodology |
| Bioinformatics (OUP) | 5.6 | Core bioinformatics |
| GigaScience | 3.9 | Big data + biology |

---

## Phase 4: LATER CONFERENCES (August+ 2026)

| Conference | Dates | Location | Focus |
|-----------|-------|----------|-------|
| ECCB 2026 | Aug 31-Sep 4 | Geneva | European bioinformatics |
| ISPE 2026 | Aug 29-Sep 2 | Milan | Pharmacoepidemiology |
| ISoP 2026 | Oct-Nov | Costa Rica | Pharmacovigilance |
| ICKG 2026 | Nov 12-13 | Shenyang | Knowledge graphs |
| KDD 2026 | Aug 9-13 | Jeju, Korea | Data mining + KG |

---

## Venue-Specific Angles

### For Bioinformatics venues (ISMB, Bioinformatics, Briefings):
- KG construction from 5 heterogeneous sources
- DistMult/RotatE embedding methodology
- 127K nodes, 5.8M edges at scale
- Embedding-based drug clustering

### For Drug Safety venues (Drug Safety, ISPE, ISoP, DIA):
- 49,026 sex-differential safety signals from 14.5M FAERS reports
- Top drugs/AEs with extreme sex bias
- Regulatory implications for sex-stratified safety monitoring
- Actionable pharmacovigilance findings

### For Sex/Gender Medicine venues (Biology of Sex Differences, ASHG):
- 430 gene targets with sex-biased drug safety
- ESR1, HDAC, JAK1 findings
- Mechanistic hypotheses for sex-specific ADRs
- Precision medicine implications

### For KG/AI venues (KDD, NeurIPS, ESWC, KGC):
- Novel KG design for pharmacovigilance
- Multi-relational embedding in biomedical domain
- Link prediction for drug safety
- Scalable sex-differential signal detection

### For Data/Resource venues (Scientific Data, GigaScience, NAR):
- Complete reusable dataset: 127K nodes, 5.8M edges
- 49,026 curated sex-differential signals
- 430 gene targets with sex bias scores
- 29,201 drug embeddings + PCA coordinates

---

## Preprint Strategy

1. **bioRxiv** — Submit immediately under "Pharmacology and Toxicology"
2. **medRxiv** — Consider for clinical/regulatory angle version
3. **arXiv** — Consider cs.AI version emphasizing ML methodology

---

## Timeline

| Date | Action |
|------|--------|
| Mar 1 | Submit bioRxiv preprint |
| Mar 2 | Bio-IT World Award application |
| Mar 15 | Finalize ISMB abstract |
| Apr 9 | Submit ISMB 2026 + BOSC 2026 |
| Apr 15 | Submit to Drug Safety |
| Apr 30 | Submit to Biology of Sex Differences |
| May 15 | Submit NeurIPS / Check ESWC |
| May 18 | Submit ASHG abstract |
| Jun 1 | Submit Scientific Data (data descriptor) |
| Jul 12-16 | Present at ISMB, Washington DC |
| Sep-Nov | Present at ISPE, ISoP, ECCB |
| Dec 6-12 | Present at NeurIPS, Sydney |

---

## Infrastructure Note

All computation performed on sovereign local infrastructure:
- NVIDIA DGX Spark (Grace Blackwell GB10)
- 128GB unified memory, ARM64
- Zero cloud dependencies
- Full reproducibility on single-node setup
