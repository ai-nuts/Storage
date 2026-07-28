# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_university_tokyo_neurips_2022_langev`

- Preferred role: `method`
- Cue keywords: `university, tokyo, neurips, 2022, langevin, autoencoder`
- Narration: From the University of Tokyo, NeurIPS 2022: the Langevin autoencoder.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c1_university_tokyo_neurips_2022_langev" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords university, tokyo, neurips, 2022, langevin, autoencoder in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_langevin_dynamics_samples_intractabl`

- Preferred role: `content`
- Cue keywords: `langevin, dynamics, samples, intractable, posteriors, deep, latent, models, but, slowly`
- Narration: Langevin dynamics samples the intractable posteriors of deep latent models, but slowly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_langevin_dynamics_samples_intractabl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords langevin, dynamics, samples, intractable, posteriors, deep in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_authors_amortize_shared_encoder_prov`

- Preferred role: `method`
- Cue keywords: `authors, amortize, shared, encoder, prove, valid, mcmc, beat, variational, autoencoders`
- Narration: The authors amortize it into a shared encoder, prove it valid MCMC, and beat variational autoencoders.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_authors_amortize_shared_encoder_prov" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, amortize, shared, encoder, prove, valid in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_deep_latent_variable_models_maximum`

- Preferred role: `method`
- Cue keywords: `deep, latent, variable, models, maximum, likelihood, needs, expectation, over, latent`
- Narration: Training deep latent variable models by maximum likelihood needs an expectation over the latent posterior, which is intractable.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c1_deep_latent_variable_models_maximum" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, latent, variable, models, maximum, likelihood in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_langevin_dynamics_samples_posterior`

- Preferred role: `content`
- Cue keywords: `langevin, dynamics, samples, posterior, accurately, but, runs, fresh, chain, per`
- Narration: Langevin dynamics samples that posterior accurately, but runs a fresh chain per data point and converges slowly.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_langevin_dynamics_samples_posterior" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords langevin, dynamics, samples, posterior, accurately, but in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_variational_inference_dominates_than`

- Preferred role: `method`
- Cue keywords: `variational, inference, dominates, thanks, amortization, one, shared, encoder, predicts, latents`
- Narration: Variational inference dominates thanks to amortization: one shared encoder predicts the latents for all data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_variational_inference_dominates_than" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords variational, inference, dominates, thanks, amortization, one in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_but_relies_tractable_gaussians_limit`

- Preferred role: `result`
- Cue keywords: `but, relies, tractable, gaussians, limiting, accuracy`
- Narration: But it relies on tractable Gaussians, limiting accuracy.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_but_relies_tractable_gaussians_limit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, relies, tractable, gaussians, limiting, accuracy in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_mcmc_such_limit_yet_nobody`

- Preferred role: `content`
- Cue keywords: `mcmc, such, limit, yet, nobody, truly, amortized, before`
- Narration: MCMC has no such limit, yet nobody truly amortized it before.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_mcmc_such_limit_yet_nobody" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mcmc, such, limit, yet, nobody, truly in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_goal_amortized_efficiency_mcmc_flexi`

- Preferred role: `content`
- Cue keywords: `goal, amortized, efficiency, mcmc, flexibility`
- Narration: The goal: amortized efficiency with MCMC flexibility.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_goal_amortized_efficiency_mcmc_flexi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords goal, amortized, efficiency, mcmc, flexibility in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_two_contributions`

- Preferred role: `content`
- Cue keywords: `two, contributions`
- Narration: Two contributions.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_two_contributions" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, contributions in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_amortized_langevin_dynamics_mc`

- Preferred role: `method`
- Cue keywords: `first, amortized, langevin, dynamics, mcmc, algorithm, replaces, per-datapoint, iterations, langevin`
- Narration: First, amortized Langevin dynamics: an MCMC algorithm that replaces per-datapoint iterations with Langevin updates on a shared encoder's parameters, proven valid.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_amortized_langevin_dynamics_mc" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, amortized, langevin, dynamics, mcmc, algorithm in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_second_langevin_autoencoder_generati`

- Preferred role: `method`
- Cue keywords: `second, langevin, autoencoder, generative, small, tweak, standard, autoencoder`
- Narration: Second, the Langevin autoencoder, a generative model that is a small tweak of a standard autoencoder.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_second_langevin_autoencoder_generati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, langevin, autoencoder, generative, small, tweak in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_key_idea_move_randomness_latent`

- Preferred role: `method`
- Cue keywords: `key, idea, move, randomness, latent, space, encoder, parameters`
- Narration: The key idea: move randomness from latent space to encoder parameters.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_key_idea_move_randomness_latent" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, idea, move, randomness, latent, space in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_deterministic_encoder_maps_observati`

- Preferred role: `method`
- Cue keywords: `deterministic, encoder, maps, observations, latents, updating, its, parameters, moves, samples`
- Narration: A deterministic encoder maps observations to latents; updating its parameters moves the samples.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_deterministic_encoder_maps_observati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deterministic, encoder, maps, observations, latents, updating in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_convergence_guaranteed_when_fixed_fe`

- Preferred role: `content`
- Cue keywords: `convergence, guaranteed, when, fixed, feature, extractor, feeds, linear, layer, wider`
- Narration: Convergence is guaranteed when a fixed feature extractor feeds a linear layer wider than the batch.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c3_convergence_guaranteed_when_fixed_fe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords convergence, guaranteed, when, fixed, feature, extractor in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_autoencoder_runs_few_steps_before`

- Preferred role: `method`
- Cue keywords: `autoencoder, runs, few, steps, before, decoder, update, optionally, metropolis-hastings`
- Narration: The autoencoder runs a few steps before each decoder update, optionally with Metropolis-Hastings.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c4_autoencoder_runs_few_steps_before" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords autoencoder, runs, few, steps, before, decoder in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_validation_comes_two_stages`

- Preferred role: `content`
- Cue keywords: `validation, comes, two, stages`
- Narration: Validation comes in two stages.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_validation_comes_two_stages" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords validation, comes, two, stages in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_first_toy_problems_known_answers`

- Preferred role: `result`
- Cue keywords: `first, toy, problems, known, answers, bivariate-gaussian, posterior, random-network, posterior`
- Narration: First, toy problems with known answers: a bivariate-Gaussian posterior and a random-network posterior.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_first_toy_problems_known_answers" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, toy, problems, known, answers, bivariate-gaussian in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_image_generation_mnist_s_v_h_n_cifar`

- Preferred role: `method`
- Cue keywords: `image, generation, mnist, s-v-h-n, cifar-10, celeba, scored, negative, elbo, per`
- Narration: Then image generation on MNIST, S-V-H-N, CIFAR-10, and CelebA, scored by negative ELBO per dimension over three seeds.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_image_generation_mnist_s_v_h_n_cifar" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords image, generation, mnist, s-v-h-n, cifar-10, celeba in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_toy_problems_amortized_langevin_dyna`

- Preferred role: `content`
- Cue keywords: `toy, problems, amortized, langevin, dynamics, reproduces, multimodal, correlated, posteriors, variational`
- Narration: On toy problems, amortized Langevin dynamics reproduces multimodal, correlated posteriors that variational inference misses.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_toy_problems_amortized_langevin_dyna" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords toy, problems, amortized, langevin, dynamics, reproduces in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_images_langevin_autoencoder_achieves`

- Preferred role: `method`
- Cue keywords: `images, langevin, autoencoder, achieves, lowest, negative, elbo, all, four, datasets`
- Narration: On images, the Langevin autoencoder achieves the lowest negative ELBO on all four datasets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_images_langevin_autoencoder_achieves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords images, langevin, autoencoder, achieves, lowest, negative in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_lesson_more_accurate_posterior_sampl`

- Preferred role: `content`
- Cue keywords: `lesson, more, accurate, posterior, sampling, yields, better, models`
- Narration: The lesson: more accurate posterior sampling yields better models.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c3_lesson_more_accurate_posterior_sampl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lesson, more, accurate, posterior, sampling, yields in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_two_ablations`

- Preferred role: `content`
- Cue keywords: `two, ablations`
- Narration: Two ablations.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_two_ablations" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, ablations in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_encoder_capacity_confirms_theory_whe`

- Preferred role: `method`
- Cue keywords: `encoder, capacity, confirms, theory, when, final, linear, layer, least, batch`
- Narration: Encoder capacity confirms the theory: when the final linear layer is at least the batch size, samples match; smaller, some collapse.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_encoder_capacity_confirms_theory_whe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords encoder, capacity, confirms, theory, when, final in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_images_metropolis_hastings_step_stab`

- Preferred role: `method`
- Cue keywords: `images, metropolis-hastings, step, stabilizes, while, iteration, count, barely, matters, beyond`
- Narration: On images, the Metropolis-Hastings step stabilizes training, while iteration count barely matters beyond two.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_images_metropolis_hastings_step_stab" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords images, metropolis-hastings, step, stabilizes, while, iteration in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_gains_consistent_but_modest`

- Preferred role: `result`
- Cue keywords: `gains, consistent, but, modest`
- Narration: The gains are consistent but modest.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c1_gains_consistent_but_modest" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gains, consistent, but, modest in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_mnist_negative_elbo_drops_one`

- Preferred role: `content`
- Cue keywords: `mnist, negative, elbo, drops, one, point, one, seven, seven, versus`
- Narration: On MNIST, negative ELBO drops to one point one seven seven, versus one point one eight nine for the VAE.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_mnist_negative_elbo_drops_one" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords mnist, negative, elbo, drops, one, point in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_cifar_10_celeba_s_v_h_n_show_similar`

- Preferred role: `result`
- Cue keywords: `cifar-10, celeba, s-v-h-n, show, similar, small, improvements`
- Narration: CIFAR-10, CelebA, and S-V-H-N show similar small improvements.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c3_cifar_10_celeba_s_v_h_n_show_similar" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cifar-10, celeba, s-v-h-n, show, similar, small in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_cost_about_two_and_a_quarter_times_s`

- Preferred role: `content`
- Cue keywords: `cost, about, two-and-a-quarter, times, slower, vae`
- Narration: The cost: about two-and-a-quarter times slower than a VAE.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_cost_about_two_and_a_quarter_times_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords cost, about, two-and-a-quarter, times, slower, vae in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_elegant_move_langevin_noise`

- Preferred role: `method`
- Cue keywords: `takeaway, elegant, move, langevin, noise, latents, encoder, parameters, sampling, becomes`
- Narration: The takeaway is elegant: move Langevin noise from the latents to the encoder's parameters, so sampling becomes both efficient and flexible.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c1_takeaway_elegant_move_langevin_noise" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, elegant, move, langevin, noise, latents in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_provably_valid_looks_almost_like`

- Preferred role: `method`
- Cue keywords: `provably, valid, looks, almost, like, standard, autoencoder, yet, consistently, beats`
- Narration: Provably valid, it looks almost like a standard autoencoder yet consistently beats variational autoencoders on test likelihood.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_provably_valid_looks_almost_like" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords provably, valid, looks, almost, like, standard in title/desc so the matcher can verify semantic overlap.
