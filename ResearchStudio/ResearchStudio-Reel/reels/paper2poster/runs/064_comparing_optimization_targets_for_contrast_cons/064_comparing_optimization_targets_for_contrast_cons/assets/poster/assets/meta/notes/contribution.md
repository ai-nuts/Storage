# Contribution

Core claim: (1) Conceptual clarifications correcting two misconceptions about CCS (it classifies via translation-invariant displacement vectors, not a separating hyperplane, and can succeed even when its "probabilities" cluster near 0.5). (2) A heuristic account of CCS's optimization target and a new Midpoint-Displacement (MD) loss derived from it. (3) An empirical comparison of many loss functions across models and datasets showing MD is a good proxy for CCS and can outperform it.

Supporting detail: Two further loss functions (Mean Absolute, Square Mean Root) are introduced as baselines in the appendix.

Narration: The paper makes three contributions. First, it corrects two misconceptions: CCS classifies using only the displacement between a statement and its negation, needing no separating hyperplane, and succeeds even when probabilities cluster near one half. Second, it derives a new Midpoint-Displacement loss. Third, a comparison shows it proxies, and can beat, CCS.
