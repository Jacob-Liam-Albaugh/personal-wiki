---
type: paper
area: stochastic
areas: [stochastic, ml]
source-ref: "Ho, Salimans 2022, arXiv:2207.12598v1, eqs. 1-6, Alg. 1-2, Tables 1-2"
tags: [diffusion, generative, ml]
authors: [Ho, Salimans]
year: 2022
venue: "arXiv:2207.12598v1 (26 Jul 2022); short version at NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications"
file: "Diffusion/Ho, Salimans - Classifier-Free Diffusion Guidance.pdf"
---

# Classifier-Free Diffusion Guidance (Ho 2022)

**Summary**: [[Classifier guidance]] (Dhariwal-Nichol) trades sample diversity for fidelity in conditional [[Diffusion models]] but needs a separate classifier trained on noisy data. Ho and Salimans train one network on both the conditional and the unconditional task (by dropping the label with probability $p_\text{uncond}$) and sample from the extrapolation $(1+w)\epsilon_\theta(z,c)-w\,\epsilon_\theta(z)$, which gives a similar FID/IS trade-off with no classifier ([[Classifier-free guidance]]). The cost is two network evaluations per sampling step.

**Authors**: Jonathan Ho, Tim Salimans (Google Research, Brain team) · **Year**: 2022 · **File**: `Diffusion/Ho, Salimans - Classifier-Free Diffusion Guidance.pdf`

---

## Problem

Truncation in BigGAN and low-temperature sampling in Glow trade diversity for per-sample quality. In diffusion models the obvious analogues (scaling the scores, shrinking the sampling noise) give blurry, low-quality samples (source: Ho, Salimans, p. 1 and §3, p. 3, citing Dhariwal-Nichol).

[[Classifier guidance]] fixes this but has three drawbacks the paper names (source: §1, p. 2):

- It needs an extra classifier, and that classifier must be trained on noisy $z_\lambda$, so an off-the-shelf pre-trained classifier cannot be plugged in.
- Sampling follows classifier gradients, so it can be read as a gradient-based adversarial attack on an image classifier. This raises the question whether the FID and Inception-score (IS) gains come only from being adversarial to classifier-based metrics.
- Stepping along classifier gradients resembles [[GAN]] training, which also does well on those metrics.

Question: can guidance be done with a pure generative model?

## Method

### Setup (§2, p. 2-3)

Continuous-time variance-preserving diffusion indexed by log-SNR $\lambda\in[\lambda_{\min},\lambda_{\max}]$. This is the setting of [[Score SDE (Song 2021)]] and of [[DDPM (Ho 2020)]] with $\epsilon$-prediction; see [[Diffusion models#Reverse-time SDE]].

> [!definition] Forward process (log-SNR parametrisation)
> $$q(z_\lambda\mid x)=\mathcal N(\alpha_\lambda x,\ \sigma_\lambda^2 I),\qquad \alpha_\lambda^2=\frac{1}{1+e^{-\lambda}},\quad \sigma_\lambda^2=1-\alpha_\lambda^2$$
> $\lambda=\log(\alpha_\lambda^2/\sigma_\lambda^2)$ is the log signal-to-noise ratio; the forward process runs in the direction of decreasing $\lambda$.
>
> (source: Ho, Salimans, eq. 1, p. 2; transitions eq. 2, reverse transitions given $x$ eq. 3)

The reverse process starts at $p_\theta(z_{\lambda_{\min}})=\mathcal N(0,I)$ with transitions eq. 4, whose variance is a log-space interpolation $(\tilde\sigma^2_{\lambda'|\lambda})^{1-v}(\sigma^2_{\lambda|\lambda'})^{v}$ with a fixed hyperparameter $v$ (source: eq. 4, p. 2-3, following Nichol-Dhariwal).

> [!definition] Training objective ($\epsilon$-prediction, denoising score matching)
> $$\mathbb E_{\epsilon,\lambda}\big[\,\|\epsilon_\theta(z_\lambda)-\epsilon\|_2^2\,\big],\quad \epsilon\sim\mathcal N(0,I),\ z_\lambda=\alpha_\lambda x+\sigma_\lambda\epsilon,\ \lambda\sim p(\lambda)$$
> with $x_\theta(z_\lambda)=(z_\lambda-\sigma_\lambda\epsilon_\theta(z_\lambda))/\alpha_\lambda$. This is [[Score matching]] (denoising) over many noise scales, so
> $$\epsilon_\theta(z_\lambda)\approx-\sigma_\lambda\nabla_{z_\lambda}\log p(z_\lambda).$$
>
> (source: eq. 5 and the text below it, p. 3)

$p(\lambda)$ is a hyperbolic-secant-like distribution on a bounded interval, $\lambda=-2\log\tan(au+b)$ with $u\sim U[0,1]$, inspired by the cosine schedule (p. 3). Sampling is described as resembling [[Langevin dynamics]] on a sequence of distributions $p(z_\lambda)$ (p. 3). In the conditional case $c$ is an extra input, $\epsilon_\theta(z_\lambda,c)$.

The paper notes that $\epsilon_\theta$ is an unconstrained network, so it need not be a conservative vector field: no scalar potential has to exist whose gradient is $\epsilon_\theta$ (p. 3).

### Classifier guidance as stated (§3.1, p. 3-4)

> [!definition] Classifier guidance (Dhariwal-Nichol, as restated here)
> $$\tilde\epsilon_\theta(z_\lambda,c)=\epsilon_\theta(z_\lambda,c)-w\,\sigma_\lambda\nabla_{z_\lambda}\log p_\theta(c\mid z_\lambda)\approx-\sigma_\lambda\nabla_{z_\lambda}\big[\log p(z_\lambda\mid c)+w\log p_\theta(c\mid z_\lambda)\big]$$
> so sampling targets approximately
> $$\tilde p_\theta(z_\lambda\mid c)\ \propto\ p_\theta(z_\lambda\mid c)\,p_\theta(c\mid z_\lambda)^{w}.$$
>
> (source: Ho, Salimans, unnumbered display, p. 4, §3.1)

Effect: data that the classifier $p_\theta(c\mid z_\lambda)$ labels correctly with high confidence is up-weighted, which raises IS and lowers diversity. Fig. 2 (p. 2, and discussion p. 4) shows a toy mixture of three 2-D Gaussians: as $w$ grows each guided conditional becomes non-Gaussian, moves away from the other classes, and concentrates in a smaller region.

Equivalence remark (p. 4): guidance with weight $w+1$ on an unconditional model targets the same density as weight $w$ on a conditional model, since $p(z\mid c)\,p(c\mid z)^{w}\propto p(z)\,p(c\mid z)^{w+1}$. Dhariwal-Nichol got their best results with the conditional model, so the paper stays in that setup.

### Classifier-free guidance (§3.2, p. 4-5)

> [!algorithm] Joint training with classifier-free guidance (Alg. 1)
> Require $p_\text{uncond}$. Repeat:
> 1. $(x,c)\sim p(x,c)$
> 2. $c\leftarrow\varnothing$ with probability $p_\text{uncond}$ (randomly discard conditioning)
> 3. $\lambda\sim p(\lambda)$, $\epsilon\sim\mathcal N(0,I)$, $z_\lambda=\alpha_\lambda x+\sigma_\lambda\epsilon$
> 4. gradient step on $\nabla_\theta\|\epsilon_\theta(z_\lambda,c)-\epsilon\|_2^2$
>
> One network represents both models: $\epsilon_\theta(z_\lambda)=\epsilon_\theta(z_\lambda,c=\varnothing)$.
>
> (source: Ho, Salimans, Alg. 1, p. 4)

> [!definition] Classifier-free guided score
> $$\tilde\epsilon_\theta(z_\lambda,c)=(1+w)\,\epsilon_\theta(z_\lambda,c)-w\,\epsilon_\theta(z_\lambda)$$
> $w=0$ is the non-guided conditional model; $w>0$ extrapolates away from the unconditional score.
>
> (source: Ho, Salimans, eq. 6, p. 5)

> [!algorithm] Conditional sampling with classifier-free guidance (Alg. 2)
> Require $w$, $c$, increasing $\lambda_1=\lambda_{\min}<\dots<\lambda_T=\lambda_{\max}$. $z_1\sim\mathcal N(0,I)$. For $t=1..T$:
> 1. $\tilde\epsilon_t=(1+w)\epsilon_\theta(z_t,c)-w\,\epsilon_\theta(z_t)$
> 2. $\tilde x_t=(z_t-\sigma_{\lambda_t}\tilde\epsilon_t)/\alpha_{\lambda_t}$
> 3. $z_{t+1}\sim\mathcal N\big(\tilde\mu_{\lambda_{t+1}|\lambda_t}(z_t,\tilde x_t),\ (\tilde\sigma^2_{\lambda_{t+1}|\lambda_t})^{1-v}(\sigma^2_{\lambda_t|\lambda_{t+1}})^{v}\big)$ if $t<T$, else $z_{t+1}=\tilde x_t$.
>
> Return $z_{T+1}$. The paper notes step 2-3 "could be replaced by another sampler, e.g. DDIM" ([[DDIM (Song 2021)]]; see [[Diffusion models#Probability-flow ODE]]).
>
> (source: Ho, Salimans, Alg. 2, p. 5)

### Implicit-classifier interpretation (p. 5)

> [!theorem] Implicit classifier (heuristic motivation, not a guarantee)
> Define the implicit classifier $p^i(c\mid z_\lambda)\propto p(z_\lambda\mid c)/p(z_\lambda)$. With the exact scores $\epsilon^*(z_\lambda,c)$ and $\epsilon^*(z_\lambda)$,
> $$\nabla_{z_\lambda}\log p^i(c\mid z_\lambda)=-\frac{1}{\sigma_\lambda}\big[\epsilon^*(z_\lambda,c)-\epsilon^*(z_\lambda)\big],$$
> and classifier guidance with this classifier gives $\tilde\epsilon^*(z_\lambda,c)=(1+w)\epsilon^*(z_\lambda,c)-w\,\epsilon^*(z_\lambda)$, which has the form of eq. 6.
>
> (source: Ho, Salimans, p. 5, §3.2, text between eq. 6 and §4)

The authors stress the difference: eq. 6 uses the network estimates $\epsilon_\theta$, whose difference $\epsilon_\theta(z_\lambda,c)-\epsilon_\theta(z_\lambda)$ is in general not the gradient of any classifier because the networks are not conservative fields. They also warn that Bayes-inverting a generative model need not give a good classifier: Grandvalet-Bengio find discriminative models usually beat classifiers derived from generative ones even when the generative model is correctly specified, and under misspecification Bayes classifiers can be inconsistent (Grunwald-Langford), so "we lose all guarantees on their performance" (p. 5). The justification is empirical (Section 4).

Wiki note: the intuition in the Discussion (p. 9) is that guidance "decreases the unconditional likelihood of the sample while increasing the conditional likelihood", via a negative score term.

### Choices fixed in the paper

- One network for both tasks; chosen for simplicity, no extra parameters (p. 5).
- Experiments reuse the Dhariwal-Nichol ADM architecture and hyperparameters (tuned for classifier guidance, so possibly suboptimal here), trained in continuous time (p. 6).
- $\lambda_{\min}=-20$, $\lambda_{\max}=20$. 64x64: $v=0.3$, 400k steps; 128x128: $v=0.2$, 2.7M steps (p. 7).

## Results

Class-conditional ImageNet, area-downsampled to 64x64 and 128x128. FID and IS on 50,000 samples, $w\in\{0,0.1,\dots,4\}$ (source: §4.1, p. 7). The experiments are described as "a proof of concept", not an attempt at state of the art (p. 5-6).

**Main claim (p. 7)**: best FID at small guidance ($w=0.1$ or $0.3$, depending on dataset), best IS at strong guidance ($w\ge4$), and a clear trade-off in between. The text says "FID monotonically decreasing and IS monotonically increasing with $w$" between the two extremes; in the tables FID falls to its minimum and then rises with $w$ while IS keeps rising, so the monotone statement should be read as "FID and IS trade off".

**Table 1, ImageNet 64x64 (p. 7), columns are $p_\text{uncond}=0.1/0.2/0.5$**, FID (lower better) / IS (higher better):

| Model | FID | IS |
|---|---|---|
| ADM (Dhariwal-Nichol) | 2.07 | - |
| CDM (Ho et al. 2021) | 1.48 | 67.95 |
| Ours, $w=0$ | 1.8 / 1.8 / 2.21 | 53.71 / 52.9 / 47.61 |
| Ours, $w=0.1$ | 1.55 / 1.62 / 1.91 | 66.11 / 64.58 / 56.1 |
| Ours, $w=0.3$ | 3.03 / 2.93 / 2.65 | 92.8 / 88.64 / 74.92 |
| Ours, $w=1.0$ | 12.6 / 11.21 / 9.13 | 170.1 / 158.29 / 131.1 |
| Ours, $w=2.0$ | 21.03 / 18.79 / 16.16 | 225.5 / 212.98 / 183 |
| Ours, $w=4.0$ | 26.22 / 23.84 / 21.48 | 260.2 / 248.97 / 225.1 |

For $p_\text{uncond}=0.1$ the best FID is 1.55 at $w=0.1$ and IS grows from 53.71 ($w=0$) to 260.2 ($w=4$) while FID grows to 26.22.

**Table 2, ImageNet 128x128 (p. 8), columns are $T=128/256/1024$ sampling steps**:

| Model | FID | IS |
|---|---|---|
| BigGAN-deep, max IS | 25 | 253 |
| BigGAN-deep | 5.7 | 124.5 |
| CDM | 3.52 | 128.8 |
| LOGAN | 3.36 | 148.2 |
| ADM-G | 2.97 | - |
| Ours, $w=0$ | 8.11 / 7.27 / 7.22 | 81.46 / 82.45 / 81.54 |
| Ours, $w=0.3$ | 3.04 / 2.43 / 2.43 | 156.09 / 158.47 / 156 |
| Ours, $w=0.4$ | 3.02 / 2.49 / 2.48 | 183.01 / 183.41 / 180.88 |
| Ours, $w=1.0$ | 7.88 / 7.86 / 7.8 | 295.29 / 297.98 / 294.56 |
| Ours, $w=4.0$ | 21.55 / 21.53 / 21.45 | 422.29 / 421.03 / 419.06 |

Claims in the text (p. 7): the 128x128 results are "the state of the art in the literature"; at $w=0.3$ the FID beats classifier-guided ADM-G (2.43 vs 2.97 at $T=256$); at $w=4.0$ the model beats BigGAN-deep evaluated at its best-IS truncation, on both FID and IS (21.53 / 421.03 vs 25 / 253).

**Effect of $p_\text{uncond}$ (§4.2, p. 8)**: $p_\text{uncond}=0.5$ is consistently worse than $\{0.1,0.2\}$ across the IS/FID frontier; 0.1 and 0.2 are about equal. Conclusion: only a small share of model capacity needs to go to the unconditional task. The paper notes Dhariwal-Nichol likewise found small classifiers sufficient.

**Effect of sampling steps (§4.3, p. 8)**: quality improves with $T\in\{128,256,1024\}$; $T=256$ is a good balance. $T=256$ is about the number of steps ADM-G uses, but each step here costs two network evaluations, so the speed-fair comparison is $T=128$, which has a worse FID than ADM-G (e.g. 3.02-3.04 at best versus 2.97, and 8.11 at $w=0$).

**Qualitative (Figs. 1, 3, 6-8)**: higher $w$ lowers variety and raises per-sample fidelity; strongly guided samples show saturated colours (Fig. 3, p. 6).

## Limitations

As stated by the authors (§5, p. 9):

- **Sampling cost**: each step needs two forward passes (conditional and unconditional). Classifiers can be smaller and faster than the generative model, so classifier guidance may be faster. Injecting the conditioning late in the network might reduce this; left as future work.
- **Needs a trained unconditional model.** If there are few classes and the class prior is known, $\sum_c p(x\mid c)p(c)=p(x)$ gives the unconditional score from conditional ones, but this needs one pass per class value and is inefficient for high-dimensional conditioning.
- **Diversity**: any method trading diversity for fidelity must ask whether lower diversity is acceptable; underrepresented parts of the data may suffer in deployed models. Boosting quality while keeping diversity is left open.
- **No guarantee** that the implicit classifier is a good classifier (p. 5).
- Hyperparameters were inherited from classifier-guidance models and may be suboptimal (p. 6).

Wiki notes:

- Only class-conditional ImageNet at 64x64 and 128x128 is tested; the paper's own closing line asks for "a wider variety of settings and data modalities" (p. 10).
- Fig. 5's legend (p. 9) lists $T=512$ while Table 2 and §4.3 use $T=1024$; the text and table agree with each other, so this looks like a figure-label inconsistency.
- Later literature often writes the guided score as $\epsilon_\theta(z)+s\,(\epsilon_\theta(z,c)-\epsilon_\theta(z))$ with $s=1+w$. This is **[unverified]** here (not from this paper); with the paper's convention $w=0$ means no guidance.

## Connections

- **Builds on**: [[Classifier guidance]] (Dhariwal-Nichol 2021, not in the wiki; restated on p. 3-4), the continuous-time diffusion framework of [[Score SDE (Song 2021)]], the $\epsilon$-prediction objective of [[DDPM (Ho 2020)]], and [[Score matching]] in its denoising form.
- **Sampler-agnostic**: Alg. 2 explicitly allows replacing the ancestral step with DDIM ([[DDIM (Song 2021)]]).
- **Compared with GANs**: truncation in BigGAN is the analogy; the paper beats BigGAN-deep at both FID and IS at $w=4$ ([[GAN]]).
- **Conditional sampling in other forms**: [[Diffusion posterior sampling]] steers an unconditional diffusion model with a likelihood gradient at sampling time (classifier-guidance-like, needs a differentiable forward model); classifier-free guidance instead bakes the conditional score into the network. Wiki note: this comparison is the wiki's, not the paper's.

**Sources**: `Diffusion/Ho, Salimans - Classifier-Free Diffusion Guidance.pdf`.
**Last updated**: 2026-11-06

---

## Related pages
- [[Classifier-free guidance]]
- [[Classifier guidance]]
- [[Diffusion models]]
- [[Score matching]]
- [[Score SDE (Song 2021)]]
- [[DDPM (Ho 2020)]]
- [[DDIM (Song 2021)]]
- [[Diffusion posterior sampling]]
- [[Langevin dynamics]]
- [[GAN]]
- [[CLIP (Radford 2021)]]
