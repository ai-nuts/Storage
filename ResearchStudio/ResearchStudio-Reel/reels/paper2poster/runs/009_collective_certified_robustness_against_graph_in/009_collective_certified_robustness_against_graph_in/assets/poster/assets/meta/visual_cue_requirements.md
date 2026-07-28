# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_graph_neural_networks_power_everythi`

- Preferred role: `content`
- Cue keywords: `graph, neural, networks, power, everything, citation, search, recommendation, but, they`
- Narration: Graph neural networks power everything from citation search to recommendation, but they are alarmingly easy to fool by injecting a few malicious nodes into the graph.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_graph_neural_networks_power_everythi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, neural, networks, power, everything, citation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_hong_kong_polytechnic_university_pub`

- Preferred role: `result`
- Cue keywords: `hong, kong, polytechnic, university, published, icml, 2024, presents, first, collective`
- Narration: This paper, from the Hong Kong Polytechnic University and published at ICML 2024, presents the first collective certified robustness scheme against graph injection attacks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c2_hong_kong_polytechnic_university_pub" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hong, kong, polytechnic, university, published, icml in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_instead_certifying_node_isolation_wh`

- Preferred role: `content`
- Cue keywords: `instead, certifying, node, isolation, which, hopelessly, pessimistic, authors, certify, whole`
- Narration: Instead of certifying each node in isolation, which is hopelessly pessimistic, the authors certify a whole set of target nodes at once by formulating the worst-case attacker as an optimization problem, then relaxing that hard integer program into a linear program that solves in about a minute.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_instead_certifying_node_isolation_wh" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, certifying, node, isolation, which, hopelessly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_payoff_dramatic_citeseer_certified_r`

- Preferred role: `content`
- Cue keywords: `payoff, dramatic, citeseer, certified, ratio, jumps, zero, percent, over, eighty`
- Narration: The payoff is dramatic: on Citeseer, the certified ratio jumps from zero percent to over eighty percent.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_payoff_dramatic_citeseer_certified_r" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords payoff, dramatic, citeseer, certified, ratio, jumps in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_graph_neural_networks_workhorses_gra`

- Preferred role: `content`
- Cue keywords: `graph, neural, networks, workhorses, graph, learning, but, they, broken, graph`
- Narration: Graph neural networks are the workhorses of graph learning, but they can be broken by a graph injection attack that slips a handful of malicious nodes into the graph.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_graph_neural_networks_workhorses_gra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, neural, networks, workhorses, graph, learning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_trust_these_models_want_certified`

- Preferred role: `content`
- Cue keywords: `trust, these, models, want, certified, robustness, mathematical, guarantee, predictions, stay`
- Narration: To trust these models we want certified robustness, a mathematical guarantee that predictions stay stable under attack.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_trust_these_models_want_certified" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trust, these, models, want, certified, robustness in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_trouble_every_existing_certificate_i`

- Preferred role: `content`
- Cue keywords: `trouble, every, existing, certificate, injection, attacks, works, node, node, certifying`
- Narration: The trouble is that every existing certificate for injection attacks works node by node, certifying each target in isolation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_trouble_every_existing_certificate_i" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords trouble, every, existing, certificate, injection, attacks in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_sample_wise_view_far_too_pessimistic`

- Preferred role: `content`
- Cue keywords: `sample-wise, view, far, too, pessimistic, practice, certifies, almost, nothing, once`
- Narration: That sample-wise view is far too pessimistic, and in practice it certifies almost nothing once the attacker gets a modest budget.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_sample_wise_view_far_too_pessimistic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sample-wise, view, far, too, pessimistic, practice in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_key_insight_real_world_attacker`

- Preferred role: `content`
- Cue keywords: `key, insight, real, world, attacker, cannot, conjure, different, graph, every`
- Narration: Here is the key insight. In the real world, an attacker cannot conjure a different graph for every node they want to fool.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_key_insight_real_world_attacker" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, insight, real, world, attacker, cannot in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_they_inject_one_perturbed_graph`

- Preferred role: `content`
- Cue keywords: `they, inject, one, perturbed, graph, single, graph, disrupt, entire, set`
- Narration: They inject one perturbed graph, and that single graph has to disrupt the entire set of target nodes at the same time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_they_inject_one_perturbed_graph" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, inject, one, perturbed, graph, single in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_certify_whole_target_set_jointly`

- Preferred role: `method`
- Cue keywords: `certify, whole, target, set, jointly, instead, one, node, time, guarantee`
- Narration: If we certify the whole target set jointly instead of one node at a time, the guarantee should be much stronger.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_certify_whole_target_set_jointly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords certify, whole, target, set, jointly, instead in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_prior_collective_methods_existed_edg`

- Preferred role: `method`
- Cue keywords: `prior, collective, methods, existed, edge-modification, attacks, but, they, assume, fixed`
- Narration: Prior collective methods existed for edge-modification attacks, but they assume a fixed receptive field and simply do not carry over to injection attacks, which expand the receptive field by adding new edges.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_prior_collective_methods_existed_edg" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords prior, collective, methods, existed, edge-modification, attacks in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_delivers_first_collective_certified`

- Preferred role: `result`
- Cue keywords: `delivers, first, collective, certified, robustness, scheme, graph, neural, networks, against`
- Narration: This paper delivers the first collective certified robustness scheme for graph neural networks against injection attacks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c1_delivers_first_collective_certified" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords delivers, first, collective, certified, robustness, scheme in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_authors_cast_certification_worst_cas`

- Preferred role: `method`
- Cue keywords: `authors, cast, certification, worst-case, optimization, problem, binary, integer, quadratic, constrained`
- Narration: The authors cast certification as a worst-case optimization problem, a binary integer quadratic constrained linear program, and then introduce a customized linearization that relaxes this hard program into an ordinary linear program that can be solved efficiently.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_authors_cast_certification_worst_cas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, cast, certification, worst-case, optimization, problem in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_result_almost_model_agnostic_works_a`

- Preferred role: `result`
- Cue keywords: `result, almost, model-agnostic, works, any, message-passing, gnn, buys, huge, gains`
- Narration: The result is almost model-agnostic: it works for any message-passing GNN, and it buys huge gains in certified performance at very little computational cost.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c3_result_almost_model_agnostic_works_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords result, almost, model-agnostic, works, any, message-passing in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_builds_randomized_smoothing_s`

- Preferred role: `method`
- Cue keywords: `method, builds, randomized, smoothing, specifically, node-aware, bi-smoothing, which, randomly, deletes`
- Narration: The method builds on randomized smoothing, specifically node-aware bi-smoothing, which randomly deletes edges and nodes to blur the attacker's influence. The crucial observation is locality: an injected node can only harm a target if at least one message-passing path between them survives the smoothing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_builds_randomized_smoothing_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, builds, randomized, smoothing, specifically, node-aware in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_authors_upper_bound_probability_mess`

- Preferred role: `content`
- Cue keywords: `authors, upper-bound, probability, message, interference, turn, certifying, condition, worst-case, attacker`
- Narration: The authors upper-bound the probability of that message interference, turn it into a certifying condition, and then model a worst-case attacker who tries to make as many target nodes non-robust as possible under a budget on injected nodes and edges. That worst-case problem is the binary integer quadratic program. Because it is NP-hard, they relax it to a linear program, and they offer two versions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_authors_upper_bound_probability_mess" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, upper-bound, probability, message, interference, turn in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_standard_relaxation_needs_many_extra`

- Preferred role: `content`
- Cue keywords: `standard, relaxation, needs, many, extra, variables, while, their, customized, reformulation`
- Narration: The standard relaxation needs many extra variables, while their customized reformulation, Collective-LP-two, first collapses a quadratic term into a single vector, cutting the extra variables from order rho-squared to order rho and improving both quality and speed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_standard_relaxation_needs_many_extra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords standard, relaxation, needs, many, extra, variables in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_since_linear_program_larger_feasible`

- Preferred role: `title`
- Cue keywords: `since, linear, program, larger, feasible, region, integer, one, its, answer`
- Narration: Since the linear program has a larger feasible region than the integer one, its answer is always a sound lower bound on the true certified ratio.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s05_c4_since_linear_program_larger_feasible" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords since, linear, program, larger, feasible, region in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_evaluation_two_standard_citation_gra`

- Preferred role: `method`
- Cue keywords: `evaluation, two, standard, citation, graphs, cora-ml, citeseer, few, thousand, nodes`
- Narration: The evaluation uses two standard citation graphs, Cora-ML and Citeseer, with a few thousand nodes each, and two representative backbones, a graph convolution network and a graph attention network.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_evaluation_two_standard_citation_gra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, two, standard, citation, graphs, cora-ml in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_attacker_budget_swept_twenty_hundred`

- Preferred role: `result`
- Cue keywords: `attacker, budget, swept, twenty, hundred, sixty, injected, nodes, per-node, edge`
- Narration: The attacker's budget is swept from twenty up to a hundred and sixty injected nodes, with the per-node edge limit set to each graph's average degree.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_attacker_budget_swept_twenty_hundred" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords attacker, budget, swept, twenty, hundred, sixty in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_smoothed_classifier_estimated_hundre`

- Preferred role: `content`
- Cue keywords: `smoothed, classifier, estimated, hundred, thousand, monte, carlo, samples, one, percent`
- Narration: The smoothed classifier is estimated with a hundred thousand Monte Carlo samples at a one percent confidence level, and every linear program is solved with the MOSEK solver through CVXPY.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_smoothed_classifier_estimated_hundre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords smoothed, classifier, estimated, hundred, thousand, monte in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_night_and_day_improv`

- Preferred role: `result`
- Cue keywords: `headline, result, night-and-day, improvement`
- Narration: The headline result is a night-and-day improvement.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_headline_result_night_and_day_improv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, night-and-day, improvement in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_number_injected_nodes_grows_sample_w`

- Preferred role: `method`
- Cue keywords: `number, injected, nodes, grows, sample-wise, baseline, collapses, zero, certified, nodes`
- Narration: As the number of injected nodes grows, the sample-wise baseline collapses to zero certified nodes, while the collective certificates hold strong.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_number_injected_nodes_grows_sample_w" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords number, injected, nodes, grows, sample-wise, baseline in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_citeseer_hundred_forty_injected_node`

- Preferred role: `result`
- Cue keywords: `citeseer, hundred, forty, injected, nodes, standard, collective, relaxation, certifies, seventy-three`
- Narration: On Citeseer with a hundred and forty injected nodes, the standard collective relaxation certifies seventy-three percent of targets and the customized version reaches eighty-one point two percent, both against zero percent for sample-wise.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_citeseer_hundred_forty_injected_node" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords citeseer, hundred, forty, injected, nodes, standard in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_customized_collective_lp_two_consist`

- Preferred role: `content`
- Cue keywords: `customized, collective-lp-two, consistently, matches, beats, standard, one, one, setting, over`
- Narration: The customized Collective-LP-two consistently matches or beats the standard one, in one setting by over two hundred percent relative, and it does so far faster, solving even the largest budgets in about a minute.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_customized_collective_lp_two_consist" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords customized, collective-lp-two, consistently, matches, beats, standard in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_how_much_does_linear_relaxation`

- Preferred role: `content`
- Cue keywords: `how, much, does, linear, relaxation, cost`
- Narration: How much does the linear relaxation cost us?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_how_much_does_linear_relaxation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, much, does, linear, relaxation, cost in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_find_out_authors_compare_relaxed`

- Preferred role: `result`
- Cue keywords: `find, out, authors, compare, relaxed, program, against, exact, integer, program`
- Narration: To find out, the authors compare the relaxed program against the exact integer program, which is only tractable for very small budgets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c2_find_out_authors_compare_relaxed" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords find, out, authors, compare, relaxed, program in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_gap_small_customized_relaxation_lose`

- Preferred role: `content`
- Cue keywords: `gap, small, customized, relaxation, loses, only, about, five, percent, certified`
- Narration: The gap is small: the customized relaxation loses only about five percent in certified ratio, which also explains why the collective approach can trail sample-wise at very tiny budgets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_gap_small_customized_relaxation_lose" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gap, small, customized, relaxation, loses, only in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_runtime_standard_relaxation_blows_pa`

- Preferred role: `result`
- Cue keywords: `runtime, standard, relaxation, blows, past, thousand, seconds, attack, grows, while`
- Narration: On runtime, the standard relaxation blows up past a thousand seconds as the attack grows, while the customized version stays near a single minute, and at equal clean accuracy it dominates the standard version on the accuracy-versus-certification trade-off.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c4_runtime_standard_relaxation_blows_pa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords runtime, standard, relaxation, blows, past, thousand in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_put_numbers_citeseer_hundred_forty`

- Preferred role: `method`
- Cue keywords: `put, numbers, citeseer, hundred, forty, injected, nodes, certified, ratio, jumps`
- Narration: To put numbers on it: on Citeseer at a hundred and forty injected nodes, the certified ratio jumps from zero percent under sample-wise certification to eighty-one point two percent with the customized collective method.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_put_numbers_citeseer_hundred_forty" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords put, numbers, citeseer, hundred, forty, injected in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_collective_linear_program_solves_rou`

- Preferred role: `content`
- Cue keywords: `collective, linear, program, solves, roughly, one, minute`
- Narration: That collective linear program solves in roughly one minute.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_collective_linear_program_solves_rou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords collective, linear, program, solves, roughly, one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_customized_relaxation_improves_stand`

- Preferred role: `content`
- Cue keywords: `customized, relaxation, improves, standard, one, two, hundred, sixteen, percent, relative`
- Narration: The customized relaxation improves on the standard one by up to two hundred and sixteen percent relative, and it sits only about five percent below the exact but far slower integer solution.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_customized_relaxation_improves_stand" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords customized, relaxation, improves, standard, one, two in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_short_injecting_five_percent_graph`

- Preferred role: `content`
- Cue keywords: `short, injecting, five, percent, graph, certified, ratio, climbs, zero, over`
- Narration: In short, injecting five percent of the graph, the certified ratio climbs from zero to over eighty percent on both datasets.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_short_injecting_five_percent_graph" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords short, injecting, five, percent, graph, certified in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lesson_simple_but_powerful`

- Preferred role: `content`
- Cue keywords: `lesson, simple, but, powerful`
- Narration: The lesson is simple but powerful.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lesson_simple_but_powerful" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lesson, simple, but, powerful in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_certifying_whole_set_nodes_together`

- Preferred role: `result`
- Cue keywords: `certifying, whole, set, nodes, together, instead, one, time, transforms, near-useless`
- Narration: Certifying a whole set of nodes together, instead of one at a time, transforms a near-useless zero percent guarantee into an eighty percent certified ratio against graph injection attacks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c2_certifying_whole_set_nodes_together" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords certifying, whole, set, nodes, together, instead in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_customized_linear_relaxation_keeps_t`

- Preferred role: `content`
- Cue keywords: `customized, linear, relaxation, keeps, tractable, solving, about, minute, even, large`
- Narration: A customized linear relaxation keeps this tractable, solving in about a minute even for large attacks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_customized_linear_relaxation_keeps_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords customized, linear, relaxation, keeps, tractable, solving in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_concrete_step_toward_provable_defens`

- Preferred role: `method`
- Cue keywords: `concrete, step, toward, provable, defenses, practical, because, shares, same, smoothed`
- Narration: It is a concrete step toward provable defenses that are practical, and because it shares the same smoothed model, it plugs right in alongside existing sample-wise certificates to stay strong across every attack budget.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_concrete_step_toward_provable_defens" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords concrete, step, toward, provable, defenses, practical in title/desc so the matcher can verify semantic overlap.
