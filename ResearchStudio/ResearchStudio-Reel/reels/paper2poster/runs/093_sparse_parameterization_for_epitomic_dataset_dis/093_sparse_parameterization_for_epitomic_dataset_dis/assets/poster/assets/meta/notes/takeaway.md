# Takeaway

Core claim: How you parameterize the synthetic dataset matters as much as the matching objective: a shared epitomic-token dictionary with sparse per-image codes and a recurrent synthesizer removes spatial redundancy, delivering state-of-the-art distillation at a fraction of the storage, especially on high-resolution data.

Supporting detail: Sparse parameterization also improves generalization to unseen architectures and robustness to corruption, suggesting sparsity is a general lever for efficient, transferable synthetic data.

Narration: The lasting message of SPEED is that parameterization deserves as much attention as the matching objective. By treating a synthetic dataset as a shared dictionary of spatial-agnostic epitomic tokens, sparse per-image coding matrices, and a small recurrent network that reassembles them, SPEED removes the spatial redundancy that naive methods leave on the table. The payoff is state-of-the-art distillation at a fraction of the storage, biggest on high-resolution images, plus better generalization to unseen architectures and stronger robustness to corruption. In short, sparse, shared representation is a powerful and general lever for making tiny synthetic datasets do far more.
