# Motivation

Core claim: To predict single-cell drug responses we need nonlinear maps that model both feature shifts and mass changes; prior neural OT methods either assume balance or only crudely rescale mass, missing per-cell proliferation and death.

Supporting detail: Aggregate or mechanistic models cannot capture the heterogeneous, cell-type-specific responses that drive treatment outcomes.

Narration: Cellular responses to drugs are highly heterogeneous: different cell types and states can respond in opposite ways, some proliferating while others die. Capturing this requires nonlinear maps at the level of single cells, not aggregate averages. Prior neural optimal transport methods can learn such maps, but they either assume the balanced setting where mass is conserved, or, like the state-of-the-art unbalanced GAN approach, they only capture the general trend of growth and shrinkage without recovering the exact reweighting each subpopulation needs. What has been missing is a method that jointly and accurately models where mass moves and how much of it is created or destroyed, in a way that stays faithful to the biology.
