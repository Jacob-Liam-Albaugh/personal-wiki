---
type: method
area: operators
source-ref: "Kovachki, Lanthaler, Stuart 2024, §3.1, p. 7; Thm 4.4, p. 14"
tags: [operators, ml]
---

# PCA-Net

> [!algorithm] PCA-Net (Kovachki et al. 2024, §3.1, p. 7)
> $$F_U(u)=\{\langle\phi_j,u\rangle\}_{j=1}^{d_U}$$
> $$\Psi_{PCA}(u;\theta)(y)=\sum_{j=1}^{d_V}\alpha_j(F_Uu;\theta)\,\psi_j(y)$$
> $\phi_j$: leading eigenfunctions of the input covariance under $\mu$. $\psi_j$: leading eigenfunctions of the output covariance under $\Psi^\dagger_\#\mu$. $\alpha$: a neural network.
>
> (source: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`, p. 7)

**Intuition**: compress inputs and outputs with PCA, then learn a finite-dimensional map between the coefficients. It is the data-driven [[Encoder-decoder operators]]. The PCA bases are empirical [[Karhunen-Loève expansion]] modes (Wiki note).

> [!theorem] Theorem 4.4 — universality (p. 14)
> Let $\mathcal U,\mathcal V$ be separable Hilbert spaces, with $\mathbb E\|u\|^2<\infty$, $\mathbb E\|\Psi^\dagger(u)\|^2<\infty$ and $\Psi^\dagger$ $\mu$-measurable. For every $\varepsilon>0$ there are sizes and a network such that
> $$\mathbb E_{\{u_j\}}\,\mathbb E_u\|\Psi^\dagger(u)-\Psi(u;\{u_j\})\|^2<\varepsilon$$
> where the PCA bases are estimated from the samples $\{u_j\}$.

## Where it appears
- [[Operator learning review (Kovachki 2024)]].
- "PCANN" is a baseline in [[FNO (Li 2021)]] Table 3 (Burgers, 0.038-0.040).
- The PCA used for output reduction in [[Principal component analysis]] and [[Karhunen-Loève expansion]] is the finite-dimensional version of its encoder.

**Sources**: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Encoder-decoder operators]] · [[DeepONet]] · [[Karhunen-Loève expansion]]
