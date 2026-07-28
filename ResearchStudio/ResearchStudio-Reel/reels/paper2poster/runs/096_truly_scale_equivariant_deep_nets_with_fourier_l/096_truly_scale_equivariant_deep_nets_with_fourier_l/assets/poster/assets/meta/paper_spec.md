---
title: Truly Scale-Equivariant Deep Nets with Fourier Layers
authors: Md Ashiqur Rahman¹, Raymond A. Yeh¹
institutes: ¹Department of Computer Science, Purdue University
venue: NeurIPS 2023
paper_url: https://arxiv.org/abs/2311.02922
code_url: https://github.com/ashiq24/Scale_Equivarinat_Fourier_Layer
title_audio_script: In computer vision, models should adapt gracefully when image resolution changes, a property called scale-equivariance. This paper, from Purdue University, points out that existing scale-equivariant CNNs are not truly scale-equivariant, because they formulate down-scaling in the continuous domain and ignore anti-aliasing. The authors instead formulate down-scaling directly in the discrete domain with anti-aliasing, and build a new family of deep nets from Fourier layers that achieves absolute zero equivariance error, both in theory and in practice, while staying competitive on classification accuracy.
---

## Problem
**Necessary:** Existing scale-equivariant CNNs are not *truly* scale-equivariant in practice: they achieve equivariance through weight-sharing and kernel resizing but incur non-negligible equivariance error.
**Additional:** They derive resizing in the continuous domain, so they never account for anti-aliasing that a discrete down-scaling operation demands.
**Audio script:** Scale-equivariance means that when an object in an image is resized, the network's features should transform consistently, and its label should stay the same. Recent scale-equivariant convolutional networks pursue this through weight-sharing and kernel resizing, using the same but resized kernel across scales. The trouble is that these methods are derived in the continuous domain, then discretized when implemented. That discretization step introduces a non-negligible equivariance error, so the networks are only approximately scale-equivariant, not truly so.

## Motivation
**Necessary:** When you down-scale a discrete signal, the Nyquist theorem requires an anti-aliasing filter; ignoring it lets high frequencies alias into low ones, breaking equivariance.
**Additional:** Prior continuous-domain formulations have no notion of anti-aliasing, which is precisely the gap that produces their residual error.
**Audio script:** The key insight is that down-scaling a discrete signal is fundamentally a signal-processing operation. The Nyquist sampling theorem tells us that before subsampling, we must apply an anti-aliasing filter, otherwise high-frequency content folds down into lower frequencies, the classic aliasing artifact seen in the wagon-wheel effect. Prior scale-equivariant networks, because they were formulated in the continuous domain, simply had no place for this filter. The authors argue that to be truly scale-equivariant, you must formulate the down-scaling directly in the discrete domain, with anti-aliasing built in from the start.

## Contribution
**Necessary:** They (1) formulate down-scaling in the discrete domain as ideal downsampling with anti-aliasing, (2) propose a family of truly scale-equivariant deep nets built from Fourier layers with a simple frequency-dependency condition, and (3) show absolute zero end-to-end equivariance error with competitive accuracy on MNIST-scale and STL-10.
**Additional:** They design scale-equivariant versions of every module (convolution, non-linearity, pooling), plus a per-scale classifier and a consistency loss tailored to scale-consistent prediction.
**Audio script:** The paper makes three contributions. First, it formulates the down-scaling operation directly in the discrete domain as ideal downsampling, properly accounting for anti-aliasing. Second, it proposes a whole family of deep nets that are truly scale-equivariant, by rethinking every component, convolution layers, non-linearities, and pooling, and re-expressing them as Fourier layers that obey a simple frequency-dependency rule. Third, through extensive experiments on MNIST-scale and STL-10, it shows the model attains an absolute zero end-to-end scale-equivariance error while remaining competitive in classification accuracy and more data-efficient in low-resource settings.

## Method
**Necessary:** Down-scaling is defined as ideal downsampling D_R = subsampling after an ideal low-pass (anti-aliasing) filter. The core condition (Claim 1) is that a net is scale-equivariant iff each output frequency Y[k] depends only on equal-or-lower input frequencies X[-k:k]. Every module (a spatially-local Fourier convolution, a frequency-aware non-linearity, and a Fourier pooling) is built to satisfy this condition.
**Additional:** A per-scale classifier shares an MLP across scales via Fourier zero-padding, and a hinge consistency loss encourages high-resolution predictions to beat their down-scaled versions. All operations run in the Fourier domain, giving O(|A| N log N + K N) per-layer cost.
**Key equation:** `$D_R(x) \triangleq \mathrm{Sub}_R(h \circledast x)$` ; `$Y[k] = \tilde{G}_k\big(X[-k:k]\big)\ \forall k \implies g(D_R(x)) = D_R(g(x))$` ; `$\sum_{k \in R(x)} \max\big(L(\hat{y}[k], y) - L(\hat{y}[k-1], y),\, 0\big)$`
**Audio script:** The method starts from a precise definition of down-scaling: ideal downsampling, which first applies an ideal low-pass filter that zeros out all frequencies above the new Nyquist limit, then subsamples. From this the authors derive their central condition, Claim 1: a deep net is truly scale-equivariant if and only if every output frequency term depends only on input frequency terms that are equal or lower. They then redesign each network component to satisfy this rule. A spatially-local Fourier layer constrains the kernel so it learns local features while staying equivariant. A scale-equivariant non-linearity applies ReLU frequency-band by frequency-band. A Fourier pooling layer preserves the same dependency structure. On top of the equivariant feature extractor, they add a classifier that predicts once per scale, sharing a single MLP across scales through Fourier padding, and train it with a hinge consistency loss that penalizes the model whenever a higher-resolution image is predicted worse than its lower-resolution version.

## Dataset / Benchmark
**Necessary:** Evaluated on MNIST-scale (resolutions 8×8 to 28×28) and STL10-scale (resolutions 48 to 97), the standard benchmarks for scale-equivariant networks, under both ideal and non-ideal (Gibbs-ringing) downsampling.
**Additional:** MNIST-scale uses 10k / 2k / 50k train/val/test; STL10-scale uses 7k / 1k / 5k. Data-efficiency is probed at 5k, 2.5k, and 1k training samples.
**Audio script:** The authors follow prior work and evaluate on two benchmarks. MNIST-scale is built by randomly downsampling MNIST digits so that every resolution from eight-by-eight up to twenty-eight-by-twenty-eight is equally represented. STL10-scale applies the same construction to natural color images, spanning resolutions from forty-eight up to ninety-seven. They study performance under ideal downsampling, where theory exactly matches practice, generalization to unseen scales, data efficiency at 5k, 2.5k, and 1k training samples, and a harder non-ideal downsampling setting where the anti-aliasing filter is imperfect.

## Key Result
**Necessary:** On MNIST-scale (ideal, all scales) the model reaches 0.9889 accuracy with 0.9716 scale-consistency and 0.00 equivariance error, the best on every metric. On STL10-scale it reaches 0.7332 accuracy versus 0.5844 for the next best (Fourier CNN), a ~15-point gain, again with zero equivariance error.
**Additional:** It stays best under non-ideal downsampling (0.9880 accuracy, 0.9760 scale-consistency, 0.05 error) and is the most data-efficient, reaching 0.9606 accuracy at just 1k training samples versus DISCO's 0.9457.
**Audio script:** The results are striking. On MNIST-scale with ideal downsampling, the model achieves the highest accuracy at ninety-eight point nine percent, the highest scale-consistency at ninety-seven percent, and, crucially, an absolute zero equivariance error, while competing methods like DISCO show errors around zero point four. The advantage is largest on the harder STL10-scale natural-image benchmark, where the model reaches seventy-three percent accuracy against roughly fifty-eight percent for the strongest baseline, a gain of about fifteen points, still with exactly zero equivariance error. It also degrades gracefully: even under non-ideal downsampling it remains the best model, and in low-data regimes it is the most data-efficient of all methods tested.

## Ablation Study
**Necessary:** Removing the consistency loss lowers both accuracy and scale-consistency at every training-set size (e.g. at 5k samples scale-consistency drops from 0.9296 to 0.9150; at 2.5k from 0.8906 to 0.8633), validating the loss.
**Additional:** Frequency-domain non-linearities were also tried but empirically degraded classification, motivating the spatial-domain scale-equivariant non-linearity σ_s used instead.
**Audio script:** An ablation isolates the consistency loss. Across training-set sizes of five thousand, twenty-five hundred, and one thousand samples, adding the consistency loss consistently improves both accuracy and the scale-consistency rate. For example, at five thousand samples the scale-consistency rises from ninety-one and a half percent to nearly ninety-three percent. This confirms that the hinge consistency loss is doing real work, encouraging the model to make better predictions as resolution increases. The authors also note that applying the non-linearity directly in the frequency domain, though equivariant, hurt classification, which is why they designed the spatial-domain scale-equivariant non-linearity.

## Headline Numbers
**Necessary:**
- **0.00** end-to-end scale-equivariance error (absolute zero, by construction) on MNIST-scale and STL10-scale.
- **0.9889** MNIST-scale accuracy (best), with **0.9716** scale-consistency.
**Additional:**
- **0.7332** STL10-scale accuracy vs **0.5844** next-best, a **~15-point** gain.
- **0.9606** accuracy at only **1k** training samples (most data-efficient; DISCO 0.9457).

## Takeaway
**Necessary:** By formulating down-scaling as ideal (anti-aliased) downsampling and enforcing a frequency-dependency rule via Fourier layers, the network becomes *exactly* scale-equivariant, zero error, not merely approximately, while staying accurate and data-efficient.
**Additional:** Getting the signal-processing right, treating down-scaling as a discrete anti-aliased operation, is what turns approximate equivariance into provable, absolute equivariance.
**Audio script:** The lasting takeaway is that scale-equivariance should be treated as a signal-processing problem. Once you formulate down-scaling as ideal, anti-aliased downsampling and require every output frequency to depend only on equal or lower input frequencies, you can build networks from Fourier layers that are exactly scale-equivariant, with provably zero error rather than the small residual errors that plagued earlier methods. And this theoretical guarantee comes at no practical cost: the model matches or beats prior scale-equivariant CNNs on accuracy and is more data-efficient, especially on challenging natural images.
