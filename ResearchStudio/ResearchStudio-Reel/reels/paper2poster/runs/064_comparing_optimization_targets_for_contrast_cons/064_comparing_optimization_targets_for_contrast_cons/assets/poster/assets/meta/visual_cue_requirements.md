# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_contrast_consistent_search_ccs_unsup`

- Preferred role: `content`
- Cue keywords: `contrast-consistent, search, ccs, unsupervised, probe, reads, language, sense, truth, its`
- Narration: Contrast-Consistent Search, or CCS, is an unsupervised probe that reads a language model's sense of truth from its activations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_contrast_consistent_search_ccs_unsup" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contrast-consistent, search, ccs, unsupervised, probe, reads in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_but_what_does_ccs_actually`

- Preferred role: `content`
- Cue keywords: `but, what, does, ccs, actually, optimize`
- Narration: But what does CCS actually optimize?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_but_what_does_ccs_actually" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, what, does, ccs, actually, optimize in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_explains_its_target_derives_new`

- Preferred role: `figure`
- Cue keywords: `explains, its, target, derives, new, loss, midpoint-displacement, matches, ccs, beat`
- Narration: This paper explains its target and derives a new loss, Midpoint-Displacement, that matches CCS and can beat it.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c3_explains_its_target_derives_new" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords explains, its, target, derives, new, loss in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_ccs_recovers_direction_activations_e`

- Preferred role: `method`
- Cue keywords: `ccs, recovers, direction, activations, encoding, whether, statement, true, false, labels`
- Narration: CCS recovers a direction in a model's activations encoding whether a statement is true or false, using no labels, only the constraint that a statement and its negation disagree.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_ccs_recovers_direction_activations_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ccs, recovers, direction, activations, encoding, whether in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_yet_nobody_had_pinned_down`

- Preferred role: `figure`
- Cue keywords: `yet, nobody, had, pinned, down, what, its, loss, really, optimizes`
- Narration: Yet nobody had pinned down what its loss really optimizes, or whether that target is best.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c2_yet_nobody_had_pinned_down" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yet, nobody, had, pinned, down, what in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_safely_deploying_capable_models_mean`

- Preferred role: `content`
- Cue keywords: `safely, deploying, capable, models, means, catching, confident, falsehoods, probes, read`
- Narration: Safely deploying capable models means catching confident falsehoods, and probes that read a model's own truth representation could help, but only if we understand them.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_safely_deploying_capable_models_mean" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords safely, deploying, capable, models, means, catching in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_ccs_explained_through_clustering_act`

- Preferred role: `content`
- Cue keywords: `ccs, explained, through, clustering, activations, learning, probabilities`
- Narration: CCS was explained through clustering activations and learning probabilities.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_ccs_explained_through_clustering_act" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ccs, explained, through, clustering, activations, learning in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_authors_argue_both_pictures_mislead`

- Preferred role: `content`
- Cue keywords: `authors, argue, both, pictures, mislead, motivating, cleaner, account, its, target`
- Narration: The authors argue both pictures mislead, motivating a cleaner account of its target.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_authors_argue_both_pictures_mislead" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, both, pictures, mislead, motivating in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_corrects_two_misconceptions_cc`

- Preferred role: `content`
- Cue keywords: `first, corrects, two, misconceptions, ccs, classifies, only, displacement, between, statement`
- Narration: First, it corrects two misconceptions: CCS classifies using only the displacement between a statement and its negation, needing no separating hyperplane, and succeeds even when probabilities cluster near one half.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_corrects_two_misconceptions_cc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, corrects, two, misconceptions, ccs, classifies in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_derives_new_midpoint_displace`

- Preferred role: `figure`
- Cue keywords: `second, derives, new, midpoint-displacement, loss`
- Narration: Second, it derives a new Midpoint-Displacement loss.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c3_second_derives_new_midpoint_displace" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, derives, new, midpoint-displacement, loss in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_comparison_shows_proxies_beat`

- Preferred role: `content`
- Cue keywords: `third, comparison, shows, proxies, beat, ccs`
- Narration: Third, a comparison shows it proxies, and can beat, CCS.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_third_comparison_shows_proxies_beat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, comparison, shows, proxies, beat, ccs in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_ccs_described_two_statistics_along`

- Preferred role: `content`
- Cue keywords: `ccs, described, two, statistics, along, probe, direction, sigma-d-squared, how, far`
- Narration: CCS is described by two statistics along the probe direction: sigma-d-squared, how far a statement and its negation are pushed apart, and sigma-m-squared, how far their midpoint sits from origin.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_ccs_described_two_statistics_along" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ccs, described, two, statistics, along, probe in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_its_saturating_sigmoid_forces_trade`

- Preferred role: `content`
- Cue keywords: `its, saturating, sigmoid, forces, trade-off, between, two`
- Narration: Its saturating sigmoid forces a trade-off between the two.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_its_saturating_sigmoid_forces_trade" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, saturating, sigmoid, forces, trade-off, between in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_midpoint_displacement_makes_explicit`

- Preferred role: `result`
- Cue keywords: `midpoint-displacement, makes, explicit, one, knob, lambda, reproducing, ccs, maximizing, accuracy`
- Narration: Midpoint-Displacement makes this explicit with one knob, lambda, reproducing CCS or maximizing accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_midpoint_displacement_makes_explicit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords midpoint-displacement, makes, explicit, one, knob, lambda in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_hidden_state_activations`

- Preferred role: `method`
- Cue keywords: `experiments, hidden-state, activations, four, models, encoder, decoder, unifiedqa, t5-large, deberta`
- Narration: Experiments use hidden-state activations from four models: the encoder and decoder of UnifiedQA T5-Large, DeBERTa, and GPT-Neo, averaged over five datasets including BoolQ.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_experiments_hidden_state_activations" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, hidden-state, activations, four, models, encoder in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_contrast_pairs_append_two_exclusive`

- Preferred role: `title`
- Cue keywords: `contrast, pairs, append, two, exclusive, answers, set, normalized, independently, probe`
- Narration: Contrast pairs append two exclusive answers, each set normalized independently so the probe cannot detect the answer token.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c2_contrast_pairs_append_two_exclusive" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contrast, pairs, append, two, exclusive, answers in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_midpoint_displacement_tuned`

- Preferred role: `content`
- Cue keywords: `headline, midpoint-displacement, tuned, imitate, ccs, gives, probe, directions, averaging, cosine`
- Narration: The headline: Midpoint-Displacement tuned to imitate CCS gives probe directions averaging cosine similarity about zero point six three to real CCS probes, while CCS agrees with itself only at zero point seven eight.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_headline_midpoint_displacement_tuned" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, midpoint-displacement, tuned, imitate, ccs, gives in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_other_accurate_losses_like_pca`

- Preferred role: `figure`
- Cue keywords: `other, accurate, losses, like, pca, sit, near, zero, point, one`
- Narration: Other accurate losses like PCA sit near zero point one five, so the resemblance is specific to Midpoint-Displacement.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s07_c2_other_accurate_losses_like_pca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords other, accurate, losses, like, pca, sit in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_two_midpoint_displacement_variants_d`

- Preferred role: `content`
- Cue keywords: `two, midpoint-displacement, variants, differ, only, lambda`
- Narration: The two Midpoint-Displacement variants differ only in lambda.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_two_midpoint_displacement_variants_d" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, midpoint-displacement, variants, differ, only, lambda in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_tuned_mimic_ccs_cosine_similarity`

- Preferred role: `result`
- Cue keywords: `tuned, mimic, ccs, cosine, similarity, about, zero, point, six, three`
- Narration: Tuned to mimic CCS, cosine similarity is about zero point six three; tuned for accuracy, it drops to zero point three eight, showing the displacement-versus-midpoint trade-off defines CCS's target.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_tuned_mimic_ccs_cosine_similarity" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tuned, mimic, ccs, cosine, similarity, about in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_retuning_lambda_raises_test_accuracy`

- Preferred role: `result`
- Cue keywords: `retuning, lambda, raises, test, accuracy, zero, point, seven, six`
- Narration: Retuning lambda raises test accuracy to zero point seven six.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_retuning_lambda_raises_test_accuracy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords retuning, lambda, raises, test, accuracy, zero in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_midpoint_displacement_ma`

- Preferred role: `result`
- Cue keywords: `few, numbers, midpoint-displacement, matched, ccs, reaches, average, cosine, similarity, about`
- Narration: A few numbers: Midpoint-Displacement matched to CCS reaches average cosine similarity about zero point six three, versus CCS self-similarity zero point seven eight, while competing losses reach only zero point one five.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_few_numbers_midpoint_displacement_ma" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, midpoint-displacement, matched, ccs, reaches in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_accuracy_tuned_variant_averages_zero`

- Preferred role: `result`
- Cue keywords: `accuracy-tuned, variant, averages, zero, point, seven, six, accuracy, versus, zero`
- Narration: The accuracy-tuned variant averages zero point seven six accuracy versus zero point seven one, winning on three of four models, across five datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_accuracy_tuned_variant_averages_zero" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords accuracy-tuned, variant, averages, zero, point, seven in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_take_home_ccs_succeeds_because_displ`

- Preferred role: `figure`
- Cue keywords: `take-home, ccs, succeeds, because, displacement, information, its, contrast-pair, not, its`
- Narration: The take-home: CCS succeeds because of the displacement information in its contrast-pair data, not its specific loss formula.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c1_take_home_ccs_succeeds_because_displ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords take-home, ccs, succeeds, because, displacement, information in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_simple_midpoint_displacement_loss_re`

- Preferred role: `figure`
- Cue keywords: `simple, midpoint-displacement, loss, reproduces, ccs, retuned, beats`
- Narration: A simple Midpoint-Displacement loss reproduces CCS and, retuned, beats it.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c2_simple_midpoint_displacement_loss_re" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords simple, midpoint-displacement, loss, reproduces, ccs, retuned in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_exact_loss_interchangeable_real_leve`

- Preferred role: `figure`
- Cue keywords: `exact, loss, interchangeable, real, lever, displacement-versus-midpoint, trade-off`
- Narration: The exact loss is interchangeable; the real lever is the displacement-versus-midpoint trade-off.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c3_exact_loss_interchangeable_real_leve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords exact, loss, interchangeable, real, lever, displacement-versus-midpoint in title/desc so the matcher can verify semantic overlap.
