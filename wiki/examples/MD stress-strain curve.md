---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [ml]
data-origin: [simulated]
tasks: [regression]
uses: 1
---

# MD stress-strain curve

**Summary**: 1 use in Intro SciML (ME 539). Data: simulated. Tasks: regression.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-04.ipynb`.
**Last updated**: 2026-11-18

---

## Molecular-dynamics stress-strain curve, ultimate strength

`text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-04.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: regression, latent peak inference
- **Technique**: zero-intercept elastic fit, elastic cutoff selection, smooth whole-curve basis with ARDRegression, posterior draws of ultimate strength
- **Data**: 1001 rows x 2 (strain 0-0.2516, stress MPa -29.5 to 326); header #ex Sx; MD tensile loading, material not stated
- **Data origin**: simulated
- **Data file**: data/stress_strain.txt
- **Unknown dimension**: basis weights
- **Data dimension**: 1 input
- **Ground truth**: held-out assessment strains
- **What makes it hard**: peak of noisy curve, model selection
- **Libraries**: sklearn, numpy
- **References**: Strachan group, Purdue MSE

## Related pages
- [[Examples catalogue]]
