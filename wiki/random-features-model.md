---
type: method
area: operators
areas: [operators, gp]
source-ref: "Kovachki, Lanthaler, Stuart 2024, §3.4, pp. 9-10"
---

# Random features model (operator)

> [!algorithm] Random features model (Kovachki et al. 2024, §3.4, pp. 9-10)
> $$\Psi_{RFM}(u;\theta)(y)=\sum_{j=1}^M\theta_j\,\psi(u;\gamma_j)(y),\qquad\gamma_j\overset{iid}\sim\nu$$
> The features $\gamma_j$ are drawn once and frozen. Only the linear weights $\theta$ are trained, so the fit is convex with a unique minimizer.
> Fourier example: $\psi(u;\gamma)=\sigma\big(\mathcal F^{-1}(\chi\,\mathcal F_\gamma\,\mathcal Fu)\big)$, with $\gamma$ a Gaussian random field.
>
> (source: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`, pp. 9-10)

**Intuition**: a kernel method in disguise. The review relates it to kernel methods (p. 11). Wiki note: as $M\to\infty$ it tends to kernel regression with the induced kernel, which links it to [[gaussian-process]] regression. The outputs still lie on a nonlinear manifold, because $\psi$ is nonlinear in $u$.

The review says its analysis can account for finite samples, finite parameters and optimization together (citing its ref. [76]).

## Where it appears
- [[kovachki-2024-operator-learning-review]].

**Sources**: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[operator-learning]] · [[gaussian-process]] · [[fourier-neural-operator]]
