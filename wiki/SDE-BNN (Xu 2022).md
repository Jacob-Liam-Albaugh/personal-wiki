---
type: paper
area: bayesian
areas: [bayesian, stochastic]
source-ref: "Xu, Chen, Li, Duvenaud 2022 (AISTATS), eqs. 3-12"
tags: [bayesian, vi, ml]
authors: ["[[Winnie Xu]]", "[[Ricky T. Q. Chen]]", "[[Xuechen Li]]", "[[David Duvenaud]]"]
year: 2022
venue: "AISTATS 2022 (PMLR 151); arXiv:2102.06559v4"
file: "papers/Bayesian/Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns.pdf"
---

# Infinitely Deep BNNs with SDEs (Xu 2022)

**Summary**: The paper treats the weights of a continuous-depth residual network as a stochastic process with an Ornstein-Uhlenbeck prior and learns an implicit, non-Gaussian, non-factorised approximate posterior over weight paths, itself an SDE with a neural-network drift. Training maximises a path-space [[ELBO]] with a "sticking the landing" low-variance gradient estimator. On MNIST and CIFAR-10 it beats mean-field baselines on calibration and is competitive with discrete-depth BNNs.

**Authors**: Winnie Xu, Ricky T.Q. Chen, Xuechen Li, David Duvenaud (the filename lists Chen first; the paper's own order is Xu first) · **Year**: 2022 · **File**: `papers/Bayesian/Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns.pdf`

---

## Problem

Continuous-depth models (neural ODEs) trade compute for precision via adaptive solvers and train with constant memory via the adjoint method (p. 1). Bayesian treatment of the weights gives model averaging and better calibration, especially out of distribution (p. 1). The simplest combination, a "Bayesian neural ODE" that integrates out the finitely many ODE parameters, relies on Gaussian approximate posteriors that the authors report fit neural ODEs poorly, and it does not exploit the synergy between continuous-time models and variational inference (pp. 1-2).

The goal is [[Variational inference]] in the limit of infinitely many residual layers, each with its own unknown weights, with a posterior that can be made arbitrarily expressive (p. 2).

## Method

**Continuous-depth residual net with time-varying weights.** The discrete residual layer $h_{t+\epsilon}=h_t+\epsilon f(h_t,w_t)$ becomes, with $\epsilon=1/T$, $T\to\infty$, an ODE; a hypernetwork $f_w$ gives the weights' evolution with a finite number of parameters (p. 4, eq. 7-8). Time-varying weights act like state augmentation.

> [!definition] Latent SDE and path-space KL
> Prior and approximate posterior share the diffusion $g_\theta$:
> $$dw_t = f_\theta(w_t,t)\,dt + g_\theta(w_t,t)\,dB_t \quad(\text{prior}),\qquad
> dw_t = f_\phi(w_t,t)\,dt + g_\theta(w_t,t)\,dB_t \quad(\text{posterior}).$$
> The KL between the induced path measures is
> $$D_{KL}(\mu_q\|\mu_p)=\mathbb{E}_{q_\phi(w)}\!\int_0^1 \tfrac12\|u(t,\phi)\|_2^2\,dt,\qquad
> u(t,\phi)=g_\theta(w_t,t)^{-1}\big[f_\theta(w_t,t)-f_\phi(w_t,t)\big].$$
> (source: `papers/Bayesian/Chen, Xu, Li, Duvenaud ...pdf`, eqs. 3-6, p. 3)

The shared diffusion is required for the KL to be finite. The authors cite Boue and Dupuis (1998) for a one-to-one correspondence between path measures and drifts, and Tzen-Raginsky for the Girsanov form showing the ELBO is tight at the optimal drift. So any path measure near the true posterior can be reached by a suitably expressive drift network (p. 3).

> [!definition] OU prior on weights
> $f_p(w_t,t)=-w_t$, $g(w_t,t)=\sigma I_d$ (source: eq. 9, p. 4). Chosen over the white-noise limit of an i.i.d. Gaussian prior (hard to initialise at finite variance) for simplicity and bounded marginal variance at large $t$.

> [!definition] Posterior drift
> $f_q(w_t,t,\phi)=\mathrm{NN}_\phi(w_t,t)-f_p(w_t,t)$ (eq. 10, p. 4). Subtracting the prior drift makes posterior = prior when the last layer outputs zero, a stable initialisation (p. 6).

> [!definition] Augmented weight-and-state SDE
> $$d\begin{pmatrix}w_t\\h_t\end{pmatrix}=\begin{pmatrix}f_w(w_t,t,\phi)\\ f_h(h_t,t,w_t)\end{pmatrix}dt+\begin{pmatrix}g_w(w_t,t)\\0\end{pmatrix}dB_t,\quad h_0=x$$
> Sampled weights, hidden activations and the objective come out of one adaptive SDE-solver call; the learned parameters are the initial weights $w_0$ and $\phi$ (source: eq. 11, p. 4). Only $w$ receives noise, so hidden-state samples are smooth in depth (p. 6).

The output likelihood is $p(y|h_1)$, evaluated on the final state (p. 4).

> [!definition] Infinite-dimensional ELBO
> $$\mathcal{L}_{ELBO\infty}(\phi)=\mathbb{E}_{q_\phi(w)}\Big[\log p(D|w)-\int_0^1\tfrac12\|u(w_t,t,\phi)\|_2^2\,dt\Big]$$
> (source: p. 4, unnumbered). Gradients via [[Reparameterization trick]] through the solver, or the stochastic adjoint of Li et al. (2020).

> [!algorithm] Continuous-time sticking-the-landing (STL) estimator
> Following Roeder et al. (2017), the fully Monte Carlo KL estimator includes a martingale term of zero mean:
> $$\widehat{KL}_{STL}=\int_0^1\tfrac12\|u(w_t,t,\phi)\|_2^2\,dt+\int_0^1 u(w_t,t,\perp(\phi))\,dB_t$$
> with $\perp(\cdot)$ the stop-gradient. Earlier work (Li 2020; Tzen-Raginsky) dropped the second term; the authors keep it with stopped gradient on $\phi$. The Euler-discretised derivation (App. A.1-A.2) takes per-step Gaussian KLs, applies the discrete STL trick, and sends the step to zero.
> (source: eq. 12, p. 5; derivation eqs. 13-20, pp. 12-13)

The authors conjecture the gradient variance vanishes as $q$ approaches the true posterior (heuristic derivation only, p. 5, App. A.2). They state this "approaches zero variance" claim in the abstract; it is a heuristic argument, not a proved theorem.

**Architecture (image classification)**: $f_h$ is a convolutional net (strided conv down, transposed conv up); $w$ are the conv filters and biases; $f_w$ is an MLP with hidden widths 2, 128, 2, a narrow bottleneck chosen so variational parameters scale linearly in $\dim w$ (p. 6). CIFAR-10 uses stacked multi-scale blocks with invertible downsampling (Dinh et al.). Fixed-step solvers were used for final evaluation because adaptive-solver error estimation was costly (p. 5).

## Results

- **Gradient variance** (1D regression, matching an exponentiated Brownian motion): STL reduces variance by roughly a factor of 4 versus the other estimators (Fig. 4, p. 5).
- **Adjoint vs backprop through solver**: similar optimisation dynamics (Fig. 5, p. 5). On MNIST, 162.58 s/epoch (backprop) vs 135.90 s/epoch (adjoint) (App. C.8, p. 18).
- **1D regression**: with 2 augmented zero dimensions the SDE-BNN learns non-monotonic functions and a flexible posterior (Fig. 2, p. 6). Without augmentation every sample is monotone (p. 6).
- **Classification** (Table 1, p. 6; mean +- std):

| Model | MNIST acc % | MNIST ECE x1e-2 | CIFAR-10 acc % | CIFAR-10 ECE x1e-2 |
|---|---|---|---|---|
| ResNet32 | 99.46 | 2.88 | 87.35 | 8.47 |
| ODEnet | 98.90 | 1.11 | 88.30 | 8.71 |
| MFVI ResNet32 | 99.44 | 2.76 | 86.97 | 3.04 |
| MFVI ODEnet | 98.81 | 2.63 | 81.59 | 3.62 |
| MFVI HyperODEnet | 98.77 | 2.82 | 80.62 | 4.29 |
| HMC (Izmailov 2021, one seed) | 98.31 | 1.79 | 90.70 | 5.94 |
| Deep ensemble (Izmailov 2021) | n/a | n/a | 89.22 | 2.79 |
| SDE BNN | 99.30 | 0.63 | 89.84 | 7.19 |
| SDE BNN (+STL) | 99.10 | 0.78 | 89.10 | 7.97 |

  The SDE-BNN has the best MNIST ECE and a CIFAR-10 accuracy above ResNet32 and MFVI variants, but its CIFAR-10 ECE (7.19) is worse than MFVI ResNet32 (3.04) and the deep ensemble (2.79). The paper's claim of "lower ECE" holds against the ResNet and ODEnet, not against mean-field ResNet on CIFAR-10. Izmailov et al. numbers use a modified ResNet and one seed.
- **Priors on $w_0$** (Table 3, p. 15): inferring $w_0$ with a Gaussian prior gives CIFAR-10 accuracy 88.04 % and ECE 6.56 versus 88.08 % and 7.53 for the default SDE-BNN, both at epoch 300: slightly lower accuracy for better calibration.
- **STL in training** (Table 4, p. 16): on CIFAR-10, accuracy 95.91 -> 96.89 %, NLL 1.17e-4 -> 0.309e-4, ELBO 1.40 -> 1.183. In Table 1, STL variants have slightly lower accuracy and worse ECE than plain SDE-BNN.
- **Speed-precision trade-off**: changing solver tolerance at test time trades inference time against NLL and ECE (Fig. 6a); calibration is insensitive to tolerance near the training value (Figs. 11-12, App. C.7).
- **CIFAR10-C** (19 corruptions, 5 severities): SDE-BNN has lower error and better calibration than ResNet and MF ResNet; about 4.4 % lower absolute corruption error (p. 7, Fig. 7, Fig. 9).

## Limitations

As stated by the authors (p. 8):
- Cost is $O(DT)$ ($D$ weights, $T$ solver steps), versus $O(D^3)$ for full-covariance Gaussians, but the number of steps is hard to characterise and hard to control at training time, so training is relatively slow.
- No batch norm: normalisation breaks the Lipschitz condition needed for unique SDE solutions and couples samples within a batch.
- The STL variance claim is heuristic (App. A.2); STL did not improve Table 1 numbers.
- A 1D SDE-BNN is monotone in the input unless the state is augmented (p. 6).

Wiki note: none of the baselines include a function-space or [[SVGD]] posterior, and the comparison against HMC and deep ensembles is taken from another paper with a different architecture.

## Connections

- Instance of [[Bayesian neural networks]] with [[Variational inference]]; the KL on path space is a special case of [[KL divergence]] between measures. The "implicit posterior as a neural SDE" idea parallels [[Normalizing flows]] posteriors (Krueger 2018; Louizos-Welling 2017).
- Weight-space prior choice (OU process, bounded variance) is a design instance of the issues in [[Priors in Bayesian deep learning (Fortuin 2022)]]; weight-process priors are not covered in that review.
- Uses [[SGLD]]-adjacent machinery only indirectly: the paper lists MCMC for BNNs (Neal; Wenzel; Izmailov) as the sampling-based alternative in its Table 5 comparison of Bayesian methods.
- Compared with [[Bayesian DenseED surrogate (Zhu 2018)]]: Zhu uses a particle-based posterior over a fixed-architecture CNN; this paper puts a stochastic process on the weights over depth. Wiki note: neither is a function-space prior.
- Related background in the wiki: [[Bayesian model averaging]], [[Langevin dynamics]] (OU process is the simplest Langevin diffusion; Wiki note).

**Sources**: `papers/Bayesian/Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns.pdf`. A Finder alias to the same paper sits at `papers/Stochastic Methods/Chen, Xu, Li, Duvenaud - inf Deep Bayseian NN with Stochastic Diff. Eqns` (not a separate source).
**Last updated**: 2026-11-06

---

## Related pages
- [[Variational inference]]
- [[ELBO]]
- [[Reparameterization trick]]
- [[KL divergence]]
- [[Bayesian neural networks]]
- [[Normalizing flows]]
- neural sde
- sticking the landing estimator
- ornstein uhlenbeck process
- [[Priors in Bayesian deep learning (Fortuin 2022)]]
- [[Bayesian DenseED surrogate (Zhu 2018)]]
- [[Bayesian model averaging]]
- [[Langevin dynamics]]
