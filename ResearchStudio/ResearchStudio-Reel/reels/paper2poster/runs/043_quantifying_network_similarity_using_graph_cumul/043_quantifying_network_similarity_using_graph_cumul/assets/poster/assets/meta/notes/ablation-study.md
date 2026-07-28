# Ablation Study

Core claim: Varying the maximum subgraph order r shows the divergence clearly: at r = 1 neither test can separate the density-matched real networks; at r = 2 cumulants already outperform moments; at r = 3 cumulants keep improving while moments perform worse.

Supporting detail: Sweeping the SBM parameters ε_h and ε_a and the sample size s confirms the qualitative advantage of cumulants is robust across regimes.

Narration: A clean ablation over subgraph order tells the story on real data. Using only single edges, at order one, neither test can separate the density-matched networks, exactly as expected. Adding two-edge subgraphs already tips the balance in favor of cumulants. Adding three-edge subgraphs pushes the cumulant test further ahead, while the moment test starts to overfit and slip backward. Sweeping the block-model parameters and the sample size confirms this advantage is not a quirk of one setting but a robust, qualitative feature.
