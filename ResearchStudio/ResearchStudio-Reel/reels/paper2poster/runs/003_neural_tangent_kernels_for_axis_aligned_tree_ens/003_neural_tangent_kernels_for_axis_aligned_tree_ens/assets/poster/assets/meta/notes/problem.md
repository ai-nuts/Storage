# Problem

Core claim: Soft tree ensembles are trained by gradient descent and perform strongly on tabular data, yet little theory explains their training dynamics, generalization, or the empirical tricks used to train them.

Supporting detail: Unlike hard decision trees, soft trees make splits differentiable and update all parameters jointly, but this gradient view has had no kernel-theoretic foundation.

Narration: Tree ensembles and neural networks are two of the most widely used model families. A soft tree is a decision tree whose splitting rules are made differentiable, so the whole model trains by gradient descent instead of greedy search. Ensembles of soft trees excel on tabular data, and practitioners rely on tricks like parameter sharing, adjusting split hardness, and over-parameterization. Yet almost no theory explains why they work. This paper fills that gap.
