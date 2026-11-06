---
type: definition
area: physics-informed
source-ref: "Bhattacharya et al. 2023, p. 8, eq. 2.2, App. D"
tags: [mechanics]
---

# Kelvin-Voigt viscoelasticity

> [!definition] 1D Kelvin-Voigt material (Bhattacharya et al. 2023, p. 8)
> $$\sigma^\epsilon=E^\epsilon\,\partial_xu^\epsilon+\nu^\epsilon\,\partial^2_{xt}u^\epsilon,\qquad E^\epsilon(x)=E(x/\epsilon),\ \nu^\epsilon(x)=\nu(x/\epsilon)\ \text{1-periodic.}$$
> Weak form (eq. 2.2): $q_{\nu^\epsilon}(\partial_tu^\epsilon,\varphi)+q_{E^\epsilon}(u^\epsilon,\varphi)=\langle f,\varphi\rangle$, $q_\xi(u,w)=\int\xi\,u_xw_x\,dx$.

**Intuition**: a spring $E$ and a dashpot $\nu$ in parallel; stress is affine in strain and strain rate. No memory at the micro scale, yet [[Homogenization]] produces memory at the macro scale.

## Variant: standard linear solid
$\sigma=E_1e+E_2(e-e^p)$, $\partial_te^p=\tfrac{E_2}{\nu}(e-e^p)$ (App. D, eq. D.1).

## Where it appears
- [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]].

**Sources**: `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Homogenization]] · [[Markovian constitutive model]]
