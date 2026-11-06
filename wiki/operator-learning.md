---
type: concept
area: operators
---

# Operator learning

**Summary**: learning maps between function spaces from data, e.g. coefficient → PDE solution, or strain history → stress history.

**Sources**: `26.10.22 - DeepONets.pdf`, `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, `Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`, `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

## Approaches in the wiki
| Approach | Page | Idea |
|---|---|---|
| Branch-trunk networks | [[deeponet]] | sensor values → coefficients of a learned basis |
| Recurrent hidden-state models | [[recurrent-constitutive-model]] | Markovian ODE in hidden variables, learned pointwise in time |
| Neural operators | [[neural-operator]] | stacked kernel integral layers, mesh-free parameters |
| Fourier neural operator | [[fourier-neural-operator]] | kernel multiplied in Fourier space |
| Laplace neural operator | [[laplace-neural-operator]] | pole-residue kernel, transient plus steady response |
| PCA-Net | [[pca-net]] | PCA encoder and decoder around a network |
| Random features | [[random-features-model]] | frozen random features, linear fit |

Kovachki et al. 2024 split these into linear methods (DeepONet, PCA-Net: output in a fixed linear subspace) and nonlinear ones (FNO, random features); see [[encoder-decoder-architecture]].

## Theory
- Universality: [[universal-approximation-theorem-for-operators]].
- Lower bounds: [[curse-of-parametric-complexity]].
- Mesh independence: [[discretization-invariance]].

## Benchmarks
[[burgers-equation]] · [[darcy-flow]] · [[navier-stokes-equations]]

Bhattacharya et al. (`26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`, p. 6) group the literature into model-reduction-based and mesh-invariant (neural-operator) methods.

## Related pages
- [[universal-approximation-theorem-for-operators]] · [[lu-2021-deeponet]] · [[bhattacharya-2023-markovian-homogenized-viscoelasticity]] · [[kovachki-2022-neural-operator]] · [[li-2021-fno]] · [[cao-2023-lno]] · [[kovachki-2024-operator-learning-review]]
