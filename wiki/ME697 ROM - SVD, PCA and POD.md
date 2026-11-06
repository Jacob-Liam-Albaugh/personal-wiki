---
type: lecture
area: me697
areas: [me697, ml]
course: me697
lecture: reduced_order_modeling
source-ref: "ME 697 book, reduced_order_modeling 01_svd, 02_pca, 03_pod"
tags: [ml, signals, pde, uq]
---

# ME697 ROM - SVD, PCA and POD

**Summary**: Three notebooks on linear dimension reduction. SVD gives the best low-rank approximation, PCA is the SVD of centered data, and POD is PCA in a Hilbert space of fields, equivalently an empirical Karhunen-Loève expansion.
**File**: `advanced-scientific-machine-learning/book/reduced_order_modeling/` (`01_svd.ipynb`, `02_pca.ipynb`, `03_pod.ipynb`, one photo). Not in `_toc.yml`.

---

## Topics
- [[Singular value decomposition]]: full, economy-size and truncated forms; image compression demo.
- [[Principal component analysis]]: covariance diagonalized by the SVD; MNIST demo.
- [[Proper orthogonal decomposition]]: operator eigenproblem on a Hilbert space; kernel form; computation through the SVD.
- Reference text: Brunton and Kutz, Data-Driven Science and Engineering.

## Key results
**SVD** of an $n\times m$ matrix:

$$
X = U\Sigma V^T.
$$

Truncation to rank $k$ is the best rank-$k$ approximation in the Frobenius norm:

$$
X_k = \sum_{i=1}^{k}\sigma_i\,u_i v_i^T.
$$

Choose $k$ so that the retained energy reaches a target:

$$
\frac{\sum_{i\le k}\sigma_i^2}{\sum_{i}\sigma_i^2} \ge 0.9.
$$

**PCA.** Center the data, $B$ with rows $x_i - $ mean. Covariance and its SVD form:

$$
C = \tfrac1n B^T B = \tfrac1n V\Sigma^2V^T.
$$

Columns of $V$ are principal directions, variance along direction $j$ is $\sigma_j^2/n$, total variance is $\sum_j\sigma_j^2/n$. Principal components $Z=XV=U\Sigma$ are uncorrelated:

$$
\langle z_{ik}z_{il}\rangle = \frac{\sigma_k^2}{n}\,\delta_{kl}.
$$

**POD.** For fields $u_i$ in a Hilbert space with inner product $\langle\cdot,\cdot\rangle$ and empirical average $\langle\cdot\rangle$ (not the inner product), minimizing mean squared reconstruction error over a unit $\phi$ is the same as maximizing mean squared projection, with Lagrange multiplier $\lambda$:

$$
\big\langle \langle\phi,u\rangle\,u \big\rangle = \lambda\,\phi.
$$

So $\phi$ is an eigenfunction of $R\phi=\langle\langle\phi,u\rangle u\rangle$, which is linear, self-adjoint and compact. In $L^2(\Omega)$ it has the kernel

$$
R(x,y) = \langle u(x)\,u(y)\rangle = \sum_i\lambda_i\phi_i(x)\phi_i(y).
$$

**Discrete POD.** With data matrix $X$ ($n$ snapshots by $N$ grid points), $R=\tfrac1n X^TX$, so

$$
\phi_i = v_i,
\qquad
\lambda_i = \sigma_i^2/n,
\qquad
Z = XV = U\Sigma.
$$

## Examples
> [!example] Image compression (01_svd)
> A grayscale photo is compressed with $k\in\{1,2,4,\dots,256,682\}$; the title of each plot gives the stored size $(n+m)k/(nm)$ as a percent of the original.

> [!example] MNIST (02_pca)
> Centered MNIST, SVD, cumulative variance plot with a 90% line, the first principal directions drawn as $28\times28$ images, and a 2D scatter of the first two components coloured by digit.

> [!example] Homework 5 and 7
> Homework 5 derives POD operator properties and applies POD to a Navier-Stokes velocity-magnitude dataset; homework 7 uses SVD of a Hankel matrix. See [[ME697 7 - Homework]].

## Connections
- POD with an analytical covariance is the [[Karhunen-Loève expansion]]; POD uses the empirical covariance.
- Spatial basis for [[Dynamic mode decomposition]] ([[ME697 DMD - Dynamic mode decomposition]]).
- Surrogates in a reduced basis: [[ME697 2.3 - Surrogates]]; operator-learning alternatives: [[Operator learning]].

**Wiki note (book errors)**:
- 01_svd and 02_pca: the text defines $k$ through the sum of squared singular values, but the code computes `cumsum(s)/sum(s)` without squaring. The cumulative-variance plots and the "90% at k" label therefore describe singular values, not variance.
- 02_pca: states that typically $n\ll m$ for $n$ samples and $m$ features; this is the opposite of the usual case for MNIST and the economy-SVD discussion in 01 assumes $n\ge m$ **[unverified]**.
- 03_pod: the loss is called $L(\phi)$ then $J(\phi)$, and "$\langle\langle\phi,u\rangle u\rangle-\lambda\phi$" is missing "$=0$".

**Sources**: `advanced-scientific-machine-learning/book/reduced_order_modeling/01_svd.ipynb`, `02_pca.ipynb`, `03_pod.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Singular value decomposition]] · [[Principal component analysis]] · [[Proper orthogonal decomposition]] · [[Karhunen-Loève expansion]] · [[Dynamic mode decomposition]]
- [[ME697 DMD - Dynamic mode decomposition]] · [[ME697 7 - Homework]]
