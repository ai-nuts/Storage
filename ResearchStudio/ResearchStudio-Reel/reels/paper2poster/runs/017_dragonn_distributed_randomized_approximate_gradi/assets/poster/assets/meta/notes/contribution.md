# Contribution

Core claim: (1) DRAGONN, a randomized hashing algorithm for GS that reduces compression overhead while preserving iteration-wise accuracy, with theoretical bounds on compression and generalization error. (2) System-level optimizations: efficiency-aware tensor selection and sparse decoding. (3) Extensive vision and recommendation evaluation showing large end-to-end speedups.

Supporting detail: DRAGONN supports massively parallel gradient extraction because independent threads can hash and write indices simultaneously without ordering dependencies.

Narration: The paper makes three contributions. First, it proposes DRAGONN, a hashing-based sparsification algorithm that slashes compression overhead while keeping the same per-iteration convergence, backed by theoretical bounds on both compression error and generalization error. Second, it adds two system-level optimizations: an efficiency-aware tensor selection that only compresses tensors where it actually pays off, and a sparse decoding scheme that keeps decode cost from growing with the number of GPUs. Third, it evaluates the method broadly across vision and recommendation models and demonstrates substantial end-to-end training speedups.
