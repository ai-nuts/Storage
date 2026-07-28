# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_comparing_collider_measurements_theo`

- Preferred role: `content`
- Cue keywords: `comparing, collider, measurements, theory, requires, unfolding, correcting, distortions, detectors, introduce`
- Narration: Comparing collider measurements with theory requires unfolding, that is, correcting the distortions that detectors introduce into the data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_comparing_collider_measurements_theo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords comparing, collider, measurements, theory, requires, unfolding in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_but_most_unfolding_methods_first`

- Preferred role: `method`
- Cue keywords: `but, most, unfolding, methods, first, bin, histograms, while, many, theory`
- Narration: But most unfolding methods first bin the data into histograms, while many theory predictions live at the level of statistical moments.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_but_most_unfolding_methods_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, most, unfolding, methods, first, bin in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_introduces_moment_unfolding_machine`

- Preferred role: `method`
- Cue keywords: `introduces, moment, unfolding, machine-learning, method, directly, unfolds, distribution, moments, without`
- Narration: This paper introduces Moment Unfolding, a machine-learning method that directly unfolds distribution moments without ever binning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_introduces_moment_unfolding_machine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, moment, unfolding, machine-learning, method, directly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_inspired_generative_adversarial_netw`

- Preferred role: `result`
- Cue keywords: `inspired, generative, adversarial, networks, boltzmann, approach, statistical, mechanics, recovers, moments`
- Narration: Inspired by Generative Adversarial Networks and by Boltzmann's approach to statistical mechanics, it recovers moments to sub-percent accuracy on both Gaussian toy data and simulated LHC jets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_inspired_generative_adversarial_netw" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords inspired, generative, adversarial, networks, boltzmann, approach in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_unfolding_also_known_deconvolution_c`

- Preferred role: `content`
- Cue keywords: `unfolding, also, known, deconvolution, corrects, distortions, detector, imprints, measured, experiments`
- Narration: Unfolding, also known as deconvolution, corrects the distortions a detector imprints on measured data so that experiments can be compared with each other and with theory.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_unfolding_also_known_deconvolution_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unfolding, also, known, deconvolution, corrects, distortions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_usual_recipe_unfolds_entire_spectrum`

- Preferred role: `content`
- Cue keywords: `usual, recipe, unfolds, entire, spectrum, after, first, discretizing, histogram, computes`
- Narration: The usual recipe unfolds an entire spectrum after first discretizing it into a histogram, then computes moments from that histogram.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_usual_recipe_unfolds_entire_spectrum" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords usual, recipe, unfolds, entire, spectrum, after in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_but_binning_step_introduces_discreti`

- Preferred role: `content`
- Cue keywords: `but, binning, step, introduces, discretization, artifacts, wasteful, when, quantity, you`
- Narration: But this binning step introduces discretization artifacts, and it is wasteful when the quantity you actually care about is just a small set of moments as a function of another observable.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_but_binning_step_introduces_discreti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, binning, step, introduces, discretization, artifacts in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_mismatch_between_binned_moment_level`

- Preferred role: `content`
- Cue keywords: `mismatch, between, binned, moment-level, theory, predictions, gap, closes`
- Narration: That mismatch between binned data and moment-level theory predictions is the gap this paper closes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_mismatch_between_binned_moment_level" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mismatch, between, binned, moment-level, theory, predictions in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_summarizing_distribution_few_moments`

- Preferred role: `method`
- Cue keywords: `summarizing, distribution, few, moments, makes, tractable, visualize, crucially, predict, first`
- Narration: Summarizing a distribution with a few moments makes it tractable to visualize and, crucially, to predict from first principles.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_summarizing_distribution_few_moments" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords summarizing, distribution, few, moments, makes, tractable in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_example_full_densities_hadronic_jets`

- Preferred role: `content`
- Cue keywords: `example, full, densities, hadronic, jets, cannot, computed, perturbative, qcd, but`
- Narration: For example, the full densities of hadronic jets cannot be computed in perturbative QCD, but the energy dependence of their moments can be.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_example_full_densities_hadronic_jets" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords example, full, densities, hadronic, jets, cannot in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_unbinned_unfolding_methods_already_e`

- Preferred role: `method`
- Cue keywords: `unbinned, unfolding, methods, already, exist, avoid, binning, artifacts, but, they`
- Narration: Unbinned unfolding methods already exist and avoid binning artifacts, but they are built to unfold entire spectra, so they may trade away precision on the handful of moments a physicist actually wants.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_unbinned_unfolding_methods_already_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unbinned, unfolding, methods, already, exist, avoid in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_motivates_dedicated_method_unfolds_m`

- Preferred role: `method`
- Cue keywords: `motivates, dedicated, method, unfolds, moments, themselves`
- Narration: This motivates a dedicated method that unfolds the moments themselves.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_motivates_dedicated_method_unfolds_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords motivates, dedicated, method, unfolds, moments, themselves in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_core_contribution_moment_unfolding_n`

- Preferred role: `content`
- Cue keywords: `core, contribution, moment, unfolding, new, unbinned, non-iterative, reweighting, technique`
- Narration: The core contribution is Moment Unfolding, a new unbinned and non-iterative reweighting technique.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_core_contribution_moment_unfolding_n" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, contribution, moment, unfolding, new, unbinned in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_learns_reweighting_function_playing`

- Preferred role: `content`
- Cue keywords: `learns, reweighting, function, playing, role, gan, generator, whose, form, inspired`
- Narration: It learns a reweighting function, playing the role of a GAN generator, whose form is inspired by the Boltzmann factor so that its trainable parameters can be directly identified with the observable's moments.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_learns_reweighting_function_playing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords learns, reweighting, function, playing, role, gan in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_discriminator_pushes_reweighted_simu`

- Preferred role: `content`
- Cue keywords: `discriminator, pushes, reweighted, simulation, match, target`
- Narration: A discriminator pushes the reweighted simulation to match the target data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_discriminator_pushes_reweighted_simu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords discriminator, pushes, reweighted, simulation, match, target in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_unlike_omnifold_which_trains_fresh`

- Preferred role: `content`
- Cue keywords: `unlike, omnifold, which, trains, fresh, pair, networks, every, iteration, moment`
- Narration: Unlike OmniFold, which trains a fresh pair of networks on every iteration, Moment Unfolding trains a single pair of networks just once.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_unlike_omnifold_which_trains_fresh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unlike, omnifold, which, trains, fresh, pair in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_borrows_boltzmann_idea_buildi`

- Preferred role: `method`
- Cue keywords: `method, borrows, boltzmann, idea, building, distribution, maximizes, entropy, subject, fixed`
- Narration: The method borrows Boltzmann's idea of building the distribution that maximizes entropy subject to fixed moments. Concretely, the generator is written as the exponential of a polynomial in the observable, so its coefficients, the lambdas, are the moments being unfolded.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_borrows_boltzmann_idea_buildi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, borrows, boltzmann, idea, building, distribution in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_generator_reweights_simulated_events`

- Preferred role: `content`
- Cue keywords: `generator, reweights, simulated, events, discriminator, neural, network, tries, tell, reweighted`
- Narration: This generator reweights the simulated events, and a discriminator neural network tries to tell the reweighted simulation apart from the real data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_generator_reweights_simulated_events" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords generator, reweights, simulated, events, discriminator, neural in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_two_trained_against_other_weighted`

- Preferred role: `method`
- Cue keywords: `two, trained, against, other, weighted, binary, cross-entropy, loss, discriminator, minimizes`
- Narration: The two are trained against each other on a weighted binary cross-entropy loss: the discriminator minimizes it while the generator maximizes it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_two_trained_against_other_weighted" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, trained, against, other, weighted, binary in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_because_reweighting_only_changes_imp`

- Preferred role: `content`
- Cue keywords: `because, reweighting, only, changes, importance, weights, not, event, features, expensive`
- Narration: Because the reweighting only changes importance weights and not the event features, the expensive detector emulation runs a single time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_because_reweighting_only_changes_imp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, reweighting, only, changes, importance, weights in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_method_tested_two_problems`

- Preferred role: `method`
- Cue keywords: `method, tested, two, problems`
- Narration: The method is tested on two problems.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_method_tested_two_problems" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, tested, two, problems in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_first_gaussian_toy_truth_standard`

- Preferred role: `method`
- Cue keywords: `first, gaussian, toy, truth, standard, normal, generation, shifted, mean, minus`
- Narration: First, a Gaussian toy: the truth is a standard normal, the generation is shifted to mean minus one-half, and the detector adds wide Gaussian noise, with a million samples split three to one for training and testing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_first_gaussian_toy_truth_standard" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, gaussian, toy, truth, standard, normal in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_because_gaussian_only_finitely_many`

- Preferred role: `content`
- Cue keywords: `because, gaussian, only, finitely, many, moments, unfolding, its, moments, equivalent`
- Narration: Because a Gaussian has only finitely many moments, unfolding its moments is equivalent to unfolding the whole density.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_because_gaussian_only_finitely_many" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, gaussian, only, finitely, many, moments in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_second_hadronic_jets_simulated_lhc`

- Preferred role: `content`
- Cue keywords: `second, hadronic, jets, simulated, lhc, collisions, jet, width, observable, drawn`
- Narration: Second, hadronic jets from simulated LHC collisions, using the jet width observable, drawn from the same Pythia and Herwig plus Delphes datasets used in the OmniFold paper, where one simulation stands in for data and the other for the synthetic reference.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_second_hadronic_jets_simulated_lhc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, hadronic, jets, simulated, lhc, collisions in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_strong_both_tasks_gaussian`

- Preferred role: `method`
- Cue keywords: `results, strong, both, tasks, gaussian, example, loss, function, peaks, exactly`
- Narration: The results are strong on both tasks. For the Gaussian example, the loss function peaks exactly at the true mean, confirming the method recovers the right answer, and the discriminator converges within about ten epochs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_results_strong_both_tasks_gaussian" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, strong, both, tasks, gaussian, example in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_jet_width_team_unfolds_first`

- Preferred role: `content`
- Cue keywords: `jet, width, team, unfolds, first, second, moments, simultaneously`
- Narration: For the jet width, the team unfolds the first and second moments simultaneously.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_jet_width_team_unfolds_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords jet, width, team, unfolds, first, second in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_scanning_loss_function_candidate_mom`

- Preferred role: `method`
- Cue keywords: `scanning, loss, function, candidate, moment, produces, curves, whose, peaks, land`
- Narration: Scanning the loss as a function of each candidate moment produces curves whose peaks land on the true values, with a mean absolute error of two hundredths of a percent or better.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_scanning_loss_function_candidate_mom" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords scanning, loss, function, candidate, moment, produces in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_sub_percent_agreement_between_unfold`

- Preferred role: `content`
- Cue keywords: `sub-percent, agreement, between, unfolded, true, moments`
- Narration: That is sub-percent agreement between the unfolded and true moments.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_sub_percent_agreement_between_unfold" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sub-percent, agreement, between, unfolded, true, moments in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_one_instructive_observation_concerns`

- Preferred role: `method`
- Cue keywords: `one, instructive, observation, concerns, limits, unfolding, only, couple, moments`
- Narration: One instructive observation concerns the limits of unfolding only a couple of moments.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_one_instructive_observation_concerns" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, instructive, observation, concerns, limits, unfolding in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_after_moment_unfolding_matches_first`

- Preferred role: `method`
- Cue keywords: `after, moment, unfolding, matches, first, second, moments, jet, width, full`
- Narration: After Moment Unfolding matches the first and second moments of the jet width, the full distributions of truth and reweighted generation still are not statistically identical.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_after_moment_unfolding_matches_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords after, moment, unfolding, matches, first, second in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_reason_simply_higher_moments_remain`

- Preferred role: `content`
- Cue keywords: `reason, simply, higher, moments, remain, relevant, not, part, fit`
- Narration: The reason is simply that higher moments remain relevant and were not part of the fit.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_reason_simply_higher_moments_remain" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reason, simply, higher, moments, remain, relevant in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_expected_behavior_clarifies_techniqu`

- Preferred role: `content`
- Cue keywords: `expected, behavior, clarifies, technique, deliberately, controls, specific, moments, you, ask`
- Narration: This is expected behavior, and it clarifies that the technique deliberately controls the specific moments you ask for, leaving the rest free.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_expected_behavior_clarifies_techniqu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords expected, behavior, clarifies, technique, deliberately, controls in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_unfolded_moments_agree_true_moments`

- Preferred role: `result`
- Cue keywords: `unfolded, moments, agree, true, moments, within, two, hundredths, percent, mean`
- Narration: The unfolded moments agree with the true moments to within two hundredths of a percent mean absolute error.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_unfolded_moments_agree_true_moments" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unfolded, moments, agree, true, moments, within in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_two_moments_jet_width_unfolded`

- Preferred role: `content`
- Cue keywords: `two, moments, jet, width, unfolded, once, discriminator, converges, within, ten`
- Narration: Two moments of the jet width are unfolded at once. The discriminator converges within ten epochs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_two_moments_jet_width_unfolded" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, moments, jet, width, unfolded, once in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_gaussian_study_million_samples_three`

- Preferred role: `content`
- Cue keywords: `gaussian, study, million, samples, three-to-one, train-test, split, entire, set, notebooks`
- Narration: The Gaussian study uses a million samples with a three-to-one train-test split, and the entire set of notebooks reproduces in under five minutes on a single Nvidia RTX6000 GPU.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_gaussian_study_million_samples_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gaussian, study, million, samples, three-to-one, train-test in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_you_unfold_detector_effects`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, you, unfold, detector, effects, directly, level, moments, without, ever`
- Narration: The takeaway is that you can unfold detector effects directly at the level of moments, without ever binning the data.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_you_unfold_detector_effects" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, you, unfold, detector, effects, directly in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_moment_unfolding_does_gan_like_gener`

- Preferred role: `content`
- Cue keywords: `moment, unfolding, does, gan-like, generator, whose, parameters, moments, trains, only`
- Narration: Moment Unfolding does this with a GAN-like generator whose parameters are the moments, trains only once rather than iterating, and recovers the true moments to better than a hundredth of a percent on realistic LHC jet simulations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_moment_unfolding_does_gan_like_gener" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords moment, unfolding, does, gan-like, generator, whose in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_because_algorithm_agnostic_dataset_s`

- Preferred role: `content`
- Cue keywords: `because, algorithm, agnostic, dataset, same, idea, could, carry, over, deconvolution`
- Narration: Because the algorithm is agnostic to the dataset, the same idea could carry over to deconvolution problems well beyond particle physics.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_because_algorithm_agnostic_dataset_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, algorithm, agnostic, dataset, same, idea in title/desc so the matcher can verify semantic overlap.
