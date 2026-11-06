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
