# Problem

Core claim: Gaussian Graphical Models recover conditional independence by sparsifying the precision matrix Ω, but the ideal sub-l1 (q<1) penalties are highly non-convex, so methods default to the l1 norm and its over-shrinkage.

Supporting detail: In high dimensions (d>n) the sample covariance is singular, so the precision matrix cannot be obtained by inversion and must be estimated under a sparsity penalty.

Narration: Gaussian Graphical Models read conditional independence from the precision matrix, the inverse covariance: a zero entry means two variables are conditionally independent, so a sparse precision matrix recovers the network. The ideal l-zero penalty that counts edges is combinatorial and intractable. Sub-l-one pseudo-norms approximate it well but are non-convex, so most methods retreat to the convex l-one norm, which over-shrinks, especially when variables outnumber samples.
