# Motivation

Core claim: Judging the exact class is much harder than confirming a guess. A relaxed yes/no query is cheaper per node, and prior uncertainty-based criteria ignore that a labeled node propagates information to its k-hop neighbors in a GNN.

Supporting detail: An exact multi-class query costs roughly c−1 times a binary query for c classes; prior criteria maximize single-node uncertainty, not graph-wide information gain.

Narration: Confirming a guess is far easier than naming the exact class. If an expert only answers a binary yes-or-no question, the labeling cost per node drops sharply, especially with many classes. Meanwhile, existing selection criteria were built for hard labels and only measure a single node's uncertainty. They ignore that in a graph network, labeling one node propagates supervision across its k-hop neighborhood.
