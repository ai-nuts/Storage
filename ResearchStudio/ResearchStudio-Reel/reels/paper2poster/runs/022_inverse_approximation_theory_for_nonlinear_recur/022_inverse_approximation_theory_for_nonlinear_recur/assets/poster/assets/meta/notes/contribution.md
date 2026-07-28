# Contribution

Core claim: The paper (1) generalizes the memory function from linear to nonlinear functional sequences in a numerically queryable form, (2) introduces a notion of stable approximation tied to perturbation continuity, and (3) proves the first Bernstein-type inverse approximation theorem for nonlinear RNNs.

Supporting detail: It further proposes stable reparameterization as a principled remedy and validates it numerically, including on sentiment analysis and MNIST.

Narration: The paper makes three main contributions. First, it extends the concept of a memory function from the linear setting to general nonlinear functional sequences, and crucially this memory function can be numerically quantified by querying a trained model, not just defined abstractly. Second, it introduces a framework of stable approximation, a mild requirement that the approximant behaves continuously under small parameter perturbations, which is exactly what gradient-based optimization needs. Third, using these two ingredients it proves what the authors believe is the first Bernstein-type approximation theorem for nonlinear RNNs. On top of the theory, it proposes a principled reparameterization method to overcome the identified limitation and confirms the whole story with experiments.
