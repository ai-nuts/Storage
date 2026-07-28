# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_color_powerful_cue_convolutional_net`

- Preferred role: `method`
- Cue keywords: `color, powerful, cue, convolutional, networks, readily, exploit, object, recognition, but`
- Narration: Color is a powerful cue that convolutional networks readily exploit for object recognition, but it becomes a liability when the colors seen at test time differ from those in training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_color_powerful_cue_convolutional_net" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords color, powerful, cue, convolutional, networks, readily in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_introduces_color_equivariant_convolu`

- Preferred role: `figure`
- Cue keywords: `introduces, color, equivariant, convolutions, ceconvs, new, building, block, shares, shape`
- Narration: This paper introduces Color Equivariant Convolutions, or CEConvs, a new building block that shares shape features across the color spectrum while preserving discriminative color information.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c2_introduces_color_equivariant_convolu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, color, equivariant, convolutions, ceconvs, new in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_hard_wiring_parameter_sharing_over_d`

- Preferred role: `content`
- Cue keywords: `hard-wiring, parameter, sharing, over, discrete, hue, shifts, ceconvs, let, networks`
- Narration: By hard-wiring parameter sharing over discrete hue shifts, CEConvs let networks like ResNets generalize to underrepresented colors and stay robust to test-time hue shifts, without throwing color away.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_hard_wiring_parameter_sharing_over_d" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hard-wiring, parameter, sharing, over, discrete, hue in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_convolutional_neural_networks_lean_h`

- Preferred role: `content`
- Cue keywords: `convolutional, neural, networks, lean, heavily, color, recognize, objects, but, real-world`
- Narration: Convolutional neural networks lean heavily on color to recognize objects, but real-world data rarely contains every color a class can take.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_convolutional_neural_networks_lean_h" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords convolutional, neural, networks, lean, heavily, color in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_when_trained_mostly_red_cars`

- Preferred role: `method`
- Cue keywords: `when, trained, mostly, red, cars, sees, blue, one, accuracy, collapses`
- Narration: When a model trained mostly on red cars sees a blue one, accuracy collapses.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_when_trained_mostly_red_cars" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, trained, mostly, red, cars, sees in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_classic_remedy_color_invariance_side`

- Preferred role: `content`
- Cue keywords: `classic, remedy, color, invariance, sidesteps, problem, removing, color, entirely, but`
- Narration: The classic remedy, color invariance, sidesteps the problem by removing color entirely, but that throws away a genuinely useful signal.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_classic_remedy_color_invariance_side" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classic, remedy, color, invariance, sidesteps, problem in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_frames_real_challenge_keeping_color`

- Preferred role: `method`
- Cue keywords: `frames, real, challenge, keeping, color, information, while, still, generalizing, across`
- Narration: The paper frames the real challenge as keeping color information while still generalizing across colors that were rare or absent during training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_frames_real_challenge_keeping_color" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords frames, real, challenge, keeping, color, information in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_group_equivariant_convolutions_taugh`

- Preferred role: `content`
- Cue keywords: `group, equivariant, convolutions, taught, networks, share, parameters, across, rotations, flips`
- Narration: Group equivariant convolutions taught networks to share parameters across rotations and flips, dramatically improving data efficiency for geometric transformations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_group_equivariant_convolutions_taugh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords group, equivariant, convolutions, taught, networks, share in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_yet_photometric_changes_such_shifts`

- Preferred role: `content`
- Cue keywords: `yet, photometric, changes, such, shifts, hue, had, been, left, aside`
- Narration: Yet photometric changes, such as shifts in hue, had been left aside.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_yet_photometric_changes_such_shifts" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yet, photometric, changes, such, shifts, hue in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_studies_trained_cnns_show_early`

- Preferred role: `method`
- Cue keywords: `studies, trained, cnns, show, early, layers, learn, strongly, color-selective, neurons`
- Narration: Studies of trained CNNs show that early layers learn strongly color-selective neurons, which suggests color is a natural axis for equivariance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_studies_trained_cnns_show_early" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords studies, trained, cnns, show, early, layers in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_motivates_treating_hue_shift_same`

- Preferred role: `content`
- Cue keywords: `motivates, treating, hue, shift, same, way, prior, work, treated, rotation`
- Narration: This motivates treating a hue shift the same way prior work treated a rotation: as a symmetry the network should respect by design, rather than something it must relearn from data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_motivates_treating_hue_shift_same" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords motivates, treating, hue, shift, same, way in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_core_contribution_color_equivariant`

- Preferred role: `content`
- Cue keywords: `core, contribution, color, equivariant, convolution, new, layer, hard-wires, parameter, sharing`
- Narration: The core contribution is the Color Equivariant Convolution, a new layer that hard-wires parameter sharing over hue shifts.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_core_contribution_color_equivariant" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, contribution, color, equivariant, convolution, new in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_shares_shape_information_across_colo`

- Preferred role: `content`
- Cue keywords: `shares, shape, information, across, color, spectrum, while, keeping, color, dedicated`
- Narration: It shares shape information across the color spectrum while keeping color in a dedicated group dimension of the feature map.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_shares_shape_information_across_colo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords shares, shape, information, across, color, spectrum in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_because_formulated_language_symmetry`

- Preferred role: `content`
- Cue keywords: `because, formulated, language, symmetry, groups, slots, directly, standard, networks, like`
- Narration: Because it is formulated in the language of symmetry groups, it slots directly into standard networks like ResNet with no architectural surgery.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_because_formulated_language_symmetry" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, formulated, language, symmetry, groups, slots in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_authors_demonstrate_through_both_con`

- Preferred role: `method`
- Cue keywords: `authors, demonstrate, through, both, controlled, toy, experiments, realistic, benchmarks, design`
- Narration: The authors demonstrate, through both controlled toy experiments and realistic benchmarks, that this design improves robustness to color shifts between training and testing and works hand in hand with color augmentation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_authors_demonstrate_through_both_con" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, demonstrate, through, both, controlled, toy in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_hue_shift_hsv_space_becomes`

- Preferred role: `content`
- Cue keywords: `hue, shift, hsv, space, becomes, rgb, space, rotation, around, gray`
- Narration: A hue shift in HSV space becomes, in RGB space, a rotation around the gray diagonal from black to white. The authors formalize this as the group H-n of n discrete rotations about that diagonal, a subgroup of all three-dimensional rotations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_hue_shift_hsv_space_becomes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hue, shift, hsv, space, becomes, rgb in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_color_equivariant_convolution_correl`

- Preferred role: `content`
- Cue keywords: `color, equivariant, convolution, correlates, input, hue-rotated, copies, filter, producing, feature`
- Narration: A Color Equivariant Convolution correlates the input with hue-rotated copies of each filter, producing feature maps that carry an extra dimension indexing the hue rotation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_color_equivariant_convolution_correl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords color, equivariant, convolution, correlates, input, hue-rotated in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_hidden_layers_filters_cyclically_per`

- Preferred role: `guidance`
- Cue keywords: `hidden, layers, filters, cyclically, permuted, across, dimension, equivariance, preserved, throughout`
- Narration: In hidden layers, filters are cyclically permuted across this dimension so equivariance is preserved throughout the network.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s05_c3_hidden_layers_filters_cyclically_per" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hidden, layers, filters, cyclically, permuted, across in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_because_extra_dimension_multiplies_n`

- Preferred role: `method`
- Cue keywords: `because, extra, dimension, multiplies, number, feature, maps, authors, decompose, filters`
- Narration: Because the extra dimension multiplies the number of feature maps, the authors decompose filters into spatial and pointwise components and offer hybrid variants that use color equivariance only in the early, most color-selective stages, keeping parameter and compute cost in check.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_because_extra_dimension_multiplies_n" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, extra, dimension, multiplies, number, feature in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_evaluation_spans_two_scales`

- Preferred role: `result`
- Cue keywords: `evaluation, spans, two, scales`
- Narration: The evaluation spans two scales.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_evaluation_spans_two_scales" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, spans, two, scales in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_first_two_synthetic_mnist_variants`

- Preferred role: `method`
- Cue keywords: `first, two, synthetic, mnist, variants, isolate, phenomenon, long-tailed, colormnist, strong`
- Narration: First, two synthetic MNIST variants isolate the phenomenon: a long-tailed ColorMNIST with strong class imbalance, and a biased ColorMNIST where each class has a characteristic hue with tunable spread.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_first_two_synthetic_mnist_variants" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, two, synthetic, mnist, variants, isolate in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_eight_standard_image_classification`

- Preferred role: `method`
- Cue keywords: `eight, standard, image, classification, benchmarks, cifar, stl-10, flowers-102, stanford, cars`
- Narration: Then, eight standard image classification benchmarks, from CIFAR and STL-10 to Flowers-102, Stanford Cars, and ImageNet, test the method in realistic settings.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_eight_standard_image_classification" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords eight, standard, image, classification, benchmarks, cifar in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_probe_robustness_every_test_image`

- Preferred role: `result`
- Cue keywords: `probe, robustness, every, test, image, re-rendered, under, gradual, hue, shift`
- Narration: To probe robustness, every test image is re-rendered under a gradual hue shift from minus one-hundred-eighty to plus one-hundred-eighty degrees, and accuracy is averaged across the full sweep.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_probe_robustness_every_test_image" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords probe, robustness, every, test, image, re-rendered in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_robustness_without`

- Preferred role: `result`
- Cue keywords: `headline, finding, robustness, without, cost, clean, accuracy, original, unshifted, test`
- Narration: The headline finding is robustness without a cost to clean accuracy. On the original, unshifted test sets, color equivariant ResNets perform on par with vanilla ResNets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_headline_finding_robustness_without" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, robustness, without, cost, clean in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_but_when_test_images_hue_shifted`

- Preferred role: `content`
- Cue keywords: `but, when, test, images, hue-shifted, gap, opens, dramatically`
- Narration: But when the test images are hue-shifted, the gap opens dramatically.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_but_when_test_images_hue_shifted" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, when, test, images, hue-shifted, gap in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_flowers_102_average_accuracy_across`

- Preferred role: `result`
- Cue keywords: `flowers-102, average, accuracy, across, hue, shifts, jumps, about, thirteen, percent`
- Narration: On Flowers-102, average accuracy across hue shifts jumps from about thirteen percent for the baseline to thirty-three percent for the fully equivariant model, and similar gains appear on CIFAR-100 and Stanford Cars.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_flowers_102_average_accuracy_across" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords flowers-102, average, accuracy, across, hue, shifts in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_controlled_long_tailed_experiment_eq`

- Preferred role: `result`
- Cue keywords: `controlled, long-tailed, experiment, equivariant, network, reaches, ninety-one, percent, against, baseline`
- Narration: In the controlled long-tailed experiment the equivariant network reaches ninety-one percent against the baseline's seventy-two percent, with the biggest improvements exactly on the rare classes that shape sharing is meant to help.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_controlled_long_tailed_experiment_eq" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords controlled, long-tailed, experiment, equivariant, network, reaches in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_clarify_design_choices_inc`

- Preferred role: `content`
- Cue keywords: `ablations, clarify, design, choices, increasing, number, discrete, hue, rotations, makes`
- Narration: The ablations clarify the design choices. Increasing the number of discrete hue rotations makes the network more robust to test-time hue shifts, though it slightly reduces capacity because channels must shrink to keep parameters fixed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablations_clarify_design_choices_inc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, clarify, design, choices, increasing, number in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_group_coset_pooling_turns_out`

- Preferred role: `content`
- Cue keywords: `group, coset, pooling, turns, out, mechanism, yields, hue, invariance, remove`
- Narration: Group coset pooling turns out to be the mechanism that yields hue invariance; remove it, and the network behaves like a regular one.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_group_coset_pooling_turns_out" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords group, coset, pooling, turns, out, mechanism in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_finally_color_equivariance_color_jit`

- Preferred role: `guidance`
- Cue keywords: `finally, color, equivariance, color-jitter, augmentation, complementary, equivariant, network, needs, lower`
- Narration: Finally, color equivariance and color-jitter augmentation are complementary: an equivariant network needs a lower intensity of augmentation to reach the same robustness.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s08_c3_finally_color_equivariance_color_jit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, color, equivariance, color-jitter, augmentation, complementary in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_color_selectivity_analysis_further_e`

- Preferred role: `method`
- Cue keywords: `color-selectivity, analysis, further, explains, when, method, helps, showing, datasets, more`
- Narration: A color-selectivity analysis further explains when the method helps, showing that datasets with more color-selective neurons benefit from equivariance up to later stages.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_color_selectivity_analysis_further_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords color-selectivity, analysis, further, explains, when, method in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_flowers_1`

- Preferred role: `result`
- Cue keywords: `few, numbers, capture, impact, flowers-102, under, hue, shifts, accuracy, nearly`
- Narration: A few numbers capture the impact. On Flowers-102 under hue shifts, accuracy nearly triples, from thirteen to thirty-three percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_flowers_1" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, flowers-102, under in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_long_tailed_color_experiment_equivar`

- Preferred role: `result`
- Cue keywords: `long-tailed, color, experiment, equivariant, network, gains, almost, twenty, points, over`
- Narration: On the long-tailed color experiment the equivariant network gains almost twenty points over the baseline.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_long_tailed_color_experiment_equivar" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords long-tailed, color, experiment, equivariant, network, gains in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_cifar_100_improves_fifteen_points_st`

- Preferred role: `result`
- Cue keywords: `cifar-100, improves, fifteen, points, stanford, cars, roughly, thirteen, points, hue-shifted`
- Narration: CIFAR-100 improves by fifteen points and Stanford Cars by roughly thirteen points on hue-shifted tests.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_cifar_100_improves_fifteen_points_st" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-100, improves, fifteen, points, stanford, cars in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_all_comes_modest_compute_overhead`

- Preferred role: `content`
- Cue keywords: `all, comes, modest, compute, overhead, since, filter, decomposition, keeps, increase`
- Narration: And all of this comes at a modest compute overhead, since the filter decomposition keeps the increase in operations and parameters to a small factor of the number of hue rotations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_all_comes_modest_compute_overhead" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, comes, modest, compute, overhead, since in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_color_deserves_same`

- Preferred role: `content`
- Cue keywords: `lasting, message, color, deserves, same, equivariance, treatment, rotations, translations, long`
- Narration: The lasting message is that color deserves the same equivariance treatment that rotations and translations have long enjoyed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lasting_message_color_deserves_same" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, color, deserves, same, equivariance in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_instead_choosing_between_exploiting`

- Preferred role: `content`
- Cue keywords: `instead, choosing, between, exploiting, color, being, robust, color, changes, color`
- Narration: Instead of choosing between exploiting color and being robust to color changes, Color Equivariant Convolutions let a network do both, by sharing shape information across the color spectrum while keeping color in its own dimension.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_instead_choosing_between_exploiting" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, choosing, between, exploiting, color, being in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_block_plugs_standard_architectures_p`

- Preferred role: `result`
- Cue keywords: `block, plugs, standard, architectures, plays, well, augmentation, delivers, its, largest`
- Narration: The block plugs into standard architectures, plays well with augmentation, and delivers its largest gains precisely where color matters most, offering a practical route to color-robust recognition.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_block_plugs_standard_architectures_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords block, plugs, standard, architectures, plays, well in title/desc so the matcher can verify semantic overlap.
