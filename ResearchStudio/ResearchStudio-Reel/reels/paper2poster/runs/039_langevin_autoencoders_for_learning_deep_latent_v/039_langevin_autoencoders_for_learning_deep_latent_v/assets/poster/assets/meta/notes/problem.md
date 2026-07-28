# Problem

Core claim: Langevin-dynamics MCMC can approximate the intractable posteriors of deep latent variable models, but its costly per-datapoint sampling iterations and slow convergence make it impractical for training.

Supporting detail: Gradient-based maximum-likelihood learning needs an expectation over the posterior p(z|x), which has no closed form and must be Monte-Carlo estimated separately for every data point.

Narration: Training deep latent variable models by maximum likelihood needs an expectation over the hidden variables' posterior, which is intractable. Langevin dynamics samples that posterior accurately, but runs a fresh chain of iterations per data point and converges slowly, so it has rarely been practical.
