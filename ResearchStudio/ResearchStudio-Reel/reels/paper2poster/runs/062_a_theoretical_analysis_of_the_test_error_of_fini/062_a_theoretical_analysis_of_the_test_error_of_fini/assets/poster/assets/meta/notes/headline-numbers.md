# Headline Numbers

Core claim: - Bounds hold with probability at least 1 − 2/N with respect to the random sampling. - Upper-bound decay rate log N / N, versus the O(√(log N / N)) rate of a Rademacher-complexity bound (Mohri et al.), an order-of-magnitude faster decay. - Variance upper bound scales as σ²·2M/N (M = kernel rank, N = sample size), valid in the under-parameterized regime N > M.

Supporting detail: - New two-sided bounds are the first to supply a high-probability LOWER bound on finite-rank KRR test error (prior works: none). - Validated over 10 trials on both tNTK and LK kernels for N from ~10 to 200.

Narration: The bounds hold with probability at least one minus two over N. The upper bound decays at a log-N-over-N rate, faster than the square-root Rademacher rate. Variance scales as noise times twice the rank over N. And these are the first finite-rank bounds with a high-probability lower bound.
