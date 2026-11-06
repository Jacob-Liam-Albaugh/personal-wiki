---
type: method
area: me697
areas: [me697, ml]
tags: [ml, uq, inverse-problems]
---

# Singular value decomposition

**Summary**: Factors any matrix $\mathbf X\in\mathbb R^{n\times m}$ into orthogonal factors and non-negative singular values. Truncating gives the best low-rank approximation, and it underlies [[Principal component analysis]].

---

## Definition
$$\mathbf X=\mathbf U\boldsymbol\Sigma\mathbf V^{T}$$
Columns of $\mathbf U$, $\mathbf V$ are orthonormal; $\boldsymbol\Sigma$ is diagonal with $\sigma_1\ge\sigma_2\ge\dots\ge0$. Variants: full, economy (thin), truncated.

## Truncation
$$\mathbf X_k=\sum_{i=1}^k\sigma_i\mathbf u_i\mathbf v_i^T$$
- Best rank-$k$ approximation in the Frobenius norm (`02_svd.ipynb`; Wiki note: this is the Eckart-Young theorem).
- Storage $(n+m)k$ instead of $nm$.
- Pick $k$ so the retained fraction of $\sum_i\sigma_i^2$ reaches a target (0.998 in the image-compression demo).

## Wiki notes
- Energy uses squared singular values. The PCA notebooks (03, 06) accumulate unsquared $\sigma_i$ for "explained variance", which is wrong; see [[ME697 3.1 - Functional inputs]].
- Eigenvectors of $\mathbf X^T\mathbf X$ are $\mathbf V$ and its eigenvalues are $\sigma_i^2$, which is the link to PCA and to [[Proper orthogonal decomposition]].

## Where it appears
Image compression and PCA ([[ME697 3.1 - Functional inputs]]), dimension reduction of PDE outputs, [[Dynamic mode decomposition]], [[PCA-Net]].

## Related / image transforms
- Appears next to the separable 2D transforms in [[ECE438 IP.5 - Image transforms and wavelets]] and [[ECE438 L33 - Specific 2D image transforms]]. **[unverified]** whether the lecture names the SVD; link is by topic. (source: Digital Signal Processing/Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf)

**Sources**: `advanced-scientific-machine-learning/book/hup/funcin/02_svd.ipynb`, `03_pca.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Principal component analysis]] · [[Karhunen-Loève expansion]] · [[Proper orthogonal decomposition]] · [[Dynamic mode decomposition]]
- [[ME697 3.1 - Functional inputs]]
