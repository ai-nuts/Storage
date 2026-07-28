# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_reinforcement_learning_now_drives_sa`

- Preferred role: `content`
- Cue keywords: `reinforcement, learning, now, drives, safety-critical, systems, like, autonomous, vehicles, but`
- Narration: Reinforcement learning now drives safety-critical systems like autonomous vehicles, but adversarial perturbations to a policy's input states can quietly steer it toward disaster.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_reinforcement_learning_now_drives_sa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reinforcement, learning, now, drives, safety-critical, systems in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_many_defenses_improve_robustness_emp`

- Preferred role: `guidance`
- Cue keywords: `many, defenses, improve, robustness, empirically, yet, almost, none, certify, guarantees`
- Narration: Many defenses improve robustness empirically, yet almost none can certify it with guarantees. This paper introduces CROP, the first unified framework to certify robust policies for reinforcement learning through functional smoothing.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s01_c2_many_defenses_improve_robustness_emp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords many, defenses, improve, robustness, empirically, yet in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_crop_certifies_robustness_two_levels`

- Preferred role: `figure`
- Cue keywords: `crop, certifies, robustness, two, levels, stability, action, taken, state, provable`
- Narration: CROP certifies robustness at two levels: the stability of the action taken at each state, and a provable lower bound on the cumulative reward across a whole trajectory.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c3_crop_certifies_robustness_two_levels" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crop, certifies, robustness, two, levels, stability in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_authors_benchmark_nine_existing_robu`

- Preferred role: `result`
- Cue keywords: `authors, benchmark, nine, existing, robust, algorithms, across, four, environments, show`
- Narration: Using it, the authors benchmark nine existing robust RL algorithms across four environments and show that their certificates are often tight.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_authors_benchmark_nine_existing_robu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, benchmark, nine, existing, robust, algorithms in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_reinforcement_learning_moved_domains`

- Preferred role: `content`
- Cue keywords: `reinforcement, learning, moved, domains, where, failure, costly, such, autonomous, driving`
- Narration: Reinforcement learning has moved into domains where failure is costly, such as autonomous driving and trading.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_reinforcement_learning_moved_domains" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reinforcement, learning, moved, domains, where, failure in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_researchers_shown_adversary_who`

- Preferred role: `content`
- Cue keywords: `but, researchers, shown, adversary, who, slightly, perturbs, state, observations, fed`
- Narration: But researchers have shown that an adversary who slightly perturbs the state observations fed to an RL agent can reliably change its decisions. A wave of empirical defenses followed, only to be defeated by newer adaptive attacks.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_but_researchers_shown_adversary_who" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, researchers, shown, adversary, who, slightly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_what_been_missing_certification_way`

- Preferred role: `method`
- Cue keywords: `what, been, missing, certification, way, prove, rather, just, observe, trained`
- Narration: What has been missing is certification: a way to prove, rather than just observe, that a trained policy stays reliable under every perturbation within a bounded budget.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_what_been_missing_certification_way" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, been, missing, certification, way, prove in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_tackles_exactly_gap_reinforcement_le`

- Preferred role: `content`
- Cue keywords: `tackles, exactly, gap, reinforcement, learning`
- Narration: This paper tackles exactly that gap for reinforcement learning.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_tackles_exactly_gap_reinforcement_le" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tackles, exactly, gap, reinforcement, learning in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_core_motivation_trust_you_cannot`

- Preferred role: `content`
- Cue keywords: `core, motivation, trust, you, cannot, prove, policy, robust, passing, today`
- Narration: The core motivation is trust. If you cannot prove a policy is robust, then passing today's attacks tells you little about tomorrow's.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_core_motivation_trust_you_cannot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, motivation, trust, you, cannot, prove in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_randomized_smoothing_become_leading`

- Preferred role: `result`
- Cue keywords: `randomized, smoothing, become, leading, tool, certifying, image, classifiers, but, reinforcement`
- Narration: Randomized smoothing has become a leading tool for certifying image classifiers, but reinforcement learning does not fit its mold.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_randomized_smoothing_become_leading" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords randomized, smoothing, become, leading, tool, certifying in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_classification_confidence_output_liv`

- Preferred role: `result`
- Cue keywords: `classification, confidence, output, lives, known, zero-to-one, range, behaves, like, probability`
- Narration: In classification the confidence output lives in a known zero-to-one range and behaves like a probability; in Q-learning the value function has an unknown range and its outputs are not probabilities at all.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c3_classification_confidence_output_liv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classification, confidence, output, lives, known, zero-to-one in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_top_single_action_decision_not`

- Preferred role: `figure`
- Cue keywords: `top, single, action, decision, not, whole, story, what, ultimately, matters`
- Narration: On top of that, a single action decision is not the whole story: what ultimately matters is the reward accumulated along an entire trajectory of decisions. CROP is designed to overcome both obstacles.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c4_top_single_action_decision_not" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, single, action, decision, not, whole in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_crop_makes_three_main_contributions`

- Preferred role: `content`
- Cue keywords: `crop, makes, three, main, contributions, first, defines, two, certification, criteria`
- Narration: CROP makes three main contributions. First, it defines two certification criteria for reinforcement learning: robustness of the per-state action, and a lower bound on the cumulative reward.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_crop_makes_three_main_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crop, makes, three, main, contributions, first in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_turns_criterion_algorithm_cro`

- Preferred role: `result`
- Cue keywords: `second, turns, criterion, algorithm, crop-loact, local, randomized, smoothing, certify, radius`
- Narration: Second, it turns each criterion into an algorithm. CROP-LoAct uses local randomized smoothing to certify a radius around each state within which the chosen action cannot change.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_second_turns_criterion_algorithm_cro" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, turns, criterion, algorithm, crop-loact, local in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_crop_gre_global_smoothing_bound_expe`

- Preferred role: `content`
- Cue keywords: `crop-gre, global, smoothing, bound, expected, percentile, reward, crop-lore, performs, adaptive`
- Narration: CROP-GRe uses global smoothing to bound the expected and percentile reward, and CROP-LoRe performs an adaptive tree search to produce a much tighter absolute lower bound on reward.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_crop_gre_global_smoothing_bound_expe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crop-gre, global, smoothing, bound, expected, percentile in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_authors_apply_these_tools`

- Preferred role: `result`
- Cue keywords: `third, authors, apply, these, tools, nine, existing, robust, algorithms, across`
- Narration: Third, the authors apply these tools to nine existing robust RL algorithms across four environments, and release the results as an open leaderboard for the community.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_third_authors_apply_these_tools" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, authors, apply, these, tools, nine in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_engine_crop_functional_smoothing_sta`

- Preferred role: `method`
- Cue keywords: `engine, crop, functional, smoothing, state, action, method, adds, gaussian, noise`
- Narration: The engine of CROP is functional smoothing. At each state, and for each action, the method adds Gaussian noise to the state and averages the trained Q-network's output, producing a smoothed value function.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_engine_crop_functional_smoothing_sta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords engine, crop, functional, smoothing, state, action in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_key_lemma_shows_smoothed_function`

- Preferred role: `guidance`
- Cue keywords: `key, lemma, shows, smoothed, function, lipschitz, continuous, constant, shrinks, smoothing`
- Narration: A key lemma shows this smoothed function is Lipschitz continuous, with a constant that shrinks as the smoothing variance grows. From that continuity, Theorem 1 gives a certified radius: as long as the perturbation is smaller than this radius, the smoothed policy's action does not change.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s05_c2_key_lemma_shows_smoothed_function" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, lemma, shows, smoothed, function, lipschitz in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_radius_depends_gap_between_best`

- Preferred role: `method`
- Cue keywords: `radius, depends, gap, between, best, runner-up, smoothed, action-values, revealing, trade-off`
- Narration: The radius depends on the gap between the best and runner-up smoothed action-values, revealing a trade-off, since more smoothing stabilizes the values but also narrows their margin.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_radius_depends_gap_between_best" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords radius, depends, gap, between, best, runner-up in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_cumulative_reward_global_smoothing_t`

- Preferred role: `figure`
- Cue keywords: `cumulative, reward, global, smoothing, treats, whole, trajectory, function, bound, expected`
- Narration: For cumulative reward, global smoothing treats the whole trajectory as a function to bound the expected and percentile reward, while the adaptive local search of CROP-LoRe grows a trajectory tree to certify a tight absolute lower bound.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c4_cumulative_reward_global_smoothing_t" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cumulative, reward, global, smoothing, treats, whole in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_test_framework_broadly_authors_run`

- Preferred role: `guidance`
- Cue keywords: `test, framework, broadly, authors, run, four, environments, spanning, very, different`
- Narration: To test the framework broadly, the authors run it on four environments spanning very different regimes.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s06_c1_test_framework_broadly_authors_run" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, framework, broadly, authors, run, four in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_pong_freeway_high_dimensional_atari`

- Preferred role: `content`
- Cue keywords: `pong, freeway, high-dimensional, atari, games, cartpole, classic, low-dimensional, control, task`
- Narration: Pong and Freeway are high-dimensional Atari games; CartPole is a classic low-dimensional control task; and Highway simulates autonomous driving.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_pong_freeway_high_dimensional_atari" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pong, freeway, high-dimensional, atari, games, cartpole in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_these_they_certify_nine_existing`

- Preferred role: `method`
- Cue keywords: `these, they, certify, nine, existing, reinforcement, learning, methods, ranging, standard`
- Narration: On these, they certify nine existing reinforcement learning methods, ranging from standard training and Gaussian augmentation to adversarial training, the SA-MDP variants, RadialRL, CARRL, NoisyNet, and gradient-based DQN.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_these_they_certify_nine_existing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, they, certify, nine, existing, reinforcement in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_makes_crop_not_just_single`

- Preferred role: `method`
- Cue keywords: `makes, crop, not, just, single, certificate, but, benchmark, places, many`
- Narration: This makes CROP not just a single certificate but a benchmark that places many robust RL methods on a common, provable footing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_makes_crop_not_just_single" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, crop, not, just, single, certificate in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_certifications_reveal_clear_consiste`

- Preferred role: `result`
- Cue keywords: `certifications, reveal, clear, consistent, winners, freeway, radialrl, achieves, highest, certified`
- Narration: The certifications reveal clear and consistent winners. On Freeway, RadialRL achieves the highest certified radius across every smoothing level, because it explicitly optimizes against worst-case perturbations.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_certifications_reveal_clear_consiste" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords certifications, reveal, clear, consistent, winners, freeway in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_pong_sa_mdp_convex_relaxation_most`

- Preferred role: `content`
- Cue keywords: `pong, sa-mdp, convex, relaxation, most, certifiably, robust`
- Narration: On Pong, SA-MDP with the convex relaxation is the most certifiably robust.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_pong_sa_mdp_convex_relaxation_most" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pong, sa-mdp, convex, relaxation, most, certifiably in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_encouragingly_these_certified_rankin`

- Preferred role: `content`
- Cue keywords: `encouragingly, these, certified, rankings, largely, agree, what, people, had, observed`
- Narration: Encouragingly, these certified rankings largely agree with what people had observed empirically, which builds confidence in the certificates.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_encouragingly_these_certified_rankin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords encouragingly, these, certified, rankings, largely, agree in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_analysis_also_surfaces_new_structure`

- Preferred role: `method`
- Cue keywords: `analysis, also, surfaces, new, structure, pong, every, method, shows, periodic`
- Narration: The analysis also surfaces new structure: on Pong every method shows a periodic pattern in its certified radius over time, with robustness peaking at confident states such as when the ball flies toward the paddle, an insight that could guide future robust training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_analysis_also_surfaces_new_structure" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords analysis, also, surfaces, new, structure, pong in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_central_ablation_studies_smoothing_v`

- Preferred role: `method`
- Cue keywords: `central, ablation, studies, smoothing, variance, sigma, freeway, robustness, strong, methods`
- Narration: A central ablation studies the smoothing variance sigma. On Freeway, robustness for the strong methods keeps improving as sigma grows all the way to one point zero, since Freeway tolerates large noise.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_central_ablation_studies_smoothing_v" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords central, ablation, studies, smoothing, variance, sigma in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_pong_story_differs_too_much`

- Preferred role: `method`
- Cue keywords: `pong, story, differs, too, much, smoothing, hurts, moderate, sigma, between`
- Narration: On Pong the story differs: too much smoothing hurts, and a moderate sigma between about zero point zero one and zero point zero three works best for nearly all methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_pong_story_differs_too_much" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pong, story, differs, too, much, smoothing in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_authors_also_compare_their_three`

- Preferred role: `content`
- Cue keywords: `authors, also, compare, their, three, reward, bounds`
- Narration: The authors also compare their three reward bounds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_authors_also_compare_their_three" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, compare, their, three, reward in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_percentile_bound_far_tighter_loose`

- Preferred role: `method`
- Cue keywords: `percentile, bound, far, tighter, loose, expectation, bound, absolute, lower, bound`
- Narration: The percentile bound is far tighter than the loose expectation bound, and the absolute lower bound from CROP-LoRe often matches the empirical reward under PGD attack exactly, a zero gap that demonstrates the certificates are tight rather than merely valid.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_percentile_bound_far_tighter_loose" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords percentile, bound, far, tighter, loose, expectation in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_scope_crop`

- Preferred role: `guidance`
- Cue keywords: `few, numbers, capture, scope, crop, first, unified, certification, framework, reinforcement`
- Narration: A few numbers capture the scope. CROP is the first unified certification framework for reinforcement learning, working at both the action level and the cumulative-reward level.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_scope_crop" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, scope, crop, first in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_certifies_nine_existing_robust_metho`

- Preferred role: `method`
- Cue keywords: `certifies, nine, existing, robust, methods, across, four, environments, pong, freeway`
- Narration: It certifies nine existing robust RL methods across four environments: Pong, Freeway, CartPole, and Highway.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_certifies_nine_existing_robust_metho" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords certifies, nine, existing, robust, methods, across in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_does_three_algorithms_crop_loact_act`

- Preferred role: `content`
- Cue keywords: `does, three, algorithms, crop-loact, actions, crop-gre, crop-lore, reward`
- Narration: It does so with three algorithms: CROP-LoAct for actions, and CROP-GRe and CROP-LoRe for reward.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_does_three_algorithms_crop_loact_act" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords does, three, algorithms, crop-loact, actions, crop-gre in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_smoothing_variance_pushed_high_one`

- Preferred role: `content`
- Cue keywords: `smoothing, variance, pushed, high, one, point, zero, freeway, reward, robustness`
- Narration: The smoothing variance is pushed as high as one point zero on Freeway, and reward robustness is reported through three bounds, an expectation bound, a fifty-percent percentile bound, and an absolute lower bound.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_smoothing_variance_pushed_high_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords smoothing, variance, pushed, high, one, point in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_message_crop_robustness_rein`

- Preferred role: `content`
- Cue keywords: `lasting, message, crop, robustness, reinforcement, learning, need, not, matter, hope`
- Narration: The lasting message of CROP is that robustness in reinforcement learning need not be a matter of hope.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c1_lasting_message_crop_robustness_rein" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, message, crop, robustness, reinforcement, learning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_smoothing_value_function_you_prove`

- Preferred role: `content`
- Cue keywords: `smoothing, value, function, you, prove, agent, action, stays, fixed, within`
- Narration: By smoothing the value function, you can prove that an agent's action stays fixed within a certified radius, and you can prove a lower bound on the reward it will collect under any bounded attack.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_smoothing_value_function_you_prove" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords smoothing, value, function, you, prove, agent in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_applied_nine_methods_across_four`

- Preferred role: `method`
- Cue keywords: `applied, nine, methods, across, four, environments, these, certificates, not, only`
- Narration: Applied to nine methods across four environments, these certificates are not only correct but often tight, matching what attacks achieve.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_applied_nine_methods_across_four" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords applied, nine, methods, across, four, environments in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_crop_turns_robust_something_you`

- Preferred role: `method`
- Cue keywords: `crop, turns, robust, something, you, measure, compare, common, provable, leaderboard`
- Narration: CROP turns robust RL into something you can measure and compare on a common, provable leaderboard, and invites the community to certify more methods and more environments in future work.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c4_crop_turns_robust_something_you" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crop, turns, robust, something, you, measure in title/desc so the matcher can verify semantic overlap.
