---
type: paper
area: physics-informed
areas: [physics-informed, ml, mechanics]
source-ref: "Greydanus, Dzamba, Yosinski 2019, NeurIPS, eqs. 1-3, Table 1"
tags: [physics-informed, mechanics, ml]
authors: ["[[Sam Greydanus]]", "[[Misko Dzamba]]", "[[Jason Yosinski]]"]
year: 2019
venue: "NeurIPS 2019 (arXiv 1906.01563)"
file: "papers/Physics Informed Architectures/Greydanus, Dzamba, Yosinski - HNNs.pdf"
---

# Hamiltonian Neural Networks (Greydanus 2019)

**Summary**: Parameterize the scalar Hamiltonian $H_\theta(q,p)$ with a network and obtain the dynamics as its symplectic gradient, trained by matching time derivatives. The learned flow conserves an energy-like quantity exactly, trains as fast as a baseline MLP and drifts far less in energy over long rollouts. Tested on mass-spring, pendulum, real pendulum, two-body, and a pixel pendulum with an autoencoder.

**Authors**: Sam Greydanus, Misko Dzamba, Jason Yosinski · **Year**: 2019 · **File**: `papers/Physics Informed Architectures/Greydanus, Dzamba, Yosinski - HNNs.pdf`

---

## Problem

A plain network that predicts next states or derivatives learns only an approximate conservation law; rollouts drift to higher or lower energy (Fig. 1, p. 2). Predicting the next state also bakes in discrete time steps. The paper wants a model class that conserves an energy-like quantity by construction, learned unsupervised from data (pp. 1-2).

## Method

> [!definition] Hamilton's equations (eq. 2)
> With canonical coordinates $(q,p)$ and scalar $H(q,p)$:
> $$\frac{dq}{dt}=\frac{\partial H}{\partial p}$$
> $$\frac{dp}{dt}=-\frac{\partial H}{\partial q}$$
> The vector field $S_H=(\partial H/\partial p,\,-\partial H/\partial q)$ is the symplectic gradient. Moving along it keeps $H$ constant.
>
> (source: HNNs.pdf, eq. 2, p. 2-3)

> [!algorithm] HNN training loss (eq. 3)
> A network $H_\theta$ maps $(q,p)$ to one scalar. An in-graph gradient gives the vector field, and the loss is
> $$\mathcal L_{\mathrm{HNN}}=\Big\|\frac{\partial H_\theta}{\partial p}-\frac{\partial q}{\partial t}\Big\|^2$$
> $$\qquad+\Big\|\frac{\partial H_\theta}{\partial q}+\frac{\partial p}{\partial t}\Big\|^2.$$
> Dynamics are then integrated as $(q_1,p_1)=(q_0,p_0)+\int_{t_0}^{t_1}S(q,p)\,dt$ (eq. 1), with a Runge-Kutta solver. See [[Hamiltonian neural network]].
>
> (source: eqs. 1, 3, p. 2-3)

Targets are analytic derivatives where available, otherwise finite differences (p. 4). The baseline network maps $(q,p)$ directly to $(\dot q,\dot p)$.

**Pixel pendulum** (§5): encoder and decoder of four fully connected layers with residual connections, latent size 2, two stacked frames so velocity is observable. Loss = HNN loss + pixel reconstruction + an auxiliary term
$$\mathcal L_{CC}=\|z_p^t-(z_q^t-z_q^{t+1})\|^2$$
(eq. 7) that pushes the second half of the latent vector to act like the derivative of the first, i.e. canonical-like coordinates (pp. 6-7).

**Extra properties** (§6): alternating the symplectic gradient with the Riemann gradient $R_H=(\partial H/\partial q,\partial H/\partial p)$ adds or removes energy (counterfactual "what if we added energy"); by Liouville's theorem the flow is bijective, so trajectories are exactly time-reversible (p. 8).

## Results

Setup: three layers, 200 tanh units, Adam at $10^{-3}$, 2000 steps for the simple tasks, 10,000 for two-body (pp. 3-5). Energy metric = MSE between true and predicted total energy along a rollout.

| Task | Energy MSE baseline ($\times10^{3}$) | Energy MSE HNN |
|---|---|---|
| Ideal mass-spring | 170 ± 20 | 0.38 ± 0.1 |
| Ideal pendulum | 42 ± 10 | 25 ± 5 |
| Real pendulum | 390 ± 7 | 14 ± 5 |
| Two body | 6.3e4 ± 3e4 | 39 ± 5 |
| Pixel pendulum | 9.3 ± 1 | 0.15 ± 0.01 |

(source: Table 1, p. 7.) Train and test losses are about equal to the baseline on tasks 1, 2, 5; HNN losses are about 10x lower for two-body and higher on the real pendulum (9.2 vs 2.7 train). The HNN-conserved quantity matches total energy up to a constant offset (p. 5). Three-body (chaotic) results are preliminary and in the appendix (p. 6).

## Limitations

- Assumes a conserved quantity exists; the real pendulum has friction and the HNN still conserves, so dissipation must be modelled separately (p. 5).
- Needs canonical coordinates $(q,p)$ or an autoencoder encouraged to produce them (§5). [[Lagrangian neural network]] removes this requirement (see [[LNNs (Cranmer 2020)]]).
- Authors say the three-body results "still need improvement" (p. 6).
- Wiki note: training uses derivative targets, so noisy finite-difference estimates feed directly into the loss; the paper adds Gaussian noise of variance 0.1 but no ablation on derivative error.

## Connections

- Uses the continuous-time viewpoint of [[Neural ODEs (Chen 2018)]]; cites Neural ODEs as a step "in the right direction" (p. 2). Reversibility claim contrasts with approximately reversible nets.
- Followed by [[LNNs (Cranmer 2020)]], which compares against HNNs on a relativistic particle.
- Sits in [[Physics-informed machine learning]] as an inductive bias (conservation law built into the architecture) vs. the loss-based approach of [[PINN]].
- Cites Schmidt and Lipson 2009 (genetic search for conservation laws) as inspiration; compare [[SINDy]] for sparse equation discovery.

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Neural ODEs (Chen 2018)]]
**Cited by in this wiki**: [[DeepONet (Lu 2021)]], [[LNNs (Cranmer 2020)]], [[Symbolic models from deep learning (Cranmer 2020)]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Greydanus, Dzamba, Yosinski - HNNs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Hamiltonian neural network]] · [[Neural ODE]] · [[Lagrangian neural network]] · [[Physics-informed machine learning]]
- [[LNNs (Cranmer 2020)]] · [[Neural ODEs (Chen 2018)]] · [[PINN]]
