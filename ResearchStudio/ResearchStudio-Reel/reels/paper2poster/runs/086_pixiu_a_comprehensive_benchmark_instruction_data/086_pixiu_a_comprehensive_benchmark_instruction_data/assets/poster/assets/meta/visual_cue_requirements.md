# paper2video visual cue requirements for ppt-master

Use this file while authoring the deck. It is not a design style; it is a semantic anchor contract for video highlights.

For each slide, create 2-5 visible content groups whose IDs, `<title>`, `<desc>`, or `data-cue-label` match the requested anchor IDs. Keep the highlight target on real content, not headers, captions, logos, or background chrome.

The final cue renderer uses translucent point highlights centered on these regions, so the region should wrap the specific diagram/card/chart area being discussed. Prefer a stable SVG group id beginning with `cue_`; include the narration keywords in `<desc>` or `data-cue-label` so the matcher can confirm semantic overlap instead of guessing from layout alone.

## Slide 01: title

Heading: Title

### Cue 1: `cue_s01_c1_pixiu_comprehensive_open_source_fram`

- Preferred role: `guidance`
- Cue keywords: `pixiu, comprehensive, open-source, framework, financial, artificial, intelligence, published, neurips, 2023`
- Narration: This is PIXIU, a comprehensive open-source framework for financial artificial intelligence, published at NeurIPS 2023.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s01_c1_pixiu_comprehensive_open_source_fram" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pixiu, comprehensive, open-source, framework, financial, artificial in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s01_c2_financial_language_highly_technical`

- Preferred role: `method`
- Cue keywords: `financial, language, highly, technical, yet, before, pixiu, openly, released, financial`
- Narration: Financial language is highly technical, yet before PIXIU there were no openly released financial large language models, no financial instruction tuning data, and no holistic evaluation benchmark. PIXIU fills all three gaps at once.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c2_financial_language_highly_technical" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords financial, language, highly, technical, yet, before in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s01_c3_contributes_fit_first_multi_task_mul`

- Preferred role: `method`
- Cue keywords: `contributes, fit, first, multi-task, multi-modal, financial, instruction, dataset, one, hundred`
- Narration: It contributes FIT, the first multi-task, multi-modal financial instruction dataset with one hundred and thirty-six thousand samples; FinMA, the first openly released instruction-following financial large language model built by fine-tuning LLaMA; and FLARE, a standardized benchmark spanning financial natural language tasks and stock movement prediction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s01_c3_contributes_fit_first_multi_task_mul" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords contributes, fit, first, multi-task, multi-modal, financial in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s01_c4_together_they_let_community_build`

- Preferred role: `content`
- Cue keywords: `together, they, let, community, build, compare, advance, financial, llms, open`
- Narration: Together they let the community build, compare, and advance financial LLMs in the open.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s01_c4_together_they_let_community_build" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords together, they, let, community, build, compare in title/desc so the matcher can verify semantic overlap.

## Slide 02: problem

Heading: Problem

### Cue 1: `cue_s02_c1_financial_technology_advanced_rapidl`

- Preferred role: `content`
- Cue keywords: `financial, technology, advanced, rapidly, nlp, but, highly, technical, nature, financial`
- Narration: Financial technology has advanced rapidly with NLP, but the highly technical nature of financial text demands domain-specific models.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s02_c1_financial_technology_advanced_rapidl" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords financial, technology, advanced, rapidly, nlp, but in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s02_c2_existing_financial_pre_trained_model`

- Preferred role: `method`
- Cue keywords: `existing, financial, pre-trained, models, like, finbert, flang, small, below, one`
- Narration: Existing financial pre-trained models like finBERT and FLANG are small, below one billion parameters, limiting their generalization.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c2_existing_financial_pre_trained_model" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords existing, financial, pre-trained, models, like, finbert in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s02_c3_one_large_financial_fifty_billion_pa`

- Preferred role: `method`
- Cue keywords: `one, large, financial, fifty-billion-parameter, bloomberggpt, proprietary, neither, its, weights, nor`
- Narration: The one large financial model, the fifty-billion-parameter BloombergGPT, is proprietary: neither its weights nor its training data are released, and it is not instruction-following.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c3_one_large_financial_fifty_billion_pa" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords one, large, financial, fifty-billion-parameter, bloomberggpt, proprietary in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s02_c4_critically_open_financial_instructio`

- Preferred role: `method`
- Cue keywords: `critically, open, financial, instruction, datasets, standardized, benchmarks, comprehensively, assessing, financial`
- Narration: Critically, there are no open financial instruction datasets and no standardized benchmarks for comprehensively assessing financial LLMs. This leaves the research community without the resources needed to push financial AI forward in the open.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s02_c4_critically_open_financial_instructio" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords critically, open, financial, instruction, datasets, standardized in title/desc so the matcher can verify semantic overlap.

## Slide 03: motivation

Heading: Motivation

### Cue 1: `cue_s03_c1_two_gaps_motivate_work_first`

- Preferred role: `method`
- Cue keywords: `two, gaps, motivate, work, first, instruction, tuning, proven, essential, improving`
- Narration: Two gaps motivate this work. First, instruction tuning has proven essential for improving a model's zero-shot ability on downstream tasks, yet no financial instruction data exists to enable it.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s03_c1_two_gaps_motivate_work_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords two, gaps, motivate, work, first, instruction in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s03_c2_second_existing_financial_benchmarks`

- Preferred role: `result`
- Cue keywords: `second, existing, financial, benchmarks, such, flue, cover, only, natural, language`
- Narration: Second, existing financial benchmarks such as FLUE cover only natural language processing tasks.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s03_c2_second_existing_financial_benchmarks" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, existing, financial, benchmarks, such, flue in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s03_c3_they_ignore_financial_prediction_tas`

- Preferred role: `title`
- Cue keywords: `they, ignore, financial, prediction, tasks, like, stock, movement, prediction, which`
- Narration: They ignore financial prediction tasks like stock movement prediction, which require exploiting both text and time-series data and are far more aligned with real-world financial scenarios.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s03_c3_they_ignore_financial_prediction_tas" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords they, ignore, financial, prediction, tasks, like in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s03_c4_pixiu_built_close_both_gaps`

- Preferred role: `guidance`
- Cue keywords: `pixiu, built, close, both, gaps, open, resources, multi-task, coverage, multi-modal`
- Narration: PIXIU is built to close both gaps with open resources, multi-task coverage, multi-modal data, and greater task diversity.
- Authoring: Create or label one visible guidance region for this narration chunk. Use id="cue_s03_c4_pixiu_built_close_both_gaps" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pixiu, built, close, both, gaps, open in title/desc so the matcher can verify semantic overlap.

## Slide 04: contribution

Heading: Contribution

### Cue 1: `cue_s04_c1_pixiu_makes_four_contributions_first`

- Preferred role: `method`
- Cue keywords: `pixiu, makes, four, contributions, first, introduces, fit, first, multi-task, multi-modal`
- Narration: PIXIU makes four contributions. First, it introduces FIT, the first multi-task and multi-modal instruction tuning dataset for finance, covering five tasks and nine datasets with one hundred thirty-six thousand samples.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c1_pixiu_makes_four_contributions_first" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pixiu, makes, four, contributions, first, introduces in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s04_c2_second_introduces_flare_first_evalua`

- Preferred role: `result`
- Cue keywords: `second, introduces, flare, first, evaluation, benchmark, includes, both, financial, language`
- Narration: Second, it introduces FLARE, the first evaluation benchmark that includes both financial language understanding and financial prediction.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c2_second_introduces_flare_first_evalua" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, introduces, flare, first, evaluation, benchmark in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s04_c3_third_introduces_finma_first_openly`

- Preferred role: `method`
- Cue keywords: `third, introduces, finma, first, openly, released, instruction-following, financial, large, language`
- Narration: Third, it introduces FinMA, the first openly released, instruction-following financial large language model, achieving state-of-the-art on three financial NLP tasks and one prediction task.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s04_c3_third_introduces_finma_first_openly" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, introduces, finma, first, openly, released in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s04_c4_fourth_benchmarks_finma_against_exis`

- Preferred role: `result`
- Cue keywords: `fourth, benchmarks, finma, against, existing, llms, revealing, both, their, superiority`
- Narration: Fourth, it benchmarks FinMA against existing LLMs, revealing both their superiority and their key limitations for finance.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s04_c4_fourth_benchmarks_finma_against_exis" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fourth, benchmarks, finma, against, existing, llms in title/desc so the matcher can verify semantic overlap.

## Slide 05: method

Heading: Method

### Cue 1: `cue_s05_c1_method_three_stages_first_pixiu`

- Preferred role: `method`
- Cue keywords: `method, three, stages, first, pixiu, gathers, open-released, across, five, financial`
- Narration: The method has three stages. First, PIXIU gathers open-released data across five financial tasks: sentiment analysis, news headline classification, named entity recognition, question answering, and stock movement prediction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c1_method_three_stages_first_pixiu" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords method, three, stages, first, pixiu, gathers in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s05_c2_domain_experts_write_diverse_task_sp`

- Preferred role: `method`
- Cue keywords: `domain, experts, write, diverse, task-specific, instructions, task, which, assembled, samples`
- Narration: Domain experts write diverse task-specific instructions for each task, which are assembled with the data samples to form the FIT instruction dataset. This data is multi-modal, spanning text, tables from financial reports, and historical stock prices as time series.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c2_domain_experts_write_diverse_task_sp" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords domain, experts, write, diverse, task-specific, instructions in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s05_c3_second_llama_checkpoints_seven_thirt`

- Preferred role: `method`
- Cue keywords: `second, llama, checkpoints, seven, thirty, billion, parameters, fine-tuned, fit, multi-task`
- Narration: Second, LLaMA checkpoints at seven and thirty billion parameters are fine-tuned on FIT with multi-task instruction tuning, producing the FinMA model family.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s05_c3_second_llama_checkpoints_seven_thirt" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords second, llama, checkpoints, seven, thirty, billion in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s05_c4_third_finma_other_llms_evaluated`

- Preferred role: `result`
- Cue keywords: `third, finma, other, llms, evaluated, flare, benchmark, which, unifies, four`
- Narration: Third, FinMA and other LLMs are evaluated on the FLARE benchmark, which unifies four financial NLP tasks with six datasets and one prediction task with three datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s05_c4_third_finma_other_llms_evaluated" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords third, finma, other, llms, evaluated, flare in title/desc so the matcher can verify semantic overlap.

## Slide 06: dataset-benchmark

Heading: Dataset / Benchmark

### Cue 1: `cue_s06_c1_fit_financial_instruction_tuning_dat`

- Preferred role: `method`
- Cue keywords: `fit, financial, instruction, tuning, dataset, contains, one, hundred, thirty-six, thousand`
- Narration: FIT, the financial instruction tuning dataset, contains one hundred thirty-six thousand instruction samples across five tasks and nine datasets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c1_fit_financial_instruction_tuning_dat" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords fit, financial, instruction, tuning, dataset, contains in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s06_c2_flare_evaluation_benchmark_covers_fo`

- Preferred role: `result`
- Cue keywords: `flare, evaluation, benchmark, covers, four, financial, nlp, tasks, six, datasets`
- Narration: The FLARE evaluation benchmark covers four financial NLP tasks with six datasets and one financial prediction task with three datasets.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c2_flare_evaluation_benchmark_covers_fo" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords flare, evaluation, benchmark, covers, four, financial in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s06_c3_sentiment_analysis_financial_phrase`

- Preferred role: `result`
- Cue keywords: `sentiment, analysis, financial, phrase, bank, fiqa-sa, news, headline, classification, headline`
- Narration: Sentiment analysis uses the Financial Phrase Bank and FiQA-SA, news headline classification uses the Headline dataset, named entity recognition uses a financial NER dataset, question answering uses FinQA and ConvFinQA, and stock movement prediction uses BigData22, ACL18, and CIKM18.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s06_c3_sentiment_analysis_financial_phrase" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords sentiment, analysis, financial, phrase, bank, fiqa-sa in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s06_c4_task_scored_its_standard_metric`

- Preferred role: `method`
- Cue keywords: `task, scored, its, standard, metric, such, weighted, 1, entity-level, 1`
- Narration: Each task is scored with its standard metric, such as weighted F1, entity-level F1, exact-match accuracy, and the Matthews correlation coefficient for prediction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s06_c4_task_scored_its_standard_metric" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords task, scored, its, standard, metric, such in title/desc so the matcher can verify semantic overlap.

## Slide 07: key-result

Heading: Key Result

### Cue 1: `cue_s07_c1_flare_benchmark_fine_tuned_finma_mod`

- Preferred role: `result`
- Cue keywords: `flare, benchmark, fine-tuned, finma, models, significantly, outperform, other, large, language`
- Narration: On the FLARE benchmark, the fine-tuned FinMA models significantly outperform other large language models on most financial NLP tasks, including sentiment analysis, headline classification, and named entity recognition.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c1_flare_benchmark_fine_tuned_finma_mod" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords flare, benchmark, fine-tuned, finma, models, significantly in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s07_c2_example_financial_phrase_bank_sentim`

- Preferred role: `method`
- Cue keywords: `example, financial, phrase, bank, sentiment, dataset, finma-30b, outperforms, gpt-4, ten`
- Narration: For example, on the Financial Phrase Bank sentiment dataset, FinMA-30B outperforms GPT-4 by ten percent F1 and BloombergGPT by thirty-seven percent F1. This demonstrates the value of tailoring LLMs to the financial domain through instruction tuning.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s07_c2_example_financial_phrase_bank_sentim" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords example, financial, phrase, bank, sentiment, dataset in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s07_c3_however_finma_underperforms_question`

- Preferred role: `title`
- Cue keywords: `however, finma, underperforms, question, answering, tasks, demand, quantitative, reasoning, limitation`
- Narration: However, FinMA underperforms on question answering tasks that demand quantitative reasoning, a limitation inherited from LLaMA's weak mathematical ability.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s07_c3_however_finma_underperforms_question" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords however, finma, underperforms, question, answering, tasks in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s07_c4_across_all_models_stock_movement`

- Preferred role: `result`
- Cue keywords: `across, all, models, stock, movement, prediction, remains, challenging, leaving, clear`
- Narration: And across all models, stock movement prediction remains challenging, leaving clear room for future improvement.
- Authoring: Create or label one visible result region for this narration chunk. Use id="cue_s07_c4_across_all_models_stock_movement" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords across, all, models, stock, movement, prediction in title/desc so the matcher can verify semantic overlap.

## Slide 08: ablation-study

Heading: Ablation Study

### Cue 1: `cue_s08_c1_comparing_variants_revealing`

- Preferred role: `content`
- Cue keywords: `comparing, variants, revealing`
- Narration: Comparing model variants is revealing.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s08_c1_comparing_variants_revealing" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords comparing, variants, revealing in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s08_c2_finma_30b_shows_significantly_better`

- Preferred role: `method`
- Cue keywords: `finma-30b, shows, significantly, better, performance, finma-7b, most, nlp, tasks, stock`
- Narration: FinMA-30B shows no significantly better performance than FinMA-7B on most NLP tasks or on stock movement prediction, indicating that the quality and diversity of the instruction data matter more than sheer parameter count.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c2_finma_30b_shows_significantly_better" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finma-30b, shows, significantly, better, performance, finma-7b in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s08_c3_scale_does_help_complex_quantitative`

- Preferred role: `title`
- Cue keywords: `scale, does, help, complex, quantitative, question, answering, like, convfinqa, mirroring`
- Narration: Scale does help on complex quantitative question answering like ConvFinQA, mirroring LLaMA's improved math ability at larger sizes, though it still trails GPT-4.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s08_c3_scale_does_help_complex_quantitative" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords scale, does, help, complex, quantitative, question in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s08_c4_notably_finma_7b_full_fine_tuned_bot`

- Preferred role: `method`
- Cue keywords: `notably, finma-7b-full, fine-tuned, both, nlp, prediction, tasks, achieves, best, performance`
- Narration: Notably, FinMA-7B-full, fine-tuned on both NLP and prediction tasks, achieves the best performance among all models on the ACL18 stock prediction dataset, highlighting the promise of task-specific instruction tuning for financial prediction.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s08_c4_notably_finma_7b_full_fine_tuned_bot" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords notably, finma-7b-full, fine-tuned, both, nlp, prediction in title/desc so the matcher can verify semantic overlap.

## Slide 09: headline-numbers

Heading: Headline Numbers

### Cue 1: `cue_s09_c1_few_numbers_capture_pixiu_impact`

- Preferred role: `method`
- Cue keywords: `few, numbers, capture, pixiu, impact, fit, instruction, dataset, holds, one`
- Narration: A few numbers capture PIXIU's impact. The FIT instruction dataset holds one hundred thirty-six thousand samples across five tasks and nine datasets.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s09_c1_few_numbers_capture_pixiu_impact" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords few, numbers, capture, pixiu, impact, fit in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s09_c2_finma_built_open_llama_seven`

- Preferred role: `content`
- Cue keywords: `finma, built, open, llama, seven, thirty, billion, parameters`
- Narration: FinMA is built on the open LLaMA model at seven and thirty billion parameters.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c2_finma_built_open_llama_seven" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finma, built, open, llama, seven, thirty in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s09_c3_financial_phrase_bank_sentiment_task`

- Preferred role: `content`
- Cue keywords: `financial, phrase, bank, sentiment, task, finma-30b, exceeds, gpt-4, ten, percent`
- Narration: On the Financial Phrase Bank sentiment task, FinMA-30B exceeds GPT-4 by ten percent F1 and BloombergGPT by thirty-seven percent F1, reaching a weighted F1 around zero point eight eight.
- Authoring: Create or label one visible content region for this narration chunk. Use id="cue_s09_c3_financial_phrase_bank_sentiment_task" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords financial, phrase, bank, sentiment, task, finma-30b in title/desc so the matcher can verify semantic overlap.

### Cue 4: `cue_s09_c4_finma_achieves_state_of_the_art_thre`

- Preferred role: `title`
- Cue keywords: `finma, achieves, state-of-the-art, three, financial, nlp, tasks, one, financial, prediction`
- Narration: FinMA achieves state-of-the-art on three financial NLP tasks and one financial prediction dataset, all while being fully open-sourced.
- Authoring: Create or label one visible title region for this narration chunk. Use id="cue_s09_c4_finma_achieves_state_of_the_art_thre" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords finma, achieves, state-of-the-art, three, financial, nlp in title/desc so the matcher can verify semantic overlap.

## Slide 10: takeaway

Heading: Takeaway

### Cue 1: `cue_s10_c1_takeaway_simple`

- Preferred role: `takeaway`
- Cue keywords: `takeaway, simple`
- Narration: The takeaway is simple.
- Authoring: Create or label one visible takeaway region for this narration chunk. Use id="cue_s10_c1_takeaway_simple" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords takeaway, simple in title/desc so the matcher can verify semantic overlap.

### Cue 2: `cue_s10_c2_pixiu_provides_financial_community_i`

- Preferred role: `method`
- Cue keywords: `pixiu, provides, financial, community, its, first, fully, open, triad, instruction-following`
- Narration: PIXIU provides the financial AI community with its first fully open triad: an instruction-following financial large language model, a large multi-task instruction dataset, and a holistic evaluation benchmark.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c2_pixiu_provides_financial_community_i" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords pixiu, provides, financial, community, its, first in title/desc so the matcher can verify semantic overlap.

### Cue 3: `cue_s10_c3_shows_careful_domain_instruction_tun`

- Preferred role: `method`
- Cue keywords: `shows, careful, domain, instruction, tuning, let, relatively, small, open, beat`
- Narration: It shows that careful domain instruction tuning can let a relatively small open model beat far larger general-purpose systems on financial language tasks, while honestly exposing quantitative reasoning and stock movement prediction as the field's remaining open challenges.
- Authoring: Create or label one visible method region for this narration chunk. Use id="cue_s10_c3_shows_careful_domain_instruction_tun" when possible; otherwise include this value in data-cue-label/title/desc. Also include the cue keywords shows, careful, domain, instruction, tuning, let in title/desc so the matcher can verify semantic overlap.
