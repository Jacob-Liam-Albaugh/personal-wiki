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

## Gaussian Markov process view (Enßlin)
Page numbers here are PDF pages of the lecture notes (printed page = PDF page minus 6).

> [!definition] Markov property, Wiener process with volatility (source: Ensslin - Information Theory & Information Field Theory.pdf, §10.1.1-10.1.2, p. 115)
> $s$ is Markov if $P(s_f|s_t,s_p)=P(s_f|s_t)$ for $f\ge t\ge p$. The Wiener process is $\dot s_t=\sigma_t\xi_t$ with $P(\xi)=\mathcal G(\xi,\mathbb 1)$ and known volatility $\sigma_t$.

Given $s_p$, the increment is $s-s_p=L\xi$ with $L^f{}_t=\sigma_t\mathbb 1_{p\le t\le f}$, so $P(s|s_p)=\mathcal G(s-s_p,LL^\dagger)$ and (eq. 306, p. 116)

$$D^{tt'}=\langle(s^t-s^p)(s^{t'}-s^p)\rangle=\int_p^{\min\{t,t'\}}dt''\,(\sigma^{t''})^2=\min\{D^{tt},D^{t't'}\}.$$

With $\sigma$ constant and $s_p=0$ this is the covariance $s\wedge t$ above.

> [!theorem] Markov covariance (source: §10.1.3, pp. 116-117)
> For a zero-mean Gaussian Markov process and $f\ge t\ge p$: $S^{fp}=S^{ft}S^{tp}/S^{tt}$. Proof: Wick's theorem gives $\langle s^fs^ts^ts^p\rangle=2S^{ft}S^{tp}+S^{fp}S^{tt}$, while the Markov factorization gives $3S^{ft}S^{tp}$.

The expected future value, $\langle s^f\rangle=S^{ft}s^t/S^{tt}$, is the data-space [[Wiener filter]] with $s^t$ as the datum (true also without the Markov property).

> [!example] Stock price as a Wiener process (source: §10.1.4, pp. 117-119)
> With $s=\ln(p_f/p_p)-\ln(q_f/q_p)$ the log-performance against a market index, no arbitrage means $\langle s^f\rangle=s^t$ (a martingale), so $S^{ft}=S^{tt}$, $S^{ab}=\min\{S^{aa},S^{bb}\}$, and $\dot s=\sigma\xi$. The price is lognormal, $\langle e^{s^f}\rangle=e^{s^t+\Sigma/2}\ge e^{s^t}$ with $\Sigma=\int_t^fdt'\,\sigma^2$: uncertainty in the log-price gives the price a positive drift. See [[Geometric Brownian motion]].

Spectrum: the Wiener process has $P_s(\omega)=\omega^{-2}$ for unit white-noise excitation (§10.2.1, p. 119; §10.3.1, p. 121).

Wiki note: the book's exercise (p. 121) asks to rebuild the prior and posterior from this spectrum; its text on p. 116 says that happens "in Sec. 10.2", but the construction is in §10.3, apparently a stale cross-reference.

**Covered in**: ASML book sinverse/sodes (ME 697 6.1); Enßlin IT & IFT ch. 10.1-10.3 (pp. 115-121)
**Sources**: Li; Deheuvels 2006, `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Brownian motion]]
- [[Karhunen-Loève expansion]]
- [[Mercer's theorem]]
- [[Brownian motion construction (Li n.d.)]]
- [[KL expansions of the Wiener process (Deheuvels 2006)]]
- [[Wiener-Askey chaos (Xiu 2002)]]
- [[Stochastic differential equation]].
- [[Wiener filter]] · [[Information Hamiltonian]] (Enßlin's Gaussian-process chapter)
