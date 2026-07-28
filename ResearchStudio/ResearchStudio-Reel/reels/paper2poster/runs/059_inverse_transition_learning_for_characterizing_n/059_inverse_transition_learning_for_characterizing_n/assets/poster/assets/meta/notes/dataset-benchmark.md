# Dataset / Benchmark

Core claim: Experiments use a synthetic tabular MDP with 15 states (+1 terminal) and 6 actions, discount γ=0.95, with dynamics that are sometimes uniform and sometimes highly skewed to create varied behavior.

Supporting detail: Two coverage regimes (low data K=15 episodes, high data K=300) are crossed with three optimality levels ε=0 (0 stochastic states), ε=3 (3 stochastic states), ε=4 (6 stochastic states); every result is averaged over 1000 datasets.

Narration: All experiments run on a synthetic tabular Markov decision process with fifteen states plus a terminal state and six actions, using a discount factor of zero point nine five. The true dynamics are deliberately mixed, sometimes uniform and sometimes highly skewed toward a few states, to create rich and varied behavior. We study two coverage regimes, a low data setting of fifteen episodes and a high data setting of three hundred, crossed with three levels of expert optimality that create zero, three, and six uncertain policy states. Every reported number is averaged over one thousand independently generated datasets.
