#!/usr/bin/env python3
"""Fill the composed poster.html for the SKiNN paper (indirect build)."""
import re
import sys
from pathlib import Path


def drop_section(doc: str, sec: str) -> str:
    m = re.search(rf'<div\b[^>]*\bdata-section="{re.escape(sec)}"', doc)
    if not m:
        return doc
    start = doc.rfind("<div", 0, m.end())
    i, depth = start, 0
    while i < len(doc):
        o, c = doc.find("<div", i), doc.find("</div>", i)
        if c == -1:
            return doc
        if o != -1 and o < c:
            depth += 1
            i = o + 4
        else:
            depth -= 1
            i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n":
                    i += 1
                return doc[:start] + doc[i:]
    return doc


target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

# 1. strip HTML comments (kills the commented-out Contribution block + its placeholders,
#    and the inline instructional comments) — keeps <script>/<style> bodies intact.
html = re.sub(r"<!--.*?-->", "", html, flags=re.S)

# 2. drop the Ablation section (proof-of-concept paper, no formal ablation table)
html = drop_section(html, "ablation-study")

# 3. remove the unused Motivation teaser <figure> (Figure 2 goes into Key Result instead)
html = re.sub(r'<figure><img src="\{\{TEASER_FIGURE\}\}".*?</figure>', "", html, flags=re.S)

# 4. keep PLAYLIST in sync — drop ablation
html = html.replace(
    '["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "ablation-study", "takeaway"]',
    '["title", "problem", "motivation", "method", "dataset-benchmark", "key-result", "takeaway"]',
)

SUBS = {
    "{{TITLE}}": "Fast Kinematics Modeling for Conjunction with Lens Image Modeling",
    "{{AUTHORS}}": ('Matthew R. Gomer<sup>1</sup>, Luca Biggio<sup>2</sup>, Sebastian Ertl<sup>3,4</sup>, '
                    'Han Wang<sup>3,4</sup>, Aymeric Galan<sup>5</sup>, Lyne Van de Vyvere<sup>1</sup>, '
                    'Dominique Sluse<sup>1</sup>, Georgios Vernardos<sup>5</sup>, Sherry Suyu<sup>3,4,6</sup>'),
    "{{AUTHOR_LEGEND}}": ('<sup>1</sup> Universit&eacute; de Li&egrave;ge &nbsp;&nbsp; <sup>2</sup> ETH Z&uuml;rich '
                          '&nbsp;&nbsp; <sup>3</sup> Max-Planck-Institut f&uuml;r Astrophysik &nbsp;&nbsp; '
                          '<sup>4</sup> Technische Universit&auml;t M&uuml;nchen &nbsp;&nbsp; <sup>5</sup> EPFL '
                          '&nbsp;&nbsp; <sup>6</sup> ASIAA'),
    "{{CONTACT}}": "",
    "{{VENUE_NAME}}": "NeurIPS",
    "{{VENUE_YEAR}}": "2022",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{LOGO_1}}": "assets/logos/universit-de-li-ge.png",
    "{{LOGO_2}}": "assets/logos/eth-z-rich.png",
    "{{LOGO_3}}": "assets/logos/max-planck-institut-f-r-astrophysik.png",
    "{{LOGO_4}}": "assets/logos/technische-universit-t-m-nchen.png",
    "{{LOGO_5}}": "assets/logos/cole-polytechnique-f-d-rale-de-lausanne.png",
    "{{LOGO_6}}": "assets/logos/academia-sinica-institute-of-astronomy-and-astrophysics-asiaa.png",
    "{{QR_PAPER}}": "assets/qr/paper.png",
    "{{QR_CODE}}": "assets/qr/code.png",

    "{{PROBLEM}}": ("Galaxy-kinematics modeling is the computational <strong>bottleneck</strong> in joint "
                    "gravitational-lensing + kinematics modeling: the physics code <strong>JAM</strong> must be "
                    "re-run for <em>every</em> likelihood evaluation inside an MCMC."),

    "{{MOTIVATION_1}}": ("Spatially resolved kinematics from <strong>JWST</strong> are now available, but spherical "
                         "Jeans models are too crude and inconsistent with elliptical lens mass models."),
    "{{MOTIVATION_2}}": ("Self-consistent <strong>axisymmetric</strong> modeling with JAM is the right tool, yet far "
                         "too slow for joint sampling &mdash; prior frameworks fit lens and kinematics separately."),

    "{{METHOD_1}}": ("SKiNN is a convolutional network <strong>&Psi;<sub>&theta;</sub></strong> mapping an "
                     "<strong>8-D</strong> galaxy-parameter vector (PEMD mass + elliptical S&eacute;rsic light, "
                     "inclination <em>i</em>, anisotropy <em>&beta;</em>) to a <em>d&times;d</em> velocity-dispersion "
                     "(<em>v</em><sub>rms</sub>) image."),
    "{{METHOD_2}}": ("Architecture: <strong>5 blocks</strong>, each with two 2-D convolutional layers + upsampling + "
                     "ReLU; <strong>~7.07M</strong> trainable parameters."),
    "{{METHOD_3}}": ("Trained with <strong>MSE loss</strong> and the Adam optimizer on JAM-generated data (via GLEE), "
                     "so the network learns to mimic the JAM procedure."),
    "{{METHOD_FIGURE}}": "assets/figures/page3_figure1.png",
    "{{METHOD_CAPTION}}": ("SKiNN&rsquo;s role in a joint modeling framework: it emulates the stellar-kinematics branch "
                           "(orange), producing a <em>v</em><sub>rms</sub> image whose &chi;&sup2; combines with the "
                           "lens-modeling branch (blue) into a single joint &chi;&sup2;<sub>tot</sub>."),

    "{{DATASET_1}}": ("<strong>5000</strong> input&ndash;output pairs generated with JAM &mdash; "
                      "<strong>4000</strong> train / <strong>500</strong> val / <strong>500</strong> test; each "
                      "<em>v</em><sub>rms</sub> image is <strong>551&times;551</strong> px."),
    "{{DATASET_2}}": ("A single JAM image takes <strong>~15 s</strong> to create; implemented in PyTorch + PyTorch "
                      "Lightning, trained <strong>~1 day</strong> on 5&times; Tesla P100 (16 GB) GPUs."),

    # Key Result placeholders (table restructured + Figure 2 added by a later Edit)
    "{{BASELINE}}": "JAM (physics)",
    "{{BASELINE_NUM}}": "~15 s",
    "{{OURS}}": "SKiNN (ours)",
    "{{OURS_NUM}}": "~50 ms",
    "{{HEADLINE_DELTA}}": "&approx;300&times; faster &middot; &lt;1% error inside the inner 2&Prime; region",
    "{{KEY_RESULT_CONCLUSION}}": ("Inside the innermost 2&Prime; region &mdash; where data actually constrains the "
                                  "model &mdash; SKiNN matches JAM to &lt;1% for almost all pixels."),

    "{{HERO_VAL}}": "~300&times;",
    "{{HERO_LABEL}}": "Faster than JAM per <em>v</em><sub>rms</sub> image",
    "{{HERO_NOTE}}": "&approx;50 ms vs ~15 s",
    "{{STAT_2_VAL}}": "&lt;1%",
    "{{STAT_2_LBL}}": "error, inner 2&Prime;",
    "{{STAT_3_VAL}}": "0.47%",
    "{{STAT_3_LBL}}": "median abs. error",
    "{{STAT_4_VAL}}": "~7.07M",
    "{{STAT_4_LBL}}": "parameters",

    "{{TAKEAWAY}}": ("A neural network can emulate slow physics-based galaxy kinematics (JAM) at <strong>~300&times;</strong> "
                     "speed and <strong>sub-percent</strong> accuracy &mdash; making joint lensing + resolved-kinematics "
                     "modeling feasible for precise Hubble-constant measurements."),
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
