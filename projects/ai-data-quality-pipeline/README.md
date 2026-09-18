# AI Data Quality & Evaluation Pipeline

A **working dataset quality-control tool** for AI/ML and annotation workflows. It reads a CSV dataset, validates required fields, detects duplicate identifiers/text, measures missing values, and reports label distribution.

![AI dataset quality pipeline](docs/data-quality-flow.svg)

## What problem it solves

Before training, evaluation, or annotation handoff, bad records can create misleading model results. This project turns common data defects into a repeatable inspection step.

## Process

1. Load the source dataset.
2. Validate the required schema: `id`, `text`, `label`.
3. Count missing values.
4. Detect duplicate IDs and duplicate text.
5. Calculate label distribution.
6. Print a quality report.
7. Review and fix the affected records before downstream AI work.

## Run the included real test dataset

```bash
python pipeline.py sample_data.csv
```

The included dataset intentionally contains defects so the tool can be verified: a missing text value, a duplicate identifier, and duplicate text.

## Automated tests

```bash
python -m pytest tests/
```

The test suite verifies that known defects are detected.

## Example output

```text
AI DATA QUALITY REPORT
========================
Rows: 6
Duplicate IDs: 1
Duplicate text: 1
Missing fields: {'id': 0, 'text': 1, 'label': 0}
Label distribution: {'password_reset': 2, 'delivery': 4}
```

## Skills demonstrated

**Python · AI/ML Data Preparation · Dataset QA · Annotation QA · Data Validation · Error Analysis · Automation · Testing**

## Scope

This is a functioning portfolio implementation. It is not presented as a production enterprise data platform. The architecture is ready to be extended with JSONL/Parquet support, configurable schemas, severity thresholds, CI quality gates, and human review queues.
