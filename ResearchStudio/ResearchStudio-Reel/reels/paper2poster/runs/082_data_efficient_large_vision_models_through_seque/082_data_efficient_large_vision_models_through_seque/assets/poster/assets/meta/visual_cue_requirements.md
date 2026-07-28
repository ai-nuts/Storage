# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_large_vision_models_trained_autoregr`

- Preferred role: `method`
- Cue keywords: `large, vision, models, trained, autoregression, promise, single, generalist, many, visual`
- Narration: Large vision models trained by autoregression promise a single generalist model for many visual tasks, but today's versions demand billions of parameters and hundreds of billions of visual tokens to train.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_large_vision_models_trained_autoregr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, vision, models, trained, autoregression, promise in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_icml_2024_delvm_asks_whether`

- Preferred role: `title`
- Cue keywords: `icml, 2024, delvm, asks, whether, really, need, all`
- Narration: This ICML 2024 paper, DeLVM, asks whether we really need all that.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c2_icml_2024_delvm_asks_whether" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords icml, 2024, delvm, asks, whether, really in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_show_two_simple_classical`

- Preferred role: `method`
- Cue keywords: `authors, show, two, simple, classical, ideas, augmentation, knowledge, distillation, let`
- Narration: The authors show that two simple, classical ideas, data augmentation and knowledge distillation, let a compact autoregressive vision model reach strong performance on a limited dataset, cutting both the parameter footprint and the training data requirement dramatically.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_authors_show_two_simple_classical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, show, two, simple, classical, ideas in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_language_modeling_autoregressive_mod`

- Preferred role: `content`
- Cue keywords: `language, modeling, autoregressive, models, like, gpt, thrive, universal, token, interface`
- Narration: In language modeling, autoregressive models like GPT thrive on a universal token interface. Recent work extends this idea to vision, treating images and annotations as visual sentences.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_language_modeling_autoregressive_mod" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords language, modeling, autoregressive, models, like, gpt in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_leading_large_vision_needs`

- Preferred role: `content`
- Cue keywords: `but, leading, large, vision, needs, over, three, billion, parameters, roughly`
- Narration: But the leading large vision model needs over three billion parameters and roughly four hundred billion visual tokens drawn from more than a billion images.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_but_leading_large_vision_needs" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, leading, large, vision, needs, over in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_scale_expensive_impractical_edge_dep`

- Preferred role: `content`
- Cue keywords: `scale, expensive, impractical, edge, deployment`
- Narration: That scale is expensive and impractical for edge deployment.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_scale_expensive_impractical_edge_dep" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords scale, expensive, impractical, edge, deployment in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_worse_visual_world_long_tailed_some`

- Preferred role: `method`
- Cue keywords: `worse, visual, world, long-tailed, some, tasks, like, segmentation, abundant, while`
- Narration: Worse, the visual world is long-tailed: some tasks like segmentation have abundant data while others like pose estimation are starved, and training on the raw mixture leaves the model unable to learn the rare tasks at all.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_worse_visual_world_long_tailed_some" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords worse, visual, world, long-tailed, some, tasks in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_language_models_typically_trained_si`

- Preferred role: `method`
- Cue keywords: `language, models, typically, trained, single, epoch, over, vast, corpora, avoid`
- Narration: Language models are typically trained for a single epoch over vast corpora to avoid overfitting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_language_models_typically_trained_si" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords language, models, typically, trained, single, epoch in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_computer_vision_rarely_luxury_many`

- Preferred role: `method`
- Cue keywords: `computer, vision, rarely, luxury, many, tasks, only, tiny, datasets, language`
- Narration: Computer vision rarely has that luxury: many tasks have only tiny datasets, so the language training schedule does not carry over.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_computer_vision_rarely_luxury_many" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords computer, vision, rarely, luxury, many, tasks in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_same_time_community_keeps_scaling`

- Preferred role: `figure`
- Cue keywords: `same, time, community, keeps, scaling, dataset, size, while, classical, remedies`
- Narration: At the same time, the community keeps scaling model and dataset size, while classical remedies for scarce and imbalanced data, namely data augmentation and knowledge distillation, have barely been tried in the autoregressive vision setting.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c3_same_time_community_keeps_scaling" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords same, time, community, keeps, scaling, dataset in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_closes_gap`

- Preferred role: `content`
- Cue keywords: `closes, gap`
- Narration: This paper closes that gap.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_closes_gap" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords closes, gap in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_authors_make_three_main_contribution`

- Preferred role: `content`
- Cue keywords: `authors, make, three, main, contributions`
- Narration: The authors make three main contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_authors_make_three_main_contribution" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, make, three, main, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_they_show_simple_augmentation`

- Preferred role: `result`
- Cue keywords: `first, they, show, simple, augmentation, random, crop, flip, rebalances, long-tailed`
- Narration: First, they show that simple data augmentation, random crop and flip, rebalances long-tailed multi-task data and improves an autoregressive vision model just as effectively as collecting more real samples.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_first_they_show_simple_augmentation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, they, show, simple, augmentation, random in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_they_bring_knowledge_distilla`

- Preferred role: `result`
- Cue keywords: `second, they, bring, knowledge, distillation, autoregressive, large, vision, models, first`
- Narration: Second, they bring knowledge distillation to autoregressive large vision models for the first time, using a LLaMA one-billion teacher to lift a compact three-hundred-million student across single-task and multi-task benchmarks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c3_second_they_bring_knowledge_distilla" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, they, bring, knowledge, distillation, autoregressive in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_they_build_practical_eighty_mi`

- Preferred role: `result`
- Cue keywords: `third, they, build, practical, eighty-million-parameter, combining, both, techniques, surprisingly, reaches`
- Narration: Third, they build a practical eighty-million-parameter model that, combining both techniques, surprisingly reaches eighty-three percent top-one accuracy on ImageNet, suggesting generation and understanding can be learned together.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_third_they_build_practical_eighty_mi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, they, build, practical, eighty-million-parameter, combining in title/desc so the matcher can verify semantic overlap.

## Slide 05: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s05_c1_experiments_cover_three_core_tasks`

- Preferred role: `result`
- Cue keywords: `experiments, cover, three, core, tasks, image, segmentation, subsets, sa-1b, ranging`
- Narration: Experiments cover three core tasks. Image segmentation uses subsets of SA-1B ranging from one to ten percent; human pose estimation uses the full COCO-Pose dataset; image deraining uses Rain13K.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c1_experiments_cover_three_core_tasks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, cover, three, core, tasks, image in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_validation_relies_held_out_sa_1b_spl`

- Preferred role: `content`
- Cue keywords: `validation, relies, held-out, sa-1b, splits, together, mpii, test2800`
- Narration: Validation relies on held-out SA-1B splits together with MPII and Test2800.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_validation_relies_held_out_sa_1b_spl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords validation, relies, held-out, sa-1b, splits, together in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_distilled_models_also_benchmarked_pa`

- Preferred role: `result`
- Cue keywords: `distilled, models, also, benchmarked, pascal, five-i, foreground, segmentation, mean, intersection-over-union`
- Narration: The distilled models are also benchmarked on Pascal five-i foreground segmentation using mean intersection-over-union, and the practical eighty-million model is evaluated on ImageNet classification.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_distilled_models_also_benchmarked_pa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords distilled, models, also, benchmarked, pascal, five-i in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_throughout_vqgan_tokenizer_trained_l`

- Preferred role: `method`
- Cue keywords: `throughout, vqgan, tokenizer, trained, laion, dataset, used, off, shelf`
- Narration: Throughout, the VQGAN tokenizer is trained on the Laion dataset and used off the shelf.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_throughout_vqgan_tokenizer_trained_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords throughout, vqgan, tokenizer, trained, laion, dataset in title/desc so the matcher can verify semantic overlap.

## Slide 06: key-result

Heading: Key Result

### Cue 1: `cue_s06_c1_results_consistently_favor_proposed`

- Preferred role: `result`
- Cue keywords: `results, consistently, favor, proposed, recipe, mixed, three-task, benchmark, balancing, through`
- Narration: The results consistently favor the proposed recipe. On the mixed three-task benchmark, balancing the data through augmentation beats both the raw unbalanced mixture and naive re-sampling, which actually collapses on the scarce tasks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_results_consistently_favor_proposed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, consistently, favor, proposed, recipe, mixed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_knowledge_distillation_improves_comp`

- Preferred role: `method`
- Cue keywords: `knowledge, distillation, improves, compact, student, segmentation, pose, estimation, deraining, both`
- Narration: Knowledge distillation then improves the compact student on segmentation, pose estimation, and deraining, in both single-task and multi-task training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_knowledge_distillation_improves_comp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords knowledge, distillation, improves, compact, student, segmentation in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_pascal_five_i_foreground_segmentatio`

- Preferred role: `method`
- Cue keywords: `pascal, five-i, foreground, segmentation, benchmark, distilled, fine-tuned, three-hundred-million, clearly, surpasses`
- Narration: On the Pascal five-i foreground segmentation benchmark, the distilled and fine-tuned three-hundred-million model clearly surpasses the same model trained from scratch.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_pascal_five_i_foreground_segmentatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pascal, five-i, foreground, segmentation, benchmark, distilled in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_scaling_segmentation_one_ten_percent`

- Preferred role: `figure`
- Cue keywords: `scaling, segmentation, one, ten, percent, lowers, validation, loss, nearly, two`
- Narration: And scaling data on segmentation from one to ten percent lowers validation loss by nearly two tenths and perplexity by over twenty-two points, an effect augmentation reproduces with no new data at all.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c4_scaling_segmentation_one_ten_percent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords scaling, segmentation, one, ten, percent, lowers in title/desc so the matcher can verify semantic overlap.

## Slide 07: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s07_c1_several_ablations_sharpen_picture`

- Preferred role: `content`
- Cue keywords: `several, ablations, sharpen, picture`
- Narration: Several ablations sharpen the picture.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_several_ablations_sharpen_picture" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords several, ablations, sharpen, picture in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_changing_prompt_background_color_cha`

- Preferred role: `content`
- Cue keywords: `changing, prompt, background, color, changes, generated, background, black-background, prompts, makes`
- Narration: Changing the prompt background color changes the generated background, and using black-background prompts makes a simple grayscale-threshold post-processing step reliable.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_changing_prompt_background_color_cha" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords changing, prompt, background, color, changes, generated in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_without_shuffling_task_triggers_cata`

- Preferred role: `method`
- Cue keywords: `without, shuffling, task, triggers, catastrophic, forgetting, becomes, proficient, only, its`
- Narration: Training without shuffling the task data triggers catastrophic forgetting: the model becomes proficient only on its most recently seen task, with perplexity on earlier tasks exploding into the thousands, underscoring that shuffling is essential for multi-task LVMs.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_without_shuffling_task_triggers_cata" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords without, shuffling, task, triggers, catastrophic, forgetting in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_finally_even_just_eighty_million`

- Preferred role: `content`
- Cue keywords: `finally, even, just, eighty, million, parameters, knowledge, distillation, still, improves`
- Narration: Finally, even at just eighty million parameters, knowledge distillation still improves validation perplexity across segmentation, pose estimation, and deraining.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_finally_even_just_eighty_million" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, even, just, eighty, million, parameters in title/desc so the matcher can verify semantic overlap.

## Slide 08: takeaway

Heading: Takeaway

### Cue 1: `cue_s08_c1_takeaway_refreshingly_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, refreshingly, simple`
- Narration: The takeaway is refreshingly simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s08_c1_takeaway_refreshingly_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, refreshingly, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_you_not_need_three_billion_parameter`

- Preferred role: `content`
- Cue keywords: `you, not, need, three-billion-parameter, hundreds, billions, tokens, build, capable, autoregressive`
- Narration: You do not need a three-billion-parameter model and hundreds of billions of tokens to build a capable autoregressive vision model.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_you_not_need_three_billion_parameter" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords you, not, need, three-billion-parameter, hundreds, billions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_two_classical_techniques_augmentatio`

- Preferred role: `method`
- Cue keywords: `two, classical, techniques, augmentation, rebalance, long-tailed, tasks, knowledge, distillation, compress`
- Narration: Two classical techniques, data augmentation to rebalance long-tailed tasks and knowledge distillation to compress a large teacher, together let compact models trained on limited data perform strongly across segmentation, pose estimation, and deraining.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_two_classical_techniques_augmentatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, classical, techniques, augmentation, rebalance, long-tailed in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_eighty_million_parameter_version_eve`

- Preferred role: `result`
- Cue keywords: `eighty-million-parameter, version, even, reaches, eighty-three, percent, accuracy, imagenet, points, toward`
- Narration: That an eighty-million-parameter version even reaches eighty-three percent accuracy on ImageNet points toward efficient, deployable generalist vision models that unify generation and understanding.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_eighty_million_parameter_version_eve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords eighty-million-parameter, version, even, reaches, eighty-three, percent in title/desc so the matcher can verify semantic overlap.
