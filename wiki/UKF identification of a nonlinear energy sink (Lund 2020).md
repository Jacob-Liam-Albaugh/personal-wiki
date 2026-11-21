---
type: paper
area: bayesian
areas: [bayesian, stochastic]
source-ref: "Lund, Dyke, Song, Bilionis 2020, Mech. Syst. Signal Process. 136, 106512, secs. 2-6, Tables 3-6"
tags: [bayesian, inverse-problems, uq, signals]
authors: ["[[Alana Lund]]", "[[Shirley J. Dyke]]", "[[Wei Song]]", "[[Ilias Bilionis]]"]
year: 2020
venue: "Mechanical Systems and Signal Processing 136"
file: "[[papers/Bayesian/Lund, Dyke, Song, Bilionis - Identification of an experimental nonlinear energy sink device using the unscented Kalman filter.pdf]]"
---

# UKF identification of a nonlinear energy sink (Lund 2020)

**Summary**: Identifies a lab nonlinear energy sink (NES), a [[Duffing oscillator]] with viscous and Coulomb damping, from measured data using a joint unscented [[Kalman filter]] (UKF) over state and parameters. The UKF result depends strongly on the prior, so the paper runs 5000 prior trials and compares three ways of choosing among them. The robust choice trains on a less sensitive signal and selects on a more sensitive one, with the order set by [[Sobol indices]].

**Authors**: Alana Lund, Shirley J. Dyke, Wei Song, Ilias Bilionis · **Year**: 2020 · **File**: [[papers/Bayesian/Lund, Dyke, Song, Bilionis - Identification of an experimental nonlinear energy sink device using the unscented Kalman filter.pdf]]

---

## Problem (Sec. 1-3)
- An NES is a small, strongly nonlinear attachment that absorbs vibration. Its model must hold over many amplitudes, so the identified parameters have to be good beyond the training signal.
- Test bed: NES of mass 0.65 kg on a shake table, sampled at 4096 Hz, 8 excitation signals. Signals 1-2 identify; 3-8 only evaluate.

> [!definition] NES model (eq. 1)
> ```
> m x'' + c_v x' + c_f tanh(200 x')
>   + k x + z x^3 = -m x_g''
> ```
> $\tanh(200\dot x)$ smooths Coulomb friction so the model is differentiable.

## Method

> [!algorithm] Joint UKF (Sec. 3)
> Augmented state = displacement, velocity, and the four parameters, scaled and log-transformed so they stay positive. Sigma-point weights $\alpha=1,\beta=3,\kappa=0$. $Q$ and $R$ come from a 60 s record with zero command.

> [!algorithm] Prior study (Sec. 4)
> [[Latin hypercube sampling]] of 500 prior means, each with 10 covariance scales from 0.1% to 600%: 5000 UKF runs. Each run's final parameters give a model.

> [!definition] Selection metric
> Normalized mean squared error between simulated and measured response; under Gaussian noise this is the log-likelihood.

> [!algorithm] Three selection approaches (Sec. 5)
> - **A**: train and select on the same signal. Overfits.
> - **B**: stack signals 1 and 2. Signal 1 dominates.
> - **C**: train on signal 2 (lower sensitivity), select on signal 1 (higher). The order comes from Sobol indices. Most robust.

## Results

> [!example] Sobol first-order indices (c_v, c_f, k, z)
> - Signal 1: 0.27, 1.00, 0.43, 0.89.
> - Signal 2: 0.09, 1.00, 0.36, 0.61.

> [!example] Approach C, minimum-MSE model
> ```
> c_v = 0.296   c_f = 0.075
> k   = 43.2    z   = 6.23e5
> ```
> MSE/1e8: validation 0.7; evaluation signals 3-8: 1.2, 0.6, 1.1, 17.1, 5.6, 113.6.

> [!example] "Sub-modal" model
> The mode of the 500 per-mean best models:
> ```
> c_v = 0.344   c_f = 0.064
> k   = 33.1    z   = 6.54e5
> ```
> Validation 0.9; evaluation 1.3, 0.7, 6.9, 10.5, 2.0, 68.6. Better on the hardest signals (6 and 8) than the min-MSE model.

- 15-20% of trials failed with a singular covariance $P$.
- A band-limited white noise (BLWN) training signal gives similar results to signal 2.
- The data are published (ref. [48] of the paper).

## Limitations
- The authors: the UKF needs many prior trials; no single model is best on every evaluation signal; selection uses a point metric, not a posterior.
- Wiki note: the "prior study" is a brute-force search over UKF initialisations. A posterior over parameters (e.g. [[Particle MCMC]] or the IFT methods below) would replace the selection step with uncertainty.

## Connections
- [[Neural information field filter (Hao 2025)]] reuses this data and model. Its "Lund's estimates" ($c_\nu=0.344$, $k=33.1$, $z=6.54\times10^5$) are the sub-modal model here, not the min-MSE model.
- The sensitivity ranking of signals comes from [[Sobol sensitivity for identification experiments (Lund 2019)]].
- Filter class: [[Kalman filter]] on a [[Stochastic state-space model]]; identifiability ideas in [[Identifiability]].

%% refs:start %%
**Cites in this wiki**: [[Sobol sensitivity for identification experiments (Lund 2019)]]
**Cited by in this wiki**: [[Neural information field filter (Hao 2025)]], [[Sobol sensitivity for identification experiments (Lund 2019)]]
%% refs:end %%

**Sources**: `papers/Bayesian/Lund, Dyke, Song, Bilionis - Identification of an experimental nonlinear energy sink device using the unscented Kalman filter.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Kalman filter]]
- [[Sobol indices]]
- [[Duffing oscillator]]
- [[Latin hypercube sampling]]
- [[Identifiability]]
- [[Sobol sensitivity for identification experiments (Lund 2019)]]
- [[Neural information field filter (Hao 2025)]]
