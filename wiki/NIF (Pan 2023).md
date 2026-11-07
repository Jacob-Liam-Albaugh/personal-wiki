---
type: paper
area: physics-informed
areas: [physics-informed, operators, ml]
source-ref: "Pan, Brunton, Kutz 2023, JMLR 24, eqs. 1-8"
tags: [physics-informed, operators, ml, pde]
authors: ["[[Shaowu Pan]]", "[[Steven L. Brunton]]", "[[J. Nathan Kutz]]"]
year: 2023
venue: "JMLR 24 (arXiv 2204.03216)"
file: "papers/Physics Informed Architectures/Brunton, Pan, Kutz - NIF - Neural Implicit Flow.pdf"
---

# Neural Implicit Flow: a mesh-agnostic dimensionality reduction paradigm (Pan 2023)

**Summary**: A hypernetwork that represents a parametric spatio-temporal field as one small MLP in space (ShapeNet) whose weights are produced by a second MLP of time, parameters or sensor readings (ParameterNet). The bottleneck of ParameterNet is the latent code. Because only point samples $(x,u)$ are needed, it works on adaptive, moving or unstructured meshes where SVD and convolutional autoencoders need projection to a fixed grid. See [[Neural implicit flow]].

**Authors**: Shaowu Pan, Steven L. Brunton, J. Nathan Kutz · **Year**: 2023 · **File**: `papers/Physics Informed Architectures/Brunton, Pan, Kutz - NIF - Neural Implicit Flow.pdf`

---

## Problem

Dimensionality reduction of PDE data by [[Singular value decomposition]] or convolutional autoencoders (CAE) assumes a fixed uniform grid. Data from adaptive mesh refinement (AMR), overset or moving meshes must be projected onto a static fine mesh, which adds projection error and, for CNNs in 3D, cubic memory (typically $64^3$ at most) (source: NIF.pdf, §1, p. 3). Coordinate-MLP methods such as [[PINN]] are mesh-agnostic but put everything in one network.

## Method

> [!algorithm] NIF (§2, eqs. 1-4, Fig. 1)
> **ShapeNet** is an $L$-layer MLP of the spatial coordinate only,
> $$u_{\mathrm{MLP}}(x;W,B)=W_L\eta_L+b_L,\quad \eta_l=\sigma(W_l\eta_{l-1}+b_l),\ \eta_0=x.$$
> **ParameterNet** $f_{\mathrm{MLP}}$ maps $(t,\mu)$ (or sensor data) to all weights and biases of ShapeNet:
> $$\big[\mathrm{vec}(W_1),\dots,b_L\big]=f_{\mathrm{MLP}}(t,\mu;\Theta).$$
> A linear bottleneck of width $r$ before the output gives the latent code $\zeta\in\mathbb R^r$. Training is plain least squares over scattered samples:
> $$\min_\Theta\ \tfrac1M\sum_i\big(u_{\mathrm{MLP}}(x_i;W(t_i,\mu_i;\Theta),B(\cdot))-u(x_i,t_i,\mu_i)\big)^2.$$
>
> (source: eqs. 1-4, pp. 5-9)

Design choices:
- **Hypernetwork view** (Ha et al. 2016): spatial complexity is decoupled from temporal and parametric complexity (p. 6).
- **[[DeepONet]] as special case**: DeepONet is NIF with only the last linear layer of ShapeNet set by the trunk net (p. 6, Fig. 2). A 51-parameter NIF is compared against a 3003-parameter DeepONet on a modulated traveling sine wave.
- **ShapeNet activation**: [[SIREN]] with ResNet-like skips ($\sin(\omega_0\cdot)$, $\omega_0=30$) to counter [[Spectral bias]]; the authors found SIREN less sensitive to hyperparameters than [[Fourier features]] (p. 9).
- **Linear variant** (eq. 6, §2.3): ParameterNet sets only the last layer, giving $u\approx\sum_{i=1}^r a_i(t)\,\varphi_i(x)$, an SVD/POD-like decomposition valid on any mesh. Normalizing $\varphi_i$ gives a latent series $\zeta(t)$ usable with [[Dynamic mode decomposition]] (pp. 11-13).
- **Sparse reconstruction** (§2.4): sensor readings (placed by POD-QDEIM, QR pivoting) feed ParameterNet in place of $t$; compare [[Proper orthogonal decomposition]].
- **Initialization**: small weights help (p. 16, footnote 8); Jacobian and approximate Hessian regularization smooth the encoder in the R-T case (p. 18).

## Results

- **Parametric Kuramoto-Sivashinsky** (§3.1, Table 1): 20 training values of $\mu\in[0.2,0.28]$. NIF (Swish) test RMSE 0.64 vs 1.10 for an MLP of similar size; NIF with half the data matches the MLP's error; abstract/intro quote about 40% better RMSE.
- **Rayleigh-Taylor on AMR, $r=1$** (§3.2, Fig. 10): lower error than SVD and CAE (error reduction from 50% up to a factor of 10 depending on rank and comparison).
- **3D homogeneous isotropic turbulence, $128^3\times20$ snapshots** (§3.3): $r=3$, 1,297,365 trainable parameters, about 3% of the data size; PDFs and Q-criterion contours well preserved.
- **Spatial query efficiency** (§3.4, Table 2, Fig. 14): versus a single SIREN with $(t,x,y,z)$ input, 27% less width, 30% less CPU time and 26%/27% less memory (forward/backward) at equal error. On a 2D turbulence slice NIF has normalized error 0.071 / 0.022 / 0.0131 at widths 36 / 75 / 150, against SIREN 0.121 / 0.040 / 0.0116 (so SIREN is slightly better at width 150).
- **Cylinder wake with AMR** (§3.5): rank-10 linear NIF then DMD gives mode shapes agreeing qualitatively with prior studies.
- **Sea surface temperature sparse sensing** (§3.6): best test space-time MSE 0.46 with 600 sensors vs 0.71 for POD-QDEIM at its best (5 sensors), 34% smaller; NIF overtakes POD-QDEIM beyond about 200 sensors.

## Limitations (§4.1, p. 27)

Network sizes must be chosen by hand and grow with spatial complexity; training is slow compared with SVD/CAE; the very wide last ParameterNet layer is costly. Does not by itself learn a solution operator, which the authors say is the aim of [[DeepONet]] and the [[Neural operator]] family. Wiki note: no physics residual is used in these experiments, so this is data-driven compression, not a PINN.

## Connections

- Compared with [[Graph neural network]] mesh methods: online cost scales with graph size there, not here.
- A neural-field form of reduced-order modelling; see [[Surrogate model]] and [[Physics-informed machine learning]].

%% refs:start %%
**Cites in this wiki**: [[AlexNet (Krizhevsky 2012)]], [[Bayesian DenseED surrogate (Zhu 2018)]], [[Deep Koopman (Lusch 2018)]], [[DeepONet (Lu 2021)]], [[FNO (Li 2021)]], [[Fourier features (Tancik 2020)]], [[Hidden fluid mechanics (Raissi 2020)]], [[Neural operator (Kovachki 2022)]], [[Physics-informed ML review (Karniadakis 2021)]], [[SINDy autoencoders (Champion 2019)]], [[Spectral bias (Rahaman 2019)]], [[Universal approximation (Hornik 1989)]]
%% refs:end %%

**Sources**: `papers/Physics Informed Architectures/Brunton, Pan, Kutz - NIF - Neural Implicit Flow.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Neural implicit flow]] · [[DeepONet]] · [[Neural operator]] · [[Operator learning]] · [[PINN]]
- [[SIREN]] · [[Spectral bias]] · [[Fourier features]] · [[Singular value decomposition]] · [[Dynamic mode decomposition]] · [[Surrogate model]]
