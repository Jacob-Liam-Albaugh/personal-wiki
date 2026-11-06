---
type: theorem
area: physics-informed
areas: [physics-informed, operators]
source-ref: "Bhattacharya et al. 2023, Thm 3.6, Lemma A.3, Thm 3.4"
tags: [mechanics]
---

# Exact Markovian law for piecewise-constant Kelvin-Voigt

> [!theorem] Theorem 3.6 (Bhattacharya et al. 2023, eq. 3.4, p. 12)
> For a piecewise-constant KV material with $L'+1$ pieces, the homogenized law is exactly
> $$\Psi_0^{PC}=E'\partial_xu_0+\nu'\partial^2_{xt}u_0-\sum_{\ell=1}^{L'}\xi_\ell,\qquad \partial_t\xi_\ell=\beta_\ell\,\partial_xu_0-\alpha_\ell\,\xi_\ell,\ \xi_\ell(0)=0,$$
> with $\alpha_\ell>0$, $\beta_\ell\in\mathbb R$.

> [!proof] Sketch (App. A.2, pp. 28-29)
> Lemma A.3: $\hat a_0(s)=E'+\nu's-\sum_\ell\beta_\ell/(s+\alpha_\ell)$ — a rational function whose denominator has only real negative roots. Each pole is one exponential memory mode, i.e. one hidden variable.

**Intuition / when to use it**: it justifies the [[Markovian constitutive model]] class: finitely many hidden variables suffice exactly for piecewise-constant media, and Theorem 3.4 (Lipschitz dependence on $(E,\nu)$ in $L^\infty$, uniform in $\epsilon$) extends this approximately to general media.

## Corollaries
- Approximation by an RNN: see [[Recurrent constitutive model]] (Theorem 3.10).
- Standard linear solid: same structure without the strain-rate term and one more hidden variable (eq. D.5).

**Sources**: `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Homogenization]] · [[Kelvin-Voigt viscoelasticity]] · [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]]
