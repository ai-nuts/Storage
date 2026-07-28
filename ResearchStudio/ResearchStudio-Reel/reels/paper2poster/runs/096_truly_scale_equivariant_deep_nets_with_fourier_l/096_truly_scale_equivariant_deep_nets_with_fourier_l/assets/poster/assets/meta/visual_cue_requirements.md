# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_computer_vision_models_should_adapt`

- Preferred role: `content`
- Cue keywords: `computer, vision, models, should, adapt, gracefully, when, image, resolution, changes`
- Narration: In computer vision, models should adapt gracefully when image resolution changes, a property called scale-equivariance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_computer_vision_models_should_adapt" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords computer, vision, models, should, adapt, gracefully in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_purdue_university_points_out_existin`

- Preferred role: `figure`
- Cue keywords: `purdue, university, points, out, existing, scale-equivariant, cnns, not, truly, scale-equivariant`
- Narration: This paper, from Purdue University, points out that existing scale-equivariant CNNs are not truly scale-equivariant, because they formulate down-scaling in the continuous domain and ignore anti-aliasing.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c2_purdue_university_points_out_existin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords purdue, university, points, out, existing, scale-equivariant in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_instead_formulate_down_scali`

- Preferred role: `result`
- Cue keywords: `authors, instead, formulate, down-scaling, directly, discrete, domain, anti-aliasing, build, new`
- Narration: The authors instead formulate down-scaling directly in the discrete domain with anti-aliasing, and build a new family of deep nets from Fourier layers that achieves absolute zero equivariance error, both in theory and in practice, while staying competitive on classification accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c3_authors_instead_formulate_down_scali" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, instead, formulate, down-scaling, directly, discrete in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_scale_equivariance_means_when_object`

- Preferred role: `content`
- Cue keywords: `scale-equivariance, means, when, object, image, resized, network, features, should, transform`
- Narration: Scale-equivariance means that when an object in an image is resized, the network's features should transform consistently, and its label should stay the same.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_scale_equivariance_means_when_object" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords scale-equivariance, means, when, object, image, resized in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_recent_scale_equivariant_convolution`

- Preferred role: `content`
- Cue keywords: `recent, scale-equivariant, convolutional, networks, pursue, through, weight-sharing, kernel, resizing, same`
- Narration: Recent scale-equivariant convolutional networks pursue this through weight-sharing and kernel resizing, using the same but resized kernel across scales.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_recent_scale_equivariant_convolution" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recent, scale-equivariant, convolutional, networks, pursue, through in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_trouble_these_methods_derived_contin`

- Preferred role: `method`
- Cue keywords: `trouble, these, methods, derived, continuous, domain, discretized, when, implemented`
- Narration: The trouble is that these methods are derived in the continuous domain, then discretized when implemented.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_trouble_these_methods_derived_contin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trouble, these, methods, derived, continuous, domain in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_discretization_step_introduces_non_n`

- Preferred role: `result`
- Cue keywords: `discretization, step, introduces, non-negligible, equivariance, error, networks, only, approximately, scale-equivariant`
- Narration: That discretization step introduces a non-negligible equivariance error, so the networks are only approximately scale-equivariant, not truly so.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c4_discretization_step_introduces_non_n" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords discretization, step, introduces, non-negligible, equivariance, error in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_key_insight_down_scaling_discrete_si`

- Preferred role: `figure`
- Cue keywords: `key, insight, down-scaling, discrete, signal, fundamentally, signal-processing, operation`
- Narration: The key insight is that down-scaling a discrete signal is fundamentally a signal-processing operation.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c1_key_insight_down_scaling_discrete_si" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, insight, down-scaling, discrete, signal, fundamentally in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_nyquist_sampling_theorem_tells_befor`

- Preferred role: `content`
- Cue keywords: `nyquist, sampling, theorem, tells, before, subsampling, must, apply, anti-aliasing, filter`
- Narration: The Nyquist sampling theorem tells us that before subsampling, we must apply an anti-aliasing filter, otherwise high-frequency content folds down into lower frequencies, the classic aliasing artifact seen in the wagon-wheel effect.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_nyquist_sampling_theorem_tells_befor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords nyquist, sampling, theorem, tells, before, subsampling in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_prior_scale_equivariant_networks_bec`

- Preferred role: `content`
- Cue keywords: `prior, scale-equivariant, networks, because, they, formulated, continuous, domain, simply, had`
- Narration: Prior scale-equivariant networks, because they were formulated in the continuous domain, simply had no place for this filter.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_prior_scale_equivariant_networks_bec" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, scale-equivariant, networks, because, they, formulated in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_authors_argue_truly_scale_equivarian`

- Preferred role: `figure`
- Cue keywords: `authors, argue, truly, scale-equivariant, you, must, formulate, down-scaling, directly, discrete`
- Narration: The authors argue that to be truly scale-equivariant, you must formulate the down-scaling directly in the discrete domain, with anti-aliasing built in from the start.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c4_authors_argue_truly_scale_equivarian" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, truly, scale-equivariant, you, must in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_formulates_down_scaling_operat`

- Preferred role: `figure`
- Cue keywords: `first, formulates, down-scaling, operation, directly, discrete, domain, ideal, downsampling, properly`
- Narration: First, it formulates the down-scaling operation directly in the discrete domain as ideal downsampling, properly accounting for anti-aliasing.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c2_first_formulates_down_scaling_operat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, formulates, down-scaling, operation, directly, discrete in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_proposes_whole_family_deep`

- Preferred role: `guidance`
- Cue keywords: `second, proposes, whole, family, deep, nets, truly, scale-equivariant, rethinking, every`
- Narration: Second, it proposes a whole family of deep nets that are truly scale-equivariant, by rethinking every component, convolution layers, non-linearities, and pooling, and re-expressing them as Fourier layers that obey a simple frequency-dependency rule.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c3_second_proposes_whole_family_deep" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, proposes, whole, family, deep, nets in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_through_extensive_experiments`

- Preferred role: `result`
- Cue keywords: `third, through, extensive, experiments, mnist-scale, stl-10, shows, attains, absolute, zero`
- Narration: Third, through extensive experiments on MNIST-scale and STL-10, it shows the model attains an absolute zero end-to-end scale-equivariance error while remaining competitive in classification accuracy and more data-efficient in low-resource settings.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_third_through_extensive_experiments" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, through, extensive, experiments, mnist-scale, stl-10 in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_starts_precise_definition_dow`

- Preferred role: `method`
- Cue keywords: `method, starts, precise, definition, down-scaling, ideal, downsampling, which, first, applies`
- Narration: The method starts from a precise definition of down-scaling: ideal downsampling, which first applies an ideal low-pass filter that zeros out all frequencies above the new Nyquist limit, then subsamples.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_starts_precise_definition_dow" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, starts, precise, definition, down-scaling, ideal in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_authors_derive_their_central_conditi`

- Preferred role: `content`
- Cue keywords: `authors, derive, their, central, condition, claim, 1, deep, net, truly`
- Narration: From this the authors derive their central condition, Claim 1: a deep net is truly scale-equivariant if and only if every output frequency term depends only on input frequency terms that are equal or lower.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_authors_derive_their_central_conditi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, derive, their, central, condition, claim in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_they_redesign_network_component_sati`

- Preferred role: `method`
- Cue keywords: `they, redesign, network, component, satisfy, rule, spatially-local, fourier, layer, constrains`
- Narration: They then redesign each network component to satisfy this rule. A spatially-local Fourier layer constrains the kernel so it learns local features while staying equivariant. A scale-equivariant non-linearity applies ReLU frequency-band by frequency-band. A Fourier pooling layer preserves the same dependency structure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_they_redesign_network_component_sati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, redesign, network, component, satisfy, rule in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_top_equivariant_feature_extractor_th`

- Preferred role: `figure`
- Cue keywords: `top, equivariant, feature, extractor, they, add, classifier, predicts, once, per`
- Narration: On top of the equivariant feature extractor, they add a classifier that predicts once per scale, sharing a single MLP across scales through Fourier padding, and train it with a hinge consistency loss that penalizes the model whenever a higher-resolution image is predicted worse than its lower-resolution version.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c4_top_equivariant_feature_extractor_th" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, equivariant, feature, extractor, they, add in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_authors_follow_prior_work_evaluate`

- Preferred role: `result`
- Cue keywords: `authors, follow, prior, work, evaluate, two, benchmarks`
- Narration: The authors follow prior work and evaluate on two benchmarks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_authors_follow_prior_work_evaluate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, follow, prior, work, evaluate, two in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_mnist_scale_built_randomly_downsampl`

- Preferred role: `result`
- Cue keywords: `mnist-scale, built, randomly, downsampling, mnist, digits, every, resolution, eight-by-eight, twenty-eight-by-twenty-eight`
- Narration: MNIST-scale is built by randomly downsampling MNIST digits so that every resolution from eight-by-eight up to twenty-eight-by-twenty-eight is equally represented.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_mnist_scale_built_randomly_downsampl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mnist-scale, built, randomly, downsampling, mnist, digits in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_stl10_scale_applies_same_constructio`

- Preferred role: `method`
- Cue keywords: `stl10-scale, applies, same, construction, natural, color, images, spanning, resolutions, forty-eight`
- Narration: STL10-scale applies the same construction to natural color images, spanning resolutions from forty-eight up to ninety-seven.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_stl10_scale_applies_same_constructio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stl10-scale, applies, same, construction, natural, color in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_they_study_performance_under_ideal`

- Preferred role: `method`
- Cue keywords: `they, study, performance, under, ideal, downsampling, where, theory, exactly, matches`
- Narration: They study performance under ideal downsampling, where theory exactly matches practice, generalization to unseen scales, data efficiency at 5k, 2.5k, and 1k training samples, and a harder non-ideal downsampling setting where the anti-aliasing filter is imperfect.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_they_study_performance_under_ideal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, study, performance, under, ideal, downsampling in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_striking`

- Preferred role: `method`
- Cue keywords: `results, striking`
- Narration: The results are striking.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_striking" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, striking in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_mnist_scale_ideal_downsampling_achie`

- Preferred role: `method`
- Cue keywords: `mnist-scale, ideal, downsampling, achieves, highest, accuracy, ninety-eight, point, nine, percent`
- Narration: On MNIST-scale with ideal downsampling, the model achieves the highest accuracy at ninety-eight point nine percent, the highest scale-consistency at ninety-seven percent, and, crucially, an absolute zero equivariance error, while competing methods like DISCO show errors around zero point four.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_mnist_scale_ideal_downsampling_achie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mnist-scale, ideal, downsampling, achieves, highest, accuracy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_advantage_largest_harder_stl10_scale`

- Preferred role: `method`
- Cue keywords: `advantage, largest, harder, stl10-scale, natural-image, benchmark, where, reaches, seventy-three, percent`
- Narration: The advantage is largest on the harder STL10-scale natural-image benchmark, where the model reaches seventy-three percent accuracy against roughly fifty-eight percent for the strongest baseline, a gain of about fifteen points, still with exactly zero equivariance error.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_advantage_largest_harder_stl10_scale" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords advantage, largest, harder, stl10-scale, natural-image, benchmark in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_also_degrades_gracefully_even_under`

- Preferred role: `method`
- Cue keywords: `also, degrades, gracefully, even, under, non-ideal, downsampling, remains, best, low-data`
- Narration: It also degrades gracefully: even under non-ideal downsampling it remains the best model, and in low-data regimes it is the most data-efficient of all methods tested.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_also_degrades_gracefully_even_under" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, degrades, gracefully, even, under, non-ideal in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_isolates_consistency_loss_a`

- Preferred role: `method`
- Cue keywords: `ablation, isolates, consistency, loss, across, training-set, sizes, five, thousand, twenty-five`
- Narration: An ablation isolates the consistency loss. Across training-set sizes of five thousand, twenty-five hundred, and one thousand samples, adding the consistency loss consistently improves both accuracy and the scale-consistency rate.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_ablation_isolates_consistency_loss_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, isolates, consistency, loss, across, training-set in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_example_five_thousand_samples_scale`

- Preferred role: `content`
- Cue keywords: `example, five, thousand, samples, scale-consistency, rises, ninety-one, half, percent, nearly`
- Narration: For example, at five thousand samples the scale-consistency rises from ninety-one and a half percent to nearly ninety-three percent.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_example_five_thousand_samples_scale" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords example, five, thousand, samples, scale-consistency, rises in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_confirms_hinge_consistency_loss_doin`

- Preferred role: `figure`
- Cue keywords: `confirms, hinge, consistency, loss, doing, real, work, encouraging, make, better`
- Narration: This confirms that the hinge consistency loss is doing real work, encouraging the model to make better predictions as resolution increases.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c3_confirms_hinge_consistency_loss_doin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords confirms, hinge, consistency, loss, doing, real in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_authors_also_note_applying_non_linea`

- Preferred role: `result`
- Cue keywords: `authors, also, note, applying, non-linearity, directly, frequency, domain, though, equivariant`
- Narration: The authors also note that applying the non-linearity directly in the frequency domain, though equivariant, hurt classification, which is why they designed the spatial-domain scale-equivariant non-linearity.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_authors_also_note_applying_non_linea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, note, applying, non-linearity, directly in title/desc so the matcher can verify semantic overlap.

## Slide 09: takeaway

Heading: Takeaway

### Cue 1: `cue_s09_c1_lasting_takeaway_scale_equivariance`

- Preferred role: `takeaway`
- Cue keywords: `lasting, takeaway, scale-equivariance, should, treated, signal-processing, problem`
- Narration: The lasting takeaway is that scale-equivariance should be treated as a signal-processing problem.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s09_c1_lasting_takeaway_scale_equivariance" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, takeaway, scale-equivariance, should, treated, signal-processing in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_once_you_formulate_down_scaling_idea`

- Preferred role: `method`
- Cue keywords: `once, you, formulate, down-scaling, ideal, anti-aliased, downsampling, require, every, output`
- Narration: Once you formulate down-scaling as ideal, anti-aliased downsampling and require every output frequency to depend only on equal or lower input frequencies, you can build networks from Fourier layers that are exactly scale-equivariant, with provably zero error rather than the small residual errors that plagued earlier methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_once_you_formulate_down_scaling_idea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords once, you, formulate, down-scaling, ideal, anti-aliased in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_theoretical_guarantee_comes_practica`

- Preferred role: `result`
- Cue keywords: `theoretical, guarantee, comes, practical, cost, matches, beats, prior, scale-equivariant, cnns`
- Narration: And this theoretical guarantee comes at no practical cost: the model matches or beats prior scale-equivariant CNNs on accuracy and is more data-efficient, especially on challenging natural images.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_theoretical_guarantee_comes_practica" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords theoretical, guarantee, comes, practical, cost, matches in title/desc so the matcher can verify semantic overlap.
