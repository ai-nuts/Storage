# Motivation

Core claim: It is widely hypothesized that different attention heads learn different relational biases, suggesting a mixture of attention types might outperform any single one; this paper tests whether that intuition holds.

Supporting detail: Trying every attention mechanism (and every combination) by brute-force training is prohibitively expensive, motivating a cheap search-based selection method.

Narration: There is a long-standing intuition that each attention head can specialize, learning a different kind of relationship, much as convolutional kernels learn different features. If that is true, then a Transformer mixing several attention types could learn a richer set of relationships and outperform any single-attention model. This paper takes that intuition seriously and asks directly whether the optimal attention for a task is actually a mixture of different attentions, rather than assuming the answer.
