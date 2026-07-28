# Problem

Core claim: Classical mixture models can only add non-negative components, so approximating distributions with "holes" or sharp structure needs a large, wasteful number of components.

Supporting detail: Allowing components to subtract mass can drastically cut the count, but learning such subtractive mixtures while guaranteeing a valid non-negative density is hard.

Narration: Traditional mixture models build complex distributions by blending simple ones additively. That works, but it can be wildly inefficient. If the target distribution has gaps or holes in its domain, an additive mixture must stack up many components just to carve those holes out. The natural fix is to let some components subtract probability mass instead of only adding it. The catch: once you allow subtraction, the model can dip below zero and stop being a valid distribution, and learning it becomes genuinely hard.
