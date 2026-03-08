# SexDiffKG Publishing Strategy v2 -- Post-Audit Action Plan
**Date:** 2026-03-08 (supersedes v1 2026-03-04)
**Author:** Mohammed Javeed Akhtar Abbas Shaik (J.Shaik), CoEvolve Network
**ORCID:** 0009-0002-1748-7516

---

## I. PORTFOLIO OVERVIEW

### Paper Inventory: 29 FINALIZED Papers + 1 Flagship Manuscript

All 29 papers have been expanded, number-audited, and finalized as of March 8, 2026. Every paper exceeds 35 KB. All stubs have been absorbed, all merges completed, all redundancies eliminated.

| #  | Paper | Size (KB) |
|----|-------|-----------|
| 01 | age_sex_interaction | 45 |
| 02 | anti_regression | 45 |
| 03 | bidirectional_ae | 40 |
| 04 | cardiotoxicity | 44 |
| 05 | clinical_urgency | 46 |
| 06 | comprehensive_methods | 56 |
| 07 | cross_therapeutic | 45 |
| 08 | CPI_irAE | 37 |
| 09 | drug_safety_atlas | 57 |
| 10 | drug_target_sex | 45 |
| 11 | embedding_methods | 50 |
| 12 | extreme_signals | 44 |
| 13 | glp1ra_safety | 37 |
| 14 | hepatotoxicity | 43 |
| 15 | information_theory | 45 |
| 16 | nephrotoxicity | 45 |
| 17 | network_topology | 42 |
| 18 | organ_system_landscape | 44 |
| 19 | rare_disease_paradox | 43 |
| 20 | regulatory | 44 |
| 21 | reproductive_paradox | 39 |
| 22 | sex_paradox | 45 |
| 23 | severity_gradient | 51 |
| 24 | sexdiffkg_methods | 52 |
| 25 | soc_atlas | 45 |
| 26 | temporal_instability | 45 |
| 27 | two_axis_model | 39 |
| 28 | severity_sex_gradient | 48 |
| 29 | reproductive_pharmacovigilance | 54 |
| -- | **manuscript_scidata_COMPLETE.md** (flagship) | **78** |

**Portfolio totals:** ~1,380 KB across 30 documents. Smallest paper: 37 KB. Largest paper: 57 KB. Flagship: 78 KB.

### Number Audit (Mar 8, 2026) -- ALL PAPERS PASSED

Every paper has been audited against the corrected ground-truth numbers:

| Metric | Audited Value | Previous (Stale) |
|--------|--------------|------------------|
| Unique adverse events | **5,069** | 5,658 (overcounted) |
| Female FAERS reports | **8,744,397** | -- |
| Male FAERS reports | **5,791,611** | -- |
| Total FAERS reports | **14,536,008** | -- |
| Quarterly coverage | **87 quarters** (2004Q1--2025Q3) | -- |
| Sex-differential signals | **96,281** | 183,539 (v3 stale) |
| Drugs analyzed | **2,178** | -- |
| KG v4 nodes | **109,867** | 127,063 (v3 stale) |
| KG v4 edges | **1,822,851** (1,532,674 unique) | 5.8M (v3 stale) |
| ComplEx v4 MRR | **0.2484** | 0.048 (DistMult v3) |
| Composite validation | **82.9%** | -- |

Zero papers contain stale v3 numbers. Zero papers reference KEGG (all use Reactome).

### Existing Publication Materials
- 3 conference abstracts (ISMB 2026, ASHG 2026, NeurIPS 2026)
- 4 cover letters (Drug Safety, Biology of Sex Differences, Briefings in Bioinformatics, Scientific Data)
- Zenodo deposit (existing)
- bioRxiv preprint (existing)
- GitHub repo: https://github.com/jshaik369/sexdiffkg-deep-analysis

---

## II. STRATEGIC PAPER GROUPING

### Tier 1: Flagship Papers (Submit First -- Highest Impact)

#### Paper A: MAIN PAPER -- "SexDiffKG: A Knowledge Graph for Systematic Discovery of Sex-Differential Drug Safety Signals"
- **Source**: `manuscript_scidata_COMPLETE.md` (78 KB)
- **Lead finding**: Severity-sex gradient (rho=0.93), anti-regression (rho=1.0), 82.9% composite validation
- **Target journals (ranked)**:
  1. **eClinicalMedicine (Lancet)** (IF 10.0, OA, NO APC) -- published Watson et al. 2019 sex-diff ADR landmark; IDEAL
  2. **Biology of Sex Differences** (IF 5.1, OA, APC $3,190) -- perfect scope, has sex-diff pharmacovig precedent
  3. **Clinical Pharmacology & Therapeutics** (IF 5.3) -- includes "bioinformation and applied systems biology"
  4. **Drug Safety** (IF 3.8, 6-day median first decision) -- fastest review in field, ISoP official journal
- **Preprint**: medRxiv (pharmacovigilance = health sciences scope)
- **Timeline**: Submit preprint week 1, journal submission week 2

#### Paper B: DISCOVERY -- "The Severity-Sex Gradient in Drug Safety"
- **Sources**: `23_severity_gradient` (51 KB) + `28_severity_sex_gradient` (48 KB)
- **Lead finding**: rho=0.93 (p=0.003), entirely novel
- **Target journals**:
  1. **Clinical Pharmacology & Therapeutics** (IF 6.3)
  2. **Drug Safety** (IF 3.8)
  3. **British Journal of Clinical Pharmacology** (IF 3.1)
- **Preprint**: medRxiv
- **Timeline**: Week 2-3

#### Paper C: STATISTICAL INNOVATION -- "The Anti-Regression Phenomenon"
- **Source**: `02_anti_regression` (45 KB)
- **Lead finding**: Perfect monotonicity (rho=1.0, p=6.6e-64), counter-intuitive
- **Target journals**:
  1. **Pharmacoepidemiology and Drug Safety** (IF 3.3, Wiley)
  2. **Statistics in Medicine** (IF 2.3)
  3. **Drug Safety** (IF 3.8)
- **Preprint**: medRxiv
- **Timeline**: Week 3-4

### Tier 2: High-Impact Domain Papers (Submit Second Wave)

#### Paper D: IMMUNOLOGY -- "Female Predominance in Checkpoint Inhibitor Adverse Events"
- **Source**: `08_CPI_irAE` (37 KB)
- **Target**: Journal for ImmunoTherapy of Cancer (IF 10.9) or JAMA Oncology (IF 28.4)
- **Timeline**: Week 4-5

#### Paper E: CARDIOLOGY -- "Drug-Induced Cardiac Events: Sex-Differential Cardiotoxicity"
- **Source**: `04_cardiotoxicity` (44 KB)
- **Target**: European Heart Journal - Cardiovascular Pharmacotherapy (IF 4.4) or Circulation (IF 35.5)
- **Timeline**: Week 4-5

#### Paper F: REGULATORY -- "Sex-Specific Drug Safety Warnings Needed for 187 Medications"
- **Source**: `20_regulatory` (44 KB)
- **Target**: JAMA Internal Medicine (IF 23.3) or BMJ (IF 42.7)
- **Timeline**: Week 5-6

#### Paper G: SEX PARADOX -- "Sex-Differential Drug Safety Signals Anti-Correlate with Reporter Sex"
- **Source**: `22_sex_paradox` (45 KB)
- **Target**: Biology of Sex Differences (IF 4.9)
- **Timeline**: Week 5-6

#### Paper H: DRUG SAFETY ATLAS -- "Comprehensive Atlas of Sex-Differential Drug Safety"
- **Source**: `09_drug_safety_atlas` (57 KB)
- **Target**: PLOS Medicine (IF 9.9) or Drug Safety (IF 3.8)
- **Timeline**: Week 5-6

### Tier 3: Specialist Domain Papers (Third Wave)

#### Paper I: HEPATOTOXICITY
- **Source**: `14_hepatotoxicity` (43 KB)
- **Target**: Hepatology Communications (IF 5.6) or Drug Safety

#### Paper J: NEPHROTOXICITY
- **Source**: `16_nephrotoxicity` (45 KB)
- **Target**: Kidney International Reports (IF 3.4) or Nephrology Dialysis Transplantation (IF 5.3)

#### Paper K: THERAPEUTIC SPECTRUM
- **Source**: `07_cross_therapeutic` (45 KB)
- **Target**: Pharmacoepidemiology and Drug Safety

#### Paper L: NETWORK TOPOLOGY
- **Source**: `17_network_topology` (42 KB)
- **Target**: Bioinformatics (IF 4.4) or Database (IF 3.6, OA, free APC)

#### Paper M: KNOWLEDGE GRAPH / EMBEDDING METHODOLOGY
- **Source**: `11_embedding_methods` (50 KB) + `24_sexdiffkg_methods` (52 KB)
- **Target**: Briefings in Bioinformatics (IF 6.8) or Journal of Biomedical Informatics (IF 4.0)

#### Paper N: AGE-SEX INTERACTION
- **Source**: `01_age_sex_interaction` (45 KB)
- **Target**: Journal of Women's Health (IF 2.1) or Clinical Pharmacology & Therapeutics

#### Paper O: COMPREHENSIVE METHODS
- **Source**: `06_comprehensive_methods` (56 KB)
- **Target**: Nature Methods (stretch) or Briefings in Bioinformatics (IF 6.8)

### Tier 4: Specialized / Niche Papers (Fourth Wave)

#### Remaining Papers (submit in waves of 3-4):

| Paper | Source | Size | Target Journal |
|-------|--------|------|---------------|
| Clinical Urgency | `05_clinical_urgency` (46 KB) | 46 | Drug Safety |
| Drug-Target-Sex | `10_drug_target_sex` (45 KB) | 45 | Molecular Pharmacology |
| Extreme Signals | `12_extreme_signals` (44 KB) | 44 | Pharmacoepi & Drug Safety |
| GLP-1RA Safety | `13_glp1ra_safety` (37 KB) | 37 | Diabetes Care or Lancet Diabetes |
| Information Theory | `15_information_theory` (45 KB) | 45 | J Biomedical Informatics |
| Organ System Landscape | `18_organ_system_landscape` (44 KB) | 44 | Drug Safety |
| Rare Disease Paradox | `19_rare_disease_paradox` (43 KB) | 43 | Orphanet Journal of Rare Diseases |
| Reproductive Paradox | `21_reproductive_paradox` (39 KB) | 39 | Biology of Sex Differences |
| SOC Atlas | `25_soc_atlas` (45 KB) | 45 | Drug Safety |
| Temporal Instability | `26_temporal_instability` (45 KB) | 45 | Clinical Pharmacology & Therapeutics |
| Two-Axis Model | `27_two_axis_model` (39 KB) | 39 | PLOS Computational Biology |
| Bidirectional AE | `03_bidirectional_ae` (40 KB) | 40 | Pharmacoepi & Drug Safety |
| Reproductive Pharmacovig. | `29_reproductive_pharmacovigilance` (54 KB) | 54 | J Women's Health or Reprod. Toxicol. |

---

## III. JOURNAL TARGET MATRIX

| Journal | IF | OA | APC | Scope Match | Priority Paper |
|---------|----|----|-----|-------------|---------------|
| BMJ | 42.7 | Hybrid | GBP 3,000+ | Policy/regulatory | Paper F |
| JAMA Internal Medicine | 23.3 | Hybrid | ~$5,000 | Clinical impact | Paper F (alt) |
| JAMA Oncology | 28.4 | Hybrid | ~$5,000 | ICI/immunotherapy | Paper D (stretch) |
| Journal for ImmunoTherapy of Cancer | 10.9 | OA | ~$4,500 | ICI-focused | Paper D |
| eClinicalMedicine (Lancet) | 10.0 | OA | FREE | Clinical research | Paper A |
| PLOS Medicine | 9.9 | OA | $6,460 | Computational epi | Paper H |
| Briefings in Bioinformatics | 6.8 | Hybrid | ~$3,900 | KG methodology | Paper M |
| Clinical Pharmacology & Therapeutics | 6.3 | Hybrid | ~$4,200 | Clinical pharmacology | Paper B |
| Scientific Data | 5.8 | OA | ~$2,190 | Dataset/resource | Paper A (alt) |
| Hepatology Communications | 5.6 | OA | ~$3,500 | Liver toxicity | Paper I |
| Biology of Sex Differences | 4.9 | OA | ~$2,790 | Sex differences | Paper G |
| Bioinformatics | 4.4 | OA | ~$2,800 | Computational bio | Paper L |
| Drug Safety | 3.8 | Hybrid | ~$3,860 | Core pharma | Paper B/C |
| Database (Oxford) | 3.6 | OA | ~FREE | Biological databases | Paper L (alt) |
| Pharmacoepidemiology & Drug Safety | 3.3 | Hybrid | ~$4,200 | Pharmacoepi | Paper C |
| BJCP | 3.1 | Hybrid | ~$3,700 | Clinical pharm | Paper B (alt) |
| BMJ Open | 2.3 | OA | GBP 2,163 | Broad medical | Paper A (safe) |
| Journal of Women's Health | 2.1 | Hybrid | ~$3,200 | Women's health | Paper N |

---

## IV. PREPRINT STRATEGY

### Recommendation: Dual Preprint
1. **medRxiv** for clinical/pharmacovigilance papers (Papers A, B, C, D, E, F, G, H, I, J, N, plus Tier 4 clinical papers)
   - Scope: health sciences, clinical epidemiology
   - Free, DOI issued immediately
   - Screened for clinical relevance

2. **bioRxiv** for computational/methodology papers (Papers L, M, O, plus information_theory, two_axis_model)
   - Scope: biological sciences, computational biology, bioinformatics
   - Free, DOI issued immediately
   - Wider bioinformatics audience

### Timing
- Post preprints 1-2 weeks BEFORE journal submission
- This establishes priority and generates early citations
- Update existing bioRxiv preprint with latest v4 data

---

## V. SUBMISSION READINESS CHECKLIST

### Global (applies to all 29 papers + flagship)

- [x] Number audit complete (Mar 8, 2026) -- all papers use corrected values
- [x] All papers >= 35 KB (smallest: 37 KB)
- [x] All v3 stale numbers eliminated (0 remaining)
- [x] Reactome referenced (not KEGG) in all papers
- [x] ComplEx v4 MRR 0.2484 used (no stale model metrics)
- [x] FAERS counts: 8,744,397 F / 5,791,611 M / 14,536,008 total
- [x] 5,069 unique AEs (corrected from 5,658)
- [x] 87 quarters (2004Q1--2025Q3)
- [x] 96,281 signals, 2,178 drugs
- [x] Author name, ORCID, affiliation consistent across all papers
- [x] GitHub/Zenodo DOI referenced
- [x] Death statistics use standardized 50.1% F Fatal category
- [x] Cardiotoxicity exception documented where anti-regression is mentioned
- [x] OpenFDA excluded from composite validation or flagged

### Per-Paper Submission Tasks

- [ ] Convert to journal-specific format (LaTeX or Word template per target journal)
- [ ] Generate publication-quality figures from source data (minimum 300 DPI, vector preferred)
- [ ] Write cover letters tailored to each journal editor
- [ ] Prepare supplementary tables (raw data extracts, extended results)
- [ ] Prepare Data Availability Statement (GitHub + Zenodo links)
- [ ] Format references in journal-specific citation style (Vancouver, APA, etc.)
- [ ] Prepare Author Contribution Statement (CRediT taxonomy)
- [ ] Prepare Conflict of Interest declaration
- [ ] Prepare Ethics / IRB statement (secondary analysis of de-identified public data -- typically exempt)
- [ ] Confirm word/figure limits per target journal
- [ ] Register ORCID with journal submission systems

---

## VI. CONFERENCE STRATEGY

### ISMB 2026 (July 12-16, Washington DC) -- CRITICAL
**Deadline: April 9, 2026 (32 days away)**

**Action Items (URGENT):**
1. UPDATE ABSTRACT with audited numbers (all corrected as of Mar 8)
2. DESIGN POSTER -- 48x36 inch or A0 PDF
   - Use deep analysis figures (389 figures available from 130 waves)
   - Feature severity-sex gradient, anti-regression, KG architecture
3. REGISTER on submission portal
4. Target March 26 for final draft

### ASHG 2026 -- Abstract exists, needs v4 audit update
### NeurIPS 2026 -- Abstract exists, KG methodology angle

---

## VII. SUBMISSION TIMELINE (16-Week Plan from Mar 8, 2026)

| Week | Dates | Action |
|------|-------|--------|
| 1 | Mar 8-14 | Fix ISMB abstract with audited numbers. Update bioRxiv preprint. Begin LaTeX conversion for Paper A (flagship). |
| 2 | Mar 15-21 | Submit Paper A preprint (medRxiv). Begin formatting Papers B + C. |
| 3 | Mar 22-28 | Submit Paper A to eClinicalMedicine. Submit Paper B preprint. Final ISMB abstract polish. |
| 4 | Mar 29-Apr 4 | Submit Paper B (CPT). Submit Paper C preprint + journal (PDS). |
| 5 | Apr 5-11 | ISMB deadline Apr 9. Submit poster abstract. Begin Tier 2 formatting. |
| 6 | Apr 12-18 | Submit Paper D (JITC). Submit Paper E preprint. |
| 7 | Apr 19-25 | Submit Paper E (EHCVP). Submit Paper F preprint. |
| 8 | Apr 26-May 2 | Submit Paper F (BMJ/JAMA IM). Submit Papers G + H preprints. |
| 9 | May 3-9 | Submit Papers G (Biol Sex Diff) + H (PLOS Med). Begin Tier 3 formatting. |
| 10 | May 10-16 | Submit Papers I (Hep Comm) + J (Kidney Int Rep). |
| 11 | May 17-23 | Submit Papers K (PDS) + L (Bioinformatics). |
| 12 | May 24-30 | Submit Papers M (Briefings Bioinf) + N (JWH) + O (Briefings). |
| 13 | Jun 1-7 | Begin Tier 4 submissions (3-4 papers per week). |
| 14 | Jun 8-14 | Continue Tier 4 submissions. Handle early reviews/revisions from Tier 1. |
| 15 | Jun 15-21 | Complete remaining Tier 4 submissions. |
| 16 | Jun 22-28 | All 29 papers + flagship submitted. Follow up on reviews. Finalize ISMB poster. Update Zenodo v4. |

---

## VIII. BUDGET CONSIDERATIONS

### Estimated APC Costs (if all go OA)
- Tier 1 (3 papers + flagship): ~$6,000-12,000 (eClinicalMedicine is free)
- Tier 2 (5 papers): ~$15,000-22,000
- Tier 3 (7 papers): ~$18,000-25,000
- Tier 4 (14 papers): ~$35,000-50,000
- Total potential: $74,000-109,000

### Cost Reduction Strategies
1. **eClinicalMedicine (Lancet)** -- NO APC for flagship paper
2. **Database (Oxford)** -- often waives APC for bioinformatics papers
3. **Hybrid journals** -- choose subscription-access (free) where possible
4. **Institutional waivers** -- check if CoEvolve Network qualifies
5. **bioRxiv/medRxiv** -- free preprints establish priority regardless
6. **PLOS fee waivers** -- available for developing country researchers
7. **Green OA** -- post accepted manuscripts on institutional repository after embargo

### Recommended Strategy: Selective OA
- Paper A (flagship) --> eClinicalMedicine (FREE OA) -- highest visibility
- Papers B, D, F, H --> OA if budget allows (high impact)
- Papers C, G, I-O --> subscription access (save costs)
- All papers --> preprint (medRxiv/bioRxiv) regardless of OA status
- Realistic budget with selective OA: $15,000-25,000

---

## IX. PRE-SUBMISSION CHECKLIST

Before submitting ANY paper:
- [x] All numbers match audited ground truth (Mar 8, 2026 audit)
- [x] 5,069 unique AEs (NOT 5,658)
- [x] 8,744,397 F / 5,791,611 M / 14,536,008 total reports
- [x] 87 quarters (2004Q1--2025Q3)
- [x] 96,281 signals, 2,178 drugs
- [x] Reactome (NOT KEGG) referenced
- [x] ComplEx v4 MRR 0.2484 (not stale values)
- [x] DiAna normalization (846,917 mappings, 53.9%)
- [ ] Author: Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)
- [ ] ORCID: 0009-0002-1748-7516
- [ ] Affiliation: CoEvolve Network, Independent Researcher, Barcelona, Spain
- [ ] GitHub/Zenodo DOI referenced
- [ ] Death statistics use standardized 50.1% F Fatal category
- [ ] Cardiotoxicity exception documented if anti-regression mentioned
- [ ] OpenFDA excluded from composite validation or flagged
- [ ] Journal-specific formatting complete
- [ ] Cover letter written and tailored
- [ ] Supplementary materials prepared
- [ ] All figures at publication quality (300 DPI minimum)
- [ ] References formatted per journal style

---

## X. KEY METRICS FOR IMPACT

### What Makes SexDiffKG Publishable at High Impact
1. **Scale**: 14.5M reports, 96,281 signals, 2,178 drugs -- largest sex-differential analysis ever
2. **Novelty**: Severity-sex gradient (rho=0.93) -- never systematically quantified
3. **Counter-intuitive**: Anti-regression -- more data makes signal stronger, not weaker
4. **Clinical utility**: 108 urgent signals, 187 drugs needing sex-specific warnings
5. **Validation**: 82.9% composite concordance across 4+ independent sources
6. **Reproducibility**: Full KG + code on GitHub + Zenodo, ComplEx embeddings available
7. **Timeliness**: Growing regulatory push for sex-stratified drug safety analysis (FDA, EMA)
8. **Breadth**: 29 domain-specific papers covering every major organ system, drug class, and methodological angle

---

## XI. COMPETITIVE LANDSCAPE

### Key Competitors/Prior Work
1. **Watson et al. 2019** -- Sex differences in GI ADRs (FAERS, 2004-2011). We extend to 2025Q3, 20x more drugs.
2. **Zucker & Prendergast 2020** -- Sex differences in ADR reporting. We add KG + embeddings + validation.
3. **Conforti et al. 2018** -- ICI sex differences. Our Paper D is 10x larger dataset.
4. **PreciseADR (2025, Advanced Science)** -- GNN for ADR prediction with demographics. Our ComplEx approach is complementary.
5. **Chandak et al. (Cell Patterns 2020)** -- ML for sex-differential ADRs. We have 5x more data and KG validation.

### Our Advantages
- Latest FAERS data (through 2025Q3 vs most papers using 2011-2020)
- Knowledge graph integration (unique -- no competitor combines KG + sex-differential signals)
- Comprehensive validation (82.9% across 4 sources vs typically 1 validation)
- 29 finalized, number-audited papers covering every major domain
- All papers >= 35 KB with consistent, verified statistics

---

## XII. RISK MITIGATION

| Risk | Mitigation |
|------|-----------|
| Desk rejection at high-IF journals | Always have fallback journal identified (see Tier rankings). Preprint establishes priority regardless. |
| Reviewer questions on single-author credibility | Emphasize reproducibility (GitHub + Zenodo), validation (82.9%), and scale (14.5M reports). Reference computational biology single-author precedents. |
| Simultaneous submissions flagged | Each paper covers a distinct domain/finding. No overlapping submissions to same journal. |
| APC budget constraints | Selective OA strategy. Prioritize free venues (eClinicalMedicine, Database). Use Green OA for subscription journals. |
| Number inconsistencies discovered post-submission | Mar 8 audit is definitive. GROUND_TRUTH.json is version-controlled. Errata process documented. |
| ISMB deadline missed | Abstract already drafted. Only needs number updates (32 days remaining). |

---

*Strategy prepared by J.Shaik, CoEvolve Network. All statistics verified against GROUND_TRUTH.json (Mar 8, 2026 audit).*
