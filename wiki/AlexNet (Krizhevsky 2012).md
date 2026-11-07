---
type: paper
area: ml
areas: [ml]
source-ref: "Krizhevsky, Sutskever, Hinton 2012 (CACM 2017 reprint), §4-7, Figs. 1-2, Tables 1-2"
tags: [ml, optimization]
authors: ["[[Alex Krizhevsky]]", "[[Ilya Sutskever]]", "[[Geoffrey Hinton]]"]
year: 2012
venue: "NeurIPS 2012 (reprinted CACM 2017)"
file: "papers/ML/Krizhevsky et al - ImageNet Classification with Deep Convolutional Neural Networks.pdf"
---

# AlexNet (Krizhevsky 2012)

**Summary**: An 8-layer convolutional network (5 convolutional, 3 fully connected; 60M parameters) trained on 1.2M ImageNet images on two GPUs. ReLU units, data augmentation and dropout made training fast and overfitting tolerable. It cut the ILSVRC top-5 error from 26.2% (second place) to 15.3% in 2012.

**Authors**: Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton · **Year**: 2012 · **File**: `papers/ML/Krizhevsky et al - ImageNet Classification with Deep Convolutional Neural Networks.pdf`

---

## Problem

Object recognition needs large labeled datasets and high-capacity models, but the task is too complex for even ImageNet to specify, so the model also needs prior knowledge. [[Convolutional neural network]]s supply it (stationary statistics, local pixel dependencies) with far fewer connections than a dense net, but had been too costly for high-resolution images. GPUs and ImageNet changed that (source: AlexNet.pdf, pp. 1-2).

## Method

### Architecture (§4.5, Fig. 2, pp. 3-4)

Input is a $224\times224\times3$ crop. Layer sizes:
- conv1: 96 kernels $11\times11\times3$, stride 4;
- conv2: 256 kernels $5\times5\times48$;
- conv3: 384 kernels $3\times3\times256$; conv4: 384 kernels $3\times3\times192$; conv5: 256 kernels $3\times3\times192$;
- two dense layers of 4096 units, then a 1000-way softmax trained with the multinomial logistic (cross-entropy) objective.

ReLU follows every conv and dense layer; response normalization follows conv1 and conv2; max pooling follows both of those and conv5. Neuron counts: 290,400-186,624-64,896-64,896-43,264-4096-4096-1000 (Fig. 2 caption). The net is split over two GTX 580 GPUs that communicate only at conv3 and the dense layers (§4.2); this lowered top-1/top-5 error by 1.7%/1.2% against a half-width one-GPU net.

### Ingredients, in the authors' order of importance (§4)

> [!definition] ReLU
> $f(x)=\max(0,x)$. A four-layer CNN reached 25% training error on CIFAR-10 six times faster than with tanh (Fig. 1). See [[ReLU]].
>
> (source: AlexNet.pdf, §4.1, p. 2)

> [!definition] Local response normalization
> With $a^i_{x,y}$ the ReLU output of kernel $i$ at $(x,y)$ and $N$ kernels in the layer:
> $$b^i_{x,y}=a^i_{x,y}\Big/\Big(k+\alpha\sum_{j=\max(0,i-n/2)}^{\min(N-1,i+n/2)}(a^j_{x,y})^2\Big)^{\beta}$$
> with $k=2,\ n=5,\ \alpha=10^{-4},\ \beta=0.75$. Lateral-inhibition style competition across kernels. Lowers top-1/top-5 error by 1.4%/1.2%.
>
> (source: §4.3, p. 3; checked against the page image)

Overlapping pooling ($s=2$, $z=3$ instead of $s=z=2$) lowers errors by 0.4%/0.3% (§4.4, p. 3).

### Reducing overfitting (§5)

- **Data augmentation** (§5.1, pp. 4-5): random $224\times224$ crops and horizontal flips of the $256\times256$ images (factor 2048 more data); at test time average the softmax over 10 patches (4 corners + centre, with flips). A second scheme adds PCA-weighted RGB shifts $[p_1,p_2,p_3][\alpha_1\lambda_1,\alpha_2\lambda_2,\alpha_3\lambda_3]^\top$ with $\alpha_i\sim N(0,0.1^2)$, reducing top-1 error by over 1%.
- **Dropout** (§5.2, p. 5): probability 0.5 on the first two dense layers; test time multiplies outputs by 0.5. Roughly doubles iterations to converge. See [[Dropout]].

### Training (§6, p. 5)

[[SGD]] with batch 128, [[Momentum]] 0.9, weight decay 0.0005 (which lowers training error, so it is not only a regularizer):
$$v_{i+1}=0.9\,v_i-0.0005\,\varepsilon\,w_i-\varepsilon\Big\langle\frac{\partial L}{\partial w}\Big|_{w_i}\Big\rangle_{D_i},\qquad w_{i+1}=w_i+v_{i+1}$$
(p. 6; checked against the page image). Weights drawn from $N(0,0.01^2)$; biases 1 in conv2, conv4, conv5 and the dense hidden layers (positive inputs to ReLUs), 0 elsewhere. Learning rate 0.01, divided by 10 three times when validation error stalled; about 90 epochs, 5-6 days on two GPUs.

## Results

- **ILSVRC-2010 test** (Table 1, p. 5): CNN top-1/top-5 error 37.5%/17.0%, vs sparse coding 47.1%/28.2% and SIFT+Fisher vectors 45.7%/25.7%. Without 10-patch averaging: 39.0%/18.3%.
- **ILSVRC-2012** (Table 2, p. 5): 1 CNN 40.7%/18.2% (val); 5 CNNs 38.1%/16.4%; 7 CNNs with ImageNet-2011 pre-training 15.3% top-5 test, vs 26.2% for the second-best entry.
- **ImageNet Fall 2009** (10,184 classes): 67.4%/40.9% vs previous best 78.1%/60.9% (p. 6).
- **Qualitative** (§7.1, Figs. 3-4, p. 6): conv1 learns frequency- and orientation-selective kernels and colour blobs; the two GPUs specialize (one colour-agnostic, one colour-specific). Nearest neighbours in the 4096-d last hidden layer are semantically similar although far apart in pixel $L_2$.
- **Depth matters**: removing any middle layer costs about 2% top-1 (§8, p. 7).

## Limitations

Stated by the authors: size is capped by GPU memory and training time; no unsupervised pre-training was used though it is expected to help; the network is still far from the human visual pathway; video is the stated next target (p. 7).

Wiki note: the paper reports the ReLU-vs-tanh comparison only on CIFAR-10 (Fig. 1), not on ImageNet itself.

## Connections

- Brings ReLU, augmentation and [[Dropout]] to large scale; [[Dropout paper (Srivastava 2014)]] shares three of the authors and describes the technique this network used.
- Plain SGD with momentum and small Gaussian init; compare [[Glorot init (Glorot 2010)]] and [[Init and momentum (Sutskever 2013)]].
- Directly motivates [[U-Net paper (Ronneberger 2015)]], whose introduction credits this paper for the breakthrough, and the deeper [[ResNet paper (He 2016)]] (the epilogue says later depth cut error a further factor of three).
- The prologue states the "learning beats hand-design given data and compute" thesis behind the ML area.

%% refs:start %%
**Cited by in this wiki**: [[Adam paper (Kingma 2015)]], [[Bayesian DenseED surrogate (Zhu 2018)]], [[Deep Koopman (Lusch 2018)]], [[GAN paper (Goodfellow 2014)]], [[HNNs (Greydanus 2019)]], [[Init and momentum (Sutskever 2013)]], [[LNNs (Cranmer 2020)]], [[Mamba (Gu 2023)]], [[NIF (Pan 2023)]], [[PINNs (Raissi 2019)]], [[ResNet paper (He 2016)]], [[SINDy autoencoders (Champion 2019)]], [[U-Net paper (Ronneberger 2015)]]
%% refs:end %%

**Sources**: `papers/ML/Krizhevsky et al - ImageNet Classification with Deep Convolutional Neural Networks.pdf`.
**Last updated**: 2026-11-07

---

## Related pages
- [[Convolutional neural network]] · [[ReLU]] · [[Dropout]] · [[SGD]] · [[Momentum]] · [[ResNet]] · [[U-Net]]
