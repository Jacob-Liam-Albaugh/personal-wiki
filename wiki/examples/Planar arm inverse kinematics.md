---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [bayesian, inverse-problems, vi]
data-origin: [synthetic]
tasks: [inverse problem and calibration, variational inference]
uses: 1
---

# Planar arm inverse kinematics

**Summary**: 1 use in ASML (ME 697). Data: synthetic. Tasks: inverse problem and calibration, variational inference.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/hbayes/04_amortized_vi.ipynb`.
**Last updated**: 2026-11-18

---

## Planar multi-jointed arm inverse kinematics

`text_books/Machine Learning & Statistics/advanced-scientific-machine-learning/book/inverse/hbayes/04_amortized_vi.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: Bayesian inverse problem (amortized)
- **Technique**: Amortized VI: equinox MLPs (2-20-10-out, ReLU) give mean, Cholesky diag (softplus+1e-6) and off-diag of full-rank Gaussian q(xi/y); ELBO with 6 particles, 10000 steps, Adam lr 0.01 dropping x0.1 at 5000; prior N(0,diag(0.25^2,0.5^2,0.5^2,0.5^2))
- **Data**: Generated on the fly from the prior (30 obs per training batch; 5000 prior samples for plots); noise std 0.01 known
- **Data origin**: synthetic
- **Forward model**: f(xi)=(l1 cos xi2+l2 cos(xi2+xi3)+l3 cos(xi2+xi3+xi4), xi1+l1 sin xi2+l2 sin(xi2+xi3)+l3 sin(xi2+xi3+xi4)); lengths 0.5,0.5,1.0; xi=(slider height, 3 angles)
- **Unknown dimension**: 4
- **Data dimension**: 2
- **Ground truth**: known true xi in test cases
- **What makes it hard**: Non-identifiable, multimodal posterior (many joint configurations reach same end point)
- **Libraries**: jax, equinox, optax
- **References**: Karumuri et al. 2024, sec 3.4, J. Comput. Phys. (S0021999124003668)
- **Notes**: AVI works in some cases, misses true trajectory in others (stated). float32.

## Related pages
- [[Examples catalogue]]
- [[Variational inference]] · [[ELBO]] · [[Amortized VI]] · [[Identifiability]] · [[Adam]]
