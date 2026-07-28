#!/usr/bin/env python3
import re, sys
from pathlib import Path

def drop_section(doc, sec):
    m = re.search(rf'<div\b[^>]*\bdata-section="{re.escape(sec)}"', doc)
    if not m: return doc
    start = doc.rfind("<div", 0, m.end())
    i, depth = start, 0
    while i < len(doc):
        o, c = doc.find("<div", i), doc.find("</div>", i)
        if c == -1: return doc
        if o != -1 and o < c:
            depth += 1; i = o + 4
        else:
            depth -= 1; i = c + len("</div>")
            if depth == 0:
                while i < len(doc) and doc[i] in " \t\r\n": i += 1
                return doc[:start] + doc[i:]
    return doc

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("poster.html")
html = target.read_text(encoding="utf-8")

SUBS = {
    "{{TITLE}}": "High-Performance Temporal Reversible Spiking Neural Networks with O(L) Training Memory and O(1) Inference Cost",
    "{{AUTHORS}}": ("Jiakui Hu<sup>1</sup>, Man Yao<sup>2</sup>, Xuerui Qiu<sup>3</sup>, "
                    "Yuhong Chou<sup>4</sup>, Yuxuan Cai<sup>5</sup>, Ning Qiao<sup>6</sup>, "
                    "Yonghong Tian<sup>1,7</sup>, Bo Xu<sup>2</sup>, Guoqi Li<sup>2,8&#8224;</sup>"),
    "{{AUTHOR_LEGEND}}": ("<sup>1</sup> Peking University &nbsp;&nbsp; "
                          "<sup>2</sup> Institute of Automation, CAS &nbsp;&nbsp; "
                          "<sup>3</sup> Future Technology, UCAS &nbsp;&nbsp; "
                          "<sup>4</sup> The Hong Kong Polytechnic University &nbsp;&nbsp; "
                          "<sup>5</sup> 01.AI &nbsp;&nbsp; <sup>6</sup> SynSense AG &nbsp;&nbsp; "
                          "<sup>7</sup> Peng Cheng Laboratory &nbsp;&nbsp; "
                          "<sup>8</sup> Key Lab of Brain-inspired Intelligence, CAS"),
    "{{VENUE_NAME}}": "ICML",
    "{{VENUE_YEAR}}": "2024",
    "{{VENUE_LOGO}}": "assets/logos/_venue.png",
    "{{CONTACT}}": "Email: guoqi.li@ia.ac.cn",
    "{{LOGO_1}}": "assets/logos/peking-university.png",
    "{{LOGO_2}}": "assets/logos/university-of-chinese-academy-of-sciences.png",
    "{{LOGO_3}}": "assets/logos/the-hong-kong-polytechnic-university.png",
    "{{LOGO_4}}": "assets/logos/01-ai.png",
    "{{LOGO_5}}": "",
    "{{LOGO_6}}": "",
    "{{QR_PAPER}}": "",
    "{{QR_CODE}}": "",

    "{{PROBLEM}}": ("Multi-timestep simulation of SNNs costs <strong>O(L&#215;T)</strong> training memory and "
                    "<strong>O(T)</strong> inference energy. Existing training methods relieve one bottleneck but "
                    "<strong>never both at once</strong>, keeping SNNs from scaling."),

    "{{MOTIVATION_1}}": ("Temporal gradients in SNNs are largely <strong>unimportant</strong> &mdash; only neurons at "
                         "a few key positions carry temporal information that actually matters."),
    "{{MOTIVATION_2}}": ("Prior work either decouples training from the timestep (OTTT / SLTT) or shrinks inference "
                         "steps &mdash; each solves only <strong>half</strong> the dilemma."),
    "{{TEASER_FIGURE}}": "assets/figures/figure2.png",
    "{{TEASER_CAPTION}}": ("Cosine similarity of spatial gradients vs. the baseline. Each stage&#39;s final-layer temporal "
                           "gradients stay high (Case 1, left); earlier neurons diverge (Case 2, right) &mdash; most temporal "
                           "gradients are dispensable."),

    "{{METHOD_1}}": "placeholder-m1",
    "{{METHOD_2}}": "placeholder-m2",
    "{{KEY_EQUATION}}": (r"V^{l}[t{+}1]=\sum_{i=l}^{L}\left(1-\tfrac{1}{\tau_i}\right)V^{i}[t]"
                         r"+\tfrac{1}{\tau_m}W_l\,S^{l-1}[t{+}1]"),
    "{{KEY_EQUATION_NOTE}}": ("Multi-level temporal-reversible update: membrane potentials are exactly recoverable across "
                              "timesteps, so intermediate activations need not be stored &mdash; only the last timestep is kept "
                              "(memory O(L))."),
    "{{METHOD_FIGURE}}": "assets/figures/figure1.png",
    "{{METHOD_CAPTION}}": ("Vanilla SNNs unfold every neuron in time (O(L&#215;T) memory, O(T) inference). T-RevSNN encodes the "
                           "image once, splits it into T groups over T parameter-sharing sub-networks, and passes temporal "
                           "information only at key neurons &mdash; giving O(L) memory and O(1) inference."),

    "{{BASELINE}}": "placeholder-baseline",
    "{{BASELINE_NUM}}": "placeholder-bn",
    "{{OURS}}": "placeholder-ours",
    "{{OURS_NUM}}": "placeholder-on",
    "{{HEADLINE_DELTA}}": ("8.6&#215; less memory, 2.0&#215; faster training, 1.6&#215; lower inference energy vs. the "
                           "Spike-driven Transformer &mdash; at comparable accuracy."),
    "{{SECONDARY_FIGURE}}": "assets/figures/figure5.png",
    "{{SECONDARY_CAPTION}}": ("Forward / backward of prior methods vs. T-RevSNN. Turning off most neurons&#39; temporal dynamics "
                              "and making the key connections reversible means only last-timestep membrane potentials are stored."),
    "{{KEY_RESULT_CONCLUSION}}": ("Best accuracy among CNN-based spiking ResNets, with the lowest training memory, training time, "
                                  "and inference energy in its class."),

    "{{HERO_VAL}}": "8.6&#215;",
    "{{HERO_LABEL}}": "Less training memory vs. Spike-driven Transformer",
    "{{HERO_NOTE}}": "at comparable 73.2% top-1 accuracy",
    "{{STAT_2_VAL}}": "2.0&#215;",
    "{{STAT_2_LBL}}": "Faster training",
    "{{STAT_3_VAL}}": "1.6&#215;",
    "{{STAT_3_LBL}}": "Lower inference energy",
    "{{STAT_4_VAL}}": "73.2%",
    "{{STAT_4_LBL}}": "ImageNet-1K top-1",

    "{{TAKEAWAY}}": ("Because most temporal gradients in SNNs don&#39;t matter, turning off most neurons&#39; temporal dynamics "
                     "and making the rest reversible delivers <strong>O(L) training memory</strong> and "
                     "<strong>O(1) inference cost</strong> while keeping high accuracy."),
}

for sec in ["dataset-benchmark"]:
    html = drop_section(html, sec)
    html = re.sub(rf'"{re.escape(sec)}"\s*,?\s*', "", html)

# ablation-study ships commented-out; blank its tokens so the leftover check passes.
for t in ("{{ABLATION_1}}", "{{ABLATION_2}}", "{{ABLATION_CONCLUSION}}"):
    html = html.replace(t, "")

missing = [k for k in SUBS if k not in html]
if missing:
    sys.exit(f"placeholders not in template: {missing}")
for t, v in SUBS.items():
    html = html.replace(t, v)

leftover = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
if leftover:
    sys.exit(f"unreplaced placeholders remain: {leftover}")

target.write_text(html, encoding="utf-8")
print(f"wrote {target} ({len(html)} bytes)")
