# SexDiffKG Pipeline Makefile
# Run: make all 2>&1 | tee logs/pipeline_$(date +%Y%m%d).log

PYTHON := python3
SCRIPTS := scripts
DATA := data
RESULTS := results
EXT_STORE := /media/jshaik369/cen8tb/sexdiffkg_data

.PHONY: all clean phase1 phase2 phase3 phase4 phase5 phase6

all: $(RESULTS)/kg_embeddings/model.pkl

# Phase 1: FAERS acquisition and cleaning
$(DATA)/raw/faers/.done: $(SCRIPTS)/01_download_faers.py
	$(PYTHON) $< --output-dir $(EXT_STORE)/raw_faers --link-dir $(DATA)/raw/faers && touch $@

$(DATA)/processed/faers/demo.parquet: $(DATA)/raw/faers/.done $(SCRIPTS)/02_parse_faers.py
	$(PYTHON) $(SCRIPTS)/02_parse_faers.py --input-dir $(DATA)/raw/faers --output-dir $(DATA)/processed/faers

$(DATA)/processed/faers_clean/demo.parquet: $(DATA)/processed/faers/demo.parquet $(SCRIPTS)/03_deduplicate.py
	$(PYTHON) $(SCRIPTS)/03_deduplicate.py --input-dir $(DATA)/processed/faers --output-dir $(DATA)/processed/faers_clean

$(DATA)/processed/faers_clean/drug_normalized.parquet: $(DATA)/processed/faers_clean/demo.parquet $(SCRIPTS)/03b_normalize_drugs.py
	$(PYTHON) $(SCRIPTS)/03b_normalize_drugs.py --input-dir $(DATA)/processed/faers_clean --output-dir $(DATA)/processed/faers_clean

phase1: $(DATA)/processed/faers_clean/drug_normalized.parquet

# Phase 2: Signal computation
$(RESULTS)/signals/ror_by_sex.parquet: $(DATA)/processed/faers_clean/drug_normalized.parquet $(SCRIPTS)/04_compute_signals.py
	$(PYTHON) $(SCRIPTS)/04_compute_signals.py --input-dir $(DATA)/processed/faers_clean --output-dir $(RESULTS)/signals

phase2: $(RESULTS)/signals/ror_by_sex.parquet

# Phase 3: Molecular layer
$(DATA)/raw/string/.done: $(SCRIPTS)/05a_download_molecular.py
	$(PYTHON) $< && touch $@

$(DATA)/processed/molecular/drug_targets.parquet: $(DATA)/raw/string/.done $(SCRIPTS)/05b_build_molecular.py
	$(PYTHON) $(SCRIPTS)/05b_build_molecular.py --output-dir $(DATA)/processed/molecular

phase3: $(DATA)/processed/molecular/drug_targets.parquet

# Phase 4: GTEx
$(DATA)/processed/molecular/sex_de_genes.parquet: $(SCRIPTS)/05c_gtex_sex_de.py
	$(PYTHON) $< --output-dir $(DATA)/processed/molecular

phase4: $(DATA)/processed/molecular/sex_de_genes.parquet

# Phase 5: KG assembly
$(DATA)/kg/triples.tsv: $(RESULTS)/signals/ror_by_sex.parquet $(DATA)/processed/molecular/drug_targets.parquet $(SCRIPTS)/06_build_kg.py
	$(PYTHON) $(SCRIPTS)/06_build_kg.py --output-dir $(DATA)/kg

phase5: $(DATA)/kg/triples.tsv

# Phase 6: Embeddings
$(RESULTS)/kg_embeddings/model.pkl: $(DATA)/kg/triples.tsv $(SCRIPTS)/07_train_embeddings.py
	$(PYTHON) $(SCRIPTS)/07_train_embeddings.py --input $(DATA)/kg/triples.tsv --output-dir $(RESULTS)/kg_embeddings

phase6: $(RESULTS)/kg_embeddings/model.pkl

clean:
	rm -f $(DATA)/raw/faers/.done $(DATA)/raw/string/.done
