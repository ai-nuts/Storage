# Motivation

Core claim: A good expressiveness measure should be interpretable and constructive, pointing directly at operations a model is missing, rather than only certifying pass or fail on an isomorphism test.

Supporting detail: Prior work characterized only low-order equivariant maps or leaned on WL, leaving a gap for a complete, computation-friendly description of what a GNN should be able to output.

Narration: The authors argue the right way to grade a graph network is by the quantities it can compute. Equivariant polynomials, polynomials of the adjacency matrix that respect node relabeling, are natural candidates: subgraph counts and many structural features are exactly such polynomials. Knowing their full space, and which a network can evaluate, gives both a fine-grained ruler and a to-do list of missing operations.
