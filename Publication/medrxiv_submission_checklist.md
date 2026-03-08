# medRxiv Preprint Submission Checklist

**Manuscript:** SexDiffKG: A Knowledge Graph for Sex-Differential Drug Safety
**Author:** Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)
**Target server:** medRxiv (https://submit.medrxiv.org/)

---

## 1. Manuscript Format Requirements

### General Format
- [ ] medRxiv does NOT enforce a specific journal style. Use a clean, readable format.
- [ ] No strict word limit imposed by medRxiv; however, keep the main text under ~8,000 words for readability and downstream journal compatibility.
- [ ] No strict figure limit; include all figures needed but keep total PDF under 40 MB.
- [ ] Number all pages consecutively.
- [ ] Use line numbering (continuous, not per-page) to facilitate reviewer/reader comments.
- [ ] Double-space the manuscript text.

### Required Sections (in order)
- [ ] **Title page** — title, author name(s), affiliation(s), corresponding author email, ORCID
- [ ] **Abstract** — structured or unstructured; recommend structured (Background, Methods, Results, Conclusions); keep under 350 words for downstream compatibility
- [ ] **Introduction**
- [ ] **Methods**
- [ ] **Results**
- [ ] **Discussion**
- [ ] **Conclusions** (can be final subsection of Discussion)
- [ ] **Data Availability Statement** (mandatory; see Section 4)
- [ ] **Competing Interests Statement** (mandatory; see Section 5)
- [ ] **Ethics Statement** (mandatory; see Section 6)
- [ ] **Funding Statement**
- [ ] **Acknowledgments**
- [ ] **References**
- [ ] **Figure Legends** (if figures not embedded inline)
- [ ] **Tables** (embedded or at end of manuscript)

### Pharmacovigilance-Specific Sections to Include
- [ ] FAERS data extraction methodology (date range, versions, inclusion/exclusion criteria)
- [ ] Signal detection methodology (disproportionality analysis: PRR, ROR, EBGM, or other)
- [ ] Sex stratification methodology
- [ ] KG construction pipeline description
- [ ] Validation methodology and benchmarking approach
- [ ] Limitations section explicitly addressing FAERS reporting biases

---

## 2. Required Files

### Manuscript File
- [ ] **Single PDF** (simplest and recommended) containing all text, figures, and tables
  - OR individual text file (Word or PDF) plus separate figure files
  - TeX/LaTeX users: convert to PDF before submission
- [ ] PDF file size under **40 MB**
- [ ] All figures embedded at appropriate locations in text, OR appended at end with clear legends
- [ ] All tables embedded or appended

### Figure Files (if submitting separately)
- [ ] Accepted formats: **TIFF, EPS, JPEG, GIF**
- [ ] Resolution: minimum 300 DPI for photographs, 600 DPI for line art
- [ ] Figures numbered sequentially (Figure 1, Figure 2, etc.)
- [ ] Each figure has a descriptive legend/caption

### Supplementary Material Files
- [ ] Supplementary tables (e.g., full signal lists, edge type distributions) as separate files
- [ ] Supplementary figures as separate files
- [ ] Supplementary methods (KG construction details, embedding hyperparameters) if too lengthy for main text
- [ ] Large datasets deposited in external repository (Zenodo, GitHub), NOT uploaded as supplementary files
- [ ] Supplementary files clearly labeled (Supplementary Table S1, Supplementary Figure S1, etc.)

### Recommended Supplementary Materials for This Manuscript
- [ ] Full list of 96,281 sex-differential signals (as downloadable table or Zenodo deposit)
- [ ] KG schema diagram showing all 16 node types and edge types
- [ ] Complete validation results against 40 literature benchmarks
- [ ] Embedding model hyperparameters and training curves
- [ ] Code availability documentation (link to GitHub repository)

---

## 3. Metadata (Entered in Submission System)

### Author Information
- [ ] **Full name:** Mohammed Javeed Akhtar Abbas Shaik
- [ ] **Display name / short form:** J. Shaik (confirm how name should appear)
- [ ] **ORCID iD:** 0009-0002-1748-7516 (link and verify at https://orcid.org/0009-0002-1748-7516)
- [ ] **Email address:** corresponding author email (must be valid and monitored)
- [ ] **Affiliation:** CoEvolve Network, Independent Researcher, Barcelona, Spain

### Submission Metadata
- [ ] **Title:** SexDiffKG: A Knowledge Graph for Sex-Differential Drug Safety
- [ ] **Subject area:** Select **Pharmacology and Therapeutics** (primary recommendation)
  - Alternative: Public and Global Health; or Health Informatics
  - Note: only ONE subject area can be selected per submission
- [ ] **Abstract:** paste into submission form (will also be in the PDF)
- [ ] **Keywords/tags:** sex differences, pharmacovigilance, knowledge graph, drug safety, FAERS, adverse drug reactions, disproportionality analysis, graph embedding

### Funding Statement
- [ ] Declare all funding sources that supported the work
- [ ] If unfunded / self-funded: "This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors."
- [ ] Must explicitly acknowledge whether any payments or services were received from third parties in the past 36 months

---

## 4. Data Availability Statement

Use the following template (adapt as needed):

> **Data Availability Statement**
>
> The FDA Adverse Event Reporting System (FAERS) data used in this study are publicly available from the U.S. Food and Drug Administration (https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html). The SexDiffKG knowledge graph, including all nodes, edges, and metadata files, is available on GitHub at https://github.com/jshaik369/SexDiffKG. The complete dataset, embeddings, and supplementary materials are archived on Zenodo (DOI: [insert Zenodo DOI upon deposit]). All code for KG construction, signal detection, and analysis is provided in the GitHub repository under an open-source license.

### Checklist for Data Availability
- [ ] FAERS source URL included
- [ ] GitHub repository URL included and repository is PUBLIC
- [ ] Zenodo DOI obtained and included (or marked as "pending; will be available upon publication")
- [ ] License specified for code (e.g., MIT, Apache 2.0) and data (e.g., CC-BY 4.0)
- [ ] All external data dependencies documented (DrugBank, MeSH, ATC, etc.)
- [ ] Repository contains README with reproduction instructions

---

## 5. Competing Interests Statement

Use the following template:

> **Competing Interests**
>
> The author declares no competing interests. No payments or services were received from any third party in the past 36 months that could be perceived to influence, or give the appearance of potentially influencing, the submitted work.

### Checklist for Competing Interests
- [ ] Statement covers the 36-month lookback period required by medRxiv
- [ ] Explicitly addresses payments, services, or relationships with third parties
- [ ] If any potential conflicts exist (e.g., consulting, advisory roles, equity holdings), disclose them fully
- [ ] Statement is included both in the manuscript AND in the submission form

---

## 6. Ethics Statement

### Why IRB Approval Is Not Required
FAERS data qualifies for IRB exemption because:
1. **Publicly available data:** FAERS quarterly data files are freely downloadable from the FDA's public website (https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html) without any data use agreement or access restrictions.
2. **Fully deidentified:** FAERS data are stripped of all personally identifiable information (names, dates of birth, etc.) before public release by the FDA. Individual reporters and patients cannot be identified.
3. **Not human subjects research:** Under 45 CFR 46.102, analysis of deidentified, publicly available data does not constitute "human subjects research" and therefore does not require IRB review.
4. **Regulatory precedent:** Hundreds of published FAERS-based pharmacovigilance studies on medRxiv and in peer-reviewed journals use this same exemption.

### Ethics Statement Template

> **Ethics Statement**
>
> This study is a secondary analysis of the FDA Adverse Event Reporting System (FAERS), a publicly available, deidentified database maintained by the U.S. Food and Drug Administration. As the study exclusively used publicly available, anonymized data with no possibility of identifying individual patients, it does not constitute human subjects research as defined by 45 CFR 46.102. Institutional review board (IRB) approval and informed consent were therefore not required. This determination is consistent with standard practice for FAERS-based pharmacovigilance research.

### Ethics Checklist
- [ ] Ethics statement is included in the manuscript (typically in Methods section)
- [ ] Statement explains WHY IRB was not needed (not just that it was not obtained)
- [ ] References the deidentified and public nature of FAERS data
- [ ] Cites 45 CFR 46.102 or equivalent regulatory framework
- [ ] Statement is consistent with medRxiv's screening expectations
- [ ] During submission, select the appropriate ethics oversight checkbox (medRxiv provides an option for studies using publicly available data)

---

## 7. Pre-Submission Checks for Pharmacovigilance Papers

### FAERS-Specific Methodology Checks
- [ ] FAERS data version and date range clearly stated (2004-2025, quarterly files)
- [ ] Number of total reports stated (14.5M)
- [ ] Deduplication method described (FDA's recommended CASEID-based or other method)
- [ ] Drug name standardization method described (mapping to generic names, ATC codes)
- [ ] Adverse event coding system identified (MedDRA Preferred Terms, System Organ Classes)
- [ ] Sex classification criteria stated (how male/female were determined from FAERS fields)
- [ ] Handling of missing sex data described
- [ ] Disproportionality measures defined with formulas (PRR, ROR, IC, EBGM, or custom metrics)
- [ ] Thresholds for signal detection clearly stated
- [ ] Multiple testing correction addressed

### Knowledge Graph-Specific Checks
- [ ] Node types and counts provided (109,867 nodes across X types)
- [ ] Edge types and counts provided (1,822,851 edges across X types)
- [ ] Data sources for each node/edge type documented
- [ ] KG construction pipeline reproducible from code
- [ ] Graph statistics reported (density, connected components, degree distribution)
- [ ] Embedding model and hyperparameters documented
- [ ] Train/validation/test split described
- [ ] Evaluation metrics defined (MRR, Hits@k, AMRI)

### Validation Checks
- [ ] 82.8% directional precision claim is clearly defined (what does "directional precision" mean operationally?)
- [ ] 40 literature benchmarks are cited with references
- [ ] Benchmark selection criteria described (how were the 40 benchmarks chosen?)
- [ ] Comparison with existing pharmacovigilance databases or studies
- [ ] Limitations of validation approach acknowledged

### FAERS Bias and Limitations (Must Be Addressed)
- [ ] **Reporting bias:** FAERS is a voluntary reporting system; underreporting is acknowledged
- [ ] **Notoriety bias:** media attention inflates reports for some drugs
- [ ] **Weber effect:** reporting peaks shortly after drug approval
- [ ] **Duplicate reports:** describe deduplication approach
- [ ] **Missing data:** rates of missing sex, age, indication fields
- [ ] **Confounding:** FAERS lacks denominator data (prescription counts); cannot calculate incidence rates
- [ ] **Channeling bias:** some drugs preferentially prescribed to one sex
- [ ] **Indication bias:** diseases with sex-skewed prevalence affect baseline reporting
- [ ] **Polypharmacy:** difficulty attributing events to specific drugs
- [ ] **Temporal changes:** reporting practices change over 2004-2025 period
- [ ] Explicitly state that disproportionality signals are hypothesis-generating, not confirmatory

### medRxiv Screening Readiness
- [ ] Manuscript is original research (not a narrative review, case report, or editorial)
- [ ] No content that could endanger public health or discourage standard medical treatment
- [ ] No identifying patient information anywhere in manuscript or supplementary files
- [ ] No clinical trial component (if there were, registration would be required)
- [ ] Manuscript is within medRxiv scope (health sciences, clinical research, public health)
- [ ] All references are properly formatted and complete
- [ ] No plagiarism (run through iThenticate or similar before submission)
- [ ] Manuscript has not been previously published in a peer-reviewed journal

---

## 8. Submission Process Summary

### Step-by-Step
1. [ ] Create account at https://submit.medrxiv.org/ (if not already registered)
2. [ ] Prepare final PDF (all text + figures + tables in one file)
3. [ ] Prepare supplementary files separately
4. [ ] Deposit dataset on Zenodo; obtain DOI
5. [ ] Ensure GitHub repository is public and contains README
6. [ ] Log in to submission system
7. [ ] Enter metadata: title, authors, affiliations, ORCID, abstract, subject area
8. [ ] Upload manuscript PDF
9. [ ] Upload supplementary files
10. [ ] Enter Data Availability Statement
11. [ ] Enter Competing Interests Statement
12. [ ] Confirm ethics declarations
13. [ ] Enter Funding Statement
14. [ ] Review all entries; submit
15. [ ] Expect screening to complete in **2-4 business days** (may take longer on weekends/holidays)
16. [ ] Respond promptly to any screening queries from medRxiv staff

### After Posting
- [ ] Verify the posted preprint displays correctly (text, figures, metadata)
- [ ] Note the medRxiv DOI (format: 10.1101/YYYY.MM.DD.XXXXXXXX)
- [ ] Update GitHub README with medRxiv DOI/link
- [ ] Update Zenodo deposit with medRxiv DOI/link
- [ ] Share preprint via appropriate channels
- [ ] Monitor for reader comments on medRxiv
- [ ] Plan journal submission (medRxiv supports direct transfer to select journals)

---

## 9. Quick Reference: Key Numbers

| Item | Value |
|------|-------|
| PDF size limit | 40 MB |
| Screening time | 2-4 business days |
| Subject area | Pharmacology and Therapeutics |
| FAERS reports | 14.5M (2004-2025) |
| KG nodes | 109,867 |
| KG edges | 1,822,851 |
| Sex-differential signals | 96,281 |
| Validation precision | 82.8% directional (40 benchmarks) |
| GitHub | github.com/jshaik369/SexDiffKG |
| ORCID | 0009-0002-1748-7516 |

---

*Checklist prepared for medRxiv submission. Last updated: March 2026.*
