# Method

Core claim: They study the finite-rank KRR estimator and decompose its test error via the classical bias-variance split, then bound bias and variance separately with high probability. The proof combines careful algebra in the ridge terms with a sub-Gaussian covariance-matrix concentration result plus a Neumann-series expansion of the matrix inverse, so the bounds hold for any λ chosen independently of N.

Supporting detail: The target function f̃ is decomposed into an in-RKHS part f̃≤M and an orthogonal complement γ̃>M ψ>M (an input-dependent noise term); the complementary coefficient γ̃>M captures the irreducible finite-rank error that never vanishes even as N→∞.

Narration: The method starts from the kernel-ridge estimator and splits the test error into a bias term and a variance term, each bounded with high probability. The key ingredients: careful algebra on the ridge terms, a sub-Gaussian covariance concentration inequality, and a Neumann-series expansion. That lets the bounds hold for any ridge value.
