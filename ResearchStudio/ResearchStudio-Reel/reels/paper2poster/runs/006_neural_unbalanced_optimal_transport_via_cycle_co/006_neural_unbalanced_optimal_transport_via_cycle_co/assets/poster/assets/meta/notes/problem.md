# Problem

Core claim: Predicting how an unpaired population evolves under an intervention when measurement is destructive; classical optimal transport assumes conserved mass, which fails when population size changes via cell proliferation or death.

Supporting detail: In single-cell biology the same cell cannot be measured twice, so correspondences across time points must be inferred from unpaired replicas of the population.

Narration: A recurring problem in the natural sciences is modeling how a population changes after an intervention, when you can only observe unpaired snapshots rather than track individuals. In single-cell biology this is unavoidable, because profiling a cell destroys it, so the same cell can never be measured twice. Optimal transport offers a principled way to infer these correspondences by learning an optimal coupling between distributions. But the standard formulation assumes conservation of mass, meaning every unit of source mass must be transported somewhere. That assumption is violated exactly when it matters most, in unbalanced settings where cells proliferate or die, and the total population size shifts between measurements.
