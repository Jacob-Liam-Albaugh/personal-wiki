---
type: paper
area: stochastic
areas: [stochastic, math]
source-ref: "Li, Lecture 12, Construction of BM and its properties, Thm 1.1, 1.5, 1.7, 2.1-2.7"
tags: [uq, gp]
authors: ["[[Tiejun Li]]"]
venue: "Lecture notes (Lecture 12), School of Mathematical Sciences, Peking University; year not stated in the PDF"
file: "Stochastic Methods/Li - Construction of Brownian Motion.pdf"
---

# Brownian motion construction (Li n.d.)

**Summary**: Lecture notes that build the [[Wiener process]] in three ways (invariance principle, [[Karhunen-Loève expansion]], Haar basis) and then prove its basic path properties: scaling, quadratic variation $t$, infinite total variation, Hölder exponent below one half, and the law of the iterated logarithm.

**Authors**: Tiejun Li · **Year**: not stated · **File**: `Stochastic Methods/Li - Construction of Brownian Motion.pdf`

---

## Problem

Define Brownian motion rigorously and show that a process with the required law exists with continuous paths. Different constructions serve different purposes (p. 1).

## Method

> [!theorem] A. Invariance principle (Thm 1.1, p. 1)
> Let $\xi_i$ be iid $\mathcal N(0,1)$, $S_n=\sum_{i\le n}\xi_i$, and $X^n_t$ the piecewise-linear interpolation of $S_k/\sqrt n$ at $t=k/n$. Then $X^n\to W$ weakly on $C[0,\infty)$.
>
> (source: Li - Construction of Brownian Motion.pdf, Thm 1.1)

Brownian motion is the limit of a symmetric random walk with space step $1/\sqrt n$ and time step $1/n$, so $\ell^2/\tau=1$ (p. 1). The proof uses Prohorov's theorem and is skipped. The limit law on $C[0,\infty)$ is the Wiener measure. The CLT gives the heuristic: $S_k/\sqrt n\to\mathcal N(0,t)$ and the covariance tends to $t\wedge s$. Only mean zero and variance one of $\xi_i$ matter, hence "invariance" (p. 3).

> [!theorem] B. Karhunen-Loève construction (Thm 1.5-1.6, pp. 3-5)
> A centered Gaussian process on $[0,1]$ with continuous covariance $K$ has
> $$X_t=\sum_k\alpha_k\sqrt{\lambda_k}\,\varphi_k(t),\qquad\alpha_k\ \text{iid}\ \mathcal N(0,1),$$
> converging in $L^\infty_tL^2_P$. The proof uses compactness and self-adjointness of $K$, and [[Mercer's theorem]] for the Cauchy property.
>
> (source: ibid., Thm 1.5)

For $K(s,t)=s\wedge t$, the eigen-equation $\int_0^1(s\wedge t)\varphi(t)\,dt=\lambda\varphi(s)$ differentiates twice to $\lambda\varphi''=-\varphi$ with $\varphi(0)=0$, $\varphi'(1)=0$, so
$$\lambda_k=\Big((k-\tfrac12)\pi\Big)^{-2},\qquad\varphi_k(s)=\sqrt2\sin\!\big((k-\tfrac12)\pi s\big),$$
$$W_t=\sum_{k\ge1}\alpha_k\frac{\sqrt2}{(k-\tfrac12)\pi}\sin\!\big((k-\tfrac12)\pi t\big)\qquad\text{(eq. 1.6)}.$$
Almost-sure uniform convergence, hence continuous paths, follows from a Dudley-type integral condition (Thm 1.6, cited to Adler); for Wiener, $\sigma(s,t)=|t-s|$ satisfies it.

> [!theorem] C. Haar basis (Lévy's construction) (Thm 1.7, pp. 5-7)
> With the Haar system $H^{(n)}_k$ (orthonormal basis of $L^2[0,1]$) and iid normals $\alpha^{(n)}_k$,
> $$W^N_t=\sum_{n\le N}\sum_k\alpha^{(n)}_k\int_0^tH^{(n)}_k(s)\,ds\ \to\ W_t$$
> uniformly in $t$, almost surely. The covariance $\to t\wedge s$ by Parseval. Uniform convergence uses the Gaussian tail bound $P(|\xi|>x)\le\sqrt{2/\pi}\,e^{-x^2/2}/x$ and Borel-Cantelli.

> [!example] Wiener functional via KL (Ex. 1.8, pp. 7-8)
> Since $\int_0^1W_t^2dt=\sum_k\lambda_k\alpha_k^2$,
> $$\mathbb E\exp\!\Big(-\tfrac12\int_0^1W_t^2dt\Big)=\prod_k(1+\lambda_k)^{-1/2}=\cosh(1)^{-1/2}=\sqrt{\tfrac{2e}{1+e^2}},$$
> using the product formula for $\cosh$.

Path properties (§2, pp. 8-11):

- Time homogeneity, symmetry $-W$, scaling $cW_{t/c^2}$, and time inversion $tW_{1/t}$ all give Brownian motions (Thm 2.1). Scaling means $W_{kt}\sim\sqrt kW_t$, unlike a smooth function, whose derivative scales as $1/k$ (eq. 2.1-2.2).
- Quadratic variation: $\mathbb E(Q^\Delta_t-t)^2=2\sum_k(t_{k+1}-t_k)^2$, so $\langle W,W\rangle_t=t$, written $dW_t^2=dt$ (Prop. 2.2).
- Paths have infinite variation on every interval a.s. (Thm 2.3).
- Hölder continuous of every order $\alpha<\tfrac12$ a.s., and of no order $\alpha>\tfrac12$ (Thm 2.4, via Kolmogorov continuity). Paths are continuous and nowhere differentiable.
- Khinchin's local law of the iterated logarithm: $\limsup_{t\to0}W_t/\sqrt{-2t\ln\ln t}=1$ a.s. (Thm 2.6). Strong law: $W_t/t\to0$ (Thm 2.7).

## Results

Fig. 1 shows one realization from each construction (invariance principle, KL with cutoff $N=1000$, Haar with finite cutoff). The notes give no numerical comparison beyond that.

## Limitations

Proofs of the invariance principle and of Thm 2.4 at $\alpha=\tfrac12$ are skipped and referred to Karatzas-Shreve and Revuz-Yor. Homework items HW1-HW4 (scaling invariance, quadratic variation, metric on $C[0,\infty)$, conditional law of the midpoint $W_{(s+t)/2}\mid W_s,W_t\sim\mathcal N(\tfrac{x+y}2,\tfrac{t-s}4)$) are stated without solutions.

## Connections

- The KL construction (B) is the series used for sampling Brownian paths in [[Quantum option pricing KL (Prakash 2025)]]; the general theory is in [[KL expansion note (Alexanderian 2015)]] and related Wiener-based expansions in [[KL expansions of the Wiener process (Deheuvels 2006)]].
- Physical origin of the $\sqrt t$ law: [[Brownian movement (Einstein 1905)]].
- Brownian increments drive SDEs: see [[Langevin dynamics]] and [[Wiener-Askey chaos (Xiu 2002)]].
- The Haar system is the simplest [[Wavelet transform]] basis.

**Sources**: `Stochastic Methods/Li - Construction of Brownian Motion.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Brownian motion]] · [[Wiener process]] · [[Karhunen-Loève expansion]] · [[Mercer's theorem]]
- [[Brownian movement (Einstein 1905)]] · [[KL expansion note (Alexanderian 2015)]] · [[KL expansions of the Wiener process (Deheuvels 2006)]]
- [[Wavelet transform]] · [[Quantum option pricing KL (Prakash 2025)]]
