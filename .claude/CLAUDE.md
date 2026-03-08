# SexDiffKG Repository Governance

## Branch Workflow
- NEVER push directly to main. Main is protected and requires a PR.
- Create a feature branch for all work: `git checkout -b wave/NNN-description` or `git checkout -b fix/description`
- Push to the feature branch, then create a PR via `gh pr create`
- Merge PRs via `gh pr merge --squash` or `gh pr merge --merge`
- Delete the feature branch after merge

## Commit Messages
- Deep analysis waves: `Wave N: short description`
- Bug fixes: `fix: description`
- Data updates: `data: description`
- Keep messages under 72 characters on the first line

## Data Integrity
- GROUND_TRUTH.json is the single source of truth for all KG statistics
- Cross-reference GROUND_TRUTH.json before citing any number
- Never hardcode numbers that exist in GROUND_TRUTH.json
- If a number changes, update GROUND_TRUTH.json FIRST, then propagate

### Numbers That Must NEVER Be Used (stale v3 data)
- 49,026 / 28,669 / 20,357 strong signals (correct v4: 32,244 / 18,174 / 14,070 at |logR|>=1.0)
- 5,658 unique AEs (correct: 5,069)
- Any v3-era counts that don't match GROUND_TRUTH.json

## Security Rules
- NEVER commit credentials, API keys, tokens, or passwords
- NEVER commit .env files or secret configuration
- NEVER include local filesystem paths (e.g., /home/jshaik369/...) in committed data files
- NEVER add Co-Authored-By or any AI attribution to git commits
- Keep sensitive paths in .gitignore

## Accuracy Standards
- Verify paths resolve correctly before file operations
- Use `head -1` to check column names before pandas operations
- No shortcuts, approximations, or rounding of KG statistics
- Log all analysis results to the vault before committing

## Vault Logging
- Log session activity to /home/jshaik369/AYURFEM-Vault/projects/sexdiffkg/
- Update CONTINUITY_STATE.md after significant milestones
- Record decision rationale for non-obvious choices

## File Organization
- Deep analysis JSONs go in results/deep_analysis/
- Figures go in results/deep_analysis/figures/
- Publication papers go in Publication/papers/
- KG data versions go in data/kg_vN/
