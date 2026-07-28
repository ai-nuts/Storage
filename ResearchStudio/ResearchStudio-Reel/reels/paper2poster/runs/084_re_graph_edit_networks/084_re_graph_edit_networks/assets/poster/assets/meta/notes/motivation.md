# Motivation

Core claim: The original GEN paper reports strong wins over baselines and favourable sub-quadratic and linear scaling, but the synthetic data generators and runtime claims were never described in enough detail to verify independently.

Supporting detail: Reproducibility matters most exactly where results look impressive on small, custom benchmarks whose difficulty is hard to judge from the paper alone.

Narration: Graph Edit Networks close this gap by predicting an explicit, human-readable edit script. The original work claims it beats every baseline, reaches perfect accuracy on trees, and scales to large graphs, but those claims rest on briefly-described benchmarks, where independent reproduction adds value.
