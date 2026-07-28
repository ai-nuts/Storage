# Contribution

Core claim: The paper introduces the Tree Neural Tangent Kernel (TNTK) for infinite soft-tree ensembles, gives its closed form at initialization, proves it stays constant during training (enabling kernel-regression analysis and global convergence), shows oblivious trees induce the same TNTK as ordinary ones, and identifies a degeneracy of the kernel for deep trees.

Supporting detail: These four results together provide theoretical support for empirical techniques such as parameter sharing (NODE-style oblivious trees), adjusting split hardness, and limiting tree depth.

Narration: The paper makes four contributions. First, it derives the Tree Neural Tangent Kernel at initialization for infinitely many perfect binary trees of arbitrary depth, and proves the kernel stays essentially constant during training, enabling analysis as kernel regression and a proof of global convergence. Second, it shows oblivious ensembles, which share splitting rules within each depth as in NODE, converge to the very same kernel. Third, it characterizes the decision function, nearly linear in the basic case and more nonlinear as splits harden. Fourth, it uncovers a degeneracy where deep trees flatten the kernel.
