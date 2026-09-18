"""Simple, explainable evaluation harness for text-model outputs."""
from __future__ import annotations
import json
import sys

def score(expected: str, actual: str) -> dict:
    e, a = expected.strip().lower(), actual.strip().lower()
    exact = e == a
    keywords = [w for w in e.split() if len(w) > 3]
    hit_rate = sum(w in a for w in keywords) / len(keywords) if keywords else 1.0
    return {"exact_match": exact, "keyword_coverage": round(hit_rate, 3)}

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python evaluate.py evaluations.jsonl")
    results = []
    with open(sys.argv[1], encoding="utf-8") as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                results.append({**row, **score(row["expected"], row["actual"])})
    exact = sum(r["exact_match"] for r in results) / len(results) if results else 0
    coverage = sum(r["keyword_coverage"] for r in results) / len(results) if results else 0
    print(json.dumps({
        "examples": len(results),
        "exact_match_rate": round(exact, 3),
        "mean_keyword_coverage": round(coverage, 3),
        "errors": [r for r in results if not r["exact_match"]],
    }, indent=2))

if __name__ == "__main__":
    main()
