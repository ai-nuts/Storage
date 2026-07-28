# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_peking_university_google_citransnet`

- Preferred role: `method`
- Cue keywords: `peking, university, google, citransnet, context-integrated, transformer, auction, design`
- Narration: From Peking University and Google, CITransNet is a context-integrated transformer for auction design.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_peking_university_google_citransnet" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords peking, university, google, citransnet, context-integrated, transformer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_maximizes_seller_revenue_while_stayi`

- Preferred role: `method`
- Cue keywords: `maximizes, seller, revenue, while, staying, incentive-compatible, discovers, asymmetric, solutions, generalizes`
- Narration: It maximizes seller revenue while staying incentive-compatible, discovers asymmetric solutions, and generalizes to auction sizes it never saw during training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_maximizes_seller_revenue_while_stayi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords maximizes, seller, revenue, while, staying, incentive-compatible in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_classic_problem_auction_theory_desig`

- Preferred role: `content`
- Cue keywords: `classic, problem, auction, theory, designing, mechanism, maximizes, seller, revenue, while`
- Narration: A classic problem in auction theory is designing a mechanism that maximizes the seller's revenue while staying incentive-compatible.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_classic_problem_auction_theory_desig" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords classic, problem, auction, theory, designing, mechanism in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_myerson_solved_single_item_case_1981`

- Preferred role: `method`
- Cue keywords: `myerson, solved, single-item, case, 1981, but, multi-item, case, remains, open`
- Narration: Myerson solved the single-item case in 1981, but the multi-item case remains open, and prior deep methods assume fixed or symmetric auctions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_myerson_solved_single_item_case_1981" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords myerson, solved, single-item, case, 1981, but in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_real_auctions_richer`

- Preferred role: `content`
- Cue keywords: `real, auctions, richer`
- Narration: Real auctions are richer.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_real_auctions_richer" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords real, auctions, richer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_e_commerce_advertising_many_bidders`

- Preferred role: `content`
- Cue keywords: `e-commerce, advertising, many, bidders, compete, many, slots, described, features, every`
- Narration: In e-commerce advertising, many bidders compete for many ad slots described by features, and every round has a different number of participants.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_e_commerce_advertising_many_bidders" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords e-commerce, advertising, many, bidders, compete, many in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_need_architecture_absorbs_context_ha`

- Preferred role: `figure`
- Cue keywords: `need, architecture, absorbs, context, handles, varying, auction, sizes`
- Narration: We need an architecture that absorbs context and handles varying auction sizes.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s03_c3_need_architecture_absorbs_context_ha" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords need, architecture, absorbs, context, handles, varying in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_two_contributions`

- Preferred role: `content`
- Cue keywords: `makes, two, contributions`
- Narration: The paper makes two contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_two_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, two, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_extends_regretnet_framework_contextu`

- Preferred role: `guidance`
- Cue keywords: `extends, regretnet, framework, contextual, setting, proves, sample-complexity, bound`
- Narration: It extends the RegretNet framework to the contextual setting and proves a sample-complexity bound.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c2_extends_regretnet_framework_contextu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords extends, regretnet, framework, contextual, setting, proves in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_introduces_citransnet_permutation_eq`

- Preferred role: `method`
- Cue keywords: `introduces, citransnet, permutation-equivariant, over, bids, contexts, not, restricted, symmetric, auctions`
- Narration: And it introduces CITransNet, permutation-equivariant over bids and contexts, not restricted to symmetric auctions, with a parameter count independent of auction scale.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_introduces_citransnet_permutation_eq" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, citransnet, permutation-equivariant, over, bids, contexts in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_citransnet_takes_three_inputs_biddin`

- Preferred role: `content`
- Cue keywords: `citransnet, takes, three, inputs, bidding, profile, bidder-contexts, item-contexts`
- Narration: CITransNet takes three inputs: the bidding profile, bidder-contexts, and item-contexts.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_citransnet_takes_three_inputs_biddin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords citransnet, takes, three, inputs, bidding, profile in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_embeds_contexts_bids_representation`

- Preferred role: `method`
- Cue keywords: `embeds, contexts, bids, representation, per, bidder-item, pair, passes, through, transformer`
- Narration: It embeds contexts with bids into a representation per bidder-item pair, then passes it through transformer interaction layers that mix a global average with row and column transformers, staying permutation-equivariant.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_embeds_contexts_bids_representation" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords embeds, contexts, bids, representation, per, bidder-item in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_final_layer_outputs_allocations_paym`

- Preferred role: `method`
- Cue keywords: `final, layer, outputs, allocations, payments, zero-regret, enforced, during`
- Narration: A final layer outputs allocations and payments, with zero-regret enforced during training.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_final_layer_outputs_allocations_paym" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords final, layer, outputs, allocations, payments, zero-regret in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_they_evaluate_nine_synthetic_setting`

- Preferred role: `content`
- Cue keywords: `they, evaluate, nine, synthetic, settings`
- Narration: They evaluate on nine synthetic settings.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_they_evaluate_nine_synthetic_setting" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, evaluate, nine, synthetic, settings in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_three_single_item_cases_through_know`

- Preferred role: `content`
- Cue keywords: `three, single-item, cases, through, known, myerson-optimal, solutions, sanity, check`
- Narration: Three single-item cases, A through C, have known Myerson-optimal solutions as a sanity check.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_three_single_item_cases_through_know" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords three, single-item, cases, through, known, myerson-optimal in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_other_six_through_multi_item_auction`

- Preferred role: `content`
- Cue keywords: `other, six, through, multi-item, auctions, five, bidders, ten, items, largest`
- Narration: The other six, D through I, are multi-item auctions up to five bidders and ten items, the largest size in the auction-design literature.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_other_six_through_multi_item_auction" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords other, six, through, multi-item, auctions, five in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_results_come_two_parts`

- Preferred role: `result`
- Cue keywords: `results, come, two, parts`
- Narration: Results come in two parts.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_results_come_two_parts" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords results, come, two, parts in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_single_item_settings_citransnet_near`

- Preferred role: `result`
- Cue keywords: `single-item, settings, citransnet, nearly, recovers, myerson, optimal, revenue, 0.593, against`
- Narration: On single-item settings, CITransNet nearly recovers Myerson's optimal revenue, 0.593 against 0.594, with regret below one thousandth, while context-blind baselines fall short.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_single_item_settings_citransnet_near" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single-item, settings, citransnet, nearly, recovers, myerson in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_harder_multi_item_settings_beats_ite`

- Preferred role: `result`
- Cue keywords: `harder, multi-item, settings, beats, item-wise, myerson, baseline, all, six, configurations`
- Narration: On the harder multi-item settings, it beats the Item-wise Myerson baseline in all six configurations, with gains reaching ten percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_harder_multi_item_settings_beats_ite" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords harder, multi-item, settings, beats, item-wise, myerson in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_isolate_why_works_authors_replace`

- Preferred role: `method`
- Cue keywords: `isolate, why, works, authors, replace, transformer, layers, regretnet, fully-connected, equivariantnet`
- Narration: To isolate why it works, the authors replace the transformer layers with RegretNet's fully-connected and EquivariantNet's equivariant layers, giving CIRegretNet and CIEquivariantNet.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_isolate_why_works_authors_replace" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords isolate, why, works, authors, replace, transformer in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_both_still_get_context_yet`

- Preferred role: `method`
- Cue keywords: `both, still, get, context, yet, earn, less, revenue, everywhere, pinning`
- Narration: Both still get context, yet earn less revenue everywhere, pinning the gain on the transformer layers.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_both_still_get_context_yet" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords both, still, get, context, yet, earn in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_removing_context_hurts_even_easy`

- Preferred role: `content`
- Cue keywords: `removing, context, hurts, even, easy, settings`
- Narration: Removing context hurts even easy settings.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_removing_context_hurts_even_easy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords removing, context, hurts, even, easy, settings in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_single_item_benchmark_citransnet_rea`

- Preferred role: `result`
- Cue keywords: `single-item, benchmark, citransnet, reaches, 0.593, versus, optimal, 0.594`
- Narration: On the single-item benchmark, CITransNet reaches 0.593 versus the optimal 0.594.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_single_item_benchmark_citransnet_rea" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single-item, benchmark, citransnet, reaches, 0.593, versus in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_three_bidder_ten_item_setting_earns`

- Preferred role: `result`
- Cue keywords: `three-bidder, ten-item, setting, earns, 6.872, against, item-wise, myerson, 6.509, one`
- Narration: In the three-bidder ten-item setting it earns 6.872 against Item-wise Myerson's 6.509, and one continuous-context margin nears ten percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_three_bidder_ten_item_setting_earns" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords three-bidder, ten-item, setting, earns, 6.872, against in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_wins_all_six_multi_item_settings`

- Preferred role: `content`
- Cue keywords: `wins, all, six, multi-item, settings`
- Narration: It wins all six multi-item settings.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_wins_all_six_multi_item_settings" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords wins, all, six, multi-item, settings in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_context_first_class_input_u`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, context, first-class, input, unlocks, better, learned, auctions`
- Narration: The takeaway: context as a first-class input unlocks better learned auctions.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_context_first_class_input_u" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, context, first-class, input, unlocks, better in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_citransnet_near_optimal_asymmetric_w`

- Preferred role: `content`
- Cue keywords: `citransnet, near-optimal, asymmetric, when, needed, incentive-compatible`
- Narration: CITransNet is near-optimal, asymmetric when needed, and incentive-compatible.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_citransnet_near_optimal_asymmetric_w" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords citransnet, near-optimal, asymmetric, when, needed, incentive-compatible in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_its_size_independent_parameter_count`

- Preferred role: `method`
- Cue keywords: `its, size-independent, parameter, count, lets, one, trained, transfer, auction, sizes`
- Narration: Its size-independent parameter count lets one trained model transfer to auction sizes it never saw.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_its_size_independent_parameter_count" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, size-independent, parameter, count, lets, one in title/desc so the matcher can verify semantic overlap.
