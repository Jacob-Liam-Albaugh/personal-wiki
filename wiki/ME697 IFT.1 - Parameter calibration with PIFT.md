---
type: lecture
area: me697
areas: [me697, ift]
course: me697
lecture: ift/calibration
source-ref: "ME 697 book, ift/calibration/intro.md (takeaway only)"
tags: [ift, bayesian, inverse-problems, sampling]
---

# ME697 IFT.1 - Parameter calibration with PIFT

**Summary**: The book folder holds a single takeaway: calibrating parameters with physics-informed information field theory requires dealing with an intractable quantity, the partition function. There is no other content in the source.
**File**: `advanced-scientific-machine-learning/book/ift/calibration/intro.md`. The folder is not in `_toc.yml`.

---

## Topics
- Parent module `ift/intro.md`: solve severely ill-defined inverse problems involving physical fields (source: ift/intro.md).
- Takeaway: parameter calibration requires dealing with the partition function (source: ift/calibration/intro.md).

## Key results
The source states no equations. Background, labelled as a wiki addition:

**Wiki note**: in a [[Physics-informed prior]] the prior density over a field is $p(u\mid\theta)=e^{-H_\theta[u]}/Z(\theta)$, where $Z$ is the partition function. Calibrating $\theta$ from the marginal likelihood needs $\nabla_\theta\log Z$, which is a path integral over fields and cannot be computed in closed form. Details for the lab's approach, including how this is handled by nested sampling of fields, are on [[Information field theory]], [[PIFT (Alberts 2023)]] and [[Nested SGLD]] **[unverified: check those pages for the exact estimator]**.

## Examples
No notebooks. Worked IFT calibration appears in [[IFT thermal conductivity (Alberts 2026)]].

## Connections
- Same marginal-likelihood problem as hyperparameter learning for a [[Gaussian process]], except that the energy is not quadratic.
- Sampling tools: [[Langevin dynamics]], [[SGLD]], [[Markov chain Monte Carlo]].
- Sibling pages: [[ME697 IFT.2 - Bayesian inference over fields]], [[ME697 IFT.3 - Physics-informed information field theory]].

**Sources**: `advanced-scientific-machine-learning/book/ift/intro.md`, `ift/calibration/intro.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Information field theory]] · [[Physics-informed prior]] · [[PIFT (Alberts 2023)]] · [[Nested SGLD]]
- [[ME697 IFT.2 - Bayesian inference over fields]] · [[ME697 IFT.3 - Physics-informed information field theory]] · [[ME697 7 - Homework]]
