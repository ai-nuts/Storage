---
title: Automatic Clipping: Differentially Private Deep Learning Made Easier and Stronger
authors: Zhiqi Bu¹, Yu-Xiang Wang¹², Sheng Zha¹, George Karypis¹
institutes: ¹AWS AI; ²UC Santa Barbara
venue: NeurIPS 2023
paper_url: https://arxiv.org/abs/2206.07136
code_url: https://github.com/awslabs/fast-differential-privacy
title_audio_script: This work, from AWS AI and UC Santa Barbara, is titled "Automatic Clipping: Differentially Private Deep Learning Made Easier and Stronger." Differentially private training of deep networks relies on per-sample gradient clipping, but the clipping threshold R is a fragile hyperparameter that must be tuned carefully for good accuracy. The authors propose automatic clipping, a drop-in replacement that removes R entirely from any DP optimizer, so private training becomes as tuning-friendly as ordinary training while matching or beating the state of the art.
---

## Problem
**Necessary:** Differentially private deep learning depends on per-example gradient clipping, but the clipping threshold R is a fragile, task-specific hyperparameter whose value strongly determines final accuracy.
**Additional:** On ImageNet, ResNet18 accuracy can fall from 45% to 31% if R is set 2x too large; SOTA results often need very small R (e.g. R=1 or R=0.1), found only by expensive search.
**Audio script:** In differentially private deep learning, every per-sample gradient is clipped to a fixed norm R before noise is added, and that single threshold R turns out to be decisive for accuracy. Picking it wrong is costly: on ImageNet, ResNet18 accuracy can collapse from forty-five percent to thirty-one percent when R is merely doubled. State-of-the-art private models tend to need very small clipping thresholds that can only be found through careful, expensive tuning.

## Motivation
**Necessary:** Tuning the pair (R, learning rate) for large models takes days to months of compute and, because it touches private data, also consumes extra privacy budget, making DP training far harder than standard training.
**Additional:** In practice the threshold is set so small that essentially all per-sample gradients are clipped at every iteration, so the exact value of R stops carrying useful magnitude information.
**Audio script:** Searching jointly over the clipping threshold and the learning rate is one of the main reasons DP training is painful. For large models this grid search can take days to months of compute, and because it inspects private data it also spends additional privacy budget. Crucially, the best thresholds are usually so small that nearly every per-sample gradient is clipped at every step, which hints that the precise value of R may not matter at all if we reformulate the clipping.

## Contribution
**Necessary:** The paper introduces automatic clipping (AUTO-V and AUTO-S) that removes the clipping threshold from any DP optimizer, gives a non-convex convergence theorem matching standard SGD, and demonstrates state-of-the-art results on vision and language tasks with a one-line code change.
**Additional:** It shows any constant R is equivalent to R=1, sets a default stability constant gamma=0.01, and integrates into existing libraries (Opacus, ObJAX) by replacing Abadi's clipping.
**Audio script:** The authors make four contributions. First, they propose automatic clipping, which mathematically expunges the clipping threshold from general DP optimizers including DP-SGD, DP-Adam, and DP-LAMB. Second, they prove that automatic DP-SGD converges in the non-convex setting at the same asymptotic rate as standard SGD. Third, they show any positive constant threshold is equivalent to setting it to one, so a single default suffices. And fourth, they demonstrate superior results across vision and language benchmarks, achievable by changing a single line of code in popular libraries.

## Method
**Necessary:** Automatic clipping replaces Abadi's clipping factor min(R/||g||, 1) with a pure normalization R/||g||, called AUTO-V. To preserve gradient magnitude and escape the resulting "lazy region," AUTO-S divides by ||g|| + gamma with a small stability constant gamma. Because any constant R rescales into the learning rate, R is fixed to 1, leaving a threshold-free optimizer.
**Additional:** AUTO-V maximizes dot-product similarity between the private and true gradient but is scale-invariant, so small gradients cannot vanish; the gamma in AUTO-S restores magnitude so clipped gradients approach g/gamma as g -> 0, enabling convergence to zero gradient norm.
**Audio script:** The idea starts from a simple observation: when the threshold is small, Abadi's clipping factor, the minimum of R over the gradient norm and one, is almost always just R over the gradient norm. So the authors drop the minimum entirely and normalize every per-sample gradient, a variant they call AUTO-V for vanilla. This maximizes alignment between the private and true gradient, but it makes all gradients the same size, creating a lazy region where updates stall. To fix this they add a small stability constant gamma in the denominator, giving AUTO-S: R divided by the gradient norm plus gamma. This preserves relative magnitudes, letting small gradients shrink toward zero. Finally, because any constant threshold simply rescales the learning rate, they fix R to one, and set gamma to a default of zero point zero one, leaving a fully threshold-free optimizer.
**Key equation:** `$\text{Clip}_{\text{AUTO-V}}(g_i;R)=R/\lVert g_i\rVert$` ; `$\text{Clip}_{\text{AUTO-S}}(g_i;R)=R/(\lVert g_i\rVert+\gamma)$` ; `$\hat g_t=\sum_i \frac{g_{t,i}}{\lVert g_{t,i}\rVert+\gamma}+\sigma\cdot N(0,I)$`

## Dataset / Benchmark
**Necessary:** Evaluated on language tasks with RoBERTa-base/large (MNLI, QQP, QNLI, SST-2) and GPT2/GPT2-medium/large text generation (E2E, DART), plus vision tasks (CIFAR10 with SimCLRv2, ImageNette with ResNet9, ImageNet with ResNet18).
**Additional:** Uses standard privacy budgets epsilon=3 and epsilon=8, the exact hyperparameters of prior SOTA (Li et al.), and reports 95% confidence intervals over 5 runs on image tasks.
**Audio script:** The method is tested broadly. On language, the authors finetune RoBERTa base and large on the GLUE tasks MNLI, QQP, QNLI, and SST-2, and finetune GPT2 in three sizes for table-to-text generation on the E2E and DART datasets. On vision, they evaluate CIFAR-10 with a pretrained SimCLRv2, ImageNette with a ResNet9, and ImageNet with ResNet18. They use standard privacy budgets of epsilon three and epsilon eight and reuse the exact hyperparameters of prior state-of-the-art work, changing only the clipping.

## Key Result
**Necessary:** Automatic clipping (AUTO-S) matches or beats state-of-the-art on every task without tuning R: e.g. GPT2 on E2E reaches BLEU 64.18 at epsilon=3 (vs 63.85 prior), and RoBERTa-base SST-2 reaches 92.32% vs 91.86%.
**Additional:** On CIFAR10 with SimCLRv2, AUTO-S reaches 92.70% at epsilon=2; RoBERTa-large SST-2 hits 94.61% at epsilon=8; searching only the learning rate (not the (R, learning rate) grid) cuts tuning cost roughly 5x.
**Audio script:** Across the board, automatic clipping matches or outperforms the state of the art, and it does so without ever tuning the threshold. For GPT2 text generation on E2E, AUTO-S reaches a BLEU score of sixty-four point one eight at epsilon three, edging past the prior best of sixty-three point eight five. For RoBERTa-base on SST-2, it reaches ninety-two point three two percent, above the prior ninety-one point eight six. On CIFAR-10 with a pretrained SimCLRv2 it hits ninety-two point seven percent at epsilon two. And because only the learning rate needs searching, the tuning cost drops by about five times.

## Ablation Study
**Necessary:** AUTO-S consistently outperforms AUTO-V once magnitude information is preserved, and the method is insensitive to the stability constant gamma: any gamma > 0 yields the same asymptotic convergence rate, justifying the fixed default gamma=0.01.
**Additional:** Heatmaps over (R, learning rate) show the AUTO-S column matching the best hand-tuned R across SST2, QNLI, and MNLI, confirming R can be safely eliminated rather than tuned.
**Audio script:** Two ablations anchor the design. First, comparing AUTO-V and AUTO-S shows that once the small stability constant restores gradient magnitude, AUTO-S consistently wins, confirming that the lazy region really does hurt AUTO-V. Second, sweeping the stability constant gamma shows the method is essentially insensitive to it: any positive gamma gives the same asymptotic convergence rate, which is why a single default of zero point zero one works everywhere. Heatmaps over threshold and learning rate further show the AUTO-S result landing right at the best hand-tuned threshold.

## Headline Numbers
**Necessary:**
- GPT2 on E2E: BLEU 64.18 at epsilon=3 (AUTO-S), vs 63.85 prior SOTA
- RoBERTa-base SST-2: 92.32% at epsilon=3 (AUTO-S) vs 91.86%
- CIFAR10 (SimCLRv2): 92.70% at epsilon=2 (AUTO-S)
- ImageNet ResNet18: accuracy drops from 45% to 31% when R is doubled (motivating removal of R)
**Additional:**
- RoBERTa-large SST-2: 94.61% at epsilon=8 (AUTO-S)
- Convergence: min_t E(||g_t||) = O(T^{-1/4}), matching standard SGD
- Default stability constant gamma = 0.01; tuning cost cut ~5x
**Audio script:** The headline numbers: GPT2 on E2E reaches BLEU sixty-four point one eight at epsilon three, versus sixty-three point eight five for the prior best. RoBERTa-base on SST-2 reaches ninety-two point three two percent, and RoBERTa-large on the same task reaches ninety-four point six one percent at epsilon eight. CIFAR-10 with SimCLRv2 hits ninety-two point seven percent at epsilon two. The sensitivity of the old approach is stark: on ImageNet, doubling the threshold drops ResNet18 accuracy from forty-five to thirty-one percent. Theoretically, the minimum expected gradient norm shrinks at the rate T to the minus one quarter, matching standard SGD.

## Takeaway
**Necessary:** Per-sample gradient clipping in DP training does not need a tuned threshold: normalize each gradient and add a tiny stability constant, and you get a threshold-free optimizer that is as private, as fast, and as accurate as the best hand-tuned DP methods.
**Additional:** Automatic clipping is a one-line change in existing DP libraries with rigorous convergence guarantees, making DP training as easy as non-private training.
**Audio script:** The lasting message is that the clipping threshold, long treated as a critical knob in differentially private training, can simply be removed. By normalizing each per-sample gradient and adding a tiny stability constant, you get an optimizer that is just as private, just as fast, and just as accurate as the best hand-tuned methods, backed by a convergence guarantee matching standard SGD. It is a one-line change in existing libraries, which finally makes DP training about as easy as ordinary training.
