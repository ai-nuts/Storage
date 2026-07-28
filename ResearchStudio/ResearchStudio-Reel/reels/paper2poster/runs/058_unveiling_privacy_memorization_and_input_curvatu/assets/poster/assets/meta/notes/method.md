# Method

Core claim: Under error-stability, generalization, uniform-model-bias, and dataset adjacency assumptions with bounded loss, a second-order (Nesterov-Polyak) expansion of the loss plus DP definitions yield the three bounds. Curvature is estimated efficiently via Hutchinson's trace estimator.

Supporting detail: Bounds are validated using Feldman & Zhang's precomputed memorization scores and models (1000 for CIFAR100, 100 for ImageNet); privacy models are trained with DP-SGD at several epsilon budgets. Curvature uses step h=1e-3 and n=10 Rademacher vectors.

Narration: The theory starts from a second-order Nesterov-Polyak expansion of the loss, introducing the input Hessian. A zero-mean perturbation cancels first-order terms, and taking expectations bounds memorization by expected curvature plus a data-independent offset. With the definition of differential privacy, a smaller epsilon forces lower curvature. Curvature itself is estimated cheaply via Hutchinson's trace estimator.
