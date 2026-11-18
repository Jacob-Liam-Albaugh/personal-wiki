---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [ml]
data-origin: [real]
tasks: [regression]
uses: 1
---

# Chwirut1 ultrasonic calibration

**Summary**: 1 use in Intro SciML (ME 539). Data: real. Tasks: regression.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-07.ipynb`.
**Last updated**: 2026-11-18

---

## NIST Chwirut1 ultrasonic calibration GP

`text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-07.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: GP regression with replicates
- **Technique**: GP with learned noise, Matern 3/2 vs other kernel, RMSE, NLPD, interval width, Bastos-O'Hagan standardised errors, chi-square
- **Data**: replicated ultrasonic response vs metal distance; hold out distances 2.25-2.75 (interpolation) and >=5.0 (extrapolation)
- **Data origin**: real
- **Data file**: download Chwirut1.dat (not in data/)
- **Unknown dimension**: 3 (amplitude, length, noise)
- **Data dimension**: 1 input
- **Ground truth**: held-out distances
- **What makes it hard**: extrapolation
- **Libraries**: numpy, scipy
- **References**: NIST STRD Chwirut1; Bastos & O'Hagan 2009 Technometrics 51
- **Notes**: row count 214 not verified

## Related pages
- [[Examples catalogue]]
- [[Gaussian process]]
