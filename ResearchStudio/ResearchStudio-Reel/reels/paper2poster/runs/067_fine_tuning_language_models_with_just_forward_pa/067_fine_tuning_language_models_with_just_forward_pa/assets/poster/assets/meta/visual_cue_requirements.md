# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_fine_tuning_large_language_models_no`

- Preferred role: `content`
- Cue keywords: `fine-tuning, large, language, models, normally, requires, backpropagation, which, stores, activations`
- Narration: Fine-tuning large language models normally requires backpropagation, which stores activations and gradients and consumes enormous memory.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_fine_tuning_large_language_models_no" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fine-tuning, large, language, models, normally, requires in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_princeton_university_introduces_mezo`

- Preferred role: `content`
- Cue keywords: `princeton, university, introduces, mezo, memory-efficient, zeroth-order, optimizer, fine-tunes, language, models`
- Narration: This paper, from Princeton University, introduces MeZO, a memory-efficient zeroth-order optimizer that fine-tunes language models using only forward passes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_princeton_university_introduces_mezo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords princeton, university, introduces, mezo, memory-efficient, zeroth-order in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_mezo_adapts_classical_zeroth_order_s`

- Preferred role: `method`
- Cue keywords: `mezo, adapts, classical, zeroth-order, sgd, method, run, place, costs, same`
- Narration: MeZO adapts the classical zeroth-order SGD method to run in place, so training costs the same memory as inference.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_mezo_adapts_classical_zeroth_order_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mezo, adapts, classical, zeroth-order, sgd, method in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_single_80_gigabyte_a100_gpu`

- Preferred role: `title`
- Cue keywords: `single, 80, gigabyte, a100, gpu, mezo, train, 30, billion-parameter, where`
- Narration: On a single 80-gigabyte A100 GPU, MeZO can train a 30-billion-parameter model, where backpropagation with Adam fits only a 2.7-billion one. Across many tasks and model scales, MeZO matches fine-tuning performance with up to twelve times less memory.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c4_single_80_gigabyte_a100_gpu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single, 80, gigabyte, a100, gpu, mezo in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_fine_tuning_driven_much_recent_succe`

- Preferred role: `content`
- Cue keywords: `fine-tuning, driven, much, recent, success, language, models, but, comes, steep`
- Narration: Fine-tuning has driven much of the recent success of language models, but it comes at a steep memory cost.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_fine_tuning_driven_much_recent_succe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fine-tuning, driven, much, recent, success, language in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_backpropagation_must_cache_intermedi`

- Preferred role: `content`
- Cue keywords: `backpropagation, must, cache, intermediate, activations, store, gradients, optimizer, states, which`
- Narration: Backpropagation must cache intermediate activations and store gradients and optimizer states, which together can require up to twelve times the memory of plain inference.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_backpropagation_must_cache_intermedi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords backpropagation, must, cache, intermediate, activations, store in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_models_scale_tens_billions_parameter`

- Preferred role: `method`
- Cue keywords: `models, scale, tens, billions, parameters, becomes, binding, constraint`
- Narration: As models scale into the tens of billions of parameters, this becomes the binding constraint.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_models_scale_tens_billions_parameter" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords models, scale, tens, billions, parameters, becomes in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_concretely_single_eighty_gigabyte_a1`

- Preferred role: `content`
- Cue keywords: `concretely, single, eighty-gigabyte, a100, gpu, run, inference, thirty-billion-parameter, yet, standard`
- Narration: Concretely, a single eighty-gigabyte A100 GPU can run inference on a thirty-billion-parameter model, yet standard Adam fine-tuning on the same hardware is limited to only a two-point-seven-billion-parameter model.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_concretely_single_eighty_gigabyte_a1" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords concretely, single, eighty-gigabyte, a100, gpu, run in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_zeroth_order_optimization_offers_tem`

- Preferred role: `content`
- Cue keywords: `zeroth-order, optimization, offers, tempting, escape, estimate, gradient, only, two, forward`
- Narration: Zeroth-order optimization offers a tempting escape: it can estimate a gradient using only two forward passes, requiring no backpropagation at all.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_zeroth_order_optimization_offers_tem" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords zeroth-order, optimization, offers, tempting, escape, estimate in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_catch_classical_analyses_suggest_zer`

- Preferred role: `method`
- Cue keywords: `catch, classical, analyses, suggest, zeroth-order, methods, converge, catastrophically, slowly, large`
- Narration: The catch is that classical analyses suggest zeroth-order methods converge catastrophically slowly for large models, with the rate degrading in proportion to the number of parameters.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_catch_classical_analyses_suggest_zer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords catch, classical, analyses, suggest, zeroth-order, methods in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_pessimism_combined_naive_implementat`

- Preferred role: `method`
- Cue keywords: `pessimism, combined, naive, implementation, still, doubles, memory, why, zeroth-order, methods`
- Narration: That pessimism, combined with a naive implementation that still doubles memory, is why zeroth-order methods have been overlooked for modern language models.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_pessimism_combined_naive_implementat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pessimism, combined, naive, implementation, still, doubles in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_asks_whether_pessimism_actually_hold`

- Preferred role: `method`
- Cue keywords: `asks, whether, pessimism, actually, holds, when, fine-tuning, pre-trained, models, downstream`
- Narration: This paper asks whether that pessimism actually holds when fine-tuning pre-trained models on downstream tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_asks_whether_pessimism_actually_hold" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords asks, whether, pessimism, actually, holds, when in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_four_main_contributions_first`

- Preferred role: `content`
- Cue keywords: `makes, four, main, contributions, first, introduces, mezo, memory-efficient, zeroth-order, optimizer`
- Narration: The paper makes four main contributions. First, it introduces MeZO, a memory-efficient zeroth-order optimizer that adapts classical zeroth-order SGD to operate in place, so fine-tuning costs no more memory than inference.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_four_main_contributions_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, four, main, contributions, first, introduces in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_through_comprehensive_experim`

- Preferred role: `result`
- Cue keywords: `second, through, comprehensive, experiments, across, masked, autoregressive, models, scales, sixty-six`
- Narration: Second, through comprehensive experiments across masked and autoregressive models, scales up to sixty-six billion parameters, and classification, multiple-choice, and generation tasks, it shows MeZO matches full backpropagation fine-tuning while using far less memory.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_second_through_comprehensive_experim" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, through, comprehensive, experiments, across, masked in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_demonstrates_compatibility_par`

- Preferred role: `method`
- Cue keywords: `third, demonstrates, compatibility, parameter-efficient, methods, like, lora, prefix, tuning, ability`
- Narration: Third, it demonstrates compatibility with parameter-efficient methods like LoRA and prefix tuning, and the ability to optimize non-differentiable objectives such as accuracy or F1.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_third_demonstrates_compatibility_par" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, demonstrates, compatibility, parameter-efficient, methods, like in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_fourth_supplies_theory_explaining_wh`

- Preferred role: `content`
- Cue keywords: `fourth, supplies, theory, explaining, why, mezo, converges, quickly, despite, enormous`
- Narration: Fourth, it supplies theory explaining why MeZO converges quickly despite the enormous parameter count.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_fourth_supplies_theory_explaining_wh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, supplies, theory, explaining, why, mezo in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_mezo_built_classical_zeroth_order_gr`

- Preferred role: `result`
- Cue keywords: `mezo, built, classical, zeroth-order, gradient, estimator, called, spsa, simultaneous, perturbation`
- Narration: MeZO is built on a classical zeroth-order gradient estimator called SPSA, or simultaneous perturbation stochastic approximation. At each step it samples a single random Gaussian direction z, adds epsilon times z to every parameter and records the loss, then subtracts to get the loss on the opposite side.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_mezo_built_classical_zeroth_order_gr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mezo, built, classical, zeroth-order, gradient, estimator in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_difference_these_two_losses_divided`

- Preferred role: `figure`
- Cue keywords: `difference, these, two, losses, divided, twice, epsilon, gives, scalar, called`
- Narration: The difference of these two losses divided by twice epsilon gives a scalar called the projected gradient, and the parameters are then updated by moving along z scaled by this scalar and the learning rate.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c2_difference_these_two_losses_divided" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords difference, these, two, losses, divided, twice in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_crucial_engineering_insight_instead`

- Preferred role: `result`
- Cue keywords: `crucial, engineering, insight, instead, storing, full, random, vector, which, would`
- Narration: The crucial engineering insight is that instead of storing the full random vector z, which would double memory, MeZO stores only the random seed and regenerates z deterministically each time it is needed.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_crucial_engineering_insight_instead" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucial, engineering, insight, instead, storing, full in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_lets_entire_perturb_evaluate_update`

- Preferred role: `method`
- Cue keywords: `lets, entire, perturb, evaluate, update, cycle, happen, place, exactly, same`
- Narration: This lets the entire perturb, evaluate, and update cycle happen in place, so training uses exactly the same memory as inference.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_lets_entire_perturb_evaluate_update" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lets, entire, perturb, evaluate, update, cycle in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_evaluation_deliberately_broad`

- Preferred role: `result`
- Cue keywords: `evaluation, deliberately, broad`
- Narration: The evaluation is deliberately broad.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_evaluation_deliberately_broad" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, deliberately, broad in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_masked_language_model_side_roberta_l`

- Preferred role: `result`
- Cue keywords: `masked-language-model, side, roberta-large, six, sentence-classification, inference, tasks, tested, both, few-shot`
- Narration: On the masked-language-model side, it uses RoBERTa-large on six sentence-classification and inference tasks, tested in both a few-shot regime with sixteen examples per class and a many-shot regime with five hundred and twelve.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_masked_language_model_side_roberta_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords masked-language-model, side, roberta-large, six, sentence-classification, inference in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_autoregressive_side_opt_models_rangi`

- Preferred role: `result`
- Cue keywords: `autoregressive, side, opt, models, ranging, one-point-three, billion, sixty-six, billion, parameters`
- Narration: On the autoregressive side, it uses OPT models ranging from one-point-three billion up to sixty-six billion parameters, evaluated on SuperGLUE classification tasks, multiple-choice tasks like COPA and ReCoRD, and generation tasks including SQuAD and DROP.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_autoregressive_side_opt_models_rangi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords autoregressive, side, opt, models, ranging, one-point-three in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_baselines_include_zero_shot_predicti`

- Preferred role: `content`
- Cue keywords: `baselines, include, zero-shot, prediction, in-context, learning, linear, probing, standard, adam`
- Narration: Baselines include zero-shot prediction, in-context learning, linear probing, and standard Adam fine-tuning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_baselines_include_zero_shot_predicti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords baselines, include, zero-shot, prediction, in-context, learning in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_mezo_closes_most`

- Preferred role: `result`
- Cue keywords: `headline, result, mezo, closes, most, gap, backpropagation, fine-tuning, fraction, memory`
- Narration: The headline result is that MeZO closes most of the gap to backpropagation fine-tuning at a fraction of the memory.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_headline_result_mezo_closes_most" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, mezo, closes, most, gap in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_opt_thirteen_billion_mezo_comes_with`

- Preferred role: `title`
- Cue keywords: `opt-thirteen-billion, mezo, comes, within, about, one, percent, full, adam, fine-tuning`
- Narration: On OPT-thirteen-billion, MeZO comes within about one percent of full Adam fine-tuning on seven of eleven tasks, while consuming only one-twelfth of the memory, and it clearly beats zero-shot prediction, in-context learning, and linear probing.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s07_c2_opt_thirteen_billion_mezo_comes_with" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords opt-thirteen-billion, mezo, comes, within, about, one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_roberta_large_many_shot_setting_land`

- Preferred role: `content`
- Cue keywords: `roberta-large, many-shot, setting, lands, within, roughly, five, percent, fine-tuning`
- Narration: On RoBERTa-large in the many-shot setting, it lands within roughly five percent of fine-tuning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_roberta_large_many_shot_setting_land" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords roberta-large, many-shot, setting, lands, within, roughly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_beyond_memory_mezo_also_faster`

- Preferred role: `content`
- Cue keywords: `beyond, memory, mezo, also, faster, practice, requiring, about, half, gpu-hours`
- Narration: Beyond memory, MeZO is also faster in practice, requiring about half the GPU-hours of Adam fine-tuning for a thirty-billion-parameter model.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_beyond_memory_mezo_also_faster" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beyond, memory, mezo, also, faster, practice in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_several_ablations_probe_mezo_flexibi`

- Preferred role: `method`
- Cue keywords: `several, ablations, probe, mezo, flexibility, combining, mezo, parameter-efficient, methods, namely`
- Narration: Several ablations probe MeZO's flexibility. Combining MeZO with parameter-efficient methods, namely LoRA and prefix tuning, gives accuracy on par with tuning all parameters, showing the two approaches compose well.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_several_ablations_probe_mezo_flexibi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords several, ablations, probe, mezo, flexibility, combining in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_single_random_perturbation_per_step`

- Preferred role: `result`
- Cue keywords: `single, random, perturbation, per, step, rather, averaging, several, turns, out`
- Narration: Using a single random perturbation per step, rather than averaging several, turns out to be the most efficient setting for a fixed number of forward passes.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_single_random_perturbation_per_step" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single, random, perturbation, per, step, rather in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_because_mezo_only_needs_loss`

- Preferred role: `method`
- Cue keywords: `because, mezo, only, needs, loss, values, never, actual, gradients, optimize`
- Narration: Because MeZO only needs loss values and never actual gradients, it can optimize non-differentiable objectives directly, such as maximizing accuracy or F1 score.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_because_mezo_only_needs_loss" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, mezo, only, needs, loss, values in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_against_prior_zeroth_order_baseline`

- Preferred role: `result`
- Cue keywords: `against, prior, zeroth-order, baseline, bbtv2, mezo, improves, accuracy, eleven, percentage`
- Narration: And against a prior zeroth-order baseline, BBTv2, MeZO improves accuracy by up to eleven percentage points.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_against_prior_zeroth_order_baseline" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords against, prior, zeroth-order, baseline, bbtv2, mezo in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_mezo_delivers_twelvefold_reduction_m`

- Preferred role: `content`
- Cue keywords: `mezo, delivers, twelvefold, reduction, memory, compared, adam, fine-tuning, opt-thirteen-billion, more`
- Narration: MeZO delivers up to a twelvefold reduction in memory compared with Adam fine-tuning on OPT-thirteen-billion, using no more memory than inference.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_mezo_delivers_twelvefold_reduction_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mezo, delivers, twelvefold, reduction, memory, compared in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_single_eighty_gigabyte_a100_trains_t`

- Preferred role: `content`
- Cue keywords: `single, eighty-gigabyte, a100, trains, thirty-billion-parameter, where, backpropagation, fits, only, two-point-seven`
- Narration: On a single eighty-gigabyte A100, it trains a thirty-billion-parameter model where backpropagation fits only two-point-seven billion.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_single_eighty_gigabyte_a100_trains_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single, eighty-gigabyte, a100, trains, thirty-billion-parameter, where in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_matches_fine_tuning_within_about_one`

- Preferred role: `title`
- Cue keywords: `matches, fine-tuning, within, about, one, percent, seven, eleven, tasks, roughly`
- Narration: It matches fine-tuning within about one percent on seven of eleven tasks, and it roughly halves the GPU-hours needed at the thirty-billion scale.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s09_c4_matches_fine_tuning_within_about_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords matches, fine-tuning, within, about, one, percent in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_takeaway_fine_tuning_longer`

- Preferred role: `method`
- Cue keywords: `lasting, takeaway, fine-tuning, longer, strictly, requires, backpropagation`
- Narration: The lasting takeaway is that fine-tuning no longer strictly requires backpropagation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_lasting_takeaway_fine_tuning_longer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, takeaway, fine-tuning, longer, strictly, requires in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_mezo_you_adapt_very_large`

- Preferred role: `title`
- Cue keywords: `mezo, you, adapt, very, large, language, models, only, forward, passes`
- Narration: With MeZO, you can adapt very large language models using only forward passes, at the memory cost of inference, and still match the quality of gradient-based fine-tuning on many tasks.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s10_c2_mezo_you_adapt_very_large" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mezo, you, adapt, very, large, language in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_overturns_classical_worry_zeroth_ord`

- Preferred role: `method`
- Cue keywords: `overturns, classical, worry, zeroth-order, methods, must, scale, badly, size, when`
- Narration: This overturns the classical worry that zeroth-order methods must scale badly with model size: when you start from a strong pre-trained model, convergence is governed by the effective local structure of the loss landscape rather than the sheer number of parameters, which is why MeZO works at billion-parameter scale.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_overturns_classical_worry_zeroth_ord" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords overturns, classical, worry, zeroth-order, methods, must in title/desc so the matcher can verify semantic overlap.
