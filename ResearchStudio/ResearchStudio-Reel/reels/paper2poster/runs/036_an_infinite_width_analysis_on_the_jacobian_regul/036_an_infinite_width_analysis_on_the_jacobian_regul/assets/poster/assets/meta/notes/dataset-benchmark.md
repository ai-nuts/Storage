# Dataset / Benchmark

Core claim: Kernel-convergence tests use a synthetic 256-point dataset in R⁴ approximating an ε-net of the sphere S³, over all width-depth combinations in {2⁶,…,2¹³} × {1,2,3}. The constancy-during-training test uses the Algerian forest fire dataset (UCI, 224 points, input dimension 11) treated as a ±1 regression task.

Supporting detail: Robust and standard training solutions are compared on the same setups; an 11-layer GeLU MLP is used for the kernel-regression robustness study.

Narration: The experiments are deliberately small and controlled. To test the kernel-convergence claims, the authors use a synthetic 256-point dataset in four dimensions, built to approximate an even covering of the sphere, and sweep every combination of width from 64 up to 8192 and depth one, two, and three. To test that the kernel really stays constant during robust training, they switch to the Algerian forest fire dataset from the UCI repository, 224 points with eleven input features, treated as a plus-or-minus-one regression problem. The same setups let them line up robust training against standard training head to head.
