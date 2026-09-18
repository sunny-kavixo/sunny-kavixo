"""Annotation dataset QA and review-queue generator."""
from __future__ import annotations
import csv, json, sys
from collections import defaultdict

ALLOWED = {"positive", "negative"}

def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def analyze(rows):
    required = {"item_id", "annotator", "label", "confidence"}
    missing_columns = required.difference(rows[0].keys()) if rows else required
    if missing_columns:
        raise ValueError("Missing columns: " + ", ".join(sorted(missing_columns)))

    missing = [r for r in rows if not (r.get("label") or "").strip()]
    invalid = [r for r in rows if (r.get("label") or "").strip() and r["label"].strip() not in ALLOWED]

    groups = defaultdict(list)
    for r in rows:
        groups[r["item_id"].strip()].append(r)

    disagreements, queue = [], []
    comparable = 0
    agreements = 0

    for item_id, records in groups.items():
        labels = [r["label"].strip() for r in records if r.get("label", "").strip()]
        if len(labels) >= 2:
            comparable += 1
            if len(set(labels)) == 1:
                agreements += 1
            else:
                disagreements.append(item_id)
                queue.append({"item_id": item_id, "reason": "label_disagreement"})
        if len(labels) < 2:
            queue.append({"item_id": item_id, "reason": "incomplete_annotation"})

    agreement = agreements / comparable if comparable else 0.0
    return {
        "records": len(rows),
        "unique_items": len(groups),
        "annotators": len({r["annotator"] for r in rows}),
        "missing_labels": len(missing),
        "invalid_labels": len(invalid),
        "items_with_disagreement": len(disagreements),
        "agreement": round(agreement, 3),
        "review_queue": queue,
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python qa.py annotations.csv")
    report = analyze(load(sys.argv[1]))
    print("ANNOTATION QA REPORT")
    print("====================")
    for key, value in report.items():
        if key != "review_queue":
            print(f"{key.replace('_', ' ').title()}: {value}")
    print("Review queue:", len(report["review_queue"]))
    print("\nJSON:")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
