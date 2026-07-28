# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_spherical_cnns_generalize_convolutio`

- Preferred role: `content`
- Cue keywords: `spherical, cnns, generalize, convolutional, networks, signals, living, sphere, which, makes`
- Narration: Spherical CNNs generalize convolutional networks to signals living on the sphere, which makes them a natural fit for molecules and weather data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_spherical_cnns_generalize_convolutio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spherical, cnns, generalize, convolutional, networks, signals in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_but_until_now_they_stuck`

- Preferred role: `content`
- Cue keywords: `but, until, now, they, stuck, low, resolutions, shallow, depths, they`
- Narration: But until now they were stuck at low resolutions and shallow depths, so they never really competed on large real-world problems.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_but_until_now_they_stuck" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, until, now, they, stuck, low in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_scaling_spherical_cnns_google_resear`

- Preferred role: `figure`
- Cue keywords: `scaling, spherical, cnns, google, research, mit, shows, how, scale, these`
- Narration: This paper, Scaling Spherical CNNs from Google Research and MIT, shows how to scale these models by a full order of magnitude.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c3_scaling_spherical_cnns_google_resear" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords scaling, spherical, cnns, google, research, mit in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_new_activations_normalization_residu`

- Preferred role: `method`
- Cue keywords: `new, activations, normalization, residual, blocks, tpu-optimized, implementation, authors, reach, state`
- Narration: With new activations, normalization, residual blocks, and a TPU-optimized implementation, the authors reach state of the art on the QM9 molecular benchmark and become competitive on several weather forecasting tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_new_activations_normalization_residu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords new, activations, normalization, residual, blocks, tpu-optimized in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_spherical_cnns_replace_plane_sphere`

- Preferred role: `content`
- Cue keywords: `spherical, cnns, replace, plane, sphere, domain, signal, which, exactly, right`
- Narration: Spherical CNNs replace the plane with the sphere as the domain of the signal, which is exactly right for data like molecules and the atmosphere.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_spherical_cnns_replace_plane_sphere" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spherical, cnns, replace, plane, sphere, domain in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_catch_their_core_operation_spherical`

- Preferred role: `content`
- Cue keywords: `catch, their, core, operation, spherical, convolution, most, accurate, spectral, domain`
- Narration: The catch is that their core operation, spherical convolution, is most accurate in the spectral domain, and that is far more expensive than an ordinary planar convolution.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_catch_their_core_operation_spherical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords catch, their, core, operation, spherical, convolution in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_because_cost_spherical_cnns_had`

- Preferred role: `content`
- Cue keywords: `because, cost, spherical, cnns, had, been, limited, small, low-resolution, problems`
- Narration: Because of this cost, spherical CNNs had been limited to small, low-resolution problems with modest model capacity.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_because_cost_spherical_cnns_had" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, cost, spherical, cnns, had, been in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_simply_large_scale_spherical_archite`

- Preferred role: `figure`
- Cue keywords: `simply, large-scale, spherical, architecture, analogous, deep, planar, networks, power, modern`
- Narration: There simply was no large-scale spherical architecture analogous to the deep planar networks that power modern computer vision.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c4_simply_large_scale_spherical_archite" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords simply, large-scale, spherical, architecture, analogous, deep in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_two_scientific_problems_motivate_wor`

- Preferred role: `content`
- Cue keywords: `two, scientific, problems, motivate, work, predicting, molecular, properties, forecasting, weather`
- Narration: Two scientific problems motivate this work: predicting molecular properties and forecasting the weather. Both are intrinsically spherical and tied to rotations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_two_scientific_problems_motivate_wor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, scientific, problems, motivate, work, predicting in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_molecule_properties_don_change_when`

- Preferred role: `content`
- Cue keywords: `molecule, properties, don, change, when, you, rotate, space, earth, atmosphere`
- Narration: A molecule's properties don't change when you rotate it in space, and the Earth's atmosphere is naturally a signal on a sphere.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_molecule_properties_don_change_when" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords molecule, properties, don, change, when, you in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_rotation_equivariant_spherical_cnns`

- Preferred role: `result`
- Cue keywords: `rotation-equivariant, spherical, cnns, should, perfect, match, but, standard, benchmarks, large`
- Narration: Rotation-equivariant spherical CNNs should be a perfect match. But the standard benchmarks are large.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c3_rotation_equivariant_spherical_cnns" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rotation-equivariant, spherical, cnns, should, perfect, match in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_qm9_one_hundred_thirty_four`

- Preferred role: `content`
- Cue keywords: `qm9, one, hundred, thirty, four, thousand, molecules, over, eighteen, times`
- Narration: QM9 has one hundred thirty four thousand molecules, over eighteen times bigger than the tiny QM7 set earlier spherical CNNs could handle, and weather grids demand high spatial resolution. To compete, these models had to scale.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_qm9_one_hundred_thirty_four" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords qm9, one, hundred, thirty, four, thousand in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_authors_contribute_systematic_recipe`

- Preferred role: `figure`
- Cue keywords: `authors, contribute, systematic, recipe, scaling, spherical, cnns, order, magnitude, three`
- Narration: The authors contribute a systematic recipe for scaling spherical CNNs by an order of magnitude. It has three parts.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c1_authors_contribute_systematic_recipe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, contribute, systematic, recipe, scaling, spherical in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_efficient_implementation_spin`

- Preferred role: `method`
- Cue keywords: `first, efficient, implementation, spin-weighted, spherical, harmonic, transforms, jax, tuned, run`
- Narration: First, an efficient implementation of spin-weighted spherical harmonic transforms in JAX, tuned to run fast and distributed on TPUs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_efficient_implementation_spin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, efficient, implementation, spin-weighted, spherical, harmonic in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_new_general_purpose_layers_ac`

- Preferred role: `content`
- Cue keywords: `second, new, general-purpose, layers, activations, improve, both, expressivity, efficiency, third`
- Narration: Second, new general-purpose layers and activations that improve both expressivity and efficiency. And third, application-specific input representations designed for molecules and for weather data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_second_new_general_purpose_layers_ac" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, new, general-purpose, layers, activations, improve in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_key_finding_naive_scaling_just`

- Preferred role: `figure`
- Cue keywords: `key, finding, naive, scaling, just, adding, depth, width, not, enough`
- Narration: A key finding is that naive scaling, just adding depth and width, is not enough; the core components themselves had to be redesigned.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c4_key_finding_naive_scaling_just" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, finding, naive, scaling, just, adding in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_builds_spin_weighted_spherica`

- Preferred role: `method`
- Cue keywords: `method, builds, spin-weighted, spherical, cnns, its, centerpiece, set, new, components`
- Narration: The method builds on spin-weighted spherical CNNs. Its centerpiece is a set of new components that all live in the spectral domain.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_builds_spin_weighted_spherica" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, builds, spin-weighted, spherical, cnns, its in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_phase_collapse_nonlinearity_takes_mo`

- Preferred role: `content`
- Cue keywords: `phase, collapse, nonlinearity, takes, modulus, features, collapse, their, phase, which`
- Narration: A phase collapse nonlinearity takes the modulus of the features to collapse their phase, which restores rotation invariance while losing no information in the nonzero spins.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_phase_collapse_nonlinearity_takes_mo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords phase, collapse, nonlinearity, takes, modulus, features in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_batch_normalization_pooling_also_mov`

- Preferred role: `method`
- Cue keywords: `batch, normalization, pooling, also, moved, spectral, domain, residual, block, adds`
- Narration: Batch normalization and pooling are also moved into the spectral domain, and the residual block adds its skip connection directly between Fourier coefficients.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_batch_normalization_pooling_also_mov" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords batch, normalization, pooling, also, moved, spectral in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_implementation_side_authors_compute`

- Preferred role: `method`
- Cue keywords: `implementation, side, authors, compute, fourier, transforms, dense, matrix, multiplications, rather`
- Narration: On the implementation side, the authors compute the Fourier transforms as dense matrix multiplications rather than fast Fourier transforms, because on TPUs matrix multiplies are extremely fast while memory reshuffling is the bottleneck.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_implementation_side_authors_compute" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords implementation, side, authors, compute, fourier, transforms in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_span_two_very_different`

- Preferred role: `content`
- Cue keywords: `experiments, span, two, very, different, domains`
- Narration: The experiments span two very different domains.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_span_two_very_different" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, span, two, very, different, domains in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_molecules_benchmark_qm9_one_hundred`

- Preferred role: `result`
- Cue keywords: `molecules, benchmark, qm9, one, hundred, thirty, four, thousand, molecules, twenty`
- Narration: For molecules, the benchmark is QM9, with one hundred thirty four thousand molecules, up to twenty nine atoms each, and twelve regression targets covering energetic, electronic, and thermodynamic properties.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_molecules_benchmark_qm9_one_hundred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords molecules, benchmark, qm9, one, hundred, thirty in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_weather_models_trained_era5_reanalys`

- Preferred role: `method`
- Cue keywords: `weather, models, trained, era5, reanalysis, through, weatherbench, benchmark, forecasting, quantities`
- Narration: For weather, the models are trained on ERA5 reanalysis data through the WeatherBench benchmark, forecasting quantities like geopotential height and temperature at three and five day horizons, plus longer tasks reaching out to twenty eight days and iterative high-resolution forecasting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_weather_models_trained_era5_reanalys" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords weather, models, trained, era5, reanalysis, through in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_strong_both_fronts`

- Preferred role: `method`
- Cue keywords: `results, strong, both, fronts`
- Narration: The results are strong on both fronts.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_strong_both_fronts" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, strong, both, fronts in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_qm9_scaled_spherical_cnn_reaches`

- Preferred role: `method`
- Cue keywords: `qm9, scaled, spherical, cnn, reaches, state, art, beating, previously, dominant`
- Narration: On QM9, the scaled spherical CNN reaches state of the art, beating the previously dominant graph neural networks and transformers on eight of twelve targets under the first data split and nine of twelve under the second.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_qm9_scaled_spherical_cnn_reaches" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords qm9, scaled, spherical, cnn, reaches, state in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_weather_outperforms_weatherbench_bas`

- Preferred role: `method`
- Cue keywords: `weather, outperforms, weatherbench, baseline, every, metric, simpler, two-predictor, setting, even`
- Narration: On weather, it outperforms the WeatherBench baseline on every metric in the simpler two-predictor setting, and it even beats models that were pre-trained on large amounts of simulated data on several temperature metrics.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_weather_outperforms_weatherbench_bas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords weather, outperforms, weatherbench, baseline, every, metric in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_first_demonstration_spherical_cnns_v`

- Preferred role: `method`
- Cue keywords: `first, demonstration, spherical, cnns, viable, neural, weather, models`
- Narration: This is the first demonstration that spherical CNNs are viable neural weather models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_first_demonstration_spherical_cnns_v" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, demonstration, spherical, cnns, viable, neural in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_careful_ablation_isolates_effect_cha`

- Preferred role: `content`
- Cue keywords: `careful, ablation, isolates, effect, change`
- Narration: A careful ablation isolates the effect of each change.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_careful_ablation_isolates_effect_cha" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords careful, ablation, isolates, effect, change in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_starting_jax_implementation_phase_co`

- Preferred role: `method`
- Cue keywords: `starting, jax, implementation, phase, collapse, activation, cuts, error, eight, percent`
- Narration: Starting from the JAX implementation, the phase collapse activation cuts error by eight percent, spectral batch normalization trims a further one and a half percent, and the efficient residual block another two and a half percent, all while improving speed.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_starting_jax_implementation_phase_co" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords starting, jax, implementation, phase, collapse, activation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_separate_comparison_confirms_phase_c`

- Preferred role: `result`
- Cue keywords: `separate, comparison, confirms, phase, collapse, activation, spectral, pooling, new, spherical`
- Narration: A separate comparison confirms that the phase collapse activation, spectral pooling, and the new spherical molecule representation each beat the prior alternatives from earlier work, together driving the QM9 enthalpy error down to about fifteen point two five milli electron volts.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_separate_comparison_confirms_phase_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separate, comparison, confirms, phase, collapse, activation in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_summarize_impact_models_scal`

- Preferred role: `content`
- Cue keywords: `numbers, summarize, impact, models, scale, one, full, order, magnitude, both`
- Narration: Here are the numbers that summarize the impact. The models scale by one full order of magnitude in both operations and feature resolution compared to prior spherical CNNs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_numbers_summarize_impact_models_scal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, summarize, impact, models, scale, one in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_they_set_state_art_eight`

- Preferred role: `content`
- Cue keywords: `they, set, state, art, eight, twelve, qm9, targets, first, split`
- Narration: They set state of the art on eight of twelve QM9 targets in the first split and nine of twelve in the second.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_they_set_state_art_eight" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, set, state, art, eight, twelve in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_new_jax_implementation_about_three`

- Preferred role: `method`
- Cue keywords: `new, jax, implementation, about, three, times, faster, original, running, distributed`
- Narration: The new JAX implementation is about three times faster than the original, and running distributed across thirty two TPUs speeds it up by a hundred times or more.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_new_jax_implementation_about_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords new, jax, implementation, about, three, times in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_phase_collapse_nonlinearity_alone_re`

- Preferred role: `result`
- Cue keywords: `phase, collapse, nonlinearity, alone, reduces, qm9, error, eight, percent`
- Narration: And the phase collapse nonlinearity alone reduces QM9 error by eight percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_phase_collapse_nonlinearity_alone_re" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords phase, collapse, nonlinearity, alone, reduces, qm9 in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_spherical_cnns_never_fundam`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, spherical, cnns, never, fundamentally, limited, they, just, poorly, scaled`
- Narration: The takeaway is that spherical CNNs were never fundamentally limited, they were just poorly scaled.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_spherical_cnns_never_fundam" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, spherical, cnns, never, fundamentally, limited in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_redesign_nonlinearity_normalization`

- Preferred role: `method`
- Cue keywords: `redesign, nonlinearity, normalization, residual, block, plus, implementation, tuned, modern, accelerators`
- Narration: With a redesign of the nonlinearity, normalization, and residual block, plus an implementation tuned to modern accelerators, these models finally scale to real problems, reaching state of the art on molecular property prediction and becoming genuinely competitive neural weather models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_redesign_nonlinearity_normalization" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords redesign, nonlinearity, normalization, residual, block, plus in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_authors_release_their_jax_implementa`

- Preferred role: `content`
- Cue keywords: `authors, release, their, jax, implementation, platform, further, research, spherical`
- Narration: The authors release their JAX implementation as a platform for further research on spherical data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_authors_release_their_jax_implementa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, release, their, jax, implementation, platform in title/desc so the matcher can verify semantic overlap.
