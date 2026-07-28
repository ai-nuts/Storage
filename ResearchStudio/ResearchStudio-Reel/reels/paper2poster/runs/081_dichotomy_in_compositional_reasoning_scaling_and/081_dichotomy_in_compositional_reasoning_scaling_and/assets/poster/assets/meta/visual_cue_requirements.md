# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_large_language_models_combine_skills`

- Preferred role: `content`
- Cue keywords: `large, language, models, combine, skills, they, already, know`
- Narration: Can large language models combine skills they already know?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_large_language_models_combine_skills" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, language, models, combine, skills, they in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_colm_2024_tests_whether_models`

- Preferred role: `title`
- Cue keywords: `colm, 2024, tests, whether, models, solve, unseen, composite, task, fusing`
- Narration: This COLM 2024 paper tests whether models solve an unseen composite task by fusing two simple tasks seen separately.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c2_colm_2024_tests_whether_models" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords colm, 2024, tests, whether, models, solve in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_across_llama_gpt_sharp_dichotomy`

- Preferred role: `content`
- Cue keywords: `across, llama, gpt, sharp, dichotomy, emerges`
- Narration: Across Llama and GPT, a sharp dichotomy emerges.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_across_llama_gpt_sharp_dichotomy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, llama, gpt, sharp, dichotomy, emerges in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_suppose_learned_two_simple_tasks`

- Preferred role: `title`
- Cue keywords: `suppose, learned, two, simple, tasks, in-context, capitalizing, certain, words, swapping`
- Narration: Suppose a model learned two simple tasks in-context, capitalizing certain words and swapping others.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c1_suppose_learned_two_simple_tasks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords suppose, learned, two, simple, tasks, in-context in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_given_input_needing_both_combine`

- Preferred role: `content`
- Cue keywords: `given, input, needing, both, combine, skills`
- Narration: Given an input needing both, can it combine the skills?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_given_input_needing_both_combine" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords given, input, needing, both, combine, skills in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_humans_trivial_yet_even_gpt_4`

- Preferred role: `content`
- Cue keywords: `humans, trivial, yet, even, gpt-4, claude, 3, often, fail`
- Narration: For humans this is trivial, yet even GPT-4 and Claude 3 often fail.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_humans_trivial_yet_even_gpt_4" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords humans, trivial, yet, even, gpt-4, claude in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_models_increasingly_asked_chain_skil`

- Preferred role: `content`
- Cue keywords: `models, increasingly, asked, chain, skills, real, reasoning, yet, lack, clear`
- Narration: Models are increasingly asked to chain skills for real reasoning, yet we lack a clear account of when chaining works.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_models_increasingly_asked_chain_skil" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords models, increasingly, asked, chain, skills, real in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_prior_studies_narrow_little_theory`

- Preferred role: `content`
- Cue keywords: `prior, studies, narrow, little, theory, failure, reproduces, easily, frontier, models`
- Narration: Prior studies are narrow with little theory, and the failure reproduces easily on frontier models.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_prior_studies_narrow_little_theory" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, studies, narrow, little, theory, failure in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_three_contributions_test_suite_lingu`

- Preferred role: `method`
- Cue keywords: `three, contributions, test, suite, linguistic, logical, composite, tasks, simple-task, examples`
- Narration: Three contributions: a test suite of linguistic and logical composite tasks with simple-task examples only; evaluation across Llama and GPT scales revealing a clear dichotomy; and a linear self-attention theory explaining when composition emerges.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_three_contributions_test_suite_lingu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords three, contributions, test, suite, linguistic, logical in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_two_halves`

- Preferred role: `content`
- Cue keywords: `two, halves`
- Narration: Two halves.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_two_halves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, halves in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_empirically_composite_task_tested_fo`

- Preferred role: `content`
- Cue keywords: `empirically, composite, task, tested, four, settings, ten, in-context, examples, simple`
- Narration: Empirically, each composite task is tested in four settings with ten in-context examples: each simple task alone, a composite test with simple-task demos, and an all-composite gold standard.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_empirically_composite_task_tested_fo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords empirically, composite, task, tested, four, settings in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_theoretically_linear_self_attention`

- Preferred role: `method`
- Cue keywords: `theoretically, linear, self-attention, shows, composition, succeeds, under, confined, support`
- Narration: Theoretically, a linear self-attention model shows composition succeeds under confined support.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_theoretically_linear_self_attention" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords theoretically, linear, self-attention, shows, composition, succeeds in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_suite_pairs_simple_building_blocks`

- Preferred role: `figure`
- Cue keywords: `suite, pairs, simple, building, blocks`
- Narration: The suite pairs simple building blocks.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c1_suite_pairs_simple_building_blocks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords suite, pairs, simple, building, blocks in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_linguistic_tasks_include_capitalizat`

- Preferred role: `title`
- Cue keywords: `linguistic, tasks, include, capitalization, swapping, translations, like, phrase, recombination, passive-to-active`
- Narration: Linguistic tasks include capitalization, swapping, and translations like phrase recombination and passive-to-active.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c2_linguistic_tasks_include_capitalizat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords linguistic, tasks, include, capitalization, swapping, translations in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_logical_tasks_combine_arithmetic_wor`

- Preferred role: `title`
- Cue keywords: `logical, tasks, combine, arithmetic, word, operations`
- Narration: Logical tasks combine arithmetic with word operations.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c3_logical_tasks_combine_arithmetic_wor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords logical, tasks, combine, arithmetic, word, operations in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_tasks_split_separable_composites_act`

- Preferred role: `title`
- Cue keywords: `tasks, split, separable, composites, acting, different, input, parts, compose-by-step, composites`
- Narration: Tasks split into separable composites, acting on different input parts, and compose-by-step composites requiring chained reasoning.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s06_c4_tasks_split_separable_composites_act" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tasks, split, separable, composites, acting, different in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_sharp_split`

- Preferred role: `content`
- Cue keywords: `sharp, split`
- Narration: A sharp split.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_sharp_split" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sharp, split in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_separable_composite_tasks_models_com`

- Preferred role: `title`
- Cue keywords: `separable, composite, tasks, models, compose, well, improve, scale, approaching, gold`
- Narration: On separable composite tasks, models compose well and improve with scale, approaching the gold standard.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s07_c2_separable_composite_tasks_models_com" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separable, composite, tasks, models, compose, well in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_compose_by_step_tasks_they_collapse`

- Preferred role: `figure`
- Cue keywords: `compose-by-step, tasks, they, collapse, llama, solves, simple, task, near, ninety`
- Narration: On compose-by-step tasks they collapse: Llama solves each simple task near ninety percent, but the composite drops below twenty percent, and scaling doesn't help.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s07_c3_compose_by_step_tasks_they_collapse" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords compose-by-step, tasks, they, collapse, llama, solves in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_scale_sweep_key_ablation`

- Preferred role: `content`
- Cue keywords: `scale, sweep, key, ablation`
- Narration: The scale sweep is the key ablation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_scale_sweep_key_ablation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords scale, sweep, key, ablation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_separable_tasks_accuracy_rises_scale`

- Preferred role: `result`
- Cue keywords: `separable, tasks, accuracy, rises, scale, compose-by-step, tasks, stays, flat, degrades`
- Narration: On separable tasks accuracy rises with scale; on compose-by-step tasks it stays flat or degrades.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_separable_tasks_accuracy_rises_scale" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separable, tasks, accuracy, rises, scale, compose-by-step in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_swapping_simple_task_demos_composite`

- Preferred role: `method`
- Cue keywords: `swapping, simple-task, demos, composite, ones, recovers, performance, isolating, composition, not`
- Narration: Swapping simple-task demos for composite ones recovers performance, isolating composition, not capability, as the bottleneck.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_swapping_simple_task_demos_composite" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords swapping, simple-task, demos, composite, ones, recovers in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_tell`

- Preferred role: `content`
- Cue keywords: `numbers, tell`
- Narration: The numbers tell it.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_numbers_tell" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, tell in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_simple_capitalization_swap_reach_abo`

- Preferred role: `content`
- Cue keywords: `simple, capitalization, swap, reach, about, ninety, percent, llama`
- Narration: Simple capitalization and swap reach about ninety percent for Llama.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_simple_capitalization_swap_reach_abo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords simple, capitalization, swap, reach, about, ninety in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_compose_by_step_version_falls_twenty`

- Preferred role: `result`
- Cue keywords: `compose-by-step, version, falls, twenty, percent, lower, gain, scaling`
- Narration: The compose-by-step version falls to twenty percent or lower, with no gain from scaling.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_compose_by_step_version_falls_twenty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords compose-by-step, version, falls, twenty, percent, lower in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_milder_separable_cases_climb_forty_f`

- Preferred role: `content`
- Cue keywords: `milder, separable, cases, climb, forty-four, sixty-six, percent`
- Narration: Milder separable cases climb to forty-four and sixty-six percent.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_milder_separable_cases_climb_forty_f" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords milder, separable, cases, climb, forty-four, sixty-six in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_models_combine_two_skills`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, models, combine, two, skills, only, when, they, act, separate`
- Narration: The takeaway: models combine two skills only when they act on separate parts of the input.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_models_combine_two_skills" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, models, combine, two, skills, only in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_when_task_needs_genuinely_chained`

- Preferred role: `content`
- Cue keywords: `when, task, needs, genuinely, chained, multi-step, reasoning, they, fail, more`
- Narration: When a task needs genuinely chained, multi-step reasoning, they fail, and more parameters won't help.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_when_task_needs_genuinely_chained" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, task, needs, genuinely, chained, multi-step in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_task_structure_predicts_whether_scal`

- Preferred role: `method`
- Cue keywords: `task, structure, predicts, whether, scaling, helps`
- Narration: Task structure predicts whether scaling helps.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_task_structure_predicts_whether_scal" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords task, structure, predicts, whether, scaling, helps in title/desc so the matcher can verify semantic overlap.
