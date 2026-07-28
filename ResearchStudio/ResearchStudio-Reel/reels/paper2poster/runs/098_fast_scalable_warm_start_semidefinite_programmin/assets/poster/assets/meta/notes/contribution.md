# Contribution

Core claim: USBS is a unified spectral bundle method for general SDPs with both equality and inequality constraints that supports warm-starting, is provably convergent, and, with optional matrix sketching, scales to massive instances while sustaining convergence speed.

Supporting detail: The authors prove non-asymptotic convergence rates, let the user trade per-iteration complexity against convergence speed via the model parameters, and release a standalone pure-JAX implementation that runs on CPU, GPU, and TPU.

Narration: This paper presents USBS, a unified spectral bundle method with sketching. It makes several contributions. First, it handles general SDPs with both equality and inequality constraints, unlike prior spectral bundle methods. Second, it can be augmented with an optional matrix sketching technique that dramatically improves scalability while keeping convergence fast. Third, it reliably leverages warm-start initializations. The method comes with provable non-asymptotic convergence guarantees, and it exposes parameters that let the user trade off per-iteration cost against convergence speed. Finally, the authors release a standalone implementation in pure JAX that runs efficiently on CPUs, GPUs, and TPUs.
