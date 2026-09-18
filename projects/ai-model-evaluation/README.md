# AI Model Evaluation Lab

A **working, explainable evaluation harness** for comparing model answers against expected answers. It calculates exact-match accuracy and keyword coverage, then exposes failed cases for human review.

![LLM evaluation workflow](docs/evaluation-flow.svg)

## Real evaluation process

1. Create a versioned evaluation set.
2. Store the expected answer and candidate model output.
3. Run deterministic scoring.
4. Calculate aggregate metrics.
5. Inspect every failed example.
6. Change the model, prompt, or preprocessing.
7. Run the same evaluation set again and compare results.

## Run

```bash
python evaluate.py evaluations.jsonl
```

The repository includes four evaluation records, including an intentional incorrect answer so the failure path is visible.

## Example result

```text
{
  "examples": 4,
  "exact_match_rate": 0.75,
  "mean_keyword_coverage": 0.75
}
```

The failed example is returned in the `errors` array for review.

## Tests

```bash
python -m pytest tests/
```

## Why this matters

A model demo can show one impressive answer. An evaluation system measures a defined set repeatedly and makes failures inspectable.

## Important scope

This is a working evaluation foundation, **not a claim of production-grade LLM benchmarking**. Production evaluation should add task-specific rubrics, safety tests, multilingual datasets, hallucination checks, human ratings, versioned prompts/models, and statistical analysis.

## Skills demonstrated

**Python · Generative AI · LLM Evaluation · Experiment Design · Error Analysis · Automation · Testing**
