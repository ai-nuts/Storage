# Motivation

Core claim: Because most real-world graph nodes have low degree, small ℓ₀ budgets can already remove a node from its entire original neighbourhood, so unnoticeability heuristics like degree distribution do not guarantee unchanged semantics.

Supporting detail: Prior defenses assume every prediction change under a small budget is an adversarial failure; if the semantics actually changed, that framing mismeasures robustness.

Narration: The belief that graph neural networks are easily fooled rests on the assumption that the perturbations used are semantics-preserving. Only a few works go beyond simple edge counts, adding proxies like the degree distribution or homophily metrics. None of them directly measure whether the ground-truth label is preserved. This matters because if a "small" perturbation has actually changed a node's true class, then a model that keeps its prediction fixed is not being robustly correct, it is being wrong in a new and hidden way. The authors argue we need a principled, label-aware notion of what a semantics-preserving graph perturbation really is.
