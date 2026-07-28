# Dataset / Benchmark

Core claim: Evaluated on MNIST-scale (resolutions 8×8 to 28×28) and STL10-scale (resolutions 48 to 97), the standard benchmarks for scale-equivariant networks, under both ideal and non-ideal (Gibbs-ringing) downsampling.

Supporting detail: MNIST-scale uses 10k / 2k / 50k train/val/test; STL10-scale uses 7k / 1k / 5k. Data-efficiency is probed at 5k, 2.5k, and 1k training samples.

Narration: The authors follow prior work and evaluate on two benchmarks. MNIST-scale is built by randomly downsampling MNIST digits so that every resolution from eight-by-eight up to twenty-eight-by-twenty-eight is equally represented. STL10-scale applies the same construction to natural color images, spanning resolutions from forty-eight up to ninety-seven. They study performance under ideal downsampling, where theory exactly matches practice, generalization to unseen scales, data efficiency at 5k, 2.5k, and 1k training samples, and a harder non-ideal downsampling setting where the anti-aliasing filter is imperfect.
