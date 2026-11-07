---
type: paper
area: ml
areas: [ml]
source-ref: "Tancik et al. 2020, arXiv:2006.10739, §3-6"
tags: [ml, signals, gp]
authors: ["[[Matthew Tancik]]", "[[Pratul P. Srinivasan]]", "[[Ben Mildenhall]]", "[[Sara Fridovich-Keil]]", "[[Nithin Raghavan]]", "[[Utkarsh Singhal]]", "[[Ravi Ramamoorthi]]", "[[Jonathan T. Barron]]", "[[Ren Ng]]"]
year: 2020
venue: "NeurIPS 2020 (arXiv:2006.10739v1)"
file: "papers/ML/Tanicik, Srinivasan, Midenhall, et. al. - Fourier Features Let Netowrks Learn High Frequency Functions in Low Dimensional Domains.pdf"
---

# Fourier features (Tancik 2020)

**Summary**: A coordinate-based MLP struggles to fit high frequencies because its neural tangent kernel (NTK) has a rapidly decaying spectrum. Passing the input through a sinusoidal map $\gamma(v)$ makes the composed NTK stationary with a tunable bandwidth. Random Gaussian frequencies, with the scale tuned, beat both no mapping and the NeRF-style positional encoding.

**Authors**: Matthew Tancik, Pratul P. Srinivasan, Ben Mildenhall, Sara Fridovich-Keil, Nithin Raghavan, Utkarsh Singhal, Ravi Ramamoorthi, Jonathan T. Barron, Ren Ng · **Year**: 2020 · **File**: `papers/ML/Tanicik, Srinivasan, Midenhall, et. al. - Fourier Features Let Netowrks Learn High Frequency Functions in Low Dimensional Domains.pdf` (the file name misspells the first author)

---

## Problem

Coordinate-based MLPs map low-dimensional points (pixels, 3D positions) to colour, density or occupancy. Fed raw coordinates they give blurry output: the [[Spectral bias]] of Rahaman et al. Earlier work found that a hand-made sinusoidal "positional encoding" helps, without explanation (source: Tancik 2020, §1-2).

## Method

**Kernel regression view.** In the infinite-width, small-step limit the network follows kernel regression with the NTK, $k_{\mathrm{NTK}}(x_i,x_j) = \mathbb{E}_\theta \langle \partial f(x_i;\theta), \partial f(x_j;\theta)\rangle$ (§3). Training predictions follow

$$\hat y(t) \approx K_{\mathrm{test}} K^{-1}\left(I - e^{-\eta K t}\right) y$$

> [!theorem] Eigenmode convergence (§3)
> With $K = Q\Lambda Q^{\top}$, the error component along eigenvector $i$ decays like $e^{-\eta\lambda_i t}$. Large eigenvalues are learned fast. The NTK eigenvalues of a standard MLP fall quickly with frequency, so high frequencies essentially never converge.

> [!definition] Fourier feature mapping (eq. 5)
> $$\gamma(v) = \left[a_1\cos(2\pi b_1^{\top}v),\ a_1\sin(2\pi b_1^{\top}v),\ \dots,\ a_m\cos(2\pi b_m^{\top}v),\ a_m\sin(2\pi b_m^{\top}v)\right]^{\top}$$
> The induced kernel is stationary:
> $$k_\gamma(v_1,v_2) = \sum_j a_j^2\cos\left(2\pi b_j^{\top}(v_1-v_2)\right)$$

The MLP then sees $\gamma(v)$, so the effective kernel is $h_{\mathrm{NTK}}\circ h_\gamma$, which is a shift-invariant convolution kernel (§4). The $b_j$ set the frequencies and $a_j^2$ the spectrum weights, so the bandwidth is controllable. This is the random Fourier feature idea of Rahimi and Recht (Bochner's theorem) put in front of a deep net.

**Choosing the map.**
- 1D: set $b_j=j$, $a_j = 1/j^p$. Lower $p$ gives a wider spectrum, a narrower spatial kernel, and faster convergence on high frequencies, but overfitting if too wide (Fig. 2-3).
- Higher-dimensional: sample $b_j\sim N(0,\sigma^2)$ (isotropic Gaussian), $a_j=1$. The scale $\sigma$ matters far more than the distribution family (Fig. 4). Tune $\sigma$ on held-out data.

## Results

- 1D: the NTK linear model predicts the observed training and test loss. The best test loss was at $p=1$; narrower spectra never converge on high-frequency components (Fig. 3).
- Table 1 compares no mapping, basic ($[\cos 2\pi v,\sin 2\pi v]$), positional encoding, and Gaussian on image regression, 3D shape, CT, MRI and NeRF. Gaussian is best on all tasks. Example: natural-image PSNR 19.32 (none) to 25.57 (Gaussian); 3D shape IoU 0.864 to 0.973 (source: Tancik 2020, Table 1; other columns garbled in extraction, not cited).

## Limitations

- The theory needs very wide networks and small learning rates; the paper checks it in carefully controlled 1D settings (§4).
- $\sigma$ is a hyperparameter with an underfit/overfit trade-off; there is no single best scale.
- Dense Fourier bases do not scale to high $d$, hence random sampling (§4).
- Aimed at low-dimensional domains; not claimed for high-dimensional inputs.

## Connections

- Concept page: [[Fourier features]]. Problem it addresses: [[Spectral bias]], from [[Spectral bias (Rahaman 2019)]].
- Uses [[Neural tangent kernel]] and [[Kernel methods]]; the mapping is a [[Random features model]] feature map.
- Alternative: periodic activations in [[SIREN paper (Sitzmann 2020)]] / [[SIREN]].
- Relevant to [[Neural implicit flow]] and to [[PINN]] solution networks with sharp features. Wiki note: the PINN link is a suggested use, not made in this paper.
- Stationary-kernel vocabulary: [[Gaussian process]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Attention is all you need (Vaswani 2017)]], [[NTK (Jacot 2018)]], [[Spectral bias (Rahaman 2019)]]
**Cited by in this wiki**: [[Expert's guide to PINNs (Wang 2023)]], [[NIF (Pan 2023)]], [[When and why PINNs fail (Wang 2022)]]
**Software cited**: [[software#JAX|JAX]]
%% refs:end %%

**Sources**: `papers/ML/Tanicik, Srinivasan, Midenhall, et. al. - Fourier Features Let Netowrks Learn High Frequency Functions in Low Dimensional Domains.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Fourier features]]
- [[Spectral bias]]
- [[Spectral bias (Rahaman 2019)]]
- [[SIREN]]
- [[Neural tangent kernel]]
- [[Random features model]]
- [[Kernel methods]]
