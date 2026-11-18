---
type: example
area: me697
areas: [me697]
source-ref: "ASML (ME 697)"
tags: [ml]
data-origin: [synthetic]
tasks: [regression]
uses: 1
---

# Spectral bias 1D regression

**Summary**: 1 use in ASML (ME 697). Data: synthetic. Tasks: regression.

**Covered in**: ASML (ME 697)
**Sources**: `text_books/advanced-scientific-machine-learning/book/pinns/basics/spectral_bias.ipynb`.
**Last updated**: 2026-11-18

---

## Spectral bias: 1D noisy two-frequency regression

`text_books/advanced-scientific-machine-learning/book/pinns/basics/spectral_bias.ipynb`

- **Source**: ASML (ME 697), lecture, complete
- **Problem**: regression
- **Technique**: Compare MLP (batch 32, 300 epochs) with Fourier features (100 epochs) to show spectral bias
- **Data**: f(x)=sin(2 pi x)+0.5 sin(16 pi x) on [0,1], 1000 uniform points, Gaussian noise sd 0.1.
- **Data origin**: synthetic
- **Forward model**: Closed-form target function; plain MLP (width 128, depth 4) vs Fourier-feature MLP (sigma=5).
- **Unknown dimension**: network weights
- **Data dimension**: 1000 (x,y) pairs
- **Ground truth**: Noise-free f known
- **What makes it hard**: High-frequency component learned slowly by plain MLP
- **Libraries**: jax, equinox, optax
- **References**: Rahaman et al. 2019 (arXiv 1806.08734); Tancik et al. 2020 (arXiv 2006.10739)

## Related pages
- [[Examples catalogue]]
- [[PINN]] · [[Fourier features]] · [[Spectral bias]]
