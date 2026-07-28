# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_studies_two_workhorse_optimizers_mom`

- Preferred role: `content`
- Cue keywords: `studies, two, workhorse, optimizers, momentum, sgd, adagrad`
- Narration: This paper studies two workhorse optimizers, momentum SGD and AdaGrad.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_studies_two_workhorse_optimizers_mom" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords studies, two, workhorse, optimizers, momentum, sgd in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_despite_practical_success_their_non`

- Preferred role: `content`
- Cue keywords: `despite, practical, success, their, non-convex, theory, lags`
- Narration: Despite practical success, their non-convex theory lags.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_despite_practical_success_their_non" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords despite, practical, success, their, non-convex, theory in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_prove_both_converge_almost`

- Preferred role: `content`
- Cue keywords: `authors, prove, both, converge, almost, surely, stationary, points, show, why`
- Narration: The authors prove both converge almost surely to stationary points, and show why momentum accelerates SGD.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_authors_prove_both_converge_almost" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, prove, both, converge, almost, surely in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_momentum_sgd_adagrad_consistently_be`

- Preferred role: `content`
- Cue keywords: `momentum, sgd, adagrad, consistently, beat, plain, sgd, yet, their, theory`
- Narration: Momentum SGD and AdaGrad consistently beat plain SGD, yet their theory is incomplete.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_momentum_sgd_adagrad_consistently_be" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords momentum, sgd, adagrad, consistently, beat, plain in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_possibly_non_convex_losses_existing`

- Preferred role: `result`
- Cue keywords: `possibly, non-convex, losses, existing, analyses, prove, only, weak, guarantees, like`
- Narration: For possibly non-convex losses, existing analyses prove only weak guarantees, like subsequence or time-average convergence, not the almost-sure convergence practitioners rely on.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c2_possibly_non_convex_losses_existing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords possibly, non-convex, losses, existing, analyses, prove in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_now`

- Preferred role: `content`
- Cue keywords: `why, now`
- Narration: Why now?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_why_now" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, now in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_prior_momentum_proofs_need_coefficie`

- Preferred role: `content`
- Cue keywords: `prior, momentum, proofs, need, coefficient, shrinking, zero, but, practitioners, fix`
- Narration: Prior momentum proofs need a coefficient shrinking to zero, but practitioners fix it near zero point nine.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_prior_momentum_proofs_need_coefficie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, momentum, proofs, need, coefficient, shrinking in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_prior_adagrad_results_cover_modified`

- Preferred role: `result`
- Cue keywords: `prior, adagrad, results, cover, modified, form, not, standard, one`
- Narration: Prior AdaGrad results cover a modified form, not the standard one.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c3_prior_adagrad_results_cover_modified" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, adagrad, results, cover, modified, form in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_drops_convexity_bounded_iterate_boun`

- Preferred role: `content`
- Cue keywords: `drops, convexity, bounded-iterate, bounded-noise, assumptions`
- Narration: It drops convexity, bounded-iterate, and bounded-noise assumptions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_drops_convexity_bounded_iterate_boun" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords drops, convexity, bounded-iterate, bounded-noise, assumptions in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_three_contributions`

- Preferred role: `content`
- Cue keywords: `three, contributions`
- Narration: Three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_momentum_sgd_iterates_converge`

- Preferred role: `figure`
- Cue keywords: `first, momentum, sgd, iterates, converge, almost, surely, connected, set, stationary`
- Narration: First, momentum SGD iterates converge almost surely to a connected set of stationary points, even for non-convex losses.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c2_first_momentum_sgd_iterates_converge" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, momentum, sgd, iterates, converge, almost in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_quantifies_msgd_rate_explaini`

- Preferred role: `content`
- Cue keywords: `second, quantifies, msgd, rate, explaining, momentum, acceleration`
- Narration: Second, it quantifies mSGD's rate, explaining momentum's acceleration.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_second_quantifies_msgd_rate_explaini" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, quantifies, msgd, rate, explaining, momentum in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_standard_norm_form_adagrad_als`

- Preferred role: `content`
- Cue keywords: `third, standard, norm-form, adagrad, also, converges, almost, surely`
- Narration: Third, standard norm-form AdaGrad also converges almost surely.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_third_standard_norm_form_adagrad_als" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, standard, norm-form, adagrad, also, converges in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_analysis_stochastic_approximation_tr`

- Preferred role: `figure`
- Cue keywords: `analysis, stochastic, approximation, treating, algorithm, noisy, gradient, flow`
- Narration: The analysis uses stochastic approximation, treating each algorithm as a noisy gradient flow.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c1_analysis_stochastic_approximation_tr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords analysis, stochastic, approximation, treating, algorithm, noisy in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_stability_lemma_bounds_expected_loss`

- Preferred role: `figure`
- Cue keywords: `stability, lemma, bounds, expected, loss`
- Narration: A stability lemma bounds the expected loss.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c2_stability_lemma_bounds_expected_loss" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stability, lemma, bounds, expected, loss in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_instead_uniformly_bounded_noise_they`

- Preferred role: `figure`
- Cue keywords: `instead, uniformly, bounded, noise, they, bound, relative, loss`
- Narration: Instead of uniformly bounded noise, they bound it relative to the loss.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c3_instead_uniformly_bounded_noise_they" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, uniformly, bounded, noise, they, bound in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_msgd_decreasing_robbins_monro_steps`

- Preferred role: `content`
- Cue keywords: `msgd, decreasing, robbins-monro, steps, static, momentum, adagrad, adaptive, step, needs`
- Narration: mSGD uses decreasing Robbins-Monro steps with static momentum; AdaGrad's adaptive step needs new bounds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_msgd_decreasing_robbins_monro_steps" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords msgd, decreasing, robbins-monro, steps, static, momentum in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_work_entirely_theoretical_datasets_b`

- Preferred role: `result`
- Cue keywords: `work, entirely, theoretical, datasets, benchmarks, experiments, only, proven, theorems`
- Narration: This work is entirely theoretical: no datasets, benchmarks, or experiments, only proven theorems.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_work_entirely_theoretical_datasets_b" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, entirely, theoretical, datasets, benchmarks, experiments in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_losses_non_negative_differentiable_l`

- Preferred role: `figure`
- Cue keywords: `losses, non-negative, differentiable, lipschitz, gradients, but, possibly, non-convex, like, sine-squared`
- Narration: The losses are non-negative and differentiable with Lipschitz gradients, but possibly non-convex, like sine-squared and quartic polynomials.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c2_losses_non_negative_differentiable_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords losses, non-negative, differentiable, lipschitz, gradients, but in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_two_almost_sure_convergence`

- Preferred role: `content`
- Cue keywords: `headline, two, almost-sure, convergence, theorems`
- Narration: The headline is two almost-sure convergence theorems.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_headline_two_almost_sure_convergence" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, two, almost-sure, convergence, theorems in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_theorem_1_momentum_sgd_iterates`

- Preferred role: `content`
- Cue keywords: `theorem, 1, momentum, sgd, iterates, converge, connected, set, stationary, points`
- Narration: Theorem 1: momentum SGD iterates converge to a connected set of stationary points.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_theorem_1_momentum_sgd_iterates" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords theorem, 1, momentum, sgd, iterates, converge in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_theorem_3_standard_adagrad_does`

- Preferred role: `content`
- Cue keywords: `theorem, 3, standard, adagrad, does, same`
- Narration: Theorem 3: standard AdaGrad does the same.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_theorem_3_standard_adagrad_does" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords theorem, 3, standard, adagrad, does, same in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_both_strengthen_earlier_subsequence`

- Preferred role: `method`
- Cue keywords: `both, strengthen, earlier, subsequence, time-average, results`
- Narration: Both strengthen earlier subsequence and time-average results.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_both_strengthen_earlier_subsequence" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords both, strengthen, earlier, subsequence, time-average, results in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_place_experiments_studies_how_conver`

- Preferred role: `content`
- Cue keywords: `place, experiments, studies, how, convergence, rate, depends, momentum, coefficient`
- Narration: In place of experiments, the paper studies how the convergence rate depends on the momentum coefficient.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_place_experiments_studies_how_conver" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords place, experiments, studies, how, convergence, rate in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_zero_recovers_sgd_rate_exactly`

- Preferred role: `result`
- Cue keywords: `zero, recovers, sgd, rate, exactly, toward, one, shrinks, coefficient, pushes`
- Narration: At zero it recovers SGD's rate exactly; toward one it shrinks the coefficient and pushes the time-average rate to order one over T.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_zero_recovers_sgd_rate_exactly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords zero, recovers, sgd, rate, exactly, toward in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_key_numbers_convergence_rates`

- Preferred role: `content`
- Cue keywords: `key, numbers, convergence, rates`
- Narration: The key numbers are convergence rates.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_key_numbers_convergence_rates" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, numbers, convergence, rates in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_momentum_sgd_expected_squared_gradie`

- Preferred role: `figure`
- Cue keywords: `momentum, sgd, expected, squared, gradient, norm, decays, exponentially, exponent, scaling`
- Narration: Momentum SGD's expected squared gradient norm decays exponentially, with exponent scaling as summed step sizes over p times one-minus-alpha squared.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s09_c2_momentum_sgd_expected_squared_gradie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords momentum, sgd, expected, squared, gradient, norm in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_alpha_zero_recovers_sgd_rate`

- Preferred role: `result`
- Cue keywords: `alpha, zero, recovers, sgd, rate, near, one, reaches, order, one`
- Narration: Alpha zero recovers the SGD rate; near one it reaches order one over T.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_alpha_zero_recovers_sgd_rate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords alpha, zero, recovers, sgd, rate, near in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_reassuringly_practitioners_under_mil`

- Preferred role: `figure`
- Cue keywords: `reassuringly, practitioners, under, mild, conditions, both, fixed-momentum, sgd, standard, adagrad`
- Narration: Reassuringly for practitioners, under mild conditions both fixed-momentum SGD and standard AdaGrad converge almost surely to stationary points of non-convex losses, and momentum provably accelerates SGD, narrowing the gap between theory and practice.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c1_reassuringly_practitioners_under_mil" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reassuringly, practitioners, under, mild, conditions, both in title/desc so the matcher can verify semantic overlap.
