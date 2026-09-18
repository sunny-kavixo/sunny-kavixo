"""Backward-compatible CLI for the Annotation QA Workbench."""
from __future__ import annotations
import json, sys
from pathlib import Path
from review_queue import load_csv
from qa_engine import run_quality_checks

def analyze(rows):
    policy = json.loads(Path(__file__).with_name("policy.json").read_text(encoding="utf-8"))
    return run_quality_checks(rows, set(policy["allowed_labels"]), float(policy["low_confidence_threshold"]))

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python qa.py annotations.csv")
    report = analyze(load_csv(sys.argv[1]))
    print("ANNOTATION DATASET QUALITY REPORT")
    print("=================================")
    print(f"Records: {report['records']}")
    print(f"Unique items: {report['unique_items']}")
    print(f"Agreement: {report['agreement']:.3f}")
    print(f"High-priority findings: {report['high_priority']}")
    print(f"Medium-priority findings: {report['medium_priority']}")
    print(f"Total findings: {len(report['findings'])}")
    print("\nReview queue:")
    print(json.dumps(report["findings"], indent=2))

if __name__ == "__main__":
    main()
