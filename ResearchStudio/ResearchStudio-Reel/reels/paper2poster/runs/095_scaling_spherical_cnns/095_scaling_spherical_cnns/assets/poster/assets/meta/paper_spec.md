---
title: Scaling Spherical CNNs
authors: Carlos Esteves¹, Jean-Jacques Slotine², Ameesh Makadia¹
institutes: ¹Google Research; ²MIT
venue: ICML 2023
paper_url: https://arxiv.org/abs/2306.05420
code_url: https://github.com/google-research/spherical-cnn
title_audio_script: Spherical CNNs generalize convolutional networks to signals living on the sphere, which makes them a natural fit for molecules and weather data. But until now they were stuck at low resolutions and shallow depths, so they never really competed on large real-world problems. This paper, Scaling Spherical CNNs from Google Research and MIT, shows how to scale these models by a full order of magnitude. With new activations, normalization, residual blocks, and a TPU-optimized implementation, the authors reach state of the art on the QM9 molecular benchmark and become competitive on several weather forecasting tasks.
---

## Problem
**Necessary:** Spherical CNNs compute convolutions in the spectral domain, which is far costlier than planar convolution, so applications were confined to small, low-resolution, low-capacity problems.
**Additional:** No spherical CNN existed at the scale of common planar architectures like VGG-19, blocking their use on large scientific datasets.
**Audio script:** Spherical CNNs replace the plane with the sphere as the domain of the signal, which is exactly right for data like molecules and the atmosphere. The catch is that their core operation, spherical convolution, is most accurate in the spectral domain, and that is far more expensive than an ordinary planar convolution. Because of this cost, spherical CNNs had been limited to small, low-resolution problems with modest model capacity. There simply was no large-scale spherical architecture analogous to the deep planar networks that power modern computer vision.

## Motivation
**Necessary:** Molecular property prediction and weather forecasting are naturally spherical and rotation-related, so rotation-equivariant spherical CNNs should excel, but only if they can scale to datasets like QM9 (134K molecules) and high-resolution ERA5 weather grids.
**Additional:** These fields were dominated by equivariant graph neural networks and transformers; prior spherical CNNs were limited to tiny benchmarks like QM7 (7,165 molecules).
**Audio script:** Two scientific problems motivate this work: predicting molecular properties and forecasting the weather. Both are intrinsically spherical and tied to rotations. A molecule's properties don't change when you rotate it in space, and the Earth's atmosphere is naturally a signal on a sphere. Rotation-equivariant spherical CNNs should be a perfect match. But the standard benchmarks are large. QM9 has one hundred thirty four thousand molecules, over eighteen times bigger than the tiny QM7 set earlier spherical CNNs could handle, and weather grids demand high spatial resolution. To compete, these models had to scale.

## Contribution
**Necessary:** The paper presents a systematic approach to scale spherical CNNs one order of magnitude larger: a TPU-optimized JAX implementation of spin-weighted spherical harmonic transforms, new general-purpose layers and activations, and application-specific input representations for molecules and weather.
**Additional:** Naively increasing depth and width is shown insufficient; scaling required redesigning the nonlinearity, normalization, and residual block, each improving both efficiency and accuracy.
**Audio script:** The authors contribute a systematic recipe for scaling spherical CNNs by an order of magnitude. It has three parts. First, an efficient implementation of spin-weighted spherical harmonic transforms in JAX, tuned to run fast and distributed on TPUs. Second, new general-purpose layers and activations that improve both expressivity and efficiency. And third, application-specific input representations designed for molecules and for weather data. A key finding is that naive scaling, just adding depth and width, is not enough; the core components themselves had to be redesigned.

## Method
**Necessary:** Building on spin-weighted spherical CNNs, the authors introduce a phase collapse nonlinearity (which uses the modulus to collapse phase and recover rotation invariance), spectral batch normalization, spectral pooling, and an efficient residual block whose skip connection lives in Fourier space (Figure 2). Fourier transforms are computed as dense matrix multiplications (DFT) rather than FFTs for speed on TPUs.
**Additional:** The complete rewrite in JAX runs distributed across up to 32 TPUs; molecules are encoded as sets of spherical functions built from physically-based, power-law interactions between atom pairs (Figure 3).
**Key equation:** `$(f * k)(x) = \int_{g \in SO(3)} f(g\nu)\, k(g^{-1}x)\, dg$` and the phase collapse activation `$x_0 \leftarrow W_1 x_0 + W_2 |x| + b$`
**Audio script:** The method builds on spin-weighted spherical CNNs. Its centerpiece is a set of new components that all live in the spectral domain. A phase collapse nonlinearity takes the modulus of the features to collapse their phase, which restores rotation invariance while losing no information in the nonzero spins. Batch normalization and pooling are also moved into the spectral domain, and the residual block adds its skip connection directly between Fourier coefficients. On the implementation side, the authors compute the Fourier transforms as dense matrix multiplications rather than fast Fourier transforms, because on TPUs matrix multiplies are extremely fast while memory reshuffling is the bottleneck.

## Dataset / Benchmark
**Necessary:** QM9 (134,000 molecules, up to 29 atoms, 12 regression targets) for molecular property regression, and WeatherBench / ERA5 reanalysis data for short and medium-range weather forecasting.
**Additional:** Weather tasks span WeatherBench (Z500, T850, T2M at 3 and 5 days), global extreme temperature forecasting up to 28 days, and iterative high-resolution forecasting following Keisler (2022).
**Audio script:** The experiments span two very different domains. For molecules, the benchmark is QM9, with one hundred thirty four thousand molecules, up to twenty nine atoms each, and twelve regression targets covering energetic, electronic, and thermodynamic properties. For weather, the models are trained on ERA5 reanalysis data through the WeatherBench benchmark, forecasting quantities like geopotential height and temperature at three and five day horizons, plus longer tasks reaching out to twenty eight days and iterative high-resolution forecasting.

## Key Result
**Necessary:** The scaled spherical CNN reaches state of the art on QM9, outperforming the previously dominant graph neural networks and transformers on 8 of 12 targets in Split 1 and 9 of 12 targets in Split 2.
**Additional:** On WeatherBench it outperforms the baseline on all metrics in the 2-predictor setting and even beats models pre-trained on large simulated datasets on several temperature metrics, showing for the first time that spherical CNNs are viable neural weather models.
**Audio script:** The results are strong on both fronts. On QM9, the scaled spherical CNN reaches state of the art, beating the previously dominant graph neural networks and transformers on eight of twelve targets under the first data split and nine of twelve under the second. On weather, it outperforms the WeatherBench baseline on every metric in the simpler two-predictor setting, and it even beats models that were pre-trained on large amounts of simulated data on several temperature metrics. This is the first demonstration that spherical CNNs are viable neural weather models.

## Ablation Study
**Necessary:** Table 1 isolates each contribution on a QM9 model: phase collapse cuts RMSE by 8.0%, spectral batch norm by a further 1.4%, and the efficient residual block by another 2.4%, while the JAX/DFT/symmetry choices deliver large steps-per-second gains.
**Additional:** Table 6 confirms the phase collapse activation, spectral pooling, and the new spherical molecule representation each outperform prior alternatives, reaching 15.25 meV MAE on QM9 enthalpy.
**Audio script:** A careful ablation isolates the effect of each change. Starting from the JAX implementation, the phase collapse activation cuts error by eight percent, spectral batch normalization trims a further one and a half percent, and the efficient residual block another two and a half percent, all while improving speed. A separate comparison confirms that the phase collapse activation, spectral pooling, and the new spherical molecule representation each beat the prior alternatives from earlier work, together driving the QM9 enthalpy error down to about fifteen point two five milli electron volts.

## Headline Numbers
**Necessary:**
- Scales spherical CNNs by one order of magnitude in operations and feature resolution
- State of the art on 8/12 (Split 1) and 9/12 (Split 2) QM9 targets
- JAX implementation ~3× faster than the original; distributed runs up to 100× faster on 32 TPUs
- Phase collapse nonlinearity reduces QM9 RMSE by 8.0%
**Audio script:** Here are the numbers that summarize the impact. The models scale by one full order of magnitude in both operations and feature resolution compared to prior spherical CNNs. They set state of the art on eight of twelve QM9 targets in the first split and nine of twelve in the second. The new JAX implementation is about three times faster than the original, and running distributed across thirty two TPUs speeds it up by a hundred times or more. And the phase collapse nonlinearity alone reduces QM9 error by eight percent.

## Takeaway
**Necessary:** With the right redesign of core components and a hardware-tuned implementation, spherical CNNs can finally scale to reach state of the art on molecular property prediction and become competitive neural weather models.
**Additional:** The released JAX implementation is intended as a platform for further spherical CNN research on real-world scientific problems.
**Audio script:** The takeaway is that spherical CNNs were never fundamentally limited, they were just poorly scaled. With a redesign of the nonlinearity, normalization, and residual block, plus an implementation tuned to modern accelerators, these models finally scale to real problems, reaching state of the art on molecular property prediction and becoming genuinely competitive neural weather models. The authors release their JAX implementation as a platform for further research on spherical data.
