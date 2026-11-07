---
type: definition
area: ml
areas: [ml]
source-ref: "Krizhevsky et al. 2012, §4.1, Fig. 1"
tags: [ml, optimization]
---

# ReLU

> [!definition] Rectified linear unit
> $$f(x)=\max(0,x)$$
> Non-saturating for $x>0$. Named "ReLU" following Nair and Hinton 2010.
>
> (source: AlexNet.pdf, §4.1, p. 2)

**Intuition**: tanh and the logistic sigmoid flatten for large $|x|$, so gradients vanish and gradient descent crawls. ReLU has slope 1 on the active side. Krizhevsky et al. found a four-layer CNN reached 25% training error on CIFAR-10 six times faster than with tanh (Fig. 1), and say large networks would not have been feasible to experiment with otherwise.

## Consequences
- No input normalization is needed to avoid saturation: if some training examples give a positive input, the unit learns (AlexNet, §4.3).
- AlexNet initializes biases to 1 in several layers to give ReLUs positive inputs early (§6).
- U-Net pairs ReLU with $N(0,2/N)$ init so feature maps keep roughly unit variance (U-Net.pdf, §3, p. 5); see [[Weight initialization]].
- Piecewise-linear units were the "well-behaved gradient" the GAN paper cites for discriminative successes, and are used in its generators (source: [[GAN paper (Goodfellow 2014)]], pp. 1, 6).

## Failure modes
A unit whose input is always negative gets zero gradient and stops learning ("dead" ReLU) **[unverified, not stated in the sources]**.

## Where it appears
- [[AlexNet (Krizhevsky 2012)]], [[U-Net paper (Ronneberger 2015)]], [[GAN paper (Goodfellow 2014)]], [[FNO (Li 2021)]] (activation in the Fourier layers).

**Sources**: `papers/ML/Krizhevsky et al - ImageNet Classification with Deep Convolutional Neural Networks.pdf`, `papers/Diffusion/Ronneberger, Fischer, Brox - U-Net Convolutional Networks for Biomedical Image Segmentation.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Convolutional neural network]] · [[Dropout]] · [[Weight initialization]] · [[Glorot init (Glorot 2010)]] · [[ResNet]]
