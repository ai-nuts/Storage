# Ablation Study

Core claim: Removing all three URS structuring losses drops WikiTQ accuracy from 65.6% to 60.8%; the three losses (clustering, separation, sparsification) must act together to help. Fusing unsupervised and cell-based relevance (λuns=0.7, λcell=0.3) beats either alone.

Supporting detail: Using cell-based relevance alone (λuns=0, λcell=1) collapses performance (WikiTQ 37.6%), showing the unsupervised scorer is the primary signal and the parsing-statement module is a complementary aid.

Narration: Ablations confirm both components are needed. For the Unsupervised Relevance Scorer, applying clustering, centroid-separation, and sparsification losses together lifts WikiTQ accuracy from sixty point eight to sixty-five point six percent, whereas any subset gives little benefit, showing the three losses only help in combination. For the two relevance signals, fusing the unsupervised score at weight zero point seven with the cell-based score at weight zero point three is optimal, giving sixty-nine point one percent on WikiTQ. Relying on the cell-based signal alone collapses accuracy to thirty-seven point six percent, confirming the unsupervised scorer is the primary driver and the parsing-statement module is a complementary aid.
