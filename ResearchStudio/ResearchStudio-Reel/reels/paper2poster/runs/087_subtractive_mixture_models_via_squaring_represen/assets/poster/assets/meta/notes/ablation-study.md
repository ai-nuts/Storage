# Ablation Study

Core claim: Comparing NPC²s against squared monotonic PCs (MPC²) isolates the effect of negative parameters from squaring alone; negative parameters give the extra expressiveness, while binary-tree region graphs generally beat linear-tree ones.

Supporting detail: On continuous data, splines as input layers help NPC²s most; on discrete data, embeddings/Binomials matter more than categorical inputs, and on some image-mass tasks the advantage narrows.

Narration: To confirm the gains come from subtraction and not just squaring, the authors compare against squared monotonic circuits, which square but keep all parameters non-negative. The squared non-monotonic circuits still win, so the negative parameters are doing the real work. Two other patterns emerge: binary-tree region graphs generally beat linear-tree ones, and the input layer matters, with splines helping most on continuous data and embeddings on discrete data. On some discrete image-mass tasks the advantage narrows.
