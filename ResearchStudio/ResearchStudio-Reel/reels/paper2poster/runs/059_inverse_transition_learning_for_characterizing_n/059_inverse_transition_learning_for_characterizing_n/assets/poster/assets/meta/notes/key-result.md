# Key Result

Core claim: The clipped posterior P(T|D, πϵ) enforces 100% ± 0 accuracy on deterministic-policy states in every setting (vs MLE's 67-92%) and never picks an action outside the expert's ε-ball, so it dominates both MLE and the un-clipped posterior P(T|D) on the Q*metric.

Supporting detail: On stochastic-policy states the constraints, though silent about which action to take, still yield higher accuracy than MLE and P(T|D), showing the constraints implicitly transfer uncertainty structure.

Narration: The clipped posterior dominates both maximum likelihood and the un clipped Bayesian posterior. It guarantees one hundred percent accuracy on states where the expert knows the single best action, in every data and optimality setting, whereas maximum likelihood ranges from sixty seven to ninety two percent. It also never selects an action outside the expert's epsilon ball, so it makes no truly bad mistakes. Strikingly, even though the constraints say nothing explicit about which action to pick in uncertain states, our method is still more accurate there than the baselines, which means the constraints implicitly transfer the expert's uncertainty structure.
