# Contribution

Core claim: The paper introduces Moment Unfolding, a dedicated machine-learning technique that directly unfolds statistical moments of an observable in an unbinned, non-iterative way, using a reweighting function whose parameters are identified with the moments.

Supporting detail: The generator's form is inspired by the Boltzmann equation and the training structure is adapted from a Generative Adversarial Network; unlike iterative methods such as OmniFold, one pair of networks is trained only once.

Narration: The core contribution is Moment Unfolding, a new unbinned and non-iterative reweighting technique. It learns a reweighting function, playing the role of a GAN generator, whose form is inspired by the Boltzmann factor so that its trainable parameters can be directly identified with the observable's moments. A discriminator pushes the reweighted simulation to match the target data. Unlike OmniFold, which trains a fresh pair of networks on every iteration, Moment Unfolding trains a single pair of networks just once.
