# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_how_living_systems_learn_much`

- Preferred role: `method`
- Cue keywords: `how, living, systems, learn, much, little, adapting, sparse, minimal, energy`
- Narration: How do living systems learn so much from so little, adapting with sparse data and minimal energy while artificial deep networks demand massive datasets and constant retraining?
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_how_living_systems_learn_much" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords how, living, systems, learn, much, little in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_work_aisha_belhadi_okinawa_institute`

- Preferred role: `title`
- Cue keywords: `work, aisha, belhadi, okinawa, institute, science, technology, looks, biology, answers`
- Narration: This work by Aisha Belhadi at the Okinawa Institute of Science and Technology looks to biology for answers.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c2_work_aisha_belhadi_okinawa_institute" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, aisha, belhadi, okinawa, institute, science in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_distills_three_mechanisms_biological`

- Preferred role: `content`
- Cue keywords: `distills, three, mechanisms, biological, adaptation, metaplasticity, homeostasis, inhibition, proposes, concrete`
- Narration: It distills three mechanisms of biological adaptation — metaplasticity, homeostasis, and inhibition — and proposes concrete ways to fold them into the Hopfield-network self-optimization model, aiming for deep learning tools that learn the way living systems do.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_distills_three_mechanisms_biological" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords distills, three, mechanisms, biological, adaptation, metaplasticity in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_large_part_recent_progress_comes`

- Preferred role: `method`
- Cue keywords: `large, part, recent, progress, comes, deep, learning, paired, big, trained`
- Narration: A large part of recent AI progress comes from deep learning paired with big data, trained by supervised or reinforcement signals.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_large_part_recent_progress_comes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords large, part, recent, progress, comes, deep in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_these_systems_powerful_but_they`

- Preferred role: `method`
- Cue keywords: `these, systems, powerful, but, they, behave, very, differently, living, systems`
- Narration: These systems are powerful, but they behave very differently from living systems, which learn, make associations, and adapt using sparse data, efficient energy use, and few training iterations.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_these_systems_powerful_but_they" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, systems, powerful, but, they, behave in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_they_also_forget_previous_tasks`

- Preferred role: `method`
- Cue keywords: `they, also, forget, previous, tasks, when, trained, sequentially, problem, known`
- Narration: They also forget previous tasks when trained sequentially, a problem known as catastrophic forgetting.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_they_also_forget_previous_tasks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, also, forget, previous, tasks, when in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_hopfield_networks_unsupervised_learn`

- Preferred role: `content`
- Cue keywords: `hopfield, networks, unsupervised, learning, associative, memory, offer, more, biologically, plausible`
- Narration: Hopfield networks, with unsupervised learning and an associative memory, offer a more biologically plausible alternative, but their simplest forms are limited, storing only about zero point one four times the number of nodes in patterns, and rarely exploit the biological mechanisms that inspired them.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_hopfield_networks_unsupervised_learn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords hopfield, networks, unsupervised, learning, associative, memory in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_adapt_uncertain_changing_world_compl`

- Preferred role: `content`
- Cue keywords: `adapt, uncertain, changing, world, complex, systems, must, integrate, new, information`
- Narration: To adapt in an uncertain, changing world, complex systems must integrate new information while maintaining stability.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_adapt_uncertain_changing_world_compl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords adapt, uncertain, changing, world, complex, systems in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_too_much_destabilization_prevents_co`

- Preferred role: `content`
- Cue keywords: `too, much, destabilization, prevents, consistent, learning, too, much, reliance, past`
- Narration: Too much destabilization prevents consistent learning; too much reliance on past memory locks in outdated patterns.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_too_much_destabilization_prevents_co" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords too, much, destabilization, prevents, consistent, learning in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_biology_solves_interplay_mechanisms`

- Preferred role: `content`
- Cue keywords: `biology, solves, interplay, mechanisms, metaplasticity, tunes, how, much, synapses, change`
- Narration: Biology solves this with an interplay of mechanisms — metaplasticity that tunes how much synapses change, homeostasis that regulates the system around a set point, inhibition, and resets that enable forgetting.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_biology_solves_interplay_mechanisms" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords biology, solves, interplay, mechanisms, metaplasticity, tunes in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_self_optimization_hopfield_network_h`

- Preferred role: `content`
- Cue keywords: `self-optimization, hopfield, network, hebbian, learning, periodic, resets, already, builds, memory`
- Narration: The self-optimization model is a Hopfield network with Hebbian learning and periodic resets that already builds a memory of visited attractors and enlarges the basin of the global energy minimum, making it a promising candidate to be enriched with more of these biological features.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_self_optimization_hopfield_network_h" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords self-optimization, hopfield, network, hebbian, learning, periodic in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_work_makes_two_linked_contributions`

- Preferred role: `content`
- Cue keywords: `work, makes, two, linked, contributions`
- Narration: This work makes two linked contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_work_makes_two_linked_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, makes, two, linked, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_distills_key_mechanisms_adapta`

- Preferred role: `content`
- Cue keywords: `first, distills, key, mechanisms, adaptation, biological, systems, special, focus, metaplasticity`
- Narration: First, it distills key mechanisms of adaptation in biological systems, with a special focus on metaplasticity and homeostatic regulation, plus inhibition and forgetting.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_distills_key_mechanisms_adapta" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, distills, key, mechanisms, adaptation, biological in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_proposes_concrete_avenues_inc`

- Preferred role: `method`
- Cue keywords: `second, proposes, concrete, avenues, incorporate, these, features, self-optimization, hopfield, networks`
- Narration: Second, it proposes concrete avenues to incorporate these features into the self-optimization model and Hopfield networks more broadly — by making the learning rate adaptive with respect to synaptic weights or the energy landscape, by enhancing modular structure, and by changing the activation rule.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_proposes_concrete_avenues_inc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, proposes, concrete, avenues, incorporate, these in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_aim_deep_learning_tools_recapitulate`

- Preferred role: `content`
- Cue keywords: `aim, deep, learning, tools, recapitulate, advantages, biological, systems, plausibly, living`
- Narration: The aim is deep learning tools that recapitulate the advantages of biological systems and can plausibly model living and adaptive systems across levels of complexity.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c4_aim_deep_learning_tools_recapitulate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords aim, deep, learning, tools, recapitulate, advantages in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_core_idea_raise_network_degrees`

- Preferred role: `content`
- Cue keywords: `core, idea, raise, network, degrees, freedom, without, adding, new, parameters`
- Narration: The core idea is to raise the network's degrees of freedom without adding new parameters, by letting existing components do more work, as biology does.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_core_idea_raise_network_degrees" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, idea, raise, network, degrees, freedom in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_local_metaplasticity_learning_rate_a`

- Preferred role: `content`
- Cue keywords: `local, metaplasticity, learning, rate, alpha, longer, user-defined, constant, but, function`
- Narration: For local metaplasticity, the learning rate alpha is no longer a user-defined constant but a function of the connection weight between two nodes, so the Hebbian update becomes weight-dependent: the change in a weight equals a function of that weight times the product of the two node states.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_local_metaplasticity_learning_rate_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords local, metaplasticity, learning, rate, alpha, longer in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_potentiate_co_activated_synapses_fas`

- Preferred role: `content`
- Cue keywords: `potentiate, co-activated, synapses, faster, depress, opposing, ones, more, slowly, network-level`
- Narration: This can potentiate co-activated synapses faster and depress opposing ones more slowly. For network-level metaplasticity, alpha is instead tied to the change in the network's energy, so learning slows in shallow parts of the energy landscape and speeds up on steeper slopes, helping avoid local minima.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_potentiate_co_activated_synapses_fas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords potentiate, co-activated, synapses, faster, depress, opposing in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_homeostasis_approximated_oscillatory`

- Preferred role: `method`
- Cue keywords: `homeostasis, approximated, oscillatory, activation, functions, such, trigonometric, ones, adaptivity, further`
- Narration: Homeostasis is approximated by oscillatory activation functions, such as trigonometric ones, and adaptivity is further supported by modular structure, where modules that consistently strengthen their internal connections receive an automatic boost, and inter-module inhibition regulates overall energy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_homeostasis_approximated_oscillatory" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords homeostasis, approximated, oscillatory, activation, functions, such in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_conceptual_position_piece_rather_emp`

- Preferred role: `result`
- Cue keywords: `conceptual, position, piece, rather, empirical, study, does, not, introduce, dataset`
- Narration: This paper is a conceptual and position piece rather than an empirical study, so it does not introduce a dataset or run benchmarks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_conceptual_position_piece_rather_emp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords conceptual, position, piece, rather, empirical, study in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_instead_builds_existing_computationa`

- Preferred role: `content`
- Cue keywords: `instead, builds, existing, computational, work, self-optimization, including`
- Narration: Instead, it builds on existing computational work with the self-optimization model — including a model of the C.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_instead_builds_existing_computationa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, builds, existing, computational, work, self-optimization in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_elegans_connectome_used_inhibitory_i`

- Preferred role: `content`
- Cue keywords: `elegans, connectome, used, inhibitory, inter-cluster, connections, models, solve, combinatorial, satisfiability`
- Narration: elegans connectome that used inhibitory inter-cluster connections, and SO models that solve combinatorial satisfiability problems.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c3_elegans_connectome_used_inhibitory_i" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords elegans, connectome, used, inhibitory, inter-cluster, connections in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_these_prior_systems_define_setting`

- Preferred role: `content`
- Cue keywords: `these, prior, systems, define, setting, which, proposed, biological, mechanisms, would`
- Narration: These prior systems define the setting in which the proposed biological mechanisms would eventually be implemented and evaluated.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_these_prior_systems_define_setting" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, prior, systems, define, setting, which in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_because_proposal_its_main_result`

- Preferred role: `result`
- Cue keywords: `because, proposal, its, main, result, conceptual, rather, numerical`
- Narration: Because this is a proposal paper, its main result is conceptual rather than numerical.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_because_proposal_its_main_result" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, proposal, its, main, result, conceptual in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_delivers_unified_framework_showing_h`

- Preferred role: `guidance`
- Cue keywords: `delivers, unified, framework, showing, how, metaplasticity, homeostasis, inhibition, forgetting, map`
- Narration: It delivers a unified framework showing how metaplasticity, homeostasis, inhibition, and forgetting can each map onto specific changes in the self-optimization model — an adaptive learning rate driven by weights or energy, oscillatory activation functions, and adaptive modularity with inhibition.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s07_c2_delivers_unified_framework_showing_h" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords delivers, unified, framework, showing, how, metaplasticity in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_unifying_insight_constraints_degrees`

- Preferred role: `method`
- Cue keywords: `unifying, insight, constraints, degrees, freedom, not, opposition, network, architecture, provides`
- Narration: The unifying insight is that constraints and degrees of freedom are not in opposition: the network architecture provides the constraining framework, and within it, higher degrees of freedom can expand the space of adaptive behavior.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_unifying_insight_constraints_degrees" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unifying, insight, constraints, degrees, freedom, not in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_without_those_constraints_added_free`

- Preferred role: `method`
- Cue keywords: `without, those, constraints, added, freedom, would, simply, collapse, noise`
- Narration: Without those constraints, the added freedom would simply collapse into noise.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_without_those_constraints_added_free" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords without, those, constraints, added, freedom, would in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablation_experiments_work_since_trai`

- Preferred role: `method`
- Cue keywords: `ablation, experiments, work, since, trained`
- Narration: There are no ablation experiments in this work, since no model is trained.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_ablation_experiments_work_since_trai" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablation, experiments, work, since, trained in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_does_however_sketch_variations_futur`

- Preferred role: `content`
- Cue keywords: `does, however, sketch, variations, future, empirical, study, should, compare`
- Narration: The paper does, however, sketch the variations that a future empirical study should compare.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_does_however_sketch_variations_futur" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords does, however, sketch, variations, future, empirical in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_these_include_different_forms_functi`

- Preferred role: `content`
- Cue keywords: `these, include, different, forms, function, links, learning, rate, weights, energy`
- Narration: These include different forms of the function that links the learning rate to weights or to energy changes, ranging from simple linear approximations to more complex nonlinear ones, and different activation functions such as sigmoid, Heaviside threshold, and trigonometric functions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_these_include_different_forms_functi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, include, different, forms, function, links in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_author_suggests_these_variations_cou`

- Preferred role: `content`
- Cue keywords: `author, suggests, these, variations, could, reproduce, different, normal, pathological, behavioral`
- Narration: The author suggests these variations could reproduce different normal and pathological behavioral modes in biological systems, and are worth exploring systematically once the mechanisms are implemented.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_author_suggests_these_variations_cou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords author, suggests, these, variations, could, reproduce in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_one_quantitative_anchor_classic_capa`

- Preferred role: `content`
- Cue keywords: `one, quantitative, anchor, classic, capacity, limit, standard, hopfield, network, reliably`
- Narration: The one quantitative anchor in this paper is the classic capacity limit of a standard Hopfield network: it can reliably store only about zero point one four times the number of nodes in the network in distinct memory patterns.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_one_quantitative_anchor_classic_capa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, quantitative, anchor, classic, capacity, limit in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_ceiling_key_reason_looks_biological`

- Preferred role: `content`
- Cue keywords: `ceiling, key, reason, looks, biological, mechanisms, extend, network, capabilities`
- Narration: This ceiling is a key reason the paper looks to biological mechanisms to extend the network's capabilities.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_ceiling_key_reason_looks_biological" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ceiling, key, reason, looks, biological, mechanisms in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_beyond_figure_work_reports_experimen`

- Preferred role: `figure`
- Cue keywords: `beyond, figure, work, reports, experimental, numbers, because, conceptual, proposal, synthesizes`
- Narration: Beyond that figure, the work reports no experimental numbers, because it is a conceptual proposal that synthesizes ideas across neuroscience, molecular biology, and machine learning rather than measuring a system.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s09_c3_beyond_figure_work_reports_experimen" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords beyond, figure, work, reports, experimental, numbers in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_mechanisms_biology_adapt_me`

- Preferred role: `method`
- Cue keywords: `takeaway, mechanisms, biology, adapt, metaplasticity, homeostasis, inhibition, translated, machine, learning`
- Narration: The takeaway is that the mechanisms biology uses to adapt — metaplasticity, homeostasis, and inhibition — can be translated into machine learning by adjusting the learning rate according to synaptic weights or the system's energy, by enhancing modular structure, and by modifying the activation rule of a Hopfield-network self-optimization model.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_takeaway_mechanisms_biology_adapt_me" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, mechanisms, biology, adapt, metaplasticity, homeostasis in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_doing_could_yield_associative_memory`

- Preferred role: `content`
- Cue keywords: `doing, could, yield, associative-memory, systems, capable, complex, adaptive, learning, sparse`
- Narration: Doing so could yield associative-memory systems capable of complex adaptive learning from sparse data, closer to how living systems continually adjust and thrive.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c2_doing_could_yield_associative_memory" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords doing, could, yield, associative-memory, systems, capable in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_broader_message_constraints_flexibil`

- Preferred role: `method`
- Cue keywords: `broader, message, constraints, flexibility, work, together, right, constraints, let, increased`
- Narration: The broader message is that constraints and flexibility work together: the right constraints let increased degrees of freedom open up new adaptive possibilities instead of collapsing into noise.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_broader_message_constraints_flexibil" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords broader, message, constraints, flexibility, work, together in title/desc so the matcher can verify semantic overlap.
