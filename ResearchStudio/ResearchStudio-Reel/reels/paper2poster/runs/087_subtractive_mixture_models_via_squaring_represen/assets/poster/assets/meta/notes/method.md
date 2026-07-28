# Method

Core claim: A shallow subtractive mixture uses unconstrained real weights and is squared to guarantee non-negativity; squaring a K-component mixture yields a product-of-experts form that can be renormalized tractably. This is lifted to deep tensorized structured-decomposable circuits by recursively squaring each layer, so deep squared non-monotonic PCs (NPC²s) remain tractable for marginalization and inference.

Supporting detail: Squared layers hold a quadratic number of units but still output vectors, so the partition function Z is computed once per batch, keeping the model efficient to train with gradient-based MLE.

Narration: Here is the core idea. Take a mixture with unconstrained real weights, so components can have negative coefficients, and simply square the whole thing. Squaring forces the output to be non-negative no matter what the weights are. Expanding the square turns a K-component mixture into a sum over all pairs of components, a product-of-experts form whose partition function can still be computed in closed form for many families. To go deep, the authors square a tensorized structured-decomposable circuit layer by layer. Each squared layer holds a quadratic number of units but still outputs a vector, so the whole model trains efficiently with gradient descent, computing the normalizer just once per batch.
