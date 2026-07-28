# Motivation

Core claim: A dataset-and-attacker-specific lower bound on robust loss is a diagnostic tool: it lets practitioners measure progress for defenses against an absolute optimum instead of only against other defenses.

Supporting detail: Prior lower bounds restricted the hypothesis class to binary classifiers, so the far more common multi-class regime, where higher-order interactions between examples appear, was uncharacterized.

Narration: Comparing the robustness of the best possible classifier to what state-of-the-art training achieves is a powerful diagnostic. It tells you whether the bottleneck is your training method or a fundamental limit of the data and threat model. Past work delivered this only for two classes. Moving to many classes is not a trivial extension: with three or more classes, examples can interact in higher-order ways that binary analysis simply cannot capture, and these interactions can change what optimal robustness looks like.
