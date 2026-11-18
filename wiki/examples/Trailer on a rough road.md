---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [uq, bayesian, inverse-problems]
data-origin: [analytic, none]
tasks: [uncertainty propagation, inverse problem and calibration]
uses: 2
---

# Trailer on a rough road

**Summary**: 2 uses in Intro SciML (ME 539). Data: analytic, none. Tasks: uncertainty propagation, inverse problem and calibration.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/intro-to-scientific-machine-learning/notebooks/01 - Introduction to Scientific Machine Learning/hands-on-01.1.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Trailer on rough road (suspension amplitude)

`text_books/intro-to-scientific-machine-learning/notebooks/01 - Introduction to Scientific Machine Learning/hands-on-01.1.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: uncertainty propagation
- **Technique**: plain Monte Carlo, 1000 samples, histograms of omega and X
- **Data**: No data. Inputs k,m,y0,v,L drawn Uniform on stated intervals: k in [159999,160001] N/m, v in [80,150] km/h, m in [100,200] kg, y0 in [0,100] mm, L in [1,2] m.
- **Data origin**: analytic
- **Forward model**: X = /k\*y0/(k - m\*omega^2)/, omega = 2\*pi\*v/L (quarter-car resonance amplitude). Plain numpy, not JAX; closed form.
- **Unknown dimension**: 5 uniform inputs
- **Data dimension**: 2 outputs (omega, X) scalar
- **Ground truth**: none (closed form, no reference density given)
- **What makes it hard**: near-resonance singularity when k ~ m\*omega^2 gives heavy-tailed X
- **Libraries**: numpy, matplotlib, graphviz
- **References**: Purdue Basic Mechanics II lecture book (adapted)
- **Notes**: num_samples loop is pure python; question asks to vary N. Also introduces aleatory vs epistemic and causal graph.

## Trailer on rough road (calibration, conceptual)

`text_books/intro-to-scientific-machine-learning/notebooks/01 - Introduction to Scientific Machine Learning/hands-on-01.2.ipynb`

- **Source**: Intro SciML (ME 539), lecture, partial
- **Problem**: Bayesian inverse problem (stated, not solved)
- **Technique**: causal graph / identifiability discussion; outlines likelihood+prior+Bayes+MCMC/VI recipe
- **Data**: No data and no code beyond graphviz causal graphs. Poses calibration from one noisy amplitude Xm plus sensors mm (mass), vm (velocity) and known k=1000 N/m.
- **Data origin**: none
- **Forward model**: same as trailer uncertainty propagation: X=/k y0/(k-m omega^2)/, omega=2 pi v/L
- **Unknown dimension**: m,y0,v,L (k known); k,m,y0,v,L unidentifiable from one Xm
- **Data dimension**: Xm, mm, vm scalars
- **Ground truth**: none
- **What makes it hard**: non-identifiability from single measurement (explicitly discussed)
- **Libraries**: graphviz
- **Notes**: Conceptual stub for the inverse problem; the reusable bit is the model and the identifiability argument.

## Related pages
- [[Examples catalogue]]
- [[Markov chain Monte Carlo]] · [[Variational inference]] · [[Identifiability]]
