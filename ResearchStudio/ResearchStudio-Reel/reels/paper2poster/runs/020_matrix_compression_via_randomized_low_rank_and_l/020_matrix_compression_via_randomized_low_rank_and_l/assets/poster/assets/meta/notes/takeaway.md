# Takeaway

Core claim: Jointly exploiting low rank and low precision through a randomized Gaussian sketch, LPLR compresses matrices to roughly one bit per entry with provable error bounds, matching or beating standard compression on images, embeddings, and LLM weights at a fraction of the cost of an SVD.

Supporting detail: The equalization property of Gaussian embeddings is the key enabler, keeping quantization error bounded even at 1-bit precision.

Narration: The takeaway: low rank and low precision are complementary, and exploiting them together pays off. By sketching a matrix with a Gaussian projection and quantizing the factors, LPLR compresses to one bit per coordinate while preserving accuracy on images, embeddings, and LLM weights, with provable error bounds. And by avoiding costly SVD, it scales to largest matrices.
