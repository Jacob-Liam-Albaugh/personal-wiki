---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [uq, ml]
data-origin: [analytic]
tasks: [surrogate modelling, uncertainty propagation]
uses: 5
---

# Polynomial chaos 1D test functions

**Summary**: 5 uses in ASML (ME 697). Data: analytic. Tasks: surrogate modelling, uncertainty propagation.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/polynomial_chaos/04_orthpol_demo.ipynb` and the notebooks listed below.
**Last updated**: 2026-11-18

---

## Orthogonal polynomials for bimodal Gaussian mixture

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/polynomial_chaos/04_orthpol_demo.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: surrogate modelling / basis construction
- **Technique**: orthojax recurrence for arbitrary weight
- **Data origin**: analytic
- **Forward model**: Weight density 0.5 N(-1,0.5^2)+0.5 N(1,0.5^2); degree-10 orthonormal polynomials built with orthojax
- **Unknown dimension**: 1
- **Ground truth**: orthonormality checkable
- **What makes it hard**: bimodal weight
- **Libraries**: orthojax, JAX

## Legendre projection of sinc function

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/polynomial_chaos/04_orthpol_demo.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: surrogate modelling
- **Technique**: orthogonal projection
- **Data origin**: analytic
- **Forward model**: f(x)=sin(10x)/(10x) on [-1,1] projected onto normalized Legendre polynomials up to degree 10
- **Unknown dimension**: 1
- **Ground truth**: exact f known
- **What makes it hard**: oscillatory function, truncation error
- **Libraries**: orthojax, JAX

## PCE uncertainty propagation through sin(2X)/(2X)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/polynomial_chaos/04_orthpol_demo.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: uncertainty propagation
- **Technique**: PCE vs Monte Carlo (10,000 samples)
- **Data origin**: analytic
- **Forward model**: Z=sin(2 Xi)/(2 Xi), Xi~N(0,1); Hermite PC degree 11; mean = first coeff, variance = sum of squared higher coeffs
- **Unknown dimension**: 1
- **Data dimension**: scalar output
- **Ground truth**: MC reference
- **Libraries**: orthojax, JAX
- **Notes**: PCE mean 0.5981, variance 0.1439; MC mean 0.5967, variance 0.1449.

## 2D tensor-product PC bases

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/up/polynomial_chaos/06_tensor_product.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: basis construction / quadrature check
- **Technique**: tensor-product orthogonal polynomials, sparse-grid quadrature
- **Data origin**: analytic
- **Forward model**: 2D Legendre and Hermite tensor-product bases, degree 3 each (total degree 6); orthogonality checked with Smolyak sparse grids (py-design, Legendre level 7 'F1', Hermite level 6 'GH')
- **Unknown dimension**: 2
- **Ground truth**: orthonormality
- **Libraries**: orthojax, py-design, JAX
- **Notes**: Basis demo; also notes on mixed or dependent variables (inverse CDF, Cholesky, Rosenblatt). Marginal as a test problem.

## PCE of sin(xi), xi~Exp(1)

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/homework/03_homework.ipynb`

- **Source**: ASML (ME 697), homework, partial
- **Problem**: uncertainty propagation
- **Technique**: Polynomial chaos with orthojax
- **Data origin**: analytic
- **Forward model**: y=sin(xi), xi~Exp(1)
- **Unknown dimension**: 1
- **Ground truth**: Monte Carlo
- **Libraries**: orthojax
- **Notes**: Problem 3. Problems 1-2 are proofs, skipped.

## Related pages
- [[Examples catalogue]]
- [[Polynomial chaos]] · [[Surrogate model]]
