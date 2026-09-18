"""Small, dependency-light dataset quality checker for AI/ML data.

Usage:
    python pipeline.py sample_data.csv
"""
from __future__ import annotations
import csv
import sys
from collections import Counter

REQUIRED = ("id", "text", "label")

def read_rows(path: str):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def quality_report(rows):
    if not rows:
        return {"rows": 0, "missing": {}, "duplicate_ids": 0, "duplicate_text": 0, "labels": {}}

    missing = {c: sum(not (r.get(c) or "").strip() for r in rows) for c in REQUIRED}
    ids = [r.get("id", "").strip() for r in rows]
    texts = [r.get("text", "").strip() for r in rows]
    labels = Counter((r.get("label") or "").strip() for r in rows)

    return {
        "rows": len(rows),
        "missing": missing,
        "duplicate_ids": len(ids) - len(set(ids)),
        "duplicate_text": len(texts) - len(set(texts)),
        "labels": dict(labels),
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python pipeline.py sample_data.csv")
    rows = read_rows(sys.argv[1])
    report = quality_report(rows)
    print("\nAI DATA QUALITY REPORT")
    print("=" * 24)
    print(f"Rows: {report['rows']}")
    print(f"Duplicate IDs: {report['duplicate_ids']}")
    print(f"Duplicate text: {report['duplicate_text']}")
    print("Missing fields:", report["missing"])
    print("Label distribution:", report["labels"])

if __name__ == "__main__":
    main()
