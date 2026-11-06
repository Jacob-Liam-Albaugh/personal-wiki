---
type: definition
area: stochastic
areas: [stochastic, bayesian, me697]
source-ref: "ME 697 book, sinverse/fs (02_filter, 03_smoother) and sinverse/cali (02_em_example, 04_pmcmc_example)"
tags: [inverse-problems, bayesian, uq, sampling]
---

# Stochastic state-space model

> [!definition] State-space model for a discretized SDE (source: sinverse/fs/02_filter.ipynb)
> A hidden Markov state $x_t$ with transition density, observed through noise:

$$
x_t \sim p_\theta(x_t\mid x_{t-1},u_t),
\qquad
y_t \sim p_\theta(y_t\mid x_t).
$$

The transition comes from an [[Euler-Maruyama method]] step of an [[Stochastic differential equation]]; the likelihood is typically Gaussian (`GaussianLikelihood`). The package `dax` bundles these as `StateSpaceModel`, `EulerMaruyama`, `GaussianLikelihood`.

Not to be confused with the deep-learning "State space model" of the sequence-model literature (S4, Mamba), see [[State space model]].

## Example: stochastic Duffing oscillator
The oscillator with white-noise forcing $\xi(t)$ is

$$
\ddot x + \delta\dot x + \alpha x + \beta x^3
= \gamma\cos(\omega t) + \sigma\,\xi(t).
$$

Written as a 2D SDE for state $(x,v)$ with noise on both components and discretized by Euler-Maruyama, the transition is Gaussian:

$$
p(x_t\mid x_{t-1},u_t) = N\big(\cdot\,,\ \mathrm{diag}(\sigma_x^2,\sigma_v^2)\,\Delta t\big),
$$

centered at the Euler step, and only $x$ is observed with noise standard deviation $s$. Parameters: $\omega=1.2$, $\alpha=-1$, $\beta=1$, $\delta=0.3$, $\gamma=0.5$, $\sigma_x=0.01$, $\sigma_v=0.05$, $s=0.1$, $\Delta t=0.1$.

## Inference tasks
| Task | Target | Tool |
|---|---|---|
| Filtering | $p(x_t\mid y_{1:t})$ | [[Particle filter]], [[Kalman filter]] if linear-Gaussian |
| Smoothing | $p(x_t\mid y_{1:T})$ | bootstrap smoother |
| Point calibration | $\arg\max_\theta p_\theta(y_{1:T})$ | [[Expectation-maximization]] |
| Posterior calibration | $p(\theta\mid y_{1:T})$ | [[Particle MCMC]] |

The likelihood $p_\theta(y_{1:T})$ is an integral over all state paths, which is why exact calibration is hard.

**Wiki note**: the Duffing text writes $dX_1=X_2$ without $dt$, and gives the control as $\omega\cos(\cdot)$ while the code uses $\gamma\cos(\omega t)$.

**Wiki note**: for the case of an [[Ornstein-Uhlenbeck process]] with Gaussian noise, the model is linear-Gaussian and exact filtering is the Kalman filter.

**Covered in**: ASML book sinverse/fs (ME 697 6.2); ASML book sinverse/cali (ME 697 6.3)
**Sources**: `text_books/advanced-scientific-machine-learning/book/sinverse/fs/02_filter.ipynb`, `03_smoother.ipynb`, `sinverse/cali/02_em_example.ipynb`, `04_pmcmc_example.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Particle filter]] · [[Expectation-maximization]]
- [[Kalman filter]] · [[Particle MCMC]] · [[Euler-Maruyama method]]
