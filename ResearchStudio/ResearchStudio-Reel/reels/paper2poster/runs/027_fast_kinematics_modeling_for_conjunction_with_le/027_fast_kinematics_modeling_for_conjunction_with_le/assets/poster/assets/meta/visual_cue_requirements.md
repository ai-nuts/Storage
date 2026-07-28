# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_galaxy_kinematics_modeling_computati`

- Preferred role: `method`
- Cue keywords: `galaxy, kinematics, modeling, computational, bottleneck, when, astronomers, try, jointly, gravitational`
- Narration: Galaxy kinematics modeling is the computational bottleneck when astronomers try to jointly model gravitational lensing and kinematics to measure the Hubble constant.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_galaxy_kinematics_modeling_computati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords galaxy, kinematics, modeling, computational, bottleneck, when in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_introduces_skinn_stellar_kinematics`

- Preferred role: `content`
- Cue keywords: `introduces, skinn, stellar, kinematics, neural, network, proof-of-concept, emulator, reproduces, slow`
- Narration: This paper introduces SKiNN, the Stellar Kinematics Neural Network, a proof-of-concept emulator that reproduces slow physics-based kinematics calculations at a fraction of the cost.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_introduces_skinn_stellar_kinematics" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, skinn, stellar, kinematics, neural, network in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_after_one_time_phase_skinn_generates`

- Preferred role: `method`
- Cue keywords: `after, one-time, phase, skinn, generates, velocity, dispersion, images, accurate, within`
- Narration: After a one-time training phase, SKiNN generates velocity dispersion images that are accurate to within about one percent in the scientifically important region, while running two to three orders of magnitude faster than existing methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_after_one_time_phase_skinn_generates" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords after, one-time, phase, skinn, generates, velocity in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_speedup_finally_makes_feasible_spati`

- Preferred role: `content`
- Cue keywords: `speedup, finally, makes, feasible, spatially, resolved, kinematic, jointly, lensing, addressing`
- Narration: This speedup finally makes it feasible to model spatially resolved kinematic data jointly with lensing data, addressing the largest source of uncertainty in Hubble constant measurements.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_speedup_finally_makes_feasible_spati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords speedup, finally, makes, feasible, spatially, resolved in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_gravitational_lensing_measures_hubbl`

- Preferred role: `content`
- Cue keywords: `gravitational, lensing, measures, hubble, constant, comparing, time, delays, between, multiple`
- Narration: Gravitational lensing measures the Hubble constant by comparing time delays between multiple images of a distant source to a model of the lens galaxy's mass.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_gravitational_lensing_measures_hubbl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gravitational, lensing, measures, hubble, constant, comparing in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_lensing_degeneracies_allow_many`

- Preferred role: `method`
- Cue keywords: `but, lensing, degeneracies, allow, many, different, mass, distributions, reproduce, same`
- Narration: But lensing degeneracies allow many different mass distributions to reproduce the same image, so independent kinematic constraints are needed to break them. The trouble is speed.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_but_lensing_degeneracies_allow_many" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, lensing, degeneracies, allow, many, different in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_modeling_galaxy_kinematics_physics_c`

- Preferred role: `result`
- Cue keywords: `modeling, galaxy, kinematics, physics, code, like, jam, slow, must, recomputed`
- Narration: Modeling galaxy kinematics with a physics code like JAM is slow, and it must be recomputed for every single likelihood evaluation inside a Markov Chain Monte Carlo sampling.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c3_modeling_galaxy_kinematics_physics_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords modeling, galaxy, kinematics, physics, code, like in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_makes_jointly_exploring_full_lensing`

- Preferred role: `content`
- Cue keywords: `makes, jointly, exploring, full, lensing, kinematics, parameter, space, computationally, prohibitive`
- Narration: This makes jointly exploring the full lensing and kinematics parameter space computationally prohibitive, forcing modelers to cut corners by fitting the two components separately.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_makes_jointly_exploring_full_lensing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, jointly, exploring, full, lensing, kinematics in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_recently_spatially_resolved_kinemati`

- Preferred role: `method`
- Cue keywords: `recently, spatially, resolved, kinematics, lensing, galaxies, became, available, through, instruments`
- Narration: Recently, spatially resolved kinematics of lensing galaxies became available through instruments like the James Webb Space Telescope.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_recently_spatially_resolved_kinemati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recently, spatially, resolved, kinematics, lensing, galaxies in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_traditional_spherical_jeans_models_t`

- Preferred role: `content`
- Cue keywords: `traditional, spherical, jeans, models, too, simplistic, richer, they, lack, self-consistency`
- Narration: Traditional spherical Jeans models are too simplistic for this richer data, and they lack self-consistency with the elliptical mass models used in lensing.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_traditional_spherical_jeans_models_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords traditional, spherical, jeans, models, too, simplistic in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_natural_next_step_axisymmetric_model`

- Preferred role: `guidance`
- Cue keywords: `natural, next, step, axisymmetric, modeling, software, such, jam, but, jam`
- Narration: The natural next step is axisymmetric modeling with software such as JAM, but JAM is expensive. Existing frameworks that combine it with lens modeling either fit the two separately or remain far too slow for full joint parameter exploration.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s03_c3_natural_next_step_axisymmetric_model" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords natural, next, step, axisymmetric, modeling, software in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_key_insight_work_jam_slow`

- Preferred role: `method`
- Cue keywords: `key, insight, work, jam, slow, physics, emulated, neural, network, keeping`
- Narration: The key insight of this work is that JAM's slow physics can be emulated by a neural network, keeping the physics of the overall model while removing the computational bottleneck.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_key_insight_work_jam_slow" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, insight, work, jam, slow, physics in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_core_contribution_skinn_stellar_kine`

- Preferred role: `content`
- Cue keywords: `core, contribution, skinn, stellar, kinematics, neural, network`
- Narration: The core contribution is SKiNN, the Stellar Kinematics Neural Network.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_core_contribution_skinn_stellar_kine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, contribution, skinn, stellar, kinematics, neural in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_time_strategy_replacing_expens`

- Preferred role: `method`
- Cue keywords: `first, time, strategy, replacing, expensive, component, neural, network, been, applied`
- Narration: It is the first time the strategy of replacing an expensive model component with a neural network has been applied to the kinematic-modeling aspect of gravitational lens modeling.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_time_strategy_replacing_expens" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, time, strategy, replacing, expensive, component in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_crucially_skinn_emulates_only_jam`

- Preferred role: `content`
- Cue keywords: `crucially, skinn, emulates, only, jam, physics, calculation, rather, being, applied`
- Narration: Crucially, SKiNN emulates only the JAM physics calculation rather than being applied directly to observations. This design choice keeps the physics of the overall model intact while exploiting the speed and versatility of neural networks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_crucially_skinn_emulates_only_jam" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, skinn, emulates, only, jam, physics in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_result_roughly_300_fold_speedup`

- Preferred role: `result`
- Cue keywords: `result, roughly, 300, fold, speedup, sub-percent, accuracy, which, finally, makes`
- Narration: The result is a roughly 300-fold speedup at sub-percent accuracy, which finally makes joint lensing plus kinematics modeling computationally feasible.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_result_roughly_300_fold_speedup" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, roughly, 300, fold, speedup, sub-percent in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_skinn_precalculates_jam_lensing_appl`

- Preferred role: `content`
- Cue keywords: `skinn, precalculates, jam, lensing, applications, formally, function, maps, eight-dimensional, vector`
- Narration: SKiNN precalculates JAM for use in lensing applications. Formally, it is a function that maps an eight-dimensional vector of galaxy parameters into a d by d image of vrms, the quadratic sum of velocity dispersion and rotational velocity.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_skinn_precalculates_jam_lensing_appl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords skinn, precalculates, jam, lensing, applications, formally in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_eight_inputs_describe_power_law_elli`

- Preferred role: `method`
- Cue keywords: `eight, inputs, describe, power-law, elliptical, mass, distribution, elliptical, rsic, light`
- Narration: The eight inputs describe a power-law elliptical mass distribution and an elliptical Sérsic light profile, plus the galaxy inclination and orbital anisotropy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_eight_inputs_describe_power_law_elli" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords eight, inputs, describe, power-law, elliptical, mass in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_architecture_consists_five_blocks_tw`

- Preferred role: `figure`
- Cue keywords: `architecture, consists, five, blocks, two, two-dimensional, convolutional, layers, followed, upsampling`
- Narration: The architecture consists of five blocks, each with two two-dimensional convolutional layers followed by an upsampling layer and a ReLU nonlinearity, for about seven million trainable parameters.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c3_architecture_consists_five_blocks_tw" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords architecture, consists, five, blocks, two, two-dimensional in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_trained_minimizing_standard_mean_squ`

- Preferred role: `method`
- Cue keywords: `trained, minimizing, standard, mean-squared-error, loss, adam, optimizer, dataset, generated, jam`
- Narration: It is trained by minimizing a standard mean-squared-error loss with the Adam optimizer, using a dataset generated by JAM through the GLEE software so the network learns to mimic the JAM procedure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_trained_minimizing_standard_mean_squ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trained, minimizing, standard, mean-squared-error, loss, adam in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_set_constructed_entirely_jam_physics`

- Preferred role: `method`
- Cue keywords: `set, constructed, entirely, jam, physics, code, skinn, meant, imitate`
- Narration: The training set is constructed entirely with JAM, the physics code SKiNN is meant to imitate.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_set_constructed_entirely_jam_physics" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords set, constructed, entirely, jam, physics, code in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_authors_created_five_thousand_input`

- Preferred role: `method`
- Cue keywords: `authors, created, five, thousand, input-output, pairs, four, thousand, five, hundred`
- Narration: The authors created five thousand input-output pairs, using four thousand for training, five hundred for validation, and five hundred held out for testing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_authors_created_five_thousand_input" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, created, five, thousand, input-output, pairs in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_velocity_image_551_551_pixels`

- Preferred role: `method`
- Cue keywords: `velocity, image, 551, 551, pixels, generated, higher, resolution, real, creating`
- Narration: Each velocity image is 551 by 551 pixels, generated at higher resolution than real data. Creating a single image with JAM takes about fifteen seconds, which underscores why emulation is worthwhile.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_velocity_image_551_551_pixels" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords velocity, image, 551, 551, pixels, generated in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_network_implemented_pytorch_pytorch`

- Preferred role: `method`
- Cue keywords: `network, implemented, pytorch, pytorch, lightning, trained, five, tesla, p100, gpus`
- Narration: The network is implemented in PyTorch with PyTorch Lightning and trained on five Tesla P100 GPUs, each with sixteen gigabytes of memory, over roughly one day.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_network_implemented_pytorch_pytorch" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords network, implemented, pytorch, pytorch, lightning, trained in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_once_trained_skinn_produces_velocity`

- Preferred role: `method`
- Cue keywords: `once, trained, skinn, produces, velocity, image, input, parameter, vector, about`
- Narration: Once trained, SKiNN produces a velocity image from an input parameter vector in about fifty milliseconds on a single GPU, which is roughly three hundred times faster than JAM.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_once_trained_skinn_produces_velocity" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords once, trained, skinn, produces, velocity, image in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_accuracy_assessed_five_hundred_held`

- Preferred role: `result`
- Cue keywords: `accuracy, assessed, five, hundred, held-out, test, images, computing, relative, error`
- Narration: Accuracy is assessed on the five hundred held-out test images by computing the relative error at each pixel.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_accuracy_assessed_five_hundred_held" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords accuracy, assessed, five, hundred, held-out, test in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_while_some_outer_regions_show`

- Preferred role: `method`
- Cue keywords: `while, some, outer, regions, show, errors, few, percent, important, innermost`
- Narration: While some outer regions can show errors of a few percent, the important innermost region, where real data actually constrains the model, is matched to within plus or minus one percent for almost all pixels.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_while_some_outer_regions_show" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords while, some, outer, regions, show, errors in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_averaged_over_entire_images_median`

- Preferred role: `result`
- Cue keywords: `averaged, over, entire, images, median, absolute, error, about, 0.47, percent`
- Narration: Averaged over entire images, the median absolute error is about 0.47 percent and the ninetieth percentile is about 1.1 percent. Both are comfortably below the typical two-percent-or-greater systematic uncertainty in real velocity measurements.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_averaged_over_entire_images_median" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords averaged, over, entire, images, median, absolute in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_proof_of_concept_workshop_work_does`

- Preferred role: `content`
- Cue keywords: `proof-of-concept, workshop, work, does, not, present, formal, ablation, study`
- Narration: As a proof-of-concept workshop paper, this work does not present a formal ablation study.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_proof_of_concept_workshop_work_does" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords proof-of-concept, workshop, work, does, not, present in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_instead_performance_characterized_di`

- Preferred role: `method`
- Cue keywords: `instead, performance, characterized, distribution, per-pixel, errors, across, five, hundred, test`
- Narration: Instead, performance is characterized by the distribution of per-pixel errors across the five hundred test images, and by comparing inference on GPU versus CPU, where the GPU is about ten times faster.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_instead_performance_characterized_di" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, performance, characterized, distribution, per-pixel, errors in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_analysis_also_distinguishes_innermos`

- Preferred role: `method`
- Cue keywords: `analysis, also, distinguishes, innermost, two-arcsecond, region, where, errors, stay, within`
- Narration: The analysis also distinguishes the innermost two-arcsecond region, where errors stay within one percent, from the outer parts of the image, where errors can rise to a few percent but the data provides little constraint anyway.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_analysis_also_distinguishes_innermos" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords analysis, also, distinguishes, innermost, two-arcsecond, region in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_numbers_skinn_runs_about`

- Preferred role: `content`
- Cue keywords: `headline, numbers, skinn, runs, about, three, hundred, times, faster, jam`
- Narration: Here are the headline numbers. SKiNN runs about three hundred times faster than JAM, taking roughly fifty milliseconds per image on a GPU compared to about fifteen seconds for JAM.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_headline_numbers_skinn_runs_about" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, numbers, skinn, runs, about, three in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_its_error_under_one_percent`

- Preferred role: `result`
- Cue keywords: `its, error, under, one, percent, within, innermost, two-arcsecond, region, median`
- Narration: Its error is under one percent within the innermost two-arcsecond region, with a median absolute error around 0.47 percent and a ninetieth percentile of about 1.1 percent across five hundred test images.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_its_error_under_one_percent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, error, under, one, percent, within in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_network_maps_eight_dimensional_param`

- Preferred role: `content`
- Cue keywords: `network, maps, eight-dimensional, parameter, vector, velocity, image, about, seven, million`
- Narration: The network maps an eight-dimensional parameter vector to a velocity image and has about seven million trainable parameters.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_network_maps_eight_dimensional_param" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords network, maps, eight-dimensional, parameter, vector, velocity in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_trained_five_thousand_samples_split`

- Preferred role: `method`
- Cue keywords: `trained, five, thousand, samples, split, four, thousand, five, hundred, validation`
- Narration: It was trained on five thousand samples, split four thousand for training and five hundred each for validation and testing, over roughly one day on five Tesla P100 GPUs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_trained_five_thousand_samples_split" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trained, five, thousand, samples, split, four in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_neural_network_emulate_slow_kinemati`

- Preferred role: `method`
- Cue keywords: `neural, network, emulate, slow, kinematics, physics, jam, skinn, achieves, roughly`
- Narration: By training a neural network to emulate the slow kinematics physics of JAM, SKiNN achieves roughly a three-hundred-fold speedup at sub-percent accuracy in the region that matters.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_neural_network_emulate_slow_kinemati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neural, network, emulate, slow, kinematics, physics in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_removes_main_computational_bottlenec`

- Preferred role: `method`
- Cue keywords: `removes, main, computational, bottleneck, makes, feasible, jointly, gravitational, lensing, together`
- Narration: This removes the main computational bottleneck and makes it feasible to jointly model gravitational lensing together with spatially resolved kinematics, which corrects for the largest source of uncertainty in measuring the Hubble constant.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_removes_main_computational_bottlenec" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords removes, main, computational, bottleneck, makes, feasible in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_more_broadly_strategy_swapping_expen`

- Preferred role: `method`
- Cue keywords: `more, broadly, strategy, swapping, expensive, but, calculable, piece, trained, neural`
- Narration: More broadly, the strategy of swapping an expensive but calculable model piece for a trained neural network, while keeping the surrounding physics intact, likely transfers to many other scientific modeling problems.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_more_broadly_strategy_swapping_expen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords more, broadly, strategy, swapping, expensive, but in title/desc so the matcher can verify semantic overlap.
