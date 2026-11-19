---
type: example
area: me539
areas: [me539]
source-ref: "Intro SciML (ME 539)"
tags: [ml]
data-origin: [real]
tasks: [regression]
uses: 3
---

# Motorcycle crash (mcycle)

**Summary**: 3 uses in Intro SciML (ME 539). Data: real. Tasks: regression.

**Covered in**: Intro SciML (ME 539)
**Sources**: `text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/13 - Linear Regression via Least Squares/hands-on-13.3.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Motorcycle crash head acceleration (mcycle)

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/13 - Linear Regression via Least Squares/hands-on-13.3.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: regression
- **Technique**: least squares via numpy.linalg.lstsq with polynomial, Fourier and radial basis features
- **Data**: 94 rows x 4 columns (times in ms 2.4-57.6; accel in g -134 to 75; strata 1-3; v residual variance estimate 3.7-607). Replicates in time removed from MASS mcycle. Notebook uses only columns times (x) and accel (y).
- **Data origin**: real
- **Data file**: data/motor.dat
- **Forward model**: Generalized linear model y=w^T phi(x): polynomial, Fourier (cos/sin, L=60) and RBF (exp(-(x-c)^2/(2 l^2))) design matrices, no physics model.
- **Unknown dimension**: m basis weights (degree/terms chosen by user)
- **Data dimension**: 94 (x,y) pairs
- **Ground truth**: none (real data); no held-out test in this notebook
- **What makes it hard**: strongly nonstationary, heteroscedastic (strata variances differ ~160x), non-polynomial shape; classic test for GP/nonparametric regression
- **Libraries**: numpy, matplotlib
- **References**: Silverman (1985) JRSS B 47, 1-52; Davison and Hinkley (1997); Venables and Ripley (1994)
- **Notes**: Fits only; accuracy is judged in 13.4.

## Motorcycle crash head acceleration (mcycle)

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/13 - Linear Regression via Least Squares/hands-on-13.4.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: regression with held-out validation
- **Technique**: least squares; test MSE, relative MSE vs constant model, R^2, parity plot
- **Data**: same 94x4 file; uses times, accel only. 33% hold-out via sklearn train_test_split (seed 12345), ~62 train / ~32 test.
- **Data origin**: real
- **Data file**: data/motor.dat
- **Forward model**: Generalized linear model: polynomial (degree 3 shown), Fourier (10 terms, L=60), RBF.
- **Unknown dimension**: m basis weights
- **Data dimension**: 94 pairs split ~62/32
- **Ground truth**: held-out test set
- **What makes it hard**: heteroscedastic noise caps achievable R^2; polynomial underfits
- **Libraries**: numpy, scikit-learn (train_test_split), matplotlib
- **References**: Silverman (1985)
- **Notes**: Reports test R^2: cubic polynomial explains about 23% of variance, Fourier features about 81%. Exercises ask degrees 4,5,10,20 and RBF.

## Motorcycle crash head acceleration (mcycle) neural regression

`text_books/Machine Learning & Statistics/intro-to-scientific-machine-learning/notebooks/24 - Deep neural networks for regression/hands-on-24.ipynb`

- **Source**: Intro SciML (ME 539), lecture, complete
- **Problem**: 1D regression
- **Technique**: MLP 1-20-20-20-20-1 ReLU, StandardScaler, SGD lr 0.01 batch 5, 10000 its, 70/30 unseeded split
- **Data**: 94 rows x 4 cols: times (ms after impact, 2.4-57.6), accel (g, -134 to 75), strata (1-3), v (variance estimate per stratum, 3.7-607); replicate times removed
- **Data origin**: real
- **Data file**: data/motor.dat
- **Unknown dimension**: ~1.3k weights
- **Data dimension**: 1 input
- **Ground truth**: held-out test split
- **What makes it hard**: heteroscedastic, non-stationary, tiny data
- **Libraries**: torch, sklearn
- **References**: Silverman 1985 JRSS B 47:1-52

## Related pages
- [[Examples catalogue]]
- [[Gaussian process]] · [[Fourier features]] · [[SGD]]
