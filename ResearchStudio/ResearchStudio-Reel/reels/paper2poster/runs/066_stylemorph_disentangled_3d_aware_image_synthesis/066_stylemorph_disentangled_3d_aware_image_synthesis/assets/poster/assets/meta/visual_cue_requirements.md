# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_stylemorph_3_d_aware_generative_pull`

- Preferred role: `content`
- Cue keywords: `stylemorph, 3, d-aware, generative, pulls, apart, four, things, make, image`
- Narration: StyleMorph is a 3D-aware generative model that pulls apart the four things that make an image what it is: the object's 3D shape, the camera pose, the object's appearance, and the background.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_stylemorph_3_d_aware_generative_pull" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stylemorph, 3, d-aware, generative, pulls, apart in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_does_learning_3_morphable_nothing`

- Preferred role: `content`
- Cue keywords: `does, learning, 3, morphable, nothing, but, ordinary, 2, photos, 3`
- Narration: It does this by learning a 3D morphable model from nothing but ordinary 2D photos, with no 3D scans, no pose labels, and no template supplied by hand.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_does_learning_3_morphable_nothing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords does, learning, 3, morphable, nothing, but in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_trick_morph_single_canonical_3`

- Preferred role: `content`
- Cue keywords: `trick, morph, single, canonical, 3, template, render, its, coordinates, purely`
- Narration: The trick is to morph a single canonical 3D template and render its coordinates into a purely geometric 2D map, which then conditions a StyleGAN renderer for photorealistic synthesis.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_trick_morph_single_canonical_3" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trick, morph, single, canonical, 3, template in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_faces_cats_dogs_wild_animals`

- Preferred role: `content`
- Cue keywords: `faces, cats, dogs, wild, animals, stylemorph, matches, state-of-the-art, image, quality`
- Narration: On faces, cats, dogs, and wild animals, StyleMorph matches state-of-the-art image quality while giving you independent, fine-grained control over every factor of variation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_faces_cats_dogs_wild_animals" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords faces, cats, dogs, wild, animals, stylemorph in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_dream_3_d_aware_image_generation`

- Preferred role: `method`
- Cue keywords: `dream, 3, d-aware, image, generation, you, steer, one, where, you`
- Narration: The dream in 3D-aware image generation is a model you can steer, one where you change the pose without touching identity, or swap the background without disturbing the object.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_dream_3_d_aware_image_generation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dream, 3, d-aware, image, generation, you in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_today_best_3_d_aware_gans`

- Preferred role: `content`
- Cue keywords: `today, best, 3, d-aware, gans, make, beautiful, images, but, their`
- Narration: Today's best 3D-aware GANs make beautiful images, but their hybrid design fuses geometry and appearance together, so editing one factor bleeds into the others.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_today_best_3_d_aware_gans" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords today, best, 3, d-aware, gans, make in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_classical_3_morphable_models_solve`

- Preferred role: `content`
- Cue keywords: `classical, 3, morphable, models, solve, control, problem, elegantly, yet, they`
- Narration: Classical 3D morphable models solve the control problem elegantly, yet they require expensive 3D scanning and painstaking manual alignment, which is why they mainly exist for human faces.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_classical_3_morphable_models_solve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classical, 3, morphable, models, solve, control in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_stylemorph_asks_whether_get_morphabl`

- Preferred role: `method`
- Cue keywords: `stylemorph, asks, whether, get, morphable-model, control, arbitrary, object, categories, learning`
- Narration: StyleMorph asks whether we can get morphable-model control for arbitrary object categories, learning everything from unstructured 2D images alone.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_stylemorph_asks_whether_get_morphabl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stylemorph, asks, whether, get, morphable-model, control in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_morphable_models_workhorse_visual_ef`

- Preferred role: `content`
- Cue keywords: `morphable, models, workhorse, visual, effects, augmented, reality, because, they, hand`
- Narration: Morphable models are the workhorse of visual effects and augmented reality because they hand creators clean, separate dials for pose, expression, and appearance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_morphable_models_workhorse_visual_ef" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords morphable, models, workhorse, visual, effects, augmented in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_question_motivates_work_simple_get`

- Preferred role: `title`
- Cue keywords: `question, motivates, work, simple, get, same, level, control, inside, modern`
- Narration: The question that motivates this work is simple: can we get that same level of control inside a modern 3D-aware GAN, but without any of the 3D supervision that morphable models normally need?
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c2_question_motivates_work_simple_get" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords question, motivates, work, simple, get, same in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_prior_work_added_3_deformations`

- Preferred role: `content`
- Cue keywords: `prior, work, added, 3, deformations, synthesis, either, stayed, limited, single`
- Narration: Prior work that added 3D deformations to synthesis either stayed limited to a single dynamic scene, or leaned on a deformable template that already existed for the category.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_prior_work_added_3_deformations" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, work, added, 3, deformations, synthesis in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_stylemorph_instead_turns_morphable_i`

- Preferred role: `content`
- Cue keywords: `stylemorph, instead, turns, morphable, itself, something, network, discovers, unlabeled, 2`
- Narration: StyleMorph instead turns the morphable model itself into something the network discovers from unlabeled 2D images, making it a first-class citizen of generative modelling.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_stylemorph_instead_turns_morphable_i" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stylemorph, instead, turns, morphable, itself, something in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_stylemorph_makes_three_linked_contri`

- Preferred role: `content`
- Cue keywords: `stylemorph, makes, three, linked, contributions, first, learns, 3, morphable, object`
- Narration: StyleMorph makes three linked contributions. First, it learns a 3D morphable model of an object category's non-rigid shape variation using nothing but 2D images, by morphing a canonical template through backpropagation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_stylemorph_makes_three_linked_contri" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stylemorph, makes, three, linked, contributions, first in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_introduces_template_object_co`

- Preferred role: `method`
- Cue keywords: `second, introduces, template, object, coordinates, tocs, deformable, cousin, normalized, object`
- Narration: Second, it introduces Template Object Coordinates, or TOCS: a deformable cousin of Normalized Object Coordinates that gives every surface point a stable template identity and acts as a powerful, deformation-equivariant descriptor of shape.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_second_introduces_template_object_co" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, introduces, template, object, coordinates, tocs in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_feeds_2_tocs_maps`

- Preferred role: `content`
- Cue keywords: `third, feeds, 2, tocs, maps, purely, geometric, conditioning, signal, stylegan-based`
- Narration: Third, it feeds 2D TOCS maps as a purely geometric conditioning signal into a StyleGAN-based deferred neural renderer, cleanly separating shape from appearance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_third_feeds_2_tocs_maps" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, feeds, 2, tocs, maps, purely in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_together_these_deliver_disentangled`

- Preferred role: `content`
- Cue keywords: `together, these, deliver, disentangled, control, over, pose, shape, object, appearance`
- Narration: Together these deliver disentangled control over pose, shape, object appearance, and background, all at high resolution.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_together_these_deliver_disentangled" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, these, deliver, disentangled, control, over in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_two_halves_geometry_side`

- Preferred role: `method`
- Cue keywords: `method, two, halves, geometry, side, morphable, renderer, learns, deformation-free, object`
- Narration: The method has two halves. On the geometry side, a Morphable Renderer learns a deformation-free object in canonical template coordinates as a constant implicit function. A SIREN-based deformation field, driven by a shape code, warps each camera ray from world space into that template space by adding a predicted offset.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_two_halves_geometry_side" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, two, halves, geometry, side, morphable in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_integrating_template_coordinates_alo`

- Preferred role: `content`
- Cue keywords: `integrating, template, coordinates, along, ray, produces, 2, map, called, tocs`
- Narration: Integrating the template coordinates along each ray produces a 2D map called a TOCS map, which encodes the compounded effects of shape deformation, camera pose, and perspective, and nothing about appearance.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_integrating_template_coordinates_alo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords integrating, template, coordinates, along, ray, produces in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_synthesis_side_stylegan2_based_defer`

- Preferred role: `content`
- Cue keywords: `synthesis, side, stylegan2-based, deferred, neural, renderer, takes, geometric, tocs, map`
- Narration: On the synthesis side, a StyleGAN2-based deferred neural renderer takes this geometric TOCS map together with two independent appearance codes, one for the foreground object and one for the background scene, and generates a high-resolution image. The foreground and background are composited with an alpha mask predicted by the model.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_synthesis_side_stylegan2_based_defer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords synthesis, side, stylegan2-based, deferred, neural, renderer in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_proceeds_two_stages_first_deformable`

- Preferred role: `method`
- Cue keywords: `proceeds, two, stages, first, deformable, volume, renderer, learns, realistic, shape`
- Narration: Training proceeds in two stages: first the deformable volume renderer learns realistic shape at low resolution with weak silhouette supervision, then it is frozen and used only to supply TOCS maps while the 2D renderer is trained for photorealistic full-resolution output.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_proceeds_two_stages_first_deformable" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords proceeds, two, stages, first, deformable, volume in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_stylemorph_evaluated_four_widely_use`

- Preferred role: `content`
- Cue keywords: `stylemorph, evaluated, four, widely, used, image, datasets`
- Narration: StyleMorph is evaluated on four widely used image datasets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_stylemorph_evaluated_four_widely_use" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stylemorph, evaluated, four, widely, used, image in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_ffhq_contributes_seventy_thousand_ce`

- Preferred role: `content`
- Cue keywords: `ffhq, contributes, seventy, thousand, centered, human, face, photos, range, challenging`
- Narration: FFHQ contributes seventy thousand centered human face photos with a range of challenging backgrounds and poses.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_ffhq_contributes_seventy_thousand_ce" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ffhq, contributes, seventy, thousand, centered, human in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_afhq_collection_adds_animal_faces`

- Preferred role: `content`
- Cue keywords: `afhq, collection, adds, animal, faces, three, splits, roughly, fifty-six, hundred`
- Narration: The AFHQ collection adds animal faces in three splits: roughly fifty-six hundred cats, fifty-two hundred dogs, and fifty-two hundred wild animals.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_afhq_collection_adds_animal_faces" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords afhq, collection, adds, animal, faces, three in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_authors_report_frechet_inception_dis`

- Preferred role: `result`
- Cue keywords: `authors, report, frechet, inception, distance, two-fifty-six, resolution, comparing, against, eleven`
- Narration: The authors report Frechet Inception Distance at two-fifty-six resolution, comparing against eleven state-of-the-art 3D-aware GAN baselines, so the results test both photorealism on faces and the ability to generalize to animal categories that classical morphable models never covered.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_authors_report_frechet_inception_dis" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, report, frechet, inception, distance, two-fifty-six in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_disentanglement_doe`

- Preferred role: `content`
- Cue keywords: `headline, finding, disentanglement, does, not, cost, image, quality`
- Narration: The headline finding is that disentanglement does not have to cost image quality.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_headline_finding_disentanglement_doe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, disentanglement, does, not, cost in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_stylemorph_reaches_frechet_inception`

- Preferred role: `result`
- Cue keywords: `stylemorph, reaches, frechet, inception, distance, seven, point, nine, one, ffhq`
- Narration: StyleMorph reaches a Frechet Inception Distance of seven point nine one on FFHQ faces, and four point two nine on cats, three point four nine on wild animals, and thirteen point nine five on dogs, all at two-fifty-six resolution.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_stylemorph_reaches_frechet_inception" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stylemorph, reaches, frechet, inception, distance, seven in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_these_numbers_sit_right_alongside`

- Preferred role: `method`
- Cue keywords: `these, numbers, sit, right, alongside, strongest, 3, d-aware, gans, offer`
- Narration: These numbers sit right alongside the strongest 3D-aware GANs that offer none of StyleMorph's control.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_these_numbers_sit_right_alongside" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, numbers, sit, right, alongside, strongest in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_comparison_matters_most_against_dise`

- Preferred role: `method`
- Cue keywords: `comparison, matters, most, against, disentangled3d, only, prior, method, also, represents`
- Narration: The comparison that matters most is against Disentangled3D, the only prior method that also represents shape with a deformable template: StyleMorph's FFHQ score of seven point nine one is far ahead of its twenty-eight point one eight, and StyleMorph additionally separates foreground from background, which that method does not.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_comparison_matters_most_against_dise" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords comparison, matters, most, against, disentangled3d, only in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_all_run_under_fair`

- Preferred role: `method`
- Cue keywords: `ablations, all, run, under, fair, ninety-six-hour, budget, isolate, design, choice`
- Narration: The ablations, all run under a fair ninety-six-hour training budget, isolate each design choice. Swapping TOCS for plain NOCS raises FID from about eight point three to eight point nine and blurs the conditioning signal, showing template-space coordinates matter.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_ablations_all_run_under_fair" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, all, run, under, fair, ninety-six-hour in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_removing_deformable_module_direct_oc`

- Preferred role: `method`
- Cue keywords: `removing, deformable, module, direct, occupancy, network, instead, keeps, fid, similar`
- Narration: Removing the deformable module and using a direct occupancy network instead keeps FID similar but drastically worsens the consistency scores, proving the value of modelling shape through deformation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_removing_deformable_module_direct_oc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords removing, deformable, module, direct, occupancy, network in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_switching_late_fusion_early_fusion`

- Preferred role: `content`
- Cue keywords: `switching, late, fusion, early, fusion, nudges, fid, down, slightly, but`
- Narration: Switching from late fusion to early fusion nudges FID down slightly but badly hurts alpha consistency, letting foreground and background bleed together.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_switching_late_fusion_early_fusion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords switching, late, fusion, early, fusion, nudges in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_finally_directly_optimizing_view_con`

- Preferred role: `figure`
- Cue keywords: `finally, directly, optimizing, view, consistency, differentiable, loss, does, improve, metric`
- Narration: Finally, directly optimizing view consistency as a differentiable loss does improve that metric, from nearly sixteen down to eight, but it trades away image quality, pushing FID up to twelve point three.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c4_finally_directly_optimizing_view_con" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, directly, optimizing, view, consistency, differentiable in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_ffhq`

- Preferred role: `method`
- Cue keywords: `few, numbers, capture, impact, ffhq, faces, stylemorph, scores, seven, point`
- Narration: A few numbers capture the impact. On FFHQ faces StyleMorph scores a seven point nine one FID, versus twenty-eight point one eight for the only competing template-based method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_ffhq" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, ffhq, faces in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_animals_reaches_four_point_two`

- Preferred role: `result`
- Cue keywords: `animals, reaches, four, point, two, nine, cats, three, point, four`
- Narration: On animals it reaches four point two nine on cats, three point four nine on wild, and thirteen point nine five on dogs. It disentangles four independent factors: shape, camera pose, foreground appearance, and background appearance.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_animals_reaches_four_point_two" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords animals, reaches, four, point, two, nine in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_core_tocs_versus_nocs_ablation_shows`

- Preferred role: `content`
- Cue keywords: `core, tocs-versus-nocs, ablation, shows, template, coordinates, improving, fid, eight, point`
- Narration: And the core TOCS-versus-NOCS ablation shows template coordinates improving FID from eight point nine to eight point three while also sharpening disentanglement.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_core_tocs_versus_nocs_ablation_shows" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, tocs-versus-nocs, ablation, shows, template, coordinates in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_all_learned_unstructured_2_images`

- Preferred role: `method`
- Cue keywords: `all, learned, unstructured, 2, images, 3, supervision, all`
- Narration: All of this is learned from unstructured 2D images, with no 3D supervision at all.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_all_learned_unstructured_2_images" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, learned, unstructured, 2, images, 3 in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_one_line_takeaway_stylemorph_deliver`

- Preferred role: `takeaway`
- Cue keywords: `one-line, takeaway, stylemorph, delivers, morphable-model, control, inside, state-of-the-art, image, generator`
- Narration: The one-line takeaway is that StyleMorph delivers morphable-model control inside a state-of-the-art image generator, learned entirely from ordinary 2D photos.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_one_line_takeaway_stylemorph_deliver" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one-line, takeaway, stylemorph, delivers, morphable-model, control in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_morphing_learned_canonical_template`

- Preferred role: `content`
- Cue keywords: `morphing, learned, canonical, template, rendering, purely, geometric, tocs, map, hands`
- Narration: By morphing a learned canonical template and rendering it into a purely geometric TOCS map, it hands a StyleGAN renderer a clean geometric signal, so shape, pose, object appearance, and background can each be edited independently without sacrificing photorealism.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_morphing_learned_canonical_template" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords morphing, learned, canonical, template, rendering, purely in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_effect_builds_unsupervised_3_morphab`

- Preferred role: `content`
- Cue keywords: `effect, builds, unsupervised, 3, morphable, general, object, categories, extending, fine-grained`
- Narration: In effect it builds an unsupervised 3D morphable model for general object categories, extending the fine-grained controllability that visual-effects artists rely on from faces to cats, dogs, and wild animals.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_effect_builds_unsupervised_3_morphab" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords effect, builds, unsupervised, 3, morphable, general in title/desc so the matcher can verify semantic overlap.
