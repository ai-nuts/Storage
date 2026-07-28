# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_mixture_models_usually_blend_simple`

- Preferred role: `method`
- Cue keywords: `mixture, models, usually, blend, simple, distributions, adding, them`
- Narration: Mixture models usually blend simple distributions by adding them.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_mixture_models_usually_blend_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mixture, models, usually, blend, simple, distributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_but_what_mixture_could_also`

- Preferred role: `content`
- Cue keywords: `but, what, mixture, could, also, subtract, probability, mass`
- Narration: But what if a mixture could also subtract probability mass?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_but_what_mixture_could_also" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, what, mixture, could, also, subtract in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_published_iclr_2024_shows_how`

- Preferred role: `content`
- Cue keywords: `published, iclr, 2024, shows, how, learn, deep, subtractive, mixtures, squaring`
- Narration: Published at ICLR 2024, this paper shows how to learn deep subtractive mixtures by squaring them.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_published_iclr_2024_shows_how" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords published, iclr, 2024, shows, how, learn in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_squaring_keeps_valid_distribution_wh`

- Preferred role: `method`
- Cue keywords: `squaring, keeps, valid, distribution, while, allowing, negative, parameters, authors, prove`
- Narration: Squaring keeps the model a valid distribution while allowing negative parameters, and the authors prove these squared non-monotonic circuits can be exponentially more compact than ordinary additive mixtures, then confirm the gain on real-world density estimation and language-model distillation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_squaring_keeps_valid_distribution_wh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords squaring, keeps, valid, distribution, while, allowing in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_traditional_mixture_models_build_com`

- Preferred role: `method`
- Cue keywords: `traditional, mixture, models, build, complex, distributions, blending, simple, ones, additively`
- Narration: Traditional mixture models build complex distributions by blending simple ones additively. That works, but it can be wildly inefficient.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_traditional_mixture_models_build_com" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords traditional, mixture, models, build, complex, distributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_target_distribution_gaps_holes_its`

- Preferred role: `method`
- Cue keywords: `target, distribution, gaps, holes, its, domain, additive, mixture, must, stack`
- Narration: If the target distribution has gaps or holes in its domain, an additive mixture must stack up many components just to carve those holes out.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_target_distribution_gaps_holes_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords target, distribution, gaps, holes, its, domain in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_natural_fix_let_some_components`

- Preferred role: `content`
- Cue keywords: `natural, fix, let, some, components, subtract, probability, mass, instead, only`
- Narration: The natural fix is to let some components subtract probability mass instead of only adding it.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_natural_fix_let_some_components" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords natural, fix, let, some, components, subtract in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_catch_once_you_allow_subtraction`

- Preferred role: `method`
- Cue keywords: `catch, once, you, allow, subtraction, dip, below, zero, stop, being`
- Narration: The catch: once you allow subtraction, the model can dip below zero and stop being a valid distribution, and learning it becomes genuinely hard.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_catch_once_you_allow_subtraction" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords catch, once, you, allow, subtraction, dip in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_revisit_now_because_subtraction`

- Preferred role: `content`
- Cue keywords: `why, revisit, now, because, subtraction, pays, off, mixture, cancel, mass`
- Narration: So why revisit this now? Because subtraction pays off: a mixture that can cancel mass captures complex shapes with far fewer components.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_why_revisit_now_because_subtraction" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, revisit, now, because, subtraction, pays in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_problem_guaranteeing_result_stays_no`

- Preferred role: `result`
- Cue keywords: `problem, guaranteeing, result, stays, non-negative`
- Narration: The problem is guaranteeing the result stays non-negative.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_problem_guaranteeing_result_stays_no" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords problem, guaranteeing, result, stays, non-negative in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_energy_based_models_enforce_non_nega`

- Preferred role: `content`
- Cue keywords: `energy-based, models, enforce, non-negativity, exponentiation, but, lose, tractable, normalization`
- Narration: Energy-based models enforce non-negativity by exponentiation, but then lose tractable normalization.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_energy_based_models_enforce_non_nega" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords energy-based, models, enforce, non-negativity, exponentiation, but in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_meanwhile_several_separate_communiti`

- Preferred role: `method`
- Cue keywords: `meanwhile, several, separate, communities, signal, processing, kernel, methods, quantum, mechanics`
- Narration: Meanwhile several separate communities, from signal processing to kernel methods to quantum mechanics, each rediscovered a squaring trick to enforce non-negativity, but without a common, tractable framework tying them together.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_meanwhile_several_separate_communiti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords meanwhile, several, separate, communities, signal, processing in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_work_makes_four_contributions_first`

- Preferred role: `guidance`
- Cue keywords: `work, makes, four, contributions, first, general, framework, representing, subtractive, mixtures`
- Narration: This work makes four contributions. First, a general framework for representing subtractive mixtures by squaring, expressed in the language of tensorized probabilistic circuits.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c1_work_makes_four_contributions_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, makes, four, contributions, first, general in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_shows_these_squared_non_monot`

- Preferred role: `content`
- Cue keywords: `second, shows, these, squared, non-monotonic, circuits, generalize, several, apparently, different`
- Narration: Second, it shows these squared non-monotonic circuits generalize several apparently different models with negative parameters, including square-root-of-density models, positive semi-definite kernel models, and Born machines from quantum physics.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_second_shows_these_squared_non_monot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, shows, these, squared, non-monotonic, circuits in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_proves_exponential_lower_bound`

- Preferred role: `content`
- Cue keywords: `third, proves, exponential, lower, bound, functions, single, squared, circuit, encodes`
- Narration: Third, it proves an exponential lower bound: functions a single squared circuit encodes compactly need exponentially more units in any monotonic circuit.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_third_proves_exponential_lower_bound" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, proves, exponential, lower, bound, functions in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_fourth_backs_experiments_real_world`

- Preferred role: `content`
- Cue keywords: `fourth, backs, experiments, real-world`
- Narration: And fourth, it backs this with experiments on real-world data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_fourth_backs_experiments_real_world" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, backs, experiments, real-world in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_core_idea_take_mixture_unconstrained`

- Preferred role: `method`
- Cue keywords: `core, idea, take, mixture, unconstrained, real, weights, components, negative, coefficients`
- Narration: Here is the core idea. Take a mixture with unconstrained real weights, so components can have negative coefficients, and simply square the whole thing. Squaring forces the output to be non-negative no matter what the weights are.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_core_idea_take_mixture_unconstrained" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, idea, take, mixture, unconstrained, real in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_expanding_square_turns_k_component_m`

- Preferred role: `content`
- Cue keywords: `expanding, square, turns, k-component, mixture, sum, over, all, pairs, components`
- Narration: Expanding the square turns a K-component mixture into a sum over all pairs of components, a product-of-experts form whose partition function can still be computed in closed form for many families.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_expanding_square_turns_k_component_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords expanding, square, turns, k-component, mixture, sum in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_deep_authors_square_tensorized_struc`

- Preferred role: `method`
- Cue keywords: `deep, authors, square, tensorized, structured-decomposable, circuit, layer, layer`
- Narration: To go deep, the authors square a tensorized structured-decomposable circuit layer by layer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_deep_authors_square_tensorized_struc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, authors, square, tensorized, structured-decomposable, circuit in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_squared_layer_holds_quadratic_number`

- Preferred role: `content`
- Cue keywords: `squared, layer, holds, quadratic, number, units, but, still, outputs, vector`
- Narration: Each squared layer holds a quadratic number of units but still outputs a vector, so the whole model trains efficiently with gradient descent, computing the normalizer just once per batch.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_squared_layer_holds_quadratic_number" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords squared, layer, holds, quadratic, number, units in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_cover_three_regimes`

- Preferred role: `content`
- Cue keywords: `experiments, cover, three, regimes`
- Narration: The experiments cover three regimes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_cover_three_regimes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, cover, three, regimes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_first_two_dimensional_synthetic_dens`

- Preferred role: `content`
- Cue keywords: `first, two-dimensional, synthetic, densities, both, continuous, discrete, where, you, literally`
- Narration: First, two-dimensional synthetic densities, both continuous and discrete, where you can literally see how well each model captures rings and other holey shapes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_first_two_dimensional_synthetic_dens" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, two-dimensional, synthetic, densities, both, continuous in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_second_five_standard_uci_datasets`

- Preferred role: `content`
- Cue keywords: `second, five, standard, uci, datasets, power, gas, hepmass, miniboone, bsds300`
- Narration: Second, five standard UCI datasets: Power, Gas, Hepmass, MiniBooNE, and BSDS300. And third, distilling sentences sampled from the GPT2 language model.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_second_five_standard_uci_datasets" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, five, standard, uci, datasets, power in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_baselines_span_full_covariance_gauss`

- Preferred role: `content`
- Cue keywords: `baselines, span, full-covariance, gaussians, normalizing, flows, like, realnvp, made, maf`
- Narration: Baselines span full-covariance Gaussians, normalizing flows like RealNVP, MADE, MAF and NSF, monotonic probabilistic circuits, and tensor-train density estimators.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_baselines_span_full_covariance_gauss" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords baselines, span, full-covariance, gaussians, normalizing, flows in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_consistent_same_siz`

- Preferred role: `title`
- Cue keywords: `headline, finding, consistent, same, size, squared, non-monotonic, circuits, reach, higher`
- Narration: The headline finding is consistent: at the same model size, squared non-monotonic circuits reach higher log-likelihoods than monotonic circuits across the density-estimation tasks.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s07_c1_headline_finding_consistent_same_siz" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, consistent, same, size, squared in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_two_dimensional_ring_distributions_p`

- Preferred role: `method`
- Cue keywords: `two-dimensional, ring, distributions, plain, squaring, already, helps, but, negative, parameters`
- Narration: On the two-dimensional ring distributions, plain squaring already helps, but it is the negative parameters that let the model actually carve out the holes in the density.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_two_dimensional_ring_distributions_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two-dimensional, ring, distributions, plain, squaring, already in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_gpt2_distillation_task_squared_circu`

- Preferred role: `content`
- Cue keywords: `gpt2, distillation, task, squared, circuits, scale, better, get, closer, gpt2`
- Narration: And on the GPT2 distillation task, the squared circuits scale better and get closer to GPT2's own likelihood, approximating the intractable model more faithfully than monotonic circuits do.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_gpt2_distillation_task_squared_circu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gpt2, distillation, task, squared, circuits, scale in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_confirm_gains_come_subtraction_not`

- Preferred role: `result`
- Cue keywords: `confirm, gains, come, subtraction, not, just, squaring, authors, compare, against`
- Narration: To confirm the gains come from subtraction and not just squaring, the authors compare against squared monotonic circuits, which square but keep all parameters non-negative.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_confirm_gains_come_subtraction_not" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords confirm, gains, come, subtraction, not, just in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_squared_non_monotonic_circuits_still`

- Preferred role: `content`
- Cue keywords: `squared, non-monotonic, circuits, still, win, negative, parameters, doing, real, work`
- Narration: The squared non-monotonic circuits still win, so the negative parameters are doing the real work.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_squared_non_monotonic_circuits_still" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords squared, non-monotonic, circuits, still, win, negative in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_two_other_patterns_emerge_binary_tre`

- Preferred role: `content`
- Cue keywords: `two, other, patterns, emerge, binary-tree, region, graphs, generally, beat, linear-tree`
- Narration: Two other patterns emerge: binary-tree region graphs generally beat linear-tree ones, and the input layer matters, with splines helping most on continuous data and embeddings on discrete data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_two_other_patterns_emerge_binary_tre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, other, patterns, emerge, binary-tree, region in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_some_discrete_image_mass_tasks_advan`

- Preferred role: `title`
- Cue keywords: `some, discrete, image-mass, tasks, advantage, narrows`
- Narration: On some discrete image-mass tasks the advantage narrows.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s08_c4_some_discrete_image_mass_tasks_advan" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords some, discrete, image-mass, tasks, advantage, narrows in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_make_point`

- Preferred role: `content`
- Cue keywords: `few, numbers, make, point`
- Narration: A few numbers make the point.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_make_point" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, make, point in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_squaring_mixture_components_encodes`

- Preferred role: `content`
- Cue keywords: `squaring, mixture, components, encodes, order, k-squared-over-two, pairwise, components, while, reusing`
- Narration: Squaring a mixture with K components encodes on the order of K-squared-over-two pairwise components while reusing the same K parameters, which is where the compactness comes from, and the paper proves this gap over monotonic circuits is exponential.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_squaring_mixture_components_encodes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords squaring, mixture, components, encodes, order, k-squared-over-two in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_empirically_squared_non_monotonic_ci`

- Preferred role: `content`
- Cue keywords: `empirically, squared, non-monotonic, circuits, post, best, test, log-likelihoods, among, tractable`
- Narration: Empirically, the squared non-monotonic circuits post the best test log-likelihoods among tractable models on several UCI datasets, for example zero point six two on Power, about eleven on Gas, minus twenty point four on Hepmass, and minus twenty-six point seven on MiniBooNE.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_empirically_squared_non_monotonic_ci" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords empirically, squared, non-monotonic, circuits, post, best in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_language_they_climb_toward_gpt2`

- Preferred role: `content`
- Cue keywords: `language, they, climb, toward, gpt2, own, likelihood, around, minus, fifty-two`
- Narration: On the language data they climb toward GPT2's own likelihood of around minus fifty-two, while monotonic circuits flatten out.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_language_they_climb_toward_gpt2" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords language, they, climb, toward, gpt2, own in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_squaring_turns_subtractive_mixtures`

- Preferred role: `content`
- Cue keywords: `squaring, turns, subtractive, mixtures, valid, tractable, probabilistic, models, need, exponentially`
- Narration: Squaring turns subtractive mixtures into valid, tractable probabilistic models that need exponentially fewer components than additive mixtures for the same expressiveness.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_squaring_turns_subtractive_mixtures" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords squaring, turns, subtractive, mixtures, valid, tractable in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_along_way_one_framework_unifies`

- Preferred role: `guidance`
- Cue keywords: `along, way, one, framework, unifies, square-root-of-density, models, positive, semi-definite, kernel`
- Narration: Along the way, this one framework unifies square-root-of-density models, positive semi-definite kernel models, and quantum Born machines under a single property-driven view of circuits, making subtraction a practical, first-class tool for compact and expressive probabilistic modeling.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s10_c3_along_way_one_framework_unifies" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords along, way, one, framework, unifies, square-root-of-density in title/desc so the matcher can verify semantic overlap.
