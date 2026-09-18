import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from evaluate import score

def test_exact_match():
    assert score("Paris", "Paris")["exact_match"] is True

def test_keyword_coverage_detects_partial_answer():
    result = score("large language model", "language model")
    assert 0 < result["keyword_coverage"] < 1
