---
type: method
area: bayesian
areas: [bayesian, ift]
source-ref: "Enßlin, IT & IFT, ch. 3, §3.2-3.5, eqs. 131-135, 186-200, 218-224"
tags: [bayesian, ift]
---

# Maximum entropy principle

> [!algorithm] MaxEnt recipe (decoding a message)
> Prior knowledge $P(s\mid I_0)$; message $m=(f,d)$ meaning "$\langle f(s)\rangle_{(s\mid I_A)}=d$". Receiver Bob picks the updated state that is closest to his prior in the KL sense and respects the message:
> $$I_B=\arg\min_{I_B',\mu}\Big[D_{\mathrm{KL}}(I_B',I_0)-\mu^\dagger\big(\langle f\rangle_{I_B'}-d\big)\Big]$$
> 1. Partition sum $\mathcal Z(\mu)=\int ds\,P(s\mid I_0)\,e^{\mu^\dagger f(s)}$
> 2. Fix $\mu$ by $\partial\ln\mathcal Z/\partial\mu=d$
> 3. Assign $P(s\mid I_B)=P(s\mid I_0)\,e^{\mu^\dagger f(s)}/\mathcal Z(\mu)$
> 4. Apparent information gain $D(I_B,I_0)=\mu^\dagger d-\ln\mathcal Z(\mu)$
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §3.3.3, eqs. 131-135, pp. 55-57; p. is the PDF page)

**Intuition**: when a message tells you only some averages, change your beliefs as little as the message demands. The result is the prior tilted exponentially by the quantities that were reported. Nothing else is assumed.

Notation: the book writes $\mathcal P$, $\mathcal Z$, $D_\mathcal S$; this page uses $P$, $Z$ where simple. Entropy here is relative to the prior, $S[q\mid r]=-D_{\mathrm{KL}}(q\|r)$ (§3.5.1, eq. 211).

## Derivation as optimal decoding (§3.2, pp. 53-55)
- Alice encodes by choosing the message that maximizes the [[Achieved information gain]] $D(I_A,I_B(m),I_0)$, i.e. minimizes $D_{\mathrm{KL}}(I_A,I_B(m))$.
- Bob does not know $I_A$. Among states consistent with $\langle f\rangle_{I_B}=d$ he keeps his prior as much as possible, minimizing $D_{\mathrm{KL}}(I_B,I_0)$ with a Lagrange multiplier (§3.2.2). This is MaxEnt.
- Matching $\langle f\rangle_{I_B}=d$ is moment matching, which the book calls expectation propagation (§3.3.1, p. 55). Normalization is enforced by adding a constant function $f_0=1$, $d_0=1$.
- Mnemonic (§3.5.2, p. 67): the first argument of $D_{\mathrm{KL}}$, the distribution averaged over, is the more accurate one. Coding minimizes over the second argument, decoding over the first.
- A sender who knows the receiver decodes by MaxEnt chooses her message by a nested optimization; this needs a mental model of the receiver (theory of mind, §3.2.3, p. 55). Optimal communication is a game in which the sender anticipates the receiver's reaction (§3.5.2, eqs. 222-223).

## Examples (§3.4, pp. 57-61)
- **Coin**: $s\in\{0,1\}$, flat prior $1/2$, constraint $\langle s\rangle=d$. Result $P(s)=d^s(1-d)^{1-s}$ and gain $\ln2+d\ln d+(1-d)\ln(1-d)$ nits, up to 1 bit (eqs. 136-148).
- **Positive counts**: $n\in\mathbb N$, constant prior, $\langle n\rangle=\lambda$. Result $P(n)=\lambda^n(1+\lambda)^{-1-n}$, a geometric law (eqs. 149-157).
- **Many small count processes**: $N$ such processes with a total mean $\lambda$ and $N\to\infty$ give the Poisson law $\lambda^ne^{-\lambda}/n!$ (eq. 171), which is infinitely divisible (eqs. 172-178).
- **Known mean and variance, flat prior on $\mathbb R$**: $P(x)=\mathcal G(x-\bar x,\sigma^2)$ (eqs. 186-200). Multivariate case in [[Multivariate Gaussian]].
- **Hard data as a soft constraint** (§3.4.4, pp. 62-63): take the joint $x=(d,s)$, message topic $f=\delta(d-d^\star)$ with value 1. Approximating the delta by a box of width $\Delta$ and letting $\Delta\to0$ gives
$$P(d,s\mid I_B)=\delta(d-d^\star)\,P(s\mid d^\star,I_0)$$
  so MaxEnt reproduces the [[Bayesian inference]] update (eqs. 183-185). The book compares the step from Bayesian updating to MaxEnt with that from Newtonian to Lagrangian dynamics: forces replaced by an action principle.

## Jaynes' historical derivation (§3.5.1, pp. 65-67)
Starting from the Principle of Minimum Updating ("beliefs must be revised only as far as the new information requires") the entropy of $q$ relative to $r$ is built from criteria:
1. **Locality**: information about a part of the domain only changes that part, so $S[q\mid r]=\int ds\,F(q,r,s)$ (eqs. 202-203).
2. **Coordinate invariance**, giving $S=\int ds\,q\,F'(q/r)$ (eq. 207).
3. **Independence** of independent systems: $S$ is additive, which forces $S[q\mid r]=-\int ds\,q\ln(q/r)=-D_{\mathrm{KL}}(q\|r)$ (eq. 211).
4. **Sensitivity**: a pragmatic addition to exclude constant $S$.

Shannon's original criteria for discrete entropy (footnote, p. 54): continuity in $p$, maximal for the uniform distribution, additivity over successive choices. Jaynes extended it to densities via the relative (conditional) entropy to avoid non-invariance under change of variables. The book's route through [[Achieved information gain]] coincides with Jaynes' for decoding, and with the original discrete principle for a uniform prior.

## Flavours of entropy (§3.1, §3.5.3, pp. 53, 68-69)
- Surprise $H(s\mid I)=-\ln P(s\mid I)$; Shannon entropy $S_S(I)=-\int ds\,P\ln P=\langle H\rangle$, the expected surprise. See [[Statistical entropy]] for the physics reading.
- Relative entropy $S[p\mid q]$ with prior $q$; with constraint multipliers $\lambda$ (normalization) and $\mu$ (the new information) the auxiliary entropy $S^*[p\mid q,J]$ is maximized (eq. 224).
- $\ln\mathcal Z(\mu)$ plays the role of a free energy (p. 56, "may be interpreted as the Helmholtz free energy"); see [[Partition function]] and [[Boltzmann distribution]]: the MaxEnt solution is the same exponential family.

## Failure modes (book, §3.5.2, p. 68)
Real communication breaks the assumptions: senders emphasize or mislead, receivers distrust, models of the other party are wrong. Corrective strategies listed: send raw data rather than interpretations, ask clarifying questions, keep reputation systems.

## Where it appears
- [[Multivariate Gaussian]]: MaxEnt with known first and second moments.
- [[KL divergence]]: the objective, with the first-argument convention above.
- [[Information field theory]]: free theories are MaxEnt Gaussians **[unverified]** (Part II of the book not read here).

**Covered in**: Enßlin IT & IFT ch. 3 (pp. 53-69)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Achieved information gain]] · [[Bayesian inference]] · [[Cox's theorem]] · [[Bayesian decision theory]]
- [[Statistical entropy]] · [[Partition function]] · [[Boltzmann distribution]] · [[KL divergence]]
