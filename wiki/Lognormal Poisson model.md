---
type: method
area: ift
areas: [ift, bayesian]
source-ref: "Enßlin IT & IFT, §10.5, pp. 124-127 (PDF pages)"
tags: [ift, bayesian, inverse-problems]
---

# Lognormal Poisson model

**Summary**: a Bayesian model for counts of independent events (photons, galaxies, customers) over a space. The event density is $\varrho=\rho_0e^s$ with a Gaussian field $s$, and the counts are Poisson. The Hamiltonian is a Gaussian free part plus an exponential interaction.

Page numbers are PDF pages of the lecture notes (printed page = PDF page minus 6).

---

## Model (§10.5, pp. 124-126)

Events are detected in bins $i$; $\lambda_i=\int dx\,R^i{}_x\rho(x)$ is the expected count, $d_i$ the observed count. Independent events give $P(d|\lambda)=\prod_i\lambda_i^{d_i}e^{-\lambda_i}/d_i!$. For a local response with exposure $\kappa(x)$, $\lambda=\kappa\rho$. Positivity and variation over orders of magnitude motivate $\rho=\rho_0e^s$ with $\langle s\rangle=0$, and maximum entropy with known second moments gives $P(s)=\mathcal G(s,S)$.

> [!definition] Hamiltonian (source: Ensslin - Information Theory & Information Field Theory.pdf, §10.5, pp. 125-126)
> Up to $s$-independent terms ($\rho_0$ absorbed into $\kappa$),
> $$\mathcal H(d,s)\hat=\tfrac12 s^\dagger S^{-1}s+\kappa^\dagger e^{s}-d^\dagger s .$$
> Expanding $e^s=1+s+\tfrac{s^2}2+\dots$ splits it into a free and an interaction part:
> $$\mathcal H=\underbrace{\tfrac12s^\dagger D^{-1}s-j^\dagger s}_{\text{free}}+\underbrace{\sum_{n\ge3}\kappa^\dagger\frac{s^n}{n!}}_{\text{interaction}},\quad D=(S^{-1}+\hat\kappa)^{-1},\ j=d-\kappa,$$
> with $\hat\kappa=\mathrm{diag}(\kappa)$.

Continuous-space derivation (eqs. 310-316, pp. 125-126): $n$ events at positions $x_i$ with expected total $\Lambda=\kappa^\dagger\varrho$ have likelihood

$$\Big[\prod_i\frac{\varrho(x_i)}{\Lambda}\Big]\frac{\Lambda^ne^{-\Lambda}}{n!}.$$

Writing the data as a delta field $d(x)=\sum_i\delta(x-x_i)$ gives $e^{d^\dagger s}e^{-\kappa^\dagger e^s}/n!$, hence the same Hamiltonian.

## Classical (MAP) solution (pp. 126-127)

> [!algorithm] Fixed point
> $\partial\mathcal H/\partial s=S^{-1}s-d+\kappa e^s=0$ gives $m=S(d-\kappa e^m)$. Iterating this directly is unstable because $m$ appears linearly on the right. Moving the linear part to the left,
> $$m=D\big(d-\kappa(e^m-m)\big),\qquad D=(S^{-1}+\hat\kappa)^{-1},$$
> is more stable under iteration (the information source $j$ now depends on $m$).

Compared with the [[Wiener filter]], $\hat\kappa\sim R^\dagger N^{-1}R$ and $\kappa\sim R$: the effective noise covariance and response are both set by the exposure.

**Expansion around the classical solution** (p. 127): with $s=m+\phi$ the Hamiltonian for $\phi$ has the same form with exposure $\kappa_m=\kappa e^m$ (pointwise), no linear source term ($d_m=d-S^{-1}m=\kappa_m$), and propagator $D_m=(S^{-1}+\hat\kappa_m)^{-1}$. The remaining interaction is $\kappa_m^\dagger(e^\phi-1-\phi-\phi^2/2)$. The classical density $\rho_0e^m$ can be absorbed into an effective exposure.

## Where it appears
- A worked non-Gaussian example of an [[Information Hamiltonian]]. The perturbative treatment (propagator, vertices, Feynman diagrams) is in later chapters of the book: [[Interacting information field theory]], [[Interacting information field theory|Feynman diagrams]] (not yet pages).
- Related stock-price lognormal process: [[Geometric Brownian motion]].

**Wiki note**: the sign convention $s=\ln(\rho/\rho_0)$ and the "log-Gaussian Cox process" name from spatial statistics describe the same model **[unverified]**.

**Covered in**: Enßlin IT & IFT ch. 10.5 (pp. 124-127)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Information Hamiltonian]] · [[Wiener filter]] · [[Signal response]] · [[Information field theory]] · [[Gaussian process]] · [[Geometric Brownian motion]]
