# Takeaway

Core claim: Parallelism is the defining strength of transformers: they are, up to logarithmic depth, equivalent to Massively Parallel Computation, letting them solve in log k depth what serial architectures need depth k to handle.

Supporting detail: The k-hop induction heads task offers a crisp, empirically verified separation showing why depth and parallel structure, not raw scale, underlie transformers' algorithmic edge.

Narration: The one thing to remember is that transformers are, in a precise sense, parallel computers. This paper pins that intuition down by proving logarithmic-depth transformers are equivalent to constant-round Massively Parallel Computation. That equivalence explains both their power and their limits, and it predicts a sharp separation: on the k-hop induction heads task, transformers succeed with depth logarithmic in k, while recurrent models, state-space models like Mamba, and efficient attention approximations all need depth linear in k. Trained transformers obey the predicted threshold to the layer. So the real edge of the transformer is not just scale, it is the ability to do many things at once.
