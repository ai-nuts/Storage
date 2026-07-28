---
title: CABINET: Content Relevance-Based Noise Reduction for Table Question Answering
authors: Sohan Patnaik¹², Heril Changwal¹³, Milan Aggarwal¹, Sumit Bhatia¹, Yaman Kumar Singla¹, Balaji Krishnamurthy¹
institutes: ¹MDSR Lab, Adobe; ²IIT Kharagpur; ³IIT Roorkee
venue: ICLR 2024
paper_url: https://arxiv.org/abs/2402.01155
code_url: https://github.com/Sohanpatnaik106/CABINET_QA
title_audio_script: This is CABINET, a framework for table question answering published at ICLR 2024 by researchers at Adobe's MDSR Lab together with IIT Kharagpur and IIT Roorkee. Large language models reason over tables, but only a few cells usually matter for any given question, and the irrelevant cells act as noise that hurts accuracy. CABINET tackles this by teaching the model to focus on relevant table content and suppress the rest, rather than deleting parts of the table outright. It sets new state of the art on three challenging table QA benchmarks.
---

## Problem
**Necessary:** In table question answering, only a few cells matter for a given question; the rest act as noise, and LLMs are vulnerable to this irrelevant content, producing sub-optimal answers.
**Additional:** Degradation worsens on large tables where even more irrelevant data is present, amplifying the distraction for the QA model.
**Audio script:** Tables organize information across rows and columns, but for any single question only a small number of cells actually contain the answer. Everything else is irrelevant to that question and behaves like noise. Large language models are known to be susceptible to such distracting information, so their table reasoning degrades, and the problem gets worse as tables grow larger and carry even more irrelevant content. CABINET is built to address exactly this vulnerability.

## Motivation
**Necessary:** Prior in-context methods like DATER hard-decompose a table into a sub-table, which can discard useful cells and lock in errors when the wrong sub-table is selected.
**Additional:** Explicitly removing table content is brittle; a soft relevance-weighting scheme keeps all information available while still de-emphasizing noise.
**Audio script:** A natural way to reduce noise is to shrink the table before answering, and methods like DATER do this by decomposing the table into a smaller sub-table. The trouble is that hard decomposition is unforgiving: if the wrong sub-table is extracted, useful information is permanently lost and the reasoner answers incorrectly with no way to recover. CABINET argues for a softer approach that weighs relevant parts higher without ever explicitly removing content, so the answering model retains access to the whole table while being steered toward what matters.

## Contribution
**Necessary:** CABINET, a framework that suppresses irrelevant table content via a differentiable Unsupervised Relevance Scorer plus a weakly-supervised parsing-statement module that highlights question-relevant cells, trained end-to-end with the QA LLM.
**Additional:** It establishes new state of the art on WikiTQ, FeTaQA, and WikiSQL, and demonstrates markedly greater robustness to table perturbations and to increasing table size.
**Audio script:** The paper contributes CABINET, short for Content Relevance-Based Noise Reduction. It has two cooperating parts. First, an Unsupervised Relevance Scorer assigns a soft relevance weight to every table token and is trained differentiably alongside the question-answering model. Second, a weakly-supervised module generates a parsing statement describing which rows and columns matter, then highlights the corresponding cells to produce a cell-based relevance signal. Together they let the model focus without discarding content, and they deliver new state of the art on three benchmarks along with stronger robustness to noise and to large tables.

## Method
**Necessary:** The table is linearized and embedded with the question; an Unsupervised Relevance Scorer (a transformer encoder trained via variational inference with clustering, separation, and sparsification losses) assigns each table token a relevance score that multiplies its embedding before the QA LLM decodes the answer.
**Additional:** In parallel, a Parsing Statement Generator (Flan T5-xl, bootstrapped from ~300 annotations) produces criteria for relevant rows/columns, and a cell highlighter yields a cell-based score; the unsupervised and cell-based scores are linearly fused into the final relevance weight. The QA backbone is OmniTab (560M).
**Audio script:** CABINET works in a sequence of steps. The table is flattened into a linear string with header and row markers and embedded together with the question. An Unsupervised Relevance Scorer, a transformer encoder, reads this and predicts a relevance score for each table token. Because there are no ground-truth annotations for which cells are relevant, relevance is treated as a latent variable estimated through variational inference, and the encoder's representation space is shaped by a clustering loss that groups tokens into relevant and non-relevant, a separation loss that pushes the two cluster centroids apart, and a sparsification loss that drives irrelevant scores toward zero and relevant scores toward one. Each table token's embedding is multiplied by its relevance score, so noisy cells are softly suppressed rather than deleted, and the whole system trains end-to-end through the answer-generation cross-entropy loss. In parallel a weakly-supervised Parsing Statement Generator, a fine-tuned Flan T5-xl bootstrapped from only about three hundred manual annotations, writes a natural-language description of which rows and columns are relevant, and a cell highlighter turns that into a cell-based relevance score. The unsupervised and cell-based scores are linearly combined into the final weight applied to the table.
**Key equation:** `$\eta_p^{uns} = \mathrm{sigmoid}(z_p),\; z_p = \mu_p + s\cdot\sigma_p$`; `$\mathcal{L} = \mathcal{L}_{CE} + \lambda_{clu}\mathcal{L}_{clu} + \lambda_{sep}\mathcal{L}_{sep} + \lambda_{sparse}\mathcal{L}_{sparse}$`; `$\eta_p = \lambda_{uns}\,\eta_p^{uns} + \lambda_{cell}\,\eta_p^{cell}$`

## Dataset / Benchmark
**Necessary:** Evaluated on three table QA benchmarks: WikiTableQuestions (WikiTQ) and WikiSQL, scored by exact-match accuracy, and FeTaQA, scored by Sacre-BLEU for long free-form answers.
**Additional:** WikiTQ is among the most complex table QA datasets requiring compositional reasoning; the authors also release a dataset of ~300 manually written parsing statements to bootstrap the weakly-supervised module.
**Audio script:** CABINET is evaluated on three challenging table question-answering benchmarks. WikiTableQuestions, or WikiTQ, requires compositional reasoning over tables and uses short one-to-two-word answers scored by exact-match accuracy. WikiSQL similarly uses exact-match accuracy. FeTaQA asks for long, free-form descriptive answers, which are scored with Sacre-BLEU. The authors additionally release a small dataset of about three hundred manually written parsing statements used to bootstrap the weakly-supervised cell-highlighting module.

## Key Result
**Necessary:** CABINET sets new state of the art on all three datasets: 69.1% accuracy on WikiTQ, 40.5 Sacre-BLEU on FeTaQA, and 89.5% accuracy on WikiSQL, all with a 560M-parameter model.
**Additional:** On WikiTQ it beats OmniTab, DATER, and fine-tuned Flan T5-xl by 6.4%, 3.2%, and 4.7% absolute respectively, and outperforms GPT-3 / Codex-based in-context learning methods.
**Audio script:** CABINET establishes new state of the art on all three benchmarks. On WikiTQ it reaches sixty-nine point one percent exact-match accuracy, outperforming the strongest baseline in each category, including OmniTab, DATER, and fine-tuned Flan T5-xl by six point four, three point two, and four point seven absolute percentage points, and it beats much larger GPT-3 and Codex based in-context learning methods. On FeTaQA it achieves a Sacre-BLEU of forty point five, and on WikiSQL it reaches eighty-nine point five percent accuracy, pushing past the previous best. Notably all of this is achieved with a compact five hundred sixty million parameter model.

## Ablation Study
**Necessary:** Removing all three URS structuring losses drops WikiTQ accuracy from 65.6% to 60.8%; the three losses (clustering, separation, sparsification) must act together to help. Fusing unsupervised and cell-based relevance (λuns=0.7, λcell=0.3) beats either alone.
**Additional:** Using cell-based relevance alone (λuns=0, λcell=1) collapses performance (WikiTQ 37.6%), showing the unsupervised scorer is the primary signal and the parsing-statement module is a complementary aid.
**Audio script:** Ablations confirm both components are needed. For the Unsupervised Relevance Scorer, applying clustering, centroid-separation, and sparsification losses together lifts WikiTQ accuracy from sixty point eight to sixty-five point six percent, whereas any subset gives little benefit, showing the three losses only help in combination. For the two relevance signals, fusing the unsupervised score at weight zero point seven with the cell-based score at weight zero point three is optimal, giving sixty-nine point one percent on WikiTQ. Relying on the cell-based signal alone collapses accuracy to thirty-seven point six percent, confirming the unsupervised scorer is the primary driver and the parsing-statement module is a complementary aid.

## Headline Numbers
**Necessary:**
- WikiTQ: 69.1% accuracy (new SoTA, +6.4% over OmniTab)
- FeTaQA: 40.5 Sacre-BLEU (new SoTA)
- WikiSQL: 89.5% accuracy (new SoTA)
- Model size: 560M parameters (OmniTab backbone)
**Additional:** More robust under table perturbations (row/column permutation, cell replacement) and maintains its lead as table size grows; ~11.5% smaller performance drop than OmniTab under perturbation on WikiTQ.
**Audio script:** The headline numbers are sixty-nine point one percent accuracy on WikiTQ, a Sacre-BLEU of forty point five on FeTaQA, and eighty-nine point five percent accuracy on WikiSQL, each a new state of the art achieved with just five hundred sixty million parameters. Beyond raw accuracy, CABINET is markedly more robust: under table perturbations such as row and column permutation and cell replacement it degrades far less than baselines, with roughly an eleven and a half percent smaller performance drop than OmniTab on WikiTQ, and it holds its advantage as tables grow larger.

## Takeaway
**Necessary:** Softly weighting table content by learned relevance, rather than hard-decomposing tables, lets an LLM focus on the cells that matter and sets new state of the art on table QA with a compact model.
**Additional:** Combining an unsupervised, differentiable relevance scorer with a weakly-supervised parsing-statement cell highlighter is both more accurate and more robust to noise than prior removal-based approaches.
**Audio script:** The core lesson of CABINET is that you do not need to cut a table down to answer questions about it. By softly weighting every cell according to a learned relevance score, instead of hard-decomposing the table and risking the loss of useful information, the model keeps full access to the data while being steered toward what matters. Pairing a differentiable unsupervised relevance scorer with a weakly-supervised parsing-statement cell highlighter yields both higher accuracy and greater robustness to noise, setting new state of the art on three table QA benchmarks with a compact five hundred sixty million parameter model.
