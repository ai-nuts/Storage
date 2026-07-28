---
title: Comparing Optimization Targets for Contrast-Consistent Search
authors: Hugo Fry¹, Seamus Fallows¹, Ian Fan¹, Jamie Wright², Nandi Schoots³
institutes: ¹Independent; ²Oxford University; ³King's College London
venue: NeurIPS 2023
paper_url: https://arxiv.org/abs/2311.00488
code_url: https://github.com/ash-ai-safety-hub/g3-nandi
title_audio_script: Contrast-Consistent Search, or CCS, is a popular unsupervised probe that tries to read a language model's internal sense of truth directly from its activations. But what is CCS actually optimizing for? This paper opens up the CCS loss function, offers a heuristic explanation of its optimization target, and turns that explanation into a brand-new loss called Midpoint-Displacement. The authors show that a particular setting of Midpoint-Displacement recovers probes almost identical to CCS, that a better setting beats CCS on accuracy, and that the exact loss formula matters far less than the unusual contrast-pair training data CCS relies on.
---

## Problem
**Necessary:** Contrast-Consistent Search (CCS) recovers a language model's internal "truth" direction, but what its loss actually optimizes for, and whether that target is optimal, is poorly understood.
**Additional:** CCS is presented as learning truth probabilities via a negation-consistency constraint, yet the mechanism behind its success has not been isolated or explained.
**Audio script:** Contrast-Consistent Search recovers a direction in a language model's activation space that is supposed to encode whether a statement is true or false. It does this without any labels, using only the constraint that a statement and its negation must disagree. But despite CCS working surprisingly well, nobody had pinned down what its loss function is really optimizing for, or whether that target is even the best one. This paper sets out to answer exactly that question.

## Motivation
**Necessary:** Safely deploying LLMs requires reliably extracting their latent knowledge of truth; understanding *why* CCS works is a prerequisite for trusting and improving such probes.
**Additional:** Prior work framed CCS around clustering activations and learning calibrated probabilities. The authors show both framings are misleading, motivating a cleaner account of CCS's true optimization target.
**Audio script:** As language models grow more capable, our understanding of their internal behavior has not kept pace, and models frequently state falsehoods with confidence. Techniques that read a model's own representation of truth could help us catch this, but only if we actually understand how they work. The original CCS was explained in terms of clustering activations and learning truth probabilities. The authors argue both of these pictures are misleading, which is what motivates a cleaner explanation of what CCS truly optimizes.

## Contribution
**Necessary:** (1) Conceptual clarifications correcting two misconceptions about CCS (it classifies via translation-invariant displacement vectors, not a separating hyperplane, and can succeed even when its "probabilities" cluster near 0.5). (2) A heuristic account of CCS's optimization target and a new Midpoint-Displacement (MD) loss derived from it. (3) An empirical comparison of many loss functions across models and datasets showing MD is a good proxy for CCS and can outperform it.
**Additional:** Two further loss functions (Mean Absolute, Square Mean Root) are introduced as baselines in the appendix.
**Audio script:** The paper makes three contributions. First, it clears up two misconceptions: CCS classifies using only the displacement between a statement and its negation, so it does not need the data to be separable by a hyperplane, and it can succeed even when its probability outputs pile up around one half. Second, it gives a heuristic account of CCS's optimization target and derives a new loss, called Midpoint-Displacement, from that account. Third, it runs a broad empirical comparison across models and datasets, showing that Midpoint-Displacement is a faithful proxy for CCS and can even beat it.

## Method
**Necessary:** The authors decompose CCS behavior into two quantities along a unit weight direction θ̂: σ_d² (mean-square separation of contrast-pair displacement vectors u_i = φ⁺_i − φ⁻_i) and σ_m² (mean-square value of contrast-pair midpoints v_i = φ⁺_i + φ⁻_i). They argue CCS's double-saturating sigmoid forces a trade-off — maximizing σ_d² while minimizing σ_m² — so CCS implicitly optimizes a balance of the two. The proposed Midpoint-Displacement (MD) loss makes this trade-off explicit through a single hyper-parameter λ. Two variants are studied: MD-CCS (λ chosen to mimic CCS) and MD-Acc (λ tuned for accuracy).
**Additional:** Similarity to CCS is measured by cosine similarity between learned weight vectors; accuracy uses ground-truth labels. Probers are compared against MA, SMR, PCA, random, and supervised baselines over four models and five datasets.
**Key equation:** `$\mathcal{L}_{\mathrm{MD}} = (\lambda-1)\,\sigma_d^2 + \lambda\,\sigma_m^2,\quad \lambda\in[0,1],\ \ |\theta|=1$` where `$\sigma_d^2 = \tfrac{1}{n}\sum_i (\hat{\theta}^{T} u_i)^2,\ u_i = \phi_i^{+}-\phi_i^{-}$` and `$\sigma_m^2 = \tfrac{1}{n}\sum_i (\hat{\theta}^{T} v_i)^2,\ v_i = \phi_i^{+}+\phi_i^{-}$`; the original CCS loss is `$\mathcal{L}_{\mathrm{CCS}}(\theta,b) = \tfrac{1}{n}\sum_i \big(1 - p_{\theta,b}(\phi_i^{+}) - p_{\theta,b}(\phi_i^{-})\big)^2 + \min\big(p_{\theta,b}(\phi_i^{+}), p_{\theta,b}(\phi_i^{-})\big)^2$`.
**Audio script:** The key idea is to describe CCS using two simple statistics measured along the probe's direction. The first, sigma-d-squared, captures how far apart a statement and its negation are pushed. The second, sigma-m-squared, captures how far their midpoint sits from the origin. Because the CCS sigmoid saturates at both ends, the authors argue CCS is forced into a trade-off: it wants to spread the pair apart while keeping the midpoint small. The Midpoint-Displacement loss writes this trade-off out explicitly with a single knob, lambda. Setting lambda one way reproduces CCS; tuning it for accuracy gives a stronger probe.

## Dataset / Benchmark
**Necessary:** Probes are trained and evaluated on hidden-state activations from four models — UnifiedQA T5-Large (encoder and decoder), DeBERTa, and GPT-Neo — averaged over five datasets (including BoolQ), following the CCS contrast-pair setup.
**Additional:** Contrast pairs are formed by appending mutually exclusive answers to a question; the two answer sets are independently normalized so the probe cannot simply detect the answer token.
**Audio script:** The experiments use hidden-state activations from four models: the encoder and decoder of UnifiedQA T5-Large, DeBERTa, and GPT-Neo. Results are averaged over five datasets, including BoolQ. Each example is turned into a contrast pair by appending two mutually exclusive answers to a question, and the two resulting activation sets are normalized independently so that the probe cannot cheat by simply detecting which answer was appended.

## Key Result
**Necessary:** MD-CCS attains an average cosine similarity of ≈0.63 with CCS probers, versus a CCS self-similarity of only 0.78 — far above chance (two random 1024-d unit vectors reach 0.63 with probability ≈10⁻²³⁷), establishing MD as a faithful proxy for CCS's optimization target.
**Additional:** No other high-accuracy loss (MA, SMR, PCA) comes close to CCS in cosine similarity (averages 0.14–0.17), so the resemblance is specific to MD, not a generic byproduct of accuracy.
**Audio script:** The headline finding is that Midpoint-Displacement, tuned to imitate CCS, produces probe directions with an average cosine similarity of about zero point six three to real CCS probes. That may not sound close to one, but CCS probes only agree with themselves at zero point seven eight, and the odds of two random thousand-dimensional vectors reaching zero point six three by chance are about ten to the minus two hundred and thirty seven. Crucially, other accurate losses like Mean Absolute, Square Mean Root, and PCA sit down around zero point one five, so this resemblance is specific to Midpoint-Displacement.

## Ablation Study
**Necessary:** MD-CCS and MD-Acc differ only in the hyper-parameter λ, yet give very different cosine similarities to CCS (0.63 vs 0.38 average) — showing CCS's target is governed by the σ_d²/σ_m² trade-off. Swapping MD-CCS's λ for the accuracy-tuned value raises average test accuracy from 0.7178 to 0.7557.
**Additional:** The MD-CCS hyper-parameter is stable across datasets and models, suggesting the identified proxy target is robust.
**Audio script:** Because the two Midpoint-Displacement variants differ only in the single hyper-parameter lambda, they form a natural ablation. Tuned to mimic CCS, the probe reaches cosine similarity around zero point six three; tuned for accuracy, that drops to about zero point three eight, confirming that the displacement-versus-midpoint trade-off is what defines the CCS target. Retuning lambda for accuracy also lifts average test accuracy from about zero point seven two to zero point seven six. Encouragingly, the CCS-matching value of lambda barely changes across datasets and models, so the proxy target appears robust.

## Headline Numbers
**Necessary:**
- MD-CCS ↔ CCS average cosine similarity ≈ **0.63** (CCS self-similarity **0.78**; MA/SMR/PCA only 0.14–0.17).
- MD-Acc average test accuracy **0.7557** vs CCS **0.7105** — higher accuracy on **3 of 4** models, ~**4%** average gain.
- Probability that two random 1024-d unit vectors reach cosine 0.63 ≈ **10⁻²³⁷**.
- Evaluated over **4 models × 5 datasets**.
**Additional:** Supervised probes average 0.8674 accuracy, marking the practical ceiling for these activations.
**Audio script:** A few numbers summarize the paper. Midpoint-Displacement matched to CCS reaches an average cosine similarity of about zero point six three, against a CCS self-similarity of zero point seven eight, while competing losses only reach zero point one four to zero point one seven. The accuracy-tuned variant averages zero point seven six test accuracy versus zero point seven one for CCS, winning on three of four models by roughly four percent. And the chance of hitting that zero point six three similarity randomly is about ten to the minus two hundred thirty seven. All of this is measured across four models and five datasets.

## Takeaway
**Necessary:** CCS works because of the displacement information in its contrast-pair data, not because of its specific loss formula — a simple Midpoint-Displacement loss reproduces CCS and, retuned, beats it.
**Additional:** The exact loss formulation is largely interchangeable among high-accuracy probes; the trade-off between displacement variance and midpoint variance is what defines CCS's target.
**Audio script:** The take-home message is that CCS's success comes from the information in its contrast-pair training data, specifically the displacement between a statement and its negation, rather than from the particular shape of its loss function. A simple Midpoint-Displacement loss reproduces CCS closely and, when retuned, outperforms it. In other words, the exact loss formula is largely interchangeable among accurate probes, and the real lever is the trade-off between how far pairs are separated and how large their midpoint grows.
