---
type: method
area: me697
areas: [me697, ml]
tags: [ml, uq, inverse-problems]
---

# Principal component analysis

**Summary**: Finds orthogonal directions of maximal variance in centered data; it is the [[Singular value decomposition]] of the centered data matrix. The coefficients on those directions are uncorrelated, so a high-dimensional output can be reduced to a few of them.

---

## Derivation (03)
Center: $\mathbf B=\mathbf X-\bar{\mathbf x}$, covariance $\mathbf C=\tfrac1n\mathbf B^T\mathbf B$.
The first direction maximizes $\mathbf v^T\mathbf C\mathbf v$ over unit vectors: the top eigenvector of $\mathbf C$.
With $\mathbf B=\mathbf U\boldsymbol\Sigma\mathbf V^T$:
$$\mathbf C=\tfrac1n\mathbf V\boldsymbol\Sigma^2\mathbf V^T$$
Columns of $\mathbf V$ are principal directions; $\sigma_j^2/n$ is the variance along direction $j$.
Scores:
$$\mathbf Z=\mathbf B\mathbf V=\mathbf U\boldsymbol\Sigma$$
and $\langle z_{ik}z_{il}\rangle=\tfrac{\sigma_k^2}{n}\delta_{kl}$.

## Uses in the course
- MNIST: directions look like digits; two components separate classes.
- Output reduction: stochastic heat equation with a field-valued output, KLE on the input, PCA on the output, one GP per PCA coefficient (06). See [[ME697 3.1 - Functional inputs]].
- Cousin of the [[Karhunen-Loève expansion]], which does the same to a random field with known covariance.

## Wiki notes
- Explained variance must use $\sigma_j^2$, not $\sigma_j$.
- $\mathbf Z=\mathbf X\mathbf V$ equals $\mathbf B\mathbf V$ only for centered data.
- Book says "$n\ll m$" for MNIST, which is wrong ($n=70000$ images, $m=784$ pixels).

## Related / transform coding
- Data-adapted counterpart of fixed transforms such as the [[DFT]] and block transform coding in [[ECE438 IP.5 - Image transforms and wavelets]] and [[ECE438 IP.6 - Image compression]]; see [[Image compression]]. (source: Digital Signal Processing/Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf)

**Sources**: `advanced-scientific-machine-learning/book/hup/funcin/03_pca.ipynb`, `06_up_hout_example.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Singular value decomposition]] · [[Proper orthogonal decomposition]] · [[Karhunen-Loève expansion]] · [[PCA-Net]]
- [[ME697 3.1 - Functional inputs]] · [[Surrogate model]]
