"""
SexDiffKG centralized path module.

The auto-injected prelude at the top of each script handles the env-var lookup.
This module is a centralized version that scripts can import explicitly:

    from sexdiffkg.paths import SEXDIFFKG_HOME, KG_V4, SIGNALS_V4

It is also the canonical place to add new derived paths so they don't get
duplicated across scripts.
"""
import os
from pathlib import Path

SEXDIFFKG_HOME: Path = Path(
    os.environ.get("SEXDIFFKG_HOME", os.path.expanduser("~/sexdiffkg"))
).resolve()

SEXDIFFKG_VAULT: Path = Path(
    os.environ.get(
        "SEXDIFFKG_VAULT",
        os.path.expanduser("~/AYURFEM-Vault/projects/sexdiffkg"),
    )
).resolve()

# Common subpaths.
DATA = SEXDIFFKG_HOME / "data"
RESULTS = SEXDIFFKG_HOME / "results"
SCRIPTS = SEXDIFFKG_HOME / "scripts"
PUBLICATION = SEXDIFFKG_HOME / "Publication"

KG_V4 = DATA / "kg_v4"
KG_V5 = DATA / "kg_v5"
KG_V52 = DATA / "kg_v5.2"
KG_ACTIVE_LINK = DATA / "kg"   # symlink → kg_v4

SIGNALS_V4 = RESULTS / "signals_v4"
DEEP_ANALYSIS = RESULTS / "deep_analysis"
FIGURES = RESULTS / "figures"
MODELS_V4 = RESULTS / "models_v4"

GROUND_TRUTH = SEXDIFFKG_HOME / "GROUND_TRUTH.json"
GROUND_TRUTH_V5 = DATA / "kg_v5" / "GROUND_TRUTH_v5.json"
