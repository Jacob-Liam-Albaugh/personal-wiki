---
type: paper
area: physics-informed
areas: [physics-informed, ml, generative]
source-ref: "Chen, Rubanova, Bettencourt, Duvenaud 2018, NeurIPS, eqs. 1-5, Thm 1"
tags: [physics-informed, ml, optimization, generative]
authors: ["[[Ricky T. Q. Chen]]", "[[Yulia Rubanova]]", "[[Jesse Bettencourt]]", "[[David Duvenaud]]"]
year: 2018
venue: "NeurIPS 2018"
file: "papers/Physics Informed Architectures/Chen, Rubanova, Bettencourt, Duvenaud - Neural ODEs.pdf"
---

# Neural Ordinary Differential Equations (Chen 2018)

**Summary**: Replaces a stack of discrete residual layers by an ODE whose right-hand side is a neural network, and evaluates the output with a black-box ODE solver. Gradients come from the adjoint sensitivity method (a second ODE solved backwards), giving constant memory in depth. Three uses: continuous-depth classifiers, continuous normalizing flows, and a latent-ODE model for irregularly sampled time series.

**Authors**: Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud · **Year**: 2018 · **File**: `papers/Physics Informed Architectures/Chen, Rubanova, Bettencourt, Duvenaud - Neural ODEs.pdf`

---

## Problem

Residual networks, RNN decoders and normalizing flows all build a transformation by composing steps $h_{t+1}=h_t+f(h_t,\theta_t)$ (eq. 1), which is an Euler discretization of a continuous transformation. Backprop through many such layers costs memory linear in depth. What happens in the limit of many small steps? (source: Neural ODEs.pdf, p. 1)

## Method

> [!definition] Neural ODE
> The hidden state obeys
> $$\frac{dh(t)}{dt}=f(h(t),t,\theta),$$
> with input $h(0)$ and output $h(T)$ obtained from an ODE solver. See [[Neural ODE]].
>
> (source: eq. 2, p. 1)

Benefits claimed: constant memory in depth, adaptive computation (the solver picks the number of function evaluations and can trade accuracy for speed after training), invertible flows with cheaper density change, and natural handling of data at arbitrary times (pp. 1-2).

### Adjoint sensitivity (§2)

For $L(z(t_1))=L(\mathrm{ODESolve}(z(t_0),f,t_0,t_1,\theta))$ define the adjoint $a(t)=\partial L/\partial z(t)$.

> [!algorithm] Reverse-mode derivative of an ODE solve
> Adjoint dynamics (eq. 4):
> $$\frac{da(t)}{dt}=-a(t)^{\top}\frac{\partial f(z(t),t,\theta)}{\partial z}$$
> Parameter gradient (eq. 5):
> $$\frac{dL}{d\theta}=-\int_{t_1}^{t_0}a(t)^{\top}\frac{\partial f(z(t),t,\theta)}{\partial\theta}\,dt$$
> Algorithm 1 integrates the augmented state $[z,\,a,\,\partial L/\partial\theta]$ backwards from $t_1$ to $t_0$ in one solver call. The vector-Jacobian products come from [[Automatic differentiation]] at roughly the cost of evaluating $f$. State $z(t)$ is recomputed backwards rather than stored.
>
> (source: eqs. 3-5, Alg. 1, pp. 2-3) Full treatment: [[Adjoint sensitivity method]].

When the loss depends on several observation times, the backward solve is split into segments and the adjoint is bumped by $\partial L/\partial z(t_i)$ at each observation (p. 3).

### Continuous normalizing flows (§4)

Discrete flows need $\log\det\partial f/\partial z$ (cubic cost). In continuous time:

> [!theorem] Instantaneous change of variables (Theorem 1)
> If $dz/dt=f(z(t),t)$ with $f$ uniformly Lipschitz in $z$ and continuous in $t$, then
> $$\frac{\partial\log p(z(t))}{\partial t}=-\operatorname{tr}\!\Big(\frac{df}{dz(t)}\Big).$$
>
> (source: eq. 8, p. 4)

Only a trace is needed, and trace is linear, so a sum of $M$ hidden units costs $O(M)$ instead of $O(M^3)$ (eq. 10). $f$ need not be bijective; uniqueness of ODE solutions makes the map invertible. Time-dependent parameters and per-unit gates $\sigma_n(t)$ give the CNF. See [[Normalizing flows]].

### Latent ODE for time series (§5)

Generative model (eqs. 11-13): $z_{t_0}\sim p(z_{t_0})$; $z_{t_1},\dots,z_{t_N}=\mathrm{ODESolve}(z_{t_0},f,\theta_f,t_0,\dots,t_N)$; $x_{t_i}\sim p(x\mid z_{t_i},\theta_x)$. Trained as a [[VAE]] with an RNN recognition network run backwards in time, outputting $q_\phi(z_0\mid x_1,\dots,x_N)$. An inhomogeneous Poisson process likelihood on observation times, $\log p=\sum_i\log\lambda(z(t_i))-\int\lambda(z(t))dt$, can be added and solved in the same solver call (p. 7).

## Results

- **MNIST** (Table 1, p. 3): test error 0.42% for ODE-Net with 0.22M parameters and $O(1)$ memory, vs ResNet 0.41% (0.60M, $O(L)$ memory), RK-Net 0.47% (0.22M), 1-layer MLP 1.60%.
- Error tolerance trades accuracy for number of function evaluations (Fig. 3). The backward pass used about half the evaluations of the forward pass; the evaluation count rose during training (p. 4).
- **Density matching** (Fig. 4): CNF reached lower loss than planar NF; CNF trained 10,000 Adam iterations vs 500,000 RMSprop for NF (p. 5). On two-moons NF had difficulty fitting (p. 6).
- **Spirals with irregular times** (Table 2, p. 8): predictive RMSE for 30/50/100 observed points: RNN 0.3937/0.3202/0.1813, latent ODE 0.1642/0.1502/0.1346.

## Limitations

Stated by authors (§6, p. 8): minibatching is less direct (states are concatenated into one big ODE, error control may need more evaluations); uniqueness needs finite weights and Lipschitz nonlinearities (Picard); the user must set solver tolerances for forward and reverse passes (1.5e-8 for sequence modeling, 1e-3 and 1e-5 sufficed for classification and density estimation); reconstructing the forward trajectory by reversing dynamics can add numerical error, fixable by checkpointing, not found a problem in practice.

Wiki note: the paper's "depth" is only the solver's evaluation count; it is input dependent and not a fixed architecture hyperparameter.

## Connections

- Direct basis for [[Neural ODE]] in physics-informed modelling: [[Hamiltonian neural network]] and [[Lagrangian neural network]] learn a scalar function whose induced ODE is integrated; [[SINDy]] fits a sparse library for the same right-hand side.
- Related paper pages: [[HNNs (Greydanus 2019)]], [[LNNs (Cranmer 2020)]], [[SINDy autoencoders (Champion 2019)]].
- Cites Raissi and Karniadakis on learning differential equations with networks (p. 9): see [[PINNs (Raissi 2019)]].

%% refs:start %%
**Cited by in this wiki**: [[DDPM (Ho 2020)]], [[DeepONet (Lu 2021)]], [[Diesel PM as OU process (Bolt 2026)]], [[HNNs (Greydanus 2019)]], [[LNNs (Cranmer 2020)]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Chen, Rubanova, Bettencourt, Duvenaud - Neural ODEs.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Neural ODE]] · [[Adjoint sensitivity method]] · [[Normalizing flows]] · [[VAE]] · [[Automatic differentiation]]
- [[Physics-informed machine learning]] · [[Hamiltonian neural network]] · [[SINDy]]
