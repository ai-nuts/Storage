# Ablation Study

Core claim: Warm-starting yields more than a 100x speedup in convergence over cold-starting for USBS, while CGAL frequently cannot reliably exploit a warm start; larger kc (current eigenvectors) improves convergence whereas kp (past spectral vectors) helps little and can even hurt.

Supporting detail: The default hyperparameters (r=10, ρ=0.01, β=0.25, kc=10, kp=1) reflect these findings; unlike the original Helmberg–Rendl method that fixes kc=1, USBS benefits from a larger current-eigenvector budget.

Narration: Two ablations are especially informative. First, warm-starting: for USBS, initializing from the previous solution can speed up convergence by more than one hundred times compared with cold-starting, and, importantly, USBS actually realizes this benefit while CGAL usually cannot. Second, the model parameters: the number of current eigenvectors, kc, matters a lot, and larger values give better convergence in general. This contrasts with the original spectral bundle method, which fixed kc to one. The number of past spectral vectors, kp, turns out to be much less helpful and can sometimes even harm convergence, so the recommended settings keep kc large and kp small.
