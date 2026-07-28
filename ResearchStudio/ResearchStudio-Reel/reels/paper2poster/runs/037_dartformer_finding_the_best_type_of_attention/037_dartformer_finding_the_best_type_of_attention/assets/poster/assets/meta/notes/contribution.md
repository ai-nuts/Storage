# Contribution

Core claim: (1) A DARTS-like NAS framework that efficiently finds the best attention for a task; (2) an extension that searches for and builds heterogeneous (multi-attention) Transformers; (3) empirical evidence that heterogeneous Transformers cannot beat the best homogeneous Transformer on the tested long-range NLP tasks.

Supporting detail: Two concrete search procedures are introduced — "NAS Prune" (iterative removal of the worst block) and the far cheaper "NAS One-shot" (top-scoring blocks in a single pass).

Narration: The paper makes three contributions. First, it proposes DARTFormer, a differentiable-architecture-search-style method that efficiently finds the best attention for a task. Second, it extends that framework to build and search for heterogeneous Transformers that combine multiple attention types, using two procedures: an expensive iterative pruning method they call NAS Prune, and a cheap single-pass method called NAS One-shot. Third, and most importantly, it shows empirically that these heterogeneous Transformers cannot outperform the best homogeneous Transformer on the long-range NLP tasks studied.
