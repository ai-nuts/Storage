# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_comparing_unpaired_samples_populatio`

- Preferred role: `method`
- Cue keywords: `comparing, unpaired, samples, population, measured, different, points, time, core, challenge`
- Narration: Comparing unpaired samples of a population measured at different points in time is a core challenge in biology, where measuring cells often destroys them.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_comparing_unpaired_samples_populatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords comparing, unpaired, samples, population, measured, different in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_optimal_transport_recover_how_sample`

- Preferred role: `method`
- Cue keywords: `optimal, transport, recover, how, samples, map, across, distributions, but, classical`
- Narration: Optimal transport can recover how samples map across distributions, but classical OT assumes mass is conserved, which breaks down when populations grow or shrink through cell proliferation and death.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_optimal_transport_recover_how_sample" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords optimal, transport, recover, how, samples, map in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_introduces_nubot_neural_unbalanced_o`

- Preferred role: `method`
- Cue keywords: `introduces, nubot, neural, unbalanced, optimal, transport, method, built, formalism, semi-couplings`
- Narration: This paper introduces NubOT, a neural unbalanced optimal transport method built on the formalism of semi-couplings, letting it explicitly account for the creation and destruction of mass.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_introduces_nubot_neural_unbalanced_o" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, nubot, neural, unbalanced, optimal, transport in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_through_cycle_consistent_scheme_nubo`

- Preferred role: `method`
- Cue keywords: `through, cycle-consistent, scheme, nubot, learns, both, where, cells, move, how`
- Narration: Through a cycle-consistent training scheme, NubOT learns both where cells move and how their mass rescales, and when applied to forecasting how cancer cell lines respond to dozens of drugs, it outperforms prior neural OT methods while recovering biologically meaningful proliferation and death signals.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_through_cycle_consistent_scheme_nubo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords through, cycle-consistent, scheme, nubot, learns, both in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_recurring_problem_natural_sciences_m`

- Preferred role: `content`
- Cue keywords: `recurring, problem, natural, sciences, modeling, how, population, changes, after, intervention`
- Narration: A recurring problem in the natural sciences is modeling how a population changes after an intervention, when you can only observe unpaired snapshots rather than track individuals.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_recurring_problem_natural_sciences_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recurring, problem, natural, sciences, modeling, how in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_single_cell_biology_unavoidable_beca`

- Preferred role: `method`
- Cue keywords: `single-cell, biology, unavoidable, because, profiling, cell, destroys, same, cell, never`
- Narration: In single-cell biology this is unavoidable, because profiling a cell destroys it, so the same cell can never be measured twice.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_single_cell_biology_unavoidable_beca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single-cell, biology, unavoidable, because, profiling, cell in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_optimal_transport_offers_principled`

- Preferred role: `method`
- Cue keywords: `optimal, transport, offers, principled, way, infer, these, correspondences, learning, optimal`
- Narration: Optimal transport offers a principled way to infer these correspondences by learning an optimal coupling between distributions. But the standard formulation assumes conservation of mass, meaning every unit of source mass must be transported somewhere.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_optimal_transport_offers_principled" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords optimal, transport, offers, principled, way, infer in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_assumption_violated_exactly_when_mat`

- Preferred role: `content`
- Cue keywords: `assumption, violated, exactly, when, matters, most, unbalanced, settings, where, cells`
- Narration: That assumption is violated exactly when it matters most, in unbalanced settings where cells proliferate or die, and the total population size shifts between measurements.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_assumption_violated_exactly_when_mat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords assumption, violated, exactly, when, matters, most in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_cellular_responses_drugs_highly_hete`

- Preferred role: `content`
- Cue keywords: `cellular, responses, drugs, highly, heterogeneous, different, cell, types, states, respond`
- Narration: Cellular responses to drugs are highly heterogeneous: different cell types and states can respond in opposite ways, some proliferating while others die.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_cellular_responses_drugs_highly_hete" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cellular, responses, drugs, highly, heterogeneous, different in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_capturing_requires_nonlinear_maps_le`

- Preferred role: `result`
- Cue keywords: `capturing, requires, nonlinear, maps, level, single, cells, not, aggregate, averages`
- Narration: Capturing this requires nonlinear maps at the level of single cells, not aggregate averages.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_capturing_requires_nonlinear_maps_le" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords capturing, requires, nonlinear, maps, level, single in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_prior_neural_optimal_transport_metho`

- Preferred role: `method`
- Cue keywords: `prior, neural, optimal, transport, methods, learn, such, maps, but, they`
- Narration: Prior neural optimal transport methods can learn such maps, but they either assume the balanced setting where mass is conserved, or, like the state-of-the-art unbalanced GAN approach, they only capture the general trend of growth and shrinkage without recovering the exact reweighting each subpopulation needs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_prior_neural_optimal_transport_metho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, neural, optimal, transport, methods, learn in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_what_been_missing_method_jointly`

- Preferred role: `method`
- Cue keywords: `what, been, missing, method, jointly, accurately, models, where, mass, moves`
- Narration: What has been missing is a method that jointly and accurately models where mass moves and how much of it is created or destroyed, in a way that stays faithful to the biology.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_what_been_missing_method_jointly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, been, missing, method, jointly, accurately in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions_first`

- Preferred role: `content`
- Cue keywords: `makes, three, main, contributions, first, introduces, novel, formulation, unbalanced, optimal`
- Narration: The paper makes three main contributions. First, it introduces a novel formulation of the unbalanced optimal transport problem that connects the rigorous theory of semi-couplings, which allow mass to vary, with a practical and scalable optimal-transport mapping estimator.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions, first, introduces in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_derives_computationally_feasi`

- Preferred role: `content`
- Cue keywords: `second, derives, computationally, feasible, implementation, based, dual, potentials, parameterized, input`
- Narration: Second, it derives a computationally feasible implementation based on dual potentials parameterized by input convex neural networks, together with learned reweighting functions that predict mass changes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_second_derives_computationally_feasi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, derives, computationally, feasible, implementation, based in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_proposes_new_cycle_consistent`

- Preferred role: `method`
- Cue keywords: `third, proposes, new, cycle-consistent, procedure, alternates, between, updating, these, maps`
- Narration: Third, it proposes a new cycle-consistent training procedure that alternates between updating these maps and rescaling functions, and crucially generalizes to new, out-of-sample cells.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_third_proposes_new_cycle_consistent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, proposes, new, cycle-consistent, procedure, alternates in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_together_these_give_first_neural`

- Preferred role: `method`
- Cue keywords: `together, these, give, first, neural, method, estimates, semi-couplings, unbalanced, single-cell`
- Narration: Together these give the first neural method that estimates semi-couplings for unbalanced OT at single-cell scale.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_together_these_give_first_neural" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, these, give, first, neural, method in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_nubot_key_idea_split_hard`

- Preferred role: `figure`
- Cue keywords: `nubot, key, idea, split, hard, unbalanced, problem, two, coupled, pieces`
- Narration: NubOT's key idea is to split the hard unbalanced problem into two coupled pieces: feature transformation and mass rescaling. It introduces proxy measures that are simply rescaled versions of the source and target, weighted by scalar fields eta and zeta, chosen so the two proxies have equal mass.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c1_nubot_key_idea_split_hard" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords nubot, key, idea, split, hard, unbalanced in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_between_these_now_balanced_measures`

- Preferred role: `content`
- Cue keywords: `between, these, now-balanced, measures, solves, standard, optimal, transport, problem, learning`
- Narration: Between these now-balanced measures it solves a standard optimal transport problem, learning forward and backward Monge maps as the gradients of convex potentials represented by input convex neural networks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_between_these_now_balanced_measures" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords between, these, now-balanced, measures, solves, standard in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_because_marginals_themselves_shift_r`

- Preferred role: `figure`
- Cue keywords: `because, marginals, themselves, shift, reweighting, functions, update, nubot, alternating, minimization`
- Narration: Because the marginals themselves shift as the reweighting functions update, NubOT uses an alternating minimization: it estimates the mass rescaling with an efficient single-step unbalanced Sinkhorn update, then updates the transport potentials through a min-max objective, cycling between the two.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c3_because_marginals_themselves_shift_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, marginals, themselves, shift, reweighting, functions in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_reweighting_functions_learned_neural`

- Preferred role: `content`
- Cue keywords: `reweighting, functions, learned, neural, networks, test, time, map, new, cell`
- Narration: The reweighting functions are learned as neural networks, so at test time the model can map a new cell and simultaneously predict whether its mass should grow or shrink.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_reweighting_functions_learned_neural" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reweighting, functions, learned, neural, networks, test in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_method_evaluated_two_settings_first`

- Preferred role: `method`
- Cue keywords: `method, evaluated, two, settings, first, synthetic, benchmark, two-dimensional, mixture, three`
- Narration: The method is evaluated on two settings. The first is a synthetic benchmark: a two-dimensional mixture of three Gaussian clusters, where the target keeps the same clusters but changes their proportions and shifts them in space, across three scenarios of increasing imbalance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_method_evaluated_two_settings_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, evaluated, two, settings, first, synthetic in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_second_real_single_cell_perturbation`

- Preferred role: `content`
- Cue keywords: `second, real, single-cell, perturbation, dataset, generated, imaging, technology, called, 4`
- Narration: The second is a real single-cell perturbation dataset, generated with the imaging technology called 4i, that tracks two co-cultured melanoma cell lines responding to twenty-five different drugs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_second_real_single_cell_perturbation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, real, single-cell, perturbation, dataset, generated in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_cells_measured_zero_eight_twenty_fou`

- Preferred role: `content`
- Cue keywords: `cells, measured, zero, eight, twenty-four, hours, control, cells, exposed, only`
- Narration: Cells are measured at zero, eight, and twenty-four hours, with control cells exposed only to a vehicle serving as the source and the perturbed populations serving as targets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_cells_measured_zero_eight_twenty_fou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cells, measured, zero, eight, twenty-four, hours in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_two_cell_lines_distinguished_mutuall`

- Preferred role: `result`
- Cue keywords: `two, cell, lines, distinguished, mutually, exclusive, protein, markers, mela, sox9`
- Narration: The two cell lines are distinguished by mutually exclusive protein markers, MelA and Sox9, and additional markers for proliferation and cell death allow the predicted mass changes to be checked against biology.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_two_cell_lines_distinguished_mutuall" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, cell, lines, distinguished, mutually, exclusive in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_real_single_cell_task_nubot`

- Preferred role: `result`
- Cue keywords: `across, real, single-cell, task, nubot, outperforms, every, baseline, including, current`
- Narration: Across the real single-cell task, NubOT outperforms every baseline, including the current state-of-the-art unbalanced GAN, in almost all of the twenty-five drug perturbations, measured by a weighted version of kernel maximum mean discrepancy between predicted and observed perturbed cells.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_across_real_single_cell_task_nubot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, real, single-cell, task, nubot, outperforms in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_just_importantly_does_while_getting`

- Preferred role: `result`
- Cue keywords: `just, importantly, does, while, getting, mass, changes, right, synthetic, benchmark`
- Narration: Just as importantly, it does so while getting the mass changes right: on the synthetic benchmark it maps each cluster to its correct target without leaking mass between clusters, and it predicts the exact reweighting each cluster needs, where the GAN baseline only captures the broad direction of growth and shrinkage.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_just_importantly_does_while_getting" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords just, importantly, does, while, getting, mass in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_combination_accurate_feature_mapping`

- Preferred role: `figure`
- Cue keywords: `combination, accurate, feature, mapping, accurate, mass, rescaling, what, sets, nubot`
- Narration: This combination of accurate feature mapping and accurate mass rescaling is what sets NubOT apart.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s07_c3_combination_accurate_feature_mapping" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords combination, accurate, feature, mapping, accurate, mass in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_test_whether_predicted_mass_changes`

- Preferred role: `result`
- Cue keywords: `test, whether, predicted, mass, changes, biologically, meaningful, authors, compare, them`
- Narration: To test whether the predicted mass changes are biologically meaningful, the authors compare them against independent measurements.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_test_whether_predicted_mass_changes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, whether, predicted, mass, changes, biologically in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_summing_nubot_predicted_weights_with`

- Preferred role: `method`
- Cue keywords: `summing, nubot, predicted, weights, within, subpopulation, they, find, strong, correlation`
- Narration: Summing NubOT's predicted weights within each subpopulation, they find a strong correlation with the observed change in cell counts after eight hours, with a correlation coefficient of point nine five.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_summing_nubot_predicted_weights_with" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords summing, nubot, predicted, weights, within, subpopulation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_after_twenty_four_hours_correlation`

- Preferred role: `content`
- Cue keywords: `after, twenty-four, hours, correlation, drops, point, four, four, because, some`
- Narration: After twenty-four hours the correlation drops to point four four, because for some drugs the induced cell death is so severe that too few cells remain to evaluate reliably, yet the overall trend still holds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_after_twenty_four_hours_correlation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords after, twenty-four, hours, correlation, drops, point in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_going_further_predicted_weights_line`

- Preferred role: `method`
- Cue keywords: `going, further, predicted, weights, line, spatially, proliferation, marker, ki67, where`
- Narration: Going further, the predicted weights line up spatially with a proliferation marker, Ki67, where NubOT predicts weights above one, and with an apoptosis marker where it predicts weights below one, confirming that the model is recovering real proliferation and death signals rather than fitting the distribution superficially.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_going_further_predicted_weights_line" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords going, further, predicted, weights, line, spatially in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_numbers_tell_clear_story`

- Preferred role: `content`
- Cue keywords: `headline, numbers, tell, clear, story`
- Narration: The headline numbers tell a clear story.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_headline_numbers_tell_clear_story" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, numbers, tell, clear, story in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_nubot_beats_every_baseline_almost`

- Preferred role: `method`
- Cue keywords: `nubot, beats, every, baseline, almost, all, twenty-five, drug, perturbations, distributional`
- Narration: NubOT beats every baseline in almost all of the twenty-five drug perturbations on the distributional fit metric.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_nubot_beats_every_baseline_almost" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords nubot, beats, every, baseline, almost, all in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_its_predicted_per_subpopulation_weig`

- Preferred role: `method`
- Cue keywords: `its, predicted, per-subpopulation, weights, correlate, observed, cell, counts, coefficient, point`
- Narration: Its predicted per-subpopulation weights correlate with observed cell counts at a coefficient of point nine five after eight hours, an extremely strong agreement, and still at point four four after twenty-four hours despite drug-induced cell death thinning the observable populations.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_its_predicted_per_subpopulation_weig" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, predicted, per-subpopulation, weights, correlate, observed in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_evaluation_spans_two_co_cultured_mel`

- Preferred role: `result`
- Cue keywords: `evaluation, spans, two, co-cultured, melanoma, cell, lines, distinguished, mela, sox9`
- Narration: The evaluation spans two co-cultured melanoma cell lines distinguished by the MelA and Sox9 markers, imaged at three time points with the 4i technology, and compares against four baselines including the prior state-of-the-art unbalanced GAN.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_evaluation_spans_two_co_cultured_mel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, spans, two, co-cultured, melanoma, cell in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_unbalanced_optimal_transpor`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, unbalanced, optimal, transport, made, both, practical, biologically, faithful`
- Narration: The takeaway is that unbalanced optimal transport can be made both practical and biologically faithful.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_unbalanced_optimal_transpor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, unbalanced, optimal, transport, made, both in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_reformulating_through_learnable_semi`

- Preferred role: `method`
- Cue keywords: `reformulating, through, learnable, semi-couplings, maps, reweighting, functions, cycle-consistent, alternating, scheme`
- Narration: By reformulating it through learnable semi-couplings, and training the maps and reweighting functions with a cycle-consistent alternating scheme, NubOT simultaneously predicts the movement and the creation or destruction of mass at the level of individual cells.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_reformulating_through_learnable_semi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reformulating, through, learnable, semi-couplings, maps, reweighting in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_outperforms_previous_neural_optimal`

- Preferred role: `method`
- Cue keywords: `outperforms, previous, neural, optimal, transport, methods, challenging, task, forecasting, how`
- Narration: It outperforms previous neural optimal transport methods on the challenging task of forecasting how cancer cell lines respond to drugs, and it does so while producing predictions that align with known proliferation and death markers.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_outperforms_previous_neural_optimal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords outperforms, previous, neural, optimal, transport, methods in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_explicitly_modeling_cell_birth_death`

- Preferred role: `content`
- Cue keywords: `explicitly, modeling, cell, birth, death, rather, assuming, mass, conserved, what`
- Narration: Explicitly modeling cell birth and death, rather than assuming mass is conserved, is what makes this possible.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c4_explicitly_modeling_cell_birth_death" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords explicitly, modeling, cell, birth, death, rather in title/desc so the matcher can verify semantic overlap.
