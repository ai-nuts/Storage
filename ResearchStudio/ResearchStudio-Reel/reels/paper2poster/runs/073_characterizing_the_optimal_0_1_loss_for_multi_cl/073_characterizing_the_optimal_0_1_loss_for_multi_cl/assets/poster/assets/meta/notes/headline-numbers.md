# Headline Numbers

Core claim: - 3-class CIFAR-10: TRADES stuck near 0.6 loss where the optimal loss is ~0 - Best certifiably robust MNIST model: 0-1 loss 0.27 at budget 1.52 and 0.44 at budget 2.0, vs optimal lower bound of 0 - Best certifiably robust CIFAR-10 model: 0-1 loss 0.6 at budget 1.0 and 0.8 at budget 2.0, vs optimal lower bound of 0

Supporting detail: - CIFAR-10 at ε=3: ~3M degree-3 and ~10M degree-4 hyperedges with zero effect on the bound - Truncated bounds L(2)/L(3)/L*(4) coincide until loss > 0.4 (3-class)

Narration: The numbers make the gap concrete. On 3-class CIFAR-10, adversarial training plateaus near 0.6 loss at a budget where the optimal loss is essentially zero. State-of-the-art certifiably robust models fare no better against the optimum: the best MNIST model has 0-1 loss of 0.27 at budget one-point-five-two and 0.44 at budget two, while the achievable optimal lower bound is zero in both cases. On CIFAR-10, the best certified model reaches 0.6 loss at budget one and 0.8 at budget two, again against an optimal lower bound of zero. And on the structural side, millions of higher-degree hyperedges, three million of degree three and ten million of degree four at budget three, leave the bound completely unchanged.
