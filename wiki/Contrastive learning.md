---
type: concept
area: ml
areas: [ml]
source-ref: "Radford et al. 2021, §2.3 and Fig. 3, main p. 3; Fig. 2; supp. p. 25"
tags: [ml]
---

# Contrastive learning (CLIP objective)

**Summary**: instead of predicting a target, learn embeddings in which matched pairs score higher than mismatched ones. CLIP applies this to (image, text) pairs. In a batch of $ pairs it raises the cosine similarity of the $ true pairs and lowers it for the ^2-N$ wrong ones. The loss is a symmetric cross-entropy over the similarity matrix (main p. 3).

**Sources**: `papers/Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP).pdf`, `papers/Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP) - Supplementary.pdf`.
**Last updated**: 2026-11-06

---

## The objective (Fig. 3, main p. 3)
```
I_e = normalize(I_f W_i)     # [n, d_e]
T_e = normalize(T_f W_t)     # [n, d_e]
logits = I_e T_eᵀ · exp(t)   # [n, n]
labels = 0..n-1
loss = ½ CE(logits, labels, axis=0)
     + ½ CE(logits, labels, axis=1)
```
- $ is a learned log-temperature, so the temperature is not tuned by hand (main p. 3). The maximum temperature is 100 (supp. p. 25).
- Only linear projections map each encoder into the shared space. There is no non-linear projection head (main p. 3).
- The batch construction is the multi-class N-pair loss of Sohn (2016) (main p. 3). Wiki note: this is often called InfoNCE.

## Why contrastive (Fig. 2, main p. 3)
At equal compute, measured by zero-shot ImageNet accuracy:
- Predicting a bag-of-words encoding is 3× more efficient than a transformer captioning model.
- Swapping that prediction objective for the contrastive one gives a further 4×.

The task is easier: pick which caption goes with the image, not its exact words.

## Scale
- 400 million (image, text) pairs (WIT, main p. 2).
- Batch size 32,768, 32 epochs (supp. p. 25, Table 18).

## Where it appears
- [[CLIP (Radford 2021)]].
- It enables [[Zero-shot transfer]]: the text encoder turns class names into classifier weights.

## Related pages
- [[Zero-shot transfer]] · [[CLIP (Radford 2021)]]
