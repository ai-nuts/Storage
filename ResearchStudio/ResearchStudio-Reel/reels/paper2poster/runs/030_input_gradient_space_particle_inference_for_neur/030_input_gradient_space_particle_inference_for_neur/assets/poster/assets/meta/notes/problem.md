# Problem

Core claim: Deep ensembles gain accuracy and calibration from functional diversity, but weight-space repulsion is inefficient under over-parameterization and function-space repulsion barely improves over plain deep ensembles.

Supporting detail: Comparing whole functions requires an intractable function kernel; prior work compared functions only on training inputs, which causes underfitting and no real gains over vanilla deep ensembles.

Narration: Ensembles of neural networks are powerful because different members capture different explanations of the data. Particle-based variational inference tries to make this diversity explicit by adding a repulsion term that pushes members apart. But where you apply that repulsion matters. Repelling in weight space is wasteful, because neural networks are heavily over-parameterized and many different weights encode the same function. Repelling directly in function space sounds appealing, but it requires comparing entire functions, which is computationally hard, and the shortcuts used in prior work led to underfitting. So neither weight-space nor function-space repulsion had delivered meaningful gains over standard deep ensembles.
