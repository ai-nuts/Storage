# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_infinitygan_asks_bold_question_synth`

- Preferred role: `method`
- Cue keywords: `infinitygan, asks, bold, question, synthesize, images, arbitrary, even, infinite, size`
- Narration: InfinityGAN asks a bold question: can a model synthesize images of arbitrary, even infinite size, while training only on small patches on a single consumer GPU?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_infinitygan_asks_bold_question_synth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords infinitygan, asks, bold, question, synthesize, images in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_existing_high_resolution_gans_fail_b`

- Preferred role: `content`
- Cue keywords: `existing, high-resolution, gans, fail, because, compute, memory, all, scale, output`
- Narration: Existing high-resolution GANs fail because compute, memory, and data all scale with output resolution.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_existing_high_resolution_gans_fail_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, high-resolution, gans, fail, because, compute in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_infinitygan_breaks_coupling_disentan`

- Preferred role: `method`
- Cue keywords: `infinitygan, breaks, coupling, disentangling, image, global, appearance, local, structure, fine`
- Narration: InfinityGAN breaks that coupling, disentangling an image into global appearance, local structure, and fine texture, and generating any region patch-by-patch from continuous coordinates, seamless, globally consistent, and unbounded in size.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_infinitygan_breaks_coupling_disentan" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords infinitygan, breaks, coupling, disentangling, image, global in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_modern_generative_models_keep_improv`

- Preferred role: `method`
- Cue keywords: `modern, generative, models, keep, improving, resolution, detail, but, every, gain`
- Narration: Modern generative models keep improving in resolution and detail, but every gain costs more training time, a bigger model, and large field-of-view images that are hard to collect.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_modern_generative_models_keep_improv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords modern, generative, models, keep, improving, resolution in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_worse_existing_generators_locked_the`

- Preferred role: `method`
- Cue keywords: `worse, existing, generators, locked, their, resolution`
- Narration: Worse, existing generators are locked to their training resolution.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_worse_existing_generators_locked_the" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords worse, existing, generators, locked, their, resolution in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_push_them_larger_compute_memory`

- Preferred role: `method`
- Cue keywords: `push, them, larger, compute, memory, explode, quadratically, while, global, structure`
- Narration: Push them larger, and compute and memory explode quadratically while global structure falls apart.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_push_them_larger_compute_memory" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords push, them, larger, compute, memory, explode in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_infinitygan_asks_how_escape_coupling`

- Preferred role: `title`
- Cue keywords: `infinitygan, asks, how, escape, coupling, synthesize, arbitrary, even, infinite, images`
- Narration: InfinityGAN asks how to escape this coupling and synthesize arbitrary, even infinite images from finite data on modest hardware.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c4_infinitygan_asks_how_escape_coupling" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords infinitygan, asks, how, escape, coupling, synthesize in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_existing_models_fail_when`

- Preferred role: `content`
- Cue keywords: `why, existing, models, fail, when, asked, grow, insight, generators, like`
- Narration: Why do existing models fail when asked to grow? The insight: generators like StyleGAN2 secretly rely on zero-padding at the borders to encode position.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_why_existing_models_fail_when" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, existing, models, fail, when, asked in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_during_padding_pattern_fixed_network`

- Preferred role: `method`
- Cue keywords: `during, padding, pattern, fixed, network, memorizes`
- Narration: During training the padding pattern is fixed, so the network memorizes it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_during_padding_pattern_fixed_network" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords during, padding, pattern, fixed, network, memorizes in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_but_synthesize_larger_image_feature`

- Preferred role: `content`
- Cue keywords: `but, synthesize, larger, image, feature, size, changes, padding-derived, position, shifts`
- Narration: But synthesize a larger image, and the feature size changes, the padding-derived position shifts, and the image center no longer gets sensible positional information, producing repetitive, broken content.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_but_synthesize_larger_image_feature" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, synthesize, larger, image, feature, size in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_truly_infinite_synthesis_needs_posit`

- Preferred role: `content`
- Cue keywords: `truly, infinite, synthesis, needs, position, valid, infinitely, far, any, border`
- Narration: Truly infinite synthesis needs position valid infinitely far from any border, plus patches that combine seamlessly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_truly_infinite_synthesis_needs_posit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords truly, infinite, synthesis, needs, position, valid in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_infinitygan_makes_five_contributions`

- Preferred role: `method`
- Cue keywords: `infinitygan, makes, five, contributions, first, reframes, generation, disentangling, global, appearance`
- Narration: InfinityGAN makes five contributions. First, it reframes generation as disentangling global appearance, local structure, and fine texture, each with a dedicated component.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_infinitygan_makes_five_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords infinitygan, makes, five, contributions, first, reframes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_structure_synthesizer_built_n`

- Preferred role: `method`
- Cue keywords: `second, structure, synthesizer, built, neural, implicit, function, driven, continuous, coordinates`
- Narration: Second, a structure synthesizer built as a neural implicit function driven by continuous coordinates, so any sub-region can be queried directly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_second_structure_synthesizer_built_n" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, structure, synthesizer, built, neural, implicit in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_padding_free_generator_removin`

- Preferred role: `content`
- Cue keywords: `third, padding-free, generator, removing, all, zero-padding, letting, patches, synthesize, independently`
- Narration: Third, a padding-free generator removing all zero-padding, letting patches synthesize independently yet combine seamlessly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_third_padding_free_generator_removin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, padding-free, generator, removing, all, zero-padding in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_fourth_scale_invariant_fid_metric_si`

- Preferred role: `content`
- Cue keywords: `fourth, scale-invariant, fid, metric, sizes, where, real, reference, images, exist`
- Narration: Fourth, a scale-invariant FID metric for sizes where no real reference images exist. Finally, applications the design unlocks, from spatial style fusion to outpainting.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_fourth_scale_invariant_fid_metric_si" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, scale-invariant, fid, metric, sizes, where in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_infinitygan_generator_two_modules_st`

- Preferred role: `method`
- Cue keywords: `infinitygan, generator, two, modules, structure, synthesizer, neural, implicit, function, takes`
- Narration: InfinityGAN's generator has two modules. The structure synthesizer is a neural implicit function: it takes a global latent for scene appearance, a local latent tensor for variation, and a continuous coordinate grid, and outputs a structural latent for any region.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_infinitygan_generator_two_modules_st" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords infinitygan, generator, two, modules, structure, synthesizer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_coordinates_sine_cosine_horizontally`

- Preferred role: `content`
- Cue keywords: `coordinates, sine-cosine, horizontally, exploit, landscape, self-similarity, tanh, vertically, ground-to-sky, gradient`
- Narration: Coordinates use sine-cosine horizontally to exploit landscape self-similarity and a tanh vertically for the ground-to-sky gradient, so it can be queried infinitely far from the origin.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_coordinates_sine_cosine_horizontally" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords coordinates, sine-cosine, horizontally, exploit, landscape, self-similarity in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_texture_synthesizer_fully_convolutio`

- Preferred role: `method`
- Cue keywords: `texture, synthesizer, fully-convolutional, stylegan2, all, zero-padding, removed, turning, structural, latent`
- Narration: The texture synthesizer is a fully-convolutional StyleGAN2 with all zero-padding removed, turning the structural latent, global style, and noise into a patch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_texture_synthesizer_fully_convolutio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords texture, synthesizer, fully-convolutional, stylegan2, all, zero-padding in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_padding_same_coordinate_always_yield`

- Preferred role: `method`
- Cue keywords: `padding, same, coordinate, always, yields, identical, pixels, independent, patches, tile`
- Narration: With no padding, the same coordinate always yields identical pixels, so independent patches tile seamlessly at constant memory. Training combines adversarial, R1, path-length, diversity, and vertical-coordinate regression losses.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_padding_same_coordinate_always_yield" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords padding, same, coordinate, always, yields, identical in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_authors_introduce_flickr_landscape_f`

- Preferred role: `content`
- Cue keywords: `authors, introduce, flickr-landscape, four, hundred, fifty, thousand, high-quality, landscape, images`
- Narration: The authors introduce Flickr-Landscape, four hundred fifty thousand high-quality landscape images crawled from Flickr, to evaluate synthesis at extended sizes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_authors_introduce_flickr_landscape_f" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, introduce, flickr-landscape, four, hundred, fifty in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_outpainting_they_scenery_subsets_pla`

- Preferred role: `content`
- Cue keywords: `outpainting, they, scenery, subsets, places365, sixty-two, thousand, five, hundred, images`
- Narration: For outpainting they use scenery subsets of Places365, sixty-two thousand five hundred images, and Flickr-Scenery, about fifty-four thousand.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_outpainting_they_scenery_subsets_pla" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords outpainting, they, scenery, subsets, places365, sixty-two in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_remarkably_every_infinitygan_trains`

- Preferred role: `method`
- Cue keywords: `remarkably, every, infinitygan, trains, tiny, one-hundred-one-pixel, patches, both, any-size, inference`
- Narration: Remarkably, every InfinityGAN model trains on tiny one-hundred-one-pixel patches, and both training and any-size inference run on a single GTX TITAN X GPU.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_remarkably_every_infinitygan_trains" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords remarkably, every, infinitygan, trains, tiny, one-hundred-one-pixel in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_flickr_landscape_benchmark_infinityg`

- Preferred role: `method`
- Cue keywords: `flickr-landscape, benchmark, infinitygan, holds, steady, quality, slope, output, grows, while`
- Narration: On the Flickr-Landscape benchmark, InfinityGAN holds a steady quality slope as output grows, while baselines drift far from realistic structure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_flickr_landscape_benchmark_infinityg" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords flickr-landscape, benchmark, infinitygan, holds, steady, quality in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_beyond_four_times_extension_beats_st`

- Preferred role: `method`
- Cue keywords: `beyond, four-times, extension, beats, strongest, baseline, scoring, scale-invariant, fid, sixty-one`
- Narration: Beyond four-times extension it beats the strongest baseline, scoring a scale-invariant FID of sixty-one point four at four-times versus seventy-nine point eight for StyleGAN2, and one twenty-one versus one eighty-nine at eight-times.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_beyond_four_times_extension_beats_st" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beyond, four-times, extension, beats, strongest, baseline in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_its_memory_stays_constant_while`

- Preferred role: `content`
- Cue keywords: `its, memory, stays, constant, while, stylegan2, runs, out, memory, sixteen-times`
- Narration: Its memory stays constant, while StyleGAN2 runs out of memory at sixteen-times.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_its_memory_stays_constant_while" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, memory, stays, constant, while, stylegan2 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_over_ninety_percent_preferred_over`

- Preferred role: `method`
- Cue keywords: `over, ninety, percent, preferred, over, every, method`
- Narration: And over ninety percent preferred it over every method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_over_ninety_percent_preferred_over" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords over, ninety, percent, preferred, over, every in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_central_ablation_isolates_where_posi`

- Preferred role: `content`
- Cue keywords: `central, ablation, isolates, where, positional, information, comes`
- Narration: The central ablation isolates where positional information comes from.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_central_ablation_isolates_where_posi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords central, ablation, isolates, where, positional, information in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_starting_stylegan2_non_constant_inpu`

- Preferred role: `method`
- Cue keywords: `starting, stylegan2, non-constant, input, authors, strip, out, all, zero-padding, creating`
- Narration: Starting from StyleGAN2 with non-constant input, the authors strip out all zero-padding, creating a padding-free variant with no positional cues.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_starting_stylegan2_non_constant_inpu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords starting, stylegan2, non-constant, input, authors, strip in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_fails_generate_reasonable_structure`

- Preferred role: `method`
- Cue keywords: `fails, generate, reasonable, structure, degrades, sharply, across, every, fid, setting`
- Narration: It fails to generate reasonable structure and degrades sharply across every FID setting, confirming the original generator leaned entirely on padding for position.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_fails_generate_reasonable_structure" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fails, generate, reasonable, structure, degrades, sharply in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_add_structure_synthesizer_back_posit`

- Preferred role: `method`
- Cue keywords: `add, structure, synthesizer, back, position, now, supplied, through, coordinate-driven, structural`
- Narration: Add the structure synthesizer back, and position is now supplied through the coordinate-driven structural latent, so quality returns, validating the design.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_add_structure_synthesizer_back_posit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords add, structure, synthesizer, back, position, now in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_numbers_scale_invariant_fid`

- Preferred role: `method`
- Cue keywords: `headline, numbers, scale-invariant, fid, sixty-one, four-times, one, twenty-one, eight-times, both`
- Narration: The headline numbers: scale-invariant FID of sixty-one at four-times and one twenty-one at eight-times, both beating the strongest baseline.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_headline_numbers_scale_invariant_fid" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, numbers, scale-invariant, fid, sixty-one, four-times in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_over_ninety_percent_human_preference`

- Preferred role: `content`
- Cue keywords: `over, ninety, percent, human, preference`
- Narration: Over ninety percent human preference.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_over_ninety_percent_human_preference" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords over, ninety, percent, human, preference in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_seven_point_two_times_faster`

- Preferred role: `content`
- Cue keywords: `seven, point, two, times, faster, inference, through, parallel, batching, cutting`
- Narration: Up to seven point two times faster inference through parallel batching, cutting eight-thousand-pixel synthesis from one hundred thirty-seven seconds to nineteen.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_seven_point_two_times_faster" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords seven, point, two, times, faster, inference in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_paired_in_and_out_outpainting_fid_dr`

- Preferred role: `content`
- Cue keywords: `paired, in-and-out, outpainting, fid, drops, nine, places365, fifteen, flickr-scenery, halving`
- Narration: Paired with In-and-Out for outpainting, FID drops to nine on Places365 and fifteen on Flickr-Scenery, halving previous best.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_paired_in_and_out_outpainting_fid_dr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords paired, in-and-out, outpainting, fid, drops, nine in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_infinite_pixel_synthesis_be`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, infinite-pixel, synthesis, becomes, tractable, once, you, stop, tying, generation`
- Narration: The takeaway: infinite-pixel synthesis becomes tractable once you stop tying generation to a fixed resolution.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_infinite_pixel_synthesis_be" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, infinite-pixel, synthesis, becomes, tractable, once in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_separating_global_appearance_local_s`

- Preferred role: `method`
- Cue keywords: `separating, global, appearance, local, structure, via, coordinate-driven, implicit, function, texture`
- Narration: By separating global appearance, local structure via a coordinate-driven implicit function, and texture via a padding-free generator, InfinityGAN produces patches that are independent yet perfectly consistent, tiling into images of any size at constant memory and generated in parallel.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_separating_global_appearance_local_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separating, global, appearance, local, structure, via in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_same_framework_unlocks_spatial_style`

- Preferred role: `guidance`
- Cue keywords: `same, framework, unlocks, spatial, style, fusion, multi-modal, outpainting, arbitrary-length, panoramas`
- Narration: The same framework unlocks spatial style fusion, multi-modal outpainting, and arbitrary-length panoramas, all from tiny patches.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s10_c3_same_framework_unlocks_spatial_style" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords same, framework, unlocks, spatial, style, fusion in title/desc so the matcher can verify semantic overlap.
