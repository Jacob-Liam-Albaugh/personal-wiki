---
type: definition
area: physics-informed
areas: [physics-informed, pde]
source-ref: "Sahli Costabal et al. 2020, eqs. 1-2, p. 2"
tags: [pde, physics-informed]
---

# Eikonal equation

> [!definition] Eikonal equation for activation times
> For a wave front with local speed $V(x)>0$, the arrival (activation) time $T(x)$ satisfies
> $$\|\nabla T(x)\|=\frac1{V(x)}.$$
> Residual form used in a PINN: $R(x)=V(x)\|\nabla T\|-1=0$.
>
> (source: `Costabal et al - Physics-Informed Neural Networks for Cardiac Activation Mapping.pdf`, eqs. 1-2, p. 2)

**Intuition**: a front moves at speed $V$ normal to itself, so the time gradient points along the propagation direction with magnitude $1/V$. Knowing $T$ gives $V$ and vice versa, which is why sparse activation-time data can recover a conduction-velocity map.

## Examples
- Cardiac electro-anatomic mapping: $T$ is when cells depolarize, $V$ the conduction velocity. Both are neural networks tied by $R=0$ in [[Cardiac activation PINN (Sahli Costabal 2020)]], with $V$ bounded by $V_{max}\sigma(\cdot)$ and a total-variation penalty to allow slow patches.
- On a surface, an extra penalty $|\nabla T\cdot N|^2$ keeps the wave tangent to the atrial wall (eq. 10, p. 4).

## Failure modes / non-examples
- Where two fronts collide $T$ has a gradient kink and $\nabla T\to0$ locally, so $V=1/\|\nabla T\|$ blows up for smooth interpolants (GP, plain network, linear); the PINN handles it better (p. 5).
- Fails for spiral waves and fibrillation, where $V$ depends on time and the equation does not hold (p. 11). Isotropic form only; anisotropy needs fibre information (p. 10).

## Where it appears
- [[Cardiac activation PINN (Sahli Costabal 2020)]] — residual loss for activation mapping.

**Sources**: `papers/Physics Informed Architectures/Costabal et al - Physics-Informed Neural Networks for Cardiac Activation Mapping.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[PINN]] · [[Cardiac activation PINN (Sahli Costabal 2020)]] · [[Active learning]]
