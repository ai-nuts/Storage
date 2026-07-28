#!/usr/bin/env python3
"""Build the all-native SVG deck for Carbon Monitor Ocean (CMO-NRT), run 079.

Each narration chunk in visual_anchor_contract.json becomes its own
<g id="cue_sXX_cN_..."> card carrying a <title> with the narration keywords,
so the strict --require-pptx-anchors cue pass resolves every chunk from PPTX
geometry. No <image> elements => never trips ppt_visuals_too_small.
"""
import html
import json
import math
from pathlib import Path

DECK = Path(__file__).resolve().parent
CONTRACT = DECK.parent.parent / "meta" / "visual_anchor_contract.json"
OUT = DECK / "svg_output"
OUT.mkdir(parents=True, exist_ok=True)

# ---- palette (deep-ocean) ----
BG = "#0B1A2A"
CARD = "#12283D"
PRIMARY = "#38BDF8"   # cyan
ACCENT = "#34D399"    # teal-green
WARN = "#F87171"
AMBER = "#FBBF24"
TEXT = "#E8F1FA"
TEXT2 = "#9DB6CC"
TEXT3 = "#5F7A93"
BORDER = "#244461"
TRACK = "#1C374F"
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
    return SLIDES[slide_idx]["chunks"][cidx - 1]


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
    out.append(f'<rect x="64" y="52" width="34" height="6" rx="3" fill="{accent}"/>')
    out.append(T(108, 62, kicker.upper(), 15, fill=accent, weight=700, spacing="2.5"))
    out.append(T(64, 104, title, 34, fill=TEXT, weight=800))
    out.append(T(1216, 62, f"{idx:02d} / {total:02d}", 14, fill=TEXT3, weight=600, anchor="end", spacing="1.5"))
    return "".join(out)


def bars(x, y, w, h, series, maxv=None, fmt="{:g}"):
    """Horizontal bar group in absolute coords. series=[(label,val,color)]."""
    out = []
    maxv = maxv or max(v for _, v, _ in series)
    n = len(series)
    gap = 12
    bh = (h - gap * (n - 1)) / n
    labw = 132
    barw = w - labw - 66
    for i, (lab, val, col) in enumerate(series):
        by = y + i * (bh + gap)
        out.append(T(x, by + bh / 2 + 5, lab, 14.5, fill=TEXT2, weight=600))
        out.append(f'<rect x="{x+labw}" y="{by}" width="{barw}" height="{bh}" rx="{bh/2}" fill="{TRACK}"/>')
        bw = max(6, barw * (val / maxv))
        out.append(f'<rect x="{x+labw}" y="{by}" width="{bw:.1f}" height="{bh}" rx="{bh/2}" fill="{col}"/>')
        out.append(T(x + labw + bw + 10, by + bh / 2 + 5, fmt.format(val), 15.5, fill=TEXT, weight=800))
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
    b = [f'<rect width="{W}" height="{H}" fill="{BG}"/>']
    # right decorative panel: gridded ocean-flux motif
    px, py, pw, ph = 784, 150, 432, 300
    b.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="20" fill="{CARD}" stroke="{BORDER}"/>')
    b.append(T(px + 32, py + 40, "GRIDDED OCEAN CO2 FLUX", 13, fill=TEXT3, weight=700, spacing="2"))
    # flux grid: 14 cols x 6 rows of small cells, colored by a smooth field
    gx, gy = px + 32, py + 58
    cols, rows = 14, 6
    cw, chh, cg = 24, 22, 3
    ramp = [WARN, AMBER, ACCENT, PRIMARY]
    for r in range(rows):
        for c in range(cols):
            # smooth pseudo-field: source (warm) near equator band, sink (cool) at poles
            v = 0.5 + 0.5 * math.sin(c * 0.55 + r * 0.4) * math.cos(r * 0.7 - 0.3)
            idx = min(len(ramp) - 1, int(v * len(ramp)))
            col = ramp[idx]
            op = 0.35 + 0.5 * v
            b.append(f'<rect x="{gx + c*(cw+cg)}" y="{gy + r*(chh+cg)}" width="{cw}" height="{chh}" '
                     f'rx="3" fill="{col}" opacity="{op:.2f}"/>')
    # legend
    ly = gy + rows * (chh + cg) + 18
    b.append(T(px + 32, ly, "source", 12, fill=WARN, weight=700))
    b.append(T(px + pw - 32, ly, "sink", 12, fill=PRIMARY, weight=700, anchor="end"))
    b.append(T(px + 32, ly + 20, "monthly gridded  ·  Jan 2022 to Jul 2023", 12, fill=TEXT3, weight=500))

    # left title block = c1
    ch1 = chunk(1, 1)
    b.append(f'<g id="{esc(ch1["anchor_id"])}" data-cue-label="{esc(ch1["anchor_id"])}"><title>{esc(" ".join(ch1["cue_keywords"]))}</title><desc>{esc(ch1["text"][:180])}</desc>')
    b.append(f'<rect x="64" y="150" width="34" height="6" rx="3" fill="{PRIMARY}"/>')
    b.append(T(108, 160, "TSINGHUA  ·  MICROSOFT RESEARCH  ·  ICLR 2024", 14, fill=PRIMARY, weight=700, spacing="1.5"))
    b.append(T(64, 250, "Carbon Monitor Ocean", 64, fill=TEXT, weight=800))
    b.append(T(64, 300, "Near-real-time monitoring of the global ocean carbon sink", 24, fill=TEXT, weight=700))
    b.append(T(64, 344, "The ocean absorbs a large share of our carbon emissions, yet the", 18, fill=TEXT2, weight=500))
    b.append(T(64, 368, "official picture of its uptake always lags reality by about a year.", 18, fill=TEXT2, weight=500))
    b.append("</g>")
    b.append(T(64, 410, "Ke, Gui, Cao, Wang, Ciais, Friedlingstein, Liu  ·  arXiv:2312.01637", 14, fill=TEXT3, weight=600))

    # two highlight cards = c2, c3
    boxes = grid_boxes(2, x0=64, y0=470, x1=1216, y1=684, gap=26, cols=2)
    specs = [
        (chunk(1, 2), "THE DATASET", "CMO-NRT", "A near-real-time, monthly, gridded dataset of surface-ocean CO2 fugacity and air-sea flux.", PRIMARY),
        (chunk(1, 3), "THE METHOD", "CNN + semi-supervised", "Updates 10 biogeochemical models and 8 data products to the present month.", ACCENT),
    ]
    for (ch, kick, big, desc, col), (x, y, w, h) in zip(specs, boxes):
        b.append(card_open(ch, x, y, w, h, accent=col))
        b.append(T(x + 24, y + 36, kick, 13, fill=col, weight=700, spacing="2"))
        b.append(T(x + 24, y + 72, big, 24, fill=TEXT, weight=800))
        blk, _ = wrapped_block(x + 24, y + 100, desc, 14.5, TEXT2, 52, 20)
        b.append(blk)
        b.append(card_close())
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n' + "".join(b) + "\n</svg>\n"

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
        if spec.get("desc"):
            blk, _ = wrapped_block(ix2, cy + 22, spec["desc"], 15.5, TEXT, spec.get("mc", 40), 23, weight=500)
            b.append(blk)
    else:
        b.append(T(ix, cy, spec["kick"], 13, fill=col, weight=700, spacing="2"))
        ty = cy + 30
        if spec.get("big"):
            b.append(T(ix, ty + 20, spec["big"], 46, fill=TEXT, weight=800))
            if spec.get("biglabel"):
                b.append(T(ix, ty + 46, spec["biglabel"], 14, fill=TEXT2, weight=600))
            ty += 66
        if spec.get("desc"):
            blk, endy = wrapped_block(ix, ty + 4, spec["desc"], spec.get("size", 15.5), TEXT2, spec.get("mc", 46), 22, weight=500)
            b.append(blk)
    if spec.get("chart"):
        b.append(spec["chart"](x, y, w, h))
    b.append(card_close())
    return "".join(b)


# ---------- Slide 2: Problem ----------
def s2_chart(x, y, w, h):
    cx = x + 26
    cyy = y + h - 78
    return (T(cx, cyy - 8, "Reporting latency of the ocean sink", 12, fill=TEXT3, weight=600)
            + bars(cx, cyy, w - 52, 52, [
                ("Annual GCB", 12, WARN),
                ("CMO-NRT", 1, ACCENT)], maxv=12, fmt="{:g} mo"))

slides["02_problem"] = content_slide(2, 10, "Problem", "Our picture of the ocean sink is always a year old", [
    {"ch": chunk(2, 1), "kick": "A CLIMATE BUFFER", "accent": PRIMARY,
     "desc": "The ocean is one of the largest buffers against climate change, soaking up a big fraction of the CO2 we emit.", "mc": 40},
    {"ch": chunk(2, 2), "kick": "ALWAYS BEHIND", "accent": WARN, "big": "~1 yr",
     "biglabel": "lag of the annual Global Carbon Budget", "desc": "",
     "chart": s2_chart},
    {"ch": chunk(2, 3), "kick": "WE CANNOT SEE IT", "accent": AMBER,
     "desc": "When the ocean's uptake shifts, we simply cannot see the change until long after the fact.", "mc": 40},
    {"ch": chunk(2, 4), "kick": "WHY THE LAG", "accent": WARN,
     "desc": "Biogeochemical models are computationally heavy, and the surface-ocean observations they rely on are themselves delayed.", "mc": 42},
])


# ---------- Slide 3: Motivation ----------
slides["03_motivation"] = content_slide(3, 10, "Motivation", "Policy needs the sink now, not a year ago", [
    {"ch": chunk(3, 1), "kick": "PARIS STOCKTAKE", "accent": PRIMARY,
     "desc": "As countries move through the global stocktake, they need to know where the carbon is going right now.", "mc": 34},
    {"ch": chunk(3, 2), "kick": "TRUSTED BUT BACKWARD", "accent": AMBER,
     "desc": "Existing databases of ocean carbon fluxes are detailed and trustworthy, but always looking backward in time.", "mc": 34},
    {"ch": chunk(3, 3), "kick": "THE MISSING PIECE", "accent": ACCENT,
     "desc": "Bring that same rigor up to the present month, so scientists and policymakers can respond as the sink changes.", "mc": 34},
], cols=3)


# ---------- Slide 4: Contribution ----------
slides["04_contribution"] = content_slide(4, 10, "Contribution", "Carbon Monitor Ocean, updated to the present", [
    {"ch": chunk(4, 1), "num": "1", "kick": "THE DATASET", "accent": PRIMARY,
     "desc": "CMO-NRT: a near-real-time, monthly, gridded dataset of surface-ocean CO2 fugacity and air-sea flux.", "mc": 42},
    {"ch": chunk(4, 2), "num": "2", "kick": "UPDATE, NOT REPLACE", "accent": ACCENT,
     "desc": "Extends all 10 biogeochemical models and 8 data products of the Global Carbon Budget 2022 into a real-time framework.", "mc": 42},
    {"ch": chunk(4, 3), "num": "3", "kick": "OPEN RELEASE", "accent": AMBER,
     "desc": "Dataset and code released openly, on Figshare and on the project website.", "mc": 42},
], cols=3)


# ---------- Slide 5: Method ----------
def s5_diagram(x, y, w, h):
    # tiny conv-stack: 9 -> 64 -> 64 -> 1 across the bottom of the card
    cx = x + 26
    yy = y + h - 46
    stages = [("9", TEXT2), ("64", PRIMARY), ("64", PRIMARY), ("1", ACCENT)]
    bw, gap = 52, 40
    out = [T(cx, yy - 30, "conv + linear stack", 12, fill=TEXT3, weight=600)]
    for i, (lab, col) in enumerate(stages):
        bx = cx + i * (bw + gap)
        out.append(f'<rect x="{bx}" y="{yy-18}" width="{bw}" height="30" rx="6" fill="{TRACK}" stroke="{col}" stroke-width="1.5"/>')
        out.append(T(bx + bw / 2, yy + 2, lab, 15, fill=col, weight=800, anchor="middle"))
        if i < len(stages) - 1:
            ax = bx + bw
            out.append(f'<line x1="{ax}" y1="{yy-3}" x2="{ax+gap}" y2="{yy-3}" stroke="{TEXT3}" stroke-width="1.5"/>')
            out.append(f'<polygon points="{ax+gap},{yy-3} {ax+gap-7},{yy-7} {ax+gap-7},{yy+1}" fill="{TEXT3}"/>')
    return "".join(out)

def s5_eqbox(x, y, w, h):
    cx = x + 26
    yy = y + h - 52
    out = [f'<rect x="{cx}" y="{yy-24}" width="{w-52}" height="52" rx="8" fill="{TRACK}" stroke="{BORDER}"/>']
    out.append(T(cx + 16, yy + 8, "L = w * L_u + L_s", 20, fill=TEXT, weight=700, family="Consolas, 'Courier New', monospace"))
    out.append(T(x + w - 26, yy + 5, "supervised + consistency", 12, fill=TEXT3, weight=600, anchor="end"))
    return "".join(out)

slides["05_method"] = content_slide(5, 10, "Method", "Learn each model from observable predictors", [
    {"ch": chunk(5, 1), "num": "1", "kick": "TARGETS AND INPUTS", "accent": PRIMARY,
     "desc": "A neural network reproduces each model or product from year, month, lat, lon and 9 environmental variables (SST, salinity, chlorophyll, wind).", "mc": 44},
    {"ch": chunk(5, 2), "num": "2", "kick": "PATCH AND CONVOLVE", "accent": PRIMARY,
     "desc": "Global grids are cut into small 18x18 patches, then fed through stacked convolutional and linear layers.", "mc": 44, "chart": s5_diagram},
    {"ch": chunk(5, 3), "num": "3", "kick": "SEMI-SUPERVISED", "accent": ACCENT,
     "desc": "A supervised error on labeled points plus an unsupervised consistency loss that forces agreement between 10% and 30% feature masking.", "mc": 44, "chart": s5_eqbox},
    {"ch": chunk(5, 4), "num": "4", "kick": "MORE STABLE", "accent": AMBER,
     "desc": "Combining the two losses makes the model markedly more stable.", "mc": 44},
])


# ---------- Slide 6: Dataset & Benchmark ----------
slides["06_dataset"] = content_slide(6, 10, "Dataset and Benchmark", "Monthly gridded maps, updating 18 sources", [
    {"ch": chunk(6, 1), "kick": "THE PRODUCT", "accent": PRIMARY, "big": "18 mo",
     "biglabel": "Jan 2022 to Jul 2023, monthly & gridded", "desc": "Global surface-ocean CO2 fugacity and air-sea flux, built by updating 10 biogeochemical models and 8 data products of the Global Carbon Budget 2022.", "mc": 46},
    {"ch": chunk(6, 2), "kick": "THE INPUTS", "accent": ACCENT,
     "desc": "Satellite and reanalysis products: chlorophyll, sea-surface temperature, sea ice, mixed-layer depth, salinity, sea-surface height, pressure and wind.", "mc": 46},
], cols=2)


# ---------- Slide 7: Key Result ----------
def s7_chart(x, y, w, h):
    cx = x + 26
    cyy = y + h - 116
    return (T(cx, cyy - 8, "Prediction vs original correlation (R squared)", 12, fill=TEXT3, weight=600)
            + bars(cx, cyy, w - 52, 94, [
                ("Best GOBMs", 0.97, ACCENT),
                ("Most sources", 0.90, PRIMARY),
                ("Global aggregate", 0.85, PRIMARY)], maxv=1.0, fmt="{:.2f}"))

slides["07_key_result"] = content_slide(7, 10, "Key Result", "Predictions track the originals faithfully", [
    {"ch": chunk(7, 1), "kick": "HELD-OUT TEST", "accent": PRIMARY,
     "desc": "The authors held out the most recent two years of every model and product, trained on earlier data, then predicted the withheld period.", "mc": 40},
    {"ch": chunk(7, 2), "kick": "STRONG AGREEMENT", "accent": ACCENT,
     "desc": "For most of the 10 models and 8 products the correlation exceeds R squared of 0.9; global aggregates stay above 0.85.", "mc": 40,
     "chart": s7_chart},
    {"ch": chunk(7, 3), "kick": "TINY BIAS", "accent": AMBER,
     "desc": "On global averages the predictions run just slightly high, with most differences smaller than 3 microatmospheres.", "mc": 40},
])


# ---------- Slide 8: Ablation ----------
def s8_chart(x, y, w, h):
    cx = x + 26
    cyy = y + h - 150
    return (T(cx, cyy - 8, "Per-source R squared (models vs products)", 12, fill=TEXT3, weight=600)
            + bars(cx, cyy, w - 52, 128, [
                ("MRI-ESM2-1", 0.97, ACCENT),
                ("CESM2", 0.96, ACCENT),
                ("UOEX-Watson", 0.80, AMBER),
                ("MPI-SOMFFN", 0.53, WARN)], maxv=1.0, fmt="{:.2f}"))

slides["08_ablation"] = content_slide(8, 10, "Ablation Study", "Models reproduce more faithfully than products", [
    {"ch": chunk(8, 1), "kick": "MODEL BY MODEL", "accent": ACCENT,
     "desc": "Biogeochemical models are reproduced most faithfully, several above R squared 0.95; a few data products are noisier and scatter from the fit.", "mc": 40,
     "chart": s8_chart},
    {"ch": chunk(8, 2), "kick": "WHERE IT DIFFERS", "accent": PRIMARY,
     "desc": "Spatial difference maps confirm agreement is broadly uniform, with the largest residual gaps in the Arctic Ocean and the equatorial Pacific.", "mc": 40},
])


# ---------- Slide 9: Headline Numbers ----------
slides["09_headline"] = content_slide(9, 10, "Headline Numbers", "The numbers that matter", [
    {"ch": chunk(9, 1), "kick": "AT A GLANCE", "accent": PRIMARY,
     "desc": "Four figures that capture the impact of Carbon Monitor Ocean.", "mc": 40},
    {"ch": chunk(9, 2), "kick": "LATENCY COLLAPSED", "accent": ACCENT, "big": "1 yr to 1 mo",
     "biglabel": "near-real-time, Jan 2022 to Jul 2023", "desc": "The reporting delay drops from about a year to monthly.", "mc": 40},
    {"ch": chunk(9, 3), "kick": "VALIDATION", "accent": PRIMARY, "big": "R2 > 0.9",
     "biglabel": "for most of 18 sources; aggregate > 0.85", "desc": "Global monthly differences mostly under 3 microatmospheres.", "mc": 40},
    {"ch": chunk(9, 4), "kick": "AUXILIARY xCO2 MODEL", "accent": AMBER, "big": "1.74",
     "biglabel": "near-real-time xCO2 RMSE (~0.5% error)", "desc": "The atmospheric CO2 model is highly accurate too.", "mc": 40},
])


# ---------- Slide 10: Takeaway ----------
slides["10_takeaway"] = content_slide(10, 10, "Takeaway", "A once year-delayed sink, now near-real-time", [
    {"ch": chunk(10, 1), "kick": "THE IDEA", "accent": PRIMARY,
     "desc": "Pairing convolutional networks with semi-supervised learning to update trusted models turns a year-delayed picture into a near-real-time, monthly, gridded monitor.", "mc": 46},
    {"ch": chunk(10, 2), "kick": "WHY IT MATTERS", "accent": ACCENT,
     "desc": "It gives scientists and policymakers a far timelier, spatially detailed constraint on how much carbon the ocean is taking up, right when they need it.", "mc": 46},
], cols=2)


# ---- write ----
for name, svg in slides.items():
    (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")
    print("wrote", name)
print("done:", len(slides), "slides")
