# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_gravitational_wave_inference_usually`

- Preferred role: `content`
- Cue keywords: `gravitational-wave, inference, usually, assumes, detector, noise, gaussian, stationary, but, real`
- Narration: Gravitational-wave inference usually assumes detector noise is Gaussian and stationary, but real LIGO, Virgo, and KAGRA data break that with glitches and drifting spectral lines.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_gravitational_wave_inference_usually" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gravitational-wave, inference, usually, assumes, detector, noise in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_work_introduces_slic_score_based_lik`

- Preferred role: `method`
- Cue keywords: `work, introduces, slic, score-based, likelihood, characterization`
- Narration: This work introduces SLIC, Score-based Likelihood Characterization.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_work_introduces_slic_score_based_lik" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, introduces, slic, score-based, likelihood, characterization in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_learns_true_noise_distribution_diffu`

- Preferred role: `method`
- Cue keywords: `learns, true, noise, distribution, diffusion, couples, differentiable, waveform, unbiased, parameter`
- Narration: It learns the true noise distribution with a diffusion model and couples it to a differentiable waveform for unbiased parameter estimation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_learns_true_noise_distribution_diffu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords learns, true, noise, distribution, diffusion, couples in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_extracting_astrophysics_gravitationa`

- Preferred role: `method`
- Cue keywords: `extracting, astrophysics, gravitational, waves, needs, bayesian, inference, needs, likelihood`
- Narration: Extracting astrophysics from gravitational waves needs Bayesian inference, and that needs a likelihood.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_extracting_astrophysics_gravitationa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords extracting, astrophysics, gravitational, waves, needs, bayesian in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_decades_field_assumed_noise_gaussian`

- Preferred role: `content`
- Cue keywords: `decades, field, assumed, noise, gaussian, stationary, because, makes, likelihood, cheap`
- Narration: For decades the field assumed noise is Gaussian and stationary because it makes the likelihood cheap.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_decades_field_assumed_noise_gaussian" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords decades, field, assumed, noise, gaussian, stationary in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_but_real_detectors_drift_over`

- Preferred role: `content`
- Cue keywords: `but, real, detectors, drift, over, time, carry, transient, glitches, wandering`
- Narration: But real detectors drift over time and carry transient glitches and wandering spectral lines.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_but_real_detectors_drift_over" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, real, detectors, drift, over, time in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_these_handled_segment_segment_costly`

- Preferred role: `result`
- Cue keywords: `these, handled, segment, segment, costly, custom, fixes, bias, results, famously`
- Narration: These are handled segment by segment with costly custom fixes that can bias results. Famously, GW170817 landed right on a loud LIGO glitch.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c4_these_handled_segment_segment_costly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, handled, segment, segment, costly, custom in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_now`

- Preferred role: `content`
- Cue keywords: `why, now`
- Narration: Why now?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_why_now" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, now in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_gravitational_wave_astronomy_scaling`

- Preferred role: `method`
- Cue keywords: `gravitational-wave, astronomy, scaling, fast, analyzing, large, catalogs, makes, pipeline, sensitive`
- Narration: Gravitational-wave astronomy is scaling fast, and analyzing large catalogs makes the pipeline sensitive to tiny departures from Gaussian noise that quietly accumulate into bias.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_gravitational_wave_astronomy_scaling" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gravitational-wave, astronomy, scaling, fast, analyzing, large in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_authors_wanted_keep_trusted_determin`

- Preferred role: `content`
- Cue keywords: `authors, wanted, keep, trusted, deterministic, waveform, models, while, dropping, unrealistic`
- Narration: The authors wanted to keep the trusted deterministic waveform models while dropping the unrealistic noise assumption, and to prepare for next-generation detectors like Cosmic Explorer and the Einstein Telescope.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_authors_wanted_keep_trusted_determin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, wanted, keep, trusted, deterministic, waveform in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_core_contribution_brings_score_based`

- Preferred role: `method`
- Cue keywords: `core, contribution, brings, score-based, likelihood, characterization, slic, gravitational, waves`
- Narration: The core contribution brings Score-based Likelihood Characterization, or SLIC, to gravitational waves.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_core_contribution_brings_score_based" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, contribution, brings, score-based, likelihood, characterization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_originally_developed_astronomical_im`

- Preferred role: `method`
- Cue keywords: `originally, developed, astronomical, imaging, learns, score, noise, distribution, diffusion, instead`
- Narration: Originally developed for astronomical imaging, it learns the score of the noise distribution with a diffusion model instead of assuming its form.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_originally_developed_astronomical_im" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords originally, developed, astronomical, imaging, learns, score in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_coupled_differentiable_waveform_yiel`

- Preferred role: `content`
- Cue keywords: `coupled, differentiable, waveform, yields, unbiased, likelihood`
- Narration: Coupled with a differentiable waveform, it yields an unbiased likelihood.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_coupled_differentiable_waveform_yiel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords coupled, differentiable, waveform, yields, unbiased, likelihood in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_they_show_both_generates_realistic`

- Preferred role: `content`
- Cue keywords: `they, show, both, generates, realistic, ligo, noise, recovers, true, parameters`
- Narration: They show it both generates realistic LIGO noise and recovers the true parameters of an injected signal.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_they_show_both_generates_realistic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, show, both, generates, realistic, ligo in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_how_slic_works_setting_inverse`

- Preferred role: `content`
- Cue keywords: `how, slic, works, setting, inverse, problem, additive, noise, observation, equals`
- Narration: Here is how SLIC works. The setting is an inverse problem with additive noise: an observation equals a deterministic signal model plus noise.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_how_slic_works_setting_inverse" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, slic, works, setting, inverse, problem in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_learn_score_noise_distribution_you`

- Preferred role: `method`
- Cue keywords: `learn, score, noise, distribution, you, build, score, likelihood`
- Narration: Learn the score of the noise distribution and you can build the score of the likelihood.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_learn_score_noise_distribution_you" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords learn, score, noise, distribution, you, build in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_they_train_score_based_diffusion_rea`

- Preferred role: `method`
- Cue keywords: `they, train, score-based, diffusion, real, ligo, noise, denoising, score, matching`
- Narration: So they train a score-based diffusion model on real LIGO noise using denoising score matching, then chain it with the Jacobian of a differentiable IMRPhenomD waveform from the ripple package.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_they_train_score_based_diffusion_rea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, train, score-based, diffusion, real, ligo in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_sampling_metropolis_adjusted_langevi`

- Preferred role: `content`
- Cue keywords: `sampling, metropolis-adjusted, langevin, algorithm, mala`
- Narration: Sampling uses a Metropolis-adjusted Langevin algorithm, MALA.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_sampling_metropolis_adjusted_langevi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sampling, metropolis-adjusted, langevin, algorithm, mala in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_demonstration_real`

- Preferred role: `method`
- Cue keywords: `demonstration, real`
- Narration: The demonstration uses real data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_demonstration_real" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords demonstration, real in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_they_train_score_network_eleven`

- Preferred role: `method`
- Cue keywords: `they, train, score, network, eleven, hours, real, ligo-hanford, around, gw150914`
- Narration: They train the score network on eleven hours of real LIGO-Hanford data around GW150914, sampled at four thousand ninety-six hertz in four-second segments, discarding the segment holding the true signal.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_they_train_score_network_eleven" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, train, score, network, eleven, hours in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_runs_fourier_domain_after_tukey`

- Preferred role: `method`
- Cue keywords: `runs, fourier, domain, after, tukey, window`
- Narration: Training runs in the Fourier domain after a Tukey window.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_runs_fourier_domain_after_tukey" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords runs, fourier, domain, after, tukey, window in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_test_they_inject_simulated_gw150914`

- Preferred role: `method`
- Cue keywords: `test, they, inject, simulated, gw150914-like, signal, held-out, real, noise, never`
- Narration: To test, they inject a simulated GW150914-like signal into held-out real noise never seen during training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_test_they_inject_simulated_gw150914" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, they, inject, simulated, gw150914-like, signal in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_encouraging`

- Preferred role: `result`
- Cue keywords: `results, encouraging`
- Narration: The results are encouraging.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_results_encouraging" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, encouraging in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_drawing_one_thousand_twenty_four_noi`

- Preferred role: `method`
- Cue keywords: `drawing, one, thousand, twenty-four, noise, realizations, slic, its, power, spectrum`
- Narration: Drawing one thousand twenty-four noise realizations from SLIC, its power spectrum matches a Welch estimate from real LIGO data, and it resolves narrow spectral lines even more finely thanks to more training data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_drawing_one_thousand_twenty_four_noi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords drawing, one, thousand, twenty-four, noise, realizations in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_injecting_known_signal_slic_recovers`

- Preferred role: `content`
- Cue keywords: `injecting, known, signal, slic, recovers, all, five, varied, parameters, high`
- Narration: Injecting a known signal, SLIC recovers all five varied parameters with high credibility, and its posterior is tighter than the Gaussian-likelihood one.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_injecting_known_signal_slic_recovers" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords injecting, known, signal, slic, recovers, all in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_key_comparison_against_conventional`

- Preferred role: `result`
- Cue keywords: `key, comparison, against, conventional, approach`
- Narration: The key comparison is against the conventional approach.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_key_comparison_against_conventional" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, comparison, against, conventional, approach in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_injected_signal_they_run_inference`

- Preferred role: `content`
- Cue keywords: `injected, signal, they, run, inference, twice, once, learned, slic, likelihood`
- Narration: For the injected signal they run inference twice: once with the learned SLIC likelihood, and once with a standard Gaussian likelihood from a Welch spectrum.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_injected_signal_they_run_inference" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords injected, signal, they, run, inference, twice in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_they_pick_glitch_free_segment_both`

- Preferred role: `result`
- Cue keywords: `they, pick, glitch-free, segment, both, recover, true, parameters, but, slic`
- Narration: They pick a glitch-free segment, so both recover the true parameters, but SLIC's posterior comes out tighter, hinting at gains on noisy, glitch-contaminated data.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_they_pick_glitch_free_segment_both" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, pick, glitch-free, segment, both, recover in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_anchor_demonstration_ele`

- Preferred role: `method`
- Cue keywords: `few, numbers, anchor, demonstration, eleven, hours, real, ligo-hanford, noise, train`
- Narration: A few numbers anchor the demonstration. Eleven hours of real LIGO-Hanford noise train the score model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_few_numbers_anchor_demonstration_ele" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, anchor, demonstration, eleven, hours in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_one_thousand_twenty_four_synthetic_r`

- Preferred role: `takeaway`
- Cue keywords: `one, thousand, twenty-four, synthetic, realizations, validate, learned, power, spectrum`
- Narration: One thousand twenty-four synthetic realizations validate the learned power spectrum.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s09_c2_one_thousand_twenty_four_synthetic_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, thousand, twenty-four, synthetic, realizations, validate in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_inference_recovers_five_source_param`

- Preferred role: `content`
- Cue keywords: `inference, recovers, five, source, parameters, chirp, mass, mass, ratio, luminosity`
- Narration: Inference recovers five source parameters: chirp mass, mass ratio, luminosity distance, coalescence time, and phase.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_inference_recovers_five_source_param" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords inference, recovers, five, source, parameters, chirp in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_sampled_four_thousand_ninety_six_her`

- Preferred role: `content`
- Cue keywords: `sampled, four, thousand, ninety-six, hertz, four-second, segments`
- Narration: Data are sampled at four thousand ninety-six hertz in four-second segments.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_sampled_four_thousand_ninety_six_her" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sampled, four, thousand, ninety-six, hertz, four-second in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_you_longer_assume_gaussian`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, you, longer, assume, gaussian, stationary, noise`
- Narration: The takeaway: you no longer have to assume Gaussian, stationary noise.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_you_longer_assume_gaussian" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, you, longer, assume, gaussian, stationary in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_learning_real_noise_distribution_dif`

- Preferred role: `method`
- Cue keywords: `learning, real, noise, distribution, diffusion, coupling, differentiable, waveform, slic, produces`
- Narration: By learning the real noise distribution with a diffusion model and coupling it to a differentiable waveform, SLIC produces an unbiased likelihood straight from detector data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_learning_real_noise_distribution_dif" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords learning, real, noise, distribution, diffusion, coupling in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_proof_concept_currently_single_detec`

- Preferred role: `content`
- Cue keywords: `proof, concept, currently, single-detector, four-second, segments, points, toward, fast, scalable`
- Narration: This proof of concept, currently single-detector and four-second segments, points toward fast, scalable, unbiased inference for future gravitational-wave observations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_proof_concept_currently_single_detec" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords proof, concept, currently, single-detector, four-second, segments in title/desc so the matcher can verify semantic overlap.
