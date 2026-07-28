#!/usr/bin/env python3
import re, sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    # titlebar / metadata
    "{{TITLE}}": "GeoReasoner: Geo-localization with Reasoning in Street Views using a Large Vision-Language Model",
    "{{AUTHORS}}": ("Ling Li<sup>1</sup>, Yu Ye<sup>2</sup>, Yao Zhou<sup>3</sup>, "
                    "Bingchuan Jiang<sup>4</sup>, Wei Zeng<sup>1,5</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> HKUST (Guangzhou) &nbsp;&nbsp; <sup>2</sup> Tongji University &nbsp;&nbsp; "
                          "<sup>3</sup> Independent Researcher &nbsp;&nbsp; <sup>4</sup> Information Engineering University "
                          "&nbsp;&nbsp; <sup>5</sup> HKUST"),
    "{{CONTACT}}": "Email: jbc021@163.com",
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/the-hong-kong-university-of-science-and-technology.png",
    "{{LOGO_2}}": "assets/logos/tongji-university.png",
    "{{LOGO_3}}": "assets/logos/pla-information-engineering-university.png",
    "{{LOGO_4}}": "", "{{LOGO_5}}": "", "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "", "{{QR_CODE}}": "",
    # ablation lives only in a commented-out block in 3col; neutralize the tokens
    "{{ABLATION_1}}": "", "{{ABLATION_2}}": "", "{{ABLATION_CONCLUSION}}": "",

    # Problem
    "{{PROBLEM}}": ("Street-view geo-localization models are <strong>black boxes</strong> that output a location "
                    "with no reasoning, and the datasets used to train them are polluted with "
                    "<strong>low-quality images</strong> that carry no visual clues to where they were taken."),

    # Motivation
    "{{MOTIVATION_1}}": ("Large vision-language models excel at joint visual-textual reasoning, and reasoning boosts "
                         "capability &mdash; a natural fit for <strong>interpretable</strong> geo-localization."),
    "{{MOTIVATION_2}}": ("Online geo-games (<strong>GeoGuessr</strong>, <strong>Tuxun</strong>) hold rich human clues "
                         "encoding exactly the domain knowledge no prior street-view dataset provides."),
    "{{TEASER_FIGURE}}": "assets/figures/figure1.png",
    "{{TEASER_CAPTION}}": ("Three geo-localization paradigms: retrieval-based, classification-based, and our "
                           "LVLM-based approach with reasoning."),

    # Method
    "{{METHOD_1}}": ("Built on <strong>Qwen-VL</strong> (Vision Encoder + VL Adapter + pre-trained LLM), fine-tuned "
                     "in two stages with stacked <strong>LoRA</strong> adapters."),
    "{{METHOD_2}}": ("<strong>Reasoning tuning</strong> on 3K game-sourced pairs teaches country-level reasoning; "
                     "<strong>location tuning</strong> on 70K high-locatability GSV images sharpens city-level "
                     "prediction. A <strong>locatability metric</strong> filters the data upstream."),
    "{{METHOD_FIGURE}}": "assets/figures/figure3.png",
    "{{METHOD_CAPTION}}": ("GeoReasoner: a two-stage supervised fine-tuning process &mdash; reasoning tuning then "
                           "location tuning &mdash; enabling geo-localization with reasoning."),
    "{{KEY_EQUATION}}": r"\mathrm{locatability} = \sum_{k=1}^{n} I_{seg}(k)\,w_k^{loc}",
    "{{KEY_EQUATION_NOTE}}": "class-area ratios weighted by clue relevance",

    # Dataset / Benchmark (first-class: paper introduces the data)
    "{{DATASET_1}}": ("<strong>130K+</strong> geo-tagged GSV images from <strong>72 cities</strong> / "
                      "<strong>48 countries</strong>, filtered to <strong>70K</strong> high-locatability images "
                      "at threshold 0.4."),
    "{{DATASET_2}}": ("<strong>3K</strong> reasoned text-image clue pairs mined from GeoGuessr &amp; Tuxun and cleaned "
                      "with BERT-based NER; evaluated on 1K held-out GSV plus Im2GPS / Im2GPS3k."),

    # Key Result (table rewritten to 3-col via post-build edit)
    "{{BASELINE}}": "Qwen-VL", "{{BASELINE_NUM}}": "0.7225 / 0.5270",
    "{{OURS}}": "GeoReasoner", "{{OURS_NUM}}": "0.9033 / 0.8585",
    "{{HEADLINE_DELTA}}": "+25.02% country &middot; +38.61% city F1 over Qwen-VL",
    "{{KEY_RESULT_CONCLUSION}}": ("Matches the geo-specialist StreetCLIP while training on 70K images vs its 1.1M "
                                  "&mdash; data quality beats sheer scale."),
    "{{SECONDARY_FIGURE}}": "assets/figures/figure7.png",
    "{{SECONDARY_CAPTION}}": ("Accuracy rises monotonically as the share of high-locatability training images grows "
                              "from 0% to 100%."),

    # Headline Numbers
    "{{HERO_VAL}}": "0.9033",
    "{{HERO_LABEL}}": "Country-level F1 (full GeoReasoner)",
    "{{HERO_NOTE}}": "+25.02% over Qwen-VL",
    "{{STAT_2_VAL}}": "0.8585", "{{STAT_2_LBL}}": "City F1",
    "{{STAT_3_VAL}}": "+38.61%", "{{STAT_3_LBL}}": "city vs Qwen-VL",
    "{{STAT_4_VAL}}": "70K", "{{STAT_4_LBL}}": "images vs 1.1M",

    # Takeaway
    "{{TAKEAWAY}}": ("Curating high-locatability street views and injecting human reasoning from geo-games lets a "
                     "two-stage fine-tuned LVLM <strong>beat prior models</strong> and <strong>explain</strong> its "
                     "predictions &mdash; with a fraction of the data."),
}

missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"placeholder(s) not in template: {missing}")
for token, value in SUBS.items():
    html = html.replace(token, value)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
