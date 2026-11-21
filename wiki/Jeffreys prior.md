---
type: definition
area: bayesian
areas: [bayesian, ift]
source-ref: "Enßlin IT & IFT, §13.3, p. 151 (PDF page)"
tags: [bayesian, ift]
---

# Jeffreys prior

> [!definition] Scale prior (source: Ensslin - Information Theory & Information Field Theory.pdf, §13.3, p. 151)
> For a quantity $p>0$ of unknown magnitude, take a distribution that is flat on a logarithmic scale:
> $$P(p)\propto p^{-1}\quad\Longleftrightarrow\quad P(\tau)\propto\mathrm{const},\ \ \tau=\ln p.$$

**Intuition**: if all that is known is "positive, magnitude unknown", every decade should be equally likely. The prior does not change when the units of $p$ are rescaled.

Page numbers are PDF pages of the lecture notes (printed page = PDF page minus 6). The book writes "Jeffrey's prior".

## Use in the book
The spectral coefficients $p_i$ of an unknown signal covariance get this prior, one per spectral band, before the spectrum is marginalised out. See [[Critical filter]] and [[Power spectrum estimation]].

## General form
Wiki note: the book only uses the scale case. The general Jeffreys prior is $P(\theta)\propto\sqrt{\det g(\theta)}$ with $g$ the [[Fisher information]] metric, which makes it invariant under reparametrisation; for a scale parameter it reduces to $1/p$. It is improper (not normalisable). **[unverified]** against a source in this wiki.

## Where it appears
- [[Critical filter]] — prior on the power spectrum bands.

**Covered in**: Enßlin IT & IFT ch. 13 (p. 151)
**Sources**: `text_books/Machine Learning & Statistics/Ensslin - Information Theory & Information Field Theory.pdf`.
**Last updated**: 2026-11-21

## Related pages
- [[Critical filter]] · [[Power spectrum estimation]] · [[Fisher information]] · [[Maximum entropy principle]] · [[Bayesian inference]]
