# Dataset / Benchmark

Core claim: Evaluated on a controlled Rotated Super-pixel MNIST structural-distortion benchmark, size-generalization datasets (D&D, NCI1, NCI109, PROTEINS with GCN/GIN/PNA backbones), and the GOOD benchmark suite (GOODCMNIST-color, GOODMotif-basis, GOODMotif-size, GOODSST2-length) under both concept and covariate shifts.

Supporting detail: Baselines include Vanilla, Deep Ensembles (DEns), Temperature scaling (Temp), and Monte-Carlo Dropout (MCD); tasks span calibration, OOD detection (AUROC), and generalization-gap prediction (MAE).

Narration: The evaluation is deliberately broad. For structural shift, the authors build a Rotated Super-pixel MNIST benchmark where increasing rotation induces controlled distortion. For size shift, they use standard graph classification datasets including D and D, NCI1, NCI109, and PROTEINS with GCN, GIN, and PNA backbones. For concept and covariate shifts, they use the GOOD benchmark suite covering colored MNIST, motif, and SST2 datasets. Across all of these they compare against strong uncertainty baselines including deep ensembles, temperature scaling, and Monte Carlo dropout, measuring calibration error, out-of-distribution detection AUROC, and generalization gap mean absolute error.
