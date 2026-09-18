"""Reusable annotation quality engine.

The engine is intentionally deterministic: the same input and policy produce
the same findings, making QA results reproducible and auditable.
"""
from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass, asdict
from typing import Iterable

@dataclass(frozen=True)
class Finding:
    item_id: str
    severity: str
    reason: str
    details: str

def run_quality_checks(rows: Iterable[dict], allowed_labels: set[str], low_confidence: float = 0.60) -> dict:
    rows = list(rows)
    findings: list[Finding] = []
    groups = defaultdict(list)

    for row in rows:
        item = (row.get("item_id") or "").strip()
        label = (row.get("label") or "").strip()
        annotator = (row.get("annotator") or "").strip()

        if not item or not annotator:
            findings.append(Finding(item or "<missing>", "high", "malformed_record",
                                     "item_id and annotator are required"))
        if not label:
            findings.append(Finding(item or "<missing>", "high", "missing_annotation",
                                     f"{annotator or 'unknown annotator'} supplied no label"))
        elif label not in allowed_labels:
            findings.append(Finding(item or "<missing>", "high", "invalid_label",
                                     f"'{label}' is outside the allowed label set"))

        try:
            confidence = float(row.get("confidence", ""))
        except (TypeError, ValueError):
            confidence = 0.0
            findings.append(Finding(item or "<missing>", "medium", "invalid_confidence",
                                    "confidence is not numeric"))
        if label and confidence < low_confidence:
            findings.append(Finding(item or "<missing>", "medium", "low_confidence",
                                    f"confidence={confidence:.2f} below {low_confidence:.2f}"))

        groups[item].append(row)

    comparable = 0
    agreement_count = 0
    for item_id, records in groups.items():
        labelled = [(r.get("annotator","").strip(), r.get("label","").strip())
                    for r in records if (r.get("label") or "").strip()]
        unique_annotators = {a for a, _ in labelled if a}
        labels = {label for _, label in labelled}

        if len(unique_annotators) >= 2:
            comparable += 1
            if len(labels) == 1:
                agreement_count += 1
            else:
                findings.append(Finding(item_id, "high", "label_disagreement",
                                         "annotators supplied different labels"))

        if len(unique_annotators) < 2:
            findings.append(Finding(item_id, "medium", "incomplete_annotation",
                                     "fewer than two annotators supplied a usable label"))

    severity_order = {"high": 0, "medium": 1, "low": 2}
    findings.sort(key=lambda f: (severity_order[f.severity], f.item_id, f.reason))
    return {
        "records": len(rows),
        "unique_items": len(groups),
        "findings": [asdict(f) for f in findings],
        "agreement": round(agreement_count / comparable, 3) if comparable else 0.0,
        "high_priority": sum(f.severity == "high" for f in findings),
        "medium_priority": sum(f.severity == "medium" for f in findings),
    }
