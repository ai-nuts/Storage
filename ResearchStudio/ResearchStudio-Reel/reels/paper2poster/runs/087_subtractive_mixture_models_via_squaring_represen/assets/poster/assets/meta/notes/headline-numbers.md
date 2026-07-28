# Headline Numbers

Core claim: Squaring a K-component mixture encodes (K+1 choose 2) components within the same K-parameter budget; the class of squared non-monotonic circuits is proven exponentially more compact than any structured-decomposable monotonic PC.

Supporting detail: NPC²s attain the best average test log-likelihoods among tractable models on several UCI datasets (e.g. Power 0.62, Gas 10.98, Hepmass -20.41, MiniBooNE -26.68); on GPT2-sampled data they approach GPT2's reference log-likelihood of about -52 where monotonic PCs plateau.

Narration: A few numbers make the point. Squaring a mixture with K components encodes on the order of K-squared-over-two pairwise components while reusing the same K parameters, which is where the compactness comes from, and the paper proves this gap over monotonic circuits is exponential. Empirically, the squared non-monotonic circuits post the best test log-likelihoods among tractable models on several UCI datasets, for example zero point six two on Power, about eleven on Gas, minus twenty point four on Hepmass, and minus twenty-six point seven on MiniBooNE. On the language data they climb toward GPT2's own likelihood of around minus fifty-two, while monotonic circuits flatten out.
