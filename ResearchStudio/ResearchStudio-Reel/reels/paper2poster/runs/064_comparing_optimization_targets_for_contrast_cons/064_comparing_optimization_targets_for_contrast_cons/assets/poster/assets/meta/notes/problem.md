# Problem

Core claim: Contrast-Consistent Search (CCS) recovers a language model's internal "truth" direction, but what its loss actually optimizes for, and whether that target is optimal, is poorly understood.

Supporting detail: CCS is presented as learning truth probabilities via a negation-consistency constraint, yet the mechanism behind its success has not been isolated or explained.

Narration: CCS recovers a direction in a model's activations encoding whether a statement is true or false, using no labels, only the constraint that a statement and its negation disagree. Yet nobody had pinned down what its loss really optimizes, or whether that target is best.
