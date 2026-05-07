# Contributing to SexDiffKG

Thank you for considering contributing to SexDiffKG. This project provides a sex-differential drug safety knowledge graph and analysis pipeline; contributions that extend, validate, or improve any part of it are welcome.

## Quick start

```bash
git clone https://github.com/jshaik369/SexDiffKG.git
cd SexDiffKG
cp config.yaml.example config.yaml         # edit paths if needed
export SEXDIFFKG_HOME=$(pwd)                # or wherever you cloned to
pip install -r requirements.txt
```

See `docs/FAERS_SETUP.md` for end-to-end pipeline setup including FAERS download.

## Reporting bugs

Open an issue with:
1. Operating system and Python version.
2. Full command you ran.
3. Full traceback.
4. Minimal reproduction (preferably a small parquet slice).

## Suggesting analyses

We track ongoing analyses as "waves" in `scripts/wave_analysis/`. If you have an idea for a new analysis (a drug class, an organ system, a target family), open an issue describing:
- The hypothesis.
- The data slice required.
- The expected output (what figure / JSON / metric).

Wave proposals that align with existing data are typically prioritized.

## Pull requests

1. Branch from `main`, named `feat/...`, `fix/...`, or `wave/...`.
2. Run the audit before committing: `python3 scripts/audit_proof_verification.py`. PRs that change any numbers must update `GROUND_TRUTH.json` and pass the audit.
3. Never hardcode paths. Use `SEXDIFFKG_HOME` / `SEXDIFFKG_VAULT` env vars (see `paths.py` or the auto-injected prelude in each script).
4. Keep figures reproducible: include the script that generated them.
5. Squash to a small number of meaningful commits.

## What we don't accept

- Numerical claims without computation from raw data.
- Code that hardcodes paths to specific user directories.
- AI-generated text passed off as human-authored. (We use AI; we disclose it — see `AI_USE.md`.)

## Code of conduct

Be kind. Cite carefully. Disclose AI use. Sex-differential drug safety affects real patients, so accuracy is non-negotiable.

## Questions

Open an issue or email `jshaik@coevolvenetwork.com`.
