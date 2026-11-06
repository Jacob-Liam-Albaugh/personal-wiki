---
type: definition
area: stochastic
areas: [stochastic, math]
source-ref: "Li, Lecture 12; Deheuvels 2006"
tags: [uq, gp]
---

# Wiener process

**Summary**: The mathematical model of [[Brownian motion]]: a Gaussian process $W_t$ with continuous paths, $W_0=0$, independent Gaussian increments and covariance $s\wedge t$.

---

## Definition

$W_t$ is a centered [[Gaussian process]] with

$$K(s,t)=\mathbb E[W_sW_t]=s\wedge t$$

so $W_t-W_s\sim\mathcal N(0,t-s)$ independently over disjoint intervals (source: Li, §1).

## Expansions

KL series on $[0,1]$ (source: Li, eq. 1.6):

$$W_t=\sum_{k\ge1}\alpha_k\frac{\sqrt2}{(k-\frac12)\pi}\sin\big((k-\tfrac12)\pi t\big)$$

with $\alpha_k$ iid $\mathcal N(0,1)$. The mean-centered process gives a cosine series with eigenvalues $1/(k\pi)^2$ (source: Deheuvels 2006, Thm 1.1). The Haar construction integrates a Haar basis against iid normals (source: Li, Thm 1.7).

## Random-walk construction and bridges (book, 02_bm)
Donsker: a random walk $S_n=\sum_{i\le n}X_i$ with $E[X_i]=0$, $V[X_i]=1$, rescaled diffusively,
$$
W(t) = S_{nt}/\sqrt{n},
$$
converges to Brownian motion. Simulate with $W(t+\Delta t)=W(t)+\sqrt{\Delta t}\,Z$; 1000 samples recover $E[W(t)]=0$, $V[W(t)]=t$.

The Brownian bridge pins the endpoint:
$$
B(t) = W(t) - \tfrac{t}{T}\,W(T),
\qquad V[B(t)] = t(1-t)\ \ (T=1).
$$
Its KL expansion uses eigenfunctions of the Dirichlet Poisson problem:
$$
B(t) = \sum_{n\ge1} Z_n\,\frac{\sqrt2\,\sin(n\pi t)}{n\pi}.
$$
With 100 terms paths look rough; 1000 terms and 1000 samples recover the variance. The book's "Brownian sheet" ("basically a 2D Brownian bridge") is
$$
B(t_1,t_2) = \sum_{n,m} Z_{nm}\,\frac{2\sin(n\pi t_1)\sin(m\pi t_2)}{nm\,\pi^2}.
$$

## Path properties (source: Li, §2)

- Scaling: $cW_{t/c^2}$ is again a Wiener process.
- Quadratic variation $\langle W,W\rangle_t=t$, written $dW^2=dt$.
- Infinite variation on every interval, Hölder of every order below $\tfrac12$, nowhere differentiable.

Wiki note: a product-of-sines field vanishing on all edges (the book's 2D sheet) is a pinned, pillow-type field; the standard Brownian sheet has a different KL basis and is zero only on the two axes **[unverified]**.

Wiki note: the $\mathcal N(0,t)$ marginal is the diffusion solution Einstein derived ([[Brownian movement (Einstein 1905)]]); the noise in [[Langevin dynamics]] is $dW$.

**Covered in**: ASML book sinverse/sodes (ME 697 6.1)
**Sources**: Li; Deheuvels 2006.
**Last updated**: 2026-11-06

---

## Related pages
- [[Brownian motion]]
- [[Karhunen-Loève expansion]]
- [[Mercer's theorem]]
- [[Brownian motion construction (Li n.d.)]]
- [[KL expansions of the Wiener process (Deheuvels 2006)]]
- [[Wiener-Askey chaos (Xiu 2002)]]
- [[Stochastic differential equation]].
