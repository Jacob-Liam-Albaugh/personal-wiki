---
type: definition
area: physics-informed
areas: [physics-informed, inverse-problems]
source-ref: "Kissas et al. 2020, eq. 19, p. 11; §2.8"
tags: [physics-informed, pde, inverse-problems]
---

# Windkessel model

> [!definition] Three-element Windkessel outflow model
> Lumped model of the downstream vasculature at an outlet $j$, with resistance $R_j$ (small arteries), compliance $C_j$ (large elastic arteries) and characteristic impedance $Z_j=\rho c_0^j/A_0^j$:
> $$p_j+R_jC_j\dot p_j-(R_j+Z_j)Q_j-p_\infty-R_jC_jZ_j\dot Q_j=0,\quad Q_j=A_ju_j.$$
> Here $p_\infty=666.5$ Pa is the constant downstream pressure.
>
> (source: `Kissas et al - Machine learning in cardiovascular flows modeling ...pdf`, eq. 19, p. 11)

**Intuition**: an electric-circuit analogy (compliance as capacitor, resistance as resistor) giving a truncated arterial model the outflow boundary condition it needs. Choosing $R$ and $C$ is usually the costly calibration step.

## Calibration by PINN post-processing
Train the vessel [[PINN]]s on area and velocity only; read off $p_j(t)$ and $Q_j(t)$ at the outlet; fit $Q_j$ with a 50-mode Fourier series to get $\dot Q_j$; solve the ODE for a grid of $(R,C)$ and minimize $\frac1{N_t}\sum_m\|\tilde p(t_m)-p(t_m)\|^2$ (eq. 20, p. 12). Refine the grid in $[0.5,1.5]\times$ the current optimum, 5 rounds, about 10 min per outlet. A conventional discontinuous-Galerkin solver given the fitted values reproduced velocity waveforms in the clinical case, apart from a time shift at the carotid (p. 24). No ground truth for $R,C$ in vivo; the synthetic cases compare predicted waveform error only.

## Where it appears
- [[Cardiovascular flow PINNs (Kissas 2020)]] — outflow parameter identification, three synthetic and one clinical network.

**Sources**: `papers/Physics Informed Architectures/Kissas et al - Machine learning in cardiovascular flows modeling Predicting arterial blood pressure from non-invasive 4D flow MRI data.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[PINN]] · [[Cardiovascular flow PINNs (Kissas 2020)]] · [[Navier-Stokes equations]] · [[Bayesian inverse problems]]
