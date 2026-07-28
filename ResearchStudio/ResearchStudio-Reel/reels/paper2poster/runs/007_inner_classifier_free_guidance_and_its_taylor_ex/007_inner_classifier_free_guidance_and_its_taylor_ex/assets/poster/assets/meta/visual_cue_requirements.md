# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_classifier_free_guidance_cfg_workhor`

- Preferred role: `result`
- Cue keywords: `classifier-free, guidance, cfg, workhorse, lets, conditional, diffusion, models, trade, sample`
- Narration: Classifier-free guidance, or CFG, is the workhorse that lets conditional diffusion models trade sample diversity against fidelity.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c1_classifier_free_guidance_cfg_workhor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classifier-free, guidance, cfg, workhorse, lets, conditional in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_but_when_condition_continuous_like`

- Preferred role: `method`
- Cue keywords: `but, when, condition, continuous, like, text, embedding, cfg, ignores, structure`
- Narration: But when the condition is continuous, like a text embedding, CFG ignores that structure.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_but_when_condition_continuous_like" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, when, condition, continuous, like, text in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_iclr_2024_tsinghua_university_huawei`

- Preferred role: `guidance`
- Cue keywords: `iclr, 2024, tsinghua, university, huawei, introduces, inner, classifier-free, guidance, icfg`
- Narration: This ICLR 2024 paper from Tsinghua University and Huawei introduces Inner Classifier-Free Guidance, or ICFG, a perspective that treats standard CFG as the first-order case of a broader Taylor expansion.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s01_c3_iclr_2024_tsinghua_university_huawei" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords iclr, 2024, tsinghua, university, huawei, introduces in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_adding_second_order_term_change_auth`

- Preferred role: `method`
- Cue keywords: `adding, second-order, term, change, authors, get, better, balance, between, fidelity`
- Narration: By adding a second-order term, with no change to training, the authors get a better balance between fidelity and diversity for Stable Diffusion, using only a few lines of code.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_adding_second_order_term_change_auth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adding, second-order, term, change, authors, get in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_conditional_diffusion_models_rely_cl`

- Preferred role: `guidance`
- Cue keywords: `conditional, diffusion, models, rely, classifier-free, guidance, control, how, diverse, faithful`
- Narration: Conditional diffusion models rely on classifier-free guidance to control how diverse and faithful their samples are.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s02_c1_conditional_diffusion_models_rely_cl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords conditional, diffusion, models, rely, classifier-free, guidance in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_problem_cfg_treats_condition_opaque`

- Preferred role: `method`
- Cue keywords: `problem, cfg, treats, condition, opaque, label, places, constraints, condition, space`
- Narration: The problem is that CFG treats the condition as an opaque label; it places no constraints on the condition space.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_problem_cfg_treats_condition_opaque" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords problem, cfg, treats, condition, opaque, label in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_when_space_continuous_like_text`

- Preferred role: `guidance`
- Cue keywords: `when, space, continuous, like, text, prompt, embedding, all, continuity, goes`
- Narration: So when that space is continuous, like a text prompt embedding, all that continuity goes to waste.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s02_c3_when_space_continuous_like_text" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, space, continuous, like, text, prompt in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_authors_ask_pointed_question_conditi`

- Preferred role: `method`
- Cue keywords: `authors, ask, pointed, question, condition, lives, structured, continuous, space, better`
- Narration: The authors ask a pointed question: if the condition lives in a structured continuous space, can we do better than plain CFG?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_authors_ask_pointed_question_conditi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ask, pointed, question, condition, lives in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_two_main_ways_inject_guidance`

- Preferred role: `method`
- Cue keywords: `two, main, ways, inject, guidance, diffusion, models, external, trained, classifier`
- Narration: There are two main ways to inject guidance into diffusion models: use an external trained classifier, or use classifier-free guidance that a single model learns jointly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_two_main_ways_inject_guidance" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, main, ways, inject, guidance, diffusion in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_both_work_well_but_neither`

- Preferred role: `content`
- Cue keywords: `both, work, well, but, neither, says, anything, about, shape, condition`
- Narration: Both work well, but neither says anything about the shape of the condition space.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_both_work_well_but_neither" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords both, work, well, but, neither, says in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_authors_insight_text_encoder_maps`

- Preferred role: `method`
- Cue keywords: `authors, insight, text, encoder, maps, prompts, continuous, space, structure, you`
- Narration: The authors' insight is that a text encoder maps prompts into a continuous space with structure, and if you identify that structure, you can move along it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_authors_insight_text_encoder_maps" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, insight, text, encoder, maps, prompts in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_motivates_inner_classifier_free_guid`

- Preferred role: `guidance`
- Cue keywords: `motivates, inner, classifier-free, guidance`
- Narration: That motivates inner classifier-free guidance.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s03_c4_motivates_inner_classifier_free_guid" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords motivates, inner, classifier-free, guidance in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_central_contribution_reframing_stand`

- Preferred role: `guidance`
- Cue keywords: `central, contribution, reframing, standard, cfg, not, whole, story, just, first-order`
- Narration: The central contribution is a reframing: standard CFG is not the whole story, it is just the first-order term of a more general expansion the authors call inner classifier-free guidance.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c1_central_contribution_reframing_stand" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords central, contribution, reframing, standard, cfg, not in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_writing_guided_score_taylor_series`

- Preferred role: `method`
- Cue keywords: `writing, guided, score, taylor, series, guidance, strength, around, one, they`
- Narration: By writing the guided score as a Taylor series in the guidance strength around one, they recover CFG as the first-order case and then add a second-order term.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_writing_guided_score_taylor_series" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords writing, guided, score, taylor, series, guidance in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_term_computed_existing_pretrained_re`

- Preferred role: `method`
- Cue keywords: `term, computed, existing, pretrained, retraining, needed`
- Narration: This term is computed from the existing pretrained model, so no retraining is needed.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_term_computed_existing_pretrained_re" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords term, computed, existing, pretrained, retraining, needed in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_they_also_provide_policy_two`

- Preferred role: `method`
- Cue keywords: `they, also, provide, policy, two, sampling, algorithms, convergence, analysis`
- Narration: They also provide a training policy, two sampling algorithms, and a convergence analysis.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_they_also_provide_policy_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, also, provide, policy, two, sampling in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_mechanism_authors_write_guided_distr`

- Preferred role: `method`
- Cue keywords: `mechanism, authors, write, guided, distribution, unconditional, distribution, times, ratio, conditional`
- Narration: Here is the mechanism. The authors write the guided distribution as the unconditional distribution times the ratio of conditional to unconditional, raised to a power beta, where beta equals w plus one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_mechanism_authors_write_guided_distr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mechanism, authors, write, guided, distribution, unconditional in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_they_take_taylor_expansion_score`

- Preferred role: `method`
- Cue keywords: `they, take, taylor, expansion, score, predictor, beta, evaluated, beta, equals`
- Narration: They take a Taylor expansion of the score predictor in beta, evaluated at beta equals one. The first-order term is exactly classifier-free guidance.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_they_take_taylor_expansion_score" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, take, taylor, expansion, score, predictor in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_second_order_term_new_estimated_midd`

- Preferred role: `method`
- Cue keywords: `second-order, term, new, estimated, middle, point, between, zero, one, needs`
- Narration: The second-order term is new: it is estimated using a middle point m between zero and one, and needs only one extra score evaluation at a scaled condition, m times c.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_second_order_term_new_estimated_midd" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second-order, term, new, estimated, middle, point in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_because_everything_comes_already_tra`

- Preferred role: `method`
- Cue keywords: `because, everything, comes, already-trained, network, second-order, icfg, drops, pretrained, stable`
- Narration: Because everything comes from the already-trained network, second-order ICFG drops into a pretrained Stable Diffusion with a few lines of code, controlled by a first-order weight w and a second-order weight v.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_because_everything_comes_already_tra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, everything, comes, already-trained, network, second-order in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_main_evaluation_text_to_image_ms_coc`

- Preferred role: `result`
- Cue keywords: `main, evaluation, text-to-image, ms-coco, validation, set`
- Narration: The main evaluation is text-to-image on the MS-COCO validation set.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_main_evaluation_text_to_image_ms_coc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords main, evaluation, text-to-image, ms-coco, validation, set in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_two_metrics_carry_story_fid`

- Preferred role: `method`
- Cue keywords: `two, metrics, carry, story, fid, which, measures, image, fidelity, where`
- Narration: Two metrics carry the story: FID, which measures image fidelity, where lower is better, and CLIP Score, which measures how well the image matches the prompt, where higher is better.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_two_metrics_carry_story_fid" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, metrics, carry, story, fid, which in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_authors_run_these_pretrained_stable`

- Preferred role: `method`
- Cue keywords: `authors, run, these, pretrained, stable, diffusion, add, class-conditional, experiment, u-vit`
- Narration: The authors run these on pretrained Stable Diffusion, and add a class-conditional experiment on U-ViT plus a few-shot fine-tuning study on Stable Diffusion one point five.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_authors_run_these_pretrained_stable" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, run, these, pretrained, stable, diffusion in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_second_order_term_g`

- Preferred role: `content`
- Cue keywords: `headline, finding, second-order, term, genuinely, helps`
- Narration: The headline finding is that the second-order term genuinely helps.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_headline_finding_second_order_term_g" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, second-order, term, genuinely, helps in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_ms_coco_guidance_strength_two_second`

- Preferred role: `method`
- Cue keywords: `ms-coco, guidance, strength, two, second-order, weight, quarter, icfg, reaches, fid`
- Narration: On MS-COCO, at guidance strength two with the second-order weight at a quarter, ICFG reaches an FID of fifteen point two eight and a CLIP score of twenty six point one one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_ms_coco_guidance_strength_two_second" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ms-coco, guidance, strength, two, second-order, weight in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_beats_classifier_free_guidance_same`

- Preferred role: `method`
- Cue keywords: `beats, classifier-free, guidance, same, setting, worse, fid, fifteen, point, four`
- Narration: That beats classifier-free guidance at the same setting, with a worse FID of fifteen point four two and a lower CLIP score of twenty five point eight. So the method improves both fidelity and alignment at once, without touching training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_beats_classifier_free_guidance_same" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beats, classifier-free, guidance, same, setting, worse in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_authors_identify_sweet_spot_equals`

- Preferred role: `content`
- Cue keywords: `authors, identify, sweet, spot, equals, two, equals, one, quarter, note`
- Narration: The authors identify the sweet spot at w equals two and v equals one quarter, and note the full condition space trades off the two metrics more favorably.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_authors_identify_sweet_spot_equals" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, identify, sweet, spot, equals, two in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_two_ablations_illuminate_design_choi`

- Preferred role: `content`
- Cue keywords: `two, ablations, illuminate, design, choices`
- Narration: Two ablations illuminate the design choices.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_two_ablations_illuminate_design_choi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, ablations, illuminate, design, choices in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_first_middle_point_used_estimate`

- Preferred role: `method`
- Cue keywords: `first, middle, point, used, estimate, second-order, term, produces, u-shaped, fid`
- Narration: First, the middle point m, used to estimate the second-order term, produces a U-shaped FID curve: if the two points are too close, the estimate can't capture long-term change, and if they drift too near zero or one, the model struggles to score them, with the best value around m equals one point one.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_first_middle_point_used_estimate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, middle, point, used, estimate, second-order in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_second_varying_sampling_steps_shows`

- Preferred role: `method`
- Cue keywords: `second, varying, sampling, steps, shows, method, already, produces, well-matched, images`
- Narration: Second, varying the sampling steps shows the method already produces well-matched images at just ten steps, improving modestly up to fifty.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_second_varying_sampling_steps_shows" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, varying, sampling, steps, shows, method in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_take_away`

- Preferred role: `content`
- Cue keywords: `few, numbers, take, away`
- Narration: A few numbers to take away.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_take_away" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, take, away in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_best_fidelity_alignment_balance_ms_c`

- Preferred role: `method`
- Cue keywords: `best, fidelity-alignment, balance, ms-coco, fid, fifteen, point, two, eight, clip`
- Narration: The best fidelity-alignment balance on MS-COCO is an FID of fifteen point two eight and a CLIP score of twenty six point one one, beating classifier-free guidance on both.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_best_fidelity_alignment_balance_ms_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords best, fidelity-alignment, balance, ms-coco, fid, fifteen in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_middle_point_sweep_best_fid_fifteen`

- Preferred role: `content`
- Cue keywords: `middle-point, sweep, best, fid, fifteen, point, four, two, equal, one`
- Narration: In the middle-point sweep, the best FID is fifteen point four two at m equal to one point one.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_middle_point_sweep_best_fid_fifteen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords middle-point, sweep, best, fid, fifteen, point in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_u_vit_inner_classifier_free_guidance`

- Preferred role: `method`
- Cue keywords: `u-vit, inner, classifier-free, guidance, cuts, fid, substantially, low, sampling, budgets`
- Narration: On U-ViT, inner classifier-free guidance cuts FID substantially at low sampling budgets and edges out CFG at high budgets. And all of it comes from a few lines of code, with no change to training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_u_vit_inner_classifier_free_guidance" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords u-vit, inner, classifier-free, guidance, cuts, fid in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_classifier_free_guidance_just_first`

- Preferred role: `guidance`
- Cue keywords: `classifier-free, guidance, just, first-order, slice, richer, picture`
- Narration: Classifier-free guidance is just the first-order slice of a richer picture.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s10_c2_classifier_free_guidance_just_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classifier-free, guidance, just, first-order, slice, richer in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_treat_guided_score_taylor_expansion`

- Preferred role: `method`
- Cue keywords: `treat, guided, score, taylor, expansion, guidance, strength, single, extra, second-order`
- Narration: Treat the guided score as a Taylor expansion in the guidance strength, and a single extra second-order term buys you a better fidelity-diversity trade-off.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_treat_guided_score_taylor_expansion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords treat, guided, score, taylor, expansion, guidance in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_needs_retraining_only_scaled_conditi`

- Preferred role: `method`
- Cue keywords: `needs, retraining, only, scaled, condition, few, lines, code, points, toward`
- Narration: It needs no retraining, only a scaled condition and a few lines of code, and it points toward exploiting the continuous condition structure that plain CFG throws away.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_needs_retraining_only_scaled_conditi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords needs, retraining, only, scaled, condition, few in title/desc so the matcher can verify semantic overlap.
