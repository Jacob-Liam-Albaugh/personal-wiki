---
type: method
area: physics-informed
source-ref: "Bhattacharya et al. 2023, eqs. 2.3-2.7, Thm 3.7"
---

# Homogenization

> [!algorithm] Two-scale homogenization of 1D Kelvin-Voigt, in Laplace space (Bhattacharya et al. 2023, pp. 9-10)
> With $\hat a(s,y)=E(y)+\nu(y)s$, the cell problem is $-\partial_y(\hat a\,\partial_y\chi)=\partial_y\hat a$ (eq. 2.4), and the effective equation $-\partial_x(\hat a_0(s)\partial_x\hat u_0)=\hat f$ has
> $$\hat a_0(s)=\langle\hat a^{-1}\rangle^{-1}=\Big(\int_0^1\frac{dy}{s\nu(y)+E(y)}\Big)^{-1}.$$
> Expanding at large $s$, $\hat a_0=\nu's+E'+\hat\kappa(s)$, so in time (eq. 2.7)
> $$\sigma_0=E'\partial_xu_0+\nu'\partial^2_{xt}u_0+\int_0^t\kappa(t-\tau)\,\partial_xu_0(\tau)\,d\tau,$$
> $\nu'=\big(\int_0^1\nu^{-1}\big)^{-1}$, $E'=\int_0^1E\nu^{-2}\big/\big(\int_0^1\nu^{-1}\big)^2$.

**Intuition / when to use it**: replace a rapidly oscillating coefficient by an effective one. The harmonic mean $\langle\hat a^{-1}\rangle^{-1}$ is the 1D signature. The memory kernel $\kappa$ is what homogenization *creates*.

> [!theorem] Theorem 3.7 (p. 13)
> $u_\epsilon\rightharpoonup u_0$ in $W^{1,2}(\mathcal T;V)$ (case $\rho=0$).

> [!example] Data from the unit cell (Lemma 3.12, p. 15)
> Solving $\partial_y\sigma=0$, $\sigma=E\partial_yu+\nu\partial^2_{ty}u$, $u(0,t)=0$, $u(1,t)=b(t)$ gives $\sigma(t)=\Psi_0^\dagger(b,\partial_tb,\{b\},t)$, since $\hat\sigma=\hat a_0\hat b$. This is how training data are generated.

## Where it appears
- [[bhattacharya-2023-markovian-homogenized-viscoelasticity]].

**Sources**: `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[kelvin-voigt-viscoelasticity]] · [[exact-markovian-parametrization-piecewise-constant-kv]]
