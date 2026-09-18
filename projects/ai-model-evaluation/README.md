# AI Model Evaluation Mini-Lab

A lightweight evaluation harness for comparing model outputs against expected answers.

## Skills demonstrated
- LLM evaluation concepts
- Exact-match and keyword-based scoring
- Error categorisation
- Experiment reporting
- Python automation

## Design
Each evaluation record contains an input, expected answer, and model answer. The evaluator produces aggregate metrics and a per-example error list so failures can be reviewed instead of hidden behind a single score.
