---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [uq]
data-origin: [real]
tasks: [distribution fitting]
uses: 1
---

# Fatigue life of 6061-T6 aluminium

**Summary**: 1 use in Intro SciML (ME 539). Data: real. Tasks: distribution fitting.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-01.ipynb`.
**Last updated**: 2026-11-18

---

## Fatigue life of 6061-T6 aluminium (Birnbaum-Saunders)

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/homework/homework-01.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: distribution fitting / reliability
- **Technique**: MLE Weibull, lognormal, exponential, probability-integral transform, empirical survival, replacement-age risk
- **Data**: 101 cycles-to-rupture (thousands) at max stress 21000 psi, 370-2130+
- **Data origin**: real
- **Data file**: embedded array
- **Unknown dimension**: 2 per model
- **Data dimension**: 101
- **Ground truth**: empirical CDF
- **What makes it hard**: tail risk at 300k cycles
- **Libraries**: numpy, scipy
- **References**: NIST eda4291; Birnbaum & Saunders 1958 doi 10.1080/01621459.1958.10501433

## Related pages
- [[Examples catalogue]]
