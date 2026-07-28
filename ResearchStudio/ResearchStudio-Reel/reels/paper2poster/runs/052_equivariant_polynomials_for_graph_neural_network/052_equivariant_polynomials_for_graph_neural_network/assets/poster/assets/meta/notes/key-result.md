# Key Result

Core claim: PPGN++ with high-degree polynomial features sets state of the art on all three regression benchmarks, reaching test MAE 0.071 on ZINC-12K, 0.020 on ZINC-full, and 0.109 on Alchemy, and precomputing polynomial features gives provably strictly better than 3-WL expressive power while remaining efficient.

Supporting detail: Polynomial features also sharply improve weaker backbones: GatedGCN's ZINC-12K MAE drops from 0.265 to 0.106 once degree-6 polynomial features are added.

Narration: The result is state of the art across the board. On ZINC-12K, PPGN plus plus with degree-six polynomial features reaches 0.071 test error, beating CIN at 0.079 and GIN at 0.163. On ZINC-full it hits 0.020 and on Alchemy 0.109, both best in class. And the features are model-agnostic: adding them to a plain GatedGCN cuts its ZINC error from 0.265 to 0.106, all under a modest parameter budget.
