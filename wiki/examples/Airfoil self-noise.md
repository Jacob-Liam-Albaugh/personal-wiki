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

# Airfoil self-noise

**Summary**: 1 use in Intro SciML (ME 539). Data: real. Tasks: regression.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-09.ipynb`.
**Last updated**: 2026-11-18

---

## Airfoil self-noise regression

`text_books/intro-to-scientific-machine-learning/notebooks/homework/homework-09.ipynb`

- **Source**: Intro SciML (ME 539), homework, complete
- **Problem**: regression
- **Technique**: MLP small vs 5x100 wide, Adam, RMSE in dB, train-test
- **Data**: 1503 rows; inputs frequency, angle of attack, chord, velocity, suction displacement thickness; output scaled SPL (dB)
- **Data origin**: real
- **Data file**: downloaded from UCI
- **Data dimension**: 5
- **Ground truth**: held-out test set
- **What makes it hard**: extrapolation limits
- **Libraries**: torch
- **References**: Brooks, Pope, Marcolini 1989 doi 10.24432/C5VW2C CC BY 4.0

## Related pages
- [[Examples catalogue]]
- [[Adam]]
