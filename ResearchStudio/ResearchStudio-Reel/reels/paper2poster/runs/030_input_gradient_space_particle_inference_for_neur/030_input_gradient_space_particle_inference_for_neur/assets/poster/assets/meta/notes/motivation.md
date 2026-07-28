# Motivation

Core claim: A function can be represented up to a translation by its first-order input gradients, which are much smaller than the weight vector, so repelling in input-gradient space guarantees functional difference cheaply.

Supporting detail: Diversifying input gradients pushes each member to rely on different input features, which is expected to improve robustness of the ensemble under input perturbations.

Narration: The authors take a third view of a neural network. Beyond its weights and its function values, a model can be represented, up to a translation, by its first-order input gradients, that is, the derivatives of the output with respect to the input. This representation has two attractive properties. First, input gradients are the same size as the input, which is far smaller than the enormous weight vector, so they are much cheaper to compare with a kernel. Second, forcing members to have different input gradients means forcing them to depend on different input features. Intuitively, this should make the ensemble more robust, because if members react to complementary patterns, corrupting one pattern will not fool all of them at once.
