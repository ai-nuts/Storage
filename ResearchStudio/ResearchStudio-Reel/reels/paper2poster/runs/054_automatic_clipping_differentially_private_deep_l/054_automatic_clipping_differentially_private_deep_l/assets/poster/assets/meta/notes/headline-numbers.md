# Headline Numbers

Core claim: - GPT2 on E2E: BLEU 64.18 at epsilon=3 (AUTO-S), vs 63.85 prior SOTA - RoBERTa-base SST-2: 92.32% at epsilon=3 (AUTO-S) vs 91.86% - CIFAR10 (SimCLRv2): 92.70% at epsilon=2 (AUTO-S) - ImageNet ResNet18: accuracy drops from 45% to 31% when R is doubled (motivating removal of R)

Supporting detail: - RoBERTa-large SST-2: 94.61% at epsilon=8 (AUTO-S) - Convergence: min_t E(||g_t||) = O(T^{-1/4}), matching standard SGD - Default stability constant gamma = 0.01; tuning cost cut ~5x

Narration: The headline numbers: GPT2 on E2E reaches BLEU sixty-four point one eight at epsilon three, versus sixty-three point eight five for the prior best. RoBERTa-base on SST-2 reaches ninety-two point three two percent, and RoBERTa-large on the same task reaches ninety-four point six one percent at epsilon eight. CIFAR-10 with SimCLRv2 hits ninety-two point seven percent at epsilon two. The sensitivity of the old approach is stark: on ImageNet, doubling the threshold drops ResNet18 accuracy from forty-five to thirty-one percent. Theoretically, the minimum expected gradient norm shrinks at the rate T to the minus one quarter, matching standard SGD.
