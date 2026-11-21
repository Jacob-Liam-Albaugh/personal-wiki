---
type: method
area: bayesian
areas: [bayesian, ift]
source-ref: "Enßlin, IT & IFT, ch. 1, §1.5-1.8, eqs. 13-72"
tags: [bayesian, ift]
---

# Bayesian inference

> [!definition] Bayes' theorem for signal and data
> With signal $s$ (unknown, of interest), data $d$ (known) and background information $I$,
> $$P(s\mid d)=\frac{P(d\mid s)\,P(s)}{P(d)},\qquad P(d)=\sum_s P(d,s)$$
> Prior $P(s)$, likelihood $P(d\mid s)$, evidence $P(d)$ (a normalizing constant), posterior $P(s\mid d)$. For continuous $s$ the same rules hold for probability densities.
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §1.6.2, eqs. 15-16, p. 20; p. is the PDF page)

**Intuition**: the joint probability $P(d,s)$ holds everything. Prior, likelihood, evidence and posterior are different normalized cuts and marginals of it (§1.7.6, p. 29). Measuring $d_\mathrm{obs}$ keeps only the slice $d=d_\mathrm{obs}$ and renormalizes it.

Notation: the book writes $\mathcal P$ for probabilities and $I$ for background information, usually dropped. This page writes $P$. The rules follow from [[Cox's theorem]].

## Measurement picture (§1.6.1, pp. 19-20)
Reality is mapped into the data space by the measurement; we hold only a simplified theory with unknown parameters, the signal $s$, to be inferred from $d$ via $P(d\mid s)$. Listed failure points: the theory may miss relevant aspects, the device may be broken, the data may not fix the signal uniquely.

## Worked example: the coin (§1.7, pp. 21-29)
Signal: head frequency $f\in[0,1]$. Data: tosses $d_i\in\{0,1\}$, $n_1$ heads, $n_0$ tails, $n=n_0+n_1$. Without the shared parameter $f$ the tosses look independent and carry no information about each other (§1.7.1, p. 22); $f$ is the hidden property that connects them.

> [!theorem] Posterior and Laplace's rule of succession
> With a uniform prior on $f$ and $\int_0^1 f^{n_1}(1-f)^{n_0}df=\frac{n_0!\,n_1!}{(n+1)!}$ (beta function, eq. 37),
> $$P(f\mid d)=\frac{(n+1)!}{n_1!\,n_0!}\,f^{n_1}(1-f)^{n_0}$$
> $$P(d_{n+1}=1\mid d)=\langle f\rangle=\frac{n_1+1}{n+2}$$
> Variance $\sigma_f^2=\bar f(1-\bar f)/(n+3)$ with $\bar f=(n_1+1)/(n+2)$; width $\propto1/\sqrt n$, and for large $n$ the posterior is approximately Gaussian (eq. 43).
>
> (source: Ensslin - Information Theory & Information Field Theory.pdf, §1.7.3-1.7.4, eqs. 39, 41-43, pp. 25-27)

- The rule of succession adds one virtual head and one virtual tail to the counts. Russian-roulette remark: after $n$ wins, $\langle f\rangle=1/(n+2)>0$ for the lethal outcome, so the game is not declared safe (p. 26-27).
- The evidence $P(d)=\frac{n_0!\,n_1!}{(n+1)!}$ (eq. 38) is the integral of the joint over $f$.
- Sufficient statistics: only $(n_1,n_0)$ matter, not the order of tosses (§1.7.6, p. 29).

### Model comparison with odds (§1.7.5, p. 27-28)
Loaded coin ($f\in[0,1]\setminus\{1/2\}$) against fair coin ($f=1/2$), equal hyper-priors. The posterior odds equal the ratio of evidences:
$$O=\frac{P(d\mid\text{loaded})}{P(d\mid\text{fair})}=2^n\,\frac{n_1!\,n_0!}{(n+1)!}\quad(\text{eq. 44})$$
Only heads: $O=1,1,4/3,2,\dots$ for $n=0,1,2,3,\dots$ and $\approx10^{28.1}$ at $n=100$. Numerical result (Fig. 3, p. 28): out of 100 tosses fewer than 35 or more than 65 heads are needed before a loaded coin can be claimed at 10:1; a fair coin can never be claimed at 10:1 after only 100 tosses, but 1000 balanced tosses can suffice. The fair-coin model is nested in the loaded one; maximum likelihood would always prefer the larger model, whereas the odds ratio has Occam's razor built in (§1.7.6, p. 29).

## Adaptive data retrieval (§1.8, pp. 29-32)
Data taken sequentially, each action $a_i=A(d_{(i-1)})$ chosen by a strategy $A$ from earlier data. The likelihood factorizes as $P(d\mid A,s)=\prod_iP(d_i\mid a_i,s)$ (eqs. 45-48). Two strategies that produce the same actions for the observed data give the same posterior (eq. 53), provided $P(s\mid A)=P(s)$ (the signal does not depend on the strategy; the book notes this can fail, e.g. for an intelligent signal).

> [!theorem] The strategy cannot manufacture evidence
> The expected odds against the true hypothesis $J$ are strategy independent,
> $$\langle O\rangle_{(d\mid A,J)}=\frac{P(I)}{P(J)}$$
> so tuning the strategy (for example stopping once a significance threshold is hit) can only redistribute odds mass, trading rare high odds for more frequent moderate ones. The expected inverse odds $\langle 1/O\rangle$ for the true hypothesis are at least $P(J)/P(I)$ (Jensen), so one does learn on average.
>
> (source: same file, §1.8.2, eqs. 56-72, pp. 31-32)

Corollary stated by the book: a Bayesian analysis of an interdependent history needs no knowledge of the strategy function, while a frequentist analysis, which sums over data that were not observed, does. Wiki note: this is the likelihood-principle argument against stopping-rule dependence **[unverified]** as a named result; the book does not name it.

## Probability densities (§1.7.2, pp. 22-24)
Densities are probabilities times a volume measure, $P(f\in F)=\int_Fdf\,P(f)$ (eq. 24), so Bayes' theorem holds for them. They change with a Jacobian under coordinate change (eq. 26), so "uniform" requires choosing the natural coordinates: flat in $y=\ln x$ means $P(x)\propto1/x$. The book also warns that a density fixes all probabilities, but not conversely: adding a zero-measure function changes conditional densities at a point.

## Where it appears
- [[Bayesian decision theory]]: turns the posterior into an action.
- [[Maximum entropy principle]]: a hard data constraint treated as a soft constraint reproduces this Bayesian update.
- [[Information field theory]]: the same rules with the signal a field.
- [[Bayesian inverse problems]], [[Laplace approximation]]: applications; the Gaussian approximation of the coin posterior is the 1-D case.

**Covered in**: Enßlin IT & IFT ch. 1 (pp. 19-32)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

---

## Related pages
- [[Cox's theorem]] · [[Bayesian decision theory]] · [[Maximum entropy principle]] · [[Achieved information gain]]
- [[Central limit theorem]] · [[Active learning]] · [[Hierarchical Bayesian model]]
