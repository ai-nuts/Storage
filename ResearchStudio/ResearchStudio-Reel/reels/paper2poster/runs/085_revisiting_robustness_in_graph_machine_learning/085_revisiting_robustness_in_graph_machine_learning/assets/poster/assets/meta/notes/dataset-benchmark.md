# Dataset / Benchmark

Core claim: Experiments use Contextual Stochastic Block Models (CSBMs) with n = 1000 nodes parametrized to match CORA (p = 0.63%, q = 0.15%, d = 21), plus the real-world Cora-ML graph and a Contextual Barabási-Albert model with community structure (CBA).

Supporting detail: The signal strength K is varied from K = 0.1 (almost no discriminative features) to K = 5 (structure unnecessary); for each K, 10 training graphs are sampled and 1000 nodes are inductively added at test time, with an 80/20 train/validation node split.

Narration: The controlled experiments run on Contextual Stochastic Block Models, which let the authors compute the Bayes optimal reference exactly. Each graph has one thousand nodes and is parametrized to mimic CORA, matching its expected number of same-class and different-class edges. A parameter K controls how discriminative the node features are, swept from zero-point-one, where features carry almost no signal and structure matters most, up to five, where structure becomes unnecessary. They inductively sample a thousand test nodes per graph and average over ten graphs. Results are corroborated on the real-world Cora-ML graph and on a Barabási-Albert model with community structure.
