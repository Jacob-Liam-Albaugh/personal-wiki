---
type: paper
area: bayesian
areas: [bayesian, stochastic]
source-ref: "Lund, Dyke, Song, Bilionis 2019, Nonlinear Dyn. 98:375-394, secs. 2-6, Tables 3-4"
tags: [bayesian, inverse-problems, uq, signals]
authors: ["[[Alana Lund]]", "[[Shirley J. Dyke]]", "[[Wei Song]]", "[[Ilias Bilionis]]"]
year: 2019
venue: "Nonlinear Dynamics 98"
file: "[[papers/Bayesian/Lund, Dyke, Song, Bilionis - Global sensitivity analysis for the design of nonlinear identification experiments.pdf]]"
---

# Sobol sensitivity for identification experiments (Lund 2019)

**Summary**: Uses time-varying [[Sobol indices]] to choose which excitation signals to run when identifying a nonlinear system. On a lab nonlinear energy sink (NES) identified with a joint unscented [[Kalman filter]], a parameter is identified tightly only when the signal excites it strongly and for long enough. The Sobol view predicts this; the UKF variance ratio does not.

**Authors**: Alana Lund, Shirley J. Dyke, Wei Song, Ilias Bilionis · **Year**: 2019 · **File**: [[papers/Bayesian/Lund, Dyke, Song, Bilionis - Global sensitivity analysis for the design of nonlinear identification experiments.pdf]]

---

## Problem (Sec. 1-2)
- Which input signals make the parameters of a nonlinear model identifiable from data, before running the experiment?
- Three kinds of [[Identifiability]]:
  - structural (e.g. DAISY; it cannot handle Coulomb friction, hence $\tanh(200\dot x)$),
  - practical (Monte Carlo, correlation, online covariance such as the variance ratio $\sigma_M/\sigma_0$),
  - sensitivity-based (this paper).
- Same NES model as [[UKF identification of a nonlinear energy sink (Lund 2020)]]:
```
m x'' + c_v x' + c_f tanh(200 x')
  + k x + z x^3 = -m x_g''
```

## Method

> [!definition] First-order Sobol index (eq. 8)
> ```
> S_j = V[ E[Y | theta_j] ] / V[Y]
> ```
> Computed at each time step of the simulated response, with 95% confidence intervals.

> [!algorithm] Saltelli estimator (Sec. 3)
> Matrices A, B and $C_j$ from LPτ quasi-random samples; cost $N(K+1)$ model runs. SALib, $N=1000$, over
> ```
> c_v in [0, 1]     c_f in [0, 1]
> k   in [0, 100]   z   in [5e5, 9e5]
> ```

> [!algorithm] UKF check (Sec. 4, eq. 17-20)
> Joint UKF as in Lund 2020. Noise: $\sigma_d^2=1.44\times10^{-12}$ m², $\sigma_a^2=5.32\times10^{-3}$, base acceleration variance $1.03\times10^{-2}$. 5000 prior trials per signal show the spread of estimates.

## Results

> [!example] Low vs high amplitude sweep (Table 3, signal 3 / signal 4)
> Identified values:
> - $c_v$ 0.283 / 0.330; $c_f$ 0.061 / 0.050
> - $k$ 44.0 / 19.8; $z$ 8.52e5 / 7.12e5
>
> Variance ratio (%):
> - $c_v$ 99.6 / 61.7; $c_f$ 94.4 / 92.3
> - $k$ 36.7 / 15.3; $z$ 97.7 / 0.9
>
> The variance ratio calls $c_f$ unidentifiable, yet $c_f$ is the most precisely identified parameter.

- The low sweep barely excites $z$ and only weakly $k$ and $c_v$; the high sweep excites all four. Sensitivity to $k$ and $c_f$ peaks at the regime transitions (about 20 s and 60 s).
- Spread of the 5000 trial estimates is wide when sensitivity is low and tight when it is high. Both the peak and the duration of high sensitivity matter.

> [!example] Maximum sensitivity per signal (Table 4; c_v, c_f, k, z)
> - 1, sweep 0.1 m/s²: .01, 1, .09, 0
> - 2, sweep 9.4: .27, 1, .42, .89
> - 3: .02, 1, .24, 0
> - 4: .27, 1, .43, .89
> - 5, sine 4.9: .09, 1, .36, .61
> - 6, step: .10, .11, .12, .98
> - 7, BLWN 0.2: .02, 1, .73, 0
> - 8, BLWN 18.2: .22, 1, .34, .62

- Recommended set: signals 2, 4, 5, reduced to 4 and 5.
- Signal numbers here differ from those in the 2020 paper.

## Limitations
- The authors: Sobol analysis is costly; it assumes the model is correct; even signals with high sensitivity give several good models, so whether a signal excites the full behaviour is left open.
- Wiki note: the indices are first order only, so interactions (e.g. $k$ with $z$ in the hardening regime) are not separated.

## Connections
- Applied in [[UKF identification of a nonlinear energy sink (Lund 2020)]] to order the training and selection signals.
- General background: [[Sensitivity analysis]], [[Sobol indices]], [[Identifiability]].

%% refs:start %%
**Cites in this wiki**: [[UKF identification of a nonlinear energy sink (Lund 2020)]]
**Cited by in this wiki**: [[UKF identification of a nonlinear energy sink (Lund 2020)]]
%% refs:end %%

**Sources**: `papers/Bayesian/Lund, Dyke, Song, Bilionis - Global sensitivity analysis for the design of nonlinear identification experiments.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Sobol indices]]
- [[Sensitivity analysis]]
- [[Identifiability]]
- [[Kalman filter]]
- [[Duffing oscillator]]
- [[UKF identification of a nonlinear energy sink (Lund 2020)]]
