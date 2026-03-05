# SexDiffKG Pipeline Makefile (v4)
# NOTE: This Makefile is for reference only. v4 pipeline scripts are in scripts/v4_*.py
#
# The v4 canonical pipeline:
#   v4_01_normalize_diana.py   - Drug normalization via DiAna dictionary
#   v4_02_compute_signals.py   - Sex-differential ROR signal computation
#   v4_03_build_kg.py          - Knowledge graph assembly (109,867 nodes / 1,822,851 edges)
#   v4_04_train_distmult.py    - DistMult embedding training
#   v4_05_train_rotatE.py      - RotatE embedding training
#   v4_06_retrain_distmult_v41.py - DistMult v4.1 retraining
#   v4_07d_train_rotatE_cpu_fixed.py - RotatE v4.1 CPU training (final)
#
# Run v4 pipeline: bash scripts/v4_run_all.sh
# Run v4 chain:    bash scripts/v4_auto_chain.sh

PYTHON := python3
SCRIPTS := scripts
DATA := data
RESULTS := results
EXT_STORE := /media/jshaik369/cen8tb1/sexdiffkg_data
KG_DIR := $(DATA)/kg_v4

.PHONY: all clean phase1 phase2 phase3 phase4 phase5 phase6 phase7

all: $(RESULTS)/kg_embeddings/model.pkl

# Phase 1: Drug normalization (DiAna dictionary)
$(DATA)/processed/faers_clean/drug_normalized.parquet: $(SCRIPTS)/v4_01_normalize_diana.py
	$(PYTHON) $< --input-dir $(DATA)/processed/faers_clean --output-dir $(DATA)/processed/faers_clean

phase1: $(DATA)/processed/faers_clean/drug_normalized.parquet

# Phase 2: Signal computation
$(RESULTS)/signals/ror_by_sex.parquet: $(DATA)/processed/faers_clean/drug_normalized.parquet $(SCRIPTS)/v4_02_compute_signals.py
	$(PYTHON) $(SCRIPTS)/v4_02_compute_signals.py --input-dir $(DATA)/processed/faers_clean --output-dir $(RESULTS)/signals

phase2: $(RESULTS)/signals/ror_by_sex.parquet

# Phase 3: KG assembly
$(KG_DIR)/triples.tsv: $(RESULTS)/signals/ror_by_sex.parquet $(SCRIPTS)/v4_03_build_kg.py
	$(PYTHON) $(SCRIPTS)/v4_03_build_kg.py --output-dir $(KG_DIR)

phase3: $(KG_DIR)/triples.tsv

# Phase 4: DistMult training
$(RESULTS)/kg_embeddings/distmult/model.pkl: $(KG_DIR)/triples.tsv $(SCRIPTS)/v4_04_train_distmult.py
	$(PYTHON) $(SCRIPTS)/v4_04_train_distmult.py --input $(KG_DIR)/triples.tsv --output-dir $(RESULTS)/kg_embeddings/distmult

phase4: $(RESULTS)/kg_embeddings/distmult/model.pkl

# Phase 5: RotatE training
$(RESULTS)/kg_embeddings/rotatE/model.pkl: $(KG_DIR)/triples.tsv $(SCRIPTS)/v4_05_train_rotatE.py
	$(PYTHON) $(SCRIPTS)/v4_05_train_rotatE.py --input $(KG_DIR)/triples.tsv --output-dir $(RESULTS)/kg_embeddings/rotatE

phase5: $(RESULTS)/kg_embeddings/rotatE/model.pkl

# Phase 6: DistMult v4.1 retraining
$(RESULTS)/kg_embeddings/distmult_v41/model.pkl: $(KG_DIR)/triples.tsv $(SCRIPTS)/v4_06_retrain_distmult_v41.py
	$(PYTHON) $(SCRIPTS)/v4_06_retrain_distmult_v41.py --input $(KG_DIR)/triples.tsv --output-dir $(RESULTS)/kg_embeddings/distmult_v41

phase6: $(RESULTS)/kg_embeddings/distmult_v41/model.pkl

# Phase 7: RotatE v4.1 CPU training (final)
$(RESULTS)/kg_embeddings/rotatE_v41/model.pkl: $(KG_DIR)/triples.tsv $(SCRIPTS)/v4_07d_train_rotatE_cpu_fixed.py
	$(PYTHON) $(SCRIPTS)/v4_07d_train_rotatE_cpu_fixed.py --input $(KG_DIR)/triples.tsv --output-dir $(RESULTS)/kg_embeddings/rotatE_v41

phase7: $(RESULTS)/kg_embeddings/rotatE_v41/model.pkl

# Embeddings (legacy target, points to DistMult)
$(RESULTS)/kg_embeddings/model.pkl: $(RESULTS)/kg_embeddings/distmult/model.pkl
	@echo "All embedding models trained."

clean:
	rm -f $(DATA)/raw/faers/.done $(DATA)/raw/string/.done
