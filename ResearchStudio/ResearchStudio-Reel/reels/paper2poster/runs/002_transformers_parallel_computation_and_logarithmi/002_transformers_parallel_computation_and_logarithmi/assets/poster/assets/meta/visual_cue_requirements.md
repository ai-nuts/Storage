# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_what_makes_transformer_special_clayt`

- Preferred role: `method`
- Cue keywords: `what, makes, transformer, special, clayton, sanford, daniel, hsu, matus, telgarsky`
- Narration: What makes the transformer special? This paper by Clayton Sanford, Daniel Hsu, and Matus Telgarsky argues the answer is parallelism.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_what_makes_transformer_special_clayt" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, makes, transformer, special, clayton, sanford in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_prove_tight_two_way_correspo`

- Preferred role: `method`
- Cue keywords: `authors, prove, tight, two-way, correspondence, between, transformers, massively, parallel, computation`
- Narration: The authors prove a tight, two-way correspondence between transformers and the Massively Parallel Computation model used to study distributed algorithms.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_authors_prove_tight_two_way_correspo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, prove, tight, two-way, correspondence, between in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_upshot_striking_transformer_only_log`

- Preferred role: `method`
- Cue keywords: `upshot, striking, transformer, only, logarithmic, depth, solve, basic, reasoning, tasks`
- Narration: The upshot is striking: a transformer with only logarithmic depth can solve basic reasoning tasks that recurrent models, state-space models like Mamba, and efficient sub-quadratic attention variants provably cannot solve efficiently.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_upshot_striking_transformer_only_log" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords upshot, striking, transformer, only, logarithmic, depth in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_they_back_theory_clean_synthetic`

- Preferred role: `method`
- Cue keywords: `they, back, theory, clean, synthetic, task, k-hop, induction, heads, problem`
- Narration: They back the theory with a clean synthetic task, the k-hop induction heads problem, where trained transformers obey exactly the logarithmic depth threshold the theory predicts.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_they_back_theory_clean_synthetic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, back, theory, clean, synthetic, task in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_transformers_dominate_sequence_model`

- Preferred role: `method`
- Cue keywords: `transformers, dominate, sequence, modeling, yet, theory, explaining, why, been, unsatisfying`
- Narration: Transformers dominate sequence modeling, yet the theory explaining why has been unsatisfying. One line of work proves universality, but only for enormous models, and that tells us nothing about which tasks are solvable size-efficiently.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_transformers_dominate_sequence_model" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords transformers, dominate, sequence, modeling, yet, theory in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_second_line_studies_constant_depth_r`

- Preferred role: `title`
- Cue keywords: `second, line, studies, constant-depth, regime, where, context, length, grows, many`
- Narration: A second line studies a constant-depth regime where context length grows, and there many basic algorithmic tasks, like matching parentheses, are simply impossible.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c2_second_line_studies_constant_depth_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, line, studies, constant-depth, regime, where in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_neither_picture_isolates_property_ac`

- Preferred role: `method`
- Cue keywords: `neither, picture, isolates, property, actually, sets, transformers, apart, recurrent, networks`
- Narration: Neither picture isolates the property that actually sets transformers apart from recurrent networks or other architectures.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_neither_picture_isolates_property_ac" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neither, picture, isolates, property, actually, sets in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_asks_single_clean_computational_prop`

- Preferred role: `method`
- Cue keywords: `asks, single, clean, computational, property, captures, strengths, limits, transformers, same`
- Narration: This paper asks: is there a single, clean computational property that captures the strengths and the limits of transformers at the same time?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_asks_single_clean_computational_prop" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords asks, single, clean, computational, property, captures in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_insight_self_attention_funda`

- Preferred role: `method`
- Cue keywords: `authors, insight, self-attention, fundamentally, parallel, operation`
- Narration: The authors' insight is that self-attention is fundamentally a parallel operation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_authors_insight_self_attention_funda" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, insight, self-attention, fundamentally, parallel, operation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_every_pair_tokens_interact_one`

- Preferred role: `content`
- Cue keywords: `every, pair, tokens, interact, one, layer, through, inner, product, between`
- Narration: Every pair of tokens can interact in one layer through the inner product between their query and key embeddings, whereas a recurrent network must thread information through the sequence one step at a time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_every_pair_tokens_interact_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, pair, tokens, interact, one, layer in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_parallelism_looks_lot_like_massively`

- Preferred role: `method`
- Cue keywords: `parallelism, looks, lot, like, massively, parallel, computation, mpc, abstraction, theorists`
- Narration: That parallelism looks a lot like the Massively Parallel Computation model, or MPC, the abstraction that theorists use to reason about MapReduce and other distributed systems, where many machines each hold a little data and exchange messages in synchronous rounds.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_parallelism_looks_lot_like_massively" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords parallelism, looks, lot, like, massively, parallel in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_bet_you_make_connection_between`

- Preferred role: `method`
- Cue keywords: `bet, you, make, connection, between, attention, layers, mpc, rounds, precise`
- Narration: The paper's bet is that if you can make the connection between attention layers and MPC rounds precise, you get a single lens that explains both what transformers can do and what they cannot.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_bet_you_make_connection_between" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords bet, you, make, connection, between, attention in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_two_main_contributions_first`

- Preferred role: `method`
- Cue keywords: `makes, two, main, contributions, first, establishes, tight, correspondence, any, r-round`
- Narration: The paper makes two main contributions. First, it establishes a tight correspondence: any R-round MPC protocol can be run by a transformer of depth about R, and conversely any depth-L transformer can be simulated by an O(L)-round MPC protocol.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_makes_two_main_contributions_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, two, main, contributions, first, establishes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_algorithmic_power_logarithmic_depth`

- Preferred role: `method`
- Cue keywords: `algorithmic, power, logarithmic-depth, transformers, captured, constants, mpc`
- Narration: So the algorithmic power of logarithmic-depth transformers is captured, up to constants, by the MPC model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_algorithmic_power_logarithmic_depth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords algorithmic, power, logarithmic-depth, transformers, captured, constants in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_instantly_gives_log_depth_transforme`

- Preferred role: `method`
- Cue keywords: `instantly, gives, log-depth, transformers, classic, parallel, problems, like, graph, connectivity`
- Narration: That instantly gives log-depth transformers for classic parallel problems like graph connectivity, and, under a standard conjecture about MPC's limits, shows those constructions are near-optimal.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_instantly_gives_log_depth_transforme" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instantly, gives, log-depth, transformers, classic, parallel in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_second_authors_introduce_concrete_sy`

- Preferred role: `method`
- Cue keywords: `second, authors, introduce, concrete, synthetic, task, k-hop, induction, heads, prove`
- Narration: Second, the authors introduce a concrete synthetic task, k-hop induction heads, and prove that transformers solve it with logarithmic depth while several competing architectures cannot do so efficiently. They then train real transformers and watch them obey the very same threshold.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_second_authors_introduce_concrete_sy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, authors, introduce, concrete, synthetic, task in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_heart_forward_simulation_routing_gad`

- Preferred role: `method`
- Cue keywords: `heart, forward, simulation, routing, gadget, mpc, round, ends, machines, sending`
- Narration: The heart of the forward simulation is a routing gadget. In MPC, each round ends with machines sending addressed messages to one another, and the authors show a single self-attention layer can perform exactly this routing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_heart_forward_simulation_routing_gad" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords heart, forward, simulation, routing, gadget, mpc in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_trick_captured_lemma_3_2_encode`

- Preferred role: `content`
- Cue keywords: `trick, captured, lemma, 3.2, encode, message, redundantly, multiple, fixed, locations`
- Narration: The trick, captured in Lemma 3.2, is to encode each message redundantly in multiple fixed locations using multiple hashing, and to move information with sparse propagation, which keeps the query, key, and value matrices tall and skinny so the embedding dimension stays small.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_trick_captured_lemma_3_2_encode" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trick, captured, lemma, 3.2, encode, message in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_put_one_such_layer_per`

- Preferred role: `method`
- Cue keywords: `put, one, such, layer, per, communication, round, protocol, rounds, becomes`
- Narration: Put one such layer per communication round and a protocol of R rounds becomes a transformer of depth R plus one. The reverse direction packs a whole transformer layer into a single MPC round, proving transformers are no stronger than the model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_put_one_such_layer_per" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords put, one, such, layer, per, communication in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_k_hop_task_specifically_they_give`

- Preferred role: `method`
- Cue keywords: `k-hop, task, specifically, they, give, tailored, causally-masked, construction, constant, width`
- Narration: For the k-hop task specifically, they give a tailored, causally-masked construction of constant width whose depth is exactly floor of log base two of k, plus two.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_k_hop_task_specifically_they_give" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords k-hop, task, specifically, they, give, tailored in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_make_everything_concrete_authors_des`

- Preferred role: `title`
- Cue keywords: `make, everything, concrete, authors, design, k-hop, induction, heads, task, standard`
- Narration: To make everything concrete the authors design the k-hop induction heads task. Standard induction heads asks a model to complete a bigram by predicting the token that followed the last occurrence of the current token.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c1_make_everything_concrete_authors_des" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords make, everything, concrete, authors, design, k-hop in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_k_hop_version_chains_one_completion`

- Preferred role: `content`
- Cue keywords: `k-hop, version, chains, one, completion, decide, which, bigram, complete, next`
- Narration: The k-hop version chains this: use one completion to decide which bigram to complete next, k times over.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_k_hop_version_chains_one_completion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords k-hop, version, chains, one, completion, decide in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_composition_exactly_what_makes_task`

- Preferred role: `method`
- Cue keywords: `composition, exactly, what, makes, task, interesting, stress, test, because, intuitively`
- Narration: That composition is exactly what makes the task an interesting stress test, because intuitively it looks like it needs k sequential steps, yet a parallel architecture can fold it into logarithmically many.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_composition_exactly_what_makes_task" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords composition, exactly, what, makes, task, interesting in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_they_train_evaluate_sequences_length`

- Preferred role: `result`
- Cue keywords: `they, train, evaluate, sequences, length, one, hundred, over, four-symbol, alphabet`
- Narration: They train and evaluate on sequences of length one hundred over a four-symbol alphabet, sweeping the hop count k from zero up to sixteen, in a multi-task setup where one model handles a randomly drawn k each time.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_they_train_evaluate_sequences_length" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, train, evaluate, sequences, length, one in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_ties_theory_experime`

- Preferred role: `method`
- Cue keywords: `headline, result, ties, theory, experiment, together, theory, side, they, prove`
- Narration: The headline result ties theory and experiment together. On the theory side, they prove logarithmic depth is not just sufficient but necessary: any transformer solving k-hop needs depth on the order of log k.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_result_ties_theory_experime" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, ties, theory, experiment, together in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_experimental_side_they_train_transfo`

- Preferred role: `method`
- Cue keywords: `experimental, side, they, train, transformers, depths, two, through, six, measure`
- Narration: On the experimental side, they train transformers of depths two through six and measure token-wise error as k grows. The picture is remarkably clean.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_experimental_side_they_train_transfo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experimental, side, they, train, transformers, depths in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_extra_layer_roughly_doubles_largest`

- Preferred role: `content`
- Cue keywords: `extra, layer, roughly, doubles, largest, hop, count, learn, six-layer, network`
- Narration: Each extra layer roughly doubles the largest hop count the model can learn, so a six-layer network handles every k up to sixteen, a five-layer network up to eight, a four-layer network up to four.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_extra_layer_roughly_doubles_largest" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords extra, layer, roughly, doubles, largest, hop in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_empirical_threshold_sits_right_floor`

- Preferred role: `method`
- Cue keywords: `empirical, threshold, sits, right, floor, log, base, two, plus, two`
- Narration: The empirical threshold sits right at floor of log base two of k plus two, precisely the depth their construction predicts. The learned models even turn out to be interpretable, with attention patterns that mirror the hand-designed proof.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_empirical_threshold_sits_right_floor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords empirical, threshold, sits, right, floor, log in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_experiments_include_several_ablation`

- Preferred role: `method`
- Cue keywords: `experiments, include, several, ablations, stress, core, claim, sweeping, depth, two`
- Narration: The experiments include several ablations that stress the core claim. Sweeping depth from two to six is the main one, and it cleanly traces out the logarithmic threshold.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_experiments_include_several_ablation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, include, several, ablations, stress, core in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_when_they_widen_models_going`

- Preferred role: `guidance`
- Cue keywords: `when, they, widen, models, going, embedding, dimension, one, hundred, twenty-eight`
- Narration: When they widen the models, going from embedding dimension one hundred twenty-eight and four heads up to two hundred fifty-six and eight heads, the depth-versus-k boundary barely moves, showing the dependence is really about depth, not sheer size.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s08_c2_when_they_widen_models_going" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, they, widen, models, going, embedding in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_finite_sample_regime_where_overfitti`

- Preferred role: `title`
- Cue keywords: `finite-sample, regime, where, overfitting, risk, deeper, models, generalize, better, hinting`
- Narration: In the finite-sample regime, where overfitting is a risk, deeper models generalize better, hinting at an inductive bias suited to compositional tasks.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s08_c3_finite_sample_regime_where_overfitti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finite-sample, regime, where, overfitting, risk, deeper in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_when_they_crack_open_trained`

- Preferred role: `method`
- Cue keywords: `when, they, crack, open, trained, networks, attention, matrices, line, intermediate`
- Narration: And when they crack open the trained networks, the attention matrices line up with the intermediate pointer computations from the proof, so the learned solution mechanistically resembles the theoretical construction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_when_they_crack_open_trained" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, they, crack, open, trained, networks in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_solving_k_hop`

- Preferred role: `method`
- Cue keywords: `few, numbers, capture, solving, k-hop, needs, depth, equal, floor, log`
- Narration: A few numbers capture the paper. Solving k-hop needs depth equal to floor of log base two of k plus two, and that formula holds both in the proof and in the trained networks. Adding a single layer roughly doubles the reach in k, so six layers cover everything up to sixteen hops.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_solving_k_hop" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, solving, k-hop, needs in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_simulation_constants_clean_too_r_rou`

- Preferred role: `method`
- Cue keywords: `simulation, constants, clean, too, r-round, parallel, protocol, becomes, transformer, depth`
- Narration: The simulation constants are clean too: an R-round parallel protocol becomes a transformer of depth R plus one, and any depth-L transformer collapses into order-L parallel rounds.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_simulation_constants_clean_too_r_rou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords simulation, constants, clean, too, r-round, parallel in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_contrast_other_architectures_stark_m`

- Preferred role: `method`
- Cue keywords: `contrast, other, architectures, stark, multi-layer, recurrent, networks, extension, state-space, models`
- Narration: The contrast with other architectures is stark: multi-layer recurrent networks, and by extension state-space models like Mamba, need depth at least k, and so do efficient sub-quadratic attention variants like Performer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_contrast_other_architectures_stark_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contrast, other, architectures, stark, multi-layer, recurrent in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_where_transformer_logarithmic_altern`

- Preferred role: `method`
- Cue keywords: `where, transformer, logarithmic, alternatives, linear`
- Narration: Where the transformer is logarithmic in k, the alternatives are linear.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_where_transformer_logarithmic_altern" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords where, transformer, logarithmic, alternatives, linear in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_one_thing_remember_transformers_prec`

- Preferred role: `method`
- Cue keywords: `one, thing, remember, transformers, precise, sense, parallel, computers`
- Narration: The one thing to remember is that transformers are, in a precise sense, parallel computers.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_one_thing_remember_transformers_prec" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, thing, remember, transformers, precise, sense in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_pins_intuition_down_proving_logarith`

- Preferred role: `method`
- Cue keywords: `pins, intuition, down, proving, logarithmic-depth, transformers, equivalent, constant-round, massively, parallel`
- Narration: This paper pins that intuition down by proving logarithmic-depth transformers are equivalent to constant-round Massively Parallel Computation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_pins_intuition_down_proving_logarith" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pins, intuition, down, proving, logarithmic-depth, transformers in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_equivalence_explains_both_their_powe`

- Preferred role: `method`
- Cue keywords: `equivalence, explains, both, their, power, their, limits, predicts, sharp, separation`
- Narration: That equivalence explains both their power and their limits, and it predicts a sharp separation: on the k-hop induction heads task, transformers succeed with depth logarithmic in k, while recurrent models, state-space models like Mamba, and efficient attention approximations all need depth linear in k.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_equivalence_explains_both_their_powe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords equivalence, explains, both, their, power, their in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_trained_transformers_obey_predicted`

- Preferred role: `method`
- Cue keywords: `trained, transformers, obey, predicted, threshold, layer, real, edge, transformer, not`
- Narration: Trained transformers obey the predicted threshold to the layer. So the real edge of the transformer is not just scale, it is the ability to do many things at once.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_trained_transformers_obey_predicted" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trained, transformers, obey, predicted, threshold, layer in title/desc so the matcher can verify semantic overlap.
