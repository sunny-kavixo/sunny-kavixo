"""CLI entry point: inspect a dataset and write a reviewer queue."""
from __future__ import annotations
import csv, json, sys
from pathlib import Path
from qa_engine import run_quality_checks

def load_csv(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main() -> None:
    if len(sys.argv) not in (2, 3):
        raise SystemExit("Usage: python review_queue.py annotations.csv [policy.json]")
    policy_path = Path(sys.argv[2]) if len(sys.argv) == 3 else Path("policy.json")
    policy = json.loads(policy_path.read_text(encoding="utf-8"))
    report = run_quality_checks(
        load_csv(sys.argv[1]),
        set(policy["allowed_labels"]),
        float(policy["low_confidence_threshold"]),
    )
    output = Path("review_queue.json")
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k != "findings"}, indent=2))
    print(f"Review queue written to: {output}")
    print(f"Findings: {len(report['findings'])}")

if __name__ == "__main__":
    main()
