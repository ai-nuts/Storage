# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_presented_icml_2024_work_tackles`

- Preferred role: `content`
- Cue keywords: `presented, icml, 2024, work, tackles, underwater, salient, instance, segmentation`
- Narration: Presented at ICML 2024, this work tackles underwater salient instance segmentation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_presented_icml_2024_work_tackles" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords presented, icml, 2024, work, tackles, underwater in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_build_usis10k_first_large_sc`

- Preferred role: `content`
- Cue keywords: `authors, build, usis10k, first, large-scale, underwater, dataset, ten, thousand, pixel-level`
- Narration: The authors build USIS10K, the first large-scale underwater dataset with ten thousand pixel-level annotated images, and propose USIS-SAM, a Segment Anything Model tailored to underwater scenes that injects visual prompts and generates salient prompts automatically to set a new state of the art.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_authors_build_usis10k_first_large_sc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, build, usis10k, first, large-scale, underwater in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_underwater_salient_instance_segmenta`

- Preferred role: `title`
- Cue keywords: `underwater, salient, instance, segmentation, asks, find, separate, most, important, objects`
- Narration: Underwater salient instance segmentation asks a model to find and separate the most important objects in a scene, a foundational step for marine exploration and robotics.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c1_underwater_salient_instance_segmenta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords underwater, salient, instance, segmentation, asks, find in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_hard_underwater_images_suffer`

- Preferred role: `method`
- Cue keywords: `but, hard, underwater, images, suffer, light, scattering, color, distortion, marine`
- Narration: But it is hard. Underwater images suffer light scattering, color distortion, and marine snow, so even top methods lose accuracy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_but_hard_underwater_images_suffer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, hard, underwater, images, suffer, light in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_field_lacked_large_scale_dataset_pix`

- Preferred role: `content`
- Cue keywords: `field, lacked, large-scale, dataset, pixel-level, salient, annotations, stalling, progress`
- Narration: The field has lacked a large-scale dataset with pixel-level salient annotations, stalling progress.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_field_lacked_large_scale_dataset_pix" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords field, lacked, large-scale, dataset, pixel-level, salient in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_foundation_models_like_sam_exist`

- Preferred role: `method`
- Cue keywords: `foundation, models, like, sam, exist, but, trained, natural, images, struggle`
- Narration: Foundation models like SAM exist, but were trained on natural images and struggle underwater.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_foundation_models_like_sam_exist" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords foundation, models, like, sam, exist, but in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_large_models_advancing_sam_spread`

- Preferred role: `content`
- Cue keywords: `large, models, advancing, sam, spread, across, computer, vision, but, underwater`
- Narration: With large models advancing, SAM has spread across computer vision, but using it underwater falls short.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_large_models_advancing_sam_spread" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, models, advancing, sam, spread, across in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_its_features_not_adapt_murky`

- Preferred role: `content`
- Cue keywords: `its, features, not, adapt, murky, low-contrast, water, needs, manual, foreground`
- Narration: Its features do not adapt to murky, low-contrast water, and it needs manual foreground prompts that defeat automatic salient segmentation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_its_features_not_adapt_murky" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, features, not, adapt, murky, low-contrast in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_authors_argue_unlocking_sam_requires`

- Preferred role: `figure`
- Cue keywords: `authors, argue, unlocking, sam, requires, two, things, once, large-scale, dataset`
- Narration: The authors argue that unlocking SAM here requires two things at once: a large-scale dataset capturing underwater saliency, and an architecture that teaches SAM to see underwater and prompt itself.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c3_authors_argue_unlocking_sam_requires" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, unlocking, sam, requires, two in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_delivers_both`

- Preferred role: `content`
- Cue keywords: `delivers, both`
- Narration: This paper delivers both.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_delivers_both" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords delivers, both in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, contributions`
- Narration: The paper makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_usis10k_first_large_scale_unde`

- Preferred role: `content`
- Cue keywords: `first, usis10k, first, large-scale, underwater, salient, instance, segmentation, dataset, 10`
- Narration: First, USIS10K, the first large-scale underwater salient instance segmentation dataset, with 10,632 pixel-level annotated images across seven categories.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_usis10k_first_large_scale_unde" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, usis10k, first, large-scale, underwater, salient in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_usis_sam_architecture_built_s`

- Preferred role: `method`
- Cue keywords: `second, usis-sam, architecture, built, sam, featuring, underwater, adaptive, visual, transformer`
- Narration: Second, USIS-SAM, an architecture built on SAM featuring an Underwater Adaptive Visual Transformer encoder and an out-of-the-box Salient Feature Prompt Generator that removes manual prompts.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_usis_sam_architecture_built_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, usis-sam, architecture, built, sam, featuring in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_extensive_experiments_show_bea`

- Preferred role: `method`
- Cue keywords: `third, extensive, experiments, show, beats, state-of-the-art, methods, code, released`
- Narration: Third, extensive experiments show it beats state-of-the-art methods, with data and code released.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_extensive_experiments_show_bea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, extensive, experiments, show, beats, state-of-the-art in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_usis_sam_keeps_sam_pretrained_backbo`

- Preferred role: `method`
- Cue keywords: `usis-sam, keeps, sam, pretrained, backbone, frozen, adds, two, lightweight, modules`
- Narration: USIS-SAM keeps SAM's pretrained backbone frozen and adds two lightweight modules.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_usis_sam_keeps_sam_pretrained_backbo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords usis-sam, keeps, sam, pretrained, backbone, frozen in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_underwater_adaptive_vit_encoder_inje`

- Preferred role: `method`
- Cue keywords: `underwater, adaptive, vit, encoder, injects, domain, knowledge, through, adapters, channel`
- Narration: The Underwater Adaptive ViT encoder injects domain knowledge through adapters: a channel adapter recalibrates features, while multi-scale convolutions of size three, five, and seven capture structures, balanced by average residuals to dampen noise.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_underwater_adaptive_vit_encoder_inje" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords underwater, adaptive, vit, encoder, injects, domain in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_top_salient_feature_prompt_generator`

- Preferred role: `method`
- Cue keywords: `top, salient, feature, prompt, generator, replaces, sam, manual, prompts, its`
- Narration: On top, the Salient Feature Prompt Generator replaces SAM's manual prompts. Its Salient Feature Fusion Module aggregates features from each UA-ViT block and produces salient prompt embeddings automatically, feeding SAM's mask decoder.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_top_salient_feature_prompt_generator" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, salient, feature, prompt, generator, replaces in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_trains_end_to_end_combined_region_cl`

- Preferred role: `result`
- Cue keywords: `trains, end-to-end, combined, region, classification, box, mask, loss`
- Narration: It trains end-to-end with a combined region, classification, box, and mask loss.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c4_trains_end_to_end_combined_region_cl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trains, end-to-end, combined, region, classification, box in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_break_bottleneck_authors_built_usis1`

- Preferred role: `method`
- Cue keywords: `break, bottleneck, authors, built, usis10k, first, large-scale, underwater, salient, instance`
- Narration: To break the data bottleneck, the authors built USIS10K, the first large-scale underwater salient instance segmentation dataset.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_break_bottleneck_authors_built_usis1" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords break, bottleneck, authors, built, usis10k, first in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_contains_10_632_underwater_images`

- Preferred role: `content`
- Cue keywords: `contains, 10, 632, underwater, images, pixel-level, annotations, spanning, seven, categories`
- Narration: It contains 10,632 underwater images, each with pixel-level annotations, spanning seven categories from diverse scenes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_contains_10_632_underwater_images" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contains, 10, 632, underwater, images, pixel-level in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_authors_analyze_carefully_instances`

- Preferred role: `method`
- Cue keywords: `authors, analyze, carefully, instances, per, category, instance, distribution, per, image`
- Narration: The authors analyze it carefully: instances per category, instance distribution per image, and global versus local color contrast against the prior SIS10K benchmark, showing underwater imagery poses distinct low-contrast challenges.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_authors_analyze_carefully_instances" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, analyze, carefully, instances, per, category in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_beyond_usis_sam_usis10k_gives_whole`

- Preferred role: `method`
- Cue keywords: `beyond, usis-sam, usis10k, gives, whole, community, foundation, underwater, salient, segmentation`
- Narration: Beyond training USIS-SAM, USIS10K gives the whole community a foundation for underwater salient segmentation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_beyond_usis_sam_usis10k_gives_whole" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beyond, usis-sam, usis10k, gives, whole, community in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_both_settings_usis_sam_sets`

- Preferred role: `content`
- Cue keywords: `across, both, settings, usis-sam, sets, new, state, art, usis10k`
- Narration: Across both settings, USIS-SAM sets a new state of the art on USIS10K.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_across_both_settings_usis_sam_sets" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, both, settings, usis-sam, sets, new in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_class_agnostic_task_localizing_maski`

- Preferred role: `method`
- Cue keywords: `class-agnostic, task, localizing, masking, salient, objects, regardless, category, reaches, 59.7`
- Narration: In the class-agnostic task, localizing and masking salient objects regardless of category, it reaches 59.7 mAP, beating the best salient method OQTR by 3.1 points, the underwater WaterMask by 0.7, and the SAM-based RSPrompter by 1.5.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_class_agnostic_task_localizing_maski" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords class-agnostic, task, localizing, masking, salient, objects in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_harder_multi_class_task_scores_43_1`

- Preferred role: `method`
- Cue keywords: `harder, multi-class, task, scores, 43.1, map, extending, its, lead, 4.4`
- Narration: In the harder multi-class task it scores 43.1 mAP, extending its lead to 4.4 points over WaterMask and 5.1 over RSPrompter.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_harder_multi_class_task_scores_43_1" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords harder, multi-class, task, scores, 43.1, map in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_also_generalizes_retrained_land_base`

- Preferred role: `method`
- Cue keywords: `also, generalizes, retrained, land-based, sis10k, dataset, still, outperforms, prior, approaches`
- Narration: It also generalizes: retrained on the land-based SIS10K dataset, it still outperforms prior approaches.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_also_generalizes_retrained_land_base" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, generalizes, retrained, land-based, sis10k, dataset in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_isolate_component`

- Preferred role: `content`
- Cue keywords: `ablations, isolate, component`
- Narration: Ablations isolate each component.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablations_isolate_component" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, isolate, component in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_starting_full_43_1_map_multi_class`

- Preferred role: `figure`
- Cue keywords: `starting, full, 43.1, map, multi-class, task, reverting, underwater, adaptive, vit`
- Narration: Starting from the full model at 43.1 mAP on the multi-class task, reverting the Underwater Adaptive ViT block to the original drops performance by 1.6 mAP, confirming that adapters help the frozen backbone handle complex marine scenes.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c2_starting_full_43_1_map_multi_class" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords starting, full, 43.1, map, multi-class, task in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_replacing_salient_feature_prompt_gen`

- Preferred role: `method`
- Cue keywords: `replacing, salient, feature, prompt, generator, generic, multi-scale, feature, enhancer, costs`
- Narration: Replacing the Salient Feature Prompt Generator with a generic Multi-scale Feature Enhancer costs 0.9 mAP, showing it does more than fuse features, it focuses attention on salient regions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_replacing_salient_feature_prompt_gen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords replacing, salient, feature, prompt, generator, generic in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_further_ablations_encoder_freezing_c`

- Preferred role: `method`
- Cue keywords: `further, ablations, encoder, freezing, convolution, design, confirm, choice, matters`
- Narration: Further ablations on encoder freezing and the convolution design confirm each choice matters.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_further_ablations_encoder_freezing_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords further, ablations, encoder, freezing, convolution, design in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_headline_numbers_tell_story_usis10k`

- Preferred role: `content`
- Cue keywords: `headline, numbers, tell, story, usis10k, brings, 10, 632, annotated, underwater`
- Narration: The headline numbers tell the story. USIS10K brings 10,632 annotated underwater images across seven categories.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_headline_numbers_tell_story_usis10k" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, numbers, tell, story, usis10k, brings in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_class_agnostic_segmentation_usis_sam`

- Preferred role: `result`
- Cue keywords: `class-agnostic, segmentation, usis-sam, reaches, 59.7, map, 81.6, fifty, percent, 67.7`
- Narration: On class-agnostic segmentation, USIS-SAM reaches 59.7 mAP, with 81.6 AP at fifty percent and 67.7 at seventy-five. On multi-class it reaches 43.1 mAP.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_class_agnostic_segmentation_usis_sam" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords class-agnostic, segmentation, usis-sam, reaches, 59.7, map in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_ablations_attribute_1_6_map_underwat`

- Preferred role: `method`
- Cue keywords: `ablations, attribute, 1.6, map, underwater, adaptive, vit, encoder, 0.9, salient`
- Narration: Ablations attribute 1.6 mAP to the Underwater Adaptive ViT encoder and 0.9 to the Salient Feature Prompt Generator.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_ablations_attribute_1_6_map_underwat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, attribute, 1.6, map, underwater, adaptive in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_used_24_epochs_six_nvidia`

- Preferred role: `method`
- Cue keywords: `used, 24, epochs, six, nvidia, 3090, gpus, vit-h, backbone`
- Narration: Training used 24 epochs on six NVIDIA 3090 GPUs with a ViT-H backbone.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_used_24_epochs_six_nvidia" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords used, 24, epochs, six, nvidia, 3090 in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_adapting_foundation_hard_new_domain`

- Preferred role: `content`
- Cue keywords: `adapting, foundation, hard, new, domain, works, best, when, you, also`
- Narration: Adapting a foundation model to a hard new domain works best when you also give it the right data and let it prompt itself.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_adapting_foundation_hard_new_domain" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adapting, foundation, hard, new, domain, works in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_building_usis10k_teaching_sam_see`

- Preferred role: `content`
- Cue keywords: `building, usis10k, teaching, sam, see, underwater, while, generating, its, own`
- Narration: By building USIS10K and teaching SAM to see underwater while generating its own salient prompts, USIS-SAM sets a new state of the art.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_building_usis10k_teaching_sam_see" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords building, usis10k, teaching, sam, see, underwater in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_dataset_code_released_lays_foundatio`

- Preferred role: `qr`
- Cue keywords: `dataset, code, released, lays, foundation, underwater, vision, research`
- Narration: With dataset and code released, it lays a foundation for underwater vision research.
- Authoring: Create or label one visible qr region for this narration chunk. Use id="cue_s10_c4_dataset_code_released_lays_foundatio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dataset, code, released, lays, foundation, underwater in title/desc so the matcher can verify semantic overlap.
