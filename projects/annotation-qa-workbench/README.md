# Annotation QA Workbench

## Problem

AI-data teams can receive thousands or millions of human-labelled records. A dataset can look complete while still containing **missing labels, invalid labels, low-confidence annotations, duplicate work, or disagreements between annotators**.

If those records are exported directly into a training or evaluation dataset, the team may discover the problem much later.

## Solution

This project implements a deterministic **Dataset Quality Gate**:

```text
Annotation dataset
       ↓
Schema + policy checks
       ↓
Record-level validation
       ↓
Annotator comparison
       ↓
Confidence checks
       ↓
Severity classification
       ↓
Review queue
       ↓
Human adjudication
       ↓
Approved dataset
```

The system does **not** automatically rewrite disputed labels. It identifies questionable records and routes them to a human reviewer.

## What is actually implemented

### 1. Dataset ingestion
Reads annotation records from CSV.

### 2. Policy-driven validation
`policy.json` defines the allowed labels and low-confidence threshold.

### 3. Record checks
The quality engine detects:
- missing item IDs or annotators
- missing annotations
- invalid labels
- invalid confidence values
- low-confidence annotations

### 4. Cross-annotator checks
Records are grouped by item. When multiple annotators label the same item, the engine measures simple pairwise agreement and creates a high-priority finding when labels conflict.

### 5. Review routing
Each finding contains:
- item ID
- severity
- reason
- human-readable details

The CLI writes those findings to `review_queue.json`.

## Run the system

From this directory:

```bash
python review_queue.py annotations.csv policy.json
```

Then inspect:

```bash
cat review_queue.json
```

## Example dataset

The included dataset contains:
- matching annotations
- one disagreement
- one incomplete annotation
- confidence values

This gives the QA engine both normal and failure cases to process.

## Tests

```bash
python -m pytest tests/
```

Tests cover disagreement routing, missing annotations, low confidence, and invalid labels.

## Why this is useful

The same architecture can be applied to:
- image classification datasets
- object-detection labels
- text classification
- speech/transcription datasets
- video-event annotations
- multimodal evaluation datasets

For a production system, the next layers would include dataset versioning, persistent review state, reviewer authentication, audit history, sampling policies, richer agreement statistics, and connectors for annotation platforms.

## Engineering principle

**Automation decides what deserves attention; humans make the final annotation decision.**

This repository documents the implemented quality gate separately from those future production extensions.
