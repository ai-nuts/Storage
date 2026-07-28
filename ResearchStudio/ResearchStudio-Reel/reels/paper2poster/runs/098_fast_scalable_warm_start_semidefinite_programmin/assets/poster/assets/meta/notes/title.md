# Title

Semidefinite programming is a powerful tool for combinatorial optimization, but it has long been considered too expensive to run at real-world scale. This paper introduces USBS, Unified Spectral Bundling with Sketching, a provably correct solver that is fast, scales to billions of decision variables, and, crucially, can reuse a previous solution as a warm start. On a MaxCut instance with over two billion variables, USBS delivers a five-hundred-times speedup over the previous state of the art, and warm-starting alone can accelerate convergence by more than one hundred times.
