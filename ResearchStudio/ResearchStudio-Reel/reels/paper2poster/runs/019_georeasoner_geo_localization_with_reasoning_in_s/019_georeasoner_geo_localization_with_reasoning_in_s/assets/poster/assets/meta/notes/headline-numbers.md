# Headline Numbers

Core claim: - +25.02% country-level and +38.61% city-level F1 over the best counterpart LVLM (Qwen-VL) - Country F1 0.9033 / City F1 0.8585 for the full GeoReasoner - 70K high-locatability training images vs. 1.1M for StreetCLIP (which it still surpasses)

Supporting detail: - 130K+ raw GSV images from 72 cities / 48 countries, filtered to 70K at locatability threshold 0.4 - 3K reasoned text-image clue pairs mined from GeoGuessr and Tuxun - Only 10K Flickr images needed to match ISNs/GeoCLIP on Im2GPS / Im2GPS3k

Narration: The numbers that matter: GeoReasoner improves on the best comparable vision-language model by twenty-five point zero two percent at the country level and thirty-eight point six one percent at the city level in F1. Its full-model F1 scores are zero point nine zero for country and zero point eight six for city. It achieves this with just seventy thousand training images, versus the one point one million used by StreetCLIP, which it nonetheless surpasses. The underlying data comes from more than one hundred thirty thousand raw street views across seventy-two cities and forty-eight countries, filtered down to seventy thousand, plus three thousand human-written reasoning clues from geo-games. And on the open Im2GPS benchmarks, only ten thousand Flickr images are enough to rival models trained on millions.
