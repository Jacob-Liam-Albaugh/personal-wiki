---
type: method
area: stochastic
areas: [stochastic, ml]
source-ref: "Ronneberger et al. 2015, §2-3, Fig. 1; Ho et al. 2020, App. B"
tags: [ml, diffusion]
---

# U-Net

> [!definition] U-Net
> A fully convolutional encoder-decoder with a contracting path (conv, ReLU, $2\times2$ max pool, channels doubled per level), a symmetric expanding path (up-convolution halving channels, concatenation with the same-level encoder map, two convs) and a final $1\times1$ conv to class scores. Original: 23 conv layers, unpadded convolutions with cropped skips.
>
> (source: U-Net.pdf, §2, p. 4)

**Intuition**: pooling gives context but throws away position. The skip connections hand the decoder the high-resolution encoder features, so it can combine "what" from deep layers with "where" from shallow ones. The decoder keeps many channels so context propagates to the high-resolution layers.

## Why it shows up in this wiki

[[DDPM (Ho 2020)]] parameterizes the noise predictor $\epsilon_\theta(x_t,t)$ with a U-Net (PixelCNN++ style: Wide ResNet blocks, group norm, sinusoidal time embedding, self-attention at $16\times16$; 35.7M parameters on CIFAR-10). The input and output have the same shape, which is exactly what the encoder-decoder with skips provides. The same backbone family carries over to [[Score SDE (Song 2021)]] (NCSN++ reuses BigGAN residual blocks, per [[GAN]]) and [[Classifier-free guidance]] models **[unverified for the last]**. See [[Diffusion models]] and [[Score matching]].

## Variants and contrasts
- Padded convolutions and addition instead of crop-and-concatenate are common later; the original uses valid convolutions plus overlap-tile inference with mirrored borders (source: U-Net.pdf, Fig. 2).
- Residual shortcuts ([[ResNet]]) add; U-Net skips concatenate.
- As an operator-learning baseline for PDE solution maps (24.95M parameters in the FNO Navier-Stokes tables), it is less accurate and degrades with resolution; see [[FNO (Li 2021)]].

## Training recipe from the paper
Weighted pixel softmax cross entropy with border weights $w(x)=w_c(x)+w_0\exp(-(d_1+d_2)^2/2\sigma^2)$; elastic-deformation augmentation; batch of one large tile with momentum 0.99; $N(0,2/N)$ init (see [[Weight initialization]]).

## Failure modes
- The unpadded design needs tile sizes with even maps at every pooling step, and output is smaller than input.
- Authors report results on three small datasets only (p. 7).

## Where it appears
- [[U-Net paper (Ronneberger 2015)]]: the architecture itself.
- [[DDPM (Ho 2020)]]: denoiser backbone.
- [[FNO (Li 2021)]], [[Neural operator (Kovachki 2022)]]: baseline.

**Sources**: `papers/Diffusion/Ronneberger, Fischer, Brox - U-Net Convolutional Networks for Biomedical Image Segmentation.pdf`, `papers/Diffusion/Ho, Jain, Abbeel - Denoising Diffusion Probabilistic Models.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Convolutional neural network]] · [[ReLU]] · [[ResNet]] · [[Diffusion models]] · [[DDPM]] · [[Neural operator]]
