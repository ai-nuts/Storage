# Contribution

Core claim: A comprehensive analysis isolating the two bias sources (finite nudge vs. Jacobian asymmetry), an extension of holomorphic EP to asymmetric complex-differentiable systems, a new homeostatic loss reducing Jacobian asymmetry, and a demonstration that hEP scales to ImageNet 32×32.

Supporting detail: The homeostatic loss acts on the Jacobian rather than the weights, so it also works for architectures with no reciprocal connections at all.

Narration: This paper makes four contributions. First, it analytically separates the two sources of bias in generalized EP: the finite nudge and the asymmetry of the network's Jacobian. Second, it extends holomorphic EP to asymmetric, complex-differentiable systems, so the exact error can be recovered even without weight symmetry. Third, and most practically, it introduces a new homeostatic loss that reduces the asymmetry of the Jacobian directly, rather than forcing the weights themselves to be symmetric. And fourth, it demonstrates that with this loss, EP finally scales all the way up to ImageNet at thirty-two by thirty-two resolution.
