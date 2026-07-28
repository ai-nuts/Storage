# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_deep_generative_models_grow_more`

- Preferred role: `method`
- Cue keywords: `deep, generative, models, grow, more, capable, they, increasingly, memorize, reproduce`
- Narration: As deep generative models grow more capable, they increasingly memorize and reproduce their training data, raising serious privacy and copyright concerns.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_deep_generative_models_grow_more" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, generative, models, grow, more, capable in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_layer_6_published_iclr_2025`

- Preferred role: `guidance`
- Cue keywords: `layer, 6, published, iclr, 2025, proposes, manifold, memorization, hypothesis, geometric`
- Narration: This paper, from Layer 6 AI and published at ICLR 2025, proposes the manifold memorization hypothesis: a geometric framework that reasons about memorization through the local intrinsic dimension of the data and model manifolds.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s01_c2_layer_6_published_iclr_2025" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords layer, 6, published, iclr, 2025, proposes in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_provides_formal_standard_how_memoriz`

- Preferred role: `content`
- Cue keywords: `provides, formal, standard, how, memorized, datapoint, cleanly, separates, memorization, caused`
- Narration: It provides a formal standard for how memorized a datapoint is, cleanly separates memorization caused by overfitting from memorization caused by the data itself, and yields scalable tools to detect and mitigate memorization all the way up to Stable Diffusion.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_provides_formal_standard_how_memoriz" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords provides, formal, standard, how, memorized, datapoint in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_generative_models_diffusion_models_p`

- Preferred role: `method`
- Cue keywords: `generative, models, diffusion, models, particular, increasingly, deployed, public-facing, applications, but`
- Narration: Generative models, and diffusion models in particular, are increasingly deployed in public-facing applications, but with enough capacity they memorize training data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_generative_models_diffusion_models_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords generative, models, diffusion, models, particular, increasingly in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_memorization_expose_private_informat`

- Preferred role: `content`
- Cue keywords: `memorization, expose, private, information, reproduce, copyrighted, works, exposing, builders, legal`
- Narration: That memorization can expose private information and reproduce copyrighted works, exposing model builders to legal liability.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_memorization_expose_private_informat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords memorization, expose, private, information, reproduce, copyrighted in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_trouble_community_lacked_single_form`

- Preferred role: `guidance`
- Cue keywords: `trouble, community, lacked, single, formal, framework, say, precisely, how, memorized`
- Narration: The trouble is that the community has lacked a single formal framework to say precisely how memorized a datapoint is.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s02_c3_trouble_community_lacked_single_form" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trouble, community, lacked, single, formal, framework in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_past_definitions_lean_distance_neare`

- Preferred role: `method`
- Cue keywords: `past, definitions, lean, distance, nearest, image, pixel, space, which, fails`
- Narration: Past definitions lean on distance to a nearest training image in pixel space, which fails to capture subtler forms of memorization and cannot be computed at the scale of models like Stable Diffusion.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_past_definitions_lean_distance_neare" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords past, definitions, lean, distance, nearest, image in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_manifold_hypothesis_says_realistic_l`

- Preferred role: `content`
- Cue keywords: `manifold, hypothesis, says, realistic, lives, low-dimensional, manifold, embedded, high-dimensional, space`
- Narration: The manifold hypothesis says realistic data lives on a low-dimensional manifold embedded in a high-dimensional space.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_manifold_hypothesis_says_realistic_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords manifold, hypothesis, says, realistic, lives, low-dimensional in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_authors_argue_geometry_exactly_right`

- Preferred role: `content`
- Cue keywords: `authors, argue, geometry, exactly, right, lens, memorization`
- Narration: The authors argue that this geometry is exactly the right lens for memorization.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_authors_argue_geometry_exactly_right" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, geometry, exactly, right, lens in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_purely_probabilistic_frameworks_dema`

- Preferred role: `method`
- Cue keywords: `purely, probabilistic, frameworks, demand, whole, dataset, enormous, sample, counts, which`
- Narration: Purely probabilistic frameworks demand the whole training dataset and enormous sample counts, which is hopeless at LAION scale.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_purely_probabilistic_frameworks_dema" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords purely, probabilistic, frameworks, demand, whole, dataset in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_geometric_framing_contrast_connects`

- Preferred role: `content`
- Cue keywords: `geometric, framing, contrast, connects, memorization, quantity, local, intrinsic, dimension, which`
- Narration: A geometric framing, by contrast, connects memorization to a quantity — local intrinsic dimension — for which practical estimators already exist, even for large diffusion models.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_geometric_framing_contrast_connects" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords geometric, framing, contrast, connects, memorization, quantity in title/desc so the matcher can verify semantic overlap.

## Slide 04: method

Heading: Method

### Cue 1: `cue_s04_c1_central_quantity_local_intrinsic_dim`

- Preferred role: `method`
- Cue keywords: `central, quantity, local, intrinsic, dimension, number, degrees, freedom, datapoint, its`
- Narration: The central quantity is local intrinsic dimension, the number of degrees of freedom a datapoint has on its manifold. A perfectly reproduced training image sits on a zero-dimensional manifold — a point mass. The manifold memorization hypothesis compares the model's local dimension to the ground truth's.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_central_quantity_local_intrinsic_dim" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords central, quantity, local, intrinsic, dimension, number in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_when_manifold_too_constrained_relati`

- Preferred role: `method`
- Cue keywords: `when, manifold, too, constrained, relative, truth, overfitting-driven, memorization, genuine, modelling`
- Narration: When the model's manifold is too constrained relative to the truth, that is overfitting-driven memorization, a genuine modelling failure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_when_manifold_too_constrained_relati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, manifold, too, constrained, relative, truth in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_when_local_dimension_intrinsically_s`

- Preferred role: `content`
- Cue keywords: `when, local, dimension, intrinsically, small, even, correct, think, highly, specific`
- Narration: When the local dimension is intrinsically small even for a correct model — think of a highly specific prompt like the title of a famous artwork — that is data-driven memorization, which cannot be caught by comparing train and test likelihoods.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_when_local_dimension_intrinsically_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, local, dimension, intrinsically, small, even in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_because_true_lid_cannot_estimated`

- Preferred role: `guidance`
- Cue keywords: `because, true, lid, cannot, estimated, stable, diffusion, scale, authors, three`
- Narration: Because true LID cannot be estimated at Stable Diffusion scale, the authors use three practical proxies for the model's LID: an unconditional estimate from the FLIPD algorithm, a conditional estimate, and the classifier-free guidance vector norm. They also prove that conditioning on a prompt can only reduce local dimension, explaining why specific prompts drive memorization.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c4_because_true_lid_cannot_estimated" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, true, lid, cannot, estimated, stable in title/desc so the matcher can verify semantic overlap.

## Slide 05: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s05_c1_experiments_deliberately_sweep_acros`

- Preferred role: `content`
- Cue keywords: `experiments, deliberately, sweep, across, scales`
- Narration: The experiments deliberately sweep across scales.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_experiments_deliberately_sweep_acros" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, deliberately, sweep, across, scales in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_small_end_two_dimensional_synthetic`

- Preferred role: `content`
- Cue keywords: `small, end, two-dimensional, synthetic, von, mises, mixtures, let, authors, compute`
- Narration: At the small end, two-dimensional synthetic von Mises mixtures let the authors compute ground-truth local dimension exactly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_small_end_two_dimensional_synthetic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords small, end, two-dimensional, synthetic, von, mises in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_middle_stylegan2_ada_iddpm_diffusion`

- Preferred role: `result`
- Cue keywords: `middle, stylegan2-ada, iddpm, diffusion, cifar10`
- Narration: In the middle, StyleGAN2-ADA and an iDDPM diffusion model on CIFAR10.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_middle_stylegan2_ada_iddpm_diffusion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords middle, stylegan2-ada, iddpm, diffusion, cifar10 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_large_end_stable_diffusion_version`

- Preferred role: `result`
- Cue keywords: `large, end, stable, diffusion, version, 1.5, where, they, study, 86`
- Narration: At the large end, Stable Diffusion version 1.5, where they study 86 verbatim-memorized LAION images against thousands of non-memorized images drawn from LAION Aesthetics, COCO, and the Tuxemon dataset.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c4_large_end_stable_diffusion_version" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, end, stable, diffusion, version, 1.5 in title/desc so the matcher can verify semantic overlap.

## Slide 06: key-result

Heading: Key Result

### Cue 1: `cue_s06_c1_headline_empirical_finding_local_int`

- Preferred role: `content`
- Cue keywords: `headline, empirical, finding, local, intrinsic, dimension, tracks, memorization, everywhere, authors`
- Narration: The headline empirical finding is that local intrinsic dimension tracks memorization everywhere the authors look, from toy 2D data to Stable Diffusion.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_headline_empirical_finding_local_int" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, empirical, finding, local, intrinsic, dimension in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_memorized_images_reliably_get_low`

- Preferred role: `guidance`
- Cue keywords: `memorized, images, reliably, get, low, lid, estimates, high, classifier-free, guidance`
- Narration: Memorized images reliably get low LID estimates and high classifier-free guidance vector norms.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s06_c2_memorized_images_reliably_get_low" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords memorized, images, reliably, get, low, lid in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_even_more_striking_unconditional_lid`

- Preferred role: `method`
- Cue keywords: `even, more, striking, unconditional, lid, estimate, flags, memorized, images, without`
- Narration: Even more striking, the unconditional LID estimate flags memorized training images without needing their captions at all.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_even_more_striking_unconditional_lid" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords even, more, striking, unconditional, lid, estimate in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_genuinely_new_capability_because_pre`

- Preferred role: `content`
- Cue keywords: `genuinely, new, capability, because, previous, state, art, cfg, vector, norm`
- Narration: That is a genuinely new capability, because the previous state of the art, the CFG vector norm, depends on having the caption in hand.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_genuinely_new_capability_because_pre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords genuinely, new, capability, because, previous, state in title/desc so the matcher can verify semantic overlap.

## Slide 07: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s07_c1_mitigate_memorization_method_attribu`

- Preferred role: `method`
- Cue keywords: `mitigate, memorization, method, attributes, specific, prompt, tokens, rephrases, them, gpt-4`
- Narration: To mitigate memorization, the method attributes it to specific prompt tokens and rephrases them with GPT-4.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_mitigate_memorization_method_attribu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mitigate, memorization, method, attributes, specific, prompt in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_ablating_number_perturbed_tokens_sho`

- Preferred role: `content`
- Cue keywords: `ablating, number, perturbed, tokens, shows, clean, trade-off, perturbing, more, tokens`
- Narration: Ablating the number of perturbed tokens shows a clean trade-off: perturbing more tokens reduces memorization but also reduces fidelity.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_ablating_number_perturbed_tokens_sho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablating, number, perturbed, tokens, shows, clean in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_importantly_choosing_tokens_attribut`

- Preferred role: `method`
- Cue keywords: `importantly, choosing, tokens, attribution, beats, choosing, them, random, attribution-based, selection`
- Narration: Importantly, choosing tokens by attribution beats choosing them at random — attribution-based selection reaches lower training-image similarity while keeping a higher CLIP score.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_importantly_choosing_tokens_attribut" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords importantly, choosing, tokens, attribution, beats, choosing in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_new_attribution_metrics_built_score`

- Preferred role: `method`
- Cue keywords: `new, attribution, metrics, built, score, norm, flipd, work, about, well`
- Narration: New attribution metrics built on the score norm and on FLIPD work about as well as the original guidance-based metric.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_new_attribution_metrics_built_score" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords new, attribution, metrics, built, score, norm in title/desc so the matcher can verify semantic overlap.

## Slide 08: takeaway

Heading: Takeaway

### Cue 1: `cue_s08_c1_single_idea_walk_away_memorization`

- Preferred role: `content`
- Cue keywords: `single, idea, walk, away, memorization, geometric`
- Narration: The single idea to walk away with is that memorization is geometric.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_single_idea_walk_away_memorization" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single, idea, walk, away, memorization, geometric in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_local_intrinsic_dimension_around_poi`

- Preferred role: `content`
- Cue keywords: `local, intrinsic, dimension, around, point, too, small, point, memorized, holds`
- Narration: If the model's local intrinsic dimension around a point is too small, that point is memorized — and this holds whether the cause is overfitting or the data being inherently simple.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_local_intrinsic_dimension_around_poi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords local, intrinsic, dimension, around, point, too in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_because_local_intrinsic_dimension_es`

- Preferred role: `content`
- Cue keywords: `because, local, intrinsic, dimension, estimated, scale, you, both, detect, memorized`
- Narration: Because local intrinsic dimension can be estimated at scale, you can both detect memorized images, even without their captions, and mitigate memorization by steering generation toward higher-dimensional regions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_because_local_intrinsic_dimension_es" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, local, intrinsic, dimension, estimated, scale in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_manifold_memorization_hypothesis_tur`

- Preferred role: `content`
- Cue keywords: `manifold, memorization, hypothesis, turns, fuzzy, much-debated, phenomenon, measurable, geometric, quantity`
- Narration: The manifold memorization hypothesis turns a fuzzy, much-debated phenomenon into a measurable geometric quantity.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_manifold_memorization_hypothesis_tur" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords manifold, memorization, hypothesis, turns, fuzzy, much-debated in title/desc so the matcher can verify semantic overlap.
