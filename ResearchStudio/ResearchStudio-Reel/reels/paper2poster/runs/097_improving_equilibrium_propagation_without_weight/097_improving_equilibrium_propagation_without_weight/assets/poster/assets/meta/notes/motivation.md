# Motivation

Core claim: Physical neural substrates (brains, analog hardware) could train networks at far lower energy, but backprop's linear backward pass and transposed weights are biologically implausible, motivating EP alternatives that must survive imperfect, asymmetric connectivity.

Supporting detail: Generalized (asymmetric) EP had only been shown on MNIST and fails on CIFAR-10, so its poor scaling was an open, unexplained failure mode.

Narration: The reason this matters is energy. Physical neural systems, whether biological brains or neuromorphic chips, could train networks at a tiny fraction of the energy cost of digital hardware. But backpropagation, the workhorse of deep learning, needs a separate linear backward pass and the exact transpose of every weight matrix, neither of which physical substrates provide naturally. EP sidesteps this, yet its own symmetry assumption is nearly as demanding. And there was a warning sign: the asymmetric version of EP had only ever worked on toy tasks like MNIST and outright failed on CIFAR-10. Nobody had explained why.
