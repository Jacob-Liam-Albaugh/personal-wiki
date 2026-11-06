---
type: method
area: stochastic
areas: [stochastic, bayesian, me697]
source-ref: "Not in the ME 697 book; background page for sinverse/fs (the book's filter is the particle filter)"
tags: [inverse-problems, bayesian, signals]
---

# Kalman filter

**Wiki note**: the ME 697 book never states the Kalman filter; its filtering chapter (`sinverse/fs`) uses the [[Particle filter]]. This page records the linear-Gaussian case as the exact reference that particle methods approximate. Equations below are the standard ones and are **[unverified]** against any source in the wiki.

> [!definition] Linear-Gaussian [[Stochastic state-space model]]

$$
x_t = F x_{t-1} + q_t,\qquad q_t\sim N(0,Q),
$$

$$
y_t = H x_t + r_t,\qquad r_t\sim N(0,R).
$$

The filtering law $p(x_t\mid y_{1:t})$ is Gaussian, $N(m_t,P_t)$, and is propagated in closed form.

> [!algorithm] Predict and update
> Predict:

$$
m^- = F m_{t-1},
\qquad
P^- = F P_{t-1}F^T + Q.
$$

> Update with gain $K$:

$$
K = P^- H^T\,(H P^- H^T + R)^{-1},
$$

$$
m_t = m^- + K\,(y_t - H m^-),
\qquad
P_t = (I-KH)\,P^-.
$$

## Relation to the book
- Exact for linear drift with additive Gaussian noise, such as an [[Ornstein-Uhlenbeck process]] observed with Gaussian noise.
- The stochastic Duffing oscillator of [[ME697 6.2 - Filtering and smoothing]] has the cubic term $\beta x^3$, so the state law is non-Gaussian and the book uses a bootstrap [[Particle filter]]. Extended and unscented Kalman filters are Gaussian approximations of that case **[unverified]**.
- The Gaussian marginal likelihood from the filter's innovations makes [[Expectation-maximization]] and likelihood calibration exact in the linear case.
- The smoothing analogue is the Rauch-Tung-Striebel smoother **[unverified]**.

**Sources**: none in `advanced-scientific-machine-learning/book/`; context from `sinverse/fs/intro.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Particle filter]] · [[Stochastic state-space model]] · [[Ornstein-Uhlenbeck process]] · [[Gaussian process]]
- [[ME697 6.2 - Filtering and smoothing]]
