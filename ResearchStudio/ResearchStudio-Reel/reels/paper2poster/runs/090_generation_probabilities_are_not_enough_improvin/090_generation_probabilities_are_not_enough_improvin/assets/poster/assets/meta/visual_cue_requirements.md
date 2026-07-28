# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_code_assistants_like_copilot_suggest`

- Preferred role: `qr`
- Cue keywords: `code, assistants, like, copilot, suggest, completions, but, they, make, mistakes`
- Narration: AI code assistants like Copilot suggest completions, but they make mistakes, and programmers have to catch those mistakes before they turn into bugs.
- Authoring: Create or label one visible qr region for this narration chunk. Use id="cue_s01_c1_code_assistants_like_copilot_suggest" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords code, assistants, like, copilot, suggest, completions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_one_popular_idea_highlight_tokens`

- Preferred role: `title`
- Cue keywords: `one, popular, idea, highlight, tokens, least, confident, about, person, knows`
- Narration: One popular idea is to highlight the tokens the model was least confident about, so a person knows where to look. This paper asks a sharp question: are those generation probabilities actually the right thing to highlight?
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c2_one_popular_idea_highlight_tokens" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, popular, idea, highlight, tokens, least in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_through_preregistered_study_thirty_p`

- Preferred role: `result`
- Cue keywords: `through, preregistered, study, thirty, programmers, authors, compare, highlighting, low-probability, tokens`
- Narration: Through a preregistered study with thirty programmers, the authors compare highlighting low-probability tokens against a new edit model that instead predicts which tokens a person is likely to change.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c3_through_preregistered_study_thirty_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords through, preregistered, study, thirty, programmers, authors in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_edit_wins_speed_precision_edits`

- Preferred role: `content`
- Cue keywords: `edit, wins, speed, precision, edits, user, preference, showing, generation, probabilities`
- Narration: The edit model wins on speed, precision of edits, and user preference, showing that generation probabilities alone are not enough.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_edit_wins_speed_precision_edits" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords edit, wins, speed, precision, edits, user in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_code_assistants_now_everywhere_but`

- Preferred role: `qr`
- Cue keywords: `code, assistants, now, everywhere, but, they, imperfect, wrong, suggestion, quietly`
- Narration: AI code assistants are now everywhere, but they are imperfect, and a wrong suggestion can quietly plant a bug or a security hole.
- Authoring: Create or label one visible qr region for this narration chunk. Use id="cue_s02_c1_code_assistants_now_everywhere_but" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords code, assistants, now, everywhere, but, they in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_catch_those_mistakes_programmer_firs`

- Preferred role: `content`
- Cue keywords: `catch, those, mistakes, programmer, first, notice, them, hard, because, people`
- Narration: To catch those mistakes, a programmer first has to notice them, and that is hard, because people tend to over-trust automation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_catch_those_mistakes_programmer_firs" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords catch, those, mistakes, programmer, first, notice in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_tricky_part_single_code_suggestion`

- Preferred role: `qr`
- Cue keywords: `tricky, part, single, code, suggestion, not, one, decision, but, hundreds`
- Narration: The tricky part is that a single code suggestion is not one decision but hundreds of tiny ones, one per token.
- Authoring: Create or label one visible qr region for this narration chunk. Use id="cue_s02_c3_tricky_part_single_code_suggestion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tricky, part, single, code, suggestion, not in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_earlier_research_communicating_uncer`

- Preferred role: `content`
- Cue keywords: `earlier, research, communicating, uncertainty, built, single-shot, decisions, like, diagnosis, does`
- Narration: Earlier research on communicating AI uncertainty was built for single-shot decisions like a diagnosis, and it does not obviously carry over to this token-by-token world.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_earlier_research_communicating_uncer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords earlier, research, communicating, uncertainty, built, single-shot in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_one_natural_idea_highlight_uncertain`

- Preferred role: `content`
- Cue keywords: `one, natural, idea, highlight, uncertain, tokens, much, like, spell-checker, underlines`
- Narration: One natural idea is to highlight uncertain tokens, much like a spell-checker underlines suspect words, so the programmer's eye is drawn to the spots that most need review.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_one_natural_idea_highlight_uncertain" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, natural, idea, highlight, uncertain, tokens in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_obvious_signal_own_generation_probab`

- Preferred role: `content`
- Cue keywords: `obvious, signal, own, generation, probability, tokens, least, sure, about, get`
- Narration: The obvious signal to use is the model's own generation probability: tokens the model was least sure about get highlighted.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_obvious_signal_own_generation_probab" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords obvious, signal, own, generation, probability, tokens in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_existing_strategy_even_ships_openai`

- Preferred role: `method`
- Cue keywords: `existing, strategy, even, ships, openai, playground`
- Narration: This is an existing strategy, and it even ships in OpenAI's Playground.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_existing_strategy_even_ships_openai" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, strategy, even, ships, openai, playground in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_but_nobody_had_really_tested`

- Preferred role: `content`
- Cue keywords: `but, nobody, had, really, tested, whether, low, probability, actually, lines`
- Narration: But nobody had really tested whether low probability actually lines up with where humans need to make edits, and that gap is exactly what this paper set out to probe.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_but_nobody_had_really_tested" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, nobody, had, really, tested, whether in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_authors_ran_preregistered_mixed_meth`

- Preferred role: `method`
- Cue keywords: `authors, ran, preregistered, mixed-methods, study, thirty, programmers, comparing, three, ways`
- Narration: The authors ran a preregistered, mixed-methods study with thirty programmers, comparing three ways of presenting the same AI code completions: no highlights at all, highlights based on generation probability, and highlights based on a new edit model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_authors_ran_preregistered_mixed_meth" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ran, preregistered, mixed-methods, study, thirty in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_edit_key_idea_instead_asking`

- Preferred role: `content`
- Cue keywords: `edit, key, idea, instead, asking, how, confident, predicts, which, tokens`
- Narration: The edit model is the key idea: instead of asking how confident the model was, it predicts which tokens a human is actually likely to change.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_edit_key_idea_instead_asking" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords edit, key, idea, instead, asking, how in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_reframes_whole_problem_surfacing_unc`

- Preferred role: `content`
- Cue keywords: `reframes, whole, problem, surfacing, uncertainty, surfacing, human, intervention, authors, argue`
- Narration: This reframes the whole problem, from surfacing model uncertainty to surfacing human intervention, and the authors argue the same recipe could scale up by learning from edit telemetry that products already collect.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_reframes_whole_problem_surfacing_unc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reframes, whole, problem, surfacing, uncertainty, surfacing in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_under_hood_all_three_tools`

- Preferred role: `content`
- Cue keywords: `under, hood, all, three, tools, used, very, same, codex, any`
- Narration: Under the hood, all three tools used the very same Codex model, so any difference in behavior comes purely from how the completion was displayed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_under_hood_all_three_tools" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords under, hood, all, three, tools, used in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_generation_probability_tool_highligh`

- Preferred role: `content`
- Cue keywords: `generation-probability, tool, highlighted, tokens, least, confident, seventy-one, percent, threshold`
- Narration: The generation-probability tool highlighted tokens the model was least confident in, at a seventy-one percent threshold.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_generation_probability_tool_highligh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords generation-probability, tool, highlighted, tokens, least, confident in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_edit_model_tool_highlighted_tokens_m`

- Preferred role: `method`
- Cue keywords: `edit-model, tool, highlighted, tokens, most, likely, edited, sixty-six, percent, threshold`
- Narration: The edit-model tool highlighted tokens most likely to be edited, at a sixty-six percent threshold, using a model trained on nine coders who had previously edited Codex output until their tasks passed.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_edit_model_tool_highlighted_tokens_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords edit-model, tool, highlighted, tokens, most, likely in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_crucially_thresholds_chosen_every_co`

- Preferred role: `content`
- Cue keywords: `crucially, thresholds, chosen, every, condition, showed, same, total, number, highlights`
- Narration: Crucially, the thresholds were chosen so that every condition showed the same total number of highlights, so the comparison is about which tokens get highlighted, not how many.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_crucially_thresholds_chosen_every_co" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, thresholds, chosen, every, condition, showed in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_thirty_participants_took_part_all`

- Preferred role: `content`
- Cue keywords: `thirty, participants, took, part, all, experienced, python, programmers, large, technology`
- Narration: Thirty participants took part, all experienced Python programmers at a large US technology company, each paid fifty dollars for roughly an hour of their time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_thirty_participants_took_part_all" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords thirty, participants, took, part, all, experienced in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_every_person_solved_three_coding`

- Preferred role: `qr`
- Cue keywords: `every, person, solved, three, coding, problems, drawn, leetcode, easy, tier`
- Narration: Every person solved three coding problems drawn from LeetCode's easy tier, with a ten-minute cap per task, and could run their code and a set of provided unit tests to debug along the way.
- Authoring: Create or label one visible qr region for this narration chunk. Use id="cue_s06_c2_every_person_solved_three_coding" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, person, solved, three, coding, problems in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_task_order_which_tool_went`

- Preferred role: `result`
- Cue keywords: `task, order, which, tool, went, which, task, randomized, keep, comparison`
- Narration: Task order and which tool went with which task were randomized to keep the comparison fair.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_task_order_which_tool_went" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords task, order, which, tool, went, which in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_edit_itself_trained_earlier_separate`

- Preferred role: `method`
- Cue keywords: `edit, itself, trained, earlier, separate, group, nine, coders`
- Narration: The edit model itself was trained earlier, on a separate group of nine coders.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_edit_itself_trained_earlier_separate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords edit, itself, trained, earlier, separate, group in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_about_speed`

- Preferred role: `result`
- Cue keywords: `headline, result, about, speed`
- Narration: The headline result is about speed.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_headline_result_about_speed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, about, speed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_people_finished_fastest_when_edit_mo`

- Preferred role: `result`
- Cue keywords: `people, finished, fastest, when, edit-model, highlights, about, eight, point, six`
- Narration: People finished fastest when using edit-model highlights, at about eight point six minutes on average, and slowest with generation-probability highlights, at about nine point six minutes, with the no-highlight condition sitting in between.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_people_finished_fastest_when_edit_mo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords people, finished, fastest, when, edit-model, highlights in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_gap_between_two_highlighting_strateg`

- Preferred role: `method`
- Cue keywords: `gap, between, two, highlighting, strategies, highly, significant, p-value, zero, point`
- Narration: The gap between the two highlighting strategies is highly significant, with a p-value of zero point zero zero three.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_gap_between_two_highlighting_strateg" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gap, between, two, highlighting, strategies, highly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_what_makes_striking_generation_proba`

- Preferred role: `method`
- Cue keywords: `what, makes, striking, generation-probability, highlighting, actually, worst, three, slower, even`
- Narration: What makes this striking is that generation-probability highlighting was actually the worst of the three, slower even than showing no highlights at all, so highlighting the wrong tokens can hurt rather than help.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_what_makes_striking_generation_proba" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, makes, striking, generation-probability, highlighting, actually in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_understand_why_authors_tracked_which`

- Preferred role: `content`
- Cue keywords: `understand, why, authors, tracked, which, tokens, survived, meaning, they, left`
- Narration: To understand why, the authors tracked which tokens survived, meaning they were left unchanged by the participant.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_understand_why_authors_tracked_which" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords understand, why, authors, tracked, which, tokens in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_under_edit_tokens_left_un_highlighte`

- Preferred role: `content`
- Cue keywords: `under, edit, tokens, left, un-highlighted, survived, far, more, often, about`
- Narration: Under the edit model, tokens it left un-highlighted survived far more often, about eighty-seven percent of the time, while tokens it did highlight survived only about thirty-five percent of the time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_under_edit_tokens_left_un_highlighte" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords under, edit, tokens, left, un-highlighted, survived in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_compare_generation_probability_highl`

- Preferred role: `content`
- Cue keywords: `compare, generation-probability, highlighting, where, highlighted, tokens, still, survived, seventy-four, percent`
- Narration: Compare that to generation-probability highlighting, where highlighted tokens still survived seventy-four percent of the time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_compare_generation_probability_highl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords compare, generation-probability, highlighting, where, highlighted, tokens in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_other_words_edit_highlights_closely`

- Preferred role: `content`
- Cue keywords: `other, words, edit, highlights, closely, predict, what, people, actually, change`
- Narration: In other words, the edit model's highlights closely predict what people actually change, while generation-probability highlights barely move the needle, and all of these differences are extremely significant.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_other_words_edit_highlights_closely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords other, words, edit, highlights, closely, predict in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_put_numbers_task_time_dropped`

- Preferred role: `content`
- Cue keywords: `put, numbers, task, time, dropped, nine, point, six, one, minutes`
- Narration: To put numbers on it: task time dropped from nine point six one minutes with generation-probability highlighting to eight point five nine minutes with the edit model, a significant difference at p equals zero point zero zero three.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_put_numbers_task_time_dropped" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords put, numbers, task, time, dropped, nine in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_highlighted_token_survival_fell_seve`

- Preferred role: `content`
- Cue keywords: `highlighted-token, survival, fell, seventy-four, percent, thirty-five, percent, showing, far, tighter`
- Narration: Highlighted-token survival fell from seventy-four percent to thirty-five percent, showing far tighter alignment with real edits, at p below zero point zero zero zero one.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_highlighted_token_survival_fell_seve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords highlighted-token, survival, fell, seventy-four, percent, thirty-five in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_seven_point_preference_scale_users_r`

- Preferred role: `content`
- Cue keywords: `seven-point, preference, scale, users, rated, edit, highlights, three, point, nine`
- Narration: And on a seven-point preference scale, users rated the edit highlights three point nine four versus two point eight eight for generation probability, significant at p equals zero point zero zero one.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_seven_point_preference_scale_users_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords seven-point, preference, scale, users, rated, edit in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lesson_simple_but_pointed`

- Preferred role: `content`
- Cue keywords: `lesson, simple, but, pointed`
- Narration: The lesson is simple but pointed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lesson_simple_but_pointed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lesson, simple, but, pointed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_what_you_highlight_matters_more`

- Preferred role: `content`
- Cue keywords: `what, you, highlight, matters, more, whether, you, highlight, right, thing`
- Narration: What you highlight matters more than whether you highlight, and the right thing to highlight is where people are likely to edit, not where the model happened to be unsure.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_what_you_highlight_matters_more" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, you, highlight, matters, more, whether in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_generation_probabilities_alone_not_e`

- Preferred role: `content`
- Cue keywords: `generation, probabilities, alone, not, enough`
- Narration: Generation probabilities alone are not enough.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_generation_probabilities_alone_not_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords generation, probabilities, alone, not, enough in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_encouragingly_tools_like_copilot_alr`

- Preferred role: `result`
- Cue keywords: `encouragingly, tools, like, copilot, already, log, edits, people, make, suggestions`
- Narration: Encouragingly, tools like Copilot already log the edits people make to AI suggestions, so that same signal could train an open-world edit model and carry these speed, precision, and preference gains into everyday coding.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c4_encouragingly_tools_like_copilot_alr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords encouragingly, tools, like, copilot, already, log in title/desc so the matcher can verify semantic overlap.
