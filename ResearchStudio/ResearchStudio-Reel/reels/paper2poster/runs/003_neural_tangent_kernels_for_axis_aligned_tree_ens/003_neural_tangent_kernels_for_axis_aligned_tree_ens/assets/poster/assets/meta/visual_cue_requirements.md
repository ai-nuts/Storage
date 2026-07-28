# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_soft_tree_ensembles_gradient_trained`

- Preferred role: `method`
- Cue keywords: `soft, tree, ensembles, gradient-trained, decision, trees, rival, neural, networks, tabular`
- Narration: Soft tree ensembles are gradient-trained decision trees that rival neural networks on tabular data, yet their training has lacked theory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_soft_tree_ensembles_gradient_trained" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords soft, tree, ensembles, gradient-trained, decision, trees in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_iclr_2022_introduces_tree_neural`

- Preferred role: `content`
- Cue keywords: `iclr, 2022, introduces, tree, neural, tangent, kernel, tntk, describing, ensemble`
- Narration: This ICLR 2022 paper introduces the Tree Neural Tangent Kernel, or TNTK, describing an ensemble of infinitely many soft trees.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_iclr_2022_introduces_tree_neural" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords iclr, 2022, introduces, tree, neural, tangent in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_prove_global_convergence_sho`

- Preferred role: `method`
- Cue keywords: `authors, prove, global, convergence, show, oblivious, trees, match, ordinary, ones`
- Narration: With it, the authors prove global training convergence, show oblivious trees match ordinary ones, and reveal that very deep trees degenerate into a flat kernel, all validated on ninety datasets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_authors_prove_global_convergence_sho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, prove, global, convergence, show, oblivious in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_tree_ensembles_neural_networks_two`

- Preferred role: `content`
- Cue keywords: `tree, ensembles, neural, networks, two, most, widely, used, families`
- Narration: Tree ensembles and neural networks are two of the most widely used model families.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_tree_ensembles_neural_networks_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tree, ensembles, neural, networks, two, most in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_soft_tree_decision_tree_whose`

- Preferred role: `guidance`
- Cue keywords: `soft, tree, decision, tree, whose, splitting, rules, made, differentiable, whole`
- Narration: A soft tree is a decision tree whose splitting rules are made differentiable, so the whole model trains by gradient descent instead of greedy search.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s02_c2_soft_tree_decision_tree_whose" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords soft, tree, decision, tree, whose, splitting in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_ensembles_soft_trees_excel_tabular`

- Preferred role: `content`
- Cue keywords: `ensembles, soft, trees, excel, tabular, practitioners, rely, tricks, like, parameter`
- Narration: Ensembles of soft trees excel on tabular data, and practitioners rely on tricks like parameter sharing, adjusting split hardness, and over-parameterization.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_ensembles_soft_trees_excel_tabular" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ensembles, soft, trees, excel, tabular, practitioners in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_yet_almost_theory_explains_why`

- Preferred role: `content`
- Cue keywords: `yet, almost, theory, explains, why, they, work, fills, gap`
- Narration: Yet almost no theory explains why they work. This paper fills that gap.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_yet_almost_theory_explains_why" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yet, almost, theory, explains, why, they in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_neural_tangent_kernel_become_powerfu`

- Preferred role: `content`
- Cue keywords: `neural, tangent, kernel, become, powerful, tool, understanding, neural, networks, infinitely`
- Narration: The Neural Tangent Kernel has become a powerful tool for understanding neural networks with infinitely many hidden nodes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_neural_tangent_kernel_become_powerfu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neural, tangent, kernel, become, powerful, tool in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_been_derived_multi_layer_perceptrons`

- Preferred role: `content`
- Cue keywords: `been, derived, multi-layer, perceptrons, convolutional, networks, more, yielding, its, own`
- Narration: It has been derived for multi-layer perceptrons, convolutional networks, and more, each yielding its own distinct kernel.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_been_derived_multi_layer_perceptrons" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords been, derived, multi-layer, perceptrons, convolutional, networks in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_but_one_had_derived_ntk`

- Preferred role: `content`
- Cue keywords: `but, one, had, derived, ntk, tree, ensembles`
- Narration: But no one had derived an NTK for tree ensembles.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_but_one_had_derived_ntk" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, one, had, derived, ntk, tree in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_because_soft_trees_inherit_character`

- Preferred role: `method`
- Cue keywords: `because, soft, trees, inherit, characteristics, neural, networks, authors, saw, ntk`
- Narration: Because soft trees inherit characteristics of neural networks, the authors saw the NTK framework as the natural lens, seeking a closed-form kernel for infinitely many soft trees.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_because_soft_trees_inherit_character" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, soft, trees, inherit, characteristics, neural in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_four_contributions`

- Preferred role: `content`
- Cue keywords: `makes, four, contributions`
- Narration: The paper makes four contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_four_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, four, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_derives_tree_neural_tangent`

- Preferred role: `method`
- Cue keywords: `first, derives, tree, neural, tangent, kernel, initialization, infinitely, many, perfect`
- Narration: First, it derives the Tree Neural Tangent Kernel at initialization for infinitely many perfect binary trees of arbitrary depth, and proves the kernel stays essentially constant during training, enabling analysis as kernel regression and a proof of global convergence.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_derives_tree_neural_tangent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, derives, tree, neural, tangent, kernel in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_shows_oblivious_ensembles_whi`

- Preferred role: `guidance`
- Cue keywords: `second, shows, oblivious, ensembles, which, share, splitting, rules, within, depth`
- Narration: Second, it shows oblivious ensembles, which share splitting rules within each depth as in NODE, converge to the very same kernel.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c3_second_shows_oblivious_ensembles_whi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, shows, oblivious, ensembles, which, share in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_characterizes_decision_functio`

- Preferred role: `content`
- Cue keywords: `third, characterizes, decision, function, nearly, linear, basic, case, more, nonlinear`
- Narration: Third, it characterizes the decision function, nearly linear in the basic case and more nonlinear as splits harden. Fourth, it uncovers a degeneracy where deep trees flatten the kernel.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_third_characterizes_decision_functio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, characterizes, decision, function, nearly, linear in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_takes_number_trees_infinity`

- Preferred role: `method`
- Cue keywords: `method, takes, number, trees, infinity`
- Narration: The method takes the number of trees to infinity.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_takes_number_trees_infinity" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, takes, number, trees, infinity in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_perfect_binary_soft_trees_depth`

- Preferred role: `content`
- Cue keywords: `perfect, binary, soft, trees, depth, authors, prove, tree, neural, tangent`
- Narration: For perfect binary soft trees of depth d, the authors prove the Tree Neural Tangent Kernel converges to a deterministic kernel with two parts: one from the inner splitting nodes and one from the leaves.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_perfect_binary_soft_trees_depth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords perfect, binary, soft, trees, depth, authors in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_soft_split_scaled_error_function`

- Preferred role: `result`
- Cue keywords: `soft, split, scaled, error, function, smooth, sigmoid, whose, sharpness, set`
- Narration: The soft split uses a scaled error function, a smooth sigmoid whose sharpness is set by alpha, and its expectations have closed forms, so the kernel is analytic.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_soft_split_scaled_error_function" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords soft, split, scaled, error, function, smooth in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_because_kernel_stays_constant_positi`

- Preferred role: `method`
- Cue keywords: `because, kernel, stays, constant, positive, definite, reduces, kernel, regression, global`
- Narration: Because the kernel stays constant and positive definite, training reduces to kernel regression with global convergence, and the formula is not recursive in depth, so its cost is depth-independent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_because_kernel_stays_constant_positi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, kernel, stays, constant, positive, definite in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_empirical_study_two_kinds`

- Preferred role: `content`
- Cue keywords: `empirical, study, two, kinds`
- Narration: The empirical study uses two kinds of data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_empirical_study_two_kinds" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords empirical, study, two, kinds in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_generalization_authors_run_kernel_re`

- Preferred role: `result`
- Cue keywords: `generalization, authors, run, kernel, regression, tree, ntk, ninety, real-world, datasets`
- Narration: For generalization, the authors run kernel regression with the Tree NTK on ninety real-world datasets, comparing against the kernel of an infinitely wide multi-layer perceptron and the classic radial basis function kernel.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_generalization_authors_run_kernel_re" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords generalization, authors, run, kernel, regression, tree in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_tree_depth_tuned_one_twenty_nine`

- Preferred role: `content`
- Cue keywords: `tree, depth, tuned, one, twenty-nine, split-hardness, parameter, alpha, swept, widely`
- Narration: Tree depth is tuned from one up to twenty-nine, and the split-hardness parameter alpha is swept widely.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_tree_depth_tuned_one_twenty_nine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tree, depth, tuned, one, twenty-nine, split-hardness in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_measuring_computational_cost_they_sy`

- Preferred role: `content`
- Cue keywords: `measuring, computational, cost, they, synthetic, dataset, three, hundred, samples, ten`
- Narration: For measuring computational cost, they use a synthetic dataset of three hundred samples with ten Gaussian features.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_measuring_computational_cost_they_sy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords measuring, computational, cost, they, synthetic, dataset in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_experiments_confirm_every_prediction`

- Preferred role: `method`
- Cue keywords: `experiments, confirm, every, prediction, number, trees, grows, empirical, kernel, converges`
- Narration: The experiments confirm every prediction. As the number of trees grows, the empirical kernel converges to the closed-form Tree NTK, and training dynamics match kernel regression.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_experiments_confirm_every_prediction" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, confirm, every, prediction, number, trees in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_making_trees_deeper_first_improves`

- Preferred role: `result`
- Cue keywords: `making, trees, deeper, first, improves, hurts, accuracy, exactly, predicted, degeneracy`
- Narration: Making trees deeper first improves then hurts accuracy, exactly the predicted degeneracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_making_trees_deeper_first_improves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords making, trees, deeper, first, improves, hurts in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_ninety_datasets_multi_layer_perceptr`

- Preferred role: `result`
- Cue keywords: `ninety, datasets, multi-layer, perceptron, kernel, wins, average, but, tree, kernel`
- Narration: On the ninety datasets the multi-layer perceptron kernel wins on average, but the tree kernel is better on more than thirty percent of them, where the tree inductive bias fits.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_ninety_datasets_multi_layer_perceptr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ninety, datasets, multi-layer, perceptron, kernel, wins in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_because_its_cost_never_grows`

- Preferred role: `content`
- Cue keywords: `because, its, cost, never, grows, depth, far, faster, compute`
- Narration: And because its cost never grows with depth, it is far faster to compute.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_because_its_cost_never_grows" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, its, cost, never, grows, depth in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_two_ablations_central`

- Preferred role: `content`
- Cue keywords: `two, ablations, central`
- Narration: Two ablations are central.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_two_ablations_central" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, ablations, central in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_sweeping_split_hardness_parameter_al`

- Preferred role: `result`
- Cue keywords: `sweeping, split-hardness, parameter, alpha, shows, harder, splits, give, better, dataset-wise`
- Narration: Sweeping the split-hardness parameter alpha shows harder splits give better dataset-wise win rates against the MLP kernel, climbing from about fourteen percent when splits are soft to nearly thirty-five percent at the hardest, all above the radial basis function baseline.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_sweeping_split_hardness_parameter_al" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sweeping, split-hardness, parameter, alpha, shows, harder in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_sweeping_tree_depth_reproduces_degen`

- Preferred role: `content`
- Cue keywords: `sweeping, tree, depth, reproduces, degeneracy, story`
- Narration: Sweeping tree depth reproduces the degeneracy story.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_sweeping_tree_depth_reproduces_degen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sweeping, tree, depth, reproduces, degeneracy, story in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_authors_also_verify_empirically_obli`

- Preferred role: `content`
- Cue keywords: `authors, also, verify, empirically, oblivious, trees, used, node, induce, same`
- Narration: The authors also verify empirically that oblivious trees, as used by NODE, induce the same kernel as ordinary soft trees.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_authors_also_verify_empirically_obli" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, verify, empirically, oblivious, trees in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_across_ninety_real_world_datasets_tr`

- Preferred role: `content`
- Cue keywords: `across, ninety, real-world, datasets, tree, kernel, beats, multi-layer, perceptron, kernel`
- Narration: Across ninety real-world datasets, the tree kernel beats the multi-layer perceptron kernel on more than thirty percent, peaking near thirty-five percent when splits are hard, versus under twelve percent for the radial basis function kernel.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_across_ninety_real_world_datasets_tr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, ninety, real-world, datasets, tree, kernel in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_most_striking_tree_kernel_cost`

- Preferred role: `method`
- Cue keywords: `most, striking, tree, kernel, cost, independent, tree, depth, while, mlp`
- Narration: Most striking, the tree kernel's cost is independent of tree depth, while the MLP kernel scales linearly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_most_striking_tree_kernel_cost" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, striking, tree, kernel, cost, independent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_depths_studied_span_one_twenty_nine`

- Preferred role: `content`
- Cue keywords: `depths, studied, span, one, twenty-nine`
- Narration: The depths studied span one to twenty-nine.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_depths_studied_span_one_twenty_nine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords depths, studied, span, one, twenty-nine in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_takeaway_neural_tangent_kern`

- Preferred role: `takeaway`
- Cue keywords: `lasting, takeaway, neural, tangent, kernel, framework, once, used, only, neural`
- Narration: The lasting takeaway is that the neural tangent kernel framework, once used only for neural networks, applies to tree models.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_lasting_takeaway_neural_tangent_kern" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, takeaway, neural, tangent, kernel, framework in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_resulting_tree_ntk_explains_many`

- Preferred role: `method`
- Cue keywords: `resulting, tree, ntk, explains, many, soft-tree, behaviors, one, theory, converges`
- Narration: The resulting Tree NTK explains many soft-tree behaviors from one theory: training converges globally, oblivious sharing costs nothing in the limit, deep trees degenerate into a nearly constant kernel, and harder splits yield a more useful nonlinear kernel.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_resulting_tree_ntk_explains_many" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords resulting, tree, ntk, explains, many, soft-tree in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_also_delivers_fast_kernel_whose`

- Preferred role: `content`
- Cue keywords: `also, delivers, fast, kernel, whose, cost, independent, depth`
- Narration: It also delivers a fast kernel whose cost is independent of depth.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_also_delivers_fast_kernel_whose" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, delivers, fast, kernel, whose, cost in title/desc so the matcher can verify semantic overlap.
