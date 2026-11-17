---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Akhound-Sadegh et al. 2024, eqs. 1-10, Props. 1-2, Alg. 1, Tables 1-3, pp. 1-9"
tags: [sampling, diffusion, generative]
authors: ["[[Tara Akhound-Sadegh]]", "[[Jarrid Rector-Brooks]]", "[[Avishek Joey Bose]]", "[[Sarthak Mittal]]", "[[Pablo Lemos]]", "[[Cheng-Hao Liu]]", "[[Marcin Sendera]]", "[[Siamak Ravanbakhsh]]", "[[Gauthier Gidel]]", "[[Yoshua Bengio]]", "[[Nikolay Malkin]]", "[[Alexander Tong]]"]
year: 2024
venue: "ICML 2024"
file: "[[papers/Diffusion/Akhound-Sadegh, Rector-Brooks, Bose et al - Iterated Denoising Energy Matching for Sampling from Boltzmann Densities.pdf]]"
---

# Iterated Denoising Energy Matching for Sampling from Boltzmann Densities (Akhound-Sadegh 2024)

**Authors**: Tara Akhound-Sadegh, Jarrid Rector-Brooks, Avishek Joey Bose, Sarthak Mittal, Pablo Lemos, Cheng-Hao Liu, Marcin Sendera, Siamak Ravanbakhsh, Gauthier Gidel, Yoshua Bengio, Nikolay Malkin, Alexander Tong · **Year**: 2024 · **File**: [[papers/Diffusion/Akhound-Sadegh, Rector-Brooks, Bose et al - Iterated Denoising Energy Matching for Sampling from Boltzmann Densities.pdf]] · **Code**: https://github.com/jarridrb/dem

## Summary
iDEM trains a [[Diffusion models|diffusion]] sampler for a Boltzmann density $\mu\propto e^{-E}$ with no data. It replaces the data-driven target of [[Score matching|denoising score matching]] with a Monte Carlo estimate of the noised score built from $E$ alone (DEM). Training alternates between generating samples with the current model into a replay buffer and regressing the network onto the MC score at noised buffer points. The regression is off-policy and needs no simulation or back-propagation through the sampler. On particle systems up to LJ-55 (165 dimensions) it matches or beats FAB, [[Path Integral Sampler (Zhang 2022)|PIS]] and DDS, and trains 2-4× faster than FAB.

## Problem
Sample $\mu(x)\propto\exp(-E(x))$ given $E$ and $\nabla E$, but no samples. Standard diffusion training cannot be used: (C1) the score of the noised target is unknown, and (C2) it is unclear where in space to match it. Simulation-based samplers such as PIS and DDS back-propagate through the sampler, which costs memory linear in the number of steps and can diverge on stiff energies.

## Method

Forward and reverse SDEs (eqs. 1-2):
```
dx = −α(t) x dt + g(t) dw
VE: α = 0
VP: α = g²/2
```
For VE the noised density is a Gaussian convolution of the target (eq. 3):
```
p_t = p_0 * N(0, σ_t² I)
```

> [!theorem] Noised score as an expectation (eqs. 6-7, p. 4)
> Moving the gradient onto $p_0=\mu$:
> ```
> ∇log p_t(x)
>   = E[ ∇exp(−E(x+ε)) ]
>     / E[ exp(−E(x+ε)) ]
> ε ~ N(0, σ_t² I)
> ```
> Wiki note: this is the energy-side counterpart of Tweedie's formula ([[Score matching#Tweedie's formula]]); it needs $E$ instead of samples.

> [!definition] DEM estimator (eqs. 8-9, p. 4)
> With $K$ noise draws $\varepsilon_i\sim N(0,\sigma_t^2I)$:
> ```
> S_K(x,t) = ∇_x log Σ_i
>              exp(−E(x + ε_i))
> ```
> computed with LogSumExp. Equivalently, with self-normalised weights $w_i\propto e^{-E(x+\varepsilon_i)}$:
> ```
> S_K = −Σ_i w_i ∇E(x + ε_i)
> ```

> [!theorem] Proposition 1 (p. 5)
> Under sub-Gaussian assumptions, with probability $1-\delta$
> ```
> ‖S_K − ∇log p_t‖
>   ≤ c(x) log(1/δ) / √K
> ```
> $S_K$ is biased (a ratio of MC means). The constant grows where $p_t$ is small.

DEM loss (eq. 10):
```
L = E ‖ S_K(x_t,t) − s_θ(x_t,t) ‖²
```
Its minimiser does not depend on the distribution of $x_t$, so $x_t$ can come from anywhere (off-policy).

> [!algorithm] iDEM (Alg. 1, p. 5)
> Outer loop:
> 1. Integrate the reverse SDE with the current $s_\theta$ from the prior, with no gradients.
> 2. Add the samples to a replay buffer $B$.
>
> Inner loop, repeated:
> ```
> x0 ~ B,  t ~ U(0,1)
> x_t ~ N(x0, σ_t² I)
> step on ‖S_K(x_t,t) − s_θ(x_t,t)‖²
> ```
> The buffer is likened to persistent contrastive divergence. pDEM is the ablation that fills the buffer from the prior only.

> [!theorem] Proposition 2: symmetry (p. 6)
> If $E$ is invariant under $G=SE(3)\times S_n$ and the noise is zero-centre-of-mass Gaussian, then $S_K$ is $G$-equivariant. The network $s_\theta$ is an EGNN. See [[Equivariance]].

> [!example] Cost comparison (Table 1, p. 3)
> $L$ = number of integration steps.
>
> | Method | MCMC-free | Off-policy | Time | Memory |
> |---|---|---|---|---|
> | FAB | no | yes | O(L) | O(L+d) |
> | PIS, DDS | yes | no | O(L) | O(Ld) |
> | pDEM | yes | yes | O(1) | O(d) |
> | iDEM | yes | yes | O(L) | O(d) |

## Results

Targets: 40-mode GMM (d=2), DW-4 (d=8), LJ-13 (d=39), LJ-55 (d=165). NLL is from an OT-CFM model ([[Flow matching]]) fitted to each method's samples.

> [!example] NLL / ESS / W2 (Table 2, p. 8)
> | Method | GMM | DW-4 | LJ-13 | LJ-55 |
> |---|---|---|---|---|
> | FAB | 7.14 / .653 / 12.0 | 7.16 / .947 / 2.15 | 17.52 / .101 / 4.35 | 200.32 / .063 / 18.03 |
> | PIS | 7.72 / .295 / 7.64 | 7.19 / .901 / 2.13 | 47.05 / .004 / 4.67 | diverged |
> | DDS | 7.43 / .687 / 9.31 | 11.27 / .408 / 2.15 | diverged | diverged |
> | pDEM | 7.10 / .634 / 12.20 | 7.44 / .547 / 2.11 | 18.80 / .044 / 4.21 | diverged |
> | iDEM | 6.96 / .734 / 7.42 | 7.17 / .825 / 2.13 | 17.68 / .231 / 4.26 | 125.86 / .106 / 16.13 |

> [!example] Training hours (Table 3, p. 8)
> | Method | GMM | DW-4 | LJ-13 | LJ-55 |
> |---|---|---|---|---|
> | FAB | 1.71 | 6.87 | 21.78 | 40.35 |
> | PIS | 4.11 | 11.29 | 17.36 | diverged |
> | DDS | 1.81 | 5.65 | diverged | diverged |
> | pDEM | 0.36 | 1.40 | 1.79 | diverged |
> | iDEM | 0.87 | 4.30 | 6.55 | 7.75 |

- LJ-55 has a high-Lipschitz energy. PIS and DDS diverge; pDEM failed in 2 of 3 runs.
- Ablations: the empirical bias of $S_K$ falls like $O(1/K)$, faster than the $O(1/\sqrt K)$ bound. The score error grows as $t\to1$. The buffer helps on DW-4 and is about even on LJ-13.
- The score at $t=0$ can be pinned to $\nabla\log p_0=-\nabla E$.

## Limitations
- Authors: $S_K$ is biased and has high variance at large noise. Future work is variance reduction and a cheaper outer loop.
- Wiki note: Prop. 1's constant blows up in low-density regions, which are exactly where samples start at large $t$.
- Wiki note: the appendix (pp. 10-27, incl. App. C on links to flow matching, stochastic control and RDMC) was not read for this page, and the figures were not inspected.

## Connections
- Data-free analogue of [[Score SDE (Song 2021)]] training: the VE SDE and reverse SDE are reused, only the regression target changes ([[Score matching]]).
- Baseline [[Path Integral Sampler (Zhang 2022)]] solves the same problem by stochastic control with simulation in the loss; iDEM removes that simulation.
- Compared with FAB, a [[Normalizing flows|flow]]-based Boltzmann generator with AIS (not in the wiki).
- EGNN and the $SE(3)\times S_n$ argument: [[Equivariance]].
- Evaluation by an OT-CFM model: [[Flow matching]].
- $S_K$ is self-normalised importance sampling; the same weights appear in [[Particle filter|particle filters]].

%% refs:start %%
**Cites in this wiki**: [[Neural ODEs (Chen 2018)]], [[Path Integral Sampler (Zhang 2022)]], [[Score SDE (Song 2021)]]
%% refs:end %%

**Sources**: `papers/Diffusion/Akhound-Sadegh, Rector-Brooks, Bose et al - Iterated Denoising Energy Matching for Sampling from Boltzmann Densities.pdf`
**Last updated**: 2026-11-17

---

## Related pages
- [[Path Integral Sampler (Zhang 2022)]] · [[Diffusion models]] · [[Score matching]] · [[Equivariance]] · [[Flow matching]]
