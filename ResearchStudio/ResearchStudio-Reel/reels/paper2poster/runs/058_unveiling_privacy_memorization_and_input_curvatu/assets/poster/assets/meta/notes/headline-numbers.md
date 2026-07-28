# Headline Numbers

Core claim: - Input loss curvature is ~3 orders of magnitude more efficient to compute than Feldman's memorization score. - Memorization ensembles: 1000 models on CIFAR100, 100 models on ImageNet (Feldman & Zhang 2020). - Privacy sweep: epsilon = 1, 10, 20, 30, 40, 50 at delta = 1e-5. - Curvature estimator: step h = 1e-3, n = 10 Rademacher vectors.

Supporting detail: Three theorems (5.1, 5.3, 5.4) link curvature, privacy, and memorization; DP-SGD gradient clipping norm 1.0, learning rate 0.001, batch size 128.

Narration: A few numbers capture the work. Input loss curvature is about three orders of magnitude cheaper than the Feldman score. Ground truth averages a thousand models on CIFAR100 and a hundred on ImageNet. Privacy sweeps epsilon from one to fifty at delta 1e-5. Three theorems tie the triangle together.
