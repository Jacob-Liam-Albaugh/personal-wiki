---
type: concept
area: bayesian
areas: [bayesian, ml]
source-ref: "Fortuin 2022; Xu et al. 2022; Zhu & Zabaras 2018, §3; Kingma et al. 2015"
tags: [bayesian, ml]
---

# Bayesian neural networks

**Summary**: put a prior on network weights (or functions) and predict by averaging over the posterior, $p(y^*\mid x^*,D)=\int p(y^*\mid x^*,w)\,p(w\mid D)\,dw$, approximated by samples, particles or a variational $q$.

**Sources**: `papers/Bayesian/Fortuin - Priors in Bayesian Deep Learning.pdf`, `papers/Bayesian/Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns.pdf`, `papers/Bayesian/Zhu, Zabaras - Bayseian Deep Convolutional Encoder-Decoder Networks for Surrogate Modeling and Uncertainty Quantification.pdf`.
**Last updated**: 2026-11-06

---

## Inference routes
- Sampling: [[SGLD]], [[Cyclical SG-MCMC]], [[SGHMC]].
- Variational: mean-field weights with [[Variational dropout]]; path-space VI over time-varying weights in [[SDE-BNN (Xu 2022)]].
- Particles: [[SVGD]], used by [[Bayesian DenseED surrogate (Zhu 2018)]] with 20 particles.
- Ensembles: deep ensembles as a cheap posterior proxy (Fortuin eq. 33).
- Averaging over the result: [[Bayesian model averaging]].
- [[Parametric PINN]] and [[PINN]]: the book lists a Bayesian PINN example notebook (`02_example_Bayesian_pinns.ipynb`) but it is a stub, so no inference route is described (source: pinns/inverse).

## Priors (Fortuin)
- Isotropic Gaussian is the default and often misspecified; Fortuin links it to the cold-posterior effect.
- Heavy-tailed alternatives: Student-t (Gaussian with Gamma precision, used by Zhu §3.1), horseshoe.
- Infinite-width limits give [[Gaussian process]] kernels (NNGP, NTK).
- Function-space priors avoid weight-space symmetry but make the KL infinite (§4.2).
- [[Physics-informed prior]] pages tie to [[Physics-informed prior]].

## Calibration
- Xu Table 1: SDE-BNN has lower ECE than ResNet32 on MNIST and CIFAR-10, but on CIFAR-10 it is worse than MFVI ResNet32 and deep ensembles.
- Zhu: reliability diagrams near the diagonal, best at $N=128$ training samples.

## Related pages
- [[Priors in Bayesian deep learning (Fortuin 2022)]] · [[Variational dropout (Kingma 2015)]] · [[SGLD (Welling 2011)]]
- [[Dropout]]. Dropout as an approximate Bayesian model is a later result (Gal) not in these sources **[unverified]**; Srivastava 2014 itself treats dropout as model averaging (§1, §7).
