# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_conditional_matrix_flows_gaussian_gr`

- Preferred role: `content`
- Cue keywords: `conditional, matrix, flows, gaussian, graphical, models, university, basel, unifies, sparse`
- Narration: Conditional Matrix Flows for Gaussian Graphical Models, from the University of Basel, unifies sparse network inference.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_conditional_matrix_flows_gaussian_gr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords conditional, matrix, flows, gaussian, graphical, models in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_one_trained_matrix_normalizing_flow`

- Preferred role: `method`
- Cue keywords: `one, trained, matrix, normalizing, flow, delivers, full, bayesian, posterior, every`
- Narration: With one trained matrix normalizing flow it delivers the full Bayesian posterior for every regularization strength and every l-q pseudo-norm, the marginal likelihood for model selection, and the frequentist solution path through simulated annealing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_one_trained_matrix_normalizing_flow" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, trained, matrix, normalizing, flow, delivers in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_gaussian_graphical_models_read_condi`

- Preferred role: `content`
- Cue keywords: `gaussian, graphical, models, read, conditional, independence, precision, matrix, inverse, covariance`
- Narration: Gaussian Graphical Models read conditional independence from the precision matrix, the inverse covariance: a zero entry means two variables are conditionally independent, so a sparse precision matrix recovers the network.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_gaussian_graphical_models_read_condi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gaussian, graphical, models, read, conditional, independence in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_ideal_l_zero_penalty_counts_edges`

- Preferred role: `content`
- Cue keywords: `ideal, l-zero, penalty, counts, edges, combinatorial, intractable`
- Narration: The ideal l-zero penalty that counts edges is combinatorial and intractable.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_ideal_l_zero_penalty_counts_edges" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ideal, l-zero, penalty, counts, edges, combinatorial in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_sub_l_one_pseudo_norms_approximate_w`

- Preferred role: `method`
- Cue keywords: `sub-l-one, pseudo-norms, approximate, well, but, non-convex, most, methods, retreat, convex`
- Narration: Sub-l-one pseudo-norms approximate it well but are non-convex, so most methods retreat to the convex l-one norm, which over-shrinks, especially when variables outnumber samples.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_sub_l_one_pseudo_norms_approximate_w" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sub-l-one, pseudo-norms, approximate, well, but, non-convex in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_two_camps_exist_frequentist_graphica`

- Preferred role: `content`
- Cue keywords: `two, camps, exist, frequentist, graphical, lasso, traces, whole, solution, path`
- Narration: Two camps exist. The frequentist Graphical Lasso traces the whole solution path as lambda varies, but returns only point estimates.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_two_camps_exist_frequentist_graphica" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, camps, exist, frequentist, graphical, lasso in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_bayesian_graphical_lasso_gives_full`

- Preferred role: `content`
- Cue keywords: `bayesian, graphical, lasso, gives, full, posterior, marginal, likelihood, but, relies`
- Narration: The Bayesian Graphical Lasso gives a full posterior and a marginal likelihood, but relies on Gibbs samplers that mix poorly and must restart for every lambda.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_bayesian_graphical_lasso_gives_full" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords bayesian, graphical, lasso, gives, full, posterior in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_variational_inference_could_bridge_t`

- Preferred role: `content`
- Cue keywords: `variational, inference, could, bridge, them, yet, usual, mean-field, trick, assumes`
- Narration: Variational inference could bridge them, yet the usual mean-field trick assumes independence, exactly what a graphical model seeks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_variational_inference_could_bridge_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords variational, inference, could, bridge, them, yet in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_need_family_respects_dependence_flex`

- Preferred role: `content`
- Cue keywords: `need, family, respects, dependence, flexes, across, lambda, norm`
- Narration: We need a family that respects dependence and flexes across lambda and the norm.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_need_family_respects_dependence_flex" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords need, family, respects, dependence, flexes, across in title/desc so the matcher can verify semantic overlap.

## Slide 04: method

Heading: Method

### Cue 1: `cue_s04_c1_flow_works_cholesky_factorization_an`

- Preferred role: `content`
- Cue keywords: `flow, works, cholesky, factorization, any, positive-definite, matrix, times, l-transpose, d-dimensional`
- Narration: The flow works on the Cholesky factorization. Any positive-definite matrix is L times L-transpose, so a d-dimensional precision matrix needs only d times d plus one, over two, numbers.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_flow_works_cholesky_factorization_an" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords flow, works, cholesky, factorization, any, positive-definite in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_flow_pushes_base_vector_through`

- Preferred role: `content`
- Cue keywords: `flow, pushes, base, vector, through, sum-of-sigmoids, layers, reshapes, triangular, matrix`
- Narration: The flow pushes a base vector through Sum-of-Sigmoids layers, reshapes it into a triangular matrix, forces the diagonal positive with a softplus, and takes the Cholesky product, so every output is a valid precision matrix with cheap Jacobians.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_flow_pushes_base_vector_through" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords flow, pushes, base, vector, through, sum-of-sigmoids in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_hypernetwork_feeds_lambda_minimizes`

- Preferred role: `method`
- Cue keywords: `hypernetwork, feeds, lambda, minimizes, divergence, unnormalized, posterior, under, generalized-normal, prior`
- Narration: A hypernetwork feeds in lambda and q, and training minimizes the KL divergence to the unnormalized posterior under a generalized-Normal prior.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_hypernetwork_feeds_lambda_minimizes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hypernetwork, feeds, lambda, minimizes, divergence, unnormalized in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_lasso_appears_equals_one_ridge`

- Preferred role: `result`
- Cue keywords: `lasso, appears, equals, one, ridge, equals, two, smaller, reaches, sub-l-one`
- Narration: Lasso appears at q equals one, Ridge at q equals two, and smaller q reaches the sub-l-one regime.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_lasso_appears_equals_one_ridge" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasso, appears, equals, one, ridge, equals in title/desc so the matcher can verify semantic overlap.

## Slide 05: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s05_c1_experiments_two_types`

- Preferred role: `content`
- Cue keywords: `experiments, two, types`
- Narration: Experiments use two data types.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_experiments_two_types" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, two, types in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_first_synthetic_sparse_precision_mat`

- Preferred role: `result`
- Cue keywords: `first, synthetic, sparse, precision, matrices, scikit-learn, small, fifteen-by-fifteen, case, visualize`
- Narration: First, synthetic sparse precision matrices from Scikit-learn: a small fifteen-by-fifteen case to visualize posteriors, and a thirty-dimensional setting with fifteen to forty-five samples for edge recovery, averaged over ten ground-truth matrices.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c2_first_synthetic_sparse_precision_mat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, synthetic, sparse, precision, matrices, scikit-learn in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_second_real_colorectal_cancer_datase`

- Preferred role: `figure`
- Cue keywords: `second, real, colorectal-cancer, dataset, six, clinical, variables, three, hundred, twelve`
- Narration: Second, a real colorectal-cancer dataset with six clinical variables and three hundred twelve gene-expression measurements across one hundred ninety patients, inferring only the relevant sub-blocks of the precision matrix.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c3_second_real_colorectal_cancer_datase" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, real, colorectal-cancer, dataset, six, clinical in title/desc so the matcher can verify semantic overlap.

## Slide 06: key-result

Heading: Key Result

### Cue 1: `cue_s06_c1_one_does_work_many_trained`

- Preferred role: `method`
- Cue keywords: `one, does, work, many, trained, once, flow, reconstructs, frequentist, solution`
- Narration: One model does the work of many. Trained once, the flow reconstructs the frequentist solution path with a mean squared error of just zero point zero five two.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_one_does_work_many_trained" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, does, work, many, trained, once in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_when_samples_scarce_sub_l_one_pseudo`

- Preferred role: `result`
- Cue keywords: `when, samples, scarce, sub-l-one, pseudo-norms, clearly, beat, bayesian, graphical, lasso`
- Narration: When samples are scarce, the sub-l-one pseudo-norms clearly beat the Bayesian Graphical Lasso, and the gain grows as q approaches zero.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_when_samples_scarce_sub_l_one_pseudo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, samples, scarce, sub-l-one, pseudo-norms, clearly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_against_frequentist_competitors_wins`

- Preferred role: `result`
- Cue keywords: `against, frequentist, competitors, wins, every, sample, size, most, fifteen, samples`
- Narration: Against frequentist competitors it wins at every sample size, most at fifteen samples.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_against_frequentist_competitors_wins" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords against, frequentist, competitors, wins, every, sample in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_its_selection_picks_lambda_three`

- Preferred role: `method`
- Cue keywords: `its, selection, picks, lambda, three, point, five, two, matching, cross-validated`
- Narration: Its model selection picks a lambda of three point five two, matching the cross-validated Graphical Lasso value of three point three six.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_its_selection_picks_lambda_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, selection, picks, lambda, three, point in title/desc so the matcher can verify semantic overlap.

## Slide 07: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s07_c1_key_study_varies_pseudo_norm_exponen`

- Preferred role: `content`
- Cue keywords: `key, study, varies, pseudo-norm, exponent`
- Narration: The key study varies the pseudo-norm exponent q.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_key_study_varies_pseudo_norm_exponen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, study, varies, pseudo-norm, exponent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_shrinks_one_toward_quarter_posterior`

- Preferred role: `content`
- Cue keywords: `shrinks, one, toward, quarter, posterior, median, precision, entry, pulled, less`
- Narration: As q shrinks from one toward a quarter, the posterior median for a precision entry is pulled less toward zero, reducing over-shrinkage as promised.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_shrinks_one_toward_quarter_posterior" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords shrinks, one, toward, quarter, posterior, median in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_lambda_zero_point_three_ninety_five`

- Preferred role: `content`
- Cue keywords: `lambda, zero, point, three, ninety-five, percent, credible, interval, excludes, zero`
- Narration: At a lambda of zero point three the ninety-five percent credible interval excludes zero for q below one, while the Bayesian Lasso at q equals one still includes zero and would drop the edge.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_lambda_zero_point_three_ninety_five" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lambda, zero, point, three, ninety-five, percent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_second_knob_temperature_slides_bayes`

- Preferred role: `content`
- Cue keywords: `second, knob, temperature, slides, bayesian, regime, frequentist, path`
- Narration: A second knob, the temperature, slides the model from the Bayesian regime to the frequentist path.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_second_knob_temperature_slides_bayes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, knob, temperature, slides, bayesian, regime in title/desc so the matcher can verify semantic overlap.

## Slide 08: takeaway

Heading: Takeaway

### Cue 1: `cue_s08_c1_takeaway_one_normalizing_flow_replac`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, one, normalizing, flow, replace, toolbox`
- Narration: The takeaway: one normalizing flow can replace a toolbox.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s08_c1_takeaway_one_normalizing_flow_replac" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, one, normalizing, flow, replace, toolbox in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_built_positive_definite_matrices_con`

- Preferred role: `method`
- Cue keywords: `built, positive-definite, matrices, conditioned, both, shrinkage, strength, norm, exponent, delivers`
- Narration: Built on positive-definite matrices and conditioned on both the shrinkage strength and the norm exponent, it delivers Bayesian posteriors, marginal-likelihood model selection, and the frequentist solution path, for every setting and every l-q norm, including the non-convex sub-l-one region others avoid.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_built_positive_definite_matrices_con" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords built, positive-definite, matrices, conditioned, both, shrinkage in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_edge_recovery_improves_where_hardest`

- Preferred role: `content`
- Cue keywords: `edge, recovery, improves, where, hardest, sampling, runs, hundreds, times, faster`
- Narration: Edge recovery improves where it is hardest, and sampling runs hundreds of times faster than Gibbs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_edge_recovery_improves_where_hardest" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords edge, recovery, improves, where, hardest, sampling in title/desc so the matcher can verify semantic overlap.
