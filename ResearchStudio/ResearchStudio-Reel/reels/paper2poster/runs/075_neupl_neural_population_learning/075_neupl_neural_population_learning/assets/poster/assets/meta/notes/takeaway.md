# Takeaway

Core claim: By holding an entire policy population inside one opponent-conditioned network, NeuPL turns population learning from a sequence of wasteful from-scratch iterations into a single transfer-rich training run — where new strategies become more accessible as the population grows.

Supporting detail: The same framework recovers self-play, fictitious play, and PSRO by swapping the interaction graph, and scales from rock-paper-scissors up to MuJoCo Football.

Narration: "The one-line takeaway: represent the whole population in a single conditional model, let the interaction graph decide who trains against whom, and skills transfer for free across policies. This makes population learning cheaper, gives it convergence guarantees, and — most surprisingly — makes novel strategies more accessible, not less, as the neural population expands, from rock-paper-scissors all the way up to MuJoCo Football."
