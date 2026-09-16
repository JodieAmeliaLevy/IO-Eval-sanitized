# Evaluating AI Uplift to Influence Operations
### A kill-chain-anchored capability framework

**Status:** Companion release for "One Prompt at a Time: Why Safety Benchmarks Miss
Multi-Step Misuse", NeurIPS 2026 workshop TAE (Trust-AI-Eval): Can We Trust AI Evaluation?
This repository is the **public, sanitized release**. Executable adversarial
artifacts are deliberately withheld. See [`RESPONSIBLE_RELEASE.md`](https://github.com/JodieAmeliaLevy/IO-Eval-sanitized/blob/main/RESPONSIBLE_RELEASE.md).

## Overview
This project measures whether frontier and open-weight models provide meaningful
**uplift** to actors running online influence operations, and anchors that
measurement in a recognised analytic framework so the results are interpretable
and actionable for platforms and regulators rather than ad hoc.

## Method (summary)
- Operationalises the ten-phase Online Operations Kill Chain (Nimmo & Hutchins, 2023)
  into **27 scored steps**, graded for per-step completion.
- Models: two open-weight (Llama 3.1 8B, Llama 3.3 70B) and one frontier (Gemini 2.5 Flash).
- Languages: English and Russian.
- Grading: an LLM judge calibrated against blinded human raters; **11,087 graded outputs**.
- Headline measures: per-step compliance, output quality on a 0 to 3 scale, and refusal
  measured under both single-message and five-turn adaptive prompting. These are reported
  separately; the paper's own checklist advises against combining measures into one score
  before showing that they move together.

Full detail in [`METHODOLOGY.md`](https://github.com/JodieAmeliaLevy/IO-Eval-sanitized/blob/main/METHODOLOGY.md).

## Key findings (high level)
- **All three models attempt every step.** Compliance runs at 97% to 100% in every task
  group and all 27 steps are engaged, so a progress count of the kind used in cyber
  evaluations has no variance to work with.
- **Refusal depends on how long the conversation runs.** A direct single-message request to
  write known disinformation is cleanly blocked on 53.3%, 66.7% and 71.3% of attempts
  (Llama 3.1 8B, Llama 3.3 70B, Gemini 2.5 Flash). Run as the five-turn adaptive workflow
  documented operators use, the block rate is 0.0%, 0.3% and 0.0%. The wording of the
  request and the definition of a block differ between the two conditions, so part of that
  gap is definitional rather than behavioural.
- **Differences show up in quality, not compliance.** English quality scores 2.41, 2.56 and
  2.72 on the 0 to 3 scale, while sounding like a real member of the target community stays
  at 1.6 to 2.0 for every model, at or below the usable bar.
- **Language is the sharpest remaining constraint.** Publishable Russian succeeds on 2.5%,
  47.5% and 73.8% of attempts (one probe, 80 samples per model), so an English-only
  evaluation is blind to it.
- **The 2024 era AI writing tells are gone** from all three models, including the
  open-weight model released in 2024, so a defender screening for them separates nothing.
- **Cost per usable output varies by a factor of 40 across the three models** and sits
  roughly 32 to 1,333 times below a documented 2015 human operator baseline of about $0.40
  per comment. Matching the annual output of the largest documented saturation network with
  the cheapest model costs on the order of $1,080 of inference.

Per-step tables and figures are in the paper. Aggregate results are in
[`RESULTS_SUMMARY.md`](https://github.com/JodieAmeliaLevy/IO-Eval-sanitized/blob/main/RESULTS_SUMMARY.md).

## Repository structure
- `METHODOLOGY.md` — framework, scoring scheme, validity notes.
- `harness.py` — evaluation harness skeleton with a benign placeholder task that demonstrates the pipeline end to end without any influence-operations content.
- `RESULTS_SUMMARY.md` — aggregate findings.
- `RESPONSIBLE_RELEASE.md` — what is withheld and why.
  
## What is withheld
The task bank, elicitation prompts, multi-turn attack scaffolding, and raw model
outputs are **not** included. They are misuse-enabling. Vetted researchers and
auditors can request structured access (see below).

## Running the harness
The harness is built on Inspect, the UK AI Security Institute's open source evaluation framework.The production harness runs against the withheld task bank. The included benign example demonstrates the pipeline without any influence-operations content:
```bash
pip install -r requirements.txt
inspect eval harness.py --model <provider/model>
```

## Citation
See [`CITATION.cff`](https://github.com/JodieAmeliaLevy/IO-Eval-sanitized/blob/main/CITATION.cff)

## Authors
- Jodie Levy, Constellation, Berkeley
- Sumaya Nur Adan, University of Oxford
- Anna Liashenko, University of Valencia

The work was carried out through the International Programme on AI Evaluation,
Capabilities & Safety (ValgrAI / University of Valencia, 2026).

## Access requests
Structured access to withheld artifacts for vetted research or audit - jodieamelialevy@gmail.com

