# Dataset / Benchmark

Core claim: Evaluated on the Gushchin et al. (2023b) high-dimensional continuous EOT/SB benchmark (known ground-truth plans, D=2–128, ϵ=0.1,1,10), the Kaggle MSCI single-cell dataset (four donors, days 2/3/4/7; PCA DIM=50/100/1000), and 1024×1024 FFHQ faces in the 512-dim latent space of a pretrained ALAE autoencoder.

Supporting detail: Also a 2D Gaussian→Swiss-roll toy showing how ϵ controls trajectory volatility, plus an embryonic stem-cell differentiation dataset in the appendix.

Narration: The solver is tested across four kinds of data. First, a two-dimensional Gaussian to Swiss-roll toy, which visualizes how the noise level epsilon shapes the trajectories. Second, a recent high-dimensional entropic optimal transport benchmark with known ground-truth plans, spanning dimensions from two to one hundred twenty-eight and several values of epsilon. Third, the MSCI single-cell dataset from a Kaggle competition, with cells from four human donors at four time points, projected by PCA to fifty, one hundred, and one thousand dimensions. And fourth, unpaired image translation on FFHQ faces, performed in the five-hundred-twelve-dimensional latent space of a pretrained ALAE autoencoder.
