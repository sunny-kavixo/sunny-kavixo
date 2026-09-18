# Annotation QA Workbench

A practical quality-control tool for human-labelled AI datasets.

## Purpose

When multiple annotators label the same records, a dataset can contain missing labels, invalid labels, disagreements, and inconsistent records. This tool turns those problems into measurable QA findings and a review queue.

## Process

```text
Annotation records
      ↓
Schema + allowed-label checks
      ↓
Completeness checks
      ↓
Annotator agreement
      ↓
Conflict detection
      ↓
Priority review queue
      ↓
Human adjudication
      ↓
Clean dataset
```

## Input

The included `annotations.csv` contains records with an item ID, annotator, label, and confidence.

## Run

```bash
python qa.py annotations.csv
```

## Example output

```text
ANNOTATION QA REPORT
====================
Records: 8
Unique items: 4
Annotators: 2
Missing labels: 1
Invalid labels: 0
Items with disagreement: 1
Agreement: 0.667
Review queue: 2
```

## What the implementation does

- Validates required columns.
- Rejects labels outside the configured label set.
- Detects missing annotations.
- Groups annotations by item.
- Calculates simple pairwise agreement for items labelled by two annotators.
- Creates a review queue for disagreements and missing labels.
- Produces JSON output suitable for downstream automation.

## Test

```bash
python -m pytest tests/
```

## Why this is useful

This is directly applicable to image, text, audio, and multimodal annotation operations. The same QA pattern can sit before a training-data export or model-evaluation dataset.

## Scope

The current implementation intentionally uses transparent deterministic rules. Production annotation programs may add weighted agreement statistics, adjudicator workflows, sampling plans, audit trails, and dataset-version tracking.
