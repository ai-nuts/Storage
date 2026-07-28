# Contribution

Core claim: A model-based doubly robust procedure that tests the stationarity assumption and detects change points in offline RL, controlling type-I error as long as either the transition function or the marginal state-action distribution is correctly specified.

Supporting detail: Theoretical guarantees for size and double robustness under a bidirectional asymptotic framework (either the number of trajectories N or the horizon T may diverge), plus a Gaussian multiplier bootstrap for valid p-values.

Narration: The paper's core contribution is a model-based, doubly robust procedure that tests the stationarity assumption and locates change points in offline reinforcement learning. Doubly robust means the test controls the type-one error as long as either the transition function or the marginal state-action distribution is correctly specified, so you get valid inference even when one nuisance model is wrong. On top of the method, the authors prove size control and double robustness under a bidirectional asymptotic framework, where either the number of trajectories or the length of the horizon may grow to infinity, and they supply a Gaussian multiplier bootstrap to compute honest p-values.
