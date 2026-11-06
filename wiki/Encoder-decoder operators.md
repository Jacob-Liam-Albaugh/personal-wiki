---
type: concept
area: operators
source-ref: "Kovachki, Lanthaler, Stuart 2024, §2.4, p. 5; §3.5, pp. 10-11; Table 1, p. 11"
tags: [operators, ml]
---

# Encoder-decoder architecture (operator learning)

**Summary**: approximate $\Psi^\dagger:\mathcal U\to\mathcal V$ by encoding the input to $\mathbb R^{d_U}$, mapping with a finite-dimensional network, and decoding to $\mathcal V$. PCA-Net and DeepONet are the main examples.

**Sources**: `Operators/Stuart - Operator Leraning - Algorithms and Analysis.pdf`.
**Last updated**: 2026-11-06

---

> [!definition] Encoder-decoder net (Kovachki et al. 2024, §2.4, p. 5)
> $$\Psi_{ED}=G_V\circ\alpha\circ F_U$$
> $F_U:\mathcal U\to\mathbb R^{d_U}$ and $G_V:\mathbb R^{d_V}\to\mathcal V$ are bounded linear, and $\alpha:\mathbb R^{d_U}\to\mathbb R^{d_V}$ is continuous. The target of $\alpha$ is the latent map $\varphi=F_V\circ\Psi^\dagger\circ G_U$.

The review prints the composition as $F_U\circ\alpha\circ G_V$ in Thm 4.1, which looks like a typo for the order above (reader's note).

## Linear vs nonlinear approximation
- Outputs of an encoder-decoder net lie in the fixed $d_V$-dimensional subspace $\operatorname{span}(G_V)$. This is linear approximation, limited by the Kolmogorov $n$-width of the output set.
- A [[Neural operator]] composes nonlinear layers in function space, so its outputs lie on a nonlinear manifold.
- Table 1 (p. 11) puts the classes beside FEM, FVM and finite differences.

## Error decomposition
$$\mathcal E\lesssim\mathcal E_U+\mathcal E_\psi+\mathcal E_V$$
encoding, network and decoding errors (eq. 5.3, p. 21). This split drives the [[Curse of parametric complexity]] heuristic.

## Instances
| Model | Encoder | Decoder |
|---|---|---|
| [[PCA-Net]] | PCA of the inputs | PCA of the outputs |
| [[DeepONet]] | point evaluations (sensors) | learned trunk-net basis $\psi_j(y)$ |

## Where it appears
- [[Operator learning review (Kovachki 2024)]].

## Related pages
- [[Operator learning]] · [[PCA-Net]] · [[DeepONet]] · [[Universal approximation for operators]]
