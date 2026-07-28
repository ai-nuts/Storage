---
title: Neuro-Symbolic Language Modeling with Automaton-augmented Retrieval
authors: Uri Alon¹, Frank F. Xu¹, Junxian He¹, Sudipta Sengupta², Dan Roth³, Graham Neubig¹
institutes: ¹Language Technologies Institute, Carnegie Mellon University; ²Amazon AWS; ³AWS AI Labs
venue: ICML 2022
paper_url: https://arxiv.org/abs/2201.12431
code_url: https://github.com/neulab/retomaton
title_audio_script: Retrieval-based language models sharpen their predictions by pulling examples from a huge external datastore at test time, but that nearest-neighbor search is slow and runs at almost every single token. This paper introduces RetoMaton, short for retrieval automaton, which builds a weighted finite automaton on top of the datastore. By saving pointers between consecutive entries and clustering entries into states, RetoMaton lets the model follow cheap automaton transitions instead of searching from scratch. The result: up to eighty-three percent fewer nearest-neighbor searches with no loss in perplexity, or up to one point eight five lower perplexity when the search budget is kept.
---

## Problem
**Necessary:** Retrieval-based language models improve quality by searching an external datastore, but that nearest-neighbor search runs as often as every time step and is the dominant computational bottleneck at inference.
**Additional:** The search is far slower than the LM's forward pass, which blocks retrieval LMs from practical deployment despite their accuracy, domain-adaptability, and provenance benefits.
**Audio script:** Retrieval-based language models improve on standard neural models by fetching nearest-neighbor examples from an external datastore and blending them into the prediction. The catch is cost: that datastore search can fire at every single time step, and it is far slower than the model's own forward pass. This frequent search is the single most critical bottleneck that keeps these otherwise powerful models out of practical settings.

## Motivation
**Necessary:** kNN-LM treats the datastore as a flat list and searches it token by token, ignoring that consecutive retrieved entries are highly correlated in time and that nearby keys behave alike.
**Additional:** Prior retrieval-saving work (AdaptRet) trains an MLP to skip searches, but when it skips it backs off to the base LM alone, losing the retrieval signal exactly when it helps most.
**Audio script:** The key observation is that a flat datastore throws away structure. If a retrieved entry was useful now, the entry that follows it in the original text is very likely useful next. And entries whose key vectors are close tend to be followed by the same token. Existing approaches like Adaptive Retrieval simply learn when to skip the search, but when they skip they fall back entirely on the base language model and discard the retrieval distribution, which hurts most in domains where the base model is weak.

## Contribution
**Necessary:** RetoMaton builds an unsupervised weighted finite automaton over any datastore by (1) saving a pointer from each entry to its successor in the text and (2) clustering entries with close keys into automaton states that share pointers.
**Additional:** Traversed in parallel with LM inference, the automaton approximates the next nearest neighbors so most searches are skipped; it needs no training data and can be built from the training corpus or a new domain.
**Audio script:** RetoMaton makes two changes to the datastore. First, it saves a pointer from every entry to the entry that came right after it in the text. Second, it clusters entries with similar key vectors into states, and those states share their outgoing pointers. Together these turn the flat datastore into a weighted finite automaton. Building it is completely unsupervised, requires no extra training data, and works whether the automaton is constructed from the model's own training corpus or from a brand-new domain.

## Method
**Necessary:** At inference the model traverses the automaton in parallel with the LM, visiting a set of states each step. It follows pointers of matching-value entries to predict the next states cheaply; only when the number of valid transitions falls below a threshold τ does it launch a fresh kNN search and restart the traversal.
**Additional:** Transition weights are dynamic, computed from distances between the current LM hidden state and the entries in each state, then interpolated with the base LM. τ trades off accuracy (frequent restarts, more searches) against speed (rare searches). Clustering can use k-means or a cheaper greedy merge.
**Key equation:** `$p(w \mid c, S) = \lambda\, p_{\text{auto}}(w \mid c, S) + (1-\lambda)\, p_{\text{LM}}(w \mid c)$` ; `$p_{\text{auto}}(w \mid c, S) \propto \sum_{q \in S} \varphi(q, c, w)$` ; `$\varphi(q, c, w) = \sum_{(k_i, w_i, \cdot)\in \pi^{-1}(q)} \mathbb{1}_{w=w_i}\exp(-\text{dist}(f(c), k_i))$`
**Audio script:** RetoMaton stores each datastore entry as a triple of key, value, and pointer, where the pointer references the entry that followed it in the corpus. Entries with close keys are clustered into states, and a state inherits all the pointers of its members. At test time the model keeps a small set of active states and traverses the automaton alongside the language model. To move forward it just follows the pointers of entries whose value matches the generated token, which is essentially free. A full nearest-neighbor search is only triggered when the number of valid onward transitions drops below a threshold tau. The automaton's transition weights are computed dynamically from the distance between the current hidden state and the entries in each state, and the resulting distribution is interpolated with the base language model.

## Dataset / Benchmark
**Necessary:** In-domain modeling uses WikiText-103 (103M training tokens, 250K validation and test tokens) with a 247M-parameter Transformer base LM. Domain adaptation uses the English side of Law-MT (19M tokens) with a 656M-parameter Transformer base LM.
**Additional:** For WikiText-103 the datastore holds 103M entries clustered into 1M states; for Law-MT the datastore holds 19M entries clustered into 200K states, keeping an average cluster size near 100 in both. Baselines are the original kNN-LM and AdaptRet.
**Audio script:** The method is evaluated in two settings. For standard in-domain language modeling the authors use WikiText-103, a Wikipedia benchmark with one hundred and three million training tokens, and a two hundred forty seven million parameter Transformer as the base model, producing a datastore of one hundred and three million entries clustered into one million states. For domain adaptation they use the law-domain corpus Law-MT with nineteen million tokens and a larger six hundred fifty six million parameter base model, clustered into two hundred thousand states. Throughout, RetoMaton is compared against the original kNN-LM and against Adaptive Retrieval.

## Key Result
**Necessary:** On WikiText-103, RetoMaton saves 81% of kNN searches while matching kNN-LM perplexity, and even at zero saved searches it lowers perplexity from 16.65 (kNN-LM) and 16.35 (AdaptRet) to 16.08. On Law-MT domain adaptation it cuts perplexity from 12.34 (kNN-LM) to 10.49 at FoSS=0 and degrades only gently as searches are saved, while kNN-LM's perplexity rises sharply.
**Additional:** Across the paper the automaton reduces perplexity by up to 1.85, or saves up to 83% of nearest-neighbor searches without hurting perplexity. Fraction of Saved Searches (FoSS) is used as a hardware-independent proxy for wall-clock savings.
**Audio script:** The results are strong in both regimes. On WikiText-103, RetoMaton matches the perplexity of kNN-LM while skipping eighty-one percent of the searches, and even when it performs a search at every step it still lowers perplexity, because the carried-over pointers reinforce the correct neighbors. On the Law-MT domain-adaptation task the gains are larger and much more robust: perplexity drops from twelve point three four to ten point four nine, and as more searches are saved RetoMaton's perplexity climbs only very gently while plain kNN-LM's perplexity blows up exponentially. Overall the automaton either cuts perplexity by up to one point eight five, or saves up to eighty-three percent of the searches with no loss.

## Ablation Study
**Necessary:** Pointers versus clustering: a pointers-only variant (no clustering) already beats all baselines, reaching 16.12 perplexity at FoSS=0 and matching kNN-LM while saving over 60% of searches, showing pointers drive most of the gain at low FoSS; clustering adds its benefit mainly at high FoSS (≥0.7) by enabling longer search-free runs.
**Additional:** Clustering granularity: on WikiText-103, k=500K and k=1M means give similar perplexity while k=100K is too coarse; the cheaper greedy merge wins at FoSS=0 but degrades as FoSS grows. 98% of validation tokens fall in automaton-continued n-grams with n>1.
**Audio script:** An ablation teases apart the two ingredients. Using pointers alone, with no clustering at all, already beats every baseline and matches kNN-LM while saving more than sixty percent of searches, so the pointers deliver most of the benefit when few searches are saved. Clustering contributes mainly at high saving rates, from about seventy percent onward, where it lets the model stay search-free over longer stretches of text. On cluster count, half a million and one million means perform similarly, while one hundred thousand is too coarse, and a cheaper greedy clustering wins at zero saved searches but fades as the saving fraction grows.

## Headline Numbers
**Necessary:**
- Up to 83% of nearest-neighbor searches saved with no perplexity loss.
- Up to 1.85 lower perplexity when the search budget is kept.
- 81% of searches saved on WikiText-103 while matching kNN-LM.
**Additional:**
- Law-MT: perplexity 12.34 → 10.49 at FoSS=0.
- Fine-tuned Law-MT LM: 8.61 → 7.10 perplexity, a 17.5% relative reduction.
- Pointers-only (no clustering) still saves >60% of searches at matched perplexity.
**Audio script:** The headline numbers are simple to remember. RetoMaton saves up to eighty-three percent of nearest-neighbor searches with no loss in perplexity, or alternatively lowers perplexity by as much as one point eight five when the search budget is kept. On WikiText-103 it matches kNN-LM while skipping eighty-one percent of searches. And on a fine-tuned law-domain model it pushes perplexity from eight point six one down to seven point one zero, a relative reduction of more than seventeen percent.

## Takeaway
**Necessary:** Turning a retrieval datastore into a pointer-and-cluster automaton lets a language model reuse retrieval across time steps, so it skips most costly nearest-neighbor searches while matching or beating perplexity.
**Additional:** The construction is unsupervised, model-agnostic, and works across domains, generalizing token, chunk, and sequence retrieval within a single dynamic mechanism.
**Audio script:** The lasting idea is that a retrieval datastore has structure worth exploiting. By linking consecutive entries with pointers and grouping similar ones into automaton states, RetoMaton lets a language model carry retrieval forward in time instead of searching from scratch at every token. It is unsupervised, works with any base model, transfers across domains, and unifies token, chunk, and sequence retrieval, all while cutting the dominant cost of retrieval-based language modeling.
