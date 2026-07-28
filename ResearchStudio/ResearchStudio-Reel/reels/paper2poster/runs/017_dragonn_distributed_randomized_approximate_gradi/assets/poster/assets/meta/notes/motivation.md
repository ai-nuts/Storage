# Motivation

Core claim: State-of-the-art GS methods such as DGC extract approximate top-k gradients using exact parallel prefix sum, an inherently sequential O(log d) algorithm that scans the tensor multiple times, incurring roughly 7x more memory accesses than the lower bound.

Supporting detail: The authors argue this is an exact-approximate mismatch: only approximate top-k gradients are needed, so paying for an exact selection algorithm is unnecessary overhead.

Narration: The leading sparsification method, Deep Gradient Compression, selects gradients above an estimated threshold, which is an approximate operation. But to place those gradients into memory without conflicts it relies on parallel prefix sum, an exact algorithm that builds a balanced binary tree, runs in logarithmic sequential steps, and touches memory about seven times more than the theoretical lower bound. The authors call this an exact-approximate mismatch: since only an approximate set of top gradients is required, using an expensive exact algorithm to place them is wasted effort.
