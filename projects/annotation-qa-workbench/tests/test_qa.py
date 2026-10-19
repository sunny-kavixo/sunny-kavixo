from qa import analyze
from pathlib import Path

def test_real_dataset_has_quality_findings():
    import csv
    csv_path = Path(__file__).resolve().parents[1] / "annotations.csv"
    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    report = analyze(rows)
    reasons = {x["reason"] for x in report["findings"]}
    assert "label_disagreement" in reasons
    assert "missing_annotation" in reasons

def test_invalid_label_is_reported():
    rows = [{"item_id":"1","annotator":"A","label":"unknown","confidence":"0.9"}]
    report = analyze(rows)
    assert any(x["reason"] == "invalid_label" for x in report["findings"])
