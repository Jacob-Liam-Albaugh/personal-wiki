---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Ho, Salimans 2022, eq. 6, Alg. 1-2, Tables 1-2, pp. 4-9"
tags: [diffusion, generative, ml]
---

# Classifier-free guidance (CFG)

> [!algorithm] Guided noise prediction (Ho, Salimans 2022, eq. 6, p. 5)
> One network $\epsilon_\theta(z,c)$, trained with the label replaced by $\varnothing$ with probability \text{uncond}$ (Alg. 1). Sample with
> ```
> ε̃(z,c) = (1+w) ε_θ(z,c) - w ε_θ(z)
> ```
> where $\epsilon_\theta(z)=\epsilon_\theta(z,\varnothing)$. =0$ is plain conditional sampling.
>
> (source: `papers/Diffusion/Ho, Salimans - Classifier-Free Diffusion Guidance.pdf`, pp. 4-5)

**Intuition**: push past the conditional prediction, away from the unconditional one. This gives the fidelity-for-diversity trade-off of [[Classifier guidance]] without a classifier.

## Implicit classifier (p. 5)
With exact scores, Bayes' rule gives an implicit classifier:
```
p_i(c|z) ∝ p(z|c) / p(z)
∇ log p_i(c|z) = -(ε*(z,c) - ε*(z)) / σ
```
Classifier guidance with $ reproduces eq. 6. With learned networks $\epsilon_\theta(z,c)-\epsilon_\theta(z)$ is in general not a gradient of anything. So CFG cannot be read as an adversarial attack on a classifier, and the paper gives no guarantee the implicit classifier is good.

## Training and sampling
- Alg. 1 (p. 4): drop the label with probability \text{uncond}$, sample a log-SNR λ, take an ε-loss step ([[Noise prediction]]).
- Alg. 2 (p. 5): form ε̃ at each step, then any sampler step. The paper notes DDIM could be used ([[DDIM]]).
- \text{uncond}\in\{0.1,0.2\}$ work about equally; 0.5 is worse across the FID/IS frontier (p. 8).
- Cost: two forward passes per step, conditional and unconditional (p. 9).

## Results (ImageNet)
```
64×64, p_uncond = 0.1:
  w=0    FID 1.80   IS 53.71
  w=0.1  FID 1.55   IS 66.11
  w=4    FID 26.22  IS 260.2
128×128, T=256:
  w=0.3  FID 2.43   IS 158.47
  w=4    FID 21.53  IS 421.03
```
(Tables 1-2, pp. 7-8). Best FID at small $, best IS at large $. Wiki note: the text calls FID "monotonically decreasing" in $, but the tables show FID rising after its minimum (see [[Classifier-free guidance (Ho 2022)]]).

## Where it appears
- [[Classifier-free guidance (Ho 2022)]].
- [[Step-by-step diffusion (Nakkiran 2025)]]: lists guidance among topics outside the tutorial's scope **[unverified]**.

**Sources**: `papers/Diffusion/Ho, Salimans - Classifier-Free Diffusion Guidance.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Classifier guidance]] · [[Diffusion models]] · [[DDPM]] · [[Noise schedule]]
