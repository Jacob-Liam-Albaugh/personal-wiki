---
type: concept
area: operators
---

# Operator learning

**Summary**: learning maps between function spaces from data, e.g. coefficient → PDE solution, or strain history → stress history.

**Sources**: `26.10.22 - DeepONets.pdf`, `26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`.
**Last updated**: 2026-11-06

---

## Approaches in the wiki
| Approach | Page | Idea |
|---|---|---|
| Branch-trunk networks | [[deeponet]] | sensor values → coefficients of a learned basis |
| Recurrent hidden-state models | [[recurrent-constitutive-model]] | Markovian ODE in hidden variables, learned pointwise in time |

Bhattacharya et al. (`26.10.29 - Learning Markovian Homogenized Models In Viscoelasticity.pdf`, p. 6) group the literature into model-reduction-based and mesh-invariant (neural-operator) methods.

## Queued sources
`Operators/`: FNO, Neural Operators (Kovachki et al.), LNO, Stuart's *Operator Learning: Algorithms and Analysis*. See [[sources]].

## Related pages
- [[universal-approximation-theorem-for-operators]] · [[lu-2021-deeponet]] · [[bhattacharya-2023-markovian-homogenized-viscoelasticity]]
