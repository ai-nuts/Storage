---
title: Unveiling Privacy, Memorization, and Input Curvature Links
authors: Deepak Ravikumar¹, Efstathia Soufleri¹, Abolfazl Hashemi¹, Kaushik Roy¹
institutes: ¹Purdue University
venue: ICML 2024
paper_url: https://arxiv.org/abs/2402.18726
code_url:
title_audio_script: Deep networks memorize parts of their training data, and that memorization is tightly bound up with generalization, noisy learning, and privacy. A formal memorization score exists, but it is far too expensive to compute at scale. Recent work found that input loss curvature, the trace of the loss Hessian with respect to the input, is a cheap empirical proxy, roughly three orders of magnitude faster, yet nobody knew why the two were connected. This paper, from Purdue University and presented at ICML 2024, builds the missing theory. It derives formal bounds linking memorization, input loss curvature, and differential privacy, and validates every one of them on CIFAR and ImageNet.
---

## Problem
**Necessary:** Input loss curvature is used as a cheap proxy for memorization in deep nets, but there is no theory explaining why the two are linked, or how either relates to differential privacy.
**Additional:** Feldman's stability-based memorization score is principled but computationally prohibitive, motivating proxies whose validity was purely empirical until now.
**Audio script:** Deep neural networks tend to overfit and memorize their training data, and memorization matters because it connects to generalization, noisy learning, and privacy leakage. Feldman's memorization score gives a rigorous way to quantify it, but computing it is extremely expensive. Recent research showed that input loss curvature, the trace of the loss Hessian with respect to the input, tracks memorization empirically and is about three orders of magnitude cheaper to compute. The problem is that this link was purely empirical: there was no theoretical understanding of why curvature and memorization move together, nor how either connects to differential privacy.

## Motivation
**Necessary:** A rigorous curvature-memorization-privacy link would justify using cheap curvature as a memorization proxy and reveal how privacy mechanisms suppress memorization.
**Additional:** Influence functions, the usual counterfactual tool, assume Hessian convexity and positive-definiteness, conditions that fail for deep nets; curvature needs no such assumptions.
**Audio script:** If we could prove that input loss curvature bounds memorization, then practitioners would have a theoretical license to use the cheap curvature proxy instead of the expensive memorization score. Equally important, memorization is a privacy risk, so understanding how differential privacy relates to curvature and memorization would explain why privacy mechanisms reduce leakage. Prior counterfactual tools like influence functions rely on strong convexity and positive-definiteness of the Hessian, assumptions that simply do not hold for deep networks. The framework in this paper avoids all of those assumptions, making it far better suited to studying deep learning.

## Contribution
**Necessary:** Three theorems: (1) input loss curvature upper-bounds memorization; (2) the differential-privacy parameter upper-bounds average input loss curvature; (3) privacy upper-bounds memorization, all validated empirically.
**Additional:** The analysis makes no assumptions about Hessian convexity or definiteness, unlike influence-function theory, making it suitable for deep networks.
**Audio script:** The paper makes three theoretical contributions, framed as three links in a triangle connecting memorization, input loss curvature, and differential privacy. First, it derives an upper bound showing that memorization is controlled by input loss curvature. Second, it presents a novel result that input loss curvature is itself upper-bounded by the differential privacy parameter. Third, it connects the two to bound memorization directly by privacy. Crucially, none of these results assume convexity or positive-definiteness of the Hessian, so they apply to real deep networks, and all three are validated empirically on standard image classification benchmarks.

## Method
**Necessary:** Under error-stability, generalization, uniform-model-bias, and dataset adjacency assumptions with bounded loss, a second-order (Nesterov-Polyak) expansion of the loss plus DP definitions yield the three bounds. Curvature is estimated efficiently via Hutchinson's trace estimator.
**Additional:** Bounds are validated using Feldman & Zhang's precomputed memorization scores and models (1000 for CIFAR100, 100 for ImageNet); privacy models are trained with DP-SGD at several epsilon budgets. Curvature uses step h=1e-3 and n=10 Rademacher vectors.
**Key equation:** `$|\mathrm{mem}(A,S,i)| \le \tfrac{1}{L}\,\mathbb{E}_\phi[\mathrm{Curv}_\phi(z_i,S^{\setminus i})] + c_1$` and `$\mathbb{E}_{z,\phi}[\mathrm{Curv}_\phi(z,S)] \le L(m+1)(1-e^{-\epsilon}) + c_2$`
**Audio script:** The theoretical machinery starts from a second-order Taylor expansion of the loss using the Nesterov-Polyak bound, which introduces the Hessian of the loss with respect to the input. By choosing a zero-mean perturbation, the first-order terms vanish, and taking expectations over the algorithm's randomness leaves an upper bound on memorization in terms of expected input loss curvature plus a data-independent offset that collects stability, generalization, and model-bias terms. A parallel derivation, combined with the definition of differential privacy, shows that a stronger privacy guarantee, meaning a smaller epsilon, forces lower average curvature. To make curvature practical to measure, the authors use Hutchinson's trace estimator with a finite-difference step of one times ten to the minus three and ten Rademacher probe vectors, avoiding the full Hessian.

## Dataset / Benchmark
**Necessary:** Standard image classification benchmarks: CIFAR10, CIFAR100, and ImageNet, using Feldman & Zhang (2020) precomputed memorization scores and their released model ensembles.
**Additional:** Architectures include Small Inception and ResNet50 (CIFAR100 / ImageNet memorization ensembles) and ResNet18 trained with DP-SGD for the privacy experiments.
**Audio script:** The empirical validation uses three standard image classification datasets: CIFAR10, CIFAR100, and ImageNet. For memorization, the authors rely on the precomputed stability-based memorization scores and the large model ensembles released by Feldman and Zhang, one thousand models for CIFAR100 and one hundred for ImageNet, averaging curvature and memorization across them. The memorization ensembles use Small Inception on CIFAR100 and ResNet50 on ImageNet. For the privacy experiments they train ResNet18 models with differential-privacy stochastic gradient descent across a range of privacy budgets.

## Key Result
**Necessary:** All three theoretical bounds hold empirically: memorization vs. curvature shows a strong linear trend on CIFAR100 and ImageNet, and stronger privacy (smaller epsilon) produces measurably lower curvature and memorization, matching the predicted best-fit curves.
**Additional:** The linear memorization-curvature relationship is especially pronounced on ImageNet; as the DP budget epsilon increases, memorization of the top-500 most-memorized examples rises as predicted, staying below the Theorem 5.4 bound.
**Audio script:** Every theoretical prediction is borne out in practice. Plotting memorization score against input loss curvature yields a strong linear trend on both CIFAR100 and ImageNet, exactly as the first theorem predicts, and the effect is especially clean on ImageNet. For the privacy link, models trained with differential privacy at increasing budgets show that stronger privacy guarantees drive down input loss curvature along the best-fit curve predicted by the theory. And for the most-memorized examples, memorization rises with the privacy budget while staying under the theoretical upper bound, confirming that privacy suppresses memorization exactly as the third theorem describes.

## Ablation Study
**Necessary:** Curvature is estimated with Hutchinson's trace estimator (h=1e-3, n=10 Rademacher vectors); privacy is swept over epsilon = 1, 10, 20, 30, 40, 50 with delta = 1e-5, and curvature is averaged over 10 seeds per budget.
**Additional:** The top-500-most-memorized study splits CIFAR100 to isolate high-memorization samples, showing their memorization scores fall sharply once DP is applied and rise back as epsilon grows.
**Audio script:** The paper studies how its estimates behave across settings. Input loss curvature is computed with Hutchinson's trace estimator using a finite-difference step of one times ten to the minus three and ten Rademacher probe vectors, a configuration cheap enough to run at scale. The privacy experiments sweep the budget epsilon across values of one, ten, twenty, thirty, forty, and fifty at a fixed delta of ten to the minus five, averaging curvature over ten random seeds for each budget. A focused study on the five hundred most-memorized CIFAR100 examples shows their memorization collapses under strong privacy and climbs back as the privacy budget loosens, tracking the theoretical bound throughout.

## Headline Numbers
**Necessary:**
- Input loss curvature is ~3 orders of magnitude more efficient to compute than Feldman's memorization score.
- Memorization ensembles: 1000 models on CIFAR100, 100 models on ImageNet (Feldman & Zhang 2020).
- Privacy sweep: epsilon = 1, 10, 20, 30, 40, 50 at delta = 1e-5.
- Curvature estimator: step h = 1e-3, n = 10 Rademacher vectors.
**Additional:** Three theorems (5.1, 5.3, 5.4) link curvature, privacy, and memorization; DP-SGD gradient clipping norm 1.0, learning rate 0.001, batch size 128.
**Audio script:** A few numbers capture the work. Input loss curvature is about three orders of magnitude cheaper to compute than the Feldman memorization score, which is what makes it attractive as a proxy. The memorization ground truth comes from averaging over one thousand models on CIFAR100 and one hundred on ImageNet. The privacy experiments sweep the budget epsilon over one, ten, twenty, thirty, forty, and fifty at a delta of ten to the minus five, with curvature estimated using a step size of one times ten to the minus three and ten probe vectors. Three theorems tie the whole triangle of curvature, privacy, and memorization together.

## Takeaway
**Necessary:** Input loss curvature provably upper-bounds memorization and is itself bounded by the differential-privacy parameter, giving a rigorous, assumption-light theory that justifies curvature as a cheap memorization proxy and links both to privacy.
**Additional:** The framework needs no Hessian-convexity assumptions, so it applies directly to deep networks, and its predictions match CIFAR and ImageNet experiments closely.
**Audio script:** The lasting message is that the empirical connection between input loss curvature and memorization is now on firm theoretical ground. Curvature provably upper-bounds memorization, and curvature is in turn bounded by the differential privacy parameter, closing the triangle that also bounds memorization by privacy. Because the theory needs no assumptions about the convexity of the Hessian, it applies directly to real deep networks, and its predictions match experiments on CIFAR and ImageNet closely. In short, a cheap curvature measurement is a theoretically justified stand-in for expensive memorization scores, and privacy mechanisms provably suppress both.
