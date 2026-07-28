#!/usr/bin/env python3
"""All-native SVG deck builder for NeuPL (run 075). Reads the anchor contract,
wraps every narration chunk in its own <g id="cue_..."> card with <title>
keywords, so --require-pptx-anchors resolves 100% from PPTX geometry.
Dark cobalt/teal theme, zero <image>, zero gradients, ASCII-only equations."""
import json, os, html, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONTRACT = os.path.join(HERE, "..", "meta", "visual_anchor_contract.json")
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
BG = "#0B1B2B"
PANEL = "#122A40"
PANEL2 = "#0F2236"
STROKE = "#1E3E5A"
INK = "#EAF2FA"
MUTE = "#9FB6CC"
TEAL = "#2FB6A8"
BLUE = "#4C86F0"
GOLD = "#E0A93B"
RED = "#E0655B"
GREEN = "#49C08A"
SANS = "Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO = "'DejaVu Sans Mono', 'Courier New', monospace"

contract = json.load(open(CONTRACT))
# map sid -> {index, chunks:[{aid, kw}]}
CMAP = {}
for s in contract["slides"]:
    CMAP[s["id"]] = {
        "index": s["index"],
        "chunks": [{"aid": c["anchor_id"], "kw": " ".join(c.get("cue_keywords", []))}
                   for c in s["chunks"]],
    }


def esc(t):
    return html.escape(str(t), quote=True)


def T(x, y, t, size=17, fill=INK, weight="normal", anchor="start", family=SANS, spacing=None):
    sp = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{sp}>{esc(t)}</text>')


def wrap(t, maxc):
    words = t.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= maxc:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(x, y, t, size=16, fill=MUTE, maxc=52, lh=23, weight="normal"):
    out = []
    for i, ln in enumerate(wrap(t, maxc)):
        out.append(T(x, y + i * lh, ln, size=size, fill=fill, weight=weight))
    return "".join(out), y + len(wrap(t, maxc)) * lh


def card(aid, kw, x, y, w, h, fill=PANEL, accent=TEAL):
    """Open a cue card group with a title (keywords) and a rounded rect + accent tab."""
    s = f'<g id="{aid}"><title>{esc(kw)}</title>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{STROKE}" stroke-width="1.2"/>'
    s += f'<rect x="{x}" y="{y+18}" width="5" height="30" rx="2.5" fill="{accent}"/>'
    return s


def endg():
    return "</g>"


def header(slide_no, title, kicker):
    s = []
    # inset accent tab (NOT full-bleed -> avoids edge_touch)
    s.append(f'<rect x="56" y="52" width="7" height="34" rx="3" fill="{TEAL}"/>')
    s.append(T(78, 66, kicker, size=15, fill=TEAL, weight="bold", spacing="2"))
    s.append(T(78, 104, title, size=34, fill=INK, weight="bold"))
    s.append(T(1224, 92, f"NeuPL  ·  {slide_no:02d} / 10", size=15, fill=MUTE, anchor="end"))
    s.append(f'<line x1="56" y1="128" x2="1224" y2="128" stroke="{STROKE}" stroke-width="1"/>')
    return "".join(s)


def footer(txt):
    return T(56, 706, txt, size=13, fill="#6E869C")


def svg_open():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" font-family="{SANS}">'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>')


def svg_close():
    return "</svg>"


# ---- generic 2x2 card grid geometry ----
GX = [56, 654]
CW = 570
def row_y(r):  # r=0 top, r=1 bottom
    return 168 + r * 268
CH = 250


def text_card(ci, sid, heading, body, x, y, w=CW, h=CH, accent=TEAL, maxc=54):
    c = CMAP[sid]["chunks"][ci]
    s = card(c["aid"], c["kw"], x, y, w, h, accent=accent)
    s += T(x + 26, y + 44, heading, size=21, fill=INK, weight="bold")
    p, _ = para(x + 26, y + 78, body, size=16, fill=MUTE, maxc=maxc, lh=24)
    s += p
    s += endg()
    return s


def kpi_card(ci, sid, big, label, sub, x, y, w=CW, h=CH, accent=TEAL):
    c = CMAP[sid]["chunks"][ci]
    s = card(c["aid"], c["kw"], x, y, w, h, accent=accent)
    s += T(x + 26, y + 46, label, size=17, fill=MUTE, weight="bold")
    s += T(x + 26, y + 132, big, size=58, fill=accent, weight="bold")
    p, _ = para(x + 26, y + 176, sub, size=15, fill=MUTE, maxc=54, lh=22)
    s += p
    s += endg()
    return s


slides = {}

# ---------- Slide 1: title ----------
def s1():
    sid = "title"
    s = [svg_open()]
    s.append(f'<rect x="56" y="52" width="7" height="34" rx="3" fill="{TEAL}"/>')
    s.append(T(78, 66, "ICLR 2022  ·  UNIVERSITY COLLEGE LONDON / DEEPMIND", size=15, fill=TEAL, weight="bold", spacing="1"))
    # c1 title banner
    c = CMAP[sid]["chunks"][0]
    s.append(f'<g id="{c["aid"]}"><title>{esc(c["kw"])}</title>')
    s.append(T(78, 150, "NeuPL: Neural Population Learning", size=52, fill=INK, weight="bold"))
    s.append(T(78, 196, "One conditional network that holds an entire population of policies", size=22, fill=MUTE))
    s.append("</g>")
    # three supporting cards
    cards = [
        (1, "Why populations", "Playing StarCraft or poker well needs a whole population of diverse policies, not one strategy."),
        (2, "The usual recipe", "Prior work grows the population by iteratively best-responding to previous policies — costly and forgetful."),
        (3, "NeuPL's answer", "Represent the entire population inside a single conditional network so policies share and transfer skill."),
    ]
    xs = [56, 466, 876]
    for ci, hd, bd in cards:
        c = CMAP[sid]["chunks"][ci]
        x = xs[ci - 1]
        s.append(card(c["aid"], c["kw"], x, 250, 348, 300, accent=[TEAL, BLUE, GOLD][ci - 1]))
        s.append(T(x + 24, 296, hd, size=20, fill=INK, weight="bold"))
        p, _ = para(x + 24, 332, bd, size=16, fill=MUTE, maxc=34, lh=25)
        s.append(p)
        s.append("</g>")
    s.append(footer("Liu, Marris, Lanctot, Piliouras, Marecki, Heess, Munos, Perez-Nieves — Neural Population Learning (ICLR 2022)"))
    s.append(svg_close())
    return "".join(s)
slides["title"] = s1()

# ---------- Slide 2: problem ----------
def s2():
    sid = "problem"
    s = [svg_open(), header(2, "Iterative best-response breaks down", "PROBLEM")]
    s.append(text_card(0, sid, "Classical PSRO", "Policy Space Response Oracles grow a set of strategies by repeatedly training a best-response to the current mixture.", GX[0], row_y(0), accent=BLUE))
    s.append(text_card(1, sid, "Fine in toy games", "In toy normal-form games this works cleanly, because a best-response can be solved for exactly.", GX[1], row_y(0), accent=TEAL))
    s.append(text_card(2, sid, "But not in real games", "Real games are temporal and partially observed, so best-responses can only be approximated — slowly and expensively.", GX[0], row_y(1), accent=GOLD))
    s.append(text_card(3, sid, "Two failure modes", "Under a finite budget you cannot tell a converged best-response from a stuck one, and each iteration relearns skills from scratch.", GX[1], row_y(1), accent=RED))
    s.append(footer("Approximate best-responses truncated on hand-crafted schedules leave under-trained policies in the population."))
    s.append(svg_close())
    return "".join(s)
slides["problem"] = s2()

# ---------- Slide 3: motivation ----------
def s3():
    sid = "motivation"
    s = [svg_open(), header(3, "Policies overlap — so share them", "MOTIVATION")]
    s.append(text_card(0, sid, "Why a population at all", "Game theory demands it: in a cyclic game like rock-paper-scissors no single policy is unbeatable, so you need many.", GX[0], row_y(0), accent=BLUE))
    s.append(text_card(1, sid, "Prior frameworks waste it", "They train policies one at a time and discard the knowledge shared between them, relearning perception each round.", GX[1], row_y(0), accent=GOLD))
    s.append(text_card(2, sid, "The key insight", "These policies overlap enormously — they share perception, memory, and motor skills that need not be relearned.", GX[0], row_y(1), accent=TEAL))
    s.append(text_card(3, sid, "The consequence", "If one model held the whole population and conditioned on which opponent it faces, early skills would transfer for free.", GX[1], row_y(1), accent=GREEN))
    s.append(footer("Empirical successes like StarCraft leagues used ~1000 agents at enormous cost — motivating a far cheaper alternative."))
    s.append(svg_close())
    return "".join(s)
slides["motivation"] = s3()

# ---------- Slide 4: contribution ----------
def s4():
    sid = "contribution"
    s = [svg_open(), header(4, "Three contributions", "CONTRIBUTION")]
    # c1 banner across top
    c = CMAP[sid]["chunks"][0]
    s.append(card(c["aid"], c["kw"], 56, 168, 1168, 78, fill=PANEL2, accent=TEAL))
    s.append(T(82, 216, "NeuPL turns population learning into one shared, conditional model — with three consequences.", size=20, fill=INK, weight="bold"))
    s.append("</g>")
    trip = [
        (1, "1 · One conditional model", "A single network represents a whole population of policies, each conditioned on a meta-game mixture over opponents.", BLUE),
        (2, "2 · A unifying framework", "Choosing the interaction graph recovers self-play, fictitious play, and PSRO as special cases of one method.", TEAL),
        (3, "3 · Convergence guarantees", "For grounded, lower-triangular interaction graphs and a suitable meta-solver, the population provably converges.", GOLD),
    ]
    xs = [56, 466, 876]
    for k, (ci, hd, bd, ac) in enumerate(trip):
        c = CMAP[sid]["chunks"][ci]
        x = xs[k]
        s.append(card(c["aid"], c["kw"], x, 270, 348, 280, accent=ac))
        s.append(T(x + 24, 316, hd, size=19, fill=INK, weight="bold"))
        p, _ = para(x + 24, 352, bd, size=16, fill=MUTE, maxc=34, lh=25)
        s.append(p)
        s.append("</g>")
    s.append(footer("The meta-graph solver — not a hand-tuned schedule — decides the effective population size."))
    s.append(svg_close())
    return "".join(s)
slides["contribution"] = s4()

# ---------- Slide 5: method (pipeline + equation) ----------
def s5():
    sid = "method"
    s = [svg_open(), header(5, "One opponent-conditioned network", "METHOD")]
    # c1: pipeline card (top-left, wide)
    c = CMAP[sid]["chunks"][0]
    x, y, w, h = 56, 168, 1168, 176
    s.append(card(c["aid"], c["kw"], x, y, w, h, accent=TEAL))
    s.append(T(x + 26, y + 40, "Policy index i  +  meta-strategy σ_i  →  one shared network Πθ", size=19, fill=INK, weight="bold"))
    # pipeline boxes
    px, py, bw, bh, gap = x + 40, y + 74, 150, 62, 58
    boxes = [("observation o", BLUE), ("meta-strategy σ_i", GOLD), ("shared net Πθ", TEAL), ("action aᵢ", GREEN)]
    for i, (lb, ac) in enumerate(boxes):
        bx = px + i * (bw + gap)
        s.append(f'<rect x="{bx}" y="{py}" width="{bw}" height="{bh}" rx="9" fill="{PANEL2}" stroke="{ac}" stroke-width="1.6"/>')
        s.append(T(bx + bw / 2, py + bh / 2 + 5, lb, size=15, fill=INK, anchor="middle"))
        if i < len(boxes) - 1:
            ax = bx + bw
            s.append(f'<line x1="{ax+6}" y1="{py+bh/2}" x2="{ax+gap-6}" y2="{py+bh/2}" stroke="{MUTE}" stroke-width="2"/>')
            s.append(f'<polygon points="{ax+gap-6},{py+bh/2-5} {ax+gap-6},{py+bh/2+5} {ax+gap+2},{py+bh/2}" fill="{MUTE}"/>')
    s.append("</g>")
    # c2 equation card
    c = CMAP[sid]["chunks"][1]
    x2, y2 = 56, 362
    s.append(card(c["aid"], c["kw"], x2, y2, 570, 176, accent=BLUE))
    s.append(T(x2 + 26, y2 + 40, "Objective: discounted return, double expectation", size=18, fill=INK, weight="bold"))
    s.append(f'<rect x="{x2+24}" y="{y2+58}" width="522" height="52" rx="8" fill="{PANEL2}" stroke="{STROKE}"/>')
    s.append(T(x2 + 40, y2 + 90, "max_θ  E_{j~σ_i} E_{τ} [ sum_t γ^t r_t ]", size=19, fill=TEAL, family=MONO))
    p, _ = para(x2 + 26, y2 + 138, "First over the sampled opponent j, then over the trajectory τ that unfolds.", size=15, fill=MUTE, maxc=58, lh=22)
    s.append(p)
    s.append("</g>")
    # c3 action-value card
    s.append(text_card(2, sid, "Trained by RL", "NeuPL jointly trains an opponent-conditioned action-value function Qθ(o,a|σ_i) to optimize the objective end-to-end.", 654, 362, w=570, h=176, accent=GREEN, maxc=52))
    # c4 interaction graph card (bottom-left slot already used; place below)
    c = CMAP[sid]["chunks"][3]
    x4, y4 = 56, 556
    s.append(card(c["aid"], c["kw"], x4, y4, 1168, 128, fill=PANEL2, accent=GOLD))
    s.append(T(x4 + 26, y4 + 40, "The interaction graph Σ assigns who plays whom", size=18, fill=INK, weight="bold"))
    p, _ = para(x4 + 26, y4 + 70, "A fixed matrix reproduces fictitious play; an adaptive graph Σ←F(U) from a meta-solver (e.g. FPSRO-N) reproduces PSRO — all inside one network.", size=16, fill=MUTE, maxc=118, lh=24)
    s.append(p)
    s.append("</g>")
    s.append(svg_close())
    return "".join(s)
slides["method"] = s5()

# ---------- Slide 6: dataset-benchmark ----------
def s6():
    sid = "dataset-benchmark"
    s = [svg_open(), header(6, "Three domains, rising difficulty", "DATASET / BENCHMARK")]
    c = CMAP[sid]["chunks"][0]
    s.append(card(c["aid"], c["kw"], 56, 168, 1168, 72, fill=PANEL2, accent=TEAL))
    s.append(T(82, 212, "NeuPL is validated across three domains chosen to span the difficulty spectrum.", size=20, fill=INK, weight="bold"))
    s.append("</g>")
    dom = [
        (1, "Rock-paper-scissors", "The classic purely cyclic normal-form game. The learned population can be directly visualized in strategy space.", BLUE),
        (2, "Running-with-scissors", "A spatiotemporal, partially observed game: players move on a grid, collect items, and infer a hidden inventory.", TEAL),
        (3, "MuJoCo Football (2v2)", "A large-scale Game-of-Skills where two-versus-two teams must simultaneously master control and coordination.", GOLD),
    ]
    xs = [56, 466, 876]
    for k, (ci, hd, bd, ac) in enumerate(dom):
        c = CMAP[sid]["chunks"][ci]
        x = xs[k]
        s.append(card(c["aid"], c["kw"], x, 262, 348, 300, accent=ac))
        s.append(T(x + 24, 306, f"{k+1}", size=30, fill=ac, weight="bold"))
        s.append(T(x + 24, 346, hd, size=19, fill=INK, weight="bold"))
        p, _ = para(x + 24, 384, bd, size=16, fill=MUTE, maxc=34, lh=25)
        s.append(p)
        s.append("</g>")
    s.append(footer("Running-with-scissors gives each player only a 4×4 first-person view and requires inferring the opponent's hidden inventory."))
    s.append(svg_close())
    return "".join(s)
slides["dataset-benchmark"] = s6()

# ---------- Slide 7: key-result (bar chart) ----------
def s7():
    sid = "key-result"
    s = [svg_open(), header(7, "More efficient and more robust", "KEY RESULT")]
    c = CMAP[sid]["chunks"][0]
    s.append(card(c["aid"], c["kw"], 56, 168, 1168, 66, fill=PANEL2, accent=TEAL))
    s.append(T(82, 208, "Headline: with only 8 policies, NeuPL is both more efficient and more robust than comparable PSRO.", size=19, fill=INK, weight="bold"))
    s.append("</g>")
    # c2 bar chart: gradient updates NeuPL 1x vs PSRO 2x, NeuPL still exploits
    c = CMAP[sid]["chunks"][1]
    x, y, w, h = 56, 250, 570, 292
    s.append(card(c["aid"], c["kw"], x, y, w, h, accent=BLUE))
    s.append(T(x + 26, y + 42, "Population 8: NeuPL exploits PSRO", size=18, fill=INK, weight="bold"))
    s.append(T(x + 26, y + 66, "despite half the gradient updates", size=14, fill=MUTE))
    # two horizontal bars = gradient updates
    bx, by, bmaxw = x + 40, y + 100, 400
    rows = [("NeuPL updates", 0.5, TEAL, "1×"), ("PSRO updates", 1.0, GOLD, "2×")]
    for i, (lb, frac, ac, tag) in enumerate(rows):
        yy = by + i * 56
        s.append(T(bx, yy - 6, lb, size=14, fill=MUTE))
        s.append(f'<rect x="{bx}" y="{yy}" width="{bmaxw}" height="26" rx="5" fill="{PANEL2}" stroke="{STROKE}"/>')
        s.append(f'<rect x="{bx}" y="{yy}" width="{bmaxw*frac:.0f}" height="26" rx="5" fill="{ac}"/>')
        s.append(T(bx + bmaxw * frac + 12, yy + 19, tag, size=15, fill=ac, weight="bold"))
    s.append(T(x + 26, y + 262, "Outcome: NeuPL beats PSRO on the same 8 policies", size=15, fill=GREEN, weight="bold"))
    s.append("</g>")
    # c3 effective-pop growth curve
    c = CMAP[sid]["chunks"][2]
    x3, y3, w3, h3 = 654, 250, 570, 292
    s.append(card(c["aid"], c["kw"], x3, y3, w3, h3, accent=TEAL))
    s.append(T(x3 + 26, y3 + 42, "Gains track effective population size", size=18, fill=INK, weight="bold"))
    # simple rising line from 5 to 8
    gx, gy, gw, gh = x3 + 50, y3 + 80, 460, 128
    s.append(f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy+gh}" stroke="{STROKE}" stroke-width="1.2"/>')
    s.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{STROKE}" stroke-width="1.2"/>')
    pts = [(0, 5), (0.33, 6), (0.66, 7.2), (1.0, 8)]
    def cy(v):
        return gy + gh - (v - 4) / (8 - 4) * gh
    poly = " ".join(f"{gx+px*gw:.0f},{cy(v):.0f}" for px, v in pts)
    s.append(f'<polyline points="{poly}" fill="none" stroke="{GREEN}" stroke-width="3"/>')
    for px, v in pts:
        s.append(f'<circle cx="{gx+px*gw:.0f}" cy="{cy(v):.0f}" r="4" fill="{GREEN}"/>')
    s.append(T(gx - 10, cy(5) + 4, "5", size=13, fill=MUTE, anchor="end"))
    s.append(T(gx - 10, cy(8) + 4, "8", size=13, fill=MUTE, anchor="end"))
    s.append(T(gx, gy + gh + 26, "training  →  effective policies grow 5 to 8", size=14, fill=MUTE))
    s.append(T(x3 + 26, y3 + 272, "Relative population performance rises with diversity", size=13, fill=MUTE))
    s.append("</g>")
    s.append(footer("Both continued-training and from-scratch PSRO variants prove equally exploitable — they fail to build on prior skill."))
    # c4 as footer-anchored small card overlapping bottom band
    c = CMAP[sid]["chunks"][3]
    s.append(f'<g id="{c["aid"]}"><title>{esc(c["kw"])}</title>')
    s.append(f'<rect x="820" y="556" width="404" height="120" rx="10" fill="{PANEL2}" stroke="{STROKE}"/>')
    s.append(f'<rect x="820" y="574" width="5" height="30" rx="2.5" fill="{RED}"/>')
    s.append(T(842, 596, "Both PSRO variants: equally exploitable", size=15, fill=INK, weight="bold"))
    p, _ = para(842, 624, "Continued-training and from-scratch alike fail to accumulate skill across iterations.", size=14, fill=MUTE, maxc=42, lh=21)
    s.append(p)
    s.append("</g>")
    s.append(svg_close())
    return "".join(s)
slides["key-result"] = s7()

# ---------- Slide 8: ablation (transfer bars) ----------
def s8():
    sid = "ablation-study"
    s = [svg_open(), header(8, "Transfer is what makes it work", "ABLATION STUDY")]
    s.append(text_card(0, sid, "The setup", "NeuPL agents are re-initialized either from scratch or by transferring encoder and memory from a trained NeuPL network.", GX[0], row_y(0), accent=BLUE, maxc=52))
    s.append(text_card(1, sid, "Easy opponents: both win", "Against an easily exploitable two-policy mixture, even the from-scratch agent eventually finds a counter — just slower.", GX[1], row_y(0), accent=TEAL, maxc=52))
    # c3 bars: success against 2 / 4 / 7 policy mixtures
    c = CMAP[sid]["chunks"][2]
    x, y, w, h = GX[0], row_y(1), 570, CH
    s.append(card(c["aid"], c["kw"], x, y, w, h, accent=GOLD))
    s.append(T(x + 26, y + 42, "Hard opponents: scratch collapses", size=18, fill=INK, weight="bold"))
    groups = [("n=2", 0.9, 0.95), ("n=4", 0.15, 0.85), ("n=7", 0.05, 0.8)]
    gx0, gy0, gh = x + 40, y + 70, 120
    gap = 168
    for i, (lb, sc, tr) in enumerate(groups):
        cx = gx0 + i * gap
        # scratch bar (red) + transfer bar (green)
        s.append(f'<rect x="{cx}" y="{gy0+gh-sc*gh:.0f}" width="46" height="{sc*gh:.0f}" rx="4" fill="{RED}"/>')
        s.append(f'<rect x="{cx+54}" y="{gy0+gh-tr*gh:.0f}" width="46" height="{tr*gh:.0f}" rx="4" fill="{GREEN}"/>')
        s.append(T(cx + 50, gy0 + gh + 20, lb, size=14, fill=MUTE, anchor="middle"))
    s.append(f'<line x1="{gx0}" y1="{gy0+gh}" x2="{gx0+3*gap-40}" y2="{gy0+gh}" stroke="{STROKE}"/>')
    s.append(T(x + 26, y + 226, "scratch", size=13, fill=RED, weight="bold"))
    s.append(T(x + 120, y + 226, "transfer", size=13, fill=GREEN, weight="bold"))
    s.append("</g>")
    s.append(text_card(3, sid, "The striking property", "As the population expands, discovering new strategies becomes easier — growth compounds instead of getting harder.", GX[1], row_y(1), accent=GREEN, maxc=52))
    s.append(footer("Against competent mixtures over four or seven policies, the randomly initialized agent fails outright."))
    s.append(svg_close())
    return "".join(s)
slides["ablation-study"] = s8()

# ---------- Slide 9: headline-numbers (KPI tiles) ----------
def s9():
    sid = "headline-numbers"
    s = [svg_open(), header(9, "The numbers", "HEADLINE NUMBERS")]
    s.append(kpi_card(0, sid, "8 vs 8", "Population match", "A NeuPL population capped at 8 policies beats PSRO populations of 8 — while PSRO used 2× the gradient updates.", GX[0], row_y(0), accent=TEAL))
    s.append(kpi_card(1, sid, "5 → 8", "Effective diversity", "As relative population performance climbs, the effective number of distinct policies grows from five to eight.", GX[1], row_y(0), accent=BLUE))
    s.append(kpi_card(2, sid, "2 / 4 / 7", "Transfer study", "Nash mixtures over two, four, and seven policies, each repeated five times to measure exploiter learning.", GX[0], row_y(1), accent=GOLD))
    s.append(kpi_card(3, sid, "✓", "Bottom line", "Together these establish NeuPL as more sample-efficient and more robust than standard iterative baselines.", GX[1], row_y(1), accent=GREEN))
    s.append(footer("A population cap greater than 8 yields only marginal extra exploitability; effective size plateaus around 12."))
    s.append(svg_close())
    return "".join(s)
slides["headline-numbers"] = s9()

# ---------- Slide 10: takeaway ----------
def s10():
    sid = "takeaway"
    s = [svg_open(), header(10, "Takeaway", "TAKEAWAY")]
    c = CMAP[sid]["chunks"][0]
    s.append(card(c["aid"], c["kw"], 56, 178, 570, 380, accent=TEAL))
    s.append(T(82, 226, "The one line", size=18, fill=TEAL, weight="bold"))
    p, _ = para(82, 268, "Represent the whole population inside a single conditional model, and let the interaction graph decide which opponents each policy faces.", size=19, fill=INK, maxc=40, lh=30)
    s.append(p)
    s.append("</g>")
    c = CMAP[sid]["chunks"][1]
    s.append(card(c["aid"], c["kw"], 654, 178, 570, 380, accent=GOLD))
    s.append(T(680, 226, "Why it matters", size=18, fill=GOLD, weight="bold"))
    bullets = [
        ("Cheaper", "Population learning stops being a sequence of wasteful from-scratch runs."),
        ("Guaranteed", "Grounded lower-triangular graphs come with convergence guarantees."),
        ("Emergent", "Most surprisingly, discovering novel behaviours gets easier as the population grows."),
    ]
    yy = 268
    for hd, bd in bullets:
        s.append(f'<circle cx="690" cy="{yy-6}" r="5" fill="{GOLD}"/>')
        s.append(T(708, yy, hd, size=18, fill=INK, weight="bold"))
        p, ny = para(708, yy + 26, bd, size=15, fill=MUTE, maxc=44, lh=22)
        s.append(p)
        yy = ny + 24
    s.append("</g>")
    s.append(footer("NeuPL — Neural Population Learning  ·  ICLR 2022  ·  one framework recovers self-play, fictitious play, and PSRO."))
    s.append(svg_close())
    return "".join(s)
slides["takeaway"] = s10()

# ---------- write with numeric prefixes in narration order ----------
order = ["title", "problem", "motivation", "contribution", "method",
         "dataset-benchmark", "key-result", "ablation-study", "headline-numbers", "takeaway"]
for i, sid in enumerate(order):
    fn = os.path.join(OUT, f"{i+1:02d}_{sid}.svg")
    open(fn, "w").write(slides[sid])
    print("wrote", fn)
print("done")
