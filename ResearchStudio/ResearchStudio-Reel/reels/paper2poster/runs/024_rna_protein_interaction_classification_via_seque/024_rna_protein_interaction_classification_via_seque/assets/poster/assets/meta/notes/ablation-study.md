# Ablation Study

Core claim: Replacing either the RNA-FM or ESM-2 embedding with a random embedding, or both with one-hot encodings, causes the model to collapse into a negative-only classifier: precision, recall and F1 all drop to 0.0, with accuracy stuck at 0.624 (merely the negative class fraction). The full two-embedding model instead reaches F1 0.605 and accuracy 0.678.

Supporting detail: This shows both foundation-model embeddings are individually necessary — neither structural/functional signal can be dropped or replaced by a simpler representation without breaking the model.

Narration: To test whether the two embeddings really matter, the authors retrain the model after swapping out the RNA embedding, the protein embedding, or both, for random vectors or one-hot encodings. In every one of these variants the model stops working, predicting only the negative class, so its F1 score falls to zero and its accuracy merely reflects the fraction of negatives in the data. Only when both the RNA-FM and ESM-2 embeddings are present does the model classify correctly. This confirms that the foundation-model embeddings carry the structural and functional information the task depends on.
