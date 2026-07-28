# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_transformer_based_language_models_sh`

- Preferred role: `method`
- Cue keywords: `transformer-based, language, models, show, striking, ability, called, in-context, learning, where`
- Narration: Transformer-based language models show a striking ability called in-context learning, where a pretrained model solves brand-new tasks just by seeing a few input-output examples in its prompt, with no fine-tuning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_transformer_based_language_models_sh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords transformer-based, language, models, show, striking, ability in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_but_why_produces_ability_how`

- Preferred role: `method`
- Cue keywords: `but, why, produces, ability, how, well, generalizes, stayed, mostly, mystery`
- Narration: But why training produces this ability, and how well it generalizes, has stayed mostly a mystery because the math of nonlinear attention and nonlinear activations is hard.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_but_why_produces_ability_how" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, why, produces, ability, how, well in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_icml_2024_gives_first_theoretical`

- Preferred role: `method`
- Cue keywords: `icml, 2024, gives, first, theoretical, analysis, dynamics, transformer, both, nonlinear`
- Narration: This ICML 2024 paper gives the first theoretical analysis of the training dynamics of a Transformer with both nonlinear self-attention and a nonlinear MLP, and proves when the trained model generalizes in-context, both in-domain and under distribution shift.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_icml_2024_gives_first_theoretical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords icml, 2024, gives, first, theoretical, analysis in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_also_delivers_first_theory_how`

- Preferred role: `content`
- Cue keywords: `also, delivers, first, theory, how, pruning, affects, in-context, learning, showing`
- Narration: It also delivers the first theory of how pruning affects in-context learning, showing that removing the small-magnitude neurons barely hurts.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_also_delivers_first_theory_how" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, delivers, first, theory, how, pruning in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_in_context_learning_lets_pretrained`

- Preferred role: `method`
- Cue keywords: `in-context, learning, lets, pretrained, transformer, handle, new, tasks, simply, padding`
- Narration: In-context learning lets a pretrained Transformer handle new tasks by simply padding the query with a handful of example input-output pairs, no fine-tuning required.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_in_context_learning_lets_pretrained" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords in-context, learning, lets, pretrained, transformer, handle in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_despite_its_empirical_success_mechan`

- Preferred role: `method`
- Cue keywords: `despite, its, empirical, success, mechanics, how, transformer, actually, trained, acquire`
- Narration: Despite its empirical success, the mechanics of how a Transformer is actually trained to acquire this ability, and how far that ability generalizes, remain elusive.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_despite_its_empirical_success_mechan" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords despite, its, empirical, success, mechanics, how in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_core_difficulty_technical_self_atten`

- Preferred role: `method`
- Cue keywords: `core, difficulty, technical, self-attention, layer, nonlinear, through, softmax, mlp, nonlinear`
- Narration: The core difficulty is technical: the self-attention layer is nonlinear through the softmax, and the MLP is nonlinear through the ReLU activation, so the training problem is nonconvex and resists the tools used for simpler models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_core_difficulty_technical_self_atten" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, difficulty, technical, self-attention, layer, nonlinear in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_recent_works_began_explain_in_contex`

- Preferred role: `content`
- Cue keywords: `recent, works, began, explain, in-context, learning, but, keeps, only, part`
- Narration: Recent works began to explain in-context learning, but each keeps only part of the picture.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_recent_works_began_explain_in_contex" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recent, works, began, explain, in-context, learning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_some_ignore_nonlinear_self_attention`

- Preferred role: `method`
- Cue keywords: `some, ignore, nonlinear, self-attention, others, replace, nonlinear, mlp, linear, one`
- Narration: Some ignore the nonlinear self-attention, others replace the nonlinear MLP with a linear one, and most study linear regression rather than classification.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_some_ignore_nonlinear_self_attention" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords some, ignore, nonlinear, self-attention, others, replace in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_none_characterize_how_train_generali`

- Preferred role: `method`
- Cue keywords: `none, characterize, how, train, generalizes, under, distribution, shift, between, test`
- Narration: None can characterize how to train a model that generalizes under a distribution shift between training and test data, and none analyze how pruning a trained model changes its in-context ability.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_none_characterize_how_train_generali" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords none, characterize, how, train, generalizes, under in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_since_practitioners_routinely_prune`

- Preferred role: `takeaway`
- Cue keywords: `since, practitioners, routinely, prune, large, language, models, save, compute, while`
- Narration: Since practitioners routinely prune large language models to save compute while hoping to keep their in-context skills, closing this theoretical gap matters in practice.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s03_c4_since_practitioners_routinely_prune" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords since, practitioners, routinely, prune, large, language in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_work_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `work, makes, three, contributions`
- Narration: This work makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_work_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_first_theoretical_characteriza`

- Preferred role: `method`
- Cue keywords: `first, first, theoretical, characterization, how, train, transformer, keeps, both, nonlinear`
- Narration: First, it is the first theoretical characterization of how to train a Transformer that keeps both nonlinear self-attention and a nonlinear MLP, and it proves the trained model generalizes in context to unseen tasks, quantifying the required amount of data, number of iterations, and context length.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_first_theoretical_characteriza" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, first, theoretical, characterization, how, train in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_expands_our_understanding_mec`

- Preferred role: `method`
- Cue keywords: `second, expands, our, understanding, mechanism, in-context, learning, showing, how, attention`
- Narration: Second, it expands our understanding of the mechanism of in-context learning, showing how the attention layer and the MLP layer cooperate to make correct predictions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_expands_our_understanding_mec" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, expands, our, understanding, mechanism, in-context in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_provides_first_theoretical_ana`

- Preferred role: `figure`
- Cue keywords: `third, provides, first, theoretical, analysis, magnitude-based, pruning, in-context, learning, proving`
- Narration: Third, it provides the first theoretical analysis of magnitude-based pruning for in-context learning, proving that removing low-magnitude neurons is essentially harmless.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c4_third_provides_first_theoretical_ana" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, provides, first, theoretical, analysis, magnitude-based in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_deliberately_minimal_but_nonlinear_o`

- Preferred role: `method`
- Cue keywords: `deliberately, minimal, but, nonlinear, one, self-attention, head, softmax, followed, two-layer`
- Narration: The model is deliberately minimal but nonlinear: one self-attention head with a softmax, followed by a two-layer perceptron with ReLU activation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_deliberately_minimal_but_nonlinear_o" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deliberately, minimal, but, nonlinear, one, self-attention in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_augments_query_length_l_context_exam`

- Preferred role: `method`
- Cue keywords: `augments, query, length-l, context, example, pairs, embeds, them, prompt, minimizes`
- Narration: Training augments each query with a length-l context of example pairs, embeds them into a prompt, and minimizes a hinge loss over prompts sampled from a small subset of binary classification tasks. Every input contains relevant patterns that determine its label and irrelevant patterns that do not.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_augments_query_length_l_context_exam" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords augments, query, length-l, context, example, pairs in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_authors_follow_gradient_descent_dyna`

- Preferred role: `method`
- Cue keywords: `authors, follow, gradient-descent, dynamics, query, key, value, mlp, weights, evaluate`
- Narration: The authors follow the gradient-descent dynamics of the query, key, value, and MLP weights, and evaluate the resulting model both in-domain and under a distribution shift where the test relevant patterns are linear combinations of the training ones.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_authors_follow_gradient_descent_dyna" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, follow, gradient-descent, dynamics, query, key in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_two_quantities_drive_guarantees_alph`

- Preferred role: `content`
- Cue keywords: `two, quantities, drive, guarantees, alpha, fraction, context, examples, share, query`
- Narration: Two quantities drive the guarantees: alpha, the fraction of context examples that share the query's relevant pattern, and beta, the magnitude of the relevant features.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_two_quantities_drive_guarantees_alph" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, quantities, drive, guarantees, alpha, fraction in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_controlled_synthetic_set`

- Preferred role: `content`
- Cue keywords: `experiments, controlled, synthetic, setup, matches, theory`
- Narration: Experiments use a controlled synthetic setup that matches the theory.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_controlled_synthetic_set" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, controlled, synthetic, setup, matches, theory in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_six_in_domain_relevant_patterns_twen`

- Preferred role: `result`
- Cue keywords: `six, in-domain, relevant, patterns, twenty-four, irrelevant, ones, tasks, binary, classifications`
- Narration: There are six in-domain relevant patterns and twenty-four irrelevant ones, and tasks are binary classifications built from these patterns.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_six_in_domain_relevant_patterns_twen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords six, in-domain, relevant, patterns, twenty-four, irrelevant in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_two_models_trained_one_layer_transfo`

- Preferred role: `method`
- Cue keywords: `two, models, trained, one-layer, transformer, theory, analyzes, small, real-world, gpt-2`
- Narration: Two models are trained: the one-layer Transformer that the theory analyzes, and a small real-world GPT-2 with three layers and two heads.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_two_models_trained_one_layer_transfo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, models, trained, one-layer, transformer, theory in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_context_length_twenty_relevant_patte`

- Preferred role: `method`
- Cue keywords: `context, length, twenty, relevant-pattern, fraction, eighty, percent, out-of-domain, evaluation, new`
- Narration: Training uses a context length of twenty and a relevant-pattern fraction of eighty percent, and out-of-domain evaluation uses new tasks whose relevant patterns are linear combinations of the training patterns, exactly the regime the theorems cover.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_context_length_twenty_relevant_patte" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords context, length, twenty, relevant-pattern, fraction, eighty in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_main_theorem_shows_number_iterations`

- Preferred role: `result`
- Cue keywords: `main, theorem, shows, number, iterations, matching, number, samples, grow, only`
- Narration: The main theorem shows that a number of iterations, and a matching number of samples, that grow only polynomially in the problem parameters is enough to drive the in-domain generalization error down to order epsilon.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_main_theorem_shows_number_iterations" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords main, theorem, shows, number, iterations, matching in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_crucially_same_trained_also_generali`

- Preferred role: `method`
- Cue keywords: `crucially, same, trained, also, generalizes, out, domain, shifted, tasks, long`
- Narration: Crucially, the same trained model also generalizes out of domain to shifted tasks, as long as the new relevant patterns are linear combinations of the training patterns with coefficients summing to at least one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_crucially_same_trained_also_generali" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, same, trained, also, generalizes, out in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_experiments_confirm_sharply_out_of_d`

- Preferred role: `method`
- Cue keywords: `experiments, confirm, sharply, out-of-domain, classification, error, falls, below, one, percent`
- Narration: The experiments confirm this sharply: the out-of-domain classification error falls below one percent exactly when the combination strength S-one reaches one, and stays near zero above it, while the required context length and iterations track the predicted dependence on alpha.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_experiments_confirm_sharply_out_of_d" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, confirm, sharply, out-of-domain, classification, error in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_vary_fraction_context_exam`

- Preferred role: `content`
- Cue keywords: `ablations, vary, fraction, context, examples, share, query, relevant, pattern`
- Narration: Ablations vary the fraction of context examples that share the query's relevant pattern.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablations_vary_fraction_context_exam" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, vary, fraction, context, examples, share in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_predicted_needed_context_length_grow`

- Preferred role: `content`
- Cue keywords: `predicted, needed, context, length, grows, like, one, over, alpha, needed`
- Narration: As predicted, the needed context length grows like one over alpha and the needed iterations and samples grow like alpha to the minus two-thirds, so richer contexts converge faster and need shorter prompts.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_predicted_needed_context_length_grow" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords predicted, needed, context, length, grows, like in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_second_comparison_pits_in_context_le`

- Preferred role: `result`
- Cue keywords: `second, comparison, pits, in-context, learning, against, logistic, regression, kernel, linear`
- Narration: A second comparison pits in-context learning against logistic regression, kernel and linear SVMs, and nearest-neighbor classifiers.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c3_second_comparison_pits_in_context_le" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, comparison, pits, in-context, learning, against in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_when_relevant_fraction_high_gap`

- Preferred role: `method`
- Cue keywords: `when, relevant, fraction, high, gap, small, but, harder, low-fraction, regime`
- Narration: When the relevant fraction is high the gap is small, but in the harder low-fraction regime in-context learning is the most sample-efficient method, indicating it removes irrelevant data and tolerates label noise better than the classical baselines.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_when_relevant_fraction_high_gap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, relevant, fraction, high, gap, small in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_message_cost`

- Preferred role: `method`
- Cue keywords: `few, numbers, capture, message, cost, both, iterations, samples, scales, alpha`
- Narration: A few numbers capture the paper's message. The training cost, both in iterations and in samples, scales as alpha to the minus two-thirds, and the required context length as one over alpha.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_message_cost" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, message, cost, both in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_needs_trained_only_vanishing_fractio`

- Preferred role: `method`
- Cue keywords: `needs, trained, only, vanishing, fraction, order, one, over, square, root`
- Narration: The model needs to be trained on only a vanishing fraction, order one over the square root of the number of patterns, of all in-domain tasks, yet it generalizes to the rest.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_needs_trained_only_vanishing_fractio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords needs, trained, only, vanishing, fraction, order in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_out_of_domain_error_drops_below_one`

- Preferred role: `method`
- Cue keywords: `out-of-domain, error, drops, below, one, percent, once, combination, strength, reaches`
- Narration: Out-of-domain error drops below one percent once the combination strength reaches one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_out_of_domain_error_drops_below_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords out-of-domain, error, drops, below, one, percent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_pruning_removing_low_magnitude_neuro`

- Preferred role: `result`
- Cue keywords: `pruning, removing, low-magnitude, neurons, keeps, error, order, epsilon, plus, one`
- Narration: And on pruning: removing the low-magnitude neurons keeps error at order epsilon plus one over the square root of M-one, essentially lossless, and in experiments magnitude-based pruning of up to about fifteen percent of the output-layer neurons leaves out-of-domain accuracy intact, whereas pruning the large-magnitude neurons degrades error at least linearly in the pruning rate.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_pruning_removing_low_magnitude_neuro" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pruning, removing, low-magnitude, neurons, keeps, error in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_in_context_learning`

- Preferred role: `method`
- Cue keywords: `lasting, message, in-context, learning, nonlinear, transformer, not, black, box, both`
- Narration: The lasting message is that in-context learning in a nonlinear Transformer is not a black box: with both nonlinear attention and a nonlinear MLP, a one-layer model can be provably trained to generalize in context, in-domain and under distribution shift, and the effort it takes is controlled by how much of the context shares the query's relevant pattern.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_lasting_message_in_context_learning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, in-context, learning, nonlinear, transformer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_trained_works_having_attention_focus`

- Preferred role: `method`
- Cue keywords: `trained, works, having, attention, focus, context, examples, match, query, relevant`
- Narration: The trained model works by having attention focus on the context examples that match the query's relevant pattern while the ReLU MLP amplifies their labels.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_trained_works_having_attention_focus" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trained, works, having, attention, focus, context in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_because_only_large_magnitude_neurons`

- Preferred role: `content`
- Cue keywords: `because, only, large-magnitude, neurons, carry, signal, pruning, small, ones, essentially`
- Narration: Because only the large-magnitude neurons carry this signal, pruning the small ones is essentially free, giving a principled reason why magnitude-based pruning preserves in-context learning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_because_only_large_magnitude_neurons" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, only, large-magnitude, neurons, carry, signal in title/desc so the matcher can verify semantic overlap.
