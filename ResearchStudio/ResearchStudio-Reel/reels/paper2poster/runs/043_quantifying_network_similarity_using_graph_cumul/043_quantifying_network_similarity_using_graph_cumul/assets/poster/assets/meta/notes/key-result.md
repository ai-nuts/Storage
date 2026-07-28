# Key Result

Core claim: Across synthetic SBM comparisons, the cumulant test achieves consistently higher AUC than the moment test, with the largest gains when the number of graphs per sample s is small; the moment test fails entirely for s < 4 (singular covariance), whereas the cumulant test works even for s = 1.

Supporting detail: On real genetic-interaction networks with matched edge density, including more subgraphs (r = 2 then r = 3) steadily improves the cumulant test but causes the moment test to overfit and degrade.

Narration: The results are decisive. On synthetic block models, the test using cumulants achieves a consistently higher area under the ROC curve than the test using moments, and the advantage widens as the number of graphs per sample shrinks. The moment test breaks down entirely below four graphs per sample, where its covariance estimate becomes singular, while the cumulant test keeps working all the way down to a single graph. The same pattern holds on real biological networks: with edge density held equal, adding more subgraph orders steadily sharpens the cumulant test, whereas it makes the moment test overfit and perform worse.
