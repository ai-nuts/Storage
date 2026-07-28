# Ablation Study

Core claim: Pointers versus clustering: a pointers-only variant (no clustering) already beats all baselines, reaching 16.12 perplexity at FoSS=0 and matching kNN-LM while saving over 60% of searches, showing pointers drive most of the gain at low FoSS; clustering adds its benefit mainly at high FoSS (≥0.7) by enabling longer search-free runs.

Supporting detail: Clustering granularity: on WikiText-103, k=500K and k=1M means give similar perplexity while k=100K is too coarse; the cheaper greedy merge wins at FoSS=0 but degrades as FoSS grows. 98% of validation tokens fall in automaton-continued n-grams with n>1.

Narration: An ablation teases apart the two ingredients. Using pointers alone, with no clustering at all, already beats every baseline and matches kNN-LM while saving more than sixty percent of searches, so the pointers deliver most of the benefit when few searches are saved. Clustering contributes mainly at high saving rates, from about seventy percent onward, where it lets the model stay search-free over longer stretches of text. On cluster count, half a million and one million means perform similarly, while one hundred thousand is too coarse, and a cheaper greedy clustering wins at zero saved searches but fades as the saving fraction grows.
