---
type: overview
area: bayesian
areas: [bayesian, ift, gp, physics-informed, habitats]
source-ref: "Lab papers by Bilionis, Alberts, Bolt, Hans, Singh, Mirfarah (wiki PDFs plus papers found online, 2014-2026)"
tags: [uq, inverse-problems, gp, sampling, ml]
---

# Lab evaluation metrics

**Summary**: How the Predictive Science Lab judges its models: the metrics each paper reports and what it compares against. The overall picture comes first, then each person. The aim is a reference for building new lab models that will be judged the same way.

**Sources**: 18 lab papers in this wiki (full text) and 33 found online (full text unless marked **[unverified]**, which means abstract only). Work notes: `notes/002-lab-evaluation-metrics.md`.
**Last updated**: 2026-11-19

---

## Overall

### How a result is trusted

Most papers climb the same three rungs.

1. **Synthetic problem with known truth.** Data generated from the model, often with an injected model-form error. Nearly every inference paper starts here.
2. **Reference solver or reference sampler.** A finite-element or finite-volume solve, an analytic solution, or MCMC (NUTS, MALA) is treated as the truth.
3. **Experiment against an outside reference.** Examples are the NASA conductivity report, the Lund UKF results, Cummins drive cycles, the HARSH habitat testbed, and an expert cardiologist's segmentation.

A random train and test split, as in a standard ML benchmark, is rare. Held-out operating conditions are used instead: a new drive cycle, an engine without EGR, a second clinical cohort.

### Metric families

| Family | Metrics | Where |
|---|---|---|
| Point accuracy vs a solver | relative L2 error, mean with percentiles or histograms; R² | Tripathy 2018, Karumuri 2020, Beltran-Pulido 2022, Stowers 2020, [[Multi-fidelity GP for tissue expansion (Lee 2020)]] |
| Point accuracy on signals | RMSE, NRMSE, MAPE, R² | Zinage 2022/24/25, [[Diesel PM as OU process (Bolt 2026)]], [[EKF leak severity (Mirfarah 2025)]], [[Thermomechanical CPT for lunar habitats (Montoya 2025)]] |
| Tail accuracy | 90th, 95th, 98th percentile absolute error | Zinage 2024, 2025 (regulatory peaks matter) |
| Domain accuracy | Dice, Jaccard, surface distance in voxels; particle yield and reliability; re-simulation error | [[SMURF (Hans 2026)]], Singh VAST 2026, Hao 2024 PTV, [[Amortized VI for inverse problems (Karumuri 2024)]] |
| Calibration | KS statistic on PIT values plus a Q-Q plot | Bolt 2026, Alberts 2025 intake manifold, Karumuri 2023, Thomas 2022, Zinage 2024 |
| Coverage | PICP and PINAW; data inside 1/2/3σ bands; standardized residuals inside [-3, 3] | Mirfarah 2025, Bolt 2026, Lee 2020 |
| Match to a reference posterior | posterior overlays; KS between samples | [[IFT state and parameter estimation (Hao 2024)]], [[Variational inverse problems (Tsilifis 2014)]], Karumuri 2024, Alberts 2026 Mercer BNN |
| Model-form error | learned trust β against injected error; β against the integrated squared residual | [[PIFT (Alberts 2023)]], Hao 2024, [[Path-space PIFT estimation (Hao 2025)]], Alberts 2025 intake manifold |
| Physics consistency | RMS divergence and momentum residuals, used where there is no ground truth | SMURF 2026, VAST 2026 |
| Cost | wall-clock time, forward-model evaluations, speed-up over MCMC or the solver, parameter count | Tsilifis 2014, [[Neural information field filter (Hao 2025)]], Karumuri 2020, SMURF, Bolt 2026, [[EWARS leak estimation (Rautela 2023)]] |
| System level | resilience (HRM, DMN, ABM); decision accuracy and latency | [[Communication delays in habitats (Mirfarah 2026)]], Manikkan 2026 |

The lab's signature metric is the **learned trust β**. Inject a known model-form error, then check that β falls as the error grows and that the posterior widens. See [[Model-form error detection]].

The preferred calibration check is **KS on PIT values**. Each measurement is mapped through the predictive CDF:

```
u_i = F_i(y_i)
```

If the model is calibrated, the u_i are Uniform(0, 1). The KS statistic is the largest gap between their empirical CDF and the diagonal:

```
KS = max |ECDF(u) - u|
```

0 is perfect. Values the lab reports range from about 0.06 (Bolt) to about 0.2 (Alberts intake pressure).

### What they compare against

| Kind | Examples |
|---|---|
| The truth itself | analytic solution, synthetic ground truth, FE/FV solver, published results |
| Gold-standard inference | NUTS, MALA, SMC², brute-force search |
| Simple classical model | plain EKF, single GP, single-fidelity GP, NARX, logistic regression, SVM |
| Current practice | Tempus clinical pipeline, the volumetric growth rule, the habitat's rule-based heuristics, B-PINNs |
| Off-the-shelf ML | MedSAM2 zero-shot (SMURF); sparse GP, deep-kernel GP, LSTM, NN, gradient-boosted trees (Bolt) |
| Own ablations | energy vs residual loss, number of RBFs, coupled vs sequential, with or without the residual net, α settings |

Ablations often stand in for baselines. Only two papers run a field of off-the-shelf ML competitors: Bolt 2026 and SMURF.

### What is rarely or never reported

- Proper scoring rules: NLPD and CRPS appear nowhere.
- MCMC diagnostics: ESS and R-hat appear nowhere, even though most papers sample with SGLD.
- Numeric coverage is rare. Most credible intervals are judged by eye; Mirfarah 2025 is the main exception.
- Error bars across random seeds are rare.
- Operator-learning baselines (FNO, DeepONet) do not appear.
- Extrapolation beyond the training range is rarely tested (Tripathy 2018 and the Bolt RMCSET cycle are exceptions).

### What this means for a new lab model

A lab-style evaluation of a new model would:

- start on synthetic data with known truth, including a model-form-error case;
- compare against the gold-standard sampler or solver and one simple classical model;
- report a point error in the field's own units, plus KS on PIT values with a Q-Q plot;
- report cost against the reference;
- end on one experimental dataset with an outside reference, and say where the model fails.

Adding NLPD or CRPS, numeric coverage and seed spread would go beyond current lab practice. Reviewers outside the lab would expect them.

---

## By person

### [[Ilias Bilionis]]

Includes papers led by his students (Tripathy, Karumuri, Hao, Zinage, Thomas, Pandita). Alberts and Bolt have their own sections below.

| Paper | Metrics | Compared against |
|---|---|---|
| Deep UQ, Tripathy 2018 (arXiv 1802.00850) | relative error, R², error of mean and std fields | FV solver, Monte Carlo |
| Deep active subspaces, Tripathy 2019 (arXiv 1902.10527) | RMSE, recovered subspace | gradient-based active subspaces |
| Simulator-free SPDEs, Karumuri 2020 (arXiv 1902.05200) | relative L2, R², moment errors, hours | FVM; energy vs residual loss |
| Thermal preferences, Awalgaonkar 2019 (arXiv 1903.09094) | distance to optimum, hit rate | random search, logistic regression, SVM |
| QoI design, Pandita 2019 (arXiv 1912.07366) | convergence to the true QoI | uncertainty sampling, EI, PI |
| Surgery GP, Stowers 2020 (arXiv 2010.02800) | relative L2, share under 0.1 | FE solves |
| [[Multi-fidelity GP for tissue expansion (Lee 2020)]] | relative error, standardized residuals | single-fidelity GPs |
| Causal BMA, Papamichalis 2021 (arXiv 2105.05395) | QoI probabilities vs truth | PC, hill-climbing |
| Magnetostatic PINN, Beltran-Pulido 2022 (arXiv 2202.04041) | relative L2 percentiles, force error | FE (checked against ANSYS) |
| SFRP inference, Thomas 2022 (arXiv 2202.12881) | surrogate MSE, Q-Q, interval coverage by eye | experiments only |
| Koopman turbine, Zinage 2022 (arXiv 2204.10421) | NRMSE, R², MAPE | NARX; number of RBFs |
| HEA GP, Karumuri 2023 | MAE, KS on PIT | standard GP |
| Diffusion hyperelasticity, Tac 2023 (arXiv 2310.03745) | total variation distance | Gaussian mixture, KDE |
| NOx causal GP, Zinage 2024 (arXiv 2410.18424) | RMSE, tail percentiles, Q-Q | RBF GP, ECM sensor, wrong graphs |
| NOx transfer, Zinage 2025 (arXiv 2511.18178) | RMSE, tail percentiles | uncalibrated GP |
| AM heat PINN, Thomas 2024 | relative L2, error maps | FE solver |
| [[Variational inverse problems (Tsilifis 2014)]] | 95% CI, evaluations, wall-clock | MALA, published values |
| [[Amortized VI for inverse problems (Karumuri 2024)]] | KS vs NUTS, re-simulation error | NUTS |
| [[IFT state and parameter estimation (Hao 2024)]] | posterior overlap, time, β | NUTS, SMC², B-PINNs |
| [[IFT for UQ of differential equations (Hao 2024)]] | same, plus experimental fits | NUTS, SMC², original study |
| [[Neural information field filter (Hao 2025)]] | normalized MSE, wall-clock | Lund UKF; its own sampler variants |
| [[Path-space PIFT estimation (Hao 2025)]] | posterior overlap, time, β | SGLD vs SVI |
| [[Polynomial equipment interfaces (Bilionis 2026)]] | none (proof and worked examples) | none |

Signature: relative L2 against a trusted solver in the surrogate papers, and RMSE with tail percentiles in the engine papers. Calibration comes from KS on PIT values. Baselines are simple.

### [[Alexander Alberts]]

| Paper | Metrics | Compared against |
|---|---|---|
| [[PIFT (Alberts 2023)]] | β vs model-form error, posterior plots, run time | ground truth only |
| [[IFT for engineering inverse problems (Alberts 2024)]] | as PIFT (dissertation) | none |
| [[MAP uniqueness in IFT (Alberts 2025)]] | none (proof) | none |
| Intake manifold, JVVUQ 2025 (doi 10.1115/1.4071047) | KS on PIT, Q-Q, β vs ISR, degraded-data robustness | none run |
| Brownian bridge prior, JUQ 2026 (arXiv 2503.00213) | none (proof) | none |
| Mercer BNN priors, CMAME 2026 (arXiv 2510.23745) | KS vs GP samples, covariance error | true GP, i.i.d. BNN prior |
| [[IFT thermal conductivity (Alberts 2026)]] | MSE and max error in K, 95% CI | NASA reference conductivity |

Signature: calibration (KS on PIT values) and the trust β, rather than RMSE. He tests robustness by degrading the data (more noise, lower sampling rate, an unseen operating cycle) and says where the model fails.

### Maxwell Bolt

| Paper | Metrics | Compared against |
|---|---|---|
| [[Diesel PM as OU process (Bolt 2026)]] | KS on PIT, Q-Q, σ-band coverage, NRMSE, parameter count | sparse GP, deep-kernel GP, NN, LSTM, gradient-boosted trees |

His only paper so far. It has the broadest baseline field in the lab. NRMSE is used because most baselines give no uncertainty.

### [[Atharva Hans]]

| Paper | Metrics | Compared against |
|---|---|---|
| [[SMURF (Hans 2026)]] | Dice, surface distance, divergence and momentum residuals, minutes per case | MedSAM2, Tempus, Tempus+DFW, sequential ablation |
| Paper replication by coding agents, 2026 (arXiv 2607.02134) | targets matched; discrepancy ratio vs the paper's own threshold; hours | the source papers' own numbers |
| Unbalanced OT particle tracking, Hao 2024 (arXiv 2407.04583) | yield and reliability rates | own α and prediction-order ablations |
| BVR particle reconstruction, MST 2024 | detection rate, ghost fraction, RMS pixel error **[unverified]** | synthetic truth, Poiseuille flow |
| Causal-knowledge model, IDETC 2020 / JCISE 2022 | not stated in the abstract **[unverified]** | 3PL item-response model |

Signature: the field's own scalar metrics, judged first on synthetic sweeps, then on an in-vitro case with an analytic answer. In the replication paper the unit of evaluation is a claim that matches a threshold set by the source paper.

### [[Abhishek Singh]]

| Paper | Metrics | Compared against |
|---|---|---|
| [[SMURF (Hans 2026)]] | as above | as above |
| VAST 4D flow, 2026 (arXiv 2601.13393) | Dice, Jaccard, F1, surface distance, RMSE, SSIM, cosine similarity, divergence | PCD, SDM, raw MRI, CFD, Poiseuille |
| Aneurysm growth, Roa Castro 2026 (arXiv 2604.06649) | AUC, Cohen's κ, LOOCV, ICC, posterior P(growth) | volumetric clinical rule, three raters |

Signature: imaging metrics in three tiers (CFD, in-vitro, in-vivo). The aneurysm paper is the most clinical-ML-style evaluation in the lab. Two JCMR 2025 papers could not be read.

### [[Motahareh Mirfarah]]

| Paper | Metrics | Compared against |
|---|---|---|
| [[EKF leak severity (Mirfarah 2025)]] | detection time, NRMSE, PICP, PINAW, run time | plain EKF; EM vs VB |
| [[EWARS leak estimation (Rautela 2023)]] | MAPE, runtime, number of evaluations | brute-force search |
| [[Thermomechanical CPT for lunar habitats (Montoya 2025)]] | NRMSE, PM1-PM3, J1-J4 | FE reference models |
| [[Communication delays in habitats (Mirfarah 2026)]] | HRM, DMN, ABM; Bayesian contrasts | delay and interruption settings |
| LLM habitat decisions, Manikkan 2026 (AERO) | decision accuracy, latency **[unverified]** | rule-based heuristics, three LLMs |

Signature: the only person who reports numeric interval coverage and width (PICP, PINAW). The habitat work is judged at system level, against testbed experiments.

### Anubhav Dey

No papers found. A Purdue Anubhav Dey is in the Vlachos lab, with nothing published yet that could be found.

## Connections

- [[Examples catalogue]]: the problems these metrics are applied to.
- [[Model-form error detection]]: the β diagnostic.
- [[Information field theory]]: the framework behind most of the Alberts and Hao rows.
