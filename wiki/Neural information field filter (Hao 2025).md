---
type: paper
area: ift
areas: [ift, bayesian, inverse-problems, physics-informed, sampling]
source-ref: "Hao, Bilionis 2025, Mech. Syst. Signal Process. 226, 112253"
tags: [ift, vi, sampling, mcmc, bayesian, inverse-problems, physics-informed, uq]
authors: ["[[Kairui Hao]]", "[[Ilias Bilionis]]"]
year: 2025
venue: "Mechanical Systems and Signal Processing 226, 112253"
file: "[[papers/IFT/Hao, Bilionis - Neural information field filter.pdf]]"
---

# Neural information field filter (Hao 2025)

**Summary**: Removes the linear-basis restriction of [[IFT state and parameter estimation (Hao 2024)]]. Instead of solving one basis coefficient for the initial state, the prior couples the path's start $\hat x(0;w)$ to an auxiliary initial state $x_0$ through a kernel; a Gaussian kernel gives a "relaxed" prior that works for any parameterization, including a Fourier-encoded residual network. Inference is either nested stochastic VI (NSVI) or nested RMSprop-preconditioned SGLD (NPSGLD). Tested on Duffing, a two-DOF nonlinear oscillator, a 20-story Bouc–Wen frame (4660 unknowns) and experimental nonlinear-energy-sink data (16 000 unknowns).

**Authors**: Kairui Hao, Ilias Bilionis · **Year**: 2025 · **File**: [[papers/IFT/Hao, Bilionis - Neural information field filter.pdf]] · **Code**: promised on acceptance (none linked)

---

## Problem (Sec. 1)
- The JCP method reparameterizes the path by $x_0$ (solve $w_i$ from the others), which is easy for a linear basis and awkward for a neural network.
- Designing a good linear basis by hand is hard for complex responses.

## Method

> [!definition] Generalized physics-informed conditional prior (Def. 1)
> ```
> p(w | x0, θ) =
>   e^{−βH(w,θ) − H_K(x̂(0;w), x0)}
>   / Z(x0, θ)
> ```
> with kernel Hamiltonian $H_K=-\log K$. Marginalizing $x_0$ convolves the prior with the kernel.

- **Prop. 1**: a Dirac kernel recovers the JCP reparameterized prior (App. A).
- **Relaxed prior** (eq. 5), Gaussian kernel:
```
p(w | x0, θ) ∝ exp(
  − β1 H(w, θ)
  − β2 ‖x̂(0;w) − x0‖² )
```
  Remark 1 reads this as a probabilistic proximal operator. The posterior (eq. 7) integrates out $x_0$.
- **Fig. 1 / Remark 3**: DAGs for B-PINN, IFT and NIFF. $Z(x_0,\theta)$ supplies the hierarchy a B-PINN lacks and matches batch filtering $p(x_{1:n}|x_0,\theta)$.

### Fourier-encoded residual network (eq. 8)
```
enc(t) = (1, sin 2πkt/T̄,
             cos 2πkt/T̄),  k=1..K
x̂(t) = MLP(enc(t))
       + Σ_i w^b_i ψ_i(t)
```
The network corrects a linear basis; the Fourier encoding addresses [[Spectral bias]] ([[Fourier features]], a [[ResNet]]-style skip).

### Inference
> [!algorithm] NSVI (Sec. 3.1, App. C)
> Guide $q(w)q(\theta)q(x_0)$. The [[ELBO]] (eq. 9) has a minibatch likelihood scaled by $n_d/m_d$ and $-\mathbb E[\log Z(x_0,\theta)]$, whose gradient comes from an inner auxiliary SVI on the prior. **Prop. 2**: maximizing it minimizes an upper bound on $\mathrm{KL}(q(w)q(\theta)\,\|\,p(w,\theta|y))$.

> [!algorithm] NPSGLD (Sec. 3.2, App. D)
> [[SGLD]] on $(w,\theta,x_0)$ with an RMSprop diagonal preconditioner (Li et al. pSGLD, Patterson–Teh form):
> ```
> V ← αV + (1−α) g⊙g
> M = diag(1/(δ + √V))
> ```
> Keep $(w,\theta)$ (eq. 10). An inner chain on the prior estimates $\nabla\log Z$, as in [[Nested SGLD]]. $\alpha$ is annealed to 1 so the preconditioner freezes and late sampling is a fixed-metric Langevin chain.

- $\beta$ is set by hand here, not learned.
- **Guidance** (Sec. 6): NSVI is faster and suits >10k unknowns but is less accurate; NPSGLD is asymptotically exact but mixes slowly in high dimension. Below ~1000 unknowns both work and NPSGLD beats a diagonal-Gaussian NSVI.

## Results
> [!example] Duffing (Sec. 5.1)
> $(k_1,k_2,k_3)=(0.3,-1,1)$, Fourier $K=40$, $\dim w=162$. Reparameterized NSVI, relaxed NSVI ($\beta_1=200$, $\beta_2=10^5$), relaxed NSGLD (3×2e6 steps) and relaxed NPSGLD all agree. Times 8 / 7 / 77 / 90 s; NPSGLD converges much faster than plain SGLD. $p(\hat x(0)|y)$ and $p(x_0|y)$ differ slightly under NSVI, almost not under the samplers.

> [!example] Two-DOF nonlinear system (Sec. 5.2)
> Duffing spring and cubic damper, 8 parameters. RBF basis alone (20 bases) cannot reconstruct the states: parameters wrong or non-identifiable, NPSGLD multimodal. Adding the residual net ($K=10$, width 10, swish) recovers them with both methods. $\dim w$ 80 → 344; times 5/25 s → 26/195 s (NSVI/NPSGLD). NSVI anneals the partition-function term over the first 200k of 300k steps.

> [!example] 20-story Bouc–Wen frame (Sec. 5.3)
> 40 states, stiffnesses $s_1..s_{20}\sim U[8,10]$, 5 s of El Centro, 1% noise, 100 RBFs + residual; $\dim w=4660$. NPSGLD (5 chains, 200k) recovers all stiffnesses in 325 s; NSVI (50k) in 196 s with a small error in $s_2$. A 30-s prediction is accurate apart from minor errors in $z_{15}$, $z_{20}$.

> [!example] Experimental nonlinear energy sink (Sec. 5.4)
> Lund et al. data, model $m\ddot x+c_\nu\dot x+c_f\tanh(200\dot x)+kx+zx^3=-m\ddot x_g$. Two datasets stacked, 4096 Hz, 4000 RBFs per signal, NSVI only; $\dim w=16\,000$, 827 s. Estimates close to Lund's ($c_\nu=0.344$, $k=33.1$, $z=6.54\times10^5$) (the sub-modal model of [[UKF identification of a nonlinear energy sink (Lund 2020)]], not its min-MSE model); validation NMSE comparable to Lund's.

## Limitations
- The authors: NPSGLD is too slow for the 16k-unknown case (hours); $\beta$ must be chosen; the inner-loop gradient of $\log Z$ is biased for NSVI.
- Wiki note: the relaxed prior adds $\beta_2$; with an NN path the prior on states is parameterization-dependent (the Jacobian issue App. A of the JCP paper raised), which the paper does not quantify.

## Connections
- Ch. 6 of [[IFT for UQ of differential equations (Hao 2024)]] (with different Duffing settings, e.g. $K=50$).
- NPSGLD is a preconditioned [[Nested SGLD]], the sampler of [[PIFT (Alberts 2023)]]; NSVI extends the JCP algorithm.
- Same [[Physics-informed prior]] and B-PINN contrast as [[IFT state and parameter estimation (Hao 2024)]]; see [[PINN]].
- Wiki note: despite the name it is a batch smoother, not a recursive filter like the [[Kalman filter]] or [[Particle filter]].
- NES data and the UKF baseline: [[UKF identification of a nonlinear energy sink (Lund 2020)]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Fourier features (Tancik 2020)]], [[IFT state and parameter estimation (Hao 2024)]], [[PIFT (Alberts 2023)]], [[PINNs (Raissi 2019)]], [[Path-space PIFT estimation (Hao 2025)]], [[SGLD (Welling 2011)]], [[SMC² (Chopin 2013)]], [[Spectral bias (Rahaman 2019)]], [[UKF identification of a nonlinear energy sink (Lund 2020)]], [[VAE paper (Kingma 2014)]], [[When and why PINNs fail (Wang 2022)]]
**Cited by in this wiki**: [[IFT thermal conductivity (Alberts 2026)]], [[MAP uniqueness in IFT (Alberts 2025)]]
**Software cited**: [[software#JAX|JAX]], [[software#PyTorch|PyTorch]]
%% refs:end %%

**Sources**: `papers/IFT/Hao, Bilionis - Neural information field filter.pdf`.
**Last updated**: 2026-11-15

---

## Related pages
- [[Information field theory]]
- [[Physics-informed prior]]
- [[Nested SGLD]]
- [[SGLD]]
- [[Variational inference]]
- [[Fourier features]]
- [[Spectral bias]]
- [[Identifiability]]
- [[Duffing oscillator]]
