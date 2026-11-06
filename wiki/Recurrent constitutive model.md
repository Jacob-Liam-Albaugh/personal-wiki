---
type: method
area: operators
areas: [operators, physics-informed]
source-ref: "Bhattacharya et al. 2023, eq. 3.12, Thm 3.10, eqs. 3.16-3.17"
tags: [mechanics, ml]
---

# Recurrent constitutive model

> [!algorithm] RNN constitutive law (Bhattacharya et al. 2023, eq. 3.12, p. 14)
> $$\Psi_0^{RNN}=\mathcal F^{RNN}(\partial_xu_0,\ \partial^2_{xt}u_0,\ \xi),\qquad \dot\xi=\mathcal G^{RNN}(\xi,\partial_xu_0),\ \xi(0)=0,$$
> $\mathcal F,\mathcal G$ feed-forward nets applied pointwise in time, $\xi$ advanced by forward Euler. Architecture (App. C.1): 3 SELU layers of 100 nodes; not an LSTM.

**Intuition**: learn the [[Markovian constitutive model]] directly: the network is the right-hand side of the hidden-variable ODE.

> [!theorem] Theorem 3.10 (p. 14; proof App. A.3)
> If $0<\rho<\min_\ell|\alpha_\ell|$ and $\max_\ell|\beta_\ell|\le B$, then for every $\eta>0$ some $\Psi_0^{RNN}$ satisfies $\sup_{t,\,b,c}|\Psi_0^{PC}-\Psi_0^{RNN}|<\eta$ on bounded strain / strain-rate inputs.
> Key estimate (Prop. A.5): $\dot e_\xi=-Ae_\xi+q$, $\|q\|\le\delta$ gives $\|e_\xi\|<\delta/\rho$.
> Not proved: well-posedness of the PDE with the RNN law, or closeness of its solution to $u_0^{PC}$.

## Losses (eqs. 3.16-3.17, p. 16)
$$L_1=\frac1N\sum_n\frac{\|\sigma_n-\hat\sigma_n\|_{L^2}}{\|\sigma_n\|_{L^2}}\quad\text{(accessible: stress only)}$$
$L_2$ adds the relative error in $\dot\xi$ (inaccessible: needs analytic hidden variables).

> [!failure] Stress-only training
> With $L_1$ only, the RNN is a good surrogate but can miss the linear structure of $\mathcal G$ (local minimizers).

## Where it appears
- [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]].

**Sources**: `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Exact Markovian law for Kelvin-Voigt]] · [[Operator learning]] · [[DeepONet]]
- [[Energy-based kernels for viscoelastic flow (Otto 2024)]]
