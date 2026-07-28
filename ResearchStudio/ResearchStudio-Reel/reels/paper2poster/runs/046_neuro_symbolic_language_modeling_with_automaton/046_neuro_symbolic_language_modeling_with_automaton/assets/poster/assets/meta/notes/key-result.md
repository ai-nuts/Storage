# Key Result

Core claim: On WikiText-103, RetoMaton saves 81% of kNN searches while matching kNN-LM perplexity, and even at zero saved searches it lowers perplexity from 16.65 (kNN-LM) and 16.35 (AdaptRet) to 16.08. On Law-MT domain adaptation it cuts perplexity from 12.34 (kNN-LM) to 10.49 at FoSS=0 and degrades only gently as searches are saved, while kNN-LM's perplexity rises sharply.

Supporting detail: Across the paper the automaton reduces perplexity by up to 1.85, or saves up to 83% of nearest-neighbor searches without hurting perplexity. Fraction of Saved Searches (FoSS) is used as a hardware-independent proxy for wall-clock savings.

Narration: The results are strong in both regimes. On WikiText-103, RetoMaton matches the perplexity of kNN-LM while skipping eighty-one percent of the searches, and even when it performs a search at every step it still lowers perplexity, because the carried-over pointers reinforce the correct neighbors. On the Law-MT domain-adaptation task the gains are larger and much more robust: perplexity drops from twelve point three four to ten point four nine, and as more searches are saved RetoMaton's perplexity climbs only very gently while plain kNN-LM's perplexity blows up exponentially. Overall the automaton either cuts perplexity by up to one point eight five, or saves up to eighty-three percent of the searches with no loss.
