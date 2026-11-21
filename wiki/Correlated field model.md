---
type: method
area: ift
areas: [ift, bayesian]
source-ref: "Enßlin, IT & IFT, §16.3, pp. 175-176"
tags: [ift, bayesian, inverse-problems]
---

# Correlated field model

**Summary**: represent a field as a zero-mode plus a Gaussian process whose log power spectrum is itself a Gaussian process (a power law plus Wiener and integrated-Wiener-process deviations), controlled by a few Gaussian hyperparameters. The result is a flexible, non-Gaussian, adaptive prior that needs interacting IFT.

Page numbers `p.` are PDF pages of `Ensslin - Information Theory & Information Field Theory.pdf` (printed page = PDF page minus 6).

## Definition (§16.3, pp. 175-176)
Field $s'_x=s_0+s_x$ with zero-mode $s_0\leftarrow\mathcal G(s_0-\bar s_0,\sigma_{s_0}^2)$ and $s$ a Gaussian field with power spectrum $P_S(k)$. Let $x=\ln(|k|/k_0)$ and $\tilde\sigma=\ln(P_S/P_{\rm ref})$, where $\tilde\sigma(x)$ is modelled by:

$$\tilde\sigma(x)=\tilde\sigma_0-\alpha x+\mathrm{WP}(x)+\mathrm{IWP}(x),$$
$$\mathrm{WP}(x)=\sigma_{\rm WP}\!\int_{x_0}^{x}\!dx'\,\xi_{x'},\qquad
\mathrm{IWP}(x)=\sigma_{\rm IWP}\!\int_{x_0}^{x}\!dx'\!\int_{x_0}^{x'}\!dx''\,\eta_{x''},$$
with $\xi,\eta\leftarrow\mathcal G(\cdot,1)$. So the spectrum follows roughly a power law $k^{-\alpha}$ with stochastic deviations.

Hyperparameters, all with Gaussian priors on a latent variable:
- fluctuations: $\tau_0\leftarrow\mathcal G(\cdot,\sigma_{\tau_0}^2)$ (overall amplitude);
- slope: $\alpha\leftarrow\mathcal G(\cdot,\sigma_\alpha^2)$;
- asperity: $\sigma_{\rm WP}=e^{\tau_{\rm WP}}$ and $\sigma_{\rm IWP}=e^{\tau_{\rm IWP}}$ with Gaussian $\tau$'s.

The means and standard deviations of these are the model's hyperparameters, to be set explicitly. In the original model of the literature, flexibility (overall variance of both processes) and asperity (WP strength relative to IWP; zero asperity leaves only the IWP) are coupled (book footnote 2, p. 176).

The generative chain is $(\tau_0,\alpha,\dots)\to P_S\to s\to d$ (Fig. 20 of the book). It is highly non-Gaussian and adaptive, hence it "requires interacting IFT" ([[Interacting information field theory]]); in practice it is paired with [[Metric Gaussian variational inference]] because all latent variables have unit Gaussian priors.

(source: Ensslin - Information Theory & Information Field Theory.pdf, §16.3, pp. 175-176)

**Role**: an informative low-dimensional prior on $P_S$ cures the overfitting and negativity of the per-mode maximum-likelihood spectrum in [[Power spectrum estimation]].

**Covered in**: Enßlin IT & IFT §16.3 (pp. 175-176)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Power spectrum estimation]] · [[Wiener-Khinchin theorem|Power spectrum]] · [[Gaussian process]]
- [[Information field theory]] · [[Metric Gaussian variational inference]] · [[Geometric variational inference]]
