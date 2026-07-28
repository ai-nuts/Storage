# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_what_could_not_only_tell`

- Preferred role: `method`
- Cue keywords: `what, could, not, only, tell, you, where, street, photo, taken`
- Narration: What if an AI could not only tell you where a street photo was taken, but explain how it knew? This paper introduces GeoReasoner, a large vision-language model for street-view geo-localization that reasons like a human.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_what_could_not_only_tell" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, could, not, only, tell, you in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_tackle_two_long_standing_obs`

- Preferred role: `method`
- Cue keywords: `authors, tackle, two, long-standing, obstacles, street-view, full, low-quality, images, visual`
- Narration: The authors tackle two long-standing obstacles: street-view training data is full of low-quality images with no visual clues, and existing localization models are black boxes that give no explanation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_authors_tackle_two_long_standing_obs" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, tackle, two, long-standing, obstacles, street-view in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_georeasoner_solves_both_quantifying`

- Preferred role: `content`
- Cue keywords: `georeasoner, solves, both, quantifying, how, locatable, image, borrowing, human, inference`
- Narration: GeoReasoner solves both by quantifying how locatable each image is, borrowing human inference knowledge from real geo-localization games, and fine-tuning in two dedicated stages.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_georeasoner_solves_both_quantifying" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords georeasoner, solves, both, quantifying, how, locatable in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_result_beats_comparable_vision_langu`

- Preferred role: `method`
- Cue keywords: `result, beats, comparable, vision-language, models, over, twenty-five, percent, country, level`
- Narration: The result beats comparable vision-language models by over twenty-five percent at country level and thirty-eight percent at city level, while matching a specialist trained on fifteen times more data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_result_beats_comparable_vision_langu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, beats, comparable, vision-language, models, over in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_predicting_where_street_view_photo_t`

- Preferred role: `method`
- Cue keywords: `predicting, where, street-view, photo, taken, useful, urban, planning, navigation, social`
- Narration: Predicting where a street-view photo was taken is useful for urban planning, navigation, and social studies. But today's approaches have two blind spots.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_predicting_where_street_view_photo_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords predicting, where, street-view, photo, taken, useful in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_first_problem_street_view_datasets_s`

- Preferred role: `method`
- Cue keywords: `first, problem, street-view, datasets, stuffed, images, captured, tunnels, against, blank`
- Narration: First, the data problem: street-view datasets are stuffed with images captured in tunnels, against blank walls, or of generic vegetation, none of which contain clues a model could use to locate them.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_first_problem_street_view_datasets_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, problem, street-view, datasets, stuffed, images in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_second_reasoning_problem_retrieval_c`

- Preferred role: `result`
- Cue keywords: `second, reasoning, problem, retrieval, classification, models, operate, black, boxes, handing`
- Narration: Second, the reasoning problem: retrieval and classification models operate as black boxes, handing back a coordinate with no explanation a person could inspect or trust.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c3_second_reasoning_problem_retrieval_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, reasoning, problem, retrieval, classification, models in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_argues_both_quality_interpretability`

- Preferred role: `content`
- Cue keywords: `argues, both, quality, interpretability, must, fixed, together`
- Narration: This paper argues that both quality and interpretability must be fixed together.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_argues_both_quality_interpretability" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords argues, both, quality, interpretability, must, fixed in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_now_why_approach`

- Preferred role: `content`
- Cue keywords: `why, now, why, approach`
- Narration: Why now, and why this approach?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_why_now_why_approach" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, now, why, approach in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_large_vision_language_models_shown_t`

- Preferred role: `method`
- Cue keywords: `large, vision-language, models, shown, they, fuse, images, text, follow, step-by-step`
- Narration: Large vision-language models have shown they can fuse images and text and follow step-by-step reasoning, and prior research shows that adding a reasoning process makes language models stronger.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_large_vision_language_models_shown_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, vision-language, models, shown, they, fuse in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_meanwhile_huge_untapped_resource_exi`

- Preferred role: `content`
- Cue keywords: `meanwhile, huge, untapped, resource, exists, communities, behind, geo-localization, games, spent`
- Narration: Meanwhile, a huge untapped resource exists: communities behind geo-localization games have spent years assembling textual clues that pinpoint countries and cities from subtle visual details.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_meanwhile_huge_untapped_resource_exi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords meanwhile, huge, untapped, resource, exists, communities in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_georeasoner_insight_harvest_human_in`

- Preferred role: `method`
- Cue keywords: `georeasoner, insight, harvest, human, inference, knowledge, pair, high-quality, street, views`
- Narration: GeoReasoner's insight is to harvest that human inference knowledge and pair it with high-quality street views, so the model learns not just to guess a location but to justify it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_georeasoner_insight_harvest_human_in" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords georeasoner, insight, harvest, human, inference, knowledge in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_work_makes_three_contributions`

- Preferred role: `content`
- Cue keywords: `work, makes, three, contributions`
- Narration: The work makes three contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_work_makes_three_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, makes, three, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_introduces_new_paradigm_leverages_la`

- Preferred role: `content`
- Cue keywords: `introduces, new, paradigm, leverages, large, vision-language, together, external, human, reasoning`
- Narration: It introduces a new paradigm that leverages a large vision-language model together with external human reasoning knowledge learned from online games, enabling geo-localization that comes with an explanation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_introduces_new_paradigm_leverages_la" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, new, paradigm, leverages, large, vision-language in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_defines_concept_locatability_metric`

- Preferred role: `method`
- Cue keywords: `defines, concept, locatability, metric, how, findable, image, location, builds, clip-based`
- Narration: It defines the concept of locatability, a metric for how findable an image's location is, and builds a CLIP-based network to compute it, which drives the curation of a clean, high-quality training set.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_defines_concept_locatability_metric" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords defines, concept, locatability, metric, how, findable in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_delivers_georeasoner_itself_beats_ex`

- Preferred role: `content`
- Cue keywords: `delivers, georeasoner, itself, beats, existing, geo-localization, systems, while, offering, detailed`
- Narration: And it delivers GeoReasoner itself, a model that beats existing geo-localization systems while offering detailed reasoning for every prediction.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_delivers_georeasoner_itself_beats_ex" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords delivers, georeasoner, itself, beats, existing, geo-localization in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_two_halves_first_curation`

- Preferred role: `method`
- Cue keywords: `method, two, halves, first, curation, georeasoner, introduces, locatability, metric, maskformer`
- Narration: The method has two halves. First, data curation. GeoReasoner introduces a locatability metric: MaskFormer segments each street view into semantic classes like buildings, sky, and vehicles, producing a vector of area ratios.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_two_halves_first_curation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, two, halves, first, curation, georeasoner in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_sentence_bert_measures_how_relevant`

- Preferred role: `content`
- Cue keywords: `sentence-bert, measures, how, relevant, class, textual, clues, mined, geo-games, producing`
- Narration: Sentence-BERT then measures how relevant each class is to the textual clues mined from geo-games, producing a weight vector.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_sentence_bert_measures_how_relevant" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sentence-bert, measures, how, relevant, class, textual in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_locatability_image_simply_weighted_s`

- Preferred role: `result`
- Cue keywords: `locatability, image, simply, weighted, sum, its, class, ratios, against, these`
- Narration: The locatability of an image is simply the weighted sum of its class ratios against these importance weights, and images scoring above a threshold of zero point four are kept. This filters over one hundred thirty thousand raw images down to seventy thousand high-quality ones. Second, the model.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_locatability_image_simply_weighted_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords locatability, image, simply, weighted, sum, its in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_built_qwen_vl_vision_encoder_vision`

- Preferred role: `method`
- Cue keywords: `built, qwen-vl, vision, encoder, vision-language, adapter, pre-trained, language, georeasoner, fine-tuned`
- Narration: Built on Qwen-VL with a vision encoder, a vision-language adapter, and a pre-trained language model, GeoReasoner is fine-tuned in two stages using lightweight LoRA adapters: a reasoning-tuning stage that learns country-level explanations from game clues, followed by a location-tuning stage that sharpens city-level accuracy on the curated street views.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_built_qwen_vl_vision_encoder_vision" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords built, qwen-vl, vision, encoder, vision-language, adapter in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_builds_its_scratch_openstreetmap_roa`

- Preferred role: `method`
- Cue keywords: `builds, its, scratch, openstreetmap, road, networks, google, street, view, api`
- Narration: The paper builds its data from scratch. Using OpenStreetMap road networks and the Google Street View API, the authors sample points every four thousand meters across the top global cities, collecting more than one hundred thirty thousand geo-tagged street views spanning seventy-two cities in forty-eight countries.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_builds_its_scratch_openstreetmap_roa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords builds, its, scratch, openstreetmap, road, networks in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_applying_locatability_filter_thresho`

- Preferred role: `content`
- Cue keywords: `applying, locatability, filter, threshold, zero, point, four, yields, roughly, seventy`
- Narration: Applying the locatability filter at a threshold of zero point four yields roughly seventy thousand high-quality images.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_applying_locatability_filter_thresho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords applying, locatability, filter, threshold, zero, point in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_separately_they_scrape_over_three`

- Preferred role: `method`
- Cue keywords: `separately, they, scrape, over, three, thousand, textual, clues, two, geo-localization`
- Narration: Separately, they scrape over three thousand textual clues from two geo-localization games, GeoGuessr and Tuxun, cleaning them with a BERT-based entity recognizer and pairing each with a street-view image.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_separately_they_scrape_over_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separately, they, scrape, over, three, thousand in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_evaluation_they_held_out_set_thousan`

- Preferred role: `result`
- Cue keywords: `evaluation, they, held-out, set, thousand, images, test, generalization, standard, im2gps`
- Narration: For evaluation they use a held-out set of a thousand images and, to test generalization, the standard Im2GPS and Im2GPS3k Flickr benchmarks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_evaluation_they_held_out_set_thousan" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, they, held-out, set, thousand, images in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_decisive`

- Preferred role: `result`
- Cue keywords: `headline, result, decisive`
- Narration: The headline result is decisive.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_headline_result_decisive" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, decisive in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_measured_1_score_georeasoner_beats`

- Preferred role: `method`
- Cue keywords: `measured, 1, score, georeasoner, beats, strongest, comparable, vision-language, qwen-vl, just`
- Narration: Measured by F1 score, GeoReasoner beats the strongest comparable vision-language model, Qwen-VL, by just over twenty-five percent at country level and nearly thirty-nine percent at city level, reaching a country F1 of zero point nine zero and a city F1 of zero point eight six.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_measured_1_score_georeasoner_beats" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords measured, 1, score, georeasoner, beats, strongest in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_even_more_striking_edges_out`

- Preferred role: `method`
- Cue keywords: `even, more, striking, edges, out, streetclip, built, specifically, geo-localization, trained`
- Narration: Even more striking, it edges out StreetCLIP, a model built specifically for geo-localization and trained on one point one million street views, while GeoReasoner uses only seventy thousand.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_even_more_striking_edges_out" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords even, more, striking, edges, out, streetclip in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_authors_also_show_fraction_high_loca`

- Preferred role: `method`
- Cue keywords: `authors, also, show, fraction, high-locatability, images, rises, zero, one, hundred`
- Narration: The authors also show that as the fraction of high-locatability images in training rises from zero to one hundred percent, accuracy climbs steadily, proving that the quality of the curated data, not merely its quantity, is what powers the gains.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_authors_also_show_fraction_high_loca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, show, fraction, high-locatability, images in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_isolates_contribution_fine`

- Preferred role: `content`
- Cue keywords: `ablation, isolates, contribution, fine-tuning, stage, starting, qwen-vl, baseline, adding, only`
- Narration: An ablation isolates the contribution of each fine-tuning stage. Starting from the Qwen-VL baseline, adding only reasoning tuning improves country and city F1 modestly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_ablation_isolates_contribution_fine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, isolates, contribution, fine-tuning, stage, starting in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_adding_only_location_tuning_produces`

- Preferred role: `content`
- Cue keywords: `adding, only, location, tuning, produces, much, larger, jump, especially, fine-grained`
- Narration: Adding only location tuning produces a much larger jump, especially at the fine-grained city level, confirming that location tuning is essential for pinpointing cities.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_adding_only_location_tuning_produces" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adding, only, location, tuning, produces, much in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_but_full_both_stages_stacked`

- Preferred role: `method`
- Cue keywords: `but, full, both, stages, stacked, strongest, all, reaching, country, 1`
- Narration: But the full model, with both stages stacked, is the strongest of all, reaching a country F1 of zero point nine zero and a city F1 of zero point eight six.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_but_full_both_stages_stacked" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, full, both, stages, stacked, strongest in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_two_stages_complementary_location_tu`

- Preferred role: `result`
- Cue keywords: `two, stages, complementary, location, tuning, supplies, precision, reasoning, tuning, supplies`
- Narration: The two stages are complementary: location tuning supplies precision, reasoning tuning supplies explanations and a further accuracy lift.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_two_stages_complementary_location_tu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, stages, complementary, location, tuning, supplies in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_matter_georeasoner_improves`

- Preferred role: `content`
- Cue keywords: `numbers, matter, georeasoner, improves, best, comparable, vision-language, twenty-five, point, zero`
- Narration: The numbers that matter: GeoReasoner improves on the best comparable vision-language model by twenty-five point zero two percent at the country level and thirty-eight point six one percent at the city level in F1.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_numbers_matter_georeasoner_improves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, matter, georeasoner, improves, best, comparable in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_its_full_model_1_scores_zero`

- Preferred role: `method`
- Cue keywords: `its, full-model, 1, scores, zero, point, nine, zero, country, zero`
- Narration: Its full-model F1 scores are zero point nine zero for country and zero point eight six for city. It achieves this with just seventy thousand training images, versus the one point one million used by StreetCLIP, which it nonetheless surpasses.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_its_full_model_1_scores_zero" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, full-model, 1, scores, zero, point in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_underlying_comes_more_one_hundred`

- Preferred role: `method`
- Cue keywords: `underlying, comes, more, one, hundred, thirty, thousand, raw, street, views`
- Narration: The underlying data comes from more than one hundred thirty thousand raw street views across seventy-two cities and forty-eight countries, filtered down to seventy thousand, plus three thousand human-written reasoning clues from geo-games.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c3_underlying_comes_more_one_hundred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords underlying, comes, more, one, hundred, thirty in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_open_im2gps_benchmarks_only_ten`

- Preferred role: `method`
- Cue keywords: `open, im2gps, benchmarks, only, ten, thousand, flickr, images, enough, rival`
- Narration: And on the open Im2GPS benchmarks, only ten thousand Flickr images are enough to rival models trained on millions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_open_im2gps_benchmarks_only_ten" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords open, im2gps, benchmarks, only, ten, thousand in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple_but_powerful_you`

- Preferred role: `method`
- Cue keywords: `takeaway, simple, but, powerful, you, not, need, millions, street-view, images`
- Narration: The takeaway is simple but powerful. You do not need millions of street-view images to build a state-of-the-art geo-localization model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_takeaway_simple_but_powerful_you" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple, but, powerful, you, not in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_you_need_right_images_right`

- Preferred role: `content`
- Cue keywords: `you, need, right, images, right, knowledge`
- Narration: You need the right images and the right knowledge.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_you_need_right_images_right" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords you, need, right, images, right, knowledge in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_quantifying_which_street_views_actua`

- Preferred role: `method`
- Cue keywords: `quantifying, which, street, views, actually, locatable, borrowing, reasoning, strategies, humans`
- Narration: By quantifying which street views are actually locatable and by borrowing the reasoning strategies humans use to win geo-games, GeoReasoner matches or beats specialist models with a fraction of the data, and, crucially, it explains every prediction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_quantifying_which_street_views_actua" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords quantifying, which, street, views, actually, locatable in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_case_study_how_quality_human`

- Preferred role: `content`
- Cue keywords: `case, study, how, quality, human, inference, knowledge, stand, brute-force, scale`
- Narration: It is a case study in how data quality and human inference knowledge can stand in for brute-force scale, opening a path to geo-localization that is both interpretable and resource-efficient.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c4_case_study_how_quality_human" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords case, study, how, quality, human, inference in title/desc so the matcher can verify semantic overlap.
