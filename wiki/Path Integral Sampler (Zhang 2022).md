---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Zhang & Chen 2022, eqs. 1-19, Thms. 1-4, Algs. 1-2, Tables 1-3, App. G"
tags: [sampling, diffusion, generative]
authors: ["[[Qinsheng Zhang]]", "[[Yongxin Chen]]"]
year: 2022
venue: "ICLR 2022"
file: "[[papers/Stochastic Methods/Zhang, Chen - Path Integral Sampler A Stochastic Control Approach for Sampling.pdf]]"
---

# Path Integral Sampler: A Stochastic Control Approach for Sampling (Zhang 2022)

**Authors**: Qinsheng Zhang, Yongxin Chen · **Year**: 2022 · **File**: [[papers/Stochastic Methods/Zhang, Chen - Path Integral Sampler A Stochastic Control Approach for Sampling.pdf]] · **Code**: https://github.com/qsh-zh/pis

## Summary
PIS samples from an unnormalised density $\hat\mu=Z\mu$ by learning the drift of an SDE that starts at a single point and ends, at a finite time $T$, with law $\mu$. The drift is the optimal control of a stochastic control problem whose cost is a KL divergence between path measures. Training uses only the energy, with no data. Because the path measure of the learned SDE is known through Girsanov, every sample gets an importance weight. The weights correct a suboptimal control and give an unbiased estimate of $Z$. It is an early simulation-based neural sampler; [[iDEM (Akhound-Sadegh 2024)]] uses it as a baseline.

## Problem
MCMC ([[Hamiltonian Monte Carlo|HMC]], [[NUTS]]) mixes slowly between modes. [[Variational inference|VI]] with [[Normalizing flows]] needs an invertible architecture and is limited by its expressiveness. The paper asks for a sampler that reaches $\mu$ in finite time, with a free-form network, and that can report its own error.

## Method

The KL between terminal laws is bounded by the KL between path measures (eq. 1, p. 3):
```
KL(µ_Q ‖ µ) ≤ KL(Q ‖ P)
```

> [!definition] Control problem (eqs. 2-3, p. 3)
> Controlled SDE and cost:
> ```
> dx = u(t,x) dt + dw,  x0 ~ ν
> J(u) = E[ ∫0^T ½‖u‖² dt
>          + Ψ(x_T) ]
> ```
> The value function solves an HJB equation (eq. 4). The optimal control is `u* = −∇V` (eq. 5).

The log transform `V = −log φ` makes the HJB linear (eq. 6). Feynman-Kac then gives (eqs. 7-8, p. 4):
```
φ_t(x) = E_Q0[ exp(−Ψ(x_T))
               | x_t = x ]
u*(t,x) = ∇ log φ_t(x)
```
$Q_0$ is the uncontrolled process (`dx = dw`). So $u^*$ can in principle be estimated from uncontrolled paths. This is path integral control (Kappen; Theodorou).

> [!theorem] Theorem 1 (p. 4; after Tzen & Raginsky 2019)
> Let $\nu=\delta_0$ and `Ψ = log(µ0/µ)`, where µ0 is the law of $x_T$ under $Q_0$. Then the optimal path measure is
> ```
> Q*(τ) = Q0(τ | x_T) µ(x_T)
> ```
> so `Q*(x_T) = µ`. $Q^*$ is the Schrödinger bridge from $\delta_0$ to $\mu$ with reference $Q_0$.

Girsanov gives the density of the controlled paths (eqs. 11-12):
```
dQu/dQ0 = exp( ∫ ½‖u‖² dt
               + ∫ u'dw )
KL(Qu ‖ Q0) = E ∫ ½‖u‖² dt
```
So the training loss (eqs. 13-14) is
```
L(u) = E_Qu[ ∫ ½‖u‖² dt
             + log µ0(x_T)/µ(x_T) ]
```
It equals `KL(Qu‖Q*)` up to `log Z`. This is a reverse KL, so it is mode-seeking (see [[KL divergence#Failure modes]]).

> [!algorithm] Training (Alg. 1, p. 5)
> 1. Augment the state with `y = ∫ ½‖u‖² dt`.
> 2. Simulate a batch of paths of the controlled SDE with a neural SDE solver (torchsde, stochastic adjoint).
> 3. Take a gradient step on `y_T + log µ0(x_T) − log µ̂(x_T)`.
>
> No samples of µ are needed; only $\log\hat\mu$ (and, for PIS-Grad, its gradient).

> [!definition] PIS-Grad policy (eq. 15, p. 5)
> ```
> u(t,x) = NN1(t,x)
>        + NN2(t) · ∇ log µ̂(x)
> ```
> A "modulated Langevin" drift. Unlike [[Langevin dynamics]] it reaches µ at finite $T$. PIS-NN uses `NN1` alone.

> [!theorem] Theorem 2 (informal, p. 6)
> If `‖u* − u‖² ≤ d ε` everywhere, then with step $\Delta t$ the sample law satisfies
> ```
> W2(µ_u, µ)
>   = O( √(T d (Δt + ε)) )
> ```
> See [[Wasserstein distance]].

> [!algorithm] Importance weights (eq. 17, Alg. 2, p. 6)
> Simulate with [[Euler-Maruyama method|Euler-Maruyama]] and accumulate
> ```
> y += u'Δw + ½‖u‖² Δt
> ```
> Then the weight of a path is
> ```
> w = dQ*/dQu
>   = exp( −∫ ½‖u‖² dt − ∫ u'dw
>          − Ψ(x_T) )
> ```
> Methods marked "RW" reweight samples with $w$.

> [!theorem] Theorems 3-4 (p. 6)
> - ESS (Thijssen & Kappen 2015, Cor. 7): if `max ‖u − u*‖² ≤ ε/T`, then `1/E[w²] ≥ 1 − ε`.
> - Evidence: with `Ŝ` the path cost,
> ```
> E[−Ŝ] ≤ log Z      (eq. 18)
> Z = E[ exp(−Ŝ) ]   (eq. 19)
> ```
> Equality in eq. 18 holds iff `u = u*`. Eq. 19 is unbiased for any $u$.

## Results

Baselines: [[Hamiltonian Monte Carlo|HMC]], [[NUTS]], SMC and AFT (10 linear temperatures), VI with a normalising flow. Default 100 time steps.

- Rings (Fig. 2): PIS-NN and VI-NF cover about half the inner ring, because reverse KL is zero-forcing. PIS-Grad covers more modes.

> [!example] log Z error (Table 1, p. 8)
> $A=\sqrt{B^2+S^2}$ (bias $B$, std $S$ over 100 runs). Lower is better.
>
> | Method | MG d=2 | Funnel d=10 | LGCP d=1600 |
> |---|---|---|---|
> | PIS-NN | 1.731 | 0.098 | 92.62 |
> | PIS-Grad | 0.441 | 0.104 | 13.58 |
> | PIS_RW-NN | 1.285 | 0.02 | 60.99 |
> | PIS_RW-Grad | 0.037 | 0.012 | 2.14 |
> | AFT | 0.562 | 0.284 | 3.46 |
> | SMC | 0.466 | 0.267 | 436 |
> | NUTS / HMC | ≈1.94 | 0.874 | 1.3e3 |
> | VI-NF | 1.896 | 0.243 | 78.2 |
>
> PIS_RW-GT (true optimal control, MG only): 0.018.

- Alanine dipeptide (Table 2, p. 9): KL* 171.3 for PIS-NN vs 181.8 (SNF), 183.3 (SMC), 175.6 (VI-NF). Lower torsion-angle KLs for most angles.
- VAE latent $\log p(x)$ on MNIST (Table 3, p. 9, $A$): PIS_RW-Grad 0.92, AFT 1.96, PIS_RW-NN 2.06, VI-NF 2.42, SMC 10.79.

## Limitations
- Authors (p. 9): each target needs its own trained network (amortisation could help). Quality depends on how close $u$ is to $u^*$. Bad hyperparameters cause failures (App. G).
- App. G: small $T$ gives controls with large Lipschitz constants, NaNs and missed modes. $T=1$ is the default; $T=5$ worked better in some cases. The terminal law of the uncontrolled process, `N(0, T I)`, may be far from the target's modes. Plain Euler without the adjoint was more stable than reversible Heun. Batch norm helps. Training with a Tweedie-style target lowered the loss but did not improve samples.
- Wiki note: training back-propagates through whole simulated paths, so memory scales with the number of steps. [[iDEM (Akhound-Sadegh 2024)]] reports PIS diverging on LJ-55 and losing ESS on LJ-13.
- Wiki note: there is no annealing; the reverse-KL loss can drop modes.

## Connections
- Optimal control view of [[Diffusion models]]: the learned drift plays the role of the reverse-SDE score term, but is fit from the energy, not from data ([[Score SDE (Song 2021)]]).
- [[Langevin dynamics]] is the infinite-time special case; PIS-Grad modulates its drift to finish at $T$.
- Compared against [[Hamiltonian Monte Carlo]], [[NUTS]] and VI with [[Normalizing flows]]; the loss is a reverse [[KL divergence]] on path space, i.e. [[Variational inference]] over SDE drifts.
- Uses the [[Stochastic differential equation]] toolkit: Girsanov, Feynman-Kac, [[Euler-Maruyama method|Euler-Maruyama]].
- [[iDEM (Akhound-Sadegh 2024)]] targets the same problem without simulation in the training loss.
- [[SDE-BNN (Xu 2022)]] uses the same path-space KL via Girsanov for a different end (Bayesian neural SDEs).

%% refs:start %%
**Cites in this wiki**: [[Fourier features (Tancik 2020)]], [[NTK (Jacot 2018)]]
**Cited by in this wiki**: [[iDEM (Akhound-Sadegh 2024)]]
**Software cited**: [[software#PyTorch|PyTorch]]
%% refs:end %%

**Sources**: `papers/Stochastic Methods/Zhang, Chen - Path Integral Sampler A Stochastic Control Approach for Sampling.pdf`
**Last updated**: 2026-11-17

---

## Related pages
- [[iDEM (Akhound-Sadegh 2024)]] · [[Langevin dynamics]] · [[Diffusion models]] · [[Stochastic differential equation]] · [[KL divergence]] · [[Normalizing flows]]
