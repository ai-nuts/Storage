# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_mechanistic_mode_connectivity_studie`

- Preferred role: `figure`
- Cue keywords: `mechanistic, mode, connectivity, studies, neural, network, loss, landscapes, through, lens`
- Narration: This paper, Mechanistic Mode Connectivity, studies neural network loss landscapes through the lens of mode connectivity.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c1_mechanistic_mode_connectivity_studie" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mechanistic, mode, connectivity, studies, neural, network in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_authors_ask_whether_minimizers_rely`

- Preferred role: `figure`
- Cue keywords: `authors, ask, whether, minimizers, rely, different, mechanisms, making, predictions, connected`
- Narration: The authors ask whether minimizers that rely on different mechanisms for making predictions are connected via simple paths of low loss.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s01_c2_authors_ask_whether_minimizers_rely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ask, whether, minimizers, rely, different in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_they_define_mechanistic_similarity_s`

- Preferred role: `content`
- Cue keywords: `they, define, mechanistic, similarity, shared, invariances, input, transformations, show, lack`
- Narration: They define mechanistic similarity as shared invariances to input transformations, and show that a lack of linear connectivity between two models implies they use dissimilar mechanisms.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_they_define_mechanistic_similarity_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, define, mechanistic, similarity, shared, invariances in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_building_insight_they_propose_connec`

- Preferred role: `method`
- Cue keywords: `building, insight, they, propose, connectivity-based, fine-tuning, method, deliberately, alter, mechanisms`
- Narration: Building on this insight, they propose connectivity-based fine-tuning, a method to deliberately alter a model's mechanisms and reduce its reliance on spurious attributes.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_building_insight_they_propose_connec" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords building, insight, they, propose, connectivity-based, fine-tuning in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_modern_deep_networks_infinitely_many`

- Preferred role: `figure`
- Cue keywords: `modern, deep, networks, infinitely, many, global, minimizers, mode-connectivity, literature, shows`
- Narration: Modern deep networks have infinitely many global minimizers, and the mode-connectivity literature shows these minimizers are joined by surprisingly simple, low-loss paths.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c1_modern_deep_networks_infinitely_many" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords modern, deep, networks, infinitely, many, global in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_literature_ignored_crucial_quest`

- Preferred role: `title`
- Cue keywords: `but, literature, ignored, crucial, question, what, mechanisms, connected, models, actually`
- Narration: But this literature has ignored a crucial question: what mechanisms do the connected models actually use?
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s02_c2_but_literature_ignored_crucial_quest" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, literature, ignored, crucial, question, what in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_two_models_both_reach_low`

- Preferred role: `figure`
- Cue keywords: `two, models, both, reach, low, loss, while, relying, entirely, different`
- Narration: Two models can both reach low loss while relying on entirely different attributes of the input, such as an object's background versus its shape.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c3_two_models_both_reach_low" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, models, both, reach, low, loss in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_argues_cannot_understand_loss_landsc`

- Preferred role: `figure`
- Cue keywords: `argues, cannot, understand, loss, landscapes, safely, fine-tune, models, without, accounting`
- Narration: The paper argues we cannot understand loss landscapes, or safely fine-tune models, without accounting for these prediction mechanisms.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s02_c4_argues_cannot_understand_loss_landsc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords argues, cannot, understand, loss, landscapes, safely in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_why_does_matter_now_practice`

- Preferred role: `method`
- Cue keywords: `why, does, matter, now, practice, constantly, fine-tune, pretrained, models, downstream`
- Narration: Why does this matter now? In practice we constantly fine-tune pretrained models on downstream data, assuming this fixes undesirable behavior.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_why_does_matter_now_practice" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords why, does, matter, now, practice, constantly in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_prior_work_shows_fine_tuned`

- Preferred role: `method`
- Cue keywords: `but, prior, work, shows, fine-tuned, models, often, remain, linearly, connected`
- Narration: But prior work shows fine-tuned models often remain linearly connected to their pretraining solution.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c2_but_prior_work_shows_fine_tuned" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, prior, work, shows, fine-tuned, models in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_linear_connectivity_tied_shared_mech`

- Preferred role: `content`
- Cue keywords: `linear, connectivity, tied, shared, mechanisms, naive, fine-tuning, clean, might, never`
- Narration: If linear connectivity is tied to shared mechanisms, then naive fine-tuning on clean data might never remove a model's reliance on spurious cues.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_linear_connectivity_tied_shared_mech" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords linear, connectivity, tied, shared, mechanisms, naive in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_understanding_relationship_between_c`

- Preferred role: `content`
- Cue keywords: `understanding, relationship, between, connectivity, mechanism, therefore, directly, relevant, robustness, safe`
- Narration: Understanding the relationship between connectivity and mechanism is therefore directly relevant to robustness and safe adaptation of models.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_understanding_relationship_between_c" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords understanding, relationship, between, connectivity, mechanism, therefore in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_makes_three_main_contributions`

- Preferred role: `content`
- Cue keywords: `makes, three, main, contributions`
- Narration: The paper makes three main contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_makes_three_main_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords makes, three, main, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_defines_mechanistic_similarity`

- Preferred role: `content`
- Cue keywords: `first, defines, mechanistic, similarity, two, models, mechanistically, similar, they, invariant`
- Narration: First, it defines mechanistic similarity: two models are mechanistically similar if they are invariant to the same set of unit interventions on the data-generating process.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c2_first_defines_mechanistic_similarity" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, defines, mechanistic, similarity, two, models in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_characterizes_connectivity_pr`

- Preferred role: `content`
- Cue keywords: `second, characterizes, connectivity, proving, two, models, lack, linear, connectivity, architectural`
- Narration: Second, it characterizes connectivity, proving that if two models lack linear connectivity up to architectural symmetries, they must be mechanistically dissimilar.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_second_characterizes_connectivity_pr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, characterizes, connectivity, proving, two, models in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_third_motivated_result_proposes_conn`

- Preferred role: `method`
- Cue keywords: `third, motivated, result, proposes, connectivity-based, fine-tuning, method, exploits, loss, barriers`
- Narration: Third, motivated by this result, it proposes Connectivity-Based Fine-Tuning, a method that exploits loss barriers to steer a model toward the mechanisms we actually want.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_third_motivated_result_proposes_conn" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, motivated, result, proposes, connectivity-based, fine-tuning in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_rests_defining_mechanistic_si`

- Preferred role: `method`
- Cue keywords: `method, rests, defining, mechanistic, similarity, through, invariance, interventions, data-generating, process`
- Narration: The method rests on defining mechanistic similarity through invariance to interventions on the data-generating process.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_rests_defining_mechanistic_si" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, rests, defining, mechanistic, similarity, through in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_authors_prove_loss_barrier_along`

- Preferred role: `figure`
- Cue keywords: `authors, prove, loss, barrier, along, linear, path, between, two, models`
- Narration: The authors then prove that a loss barrier along the linear path between two models implies the models are mechanistically dissimilar, they have learned different invariances. Connectivity-Based Fine-Tuning turns this into an algorithm.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c2_authors_prove_loss_barrier_along" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, prove, loss, barrier, along, linear in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_minimizes_three_terms_cross_entropy`

- Preferred role: `figure`
- Cue keywords: `minimizes, three, terms, cross-entropy, loss, small, cue-free, dataset, barrier, loss`
- Narration: It minimizes three terms: a cross-entropy loss on a small cue-free dataset, a barrier loss that deliberately raises loss along the linear path to the cue-relying solution up to an upper bound, and an invariance loss that aligns penultimate-layer representations across counterfactual versions of each class.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c3_minimizes_three_terms_cross_entropy" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords minimizes, three, terms, cross-entropy, loss, small in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_together_these_push_mechanistically`

- Preferred role: `content`
- Cue keywords: `together, these, push, mechanistically, dissimilar, cue-invariant, solution`
- Narration: Together these push the model to a mechanistically dissimilar, cue-invariant solution.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_together_these_push_mechanistically" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, these, push, mechanistically, dissimilar, cue-invariant in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_measure_mechanisms_quantitatively_au`

- Preferred role: `content`
- Cue keywords: `measure, mechanisms, quantitatively, authors, build, synthetic, datasets, embedding, easily, separable`
- Narration: To measure mechanisms quantitatively, the authors build synthetic datasets by embedding easily separable spurious cues into standard vision data.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_measure_mechanisms_quantitatively_au" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords measure, mechanisms, quantitatively, authors, build, synthetic in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_cifar_10_gets_small_box_cues`

- Preferred role: `result`
- Cue keywords: `cifar-10, gets, small, box, cues, placed, according, label, cifar-100, gets`
- Narration: CIFAR-10 gets small box cues placed according to the label, CIFAR-100 gets cues colored and positioned by label digits, and the Dominoes dataset stacks CIFAR-10 images with class-matched Fashion-MNIST images.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_cifar_10_gets_small_box_cues" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, gets, small, box, cues, placed in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_they_vary_fraction_cued_samples`

- Preferred role: `result`
- Cue keywords: `they, vary, fraction, cued, samples, sixty, one, hundred, percent, pair`
- Narration: They vary the fraction of cued samples from sixty to one hundred percent, and pair every dataset with counterfactual test sets that remove, keep, randomize, or scramble the cue.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_they_vary_fraction_cued_samples" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, vary, fraction, cued, samples, sixty in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_these_counterfactuals_reveal_exactly`

- Preferred role: `content`
- Cue keywords: `these, counterfactuals, reveal, exactly, how, much, leans, spurious, cue, versus`
- Narration: These counterfactuals reveal exactly how much a model leans on the spurious cue versus the natural image.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_these_counterfactuals_reveal_exactly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords these, counterfactuals, reveal, exactly, how, much in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_central_empirical_finding_validates`

- Preferred role: `takeaway`
- Cue keywords: `central, empirical, finding, validates, theory`
- Narration: The central empirical finding validates the theory.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s07_c1_central_empirical_finding_validates" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords central, empirical, finding, validates, theory in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_when_resnet_18_models_trained_withou`

- Preferred role: `method`
- Cue keywords: `when, resnet-18, models, trained, without, spurious, cues, they, mechanistically, dissimilar`
- Narration: When ResNet-18 models are trained with and without spurious cues, they are mechanistically dissimilar, and the paper shows they cannot be connected by a linear path, even after accounting for permutation symmetries.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_when_resnet_18_models_trained_withou" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, resnet-18, models, trained, without, spurious in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_however_quadratic_path_connects_them`

- Preferred role: `content`
- Cue keywords: `however, quadratic, path, connects, them, ease, confirms, linear, disconnection, reliable`
- Narration: However, a quadratic path connects them with ease. This confirms that linear disconnection is a reliable signal of differing mechanisms.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_however_quadratic_path_connects_them" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords however, quadratic, path, connects, them, ease in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_also_explains_why_naive_fine_tuning`

- Preferred role: `method`
- Cue keywords: `also, explains, why, naive, fine-tuning, fails, fine-tuned, models, stay, linearly`
- Narration: It also explains why naive fine-tuning fails: fine-tuned models stay linearly connected to their pretraining solution and therefore keep relying on the same spurious cues.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_also_explains_why_naive_fine_tuning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, explains, why, naive, fine-tuning, fails in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_authors_ablate_two_auxiliary_terms`

- Preferred role: `content`
- Cue keywords: `authors, ablate, two, auxiliary, terms, cbft, objective`
- Narration: The authors ablate the two auxiliary terms in the CBFT objective.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_authors_ablate_two_auxiliary_terms" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ablate, two, auxiliary, terms, cbft in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_removing_barrier_loss_prevents_movin`

- Preferred role: `method`
- Cue keywords: `removing, barrier, loss, prevents, moving, mechanistically, dissimilar, solution, while, removing`
- Narration: Removing the barrier loss prevents the model from moving to a mechanistically dissimilar solution, while removing the invariance loss means the model no longer reliably selects the specific cue-invariant mechanism the user wants.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_removing_barrier_loss_prevents_movin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords removing, barrier, loss, prevents, moving, mechanistically in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_other_words_barrier_loss_handles`

- Preferred role: `figure`
- Cue keywords: `other, words, barrier, loss, handles, where, pushing, away, cue-relying, minimizer`
- Narration: In other words, the barrier loss handles the where, pushing away from the cue-relying minimizer, and the invariance loss handles the which, locking onto the desired invariance.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s08_c3_other_words_barrier_loss_handles" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords other, words, barrier, loss, handles, where in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_both_needed_cbft_work`

- Preferred role: `content`
- Cue keywords: `both, needed, cbft, work`
- Narration: Both are needed for CBFT to work.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c4_both_needed_cbft_work" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords both, needed, cbft, work in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_numbers_make_effect_concrete`

- Preferred role: `content`
- Cue keywords: `numbers, make, effect, concrete`
- Narration: The numbers make the effect concrete.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_numbers_make_effect_concrete" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords numbers, make, effect, concrete in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_cifar_10_sixty_percent_cued_connecti`

- Preferred role: `result`
- Cue keywords: `cifar-10, sixty, percent, cued, connectivity-based, fine-tuning, achieves, seventy-four, percent, accuracy`
- Narration: On CIFAR-10 with sixty percent cued data, Connectivity-Based Fine-Tuning achieves seventy-four percent accuracy without the cue, seventy-two percent with the cue, and seventy-three percent when the cue is randomized, essentially invariant to the cue.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c2_cifar_10_sixty_percent_cued_connecti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, sixty, percent, cued, connectivity-based, fine-tuning in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_standard_fine_tuning_baseline_contra`

- Preferred role: `result`
- Cue keywords: `standard, fine-tuning, baseline, contrast, hits, ninety-nine, percent, cue, but, drops`
- Narration: A standard fine-tuning baseline, by contrast, hits ninety-nine percent with the cue but drops to just seventeen percent when the cue is randomized, revealing heavy reliance on the spurious feature.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_standard_fine_tuning_baseline_contra" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords standard, fine-tuning, baseline, contrast, hits, ninety-nine in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_when_underlying_image_randomized_cbf`

- Preferred role: `result`
- Cue keywords: `when, underlying, image, randomized, cbft, falls, near, chance, around, nine`
- Narration: And when the underlying image is randomized, CBFT falls near chance, around nine percent, showing it no longer predicts from the cue at all.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_when_underlying_image_randomized_cbf" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords when, underlying, image, randomized, cbft, falls in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_mode_connectivity_carries_m`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, mode, connectivity, carries, mechanistic, meaning`
- Narration: The takeaway is that mode connectivity carries mechanistic meaning.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_mode_connectivity_carries_m" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, mode, connectivity, carries, mechanistic, meaning in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_two_low_loss_models_not_linearly`

- Preferred role: `figure`
- Cue keywords: `two, low-loss, models, not, linearly, connected, they, rely, different, mechanisms`
- Narration: If two low-loss models are not linearly connected, they rely on different mechanisms, and this fact can be turned into a tool.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c2_two_low_loss_models_not_linearly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, low-loss, models, not, linearly, connected in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_connectivity_based_fine_tuning_delib`

- Preferred role: `content`
- Cue keywords: `connectivity-based, fine-tuning, deliberately, reshape, what, attends, removing, reliance, spurious, cues`
- Narration: Connectivity-Based Fine-Tuning uses it to deliberately reshape what a model attends to, removing reliance on spurious cues where ordinary fine-tuning cannot.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_connectivity_based_fine_tuning_delib" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords connectivity-based, fine-tuning, deliberately, reshape, what, attends in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s10_c4_mode_connectivity_short_not_merely`

- Preferred role: `content`
- Cue keywords: `mode, connectivity, short, not, merely, geometric, curiosity, but, practical, handle`
- Narration: Mode connectivity, in short, is not merely a geometric curiosity but a practical handle for building more robust and editable models.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c4_mode_connectivity_short_not_merely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mode, connectivity, short, not, merely, geometric in title/desc so the matcher can verify semantic overlap.
