from qa_engine import run_quality_checks

def test_routes_disagreement_and_missing_annotation():
    rows = [
        {"item_id":"1","annotator":"A","label":"positive","confidence":"0.9"},
        {"item_id":"1","annotator":"B","label":"negative","confidence":"0.8"},
        {"item_id":"2","annotator":"A","label":"","confidence":"0"},
        {"item_id":"2","annotator":"B","label":"positive","confidence":"0.9"},
    ]
    r = run_quality_checks(rows, {"positive","negative"})
    reasons = {x["reason"] for x in r["findings"]}
    assert "label_disagreement" in reasons
    assert "missing_annotation" in reasons

def test_low_confidence_is_reviewed():
    rows = [{"item_id":"1","annotator":"A","label":"positive","confidence":"0.4"}]
    r = run_quality_checks(rows, {"positive","negative"}, 0.6)
    assert any(x["reason"] == "low_confidence" for x in r["findings"])

def test_invalid_label_is_high_priority():
    rows = [{"item_id":"1","annotator":"A","label":"car","confidence":"0.9"}]
    r = run_quality_checks(rows, {"positive","negative"})
    finding = next(x for x in r["findings"] if x["reason"] == "invalid_label")
    assert finding["severity"] == "high"
