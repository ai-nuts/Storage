# Takeaway

Core claim: Memorization in generative models is fundamentally about geometry: when the model's local intrinsic dimension is too low, the model memorizes — so measuring and raising LID both detects and mitigates memorization, even at Stable Diffusion scale.

Supporting detail: The MMH cleanly separates overfitting-driven from data-driven memorization, unifies disparate prior observations, and enables caption-free detection of memorized training images.

Narration: The single idea to walk away with is that memorization is geometric. If the model's local intrinsic dimension around a point is too small, that point is memorized — and this holds whether the cause is overfitting or the data being inherently simple. Because local intrinsic dimension can be estimated at scale, you can both detect memorized images, even without their captions, and mitigate memorization by steering generation toward higher-dimensional regions. The manifold memorization hypothesis turns a fuzzy, much-debated phenomenon into a measurable geometric quantity.
