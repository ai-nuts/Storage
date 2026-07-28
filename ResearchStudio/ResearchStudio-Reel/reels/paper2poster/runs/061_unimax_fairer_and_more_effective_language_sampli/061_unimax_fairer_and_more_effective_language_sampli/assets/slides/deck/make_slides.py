#!/usr/bin/env python3
"""Build the all-native SVG deck for the UniMax paper2video (run 061).

Each narration chunk in visual_anchor_contract.json becomes its own
<g id="cue_sXX_cN_..."> card carrying a <title> with the narration keywords,
so the strict --require-pptx-anchors cue pass resolves every chunk from PPTX
geometry. No <image> elements => never trips ppt_visuals_too_small.
"""
import html
import json
from pathlib import Path

DECK = Path(__file__).resolve().parent
CONTRACT = DECK.parent.parent / "meta" / "visual_anchor_contract.json"
OUT = DECK / "svg_output"
OUT.mkdir(parents=True, exist_ok=True)

# ---- palette ----
BG = "#0F1626"
CARD = "#1A2438"
PRIMARY = "#4EA1FF"
ACCENT = "#6EE7B7"
WARN = "#F87171"
AMBER = "#FBBF24"
TEXT = "#E8EEF7"
TEXT2 = "#9FB2C6"
TEXT3 = "#63788F"
BORDER = "#2B3B57"
TRACK = "#22304A"
FONT = "Arial, 'Helvetica Neue', 'Microsoft YaHei', sans-serif"

W, H = 1280, 720


def esc(s):
    return html.escape(str(s), quote=True)


def wrap(text, maxchars):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= maxchars:
            cur = (cur + " " + w).strip()
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def T(x, y, s, size, fill=TEXT, weight=400, anchor="start", family=FONT, spacing=None):
    ls = f' letter-spacing="{spacing}"' if spacing is not None else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{ls}>{esc(s)}</text>')


def wrapped_block(x, y, text, size, fill, maxchars, lh, weight=400):
    out = []
    for i, ln in enumerate(wrap(text, maxchars)):
        out.append(T(x, y + i * lh, ln, size, fill=fill, weight=weight))
    return "".join(out), y + len(wrap(text, maxchars)) * lh


# ---- load contract ----
contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
SLIDES = {s["index"]: s for s in contract["slides"]}


def chunk(slide_idx, cidx):
    ch = SLIDES[slide_idx]["chunks"][cidx - 1]
    return ch


def card_open(ch, x, y, w, h, fill=CARD, stroke=BORDER, accent=None, rx=16):
    kw = " ".join(ch.get("cue_keywords", []))
    title = f'<title>{esc(kw)}</title><desc>{esc(ch["text"][:180])}</desc>'
    g = [f'<g id="{esc(ch["anchor_id"])}" data-cue-label="{esc(ch["anchor_id"])}">']
    g.append(title)
    g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
             f'fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
    if accent:
        g.append(f'<rect x="{x}" y="{y+18}" width="5" height="{h-36}" rx="2.5" fill="{accent}"/>')
    return "".join(g)


def card_close():
    return "</g>"


def header(idx, total, kicker, title, accent=PRIMARY):
    out = []
    # inset accent tab (not full-bleed; clears the 13px edge band)
    out.append(f'<rect x="64" y="52" width="34" height="6" rx="3" fill="{accent}"/>')
    out.append(T(108, 62, kicker.upper(), 15, fill=accent, weight=700, spacing="2.5"))
    out.append(T(64, 104, title, 34, fill=TEXT, weight=800))
    out.append(T(1216, 62, f"{idx:02d} / {total:02d}", 14, fill=TEXT3, weight=600, anchor="end", spacing="1.5"))
    return "".join(out)


def svg_wrap(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}">\n'
            f'<rect width="{W}" height="{H}" fill="{BG}"/>\n'
            f'<rect x="64" y="126" width="1152" height="1.5" fill="{BORDER}"/>\n'
            f'{body}\n</svg>\n')


def bars(x, y, w, h, series, maxv=None):
    """Horizontal bar group in absolute coords. series=[(label,val,color)]."""
    out = []
    maxv = maxv or max(v for _, v, _ in series)
    n = len(series)
    gap = 12
    bh = (h - gap * (n - 1)) / n
    labw = 128
    barw = w - labw - 60
    for i, (lab, val, col) in enumerate(series):
        by = y + i * (bh + gap)
        out.append(T(x, by + bh / 2 + 5, lab, 15, fill=TEXT2, weight=600))
        out.append(f'<rect x="{x+labw}" y="{by}" width="{barw}" height="{bh}" rx="{bh/2}" fill="{TRACK}"/>')
        bw = max(6, barw * (val / maxv))
        out.append(f'<rect x="{x+labw}" y="{by}" width="{bw:.1f}" height="{bh}" rx="{bh/2}" fill="{col}"/>')
        out.append(T(x + labw + bw + 10, by + bh / 2 + 5, f"{val}", 16, fill=TEXT, weight=800))
    return "".join(out)


def grid_boxes(n, x0=64, y0=150, x1=1216, y1=684, gap=26, cols=2):
    rows = (n + cols - 1) // cols
    w = (x1 - x0 - gap * (cols - 1)) / cols
    h = (y1 - y0 - gap * (rows - 1)) / rows
    boxes = []
    for i in range(n):
        r, c = divmod(i, cols)
        boxes.append((x0 + c * (w + gap), y0 + r * (h + gap), w, h))
    return boxes


# =================== SLIDES ===================
slides = {}

# ---------- Slide 1: Title ----------
def slide1():
    b = []
    b.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    # subtle right glow panel (inset, off edges)
    b.append(f'<rect x="784" y="150" width="432" height="300" rx="20" fill="{CARD}" stroke="{BORDER}"/>')
    # decorative uniform-vs-temperature mini viz inside glow panel
    b.append(T(816, 190, "SAMPLING SHAPE", 13, fill=TEXT3, weight=700, spacing="2"))
    # temperature (skewed) row
    b.append(T(816, 210, "Temperature", 14, fill=WARN, weight=700))
    tvals = [72, 52, 32, 18, 10, 5]
    for i, v in enumerate(tvals):
        b.append(f'<rect x="{816+i*62}" y="{300-v}" width="42" height="{v}" rx="4" fill="{WARN}" opacity="0.8"/>')
    b.append(f'<line x1="816" y1="300" x2="1184" y2="300" stroke="{BORDER}"/>')
    # unimax (uniform+cap) row
    b.append(T(816, 336, "UniMax", 14, fill=ACCENT, weight=700))
    uvals = [52, 52, 52, 52, 44, 30]
    for i, v in enumerate(uvals):
        b.append(f'<rect x="{816+i*62}" y="{410-v}" width="42" height="{v}" rx="4" fill="{ACCENT}" opacity="0.85"/>')
    b.append(f'<line x1="816" y1="410" x2="1184" y2="410" stroke="{BORDER}"/>')
    b.append(T(816, 432, "high-resource  →  low-resource", 12, fill=TEXT3, weight=500))

    # left title block = c1
    ch1 = chunk(1, 1)
    b.append(f'<g id="{esc(ch1["anchor_id"])}" data-cue-label="{esc(ch1["anchor_id"])}"><title>{esc(" ".join(ch1["cue_keywords"]))}</title><desc>{esc(ch1["text"][:180])}</desc>')
    b.append(f'<rect x="64" y="150" width="34" height="6" rx="3" fill="{PRIMARY}"/>')
    b.append(T(64, 150, "GOOGLE RESEARCH · ICLR 2023", 15, fill=PRIMARY, weight=700, spacing="2"))
    b.append(T(64, 268, "UniMax", 96, fill=TEXT, weight=800))
    b.append(T(64, 320, "Fairer and More Effective Language Sampling", 26, fill=TEXT, weight=700))
    b.append(T(64, 356, "for Large-Scale Multilingual Pretraining", 26, fill=TEXT, weight=700))
    b.append(T(64, 402, "Uniform budget allocation with a hard cap on per-language repeats", 18, fill=TEXT2, weight=500))
    b.append("</g>")

    # authors
    b.append(T(64, 452, "Chung, Constant, Garcia, Roberts, Tay, Narang, Firat · Google Research", 15, fill=TEXT3, weight=600))

    # three highlight cards = c2, c3, c4
    boxes = grid_boxes(3, x0=64, y0=500, x1=1216, y1=684, gap=26, cols=3)
    specs = [
        (chunk(1, 2), "METHOD", "Uniform + Max", "Spread budget evenly; cap how often any language repeats.", PRIMARY),
        (chunk(1, 3), "RESULT", "Beats temperature", "Wins across benchmarks and every model scale, gains grow with size.", ACCENT),
        (chunk(1, 4), "RELEASE", "29T-char mC4", "Refreshed corpus of 107 languages + umT5 checkpoints.", AMBER),
    ]
    for (ch, kick, big, desc, col), (x, y, w, h) in zip(specs, boxes):
        b.append(card_open(ch, x, y, w, h, accent=col))
        b.append(T(x + 24, y + 36, kick, 13, fill=col, weight=700, spacing="2"))
        b.append(T(x + 24, y + 70, big, 22, fill=TEXT, weight=800))
        blk, _ = wrapped_block(x + 24, y + 98, desc, 14, TEXT2, 34, 19)
        b.append(blk)
        b.append(card_close())
    return svg_wrap("".join(b)) if False else (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n' + "".join(b) + "\n</svg>\n")

slides["01_title"] = slide1()


# ---------- generic content slide ----------
def content_slide(idx, total, kicker, title, cards, accent=PRIMARY, cols=2):
    b = [f'<rect width="{W}" height="{H}" fill="{BG}"/>',
         f'<rect x="64" y="126" width="1152" height="1.5" fill="{BORDER}"/>',
         header(idx, total, kicker, title, accent=accent)]
    n = len(cards)
    boxes = grid_boxes(n, cols=cols)
    for spec, (x, y, w, h) in zip(cards, boxes):
        b.append(render_card(spec, x, y, w, h))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n' + "".join(b) + "\n</svg>\n"


def render_card(spec, x, y, w, h):
    ch = spec["ch"]
    col = spec.get("accent", PRIMARY)
    b = [card_open(ch, x, y, w, h, accent=col)]
    ix = x + 26
    cy = y + 40
    if spec.get("num"):
        b.append(f'<circle cx="{ix+16}" cy="{cy+2}" r="20" fill="none" stroke="{col}" stroke-width="2"/>')
        b.append(T(ix + 16, cy + 9, spec["num"], 22, fill=col, weight=800, anchor="middle"))
        ix2 = ix + 52
        b.append(T(ix2, cy - 4, spec["kick"], 13, fill=col, weight=700, spacing="2"))
        blk, _ = wrapped_block(ix2, cy + 22, spec["desc"], 15.5, TEXT, spec.get("mc", 40), 23, weight=500)
        b.append(blk)
        b.append(card_close())
        return "".join(b)
    b.append(T(ix, cy, spec["kick"], 13, fill=col, weight=700, spacing="2"))
    ty = cy + 30
    if spec.get("big"):
        b.append(T(ix, ty + 20, spec["big"], 46, fill=TEXT, weight=800))
        if spec.get("biglabel"):
            b.append(T(ix, ty + 46, spec["biglabel"], 14, fill=TEXT2, weight=600))
        ty += 66
    blk, endy = wrapped_block(ix, ty + 4, spec["desc"], spec.get("size", 15.5), TEXT2, spec.get("mc", 46), 22, weight=500)
    b.append(blk)
    if spec.get("chart"):
        b.append(spec["chart"](x, y, w, h))
    b.append(card_close())
    return "".join(b)


# ---------- Slide 2: Problem ----------
def s2_chart(x, y, w, h):
    cx = x + 26
    cyy = y + h - 70
    return (T(cx, cyy - 6, "mC4 characters (log)", 12, fill=TEXT3, weight=600)
            + bars(cx, cyy, w - 52, 44, [("English", 97, PRIMARY), ("Yoruba", 3, WARN)], maxv=100))

slides["02_problem"] = content_slide(2, 10, "Problem", "Multilingual data is wildly imbalanced", [
    {"ch": chunk(2, 1), "kick": "WHY SAMPLING MATTERS", "accent": PRIMARY,
     "desc": "The mix you train on is a design choice. Massively multilingual corpora are anything but balanced.", "mc": 40},
    {"ch": chunk(2, 2), "kick": "ENGLISH vs YORUBA", "accent": WARN, "big": "92,000×",
     "biglabel": "gap in mC4 (≈9.7T vs the tail)", "desc": "English dwarfs the lowest-resource language.", "mc": 40,
     "chart": s2_chart},
    {"ch": chunk(2, 3), "kick": "TRAIN ON RAW DATA?", "accent": AMBER,
     "desc": "Sample in proportion to raw size and the tail languages barely register at all.", "mc": 40},
    {"ch": chunk(2, 4), "kick": "OPEN & EXPENSIVE", "accent": PRIMARY,
     "desc": "Balancing languages is unsolved, and the default fix, temperature sampling, was never tested across scales.", "mc": 40},
])


# ---------- Slide 3: Motivation ----------
slides["03_motivation"] = content_slide(3, 10, "Motivation", "Temperature sampling over-repeats the tail", [
    {"ch": chunk(3, 1), "kick": "TEMPERATURE SAMPLING", "accent": PRIMARY,
     "desc": "Reshapes the data mix with a single exponent, tau. Simple, but there is a catch.", "mc": 40},
    {"ch": chunk(3, 2), "kick": "TUNE HEAD, HURT TAIL", "accent": AMBER,
     "desc": "Boosting the head languages forces heavy over-repetition of the long tail.", "mc": 40},
    {"ch": chunk(3, 3), "kick": "TAIL REPEATS AT τ=3.33", "accent": WARN, "big": ">100×",
     "biglabel": "with a 1T-token budget", "desc": "The lowest-resource languages are seen over a hundred times.", "mc": 40},
    {"ch": chunk(3, 4), "kick": "THE COST", "accent": WARN,
     "desc": "Over-repetition drives overfitting, memorized private content, and wasted compute, all worse at scale.", "mc": 40},
])


# ---------- Slide 4: Contribution ----------
slides["04_contribution"] = content_slide(4, 10, "Contribution", "Four contributions", [
    {"ch": chunk(4, 1), "num": "1", "kick": "THE METHOD", "accent": PRIMARY,
     "desc": "UniMax: allocate the budget uniformly while capping per-language repeats.", "mc": 38},
    {"ch": chunk(4, 2), "num": "2", "kick": "SYSTEMATIC STUDY", "accent": ACCENT,
     "desc": "Extensive ablation of sampling strategies run across model scales.", "mc": 38},
    {"ch": chunk(4, 3), "num": "3", "kick": "REFRESHED CORPUS", "accent": AMBER,
     "desc": "A new mC4 of 29 trillion characters across 107 languages.", "mc": 38},
    {"ch": chunk(4, 4), "num": "4", "kick": "OPEN CHECKPOINTS", "accent": PRIMARY,
     "desc": "Released umT5 checkpoints trained with UniMax to build on directly.", "mc": 38},
])


# ---------- Slide 5: Method ----------
slides["05_method"] = content_slide(5, 10, "Method", "UniMax = uniform allocation + max-epoch cap", [
    {"ch": chunk(5, 1), "num": "1", "kick": "UNIFORM + MAX", "accent": PRIMARY,
     "desc": "Start from a fixed character budget C; spread it as uniformly as possible, low to high resource.", "mc": 38},
    {"ch": chunk(5, 2), "num": "2", "kick": "CHECK EACH STEP", "accent": PRIMARY,
     "desc": "At each language, test whether the remaining budget still splits evenly.", "mc": 38},
    {"ch": chunk(5, 3), "num": "3", "kick": "CAP AT N EPOCHS", "accent": AMBER,
     "desc": "If a language would exceed N epochs, cap it and redistribute the freed budget uniformly.", "mc": 38},
    {"ch": chunk(5, 4), "num": "4", "kick": "THE RESULT", "accent": ACCENT,
     "desc": "More uniform head coverage; no tail repeated over N times (default N=1 means no repeats).", "mc": 38},
])


# ---------- Slide 6: Dataset & Benchmark ----------
slides["06_dataset"] = content_slide(6, 10, "Dataset and Benchmark", "Refreshed mC4 + a broad evaluation sweep", [
    {"ch": chunk(6, 1), "kick": "PRETRAINING CORPUS", "accent": AMBER, "big": "29T",
     "biglabel": "characters · 107 languages", "desc": "The refreshed mC4 used for pretraining.", "mc": 34},
    {"ch": chunk(6, 2), "kick": "EVALUATION SUITE", "accent": PRIMARY,
     "desc": "TyDi QA GoldP, WMT21 translation, XNLI, XQuAD, MLQA, and PAWS-X.", "mc": 34},
    {"ch": chunk(6, 3), "kick": "SWEEP THE SCALE", "accent": ACCENT,
     "desc": "Compare every strategy from Small up to XXL to see whether the gains persist.", "mc": 34},
], cols=3)


# ---------- Slide 7: Key Result ----------
def s7_chart(x, y, w, h):
    cx = x + 26
    cyy = y + h - 118
    return (T(cx, cyy - 8, "TyDi QA (½ budget, Large)", 12, fill=TEXT3, weight=600)
            + bars(cx, cyy, w - 52, 96, [
                ("UniMax", 83.1, ACCENT),
                ("τ=3.33", 82.8, PRIMARY),
                ("τ=1", 81.2, TEXT3)], maxv=84))

slides["07_key_result"] = content_slide(7, 10, "Key Result", "UniMax wins across tasks and scales", [
    {"ch": chunk(7, 1), "kick": "CONSISTENT WINS", "accent": ACCENT,
     "desc": "The advantage holds across the board, not just on average.", "mc": 40},
    {"ch": chunk(7, 2), "kick": "TyDi QA & WMT21", "accent": ACCENT,
     "desc": "Wins average TyDi QA at all three sizes, and WMT21 at every scale.", "mc": 40,
     "chart": s7_chart},
    {"ch": chunk(7, 3), "kick": "HIGH-RESOURCE", "accent": PRIMARY,
     "desc": "Beats tau=3.33, and only trails tau=1 at the very largest scale.", "mc": 40},
    {"ch": chunk(7, 4), "kick": "LOW-RESOURCE", "accent": ACCENT,
     "desc": "Wins outright, e.g. beats tau=3.33 on Swahili despite seeing fewer Swahili examples.", "mc": 40},
])


# ---------- Slide 8: Ablation ----------
def s8_chart(x, y, w, h):
    cx = x + 26
    cyy = y + h - 118
    return (T(cx, cyy - 8, "TyDi QA on Large by max-epoch N", 12, fill=TEXT3, weight=600)
            + bars(cx, cyy, w - 52, 96, [
                ("N=1", 82.2, ACCENT),
                ("N=5", 81.5, PRIMARY),
                ("N=10", 81.8, PRIMARY)], maxv=83))

slides["08_ablation"] = content_slide(8, 10, "Ablation Study", "How much does the max-epoch cap matter?", [
    {"ch": chunk(8, 1), "kick": "MAX-EPOCH N", "accent": PRIMARY,
     "desc": "Ablate N over 1, 5, and 10 on Large models.", "mc": 40, "chart": s8_chart},
    {"ch": chunk(8, 2), "kick": "N=1 WINS", "accent": ACCENT,
     "desc": "Disallowing repeats entirely is best, though the margin is small.", "mc": 40},
    {"ch": chunk(8, 3), "kick": "4× LARGER BUDGET", "accent": AMBER,
     "desc": "UniMax 83.1 versus 82.8 for tau=3.33 and 81.2 for tau=1.", "mc": 40},
    {"ch": chunk(8, 4), "kick": "LOSS CURVES", "accent": WARN,
     "desc": "High-temperature overfitting worsens with scale, while UniMax stays stable.", "mc": 40},
])


# ---------- Slide 9: Headline Numbers ----------
slides["09_headline"] = content_slide(9, 10, "Headline Numbers", "The numbers that matter", [
    {"ch": chunk(9, 1), "kick": "AT A GLANCE", "accent": PRIMARY,
     "desc": "Four figures that summarize UniMax and the refreshed corpus.", "mc": 40},
    {"ch": chunk(9, 2), "kick": "REFRESHED mC4", "accent": AMBER, "big": "29T",
     "biglabel": "chars · 107 languages", "desc": "+35% larger, about 9.0 billion documents.", "mc": 40},
    {"ch": chunk(9, 3), "kick": "TyDi QA (½ budget)", "accent": ACCENT, "big": "83.1",
     "biglabel": "UniMax vs 82.8 (τ=3.33) vs 81.2 (τ=1)", "desc": "umT5-XXL also beats mT5-XXL on TyDi QA.", "mc": 40},
    {"ch": chunk(9, 4), "kick": "WHAT THE CAP REMOVES", "accent": WARN, "big": ">100×",
     "biglabel": "tail repeats at τ=3.33", "desc": "Exactly what UniMax's per-language cap eliminates.", "mc": 40},
])


# ---------- Slide 10: Takeaway ----------
slides["10_takeaway"] = content_slide(10, 10, "Takeaway", "Cap repeats, spread the rest uniformly", [
    {"ch": chunk(10, 1), "kick": "THE TAKEAWAY", "accent": PRIMARY,
     "desc": "One idea: cap per-language repeats, and distribute the remaining budget uniformly.", "mc": 34},
    {"ch": chunk(10, 2), "kick": "BEATS TEMPERATURE", "accent": ACCENT,
     "desc": "Outperforms temperature sampling for multilingual pretraining, and the edge holds as models scale.", "mc": 34},
    {"ch": chunk(10, 3), "kick": "DROP-IN REPLACEMENT", "accent": AMBER,
     "desc": "Hyperparameter-light; ships with the refreshed mC4 and umT5 checkpoints you can use today.", "mc": 34},
], cols=3)


# ---- write ----
for name, svg in slides.items():
    (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")
    print("wrote", name)
print("done:", len(slides), "slides")
