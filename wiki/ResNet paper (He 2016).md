---
type: paper
area: ml
areas: [ml]
source-ref: "He, Zhang, Ren, Sun 2016, CVPR, eq. 1-2"
tags: [ml, optimization]
authors: ["[[Kaiming He]]", "[[Xiangyu Zhang]]", "[[Shaoqing Ren]]", "[[Jian Sun]]"]
year: 2016
venue: "CVPR 2016 (arXiv 1512.03385v1)"
file: "papers/ML/He, Zhang, Ren, Sun - ResNets.pdf"
---

# ResNet paper (He 2016)

**Summary**: Reformulates stacked layers as learning a residual $F(x)=H(x)-x$ added back through a parameter-free identity shortcut, $y=F(x)+x$. This fixes the "degradation" of plain deep nets, where more layers raise training error, and gives networks up to 152 layers on ImageNet (and 1202 on CIFAR-10) that train easily. An ensemble won ILSVRC 2015 classification at 3.57% top-5 test error.

**Authors**: Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun · **Year**: 2016 (the PDF is the arXiv v1 of Dec 2015) · **File**: `papers/ML/He, Zhang, Ren, Sun - ResNets.pdf`

---

## Problem

Depth matters, and vanishing or exploding gradients are largely handled by normalized initialization ([[Glorot init (Glorot 2010)]]) and intermediate normalization layers (p. 1). But deeper nets then show a degradation problem: accuracy saturates and then falls, and the cause is not overfitting, because the training error itself rises (Fig. 1, p. 1). A deeper net could copy a shallower one and add identity layers, so it should do no worse; the solvers fail to find that solution.

## Method

> [!definition] Residual block
> With $H(x)$ the desired mapping of a few stacked layers, let them fit $F(x):=H(x)-x$ and output
> $$y=F(x,\{W_i\})+x.$$
> For two layers, $F=W_2\,\sigma(W_1x)$ with $\sigma$ the ReLU, biases omitted, and the second ReLU applied after the addition.
>
> (source: `He, Zhang, Ren, Sun - ResNets.pdf`, eq. 1, Fig. 2, p. 3)

- If dimensions differ, a linear projection is used on the shortcut: $y=F(x,\{W_i\})+W_sx$ (eq. 2). Identity is enough for the degradation problem; $W_s$ is used only to match dimensions (p. 3).
- Identity shortcuts add no parameters or computation (besides an addition), so plain and residual nets can be compared at equal depth, width and cost.
- Motivation: if identity is optimal, the solver can push the weights of the residual branch toward 0. Otherwise the shortcut may precondition the problem; learned residuals have small responses (Fig. 7, p. 3).
- Dimension-increasing shortcuts: (A) identity with zero padding, (B) 1x1 convolution projection, (C) projection on all shortcuts (p. 4).
- Bottleneck block for 50/101/152 layers: 1x1, 3x3, 1x1 convolutions (reduce then restore width, Fig. 5). With projection shortcuts the cost would double, so identity matters there (p. 6).
- Training (§3.4, p. 4): batch normalization after each convolution and before activation; weights initialized as in He et al. 2015 (their reference [13], not in this folder); SGD, minibatch 256, learning rate 0.1 divided by 10 at plateaus, weight decay 0.0001, momentum 0.9, no [[Dropout]].

## Results

- **Plain nets degrade** (§4.1, Table 2, p. 5): top-1 validation error 27.94% (18 layers) versus 28.54% (34 layers). Training error is also higher for the deeper one (Fig. 4). The authors argue it is unlikely to be vanishing gradients, since BN keeps forward and backward signals healthy, and conjecture exponentially low convergence rates. 3x longer training did not remove it.
- **ResNets fix it** (Table 2): 27.88% (18) and 25.03% (34), i.e. the 34-layer ResNet beats the 18-layer by 2.8% and its plain counterpart by 3.5%. The 18-layer ResNet converges faster than the plain 18-layer.
- **Shortcut options** (Table 3, p. 6): ResNet-34 A 25.03 / 7.76, B 24.52 / 7.46, C 24.19 / 7.40 (top-1 / top-5). Differences are small, so projections are not essential.
- **Deeper** (Table 3): ResNet-50 22.85 / 6.71, ResNet-101 21.75 / 6.05, ResNet-152 21.43 / 5.71. The 152-layer net has 11.3 billion FLOPs, below VGG-16/19 at 15.3/19.6 billion.
- **Single model and ensemble** (Tables 4-5): ResNet-152 single model 4.49% top-5 validation, below all previous ensembles. Six-model ensemble 3.57% top-5 test error, 1st in ILSVRC 2015 classification.
- **CIFAR-10** (§4.2, Fig. 6-7, p. 7-8): architectures with $6n+2$ layers. Plain nets get worse with depth (plain-110 over 60% error); ResNets improve to 110 layers (6.43% test error). With 1202 layers training error is below 0.1% but test error is 7.93%, worse than 110 layers, which the authors attribute to overfitting (19.4M parameters).
- **Layer responses** (Fig. 7): residual functions have smaller response standard deviations than plain layers, and deeper ResNets have smaller ones.
- **Detection** (§4.3): replacing VGG-16 with ResNet-101 in Faster R-CNN gives +6.0 points on COCO mAP@[.5,.95], a 28% relative gain; also 1st on ImageNet detection and localization and COCO detection and segmentation.

## Limitations

Authors: the reason plain deep nets are hard to optimize is left for future work (p. 5); results at 1000+ layers are not better than 110 layers (p. 8); stronger regularization such as dropout or maxout was not combined with ResNets (p. 8).

Wiki note: the paper does not mention the ODE view of residual updates, which later work (see [[Neural ODE]]) develops from $y=x+F(x)$ as an Euler step. That link is the wiki's, not the paper's.

## Connections

- Initialization and normalization as the previous fix: [[Glorot init (Glorot 2010)]], [[Weight initialization]].
- Trained with SGD plus [[Momentum]] 0.9 ([[SGD]]).
- Residual updates $x+F(x)$ are the discrete form that [[Neural ODE]] takes to the continuous limit.
- Concept page: [[ResNet]].

%% refs:start %%
**Cites in this wiki**: [[Glorot init (Glorot 2010)]]
%% refs:end %%

**Sources**: `papers/ML/He, Zhang, Ren, Sun - ResNets.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[ResNet]]
- [[Glorot init (Glorot 2010)]]
- [[Weight initialization]]
- [[Dropout]]
- [[Momentum]]
- [[SGD]]
- [[Neural ODE]]
