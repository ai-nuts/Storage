# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_machine_learning_promises_accelerate`

- Preferred role: `content`
- Cue keywords: `machine, learning, promises, accelerate, therapeutic, antibody, design, but, only, models`
- Narration: Machine learning promises to accelerate therapeutic antibody design, but only if models can accurately read the sequence-to-function fitness landscape.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_machine_learning_promises_accelerate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords machine, learning, promises, accelerate, therapeutic, antibody in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_introduces_flab_fitness_landscape_an`

- Preferred role: `result`
- Cue keywords: `introduces, flab, fitness, landscape, antibodies, largest, therapeutic, antibody, benchmark, date`
- Narration: This paper introduces FLAb, the Fitness Landscape for Antibodies, the largest therapeutic antibody benchmark to date.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c2_introduces_flab_fitness_landscape_an" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, flab, fitness, landscape, antibodies, largest in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_gathers_experimental_measurements_si`

- Preferred role: `method`
- Cue keywords: `gathers, experimental, measurements, six, developability, properties, them, stress-test, six, widely`
- Narration: It gathers experimental measurements for six developability properties and uses them to stress-test six widely used deep learning protein models against physics-based Rosetta.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_gathers_experimental_measurements_si" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gathers, experimental, measurements, six, developability, properties in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_headline_finding_sobering_single_cor`

- Preferred role: `content`
- Cue keywords: `headline, finding, sobering, single, correlates, well, all, six, properties, performance`
- Narration: The headline finding is sobering: no single model correlates well with all six properties, and performance swings sharply across datasets of the same property, revealing how far the field still has to go.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_headline_finding_sobering_single_cor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, sobering, single, correlates, well in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_machine_learning_only_speed_antibody`

- Preferred role: `content`
- Cue keywords: `machine, learning, only, speed, antibody, design, models, truly, understand, what`
- Narration: Machine learning can only speed up antibody design if models truly understand what makes an antibody good.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_machine_learning_only_speed_antibody" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords machine, learning, only, speed, antibody, design in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_yet_major_protein_fitness_benchmarks`

- Preferred role: `result`
- Cue keywords: `yet, major, protein, fitness, benchmarks, like, cafa, tape, flip, either`
- Narration: Yet the major protein fitness benchmarks, like CAFA, TAPE, and FLIP, either leave antibody data out entirely or include only a sliver of it.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c2_yet_major_protein_fitness_benchmarks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yet, major, protein, fitness, benchmarks, like in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_leaves_researchers_principled_way_ch`

- Preferred role: `content`
- Cue keywords: `leaves, researchers, principled, way, check, whether, deep, learning, actually, captures`
- Narration: That leaves researchers with no principled way to check whether a deep learning model actually captures antibody fitness.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_leaves_researchers_principled_way_ch" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords leaves, researchers, principled, way, check, whether in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_today_field_often_falls_back`

- Preferred role: `content`
- Cue keywords: `today, field, often, falls, back, weak, proxies, such, native, sequence`
- Narration: Today the field often falls back on weak proxies such as native sequence recovery, which say little about real therapeutic potential.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_today_field_often_falls_back" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords today, field, often, falls, back, weak in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_therapeutic_antibody_satisfy_many_de`

- Preferred role: `content`
- Cue keywords: `therapeutic, antibody, satisfy, many, demands, once, must, express, well, stay`
- Narration: A therapeutic antibody has to satisfy many demands at once: it must express well, stay stable, avoid triggering an immune response, bind its target tightly, resist aggregation, and steer clear of sticking to the wrong things.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_therapeutic_antibody_satisfy_many_de" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords therapeutic, antibody, satisfy, many, demands, once in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_these_properties_often_pull_against`

- Preferred role: `result`
- Cue keywords: `these, properties, often, pull, against, other, improving, one, hurt, another`
- Narration: These properties often pull against each other, so improving one can hurt another.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_these_properties_often_pull_against" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, properties, often, pull, against, other in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_could_reliably_score_candidates_acro`

- Preferred role: `method`
- Cue keywords: `could, reliably, score, candidates, across, all, these, axes, could, replace`
- Narration: If a model could reliably score candidates across all of these axes, it could replace slow and expensive wet-lab screening.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_could_reliably_score_candidates_acro" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords could, reliably, score, candidates, across, all in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_new_antibody_design_methods_keep`

- Preferred role: `method`
- Cue keywords: `new, antibody, design, methods, keep, appearing, field, needs, one, shared`
- Narration: As new antibody design methods keep appearing, the field needs one shared, antibody-focused benchmark to judge them fairly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_new_antibody_design_methods_keep" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords new, antibody, design, methods, keep, appearing in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_fill_gap_authors_build_flab`

- Preferred role: `result`
- Cue keywords: `fill, gap, authors, build, flab, fitness, landscape, antibodies, largest, therapeutic`
- Narration: To fill this gap, the authors build FLAb, the Fitness Landscape for Antibodies, the largest therapeutic antibody design benchmark assembled so far.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c1_fill_gap_authors_build_flab" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fill, gap, authors, build, flab, fitness in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_curates_seventeen_mutational_landsca`

- Preferred role: `content`
- Cue keywords: `curates, seventeen, mutational, landscapes, more, thirteen, thousand, experimental, fitness, measurements`
- Narration: It curates seventeen mutational landscapes with more than thirteen thousand experimental fitness measurements, spanning six developability properties.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_curates_seventeen_mutational_landsca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords curates, seventeen, mutational, landscapes, more, thirteen in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_benchmark_they_evaluate_six_widely`

- Preferred role: `method`
- Cue keywords: `benchmark, they, evaluate, six, widely, adopted, pretrained, protein, models, compare`
- Narration: Using this benchmark, they evaluate six widely adopted pretrained protein models and compare them to physics-based Rosetta.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_benchmark_they_evaluate_six_widely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords benchmark, they, evaluate, six, widely, adopted in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_just_importantly_all_flab_released`

- Preferred role: `content`
- Cue keywords: `just, importantly, all, flab, released, openly, community, keep, expanding`
- Narration: Just as importantly, all of the FLAb data are released openly so the community can keep expanding it.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_just_importantly_all_flab_released" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords just, importantly, all, flab, released, openly in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_core_idea_simple_every_antibody`

- Preferred role: `method`
- Cue keywords: `core, idea, simple, every, antibody, sequence, its, structure, fed, reports`
- Narration: The core idea is simple. Every antibody sequence, or its structure, is fed to a model, and the model reports a perplexity score averaged over all residues in the heavy and light chains.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_core_idea_simple_every_antibody" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, idea, simple, every, antibody, sequence in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_perplexity_measures_how_surprised_se`

- Preferred role: `content`
- Cue keywords: `perplexity, measures, how, surprised, sequence, well-behaved, should, confident, meaning, low`
- Narration: Perplexity measures how surprised the model is by the sequence, so a well-behaved model should be confident, meaning low perplexity, about high-fitness antibodies.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_perplexity_measures_how_surprised_se" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords perplexity, measures, how, surprised, sequence, well-behaved in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_authors_correlate_these_scores_again`

- Preferred role: `method`
- Cue keywords: `authors, correlate, these, scores, against, real, experimental, fitness, three, coefficients`
- Narration: The authors then correlate these scores against real experimental fitness using three coefficients: Pearson for linear trends, Spearman for monotonic trends, and Kendall tau for ordinal agreement.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_authors_correlate_these_scores_again" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, correlate, these, scores, against, real in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_crucially_models_used_exactly_releas`

- Preferred role: `method`
- Cue keywords: `crucially, models, used, exactly, released, additional, fine-tuning, across, decoder-only, encoder-only`
- Narration: Crucially, the models are used exactly as released, with no additional fine-tuning, across decoder-only, encoder-only, and inverse-folding architectures.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_crucially_models_used_exactly_releas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, models, used, exactly, released, additional in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_flab_pulls_together_seventeen_mutati`

- Preferred role: `content`
- Cue keywords: `flab, pulls, together, seventeen, mutational, landscapes, distinct, antibody, families, drawn`
- Narration: FLAb pulls together seventeen mutational landscapes from distinct antibody families, drawn from eight separate studies, adding up to more than thirteen thousand fitness measurements.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_flab_pulls_together_seventeen_mutati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords flab, pulls, together, seventeen, mutational, landscapes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_together_they_cover_six_developabili`

- Preferred role: `content`
- Cue keywords: `together, they, cover, six, developability, properties, define, therapeutic, antibody, expression`
- Narration: Together they cover the six developability properties that define a therapeutic antibody: expression, thermostability, immunogenicity, aggregation, polyreactivity, and binding affinity.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_together_they_cover_six_developabili" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, they, cover, six, developability, properties in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_property_grounded_its_own_real`

- Preferred role: `content`
- Cue keywords: `property, grounded, its, own, real, experimental, unit, micrograms, per, milliliter`
- Narration: Each property is grounded in its own real experimental unit, from micrograms per milliliter for expression to melting temperature for stability and dissociation constants for binding.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_property_grounded_its_own_real" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords property, grounded, its, own, real, experimental in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_diversity_what_lets_flab_test`

- Preferred role: `guidance`
- Cue keywords: `diversity, what, lets, flab, test, whether, generalizes, across, many, facets`
- Narration: This diversity is what lets FLAb test whether a model generalizes across the many facets of antibody fitness.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s06_c4_diversity_what_lets_flab_test" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords diversity, what, lets, flab, test, whether in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_reality_check`

- Preferred role: `result`
- Cue keywords: `headline, result, reality, check`
- Narration: The headline result is a reality check.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_headline_result_reality_check" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, reality, check in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_correlates_well_all_six_properties`

- Preferred role: `content`
- Cue keywords: `correlates, well, all, six, properties, even, single, property, performance, swings`
- Narration: No model correlates well with all six properties, and even for a single property, performance swings widely from one dataset to another.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_correlates_well_all_six_properties" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords correlates, well, all, six, properties, even in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_progen2_small_most_frequent_winner_c`

- Preferred role: `result`
- Cue keywords: `progen2-small, most, frequent, winner, coming, out, top, seven, datasets, while`
- Narration: ProGen2-Small was the most frequent winner, coming out on top for seven datasets, while ProGen2-Medium, ProGen2-OAS, ESM-IF, and Rosetta energy tied just behind at six each.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_progen2_small_most_frequent_winner_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords progen2-small, most, frequent, winner, coming, out in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_notably_sequence_based_models_averag`

- Preferred role: `method`
- Cue keywords: `notably, sequence-based, models, average, beat, structure-based, ones, across, every, landscape`
- Narration: Notably, sequence-based models on average beat structure-based ones across every landscape, with the biggest gap on thermostability, suggesting that raw sequence signal still carries most of the predictive power here.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_notably_sequence_based_models_averag" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords notably, sequence-based, models, average, beat, structure-based in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_digging_what_drives_performance_auth`

- Preferred role: `method`
- Cue keywords: `digging, what, drives, performance, authors, find, parameter, count, matters, more`
- Narration: Digging into what drives performance, the authors find that parameter count matters more than architecture or training data. Encoder-only AntiBERTy and decoder-only IgLM, both trained on the same five hundred fifty eight million antibody sequences, behave almost identically.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_digging_what_drives_performance_auth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords digging, what, drives, performance, authors, find in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_scaling_progen2_one_hundred_fifty`

- Preferred role: `figure`
- Cue keywords: `scaling, progen2, one, hundred, fifty, million, over, six, billion, parameters`
- Narration: Scaling ProGen2 from one hundred fifty million up to over six billion parameters helped only two properties, polyreactivity and thermostability.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c2_scaling_progen2_one_hundred_fifty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords scaling, progen2, one, hundred, fifty, million in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_they_also_uncover_evolutionary_bias`

- Preferred role: `figure`
- Cue keywords: `they, also, uncover, evolutionary, bias, several, language, models, rank, wild-type`
- Narration: They also uncover an evolutionary bias: several language models rank the wild-type golimumab antibody as fitter than mutants that are actually more thermostable, while physics-based Rosetta gets the ranking right.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c3_they_also_uncover_evolutionary_bias" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, also, uncover, evolutionary, bias, several in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_reminder_evolutionary_likelihood_phy`

- Preferred role: `figure`
- Cue keywords: `reminder, evolutionary, likelihood, physical, fitness, not, same, thing`
- Narration: It's a reminder that evolutionary likelihood and physical fitness are not the same thing.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c4_reminder_evolutionary_likelihood_phy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reminder, evolutionary, likelihood, physical, fitness, not in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_scope_findings`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, scope, findings`
- Narration: A few numbers capture the scope and the findings.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_scope_findings" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, scope, findings in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_flab_spans_thirteen_thousand_three`

- Preferred role: `result`
- Cue keywords: `flab, spans, thirteen, thousand, three, hundred, eighty, four, fitness, measurements`
- Narration: FLAb spans thirteen thousand three hundred eighty four fitness measurements across seventeen mutational landscapes and six developability properties, testing six deep learning models against Rosetta.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_flab_spans_thirteen_thousand_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords flab, spans, thirteen, thousand, three, hundred in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_intrinsic_properties_ones_driven_ant`

- Preferred role: `result`
- Cue keywords: `intrinsic, properties, ones, driven, antibody, itself, reach, average, absolute, correlation`
- Narration: Intrinsic properties, the ones driven by the antibody itself, reach an average absolute correlation above zero point six, while extrinsic properties lag well behind, with binding under zero point four, expression under zero point four two, and immunogenicity under zero point five.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_intrinsic_properties_ones_driven_ant" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords intrinsic, properties, ones, driven, antibody, itself in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_models_far_better_telling_apart`

- Preferred role: `content`
- Cue keywords: `models, far, better, telling, apart, mutants, within, one, family, zero`
- Narration: And models are far better at telling apart mutants within one family, at zero point seven seven, than across different families, at just zero point one two.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_models_far_better_telling_apart" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords models, far, better, telling, apart, mutants in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_honest_useful_current_deep`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, honest, useful, current, deep, learning, reliably, predicts, antibody, fitness`
- Narration: The takeaway is honest and useful: no current deep learning model reliably predicts antibody fitness across all developability properties, so we are not yet at the point of trusting these models to filter therapeutic candidates on their own.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_honest_useful_current_deep" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, honest, useful, current, deep, learning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_good_news_intrinsic_properties_alrea`

- Preferred role: `content`
- Cue keywords: `good, news, intrinsic, properties, already, captured, reasonably, well, which, points`
- Narration: The good news is that intrinsic properties are already captured reasonably well, which points toward the hardest remaining challenges.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_good_news_intrinsic_properties_alrea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords good, news, intrinsic, properties, already, captured in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_authors_argue_most_promising_path`

- Preferred role: `method`
- Cue keywords: `authors, argue, most, promising, path, forward, enrich, these, models, structural`
- Narration: The authors argue the most promising path forward is to enrich these models with structural information, antigen context, and physics-based priors, and to keep growing open antibody fitness datasets like FLAb.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_authors_argue_most_promising_path" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, argue, most, promising, path, forward in title/desc so the matcher can verify semantic overlap.
