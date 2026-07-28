# Problem

Core claim: Building graph neural networks with guaranteed expressive power usually means proving a model matches the k-Weisfeiler-Lehman test after it is designed, and no systematic procedure exists to derive a GNN from a given expressive language fragment.

Supporting detail: Existing 3-WL models like 3-IGN are memory-heavy (basis size grows as the 2k-th Bell number) and PPGN, though tractable, is only shown to mimic 2-FWL without a constructive language-to-model link.

Narration: How expressive is a graph neural network? For years the field has answered that with the Weisfeiler-Lehman hierarchy, and the gold standard has been to design a model and then prove it matches, say, the third-order test. But that proof comes after the design, almost as an afterthought. What has been missing is a systematic way to go the other direction: to start from a language we already know is exactly as powerful as 3-W-L, and mechanically build a network that inherits that power. Without such a recipe, every expressive architecture is a fresh, hand-crafted proof.
