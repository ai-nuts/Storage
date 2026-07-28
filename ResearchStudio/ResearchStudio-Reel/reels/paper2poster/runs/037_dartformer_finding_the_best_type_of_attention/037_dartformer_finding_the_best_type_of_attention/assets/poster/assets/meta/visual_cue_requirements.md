# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_how_you_pick_right_attention`

- Preferred role: `method`
- Cue keywords: `how, you, pick, right, attention, mechanism, long-range, transformer, task, could`
- Narration: How do you pick the right attention mechanism for a long-range Transformer task, and could mixing several types work even better?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_how_you_pick_right_attention" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, you, pick, right, attention, mechanism in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_dartformer_adapts_differentiable_neu`

- Preferred role: `figure`
- Cue keywords: `dartformer, adapts, differentiable, neural, architecture, search, answer, both, questions`
- Narration: This paper, DARTFormer, adapts differentiable neural architecture search to answer both questions.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c2_dartformer_adapts_differentiable_neu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dartformer, adapts, differentiable, neural, architecture, search in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_build_supernetwork_contains`

- Preferred role: `method`
- Cue keywords: `authors, build, supernetwork, contains, many, efficient, attention, types, parallel, masked`
- Narration: The authors build a supernetwork that contains many efficient attention types in parallel, then use a masked validation accuracy drop metric to rank them.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_authors_build_supernetwork_contains" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, build, supernetwork, contains, many, efficient in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_their_search_reliably_finds_best`

- Preferred role: `method`
- Cue keywords: `their, search, reliably, finds, best, single, attention, task, but, surprising`
- Narration: Their search reliably finds the best single attention for a task, but a surprising second result emerges: heterogeneous Transformers that combine several attention types beat the average homogeneous model, yet never beat the single best one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_their_search_reliably_finds_best" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords their, search, reliably, finds, best, single in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_transformer_original_dot_product_att`

- Preferred role: `method`
- Cue keywords: `transformer, original, dot-product, attention, scales, quadratically, sequence, length, large, family`
- Narration: The Transformer's original dot-product attention scales quadratically with sequence length, so a large family of efficient alternatives has appeared, from Longformer and Bigbird to Performer, Reformer, and Synthesizer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_transformer_original_dot_product_att" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords transformer, original, dot-product, attention, scales, quadratically in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_catch_single_one_wins_everywhere`

- Preferred role: `method`
- Cue keywords: `catch, single, one, wins, everywhere, earlier, long-range, benchmarking, showed, best`
- Narration: The catch is that no single one wins everywhere: earlier long-range benchmarking showed that the best attention depends heavily on the task when there is no pretraining.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_catch_single_one_wins_everywhere" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords catch, single, one, wins, everywhere, earlier in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_leaves_practitioners_awkward_questio`

- Preferred role: `method`
- Cue keywords: `leaves, practitioners, awkward, question, namely, how, efficiently, discover, which, attention`
- Narration: That leaves practitioners with an awkward question, namely how to efficiently discover which attention is right for a given long-range task without simply training all of them.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_leaves_practitioners_awkward_questio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords leaves, practitioners, awkward, question, namely, how in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_long_standing_intuition_attention_he`

- Preferred role: `method`
- Cue keywords: `long-standing, intuition, attention, head, specialize, learning, different, kind, relationship, much`
- Narration: There is a long-standing intuition that each attention head can specialize, learning a different kind of relationship, much as convolutional kernels learn different features.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_long_standing_intuition_attention_he" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords long-standing, intuition, attention, head, specialize, learning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_true_transformer_mixing_several_atte`

- Preferred role: `method`
- Cue keywords: `true, transformer, mixing, several, attention, types, could, learn, richer, set`
- Narration: If that is true, then a Transformer mixing several attention types could learn a richer set of relationships and outperform any single-attention model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_true_transformer_mixing_several_atte" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords true, transformer, mixing, several, attention, types in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_takes_intuition_seriously_asks_direc`

- Preferred role: `method`
- Cue keywords: `takes, intuition, seriously, asks, directly, whether, optimal, attention, task, actually`
- Narration: This paper takes that intuition seriously and asks directly whether the optimal attention for a task is actually a mixture of different attentions, rather than assuming the answer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_takes_intuition_seriously_asks_direc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takes, intuition, seriously, asks, directly, whether in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_proposes_dartformer_differenti`

- Preferred role: `method`
- Cue keywords: `first, proposes, dartformer, differentiable-architecture-search-style, method, efficiently, finds, best, attention, task`
- Narration: First, it proposes DARTFormer, a differentiable-architecture-search-style method that efficiently finds the best attention for a task.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_proposes_dartformer_differenti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, proposes, dartformer, differentiable-architecture-search-style, method, efficiently in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_extends_framework_build_searc`

- Preferred role: `method`
- Cue keywords: `second, extends, framework, build, search, heterogeneous, transformers, combine, multiple, attention`
- Narration: Second, it extends that framework to build and search for heterogeneous Transformers that combine multiple attention types, using two procedures: an expensive iterative pruning method they call NAS Prune, and a cheap single-pass method called NAS One-shot.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_extends_framework_build_searc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, extends, framework, build, search, heterogeneous in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_most_importantly_shows_empiric`

- Preferred role: `method`
- Cue keywords: `third, most, importantly, shows, empirically, these, heterogeneous, transformers, cannot, outperform`
- Narration: Third, and most importantly, it shows empirically that these heterogeneous Transformers cannot outperform the best homogeneous Transformer on the long-range NLP tasks studied.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_most_importantly_shows_empiric" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, most, importantly, shows, empirically, these in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_dartformer_builds_single_layer_super`

- Preferred role: `method`
- Cue keywords: `dartformer, builds, single-layer, supernetwork, holds, one, candidate, block, every, efficient`
- Narration: DARTFormer builds a single-layer supernetwork that holds one candidate block for every efficient attention type in parallel.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_dartformer_builds_single_layer_super" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dartformer, builds, single-layer, supernetwork, holds, one in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_borrowing_fixed_alpha_trick_differen`

- Preferred role: `result`
- Cue keywords: `borrowing, fixed-alpha, trick, differentiable, architecture, search, does, not, learn, softmax`
- Narration: Borrowing the fixed-alpha trick from differentiable architecture search, it does not learn softmax edge weights and skips bi-level optimization; instead it simply averages the candidate block outputs, which lets the supernetwork train all the way to convergence.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c2_borrowing_fixed_alpha_trick_differen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords borrowing, fixed-alpha, trick, differentiable, architecture, search in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_rank_attentions_masked_validation_ac`

- Preferred role: `method`
- Cue keywords: `rank, attentions, masked, validation, accuracy, drop, metric, mask, out, one`
- Narration: To rank the attentions, it uses a masked validation accuracy drop metric: mask out one block, measure how far validation accuracy falls, and the block whose removal hurts the most is judged the best.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_rank_attentions_masked_validation_ac" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rank, attentions, masked, validation, accuracy, drop in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_homogeneous_models_top_scoring_block`

- Preferred role: `method`
- Cue keywords: `homogeneous, models, top-scoring, block, chosen, heterogeneous, ones, blocks, either, pruned`
- Narration: For homogeneous models the top-scoring block is chosen; for heterogeneous ones, blocks are either pruned worst-first with fine-tuning, or the top four are taken directly and stacked into a full Transformer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_homogeneous_models_top_scoring_block" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords homogeneous, models, top-scoring, block, chosen, heterogeneous in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_all_experiments_run_three_tasks`

- Preferred role: `method`
- Cue keywords: `all, experiments, run, three, tasks, drawn, long, range, arena, benchmark`
- Narration: All experiments run on three tasks drawn from the Long Range Arena benchmark, chosen to stress long-sequence modeling.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_all_experiments_run_three_tasks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, experiments, run, three, tasks, drawn in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_these_byte_level_binary_text_classif`

- Preferred role: `result`
- Cue keywords: `these, byte-level, binary, text, classification, imdb, sequences, one, thousand, tokens`
- Narration: These are byte-level binary text classification on IMDb with sequences of one thousand tokens, ListOps ten-way classification with two-thousand-token sequences, and byte-level document matching with four-thousand-token sequences.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_these_byte_level_binary_text_classif" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, byte-level, binary, text, classification, imdb in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_search_considers_nine_candidate_atte`

- Preferred role: `method`
- Cue keywords: `search, considers, nine, candidate, attention, mechanisms, including, bigbird, linear, transformer`
- Narration: The search considers nine candidate attention mechanisms, including Bigbird, Linear Transformer, Linformer, Local attention, Longformer, Performer, Reformer, Sparse Transformer, and Synthesizer, with hyperparameters largely matching the original Long Range Arena setup.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_search_considers_nine_candidate_atte" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords search, considers, nine, candidate, attention, mechanisms in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_splits_two`

- Preferred role: `content`
- Cue keywords: `headline, finding, splits, two`
- Narration: The headline finding splits in two.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_headline_finding_splits_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, splits, two in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_positive_side_masked_validation_drop`

- Preferred role: `method`
- Cue keywords: `positive, side, masked-validation-drop, search, genuinely, effective, homogeneous, selection, correctly, identifies`
- Narration: On the positive side, the masked-validation-drop search is genuinely effective at homogeneous selection: it correctly identifies the best attention for text classification and for ListOps, where Reformer stands out with a drop score of nearly twelve while every other attention scores below half a point.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_positive_side_masked_validation_drop" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords positive, side, masked-validation-drop, search, genuinely, effective in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_negative_side_when_authors_assemble`

- Preferred role: `method`
- Cue keywords: `negative, side, when, authors, assemble, heterogeneous, transformers, mix, several, attention`
- Narration: On the negative side, when the authors assemble heterogeneous Transformers that mix several attention types, none of them beats the best single-attention model on any of the three tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_negative_side_when_authors_assemble" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords negative, side, when, authors, assemble, heterogeneous in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_mixing_attention_helps_you_beat`

- Preferred role: `method`
- Cue keywords: `mixing, attention, helps, you, beat, average, choice, but, not, best`
- Narration: Mixing attention helps you beat the average choice, but not the best one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_mixing_attention_helps_you_beat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mixing, attention, helps, you, beat, average in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_useful_practical_takeaway_comes_comp`

- Preferred role: `takeaway`
- Cue keywords: `useful, practical, takeaway, comes, comparing, two, heterogeneous, search, procedures`
- Narration: A useful practical takeaway comes from comparing the two heterogeneous search procedures.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s08_c1_useful_practical_takeaway_comes_comp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords useful, practical, takeaway, comes, comparing, two in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_expensive_nas_prune_method_which`

- Preferred role: `method`
- Cue keywords: `expensive, nas, prune, method, which, repeatedly, removes, worst, block, fine-tunes`
- Narration: The expensive NAS Prune method, which repeatedly removes the worst block and fine-tunes, offers no consistent advantage over the far cheaper NAS One-shot method that just takes the top-scoring attentions in a single pass, at least when good attentions are correctly identified.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_expensive_nas_prune_method_which" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords expensive, nas, prune, method, which, repeatedly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_attempts_tilt_mixture_toward_stronge`

- Preferred role: `method`
- Cue keywords: `attempts, tilt, mixture, toward, strongest, attentions, give, them, more, heads`
- Narration: Attempts to tilt the mixture toward the strongest attentions or give them more heads also failed to produce consistent gains, reinforcing that the cheap method is good enough.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_attempts_tilt_mixture_toward_stronge" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords attempts, tilt, mixture, toward, strongest, attentions in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_put_concrete_numbers_listops_reforme`

- Preferred role: `method`
- Cue keywords: `put, concrete, numbers, listops, reformer, earns, masked-validation-drop, score, eleven, point`
- Narration: To put concrete numbers on it: on ListOps, Reformer earns a masked-validation-drop score of eleven point eight five, dwarfing every other attention's score of under half a point, a strikingly clean selection signal.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_put_concrete_numbers_listops_reforme" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords put, concrete, numbers, listops, reformer, earns in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_document_matching_best_homogeneous_s`

- Preferred role: `result`
- Cue keywords: `document, matching, best, homogeneous, synthesizer, reaches, seventy-one, point, one, percent`
- Narration: On document matching, the best homogeneous model, Synthesizer, reaches seventy-one point one percent, while the heterogeneous NAS Prune and NAS One-shot models trail at sixty-seven and sixty-four point seven percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_document_matching_best_homogeneous_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords document, matching, best, homogeneous, synthesizer, reaches in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_text_classification_best_homogeneous`

- Preferred role: `result`
- Cue keywords: `text, classification, best, homogeneous, performer, hits, sixty-four, point, five, percent`
- Narration: On text classification the best homogeneous Performer hits sixty-four point five percent, and again neither heterogeneous variant edges ahead.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_text_classification_best_homogeneous" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords text, classification, best, homogeneous, performer, hits in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_across_nine_attention_mechanisms_thr`

- Preferred role: `method`
- Cue keywords: `across, nine, attention, mechanisms, three, tasks, pattern, consistent`
- Narration: Across nine attention mechanisms and three tasks, the pattern is consistent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_across_nine_attention_mechanisms_thr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, nine, attention, mechanisms, three, tasks in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_given_task_often_unclear_which`

- Preferred role: `method`
- Cue keywords: `given, task, often, unclear, which, attention, will, best, dartformer, offers`
- Narration: For a given task it is often unclear which attention will do best, and DARTFormer offers a cheap, reliable recipe: train a single-layer mixed-attention Transformer and use masked validation accuracy drop to pick the winner, keeping in mind that very low drop scores are a warning that the choice may be unreliable.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_given_task_often_unclear_which" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords given, task, often, unclear, which, attention in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_deeper_lesson_cautionary_one_field`

- Preferred role: `content`
- Cue keywords: `deeper, lesson, cautionary, one, field`
- Narration: The deeper lesson is a cautionary one for the field.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_deeper_lesson_cautionary_one_field" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deeper, lesson, cautionary, one, field in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_combining_diverse_attention_mechanis`

- Preferred role: `method`
- Cue keywords: `combining, diverse, attention, mechanisms, does, beat, average, single, choice, but`
- Narration: Combining diverse attention mechanisms does beat the average single choice, but it never beats the best single choice, which suggests the different attentions do not simply add complementary biases the way common intuition assumes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_combining_diverse_attention_mechanis" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords combining, diverse, attention, mechanisms, does, beat in title/desc so the matcher can verify semantic overlap.
