---
type: paper
area: ml
areas: [ml]
source-ref: "Radford et al. 2021, ICML (PMLR 139), Fig. 3 pseudocode, §2.1-2.5, §3.1-3.4, §6; supplementary Apps. A-I"
tags: [ml, generative]
authors: ["[[Alec Radford]]", "[[Jong Wook Kim]]", "[[Chris Hallacy]]", "[[Aditya Ramesh]]", "[[Gabriel Goh]]", "[[Sandhini Agarwal]]", "[[Girish Sastry]]", "[[Amanda Askell]]", "[[Pamela Mishkin]]", "[[Jack Clark]]", "[[Gretchen Krueger]]", "[[Ilya Sutskever]]"]
year: 2021
venue: "ICML 2021 (PMLR 139)"
file: "papers/Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP).pdf"
file-supplementary: "papers/Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP) - Supplementary.pdf"
---

# CLIP: Learning Transferable Visual Models From Natural Language Supervision (Radford 2021)

**Summary**: CLIP trains an image encoder and a text encoder jointly on 400 million (image, text) pairs from the internet to pick out which caption goes with which image in a batch, a symmetric InfoNCE-style loss ([[Contrastive learning]]). At test time the class names, wrapped in prompts, are embedded by the text encoder to form a linear classifier, which gives [[Zero-shot transfer]] to over 30 datasets. The best model reaches 76.2% zero-shot top-1 on ImageNet, matching the original ResNet50 without using any of its 1.28M labelled images.

**Authors**: Alec Radford, Jong Wook Kim (equal contribution), Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever (OpenAI) · **Year**: 2021 · **File**: `papers/Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP).pdf` · **Supplementary**: `papers/Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP) - Supplementary.pdf`

**What the two files are.** The main file is the ICML 2021 camera-ready version (9 pages of text, then references; p. 1 carries the PMLR 139 footer). It is a condensed paper: it has no section on prompt engineering and no per-dataset tables. The "Supplementary" file is the appendix of that version, not the full arXiv version: it has no abstract or body, starts at "A. Linear-probe evaluation" (supp. p. 1), and runs to supp. p. 25 with Apps. A-I (linear-probe details, zero-shot analysis including prompt engineering, data overlap, robustness, broader impacts, human comparison, YFCC100M ablation, selected tasks, hyperparameters). Citations below are "main p. N" and "supp. p. N". The main paper has no numbered equations, so the key formula is the Fig. 3 pseudocode (main p. 3).

---

## Problem

State-of-the-art vision systems predict a fixed set of predetermined categories, so a new concept needs new labelled data (abstract, main p. 1). NLP had moved to web-scale pre-training with a text-to-text interface that transfers zero-shot (GPT-3), while vision still pre-trained on crowd-labelled sets such as ImageNet (main p. 1). Earlier work on learning from text paired with images (Joulin et al. 2016; Li et al. 2017; VirTex; ICMLM; ConVIRT) trained for accelerator days on 100-200 thousand images and lagged behind Big Transfer and weakly supervised ResNeXt, which trained for accelerator years on millions to billions of images. "A crucial difference is scale" (main p. 1). The paper asks what natural-language supervision gives at that scale.

## Method

### Dataset: WIT (main §2.1, p. 2)

- Existing sets are small or noisy: MS-COCO and Visual Genome have about 100,000 training photos each; YFCC100M has 100M photos but after keeping only images with English natural-language titles/descriptions it shrinks by a factor of 6 to 15 million, about the size of ImageNet.
- The authors built **WIT** (WebImageText): 400 million (image, text) pairs from publicly available internet sources. Pairs were found by searching for text containing one of 500,000 queries, with up to 20,000 pairs per query to approximately class-balance. The total word count is similar to the WebText set used for GPT-2.
- Query list (footnote 1): all words occurring at least 100 times in English Wikipedia, plus high-pointwise-mutual-information bigrams, plus names of Wikipedia articles above a search-volume threshold, plus all WordNet synsets not already included.
- The dataset is not released; code and model weights are (abstract).

### Why a contrastive objective (main §2.2, p. 2-3, Fig. 2)

A transformer language model that predicts the caption (63M parameters, already twice the compute of its ResNet50 image encoder) learned to recognise ImageNet classes three times slower than a bag-of-words prediction baseline (Joulin et al.). Swapping the bag-of-words prediction objective for the contrastive objective gave a further 4x efficiency gain in zero-shot ImageNet accuracy per image processed (Fig. 2, main p. 3). The motivation is that predicting which text as a whole goes with which image is an easier proxy task than predicting the exact words.

### Objective (main §2.2, p. 3; Fig. 3)

> [!algorithm] CLIP contrastive pre-training (symmetric loss over an $N\times N$ similarity matrix)
> Given a batch of $N$ aligned (image, text) pairs, learn encoders so that the $N$ true pairs have high cosine similarity and the $N^2-N$ other pairings low. Pseudocode (verbatim logic):
> ```
> I_f = image_encoder(I)          # [n, d_i]
> T_f = text_encoder(T)           # [n, d_t]
> I_e = l2_normalize(I_f @ W_i)   # [n, d_e]
> T_e = l2_normalize(T_f @ W_t)   # [n, d_e]
> logits = (I_e @ T_e.T) * exp(t) # [n, n]
> labels = arange(n)
> loss_i = cross_entropy(logits, labels, axis=0)
> loss_t = cross_entropy(logits, labels, axis=1)
> loss = (loss_i + loss_t) / 2
> ```
> $W_i, W_t$ are learned linear projections; $t$ is a learned temperature parameter.
>
> (source: Radford et al., Fig. 3, main p. 3)

Wiki note (not in the paper): writing $s_{ij}=e^{t}\,\langle I_{e,i},T_{e,j}\rangle$, the pseudocode computes
$$\mathcal L=\tfrac12\Big[-\tfrac1N\sum_i\log\frac{e^{s_{ii}}}{\sum_j e^{s_{ij}}}\;-\;\tfrac1N\sum_j\log\frac{e^{s_{jj}}}{\sum_i e^{s_{ij}}}\Big],$$
two cross-entropies with the diagonal as the correct class, one over rows and one over columns. The other $N-1$ items in the batch serve as negatives.

Further details stated in the text (main p. 3):

- The batch construction and objective were first introduced as the multi-class N-pair loss (Sohn 2016) and adapted to (text, image) pairs in medical imaging by ConVIRT (Zhang et al. 2020).
- Simplifications versus ConVIRT: trained from scratch (no pre-trained weights); only a linear projection from each encoder's representation to the shared space (no non-linear projection); no text sampling function $t_u$ (most pairs are one sentence); image augmentation is only a random square crop. "Over-fitting is not a major concern".
- The temperature $\tau$ is optimised directly as a log-parameterised multiplicative scalar, not tuned as a hyperparameter. In the pseudocode $\exp(t)$ multiplies the logits. Table 18 (supp. p. 25) lists "Maximum temperature 100.0"; Wiki note: this reads as an upper cap on the logit multiplier $e^{t}$ (**[unverified]**, the file does not define it further).

### Encoders (main §2.3-2.4, p. 3-4)

- **Image encoder, option 1**: ResNet50 with ResNetD changes (He et al. 2019), antialiased rect-2 blur pooling (Zhang 2019), and global average pooling replaced by attention pooling (one layer of multi-head QKV attention whose query is the global average-pooled image representation).
- **Image encoder, option 2**: Vision Transformer (Dosovitskiy et al. 2020), with an extra layer norm on the combined patch and position embeddings and a slightly different initialisation.
- **Text encoder**: Transformer (Vaswani et al.) with the GPT-2 modifications; base size 12 layers, 512 wide, 8 heads; lower-cased byte-pair encoding with [SOS] and [EOS] tokens; the top-layer activation at [EOS] is layer-normalised and linearly projected into the joint space. Masked self-attention is used so that a language-modelling auxiliary loss could be added later (not explored).
- **Scaling**: ResNets scale width, depth and resolution together (EfficientNet-style); the text encoder scales only width, in proportion to the ResNet width, because CLIP was less sensitive to it.
- **Models trained**: 5 ResNets (RN50, RN101, RN50x4, x16, x64 at about 4x, 16x, 64x the compute of RN50) and 3 ViTs (B/32, B/16, L/14). RN50x64 took 18 days on 592 V100 GPUs; the largest ViT took 12 days on 256 V100 GPUs. ViT-L/14 was also trained one extra epoch at 336 px (ViT-L/14@336px); "CLIP" in the paper means that model unless stated.
- **Hyperparameters (supp. p. 25, Tables 18-20)**: batch size 32,768, 32 epochs, vocabulary 49,408, weight decay 0.2, 2000 warm-up iterations, Adam $\beta_1=0.9$, $\beta_2=0.999$ (ResNet) or $0.98$ (ViT); embedding dimension 1024/512/640/768/1024 for RN50/101/x4/x16/x64 and 512/512/768/768 for the ViTs; learning rate $5\times10^{-4}$ for the smaller models down to $2\times10^{-5}$ for ViT-L/14@336px.

### Using CLIP for zero-shot classification (main §2.5, p. 4; Fig. 1)

> [!algorithm] Zero-shot classifier from class names
> For a dataset with classes $c_1,\dots,c_K$: embed the text for each class (e.g. "A photo of a {object}.") with the text encoder to get $T_1,\dots,T_K$; embed the image to get $I$; predict the class with the largest (scaled, normalised) $I\cdot T_k$. The text encoder acts as a hypernetwork that synthesises a linear classifier from natural language.
>
> (source: Radford et al., Fig. 1 and §2.5, main p. 2 and 4; wording "linear classifier" from Fig. 1 caption and supp. p. 9)

The authors frame zero-shot transfer as measuring **task-learning** ability, as opposed to the representation learning measured by linear probes (main p. 4-5). They use "zero-shot" in a broader sense than unseen classes: generalisation to unseen *datasets*, a proxy for unseen tasks (main §3.2, p. 5).

### Prompt engineering and ensembling (supp. App. B, p. 9)

(The main text only mentions that prompts and ensembles are used, p. 4.)

- Class names alone are ambiguous (polysemy: ImageNet has both construction cranes and cranes that fly; "boxer" in Oxford Pets is a dog breed, but a text encoder alone cannot tell) and unlike pre-training text, which is usually a full sentence (supp. p. 9).
- Default template "A photo of a {label}." improves ImageNet accuracy by 1.3% over the bare label.
- Task-specific prompts: "A photo of a {label}, a type of pet." (Oxford Pets); similar category hints for Food101 and FGVC Aircraft; quotes around the text for OCR datasets; "a satellite photo of a {label}." for satellite datasets.
- **Ensembling** (e.g. "A photo of a big {label}" and "A photo of a small {label}") is done **in embedding space, not probability space**, so one averaged set of text embeddings is cached and the cost equals that of a single classifier when amortised over many predictions.
- On ImageNet an ensemble of 80 context prompts gives an additional 3.5% over the default single prompt; together prompt engineering and ensembling improve ImageNet accuracy by almost 5%.
- Across 36 datasets the average gain is almost 5 points, about the gain from 4x more compute with the contextless baseline, but "free" when amortised (Fig. 13, supp. p. 9).
- Some datasets (Flowers102, GTSRB) shipped without a class-name mapping, which prevents zero-shot transfer entirely (supp. p. 9).

## Results

### Zero-shot (main §3.1-3.2, p. 4-6; supp. App. B)

- **Versus Visual N-Grams** (Table 1, main p. 4), accuracy:

| | aYahoo | ImageNet | SUN |
|---|---|---|---|
| Visual N-Grams | 72.4 | 11.5 | 23.0 |
| CLIP | 98.4 | 76.2 | 58.5 |

- **ImageNet**: 76.2% top-1, matching the original ResNet50, with no use of its 1.28M labels; top-5 is 95%, matching Inception-V4 (main p. 4). Table 4 (supp. p. 8) gives zero-shot ImageNet for each model, from 59.6 (RN50) through 73.6 (RN50x64) and 75.3 (ViT-L/14) to 76.2 (ViT-L/14@336px). The authors caution that the Visual N-Grams comparison mixes many uncontrolled differences; a CLIP ResNet50 trained on YFCC100M, the data Visual N-Grams used, matched its ImageNet result within a V100 GPU day (main p. 4).
- **Versus a supervised linear probe on ResNet50 features** (Fig. 4, main p. 5, 27 datasets): zero-shot CLIP wins on 16 of 27, including ImageNet, "slightly" on average. Largest gain is STL10 (99.3%, apparently a new SOTA, with zero training examples). On Stanford Cars and Food101 it is better by over 20%; on Flowers102 and FGVCAircraft worse by over 10%. On Kinetics700 it is 14.5% better and on UCF101 7.7% better; the authors speculate language gives wider supervision for verbs than noun-centric ImageNet.
- **Weak tasks**: satellite imagery (EuroSAT, RESISC45), lymph-node tumour detection (PatchCamelyon), counting (CLEVRCounts), German traffic signs (GTSRB), distance to nearest car (KITTI Distance). Non-expert humans do several of these well; the authors question whether zero-shot (as opposed to few-shot) is a fair test for tasks a learner has no prior for (main p. 5).
- **Versus few-shot** (Fig. 5, main p. 6): zero-shot CLIP matches the average of a 4-shot logistic-regression classifier on the same features, and roughly matches the best 16-shot classifier among public models (BiT-M ResNet152x2 on ImageNet-21K features), on the 20 datasets with at least 16 examples per class. Explanation offered: natural language communicates the concept directly, while examples leave the hypothesis underdetermined (especially one-shot).
- **Data efficiency per dataset** (supp. Fig. 14, p. 10): the number of labelled examples per class a linear probe on CLIP features needs to match zero-shot ranges from under 1 to 184; median 5.4, mean 20.8; Flowers102 and EuroSAT zero-shot is below one-shot. On ImageNet zero-shot matches a 16-shot linear classifier.
- **Zero-shot versus linear-probe performance** (supp. Fig. 15, p. 10): correlation 0.82 ($p<10^{-6}$); zero-shot is mostly 10 to 25 points lower; it comes within 3 points on only 5 datasets (STL10, CIFAR10, Food101, OxfordPets, Caltech101), all over 90% in both settings. Regression slope 1.28 (95% CI 0.93-1.79).
- **Scaling** (supp. Fig. 16, p. 11): average zero-shot error is well modelled by a log-log linear trend over a 44x range of compute (5 ResNet CLIP models, 39 evals on 36 datasets); individual evals are much noisier.

### Linear probe / representation learning (main §3.3, p. 6-7; supp. App. A)

- **Protocol** (supp. A.3, p. 2): features from the penultimate layer (for CLIP-ViT, before the projection, i.e. $I_f$ in Fig. 3); logistic regression (scikit-learn L-BFGS, up to 1000 iterations); L2 strength swept from $10^{-6}$ to $10^{6}$ on validation splits with a parametric binary search down to 8 steps per decade.
- **Kornblith et al. 12-dataset suite** (Fig. 6 left, main p. 7): CLIP scales well with compute; the largest model slightly beats Noisy Student EfficientNet-L2 in score and compute efficiency; CLIP ViTs are about 3x more compute-efficient than CLIP ResNets; ViT-L/14@336px beats the best existing model by an average of 2.6%.
- **27-dataset suite** (Fig. 6 right): all CLIP models, at any scale, beat all evaluated systems on compute efficiency, and the best model's average lead grows from 2.6% to 5%. The extra datasets cover OCR, geo-localisation, facial emotion, action recognition (the authors argue Kornblith's suite is biased towards tasks overlapping with ImageNet).
- **Per dataset** (supp. A.4, p. 2-5, Tables 3, Figs. 9-10): ViT-L/14@336px is state of the art on 21 of 27 datasets (within the Clopper-Pearson 99.5% interval of the best) and beats Noisy Student EfficientNet-L2 on 21 of 27. Biggest gains are on OCR (SST2, HatefulMemes), geo-localisation and scenes (Country211, SUN397), video activity (Kinetics700, UCF101), Stanford Cars and GTSRB. ImageNet linear-probe accuracy for ViT-L/14@336px is 85.4% (Table 3); EfficientNet-L2 is better on ImageNet, CIFAR10/100, PatchCamelyon, CLEVRCounts. The authors suspect the lack of scale augmentation in CLIP for the CIFAR gap, and suggest ImageNet's single label for all traffic signs may explain part of the GTSRB gain.

### Robustness to natural distribution shift (main §3.4, p. 6-8; supp. App. D)

- Setup follows Taori et al. (2020): accuracy on 7 natural shifts of ImageNet is a roughly linear function of logit-transformed ImageNet accuracy for standard models; **effective robustness** is accuracy above that line, **relative robustness** is any improvement in shifted accuracy. The hypothesis: a zero-shot model cannot exploit spurious correlations specific to ImageNet's training distribution (main p. 7).
- Result (Fig. 7, main p. 8): all zero-shot CLIP models raise effective robustness by a large amount and shrink the ImageNet-to-shift gap by up to 75%. They lie on "a completely distinct robustness frontier" from all 204 models in Taori et al.
- Banana example against a ResNet101 with the same ImageNet accuracy (76.2%): ImageNetV2 70.1 vs 64.3 (+5.8), ImageNet-R 88.9 vs 37.7 (+51.2), ObjectNet 72.3 vs 32.6 (+39.7), ImageNet Sketch 60.2 vs 25.2 (+35.0), ImageNet-A 77.1 vs 2.7 (+74.4) (Fig. 7 right; the zero-shot CLIP number is first).
- **Supervised adaptation removes most of the effect** (supp. App. D, p. 12-14; Fig. 18 on p. 13): an L2-regularised logistic regression on CLIP features using the ImageNet training set raises ImageNet accuracy by 9.2% to 85.4% (matching the 2018 SOTA of Mahajan et al.), but average shifted accuracy slightly decreases: -4.7 on ImageNet-R, -3.8 ObjectNet, -2.8 Sketch, -1.9 ImageNet-A, +9.2 on the distribution closest to ImageNet's collection process (ImageNetV2). The authors say they have no confident explanation (Fig. 18). Few-shot CLIP also shows elevated effective robustness that fades as more training data is used (Fig. 19); zero-shot is more robust than a few-shot model with the same ImageNet accuracy. Pattern: high effective robustness comes with minimising distribution-specific training data, at a cost in in-distribution accuracy (supp. p. 14).
- Per-dataset zero-shot class names (instead of max-pooling over ImageNet classes) raise average effective robustness by about 5%, concentrated on a few datasets (supp. p. 14).

### Data overlap (main §4, p. 8; supp. App. C, p. 11-12)

Of 35 datasets, 9 have no detected overlap; median overlap 2.2%, mean 3.2%. Accuracy shifts by more than 0.1% on only 7 datasets, and only 2 are significant after Bonferroni correction; the largest gain is 0.6% on Birdsnap. Country211 has the largest overlap (21.5%, built from YFCC100M) but gains only 0.2%. The detector's recall cannot be checked over 400M examples, and the overlap and clean subsets may differ in distribution (supp. p. 12).

### Dataset ablation (supp. App. G, p. 20)

A model trained on a filtered YFCC100M subset versus an equal-size WIT subset (32 epochs) performs similarly on average in both zero-shot and linear-probe settings, with differences on specific fine-grained datasets (supp. p. 20).

### Broader impacts (main §5, p. 8; supp. App. E)

- With Fairface race labels plus egregious terms such as "criminal" and "animal", the model classified images of people aged 0-20 into the egregious category 32.3% of the time; adding the class "child" reduced this to 8.7%. Disparities across gender and race were also found, so class design matters but does not remove disparate impact.
- Celebrity identification (CelebA, "in the wild"): top-1 59.2% from 100 candidates, 43.3% from 1000; not competitive with production models.

## Limitations

As stated by the authors (main §6, p. 8-9, and supp.):

- **Performance ceiling**: zero-shot CLIP is often only competitive with a linear classifier on ResNet-50 features, which is well below overall SOTA. They estimate about a **1000x increase in compute** would be needed for zero-shot CLIP to reach overall SOTA on their suite, infeasible with current hardware.
- **Hard tasks**: poor on specialised, complex or abstract tasks (satellite imagery, tumour detection, counting, traffic signs, distance to car).
- **Unrealistic evaluation**: validation sets were repeatedly queried to guide development, which is not true zero-shot; the main 27-dataset suite is "somewhat haphazard" and "undeniably co-adapted with the capabilities of CLIP". A benchmark designed for broad zero-shot transfer is needed.
- **Interface**: natural language is flexible but many complex tasks are hard to specify in text; CLIP does not optimise few-shot performance, so falling back to linear probes causes a counter-intuitive *drop* when going from zero-shot to few-shot.
- **Dependence on label wording**: needs prompt engineering; class-name polysemy; some datasets have no names at all (supp. p. 9).
- Data overlap analysis has imperfect recall (supp. p. 12). Social-bias and surveillance risks (above).

Wiki notes (not stated in the paper): the 400M-pair WIT set is not released, so the training results cannot be reproduced directly; and CLIP gives a similarity score between an image and a text, not a generative model of either.

## Connections

- **Objective**: a symmetric InfoNCE / N-pair loss with learned temperature; see [[Contrastive learning]]. Wiki note: the link between the cross-entropy over the batch and a lower bound on mutual information is standard but is not discussed in this paper.
- **Zero-shot transfer** as a measure of task learning and the prompt-based interface are covered in [[Zero-shot transfer]].
- **With diffusion models**: CLIP's text/image embeddings are widely used as the conditioning signal for text-to-image [[Diffusion models]], where [[Classifier-free guidance]] ([[Classifier-free guidance (Ho 2022)]]) supplies the fidelity/diversity trade-off. This is Wiki knowledge, **[unverified]** from the files here: neither CLIP paper discusses diffusion.
- **Compare**: classifier guidance ([[Classifier guidance]]) could in principle use a CLIP-style scoring model as the guiding "classifier"; **[unverified]**, not in these files.
- The 1000x-compute estimate and the log-log scaling plot (supp. Fig. 16) put CLIP in the same empirical-scaling tradition as the GPT family (supp. p. 11).


**Sources**: `papers/Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP).pdf` (main), `papers/Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP) - Supplementary.pdf` (appendix of the ICML version).
**Last updated**: 2026-11-06

---

## Related pages
- [[Contrastive learning]]
- [[Zero-shot transfer]]
- [[Classifier-free guidance]]
- [[Classifier guidance]]
- [[Diffusion models]]
- [[Classifier-free guidance (Ho 2022)]]
