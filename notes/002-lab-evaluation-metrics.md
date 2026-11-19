# 002 Lab evaluation metrics: survey notes

Date: 2026-11-19. Result page: `wiki/examples/Lab evaluation metrics.md`.

## Purpose

To learn how the lab judges its models (which metrics, and what it compares against) before I build my own lab models. People covered: Bilionis, Alberts, Bolt, Hans, Dey, Singh, Mirfarah.

## Method

- Four parallel agents gathered the evidence. Synthesis was done by hand.
  1. 13 wiki lab papers, full text.
  2. The SMURF and habitat papers in the wiki.
  3. Bilionis papers online (15).
  4. Alberts, Bolt, Hans, Dey, Singh, Mirfarah online.
- Each record holds: paper, metrics, baselines, data tier, cost reported.
- Evidence levels: full text, or abstract only (marked **[unverified]** on the page).
- Excluded: papers with no lab author, and papers that could not be retrieved (two JCMR 2025 papers by Singh).

## Findings

- **Three-rung validation**: synthetic truth, then a reference solver or MCMC, then an experiment with an outside reference.
- **Point error**: relative L2 against a solver in the surrogate papers; RMSE plus tail percentiles in the engine papers.
- **Calibration**: KS on PIT values with a Q-Q plot is the lab default.
- **Model-form error**: the learned trust β is the signature diagnostic.
- **Cost** is almost always reported, as wall-clock time or forward-model evaluations, against MCMC or the solver.
- **Baselines** are simple: a gold-standard sampler, a solver, a single GP, a plain EKF. Ablations often replace baselines. Bolt 2026 and SMURF are the only papers with a field of ML competitors.

## Gaps

- No NLPD or CRPS.
- No ESS or R-hat, despite SGLD sampling.
- Numeric interval coverage only in Mirfarah 2025 (PICP, PINAW).
- Seed error bars rare.
- No FNO or DeepONet baselines.
- Extrapolation rarely tested.

## Recommendations for my models

1. Synthetic truth with an injected model-form error; report β.
2. Compare against the gold-standard sampler or solver and one simple classical model.
3. Report point error in field units, KS on PIT values, Q-Q plot, and cost.
4. Finish on one experimental dataset with an outside reference and name the failures.
5. Add NLPD or CRPS, numeric coverage, and seed spread. This goes beyond lab practice but outside reviewers expect it.

## Caveats

- Hans BVR, Hans causal-knowledge papers, and Mirfarah's LLM habitat paper: abstract only.
- Anubhav Dey: no papers found. A Purdue Anubhav Dey is in the Vlachos lab; identity not confirmed.
- VAST (Singh, arXiv 2601.13393) has no Bilionis author; included because Singh is in the lab.
- Bolt has one paper, so his section is thin.
- No CSV of the per-paper records was kept; the page tables are the record.
