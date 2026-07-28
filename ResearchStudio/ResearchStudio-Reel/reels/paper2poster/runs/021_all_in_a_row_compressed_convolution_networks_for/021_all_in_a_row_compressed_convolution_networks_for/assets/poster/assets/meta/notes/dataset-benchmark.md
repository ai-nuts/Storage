# Dataset / Benchmark

Core claim: Graph classification uses six TU datasets — MUTAG, PROTEINS, NCI1, IMDB-BINARY, IMDB-MULTI, COLLAB — and node classification uses six heterophilic datasets — Chameleon, Squirrel, Cornell, Texas, Wisconsin, Actor.

Supporting detail: The authors additionally evaluate on de-duplicated filtered Chameleon/Squirrel and on three large-scale graphs (questions, amazon-ratings, genius) with mini-batch Cluster-GCN training to test scalability.

Narration: The evaluation is broad. For graph classification, six datasets: MUTAG, PROTEINS, NCI1, COLLAB, IMDB-Binary, and IMDB-Multi, under ten-fold cross-validation. For node classification, six heterophilic benchmarks: Chameleon, Squirrel, Cornell, Texas, Wisconsin, and Actor. To rule out leakage they test filtered Chameleon and Squirrel, and for scale, mini-batch experiments on three graphs with hundreds of thousands of nodes.
