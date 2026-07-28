# Dataset / Benchmark

Core claim: Evaluation uses simulated Gaussian designs in a low-dimensional setting (n=10000, p=100, s=5, SNR=1) and a high-dimensional setting (n=400, p=40000, s=20, SNR=2), each at correlations ρ ∈ {0, 0.4, 0.8}, plus twelve real data sets.

Supporting detail: Real data include bcTCGA, e2006-log1p, e2006-tfidf, scheetz, YearPredictionMSD (least-squares) and arcene, colon-cancer, duke-breast-cancer, ijcnn1, madelon, news20, rcv1 (logistic), spanning p up to ~4.3 million.

Narration: The experiments cover both simulated and real data. On simulated Gaussian designs, they sweep a low-dimensional regime with ten thousand observations and a hundred predictors and a high-dimensional regime with four hundred observations and forty thousand predictors, each at three correlation levels, zero, point four, and point eight, averaged over twenty repetitions. They then test twelve real data sets for both ℓ1-regularized least-squares and logistic regression, ranging from small gene-expression matrices up to problems with millions of features such as news20 and rcv1. Baselines are the working-set strategy, Celer, and Blitz.
