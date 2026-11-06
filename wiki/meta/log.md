---
tags: [meta]
---

# Log

## 2026-11-06 — setup and first ingest
- Adapted the course-vault CLAUDE.md to the whole Papers library. The topic folders are left as they are and act as the raw layer; there is no `raw/` folder. Added area slugs and paper and lecture templates.
- Set up `wiki/`, `wiki/meta/` and `notes/`, and a local git repo that tracks only the wiki, the notes and CLAUDE.md.
- Built [[sources]] from a scan of 243 files: 13 ingested, 187 queued, 35 reference, 8 Finder aliases. Two scanned PDFs have no text layer: the BJS Linear Optimization book and MIT ch. 1-5.
- Ingested 10 papers:
  - the Poly DSL paper;
  - the two reading-group papers;
  - the two lab IFT papers;
  - Wang 2026;
  - Welling-Teh SGLD;
  - three Ruqi Zhang SG-MCMC papers.
- Wrote 48 pages in total, papers plus concept pages.
- Duplicates found:
  - SGLD exists in both Bayesian/ and IFT/.
  - The PIFT arXiv preprint is in Bayesian/.
  - The DeepONet arXiv preprint is in Operators/.
- Open flags, marked **[unverified]** on the pages:
  - the SGLD noise convention in Alberts & Bilionis eq. 22;
  - the exponents of the Cyclical SG-MCMC Thm 2;
  - one term in the Low-precision SGLD Thm 3;
  - noise values in the PIFT examples.
- Plan: [notes/001](../../notes/001-library-wiki-setup-and-ingest-plan.md).

## 2026-11-06 — Bayesian batch
- Ingested 9 papers from Bayesian/:
  - lab VI: [[tsilifis-2014-variational-inverse-problems]], [[karumuri-2024-amortized-vi-inverse-problems]];
  - [[margossian-2024-amortized-vi-when-why]];
  - Kingma: [[kingma-2014-aevb]], [[kingma-2015-variational-dropout]], [[kingma-2019-intro-vae]];
  - [[xu-2022-sde-bnn]], [[fortuin-2022-priors-in-bdl]], [[zhu-2018-bayesian-denseed-surrogate]].
- Wrote 13 concept pages: [[variational-inference]], [[evidence-lower-bound]], [[kl-divergence]], [[reparameterization-trick]], [[amortized-variational-inference]], [[normalizing-flows]], [[bayesian-inverse-problems]], [[variational-autoencoder]], [[local-reparameterization-trick]], [[variational-dropout]], [[bayesian-neural-networks]], [[stein-variational-gradient-descent]], [[gaussian-process]]. The wiki now has 70 pages; [[sources]] shows 22 ingested and 178 queued.
- Incomplete PDFs:
  - Intro to VAEs has only ch. 1 and the appendix.
  - Variational Dropout has no appendices.
- Correction: the BJS and MIT ch. 1-5 books do have a text layer (748/764 and 587/605 pages). The first scan sampled only the cover. That old OCR garbles the math, so equations should be read from page images. A fresh PdfCraft OCR would not fix this, because its engine reads Latin text only.
- Open flags:
  - The Zhu & Zabaras equations were garbled in extraction. The SVGD form is standard and marked **[unverified]**.
  - The Fortuin NTK recursion is marked **[unverified]**.
  - Tsilifis Alg. 1 prints $w_i=1/N$ where $1/L$ is meant.

## 2026-11-06 — Operators and generative batch
- Ingested 4 papers from Operators/: [[kovachki-2022-neural-operator]], [[li-2021-fno]], [[cao-2023-lno]], [[kovachki-2024-operator-learning-review]].
- Ingested 2 generative papers: [[song-2021-score-sde]] (Stochastic Methods/; the Generative ML/ entry is an alias) and [[dey-2021-group-equivariant-gans]] (Symmetries/).
- New concept pages:
  - operators: [[neural-operator]], [[kernel-integral-operator]], [[fourier-neural-operator]], [[laplace-neural-operator]], [[laplace-transform]], [[discretization-invariance]], [[encoder-decoder-architecture]], [[pca-net]], [[random-features-model]], [[curse-of-parametric-complexity]];
  - benchmarks: [[darcy-flow]], [[burgers-equation]], [[navier-stokes-equations]];
  - generative: [[score-matching]], [[fokker-planck-equation]], [[generative-adversarial-network]], [[equivariance]].
- Rewrote [[diffusion-models]] as a hub. Small sub-topics are sections on hub pages, not separate pages (e.g. graph and low-rank NO on [[neural-operator]], VE/VP SDEs on [[diffusion-models]]).
- Updated [[operator-learning]], [[deeponet]], [[universal-approximation-theorem-for-operators]], [[flow-matching]], [[diffusion-posterior-sampling]], [[langevin-dynamics]], [[normalizing-flows]], [[karhunen-loeve-expansion]], [[gaussian-process]].
- Checked against page images: Score-SDE Table 1; LNO eq. 3 really omits the factor $s$ (noted on [[laplace-transform]]).
- Open flags:
  - LNO Fig. 3 values were read by eye (±0.02, **[unverified]**). By those readings the GRU beats LNO in 3 cases.
  - LNO's "exponential convergence" claim is never analysed in the paper.
  - Review eq. 5.12 exponent (p. 27) is unverified.
  - Review Thm 4.1 prints the composition in the wrong order.
  - Burgers FNO error is about 8× lower in the JMLR paper than in ICLR (0.0018 vs 0.0139-0.0160); the text does not say why.
  - Kovachki JMLR table page cites are approximate.
