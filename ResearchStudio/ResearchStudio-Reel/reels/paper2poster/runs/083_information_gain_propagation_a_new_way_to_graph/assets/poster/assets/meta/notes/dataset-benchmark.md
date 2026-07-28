# Dataset / Benchmark

Core claim: Evaluated on three citation networks (Cora, Citeseer, PubMed), one large social network (Reddit), and one OGB graph (ogbn-arxiv), under a fixed labeling-cost budget rather than a fixed label count.

Supporting detail: Budget is measured as query cost (money), with an exact query costing c−1× a relaxed query; budgets ranged from 2C to 20C labels (C = number of classes).

Narration: IGP is evaluated on five graph benchmarks: the citation networks Cora, Citeseer, and PubMed, the large social network Reddit, and the Open Graph Benchmark dataset ogbn-arxiv. Crucially, the budget is defined as true annotation cost, not a count of labels, since an exact query is far pricier than a binary one. Budgets vary from two to twenty labels per class.
