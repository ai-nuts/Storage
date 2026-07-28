# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_most_visual_question_answering_model`

- Preferred role: `title`
- Cue keywords: `most, visual, question, answering, models, black, boxes, they, output, answer`
- Narration: Most visual question answering models are black boxes: they output an answer, but not the reasoning that produced it.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c1_most_visual_question_answering_model" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, visual, question, answering, models, black in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_towards_reasoning_aware_explainable`

- Preferred role: `result`
- Cue keywords: `towards, reasoning-aware, explainable, vqa, university, illinois, amazon, alexa, augments, state-of-the-art`
- Narration: This paper, Towards Reasoning-Aware Explainable VQA from the University of Illinois and Amazon Alexa AI, augments a state-of-the-art coarse-to-fine VQA backbone with an end-to-end explanation generation module, so the model produces a human-readable textual explanation alongside every answer while keeping accuracy essentially unchanged.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c2_towards_reasoning_aware_explainable" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords towards, reasoning-aware, explainable, vqa, university, illinois in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_compares_lstm_transformer_decoders_e`

- Preferred role: `method`
- Cue keywords: `compares, lstm, transformer, decoders, explanation, generator, crucially, shows, through, large`
- Narration: It compares LSTM and Transformer decoders as the explanation generator, and, crucially, shows through a large human study that the standard string-matching metrics like BLEU and ROUGE are unreliable for judging explanations, motivating better evaluation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_compares_lstm_transformer_decoders_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords compares, lstm, transformer, decoders, explanation, generator in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_classic_visual_question_answering_ta`

- Preferred role: `method`
- Cue keywords: `classic, visual, question, answering, task, takes, image, question, returns, answer`
- Narration: In the classic visual question answering task, a model takes an image and a question and returns an answer. The field has poured enormous effort into raising accuracy, thanks to large pre-trained vision-language models, but almost no attention is paid to how a model actually reaches its answer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_classic_visual_question_answering_ta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classic, visual, question, answering, task, takes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_result_black_box_prediction_right`

- Preferred role: `result`
- Cue keywords: `result, black, box, prediction, right, yet, evidence, explaining, reasoning, behind`
- Narration: The result is a black box: the prediction may be right, yet there is no evidence explaining the reasoning behind it.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c2_result_black_box_prediction_right" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, black, box, prediction, right, yet in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_authors_distinguish_three_kinds_mode`

- Preferred role: `title`
- Cue keywords: `authors, distinguish, three, kinds, models, those, give, only, answer, those`
- Narration: The authors distinguish three kinds of models: those that give only an answer, those that add a generic caption of the image, and the rare third kind that produces a logically self-contained explanation matching the answer.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c3_authors_distinguish_three_kinds_mode" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, distinguish, three, kinds, models, those in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_almost_all_state_of_the_art_vqa_mode`

- Preferred role: `content`
- Cue keywords: `almost, all, state-of-the-art, vqa, models, fall, first, two, categories, which`
- Narration: Almost all state-of-the-art VQA models fall into the first two categories, which motivates this work.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_almost_all_state_of_the_art_vqa_mode" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords almost, all, state-of-the-art, vqa, models, fall in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_two_open_questions_drive_first`

- Preferred role: `result`
- Cue keywords: `two, open, questions, drive, first, vqa, generate, human-readable, explanation, while`
- Narration: Two open questions drive the paper. First, can a VQA model generate a human-readable explanation while still maintaining its answer accuracy?
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c1_two_open_questions_drive_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, open, questions, drive, first, vqa in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_second_how_good_those_generated`

- Preferred role: `content`
- Cue keywords: `second, how, good, those, generated, explanations, how, should, even, evaluate`
- Narration: Second, how good are those generated explanations, and how should we even evaluate them?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_second_how_good_those_generated" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, how, good, those, generated, explanations in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_existing_explainable_vqa_datasets_su`

- Preferred role: `method`
- Cue keywords: `existing, explainable-vqa, datasets, suggest, conventional, natural, language, metrics, such, bleu`
- Narration: Existing explainable-VQA datasets suggest using conventional natural language metrics such as BLEU and ROUGE, but these were designed for string matching over overlapping n-grams, not for judging whether an explanation truly supports an answer.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_existing_explainable_vqa_datasets_su" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, explainable-vqa, datasets, suggest, conventional, natural in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_authors_argue_reasoning_problems_vqa`

- Preferred role: `content`
- Cue keywords: `authors, argue, reasoning, problems, vqa, grow, more, complex, having, interpretable`
- Narration: The authors argue that as reasoning problems in VQA grow more complex, having an interpretable, well-evaluated explanation is no longer optional but urgent.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_authors_argue_reasoning_problems_vqa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, reasoning, problems, vqa, grow in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_contribution_two_fold`

- Preferred role: `content`
- Cue keywords: `contribution, two-fold`
- Narration: The contribution is two-fold.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_contribution_two_fold" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contribution, two-fold in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_authors_present_simple_easy_to`

- Preferred role: `method`
- Cue keywords: `first, authors, present, simple, easy-to-implement, methods, sit, top, state-of-the-art, vqa`
- Narration: First, the authors present simple, easy-to-implement methods that sit on top of a state-of-the-art VQA framework and maintain VQA accuracy while generating human-readable textual explanations.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_authors_present_simple_easy_to" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, authors, present, simple, easy-to-implement, methods in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_they_provide_both_quantitativ`

- Preferred role: `method`
- Cue keywords: `second, they, provide, both, quantitative, experimental, results, large, human, study`
- Narration: Second, they provide both quantitative experimental results and a large human study of the proposed explainable VQA method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_they_provide_both_quantitativ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, they, provide, both, quantitative, experimental in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_together_these_illustrate_urgency_pr`

- Preferred role: `method`
- Cue keywords: `together, these, illustrate, urgency, proposing, new, metrics, evaluate, predicted, explanations`
- Narration: Together these illustrate the urgency of proposing new metrics to evaluate predicted explanations in vision-language reasoning problems like VQA, since the metrics in common use today do not reliably reflect explanation quality.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_together_these_illustrate_urgency_pr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, these, illustrate, urgency, proposing, new in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_architecture_two_major_parts_coarse`

- Preferred role: `method`
- Cue keywords: `architecture, two, major, parts, coarse-to-fine, visual-language, reasoning, answer, explanation, generation`
- Narration: The architecture has two major parts: coarse-to-fine visual-language reasoning for the answer, and an explanation generation module. A pre-trained Faster-RCNN extracts region-of-interest features and image predicates such as object and attribute labels, which are embedded with GloVe. The question is encoded with GloVe embeddings passed through a GRU, and question predicates are extracted by filtering out stop words.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_architecture_two_major_parts_coarse" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords architecture, two, major, parts, coarse-to-fine, visual-language in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_these_signals_flow_through_three`

- Preferred role: `method`
- Cue keywords: `these, signals, flow, through, three, modules, information, filtering, which, removes`
- Narration: These signals flow through three modules: information filtering, which removes noisy region information; multimodal learning, which uses bilinear attention networks to fuse image and question at both coarse and fine granularity; and semantic reasoning, which combines the two levels into a joint embedding.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_these_signals_flow_through_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, signals, flow, through, three, modules in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_joint_embedding_sent_both_multi_laye`

- Preferred role: `method`
- Cue keywords: `joint, embedding, sent, both, multi-layer, perceptron, answer, prediction, explanation, generator`
- Narration: That joint embedding is sent both to a multi-layer perceptron for answer prediction and to the explanation generator. Two generator architectures are studied, a two-layer LSTM and an eight-head Transformer decoder, each trained with autoregressive cross-entropy loss and teacher forcing on ground-truth explanations.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_joint_embedding_sent_both_multi_laye" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords joint, embedding, sent, both, multi-layer, perceptron in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_whole_system_trained_end_to_end_comb`

- Preferred role: `method`
- Cue keywords: `whole, system, trained, end-to-end, combined, loss, balances, answer, term, explanation`
- Narration: The whole system is trained end-to-end with a combined loss that balances the answer term and the explanation term through a factor alpha.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_whole_system_trained_end_to_end_comb" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords whole, system, trained, end-to-end, combined, loss in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_because_very_few_datasets_provide`

- Preferred role: `title`
- Cue keywords: `because, very, few, datasets, provide, annotated, explanations, alongside, answers, authors`
- Narration: Because very few datasets provide annotated explanations alongside answers, the authors chose the two largest available.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c1_because_very_few_datasets_provide" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, very, few, datasets, provide, annotated in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_gqa_rex_contains_explanations_roughl`

- Preferred role: `title`
- Cue keywords: `gqa-rex, contains, explanations, roughly, ninety-eight, percent, samples, gqa-balanced, dataset, about`
- Narration: GQA-REX contains explanations for roughly ninety-eight percent of the samples in the GQA-balanced dataset, about 1.04 million question-answer pairs spanning eighty-two thousand images, with one explanation per pair.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c2_gqa_rex_contains_explanations_roughl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gqa-rex, contains, explanations, roughly, ninety-eight, percent in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_however_its_explanations_follow_reas`

- Preferred role: `content`
- Cue keywords: `however, its, explanations, follow, reasoning-format, prior, work, not, fully, human-readable`
- Narration: However, its explanations follow the reasoning-format of prior work and are not fully human-readable, sometimes containing grammatical inaccuracies.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_however_its_explanations_follow_reas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords however, its, explanations, follow, reasoning-format, prior in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_vqa_e_provides_explanations_about_fo`

- Preferred role: `title`
- Cue keywords: `vqa-e, provides, explanations, about, forty, percent, question-answer, pairs, vqa, 2.0`
- Narration: VQA-E provides explanations for about forty percent of the question-answer pairs in VQA 2.0, and because those explanations are built by matching captions to the question-answer pair, they tend to read more like image captions than genuine reasoning. Both datasets have limitations, which the authors are transparent about.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c4_vqa_e_provides_explanations_about_fo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vqa-e, provides, explanations, about, forty, percent in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_central_result_adding_explanation_ge`

- Preferred role: `result`
- Cue keywords: `central, result, adding, explanation, generation, does, not, cost, accuracy`
- Narration: The central result is that adding explanation generation does not cost accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_central_result_adding_explanation_ge" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords central, result, adding, explanation, generation, does in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_gqa_rex_reaches_vqa_score_seventy_se`

- Preferred role: `method`
- Cue keywords: `gqa-rex, reaches, vqa, score, seventy-seven, point, four, nine, percent, vqa-e`
- Narration: On GQA-REX the model reaches a VQA score of seventy-seven point four nine percent, and on VQA-E seventy-one point four eight percent, both essentially matching the baseline that was trained without any explanation supervision. Varying the balance factor alpha changes the trade-off only marginally.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_gqa_rex_reaches_vqa_score_seventy_se" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gqa-rex, reaches, vqa, score, seventy-seven, point in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_explanations_themselves_cfrf_plus_ls`

- Preferred role: `method`
- Cue keywords: `explanations, themselves, cfrf-plus-lstm, outperforms, prior, baseline, vqa-e, bleu-1, zero, point`
- Narration: For the explanations themselves, the CFRF-plus-LSTM model outperforms the prior baseline on VQA-E, with a BLEU-1 of zero point three three versus zero point two six eight and a ROUGE-L of zero point three two five versus zero point two four nine.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_explanations_themselves_cfrf_plus_ls" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords explanations, themselves, cfrf-plus-lstm, outperforms, prior, baseline in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_authors_candid_these_absolute_number`

- Preferred role: `result`
- Cue keywords: `authors, candid, these, absolute, numbers, only, satisfactory, which, sets, their`
- Narration: The authors are candid that these absolute numbers are only satisfactory, which sets up their argument about evaluation.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_authors_candid_these_absolute_number" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, candid, these, absolute, numbers, only in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_authors_ablate_two_design_choices`

- Preferred role: `result`
- Cue keywords: `authors, ablate, two, design, choices, balance, factor, alpha, weights, answer`
- Narration: The authors ablate two design choices: the balance factor alpha that weights answer loss against explanation loss, and the choice of explanation generator.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_authors_ablate_two_design_choices" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ablate, two, design, choices, balance in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_gqa_rex_lstm_variant_ranges_about`

- Preferred role: `method`
- Cue keywords: `gqa-rex, lstm, variant, ranges, about, seventy-five, seventy-seven, half, percent, across`
- Narration: On GQA-REX, the LSTM variant ranges from about seventy-five to seventy-seven and a half percent across different alpha values, and the Transformer decoder at alpha equal to one half reaches seventy-seven point zero six percent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_gqa_rex_lstm_variant_ranges_about" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gqa-rex, lstm, variant, ranges, about, seventy-five in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_vqa_e_every_configuration_lands_with`

- Preferred role: `content`
- Cue keywords: `vqa-e, every, configuration, lands, within, fraction, percent, seventy-one, half, percent`
- Narration: On VQA-E, every configuration lands within a fraction of a percent of the seventy-one and a half percent baseline.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_vqa_e_every_configuration_lands_with" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vqa-e, every, configuration, lands, within, fraction in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_takeaway_these_sweeps_answer_accurac`

- Preferred role: `method`
- Cue keywords: `takeaway, these, sweeps, answer, accuracy, remarkably, stable, matter, how, explanation`
- Narration: The takeaway from these sweeps is that answer accuracy is remarkably stable no matter how the explanation loss is weighted or which decoder architecture generates the explanation, so the explanation module can be added essentially for free.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_takeaway_these_sweeps_answer_accurac" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, these, sweeps, answer, accuracy, remarkably in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_four_numbers_summarize_impact_achiev`

- Preferred role: `method`
- Cue keywords: `four, numbers, summarize, impact, achieves, seventy-seven, point, four, nine, percent`
- Narration: Four numbers summarize the paper's impact. The model achieves a seventy-seven point four nine percent VQA score on GQA-REX and seventy-one point four eight percent on VQA-E, both at state-of-the-art level.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_four_numbers_summarize_impact_achiev" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords four, numbers, summarize, impact, achieves, seventy-seven in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_human_study_sixty_five_point_one`

- Preferred role: `title`
- Cue keywords: `human, study, sixty-five, point, one, six, percent, generated, explanations, judged`
- Narration: In the human study, sixty-five point one six percent of the generated explanations were judged by annotators to genuinely lead to the predicted answer.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s09_c2_human_study_sixty_five_point_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords human, study, sixty-five, point, one, six in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_roughly_sixty_point_five_percent`

- Preferred role: `title`
- Cue keywords: `roughly, sixty, point, five, percent, cases, both, predicts, correct, answer`
- Narration: And in roughly sixty point five percent of cases, the model both predicts the correct answer and generates a valid explanation for it.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s09_c3_roughly_sixty_point_five_percent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords roughly, sixty, point, five, percent, cases in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_human_study_itself_substantial_four`

- Preferred role: `title`
- Cue keywords: `human, study, itself, substantial, four, thousand, seven, hundred, thirty-five, unique`
- Narration: The human study itself was substantial: four thousand seven hundred thirty-five unique image-question pairs from the VQA-E validation set, each rated by three annotators, for over fourteen thousand responses from one hundred eleven subjects.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s09_c4_human_study_itself_substantial_four" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords human, study, itself, substantial, four, thousand in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_twofold`

- Preferred role: `content`
- Cue keywords: `lasting, message, twofold`
- Narration: The lasting message is twofold.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lasting_message_twofold" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, twofold in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_practically_explanation_generation_a`

- Preferred role: `result`
- Cue keywords: `practically, explanation, generation, added, state-of-the-art, vqa, backbone, almost, loss, answer`
- Narration: Practically, explanation generation can be added to a state-of-the-art VQA backbone with almost no loss in answer accuracy, giving users a human-readable reason alongside each answer.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c2_practically_explanation_generation_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords practically, explanation, generation, added, state-of-the-art, vqa in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_but_methodologically_shows_through_c`

- Preferred role: `method`
- Cue keywords: `but, methodologically, shows, through, concrete, examples, string-matching, metrics, like, bleu`
- Narration: But methodologically, the paper shows through concrete examples that string-matching metrics like BLEU and ROUGE can reward a wrong explanation and penalize a valid one, so they are unreliable for this task.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_but_methodologically_shows_through_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, methodologically, shows, through, concrete, examples in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_authors_therefore_argue_real_bottlen`

- Preferred role: `method`
- Cue keywords: `authors, therefore, argue, real, bottleneck, explainable, vqa, not, generator, but`
- Narration: The authors therefore argue that the real bottleneck for explainable VQA is not the generator but the evaluation, and they urge the community to develop proper reasoning-aware metrics for judging explanations.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_authors_therefore_argue_real_bottlen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, therefore, argue, real, bottleneck, explainable in title/desc so the matcher can verify semantic overlap.
