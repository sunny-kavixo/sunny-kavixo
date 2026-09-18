import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from pipeline import quality_report

def test_quality_report_finds_real_quality_problems():
    rows = [
        {"id":"1","text":"hello","label":"greeting"},
        {"id":"1","text":"hello","label":"greeting"},
        {"id":"2","text":"","label":"greeting"},
    ]
    report = quality_report(rows)
    assert report["rows"] == 3
    assert report["duplicate_ids"] == 1
    assert report["duplicate_text"] == 1
    assert report["missing"]["text"] == 1
