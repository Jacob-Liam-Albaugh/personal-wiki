---
type: concept
area: bayesian
areas: [bayesian, me697]
source-ref: "ME 697 book, inverse/basics 02, 05; inverse/vi 02; Tsilifis 2014 ex. 3.1"
tags: [inverse-problems, bayesian, vi, uq]
---

# Catalysis problem

**Summary**: The running inverse problem of Part 4: infer five rate constants (and the noise level) of a six-species linear reaction network from noisy concentrations. It is solved classically, by [[Laplace approximation]], and by [[Variational inference]].

**Covered in**: ASML book inverse/basics (ME 697 4.1)
**Sources**: `text_books/advanced-scientific-machine-learning/book/inverse/basics/02_classic_example.ipynb`, `05_laplace_example.ipynb`, `vi/02_catalysis.ipynb`.
**Last updated**: 2026-11-06

---

## Model
The ODE is linear,
$$\dot z=A(k)\,z,\quad z_0=(500,0,0,0,0,0).$$
There are six species, one of which (X) is a hidden intermediate, and five rate constants $k$. The source is [[Variational inverse problems (Tsilifis 2014)]], ex. 3.1, based on the experiment of Katsounaros et al. (2012). The mass balance of the measured species does not close, which motivates X (source: basics/02).

Rates are scaled as
$$x_i=\log(180\,k_i).$$

## Data
Five species are measured at six times $t_j=30j$ minutes. The data vector is $y=\mathrm{vec}(Y)\in\mathbb R^{30}$.

## Three solutions
- **Classical**: Adam, learning rate 0.1, 100 iterations, loss scaled by 500, diffrax Tsit5 (basics/02). See [[Bayesian inverse problems]].
- **Laplace**: $\sigma=5$, $\gamma=10$, 300 Adam iterations; Hessian by finite differences (basics/05).
- **VI**: all unknowns mapped to standard-normal $x\in\mathbb R^6$ (rates lognormal with $\gamma=2$, noise variance exponential), a full-rank Gaussian guide with 27 parameters, Adam $5\cdot10^{-2}$, batch 5, 3000 steps (vi/02). See [[Variational inference]].

Wiki note: the vectors in the code have six entries while the text says five rates; the sixth is the noise parameter in the VI notebook and a prior-only entry in the Laplace one.

## Related pages
- [[Bayesian inverse problems]] · [[ELBO]] · [[Surrogate model]]
- [[Identifiability]]
