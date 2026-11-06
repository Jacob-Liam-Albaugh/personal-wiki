---
type: concept
area: ift
areas: [ift, bayesian]
tags: [lab, ift, bayesian]
source-ref: "Alberts & Bilionis 2023, eqs. 2-11, 18, pp. 4-7"
---

# Information field theory

**Summary**: Bayesian inference over fields, written as path integrals. A quadratic action gives a closed-form free theory equal to Wiener filtering / GP regression; physics enters through the prior energy.

**Sources**: `IFT/Bilionis, Alberts - IFT.pdf`, `IFT/Bilionis, Alberts - IFT Thermal Conductivity.pdf`.
**Last updated**: 2026-11-06

---

## Free theory
> [!definition] Gaussian field and generating functional (eqs. 2-6, p. 4)
> $$p(\phi)\propto e^{-\frac12\phi^\dagger S\phi},\qquad Z[q]=\int\mathcal D\phi\,e^{-\frac12\phi^\dagger S\phi+\phi^\dagger q}=C\det(S)^{-1/2}e^{\frac12q^\dagger S^{-1}q}$$
> so $\mathbb E[\phi]=0$, $\mathrm{Cov}[\phi]=S^{-1}$.

> [!theorem] Posterior of the free theory (eqs. 8-11, pp. 5-6)
> With data $d=R\phi+n$, $n\sim\mathcal N(0,N)$:
> $$\tilde S=S+R^\dagger N^{-1}R,\quad \tilde m=\tilde S^{-1}R^\dagger N^{-1}d=S^{-1}R^\dagger K^{-1}d,\quad K=N+RS^{-1}R^\dagger.$$
> With Dirac measurement functionals $R$ this is GP regression.

## Information Hamiltonian
> [!definition] (p. 6; eq. 18, p. 7)
> $H[\phi|d]=-\log p(\phi|d)$ up to a constant. Gaussian case: $\tfrac12[\phi^\dagger S\phi+(R\phi-d)^\top N^{-1}(R\phi-d)]$. General: $H[\phi|d]=\ell(d,R\phi)+\beta U[\phi]$.

## Physics-informed IFT
- Prior from a PDE energy: [[Physics-informed prior]].
- Sampling: [[SGLD]]; hyperparameters by [[Nested SGLD]].
- PINNs as a limit: [[PINN]].

## Where it appears
- [[PIFT (Alberts 2023)]] — develops PIFT.
- [[IFT thermal conductivity (Alberts 2026)]] — applies it to temperature-dependent conductivity.
- [[Generative priors for turbulence (Wang 2026)]] — Wiki note: generative priors play the role a physics prior plays here; the paper does not mention IFT.

## Related pages
- [[Karhunen-Loève expansion]] · [[SGLD (Welling 2011)]]
