# Motivation

Core claim: Compressing a matrix by both factorizing it into low-rank factors and quantizing those factors can multiply the savings, but naive combinations lose accuracy fast at aggressive bit budgets.

Supporting detail: Computing a full SVD is O(nd²) and infeasible for very large matrices on current GPUs, so a cheaper randomized route to low-rank-plus-low-precision factors is needed.

Narration: If a matrix is low rank, we can write it as a tall factor times a wide one, and storing those in low precision saves more. But doing this crudely at low bit budgets degrades accuracy fast, and the exact SVD route costs order n d squared, prohibitive at scale. It seeks a randomized way to get both factors with small, analyzable error.
