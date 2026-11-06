---
type: paper
area: ml
areas: [ml]
source-ref: "Kipf & Welling 2016, arXiv:1611.07308, pp. 1-2"
tags: [ml, vi, bayesian, generative]
authors: ["[[Thomas Kipf]]", "[[Max Welling]]"]
year: 2016
venue: "arXiv:1611.07308v1 (NIPS 2016 Bayesian Deep Learning workshop)"
file: "papers/ML/Welling, Kipf - Variational Graph Auto-Encoders.pdf"
---

# Variational graph auto-encoder (Kipf 2016)

**Summary**: A VAE for graphs. A two-layer graph convolutional network (GCN) encodes node features and adjacency into Gaussian latent variables per node. An inner-product decoder gives edge probabilities. It does unsupervised link prediction and uses node features naturally, which clearly lifts accuracy.

**Authors**: Thomas Kipf, Max Welling · **Year**: 2016 · **File**: `papers/ML/Welling, Kipf - Variational Graph Auto-Encoders.pdf` (the file name lists Welling first; the first author is Kipf)

---

## Problem

Learn node embeddings for an undirected graph without labels, such that edges can be predicted. Baselines (spectral clustering, DeepWalk) cannot use node features (source: Kipf 2016, p. 1-2).

## Method

Setup: $G=(V,E)$ with $N$ nodes, adjacency $A$ (self-loops included), degree matrix $D$, features $X\in\mathbb{R}^{N\times D}$, latents $Z\in\mathbb{R}^{N\times F}$.

> [!definition] Inference model
> $$q(Z\mid X,A) = \prod_i N\left(z_i \mid \mu_i, \mathrm{diag}(\sigma_i^2)\right)$$
> $$\mu = \mathrm{GCN}_\mu(X,A),\quad \log\sigma = \mathrm{GCN}_\sigma(X,A)$$
> $$\mathrm{GCN}(X,A) = \tilde A\,\mathrm{ReLU}(\tilde A X W_0)\,W_1$$
> with $\tilde A = D^{-1/2} A D^{-1/2}$. The two GCNs share $W_0$.

> [!definition] Generative model
> $$p(A_{ij}=1\mid z_i,z_j) = \sigma(z_i^{\top} z_j)$$
> Prior: $p(Z)=\prod_i N(z_i\mid 0, I)$.

> [!algorithm] Training
> Maximize the ELBO
> $$\mathcal{L} = \mathbb{E}_{q}\left[\log p(A\mid Z)\right] - \mathrm{KL}\left[q(Z\mid X,A)\,\Vert\,p(Z)\right]$$
> with the reparameterization trick and full-batch gradient descent. For sparse $A$, edge terms ($A_{ij}=1$) are re-weighted. The non-probabilistic GAE uses $\hat A=\sigma(ZZ^{\top})$ with $Z=\mathrm{GCN}(X,A)$.

Without features, set $X=I$.

## Results

Link prediction on Cora, Citeseer, Pubmed. 5% of links held out for validation, 10% for test, with equal numbers of sampled non-edges. 200 iterations of Adam at learning rate 0.01, hidden size 32, latent size 16, Glorot init (source: Kipf 2016, p. 2).

| Model with features | Cora AUC / AP | Citeseer AUC / AP | Pubmed AUC / AP |
|---|---|---|---|
| VGAE | 91.4 / 92.6 | 90.8 / 92.0 | 94.4 / 94.7 |

Features give a large gain over the featureless variants (VGAE* about 84 to 88 on Cora, 78.9 to 84.1 on Citeseer). Other table rows (SC, DW, GAE) were partly garbled in extraction and are not cited.

## Limitations

- A Gaussian prior is probably a poor fit for an inner-product decoder, which pushes embeddings away from the origin (Fig. 1). Better priors, more flexible decoders and minibatch (SGD) scaling are listed as future work (p. 2).
- Full-batch training limits scale.
- Short workshop paper: one task, three citation graphs, 10 random-init runs on fixed splits.

## Connections

- Direct graph version of the [[VAE paper (Kingma 2014)]]; see also [[VAE]] and [[Intro to VAEs (Kingma 2019)]].
- Encoder is a message-passing network: [[Graph neural network]]. Compare the learned message functions of [[Symbolic models from deep learning (Cranmer 2020)]] and the permutation-invariant pooling in [[Deep Sets paper (Zaheer 2017)]].
- Uses [[Adam paper (Kingma 2015)]] and [[Glorot init (Glorot 2010)]].
- Variational inference background: [[Bayesian neural networks]].

%% refs:start %%
**Cites in this wiki**: [[Adam paper (Kingma 2015)]], [[Glorot init (Glorot 2010)]], [[VAE paper (Kingma 2014)]]
%% refs:end %%

**Sources**: `papers/ML/Welling, Kipf - Variational Graph Auto-Encoders.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Graph neural network]]
- [[VAE paper (Kingma 2014)]]
- [[VAE]]
- [[Deep Sets]]
- [[Adam paper (Kingma 2015)]]
- [[Glorot init (Glorot 2010)]]
