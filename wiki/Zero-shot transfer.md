---
type: concept
area: ml
areas: [ml]
source-ref: "Radford et al. 2021, §2.5, §3.1, Table 1, Fig. 4, Fig. 7; supp. App. B, p. 9"
tags: [ml]
---

# Zero-shot transfer

**Summary**: use a pretrained model on a new task without training on that task's examples. CLIP embeds every class name (wrapped in a prompt) with its text encoder and labels an image by the closest one. The class embeddings act as the weights of a linear classifier. CLIP treats this as a test of task learning rather than representation learning (main p. 4).

**Sources**: `Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP).pdf`, `Diffusion/Radford et al - Learning Transferable Visual Models From Natural Language Supervision (CLIP) - Supplementary.pdf`.
**Last updated**: 2026-11-06

---

## Results
```
Zero-shot top-1 (Table 1, main p. 4):
            Visual N-Grams   CLIP
  aYahoo        72.4         98.4
  ImageNet      11.5         76.2
  SUN           23.0         58.5
```
- 76.2% on ImageNet matches the original ResNet50 without any of its 1.28M labelled images. Top-5 is 95% (main p. 4).
- Against a logistic-regression probe on ResNet50 features, zero-shot CLIP wins on 16 of 27 datasets (Fig. 4, main p. 5). STL10 reaches 99.3%.

## Prompts (supp. App. B, p. 9)
- "A photo of a {label}." adds 1.3% on ImageNet over the bare label.
- Task hints help, e.g. "a type of pet." for Oxford Pets, or "a satellite photo of a {label}.".
- Ensembling 80 prompts adds another 3.5%, almost 5% in total. Averaging happens in embedding space, so the ensemble costs the same as one classifier.

## Robustness (main p. 7, Fig. 7)
Effective robustness (Taori et al. 2020) is accuracy under distribution shift above what in-distribution accuracy predicts. Zero-shot CLIP models improve it a lot. They close up to 75% of the gap between ImageNet accuracy and accuracy under natural shifts. They trace a frontier separate from all 204 models in Taori et al.

## Where it appears
- [[CLIP (Radford 2021)]].

## Related pages
- [[Contrastive learning]] · [[CLIP (Radford 2021)]]
