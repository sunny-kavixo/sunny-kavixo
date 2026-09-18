from qa import analyze

def test_detects_disagreement_and_missing_annotation():
    rows = [
        {"item_id":"1","annotator":"A","label":"positive","confidence":"0.9"},
        {"item_id":"1","annotator":"B","label":"negative","confidence":"0.7"},
        {"item_id":"2","annotator":"A","label":"","confidence":"0"},
        {"item_id":"2","annotator":"B","label":"positive","confidence":"0.8"},
    ]
    report = analyze(rows)
    assert report["items_with_disagreement"] == 1
    assert report["missing_labels"] == 1
    assert report["agreement"] == 0.0
    assert len(report["review_queue"]) == 2

def test_invalid_label_is_reported():
    rows = [
        {"item_id":"1","annotator":"A","label":"unknown","confidence":"0.5"},
    ]
    assert analyze(rows)["invalid_labels"] == 1
