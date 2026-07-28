# Motivation

Core claim: Tuning the pair (R, learning rate) for large models takes days to months of compute and, because it touches private data, also consumes extra privacy budget, making DP training far harder than standard training.

Supporting detail: In practice the threshold is set so small that essentially all per-sample gradients are clipped at every iteration, so the exact value of R stops carrying useful magnitude information.

Narration: Searching jointly over the clipping threshold and the learning rate is one of the main reasons DP training is painful. For large models this grid search can take days to months of compute, and because it inspects private data it also spends additional privacy budget. Crucially, the best thresholds are usually so small that nearly every per-sample gradient is clipped at every step, which hints that the precise value of R may not matter at all if we reformulate the clipping.
