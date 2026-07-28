# Title

Mixture models usually blend simple distributions by adding them. But what if a mixture could also subtract probability mass? Published at ICLR 2024, this paper shows how to learn deep subtractive mixtures by squaring them. Squaring keeps the model a valid distribution while allowing negative parameters, and the authors prove these squared non-monotonic circuits can be exponentially more compact than ordinary additive mixtures, then confirm the gain on real-world density estimation and language-model distillation.
