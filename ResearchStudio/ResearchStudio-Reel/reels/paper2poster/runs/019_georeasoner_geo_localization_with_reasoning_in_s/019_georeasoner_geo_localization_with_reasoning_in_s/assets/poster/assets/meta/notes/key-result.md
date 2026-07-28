# Key Result

Core claim: GeoReasoner outperforms the best counterpart LVLM (Qwen-VL) by 25.02% at country-level and 38.61% at city-level geo-localization in F1, reaching country F1 of 0.9033 and city F1 of 0.8585, and slightly surpasses the geo-specialist StreetCLIP (0.8854 / 0.8543) despite training on 70K street views versus StreetCLIP's 1.1 million.

Supporting detail: Higher proportions of high-locatability training images monotonically improve accuracy, rising from 0.63/0.47 (country/city) with 0% high-locatability data to 0.72/0.51 with 100%, confirming that data quality, not just quantity, drives performance.

Narration: The headline result is decisive. Measured by F1 score, GeoReasoner beats the strongest comparable vision-language model, Qwen-VL, by just over twenty-five percent at country level and nearly thirty-nine percent at city level, reaching a country F1 of zero point nine zero and a city F1 of zero point eight six. Even more striking, it edges out StreetCLIP, a model built specifically for geo-localization and trained on one point one million street views, while GeoReasoner uses only seventy thousand. The authors also show that as the fraction of high-locatability images in training rises from zero to one hundred percent, accuracy climbs steadily, proving that the quality of the curated data, not merely its quantity, is what powers the gains.
