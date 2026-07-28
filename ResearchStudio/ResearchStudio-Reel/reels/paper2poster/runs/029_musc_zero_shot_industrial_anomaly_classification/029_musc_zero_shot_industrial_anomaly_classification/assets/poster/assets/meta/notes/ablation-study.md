# Ablation Study

Core claim: Using all three aggregation degrees r∈{1,3,5} in LNAMD gives the best combined AC/AS (small r for small defects on VisA, large r for large defects on MVTec AD). For MSM, averaging the minimum 30% interval (30% + mean) is optimal, reaching 97.8% AC on MVTec AD versus 83.8% for a max strategy. RsCIN lifts VisA image-AUROC from 90.0% to 92.8%.

Supporting detail: Figure 7 confirms the minimum 30% interval selection gives the best comprehensive AC and AS across both datasets.

Narration: Ablations confirm each choice. Combining three aggregation degrees works best: small neighborhoods catch tiny VisA defects, large ones catch big MVTec defects. Averaging the smallest thirty percent interval beats the max or range, lifting AUROC to ninety-seven point eight percent. Re-scoring raises VisA image AUROC from ninety to ninety-two point eight.
