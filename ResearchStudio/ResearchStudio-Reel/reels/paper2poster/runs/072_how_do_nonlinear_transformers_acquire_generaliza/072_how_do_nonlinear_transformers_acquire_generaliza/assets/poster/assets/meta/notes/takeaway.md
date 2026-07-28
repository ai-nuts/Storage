# Takeaway

Core claim: A one-layer Transformer with genuinely nonlinear attention and MLP can be provably trained to perform in-context learning that generalizes both in-domain and under distribution shift, with training cost governed by the fraction of relevant context, and its low-magnitude MLP neurons can be pruned almost for free.

Supporting detail: The mechanism: attention concentrates on context examples sharing the query's relevant pattern, and the ReLU MLP promotes their label embeddings, so magnitude-based pruning that keeps the large neurons preserves ICL.

Narration: The lasting message is that in-context learning in a nonlinear Transformer is not a black box: with both nonlinear attention and a nonlinear MLP, a one-layer model can be provably trained to generalize in context, in-domain and under distribution shift, and the effort it takes is controlled by how much of the context shares the query's relevant pattern. The trained model works by having attention focus on the context examples that match the query's relevant pattern while the ReLU MLP amplifies their labels. Because only the large-magnitude neurons carry this signal, pruning the small ones is essentially free, giving a principled reason why magnitude-based pruning preserves in-context learning.
