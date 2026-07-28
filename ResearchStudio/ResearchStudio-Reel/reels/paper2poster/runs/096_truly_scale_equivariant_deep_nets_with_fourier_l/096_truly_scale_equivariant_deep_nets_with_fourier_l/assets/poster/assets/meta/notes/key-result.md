# Key Result

Core claim: On MNIST-scale (ideal, all scales) the model reaches 0.9889 accuracy with 0.9716 scale-consistency and 0.00 equivariance error, the best on every metric. On STL10-scale it reaches 0.7332 accuracy versus 0.5844 for the next best (Fourier CNN), a ~15-point gain, again with zero equivariance error.

Supporting detail: It stays best under non-ideal downsampling (0.9880 accuracy, 0.9760 scale-consistency, 0.05 error) and is the most data-efficient, reaching 0.9606 accuracy at just 1k training samples versus DISCO's 0.9457.

Narration: The results are striking. On MNIST-scale with ideal downsampling, the model achieves the highest accuracy at ninety-eight point nine percent, the highest scale-consistency at ninety-seven percent, and, crucially, an absolute zero equivariance error, while competing methods like DISCO show errors around zero point four. The advantage is largest on the harder STL10-scale natural-image benchmark, where the model reaches seventy-three percent accuracy against roughly fifty-eight percent for the strongest baseline, a gain of about fifteen points, still with exactly zero equivariance error. It also degrades gracefully: even under non-ideal downsampling it remains the best model, and in low-data regimes it is the most data-efficient of all methods tested.
