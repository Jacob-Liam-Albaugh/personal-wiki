---
type: definition
area: stochastic
areas: [stochastic, me697]
source-ref: "ME 697 book, sinverse/sodes/03_stochastic_exponential_growth.ipynb"
tags: [sampling, uq, inverse-problems]
---

# Geometric Brownian motion

> [!definition] Geometric Brownian motion (GBM) (source: sinverse/sodes/03_stochastic_exponential_growth.ipynb)
> The [[Stochastic differential equation]] with multiplicative noise:

$$
dX_t = \mu X_t\,dt + \sigma X_t\,dW_t.
$$

It models stochastic exponential growth: the relative increment has constant drift $\mu$ and constant volatility $\sigma$.

## Log transform
By Itô's lemma, $Y=\ln X$ satisfies

$$
dY_t = \Big(\mu-\tfrac{\sigma^2}{2}\Big)dt + \sigma\,dW_t.
$$

So $Y$ is [[Brownian motion]] with drift, and $X$ is lognormal. With $\theta=\mu-\sigma^2/2$, increments on a grid are independent:

$$
\Delta Y_i \sim N\big(\theta\,\Delta t_i,\ \sigma^2\Delta t_i\big).
$$

## Maximum likelihood
Minimizing the negative log-likelihood gives closed forms:

$$
\hat\theta = \frac{\sum_i \Delta Y_i}{\sum_i \Delta t_i},
$$

$$
\hat\sigma^2 = \frac1N\sum_i\frac{(\Delta Y_i-\hat\theta\,\Delta t_i)^2}{\Delta t_i},
$$

$$
\hat\mu = \hat\theta + \tfrac12\hat\sigma^2.
$$

With $R$ replicate series the sums run over replicates too and the denominators become $R\sum\Delta t$ and $RN$.

> [!example] Cancer-cell growth
> Counts from Johnson et al. (PLOS Biology), seeding levels near 2, 4 and 10 cells. Fit on the 10-cell series for $t<250$ h: $\hat\mu=0.010$, $\hat\sigma=0.073$. The prediction median tracks the trend, but sample paths do not resemble individual replicates, so a richer model is needed (source: 03_stochastic_exponential_growth.ipynb). Initial conditions are lognormal, fitted from data, and the prediction to 350 h uses 1000 simulations (median, 95% interval); the file is `cancer_growth.csv`.

## Simulation
[[Euler-Maruyama method]]: $X_{t+\Delta t}=X_t+\mu X_t\Delta t+\sigma X_t\sqrt{\Delta t}\,Z$, run with `lax.scan`. Zero counts must be replaced (the book uses $10^{-6}$) before taking logs.

**Wiki note**: the notebook text gives the increment variance as $\sigma^2X\Delta t$; it should be $\sigma^2X^2\Delta t$. Euler-Maruyama can go negative for large steps while the exact GBM stays positive, which is another reason to use the log form for fitting **[unverified]**.

**Covered in**: ASML book sinverse/sodes (ME 697 6.1)
**Sources**: `text_books/advanced-scientific-machine-learning/book/sinverse/sodes/03_stochastic_exponential_growth.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Stochastic differential equation]]
- [[Ornstein-Uhlenbeck process]] · [[Euler-Maruyama method]] · [[Brownian motion]] · [[Wiener process]]
