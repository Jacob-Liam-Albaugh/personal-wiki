---
type: paper
area: stochastic
areas: [stochastic, math]
source-ref: "Deheuvels 2006, IMS Lecture Notes 51, Thm 1.1, 1.3"
tags: [uq, gp]
authors: ["[[Paul Deheuvels]]"]
year: 2006
venue: "IMS Lecture Notes-Monograph Series, High Dimensional Probability, Vol. 51, pp. 62-76"
file: "Stochastic Methods/Deheuvels - Karhunen-Loeve Expantions of mean-centered Wiener Processes.pdf"
---

# KL expansions of the Wiener process (Deheuvels 2006)

**Summary**: Gives closed-form [[Karhunen-Loève expansion]]s of the mean-centered [[Wiener process]] $W(t)-\int_0^1W$, which are cosine series, and of its weighted version, whose eigenfunctions are Bessel functions. As a by-product, the $L^2[0,1]$ norm of the weighted mean-centered process has the same law as that of a weighted Brownian bridge.

**Authors**: Paul Deheuvels · **Year**: 2006 · **File**: `Stochastic Methods/Deheuvels - Karhunen-Loeve Expantions of mean-centered Wiener Processes.pdf`

---

## Problem

The KL expansions of the Brownian bridge $B(t)=W(t)-tW(1)$ are classical. The paper asks for the expansion of the mean-centered process $W_0(t)=W(t)-\int_0^1W(u)\,du$ and its weighted generalisations (Abstract, p. 62).

## Method

Basic facts recalled (§1.1, pp. 62-63): a centered Gaussian process $\zeta$ on $[0,1]^d$ with covariance $K_\zeta\in L^2$ has
$$\zeta(t)\overset{\text{law}}{=}\sum_{k\ge1}\omega_k\sqrt{\lambda_k}\,e_k(t),\qquad\omega_k\ \text{iid}\ \mathcal N(0,1)$$
(eq. 1.3), with $(\lambda_k,e_k)$ the eigenpairs of the covariance integral operator (eq. 1.5). A direct consequence is
$$\int\zeta^2\ \overset{\text{law}}{=}\ \sum_k\lambda_k\omega_k^2\qquad\text{(eq. 1.6)}.$$

> [!theorem] Mean-centered Wiener process (Thm 1.1, p. 63)
> $$W(t)-\int_0^1W(u)\,du\ \overset{\text{law}}{=}\ \sum_{k\ge1}\omega_k\frac{\sqrt2\cos(k\pi t)}{k\pi}.$$
> The Brownian bridge has the sine analogue
> $$B(t)\overset{\text{law}}{=}\sum_{k\ge1}\omega_k\frac{\sqrt2\sin(k\pi t)}{k\pi}$$
> (eq. 1.8, cited as known).
>
> (source: Deheuvels - Karhunen-Loeve Expantions of mean-centered Wiener Processes.pdf, eq. 1.7-1.8)

Both give the same eigenvalues $1/(k\pi)^2$, hence
$$\int_0^1\Big(W-\int_0^1W\Big)^2\ \overset{\text{law}}{=}\ \int_0^1B^2\ \overset{\text{law}}{=}\ \sum_k\frac{\omega_k^2}{k^2\pi^2}\qquad\text{(eq. 1.9)}.$$

Proof route (§2.1, pp. 70-71): the covariance is
$$K_{W_0}(s,t)=s\wedge t-s-t+\tfrac12s^2+\tfrac12t^2+\tfrac13.$$
Differentiating the eigen-equation $\lambda y=\int K_{W_0}(\cdot,u)y(u)\,du$ twice turns it into an ODE:
$$\lambda y''+y=\int_0^1y,\qquad y'(0)=y'(1)=0.$$
Solving it forces $\lambda=1/(k\pi)^2$ and $y=a\cos(k\pi t)$.

> [!theorem] Eigenvalues determine the norm (Thm 1.2, p. 64)
> Two centered Gaussian processes have $L^2$ norms with the same law if and only if their KL eigenvalue sequences coincide. The proof uses the moment generating function
> $$\mathbb E\,e^{z\int\zeta^2}=\prod_k(1-2z\lambda_k)^{-1/2}.$$

> [!theorem] Weighted case (Thm 1.3, p. 68)
> For $\gamma>-\tfrac12$ let
> $$W_\gamma(t)=\frac1{\sqrt{1+2\gamma}}\Big\{W(t^{1+2\gamma})-\int_0^1W(u^{1+2\gamma})\,du\Big\}.$$
> With $\nu=1/(2(1+\gamma))\in(0,1)$ and $z_{\nu,k}$ the positive zeros of the Bessel function $J_\nu$, the eigenvalues are
> $$\lambda_k=\Big(\frac{2\nu}{z_{\nu,k}}\Big)^2$$
> and the eigenfunctions are built from $J_{\nu-1}(z_{\nu,k}\,t^{1/(2\nu)})$ (eq. 1.45-1.46). The same $\lambda_k$ belong to the weighted bridge $t^\gamma B(t)$ (Fact 1.2, quoted from earlier work), so the two have equal $L^2$-norm laws (eq. 1.47).

Multivariate results (§1.3, Thm 1.4): the $d$-variate mean-centered Wiener sheet has covariance equal to the product of the univariate $K_{W_0}$, so its KL expansion is the tensor product of the cosine expansions. The product lemma (Lemma 4.1 of the cited reference) states that if a covariance factorises, the eigenpairs are products of the factors' eigenpairs and the eigenvalues multiply.

## Results

No numerical experiments; the contribution is exact formulae. The paper states that these expansions are new "up to our best knowledge" (Rem. 1.1, p. 63).

## Limitations

The results cover Gaussian processes built from the Wiener process, with explicit covariance. Eigenfunctions of the weighted case need Bessel zeros, which must be computed numerically.

Wiki note: for the plain [[Wiener process]] $W$ on $[0,1]$ the classical eigenpairs are $\lambda_k=1/((k-\tfrac12)\pi)^2$ and $e_k=\sqrt2\sin((k-\tfrac12)\pi t)$ (stated in [[Brownian motion construction (Li n.d.)]], eq. 1.6, not in this paper). This is the series used for simulating Brownian paths in [[Quantum option pricing KL (Prakash 2025)]].

## Connections

- General theory (Mercer, convergence): [[KL expansion note (Alexanderian 2015)]].
- Discretizing general random fields: [[Random field discretization (Betz 2014)]].
- Brownian motion itself: [[Brownian motion]], [[Brownian movement (Einstein 1905)]], [[Brownian motion construction (Li n.d.)]].

**Sources**: `Stochastic Methods/Deheuvels - Karhunen-Loeve Expantions of mean-centered Wiener Processes.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Karhunen-Loève expansion]] · [[Wiener process]] · [[Brownian motion]]
- [[KL expansion note (Alexanderian 2015)]] · [[Random field discretization (Betz 2014)]] · [[Mercer's theorem]]
- [[Quantum option pricing KL (Prakash 2025)]]
