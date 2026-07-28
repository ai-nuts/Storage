# Takeaway

Core claim: Repelling ensemble members in the low-dimensional space of their input gradients guarantees functional diversity cheaply and, with PCA-based lengthscales, produces ensembles that are substantially more robust and better calibrated under input corruptions than deep ensembles.

Supporting detail: Choosing where to apply repulsion, not just how much, is the key lever: input gradients are the sweet spot between over-parameterized weights and intractable function comparisons.

Narration: The lasting message of this paper is that the space in which you enforce diversity matters as much as the amount. By repelling ensemble members in the compact space of their input gradients, FoRDE guarantees that members become genuinely different functions that rely on complementary features, without the waste of weight-space repulsion or the intractability of function-space repulsion. Combined with data-driven lengthscales from principal component analysis, this yields ensembles that are more robust and better calibrated under the kinds of input corruptions that matter in the real world.
