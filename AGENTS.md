# AGENTS.md

Instructions for coding agents working in the account-level governance defaults repository.

## Setup and checks

```bash
python3 -B tools/check_history_privacy.py
python3 -B tools/check_public_surface.py .
python3 -B tools/validate_claims_integrity.py
python3 -B -m unittest discover -s tools -p "test_*.py" -v
```

## Rules

- This repository holds account-level defaults for public repositories owned by the GitHub User `GLOBAL-AI-GOVERNANCE` (not a GitHub Organization). Repository-local files take precedence.
- Do not claim that Claims Integrity or other controls automatically govern every owned repository; adoption remains explicit per repository.
- Every result keeps `authority_effect: "NONE"`. Do not add a path that approves, certifies, or authorizes.
- Prefer squash-merge through green CI. Do not force-push `main`.

## Setup guide

End-to-end local setup for the toolkit and MCP: [AGENT_SETUP](https://ai-governance.solutions/AGENT_SETUP.html).
