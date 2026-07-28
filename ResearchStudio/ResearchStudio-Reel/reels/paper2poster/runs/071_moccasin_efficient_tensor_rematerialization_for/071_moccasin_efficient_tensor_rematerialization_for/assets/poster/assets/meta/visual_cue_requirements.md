# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_deploying_neural_networks_edge_devic`

- Preferred role: `method`
- Cue keywords: `deploying, neural, networks, edge, devices, often, bottlenecked, tight, memory`
- Narration: Deploying and training neural networks on edge devices is often bottlenecked by tight memory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_deploying_neural_networks_edge_devic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deploying, neural, networks, edge, devices, often in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_tensor_rematerialization_recomputing`

- Preferred role: `content`
- Cue keywords: `tensor, rematerialization, recomputing, intermediate, tensors, instead, storing, them, trades, extra`
- Narration: Tensor rematerialization, recomputing intermediate tensors instead of storing them, trades extra compute for lower peak memory.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_tensor_rematerialization_recomputing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tensor, rematerialization, recomputing, intermediate, tensors, instead in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_introduces_moccasin_new_constraint_p`

- Preferred role: `method`
- Cue keywords: `introduces, moccasin, new, constraint, programming, formulation, problem, minimizing, execution, time`
- Narration: This paper introduces Moccasin, a new constraint programming formulation for the problem of minimizing execution time under a memory budget.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_introduces_moccasin_new_constraint_p" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords introduces, moccasin, new, constraint, programming, formulation in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_unlike_prior_work_needs_quadratic`

- Preferred role: `content`
- Cue keywords: `unlike, prior, work, needs, quadratic, number, boolean, variables, moccasin, only`
- Narration: Unlike prior work that needs a quadratic number of Boolean variables, Moccasin uses only a linear number of integer variables, letting it scale to much larger compute graphs and run up to an order of magnitude faster.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_unlike_prior_work_needs_quadratic" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unlike, prior, work, needs, quadratic, number in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_neural_networks_running_edge_devices`

- Preferred role: `method`
- Cue keywords: `neural, networks, running, edge, devices, constrained, above, all, memory`
- Narration: Neural networks running on edge devices are constrained above all by memory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_neural_networks_running_edge_devices" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords neural, networks, running, edge, devices, constrained in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_one_way_fit_large_small`

- Preferred role: `content`
- Cue keywords: `one, way, fit, large, small, memory, footprint, rematerialization, instead, storing`
- Narration: One way to fit a large model into a small memory footprint is rematerialization: instead of storing every intermediate tensor, you recompute some of them on demand. The catch is that recomputation costs time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_one_way_fit_large_small" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, way, fit, large, small, memory in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_core_problem_scheduling_one_given`

- Preferred role: `content`
- Cue keywords: `core, problem, scheduling, one, given, compute, graph, fixed, memory, budget`
- Narration: So the core problem is a scheduling one: for a given compute graph and a fixed memory budget, decide which tensors to retain and which to recompute so that total execution time is as small as possible while peak memory never exceeds the budget.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_core_problem_scheduling_one_given" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, problem, scheduling, one, given, compute in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_hard_combinatorial_optimization_gene`

- Preferred role: `content`
- Cue keywords: `hard, combinatorial, optimization, general, pspace-complete`
- Narration: This is a hard combinatorial optimization, in general PSPACE-complete.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_hard_combinatorial_optimization_gene" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hard, combinatorial, optimization, general, pspace-complete in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_leading_prior_method_checkmate_casts`

- Preferred role: `method`
- Cue keywords: `leading, prior, method, checkmate, casts, rematerialization, mixed-integer, linear, program`
- Narration: The leading prior method, Checkmate, casts rematerialization as a mixed-integer linear program.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_leading_prior_method_checkmate_casts" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords leading, prior, method, checkmate, casts, rematerialization in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_expressive_but_its_number_boolean`

- Preferred role: `content`
- Cue keywords: `expressive, but, its, number, boolean, decision, variables, grows, square, number`
- Narration: It is expressive, but its number of Boolean decision variables grows with the square of the number of nodes in the graph.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_expressive_but_its_number_boolean" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords expressive, but, its, number, boolean, decision in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_quadratic_growth_becomes_wall_graphs`

- Preferred role: `content`
- Cue keywords: `quadratic, growth, becomes, wall, graphs, few, hundred, nodes, few, thousand`
- Narration: That quadratic growth becomes a wall: for graphs with a few hundred nodes and a few thousand edges, Checkmate either times out or runs out of memory during the solve.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_quadratic_growth_becomes_wall_graphs" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords quadratic, growth, becomes, wall, graphs, few in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_because_trend_toward_on_device_stric`

- Preferred role: `method`
- Cue keywords: `because, trend, toward, on-device, stricter, latency, targets, keeps, enlarging, these`
- Narration: Because the trend toward on-device training and stricter latency targets keeps enlarging these graphs, we need a formulation whose complexity grows much more slowly, so realistic graphs can be solved within an acceptable compile time.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c4_because_trend_toward_on_device_stric" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, trend, toward, on-device, stricter, latency in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_main_contribution_moccasin_constrain`

- Preferred role: `method`
- Cue keywords: `main, contribution, moccasin, constraint, programming, formulation, tensor, rematerialization`
- Narration: The paper's main contribution is Moccasin, a constraint programming formulation of tensor rematerialization.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_main_contribution_moccasin_constrain" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords main, contribution, moccasin, constraint, programming, formulation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_its_central_idea_represent_node`

- Preferred role: `content`
- Cue keywords: `its, central, idea, represent, node, decisions, small, number, retention, intervals`
- Narration: Its central idea is to represent each node's decisions as a small number of retention intervals, defined by the start and end event of the tensor's lifetime, which reduces the count of discrete variables from quadratic to linear in the number of nodes.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_its_central_idea_represent_node" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, central, idea, represent, node, decisions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_top_authors_show_how_encode`

- Preferred role: `method`
- Cue keywords: `top, authors, show, how, encode, nonlinear, memory, precedence, constraints, standard`
- Narration: On top of this, the authors show how to encode the nonlinear memory and precedence constraints using standard CP building blocks, the cumulative and reservoir constraints, and they add an optional variant that enforces an input topological ordering to further reduce the search space.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_top_authors_show_how_encode" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords top, authors, show, how, encode, nonlinear in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_payoff_order_of_magnitude_speedup_ov`

- Preferred role: `content`
- Cue keywords: `payoff, order-of-magnitude, speedup, over, prior, work, large, graphs`
- Narration: The payoff is up to an order-of-magnitude speedup over prior work on large graphs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_payoff_order_of_magnitude_speedup_ov" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords payoff, order-of-magnitude, speedup, over, prior, work in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_moccasin_represents_schedule_retenti`

- Preferred role: `method`
- Cue keywords: `moccasin, represents, schedule, retention, intervals, node, graph, method, allows, small`
- Narration: Moccasin represents the schedule with retention intervals. For each node in the graph, the method allows up to a small constant number of intervals, each specified by an integer start event and an integer end event, indicating when that node's output tensor is computed and how long it stays in memory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_moccasin_represents_schedule_retenti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords moccasin, represents, schedule, retention, intervals, node in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_boolean_flag_marks_whether_interval`

- Preferred role: `content`
- Cue keywords: `boolean, flag, marks, whether, interval, actually, active, node, need, not`
- Narration: A Boolean flag marks whether each interval is actually active, so a node need not be recomputed a fixed number of times. The objective minimizes the total duration, a weighted sum over the active compute events where the weights are node execution times.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_boolean_flag_marks_whether_interval" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords boolean, flag, marks, whether, interval, actually in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_memory_budget_enforced_through_const`

- Preferred role: `method`
- Cue keywords: `memory, budget, enforced, through, constraint, programming, cumulative, constraint, treating, tensor`
- Narration: The memory budget is enforced through the constraint programming cumulative constraint, treating tensor sizes as resource demands and the budget as capacity, while data dependencies between predecessors and successors are handled with the reservoir constraint.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_memory_budget_enforced_through_const" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords memory, budget, enforced, through, constraint, programming in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_whole_handed_google_or_tools_cp_sat`

- Preferred role: `content`
- Cue keywords: `whole, handed, google, or-tools, cp-sat, solver, because, node, only, small`
- Narration: The whole model is handed to Google OR-Tools' CP-SAT solver. Because each node uses only a small constant number of intervals, the total number of integer variables stays linear in the graph size.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_whole_handed_google_or_tools_cp_sat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords whole, handed, google, or-tools, cp-sat, solver in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_evaluation_range_compute_graphs_main`

- Preferred role: `result`
- Cue keywords: `evaluation, range, compute, graphs, main, scaling, study, four, random, layered`
- Narration: The evaluation uses a range of compute graphs. The main scaling study is on four random layered graphs, G1 through G4, whose sizes grow from one hundred nodes and a couple hundred edges up to one thousand nodes and nearly six thousand edges.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_evaluation_range_compute_graphs_main" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, range, compute, graphs, main, scaling in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_also_real_world_compute_graph_four`

- Preferred role: `content`
- Cue keywords: `also, real-world, compute, graph, four, hundred, forty-two, nodes, over, twelve`
- Narration: There is also a real-world compute graph with four hundred forty-two nodes and over twelve hundred edges used for the headline comparison.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_also_real_world_compute_graph_four" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, real-world, compute, graph, four, hundred in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_every_graph_memory_budget_set`

- Preferred role: `content`
- Cue keywords: `every, graph, memory, budget, set, eighty, ninety, percent, peak, memory`
- Narration: For every graph the memory budget is set to eighty and ninety percent of the peak memory of the initial schedule without rematerialization, so the solver is forced to actually recompute tensors.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_every_graph_memory_budget_set" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, graph, memory, budget, set, eighty in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_all_experiments_run_sixteen_core_wor`

- Preferred role: `content`
- Cue keywords: `all, experiments, run, sixteen-core, workstation, thirty-two, gigabytes, ram`
- Narration: All experiments run on a sixteen-core workstation with thirty-two gigabytes of RAM.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_all_experiments_run_sixteen_core_wor" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords all, experiments, run, sixteen-core, workstation, thirty-two in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_across_board_moccasin_solves_remater`

- Preferred role: `content`
- Cue keywords: `across, board, moccasin, solves, rematerialization, problem, substantially, faster, checkmate, order`
- Narration: Across the board, Moccasin solves the rematerialization problem substantially faster than Checkmate, up to an order of magnitude on the larger graphs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_across_board_moccasin_solves_remater" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, board, moccasin, solves, rematerialization, problem in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_smallest_graph_two_comparable_but`

- Preferred role: `content`
- Cue keywords: `smallest, graph, two, comparable, but, gap, widens, quickly`
- Narration: On the smallest graph the two are comparable, but the gap widens quickly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_smallest_graph_two_comparable_but" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords smallest, graph, two, comparable, but, gap in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_graph_two_hundred_fifty_nodes`

- Preferred role: `content`
- Cue keywords: `graph, two, hundred, fifty, nodes, tight, memory, budget, checkmate, fails`
- Narration: For the graph with two hundred fifty nodes and a tight memory budget, Checkmate fails to find any feasible solution within thirty minutes, and at the loosest budget it takes ten minutes, while Moccasin finishes in seconds.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_graph_two_hundred_fifty_nodes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords graph, two, hundred, fifty, nodes, tight in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_five_hundred_one_thousand_node`

- Preferred role: `result`
- Cue keywords: `five, hundred, one, thousand, node, graphs, checkmate, times, out, entirely`
- Narration: For the five hundred and one thousand node graphs, Checkmate times out entirely, finding no solution even given three hours, and it exits with an out-of-memory error, whereas Moccasin converges to a good, low-duration-increase solution in under an hour.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_five_hundred_one_thousand_node" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords five, hundred, one, thousand, node, graphs in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_studies_few_key_knobs`

- Preferred role: `content`
- Cue keywords: `studies, few, key, knobs`
- Narration: The paper studies a few key knobs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_studies_few_key_knobs" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords studies, few, key, knobs in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_most_important_optional_topological`

- Preferred role: `method`
- Cue keywords: `most, important, optional, topological-ordering, restriction, enforcing, input, ordering, enlarges, variable`
- Narration: The most important is the optional topological-ordering restriction: enforcing an input ordering enlarges the variable domain slightly but shrinks the overall search space, reducing solve time compared to the fully unrestricted formulation.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_most_important_optional_topological" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords most, important, optional, topological-ordering, restriction, enforcing in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_per_node_interval_budget_called_fixe`

- Preferred role: `figure`
- Cue keywords: `per-node, interval, budget, called, fixed, two, throughout, experiments, which, authors`
- Narration: The per-node interval budget, called C, is fixed at two throughout the experiments, which the authors note in every plot legend.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c3_per_node_interval_budget_called_fixe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords per-node, interval, budget, called, fixed, two in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_complexity_table_makes_contrast_conc`

- Preferred role: `content`
- Cue keywords: `complexity, table, makes, contrast, concrete, checkmate, boolean, variable, count, grows`
- Narration: The complexity table makes the contrast concrete: Checkmate's Boolean variable count grows quadratically in the number of nodes plus a node-edge term, while Moccasin's integer variable count grows only linearly in the number of nodes, with a constant factor C.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_complexity_table_makes_contrast_conc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords complexity, table, makes, contrast, concrete, checkmate in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact_moccasin`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact, moccasin, needs, only, linear, number, integer`
- Narration: A few numbers capture the impact. Moccasin needs only a linear number of integer variables in the graph size, compared to a quadratic number of Boolean variables for the prior state of the art.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact_moccasin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact, moccasin, needs in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_translates_solve_times_order_magnitu`

- Preferred role: `content`
- Cue keywords: `translates, solve, times, order, magnitude, roughly, ten, times, faster, large`
- Narration: This translates into solve times up to an order of magnitude, roughly ten times, faster on large graphs.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_translates_solve_times_order_magnitu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords translates, solve, times, order, magnitude, roughly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_solutions_finds_high_quality_total`

- Preferred role: `content`
- Cue keywords: `solutions, finds, high, quality, total, duration, increase, rematerialization, stays, consistently`
- Narration: And the solutions it finds are high quality: the total duration increase from rematerialization stays consistently below five percent.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_solutions_finds_high_quality_total" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords solutions, finds, high, quality, total, duration in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_crucially_moccasin_scales_graphs_one`

- Preferred role: `method`
- Cue keywords: `crucially, moccasin, scales, graphs, one, thousand, nodes, nearly, six, thousand`
- Narration: Crucially, Moccasin scales to graphs with up to one thousand nodes and nearly six thousand edges, a regime where the competing method simply times out or runs out of memory.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c4_crucially_moccasin_scales_graphs_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, moccasin, scales, graphs, one, thousand in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_takeaway_right_problem_formu`

- Preferred role: `takeaway`
- Cue keywords: `lasting, takeaway, right, problem, formulation, changes, what, tractable`
- Narration: The lasting takeaway is that the right problem formulation changes what is tractable.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_lasting_takeaway_right_problem_formu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, takeaway, right, problem, formulation, changes in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_expressing_rematerialization_decisio`

- Preferred role: `method`
- Cue keywords: `expressing, rematerialization, decisions, small, set, retention, intervals, constraint, program, moccasin`
- Narration: By expressing rematerialization decisions as a small set of retention intervals in a constraint program, Moccasin reduces the number of discrete variables from quadratic to linear in the graph size.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_expressing_rematerialization_decisio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords expressing, rematerialization, decisions, small, set, retention in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_single_change_lets_scale_compute`

- Preferred role: `method`
- Cue keywords: `single, change, lets, scale, compute, graphs, far, larger, prior, methods`
- Narration: That single change lets it scale to compute graphs far larger than prior methods could handle, solving them up to ten times faster while keeping the added runtime overhead under five percent.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_single_change_lets_scale_compute" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords single, change, lets, scale, compute, graphs in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_because_output_just_execution_sequen`

- Preferred role: `result`
- Cue keywords: `because, output, just, execution, sequence, resulting, schedule, run, any, cpu`
- Narration: And because the output is just an execution sequence, the resulting schedule can run on any CPU or GPU.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c4_because_output_just_execution_sequen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, output, just, execution, sequence, resulting in title/desc so the matcher can verify semantic overlap.
