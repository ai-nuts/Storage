# Dataset / Benchmark

Core claim: Evaluated on two standard citation-graph node-classification benchmarks: Cora-ML (2,810 nodes, 7,981 edges, 7 classes) and Citeseer (2,110 nodes, 3,668 edges, 6 classes), with GCN and GAT (hidden size 64) as base classifiers.

Supporting detail: Injected-node budget ρ ∈ {20, 50, 80, 100, 120, 140, 160}; per-node degree τ set to the graph's average degree (6 for Cora-ML, 4 for Citeseer). Smoothed classifier estimated by Monte Carlo with N = 100,000 samples, α = 0.01, and LPs solved with MOSEK via CVXPY.

Narration: The evaluation uses two standard citation graphs, Cora-ML and Citeseer, with a few thousand nodes each, and two representative backbones, a graph convolution network and a graph attention network. The attacker's budget is swept from twenty up to a hundred and sixty injected nodes, with the per-node edge limit set to each graph's average degree. The smoothed classifier is estimated with a hundred thousand Monte Carlo samples at a one percent confidence level, and every linear program is solved with the MOSEK solver through CVXPY.
