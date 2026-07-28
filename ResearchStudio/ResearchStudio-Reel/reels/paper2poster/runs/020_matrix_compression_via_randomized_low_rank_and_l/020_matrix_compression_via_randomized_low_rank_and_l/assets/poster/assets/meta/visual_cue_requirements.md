# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_modern_matrices_hold_billions_entrie`

- Preferred role: `content`
- Cue keywords: `modern, matrices, hold, billions, entries, yet, they, often, nearly, low`
- Narration: Modern matrices can hold billions of entries, yet they're often nearly low rank.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_modern_matrices_hold_billions_entrie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords modern, matrices, hold, billions, entries, yet in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_stanford_work_introduces_lplr_random`

- Preferred role: `result`
- Cue keywords: `stanford, work, introduces, lplr, randomized, algorithm, factorizes, any, matrix, two`
- Narration: This Stanford work introduces LPLR, a randomized algorithm that factorizes any matrix into two low-rank factors, then quantizes them to low precision, compressing to one bit per coordinate while matching prior compression on images, embeddings, and LlaMa-7b weights.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c2_stanford_work_introduces_lplr_random" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stanford, work, introduces, lplr, randomized, algorithm in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_matrices_everywhere_science_machine`

- Preferred role: `method`
- Cue keywords: `matrices, everywhere, science, machine, learning, but, modern, ones, hold, billions`
- Narration: Matrices are everywhere in science and machine learning, but modern ones hold billions of elements that strain memory and compute.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_matrices_everywhere_science_machine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords matrices, everywhere, science, machine, learning, but in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_luckily_many_approximately_low_rank`

- Preferred role: `content`
- Cue keywords: `luckily, many, approximately, low, rank`
- Narration: Luckily, many are approximately low rank.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_luckily_many_approximately_low_rank" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords luckily, many, approximately, low, rank in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_prior_work_exploited_either_low_rank`

- Preferred role: `method`
- Cue keywords: `prior, work, exploited, either, low-rank, structure, low-precision, quantization, alone, combining`
- Narration: Prior work exploited either low-rank structure or low-precision quantization alone; combining both in one factorization, with provable error control, stayed open.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_prior_work_exploited_either_low_rank" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, work, exploited, either, low-rank, structure in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_matrix_low_rank_write_tall`

- Preferred role: `content`
- Cue keywords: `matrix, low, rank, write, tall, factor, times, wide, one, storing`
- Narration: If a matrix is low rank, we can write it as a tall factor times a wide one, and storing those in low precision saves more.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_matrix_low_rank_write_tall" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords matrix, low, rank, write, tall, factor in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_doing_crudely_low_bit`

- Preferred role: `result`
- Cue keywords: `but, doing, crudely, low, bit, budgets, degrades, accuracy, fast, exact`
- Narration: But doing this crudely at low bit budgets degrades accuracy fast, and the exact SVD route costs order n d squared, prohibitive at scale.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_but_doing_crudely_low_bit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, doing, crudely, low, bit, budgets in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_seeks_randomized_way_get_both`

- Preferred role: `result`
- Cue keywords: `seeks, randomized, way, get, both, factors, small, analyzable, error`
- Narration: It seeks a randomized way to get both factors with small, analyzable error.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c3_seeks_randomized_way_get_both" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords seeks, randomized, way, get, both, factors in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_core_contribution_lplr_low_precision`

- Preferred role: `method`
- Cue keywords: `core, contribution, lplr, low-precision, low-rank, factorization, randomized, algorithm, exploits, low-rank`
- Narration: The core contribution is LPLR, Low-Precision Low-Rank factorization: a randomized algorithm that exploits low-rank structure and quantizes the resulting factors.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_core_contribution_lplr_low_precision" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, contribution, lplr, low-precision, low-rank, factorization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_authors_derive_rigorous_upper_bounds`

- Preferred role: `result`
- Cue keywords: `authors, derive, rigorous, upper, bounds, approximation, error, terms, target, rank`
- Narration: The authors derive rigorous upper bounds on the approximation error in terms of target rank and bit budget, exposing a tunable compression-accuracy tradeoff.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_authors_derive_rigorous_upper_bounds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, derive, rigorous, upper, bounds, approximation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_they_add_svd_based_variant_lplr_svd`

- Preferred role: `result`
- Cue keywords: `they, add, svd-based, variant, lplr-svd, validate, images, embedding, classification, llama-7b`
- Narration: They add an SVD-based variant, LPLR-SVD, and validate on images, embedding classification, and LlaMa-7b weights.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c3_they_add_svd_based_variant_lplr_svd" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, add, svd-based, variant, lplr-svd, validate in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_lplr_runs_few_steps`

- Preferred role: `content`
- Cue keywords: `lplr, runs, few, steps`
- Narration: LPLR runs in a few steps.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_lplr_runs_few_steps" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lplr, runs, few, steps in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_draws_gaussian_sketching_matrix_form`

- Preferred role: `result`
- Cue keywords: `draws, gaussian, sketching, matrix, forms, sketch, times, randomized, rangefinder, column`
- Narration: It draws a Gaussian sketching matrix S and forms the sketch A times S, a randomized rangefinder for the column space of A, then quantizes it to get Q of A S.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c2_draws_gaussian_sketching_matrix_form" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords draws, gaussian, sketching, matrix, forms, sketch in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_next_least_squares_projects_columns`

- Preferred role: `content`
- Cue keywords: `next, least-squares-projects, columns, onto, quantized, basis, solving, projection, star, quantizes`
- Narration: Next it least-squares-projects A's columns onto this quantized basis, solving for the projection W star, then quantizes W star too, returning factors L and R.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_next_least_squares_projects_columns" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords next, least-squares-projects, columns, onto, quantized, basis in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_key_insight_gaussian_sketches_johnso`

- Preferred role: `method`
- Cue keywords: `key, insight, gaussian, sketches, johnson-lindenstrauss, embeddings, equalization, property, reconstruction, error`
- Narration: The key insight: Gaussian sketches are Johnson-Lindenstrauss embeddings with an equalization property, so reconstruction error stays order one and doesn't grow with dimension, keeping LPLR accurate even at one bit.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_key_insight_gaussian_sketches_johnso" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, insight, gaussian, sketches, johnson-lindenstrauss, embeddings in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_span_deliberately_divers`

- Preferred role: `content`
- Cue keywords: `experiments, span, deliberately, diverse, set, matrices`
- Narration: Experiments span a deliberately diverse set of matrices.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_span_deliberately_divers" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, span, deliberately, diverse, set, matrices in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_images_shepp_logan_phantom_hubble_im`

- Preferred role: `content`
- Cue keywords: `images, shepp-logan, phantom, hubble, image, jupiter, brain, scan`
- Narration: For images: the Shepp-Logan phantom, a Hubble image of Jupiter, and an MR brain scan.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_images_shepp_logan_phantom_hubble_im" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords images, shepp-logan, phantom, hubble, image, jupiter in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_embeddings_cifar_10_cifar_100_mobile`

- Preferred role: `method`
- Cue keywords: `embeddings, cifar-10, cifar-100, mobilenetv3, imdb, emotion, text, bert, scored, three-nearest-neighbor`
- Narration: For embeddings: CIFAR-10 and CIFAR-100 from MobileNetV3, and IMDB and Emotion text from BERT, scored by a three-nearest-neighbor classifier.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_embeddings_cifar_10_cifar_100_mobile" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords embeddings, cifar-10, cifar-100, mobilenetv3, imdb, emotion in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_llms_weight_matrices_llama_7b_every`

- Preferred role: `method`
- Cue keywords: `llms, weight, matrices, llama-7b, every, method, gets, same, total, bit`
- Narration: And for LLMs, the weight matrices of LlaMa-7b. Every method gets the same total bit budget, reporting relative Frobenius error.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_llms_weight_matrices_llama_7b_every" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords llms, weight, matrices, llama-7b, every, method in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_lplr_delivers_extreme_compr`

- Preferred role: `content`
- Cue keywords: `headline, lplr, delivers, extreme, compression, near, one, bit, per, coordinate`
- Narration: The headline: LPLR delivers extreme compression, near one bit per coordinate, while preserving performance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_headline_lplr_delivers_extreme_compr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, lplr, delivers, extreme, compression, near in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_cifar_10_embeddings_single_bit_retai`

- Preferred role: `result`
- Cue keywords: `cifar-10, embeddings, single, bit, retains, ninety-two, percent, accuracy, matching, unquantized`
- Narration: On CIFAR-10 embeddings at a single bit, it retains ninety-two percent accuracy, matching the unquantized ninety-one, while naive quantization collapses to eleven.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_cifar_10_embeddings_single_bit_retai" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, embeddings, single, bit, retains, ninety-two in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_cifar_100_seventy_nine_percent_versu`

- Preferred role: `result`
- Cue keywords: `cifar-100, seventy-nine, percent, versus, about, one`
- Narration: On CIFAR-100, seventy-nine percent versus about one.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_cifar_100_seventy_nine_percent_versu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-100, seventy-nine, percent, versus, about, one in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_llama_7b_weights_lplr_svd_reaches_me`

- Preferred role: `result`
- Cue keywords: `llama-7b, weights, lplr-svd, reaches, mean, relative, frobenius, error, near, zero`
- Narration: On LlaMa-7b weights, LPLR-SVD reaches mean relative Frobenius error near zero point five four, against zero point eight four for naive quant, with lower variance.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_llama_7b_weights_lplr_svd_reaches_me" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords llama-7b, weights, lplr-svd, reaches, mean, relative in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_separates_two_effects_low_rank_struc`

- Preferred role: `method`
- Cue keywords: `separates, two, effects, low-rank, structure, quantization, precision`
- Narration: The paper separates two effects: low-rank structure and quantization precision.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_separates_two_effects_low_rank_struc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separates, two, effects, low-rank, structure, quantization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_table_3_sweeps_bit_budget_triplet`

- Preferred role: `result`
- Cue keywords: `table, 3, sweeps, bit-budget, triplet, fixed, compression, showing, shifting, budget`
- Narration: Table 3 sweeps the bit-budget triplet at fixed compression, showing that shifting budget toward the non-quantized reference steadily lowers Frobenius error for LPLR and its SVD variant.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_table_3_sweeps_bit_budget_triplet" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords table, 3, sweeps, bit-budget, triplet, fixed in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_across_embedding_tables_raising_quan`

- Preferred role: `content`
- Cue keywords: `across, embedding, tables, raising, quantization, budget, one, four, bits, moves`
- Narration: Across embedding tables, raising the quantization budget from one to four bits moves LPLR from beating baselines toward parity, its edge largest where compression is extreme.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_across_embedding_tables_raising_quan" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, embedding, tables, raising, quantization, budget in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_lplr_compresses_one_bit`

- Preferred role: `content`
- Cue keywords: `numbers, lplr, compresses, one, bit, per, coordinate`
- Narration: By the numbers: LPLR compresses to one bit per coordinate.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_numbers_lplr_compresses_one_bit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, lplr, compresses, one, bit, per in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_cifar_10_one_bit_ninety_two_percent`

- Preferred role: `result`
- Cue keywords: `cifar-10, one, bit, ninety-two, percent, accuracy, versus, eleven, naive, quant`
- Narration: On CIFAR-10 at one bit, ninety-two percent accuracy versus eleven for naive quant, matching the unquantized ninety-one.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_cifar_10_one_bit_ninety_two_percent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, one, bit, ninety-two, percent, accuracy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_cifar_100_seventy_nine_versus_one_ll`

- Preferred role: `result`
- Cue keywords: `cifar-100, seventy-nine, versus, one, llama-7b, mean, frobenius, error, zero, point`
- Narration: On CIFAR-100, seventy-nine versus one. On LlaMa-7b, mean Frobenius error zero point five four for LPLR-SVD versus zero point eight four.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_cifar_100_seventy_nine_versus_one_ll" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-100, seventy-nine, versus, one, llama-7b, mean in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_runs_order_time_far_cheaper`

- Preferred role: `content`
- Cue keywords: `runs, order, time, far, cheaper, full, svd`
- Narration: And it runs in order n d m time, far cheaper than a full SVD.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_runs_order_time_far_cheaper" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords runs, order, time, far, cheaper, full in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_low_rank_low_precision`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, low, rank, low, precision, complementary, exploiting, them, together, pays`
- Narration: The takeaway: low rank and low precision are complementary, and exploiting them together pays off.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_low_rank_low_precision" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, low, rank, low, precision, complementary in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_sketching_matrix_gaussian_projection`

- Preferred role: `result`
- Cue keywords: `sketching, matrix, gaussian, projection, quantizing, factors, lplr, compresses, one, bit`
- Narration: By sketching a matrix with a Gaussian projection and quantizing the factors, LPLR compresses to one bit per coordinate while preserving accuracy on images, embeddings, and LLM weights, with provable error bounds.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c2_sketching_matrix_gaussian_projection" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sketching, matrix, gaussian, projection, quantizing, factors in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_avoiding_costly_svd_scales_largest`

- Preferred role: `content`
- Cue keywords: `avoiding, costly, svd, scales, largest, matrices`
- Narration: And by avoiding costly SVD, it scales to largest matrices.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_avoiding_costly_svd_scales_largest" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords avoiding, costly, svd, scales, largest, matrices in title/desc so the matcher can verify semantic overlap.
