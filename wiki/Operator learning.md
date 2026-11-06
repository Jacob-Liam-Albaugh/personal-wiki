---
type: concept
area: operators
tags: [operators, ml]
---

# Operator learning

**Summary**: learning maps between function spaces from data, e.g. coefficient → PDE solution, or strain history → stress history.

## Where it appears
- [[NIF (Pan 2023)]] — parametric neural fields with a shared ParameterNet and ShapeNet (see [[Neural implicit flow]]); [[Physics-informed ML review (Karniadakis 2021)]] names operator regression for the big-data, unknown-physics regime (Box 1).
- Functional inputs and outputs as operators, and dimension reduction (KLE in, PCA out) as the alternative to learning the map: [[Karhunen-Loève expansion]], [[Principal component analysis]].

> [!definition] Solver as operator (book, hup/funcin/01)
> For $-\nabla\cdot(a\nabla u)=f$ in $\Omega$ with $u=g$ on $\partial\Omega$, the solver is a map between function spaces
> $$S:\mathcal A\times\mathcal F\times\mathcal G\to\mathcal U,\qquad (a,f,g)\mapsto u$$
> Maps with functional inputs and outputs are operators. Surrogates, [[Polynomial chaos]] and GPs trained on the discretized input suffer the curse of dimensionality; the remedies are to reduce input dimension ([[Karhunen-Loève expansion]] in, [[Principal component analysis]] out) or to learn the operator directly.

The book's operator-learning chapter (hup/op) is a reading list: [[DeepONet (Lu 2021)]] and [[FNO (Li 2021)]], plus two external JAX tutorials by Ceyron (`simple_deepOnet_in_JAX`, antiderivative operator; `simple_FNO_in_JAX`, 1D Burgers), whose notebooks here are stubs. Citation note: the book cites the FNO paper as the 2020 arXiv preprint (arXiv:2010.08895), the wiki page the 2021 version.

**Covered in**: ASML book hup/op (ME 697 3.2)
**Sources**: `26.10.22 - DeepONets.pdf`, `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`, `papers/Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, `papers/Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, `papers/Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`, `papers/Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`, `text_books/advanced-scientific-machine-learning/book/hup/op/intro.md`, `01_reading.md`, `02_deeponet.ipynb`, `03_fno.ipynb`.
**Last updated**: 2026-11-06

---

## Approaches in the wiki
| Approach | Page | Idea |
|---|---|---|
| Branch-trunk networks | [[DeepONet]] | sensor values → coefficients of a learned basis |
| Recurrent hidden-state models | [[Recurrent constitutive model]] | Markovian ODE in hidden variables, learned pointwise in time |
| Neural operators | [[Neural operator]] | stacked kernel integral layers, mesh-free parameters |
| Fourier neural operator | [[FNO]] | kernel multiplied in Fourier space |
| Laplace neural operator | [[LNO]] | pole-residue kernel, transient plus steady response |
| PCA-Net | [[PCA-Net]] | PCA encoder and decoder around a network |
| Random features | [[Random features model]] | frozen random features, linear fit |

Kovachki et al. 2024 split these into linear methods (DeepONet, PCA-Net: output in a fixed linear subspace) and nonlinear ones (FNO, random features); see [[Encoder-decoder operators]].

## Theory
- Universality: [[Universal approximation for operators]].
- Lower bounds: [[Curse of parametric complexity]].
- Mesh independence: [[Discretization invariance]].

## Benchmarks
[[Burgers equation]] · [[Darcy flow]] · [[Navier-Stokes equations]]

Bhattacharya et al. (`26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`, p. 6) group the literature into model-reduction-based and mesh-invariant (neural-operator) methods.

## Related pages
- [[Universal approximation for operators]] · [[DeepONet (Lu 2021)]] · [[Markovian homogenized viscoelasticity (Bhattacharya 2023)]] · [[Neural operator (Kovachki 2022)]] · [[FNO (Li 2021)]] · [[LNO (Cao 2023)]] · [[Operator learning review (Kovachki 2024)]]
