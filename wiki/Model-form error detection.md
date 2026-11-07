---
type: concept
area: ift
areas: [ift, inverse-problems, physics-informed]
source-ref: "Alberts 2024 dissertation, Secs. 4.1.1, 4.3, 6.2, pp. 62-63, 79-85, 104-109"
tags: [ift, inverse-problems, physics-informed, uq]
---

# Model-form error detection

**Idea**: The inferred trust $\beta$ of a [[Physics-informed prior]] measures how well the assumed physics matches the data, so $\beta$ itself flags a wrong model.

- **Limits** (pp. 62-63): $\beta=0$ is a flat prior (pure Bayesian regression); $\beta\to\infty$ collapses the prior to the minimum-energy field.
- **Theory** (Sec. 4.3, eq. 4.27, p. 83): for a free-theory Poisson problem,
$$\beta^{*-1}=\frac{(\phi^*-Gq)^\dagger L(\phi^*-Gq)}{\mathrm{Tr}(I)}$$
Exact physics gives $\beta^*=\infty$; model-form error gives finite $\beta^*$, larger for better models. $\beta^*$ also grows with mesh refinement through $\mathrm{Tr}(I)$. Derivation on [[MAP uniqueness in IFT (Alberts 2025)]].
- **Experiment** (Example 2, pp. 104-109): nonlinear $D\phi''-\kappa\phi^3=f$ with a correctness knob $\gamma\in[0,1]$, six values each, Jeffreys prior on $\beta$.
  - (a) wrong source term: the $\beta$ quantile axis spans $3.6\times10^1$ to $4.1\times10^4$ and rises with $\gamma$ (Fig. 6.2a).
  - (b) wrong energy: axis spans $6.0\times10^2$ to $1.6\times10^4$, same trend (Fig. 6.2b).
  - Low $\beta$ makes IFT behave like Bayesian regression and ignore the physics; high $\beta$ lets the physics dominate (p. 108).
- **Caveat** (pp. 108-109): only empirical; the author proposes $\beta$ as a trigger to relax derivation assumptions and revise the physics. When $\beta$ is inferred together with a physical parameter, the uniqueness theorem no longer applies (p. 79).
- Contrast with B-PINNs, whose field posterior collapses as collocation points grow for any residual variance (pp. 100-101); see [[PINN]].

## Where it appears
- [[IFT for engineering inverse problems (Alberts 2024)]] — Chs. 4 and 6.
- [[MAP uniqueness in IFT (Alberts 2025)]] — theory.

**Sources**: `papers/IFT/Alberts - An Information Field Theory Approach to Engineering Inverse Problems.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Physics-informed prior]]
- [[Information field theory]]
- [[Identifiability]]
- [[Bayesian inverse problems]]
- [[Nested SGLD]]
- [[IFT for engineering inverse problems (Alberts 2024)]]
