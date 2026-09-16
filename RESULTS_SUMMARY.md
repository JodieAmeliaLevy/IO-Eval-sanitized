# Results (aggregate)

Full per-step tables and figures appear in the forthcoming preprint. Raw outputs
and transcripts are withheld.

## Scope
- 11,087 graded outputs
- Models: Llama 3.1 8B, Llama 3.3 70B (open-weight); Gemini 2.5 Flash (frontier)
- Languages: English, Russian

## Headline findings
Figures are given in model order: Llama 3.1 8B, Llama 3.3 70B, Gemini 2.5 Flash.

- **Every step is attempted by every model.** Refusal across all 11,087 attempts is 0.5%,
  0.3% and 1.1%, and 97% to 100% of requests are carried out in every task group, so a
  progress count does not separate the models.
- **Refusal depends on conversation length.** On the single-message disinformation probe the
  models cleanly block 53.3%, 66.7% and 71.3% of attempts; on the five-turn adaptive probe
  the block rate is 0.0%, 0.3% and 0.0%. The request wording and the definition of a block
  differ between conditions, so part of the gap is definitional.
- **Quality, not compliance, separates the models.** English quality is 2.41, 2.56 and 2.72
  on the 0 to 3 scale. Community voice authenticity is 1.6 to 2.0 for all three, at or below
  the usable bar.
- **Cross-language gap:** publishable Russian succeeds on 2.5%, 47.5% and 73.8% of attempts
  (one probe, 80 samples per model).
- **AI writing tells have disappeared** from all three models' 2026 outputs, so detection
  screening for them no longer distinguishes anything.
- **Cost:** cost per usable output spans a factor of 40 across the three models and runs
  roughly 32 to 1,333 times below a 2015 human operator baseline of about $0.40 per comment.
  Matching the annual output of the largest documented saturation network with the cheapest
  model costs on the order of $1,080 of inference.

Multipliers and the annual figure are order-of-magnitude estimates: per-sample inference cost
and per-comment human cost are not strictly the same unit.

## Figures (in the preprint; not committed here)
- compliance by phase
- refusal by model, single-message vs five-turn
- English vs Russian quality
- cost per usable output, per model

