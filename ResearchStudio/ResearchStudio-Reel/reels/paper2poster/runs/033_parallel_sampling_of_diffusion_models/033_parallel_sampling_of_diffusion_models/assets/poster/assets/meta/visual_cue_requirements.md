# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_diffusion_models_produce_stunning_sa`

- Preferred role: `title`
- Cue keywords: `diffusion, models, produce, stunning, samples, but, they, slow, often, needing`
- Narration: Diffusion models produce stunning samples, but they are slow, often needing a thousand sequential denoising steps to generate a single sample. This paper from Stanford asks a different question than most prior work.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s01_c1_diffusion_models_produce_stunning_sa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords diffusion, models, produce, stunning, samples, but in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_instead_cutting_number_steps_paying`

- Preferred role: `content`
- Cue keywords: `instead, cutting, number, steps, paying, sample, quality, keep, every, step`
- Narration: Instead of cutting the number of steps and paying with sample quality, can we keep every step but run them in parallel, trading extra compute for lower latency?
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_instead_cutting_number_steps_paying" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords instead, cutting, number, steps, paying, sample in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_answer_method_called_paradigms_which`

- Preferred role: `method`
- Cue keywords: `answer, method, called, paradigms, which, picard, iterations, guess, whole, denoising`
- Narration: The answer is a method called ParaDiGMS, which uses Picard iterations to guess the whole denoising trajectory and refine it in parallel until it converges.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_answer_method_called_paradigms_which" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords answer, method, called, paradigms, which, picard in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_delivers_two_to_four_times_faster_sa`

- Preferred role: `content`
- Cue keywords: `delivers, two-to-four, times, faster, sampling, measurable, drop, quality`
- Narration: It delivers two-to-four times faster sampling with no measurable drop in quality.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_delivers_two_to_four_times_faster_sa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords delivers, two-to-four, times, faster, sampling, measurable in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_central_limitation_diffusion_models`

- Preferred role: `content`
- Cue keywords: `central, limitation, diffusion, models, sampling, speed`
- Narration: The central limitation of diffusion models is sampling speed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_central_limitation_diffusion_models" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords central, limitation, diffusion, models, sampling, speed in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_standard_denoising_diffusion_probabi`

- Preferred role: `content`
- Cue keywords: `standard, denoising, diffusion, probabilistic, take, thousand, sequential, passes, through, neural`
- Narration: A standard denoising diffusion probabilistic model can take a thousand sequential passes through the neural network to create one sample, which is far too slow for interactive use.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_standard_denoising_diffusion_probabi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords standard, denoising, diffusion, probabilistic, take, thousand in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_popular_fix_simply_fewer_denoising`

- Preferred role: `content`
- Cue keywords: `popular, fix, simply, fewer, denoising, steps, ddim, dpmsolver, but, reducing`
- Narration: The popular fix is to simply use fewer denoising steps, as DDIM and DPMSolver do, but reducing steps comes at the cost of sample quality.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_popular_fix_simply_fewer_denoising" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords popular, fix, simply, fewer, denoising, steps in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_field_largely_accepted_quality_for_s`

- Preferred role: `content`
- Cue keywords: `field, largely, accepted, quality-for-speed, tradeoff`
- Narration: The field has largely accepted this quality-for-speed tradeoff.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_field_largely_accepted_quality_for_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords field, largely, accepted, quality-for-speed, tradeoff in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_authors_pursue_orthogonal_direction`

- Preferred role: `content`
- Cue keywords: `authors, pursue, orthogonal, direction, instead, trading, quality, speed, they, ask`
- Narration: The authors pursue an orthogonal direction. Instead of trading quality for speed, they ask whether we can trade compute for speed.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_authors_pursue_orthogonal_direction" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, pursue, orthogonal, direction, instead, trading in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_goal_lower_latency_generating_single`

- Preferred role: `content`
- Cue keywords: `goal, lower, latency, generating, single, sample, not, just, throughput, generating`
- Narration: The goal is to lower the latency of generating a single sample, not just the throughput of generating many.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_goal_lower_latency_generating_single" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords goal, lower, latency, generating, single, sample in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_first_seems_impossible_because_denoi`

- Preferred role: `content`
- Cue keywords: `first, seems, impossible, because, denoising, inherently, sequential, step, depends, previous`
- Narration: At first this seems impossible, because denoising is inherently sequential: each step depends on the previous one.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_first_seems_impossible_because_denoi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, seems, impossible, because, denoising, inherently in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_naive_parallelization_generate_multi`

- Preferred role: `content`
- Cue keywords: `naive, parallelization, generate, multiple, samples, once, but, making, single, sample`
- Narration: Naive parallelization can generate multiple samples at once, but making a single sample appear faster in wall-clock time is a much harder problem.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c4_naive_parallelization_generate_multi" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords naive, parallelization, generate, multiple, samples, once in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_key_contribution_paradigms_short_par`

- Preferred role: `content`
- Cue keywords: `key, contribution, paradigms, short, parallel, diffusion, generative, sampling`
- Narration: The key contribution is ParaDiGMS, short for Parallel Diffusion Generative Model Sampling.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_key_contribution_paradigms_short_par" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, contribution, paradigms, short, parallel, diffusion in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_first_general_method_lets_you`

- Preferred role: `method`
- Cue keywords: `first, general, method, lets, you, spend, extra, parallel, compute, sample`
- Narration: It is the first general method that lets you spend extra parallel compute to sample a pretrained diffusion model faster, without any retraining.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_first_general_method_lets_you" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords first, general, method, lets, you, spend in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_crucially_orthogonal_existing_techni`

- Preferred role: `content`
- Cue keywords: `crucially, orthogonal, existing, techniques, layered, top, ddim, dpmsolver, yield, paraddim`
- Narration: Crucially, it is orthogonal to existing techniques, so it can be layered on top of DDIM or DPMSolver to yield ParaDDIM and ParaDPMSolver, combining both axes of speedup.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c3_crucially_orthogonal_existing_techni" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords crucially, orthogonal, existing, techniques, layered, top in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_also_compatible_classifier_free_guid`

- Preferred role: `guidance`
- Cue keywords: `also, compatible, classifier-free, guidance`
- Narration: It is also compatible with classifier-free guidance.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c4_also_compatible_classifier_free_guid" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, compatible, classifier-free, guidance in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_builds_picard_iterations_clas`

- Preferred role: `method`
- Cue keywords: `method, builds, picard, iterations, classic, technique, solving, ordinary, differential, equations`
- Narration: The method builds on Picard iterations, a classic technique for solving ordinary differential equations by fixed-point iteration. The insight is to write the value at each timestep as the initial value plus the integral of the drift along the path.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_builds_picard_iterations_clas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, builds, picard, iterations, classic, technique in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_starting_full_guess_trajectory_parad`

- Preferred role: `method`
- Cue keywords: `starting, full, guess, trajectory, paradigms, updates, every, timestep, simultaneously, cumulative`
- Narration: Starting from a full guess of the trajectory, ParaDiGMS updates every timestep simultaneously using the cumulative drift, and repeats until the values stop changing.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_starting_full_guess_trajectory_parad" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords starting, full, guess, trajectory, paradigms, updates in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_because_iteration_computed_parallel`

- Preferred role: `figure`
- Cue keywords: `because, iteration, computed, parallel, across, timesteps, number, iterations, converge, much`
- Narration: Because each iteration can be computed in parallel across timesteps, and the number of iterations to converge is much smaller than the number of steps, the whole trajectory resolves much faster.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c3_because_iteration_computed_parallel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords because, iteration, computed, parallel, across, timesteps in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_practice_sliding_window_fixed_size`

- Preferred role: `content`
- Cue keywords: `practice, sliding, window, fixed, size, respect, gpu, memory, advancing, window`
- Narration: In practice it uses a sliding window of a fixed size to respect GPU memory, advancing the window as soon as the earliest timesteps converge.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c4_practice_sliding_window_fixed_size" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords practice, sliding, window, fixed, size, respect in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_experiments_cover_two_very_different`

- Preferred role: `content`
- Cue keywords: `experiments, cover, two, very, different, domains, show, generality`
- Narration: The experiments cover two very different domains to show generality.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c1_experiments_cover_two_very_different" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, cover, two, very, different, domains in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_robotics_side_authors_test_diffusion`

- Preferred role: `result`
- Cue keywords: `robotics, side, authors, test, diffusion, policies, robosuite, square, pusht, frankakitchen`
- Narration: On the robotics side, the authors test diffusion policies on Robosuite Square, PushT, and FrankaKitchen, measuring task reward averaged over hundreds of evaluation episodes.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_robotics_side_authors_test_diffusion" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords robotics, side, authors, test, diffusion, policies in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_image_side_they_evaluate_stablediffu`

- Preferred role: `method`
- Cue keywords: `image, side, they, evaluate, stablediffusion, version, 2, generating, 768, by-768`
- Narration: On the image side, they evaluate StableDiffusion version 2 generating 768-by-768 images from COCO captions, judged by CLIP score, and pixel-space LSUN Church and Bedroom models, judged by FID score.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_image_side_they_evaluate_stablediffu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords image, side, they, evaluate, stablediffusion, version in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_together_these_span_latent_space_pix`

- Preferred role: `content`
- Cue keywords: `together, these, span, latent-space, pixel-space, diffusion, very, different, scales`
- Narration: Together these span latent-space and pixel-space diffusion at very different scales.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s06_c4_together_these_span_latent_space_pix" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, these, span, latent-space, pixel-space, diffusion in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_headline_finding_remarkably_consiste`

- Preferred role: `content`
- Cue keywords: `headline, finding, remarkably, consistent, two-to-four, times, speedup, across, every, task`
- Narration: The headline finding is remarkably consistent: a two-to-four times speedup across every task and every sampler, with no measurable degradation in quality.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c1_headline_finding_remarkably_consiste" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords headline, finding, remarkably, consistent, two-to-four, times in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_robotic_control_paraddpm_speeds_samp`

- Preferred role: `content`
- Cue keywords: `robotic, control, paraddpm, speeds, sampling, roughly, 3.4, 3.9, times, while`
- Narration: On robotic control, ParaDDPM speeds up sampling by roughly 3.4 to 3.9 times while holding task reward constant.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_robotic_control_paraddpm_speeds_samp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords robotic, control, paraddpm, speeds, sampling, roughly in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_stablediffusion_version_2_brings_tim`

- Preferred role: `result`
- Cue keywords: `stablediffusion, version, 2, brings, time, generate, image, down, fifty, seconds`
- Narration: On StableDiffusion version 2, it brings the time to generate an image down from fifty seconds to under fifteen, a 3.4x gain, and stacking it on faster samplers reaches four times.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_stablediffusion_version_2_brings_tim" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stablediffusion, version, 2, brings, time, generate in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_number_parallel_iterations_needed_co`

- Preferred role: `content`
- Cue keywords: `number, parallel, iterations, needed, convergence, twenty, times, smaller, number, sequential`
- Narration: The number of parallel iterations needed for convergence is up to twenty times smaller than the number of sequential steps, which is why the approach works.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c4_number_parallel_iterations_needed_co" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords number, parallel, iterations, needed, convergence, twenty in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_main_ablation_studies_effect_error`

- Preferred role: `result`
- Cue keywords: `main, ablation, studies, effect, error, tolerance, fixed-point, iteration`
- Narration: The main ablation studies the effect of the error tolerance in the fixed-point iteration.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s08_c1_main_ablation_studies_effect_error" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords main, ablation, studies, effect, error, tolerance in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_lower_tolerance_means_more_iteration`

- Preferred role: `content`
- Cue keywords: `lower, tolerance, means, more, iterations, slower, sampling, but, higher, fidelity`
- Narration: A lower tolerance means more iterations and slower sampling but higher fidelity, while a looser tolerance is faster.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c2_lower_tolerance_means_more_iteration" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lower, tolerance, means, more, iterations, slower in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_shows_comfortable_regime_where_fairl`

- Preferred role: `content`
- Cue keywords: `shows, comfortable, regime, where, fairly, relaxed, tolerance, still, preserves, sample`
- Narration: The paper shows there is a comfortable regime where a fairly relaxed tolerance still preserves sample quality.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c3_shows_comfortable_regime_where_fairl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords shows, comfortable, regime, where, fairly, relaxed in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_importantly_lsun_church_paraddpm_mat`

- Preferred role: `method`
- Cue keywords: `importantly, lsun, church, paraddpm, matches, full, ddpm, fid, score, nearly`
- Narration: Importantly, on LSUN Church, ParaDDPM matches full DDPM's FID score at nearly four times the speed, whereas simply reducing DDIM to 500 steps produces visibly worse images, demonstrating that the gains genuinely come from parallelism rather than fewer steps.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_importantly_lsun_church_paraddpm_mat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords importantly, lsun, church, paraddpm, matches, full in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_put_concrete_numbers_sampling_speedu`

- Preferred role: `content`
- Cue keywords: `put, concrete, numbers, sampling, speedups, two, four, times, across, board`
- Narration: To put concrete numbers on it: sampling speedups of two to four times across the board.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_put_concrete_numbers_sampling_speedu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords put, concrete, numbers, sampling, speedups, two in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_stablediffusion_version_2_drops_fift`

- Preferred role: `content`
- Cue keywords: `stablediffusion, version, 2, drops, fifty, seconds, fourteen-point-six, seconds, per, image`
- Narration: StableDiffusion version 2 drops from fifty seconds to fourteen-point-six seconds per image.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_stablediffusion_version_2_drops_fift" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords stablediffusion, version, 2, drops, fifty, seconds in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_lsun_church_fid_barely_moves`

- Preferred role: `content`
- Cue keywords: `lsun, church, fid, barely, moves, twelve-point-eight, twelve-point-nine, while, running, almost`
- Narration: On LSUN Church, FID barely moves, from twelve-point-eight to twelve-point-nine, while running almost four times faster.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_lsun_church_fid_barely_moves" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lsun, church, fid, barely, moves, twelve-point-eight in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_deep_reason_scales_number_parallel`

- Preferred role: `content`
- Cue keywords: `deep, reason, scales, number, parallel, iterations, converge, twenty, times, smaller`
- Narration: And the deep reason it scales is that the number of parallel iterations to converge is up to twenty times smaller than the thousand sequential steps.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c4_deep_reason_scales_number_parallel" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deep, reason, scales, number, parallel, iterations in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_lasting_takeaway_new_axis_accelerati`

- Preferred role: `takeaway`
- Cue keywords: `lasting, takeaway, new, axis, accelerating, diffusion, models`
- Narration: The lasting takeaway is a new axis for accelerating diffusion models.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_lasting_takeaway_new_axis_accelerati" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lasting, takeaway, new, axis, accelerating, diffusion in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_rather_sacrificing_quality_taking_fe`

- Preferred role: `figure`
- Cue keywords: `rather, sacrificing, quality, taking, fewer, steps, paradigms, spends, parallel, compute`
- Narration: Rather than sacrificing quality by taking fewer steps, ParaDiGMS spends parallel compute to run all the steps faster, cutting sampling latency by two to four times with no loss in quality, and it composes with the fast samplers people already use.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s10_c2_rather_sacrificing_quality_taking_fe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rather, sacrificing, quality, taking, fewer, steps in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_looking_forward_parallel_hardware_ke`

- Preferred role: `content`
- Cue keywords: `looking, forward, parallel, hardware, keeps, improving, sampling, time, will, limited`
- Narration: Looking forward, as parallel hardware keeps improving, sampling time will be limited only by the small number of Picard iterations, pointing toward even faster real-time generation.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s10_c3_looking_forward_parallel_hardware_ke" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords looking, forward, parallel, hardware, keeps, improving in title/desc so the matcher can verify semantic overlap.
