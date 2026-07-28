# Dataset / Benchmark

Core claim: Synthetic binary classification tasks generated from the paper's data model, with M₁ = 6 in-domain-relevant patterns and M₂ = 24 irrelevant patterns; models are the analyzed one-layer Transformer and a 3-layer, 2-head GPT-2.

Supporting detail: Training uses α = 0.8 and context length l = 20; out-of-domain tests use M₁′ = 3 relevant patterns that are linear combinations of the training patterns. Classification error is measured as the probability of a sign mismatch between prediction and label.

Narration: Experiments use a controlled synthetic setup that matches the theory. There are six in-domain relevant patterns and twenty-four irrelevant ones, and tasks are binary classifications built from these patterns. Two models are trained: the one-layer Transformer that the theory analyzes, and a small real-world GPT-2 with three layers and two heads. Training uses a context length of twenty and a relevant-pattern fraction of eighty percent, and out-of-domain evaluation uses new tasks whose relevant patterns are linear combinations of the training patterns, exactly the regime the theorems cover.
