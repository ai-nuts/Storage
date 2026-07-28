# Takeaway

Core claim: CFG is just the first-order Taylor term of inner classifier-free guidance; adding the second-order term gives Stable Diffusion a better fidelity–diversity balance for free, with no retraining.

Supporting detail: By choosing a condition space with a well-defined "cone" structure, ICFG naturally extends to higher orders, offering a principled path beyond standard guidance.

Narration: The takeaway is simple. Classifier-free guidance is just the first-order slice of a richer picture. Treat the guided score as a Taylor expansion in the guidance strength, and a single extra second-order term buys you a better fidelity-diversity trade-off. It needs no retraining, only a scaled condition and a few lines of code, and it points toward exploiting the continuous condition structure that plain CFG throws away.
