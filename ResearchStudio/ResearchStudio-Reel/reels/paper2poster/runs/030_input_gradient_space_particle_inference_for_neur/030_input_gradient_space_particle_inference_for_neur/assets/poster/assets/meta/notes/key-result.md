# Key Result

Core claim: FoRDE with PCA lengthscales outperforms deep ensembles and other repulsive-ensemble and BNN baselines under input corruptions across all metrics, with roughly a +2.4% accuracy gain on CIFAR-10-C and +1.3% on CIFAR-100-C over the second-best method, while staying competitive on clean data.

Supporting detail: In 1D/2D toy tasks FoRDE captures higher predictive uncertainty outside the training data than baselines, confirming greater functional diversity.

Narration: Across the corrupted image benchmarks, FoRDE with PCA lengthscales is the strongest method on every metric, while remaining competitive on clean images. Compared to the second-best method, it improves accuracy by about two point four percent on CIFAR-10-C and about one point three percent on CIFAR-100-C. The toy experiments tell a consistent story: in one and two dimensions, FoRDE places higher uncertainty in regions away from the training data than deep ensembles and other repulsive methods, which is direct evidence that repelling input gradients yields greater functional diversity.
