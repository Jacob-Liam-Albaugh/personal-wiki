---
type: lecture
area: me697
areas: [me697, ift]
course: me697
lecture: ift/physics
source-ref: "ME 697 book, ift/physics/intro.md (takeaway only)"
tags: [ift, bayesian, physics-informed, inverse-problems]
---

# ME697 IFT.3 - Physics-informed information field theory

**Summary**: The book folder holds a single takeaway: the smoothing problem can be posed by constructing a prior over the space of state functions that is biased by the physics. No other content exists in the source.
**File**: `advanced-scientific-machine-learning/book/ift/physics/intro.md`. The folder is not in `_toc.yml`.

---

## Topics
- Takeaway: pose smoothing through a prior over state functions biased by the physics (source: ift/physics/intro.md).
- This is the field-level version of the smoothing in [[ME697 6.2 - Filtering and smoothing]].

## Key results
The source states no equations. Background, labelled as a wiki addition:

**Wiki note**: in PIFT the prior penalizes violation of the governing equation, for a residual $r[u]$ and weight $\lambda$:

$$
p[u] \propto \exp\Big(-\tfrac{\lambda}{2}\,\|r[u]\|^2\Big).
$$

A [[PINN]] is the MAP estimate under this prior (see [[Physics-informed prior]] and [[PIFT (Alberts 2023)]]). The square-residual form is one choice; the wiki's [[Physics-informed prior]] page lists the energies the lab papers use.

## Examples
No notebooks. Applied PIFT: [[IFT thermal conductivity (Alberts 2026)]]. Posterior sampling: [[Nested SGLD]].

## Connections
- [[ME697 5.1 - PINN basics]]: the PINN loss as a physics penalty. [[Energy functional]] gives the Dirichlet-energy variant.
- [[ME697 5.3 - PINNs for inverse problems]]: the same inverse problem posed with a point estimate.
- Previous: [[ME697 IFT.2 - Bayesian inference over fields]].

**Sources**: `advanced-scientific-machine-learning/book/ift/intro.md`, `ift/physics/intro.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Information field theory]] · [[Physics-informed prior]] · [[PINN]] · [[PIFT (Alberts 2023)]] · [[Nested SGLD]]
- [[ME697 IFT.1 - Parameter calibration with PIFT]] · [[ME697 IFT.2 - Bayesian inference over fields]]
