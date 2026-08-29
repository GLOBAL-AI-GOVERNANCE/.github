#!/usr/bin/env python3
"""Validate the minimal shared Claims Integrity control files."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"Claims Integrity validation failed: {message}")


def main() -> None:
    convention = json.loads((ROOT / "claims-integrity.json").read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "schemas/claims-integrity.schema.json").read_text(encoding="utf-8"))
    required = set(schema["required"])
    if set(convention) != required:
        fail("convention keys do not match the strict schema")
    for key in ("schema_version", "control_id", "delivery_states", "evidence_states"):
        if convention[key] != schema["properties"][key]["const"]:
            fail(f"unexpected {key}")
    questions = convention["required_review_questions"]
    if len(questions) < 4 or len(questions) != len(set(questions)):
        fail("review questions must be unique and complete")

    template = (ROOT / "PULL_REQUEST_TEMPLATE.md").read_text(encoding="utf-8")
    documentation = (ROOT / "docs/CLAIMS_INTEGRITY.md").read_text(encoding="utf-8")
    for value in (*convention["delivery_states"], *convention["evidence_states"]):
        if value not in template or value not in documentation:
            fail(f"status is not represented on public surfaces: {value}")
    for boundary in ("not described as a release", "does not imply certification", "humans retain authority"):
        if boundary.casefold() not in (template + documentation).casefold():
            fail(f"required boundary missing: {boundary}")
    if "every organization repository automatically" not in documentation:
        fail("adoption limitation is missing")
    print("Claims Integrity validation passed: convention, schema, review checklist, and automation boundary agree.")


if __name__ == "__main__":
    main()
