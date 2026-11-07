---
type: paper
area: physics-informed
areas: [physics-informed, pde, software]
source-ref: "Wang, Sankaran, Wang, Perdikaris, arXiv:2308.08468 (16 Aug 2023)"
tags: [physics-informed, pde, optimization, software]
authors: ["[[Sifan Wang]]", "[[Shyam Sankaran]]", "[[Hanwen Wang]]", "[[Paris Perdikaris]]"]
year: 2023
venue: "arXiv:2308.08468"
file: "papers/Physics Informed Architectures/Wang, Sankaran, Perdikaris - An Expert's Guide to Training PINNs.pdf"
---

# An expert's guide to training PINNs (Wang 2023)

**Summary**: A recipe for training [[PINN]]s that bundles recent fixes into one pipeline: non-dimensionalize, use a Fourier-feature MLP with random weight factorization, balance loss terms adaptively, and train causally with curriculum. Ablations on seven benchmarks and a JAX library give a stronger baseline than the original [[PINNs (Raissi 2019)]] formulation (source: expert.pdf, abstract and §1, pp. 1-2).

**Authors**: Sifan Wang, Shyam Sankaran, Hanwen Wang, Paris Perdikaris · **Year**: 2023 (the file name lists only three authors)

---

## The pipeline (Algorithm 1, p. 4; Fig. 1)

1. Non-dimensionalize the PDE.
2. Represent the solution by an MLP with Fourier feature embedding and random weight factorization; tanh activation, Glorot init.
3. Weighted loss $L=\lambda_{ic}L_{ic}+\lambda_{bc}L_{bc}+\lambda_rL_r$, with the residual loss split into $M$ time segments.
4. Initialize weights; each step update temporal weights (causal) and global weights (gradient or NTK balancing), then take a gradient step.

Recommended defaults: update frequency $f=1000$ steps, moving-average $\alpha=0.9$, $\gamma=1$, $\epsilon=1$; weights are frozen against back-propagation (p. 4).

## Components

**Non-dimensionalization (§3, pp. 4-5).** Rescale inputs and outputs to order one so standard initializations (Glorot) behave, variables do not dominate each other, and steps are balanced. It is "not a silver bullet": residual scales can still differ from solution scales (p. 5).

**Architecture (§4).**
- MLP width 128-512, depth 3-6, tanh; ReLU is unsuitable because its second derivative is zero (p. 5). Sin and GeLU are alternatives.
- *Random Fourier features* (Tancik et al.) fight [[Spectral bias]]:
$$\gamma(x)=\big[\cos(Bx),\ \sin(Bx)\big],\quad B_{ij}\sim N(0,\sigma^2).$$
The scale $\sigma$ sets the NTK bandwidth: low gives blurry fits, high gives salt-and-pepper artifacts. Suggested $\sigma\in[1,10]$ (p. 6). See [[Fourier features]].
- *Random weight factorization* (RWF): write each neuron's weight row as $w^{(k,l)}=s^{(k,l)}\,v^{(k,l)}$, i.e.
$$W=\mathrm{diag}(\exp(s))\,V,\quad s\sim N(\mu,\sigma I).$$
Train $s$ and $V$ directly; recommended $\mu=1.0$ (or 0.5) and $\sigma=0.1$ (p. 6, Algorithm 2). Motivated by Weight Normalization. See [[Weight initialization]].
- *Modified MLP*: two input encoders $U,V$ gated into each layer (§6.4, p. 9).

**Causal training (§5.1, p. 7).** Split time into $M$ segments, weight segment $i$ by
$$w_i=\exp\Big(-\epsilon\sum_{k<i}L_r^k\Big).$$
Choose a moderately large $\epsilon$ so all $w_i$ reach 1 by the end; reduce it if not. Details in [[Respecting causality (Wang 2022)]].

**Loss balancing (§5.2, pp. 7-8).** Two schemes, each followed by a moving average $\lambda_{new}=\alpha\lambda_{old}+(1-\alpha)\hat\lambda$:
- *Gradient-norm balancing*: set
$$\hat\lambda_{k}=\frac{\|\nabla L_{ic}\|+\|\nabla L_{bc}\|+\|\nabla L_r\|}{\|\nabla L_{k}\|}$$
so every weighted loss has equal gradient norm.
- *NTK balancing*: same form with $\mathrm{Tr}(K_k)$ in place of gradient norms, computed from diagonal entries only ([[When and why PINNs fail (Wang 2022)]], [[Neural tangent kernel]]).
The authors found similar performance, but the gradient scheme is cheaper and they recommend it first; NTK weights were smoother (p. 8).

**Curriculum (§5.3, pp. 8-9).** For time-dependent PDEs, train window by window, each initialized from the previous window's final prediction; causal weighting still helps inside a window. For singular perturbation (high Reynolds number), start at a less singular problem and increase it (Krishnapriyan et al. idea).

## Practical settings (§6)

- Adam, initial lr $10^{-3}$ with exponential decay; no weight decay for forward problems (p. 9). See [[Adam]].
- Random sampling of collocation points each step, not full batch: regularizes and avoids overfitting the residual (p. 9).
- Hard-constrained periodic BCs by Fourier embedding $v(x)=(\cos\omega x,\sin\omega x)$, extended to 2D and to a trainable time period $P_t$ (p. 9).
- Other BC types can be imposed by modifying outputs (refs. 65, 66).

## Benchmarks (§7, Table 1, p. 11)

Best relative $L^2$ error with the pipeline:

| Benchmark | Error |
|---|---|
| Allen-Cahn | $5.37\times10^{-5}$ |
| Advection | $6.88\times10^{-4}$ |
| Stokes flow | $8.04\times10^{-5}$ |
| Kuramoto-Sivashinsky (chaotic) | $1.61\times10^{-1}$ |
| Lid-driven cavity, Re=3200 | $1.58\times10^{-1}$ |
| Navier-Stokes in a torus | $2.45\times10^{-1}$ |
| Navier-Stokes around a cylinder | not reported (no reference error) |

Ablations disable one component at a time with 4 layers x 256 tanh, Adam, lr $10^{-3}$ (p. 10). Examples: Allen-Cahn full algorithm $5.84\times10^{-4}$ in the ablation, and removing Fourier features is the worst case, $4.35\times10^{-1}$. Lid-driven cavity trained directly at high $Re$ is unstable, and PINNs struggle above $Re=1000$; a ladder $Re=[100,400,1000,3200]$ fixes training (§7.5). Wiki note: the large errors on chaotic KS, cavity and torus flows show the pipeline is a baseline, not a solution; see [[Navier-Stokes equations]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Cardiac activation PINN (Sahli Costabal 2020)]], [[Cardiovascular flow PINNs (Kissas 2020)]], [[Fourier features (Tancik 2020)]], [[Glorot init (Glorot 2010)]], [[Hidden fluid mechanics (Raissi 2020)]], [[NTK (Jacot 2018)]], [[PINNs (Raissi 2019)]], [[Respecting causality (Wang 2022)]], [[SIREN paper (Sitzmann 2020)]], [[Spectral bias (Rahaman 2019)]], [[When and why PINNs fail (Wang 2022)]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Wang, Sankaran, Perdikaris - An Expert's Guide to Training PINNs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[PINN]] · [[PINNs (Raissi 2019)]] · [[Respecting causality (Wang 2022)]] · [[When and why PINNs fail (Wang 2022)]]
- [[Physics-informed machine learning]] · [[Fourier features]] · [[Spectral bias]] · [[SIREN]] · [[Automatic differentiation]]
