# AI Use Statement — SexDiffKG

This document discloses how AI tools were used in the construction of the SexDiffKG project, in line with reproducibility expectations and conference policies (e.g., BOSC, ISMB).

## Tools used

- **Anthropic Claude** (Sonnet, Opus): used during code authorship, abstract drafting, manuscript editing, and orchestration of long-running analytical "wave" pipelines on the DGX Spark GB10 hardware.
- **OpenAI GPT-4 / ChatGPT**: used during exploratory analysis and early-stage drafting.

## Where AI was used

| Area | AI involvement | Verified by human? |
|---|---|---|
| Code authorship (pipeline scripts) | AI-assisted; reviewed and edited by author | Yes |
| Wave analysis scripts (`scripts/wave_analysis/`) | AI-generated under autopilot prompt; outputs validated against `GROUND_TRUTH.json` | Yes — every numeric output cross-checked |
| Abstract / poster drafts | AI-assisted writing, author-edited | Yes |
| Manuscript text | AI-assisted, author-edited | Yes |
| Figure generation code | AI-assisted Matplotlib code | Yes |
| Citation lookup | AI suggestions cross-checked against original sources | Yes |
| Statistical methodology | Author-designed; AI used for code implementation only | Yes |
| Numerical computations | NEVER AI-generated; all values computed from source parquet/SQL data | Yes — see `GROUND_TRUTH.json` and `audit_proof_report.json` |

## Where AI was NOT used

- The decision of what to study, the scientific framing, and the interpretation of results.
- Numerical claims: every number cited in the abstract, manuscript, or poster is computed from raw data files. AI tools were instructed to never fabricate numbers (see `.claude/AUTOPILOT_PROMPT.md`, "NEVER hardcode numbers — always compute from the parquet source"). All numeric outputs are traceable to source data via `audit_proof_verification.py`.
- The peer-review responses (none yet).

## Verification

The `GROUND_TRUTH.json` file at the repo root is the canonical record of every number used in any abstract, manuscript, or poster. The script `scripts/audit_proof_verification.py` re-derives these numbers from raw data files and produces `audit_proof_report.json` with PASS/FAIL per claim.

## Author responsibility

Despite AI assistance in implementation, all scientific judgments — methodology, interpretation, and conclusions — are the responsibility of the named author (Mohammed Javeed Akhtar Abbas Shaik / J. Shaik). AI was a tool, not a co-author.
