---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Ho, Salimans 2022, §3.1, pp. 3-4 (describing Dhariwal and Nichol 2021)"
tags: [diffusion, generative, ml]
---

# Classifier guidance

> [!algorithm] Classifier-guided score (Ho, Salimans 2022, §3.1, p. 4)
> Add the gradient of a classifier trained on noisy data:
> ```
> ε̃(z,c) = ε_θ(z,c) - w σ ∇_z log p_θ(c|z)
> ```
> Sampling with ε̃ approximately draws from
> ```
> p̃(z|c) ∝ p(z|c) · p(c|z)^w
> ```
>
> (source: `Diffusion/Ho, Salimans - Classifier-Free Diffusion Guidance.pdf`, p. 4)

**Intuition**: tilt each sampling step toward images the classifier is sure about. This raises Inception score and lowers diversity, much like truncation in BigGAN or low temperature in Glow (p. 3).

Not in this wiki as a primary source: the method is Dhariwal and Nichol 2021. This page follows Ho and Salimans' account of it.

## Points from the account
- The classifier must be trained on noisy inputs \lambda$, so off-the-shelf classifiers do not plug in (p. 2).
- Guiding an unconditional model with weight +1$ is in theory the same as guiding a conditional one with weight $, because (z\mid c)\,p(c\mid z)^w\propto p(z)\,p(c\mid z)^{w+1}$ (p. 4). Dhariwal and Nichol still got their best results guiding a conditional model.
- In a toy example of three Gaussian classes, guidance moves mass away from the other classes and makes each conditional non-Gaussian (Fig. 2, p. 4).
- A classifier is usually smaller than the diffusion model, so guided sampling can be cheaper than [[Classifier-free guidance]] (p. 9).

## Where it appears
- [[Classifier-free guidance (Ho 2022)]]: the baseline that CFG replaces.
- Wiki note: the conditional-score term matches the $\nabla_x\log p_t(y\mid x)$ term of conditional sampling in [[Diffusion models#Reverse-time SDE|score SDEs]] and [[Diffusion posterior sampling]].

**Sources**: `Diffusion/Ho, Salimans - Classifier-Free Diffusion Guidance.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Classifier-free guidance]] · [[Diffusion models]] · [[Noise prediction]]
