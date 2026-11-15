---
type: paper
area: ift
areas: [ift, bayesian, inverse-problems, physics-informed]
source-ref: "Hao, Bilionis 2024, J. Comput. Phys. 512, 113139"
tags: [ift, vi, bayesian, inverse-problems, physics-informed, uq]
authors: ["[[Kairui Hao]]", "[[Ilias Bilionis]]"]
year: 2024
venue: "Journal of Computational Physics 512, 113139"
file: "papers/IFT/Hao, Bilionis - An information field theory approach to Bayesian state and parameter estimation in dynamical systems.pdf"
---

# IFT approach to Bayesian state and parameter estimation in dynamical systems (Hao 2024)

**Summary**: Extends [[Information field theory]] from boundary-value problems ([[PIFT (Alberts 2023)]]) to ODE initial-value problems. The state path is a linear basis expansion, the physics enters through a path-space prior $e^{-\beta H}$ on the ODE residual, and the posterior over state, initial condition, parameters and trust $\beta$ is fit by stochastic [[Variational inference]], with an inner VI loop for the gradient of the log partition function. It matches NUTS and SMC² on Lotka–Volterra at constant cost as the time window grows, learns a smaller $\beta$ under model-form error, and shows that a B-PINN gets the parameter posterior wrong because it drops the partition function.

**Authors**: Kairui Hao, Ilias Bilionis · **Year**: 2024 · **File**: `papers/IFT/Hao, Bilionis - An information field theory approach to Bayesian state and parameter estimation in dynamical systems.pdf` · **Code**: github.com/PredictiveScienceLab/ift-dynamics-2024

---

## Problem (Sec. 1, p. 3)
Estimate the state path $x(t)$ and parameters $\theta$ of
```
ẋ = f(x, t; θ)
Y(t_k) = R(x(t_k); θ) + noise
```
from noisy, sparse data (eq. 1). The authors list three gaps:
- [[Kalman filter]], [[Particle filter]] and VI filters must discretize time and invent transition noise, which can bias the result.
- B-PINNs put the physics in fictitious observations, so the posterior collapses as collocation points increase; this is bad when the model is wrong.
- [[PIFT (Alberts 2023)]] needed slow [[Nested SGLD]] and covered only BVPs with an energy principle.

## Method

### State path and initial condition (Sec. 2.1–2.2)
- $\hat x(t;w)=\sum_i w_i\psi_i(t)$ with a linear basis (Fourier or RBF).
- The initial condition is built in: one coefficient $w_i$ is solved for from $x_0$ and the others (eqs. 4–5), so the path is $\tilde x(t;w_{-i},x_0)$.

> [!definition] Physics-informed path prior (eqs. 2–3)
> ```
> H = ∫_0^T ‖x̂' − f(x̂, t; θ)‖² dt
> ```
> ```
> p_β(w | x0, θ)
>   = e^{−βH} / Z_β(x0, θ)
> ```
> $\beta$ is an inverse temperature, the trust in the model: $\beta=0$ is flat, $\beta\to\infty$ collapses onto the ODE solution.

Posterior (eq. 7):
```
p(w, x0, θ | y) ∝
  p(y | w, x0, θ) e^{−βH}
  · p(x0, θ) / Z_β(x0, θ)
```
$Z_\beta$ depends on $(x_0,\theta)$ and is intractable; it is what makes the model hierarchical.

### Relation to B-PINNs (Sec. 2.3)
> [!theorem] B-PINN = IFT without the partition function
> A B-PINN with residual noise $\sigma_{yr}$ on a grid of step $\Delta t$ has the same unnormalized posterior with
> ```
> β = 1 / (2 σ_yr² Δt)
> ```
> but omits $Z_\beta(x_0,\theta)$. The conditional posterior over $w$ agrees; the posteriors over $x_0$ and $\theta$ differ, and the B-PINN one is wrong.

### Algorithm (Sec. 2.4, App. C, E)
- Write $H$ as an expectation over $t\sim U[0,T]$ (eq. 13), so it is estimated with random collocation times, as in a [[PINN]].
- **Alg. 1**: VI fit of the prior $p_\beta(w|x_0,\theta)$; [[ELBO]] = $-\mathbb E[h_\beta]$ + entropy.
- **Alg. 2**: posterior ELBO (eq. 17) contains $-\mathbb E[\log Z_\beta(\lambda)]$ with $\lambda=(x_0,\theta)$. Its gradient is a prior expectation (App. C):
```
∇_λ log Z_β
  = −E_prior[ ∇_λ h_β ]
```
- The prior expectation uses an auxiliary guide updated by a persistent inner loop, one inner step per outer step. The estimator is biased; App. E shows the scheme is a max–min problem.
- Guides: diagonal Gaussian for $w$ and $x_0$, full-rank Gaussian for $\theta$, softplus for positive parameters, [[Adam]].

### Hyperparameters (Sec. 2.5)
$\beta$ is a softplus point estimate learned by maximizing the ELBO; $\sigma_y$ has a half-normal prior and a log-normal guide.

### Why a linear basis (App. A)
- The prior is the [[Euler-Maruyama method]] path density of
```
dX = f dt + (2β)^{−1/2} dB
```
  in the small-step limit, i.e. a [[Stochastic differential equation]] with diffusion set by $\beta$.
- A linear basis has a constant Jacobian, so the prior induced on state values does not depend on the basis. A neural-network path would need a Jacobian and would make results parameterization-dependent; this is the gap [[Neural information field filter (Hao 2025)]] addresses.

## Results
> [!example] Three-species Lotka–Volterra (Sec. 3.1–3.2)
> True $(a,b,c,d,e)=(0.1,0.02,0.1,0.02,0.1)$, $x_0=(10,10,10)$, data every 0.5 s with 5% noise; 20-term Fourier basis; 200k Adam steps, lr $10^{-3}\to10^{-4}$.
> - **vs [[NUTS]]** (NumPyro, 1000 warm-up + 5000 samples): as $\beta$ rises from 10 to $10^5$ the IFT posterior converges to NUTS (Fig. 1). At $\beta=10^5$, lengthening $T$ keeps the posteriors matched; IFT time stays flat while NUTS time grows (Fig. 9).
> - **Model-form error**: the truth adds $\alpha x_1x_3$; 100 s of data, $\beta$ learned from 1. Larger $\alpha$ gives smaller learned $\beta$ and wider posteriors, while NUTS on the wrong model stays overconfident (Figs. 3–4). See [[Model-form error detection]].
> - **vs SMC²** (500 parameter × 1000 state particles, auxiliary [[Particle filter]], SDE diffusion $(2\beta)^{-1/2}$): parameters agree as $\beta$ grows; IFT state uncertainty is lower because it solves the smoothing problem while SMC² filters; IFT is faster for $T$ from 10 to 100 s. In SMC², $\beta$ is only a volatility, not a model-trust measure.

> [!example] [[Duffing oscillator]] (Sec. 3.3)
> $\dot x_1=x_2$, $\dot x_2=-\delta x_2-\alpha x_1-\rho x_1^3+\gamma\cos\omega t$ with $\gamma=0.37$, $\omega=1.2$; true $(\delta,\alpha,\rho)=(0.3,-1,1)$. Position only, 50 s at 0.1 s, $x_0=(1,0)$. RBF basis 2×100 (length scale 0.02), $\beta=200$, 100k steps. State and future response are recovered; velocity is more uncertain (Fig. 10).
> A B-PINN on the same data gets the state right but the parameters and the predictive wrong (Figs. 12–13).

## Limitations
- The authors: the inner-loop estimator of $\nabla\log Z_\beta$ is biased; the linear basis must be designed by hand.
- Wiki note: the guides are Gaussian (diagonal on $w$), so posterior correlations between path coefficients are lost; the NUTS agreement is shown only for low-dimensional $\theta$.

## Connections
- Builds on [[PIFT (Alberts 2023)]]: same Boltzmann [[Physics-informed prior]], applied to ODE residuals in time instead of energies in space, with VI in place of [[Nested SGLD]].
- The B-PINN result is the dynamical-system version of the field-collapse argument in [[IFT for engineering inverse problems (Alberts 2024)]] Ch. 5; see [[PINN]].
- The learned-$\beta$ behaviour is an empirical companion to [[MAP uniqueness in IFT (Alberts 2025)]].
- Extended by [[Neural information field filter (Hao 2025)]] (neural paths, no reparameterization) and compared with SGLD in [[Path-space PIFT estimation (Hao 2025)]]. All three are chapters of [[IFT for UQ of differential equations (Hao 2024)]].
- Wiki note: the App. A path density makes this a continuous-time smoother for a [[Stochastic state-space model]] whose process noise is $(2\beta)^{-1/2}$.

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Hidden fluid mechanics (Raissi 2020)]], [[PIFT (Alberts 2023)]], [[PINNs (Raissi 2019)]], [[SGLD (Welling 2011)]], [[VAE paper (Kingma 2014)]]
**Cited by in this wiki**: [[IFT for UQ of differential equations (Hao 2024)]], [[IFT for engineering inverse problems (Alberts 2024)]], [[MAP uniqueness in IFT (Alberts 2025)]], [[Neural information field filter (Hao 2025)]], [[Path-space PIFT estimation (Hao 2025)]]
**Software cited**: [[software#JAX|JAX]], [[software#NumPyro|NumPyro]], [[software#PyTorch|PyTorch]], [[software#Pyro|Pyro]]
%% refs:end %%

**Sources**: `papers/IFT/Hao, Bilionis - An information field theory approach to Bayesian state and parameter estimation in dynamical systems.pdf`.
**Last updated**: 2026-11-15

---

## Related pages
- [[Information field theory]]
- [[Physics-informed prior]]
- [[Variational inference]]
- [[Model-form error detection]]
- [[Kalman filter]]
- [[Particle filter]]
- [[Stochastic state-space model]]
- [[Euler-Maruyama method]]
- [[NUTS]]
- [[PINN]]
- [[Duffing oscillator]]
