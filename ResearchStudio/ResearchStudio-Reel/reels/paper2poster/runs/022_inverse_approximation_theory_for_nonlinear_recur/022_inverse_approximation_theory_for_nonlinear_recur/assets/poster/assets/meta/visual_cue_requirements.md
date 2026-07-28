# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_recurrent_neural_networks_workhorse`

- Preferred role: `method`
- Cue keywords: `recurrent, neural, networks, workhorse, sequence, yet, they, famously, struggle, when`
- Narration: Recurrent neural networks are a workhorse for sequence data, yet they famously struggle when the data carries long-term dependencies. This paper asks why, from the rigorous viewpoint of approximation theory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_recurrent_neural_networks_workhorse" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recurrent, neural, networks, workhorse, sequence, yet in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_prove_inverse_bernstein_type`

- Preferred role: `method`
- Cue keywords: `authors, prove, inverse, bernstein-type, theorem, nonlinear, rnns, any, sequence, relationship`
- Narration: The authors prove an inverse, or Bernstein-type, theorem for nonlinear RNNs: any sequence relationship that can be stably approximated by an RNN must have a memory that decays exponentially in time.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_authors_prove_inverse_bernstein_type" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, prove, inverse, bernstein-type, theorem, nonlinear in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_other_words_difficulty_not_just`

- Preferred role: `method`
- Cue keywords: `other, words, difficulty, not, just, optimization, artifact, fundamental, limitation, rnn`
- Narration: In other words, the difficulty is not just an optimization artifact, it is a fundamental limitation of the RNN hypothesis space, extending the known curse of memory from linear to nonlinear networks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_other_words_difficulty_not_just" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords other, words, difficulty, not, just, optimization in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_building_analysis_they_propose_princ`

- Preferred role: `method`
- Cue keywords: `building, analysis, they, propose, principled, stable, reparameterization, lets, rnns, escape`
- Narration: Building on this analysis, they propose a principled stable reparameterization that lets RNNs escape the limitation, and they confirm everything with numerical experiments.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_building_analysis_they_propose_princ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords building, analysis, they, propose, principled, stable in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_recurrent_neural_networks_among_most`

- Preferred role: `content`
- Cue keywords: `recurrent, neural, networks, among, most, basic, models, learning, sequential, temporal`
- Narration: Recurrent neural networks are among the most basic models for learning from sequential and temporal data, with applications from time series and speech to text and sentiment.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_recurrent_neural_networks_among_most" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recurrent, neural, networks, among, most, basic in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_long_standing_empirical_observat`

- Preferred role: `content`
- Cue keywords: `but, long-standing, empirical, observation, they, falter, when, long-term, dependencies`
- Narration: But a long-standing empirical observation is that they falter when the data has long-term dependencies.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_but_long_standing_empirical_observat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, long-standing, empirical, observation, they, falter in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_open_question_confronts_whether_fail`

- Preferred role: `method`
- Cue keywords: `open, question, confronts, whether, failure, only, about, dynamics, like, exploding`
- Narration: The open question this paper confronts is whether that failure is only about training dynamics, like exploding or vanishing gradients, or whether it reflects a deeper, structural limitation of what RNNs can represent at all.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_open_question_confronts_whether_fail" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords open, question, confronts, whether, failure, only in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_answering_requires_approximation_the`

- Preferred role: `title`
- Cue keywords: `answering, requires, approximation-theoretic, lens, rather, optimization, one`
- Narration: Answering this requires an approximation-theoretic lens rather than an optimization one.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c4_answering_requires_approximation_the" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords answering, requires, approximation-theoretic, lens, rather, optimization in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_approximation_theory_offers_two_comp`

- Preferred role: `content`
- Cue keywords: `approximation, theory, offers, two, complementary, kinds, statements, forward, jackson-type, theorems`
- Narration: Approximation theory offers two complementary kinds of statements. Forward, or Jackson-type, theorems tell you how well a model can approximate a sufficiently regular target.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_approximation_theory_offers_two_comp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords approximation, theory, offers, two, complementary, kinds in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_inverse_bernstein_type_theorems_run`

- Preferred role: `content`
- Cue keywords: `inverse, bernstein-type, theorems, run, other, direction, they, assume, target, efficiently`
- Narration: Inverse, or Bernstein-type, theorems run the other direction: they assume a target can be efficiently approximated and then deduce what regularity the target must have.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_inverse_bernstein_type_theorems_run" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords inverse, bernstein-type, theorems, run, other, direction in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_inverse_theorems_precisely_tool_expo`

- Preferred role: `method`
- Cue keywords: `inverse, theorems, precisely, tool, exposing, fundamental, limitations, architecture, earlier, work`
- Narration: Inverse theorems are precisely the tool for exposing fundamental limitations of an architecture. Earlier work proved such a result for linear RNNs, showing that efficiently approximable linear targets must have exponentially decaying memory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_inverse_theorems_precisely_tool_expo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords inverse, theorems, precisely, tool, exposing, fundamental in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_pressing_question_whether_adding_non`

- Preferred role: `title`
- Cue keywords: `pressing, question, whether, adding, nonlinearity, which, greatly, increases, capacity, would`
- Narration: The pressing question was whether adding nonlinearity, which greatly increases model capacity, would break this so-called curse of memory. This paper was motivated to settle that.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c4_pressing_question_whether_adding_non" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pressing, question, whether, adding, nonlinearity, which in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions_first`

- Preferred role: `method`
- Cue keywords: `makes, three, main, contributions, first, extends, concept, memory, function, linear`
- Narration: The paper makes three main contributions. First, it extends the concept of a memory function from the linear setting to general nonlinear functional sequences, and crucially this memory function can be numerically quantified by querying a trained model, not just defined abstractly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions, first, extends in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_introduces_framework_stable_a`

- Preferred role: `guidance`
- Cue keywords: `second, introduces, framework, stable, approximation, mild, requirement, approximant, behaves, continuously`
- Narration: Second, it introduces a framework of stable approximation, a mild requirement that the approximant behaves continuously under small parameter perturbations, which is exactly what gradient-based optimization needs.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c2_second_introduces_framework_stable_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, introduces, framework, stable, approximation, mild in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_these_two_ingredients_proves`

- Preferred role: `method`
- Cue keywords: `third, these, two, ingredients, proves, what, authors, believe, first, bernstein-type`
- Narration: Third, using these two ingredients it proves what the authors believe is the first Bernstein-type approximation theorem for nonlinear RNNs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_third_these_two_ingredients_proves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, these, two, ingredients, proves, what in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_top_theory_proposes_principled_repar`

- Preferred role: `method`
- Cue keywords: `top, theory, proposes, principled, reparameterization, method, overcome, identified, limitation, confirms`
- Narration: On top of the theory, it proposes a principled reparameterization method to overcome the identified limitation and confirms the whole story with experiments.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_top_theory_proposes_principled_repar" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, theory, proposes, principled, reparameterization, method in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_three_pieces_first_memory`

- Preferred role: `method`
- Cue keywords: `method, three, pieces, first, memory, function, nonlinear, functionals, measures, over`
- Narration: The method has three pieces. First, a memory function for nonlinear functionals: it measures, over Heaviside step inputs, how strongly the output at time t still depends on the input, giving a precise, task-independent, and numerically queryable notion of memory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_three_pieces_first_memory" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, three, pieces, first, memory, function in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_second_stability_framework_perturbat`

- Preferred role: `result`
- Cue keywords: `second, stability, framework, perturbation, error, hidden, dimension, worst-case, output, error`
- Narration: Second, a stability framework: the perturbation error at hidden dimension m is the worst-case output error when parameters are perturbed within a ball of radius beta, and a target is beta-zero stably approximated if that error stays continuous up to some positive radius.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c2_second_stability_framework_perturbat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, stability, framework, perturbation, error, hidden in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_central_theorem_says_target_decaying`

- Preferred role: `method`
- Cue keywords: `central, theorem, says, target, decaying, memory, stably, approximated, rnns, whose`
- Narration: The central theorem then says: if a target with decaying memory is stably approximated by RNNs whose weight norms and perturbed memories stay uniformly controlled, then the target's memory must decay exponentially. The proof leverages stability to drive hidden-state derivatives to zero and uses the Hartman-Grobman theorem to bound the recurrent eigenvalues.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_central_theorem_says_target_decaying" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords central, theorem, says, target, decaying, memory in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_finally_overcome_curse_they_substitu`

- Preferred role: `method`
- Cue keywords: `finally, overcome, curse, they, substitute, recurrent, weight, matrix, continuous, function`
- Narration: Finally, to overcome this curse, they substitute the recurrent weight matrix with a continuous function that always maps into stable, negative-real-part matrices, such as an exponential or softplus map, so the network can push eigenvalues toward zero while remaining stable under perturbation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_finally_overcome_curse_they_substitu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, overcome, curse, they, substitute, recurrent in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_span_synthetic_real`

- Preferred role: `content`
- Cue keywords: `experiments, span, synthetic, real`
- Narration: The experiments span synthetic and real data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_span_synthetic_real" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, span, synthetic, real in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_synthetic_side_authors_build_linear`

- Preferred role: `content`
- Cue keywords: `synthetic, side, authors, build, linear, nonlinear, functional, targets, either, exponential`
- Narration: On the synthetic side, the authors build linear and nonlinear functional targets with either exponential or polynomial decaying memory and sweep the hidden dimension from about two up to sixty four to watch how the perturbation-stability radius behaves.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_synthetic_side_authors_build_linear" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords synthetic, side, authors, build, linear, nonlinear in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_they_also_construct_randomly_initial`

- Preferred role: `method`
- Cue keywords: `they, also, construct, randomly, initialized, rnn, teacher, models, large, hidden`
- Narration: They also construct randomly initialized RNN teacher models with a large hidden dimension of two hundred fifty six and approximate them with student RNNs to test the stability filter.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_they_also_construct_randomly_initial" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, also, construct, randomly, initialized, rnn in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_real_they_query_memory_function`

- Preferred role: `method`
- Cue keywords: `real, they, query, memory, function, lstm, models, imdb, movie-review, sentiment`
- Narration: On real data, they query the memory function of LSTM models on IMDB movie-review sentiment analysis, and they train nonlinear RNNs on MNIST image classification to test the optimization benefits of stable reparameterization.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_real_they_query_memory_function" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords real, they, query, memory, function, lstm in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_theoretical_result_clean_in`

- Preferred role: `method`
- Cue keywords: `headline, theoretical, result, clean, inverse, statement, nonlinear, rnn, stably, approximate`
- Narration: The headline theoretical result is a clean inverse statement: if a nonlinear RNN can stably approximate a target sequence relationship, then that target's memory must decay exponentially.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_theoretical_result_clean_in" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, theoretical, result, clean, inverse, statement in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_extends_linear_curse_memory_nonlinea`

- Preferred role: `method`
- Cue keywords: `extends, linear, curse, memory, nonlinear, regime, proves, failure, long-term, dependencies`
- Narration: This extends the linear curse of memory to the nonlinear regime and proves the failure on long-term dependencies is intrinsic to the RNN hypothesis space, not just a training artifact. The numerics back this up.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_extends_linear_curse_memory_nonlinea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords extends, linear, curse, memory, nonlinear, regime in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_polynomial_memory_targets_perturbati`

- Preferred role: `result`
- Cue keywords: `polynomial-memory, targets, perturbation-error, curves, different, hidden, dimensions, keep, intersecting, further`
- Narration: For polynomial-memory targets, the perturbation-error curves for different hidden dimensions keep intersecting further and further left as the dimension grows, meaning no positive stability radius survives.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_polynomial_memory_targets_perturbati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords polynomial-memory, targets, perturbation-error, curves, different, hidden in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_when_authors_filter_randomly_generat`

- Preferred role: `result`
- Cue keywords: `when, authors, filter, randomly, generated, teacher, models, keep, only, those`
- Narration: And when the authors filter randomly generated teacher models to keep only those that are both approximable and stable, the only survivors are teachers whose memory decays exponentially. They also observe that slowly-decaying targets take on the order of a thousand epochs to fit versus about ten for exponential ones.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_when_authors_filter_randomly_generat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, authors, filter, randomly, generated, teacher in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_key_ablation_varies_only_how`

- Preferred role: `content`
- Cue keywords: `key, ablation, varies, only, how, recurrent, weight, parameterized, holding, initialization`
- Narration: The key ablation varies only how the recurrent weight is parameterized, holding initialization fixed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_key_ablation_varies_only_how" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, ablation, varies, only, how, recurrent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_mnist_three_stable_reparameterizatio`

- Preferred role: `result`
- Cue keywords: `mnist, three, stable, reparameterizations, softplus, exponential, inverse, all, speed, optimization`
- Narration: On MNIST, the three stable reparameterizations, softplus, exponential, and inverse, all speed up optimization and reach higher test accuracy than the direct, unstable parameterization where the weight is used as-is.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_mnist_three_stable_reparameterizatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mnist, three, stable, reparameterizations, softplus, exponential in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_importantly_since_reparameterization`

- Preferred role: `content`
- Cue keywords: `importantly, since, reparameterization, does, not, change, inherent, capacity, final, performance`
- Narration: Importantly, since reparameterization does not change the model's inherent capacity, the final performance across stable variants is comparable, isolating the effect as an optimization and stability benefit rather than a capacity change.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_importantly_since_reparameterization" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords importantly, since, reparameterization, does, not, change in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_synthetic_side_applying_exponential`

- Preferred role: `method`
- Cue keywords: `synthetic, side, applying, exponential, softplus, reparameterizations, linear, rnns, approximating, polynomial-decay`
- Narration: On the synthetic side, applying exponential and softplus reparameterizations to linear RNNs approximating polynomial-decay targets restores the expected continuous limiting error curve, confirming stability is recovered.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_synthetic_side_applying_exponential" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords synthetic, side, applying, exponential, softplus, reparameterizations in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_mnist_trained_ten_epochs_averaged`

- Preferred role: `method`
- Cue keywords: `mnist, trained, ten, epochs, averaged, over, three, runs, softplus, stable`
- Narration: On MNIST, trained for ten epochs and averaged over three runs, the softplus stable reparameterization reaches seventy one point three six percent test accuracy, compared with sixty eight point four seven percent for the direct, unstable baseline, an improvement of nearly three percentage points.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_mnist_trained_ten_epochs_averaged" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mnist, trained, ten, epochs, averaged, over in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_exponential_inverse_stable_maps_also`

- Preferred role: `content`
- Cue keywords: `exponential, inverse, stable, maps, also, land, above, seventy, percent, all`
- Narration: The exponential and inverse stable maps also land above seventy percent, all beating the unstable version.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_exponential_inverse_stable_maps_also" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords exponential, inverse, stable, maps, also, land in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_synthetic_side_exponential_memory_ta`

- Preferred role: `content`
- Cue keywords: `synthetic, side, exponential-memory, targets, fit, roughly, ten, epochs, while, polynomial-memory`
- Narration: On the synthetic side, exponential-memory targets are fit in roughly ten epochs, while polynomial-memory targets need on the order of a thousand epochs and still fail the stability test. The teacher-filtering experiment uses hidden dimension two hundred fifty six.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_synthetic_side_exponential_memory_ta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords synthetic, side, exponential-memory, targets, fit, roughly in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_one_line_takeaway_matter_how_you`

- Preferred role: `method`
- Cue keywords: `one-line, takeaway, matter, how, you, train, them, plain, nonlinear, rnns`
- Narration: The one-line takeaway is this: no matter how you train them, plain nonlinear RNNs can only stably approximate sequence relationships whose memory fades exponentially, so their well-known struggle with long-term dependencies is baked into the architecture, not merely the optimizer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_one_line_takeaway_matter_how_you" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one-line, takeaway, matter, how, you, train in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_but_same_analysis_points_cure`

- Preferred role: `figure`
- Cue keywords: `but, same, analysis, points, cure`
- Narration: But the same analysis points to the cure.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c2_but_same_analysis_points_cure" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, same, analysis, points, cure in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_reparameterizing_recurrent_weights_s`

- Preferred role: `method`
- Cue keywords: `reparameterizing, recurrent, weights, stable, map, like, exponential, softplus, network, keep`
- Narration: By reparameterizing the recurrent weights with a stable map like exponential or softplus, the network can keep eigenvalues near the edge of stability without losing it, provably relaxing the curse of memory and, on real tasks like MNIST, training faster and generalizing better.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_reparameterizing_recurrent_weights_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reparameterizing, recurrent, weights, stable, map, like in title/desc so the matcher can verify semantic overlap.
