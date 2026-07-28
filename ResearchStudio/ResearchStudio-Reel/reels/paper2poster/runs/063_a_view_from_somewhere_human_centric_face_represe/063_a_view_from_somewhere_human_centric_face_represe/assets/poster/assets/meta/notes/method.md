# Method

Core claim: A conditional ResNet18 convnet maps faces to 128-dimensional embeddings and is trained on odd-one-out (3AFC) triplet judgments. Each annotator gets a learnable sigmoid mask that gates the embedding dimensions, so similarity is conditioned on who made the judgment.

Supporting detail: Setting all masks to ones recovers the unconditional MDS objective (AVFS-U); conditional variants are AVFS-C and post-hoc AVFS-CPH. A sparsity plus non-negativity penalty makes the surviving dimensions interpretable, yielding 22 active dimensions.

Narration: At the core is a conditional convolutional network, a ResNet eighteen, that maps each face to a one-hundred-twenty-eight-dimensional embedding. Training uses odd-one-out judgments: given a triplet of faces, an annotator picks the least similar one. Each annotator is assigned a learnable gating mask, passed through a sigmoid, that scales the importance of every embedding dimension for that person. Similarity between two faces is the dot product of their masked, rectified embeddings, and the model predicts the odd-one-out probability directly from these three pairwise similarities. A sparsity and non-negativity penalty keeps the dimensions few and interpretable, leaving only about twenty-two active dimensions.
