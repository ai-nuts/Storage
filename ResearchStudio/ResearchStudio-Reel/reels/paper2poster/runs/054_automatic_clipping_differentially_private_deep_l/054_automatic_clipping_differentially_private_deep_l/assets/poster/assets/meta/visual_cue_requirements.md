# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_work_aws_santa_barbara_titled`

- Preferred role: `method`
- Cue keywords: `work, aws, santa, barbara, titled, automatic, clipping, differentially, private, deep`
- Narration: This work, from AWS AI and UC Santa Barbara, is titled "Automatic Clipping: Differentially Private Deep Learning Made Easier and Stronger." Differentially private training of deep networks relies on per-sample gradient clipping, but the clipping threshold R is a fragile hyperparameter that must be tuned carefully for good accuracy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_work_aws_santa_barbara_titled" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, aws, santa, barbara, titled, automatic in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_propose_automatic_clipping_d`

- Preferred role: `method`
- Cue keywords: `authors, propose, automatic, clipping, drop-in, replacement, removes, entirely, any, optimizer`
- Narration: The authors propose automatic clipping, a drop-in replacement that removes R entirely from any DP optimizer, so private training becomes as tuning-friendly as ordinary training while matching or beating the state of the art.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_authors_propose_automatic_clipping_d" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, propose, automatic, clipping, drop-in, replacement in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_differentially_private_deep_learning`

- Preferred role: `result`
- Cue keywords: `differentially, private, deep, learning, every, per-sample, gradient, clipped, fixed, norm`
- Narration: In differentially private deep learning, every per-sample gradient is clipped to a fixed norm R before noise is added, and that single threshold R turns out to be decisive for accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c1_differentially_private_deep_learning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords differentially, private, deep, learning, every, per-sample in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_picking_wrong_costly_imagenet_resnet`

- Preferred role: `result`
- Cue keywords: `picking, wrong, costly, imagenet, resnet18, accuracy, collapse, forty-five, percent, thirty-one`
- Narration: Picking it wrong is costly: on ImageNet, ResNet18 accuracy can collapse from forty-five percent to thirty-one percent when R is merely doubled.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c2_picking_wrong_costly_imagenet_resnet" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords picking, wrong, costly, imagenet, resnet18, accuracy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_state_of_the_art_private_models_tend`

- Preferred role: `content`
- Cue keywords: `state-of-the-art, private, models, tend, need, very, small, clipping, thresholds, only`
- Narration: State-of-the-art private models tend to need very small clipping thresholds that can only be found through careful, expensive tuning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_state_of_the_art_private_models_tend" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords state-of-the-art, private, models, tend, need, very in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_searching_jointly_over_clipping_thre`

- Preferred role: `method`
- Cue keywords: `searching, jointly, over, clipping, threshold, learning, rate, one, main, reasons`
- Narration: Searching jointly over the clipping threshold and the learning rate is one of the main reasons DP training is painful.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_searching_jointly_over_clipping_thre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords searching, jointly, over, clipping, threshold, learning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_large_models_grid_search_take`

- Preferred role: `content`
- Cue keywords: `large, models, grid, search, take, days, months, compute, because, inspects`
- Narration: For large models this grid search can take days to months of compute, and because it inspects private data it also spends additional privacy budget.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_large_models_grid_search_take" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, models, grid, search, take, days in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_crucially_best_thresholds_usually_sm`

- Preferred role: `content`
- Cue keywords: `crucially, best, thresholds, usually, small, nearly, every, per-sample, gradient, clipped`
- Narration: Crucially, the best thresholds are usually so small that nearly every per-sample gradient is clipped at every step, which hints that the precise value of R may not matter at all if we reformulate the clipping.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_crucially_best_thresholds_usually_sm" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, best, thresholds, usually, small, nearly in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_authors_make_four_contributions_firs`

- Preferred role: `content`
- Cue keywords: `authors, make, four, contributions, first, they, propose, automatic, clipping, which`
- Narration: The authors make four contributions. First, they propose automatic clipping, which mathematically expunges the clipping threshold from general DP optimizers including DP-SGD, DP-Adam, and DP-LAMB.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_authors_make_four_contributions_firs" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, make, four, contributions, first, they in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_they_prove_automatic_dp_sgd`

- Preferred role: `content`
- Cue keywords: `second, they, prove, automatic, dp-sgd, converges, non-convex, setting, same, asymptotic`
- Narration: Second, they prove that automatic DP-SGD converges in the non-convex setting at the same asymptotic rate as standard SGD.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_second_they_prove_automatic_dp_sgd" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, they, prove, automatic, dp-sgd, converges in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_they_show_any_positive`

- Preferred role: `content`
- Cue keywords: `third, they, show, any, positive, constant, threshold, equivalent, setting, one`
- Narration: Third, they show any positive constant threshold is equivalent to setting it to one, so a single default suffices.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_third_they_show_any_positive" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, they, show, any, positive, constant in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_fourth_they_demonstrate_superior_res`

- Preferred role: `method`
- Cue keywords: `fourth, they, demonstrate, superior, results, across, vision, language, benchmarks, achievable`
- Narration: And fourth, they demonstrate superior results across vision and language benchmarks, achievable by changing a single line of code in popular libraries.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_fourth_they_demonstrate_superior_res" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, they, demonstrate, superior, results, across in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_idea_starts_simple_observation_when`

- Preferred role: `content`
- Cue keywords: `idea, starts, simple, observation, when, threshold, small, abadi, clipping, factor`
- Narration: The idea starts from a simple observation: when the threshold is small, Abadi's clipping factor, the minimum of R over the gradient norm and one, is almost always just R over the gradient norm.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_idea_starts_simple_observation_when" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords idea, starts, simple, observation, when, threshold in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_authors_drop_minimum_entirely_normal`

- Preferred role: `content`
- Cue keywords: `authors, drop, minimum, entirely, normalize, every, per-sample, gradient, variant, they`
- Narration: So the authors drop the minimum entirely and normalize every per-sample gradient, a variant they call AUTO-V for vanilla. This maximizes alignment between the private and true gradient, but it makes all gradients the same size, creating a lazy region where updates stall.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_authors_drop_minimum_entirely_normal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, drop, minimum, entirely, normalize, every in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_fix_they_add_small_stability`

- Preferred role: `content`
- Cue keywords: `fix, they, add, small, stability, constant, gamma, denominator, giving, auto-s`
- Narration: To fix this they add a small stability constant gamma in the denominator, giving AUTO-S: R divided by the gradient norm plus gamma. This preserves relative magnitudes, letting small gradients shrink toward zero.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_fix_they_add_small_stability" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fix, they, add, small, stability, constant in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_finally_because_any_constant_thresho`

- Preferred role: `content`
- Cue keywords: `finally, because, any, constant, threshold, simply, rescales, learning, rate, they`
- Narration: Finally, because any constant threshold simply rescales the learning rate, they fix R to one, and set gamma to a default of zero point zero one, leaving a fully threshold-free optimizer.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_finally_because_any_constant_thresho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, because, any, constant, threshold, simply in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_method_tested_broadly`

- Preferred role: `method`
- Cue keywords: `method, tested, broadly`
- Narration: The method is tested broadly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_method_tested_broadly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, tested, broadly in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_language_authors_finetune_roberta_ba`

- Preferred role: `title`
- Cue keywords: `language, authors, finetune, roberta, base, large, glue, tasks, mnli, qqp`
- Narration: On language, the authors finetune RoBERTa base and large on the GLUE tasks MNLI, QQP, QNLI, and SST-2, and finetune GPT2 in three sizes for table-to-text generation on the E2E and DART datasets.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c2_language_authors_finetune_roberta_ba" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords language, authors, finetune, roberta, base, large in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_vision_they_evaluate_cifar_10_pretra`

- Preferred role: `method`
- Cue keywords: `vision, they, evaluate, cifar-10, pretrained, simclrv2, imagenette, resnet9, imagenet, resnet18`
- Narration: On vision, they evaluate CIFAR-10 with a pretrained SimCLRv2, ImageNette with a ResNet9, and ImageNet with ResNet18.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_vision_they_evaluate_cifar_10_pretra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords vision, they, evaluate, cifar-10, pretrained, simclrv2 in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_they_standard_privacy_budgets_epsilo`

- Preferred role: `content`
- Cue keywords: `they, standard, privacy, budgets, epsilon, three, epsilon, eight, reuse, exact`
- Narration: They use standard privacy budgets of epsilon three and epsilon eight and reuse the exact hyperparameters of prior state-of-the-art work, changing only the clipping.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_they_standard_privacy_budgets_epsilo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, standard, privacy, budgets, epsilon, three in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_board_automatic_clipping_matc`

- Preferred role: `result`
- Cue keywords: `across, board, automatic, clipping, matches, outperforms, state, art, does, without`
- Narration: Across the board, automatic clipping matches or outperforms the state of the art, and it does so without ever tuning the threshold.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_across_board_automatic_clipping_matc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, board, automatic, clipping, matches, outperforms in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_gpt2_text_generation_e2e_auto_s`

- Preferred role: `method`
- Cue keywords: `gpt2, text, generation, e2e, auto-s, reaches, bleu, score, sixty-four, point`
- Narration: For GPT2 text generation on E2E, AUTO-S reaches a BLEU score of sixty-four point one eight at epsilon three, edging past the prior best of sixty-three point eight five.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_gpt2_text_generation_e2e_auto_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gpt2, text, generation, e2e, auto-s, reaches in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_roberta_base_sst_2_reaches_ninety_tw`

- Preferred role: `result`
- Cue keywords: `roberta-base, sst-2, reaches, ninety-two, point, three, two, percent, above, prior`
- Narration: For RoBERTa-base on SST-2, it reaches ninety-two point three two percent, above the prior ninety-one point eight six.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_roberta_base_sst_2_reaches_ninety_tw" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords roberta-base, sst-2, reaches, ninety-two, point, three in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_cifar_10_pretrained_simclrv2_hits_ni`

- Preferred role: `method`
- Cue keywords: `cifar-10, pretrained, simclrv2, hits, ninety-two, point, seven, percent, epsilon, two`
- Narration: On CIFAR-10 with a pretrained SimCLRv2 it hits ninety-two point seven percent at epsilon two. And because only the learning rate needs searching, the tuning cost drops by about five times.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_cifar_10_pretrained_simclrv2_hits_ni" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, pretrained, simclrv2, hits, ninety-two, point in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_two_ablations_anchor_design`

- Preferred role: `content`
- Cue keywords: `two, ablations, anchor, design`
- Narration: Two ablations anchor the design.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_two_ablations_anchor_design" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, ablations, anchor, design in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_first_comparing_auto_v_auto_s_shows`

- Preferred role: `content`
- Cue keywords: `first, comparing, auto-v, auto-s, shows, once, small, stability, constant, restores`
- Narration: First, comparing AUTO-V and AUTO-S shows that once the small stability constant restores gradient magnitude, AUTO-S consistently wins, confirming that the lazy region really does hurt AUTO-V.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_first_comparing_auto_v_auto_s_shows" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, comparing, auto-v, auto-s, shows, once in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_second_sweeping_stability_constant_g`

- Preferred role: `method`
- Cue keywords: `second, sweeping, stability, constant, gamma, shows, method, essentially, insensitive, any`
- Narration: Second, sweeping the stability constant gamma shows the method is essentially insensitive to it: any positive gamma gives the same asymptotic convergence rate, which is why a single default of zero point zero one works everywhere.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_second_sweeping_stability_constant_g" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, sweeping, stability, constant, gamma, shows in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_heatmaps_over_threshold_learning_rat`

- Preferred role: `result`
- Cue keywords: `heatmaps, over, threshold, learning, rate, further, show, auto-s, result, landing`
- Narration: Heatmaps over threshold and learning rate further show the AUTO-S result landing right at the best hand-tuned threshold.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_heatmaps_over_threshold_learning_rat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords heatmaps, over, threshold, learning, rate, further in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_numbers_gpt2_e2e_reaches`

- Preferred role: `result`
- Cue keywords: `headline, numbers, gpt2, e2e, reaches, bleu, sixty-four, point, one, eight`
- Narration: The headline numbers: GPT2 on E2E reaches BLEU sixty-four point one eight at epsilon three, versus sixty-three point eight five for the prior best.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_headline_numbers_gpt2_e2e_reaches" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, numbers, gpt2, e2e, reaches, bleu in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_roberta_base_sst_2_reaches_ninety_tw`

- Preferred role: `result`
- Cue keywords: `roberta-base, sst-2, reaches, ninety-two, point, three, two, percent, roberta-large, same`
- Narration: RoBERTa-base on SST-2 reaches ninety-two point three two percent, and RoBERTa-large on the same task reaches ninety-four point six one percent at epsilon eight.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_roberta_base_sst_2_reaches_ninety_tw" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords roberta-base, sst-2, reaches, ninety-two, point, three in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_cifar_10_simclrv2_hits_ninety_two_po`

- Preferred role: `result`
- Cue keywords: `cifar-10, simclrv2, hits, ninety-two, point, seven, percent, epsilon, two, sensitivity`
- Narration: CIFAR-10 with SimCLRv2 hits ninety-two point seven percent at epsilon two. The sensitivity of the old approach is stark: on ImageNet, doubling the threshold drops ResNet18 accuracy from forty-five to thirty-one percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_cifar_10_simclrv2_hits_ninety_two_po" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, simclrv2, hits, ninety-two, point, seven in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_theoretically_minimum_expected_gradi`

- Preferred role: `content`
- Cue keywords: `theoretically, minimum, expected, gradient, norm, shrinks, rate, minus, one, quarter`
- Narration: Theoretically, the minimum expected gradient norm shrinks at the rate T to the minus one quarter, matching standard SGD.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_theoretically_minimum_expected_gradi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords theoretically, minimum, expected, gradient, norm, shrinks in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_clipping_threshold_l`

- Preferred role: `method`
- Cue keywords: `lasting, message, clipping, threshold, long, treated, critical, knob, differentially, private`
- Narration: The lasting message is that the clipping threshold, long treated as a critical knob in differentially private training, can simply be removed.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_lasting_message_clipping_threshold_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, clipping, threshold, long, treated in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_normalizing_per_sample_gradient_addi`

- Preferred role: `method`
- Cue keywords: `normalizing, per-sample, gradient, adding, tiny, stability, constant, you, get, optimizer`
- Narration: By normalizing each per-sample gradient and adding a tiny stability constant, you get an optimizer that is just as private, just as fast, and just as accurate as the best hand-tuned methods, backed by a convergence guarantee matching standard SGD.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_normalizing_per_sample_gradient_addi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords normalizing, per-sample, gradient, adding, tiny, stability in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_one_line_change_existing_libraries_w`

- Preferred role: `method`
- Cue keywords: `one-line, change, existing, libraries, which, finally, makes, about, easy, ordinary`
- Narration: It is a one-line change in existing libraries, which finally makes DP training about as easy as ordinary training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_one_line_change_existing_libraries_w" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one-line, change, existing, libraries, which, finally in title/desc so the matcher can verify semantic overlap.
