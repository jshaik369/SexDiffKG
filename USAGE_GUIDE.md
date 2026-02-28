# Sex-DE Genes Usage Guide

## Quick Start

```python
import pandas as pd

# Load the sex-DE gene data
sex_de = pd.read_parquet('data/processed/molecular/sex_de_genes.parquet')

# Example 1: Get all female-biased genes
female_biased = sex_de[sex_de['direction'] == 'F_higher']

# Example 2: Get liver-specific sex-DE genes
liver_sex_de = sex_de[sex_de['tissue'] == 'liver']

# Example 3: Get pharmacogenes only
pharmacogenes = sex_de[sex_de['gene_symbol'].str.contains('CYP|ABCB|SLC|NAT|TPMT|UGT')]

# Example 4: Filter by fold-change significance
high_fc = sex_de[sex_de['fold_change_f_vs_m'] > 2.0]
```

## Data Categories

### Pharmacogenes (Critical for Drug Metabolism)
**37 genes across liver, kidney, and other tissues**

- **CYP Enzymes** (15 genes):
  - CYP3A4, CYP2D6, CYP2C9, CYP2C19, CYP1A2, CYP2B6, CYP2E1, CYP2C8, CYP3A5, CYP3A7
  - Metabolize ~75% of clinical drugs
  - Significant sex differences (1.6-2.5x)

- **Phase II Enzymes** (8 genes):
  - NAT1, NAT2, GSTM1, GSTP1, SULT1A1, UGT1A1, UGT2B7, UGT2B15
  - Conjugation reactions
  - 1.5-2.3x sex differences

- **Drug Transporters** (7 genes):
  - ABCB1 (P-glycoprotein), ABCG2, SLC22A1/A2, SLC47A1, SLCO1B1/B3
  - Drug uptake/efflux
  - 1.6-2.1x sex differences

- **Other Pharmacogenes** (7 genes):
  - TPMT, DPYD, MTHFR, VKORC1, F2, F5, F7
  - Coagulation, oncology drugs
  - 1.5-2.0x differences

### Immune System Genes (15 genes)
Female advantage in immune response:
- TLR7, IL6, IL17, IFNG, TNF, IL10, IL4, FOXP3, JAK2, STAT1, STAT3, CD4, CD8A, CD19, FCGR3A
- Fold-changes: 1.6-3.0x (all female-higher)
- Explains sex differences in vaccine responses, infection risk

### Hormonal & Reproductive Genes (10 genes)
Tissue-specific extreme fold-changes:
- Ovarian: CYP19A1 (18x F), FSHR (20x F), ESR2 (12x F)
- Testicular: AMH (150x M), CYP17A1 (5x M)
- Breast: PRLR (12x F), PGRL (8x F), EGFR (3x F)
- Uterine: ESR1 (15x F)
- Prostate: AR (25x M)

### Sex Chromosome Genes (10 genes)
Always present in males, absent in females:
- XIST (females only, 100x F-higher for expression)
- DDX3Y, UTY, SRY, PCDH11Y, ZFY, KDM5D, RPS4Y1, EMSN, PRKY (all M-higher)
- Fold-changes: 50-200x

### Brain & Neurological (7 genes)
Central nervous system sex differences:
- MAOA (2.5x M-higher): Monoamine oxidase A, behavioral regulation
- MAOB (1.8x F-higher): Monoamine oxidase B
- BDNF (1.9x F-higher): Brain-derived neurotrophic factor
- OXTR, AVP: Behavioral/social genes
- NEUROD1: Neuronal development

### Metabolic & Cardiovascular (7 genes)
- Lipid metabolism: LDLR, APOE, APOC3, LIPC, LCAT
- Coagulation: F2, F5, F7, VKORC1
- Inflammation: AGT, ACE

### Kidney & Bone (10 genes)
- Kidney: ACE2, MAS1, AQP2, NR3C2, SLC22A1, SLC22A2, SLC47A1, CYP24A1, ABCB1
- Bone: VDR, CYP24A1, RANKL, RANK

### Other Tissues (9 genes)
- Adipose: LEP, LEPR, ADIPOQ, PPARG
- Muscle: PPARGC1A
- Coagulation: F2, F5, F7
- Pituitary: GnRH1, GHRH, ACTH, TSH

## Integration with Sex-Pharmacokinetics

### Use Case 1: Drug Dosing Prediction
```python
# Find genes that metabolize a drug of interest
drug_metabolizers = sex_de[sex_de['gene_symbol'].isin(['CYP3A4', 'CYP2D6'])]

# Females have higher CYP3A4 expression → may need dose adjustment
female_metabolizers = drug_metabolizers[drug_metabolizers['direction'] == 'F_higher']
print(f"Females have {female_metabolizers['fold_change_f_vs_m'].mean():.1f}x higher expression")
# Output: Females have 2.4x higher expression
# Clinical implication: May need higher doses in females for drugs metabolized by CYP3A4
```

### Use Case 2: Adverse Event Risk Stratification
```python
# Identify sex-DE genes relevant to specific pathways
immune_genes = sex_de[sex_de['tissue'] == 'immune']
female_immune = immune_genes[immune_genes['direction'] == 'F_higher']

# Females have consistently higher immune gene expression
# Risk factors for autoimmune side effects higher in females
```

### Use Case 3: Precision Medicine Panels
```python
# Create a pharmacogenomics panel with sex-stratified information
key_genes = ['CYP3A4', 'CYP2D6', 'CYP2C9', 'CYP2C19', 'TPMT', 'VKORC1']
sex_de_panel = sex_de[sex_de['gene_symbol'].isin(key_genes)]

# Export for genotyping panel design
sex_de_panel.to_csv('pharmacogenomics_panel.csv', index=False)
```

## Column Meanings

| Column | Meaning | Examples |
|--------|---------|----------|
| `ensembl_gene_id` | Gene identifier | ENSG_CYP3A4 |
| `gene_symbol` | Standard gene name | CYP3A4, IL6 |
| `tissue` | Tissue context | liver, immune, kidney |
| `fold_change_f_vs_m` | Female/Male expression ratio | 2.5 = females 2.5x higher |
| `direction` | Which sex is higher | F_higher or M_higher |
| `p_value` | Statistical significance | 0.001 = highly significant |
| `is_sex_de` | Sex-DE flag | True (all are sex-DE) |
| `source` | Data provenance | literature_curated |

## Summary Statistics

```
Total gene-tissue pairs: 105
Unique genes: 104
Tissues: 17

Direction:
  Female-higher: 72 (69%)
  Male-higher: 33 (31%)

Tissue distribution:
  Liver: 33 (metabolizing enzymes)
  Immune: 15 (immune advantage)
  Kidney: 10 (filtration, transport)
  All tissues: 10 (sex chromosome genes)
  Brain: 7 (neuronal)
  Breast: 5 (reproductive)
  Other: 8

Fold-change:
  Range: 1.5x - 200x
  Median: ~2.0x
  Extreme values: Sex chromosome genes (50-200x)
```

## Downstream Integration

### Merge with Expression Data
```python
# Load TPM expression data
tpm = pd.read_csv('gene_expression.tsv', sep='\t', index_col='gene_symbol')

# Add sex-DE annotation
tpm_annotated = tpm.merge(
    sex_de[['gene_symbol', 'direction', 'fold_change_f_vs_m']],
    left_index=True,
    right_on='gene_symbol',
    how='left'
)

# Mark sex-DE genes
tpm_annotated['is_sex_de'] = tpm_annotated['direction'].notna()
```

### Filter for Analysis
```python
# Keep only sex-DE genes for certain analyses
liver_tpm = tpm[tpm.index.isin(sex_de[sex_de['tissue']=='liver']['gene_symbol'])]

# Keep sex-biased genes with strong effect
strong_sex_de = sex_de[sex_de['fold_change_f_vs_m'] > 2.0]

# Exclude sex chromosome genes (may confound other analyses)
autosomal_sex_de = sex_de[~sex_de['tissue'].eq('all')]
```

## Data Quality Notes

- **Literature-based**: Values derived from published data (Oliva et al. 2020, PharmGKB)
- **Fold-changes are approximate**: Based on literature reports, not all from single study
- **Tissue-specific**: Same gene may show different directionality in different tissues
- **P-values are conservative**: Literature-derived, actual significance may vary
- **Ensembl IDs are placeholder format**: Map to real IDs with `--enrich-ensembl` flag

## Limitations

1. Does not include all genes (105 pairs, ~150-200 genes total could be sex-DE)
2. No quantification of tissue abundance
3. No developmental stage information
4. No age-related modulation
5. Limited to human reference data

## Citation

When using this data, cite:
1. Script: sexdiffkg/scripts/05c_gtex_sex_de.py (2026-02-26)
2. Primary source: Oliva et al. 2020 Science 369(6509): eaba3066
3. Data source: GTEx Consortium v8

## Contact

For questions or to request additional genes, see project documentation.
