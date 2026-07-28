# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_present_ds_1000_natural_reliable_ben`

- Preferred role: `result`
- Cue keywords: `present, ds-1000, natural, reliable, benchmark, science, code, generation`
- Narration: We present DS-1000, a natural and reliable benchmark for data science code generation.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c1_present_ds_1000_natural_reliable_ben" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords present, ds-1000, natural, reliable, benchmark, science in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_ds_1000_gathers_thousand_real_proble`

- Preferred role: `content`
- Cue keywords: `ds-1000, gathers, thousand, real, problems, across, seven, widely, used, python`
- Narration: DS-1000 gathers a thousand real problems across seven widely used Python libraries such as NumPy and Pandas, all drawn from StackOverflow.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_ds_1000_gathers_thousand_real_proble" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ds-1000, gathers, thousand, real, problems, across in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_pairs_these_realistic_problems_relia`

- Preferred role: `result`
- Cue keywords: `pairs, these, realistic, problems, reliable, execution-based, evaluation, built-in, defense, against`
- Narration: It pairs these realistic problems with reliable execution-based evaluation and a built-in defense against memorization, giving the community a trustworthy yardstick for data science coding models.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c3_pairs_these_realistic_problems_relia" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pairs, these, realistic, problems, reliable, execution-based in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_science_coding_central_many_fields`

- Preferred role: `content`
- Cue keywords: `science, coding, central, many, fields, yet, demands, fluency, specialized, libraries`
- Narration: Data science coding is central to many fields, yet it demands fluency in specialized libraries that create real barriers for everyday users.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_science_coding_central_many_fields" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords science, coding, central, many, fields, yet in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_code_generation_models_could_lower`

- Preferred role: `result`
- Cue keywords: `code, generation, models, could, lower, those, barriers, but, community, lacked`
- Narration: Code generation models could lower those barriers, but the community lacked a benchmark to measure real progress.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c2_code_generation_models_could_lower" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords code, generation, models, could, lower, those in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_most_existing_datasets_focus_competi`

- Preferred role: `method`
- Cue keywords: `most, existing, datasets, focus, competitive, interview-style, problems, test, algorithms, rather`
- Narration: Most existing datasets focus on competitive or interview-style problems that test algorithms rather than real-world usage, and many score answers with surface-form metrics like BLEU that drift away from what programmers actually intend.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_most_existing_datasets_focus_competi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, existing, datasets, focus, competitive, interview-style in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_benchmark_combining_natural_richly_c`

- Preferred role: `result`
- Cue keywords: `benchmark, combining, natural, richly, contextual, problems, reliable, execution-based, way, judge`
- Narration: There was no benchmark combining natural, richly contextual problems with a reliable, execution-based way to judge correctness.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c4_benchmark_combining_natural_richly_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords benchmark, combining, natural, richly, contextual, problems in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_real_science_questions_rarely_look`

- Preferred role: `title`
- Cue keywords: `real, science, questions, rarely, look, like, clean, textbook, prompts`
- Narration: Real data science questions rarely look like clean textbook prompts.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c1_real_science_questions_rarely_look" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords real, science, questions, rarely, look, like in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_stackoverflow_users_describe_messy_c`

- Preferred role: `result`
- Cue keywords: `stackoverflow, users, describe, messy, contexts, their, broken, code, error, they`
- Narration: On StackOverflow, users describe messy contexts: their broken code, the error they hit, and concrete input-output examples of what they want.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_stackoverflow_users_describe_messy_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stackoverflow, users, describe, messy, contexts, their in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_prior_benchmarks_strip_richness_away`

- Preferred role: `method`
- Cue keywords: `prior, benchmarks, strip, richness, away, same, time, models, get, better`
- Narration: Prior benchmarks strip that richness away. At the same time, as models get better, surface-form scores like BLEU become misleading, rewarding text that looks right but does not run.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_prior_benchmarks_strip_richness_away" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, benchmarks, strip, richness, away, same in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_motivates_benchmark_built_natural_pr`

- Preferred role: `result`
- Cue keywords: `motivates, benchmark, built, natural, problems, judged, actually, executing, code`
- Narration: This motivates a benchmark built from natural problems and judged by actually executing the code.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c4_motivates_benchmark_built_natural_pr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords motivates, benchmark, built, natural, problems, judged in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_ds_1000_makes_three_contributions_fi`

- Preferred role: `title`
- Cue keywords: `ds-1000, makes, three, contributions, first, provides, thousand, realistic, problems, diverse`
- Narration: DS-1000 makes three contributions. First, it provides a thousand realistic problems with diverse contexts, adapted from naturally occurring StackOverflow questions across seven popular Python libraries.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s04_c1_ds_1000_makes_three_contributions_fi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ds-1000, makes, three, contributions, first, provides in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_implements_reliable_multi_cri`

- Preferred role: `method`
- Cue keywords: `second, implements, reliable, multi-criteria, evaluation, runs, test, cases, checks, surface-form`
- Narration: Second, it implements reliable multi-criteria evaluation that runs test cases and checks surface-form constraints, so accepted solutions are almost always genuinely correct.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_second_implements_reliable_multi_cri" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, implements, reliable, multi-criteria, evaluation, runs in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_proactively_defends_against_me`

- Preferred role: `method`
- Cue keywords: `third, proactively, defends, against, memorization, perturbing, problems, models, cannot, simply`
- Narration: Third, it proactively defends against memorization by perturbing problems so models cannot simply recall pre-training answers.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_third_proactively_defends_against_me" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, proactively, defends, against, memorization, perturbing in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_authors_release_benchmark_evaluate_f`

- Preferred role: `result`
- Cue keywords: `authors, release, benchmark, evaluate, five, state-of-the-art, code, models`
- Narration: The authors release the benchmark and use it to evaluate five state-of-the-art code models.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_authors_release_benchmark_evaluate_f" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, release, benchmark, evaluate, five, state-of-the-art in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_ds_1000_built_through_five_stage_pip`

- Preferred role: `method`
- Cue keywords: `ds-1000, built, through, five-stage, pipeline, annotators, first, select, high-vote, testable`
- Narration: DS-1000 is built through a five-stage pipeline. Annotators first select high-vote, testable, useful, and representative StackOverflow problems and rewrite them for clarity. They add a code context with insertion markers showing exactly where the model must fill in code.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_ds_1000_built_through_five_stage_pip" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ds-1000, built, through, five-stage, pipeline, annotators in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_they_implement_automatic_tests_check`

- Preferred role: `method`
- Cue keywords: `they, implement, automatic, tests, check, functional, correctness, executing, test, cases`
- Narration: They then implement automatic tests that check functional correctness by executing test cases and also enforce surface-form constraints, such as forbidding certain APIs or keywords in the syntax tree.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_they_implement_automatic_tests_check" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, implement, automatic, tests, check, functional in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_defend_against_memorization_they_per`

- Preferred role: `result`
- Cue keywords: `defend, against, memorization, they, perturb, original, problem, surface, perturbations, leave`
- Narration: To defend against memorization, they perturb each original problem, using surface perturbations that leave the reference solution unchanged and semantic perturbations that change it, plus deliberately difficult rewrites.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_defend_against_memorization_they_per" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords defend, against, memorization, they, perturb, original in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_finally_they_red_team_evaluation_req`

- Preferred role: `result`
- Cue keywords: `finally, they, red-team, evaluation, requiring, reject, known-wrong, solutions, every, problem`
- Narration: Finally they red-team the evaluation, requiring it to reject known-wrong solutions. Every problem, solution, and metric is reviewed by at least three expert annotators.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c4_finally_they_red_team_evaluation_req" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finally, they, red-team, evaluation, requiring, reject in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_ds_1000_contains_thousand_problems_o`

- Preferred role: `figure`
- Cue keywords: `ds-1000, contains, thousand, problems, originating, four, hundred, fifty-one, unique, stackoverflow`
- Narration: DS-1000 contains a thousand problems originating from four hundred fifty-one unique StackOverflow posts, spanning seven widely used Python libraries: NumPy, Pandas, TensorFlow, PyTorch, SciPy, Scikit-learn, and Matplotlib.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c1_ds_1000_contains_thousand_problems_o" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ds-1000, contains, thousand, problems, originating, four in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_more_half_problems_modified_their`

- Preferred role: `content`
- Cue keywords: `more, half, problems, modified, their, sources, resist, memorization, including, one`
- Narration: More than half of the problems are modified from their sources to resist memorization, including one hundred fifty-two surface perturbations, two hundred thirty-five semantic perturbations, and one hundred sixty-two difficult rewrites.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_more_half_problems_modified_their" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords more, half, problems, modified, their, sources in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_average_problem_one_point_six`

- Preferred role: `method`
- Cue keywords: `average, problem, one, point, six, test, cases, one, hundred, forty`
- Narration: On average each problem has one point six test cases, one hundred forty words, and a reference solution of three point six lines, and about one in five carry surface-form constraints.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_average_problem_one_point_six" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords average, problem, one, point, six, test in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_hundred_forty_average_words_per`

- Preferred role: `result`
- Cue keywords: `hundred, forty, average, words, per, problem, ds-1000, far, richer, context`
- Narration: With a hundred forty average words per problem, DS-1000 is far richer in context than other data science datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c4_hundred_forty_average_words_per" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hundred, forty, average, words, per, problem in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_ds_1000_clearly_separates_models_dif`

- Preferred role: `method`
- Cue keywords: `ds-1000, clearly, separates, models, different, strength, best, public, system, codex-002`
- Narration: DS-1000 clearly separates models of different strength. The best public system, Codex-002 in the insertion format, reaches only forty-three point three percent average accuracy, nontrivial but far from solved, leaving substantial room for improvement.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_ds_1000_clearly_separates_models_dif" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ds-1000, clearly, separates, models, different, strength in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_across_five_models_three_families`

- Preferred role: `result`
- Cue keywords: `across, five, models, three, families, accuracy, ranges, seven, point, four`
- Narration: Across five models from three families, accuracy ranges from seven point four percent up to forty-three point three percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_across_five_models_three_families" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, five, models, three, families, accuracy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_insertion_format_which_supplies_righ`

- Preferred role: `content`
- Cue keywords: `insertion, format, which, supplies, right-hand, context, gives, codex-002, four, point`
- Narration: Insertion format, which supplies right-hand context, gives Codex-002 a four point one percent boost over completion format, underscoring the value of infilling for data science coding.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_insertion_format_which_supplies_righ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords insertion, format, which, supplies, right-hand, context in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_weaker_models_such_codegen_6b_incode`

- Preferred role: `content`
- Cue keywords: `weaker, models, such, codegen-6b, incoder-6b, fall, below, five, percent, some`
- Narration: Weaker models such as CodeGen-6B and InCoder-6B fall below five percent on some libraries.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_weaker_models_such_codegen_6b_incode" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords weaker, models, such, codegen-6b, incoder-6b, fall in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_show_why_memorization_matters_author`

- Preferred role: `content`
- Cue keywords: `show, why, memorization, matters, authors, probe, popular, numpy-100, problem, set`
- Narration: To show why memorization matters, the authors probe the popular numpy-100 problem set.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_show_why_memorization_matters_author" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords show, why, memorization, matters, authors, probe in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_codex_002_scores_seventy_two_point_f`

- Preferred role: `method`
- Cue keywords: `codex-002, scores, seventy-two, point, five, percent, but, accuracy, collapses, forty`
- Narration: Codex-002 scores seventy-two point five percent there, but accuracy collapses to forty point six percent after perturbation, and in thirty-six percent of semantic cases the model still returns the original, now-incorrect answer, evidence that it is recalling memorized solutions rather than reasoning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_codex_002_scores_seventy_two_point_f" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords codex-002, scores, seventy-two, point, five, percent in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_ds_1000_perturbation_drop_much_gentl`

- Preferred role: `content`
- Cue keywords: `ds-1000, perturbation, drop, much, gentler, about, three, nine, percent, because`
- Narration: On DS-1000 the perturbation drop is much gentler, about three to nine percent, because these problems appear less often online.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_ds_1000_perturbation_drop_much_gentl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ds-1000, perturbation, drop, much, gentler, about in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_confirms_perturbation_practical_defe`

- Preferred role: `result`
- Cue keywords: `confirms, perturbation, practical, defense, against, memorization, future, models`
- Narration: This confirms perturbation as a practical defense against memorization by future models.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_confirms_perturbation_practical_defe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords confirms, perturbation, practical, defense, against, memorization in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_ds_1000_offers`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, ds-1000, offers, thousand, problems, over, seven, libraries`
- Narration: A few numbers capture DS-1000. It offers a thousand problems over seven libraries, drawn from four hundred fifty-one unique StackOverflow posts.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_ds_1000_offers" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, ds-1000, offers, thousand in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_best_reaches_only_forty_three_point`

- Preferred role: `result`
- Cue keywords: `best, reaches, only, forty-three, point, three, percent, accuracy`
- Narration: The best model reaches only forty-three point three percent accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_best_reaches_only_forty_three_point" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords best, reaches, only, forty-three, point, three in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_evaluation_highly_reliable_among_all`

- Preferred role: `result`
- Cue keywords: `evaluation, highly, reliable, among, all, solutions, accepts, just, one, point`
- Narration: The evaluation is highly reliable: among all solutions it accepts, just one point eight percent are actually incorrect, and only about half a percent of rejected ones are truly correct.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_evaluation_highly_reliable_among_all" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, highly, reliable, among, all, solutions in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_hundred_forty_words_per_problem`

- Preferred role: `result`
- Cue keywords: `hundred, forty, words, per, problem, average, its, contexts, far, richer`
- Narration: And with a hundred forty words per problem on average, its contexts are far richer than comparable datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_hundred_forty_words_per_problem" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hundred, forty, words, per, problem, average in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_ds_1000_gives_community_science_code`

- Preferred role: `result`
- Cue keywords: `ds-1000, gives, community, science, code, benchmark, realistic, reliably, evaluated, resistant`
- Narration: DS-1000 gives the community a data science code benchmark that is realistic, reliably evaluated, and resistant to memorization.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c1_ds_1000_gives_community_science_code" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ds-1000, gives, community, science, code, benchmark in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_because_built_natural_stackoverflow`

- Preferred role: `method`
- Cue keywords: `because, built, natural, stackoverflow, problems, judged, executing, code, against, test`
- Narration: Because it is built from natural StackOverflow problems, judged by executing code against test cases and surface-form constraints, and defended by deliberate perturbation, its scores are trustworthy and hard to game.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_because_built_natural_stackoverflow" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, built, natural, stackoverflow, problems, judged in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_because_even_strongest_reaches_only`

- Preferred role: `method`
- Cue keywords: `because, even, strongest, reaches, only, forty-three, point, three, percent, makes`
- Narration: And because even the strongest model reaches only forty-three point three percent, it makes clear how much room remains for progress in data science code generation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_because_even_strongest_reaches_only" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, even, strongest, reaches, only, forty-three in title/desc so the matcher can verify semantic overlap.
