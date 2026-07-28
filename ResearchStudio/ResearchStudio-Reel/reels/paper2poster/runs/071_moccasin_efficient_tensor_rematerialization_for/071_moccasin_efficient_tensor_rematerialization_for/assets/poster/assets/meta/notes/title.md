# Title

Deploying and training neural networks on edge devices is often bottlenecked by tight memory. Tensor rematerialization, recomputing intermediate tensors instead of storing them, trades extra compute for lower peak memory. This paper introduces Moccasin, a new constraint programming formulation for the problem of minimizing execution time under a memory budget. Unlike prior work that needs a quadratic number of Boolean variables, Moccasin uses only a linear number of integer variables, letting it scale to much larger compute graphs and run up to an order of magnitude faster.
