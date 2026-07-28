# Contribution

Core claim: NeuPL represents an entire policy population inside one opponent-conditioned neural network, unifying self-play, fictitious play, and PSRO as different interaction graphs, with convergence guarantees to an N-step best-response.

Supporting detail: The framework delegates the effective population size to the meta-graph solver (no handcrafted truncation), enables transfer learning across policies, and admits cyclic interaction graphs beyond PSRO's scope.

Narration: "NeuPL makes three contributions. First, it is a single conditional model that represents a whole population of policies, conditioned on a meta-game mixture strategy that specifies which opponents each policy should beat. Second, it is a unifying framework: by choosing the interaction graph you recover self-play, fictitious play, or PSRO-Nash as special cases, and you can even express cyclic graphs that PSRO cannot. Third, it comes with convergence guarantees — for grounded, lower-triangular interaction graphs and a suitable meta-graph solver, NeuPL provably converges to an N-step best-response and, with large enough N, to a normal-form Nash equilibrium."
