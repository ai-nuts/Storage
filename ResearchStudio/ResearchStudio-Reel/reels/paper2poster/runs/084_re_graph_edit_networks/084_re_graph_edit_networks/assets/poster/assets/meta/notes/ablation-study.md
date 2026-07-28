# Ablation Study

Core claim: Swapping random-graph initialisation for the Erdős–Rényi and Configuration models leaves all metrics within 0.05 of the reported values, and the stricter risk-estimation protocol with a 100-graph held-out test set shifts scores only by δ ∈ [−0.1, 0.05].

Supporting detail: A diagnostic sampling study shows the tree DGPs rarely produce simplifiable trees, only 13% for Boolean Formulae and 26% for Peano Addition, casting doubt on how much the benchmarks actually test the model.

Narration: Two robustness checks: swapping the ad-hoc initialisation for Erdős–Rényi and configuration-model generators barely changes any metric, and adding a proper held-out test set lowers scores slightly. But a deeper diagnostic finds the tree generators mostly produce unsimplifiable trees, only thirteen percent of Boolean and twenty-six percent of Peano samples are usable, undercutting those tasks.
