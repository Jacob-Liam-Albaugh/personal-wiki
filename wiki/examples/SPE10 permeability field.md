---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [ml]
data-origin: [real]
tasks: [dimensionality reduction]
uses: 1
---

# SPE10 permeability field

**Summary**: 1 use in ASML (ME 697). Data: real. Tasks: dimensionality reduction.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/homework/05_homework.ipynb`.
**Last updated**: 2026-11-18

---

## SPE10 permeability random field (KLE)

`text_books/advanced-scientific-machine-learning/book/homework/05_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: dimensionality reduction / prior modelling
- **Technique**: Nystrom Karhunen-Loeve to 95 percent energy; conditioning on log K(100,200)=-13.2 and log K(300,500)=-25.3
- **Data**: Geologist mean permeability on 60x220 grid over [0,356]x[0,670] m; not in repo.
- **Data origin**: real
- **Data file**: https://raw.githubusercontent.com/PredictiveScienceLab/uq-course/master/homeworks/spe10_permx.dat
- **Forward model**: Log-permeability GP with mean log(M), sd 3.2, lengthscales 50 m and 10 m.
- **Unknown dimension**: KLE coefficients
- **Ground truth**: none
- **Libraries**: numpy, pandas
- **Notes**: Problem 3.

## Related pages
- [[Examples catalogue]]
- [[Karhunen-Loève expansion]] · [[Gaussian process]]
