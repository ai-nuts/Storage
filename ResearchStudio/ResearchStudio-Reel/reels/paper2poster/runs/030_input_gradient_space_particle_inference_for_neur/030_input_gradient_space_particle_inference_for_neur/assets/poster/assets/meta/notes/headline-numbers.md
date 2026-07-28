# Headline Numbers

Core claim: - +2.4% accuracy on CIFAR-10-C over the second-best method (FoRDE-PCA) - +1.3% accuracy on CIFAR-100-C over the second-best method (FoRDE-PCA) - A 10-member FoRDE matches the corruption robustness of a 30-member deep ensemble - 19 corruption types x 5 severity levels evaluated (CIFAR-10/100-C, TinyImageNet-C)

Supporting detail: Ensemble size 10 with ResNet18 backbone; input-gradient kernel evaluated with linear cost in the number of training samples.

Narration: A few numbers capture the impact. Under input corruptions, FoRDE with PCA lengthscales improves accuracy by about two point four percent on CIFAR-10-C and one point three percent on CIFAR-100-C over the next-best method. Its diversity is efficient too: a ten-member FoRDE reaches the same corruption robustness as a thirty-member deep ensemble. And these gains hold across a demanding benchmark of nineteen corruption types at five severity levels each.
