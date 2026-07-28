# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_schr_dinger_bridges_connect_two`

- Preferred role: `method`
- Cue keywords: `schr, dinger, bridges, connect, two, probability, distributions, diffusion, process, but`
- Narration: Schrödinger Bridges connect two probability distributions with a diffusion process, but nearly every existing solver is heavy: it stacks several neural networks, needs adversarial min-max training, and can take hours on a GPU.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_schr_dinger_bridges_connect_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords schr, dinger, bridges, connect, two, probability in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_introduces_lightsb_lightweight_schr`

- Preferred role: `content`
- Cue keywords: `introduces, lightsb, lightweight, schr, dinger, bridge, solver`
- Narration: This paper introduces LightSB, a lightweight Schrödinger Bridge solver.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_introduces_lightsb_lightweight_schr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, lightsb, lightweight, schr, dinger, bridge in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_parameterizing_schr_dinger_potential`

- Preferred role: `content`
- Cue keywords: `parameterizing, schr, dinger, potential, gaussian, mixture, treating, its, logarithm, energy`
- Narration: By parameterizing the Schrödinger potential as a Gaussian mixture and treating its logarithm as an energy function, LightSB turns the problem into one simple, non-minimax optimization objective with closed-form components.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_parameterizing_schr_dinger_potential" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords parameterizing, schr, dinger, potential, gaussian, mixture in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_result_solves_schr_dinger_bridges`

- Preferred role: `result`
- Cue keywords: `result, solves, schr, dinger, bridges, moderate, dimensions, minutes, cpu, painful`
- Narration: The result solves Schrödinger Bridges in moderate dimensions in minutes on a CPU, with no painful hyperparameter tuning, and is provably a universal approximator of Schrödinger Bridges.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_result_solves_schr_dinger_bridges" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, solves, schr, dinger, bridges, moderate in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_schr_dinger_bridge_problem_asks`

- Preferred role: `method`
- Cue keywords: `schr, dinger, bridge, problem, asks, diffusion, process, between, two, given`
- Narration: The Schrödinger Bridge problem asks for the diffusion process between two given distributions that stays as close as possible to a reference Wiener process.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_schr_dinger_bridge_problem_asks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords schr, dinger, bridge, problem, asks, diffusion in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_dynamic_version_entropic_optimal_tra`

- Preferred role: `content`
- Cue keywords: `dynamic, version, entropic, optimal, transport, underpins, applications, single-cell, biology, image`
- Narration: It is the dynamic version of entropic optimal transport, and it underpins applications from single-cell biology to image translation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_dynamic_version_entropic_optimal_tra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dynamic, version, entropic, optimal, transport, underpins in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_trouble_almost_all_existing_solvers`

- Preferred role: `content`
- Cue keywords: `trouble, almost, all, existing, solvers, heavy-weighted, they, parameterize, solution, several`
- Narration: The trouble is that almost all existing solvers are heavy-weighted. They parameterize the solution with several large neural networks and require complex, often adversarial optimization.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_trouble_almost_all_existing_solvers" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trouble, almost, all, existing, solvers, heavy-weighted in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_result_field_lacks_simple_principled`

- Preferred role: `method`
- Cue keywords: `result, field, lacks, simple, principled, baseline, kind, go-to, method, k-means`
- Narration: As a result, the field lacks a simple, principled baseline, the kind of go-to method that k-means is for clustering or Sinkhorn is for discrete optimal transport.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_result_field_lacks_simple_principled" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, field, lacks, simple, principled, baseline in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_consider_researcher_who_simply_wants`

- Preferred role: `content`
- Cue keywords: `consider, researcher, who, simply, wants, compute, entropic, optimal, transport, schr`
- Narration: Consider a researcher who simply wants to compute an entropic optimal transport or Schrödinger Bridge between two moderate-dimensional datasets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_consider_researcher_who_simply_wants" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords consider, researcher, who, simply, wants, compute in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_today_means_adopting_solver_iterativ`

- Preferred role: `method`
- Cue keywords: `today, means, adopting, solver, iterative, proportional, fitting, steps, min-max, optimization`
- Narration: Today, that means adopting a solver with iterative proportional fitting steps, or min-max optimization, or simulation of the full stochastic process at every training step.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_today_means_adopting_solver_iterativ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords today, means, adopting, solver, iterative, proportional in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_these_solvers_demand_careful_neural`

- Preferred role: `content`
- Cue keywords: `these, solvers, demand, careful, neural, network, design, run, hours, gpus`
- Narration: These solvers demand careful neural network design, run for hours on GPUs, and are sensitive to many hyperparameters.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_these_solvers_demand_careful_neural" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, solvers, demand, careful, neural, network in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_yet_many_real_settings_user`

- Preferred role: `content`
- Cue keywords: `yet, many, real, settings, user, only, cares, about, where, trajectories`
- Narration: Yet in many real settings, the user only cares about where the trajectories end, that is, the conditional plan. This mismatch, heavy machinery for a modest goal, is exactly the gap LightSB is built to close.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_yet_many_real_settings_user" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yet, many, real, settings, user, only in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions_first_intr`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions, first, introduces, lightsb, lightweight, solver, combines, two`
- Narration: The paper makes three contributions. First, it introduces LightSB, a lightweight solver that combines two recent ideas: parameterizing the Schrödinger potential with sum-exp quadratic, that is Gaussian mixture, functions, and viewing the log-potential as an energy function.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions_first_intr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions, first, introduces, lightsb in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_together_these_yield_single_non_mini`

- Preferred role: `content`
- Cue keywords: `together, these, yield, single, non-minimax, simulation-free, optimization, objective, closed-form, expressions`
- Narration: Together these yield a single, non-minimax, simulation-free optimization objective with closed-form expressions for the plan and the drift.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_together_these_yield_single_non_mini" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, these, yield, single, non-minimax, simulation-free in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_authors_prove_gaussian_mixtur`

- Preferred role: `result`
- Cue keywords: `second, authors, prove, gaussian-mixture, solver, universal, approximator, schr, dinger, bridges`
- Narration: Second, the authors prove that this Gaussian-mixture solver is a universal approximator of Schrödinger Bridges, which they note is the first ever such result.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c3_second_authors_prove_gaussian_mixtur" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, authors, prove, gaussian-mixture, solver, universal in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_they_analyze_generalization_er`

- Preferred role: `result`
- Cue keywords: `third, they, analyze, generalization, error, show, converges, standard, parametric, rate`
- Narration: Third, they analyze the generalization error and show it converges at the standard parametric rate as sample size grows.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_third_they_analyze_generalization_er" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, they, analyze, generalization, error, show in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_lightsb_starts_goal_minimizing_kullb`

- Preferred role: `content`
- Cue keywords: `lightsb, starts, goal, minimizing, kullback-leibler, divergence, between, true, entropic, optimal`
- Narration: LightSB starts from the goal of minimizing the Kullback-Leibler divergence between the true entropic optimal transport plan and a parameterized plan. The obstacle is that we do not know the true plan. The key move is to exploit the known form of that plan and parameterize only the adjusted Schrödinger potential.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_lightsb_starts_goal_minimizing_kullb" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lightsb, starts, goal, minimizing, kullback-leibler, divergence in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_authors_choose_unnormalized_gaussian`

- Preferred role: `method`
- Cue keywords: `authors, choose, unnormalized, gaussian, mixture, potential, under, choice, two, things`
- Narration: The authors choose an unnormalized Gaussian mixture for this potential. Under this choice, two things become tractable in closed form: the conditional distributions of the plan, and the normalization constant.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_authors_choose_unnormalized_gaussian" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, choose, unnormalized, gaussian, mixture, potential in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_proposition_3_1_rewrites_objective_s`

- Preferred role: `content`
- Cue keywords: `proposition, 3.1, rewrites, objective, simple, difference, two, expectations, log, normalization`
- Narration: Proposition 3.1 rewrites the KL objective as a simple difference of two expectations, of the log normalization under the source and the log potential under the target, which can be estimated by Monte Carlo and optimized with ordinary stochastic gradient descent.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_proposition_3_1_rewrites_objective_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords proposition, 3.1, rewrites, objective, simple, difference in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_min_max_iterative_proportional_fitti`

- Preferred role: `method`
- Cue keywords: `min-max, iterative, proportional, fitting, simulation, trajectories, during, once, trained, same`
- Narration: No min-max, no iterative proportional fitting, and no simulation of trajectories during training. Once trained, the same potential gives a closed-form drift, so the full bridge process can be reconstructed directly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_min_max_iterative_proportional_fitti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords min-max, iterative, proportional, fitting, simulation, trajectories in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_solver_tested_across_four_kinds`

- Preferred role: `content`
- Cue keywords: `solver, tested, across, four, kinds, first, two-dimensional, gaussian, swiss-roll, toy`
- Narration: The solver is tested across four kinds of data. First, a two-dimensional Gaussian to Swiss-roll toy, which visualizes how the noise level epsilon shapes the trajectories.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_solver_tested_across_four_kinds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords solver, tested, across, four, kinds, first in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_second_recent_high_dimensional_entro`

- Preferred role: `method`
- Cue keywords: `second, recent, high-dimensional, entropic, optimal, transport, benchmark, known, ground-truth, plans`
- Narration: Second, a recent high-dimensional entropic optimal transport benchmark with known ground-truth plans, spanning dimensions from two to one hundred twenty-eight and several values of epsilon.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_second_recent_high_dimensional_entro" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, recent, high-dimensional, entropic, optimal, transport in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_third_msci_single_cell_dataset_kaggl`

- Preferred role: `content`
- Cue keywords: `third, msci, single-cell, dataset, kaggle, competition, cells, four, human, donors`
- Narration: Third, the MSCI single-cell dataset from a Kaggle competition, with cells from four human donors at four time points, projected by PCA to fifty, one hundred, and one thousand dimensions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_third_msci_single_cell_dataset_kaggl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, msci, single-cell, dataset, kaggle, competition in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_fourth_unpaired_image_translation_ff`

- Preferred role: `method`
- Cue keywords: `fourth, unpaired, image, translation, ffhq, faces, performed, five-hundred-twelve-dimensional, latent, space`
- Narration: And fourth, unpaired image translation on FFHQ faces, performed in the five-hundred-twelve-dimensional latent space of a pretrained ALAE autoencoder.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_fourth_unpaired_image_translation_ff" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, unpaired, image, translation, ffhq, faces in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_show_both_accuracy_speed`

- Preferred role: `result`
- Cue keywords: `results, show, both, accuracy, speed`
- Narration: The results show both accuracy and speed.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_results_show_both_accuracy_speed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, show, both, accuracy, speed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_entropic_optimal_transport_benchmark`

- Preferred role: `result`
- Cue keywords: `entropic, optimal, transport, benchmark, where, ground, truth, known, lightsb, reduces`
- Narration: On the entropic optimal transport benchmark, where the ground truth is known, LightSB reduces the conditional Bures-Wasserstein error to well under one percent, often around a few hundredths, while the best previous solver sits between about one and eighteen percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_entropic_optimal_transport_benchmark" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords entropic, optimal, transport, benchmark, where, ground in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_msci_single_cell_task_lightsb_reache`

- Preferred role: `method`
- Cue keywords: `msci, single-cell, task, lightsb, reaches, energy, distance, comparable, strong, gpu`
- Narration: On the MSCI single-cell task, LightSB reaches energy distance comparable to strong GPU baselines, but it trains in roughly one to two and a half minutes on just four CPU cores, whereas competing continuous solvers need tens of minutes to over an hour on a V100 GPU.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_msci_single_cell_task_lightsb_reache" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords msci, single-cell, task, lightsb, reaches, energy in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_ffhq_faces_performs_realistic_male_t`

- Preferred role: `content`
- Cue keywords: `ffhq, faces, performs, realistic, male-to-female, child-to-adult, translation, five-hundred-twelve-dimensional, latent, space`
- Narration: And on FFHQ faces, it performs realistic male-to-female and child-to-adult translation in a five-hundred-twelve-dimensional latent space, converging in under a minute on CPU.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_ffhq_faces_performs_realistic_male_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ffhq, faces, performs, realistic, male-to-female, child-to-adult in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_understand_role_noise_parameter_epsi`

- Preferred role: `method`
- Cue keywords: `understand, role, noise, parameter, epsilon, authors, map, two-dimensional, gaussian, swiss`
- Narration: To understand the role of the noise parameter epsilon, the authors map a two-dimensional Gaussian to a Swiss roll while sweeping epsilon across three values.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_understand_role_noise_parameter_epsi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords understand, role, noise, parameter, epsilon, authors in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_when_epsilon_small_learned_process`

- Preferred role: `method`
- Cue keywords: `when, epsilon, small, learned, process, nearly, deterministic, its, trajectories, almost`
- Narration: When epsilon is small, the learned process is nearly deterministic and its trajectories are almost straight lines.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_when_epsilon_small_learned_process" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, epsilon, small, learned, process, nearly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_epsilon_grows_trajectories_become_mo`

- Preferred role: `method`
- Cue keywords: `epsilon, grows, trajectories, become, more, volatile, conditional, distributions, endpoint, spread`
- Narration: As epsilon grows, the trajectories become more volatile and the conditional distributions at the endpoint spread out. This matches the theory: epsilon controls the stochasticity of the bridge.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_epsilon_grows_trajectories_become_mo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords epsilon, grows, trajectories, become, more, volatile in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_benchmark_results_also_reveal_lights`

- Preferred role: `method`
- Cue keywords: `benchmark, results, also, reveal, lightsb, gains, most, when, target, distributions`
- Narration: The benchmark results also reveal that LightSB gains the most when the target distributions align with its Gaussian-mixture inductive bias, while remaining accurate across the tested dimensions and noise levels.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_benchmark_results_also_reveal_lights" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords benchmark, results, also, reveal, lightsb, gains in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_lightsb`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact, lightsb, converges, under, one, minute, four`
- Narration: A few numbers capture the impact. LightSB converges in under one minute on four CPU cores for the five-hundred-twelve-dimensional image translation task, with no GPU at all.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_lightsb" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, lightsb, converges in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_hardest_single_cell_setting_one_thou`

- Preferred role: `result`
- Cue keywords: `hardest, single-cell, setting, one, thousand, dimensions, reaches, energy, distance, one`
- Narration: On the hardest single-cell setting, one thousand dimensions, it reaches an energy distance of one point two seven in one hundred forty-six seconds on CPU, matching a minimax GPU solver that needs seventy-one minutes on a V100.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_hardest_single_cell_setting_one_thou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hardest, single-cell, setting, one, thousand, dimensions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_entropic_transport_benchmark_its_con`

- Preferred role: `result`
- Cue keywords: `entropic, transport, benchmark, its, conditional, error, drops, little, three, hundredths`
- Narration: On the entropic transport benchmark, its conditional error drops to as little as three hundredths of a percent, against best-baseline errors ranging from about one to eighteen percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_entropic_transport_benchmark_its_con" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords entropic, transport, benchmark, its, conditional, error in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_all_comes_theoretical_guarantee_ligh`

- Preferred role: `result`
- Cue keywords: `all, comes, theoretical, guarantee, lightsb, universal, approximator, schr, dinger, bridges`
- Narration: And all of this comes with a theoretical guarantee: LightSB is a universal approximator of Schrödinger Bridges, with generalization error that vanishes at the standard parametric rate.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_all_comes_theoretical_guarantee_ligh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, comes, theoretical, guarantee, lightsb, universal in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_schr_dinger_bridge`

- Preferred role: `content`
- Cue keywords: `lasting, message, schr, dinger, bridge, solver, does, not, heavy`
- Narration: The lasting message is that a Schrödinger Bridge solver does not have to be heavy.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lasting_message_schr_dinger_bridge" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, schr, dinger, bridge, solver in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_parameterizing_transport_potential_g`

- Preferred role: `method`
- Cue keywords: `parameterizing, transport, potential, gaussian, mixture, optimizing, single, straightforward, objective, lightsb`
- Narration: By parameterizing the transport potential as a Gaussian mixture and optimizing a single, straightforward objective, LightSB solves entropic optimal transport and Schrödinger Bridges in minutes on a CPU, without adversarial training or process simulation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_parameterizing_transport_potential_g" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords parameterizing, transport, potential, gaussian, mixture, optimizing in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_matches_outperforms_much_heavier_gpu`

- Preferred role: `result`
- Cue keywords: `matches, outperforms, much, heavier, gpu-based, solvers, comes, universal-approximation, guarantee, easy`
- Narration: It matches or outperforms much heavier GPU-based solvers, comes with a universal-approximation guarantee, and is easy to use.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c3_matches_outperforms_much_heavier_gpu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords matches, outperforms, much, heavier, gpu-based, solvers in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_short_lightsb_positioned_simple_reli`

- Preferred role: `content`
- Cue keywords: `short, lightsb, positioned, simple, reliable, baseline, schr, dinger, bridge, field`
- Narration: In short, LightSB is positioned to be the simple, reliable baseline that the Schrödinger Bridge field has been missing.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c4_short_lightsb_positioned_simple_reli" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords short, lightsb, positioned, simple, reliable, baseline in title/desc so the matcher can verify semantic overlap.
