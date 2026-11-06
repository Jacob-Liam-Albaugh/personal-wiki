---
type: method
area: me697
areas: [me697, pde]
source-ref: "ME 697 book, pinns/basics (forward.ipynb, energy.ipynb)"
tags: [physics-informed, pde, optimization]
---

# Non-dimensionalization

Rescaling variables so that network inputs, outputs and PDE coefficients are $O(1)$. For a [[PINN]] this keeps the residual loss well scaled and matches the Glorot initialization.

> [!definition] Scales for the 2D Poisson-type example (source: pinns/basics/forward.ipynb)
> With length scales $L_x,L_y$, a solution scale $u_s$ and a source scale $f_s$, the dimensionless conductivities are

$$
\tilde k_x = \frac{k\,u_s}{L_x^2 f_s},
\qquad
\tilde k_y = \frac{k\,u_s}{L_y^2 f_s}.
$$

> [!example] Numbers in the notebook
> Residual version: $f_s=9.96\times10^6$, $u_s=4.40\times10^4$, giving $\tilde k_x=4.415$ and $\tilde k_y=4.415\times10^{-2}$.
> Energy version: $f_s=1.364\times10^4$, $u_s=6.414\times10^4$, giving $k_x=4702$ and $k_y=47.02$ (source: energy.ipynb).

## Why it matters
- A small ratio such as $\tilde k_y/\tilde k_x=10^{-2}$ makes one direction nearly decoupled and is a hard case for training; it connects to [[Spectral bias]].
- Mis-scaled terms in the loss let one term dominate; see the loss discussion in [[ME697 5.1 - PINN basics]].

**Wiki note**: the two notebooks use different scale choices, so their $k_x,k_y$ values are not comparable; the energy notebook also has a `kx`/`ky` slip in one energy term (flagged on the lecture page).

**Sources**: `advanced-scientific-machine-learning/book/pinns/basics/forward.ipynb`, `energy.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ME697 5.1 - PINN basics]] · [[PINN]] · [[Energy functional]] · [[Spectral bias]] · [[Fourier features]]
