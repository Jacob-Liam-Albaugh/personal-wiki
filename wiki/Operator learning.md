---
type: concept
area: operators
tags: [operators, ml]
---

# Operator learning

**Summary**: learning maps between function spaces from data, e.g. coefficient → PDE solution, or strain history → stress history.

## Where it appears
- [[NIF (Pan 2023)]] — parametric neural fields with a shared ParameterNet and ShapeNet (see [[Neural implicit flow]]); [[Physics-informed ML review (Karniadakis 2021)]] names operator regression for the big-data, unknown-physics regime (Box 1).
- Functional inputs and outputs as operators, and dimension reduction (KLE in, PCA out) as the alternative to learning the map: [[ME697 3.1 - Functional inputs]], [[ME697 3.2 - Operator learning]].

**Sources**: `26.10.22 - DeepONets.pdf`, `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - Neural Operators.pdf`, `Operators/Li, Kovachki, Stuart, Anandkumar - FNO - Fourier Neural Operators.pdf`, `Operators/Karniadakis, Cao, Goswami - LNO - Laplace Neural Operators.pdf`, `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
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
