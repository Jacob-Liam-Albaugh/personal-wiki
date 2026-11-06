---
type: definition
area: operators
areas: [operators, physics-informed]
source-ref: "Bhattacharya et al. 2023, eq. 1.3, p. 4"
tags: [mechanics, operators]
---

# Markovian homogenized constitutive model

> [!definition] Markovian model (Bhattacharya et al. 2023, eq. 1.3)
> The history-dependent homogenized stress is written through hidden variables $\xi(t)\in\mathbb R^r$:
> $$\Psi_0\big(B(t),\partial_tB(t),\{B(\tau)\}_{\tau\le t},t\big)=\mathcal F\big(B(t),\partial_tB(t),\xi(t)\big),\quad \partial_t\xi=\mathcal G(\xi,B(t)),\ \xi(0)=0.$$
>
> (source: `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`, p. 4)

**Intuition**: replace a memory integral over the whole history by a small state that is updated forward. Cost goes from $O(|\mathcal T|^2)$ to $O(|\mathcal T|)$ (p. 3). The $\xi$ are the internal variables of continuum mechanics (p. 5).

## When it is exact
- [[Exact Markovian law for Kelvin-Voigt]]: piecewise-constant Kelvin-Voigt microstructure with $L'+1$ pieces gives exactly $L'$ exponential-memory hidden variables.

## How it is learned
- [[Recurrent constitutive model]].

## Where it appears
- [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]].

**Sources**: `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Homogenization]] · [[Kelvin-Voigt viscoelasticity]] · [[Recurrent constitutive model]]
