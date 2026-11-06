---
type: paper
area: stochastic
areas: [stochastic, math]
source-ref: "Alexanderian 2015, arXiv:1509.07526, Thm 5.3, Cor 5.5"
tags: [uq, gp]
authors: ["[[Alen Alexanderian]]"]
year: 2015
venue: "arXiv:1509.07526 (math.PR), lecture note"
file: "Stochastic Methods/Alexanderian - the Karhunen-Loéve Expansion.pdf"
---

# KL expansion note (Alexanderian 2015)

**Summary**: A self-contained derivation of the [[Karhunen-Loève expansion]] of a centered, mean-square continuous process. The proof runs through compact self-adjoint operators on a Hilbert space and [[Mercer's theorem]]. A closing example expands a Gaussian field with exponential covariance and warns about truncating too early.

**Authors**: Alen Alexanderian · **Year**: 2015 · **File**: `Stochastic Methods/Alexanderian - the Karhunen-Loéve Expansion.pdf`

---

## Problem

KL expansions are used throughout uncertainty propagation with random parameter functions, but a clear and rigorous derivation, including convergence, is hard to find in the literature (p. 1). The note supplies one.

## Method

Functional-analytic prerequisites (§2-3, pp. 2-5):

- A linear map is compact if it sends bounded sets to relatively compact sets (Def. 2.4). A kernel $k\in L^2(D\times D)$ defines a Hilbert-Schmidt integral operator $[Ku](x)=\int_Dk(x,y)u(y)\,dy$, which is bounded (Cauchy-Schwarz) and compact (Lemma 2.9).
- $K$ is self-adjoint iff $k(x,y)=k(y,x)$ (Ex. 2.10).
- A compact self-adjoint $T$ has an orthonormal eigenbasis; eigenvalues are real, accumulate only at $0$, and non-zero eigenspaces are finite dimensional (Thm 2.11). If $T$ is positive the eigenvalues are ordered $\lambda_1\ge\lambda_2\ge\dots\ge0$.
- A compact operator on an infinite-dimensional space is never invertible, so $0$ is always in the spectrum (Rem. 2.8, 2.12).

> [!theorem] Mercer's theorem (Thm 3.1, p. 5)
> Let $k$ be continuous on $D\times D$, $D=[a,b]$, with positive integral operator $K$ having eigenpairs $(\lambda_i,e_i)$. Then
> $$k(s,t)=\sum_i\lambda_ie_i(s)e_i(t)$$
> with absolute and uniform convergence on $D\times D$.
>
> (source: Alexanderian - the Karhunen-Loéve Expansion.pdf, Thm 3.1, p. 5)

Process setting (§4, pp. 5-6): $X:D\times\Omega\to\mathbb R$, centered, in $L^2(D\times\Omega)$. Autocorrelation $R_X(s,t)=\mathbb E[X_sX_t]$. Mean-square continuity, $\lim_{\epsilon\to0}\mathbb E[(X_{t+\epsilon}-X_t)^2]=0$, holds iff $R_X$ is continuous (Lemma 4.2). Non-centered processes are handled by subtracting the mean.

> [!theorem] Karhunen-Loève (Thm 5.3 and Cor 5.5, pp. 7-10)
> Take $k=R_X$ in the operator $K$. Then $K$ is compact, positive and self-adjoint (Lemma 5.1), so it has eigenpairs $Ke_i=\lambda_ie_i$. With coefficients
> $$x_i(\omega)=\int_DX_t(\omega)e_i(t)\,dt$$
> one has
> $$\mathbb E[x_i]=0,\qquad \mathbb E[x_ix_j]=\delta_{ij}\lambda_j$$
> (Lemma 5.2), and
> $$X_t=\sum_{i=1}^\infty x_ie_i(t)\quad\text{in }L^2(\Omega),\ \text{for all }t.$$
> Normalizing $\xi_i=x_i/\sqrt{\lambda_i}$ gives
> $$X(t,\omega)=\sum_{i=1}^\infty\sqrt{\lambda_i}\,\xi_i(\omega)\,e_i(t)$$
> with $\xi_i$ centered, uncorrelated, unit variance.
>
> (source: ibid., Thm 5.3, Cor 5.5)

> [!proof] Sketch of convergence (Thm 5.3)
> Expand the mean-square error and use Lemma 5.2:
> $$\varepsilon_n(t)=\mathbb E\Big[\big(X_t-\sum_{i\le n}x_ie_i(t)\big)^2\Big]=k(t,t)-\sum_{i\le n}\lambda_ie_i(t)^2.$$
> Mercer's theorem sends this to $0$ uniformly in $t$.

Further statements (p. 10): a zero eigenvalue gives a zero coefficient (Rem. 5.4). For a Gaussian process the $\xi_i$ are independent standard normals, and the series converges almost surely (cited to Loève 1977, not proved here).

## Results

Example (§6, pp. 10-13): Gaussian field on $[0,1]$ with
$$R_X(s,t)=\sigma^2\exp\!\big(-|s-t|/L_c\big),\qquad\sigma^2=L_c=1.$$
Eigenpairs are analytic (cited). With $N=6$ terms the covariance error is bounded by $8\times10^{-2}$ (Fig. 3). Realizations come from the truncated sum $\sum_{i\le N}\sqrt{\lambda_i}\xi_ie_i$ with $N=6$ (Fig. 4).

## Limitations

As stated by the author (p. 11): truncating the series a priori can mislead, since higher oscillatory modes can still matter for the output of a physical system; and low-order truncations give realizations that look artificially smooth. Fig. 5 shows realizations for $N=5,10,30,70$.

Wiki note: the derivation is for $D\subset\mathbb R$ with a continuous kernel; the multi-dimensional case with a discretized field is the subject of [[Random field discretization (Betz 2014)]].

## Connections

- Supplies the Mercer and convergence statements that [[Karhunen-Loève expansion]] needed.
- The Wiener-process case with closed-form eigenpairs is in [[KL expansions of the Wiener process (Deheuvels 2006)]]; see [[Wiener process]].
- The KL coefficients of a Gaussian field are the random inputs of the [[Polynomial chaos]] expansion in [[Wiener-Askey chaos (Xiu 2002)]].
- Used for stochastic simulation in [[Quantum option pricing KL (Prakash 2025)]].

**Sources**: `Stochastic Methods/Alexanderian - the Karhunen-Loéve Expansion.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Karhunen-Loève expansion]] · [[Mercer's theorem]] · [[Random field discretization (Betz 2014)]]
- [[KL expansions of the Wiener process (Deheuvels 2006)]] · [[Wiener process]] · [[Polynomial chaos]]
- [[Gaussian process]]
