# Ablation Study

Core claim: Curvature is estimated with Hutchinson's trace estimator (h=1e-3, n=10 Rademacher vectors); privacy is swept over epsilon = 1, 10, 20, 30, 40, 50 with delta = 1e-5, and curvature is averaged over 10 seeds per budget.

Supporting detail: The top-500-most-memorized study splits CIFAR100 to isolate high-memorization samples, showing their memorization scores fall sharply once DP is applied and rise back as epsilon grows.

Narration: Curvature uses Hutchinson's trace estimator with step 1e-3 and ten Rademacher vectors, cheap enough to run at scale. Privacy sweeps epsilon over one, ten, twenty, thirty, forty, and fifty at delta 1e-5, averaging ten seeds. The five hundred most-memorized CIFAR100 examples collapse under strong privacy and recover as epsilon grows.
