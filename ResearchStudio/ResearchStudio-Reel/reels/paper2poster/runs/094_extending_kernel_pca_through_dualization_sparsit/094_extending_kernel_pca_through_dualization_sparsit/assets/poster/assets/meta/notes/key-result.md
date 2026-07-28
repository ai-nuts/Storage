# Key Result

Core claim: At tolerance δ = 10⁻², the proposed L-BFGS solver is faster than every baseline and at least 3× faster than randomized SVD, reaching a 9.17× speedup on CIFAR-10 (n=60000); full SVD exceeded 30 minutes on the larger datasets.

Supporting detail: The solver is largely insensitive to the decay rate of G's eigenspectrum, whereas randomized SVD needs sharply more oversamples as the spectrum decays slowly (a common real-world regime).

Narration: On the efficiency benchmarks, the proposed solver wins across the board. At the looser tolerance of ten-to-the-minus-two, it is faster than full SVD, Lanczos, and randomized SVD on every task, and it is at least three times faster than randomized SVD, peaking at a nine-point-one-seven times speedup on CIFAR-10 with its sixty thousand images, where full SVD could not even finish within thirty minutes. Just as importantly, the method is robust to a property that hurts randomized SVD badly: as the eigenspectrum of the Gram matrix decays more slowly, randomized SVD needs many more oversamples, while the proposed solver's iteration count barely changes.
