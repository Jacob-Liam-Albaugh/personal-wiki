---
type: method
area: bayesian
areas: [bayesian, stochastic]
source-ref: "Zhu & Zabaras 2018, §3.3, Alg. 1; Fortuin 2022, eq. 34"
tags: [sampling, vi, bayesian]
---

# Stein variational gradient descent (SVGD)

> [!algorithm] SVGD (Liu & Wang 2016; as in Zhu & Zabaras Alg. 1)
> Particles $\{\theta^i\}_{i=1}^S$, kernel $k$. Repeat
> $$\theta^i\leftarrow\theta^i+\epsilon\,\phi(\theta^i)$$
> $$\phi(\theta)=\tfrac1S\textstyle\sum_j\big[k(\theta^j,\theta)\nabla\log p(\theta^j)+\nabla_{\theta^j}k(\theta^j,\theta)\big].$$
>
> (source: `papers/Bayesian/Zhu, Zabaras - Bayseian Deep Convolutional Encoder-Decoder Networks for Surrogate Modeling and Uncertainty Quantification.pdf`, Alg. 1)

**Intuition**: the first term pulls particles uphill on the posterior, smoothed by the kernel; the second pushes them apart so they do not collapse to the mode. With one particle it is gradient ascent to the MAP.

## Basic consequences
With Stein operator $\mathcal T_p\phi=(\nabla\log p)\cdot\phi+\nabla\cdot\phi$ and map $T=\mathrm{id}+\epsilon\phi$:
$$-\tfrac{d}{d\epsilon}\mathrm{KL}(T\mu\|p)\big|_{\epsilon=0}=\mathbb E_\mu[\mathcal T_p\phi]$$
The update is the steepest-descent direction for KL in the kernel's RKHS (Zhu p. 15).

## Notes
- Zhu's PDF equations were garbled in extraction; the update above is the standard form **[unverified]** against the scan.
- Fortuin writes the same update with a minus sign on the kernel-gradient term (eq. 34), a sign convention for the kernel argument.

## Where it appears
- [[Bayesian DenseED surrogate (Zhu 2018)]]: inference for a Bayesian DenseED surrogate.
- [[Priors in Bayesian deep learning (Fortuin 2022)]]: as an ensemble-style approximation.

**Sources**: `papers/Bayesian/Zhu, Zabaras - Bayseian Deep Convolutional Encoder-Decoder Networks for Surrogate Modeling and Uncertainty Quantification.pdf`, `papers/Bayesian/Fortuin - Priors in Bayesian Deep Learning.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Variational inference]] · [[KL divergence]] · [[SGLD]] · [[Bayesian neural networks]]
