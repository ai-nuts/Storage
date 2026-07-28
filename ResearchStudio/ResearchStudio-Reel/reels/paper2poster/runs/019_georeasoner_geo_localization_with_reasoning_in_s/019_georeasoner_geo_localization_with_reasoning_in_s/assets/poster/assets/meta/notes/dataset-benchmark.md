# Dataset / Benchmark

Core claim: The authors curate two new resources: over 130K geo-tagged GSV images from 72 cities across 48 countries (filtered to 70K high-locatability images at threshold 0.4), and over 3K reasoned text-image clue pairs harvested from the GeoGuessr and Tuxun communities and cleaned with BERT-based NER.

Supporting detail: Evaluation uses a held-out set of 1K GSV images for country/city accuracy, plus the open Im2GPS and Im2GPS3k Flickr benchmarks for generalizability, where GeoReasoner is fine-tuned on only 10K Flickr images.

Narration: The paper builds its data from scratch. Using OpenStreetMap road networks and the Google Street View API, the authors sample points every four thousand meters across the top global cities, collecting more than one hundred thirty thousand geo-tagged street views spanning seventy-two cities in forty-eight countries. Applying the locatability filter at a threshold of zero point four yields roughly seventy thousand high-quality images. Separately, they scrape over three thousand textual clues from two geo-localization games, GeoGuessr and Tuxun, cleaning them with a BERT-based entity recognizer and pairing each with a street-view image. For evaluation they use a held-out set of a thousand images and, to test generalization, the standard Im2GPS and Im2GPS3k Flickr benchmarks.
