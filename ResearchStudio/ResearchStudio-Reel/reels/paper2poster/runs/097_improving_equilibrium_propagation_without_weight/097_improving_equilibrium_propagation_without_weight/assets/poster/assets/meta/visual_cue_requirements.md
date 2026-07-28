# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_equilibrium_propagation_promising_en`

- Preferred role: `method`
- Cue keywords: `equilibrium, propagation, promising, energy-based, alternative, backpropagation, neural, networks, brains, neuromorphic`
- Narration: Equilibrium propagation is a promising energy-based alternative to backpropagation for training neural networks on brains or neuromorphic hardware, but it classically demands two things physical substrates cannot easily deliver: perfectly symmetric weights and infinitesimally small nudges.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_equilibrium_propagation_promising_en" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords equilibrium, propagation, promising, energy-based, alternative, backpropagation in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_iclr_2024_friedrich_miescher_institu`

- Preferred role: `result`
- Cue keywords: `iclr, 2024, friedrich, miescher, institute, university, basel, axel, laborieux, friedemann`
- Narration: This ICLR 2024 paper from the Friedrich Miescher Institute and the University of Basel, by Axel Laborieux and Friedemann Zenke, cleanly separates the two resulting sources of gradient bias and shows how to remove them.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c2_iclr_2024_friedrich_miescher_institu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords iclr, 2024, friedrich, miescher, institute, university in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_finite_nudge_bias_eliminated_exactly`

- Preferred role: `figure`
- Cue keywords: `finite-nudge, bias, eliminated, exactly, cauchy, integral, while, weight-asymmetry, bias, tamed`
- Narration: Finite-nudge bias is eliminated exactly with a Cauchy integral, while weight-asymmetry bias is tamed by a new homeostatic loss that penalizes asymmetry of the Jacobian rather than the weights.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c3_finite_nudge_bias_eliminated_exactly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finite-nudge, bias, eliminated, exactly, cauchy, integral in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_payoff_first_time_equilibrium_propag`

- Preferred role: `result`
- Cue keywords: `payoff, first, time, equilibrium, propagation, trains, asymmetric, networks, imagenet, 32`
- Narration: The payoff: for the first time, equilibrium propagation trains asymmetric networks on ImageNet 32 by 32 with only a small gap to the ideal symmetric case.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s01_c4_payoff_first_time_equilibrium_propag" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords payoff, first, time, equilibrium, propagation, trains in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_equilibrium_propagation_appealing_wa`

- Preferred role: `method`
- Cue keywords: `equilibrium, propagation, appealing, way, train, neural, networks, directly, physical, substrates`
- Narration: Equilibrium propagation, or EP, is an appealing way to train neural networks directly on physical substrates like brains or analog chips, because it computes gradients using only the network's own relaxation dynamics.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_equilibrium_propagation_appealing_wa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords equilibrium, propagation, appealing, way, train, neural in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_comes_two_strict_requirements`

- Preferred role: `method`
- Cue keywords: `but, comes, two, strict, requirements, weights, must, perfectly, symmetric, nudge`
- Narration: But it comes with two strict requirements: the weights must be perfectly symmetric, and the nudge that pushes the network toward its target must be infinitesimally small.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_but_comes_two_strict_requirements" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, comes, two, strict, requirements, weights in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_both_very_hard_satisfy_real`

- Preferred role: `content`
- Cue keywords: `both, very, hard, satisfy, real, physical, hardware`
- Narration: Both are very hard to satisfy in real physical hardware.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_both_very_hard_satisfy_real" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords both, very, hard, satisfy, real, physical in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_crucially_whether_weight_asymmetry_a`

- Preferred role: `result`
- Cue keywords: `crucially, whether, weight, asymmetry, actually, harms, learning, had, never, been`
- Narration: And crucially, whether weight asymmetry actually harms learning had never been pinned down, because in practice its effect gets tangled up with the error introduced by using a finite nudge.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c4_crucially_whether_weight_asymmetry_a" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, whether, weight, asymmetry, actually, harms in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_reason_matters_energy_physical_neura`

- Preferred role: `content`
- Cue keywords: `reason, matters, energy, physical, neural, systems, whether, biological, brains, neuromorphic`
- Narration: The reason this matters is energy. Physical neural systems, whether biological brains or neuromorphic chips, could train networks at a tiny fraction of the energy cost of digital hardware.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_reason_matters_energy_physical_neura" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reason, matters, energy, physical, neural, systems in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_backpropagation_workhorse_deep_l`

- Preferred role: `method`
- Cue keywords: `but, backpropagation, workhorse, deep, learning, needs, separate, linear, backward, pass`
- Narration: But backpropagation, the workhorse of deep learning, needs a separate linear backward pass and the exact transpose of every weight matrix, neither of which physical substrates provide naturally.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_but_backpropagation_workhorse_deep_l" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, backpropagation, workhorse, deep, learning, needs in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_sidesteps_yet_its_own_symmetry`

- Preferred role: `content`
- Cue keywords: `sidesteps, yet, its, own, symmetry, assumption, nearly, demanding`
- Narration: EP sidesteps this, yet its own symmetry assumption is nearly as demanding.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_sidesteps_yet_its_own_symmetry" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sidesteps, yet, its, own, symmetry, assumption in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_warning_sign_asymmetric_version_had`

- Preferred role: `result`
- Cue keywords: `warning, sign, asymmetric, version, had, only, ever, worked, toy, tasks`
- Narration: And there was a warning sign: the asymmetric version of EP had only ever worked on toy tasks like MNIST and outright failed on CIFAR-10. Nobody had explained why.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c4_warning_sign_asymmetric_version_had" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords warning, sign, asymmetric, version, had, only in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_four_contributions_first_analy`

- Preferred role: `content`
- Cue keywords: `makes, four, contributions, first, analytically, separates, two, sources, bias, generalized`
- Narration: This paper makes four contributions. First, it analytically separates the two sources of bias in generalized EP: the finite nudge and the asymmetry of the network's Jacobian.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_four_contributions_first_analy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, four, contributions, first, analytically, separates in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_extends_holomorphic_asymmetri`

- Preferred role: `result`
- Cue keywords: `second, extends, holomorphic, asymmetric, complex-differentiable, systems, exact, error, recovered, even`
- Narration: Second, it extends holomorphic EP to asymmetric, complex-differentiable systems, so the exact error can be recovered even without weight symmetry.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_second_extends_holomorphic_asymmetri" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, extends, holomorphic, asymmetric, complex-differentiable, systems in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_most_practically_introduces_ne`

- Preferred role: `figure`
- Cue keywords: `third, most, practically, introduces, new, homeostatic, loss, reduces, asymmetry, jacobian`
- Narration: Third, and most practically, it introduces a new homeostatic loss that reduces the asymmetry of the Jacobian directly, rather than forcing the weights themselves to be symmetric.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s04_c3_third_most_practically_introduces_ne" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, most, practically, introduces, new, homeostatic in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_fourth_demonstrates_loss_finally_sca`

- Preferred role: `method`
- Cue keywords: `fourth, demonstrates, loss, finally, scales, all, way, imagenet, thirty-two, thirty-two`
- Narration: And fourth, it demonstrates that with this loss, EP finally scales all the way up to ImageNet at thirty-two by thirty-two resolution.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_fourth_demonstrates_loss_finally_sca" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, demonstrates, loss, finally, scales, all in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_two_parts_kill_finite_nudge`

- Preferred role: `method`
- Cue keywords: `method, two, parts, kill, finite-nudge, bias, authors, build, holomorphic, they`
- Narration: The method has two parts. To kill the finite-nudge bias, the authors build on holomorphic EP: they drive the network with an oscillating teaching signal and use a Cauchy integral from complex analysis to recover the exact error vector, no matter how large the nudge and even when the Jacobian is asymmetric.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_two_parts_kill_finite_nudge" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, two, parts, kill, finite-nudge, bias in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_better_still_estimated_continuously`

- Preferred role: `content`
- Cue keywords: `better, still, estimated, continuously, over, many, oscillation, cycles, removing, need`
- Narration: Better still, this can be estimated continuously over many oscillation cycles, removing the need for separate free and nudged phases.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_better_still_estimated_continuously" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords better, still, estimated, continuously, over, many in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_tackle_second_bias_they_show`

- Preferred role: `figure`
- Cue keywords: `tackle, second, bias, they, show, grows, skew-symmetric, part, jacobian, introduce`
- Narration: To tackle the second bias, they show it grows with the skew-symmetric part of the Jacobian, and introduce a homeostatic loss that penalizes exactly that part, estimated efficiently with the Hutchinson trace trick.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c3_tackle_second_bias_they_show" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tackle, second, bias, they, show, grows in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_key_insight_improves_functional_symm`

- Preferred role: `content`
- Cue keywords: `key, insight, improves, functional, symmetry, jacobian, without, ever, forcing, weights`
- Narration: The key insight is that this improves functional symmetry of the Jacobian without ever forcing the weights to be symmetric.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_key_insight_improves_functional_symm" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, insight, improves, functional, symmetry, jacobian in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_span_four_datasets_incre`

- Preferred role: `content`
- Cue keywords: `experiments, span, four, datasets, increasing, difficulty`
- Narration: The experiments span four datasets of increasing difficulty.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_span_four_datasets_incre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, span, four, datasets, increasing, difficulty in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_fashion_mnist_small_multilayer_netwo`

- Preferred role: `content`
- Cue keywords: `fashion, mnist, small, multilayer, networks, used, cleanly, isolate, measure, source`
- Narration: On Fashion MNIST, small multilayer networks are used to cleanly isolate and measure each source of bias.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c2_fashion_mnist_small_multilayer_netwo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fashion, mnist, small, multilayer, networks, used in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_recurrent_convolutional_architecture`

- Preferred role: `method`
- Cue keywords: `recurrent, convolutional, architecture, genuinely, asymmetric, feedback, weights, trained, cifar-10, cifar-100`
- Narration: Then a recurrent convolutional architecture with genuinely asymmetric feedback weights is trained on CIFAR-10, CIFAR-100, and finally ImageNet at thirty-two by thirty-two, which is where the homeostatic loss really earns its keep.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_recurrent_convolutional_architecture" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords recurrent, convolutional, architecture, genuinely, asymmetric, feedback in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_authors_also_confirm_appendix_same`

- Preferred role: `figure`
- Cue keywords: `authors, also, confirm, appendix, same, loss, helps, predictive, coding, networks`
- Narration: The authors also confirm in the appendix that the same loss helps predictive coding networks, which have no reciprocal connections at all.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c4_authors_also_confirm_appendix_same" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, also, confirm, appendix, same, loss in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_result_striking_cifar_10_as`

- Preferred role: `method`
- Cue keywords: `headline, result, striking, cifar-10, asymmetric, network, trained, but, without, homeostatic`
- Narration: The headline result is striking. On CIFAR-10, the asymmetric network trained with EP but without the homeostatic loss reaches only sixty point four percent accuracy.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_headline_result_striking_cifar_10_as" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, result, striking, cifar-10, asymmetric, network in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_add_homeostatic_loss_accuracy_jumps`

- Preferred role: `result`
- Cue keywords: `add, homeostatic, loss, accuracy, jumps, eighty-four, point, three, percent, just`
- Narration: Add the homeostatic loss, and accuracy jumps to eighty-four point three percent, just four point three points shy of the fully symmetric architecture, and all with only approximate weight symmetry.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c2_add_homeostatic_loss_accuracy_jumps" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords add, homeostatic, loss, accuracy, jumps, eighty-four in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_even_more_importantly_first_time`

- Preferred role: `method`
- Cue keywords: `even, more, importantly, first, time, family, methods, trains, all, imagenet`
- Narration: Even more importantly, this is the first time this family of methods trains at all on ImageNet thirty-two by thirty-two, reaching thirty-one point four percent Top-1 and fifty-five point two percent Top-5.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_even_more_importantly_first_time" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords even, more, importantly, first, time, family in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_throughout_homeostatic_loss_steadily`

- Preferred role: `method`
- Cue keywords: `throughout, homeostatic, loss, steadily, raises, jacobian, symmetry, tightens, alignment, between`
- Narration: Throughout training, the homeostatic loss steadily raises the Jacobian's symmetry and tightens the alignment between EP's error signals and true backprop.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_throughout_homeostatic_loss_steadily" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords throughout, homeostatic, loss, steadily, raises, jacobian in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_ablations_cleanly_separate_two_biase`

- Preferred role: `result`
- Cue keywords: `ablations, cleanly, separate, two, biases, fashion, mnist, when, nudge, made`
- Narration: The ablations cleanly separate the two biases. On Fashion MNIST, when the nudge is made large, classic one-sided EP falls apart, its error ballooning to thirty-eight point four percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_ablations_cleanly_separate_two_biase" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, cleanly, separate, two, biases, fashion in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_holomorphic_cauchy_integral_estimate`

- Preferred role: `content`
- Cue keywords: `holomorphic, cauchy-integral, estimate, six, points, instead, stays, fourteen, point, three`
- Narration: The holomorphic Cauchy-integral estimate with six points instead stays at fourteen point three percent, essentially matching the true derivative at fourteen point seven percent, proof that finite-nudge bias is fully removed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_holomorphic_cauchy_integral_estimate" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords holomorphic, cauchy-integral, estimate, six, points, instead in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_separately_dropping_exact_derivative`

- Preferred role: `method`
- Cue keywords: `separately, dropping, exact, derivative, coarse, two-point, estimate, costs, about, three`
- Narration: Separately, dropping from the exact derivative to a coarse two-point estimate costs about three points on CIFAR-10, quantifying the residual nudge bias.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_separately_dropping_exact_derivative" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords separately, dropping, exact, derivative, coarse, two-point in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_architecture_whose_output_feeds_stra`

- Preferred role: `method`
- Cue keywords: `architecture, whose, output, feeds, straight, back, first, layer, reciprocal, connections`
- Narration: And an architecture whose output feeds straight back to the first layer, with no reciprocal connections, benefits just as much, confirming the loss targets functional symmetry rather than weight symmetry.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_architecture_whose_output_feeds_stra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords architecture, whose, output, feeds, straight, back in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_put_numbers_one_place_cifar_10`

- Preferred role: `result`
- Cue keywords: `put, numbers, one, place, cifar-10, homeostatic, loss, lifts, asymmetric, sixty`
- Narration: To put the numbers in one place: on CIFAR-10, the homeostatic loss lifts asymmetric EP from sixty point four to eighty-four point three percent accuracy, closing the gap to the symmetric network to just four point three points.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_put_numbers_one_place_cifar_10" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords put, numbers, one, place, cifar-10, homeostatic in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_imagenet_thirty_two_thirty_two_reach`

- Preferred role: `result`
- Cue keywords: `imagenet, thirty-two, thirty-two, reaches, thirty-one, point, four, percent, top-1, fifty-five`
- Narration: On ImageNet thirty-two by thirty-two, EP reaches thirty-one point four percent Top-1 and fifty-five point two percent Top-5, the first result of its kind.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_imagenet_thirty_two_thirty_two_reach" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords imagenet, thirty-two, thirty-two, reaches, thirty-one, point in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_fashion_mnist_large_nudge_exact`

- Preferred role: `result`
- Cue keywords: `fashion, mnist, large, nudge, exact, holomorphic, estimate, cuts, error, thirty-eight`
- Narration: And on Fashion MNIST, using a large nudge, the exact holomorphic estimate cuts error from thirty-eight point four percent down to fourteen point three percent.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_fashion_mnist_large_nudge_exact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fashion, mnist, large, nudge, exact, holomorphic in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_equilibrium_propagation_doe`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, equilibrium, propagation, does, not, actually, need, perfectly, symmetric, weights`
- Narration: The takeaway is that equilibrium propagation does not actually need perfectly symmetric weights.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_equilibrium_propagation_doe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, equilibrium, propagation, does, not, actually in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_removing_finite_nudge_bias_exactly_c`

- Preferred role: `result`
- Cue keywords: `removing, finite-nudge, bias, exactly, cauchy, integral, encouraging, functional, symmetry, jacobian`
- Narration: By removing finite-nudge bias exactly with a Cauchy integral, and by encouraging functional symmetry of the Jacobian with a homeostatic loss instead of the weights, asymmetric networks can finally scale to ImageNet-level tasks with only a small gap to the ideal case.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s10_c2_removing_finite_nudge_bias_exactly_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords removing, finite-nudge, bias, exactly, cauchy, integral in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_because_functional_symmetry_weaker_m`

- Preferred role: `method`
- Cue keywords: `because, functional, symmetry, weaker, more, achievable, condition, weight, symmetry, opens`
- Narration: Because functional symmetry is a weaker, more achievable condition than weight symmetry, this opens a biologically plausible path to training real physical neural substrates, and hints that brains might rely on similar homeostatic mechanisms.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_because_functional_symmetry_weaker_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, functional, symmetry, weaker, more, achievable in title/desc so the matcher can verify semantic overlap.
