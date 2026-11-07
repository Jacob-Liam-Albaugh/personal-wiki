---
type: method
area: physics-informed
areas: [physics-informed, uq]
source-ref: "Sahli Costabal et al. 2020, §2.2, eqs. 8-9, p. 3 (method of Osband et al. 2018, cited, not read)"
tags: [uq, bayesian, ml, physics-informed]
---

# Randomized prior functions

> [!algorithm] Ensemble of networks with fixed random priors
> Each member $k$ predicts $f_k(x)=NN(x;\theta_k)+NN(x;\tilde\theta_k)$. The prior network $\tilde\theta_k$ is drawn (Glorot init) and **frozen**; only $\theta_k$ is trained, on data perturbed by $N(0,\sigma_N^2)$, with an L2 penalty. The prediction is the ensemble mean, the spread is the epistemic uncertainty.
>
> (source: `Costabal et al - Physics-Informed Neural Networks for Cardiac Activation Mapping.pdf`, eqs. 8-9, p. 3)

**Intuition**: MSE is a normal likelihood and L2 a zero-mean normal weight prior. For a linear regressor, minimizing the loss from a random start with a randomly shifted target and a fixed prior sample draws from the posterior $p(\theta|D)$ (as the paper states, citing Osband et al.). For deep nets it is an approximation that is cheap, unlike MCMC.

## Cost and use
- 30 networks chosen; error reduction slows beyond that, and 30 in parallel cost 1.75x one network (pp. 6, 9).
- The entropy of the ensemble's predictive distribution (non-parametric estimator) is the acquisition score in [[Active learning]]; high-entropy regions coincide with high error (Fig. 5).
- Posterior was not Gaussian there, which the authors attribute to the total-variation term.

## Failure modes
- Approximate: uncertainty in the cardiac case uses Euclidean not geodesic distance on the atrial surface (p. 10). Wiki note: no calibration check beyond the entropy-error co-location is reported.
- Kissas et al. name bootstrapped ensembles, MCMC and generative models as the UQ options they did not implement ([[Cardiovascular flow PINNs (Kissas 2020)]], p. 25).

## Where it appears
- [[Cardiac activation PINN (Sahli Costabal 2020)]] — UQ for a PINN, feeding active learning.

**Sources**: `papers/Physics Informed Architectures/Costabal et al - Physics-Informed Neural Networks for Cardiac Activation Mapping.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[PINN]] · [[Active learning]] · [[Bayesian neural networks]] · [[Physics-informed prior]] · [[Gaussian process]]
