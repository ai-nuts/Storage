# Key Result

Core claim: Under equal labeling budget (20 labels/class, GCN), IGP reaches 86.4% on Cora, 75.8% on Citeseer, and 83.6% on PubMed, beating the best baseline GRAIN by 1.6–2.2% on citation networks, 0.9% on Reddit, and 0.6% on ogbn-arxiv.

Supporting detail: IGP's accuracy rises fastest as budget grows, and it stays ahead across every budget size. On PubMed it beats ALG and GRAIN by more than 1.8% across four GNN backbones (SGC, APPNP, GCN, MVGRL).

Narration: Across every dataset and budget, IGP delivers the highest test accuracy. Under twenty labels per class with a GCN, it reaches 86.4 percent on Cora, 75.8 on Citeseer, and 83.6 on PubMed, beating the strongest prior method, GRAIN, by 1.6 to 2.2 percent on citation networks, with smaller but consistent gains on Reddit and ogbn-arxiv. As budget grows, IGP climbs fastest, and the lead holds across backbones.
