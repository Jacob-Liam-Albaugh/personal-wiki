---
type: paper
area: habitats
areas: [habitats, bayesian]
source-ref: "Mirfarah, Lund, Dyke 2025, AIAA J. 63(4), secs. II-VI, Tables 3-5"
tags: [bayesian, uq, inverse-problems]
authors: ["[[Motahareh Mirfarah]]", "[[Alana Lund]]", "[[Shirley J. Dyke]]"]
year: 2025
venue: "AIAA Journal 63(4)"
file: "[[papers/Space Habitats/Mirfarah, Lund, Dyke - Estimation of Pressure Leakage Severity for Space Habitats Using Extended Kalman Filter.pdf]]"
---

# EKF leak severity (Mirfarah 2025)

**Summary**: Estimates the effective leak area $A_e$ of a pressurized habitat from pressure alone, using an [[Kalman filter]] extended (EKF) to an augmented state $[p_{int}, A_e]$, then converts the estimate into a time-to-critical (TTC) forecast with a first-passage-time Monte Carlo. Noise statistics are tuned by [[Expectation-maximization]] (EKF+EM) or by variational Bayes (EKF+VB). EKF+EM is the most reliable and least sensitive to priors; the online (downsampled) variant makes it real time.

**Authors**: Motahareh Mirfarah, Alana Lund, Shirley J. Dyke · **Year**: 2025 · **File**: [[papers/Space Habitats/Mirfarah, Lund, Dyke - Estimation of Pressure Leakage Severity for Space Habitats Using Extended Kalman Filter.pdf]]

---

## Problem (Sec. I-II)
- A micrometeorite breach leaks air; the habitat needs the leak severity and the time left before pressure is unsafe, from noisy pressure data in real time.
- Test bed (II.A): lab pressure box, 1020 steel with 6061-T6 Al lid, interior 0.8 x 0.4 x 0.4 m, wall 13 mm; mass flow controller, Omega transducer, Speedgoat at 1 kHz. Fill 202.65 kPa vs 101.32 kPa ambient. Leak at $t=30$ s, constant 4.35 L/min, equivalent to $A_e = 0.2$ mm$^2$.

## Method

> [!definition] Leak model (II.B, eq. 1-3)
> Two-stage depressurization ODE (choked Stage I, unchoked Stage II). Only Stage I is used; the choked threshold is 191.5 kPa. $C_d=0.8$, $\gamma=1.4$.

> [!algorithm] EKF (III.A, eq. 6-7, Alg. 1)
> State $z=[p_{int}, A_e]$, Euler-discretized ODE, $A_e$ random walk. Process noise $Q=\mathrm{diag}(\sigma_q^2\,dt,\ \epsilon)$, measurement noise $R=\sigma_r^2$.

> [!algorithm] EKF+EM (III.B)
> $\theta=[Q,R,z_{0|0},P_{0|0}]$. E-step = EKF forward pass plus smoother; stop at relative change < 1e-3. Online version uses batches of 3 s.

> [!algorithm] EKF+VB (III.C, eq. 9-11)
> Inverse-gamma hyperprior on each noise variance, mean-field posterior, $\alpha_{post}=\alpha_0+\tfrac12$, $\beta_{post}=\beta_0+\tfrac12 r^2$, MAP $\sigma^2=\beta/(\alpha+1)$. See [[Variational inference]].

> [!definition] Time to critical (III.D, eq. 12)
> ```
> t_FPT = inf{ t :
>   x(t + t_k | t_k) <= w }
> ```
> First passage of pressure below the unsafe threshold $w=191.5$ kPa (safe range 70-101 kPa, factor 1.3). Monte Carlo, $N=1000$ particles, mean and 2.5/97.5 percentiles.

## Results

### Metrics (IV.B, eq. 13-16), applied to both $A_e$ and TTC
```
t_FDT = inf{ t_i - t0 :
  |(Xhat_i - X_i)/X_i| < eps },
  eps = 0.25   (tables: "TFDP")
NRMSE(%) = sqrt( (1/n) sum_i
  ((Xhat_i - X_i)/X_i)^2 )
  (TTC: sum to 0.95 n)
PICP = (1/n) sum_i kappa_i,
  kappa_i = 1 if X_i in
  [Xhat_L, Xhat_U] (95% central)
PINAW = (1/(n W)) sum_i
  (Xhat_U - Xhat_L)
  W = 0.5 mm^2 for A_e,
  total sim time for TTC
```
Execution time is cumulative run time.

> [!example] Numerical study (IV.A, Table 3)
> Leak at 40 s; $T_0=26.85$ C, $P_0=202.65$ kPa; $dt=0.02$ s over 160 s; $A_e=0.22$ mm$^2$; $\sigma_q=0.004$, $\sigma_r=0.4$. All methods converge after about 60 s; EM is fastest, VB most conservative. Averages over the Table 2 parameter study (A_e: EKF / EM / VB):
> - $\sigma_q=4\mathrm{e}{-3}$: TFDP 71.66 / 23.35 / 80.91 s; NRMSE 61.47 / 29.37 / 65.64 %; PICP 28.49 / 42.84 / 40.44 %; PINAW 37.13 / 6.85 / 45.75 %.
> - TTC at 4e-3: TFDP 78.40 / 8.66 / 86.80 s; NRMSE 693.83 / 52.22 / 733.49 %.
> - $\sigma_q=2\mathrm{e}{-2}$, A_e NRMSE 61.83 / 30.35 / 66.50 %; TTC NRMSE 920.90 / 49.13 / 787.53 %.

> [!example] Run time (Table 4; Matlab 2022b, i7-12700, 64 GB)
> EKF 0.6334 s, EKF+EM 73.7805 s (x116.5), EKF+VB 0.6352 s (x1.003).

> [!example] Experiment (V, Table 5; A_e: EKF / VB / EM full / EM online)
> - TFDP: 28.88 / 120.00 / 1.72 / 6.09 s.
> - NRMSE: 27.07 / 84.24 / 10.05 / 10.68 %.
> - PICP: 96.40 / 98.96 / 53.66 / 36.59 %.
> - PINAW: 49.33 / 77.27 / 5.83 / 2.48 %.
> - TTC NRMSE: 213.73 / 967.89 / 7.57 / 23.06 %.
> EM (online) downsamples to 0.1 s (30 points per batch); EM (full) uses 0.001 s.

- EKF is sensitive to large $\sigma_{q,0}$ and over-confident $\sigma_{A_e,0}$; under-estimated $\sigma_{q,0}$ gives overconfident intervals. Guideline: $\sigma_{A_e,0}$ large but plausible, $\sigma_{q,0}$ below the $A_e$ variance.
- VB does not beat the plain EKF (Fig. 9).

## Limitations
- The authors: leak area is assumed constant; Stage I (choked) flow only; EM intervals are overconfident (low PICP) though conservative in TTC.
- Wiki note: the paper's baseline is the plain EKF with hand-set priors; there is no comparison to a [[Particle filter]] or an unscented filter, and the VB failure is attributed to the mean-field independence assumption without a test.

## Connections
- Prior art for the same test bed: [[EWARS leak estimation (Rautela 2023)]] (batch search, no UQ); this paper adds uncertainty and TTC.
- The TTC output feeds the time-to-criticality idea in [[Communication delays in habitats (Mirfarah 2026)]].
- Estimator is a [[Stochastic state-space model]] filter; EM and VB tuning follow [[Expectation-maximization]] and [[Variational inference]].

%% refs:start %%
**Cites in this wiki**: [[EWARS leak estimation (Rautela 2023)]]
**Cited by in this wiki**: [[Communication delays in habitats (Mirfarah 2026)]]
%% refs:end %%

**Sources**: `papers/Space Habitats/Mirfarah, Lund, Dyke - Estimation of Pressure Leakage Severity for Space Habitats Using Extended Kalman Filter.pdf`.
**Last updated**: 2026-11-19

---

## Related pages
- [[Kalman filter]]
- [[Expectation-maximization]]
- [[Variational inference]]
- [[Stochastic state-space model]]
- [[Particle filter]]
- [[EWARS leak estimation (Rautela 2023)]]
