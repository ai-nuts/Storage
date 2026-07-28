# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_ocean_absorbs_large_share_humanity`

- Preferred role: `content`
- Cue keywords: `ocean, absorbs, large, share, humanity, carbon, emissions, yet, our, official`
- Narration: The ocean absorbs a large share of humanity's carbon emissions, yet our official picture of how much it takes up always lags reality by about a year.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_ocean_absorbs_large_share_humanity" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ocean, absorbs, large, share, humanity, carbon in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_work_introduces_carbon_monitor_ocean`

- Preferred role: `content`
- Cue keywords: `work, introduces, carbon, monitor, ocean, cmo-nrt, near-real-time, monthly, gridded, dataset`
- Narration: This work introduces Carbon Monitor Ocean, or CMO-NRT, a near-real-time, monthly, gridded dataset of global surface ocean fugacity of CO2 and air-sea CO2 flux.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c2_work_introduces_carbon_monitor_ocean" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords work, introduces, carbon, monitor, ocean, cmo-nrt in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_convolutional_neural_networks_semi_s`

- Preferred role: `content`
- Cue keywords: `convolutional, neural, networks, semi-supervised, learning, update, estimates, ten, ocean, biogeochemical`
- Narration: By using convolutional neural networks and semi-supervised learning to update the estimates from ten ocean biogeochemical models and eight data products, the authors extend the global carbon budget to the present month, giving scientists and policymakers a far more timely view of the ocean carbon sink.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c3_convolutional_neural_networks_semi_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords convolutional, neural, networks, semi-supervised, learning, update in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_ocean_one_largest_buffers_against`

- Preferred role: `result`
- Cue keywords: `ocean, one, largest, buffers, against, climate, change, soaking, big, fraction`
- Narration: The ocean is one of the largest buffers against climate change, soaking up a big fraction of the carbon dioxide we emit.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s02_c1_ocean_one_largest_buffers_against" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ocean, one, largest, buffers, against, climate in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_but_our_best_official_accounting`

- Preferred role: `content`
- Cue keywords: `but, our, best, official, accounting, how, much, absorbs, annual, global`
- Narration: But our best official accounting of how much it absorbs, the annual Global Carbon Budget, always trails reality by about a year.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_but_our_best_official_accounting" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords but, our, best, official, accounting, how in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_means_when_ocean_uptake_shifts`

- Preferred role: `content`
- Cue keywords: `means, when, ocean, uptake, shifts, simply, cannot, see, until, long`
- Narration: That means when the ocean's uptake shifts, we simply cannot see it until long after the fact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c3_means_when_ocean_uptake_shifts" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords means, when, ocean, uptake, shifts, simply in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_lag_baked_biogeochemical_models_comp`

- Preferred role: `content`
- Cue keywords: `lag, baked, biogeochemical, models, computationally, heavy, surface-ocean, observations, they, rely`
- Narration: This lag is baked in: the biogeochemical models are computationally heavy, and the surface-ocean observations they rely on are themselves delayed by roughly a year.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c4_lag_baked_biogeochemical_models_comp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords lag, baked, biogeochemical, models, computationally, heavy in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_countries_move_through_global_stockt`

- Preferred role: `content`
- Cue keywords: `countries, move, through, global, stocktake, under, paris, agreement, they, need`
- Narration: As countries move through the global stocktake under the Paris Agreement, they need to know where the carbon is going right now, not a year ago.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c1_countries_move_through_global_stockt" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords countries, move, through, global, stocktake, under in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_existing_databases_ocean_carbon_flux`

- Preferred role: `content`
- Cue keywords: `existing, databases, ocean, carbon, fluxes, detailed, trustworthy, but, they, always`
- Narration: The existing databases of ocean carbon fluxes are detailed and trustworthy, but they are always looking backward in time.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_existing_databases_ocean_carbon_flux" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, databases, ocean, carbon, fluxes, detailed in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_what_missing_way_bring_same`

- Preferred role: `content`
- Cue keywords: `what, missing, way, bring, same, rigor, present, month, policymakers, scientists`
- Narration: What is missing is a way to bring that same rigor up to the present month, so that policymakers and scientists can respond to changes in the ocean sink as they happen.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c3_what_missing_way_bring_same" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords what, missing, way, bring, same, rigor in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_core_contribution_carbon_monitor_oce`

- Preferred role: `guidance`
- Cue keywords: `core, contribution, carbon, monitor, ocean, cmo-nrt, near-real-time, monthly, gridded, dataset`
- Narration: The core contribution is Carbon Monitor Ocean, or CMO-NRT: a near-real-time, monthly, gridded dataset of global surface ocean carbon dioxide fugacity and air-sea flux, together with the machine-learning framework that generates it.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c1_core_contribution_carbon_monitor_oce" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords core, contribution, carbon, monitor, ocean, cmo-nrt in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_rather_replace_trusted_community_mod`

- Preferred role: `guidance`
- Cue keywords: `rather, replace, trusted, community, models, updates, all, ten, ocean, biogeochemical`
- Narration: Rather than replace the trusted community models, it updates all ten ocean biogeochemical models and eight data products from the Global Carbon Budget 2022 into a near-real-time framework.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s04_c2_rather_replace_trusted_community_mod" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords rather, replace, trusted, community, models, updates in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_dataset_code_released_openly_figshar`

- Preferred role: `qr`
- Cue keywords: `dataset, code, released, openly, figshare, project, website`
- Narration: The dataset and the code are released openly, on Figshare and on the project website.
- Authoring: Create or label one visible qr region for this narration chunk. Use id="cue_s04_c3_dataset_code_released_openly_figshar" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dataset, code, released, openly, figshare, project in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_treats_biogeochemical_product`

- Preferred role: `method`
- Cue keywords: `method, treats, biogeochemical, product, target, neural, network, learns, reproduce, observable`
- Narration: The method treats each biogeochemical model or data product as a target that a neural network learns to reproduce from observable predictors: year, month, latitude, longitude, and nine environmental variables like sea-surface temperature, salinity, chlorophyll and wind.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_treats_biogeochemical_product" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, treats, biogeochemical, product, target, neural in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_global_grids_cut_small_eighteen_by_e`

- Preferred role: `content`
- Cue keywords: `global, grids, cut, small, eighteen-by-eighteen, patches, fed, through, stacked, convolutional`
- Narration: Global grids are cut into small eighteen-by-eighteen patches and fed through stacked convolutional and linear layers.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c2_global_grids_cut_small_eighteen_by_e" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords global, grids, cut, small, eighteen-by-eighteen, patches in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_clever_part_semi_supervised_learning`

- Preferred role: `result`
- Cue keywords: `clever, part, semi-supervised, learning, alongside, standard, supervised, error, labeled, points`
- Narration: The clever part is semi-supervised learning: alongside a standard supervised error on labeled points, the model adds an unsupervised consistency loss that forces its predictions to agree when ten percent versus thirty percent of the input features are masked.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c3_clever_part_semi_supervised_learning" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords clever, part, semi-supervised, learning, alongside, standard in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_combining_two_losses_makes_markedly`

- Preferred role: `figure`
- Cue keywords: `combining, two, losses, makes, markedly, more, stable`
- Narration: Combining the two losses makes the model markedly more stable.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s05_c4_combining_two_losses_makes_markedly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords combining, two, losses, makes, markedly, more in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_resulting_dataset_delivers_monthly_g`

- Preferred role: `result`
- Cue keywords: `resulting, dataset, delivers, monthly, gridded, maps, global, surface-ocean, carbon, dioxide`
- Narration: The resulting dataset delivers monthly, gridded maps of global surface-ocean carbon dioxide fugacity and air-sea flux, spanning January 2022 through July 2023, built by updating the ten ocean biogeochemical models and eight data products of the Global Carbon Budget 2022.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c1_resulting_dataset_delivers_monthly_g" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords resulting, dataset, delivers, monthly, gridded, maps in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_its_inputs_draw_satellite_reanalysis`

- Preferred role: `figure`
- Cue keywords: `its, inputs, draw, satellite, reanalysis, products, chlorophyll, temperature, sea, ice`
- Narration: Its inputs draw on satellite and reanalysis products for chlorophyll, temperature, sea ice, mixed-layer depth, salinity, sea-surface height, pressure and wind, and the whole dataset is published openly on Figshare and refreshed on the project website.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c2_its_inputs_draw_satellite_reanalysis" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords its, inputs, draw, satellite, reanalysis, products in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_test_approach_authors_held_out`

- Preferred role: `method`
- Cue keywords: `test, approach, authors, held, out, most, recent, two, years, every`
- Narration: To test the approach, the authors held out the most recent two years of every model and product, trained only on earlier data, and then predicted the withheld period.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_test_approach_authors_held_out" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords test, approach, authors, held, out, most in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_predictions_track_originals_remarkab`

- Preferred role: `content`
- Cue keywords: `predictions, track, originals, remarkably, well, most, ten, models, eight, products`
- Narration: The predictions track the originals remarkably well: for most of the ten models and eight products, the correlation exceeds an R-squared of point nine, and even the global monthly aggregates mostly stay above point eight five.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_predictions_track_originals_remarkab" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords predictions, track, originals, remarkably, well, most in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_global_averages_predictions_run_just`

- Preferred role: `result`
- Cue keywords: `global, averages, predictions, run, just, slightly, high, most, differences, smaller`
- Narration: On global averages the predictions run just slightly high, with most differences smaller than three microatmospheres.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c3_global_averages_predictions_run_just" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords global, averages, predictions, run, just, slightly in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_looking_reveals_clear_pattern_biogeo`

- Preferred role: `content`
- Cue keywords: `looking, reveals, clear, pattern, biogeochemical, models, reproduced, most, faithfully, consistently`
- Narration: Looking model by model reveals a clear pattern: the biogeochemical models are reproduced most faithfully and consistently, with several exceeding an R-squared of point nine five, while a few data products are noisier and occasionally scatter away from the fit line.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_looking_reveals_clear_pattern_biogeo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords looking, reveals, clear, pattern, biogeochemical, models in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_spatial_maps_differences_confirm_agr`

- Preferred role: `method`
- Cue keywords: `spatial, maps, differences, confirm, agreement, broadly, uniform, across, globe, largest`
- Narration: Spatial maps of the differences confirm that agreement is broadly uniform across the globe, with the largest residual gaps concentrated in the Arctic Ocean and the equatorial Pacific.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_spatial_maps_differences_confirm_agr" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords spatial, maps, differences, confirm, agreement, broadly in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_impact`

- Preferred role: `content`
- Cue keywords: `few, numbers, capture, impact`
- Narration: A few numbers capture the impact.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, impact in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_method_collapses_roughly_one_year_re`

- Preferred role: `method`
- Cue keywords: `method, collapses, roughly, one-year, reporting, delay, down, monthly, near-real-time, coverage`
- Narration: The method collapses the roughly one-year reporting delay down to monthly, near-real-time coverage, here spanning January 2022 through July 2023.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c2_method_collapses_roughly_one_year_re" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, collapses, roughly, one-year, reporting, delay in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_validation_correlations_exceed_r_squ`

- Preferred role: `content`
- Cue keywords: `validation, correlations, exceed, r-squared, point, nine, most, eighteen, source, estimates`
- Narration: Validation correlations exceed an R-squared of point nine for most of the eighteen source estimates, global aggregates stay above point eight five, and global monthly differences are mostly under three microatmospheres.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_validation_correlations_exceed_r_squ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords validation, correlations, exceed, r-squared, point, nine in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_even_auxiliary_near_real_time_atmosp`

- Preferred role: `result`
- Cue keywords: `even, auxiliary, near-real-time, atmospheric, carbon, dioxide, achieves, root-mean-square, error, just`
- Narration: Even the auxiliary near-real-time atmospheric carbon dioxide model achieves a root-mean-square error of just one point seven four, about a half-percent error.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s09_c4_even_auxiliary_near_real_time_atmosp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords even, auxiliary, near-real-time, atmospheric, carbon, dioxide in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple_pairing_convolutiona`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple, pairing, convolutional, networks, semi-supervised, learning, update, trusted, models`
- Narration: The takeaway is simple: by pairing convolutional networks with semi-supervised learning to update trusted models and data products, Carbon Monitor Ocean turns a once year-delayed picture of the global ocean carbon sink into a near-real-time, monthly, gridded monitor.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple_pairing_convolutiona" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple, pairing, convolutional, networks, semi-supervised in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_gives_scientists_policymakers_far_ti`

- Preferred role: `method`
- Cue keywords: `gives, scientists, policymakers, far, timelier, spatially, detailed, constraint, how, much`
- Narration: That gives scientists and policymakers a far timelier and spatially detailed constraint on how much carbon the ocean is taking up, right when they need it for the carbon budget and climate decisions.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_gives_scientists_policymakers_far_ti" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords gives, scientists, policymakers, far, timelier, spatially in title/desc so the matcher can verify semantic overlap.
