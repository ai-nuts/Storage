# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_foundation_models_transformed_langua`

- Preferred role: `content`
- Cue keywords: `foundation, models, transformed, language, vision, yet, tabular, workhorse, science, left`
- Narration: Foundation models have transformed language and vision, yet tabular data, the workhorse of data science, was left behind.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c1_foundation_models_transformed_langua" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords foundation, models, transformed, language, vision, yet in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_every_table_different_schema_trained`

- Preferred role: `method`
- Cue keywords: `every, table, different, schema, trained, one, rarely, transfers, another, introduces`
- Narration: Every table has a different schema, so a model trained on one rarely transfers to another. This paper introduces UniTabE, a universal pretraining protocol that handles any table uniformly.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_every_table_different_schema_trained" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords every, table, different, schema, trained, one in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_encodes_cell_small_module_called`

- Preferred role: `method`
- Cue keywords: `encodes, cell, small, module, called, tabunit, refines, table, transformer, adapts`
- Narration: It encodes each cell with a small module called TabUnit, refines the table with a Transformer, and adapts through text prompts.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_encodes_cell_small_module_called" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords encodes, cell, small, module, called, tabunit in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_pretrained_thirteen_billion_kaggle_s`

- Preferred role: `method`
- Cue keywords: `pretrained, thirteen, billion, kaggle, samples, beats, xgboost`
- Narration: Pretrained on thirteen billion Kaggle samples, it beats XGBoost.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c4_pretrained_thirteen_billion_kaggle_s" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pretrained, thirteen, billion, kaggle, samples, beats in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_tabular_underpins_applications_like`

- Preferred role: `content`
- Cue keywords: `tabular, underpins, applications, like, stock, prediction, real-estate, forecasting, credit, scoring`
- Narration: Tabular data underpins applications like stock prediction, real-estate forecasting, and credit scoring.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_tabular_underpins_applications_like" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords tabular, underpins, applications, like, stock, prediction in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_yet_unlike_text_images_widely`

- Preferred role: `content`
- Cue keywords: `yet, unlike, text, images, widely, adopted, foundation`
- Narration: Yet unlike text and images, it has no widely adopted foundation model.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c2_yet_unlike_text_images_widely" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords yet, unlike, text, images, widely, adopted in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_reason_tables_come_endless_schemas`

- Preferred role: `method`
- Cue keywords: `reason, tables, come, endless, schemas, different, column, names, types, counts`
- Narration: The reason: tables come in endless schemas, different column names, data types, and counts, so a model trained on one cannot be reused on another.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_reason_tables_come_endless_schemas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords reason, tables, come, endless, schemas, different in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_existing_methods_either_flatten_tabl`

- Preferred role: `method`
- Cue keywords: `existing, methods, either, flatten, tables, text, losing, numerical, meaning, assume`
- Narration: Existing methods either flatten tables into text, losing numerical meaning, or assume train and test share a fixed structure. Both block knowledge transfer across tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_existing_methods_either_flatten_tabl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, methods, either, flatten, tables, text in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_promise_pretraining_learns_general_k`

- Preferred role: `method`
- Cue keywords: `promise, pretraining, learns, general, knowledge, once, huge, unlabeled, transfers, many`
- Narration: The promise of pretraining is that a model learns general knowledge once from huge unlabeled data, then transfers it to many tasks.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_promise_pretraining_learns_general_k" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords promise, pretraining, learns, general, knowledge, once in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_authors_ask_whether_recipe_work`

- Preferred role: `content`
- Cue keywords: `authors, ask, whether, recipe, work, tables`
- Narration: The authors ask whether this recipe can work for tables.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s03_c2_authors_ask_whether_recipe_work" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords authors, ask, whether, recipe, work, tables in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_three_ingredients_needed_way_represe`

- Preferred role: `method`
- Cue keywords: `three, ingredients, needed, way, represent, any, table, regardless, schema, framework`
- Narration: Three ingredients are needed: a way to represent any table regardless of schema, a training framework flexible enough for many objectives, and a data source large enough to pretrain at scale.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c3_three_ingredients_needed_way_represe" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords three, ingredients, needed, way, represent, any in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_together_one_tabular_could_handle`

- Preferred role: `result`
- Cue keywords: `together, one, tabular, could, handle, classification, regression, missing-value, imputation, zero-shot`
- Narration: Together, one tabular model could handle classification, regression, missing-value imputation, zero-shot prediction, and tables that grow new columns, without redesigning per task.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c4_together_one_tabular_could_handle" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, one, tabular, could, handle, classification in title/desc so the matcher can verify semantic overlap.

## Slide 04: method

Heading: Method

### Cue 1: `cue_s04_c1_unitabe_heart_module_called_tabunit`

- Preferred role: `content`
- Cue keywords: `unitabe, heart, module, called, tabunit, handles, one, cell, time, treats`
- Narration: At UniTabE's heart is a module called TabUnit that handles one cell at a time. It treats each cell as a key-value pair: the column name is the key, the content the value.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s04_c1_unitabe_heart_module_called_tabunit" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords unitabe, heart, module, called, tabunit, handles in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_name_embedded_mean_pooled_data_type`

- Preferred role: `method`
- Cue keywords: `name, embedded, mean-pooled, data-type, embedding, marking, numerical, categorical, textual, fused`
- Narration: The name is embedded and mean-pooled, and a data-type embedding, marking numerical, categorical, or textual, is fused in through a gate, so a salary column is handled whether its values are numbers or words.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c2_name_embedded_mean_pooled_data_type" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords name, embedded, mean-pooled, data-type, embedding, marking in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_linking_layer_injects_column_vector`

- Preferred role: `method`
- Cue keywords: `linking, layer, injects, column, vector, value, token, attention, links, values`
- Narration: A linking layer injects the column vector into each value token, so attention links values to their column. All cell vectors, plus a CLS token, pass through a Transformer encoder.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_linking_layer_injects_column_vector" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords linking, layer, injects, column, vector, value in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_deliberately_shallow_lstm_decoder_gu`

- Preferred role: `method`
- Cue keywords: `deliberately, shallow, lstm, decoder, guided, free-form, prompt, like, fill, missing`
- Narration: A deliberately shallow LSTM decoder, guided by a free-form prompt like fill in missing value salary, generates the answer token by token. Keeping the decoder weak forces most knowledge into the reusable encoder. Pretraining mixes multi-cell masking and contrastive learning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c4_deliberately_shallow_lstm_decoder_gu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords deliberately, shallow, lstm, decoder, guided, free-form in title/desc so the matcher can verify semantic overlap.

## Slide 05: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s05_c1_pretrain_scale_team_assembled_massiv`

- Preferred role: `content`
- Cue keywords: `pretrain, scale, team, assembled, massive, tabular, dataset, kaggle, about, seven`
- Narration: To pretrain at scale, the team assembled a massive tabular dataset from Kaggle: about seven terabytes spanning three hundred and three domains, two hundred eighty-three thousand tables, and roughly thirteen billion examples.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s05_c1_pretrain_scale_team_assembled_massiv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pretrain, scale, team, assembled, massive, tabular in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_average_table_about_twenty_nine_nume`

- Preferred role: `result`
- Cue keywords: `average, table, about, twenty-nine, numerical, columns, eight, textual, ones, investing`
- Narration: On average each table has about twenty-nine numerical columns and eight textual ones, with investing, finance, and economics among the largest domains.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c2_average_table_about_twenty_nine_nume" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords average, table, about, twenty-nine, numerical, columns in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_evaluation_they_hold_out_twelve`

- Preferred role: `method`
- Cue keywords: `evaluation, they, hold, out, twelve, kaggle, tasks, six, classification, six`
- Narration: For evaluation, they hold out twelve Kaggle tasks, six classification and six regression, never seen in pretraining, plus seven widely used public benchmarks to compare against established methods.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_evaluation_they_hold_out_twelve" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords evaluation, they, hold, out, twelve, kaggle in title/desc so the matcher can verify semantic overlap.

## Slide 06: key-result

Heading: Key Result

### Cue 1: `cue_s06_c1_experiments_show_pretraining_pays_of`

- Preferred role: `method`
- Cue keywords: `experiments, show, pretraining, pays, off`
- Narration: The experiments show pretraining pays off.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_experiments_show_pretraining_pays_of" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords experiments, show, pretraining, pays, off in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_seven_standard_public_benchmarks_uni`

- Preferred role: `method`
- Cue keywords: `seven, standard, public, benchmarks, unitabe, reaches, average, area-under-curve, about, zero`
- Narration: On seven standard public benchmarks, UniTabE reaches an average area-under-curve of about zero point eight three, beating Tapas, FT-Transformer, and the industry favorite XGBoost.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c2_seven_standard_public_benchmarks_uni" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords seven, standard, public, benchmarks, unitabe, reaches in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_twelve_held_out_kaggle_tasks_spannin`

- Preferred role: `method`
- Cue keywords: `twelve, held-out, kaggle, tasks, spanning, classification, regression, again, outperforms, xgboost`
- Narration: On the twelve held-out Kaggle tasks, spanning classification and regression, it again outperforms XGBoost and a strong TransTab variant.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c3_twelve_held_out_kaggle_tasks_spannin" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords twelve, held-out, kaggle, tasks, spanning, classification in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_also_performs_well_zero_shot_mode`

- Preferred role: `figure`
- Cue keywords: `also, performs, well, zero-shot, mode, making, accurate, predictions, some, datasets`
- Narration: It also performs well in zero-shot mode, making accurate predictions on some datasets with no task-specific finetuning, evidence of genuine transferable reasoning about tables.
- Authoring: Create or label one visible figure region for this narration chunk. Use id="cue_s06_c4_also_performs_well_zero_shot_mode" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords also, performs, well, zero-shot, mode, making in title/desc so the matcher can verify semantic overlap.

## Slide 07: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s07_c1_ablations_confirm_part_earns_its`

- Preferred role: `method`
- Cue keywords: `ablations, confirm, part, earns, its, place, removing, linking, layer, which`
- Narration: Ablations confirm each part earns its place. Removing the linking layer, which ties names to values, causes the largest drop, from an AUC of zero point eight three down to zero point seven five.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c1_ablations_confirm_part_earns_its" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords ablations, confirm, part, earns, its, place in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_removing_fuse_layer_injects_data_typ`

- Preferred role: `content`
- Cue keywords: `removing, fuse, layer, injects, data-type, information, also, hurts, removing, both`
- Narration: Removing the fuse layer that injects data-type information also hurts, and removing both is worse.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s07_c2_removing_fuse_layer_injects_data_typ" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords removing, fuse, layer, injects, data-type, information in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_dropping_either_pretraining_objectiv`

- Preferred role: `method`
- Cue keywords: `dropping, either, pretraining, objective, multi-cell, masking, contrastive, learning, reduces, performance`
- Narration: Dropping either pretraining objective, multi-cell masking or contrastive learning, reduces performance too.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c3_dropping_either_pretraining_objectiv" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords dropping, either, pretraining, objective, multi-cell, masking in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_notably_one_layer_decoder_beats_thre`

- Preferred role: `method`
- Cue keywords: `notably, one-layer, decoder, beats, three-, six-layer, ones, supporting, choice, keep`
- Narration: Notably, a one-layer decoder beats three- or six-layer ones, supporting the choice to keep the decoder shallow.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c4_notably_one_layer_decoder_beats_thre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords notably, one-layer, decoder, beats, three-, six-layer in title/desc so the matcher can verify semantic overlap.

## Slide 08: takeaway

Heading: Takeaway

### Cue 1: `cue_s08_c1_pretraining_paradigm_reshaped_langua`

- Preferred role: `method`
- Cue keywords: `pretraining, paradigm, reshaped, language, vision, extend, tabular`
- Narration: The pretraining paradigm that reshaped language and vision can extend to tabular data.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c1_pretraining_paradigm_reshaped_langua" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pretraining, paradigm, reshaped, language, vision, extend in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_key_respect_table_structure_rather`

- Preferred role: `method`
- Cue keywords: `key, respect, table, structure, rather, flatten, text, represent, cell, its`
- Narration: The key is to respect table structure rather than flatten it into text: represent each cell by its column name, value, and data type, refine with a Transformer, and adapt through free-form prompts.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_key_respect_table_structure_rather" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords key, respect, table, structure, rather, flatten in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_pretrained_billions_unitabe_becomes`

- Preferred role: `method`
- Cue keywords: `pretrained, billions, unitabe, becomes, general, tabular, transfers, across, tasks, beats`
- Narration: Pretrained on billions, UniTabE becomes a general tabular model that transfers across tasks, beats the XGBoost baseline, and handles missing values and tables that gain columns.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c3_pretrained_billions_unitabe_becomes" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pretrained, billions, unitabe, becomes, general, tabular in title/desc so the matcher can verify semantic overlap.
