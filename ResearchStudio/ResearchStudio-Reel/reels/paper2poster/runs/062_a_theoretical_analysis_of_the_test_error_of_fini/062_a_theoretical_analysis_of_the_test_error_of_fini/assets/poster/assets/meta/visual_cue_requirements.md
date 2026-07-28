# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_work_sharply_analyzes_test_error`

- Preferred role: `result`
- Cue keywords: `work, sharply, analyzes, test, error, finite-rank, kernel, ridge, regression, behind`
- Narration: This work sharply analyzes the test error of finite-rank kernel ridge regression, the model behind tuning a frozen network's last layer.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c1_work_sharply_analyzes_test_error" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, sharply, analyzes, test, error, finite-rank in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_derives_matching_upper_lower_bounds`

- Preferred role: `content`
- Cue keywords: `derives, matching, upper, lower, bounds, stay, tight, any, regularization`
- Narration: It derives matching upper and lower bounds that stay tight for any regularization.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_derives_matching_upper_lower_bounds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords derives, matching, upper, lower, bounds, stay in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_kernel_ridge_regression_helps_explai`

- Preferred role: `content`
- Cue keywords: `kernel, ridge, regression, helps, explain, generalization, tuning, network, last, layer`
- Narration: Kernel ridge regression helps explain generalization, and tuning a network's last layer behaves like it with a finite-rank kernel.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_kernel_ridge_regression_helps_explai" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords kernel, ridge, regression, helps, explain, generalization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_classical_bounds_far_too`

- Preferred role: `content`
- Cue keywords: `but, classical, bounds, far, too, loose, they, keep, ridge, above`
- Narration: But classical bounds are far too loose here: they keep the ridge above zero, give only upper bounds, and go vacuous as regularization vanishes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_but_classical_bounds_far_too" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, classical, bounds, far, too, loose in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_freezing_pre_trained_backbone_retrai`

- Preferred role: `method`
- Cue keywords: `freezing, pre-trained, backbone, retraining, only, final, layer, everywhere, defines, finite-rank`
- Narration: Freezing a pre-trained backbone and retraining only the final layer is everywhere, and it defines a finite-rank kernel.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_freezing_pre_trained_backbone_retrai" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords freezing, pre-trained, backbone, retraining, only, final in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_yet_theory_lags_many_results`

- Preferred role: `result`
- Cue keywords: `yet, theory, lags, many, results, need, input, dimension, grow, others`
- Narration: Yet the theory lags: many results need the input dimension to grow, others fix how the ridge decays, and almost none give a lower bound, without which tightness cannot be claimed.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_yet_theory_lags_many_results" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yet, theory, lags, many, results, need in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_contribution_threefold_first_bounds`

- Preferred role: `content`
- Cue keywords: `contribution, threefold, first, bounds, improve, ridge, goes, zero`
- Narration: The contribution is threefold. First, the bounds improve as the ridge goes to zero.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_contribution_threefold_first_bounds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contribution, threefold, first, bounds, improve, ridge in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_sharp_lower_bound_matches`

- Preferred role: `content`
- Cue keywords: `second, sharp, lower, bound, matches, upper, bound, samples, grow, both`
- Narration: Second, a sharp lower bound matches the upper bound as samples grow, so both are tight.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_second_sharp_lower_bound_matches" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, sharp, lower, bound, matches, upper in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_experiments_show_large_gain`

- Preferred role: `result`
- Cue keywords: `third, experiments, show, large, gain, over, prior, work`
- Narration: Third, experiments show a large gain over prior work.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c3_third_experiments_show_large_gain" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, experiments, show, large, gain, over in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_key_trick_work_eigenfunction_basis`

- Preferred role: `content`
- Cue keywords: `key, trick, work, eigenfunction, basis, separating, spectrum, sampling, noise`
- Narration: The key trick: work in the eigenfunction basis, separating spectrum from sampling noise.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_key_trick_work_eigenfunction_basis" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, trick, work, eigenfunction, basis, separating in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_starts_kernel_ridge_estimator`

- Preferred role: `method`
- Cue keywords: `method, starts, kernel-ridge, estimator, splits, test, error, bias, term, variance`
- Narration: The method starts from the kernel-ridge estimator and splits the test error into a bias term and a variance term, each bounded with high probability.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_starts_kernel_ridge_estimator" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, starts, kernel-ridge, estimator, splits, test in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_key_ingredients_careful_algebra_ridg`

- Preferred role: `content`
- Cue keywords: `key, ingredients, careful, algebra, ridge, terms, sub-gaussian, covariance, concentration, inequality`
- Narration: The key ingredients: careful algebra on the ridge terms, a sub-Gaussian covariance concentration inequality, and a Neumann-series expansion.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_key_ingredients_careful_algebra_ridg" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, ingredients, careful, algebra, ridge, terms in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_lets_bounds_hold_any_ridge`

- Preferred role: `content`
- Cue keywords: `lets, bounds, hold, any, ridge, value`
- Narration: That lets the bounds hold for any ridge value.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_lets_bounds_hold_any_ridge" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lets, bounds, hold, any, ridge, value in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_being_theory_experiments_controlled`

- Preferred role: `content`
- Cue keywords: `being, theory, experiments, controlled, synthetic, settings`
- Narration: Being a theory paper, the experiments use controlled synthetic settings.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_being_theory_experiments_controlled" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords being, theory, experiments, controlled, synthetic, settings in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_authors_test_two_finite_rank_kernels`

- Preferred role: `method`
- Cue keywords: `authors, test, two, finite-rank, kernels, truncated, neural, tangent, kernel, constructed`
- Narration: The authors test two finite-rank kernels: a truncated neural tangent kernel and a constructed low-rank kernel.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_authors_test_two_finite_rank_kernels" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, test, two, finite-rank, kernels, truncated in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_they_sweep_sample_sizes_ten`

- Preferred role: `method`
- Cue keywords: `they, sweep, sample, sizes, ten, two, hundred, many, ridge, values`
- Narration: For each they sweep sample sizes from ten to two hundred and many ridge values, averaging ten trials with median and quartile bars.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_they_sweep_sample_sizes_ten" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, sweep, sample, sizes, ten, two in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_new_upper_lower_bounds_bracket`

- Preferred role: `result`
- Cue keywords: `new, upper, lower, bounds, bracket, error, across, sample, sizes, both`
- Narration: The new upper and lower bounds bracket the error across sample sizes on both kernels, and squeeze together as samples grow.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_new_upper_lower_bounds_bracket" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords new, upper, lower, bounds, bracket, error in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_against_bach_bound_gain_stark`

- Preferred role: `result`
- Cue keywords: `against, bach, bound, gain, stark, new, bound, hugs, true, error`
- Narration: Against Bach's bound the gain is stark: the new bound hugs the true error while Bach's floats far above.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_against_bach_bound_gain_stark" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords against, bach, bound, gain, stark, new in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_ridgeless_limit_bias_reduces_finite`

- Preferred role: `result`
- Cue keywords: `ridgeless, limit, bias, reduces, finite-rank, error, variance, noise`
- Narration: In the ridgeless limit, bias reduces to the finite-rank error and variance to the noise.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_ridgeless_limit_bias_reduces_finite" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ridgeless, limit, bias, reduces, finite-rank, error in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablates_its_bound`

- Preferred role: `content`
- Cue keywords: `ablates, its, bound`
- Narration: The paper ablates its bound.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablates_its_bound" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablates, its, bound in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_finite_rank_error_irreducible_floor`

- Preferred role: `result`
- Cue keywords: `finite-rank, error, irreducible, floor, while, residue, terms, shrink, log-n-over-n, rate`
- Narration: The finite-rank error is an irreducible floor, while residue terms shrink at a log-N-over-N rate and vanish for large samples.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_finite_rank_error_irreducible_floor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finite-rank, error, irreducible, floor, while, residue in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_dropped_simplified_bounds_fail_only`

- Preferred role: `content`
- Cue keywords: `dropped, simplified, bounds, fail, only, small-sample, regime, predicted`
- Narration: Dropped, the simplified bounds fail only in the small-sample regime, as predicted.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_dropped_simplified_bounds_fail_only" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dropped, simplified, bounds, fail, only, small-sample in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_ridge_sweep_shows_new_bound`

- Preferred role: `content`
- Cue keywords: `ridge, sweep, shows, new, bound, improves, toward, ridgeless, limit, while`
- Narration: A ridge sweep shows the new bound improves toward the ridgeless limit while the prior worsens.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_ridge_sweep_shows_new_bound" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ridge, sweep, shows, new, bound, improves in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_bounds_hold_probability_least_one`

- Preferred role: `content`
- Cue keywords: `bounds, hold, probability, least, one, minus, two, over`
- Narration: The bounds hold with probability at least one minus two over N.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_bounds_hold_probability_least_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords bounds, hold, probability, least, one, minus in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_upper_bound_decays_log_n_over_n_rate`

- Preferred role: `content`
- Cue keywords: `upper, bound, decays, log-n-over-n, rate, faster, square-root, rademacher, rate`
- Narration: The upper bound decays at a log-N-over-N rate, faster than the square-root Rademacher rate.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_upper_bound_decays_log_n_over_n_rate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords upper, bound, decays, log-n-over-n, rate, faster in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_variance_scales_noise_times_twice`

- Preferred role: `content`
- Cue keywords: `variance, scales, noise, times, twice, rank, over`
- Narration: Variance scales as noise times twice the rank over N.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_variance_scales_noise_times_twice" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords variance, scales, noise, times, twice, rank in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_these_first_finite_rank_bounds_high`

- Preferred role: `content`
- Cue keywords: `these, first, finite-rank, bounds, high-probability, lower, bound`
- Narration: And these are the first finite-rank bounds with a high-probability lower bound.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_these_first_finite_rank_bounds_high" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, first, finite-rank, bounds, high-probability, lower in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_finite_rank_kernel_ridge_re`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, finite-rank, kernel, ridge, regression, behind, last-layer, fine-tuning, sharp, bounds`
- Narration: The takeaway: finite-rank kernel ridge regression, behind last-layer fine-tuning, has sharp bounds, matching upper and lower, tight for any regularization including none.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_finite_rank_kernel_ridge_re" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, finite-rank, kernel, ridge, regression, behind in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_key_idea_working_eigenfunction_basis`

- Preferred role: `content`
- Cue keywords: `key, idea, working, eigenfunction, basis, separate, spectrum, sampling, noise, template`
- Narration: The key idea, working in the eigenfunction basis to separate spectrum from sampling noise, is a template others can borrow.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_key_idea_working_eigenfunction_basis" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, idea, working, eigenfunction, basis, separate in title/desc so the matcher can verify semantic overlap.
