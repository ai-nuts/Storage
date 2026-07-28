# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_cabinet_framework_table_question_ans`

- Preferred role: `title`
- Cue keywords: `cabinet, framework, table, question, answering, published, iclr, 2024, researchers, adobe`
- Narration: This is CABINET, a framework for table question answering published at ICLR 2024 by researchers at Adobe's MDSR Lab together with IIT Kharagpur and IIT Roorkee.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c1_cabinet_framework_table_question_ans" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cabinet, framework, table, question, answering, published in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_large_language_models_reason_over`

- Preferred role: `result`
- Cue keywords: `large, language, models, reason, over, tables, but, only, few, cells`
- Narration: Large language models reason over tables, but only a few cells usually matter for any given question, and the irrelevant cells act as noise that hurts accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c2_large_language_models_reason_over" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, language, models, reason, over, tables in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_cabinet_tackles_teaching_focus_relev`

- Preferred role: `content`
- Cue keywords: `cabinet, tackles, teaching, focus, relevant, table, content, suppress, rest, rather`
- Narration: CABINET tackles this by teaching the model to focus on relevant table content and suppress the rest, rather than deleting parts of the table outright.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_cabinet_tackles_teaching_focus_relev" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cabinet, tackles, teaching, focus, relevant, table in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_sets_new_state_art_three`

- Preferred role: `result`
- Cue keywords: `sets, new, state, art, three, challenging, table, benchmarks`
- Narration: It sets new state of the art on three challenging table QA benchmarks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_sets_new_state_art_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sets, new, state, art, three, challenging in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_tables_organize_information_across_r`

- Preferred role: `method`
- Cue keywords: `tables, organize, information, across, rows, columns, but, any, single, question`
- Narration: Tables organize information across rows and columns, but for any single question only a small number of cells actually contain the answer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_tables_organize_information_across_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tables, organize, information, across, rows, columns in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_everything_else_irrelevant_question`

- Preferred role: `title`
- Cue keywords: `everything, else, irrelevant, question, behaves, like, noise`
- Narration: Everything else is irrelevant to that question and behaves like noise.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c2_everything_else_irrelevant_question" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords everything, else, irrelevant, question, behaves, like in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_large_language_models_known_suscepti`

- Preferred role: `method`
- Cue keywords: `large, language, models, known, susceptible, such, distracting, information, their, table`
- Narration: Large language models are known to be susceptible to such distracting information, so their table reasoning degrades, and the problem gets worse as tables grow larger and carry even more irrelevant content.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_large_language_models_known_suscepti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, language, models, known, susceptible, such in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_cabinet_built_address_exactly_vulner`

- Preferred role: `content`
- Cue keywords: `cabinet, built, address, exactly, vulnerability`
- Narration: CABINET is built to address exactly this vulnerability.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_cabinet_built_address_exactly_vulner" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cabinet, built, address, exactly, vulnerability in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_natural_way_reduce_noise_shrink`

- Preferred role: `method`
- Cue keywords: `natural, way, reduce, noise, shrink, table, before, answering, methods, like`
- Narration: A natural way to reduce noise is to shrink the table before answering, and methods like DATER do this by decomposing the table into a smaller sub-table.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_natural_way_reduce_noise_shrink" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords natural, way, reduce, noise, shrink, table in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_trouble_hard_decomposition_unforgivi`

- Preferred role: `title`
- Cue keywords: `trouble, hard, decomposition, unforgiving, wrong, sub-table, extracted, useful, information, permanently`
- Narration: The trouble is that hard decomposition is unforgiving: if the wrong sub-table is extracted, useful information is permanently lost and the reasoner answers incorrectly with no way to recover.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c2_trouble_hard_decomposition_unforgivi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trouble, hard, decomposition, unforgiving, wrong, sub-table in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_cabinet_argues_softer_approach_weigh`

- Preferred role: `title`
- Cue keywords: `cabinet, argues, softer, approach, weighs, relevant, parts, higher, without, ever`
- Narration: CABINET argues for a softer approach that weighs relevant parts higher without ever explicitly removing content, so the answering model retains access to the whole table while being steered toward what matters.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c3_cabinet_argues_softer_approach_weigh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cabinet, argues, softer, approach, weighs, relevant in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_contributes_cabinet_short_content_re`

- Preferred role: `content`
- Cue keywords: `contributes, cabinet, short, content, relevance-based, noise, reduction, two, cooperating, parts`
- Narration: The paper contributes CABINET, short for Content Relevance-Based Noise Reduction. It has two cooperating parts.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_contributes_cabinet_short_content_re" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contributes, cabinet, short, content, relevance-based, noise in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_unsupervised_relevance_scorer`

- Preferred role: `method`
- Cue keywords: `first, unsupervised, relevance, scorer, assigns, soft, relevance, weight, every, table`
- Narration: First, an Unsupervised Relevance Scorer assigns a soft relevance weight to every table token and is trained differentiably alongside the question-answering model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_unsupervised_relevance_scorer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, unsupervised, relevance, scorer, assigns, soft in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_weakly_supervised_module_gene`

- Preferred role: `content`
- Cue keywords: `second, weakly-supervised, module, generates, parsing, statement, describing, which, rows, columns`
- Narration: Second, a weakly-supervised module generates a parsing statement describing which rows and columns matter, then highlights the corresponding cells to produce a cell-based relevance signal.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_second_weakly_supervised_module_gene" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, weakly-supervised, module, generates, parsing, statement in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_together_they_let_focus_without`

- Preferred role: `method`
- Cue keywords: `together, they, let, focus, without, discarding, content, they, deliver, new`
- Narration: Together they let the model focus without discarding content, and they deliver new state of the art on three benchmarks along with stronger robustness to noise and to large tables.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_together_they_let_focus_without" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, they, let, focus, without, discarding in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_cabinet_works_sequence_steps_table`

- Preferred role: `method`
- Cue keywords: `cabinet, works, sequence, steps, table, flattened, linear, string, header, row`
- Narration: CABINET works in a sequence of steps. The table is flattened into a linear string with header and row markers and embedded together with the question. An Unsupervised Relevance Scorer, a transformer encoder, reads this and predicts a relevance score for each table token.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_cabinet_works_sequence_steps_table" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cabinet, works, sequence, steps, table, flattened in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_because_ground_truth_annotations_whi`

- Preferred role: `method`
- Cue keywords: `because, ground-truth, annotations, which, cells, relevant, relevance, treated, latent, variable`
- Narration: Because there are no ground-truth annotations for which cells are relevant, relevance is treated as a latent variable estimated through variational inference, and the encoder's representation space is shaped by a clustering loss that groups tokens into relevant and non-relevant, a separation loss that pushes the two cluster centroids apart, and a sparsification loss that drives irrelevant scores toward zero and relevant scores toward one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_because_ground_truth_annotations_whi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, ground-truth, annotations, which, cells, relevant in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_table_token_embedding_multiplied_its`

- Preferred role: `method`
- Cue keywords: `table, token, embedding, multiplied, its, relevance, score, noisy, cells, softly`
- Narration: Each table token's embedding is multiplied by its relevance score, so noisy cells are softly suppressed rather than deleted, and the whole system trains end-to-end through the answer-generation cross-entropy loss.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_table_token_embedding_multiplied_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords table, token, embedding, multiplied, its, relevance in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_parallel_weakly_supervised_parsing_s`

- Preferred role: `method`
- Cue keywords: `parallel, weakly-supervised, parsing, statement, generator, fine-tuned, flan, t5-xl, bootstrapped, only`
- Narration: In parallel a weakly-supervised Parsing Statement Generator, a fine-tuned Flan T5-xl bootstrapped from only about three hundred manual annotations, writes a natural-language description of which rows and columns are relevant, and a cell highlighter turns that into a cell-based relevance score. The unsupervised and cell-based scores are linearly combined into the final weight applied to the table.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_parallel_weakly_supervised_parsing_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords parallel, weakly-supervised, parsing, statement, generator, fine-tuned in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_cabinet_evaluated_three_challenging`

- Preferred role: `result`
- Cue keywords: `cabinet, evaluated, three, challenging, table, question-answering, benchmarks`
- Narration: CABINET is evaluated on three challenging table question-answering benchmarks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_cabinet_evaluated_three_challenging" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cabinet, evaluated, three, challenging, table, question-answering in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_wikitablequestions_wikitq_requires_c`

- Preferred role: `method`
- Cue keywords: `wikitablequestions, wikitq, requires, compositional, reasoning, over, tables, short, one-to-two-word, answers`
- Narration: WikiTableQuestions, or WikiTQ, requires compositional reasoning over tables and uses short one-to-two-word answers scored by exact-match accuracy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_wikitablequestions_wikitq_requires_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords wikitablequestions, wikitq, requires, compositional, reasoning, over in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_wikisql_similarly_exact_match_accura`

- Preferred role: `method`
- Cue keywords: `wikisql, similarly, exact-match, accuracy, fetaqa, asks, long, free-form, descriptive, answers`
- Narration: WikiSQL similarly uses exact-match accuracy. FeTaQA asks for long, free-form descriptive answers, which are scored with Sacre-BLEU.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_wikisql_similarly_exact_match_accura" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords wikisql, similarly, exact-match, accuracy, fetaqa, asks in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_authors_additionally_release_small_d`

- Preferred role: `method`
- Cue keywords: `authors, additionally, release, small, dataset, about, three, hundred, manually, written`
- Narration: The authors additionally release a small dataset of about three hundred manually written parsing statements used to bootstrap the weakly-supervised cell-highlighting module.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_authors_additionally_release_small_d" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, additionally, release, small, dataset, about in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_cabinet_establishes_new_state_art`

- Preferred role: `result`
- Cue keywords: `cabinet, establishes, new, state, art, all, three, benchmarks`
- Narration: CABINET establishes new state of the art on all three benchmarks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_cabinet_establishes_new_state_art" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cabinet, establishes, new, state, art, all in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_wikitq_reaches_sixty_nine_point_one`

- Preferred role: `method`
- Cue keywords: `wikitq, reaches, sixty-nine, point, one, percent, exact-match, accuracy, outperforming, strongest`
- Narration: On WikiTQ it reaches sixty-nine point one percent exact-match accuracy, outperforming the strongest baseline in each category, including OmniTab, DATER, and fine-tuned Flan T5-xl by six point four, three point two, and four point seven absolute percentage points, and it beats much larger GPT-3 and Codex based in-context learning methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_wikitq_reaches_sixty_nine_point_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords wikitq, reaches, sixty-nine, point, one, percent in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_fetaqa_achieves_sacre_bleu_forty_poi`

- Preferred role: `result`
- Cue keywords: `fetaqa, achieves, sacre-bleu, forty, point, five, wikisql, reaches, eighty-nine, point`
- Narration: On FeTaQA it achieves a Sacre-BLEU of forty point five, and on WikiSQL it reaches eighty-nine point five percent accuracy, pushing past the previous best.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_fetaqa_achieves_sacre_bleu_forty_poi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fetaqa, achieves, sacre-bleu, forty, point, five in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_notably_all_achieved_compact_five`

- Preferred role: `content`
- Cue keywords: `notably, all, achieved, compact, five, hundred, sixty, million, parameter`
- Narration: Notably all of this is achieved with a compact five hundred sixty million parameter model.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_notably_all_achieved_compact_five" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords notably, all, achieved, compact, five, hundred in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_confirm_both_components_ne`

- Preferred role: `content`
- Cue keywords: `ablations, confirm, both, components, needed`
- Narration: Ablations confirm both components are needed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablations_confirm_both_components_ne" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, confirm, both, components, needed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_unsupervised_relevance_scorer_applyi`

- Preferred role: `method`
- Cue keywords: `unsupervised, relevance, scorer, applying, clustering, centroid-separation, sparsification, losses, together, lifts`
- Narration: For the Unsupervised Relevance Scorer, applying clustering, centroid-separation, and sparsification losses together lifts WikiTQ accuracy from sixty point eight to sixty-five point six percent, whereas any subset gives little benefit, showing the three losses only help in combination.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_unsupervised_relevance_scorer_applyi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unsupervised, relevance, scorer, applying, clustering, centroid-separation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_two_relevance_signals_fusing_unsuper`

- Preferred role: `method`
- Cue keywords: `two, relevance, signals, fusing, unsupervised, score, weight, zero, point, seven`
- Narration: For the two relevance signals, fusing the unsupervised score at weight zero point seven with the cell-based score at weight zero point three is optimal, giving sixty-nine point one percent on WikiTQ.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_two_relevance_signals_fusing_unsuper" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, relevance, signals, fusing, unsupervised, score in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_relying_cell_based_signal_alone_coll`

- Preferred role: `method`
- Cue keywords: `relying, cell-based, signal, alone, collapses, accuracy, thirty-seven, point, six, percent`
- Narration: Relying on the cell-based signal alone collapses accuracy to thirty-seven point six percent, confirming the unsupervised scorer is the primary driver and the parsing-statement module is a complementary aid.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_relying_cell_based_signal_alone_coll" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords relying, cell-based, signal, alone, collapses, accuracy in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_numbers_sixty_nine_point_on`

- Preferred role: `result`
- Cue keywords: `headline, numbers, sixty-nine, point, one, percent, accuracy, wikitq, sacre-bleu, forty`
- Narration: The headline numbers are sixty-nine point one percent accuracy on WikiTQ, a Sacre-BLEU of forty point five on FeTaQA, and eighty-nine point five percent accuracy on WikiSQL, each a new state of the art achieved with just five hundred sixty million parameters.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_headline_numbers_sixty_nine_point_on" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, numbers, sixty-nine, point, one, percent in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_beyond_raw_accuracy_cabinet_markedly`

- Preferred role: `result`
- Cue keywords: `beyond, raw, accuracy, cabinet, markedly, more, robust, under, table, perturbations`
- Narration: Beyond raw accuracy, CABINET is markedly more robust: under table perturbations such as row and column permutation and cell replacement it degrades far less than baselines, with roughly an eleven and a half percent smaller performance drop than OmniTab on WikiTQ, and it holds its advantage as tables grow larger.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_beyond_raw_accuracy_cabinet_markedly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beyond, raw, accuracy, cabinet, markedly, more in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_core_lesson_cabinet_you_not`

- Preferred role: `title`
- Cue keywords: `core, lesson, cabinet, you, not, need, cut, table, down, answer`
- Narration: The core lesson of CABINET is that you do not need to cut a table down to answer questions about it.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s10_c1_core_lesson_cabinet_you_not" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, lesson, cabinet, you, not, need in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_softly_weighting_every_cell_accordin`

- Preferred role: `method`
- Cue keywords: `softly, weighting, every, cell, according, learned, relevance, score, instead, hard-decomposing`
- Narration: By softly weighting every cell according to a learned relevance score, instead of hard-decomposing the table and risking the loss of useful information, the model keeps full access to the data while being steered toward what matters.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_softly_weighting_every_cell_accordin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords softly, weighting, every, cell, according, learned in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_pairing_differentiable_unsupervised`

- Preferred role: `method`
- Cue keywords: `pairing, differentiable, unsupervised, relevance, scorer, weakly-supervised, parsing-statement, cell, highlighter, yields`
- Narration: Pairing a differentiable unsupervised relevance scorer with a weakly-supervised parsing-statement cell highlighter yields both higher accuracy and greater robustness to noise, setting new state of the art on three table QA benchmarks with a compact five hundred sixty million parameter model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_pairing_differentiable_unsupervised" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pairing, differentiable, unsupervised, relevance, scorer, weakly-supervised in title/desc so the matcher can verify semantic overlap.
