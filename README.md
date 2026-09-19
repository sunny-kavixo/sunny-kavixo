<div align="center">

# Sandeep 👋

### AI Data • Physical AI • Robotics • Generative AI • Automation

I build **practical engineering systems** and document the problem, implementation, tests, evidence, limitations, and measurable output. This profile is a portfolio of work—not a list of unverified technology claims.

[GitHub](https://github.com/sunny-kavixo) · [KAVIXO](https://kavixo.in)

</div>

---

## Featured engineering work

### 01 · Physical AI Robot Task Evaluator
**Python · DROID · Robot Telemetry · Computer Vision · Physical AI**

A real robot-task evaluation prototype built around DROID manipulation episodes. It evaluates the ordered stages **Approach → Grasp → Lift → Transport → Place → Release**, combines telemetry with visual evidence, and produces JSON/HTML reports.

**Verified demo:** DROID Episode 0 — `Put the marker in the pot`, 166 robot steps.

**Automatic telemetry path:** Grasp, Lift, Transport, and Release are established; Approach and Place remain `UNKNOWN` without trustworthy object-relative visual evidence.

**Validation:** full repository test suite — **31/31 tests passed** on the final demo revision.

[Open project](https://github.com/sunny-kavixo/physical-ai-robot-task-evaluator)

### 02 · AI Data Quality Pipeline
**Python · Dataset QA · AI/ML Data**

A command-line quality-control system that detects missing fields, duplicate records, duplicate text, and label-distribution issues before data reaches a training or evaluation workflow.

**Inside:** source data · implementation · tests · reproducible output · documented limitations

[Open project](projects/ai-data-quality-pipeline)

### 03 · Annotation QA Workbench
**Python · AI Data Operations · Quality Engineering**

A deterministic dataset quality gate for human-labelled AI data. It checks missing/invalid annotations, confidence values, cross-annotator disagreement, and routes questionable records to a human review queue.

**Inside:** policy-driven validation · disagreement checks · review routing · tests

[Open project](projects/annotation-qa-workbench)

### 04 · AI Model Evaluation Lab
**Python · LLM Evaluation · Generative AI**

A repeatable evaluator that compares model outputs with expected answers, calculates deterministic metrics, and exposes failed examples for human error analysis.

**Inside:** evaluation dataset · scoring code · failure cases · tests · documented scope

[Open project](projects/ai-model-evaluation)

### 05 · Autonomous Robot Control Core
**Python · Robotics · Raspberry Pi Architecture · Safety Logic**

A hardware-independent control layer that converts distance telemetry and perception state into deterministic motion decisions. Safety behavior can be tested before motor hardware is connected.

**Inside:** control logic · safety rules · automated tests · hardware integration boundary

[Open project](projects/robotics-vision-demo)

---

## What I work on

| Area | Portfolio evidence |
|---|---|
| Physical AI / Robotics | Real DROID evaluation, telemetry events, robot control and safety logic |
| AI / Data | Dataset quality checks, annotation QA, disagreement review |
| Generative AI | Deterministic model evaluation and failure analysis |
| Computer Vision | Detection/tracking experiments and evidence-aware visual validation |
| Software | Python, TypeScript, JavaScript, web architecture |
| Automation | GitHub workflows, n8n, backend workflows |
| Systems | Linux, debugging, technical operations, Raspberry Pi |

---

## Engineering workflow

```text
Real problem
    ↓
Define inputs + expected behavior
    ↓
Build the smallest useful system
    ↓
Test normal + failure cases
    ↓
Measure and inspect output
    ↓
Document decisions + limitations
    ↓
Improve from evidence
```

I intentionally separate **implemented functionality** from future ideas. A reviewer should be able to inspect the repository and understand what is automatic, what was manually validated, and what remains experimental.

---

## Technical skills

**Programming:** Python · TypeScript · JavaScript · HTML5 · CSS3

**AI / Data:** Dataset preparation · Data quality · Annotation QA · Error analysis · LLM evaluation · Generative AI · Multimodal data concepts

**Physical AI / Robotics:** Robot telemetry · Task-stage evaluation · Raspberry Pi · Autonomous systems · Sensor integration · Safety logic · Motor-control architecture

**Computer Vision:** Detection/tracking foundations · Temporal visual analysis · Evidence validation

**Systems & Engineering:** Linux · Git · GitHub · Testing · Debugging · REST/API concepts · Technical documentation

**Backend & Automation:** Supabase · PostgreSQL · n8n · Netlify · Cloudflare

---

## KAVIXO

KAVIXO is an education and career technology product being developed under Sunny AI Solutions. The main product repository is private; this public profile exposes selected engineering work without presenting private functionality as publicly reproducible.

---

## Portfolio standard

- No fake users, revenue, deployments, accuracy, or performance claims.
- No experimental AI output presented as production capability.
- Tests accompany important deterministic logic.
- Failure cases and limitations are documented where useful.
- Human validation and automatic results are clearly separated.
- Future work is separated from completed work.

### Build · Test · Measure · Improve

## Development transparency

Development may use modern engineering assistants for research, brainstorming, code drafting, debugging, and documentation. The standard is that resulting work is reviewed, tested, understood, and represented accurately.

For portfolio work:

- requirements are defined before implementation;
- code is reviewed and tested rather than accepted blindly;
- important behavior uses reproducible inputs and tests;
- failed experiments and limitations are documented;
- claims are limited to functionality that can actually be demonstrated.

**The goal of this profile is independently inspectable engineering work, not inflated claims.**
