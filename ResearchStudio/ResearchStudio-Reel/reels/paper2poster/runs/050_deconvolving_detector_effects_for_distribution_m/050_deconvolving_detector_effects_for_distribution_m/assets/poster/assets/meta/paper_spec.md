---
title: Deconvolving Detector Effects for Distribution Moments
authors: Krish Desai¹, Benjamin Nachman², Jesse Thaler³⁴
institutes: ¹University of California, Berkeley; ²Lawrence Berkeley National Laboratory; ³Massachusetts Institute of Technology; ⁴NSF AI Institute for Artificial Intelligence and Fundamental Interactions
venue: NeurIPS 2022
paper_url: https://ml4physicalsciences.github.io/2022/files/NeurIPS_ML4PS_2022_43.pdf
code_url: https://github.com/hep-lbdl/MomentUnfolding
title_audio_script: Comparing collider measurements with theory requires unfolding, that is, correcting the distortions that detectors introduce into the data. But most unfolding methods first bin the data into histograms, while many theory predictions live at the level of statistical moments. This paper introduces Moment Unfolding, a machine-learning method that directly unfolds distribution moments without ever binning. Inspired by Generative Adversarial Networks and by Boltzmann's approach to statistical mechanics, it recovers moments to sub-percent accuracy on both Gaussian toy data and simulated LHC jets.
---

## Problem
**Necessary:** Deconvolving ('unfolding') detector distortions is critical for comparing cross-section measurements with theory, yet most unfolding methods require histogram binning even though many theoretical predictions are stated at the level of moments.
**Additional:** Binning the two-dimensional (X, Y) support to compute moments of X in bins of Y introduces discretization artifacts that limit precision.
**Audio script:** Unfolding, also known as deconvolution, corrects the distortions a detector imprints on measured data so that experiments can be compared with each other and with theory. The usual recipe unfolds an entire spectrum after first discretizing it into a histogram, then computes moments from that histogram. But this binning step introduces discretization artifacts, and it is wasteful when the quantity you actually care about is just a small set of moments as a function of another observable. That mismatch between binned data and moment-level theory predictions is the gap this paper closes.

## Motivation
**Necessary:** Statistical moments of observables, such as their energy-scale dependence, are often predictable from theory even when the full probability density is not, so a method that targets moments directly is valuable.
**Additional:** Existing unbinned unfolding methods unfold whole spectra generically, which can compromise precision for any specific aspect like a small set of moments.
**Audio script:** Summarizing a distribution with a few moments makes it tractable to visualize and, crucially, to predict from first principles. For example, the full densities of hadronic jets cannot be computed in perturbative QCD, but the energy dependence of their moments can be. Unbinned unfolding methods already exist and avoid binning artifacts, but they are built to unfold entire spectra, so they may trade away precision on the handful of moments a physicist actually wants. This motivates a dedicated method that unfolds the moments themselves.

## Contribution
**Necessary:** The paper introduces Moment Unfolding, a dedicated machine-learning technique that directly unfolds statistical moments of an observable in an unbinned, non-iterative way, using a reweighting function whose parameters are identified with the moments.
**Additional:** The generator's form is inspired by the Boltzmann equation and the training structure is adapted from a Generative Adversarial Network; unlike iterative methods such as OmniFold, one pair of networks is trained only once.
**Audio script:** The core contribution is Moment Unfolding, a new unbinned and non-iterative reweighting technique. It learns a reweighting function, playing the role of a GAN generator, whose form is inspired by the Boltzmann factor so that its trainable parameters can be directly identified with the observable's moments. A discriminator pushes the reweighted simulation to match the target data. Unlike OmniFold, which trains a fresh pair of networks on every iteration, Moment Unfolding trains a single pair of networks just once.

## Method
**Necessary:** Each synthetic event is a pair (X_T, X_D) of pre-detector 'generation' and post-detector 'simulation'. A generator g reweights the generation so that, after detector emulation, the reweighted simulation becomes statistically indistinguishable from the observed data, as judged by a discriminator d trained on a weighted binary cross-entropy loss.
**Additional:** g is parametrized as the exponential of a degree-n polynomial with only n trainable parameters {λ_i} identified with the moments; d has three hidden layers of 50 ReLU nodes with a sigmoid output. The generator maximizes the loss while the discriminator minimizes it, mirroring a GAN, and detector emulation is run only once because reweighting changes importance weights rather than features.
**Key equation:** `$g(x) = e^{\lambda_1 x + \lambda_2 x^2 + \cdots + \lambda_n x^n}$` and `$L[g,d] = -\frac{1}{N_x}\left[\sum_{\text{data}} \log d(x_{\text{data}}) + \sum_{(x_{\text{gen}}, x_{\text{sim}})} g(x_{\text{gen}}) \log\bigl(1 - d(x_{\text{sim}})\bigr)\right]$`
**Audio script:** The method borrows Boltzmann's idea of building the distribution that maximizes entropy subject to fixed moments. Concretely, the generator is written as the exponential of a polynomial in the observable, so its coefficients, the lambdas, are the moments being unfolded. This generator reweights the simulated events, and a discriminator neural network tries to tell the reweighted simulation apart from the real data. The two are trained against each other on a weighted binary cross-entropy loss: the discriminator minimizes it while the generator maximizes it. Because the reweighting only changes importance weights and not the event features, the expensive detector emulation runs a single time.

## Dataset / Benchmark
**Necessary:** Two case studies: a Gaussian toy example (truth N(0,1), generation N(−0.5,1), Gaussian detector noise N(0,5), 10⁶ samples, 3:1 train–test split) and hadronic jet substructure from LHC simulations using the jet width observable w.
**Additional:** The jet data are the Pythia/Herwig + Delphes samples from the OmniFold study, with one simulation acting as 'data' and the other as the synthetic dataset; two moments of the jet width are unfolded.
**Audio script:** The method is tested on two problems. First, a Gaussian toy: the truth is a standard normal, the generation is shifted to mean minus one-half, and the detector adds wide Gaussian noise, with a million samples split three to one for training and testing. Because a Gaussian has only finitely many moments, unfolding its moments is equivalent to unfolding the whole density. Second, hadronic jets from simulated LHC collisions, using the jet width observable, drawn from the same Pythia and Herwig plus Delphes datasets used in the OmniFold paper, where one simulation stands in for data and the other for the synthetic reference.

## Key Result
**Necessary:** On the jet substructure task the predicted moments, read off as the peaks of the loss-function scans, coincide with the known true moments (the vertical dotted lines) with a mean absolute error of ≤ 0.02%.
**Additional:** On the Gaussian example the maximum of the loss function sits at the true mean, verifying the procedure, and the discriminator converges within 10 epochs of training.
**Audio script:** The results are strong on both tasks. For the Gaussian example, the loss function peaks exactly at the true mean, confirming the method recovers the right answer, and the discriminator converges within about ten epochs. For the jet width, the team unfolds the first and second moments simultaneously. Scanning the loss as a function of each candidate moment produces curves whose peaks land on the true values, with a mean absolute error of two hundredths of a percent or better. That is sub-percent agreement between the unfolded and true moments.

## Ablation Study
**Necessary:** Even though the first and second moments of the reweighted generation match the truth well, the full jet-width distributions remain not statistically identical, because higher moments differ between truth and generation and are not constrained by unfolding only two moments.
**Additional:** This highlights the intended scope of the method: it targets a chosen small set of moments rather than the entire density, so residual differences appear in the uncontrolled higher moments.
**Audio script:** One instructive observation concerns the limits of unfolding only a couple of moments. After Moment Unfolding matches the first and second moments of the jet width, the full distributions of truth and reweighted generation still are not statistically identical. The reason is simply that higher moments remain relevant and were not part of the fit. This is expected behavior, and it clarifies that the technique deliberately controls the specific moments you ask for, leaving the rest free.

## Headline Numbers
**Necessary:** Predicted-vs-true moment mean absolute error ≤ 0.02%; 2 moments unfolded simultaneously for jet width; discriminator converges within 10 epochs.
**Additional:** 10⁶ samples with a 3:1 train–test split in the Gaussian study; the full analysis reproduces in under 5 minutes on a single Nvidia RTX6000 GPU.
**Audio script:** A few numbers capture the impact. The unfolded moments agree with the true moments to within two hundredths of a percent mean absolute error. Two moments of the jet width are unfolded at once. The discriminator converges within ten epochs. The Gaussian study uses a million samples with a three-to-one train-test split, and the entire set of notebooks reproduces in under five minutes on a single Nvidia RTX6000 GPU.

## Takeaway
**Necessary:** Moment Unfolding is a novel unbinned, non-iterative, GAN-inspired reweighting method that directly unfolds a chosen set of distribution moments to sub-percent accuracy, avoiding the discretization artifacts of binned unfolding.
**Additional:** It is dataset-agnostic, so beyond collider physics it could serve deconvolution problems in fields from medical devices and seismology to spectral astronomy and computer vision.
**Audio script:** The takeaway is that you can unfold detector effects directly at the level of moments, without ever binning the data. Moment Unfolding does this with a GAN-like generator whose parameters are the moments, trains only once rather than iterating, and recovers the true moments to better than a hundredth of a percent on realistic LHC jet simulations. Because the algorithm is agnostic to the dataset, the same idea could carry over to deconvolution problems well beyond particle physics.
