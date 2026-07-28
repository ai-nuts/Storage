---
title: Langevin Autoencoders for Learning Deep Latent Variable Models
authors: Shohei Taniguchi¹, Yusuke Iwasawa¹, Wataru Kumagai¹, Yutaka Matsuo¹
institutes: ¹The University of Tokyo
venue: NeurIPS 2022
paper_url: https://arxiv.org/abs/2209.07036
code_url: https://github.com/iShohei220/LAE
title_audio_script: This work, from the University of Tokyo and presented at NeurIPS 2022, introduces the Langevin autoencoder. Markov chain Monte Carlo methods like Langevin dynamics can approximate the intractable posteriors of deep latent variable models, but they are too slow because they run separate sampling iterations for every single data point. The authors propose amortized Langevin dynamics, which replaces those per-datapoint iterations with updates to a shared encoder network. They prove this is still a valid MCMC method, and they turn it into a new generative model, the Langevin autoencoder, that looks like a small tweak to a standard autoencoder yet outperforms variational autoencoders on test likelihood.
---

## Problem
**Necessary:** Langevin-dynamics MCMC can approximate the intractable posteriors of deep latent variable models, but its costly per-datapoint sampling iterations and slow convergence make it impractical for training.
**Additional:** Gradient-based maximum-likelihood learning needs an expectation over the posterior p(z|x), which has no closed form and must be Monte-Carlo estimated separately for every data point.
**Audio script:** Deep latent variable models describe data through hidden variables, but training them by maximum likelihood requires an expectation over the posterior distribution of those hidden variables, which is intractable. Markov chain Monte Carlo, and in particular Langevin dynamics, can sample from such posteriors accurately. The problem is speed. Traditional Langevin dynamics runs a fresh chain of sampling iterations for every single data point, and it converges slowly, so it has rarely been practical for training deep models.

## Motivation
**Necessary:** Amortized variational inference (the VAE) is efficient because an encoder predicts latents for all data, but its accuracy is capped by the tractable variational family; MCMC is flexible yet has never been truly amortized.
**Additional:** Prior encoder-plus-MCMC hybrids (e.g. Hoffman 2017) only use the encoder to initialize sampling, so they still pay for datapoint-wise Langevin iterations at train and test time.
**Audio script:** Variational inference became dominant for deep latent variable models thanks to amortization: instead of optimizing separate parameters for each data point, a shared encoder network predicts the latent variables for all of them, which is exactly what the variational autoencoder does. But variational inference relies on tractable distributions like Gaussians, so its approximation power is fundamentally limited. Markov chain Monte Carlo does not have that limitation, yet no one had truly amortized it. Earlier hybrids only used an encoder to warm-start sampling and still ran per-datapoint chains. The goal here is to bring amortization's efficiency to MCMC's flexibility.

## Contribution
**Necessary:** (1) Amortized Langevin Dynamics (ALD), which entirely replaces datapoint-wise MCMC with Langevin updates of an encoder's parameters, proven to keep the true posterior as its stationary distribution; (2) the Langevin Autoencoder (LAE), a deep latent-variable model realized as a small modification of a traditional autoencoder.
**Additional:** Traditional Langevin dynamics is shown to be a special case of ALD, and the standard autoencoder is a special case of the LAE.
**Audio script:** The paper makes two main contributions. First, amortized Langevin dynamics, a new MCMC algorithm that entirely removes per-datapoint sampling iterations by instead running Langevin updates on the parameters of a shared encoder, with a proof that it keeps the true posterior as its stationary distribution. Second, the Langevin autoencoder, a new framework for training deep generative models built on amortized Langevin dynamics that, remarkably, amounts to only a small modification of a traditional autoencoder. As nice special cases, ordinary Langevin dynamics and the plain autoencoder both fall out of this framework.

## Method
**Necessary:** Instead of simulating the latent SDE per datapoint, ALD defines a deterministic encoder f(x;φ) and runs a Langevin SDE on its parameters φ; the encoder's outputs are taken directly as posterior samples. When the encoder has the form f(x;Φ)=Φg(x) with a fixed feature extractor and a trainable last linear layer whose width exceeds the batch size, Theorem 1 guarantees the induced latent samples converge to the true posterior. The LAE trains a decoder by running T ALD steps on the encoder's last layer before each parameter update, with an optional Metropolis-Hastings rejection step to remove discretization error.
**Additional:** ALD amortizes MCMC across all data through the shared encoder, so a warmed-up encoder can also accelerate sampling for new test data.
**Key equation:** `$d\phi = -\nabla_\phi V(\phi)\,dt + \sqrt{2}\,dB, \quad V(\phi) := \sum_{i=1}^{n} U\!\left(x^{(i)}, f_{z|x}(x^{(i)};\phi);\theta\right)$` and the discretized update `$q(\phi' \mid \phi) := \mathcal{N}\!\left(\phi';\, \phi - \eta\nabla_\phi V(\phi),\, 2\eta I\right)$` with encoder form `$f_{z|x}(x;\Phi)=\Phi\, g(x)$`.
**Audio script:** The key idea is to move the randomness from the latent space to the encoder's parameters. Rather than simulating a stochastic differential equation on each latent variable, amortized Langevin dynamics defines a deterministic encoder that maps observations to latents, and runs the Langevin equation on the encoder's parameters. Because the encoder produces the latents, dynamics on its parameters induce dynamics on the latent space, and the encoder's outputs are treated directly as posterior samples. A theorem shows that when the encoder is a fixed feature extractor followed by a trainable linear layer whose width exceeds the batch size, the samples converge to the true posterior. The Langevin autoencoder simply runs a few of these update steps before each decoder update, optionally with a Metropolis-Hastings correction.

## Dataset / Benchmark
**Necessary:** Toy studies use a conjugate bivariate-Gaussian latent-variable model and a neural-network (neural-likelihood) posterior; image generation is evaluated on MNIST, SVHN, CIFAR-10, and CelebA.
**Additional:** All methods share the same fully-connected networks; test performance is measured by the negative evidence lower bound (ELBO) per data dimension over three seeds.
**Audio script:** The method is validated in two stages. First, on toy examples where the answer is known: a conjugate bivariate-Gaussian model whose posterior has a closed form, and a harder posterior defined by a randomly initialized neural network. Then, on realistic image generation using four standard datasets, MNIST, S-V-H-N, CIFAR-10, and CelebA. All methods use the same fully-connected architectures for a fair comparison, and quality is measured by the negative evidence lower bound per data dimension, averaged over three random seeds.

## Key Result
**Necessary:** The LAE consistently achieves the best (lowest) negative ELBO per dimension on all four image datasets, beating the VAE, VAE-flow, and Hoffman (2017), showing that ALD's more accurate posterior sampling yields better DLVM training.
**Additional:** On toy posteriors, ALD captures multimodal, correlated posteriors that mean-field and full VI cannot, matching the ground-truth density.
**Audio script:** On the toy problems, amortized Langevin dynamics reproduces the true posterior faithfully, including multimodal and strongly correlated shapes that mean-field and even full variational inference cannot capture. On the image datasets, the Langevin autoencoder achieves the lowest negative evidence lower bound on all four benchmarks, beating the variational autoencoder, its normalizing-flow extension, and the earlier encoder-initialized Langevin method. The message is consistent: more accurate posterior sampling translates directly into better-trained generative models.

## Ablation Study
**Necessary:** The Metropolis-Hastings rejection step is important for stabilizing training, while the number of ALD iterations T has little effect once T ≥ 2. The encoder's last-layer dimensionality must satisfy d ≥ n (batch size) for samples to converge to the true posterior.
**Additional:** With d < n some datapoints' samples collapse to a small region, empirically confirming the rank condition of Theorem 1.
**Audio script:** Two ablations probe what matters. The encoder-capacity study confirms the theory: when the last linear layer's dimensionality is at least the batch size, samples match the true posterior, but when it is smaller, samples for some data points collapse. And on the image side, the Metropolis-Hastings rejection step turns out to be important for stabilizing training, while the number of Langevin iterations barely matters as long as it is at least two, which is why the experiments use just two steps.

## Headline Numbers
**Necessary:**
- MNIST negative ELBO/dim: 1.177 (LAE) vs 1.189 (VAE)
- CIFAR-10: 4.773 (LAE) vs 4.820 (VAE)
- CelebA: 4.636 (LAE) vs 4.671 (VAE)
- SVHN: 4.412 (LAE) vs 4.442 (VAE); LAE trains ~2.24× slower than VAE
**Additional:** Only T = 2 ALD iterations are used in the image experiments; LAE and Hoffman (2017) have nearly identical training speed.
**Audio script:** The gains are consistent though modest in absolute terms. On MNIST, the Langevin autoencoder reaches a negative evidence lower bound of one point one seven seven per dimension, versus one point one eight nine for the variational autoencoder. On CIFAR-10 it improves from four point eight two to four point seven seven, on CelebA from four point six seven to four point six four, and on S-V-H-N from four point four four to four point four one. The cost is training time: the Langevin autoencoder is about two and a quarter times slower than a plain variational autoencoder, but essentially the same speed as the earlier encoder-initialized Langevin baseline.

## Takeaway
**Necessary:** Replacing per-datapoint MCMC with a Langevin update of a shared encoder's parameters gives efficient yet flexible posterior sampling, turning a plain autoencoder into a provably valid MCMC-based generative model that outperforms VAEs on test likelihood.
**Additional:** The LAE reframes the traditional autoencoder as a bias-corrected, sampling-based alternative to variational inference.
**Audio script:** The takeaway is elegant. By moving Langevin noise from the latent space to the encoder's parameters, you get posterior sampling that is both efficient, because it is amortized across all data, and flexible, because it is genuine MCMC rather than a constrained Gaussian. The resulting Langevin autoencoder is provably valid as an MCMC method, looks almost identical to a standard autoencoder in code, and yet consistently beats variational autoencoders on test likelihood. In effect, it reframes the ordinary autoencoder as a bias-corrected, sampling-based alternative to variational inference.
