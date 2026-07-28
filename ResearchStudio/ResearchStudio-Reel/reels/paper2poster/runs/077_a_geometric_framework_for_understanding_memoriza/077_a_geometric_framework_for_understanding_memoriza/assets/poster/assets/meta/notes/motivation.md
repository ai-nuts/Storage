# Motivation

Core claim: A geometric view grounded in the manifold hypothesis promises tractable, scalable memorization detection where probability-mass-based theory does not, and can unify the many scattered empirical "memorization phenomena" reported in the literature.

Supporting detail: Earlier probabilistic definitions require access to the full training set and huge numbers of samples, which is intractable at scale; a manifold-dimension perspective admits estimators that remain tractable for Stable Diffusion.

Narration: The manifold hypothesis says realistic data lives on a low-dimensional manifold embedded in a high-dimensional space. The authors argue that this geometry is exactly the right lens for memorization. Purely probabilistic frameworks demand the whole training dataset and enormous sample counts, which is hopeless at LAION scale. A geometric framing, by contrast, connects memorization to a quantity — local intrinsic dimension — for which practical estimators already exist, even for large diffusion models.
