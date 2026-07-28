# Headline Numbers

Core claim: - Up to 83% of nearest-neighbor searches saved with no perplexity loss. - Up to 1.85 lower perplexity when the search budget is kept. - 81% of searches saved on WikiText-103 while matching kNN-LM.

Supporting detail: - Law-MT: perplexity 12.34 → 10.49 at FoSS=0. - Fine-tuned Law-MT LM: 8.61 → 7.10 perplexity, a 17.5% relative reduction. - Pointers-only (no clustering) still saves >60% of searches at matched perplexity.

Narration: The headline numbers are simple to remember. RetoMaton saves up to eighty-three percent of nearest-neighbor searches with no loss in perplexity, or alternatively lowers perplexity by as much as one point eight five when the search budget is kept. On WikiText-103 it matches kNN-LM while skipping eighty-one percent of searches. And on a fine-tuned law-domain model it pushes perplexity from eight point six one down to seven point one zero, a relative reduction of more than seventeen percent.
