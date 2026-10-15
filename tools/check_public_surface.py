#!/usr/bin/env python3
"""Fail closed on public artifacts that expose protected-report fields.

This checker intentionally emits reason classes only; it never prints matched values.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

PROTECTED_KEYS = {
    "reporter", "reporter_id", "reporter_identity", "source_identity",
    "protected_source", "protected_source_identity", "raw_report",
    "private_evidence", "confidential_evidence", "private_contact",
}
LOCAL_PATH = re.compile(r"(?i)(?:[a-z]:[\\/]users[\\/][^\\/\s]+|/" r"users/[^/\s]+|/" r"home/[^/\s]+)")
SKIP = {".git", ".venv", "venv", "node_modules", "__pycache__"}

def walk(value):
    if isinstance(value, dict):
        for k, v in value.items():
            yield str(k)
            yield from walk(v)
    elif isinstance(value, list):
        for v in value: yield from walk(v)

def main(argv=None):
    root=Path(argv[0] if argv else ".").resolve()
    reasons=set()
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP for part in path.parts):
            continue
        rel=path.relative_to(root)
        if LOCAL_PATH.search(str(rel)): reasons.add("PERSONAL_PATH")
        try: raw=path.read_text(encoding="utf-8")
        except (UnicodeDecodeError,OSError): continue
        if LOCAL_PATH.search(raw): reasons.add("PERSONAL_PATH")
        if path.suffix.lower()==".json":
            try: data=json.loads(raw)
            except json.JSONDecodeError: continue
            keys={k.casefold() for k in walk(data)}
            if keys & PROTECTED_KEYS: reasons.add("PROTECTED_CONCERN_FIELD")
    if reasons:
        print("SAFE_STOP")
        for r in sorted(reasons): print(r)
        return 1
    print("PASS")
    return 0

if __name__=="__main__": raise SystemExit(main(sys.argv[1:]))
