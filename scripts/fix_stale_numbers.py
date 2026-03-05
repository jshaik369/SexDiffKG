#!/usr/bin/env python3
"""Fix stale v3 numbers in publication-critical files.
Only modifies files that would be sent externally.
Historical vault docs are left untouched (they correctly reference v3 in context).
"""
import os
import re
from datetime import datetime

base = "/home/jshaik369/sexdiffkg"

# Files to fix (publication-critical ONLY)
CRITICAL_FILES = [
    f"{base}/README.md",
    f"{base}/Publication/manuscript_scidata_COMPLETE.md",
    f"{base}/Publication/manuscript_scidata_draft.md",
]

# Replacement map: old → new
REPLACEMENTS = [
    # Node counts
    ('127,063', '109,867'),
    ('127063', '109867'),
    ('126,575', '109,867'),
    ('126575', '109867'),
    # Edge counts
    ('5,839,717', '1,822,851'),
    ('5839717', '1822851'),
    ('5,489,928', '1,822,851'),
    ('5489928', '1822851'),
    # Signal counts
    ('183,539', '96,281'),
    ('183539', '96281'),
]

# Context-aware replacements (only replace in specific contexts)
CONTEXT_REPLACEMENTS = [
    # KEGG → Reactome (only in pathway context, not in VEDA-KG descriptions)
    # DistMult MRR values
    ('MRR of 0.048', 'MRR of 0.2484'),
    ('MRR of 0.039', 'MRR of 0.2484'),
    ('MRR of 0.093', 'MRR of 0.2484'),
    ('MRR 0.048', 'MRR 0.2484'),
    ('MRR 0.039', 'MRR 0.2484'),
    ('MRR 0.093', 'MRR 0.2484'),
    # Old node type counts
    ('29,277 drugs', '3,920 drugs'),
    ('16,162 adverse events', '9,949 adverse events'),
    ('70,607 genes', '77,498 genes'),
    ('8,721 proteins', '16,201 proteins'),
]

KEGG_PATTERNS = [
    (r'KEGG pathways', 'Reactome pathways'),
    (r'KEGG pathway', 'Reactome pathway'),
    (r'KEGG \(', 'Reactome ('),
    (r'from KEGG', 'from Reactome'),
]

print("=" * 60)
print("STALE NUMBER CLEANUP — Publication-Critical Files")
print(f"Date: {datetime.now().isoformat()}")
print("=" * 60)

total_replacements = 0

for filepath in CRITICAL_FILES:
    if not os.path.exists(filepath):
        print(f"\n  SKIP: {filepath} (not found)")
        continue

    with open(filepath) as f:
        content = f.read()

    original = content
    file_replacements = 0

    # Direct replacements
    for old, new in REPLACEMENTS:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            file_replacements += count
            print(f"  {os.path.basename(filepath)}: {old} → {new} ({count}x)")

    # Context-aware replacements
    for old, new in CONTEXT_REPLACEMENTS:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            file_replacements += count
            print(f"  {os.path.basename(filepath)}: {old} → {new} ({count}x)")

    # KEGG → Reactome (careful — only SexDiffKG pathway references)
    for pattern, replacement in KEGG_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            file_replacements += len(matches)
            print(f"  {os.path.basename(filepath)}: KEGG → Reactome ({len(matches)}x)")

    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        total_replacements += file_replacements
        print(f"  → Updated {os.path.basename(filepath)} ({file_replacements} replacements)")
    else:
        print(f"  {os.path.basename(filepath)}: no changes needed")

# Also fix the main repo GROUND_TRUTH.json vault copy README
vault_readme = "/home/jshaik369/AYURFEM-Vault/projects/sexdiffkg/README.md"
if os.path.exists(vault_readme):
    with open(vault_readme) as f:
        content = f.read()
    original = content
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)
    if content != original:
        with open(vault_readme, 'w') as f:
            f.write(content)
        print(f"  → Updated vault README.md")

print(f"\n{'=' * 60}")
print(f"Total replacements: {total_replacements}")
print(f"Files modified: {sum(1 for f in CRITICAL_FILES if os.path.exists(f))}")
print(f"\nNOTE: Historical vault docs (session logs, audit reports) are")
print(f"intentionally NOT modified — they correctly reference v3 in")
print(f"historical context as part of the v3→v4 transition record.")
