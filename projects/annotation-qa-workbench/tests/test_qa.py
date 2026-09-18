from qa import analyze

def test_real_dataset_has_quality_findings():
    import csv
    with open("../annotations.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    report = analyze(rows)
    reasons = {x["reason"] for x in report["findings"]}
    assert "label_disagreement" in reasons
    assert "missing_annotation" in reasons

def test_invalid_label_is_reported():
    rows = [{"item_id":"1","annotator":"A","label":"unknown","confidence":"0.9"}]
    report = analyze(rows)
    assert any(x["reason"] == "invalid_label" for x in report["findings"])
