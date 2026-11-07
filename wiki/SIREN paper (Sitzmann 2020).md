---
type: paper
area: ml
areas: [ml]
source-ref: "Sitzmann et al. 2020, arXiv:2006.09661, §3-4"
tags: [ml, physics-informed, pde, signals]
authors: ["[[Vincent Sitzmann]]", "[[Julien Martel]]", "[[Alexander Bergman]]", "[[David Lindell]]", "[[Gordon Wetzstein]]"]
year: 2020
venue: "NeurIPS 2020 (arXiv:2006.09661v1)"
file: "papers/ML/Sitzmann - SIREN - Implicit Neural Representations with Periodic Activation Functions.pdf"
---

# SIREN paper (Sitzmann 2020)

**Summary**: An MLP with sine activations (a SIREN) represents signals and their derivatives far better than ReLU, tanh or positional-encoding networks. A specific initialization keeps activation statistics stable with depth. SIRENs are trained on images, video, signed distance fields and on PDE constraints (Poisson, Eikonal, Helmholtz, wave equation).

**Authors**: Vincent Sitzmann, Julien Martel, Alexander Bergman, David Lindell, Gordon Wetzstein · **Year**: 2020 · **File**: `papers/ML/Sitzmann - SIREN - Implicit Neural Representations with Periodic Activation Functions.pdf`

---

## Problem

An implicit neural representation is a network $\Phi(x)$ defined by constraints on $\Phi$ and its derivatives, not only by sample values (eq. 1). ReLU networks are piecewise linear, so their second derivative is zero and they cannot represent higher-order content. tanh and softplus have poorly behaved derivatives and still miss fine detail (source: Sitzmann 2020, §1).

## Method

> [!definition] SIREN
> $$\phi_i(x_i) = \sin(W_i x_i + b_i)$$
> $$\Phi(x) = W_n(\phi_{n-1}\circ\cdots\circ\phi_0)(x) + b_n$$
> Every derivative of a SIREN is again a SIREN, because the derivative of sine is a phase-shifted sine (source: Sitzmann 2020, §3).

**Training as a feasibility problem.** Find $\Phi$ such that constraints $C_m(a(x),\Phi,\nabla\Phi,\dots)=0$ hold on domains $\Omega_m$; the loss sums constraint norms over sampled points (eq. 2-4).

> [!algorithm] Initialization (§3.2)
> Hidden layers: draw weights from
> $$w_i \sim U\left(-\sqrt{6/n},\ \sqrt{6/n}\right)$$
> with $n$ the layer fan-in. Then $w^{\top}x$ is approximately $N(0, 1)$-scaled before each sine, and the activations stay arcsine-distributed at every depth. First layer: use $\sin(\omega_0 W x + b)$ with $\omega_0 = 30$ so it spans many periods over $[-1,1]$.

Weights act as angular frequencies and biases as phase offsets. Few weights exceed $\pi$ in magnitude, so frequency grows only slowly with depth (source: Sitzmann 2020, §3.2). Training uses Adam ([[Adam paper (Kingma 2015)]]). A uniform weight init without this scaling gave poor accuracy and convergence.

## Results

- **Image fit** (Fig. 1): only SIREN and ReLU with positional encoding match the image; only SIREN also matches its gradient and Laplacian. A single image fits in a few hundred iterations.
- **Video** (300 frames, 512x512): PSNR 29.90 (SD 1.08) dB for SIREN against 25.12 (1.16) dB for ReLU (Fig. 2).
- **Poisson**: images reconstructed from gradients only, or Laplacians only; gradient-domain image editing by blending two gradient fields (Fig. 3, eq. 5).
- **Signed distance fields** (Eikonal, $|\nabla\Phi|=1$, eq. 6): a whole room from one five-layer network (Fig. 4).
- **Helmholtz and wave equations** (eq. 7): SIREN output matches a grid solver while tanh, ReLU and RBF networks fail; neural full-waveform inversion recovers velocity better than an ADMM-based FWI baseline with one frequency (Fig. 5).
- **Hypernetwork prior** over SIREN weights: CelebA 32x32 inpainting, pixel MSE 0.039/0.016/0.009 for CNP against 0.033/0.009/0.008 for a CNN encoder with hypernetwork, at increasing context sizes (Table 1; context sizes garbled in extraction).

## Limitations

- Initialization is justified informally; proofs are in the supplement, not read. **[unverified]** beyond the main text.
- $\omega_0 = 30$ was found empirically "to work well for all applications" (§3.2).
- The frequency growth through layers is not formalized: "a hard task" (footnote 2).
- Single-frequency FWI is a small test; ill-posed problems remain.

## Connections

- Concept page: [[SIREN]]. Competing fix for [[Spectral bias]]: [[Fourier features (Tancik 2020)]] (concurrent work, cited here as positional encoding).
- Solves PDE constraints with a network, like [[PINN]] and [[Physics-informed machine learning]]; second-order derivatives come from autodiff.
- Contrast with [[Neural ODE]], which pairs a solver with learned dynamics (source: Sitzmann 2020, §2). Related representation idea: [[Neural implicit flow]].
- The initialization argument parallels [[Glorot init (Glorot 2010)]] (variance preservation); see [[Weight initialization]].

%% refs:start %%
**Cites in this wiki**: [[Glorot init (Glorot 2010)]], [[PINNs (Raissi 2019)]]
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]], [[FNO (Li 2021)]], [[Neural operator (Kovachki 2022)]]
**Software cited**: [[software#OpenCV|OpenCV]], [[software#k-Wave|k-Wave]]
%% refs:end %%

**Sources**: `papers/ML/Sitzmann - SIREN - Implicit Neural Representations with Periodic Activation Functions.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[SIREN]]
- [[Spectral bias]]
- [[Fourier features]]
- [[PINN]]
- [[Neural ODE]]
- [[Weight initialization]]
