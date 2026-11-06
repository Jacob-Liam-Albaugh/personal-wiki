---
type: lecture
area: me697
areas: [me697, ift]
course: me697
lecture: ift/fields
source-ref: "ME 697 book, ift/fields/intro.md (takeaway only)"
tags: [ift, bayesian, gp]
---

# ME697 IFT.2 - Bayesian inference over fields

**Summary**: The book folder holds a single takeaway: Feynman path integrals can be used to formally develop a generalization of Gaussian processes. No other content exists in the source.
**File**: `advanced-scientific-machine-learning/book/ift/fields/intro.md`. The folder is not in `_toc.yml`.

---

## Topics
- Takeaway: Feynman path integrals give a formal generalization of Gaussian processes (source: ift/fields/intro.md).
- Objective of the parent module: ill-defined inverse problems for physical fields (source: ift/intro.md).

## Key results
The source states no equations. Background, labelled as a wiki addition:

**Wiki note**: a [[Gaussian process]] is a Gaussian measure on functions, equivalently a field with quadratic energy. Allowing a non-quadratic energy, the prior over a field $u$ is written as a path integral

$$
p[u] \propto e^{-H[u]},
$$

which is the field-theory view used by [[Information field theory]]. The normalizing integral is the partition function, see [[ME697 IFT.1 - Parameter calibration with PIFT]].

## Examples
No notebooks. Prior fields built from a GP are sampled via the [[Karhunen-Loève expansion]], see [[ME697 6.1 - Stochastic differential equations]] and [[ME697 7 - Homework]] (homework 5, permeability).

## Connections
- [[Brownian motion]] is the simplest field with a path-integral (Wiener measure) description.
- Next: [[ME697 IFT.3 - Physics-informed information field theory]].

**Sources**: `advanced-scientific-machine-learning/book/ift/intro.md`, `ift/fields/intro.md`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Information field theory]] · [[Gaussian process]] · [[Physics-informed prior]] · [[Karhunen-Loève expansion]]
- [[ME697 IFT.1 - Parameter calibration with PIFT]] · [[ME697 IFT.3 - Physics-informed information field theory]]
