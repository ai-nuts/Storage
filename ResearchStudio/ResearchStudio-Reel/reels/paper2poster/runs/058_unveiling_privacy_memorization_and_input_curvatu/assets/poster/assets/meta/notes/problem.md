# Problem

Core claim: Input loss curvature is used as a cheap proxy for memorization in deep nets, but there is no theory explaining why the two are linked, or how either relates to differential privacy.

Supporting detail: Feldman's stability-based memorization score is principled but computationally prohibitive, motivating proxies whose validity was purely empirical until now.

Narration: Deep networks memorize training data, which matters for generalization, noisy learning, and privacy leakage. Feldman's memorization score quantifies this rigorously but is far too expensive. Input loss curvature, the trace of the input-loss Hessian, tracks memorization roughly a thousand times cheaper, yet the connection was purely empirical, with no theory linking either to differential privacy.
