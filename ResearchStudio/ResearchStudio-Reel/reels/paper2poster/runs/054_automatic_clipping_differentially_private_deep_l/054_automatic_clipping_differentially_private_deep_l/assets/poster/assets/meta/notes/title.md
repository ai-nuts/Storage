# Title

This work, from AWS AI and UC Santa Barbara, is titled "Automatic Clipping: Differentially Private Deep Learning Made Easier and Stronger." Differentially private training of deep networks relies on per-sample gradient clipping, but the clipping threshold R is a fragile hyperparameter that must be tuned carefully for good accuracy. The authors propose automatic clipping, a drop-in replacement that removes R entirely from any DP optimizer, so private training becomes as tuning-friendly as ordinary training while matching or beating the state of the art.
