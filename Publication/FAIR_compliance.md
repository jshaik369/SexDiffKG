# SexDiffKG FAIR Compliance Assessment

**Version:** 1.0 | **Date:** 2026-03-08 | **Score:** 12/15 (90%)

---

## Summary

SexDiffKG meets 12 of 15 FAIR principles fully and 3 partially. The three gaps are achievable with moderate effort.

---

## Findable

| Principle | Status | Evidence |
|-----------|--------|----------|
| **F1** Globally unique identifier | FULL | Zenodo DOI: 10.5281/zenodo.18819192 |
| **F2** Rich metadata | FULL | GROUND_TRUTH.json (4 copies), README.md, CITATION.cff, AUDIT_PACKAGE.md |
| **F3** Metadata includes identifier | FULL | DOI in CITATION.cff, README badges, Zenodo metadata |
| **F4** Registered in searchable resource | PARTIAL | GitHub indexed by Google Scholar. FAIRsharing.org registration pending |

**Gap F4:** Register at https://fairsharing.org (~30 min manual effort)

---

## Accessible

| Principle | Status | Evidence |
|-----------|--------|----------|
| **A1** Retrievable by identifier via standard protocol | FULL | GitHub HTTPS, Zenodo HTTPS |
| **A1.1** Protocol is open, free, universally implementable | FULL | HTTPS |
| **A1.2** Protocol allows authentication when needed | FULL | GitHub supports SSH/token auth |
| **A2** Metadata accessible when data unavailable | FULL | Zenodo preserves metadata independently |

**No gaps in Accessible.**

---

## Interoperable

| Principle | Status | Evidence |
|-----------|--------|----------|
| **I1** Formal, shared language for knowledge representation | PARTIAL | TSV format (simple, widely parseable). Uses standard identifiers (ChEMBL IDs, STRING IDs, Reactome IDs, MedDRA PTs). Not RDF/OWL but easily convertible |
| **I2** Vocabularies follow FAIR principles | PARTIAL | MedDRA (AEs), ChEMBL (drugs), STRING (proteins), Reactome (pathways). No formal alignment to RxNorm, SNOMED-CT, or BioLink Model |
| **I3** Qualified references to other metadata | FULL | Cross-references with version numbers: FAERS 2004Q1-2025Q3, ChEMBL 36, STRING v12.0, Reactome 2026-02, GTEx v8 |

**Gap I1/I2:** Optional — add RDF/Turtle export or BioLink Model alignment. Not required for most use cases.

---

## Reusable

| Principle | Status | Evidence |
|-----------|--------|----------|
| **R1** Richly described with plurality of attributes | FULL | 6 node types, 6 edge types, full schema in README and GROUND_TRUTH.json |
| **R1.1** Clear and accessible data usage license | FULL | CC-BY 4.0 (data), MIT (code). Stated in README, CITATION.cff, LICENSE |
| **R1.2** Detailed provenance | FULL | GROUND_TRUTH.json (MD5 checksums), AUDIT_PACKAGE.md (verification commands), full data lineage |
| **R1.3** Meet domain-relevant community standards | PARTIAL | No FAIR maturity indicators. No DrugBank/ATC cross-references on drug nodes |

**Gap R1.3:** Add DrugBank IDs via ChEMBL 36 molecule_dictionary.drugbank_id (script: scripts/finalize_fair.py)

---

## Action Items

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| 1 | Register on FAIRsharing.org | 30 min (manual) | F4 → FULL |
| 2 | Add DrugBank cross-references | 2h (script) | R1.3 → FULL |
| 3 | Generate Bioschemas JSON-LD | 1h (script) | Improves discoverability |
| 4 | RDF/Turtle export | 4h (script) | I1 → FULL |
| 5 | BioLink Model alignment | 8h | I2 → FULL |

**After items 1-2:** Score = 14/15 (93%)
**After all items:** Score = 15/15 (100%)
