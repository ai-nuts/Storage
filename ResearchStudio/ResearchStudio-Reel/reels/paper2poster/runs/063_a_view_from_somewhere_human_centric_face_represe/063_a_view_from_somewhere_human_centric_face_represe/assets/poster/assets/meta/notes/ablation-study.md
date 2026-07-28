# Ablation Study

Core claim: Randomly swapping annotator masks across the 80,300 judgments drops AVFS-CPH accuracy from 61.7% to 52.8% ± 0.02%, showing annotators are not interchangeable.

Supporting detail: Dimension-elimination shows only 6–13 dimensions recover 95–99% of predictive accuracy, while 15–22 dimensions are needed to explain 95–99% of the similarity-matrix variance, evidencing context-dependent similarity.

Narration: To test whether annotators really matter, the authors randomly shuffle which annotator mask is attached to each of the eighty thousand judgments and recompute accuracy a hundred times over. Accuracy drops from about sixty-two percent down to roughly fifty-three percent, proving that annotators are genuinely not interchangeable. A dimension-elimination analysis further shows that only six to thirteen dimensions are needed to recover most of the predictive accuracy, while fifteen to twenty-two dimensions are required to explain the full similarity structure, clear evidence that similarity is context-dependent.
