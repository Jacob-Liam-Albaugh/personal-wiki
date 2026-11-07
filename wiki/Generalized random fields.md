---
type: concept
area: ift
areas: [ift, bayesian]
source-ref: "Alberts 2024 dissertation, Secs. 2.1.3, 2.2.1-2.2.2, pp. 20-33, 121"
tags: [ift, bayesian, inverse-problems]
---

# Generalized random fields

**Definition**: A random field defined by its action on test functions rather than by point values. It is the function-space setting in which [[Information field theory]] defines priors without discretising.

> [!definition] Characteristic functional (Def. 2.1.1, p. 21)
> $L_X(\phi)=E[e^{iX(\phi)}]$ for $\phi$ in the Schwartz space.

> [!theorem] Bochner-Minlos (Thm 2.1.1, p. 22)
> If $L$ is positive-definite, continuous at 0 and $L(0)=1$, it is the characteristic functional of a generalized random field. Standard Gaussian example: $L(f)=\exp(-\|f\|_2^2/2)$.

- **Gaussian field** (Def. 2.2.6, p. 31): characteristic functional $\exp(-\tfrac12 Q(\phi,\phi))$ for a positive-definite $Q$.
- **No flat measure** (Thm 2.2.4, p. 31): the only translation-invariant finite measure on an infinite-dimensional Banach space is zero (disjoint-ball proof). So $\int\mathcal D\phi$ is formal; ratios such as posterior over partition function can still be finite.
- **Function-space assumptions** (p. 27): compact Lipschitz domain, Sobolev $W^k$ with $k=d_H+r$, $d_H>d_\Omega/2$, $0<r<1$.
- **Link to the physics prior** (pp. 120-121): $e^{-U(\phi)}$ for the energy $U$ of Example 2 satisfies the Bochner-Minlos conditions, so it defines a generalized random field. The dissertation lists studying these fields as open work; it does not prove existence of the measure.
- Why it matters (pp. 23-25): no Gaussian-process prior exists for a nonlinear PDE, and learned priors (PI-GAN, VAE) need a discretisation up front.

## Where it appears
- [[IFT for engineering inverse problems (Alberts 2024)]] — Ch. 2 and Sec. 7.2.1.

**Sources**: `papers/IFT/Alberts - An Information Field Theory Approach to Engineering Inverse Problems.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Information field theory]]
- [[Physics-informed prior]]
- [[Gaussian process]]
- [[Wiener process]]
- [[IFT for engineering inverse problems (Alberts 2024)]]
