# Problem

Core claim: GNNs need many labeled nodes, and existing graph active-learning methods assume an oracle can name the exact class of every selected node, an expensive multi-class query that exceeds expert capability when categories are many.

Supporting detail: Exact labeling is costly, especially out-of-domain (e.g. ogbn-papers100M has 172 classes), so hard-label queries do not scale with the number of categories.

Narration: Graph neural networks rely on large amounts of labeled data, which is costly to obtain. Active learning cuts this cost by selecting the most valuable nodes to label. But every prior method assumes an oracle can always name a node's exact class. When categories are many or the domain is unfamiliar, that multi-class question is too demanding, and the budget is spent inefficiently.
