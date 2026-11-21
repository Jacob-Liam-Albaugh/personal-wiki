---
type: definition
area: bayesian
areas: [bayesian, ift]
source-ref: "Enßlin, IT & IFT, ch. 2, §2.6-2.8, eqs. 100-113; ch. 3 §3.1"
tags: [bayesian, ift]
---

# Achieved information gain

> [!definition] Achieved information gain (AIG)
> Alice knows $I_A$, Bob updates his knowledge $I_0\to I_B$. Seen from Alice, the gain is
> $$G_S(I_A,I_B,I_0)=\lambda\,D_S(I_A,I_B,I_0)$$
> $$D_S(I_A,I_B,I_0)=\int_S ds\,P(s\mid I_A)\ln\frac{P(s\mid I_B)}{P(s\mid I_0)}$$
> The multiplier $\lambda$ sets the units: nits for $\ln$, bits for $\log_2$. Surprise $H(s\mid I)=-\ln P(s\mid I)$ gives the reading $D_S=\langle H(s\mid I_0)-H(s\mid I_B)\rangle_{(s\mid I_A)}$, the reduction in surprise that Alice expects Bob to feel.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §2.6.1-2.6.2, pp. 43-45; p. is the PDF page)

**Intuition**: how much closer to what Alice knows did a message bring Bob? The "ideal" gain is reached if Bob ends up knowing exactly what Alice knows; the achieved gain is that ideal gain minus what is still missing.

Notation: the book writes $D_\mathcal S$, $\mathcal P$ and $G_\mathcal S$; this page drops the calligraphic letters.

## Derivation from five criteria (§2.6, pp. 42-44)
The gain $G_S(I_A,I_B,I_0)$ should satisfy:
1. **Additivity** over hierarchical knowledge $P(s\mid I_A)=\sum_ip_{A,i}P(s\mid I_{A,i})$.
2. **Locality**: if Alice knows $s=s'$, the gain depends only on $P(s'\mid I_B)$, not on counterfactual values. The book footnote: frequentist $p$-values $\int_{s\ge s_0}ds\,P$ are not local.
3. **Analyticality**: differentiable in $I_B$.
4. **Properness**: maximal at $I_B=I_A$ (the book assumes Alice knows all Bob knows, plus more).
5. **Calibration**: $G_S(I_A,I_0,I_0)=0$, "no update, no gain".

Additivity reduces the gain to an average over $s'\sim P(s\mid I_A)$ of a local function $g(s',P(s'\mid I_B),I_0)$. Properness with a Lagrange multiplier $\lambda$ for normalization gives $\partial g/\partial\tilde q=\lambda/\tilde q$, so $g=\lambda\ln\tilde q+c$, and calibration fixes $c=-\lambda\ln P(s\mid I_0)$. The result is the log ratio above.

## Properties (§2.6.2, pp. 44-47)
- **Ideal AIG** at $I_B=I_A$ is the Kullback-Leibler divergence $D_{\mathrm{KL}}(P(s\mid I_A)\,\|\,P(s\mid I_0))\ge0$, zero iff $I_A=I_0$ (Gibbs inequality, proved in footnote 4 via $\ln x\le x-1$). See [[KL divergence]]. 1 nit $=1/\ln2$ bit $\approx1.44$ bit.
- **Achieved = ideal - remaining**: $D_S(I_A,I_B,I_0)=D_S(I_A,I_0)-D_S(I_A,I_B)$.
- **No update** gives 0; **perfect knowledge** $I_A=I_{s=s'}$ gives $\ln[P(s'\mid I_B)/P(s'\mid I_0)]$, finite although the ideal gain $D_S(I_A,I_0)$ is infinite.
- **Additive over independent parts** of $S=S_1\otimes S_2$ when $I_0,I_B$ factorize (footnote 5, eqs. 108-112). **Mutual information** is the KL from the separated to the correlated state, $\mathrm{MI}=D_S(I_B,I_0)$ with $I_0$ the product of the marginals.
- **Antisymmetry** $D_S(I_A,I_B,I_0)=-D_S(I_A,I_0,I_B)$ and **path additivity** $D_S(I_A,I_B,I_0)=D_S(I_A,I_B,I_C)+D_S(I_A,I_C,I_0)$ (eq. 113).
- **Surprise is additive**: $H(d,s\mid I)=H(d\mid s,I)+H(s\mid I)$ (eqs. 104-107).
- **Learning a bit**: a fair coin ($P=1/2$) and the news "head" give exactly 1 bit. If Bob's prior was $P(\mathrm{head})=2^{-n-1}$ the gain is $n+1$ bits; for $P=0$ it is infinite.

## Cognitive operations (§2.7, pp. 47-48)
- **Communicating**: $I_0\to I_B$ on receiving a message. **Memorizing**: $I_0=I_A$, so $D_S(I_A,I_B,I_A)=-D_S(I_A,I_B)\le0$; memory is at best lossless. **Inference**: $I_A=(d,I_0)$ and $I_B$ an approximate posterior; the AIG scores approximate inference.
- **Cognitive fidelity** 
$$\mathrm{CF}=\frac{D_S(I_A,I_B,I_0)}{D_S(I_A,I_A,I_0)}=1-\frac{D_S(I_A,I_B)}{D_S(I_A,I_0)}\in[-\infty,1]$$
It is 1 for a perfect update, 0 for none, negative if the update makes things worse than not updating.
- **Cognitive efficiency** $\mathrm{CE}=D_S(I_A,I_B,I_0)/C(I_A,I_B,I_0)$, gain per cost (bits per euro, joule or second).

## Examples and recipe (§2.8, pp. 49-50)
- **Bernoulli weather report**: with $p_A=P(s=0\mid I_A)$, a rounded report $p_B$ is worth sending only if $p_A\ln(p_B/p_0)+(1-p_A)\ln\frac{1-p_B}{1-p_0}>0$.
- **Expected AIG for intractable posteriors**: sample $s_i\sim P(s\mid I_0)$, $d_i\sim P(d\mid s_i,I_0)$, then
$$\langle D_S(I_A,I_B(d),I_0)\rangle_{(d\mid I_0)}\approx\frac1n\sum_i\big[H(s_i\mid I_0)-H(s_i\mid I_B(d_i))\big]$$
It works because of the product rule, and requires no access to the true posterior. Training a generative or inference model by this score drives $I_B(d)$ toward the Bayesian posterior.

## Where it appears
- [[Maximum entropy principle]]: encoding maximizes the AIG, decoding minimizes the first KL argument.
- [[Bayesian decision theory]]: the same chapter derives the AIG as the utility-free score for knowledge.
- [[Fisher information]]: second-order expansion of the KL.
- [[Active learning]]: expected information gain as acquisition function; this page's AIG averages the same log ratio.

**Covered in**: Enßlin IT & IFT ch. 2 (pp. 42-51); ch. 3 §3.1 (p. 53)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[KL divergence]] · [[Statistical entropy]] · [[Bayesian inference]] · [[Information field theory]]
