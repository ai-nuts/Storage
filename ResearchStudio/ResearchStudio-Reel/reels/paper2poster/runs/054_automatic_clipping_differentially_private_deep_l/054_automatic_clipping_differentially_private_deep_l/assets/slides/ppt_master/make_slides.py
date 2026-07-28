#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 054 (Automatic Clipping, NeurIPS'23).

Reads visual_anchor_contract.json and wraps each narration chunk in its own
<g id="cue_sXX_cN_..."> card whose <title> holds the cue keywords, so the strict
--require-pptx-anchors cue pass resolves every anchor from PPTX geometry.
Zero <image> elements -> sidesteps every image gate. Dark cobalt/teal theme.
"""
import json, os, html, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONTRACT = os.environ["VIDEO_META"] + "/visual_anchor_contract.json"
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
SANS = "Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO = "Consolas, 'Courier New', monospace"

C = dict(
    bg="#0E1826", panel="#16233A", panel2="#1B2E4A",
    accent="#4C86F0", accent2="#2FB6A8", warn="#E9603E", green="#38C08A",
    amber="#E7B24C", text="#E8EEF7", muted="#9DB0C8", dim="#6E82A0",
    border="#29405F", kpi="#7FB0FF",
)

def esc(s):
    return html.escape(str(s), quote=True)

def wrap(text, max_chars):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if len(t) <= max_chars:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

class SVG:
    def __init__(self):
        self.parts = []
    def add(self, s):
        self.parts.append(s)
    def text(self, x, y, s, size, fill, weight="400", family=SANS, anchor="start", spacing="0"):
        ls = f' letter-spacing="{spacing}"' if spacing != "0" else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" '
                 f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
                 f'text-anchor="{anchor}"{ls}>{esc(s)}</text>')
    def rect(self, x, y, w, h, fill, rx=0, stroke=None, sw=1, opacity=None):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        op = f' opacity="{opacity}"' if opacity is not None else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
                 f'rx="{rx}" fill="{fill}"{st}{op}/>')
    def line(self, x1, y1, x2, y2, stroke, sw=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def render(self):
        body = "\n".join(self.parts)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
                f'width="{W}" height="{H}">\n{body}\n</svg>\n')

def base(s, kicker=None, title=None, accent=None):
    accent = accent or C["accent"]
    s.rect(0, 0, W, H, C["bg"])
    # inset accent tab (not full-bleed -> avoids edge_touch)
    s.rect(64, 58, 6, 34, accent, rx=3)
    if kicker:
        s.text(84, 74, kicker.upper(), 15, C["accent2"], weight="700", spacing="3")
    if title:
        s.text(84, 104, title, 34, C["text"], weight="800")
        s.line(84, 122, W - 64, 122, C["border"], sw=1)

def card_group(s, anchor_id, keywords, inner_fn):
    kw = " ".join(keywords)
    s.add(f'<g id="{esc(anchor_id)}" data-cue-label="{esc(anchor_id)}">')
    s.add(f'<title>{esc(kw)}</title>')
    s.add(f'<desc>{esc(kw)}</desc>')
    inner_fn()
    s.add('</g>')

def text_card(s, x, y, w, h, heading, lines, accent, num=None, body_size=18):
    s.rect(x, y, w, h, C["panel"], rx=14, stroke=C["border"], sw=1)
    s.rect(x, y, 5, h, accent, rx=2)
    tx = x + 24
    ty = y + 40
    if num:
        s.add(f'<circle cx="{tx+11:.1f}" cy="{ty-6:.1f}" r="15" fill="{accent}" opacity="0.16"/>')
        s.text(tx + 11, ty - 1, num, 16, accent, weight="800", anchor="middle")
        tx2 = tx + 38
    else:
        tx2 = tx
    s.text(tx2, ty, heading, 21, C["text"], weight="700")
    yy = ty + 30
    for ln in lines:
        for wl in wrap(ln, int((w - 48) / (body_size * 0.55))):
            s.text(tx, yy, wl, body_size, C["muted"], weight="400")
            yy += body_size + 8

def kpi_card(s, x, y, w, h, value, label, accent, sub=None):
    s.rect(x, y, w, h, C["panel"], rx=14, stroke=C["border"], sw=1)
    s.rect(x, y, w, 5, accent, rx=2)
    cx = x + w / 2
    s.text(cx, y + h * 0.46, value, 44, accent, weight="800", anchor="middle")
    yy = y + h * 0.46 + 30
    for wl in wrap(label, int((w - 28) / (14 * 0.55))):
        s.text(cx, yy, wl, 14, C["muted"], weight="600", anchor="middle")
        yy += 20
    if sub:
        s.text(cx, y + h - 16, sub, 12, C["dim"], weight="500", anchor="middle")

# ---- per-slide visible layouts, keyed by slide id ----------------------------
def layout_title(s, chunks):
    accent = C["accent"]
    s.rect(0, 0, W, H, C["bg"])
    s.rect(0, 0, W, 6, accent)
    s.rect(64, 150, 6, 150, accent, rx=3)
    s.text(90, 150, "NEURIPS 2023", 16, C["accent2"], weight="700", spacing="4")
    # c1 -> title block
    def c1():
        s.text(90, 214, "Automatic Clipping", 58, C["text"], weight="800")
        s.text(90, 262, "Differentially Private Deep Learning", 27, C["muted"], weight="500")
        s.text(90, 296, "Made Easier and Stronger", 27, C["muted"], weight="500")
    card_group(s, chunks[0]["anchor_id"], chunks[0]["cue_keywords"], c1)
    # authors / affiliations (chrome)
    s.line(90, 330, 760, 330, C["border"], sw=1)
    s.text(90, 364, "Zhiqi Bu · Yu-Xiang Wang · Sheng Zha · George Karypis", 19, C["text"], weight="600")
    s.text(90, 392, "AWS AI   ·   UC Santa Barbara", 16, C["dim"], weight="500")
    s.text(90, 416, "github.com/awslabs/fast-differential-privacy", 15, C["accent"], weight="500", family=MONO)
    # c2 -> drop-in highlight panel (right)
    def c2():
        px, py, pw, ph = 812, 196, 404, 300
        s.rect(px, py, pw, ph, C["panel2"], rx=18, stroke=C["accent"], sw=1)
        s.rect(px, py, pw, 5, C["accent"], rx=2)
        s.text(px + 28, py + 52, "Drop-in replacement", 24, C["text"], weight="800")
        s.text(px + 28, py + 92, "Removes the clipping", 18, C["muted"])
        s.text(px + 28, py + 118, "threshold R from any", 18, C["muted"])
        s.text(px + 28, py + 144, "DP optimizer", 18, C["muted"])
        s.rect(px + 28, py + 172, pw - 56, 88, C["bg"], rx=10, stroke=C["border"], sw=1)
        s.text(px + 44, py + 210, "R / (||g|| + γ)  →  R = 1", 22, C["accent2"], weight="700", family=MONO)
        s.text(px + 44, py + 240, "one line of code", 15, C["dim"], weight="500")
    card_group(s, chunks[1]["anchor_id"], chunks[1]["cue_keywords"], c2)

def three_row(specs):
    def fn(s, chunks):
        y, h = 190, 340
        m, gap = 64, 26
        w = (W - 2 * m - 2 * gap) / 3
        for i, (ch, sp) in enumerate(zip(chunks, specs)):
            x = m + i * (w + gap)
            def draw(x=x, sp=sp):
                if sp.get("chart") == "collapse":
                    text_card(s, x, y, w, h, sp["heading"], sp["lines"], sp["accent"])
                    draw_collapse(s, x + 22, y + 150, w - 44, 150)
                else:
                    text_card(s, x, y, w, h, sp["heading"], sp["lines"], sp["accent"])
            card_group(s, ch["anchor_id"], ch["cue_keywords"], draw)
    return fn

def draw_collapse(s, x, y, w, h):
    # two-bar collapse chart 45% -> 31%
    base_y = y + h - 26
    maxv = 50.0
    bw = 54
    xs = [x + w * 0.28, x + w * 0.66]
    vals = [(45, C["green"], "R ok"), (31, C["warn"], "R wrong")]
    for cx, (v, col, lab) in zip(xs, vals):
        bh = (v / maxv) * (h - 44)
        s.rect(cx - bw / 2, base_y - bh, bw, bh, col, rx=4)
        s.text(cx, base_y - bh - 8, f"{v}%", 16, col, weight="800", anchor="middle")
        s.text(cx, base_y + 16, lab, 12, C["dim"], anchor="middle")
    s.add(f'<path d="M {xs[0]+bw/2:.0f} {base_y-((45/maxv)*(h-44)):.0f} '
          f'L {xs[1]-bw/2:.0f} {base_y-((31/maxv)*(h-44)):.0f}" '
          f'stroke="{C["warn"]}" stroke-width="2" stroke-dasharray="4 4" fill="none"/>')

def two_by_two(specs, body_size=18):
    def fn(s, chunks):
        y0, m, gap = 176, 64, 26
        w = (W - 2 * m - gap) / 2
        h = 200
        for i, (ch, sp) in enumerate(zip(chunks, specs)):
            r, c = divmod(i, 2)
            x = m + c * (w + gap)
            yy = y0 + r * (h + 22)
            def draw(x=x, yy=yy, sp=sp):
                text_card(s, x, yy, w, h, sp["heading"], sp["lines"], sp["accent"],
                          num=sp.get("num"), body_size=body_size)
            card_group(s, ch["anchor_id"], ch["cue_keywords"], draw)
    return fn

def kpi_row(specs):
    def fn(s, chunks):
        y, h, m, gap = 210, 300, 64, 22
        w = (W - 2 * m - 3 * gap) / 4
        for i, (ch, sp) in enumerate(zip(chunks, specs)):
            x = m + i * (w + gap)
            def draw(x=x, sp=sp):
                if sp.get("kpi"):
                    kpi_card(s, x, y, w, h, sp["value"], sp["label"], sp["accent"], sp.get("sub"))
                else:
                    text_card(s, x, y, w, h, sp["heading"], sp["lines"], sp["accent"], body_size=17)
            card_group(s, ch["anchor_id"], ch["cue_keywords"], draw)
    return fn

# ---- slide registry ----------------------------------------------------------
A, A2, WARN, GREEN, AMBER = C["accent"], C["accent2"], C["warn"], C["green"], C["amber"]

SLIDES = {
    "title": dict(builder=layout_title),
    "problem": dict(kicker="Problem", title="The clipping threshold R is fragile", accent=WARN,
        builder=three_row([
            dict(heading="Per-sample clipping", accent=A,
                 lines=["Every gradient is clipped to a", "fixed norm R, then noise is added."]),
            dict(heading="Wrong R is costly", accent=WARN, chart="collapse",
                 lines=["ImageNet ResNet18 accuracy"]),
            dict(heading="SOTA needs tiny R", accent=A2,
                 lines=["Best thresholds are found only", "by careful, expensive tuning."]),
        ])),
    "motivation": dict(kicker="Motivation", title="Why DP training is painful", accent=AMBER,
        builder=three_row([
            dict(heading="Joint hyperparameter search", accent=A,
                 lines=["Tune the clipping threshold R", "and the learning rate together."]),
            dict(heading="Costly grid search", accent=WARN,
                 lines=["Days to months of compute,", "and it spends privacy budget."]),
            dict(heading="Best R is tiny", accent=A2,
                 lines=["So small that nearly every", "gradient is clipped every step."]),
        ])),
    "contribution": dict(kicker="Contribution", title="Four contributions", accent=A,
        builder=two_by_two([
            dict(heading="Automatic clipping", num="1", accent=A,
                 lines=["Expunge R from the DP optimizer,", "a drop-in replacement."]),
            dict(heading="Convergence proof", num="2", accent=A2,
                 lines=["Non-convex; same asymptotic", "rate as standard SGD."]),
            dict(heading="One default suffices", num="3", accent=GREEN,
                 lines=["Any positive constant R", "is equivalent to R = 1."]),
            dict(heading="Stronger results", num="4", accent=AMBER,
                 lines=["Vision + language SOTA by", "changing a single line."]),
        ])),
    "method": dict(kicker="Method", title="From Abadi's clip to automatic clip", accent=A2,
        builder=two_by_two([
            dict(heading="Observation", num="1", accent=A,
                 lines=["Small R ⇒ min(R/||g||, 1) ≈ R/||g||;", "the clip almost always fires."]),
            dict(heading="AUTO-V: normalize", num="2", accent=A2,
                 lines=["Drop the minimum, normalize", "every gradient:  g · R / ||g||."]),
            dict(heading="AUTO-S: stabilize", num="3", accent=GREEN,
                 lines=["Add a stability constant γ:", "g · R / (||g|| + γ)."]),
            dict(heading="One knob fewer", num="4", accent=AMBER,
                 lines=["Fix R = 1, γ = 0.01; a constant", "threshold just rescales lr."]),
        ])),
    "dataset-benchmark": dict(kicker="Benchmarks", title="Evaluated across vision & language", accent=A,
        builder=two_by_two([
            dict(heading="Broad evaluation", num="1", accent=A,
                 lines=["Vision and language, reusing", "the same recipes as prior work."]),
            dict(heading="Language", num="2", accent=A2,
                 lines=["RoBERTa base/large on GLUE", "(MNLI, QQP, QNLI, SST-2); GPT2 on E2E."]),
            dict(heading="Vision", num="3", accent=GREEN,
                 lines=["CIFAR-10 (SimCLRv2), ImageNette", "(ResNet9), ImageNet (ResNet18)."]),
            dict(heading="Privacy budgets", num="4", accent=AMBER,
                 lines=["ε = 3 and ε = 8, reusing", "prior hyperparameters exactly."]),
        ])),
    "key-result": dict(kicker="Key Result", title="Matches or beats SOTA — without tuning R", accent=GREEN,
        builder=kpi_row([
            dict(heading="No R tuning", accent=A,
                 lines=["Tune the learning rate", "only — about 5× cheaper."]),
            dict(kpi=True, value="64.18", label="GPT2 E2E BLEU", accent=A2, sub="ε = 3"),
            dict(kpi=True, value="92.32%", label="RoBERTa-base SST-2", accent=GREEN, sub="> prior 91.86%"),
            dict(kpi=True, value="92.7%", label="CIFAR-10 SimCLRv2", accent=AMBER, sub="ε = 2"),
        ])),
    "ablation-study": dict(kicker="Ablation", title="What makes automatic clipping work", accent=A2,
        builder=two_by_two([
            dict(heading="Two ablations", num="1", accent=A,
                 lines=["Isolating the two ingredients", "behind the design."]),
            dict(heading="AUTO-V vs AUTO-S", num="2", accent=A2,
                 lines=["Stability γ restores gradient", "magnitude: AUTO-S ≥ AUTO-V."]),
            dict(heading="Insensitive to γ", num="3", accent=GREEN,
                 lines=["Sweeping γ: any positive", "value works, no tuning."]),
            dict(heading="R × lr heatmaps", num="4", accent=AMBER,
                 lines=["AUTO-S lands right at the", "best hand-tuned cell."]),
        ])),
    "headline-numbers": dict(kicker="Results", title="Headline numbers", accent=A,
        builder=kpi_row([
            dict(kpi=True, value="64.18", label="GPT2 E2E BLEU", accent=A2, sub="ε=3, vs 63.8"),
            dict(kpi=True, value="92.32%", label="RoBERTa-base SST-2", accent=GREEN, sub="large: 96.2%"),
            dict(kpi=True, value="92.7%", label="CIFAR-10 SimCLRv2", accent=AMBER, sub="ε = 2"),
            dict(kpi=True, value="T^−1/4", label="min E||g|| rate", accent=A, sub="= standard SGD"),
        ])),
    "takeaway": dict(kicker="Takeaway", title="R need not be a critical knob", accent=GREEN,
        builder=three_row([
            dict(heading="Rethink the threshold", accent=A,
                 lines=["Long treated as critical,", "R can simply be fixed to 1."]),
            dict(heading="Normalize + stabilize", accent=A2,
                 lines=["Per-sample normalization plus a", "tiny γ matches best-tuned accuracy."]),
            dict(heading="One-line change", accent=GREEN,
                 lines=["Drop-in for existing libraries;", "DP as easy as ordinary training."]),
        ])),
}

def main():
    contract = json.load(open(CONTRACT))
    prefix = {sl["id"]: f"{i+1:02d}" for i, sl in enumerate(contract["slides"])}
    for sl in contract["slides"]:
        sid = sl["id"]
        spec = SLIDES[sid]
        s = SVG()
        if sid == "title":
            spec["builder"](s, sl["chunks"])
        else:
            base(s, kicker=spec.get("kicker"), title=spec.get("title"), accent=spec.get("accent"))
            spec["builder"](s, sl["chunks"])
        # footer link (chrome, not a cue) on non-title slides
        if sid != "title":
            s.text(64, H - 22, "Automatic Clipping  ·  Bu et al., NeurIPS 2023", 12, C["dim"], weight="500")
            s.text(W - 64, H - 22, "arxiv.org/abs/2206.07136", 12, C["dim"], weight="500",
                   anchor="end", family=MONO)
        fname = f'{prefix[sid]}_{sid.replace("-", "_")}.svg'
        with open(os.path.join(OUT, fname), "w") as f:
            f.write(s.render())
        print("wrote", fname, f"({len(sl['chunks'])} cues)")

if __name__ == "__main__":
    main()
