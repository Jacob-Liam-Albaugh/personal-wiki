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
Columns of $\mathbf V$ are principal directions; $\sigma_j^2/n$ is the variance along direction $j$ and $\sum_j\sigma_j^2/n$ the total variance.
Scores:
$$\mathbf Z=\mathbf B\mathbf V=\mathbf U\boldsymbol\Sigma$$
and $\langle z_{ik}z_{il}\rangle=\tfrac{\sigma_k^2}{n}\delta_{kl}$.

## Uses in the course
- MNIST: directions look like digits; two components separate classes.
- Output reduction: stochastic heat equation with a field-valued output, KLE on the input, PCA on the output, one GP per PCA coefficient (06). See [[Karhunen-Loève expansion]].
- Cousin of the [[Karhunen-Loève expansion]], which does the same to a random field with known covariance.

## Wiki notes
- Explained variance must use $\sigma_j^2$, not $\sigma_j$.
- $\mathbf Z=\mathbf X\mathbf V$ equals $\mathbf B\mathbf V$ only for centered data.
- Book says "$n\ll m$" for MNIST, which is wrong ($n=70000$ images, $m=784$ pixels).

## Related / transform coding
- Data-adapted counterpart of fixed transforms such as the [[DFT]] and block transform coding in [[Image transforms]] and [[Image compression]]; see [[Image compression]]. (source: Digital Signal Processing/Topic IP.5 image transforms and wavelets Apr 14, 2025.pdf)

> [!example] Stochastic heat equation to a whole field (06)
> Same input model as the KLE example. Collect 100 temperature fields, hold out 10%, run PCA (energy 0.95) on the 90 training fields, and train one GP per coefficient $\eta_j$ on $\boldsymbol\xi\mapsto\eta_j$. Reconstruct
> $$u(x)\approx\bar u(x)+\sum_{j}\eta_j\phi^{\text{PCA}}_j(x)$$
> For 1000 samples of $\boldsymbol\xi$ this gives the mean field and a 95% band in a fraction of a second: uncertainty propagated from one infinite-dimensional random field to another.

Further wiki notes:
- `best_k = argmax(cum_var > alpha)` is a zero-based index, so $k$ = `best_k + 1` components are needed; the plotted label reports `best_k`. The "first 10 principal directions" cell plots 25.
- In 06 the displayed expansion $c(x)\approx\sum\xi_i\sqrt{\lambda_i}\phi_i$ is really for $g=\log c$, the output expansion omits the PCA mean, and the same `subkey` is reused for every coefficient's GP. Batch size 100 exceeds the 90 training points.

**Covered in**: ASML book hup/funcin (ME 697 3.1)
**Sources**: `advanced-scientific-machine-learning/book/hup/funcin/03_pca.ipynb`, `06_up_hout_example.ipynb`, `advanced-scientific-machine-learning/book/hup/intro.md`, `hup/funcin/intro.md`, `01_functional_inputs.md`, `02_svd.ipynb`, `04_kle.ipynb`, `05_up_example.ipynb`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Singular value decomposition]] · [[Proper orthogonal decomposition]] · [[Karhunen-Loève expansion]] · [[PCA-Net]]
- [[Surrogate model]]
