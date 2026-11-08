---
type: paper
area: stochastic
areas: [stochastic, ml, uq]
source-ref: "Bolt, Alberts, Desai, Meckl, Bilionis 2026, arXiv 2603.12356v1 [stat.AP]"
tags: [uq, ml, gp, signals, optimization]
year: 2026
venue: "arXiv 2603.12356v1"
file: "papers/ML/Bolt et al - Modeling diesel output particulate matter as the Ornstein-Uhlenbeck process.pdf"
---

# Modeling diesel output PM as the Ornstein-Uhlenbeck process (Bolt 2026)

**Summary**: Engine-out particulate matter (PM) from a diesel engine is modelled as an [[Ornstein-Uhlenbeck process]] whose mean level $\mu_t$ and volatility $\sigma_t$ are linear functions (softplus for $\sigma_t$) of 16 engine signals, with one constant reversion rate $\lambda$. Because the engine signals are piecewise constant between samples, the transition density is the exact Gaussian OU transition, so the 35 parameters are fit by maximum likelihood with [[Adam]]. Evaluated by PIT/Kolmogorov–Smirnov calibration on six Cummins test cycles, it beats GPs, neural nets, LSTM, NARX and gradient boosting on average NRMSE and KS, with at least 100× fewer parameters. It fails on the steady-state-stepping RMCSET cycle, which is out of distribution for the training data.

**Authors**: Maxwell Bolt, Alex Alberts, Akash S. Desai (Cummins), Peter Meckl, Ilias Bilionis (Purdue ME) · **Year**: 2026 · **File**: `papers/ML/Bolt et al - Modeling diesel output particulate matter as the Ornstein-Uhlenbeck process.pdf` · **Code** (synthetic example): github.com/PredictiveScienceLab/ou-pm-paper

---

## Motivation (Sec. 1)
- A GP with a structured deep kernel (as in Zinage 2025 for NOx) gave **correlated standardised errors** on test cycles, so plain regression is the wrong model for transient PM (p. 2).
- [[SINDy]] needs derivatives of noisy signals and failed; [[Neural ODE]]s overfit and diverged (pp. 2–3).
- The same operating point gives different PM from cycle to cycle, so PM is treated as a stochastic process: drift for the dynamics, volatility for the cycle-to-cycle variation (p. 3).
- The RMCSET cycle (Fig. 1) shows the OU picture directly: each steady set point has a mean PM level with noise around it, and after a step the signal relaxes to the new mean.

## Model (Sec. 2.2)
Itô SDE with state-dependent coefficients (eqs. 2–3):
```
dX_t = λ (μ_t − X_t) dt + σ_t dW_t
```
```
μ_t = Σ_i a_i U_i,t + b
σ_t = softplus(Σ_i c_i U_i,t + d)
```
- $U_1..U_{16}$: speed, torque, injection timings and quantities, rail pressure, VGT and EGR actuation, temperatures, air and EGR mass flows, in-cylinder O₂ (Table 1).
- $\theta=(a,c,b,d,\lambda)$, 35 parameters. A deep-net parameterisation overfit (p. 5).
- PM is assumed first-order Markov.

## Training by exact transition likelihood (Sec. 2.3)
[[Euler-Maruyama method]] was unstable at the data's sampling step. Instead the transition comes from the [[Fokker-Planck equation]] (eq. 4), whose Green's function is Gaussian. Taking expectations gives the moments (eqs. 6–7):
```
m(t) = X_0 e^{−λt}
     + λ ∫ μ_s e^{−λ(t−s)} ds
```
```
V(t) = ∫ σ_s² e^{−2λ(t−s)} ds
```
With $\mu,\sigma$ constant over a step $\Delta t$ (eq. 8):
```
m = X_t e^{−λΔt}
  + μ_t (1 − e^{−λΔt})
```
```
V = σ_t²/(2λ) · (1 − e^{−2λΔt})
```
Negative log-likelihood over the series (eq. 10), minimised with minibatched Adam:
```
Σ_i log V(t_i)
  + (Y_i − m(t_i))² / V(t_i)
```

- **Data transform** (Sec. 2.4): divide by the standard deviation, then log below 1 and linear above ($Y=\log Z$ for $Z<1$, $Z-1$ otherwise), so spikes stay expressive.
- **Deployment** (Sec. 2.5): no PM is observed at test time. Start at $X_0=\mu_{t_0}$ (eq. 11), then sample $X_{i+1}=m+\sqrt V\,\eta$ (eq. 12); 10 000 paths.

## Calibration metric (Sec. 2.6)
- Standardised error $e_i=(Y_i-\bar X_i)/s_i$ from the sample mean and standard deviation; PIT value $\Phi(e_i)$.
- If the data come from the model, PIT values are uniform. The KS statistic against uniform scores this (0 is perfect); Q–Q plots show the direction of miscalibration.

## Results
- **Synthetic** (Sec. 3): one piecewise-constant control, trained on the first 7 s of 10 s. Recovered $\lambda$ 10.96 vs 10 (9.6% error, the hardest), $a$, $b$, $\sigma$ within 0.3–6.5% (Table 2); KS 0.091.
- **Engine data** (Sec. 4.1): Cummins B6.7L inline-6, trained on in-house cycles that sweep each control, 15% held out for early stopping. JAX + Equinox + Optax, 1000 epochs in ~135 s on an M2 Max.
- **Test KS** (Table 3): FTP Low NOx 0.085, STC High NOx 0.057, STC Nominal 0.134; FTP Nominal/High 0.29/0.25; RMCSET 0.48. Where it misses, Q–Q plots show consistent **overprediction**.
- **RMCSET**: the predictive distribution is right-skewed and the median overpredicts, but the data stay in the 95% CI (Fig. 7). Adding the first half of RMCSET to training improved KS on five of six cycles (Table 4).
- **Cumulative PM** stays inside the CI for three of six cycles (Fig. 8).

| Model (avg., excl. RMCSET; Table 7) | Params | NRMSE | KS |
|---|---|---|---|
| OU model | 35 | 0.042 | 0.162 |
| Sparse GP (50 inducing) | 3 385 | 0.045 | 0.248 |
| Deep-kernel GP (CNN) | 2.4 M | 0.048 | 0.428 |
| MLP | 46 k | 0.045 | – |
| LSTM | 38 M | 0.050 | – |
| NARX | 89 k | 0.048 | – |
| Gradient boosting | 21 k | 0.049 | – |

The deep-kernel GP was worse than the plain sparse GP everywhere, which the authors read as overfitting or PM being more Markovian than NOx (p. 14).

## Limitations and future work (Sec. 5)
- Linear parameterisation only; neural drift/volatility and a neural-ODE map into OU space both overfit.
- Training data lack steady-state-to-steady-state transitions.
- Proposed: a fully Bayesian treatment of $\mu_t,\sigma_t,\lambda$ with priors for positivity and smoothness, via hierarchical models or scalable VI.

## Connections
- The moment equations are the time-varying form of the constant-coefficient moments on [[Ornstein-Uhlenbeck process]]; the fitting differs from the ME 697 recipe there, which fits $\lambda$ by MSE and simulates with Euler–Maruyama.
- Wiki note: with piecewise-constant inputs this is an AR(1) model with input-dependent mean and heteroscedastic noise, i.e. a linear-Gaussian [[Stochastic state-space model]] observed without noise. Adding measurement noise would make the [[Kalman filter]] the exact likelihood.
- Wiki note: the PIT/KS check is the same calibration idea as the KS-against-MCMC metric in [[Amortized VI for inverse problems (Karumuri 2024)]], but applied to data instead of a reference posterior.
- [[Gaussian process]] regression was the prior best architecture for PM (Shahpouri 2021, as cited p. 2) and is the main benchmark here.

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Neural ODEs (Chen 2018)]], [[SINDy (Brunton 2016)]]
**Software cited**: [[software#JAX|JAX]], [[software#PyTorch|PyTorch]], [[software#scikit-learn|scikit-learn]]
%% refs:end %%

**Sources**: `papers/ML/Bolt et al - Modeling diesel output particulate matter as the Ornstein-Uhlenbeck process.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Ornstein-Uhlenbeck process]]
- [[Stochastic differential equation]]
- [[Fokker-Planck equation]]
- [[Euler-Maruyama method]]
- [[Stochastic state-space model]]
- [[Gaussian process]]
- [[SINDy]]
- [[Neural ODE]]
- [[Adam]]
