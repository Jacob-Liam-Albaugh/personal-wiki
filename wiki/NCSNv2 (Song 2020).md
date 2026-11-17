---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Song & Ermon 2020, Props. 1-3, Techniques 1-5, Table 1, pp. 3-9"
tags: [diffusion, generative, sampling]
authors: ["[[Yang Song]]", "[[Stefano Ermon]]"]
year: 2020
venue: "NeurIPS 2020"
file: "[[papers/Diffusion/Song, Ermon - Improved Techniques for Training Score-Based Generative Models.pdf]]"
---

# Improved Techniques for Training Score-Based Generative Models (Song 2020)

**Authors**: Yang Song, Stefano Ermon · **Year**: 2020 · **File**: [[papers/Diffusion/Song, Ermon - Improved Techniques for Training Score-Based Generative Models.pdf]] · **Code**: none given in the paper text

## Summary
NCSNv2 is a set of five rules for configuring a noise-conditional score network. They set the largest noise scale, the spacing of the scales, how the network is conditioned on σ, the Langevin step size and step count, and weight averaging. Each rule comes from a small analysis rather than a grid search. With them, score models train stably and generate 64-256 px images where the original NCSN failed above 96 px. CIFAR-10 FID drops from 25.32 to 10.87 when the final denoising step is used. Part of [[Diffusion models]].

## Problem
The original NCSN (Song & Ermon 2019) perturbs data at $L$ Gaussian noise scales, learns $s_\theta(x,\sigma)\approx\nabla_x\log p_\sigma(x)$ by [[Score matching|denoising score matching]], and samples with annealed [[Langevin dynamics]]. It used hand-set values: $L=10$, $\sigma_1=1$, $\sigma_L=0.01$, $\epsilon=2\times10^{-5}$, $T=100$ (p. 3). It worked at 32×32 but was unstable and failed at higher resolution. The paper asks how to choose these values from the data.

## Method

> [!algorithm] Annealed Langevin dynamics (Alg. 1, p. 3)
> Set $\alpha_i=\epsilon\,\sigma_i^2/\sigma_L^2$. For each $i=1..L$, run $T$ steps of
> ```
> x ← x + α_i s_θ(x, σ_i)
>       + √(2 α_i) z,   z ~ N(0, I)
> ```
> Optional last step (denoising):
> ```
> x ← x + σ_L² s_θ(x, σ_L)
> ```
> This is Tweedie's formula; see [[Score matching#Tweedie's formula]]. The paper credits the trick to Jolicoeur-Martineau et al. 2020 (p. 7).

Training loss (eq. 2, p. 3):
```
(1/2L) Σ_i E ‖ σ_i s_θ(x̃, σ_i)
            + (x̃ − x)/σ_i ‖²
x̃ ~ N(x, σ_i² I)
```

> [!theorem] Technique 1: initial noise scale (Prop. 1, p. 4)
> For an empirical distribution perturbed by $N(0,\sigma_1^2 I)$, the expected posterior weight $r$ that a sample from point $i$ gives to point $j$ is bounded:
> ```
> E_{p(i)}[ r(j) ]
>   ≤ ½ exp(−‖x(i) − x(j)‖² / (8 σ1²))
> ```
> If $\sigma_1$ is small, Langevin cannot move between modes. **Rule**: make $\sigma_1$ about as large as the maximum pairwise distance in the training data.

On CIFAR-10 the median pairwise distance is about 18. With $\sigma_1=1$ the bound is below $10^{-17}$. In a 10k-component Gaussian mixture centred on test images, sampled with the true score, $\sigma_1=50$ gives a sample pairwise distance of 18.65 (data: 17.78). $\sigma_1=1$ gives 10.12 (Fig. 2, p. 4).

> [!theorem] Technique 2: other noise scales (Prop. 2, p. 5)
> For $x\sim N(0,\sigma^2I)$ in $D$ dimensions, $r=\|x\|$ satisfies
> ```
> r − √D σ  →  N(0, σ²/2)
> ```
> Mass sits on a thin shell of radius $\sqrt D\,\sigma$. Neighbouring scales should overlap in their $3$-sigma shells. **Rule**: use a geometric sequence $\sigma_{i}=\gamma\sigma_{i+1}$ with $\gamma$ chosen so that
> ```
> Φ(√(2D)(γ−1) + 3γ)
>  − Φ(√(2D)(γ−1) − 3γ) ≈ 0.5
> ```
> $\Phi$ is the standard normal CDF. With $L=10$ at 32×32 the original NCSN had this overlap near 0.

> [!definition] Technique 3: noise conditioning (p. 5)
> Use $s_\theta(x,\sigma)=s_\theta(x)/\sigma$, an unconditional network divided by $\sigma$. The reason is $\mathbb E\|\nabla\log p_\sigma\|\approx\sqrt D/\sigma$. This drops the per-scale normalisation parameters (memory linear in $L$), allows continuous $\sigma$, and gives a similar training loss (Fig. 3).

> [!theorem] Technique 4: step size and step count (Prop. 3, p. 6)
> For a single data point, after $T$ Langevin steps at scale $i$, the ratio $s_T^2/\sigma_i^2$ of sample variance to target variance has a closed form (eq. 4). With a geometric $\sigma$ the ratio is the same for every scale and does not depend on $D$.
> **Rule**: pick $T$ from the compute budget (so $T\times L$ is several thousand), then grid-search $\epsilon$ so that eq. 4 ≈ 1.

> [!definition] Technique 5: weight EMA (p. 7)
> Keep an exponential moving average of weights:
> ```
> θ′ ← m θ′ + (1 − m) θ_i
> m = 0.999
> ```
> Sample with $\theta'$. This removes the large FID swings during training and the colour-shift artifacts (Fig. 4).

Architecture: RefineNet-based, ELU activations, trained with [[Adam]] (p. 7).

## Results

> [!example] Inception and FID (Table 1, p. 7)
> | Model | CIFAR-10 IS | CIFAR-10 FID | CelebA 64 FID |
> |---|---|---|---|
> | NCSN | 8.87 ± .12 | 25.32 | 26.89 |
> | NCSN + denoising | 7.32 ± .12 | 29.8 | 25.30 |
> | NCSNv2 | 8.73 ± .13 | 31.75 | 28.86 |
> | NCSNv2 + denoising | 8.40 ± .07 | 10.87 | 10.23 |
> | WGAN-GP | 7.86 | 36.4 | |
> | SNGAN | 8.22 | 21.7 | |
>
> Other baselines in the table: PixelCNN IS 4.60 / FID 65.93, IGEBM 6.02 / 40.58.

- The denoising step matters much more for NCSNv2 than for NCSN: FID 31.75 → 10.87.
- Ablation (Fig. 5, p. 8): techniques are grouped as {5}, {1, 2, 4} and {3}. Every combination beats NCSN, but FID is not monotone as groups are removed.
- Scale (p. 8): FFHQ 256, LSUN bedroom and tower 128, church 96, CelebA 64. NCSN fails above 96 px.
- Memorisation check: training and test losses track each other, nearest neighbours in the training set differ from samples, and interpolations are smooth (p. 9).

## Limitations
- Authors: Inception and FID "have known issues" (p. 8). Performance could improve with hyperparameter tuning. Open questions are a theory of sample quality and non-Gaussian noise (Conclusion, p. 9).
- Wiki note: the rules use a single-point or empirical-mixture model; Prop. 3 assumes one data point. They are heuristics for real data.
- Wiki note: NCSNv2 without denoising is worse than NCSN on FID. The headline gain depends on the last Tweedie step.

## Connections
- Builds on NCSN (Song & Ermon 2019; not in the wiki), [[Score matching]] (Hyvärinen 2005, Vincent 2011) and [[Langevin dynamics]]. It cites [[SGLD (Welling 2011)]] and uses [[Adam paper (Kingma 2015)|Adam]].
- [[Score SDE (Song 2021)]] takes the geometric $\sigma$ schedule to the continuous limit: the VE SDE. NCSNv2 is a baseline there (FID 10.87). See [[Diffusion models#SMLD and DDPM]].
- [[DDPM (Ho 2020)]] compares against it (FID 31.75, no denoising step). DDPM fixes the noise schedule by a variance-preserving process instead of the rules here.
- Technique 3 (score ∝ 1/σ) is the same scaling as $\epsilon$-prediction; see [[Noise prediction]].
- Technique 5 is reused by later diffusion models (Score SDE uses EMA 0.999 and 0.9999).

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[SGLD (Welling 2011)]]
**Cited by in this wiki**: [[DDIM (Song 2021)]], [[DDPM (Ho 2020)]], [[Inflationary flows (de Albuquerque 2024)]]
%% refs:end %%

**Sources**: `papers/Diffusion/Song, Ermon - Improved Techniques for Training Score-Based Generative Models.pdf`
**Last updated**: 2026-11-17

---

## Related pages
- [[Score matching]] · [[Langevin dynamics]] · [[Diffusion models]] · [[Score SDE (Song 2021)]] · [[DDPM (Ho 2020)]]
