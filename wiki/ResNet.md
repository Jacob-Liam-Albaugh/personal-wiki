---
type: concept
area: ml
areas: [ml]
source-ref: "He et al. 2016, eq. 1-2"
tags: [ml, optimization]
---

# ResNet

**Summary**: A network whose blocks compute $y=x+F(x)$: a residual branch $F$ added to an identity shortcut. The shortcut gives gradients a direct path through depth and makes "do nothing" the default for each block.

**Sources**: `papers/ML/He, Zhang, Ren, Sun - ResNets.pdf`.
**Last updated**: 2026-11-06

---

## Definition

> [!definition] Residual block
> $$y=F(x,\{W_i\})+x$$
> If input and output sizes differ, $y=F(x,\{W_i\})+W_sx$ with a projection $W_s$.
>
> (source: `He, Zhang, Ren, Sun - ResNets.pdf`, eq. 1-2, p. 3)

## Why it helps

- Plain deep nets show a degradation problem: training error rises with depth even with normalized init and batch norm. ResNets remove it in the paper's experiments ([[ResNet paper (He 2016)]]).
- Identity shortcuts cost no parameters, so depth can be raised at fixed width and compute.
- The block only has to learn a perturbation of identity; the paper's evidence is that learned residuals have small responses (Fig. 7).

## Wiki note: connections

- Same form as one forward-Euler step $x_{k+1}=x_k+hf(x_k)$, which is how [[Neural ODE]] reads depth as time.
- In the Poly/lens language of the lab, blocks compose by function composition; no source in this folder links the two **[unverified]**.
- Deep nets also train with careful init ([[Weight initialization]]) and [[Momentum]]/[[Adam]].

## Related pages
- [[ResNet paper (He 2016)]]
- [[Weight initialization]]
- [[Glorot init (Glorot 2010)]]
- [[Neural ODE]]
- [[Dropout]]
- [[Convolutional neural network]] · [[AlexNet (Krizhevsky 2012)]] · [[U-Net]]
