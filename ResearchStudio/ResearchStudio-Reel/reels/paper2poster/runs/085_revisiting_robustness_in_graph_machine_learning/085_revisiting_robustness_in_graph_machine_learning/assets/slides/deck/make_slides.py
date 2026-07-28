#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 085.
Revisiting Robustness in Graph Machine Learning (ICLR 2023, TUM).
Each narration chunk -> its own <g id="cue_..."> card with <title>=keywords.
No <image>, no gradients. viewBox 0 0 1280 720. Dark cobalt/teal theme."""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
AMAP = json.load(open(os.path.join(HERE, "_anchor_map.json")))
OUT = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
BG = "#0B1B2B"
CARD = "#10263B"
CARD2 = "#12314A"
STROKE = "#1E3A52"
TEXT = "#E8F0F7"
MUTED = "#9DB2C4"
TEAL = "#35D0BA"
BLUE = "#4C8DFF"
GOLD = "#F5B841"
RED = "#FF6B6B"
GREEN = "#48D597"
FF = "Arial, 'Helvetica Neue', sans-serif"
MONO = "'DejaVu Sans Mono', 'Courier New', monospace"

def esc(s): return html.escape(str(s), quote=True)

def rect(x, y, w, h, fill=CARD, stroke=STROKE, sw=1.5, rx=14, op=1.0):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"/>')

def line(x1, y1, x2, y2, stroke=STROKE, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def T(x, y, s, size=18, fill=TEXT, weight="normal", anchor="start", ff=FF, spacing=None):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{ff}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{ls}>{esc(s)}</text>')

def wrap(s, maxchars):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= maxchars:
            cur = (cur + " " + w).strip()
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def para(x, y, s, size=17, fill=MUTED, width=520, lh=None, weight="normal", ff=FF):
    lh = lh or int(size * 1.42)
    maxchars = max(8, int(width / (size * 0.53)))
    out = []
    yy = y
    for ln in wrap(s, maxchars):
        out.append(T(x, yy, ln, size=size, fill=fill, weight=weight, ff=ff))
        yy += lh
    return "\n".join(out), yy

def chip(x, y, w, txt, fill, tcol="#08131F"):
    return (rect(x, y, w, 26, fill=fill, stroke=fill, sw=0, rx=13) +
            T(x + w / 2, y + 18, txt, size=14, fill=tcol, weight="bold", anchor="middle"))

def header(kicker, title, idx):
    s = []
    s.append(rect(64, 44, 6, 40, fill=TEAL, stroke=TEAL, sw=0, rx=3))
    s.append(T(86, 62, kicker, size=15, fill=TEAL, weight="bold", spacing="2"))
    s.append(T(86, 90, title, size=30, fill=TEXT, weight="bold"))
    s.append(T(1216, 68, f"{idx:02d} / 10", size=15, fill=MUTED, anchor="end", weight="bold"))
    s.append(line(64, 104, 1216, 104, stroke=STROKE, sw=1.5))
    return "\n".join(s)

def group(aid, kw, body):
    title = " ".join(kw) if isinstance(kw, list) else str(kw)
    return f'<g id="{esc(aid)}"><title>{esc(title)}</title>\n{body}\n</g>'

def chunks(sid):
    return AMAP[sid]["chunks"]

def svg_wrap(inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>\n{inner}\n</svg>\n')

# ------------------------------------------------------------------ slides
def s_title(sid):
    c = chunks(sid); s = []
    s.append(rect(64, 44, 6, 40, fill=TEAL, stroke=TEAL, sw=0, rx=3))
    s.append(T(86, 66, "ICLR 2023  ·  TECHNICAL UNIVERSITY OF MUNICH", size=16, fill=TEAL, weight="bold", spacing="2"))
    s.append(T(84, 150, "Revisiting Robustness in", size=58, fill=TEXT, weight="bold"))
    s.append(T(84, 214, "Graph Machine Learning", size=58, fill=TEXT, weight="bold"))
    s.append(T(84, 258, "Are graph neural networks fragile — or over-robust?", size=23, fill=GOLD))
    s.append(T(84, 300, "Lukas Gosch · Daniel Sturm · Simon Geisler · Stephan Gunnemann", size=18, fill=MUTED))
    # four narrative beat cards along the bottom
    labels = [
        ("THE PREMISE", "GNNs are famously easy to fool with tiny edge edits — long read as pure adversarial fragility."),
        ("THE QUESTION", "Do those 'small' perturbations actually preserve a node's true meaning?"),
        ("OVER-ROBUSTNESS", "A semantics-aware view shows every GNN is over-robust: unchanged even after the label flips."),
        ("THE FIX", "Feeding the training label structure back in via label propagation sharply cuts over-robustness."),
    ]
    accents = [BLUE, GOLD, RED, GREEN]
    x0, y0, cw, gap = 64, 360, 278, 18
    for i, ch in enumerate(c):
        x = x0 + i * (cw + gap)
        b = [rect(x, y0, cw, 250, fill=CARD)]
        b.append(rect(x, y0, cw, 6, fill=accents[i], stroke=accents[i], sw=0, rx=3))
        b.append(T(x + 20, y0 + 44, labels[i][0], size=14, fill=accents[i], weight="bold", spacing="1"))
        p, _ = para(x + 20, y0 + 76, labels[i][1], size=16, fill=TEXT, width=cw - 40, lh=24)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    s.append(T(84, 648, "arxiv.org/abs/2305.00851   ·   cs.cit.tum.de/daml/revisiting-robustness", size=16, fill=MUTED))
    return svg_wrap("\n".join(s))

def two_by_two(sid, kicker, title, cards, accents=None):
    """cards: list of (heading, body) aligned to chunks."""
    c = chunks(sid); s = [header(kicker, title, AMAP[sid]["index"])]
    accents = accents or [TEAL, BLUE, GOLD, GREEN]
    pos = [(64, 122), (656, 122), (64, 400), (656, 400)]
    cw, chh = 560, 258
    for i, ch in enumerate(c):
        x, y = pos[i]; head, body = cards[i]
        b = [rect(x, y, cw, chh, fill=CARD)]
        b.append(rect(x, y, 6, chh, fill=accents[i % len(accents)], stroke=accents[i % len(accents)], sw=0, rx=3))
        b.append(T(x + 26, y + 42, head, size=21, fill=TEXT, weight="bold"))
        b.append(line(x + 26, y + 56, x + cw - 26, y + 56, stroke=STROKE, sw=1))
        p, _ = para(x + 26, y + 88, body, size=17, fill=MUTED, width=cw - 52, lh=25)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_problem(sid):
    c = chunks(sid); s = [header("PROBLEM", "No visual check for a 'small' graph edit", AMAP[sid]["index"])]
    # c1 top-left: definition
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "What an adversarial example must be", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 78, "A small change that does NOT alter the input's true category. For images a human just looks and verifies.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(chip(x + 26, y + 196, 250, "images: human eyeball verifies", GOLD))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: graphs settled on L0 budget
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Graphs have no such check", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 78, "So the community settled on a proxy: just count the edited edges with an L-zero budget.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(rect(x + 26, y + 176, cw - 52, 52, fill=CARD2, stroke=STROKE))
    b.append(T(x + 42, y + 208, "budget  =  # edited edges  <=  L0", size=18, fill=TEAL, ff=MONO, weight="bold"))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: low-degree rewire diagram
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=RED, stroke=RED, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "Low-degree nodes dominate real graphs", size=20, fill=TEXT, weight="bold"))
    b.append(T(x + 26, y + 66, "+2 edges can completely rewire a small neighbourhood:", size=15, fill=MUTED))
    # before graph
    def node(cx, cy, col, r=15):
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="#0B1B2B" stroke-width="2"/>'
    bx, by = x + 90, y + 168
    b.append(line(bx, by, bx - 46, by + 34, stroke=MUTED, sw=2))
    b.append(line(bx, by, bx + 46, by + 34, stroke=MUTED, sw=2))
    b.append(node(bx - 46, by + 34, BLUE)); b.append(node(bx + 46, by + 34, BLUE))
    b.append(node(bx, by, TEAL, 18))
    b.append(T(bx, by - 30, "before: class A", size=13, fill=MUTED, anchor="middle"))
    b.append(T(x + 300, y + 168, "→", size=40, fill=GOLD, anchor="middle"))
    ax, ay = x + 470, y + 158
    for dx in (-70, -24, 24, 70):
        b.append(line(ax, ay, ax + dx, ay + 44, stroke=RED if abs(dx) > 40 else MUTED, sw=2, dash="4 3" if abs(dx) > 40 else None))
    b.append(node(ax - 70, ay + 44, RED)); b.append(node(ax + 70, ay + 44, RED))
    b.append(node(ax - 24, ay + 44, BLUE)); b.append(node(ax + 24, ay + 44, BLUE))
    b.append(node(ax, ay, RED, 18))
    b.append(T(ax, ay - 20, "after +2: class B", size=13, fill=RED, anchor="middle"))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: the question
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "The unanswered question", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "Do standard perturbations really keep a node's semantic content — or are we attacking nodes whose true label has already flipped?", size=18, fill=TEXT, width=cw - 52, lh=27)
    b.append(p)
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_motivation(sid):
    return two_by_two(sid, "MOTIVATION", "The semantics-preserving assumption is untested", [
        ("A load-bearing assumption", "The belief that GNNs are 'easily fooled' rests on assuming the perturbations used are semantics-preserving in the first place."),
        ("Existing proxies fall short", "Only a few works go beyond raw edge counts — adding proxies like the degree distribution or homophily. None directly measure whether the ground-truth label is preserved."),
        ("Why it matters", "If a 'small' perturbation has actually changed a node's true class, a model that keeps its prediction fixed is not robustly correct — it is wrong in a new, hidden way."),
        ("What is needed", "A principled, label-aware notion of what a semantics-preserving graph perturbation really is."),
    ], accents=[BLUE, GOLD, RED, TEAL])

def s_contribution(sid):
    c = chunks(sid); s = [header("CONTRIBUTION", "Four contributions", AMAP[sid]["index"])]
    pos = [(64, 122), (656, 122), (64, 400), (656, 400)]
    cw, chh = 560, 258
    nums = ["1", "2", "3", "4"]
    accents = [TEAL, BLUE, GOLD, GREEN]
    heads = ["Define over-robustness", "Measure it on CSBMs", "A free fix: label propagation", "No inductive tradeoff"]
    bodies = [
        "A semantics-aware notion of adversarial robustness for node predictions — and with it a new concept for graphs: over-robustness, robustness against admissible perturbations whose ground-truth label has already changed.",
        "Using Contextual Stochastic Block Models, common perturbation sets contain a large fraction of graphs with changed semantics, and every examined GNN is significantly over-robust — matched on real-world graphs.",
        "Folding the known label structure into inference via label propagation significantly reduces over-robustness at no cost to accuracy or genuine adversarial robustness.",
        "Classifying an inductively sampled node carries no robustness-accuracy tradeoff at all.",
    ]
    for i, ch in enumerate(c):
        x, y = pos[i]
        b = [rect(x, y, cw, chh, fill=CARD)]
        b.append(f'<circle cx="{x+42}" cy="{y+44}" r="20" fill="{accents[i]}"/>')
        b.append(T(x + 42, y + 51, nums[i], size=22, fill="#08131F", weight="bold", anchor="middle"))
        b.append(T(x + 78, y + 51, heads[i], size=21, fill=TEXT, weight="bold"))
        b.append(line(x + 26, y + 66, x + cw - 26, y + 66, stroke=STROKE, sw=1))
        p, _ = para(x + 26, y + 98, bodies[i], size=16, fill=MUTED, width=cw - 52, lh=24)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_method(sid):
    c = chunks(sid); s = [header("METHOD", "A trusted reference that knows the true label", AMAP[sid]["index"])]
    # c1 top-left: reference classifier g
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Bayes-optimal reference g", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 78, "On CSBMs the true generative model is known, so the Bayes-optimal classifier — the most likely class given the data — is derivable and used as ground-truth reference g.", size=16, fill=MUTED, width=cw - 52, lh=24)
    b.append(p)
    b.append(rect(x + 26, y + 196, cw - 52, 44, fill=CARD2, stroke=STROKE))
    b.append(T(x + 42, y + 224, "g  =  argmax_c  P(class = c | data)", size=17, fill=TEAL, ff=MONO, weight="bold"))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: over-robust example definition (pipeline)
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=RED, stroke=RED, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "An over-robust example", size=20, fill=TEXT, weight="bold"))
    rows = [("clean input", "model f  =  reference g", GREEN, "agree"),
            ("perturb graph", "reference g  flips", GOLD, "semantics changed"),
            ("but ...", "model f  keeps old prediction", RED, "over-robust")]
    ry = y + 72
    for lab, expr, col, tag in rows:
        b.append(f'<circle cx="{x+38}" cy="{ry-5}" r="6" fill="{col}"/>')
        b.append(T(x + 56, ry, expr, size=16, fill=TEXT, weight="bold", ff=MONO))
        b.append(T(x + cw - 26, ry, tag, size=13, fill=col, anchor="end"))
        ry += 52
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: metric
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Measuring over-robustness", size=20, fill=TEXT, weight="bold"))
    b.append(rect(x + 26, y + 66, cw - 52, 60, fill=CARD2, stroke=STROKE))
    b.append(T(x + 44, y + 103, "OR  =  1  -  ( r_semantic / r_conventional )", size=18, fill=TEAL, ff=MONO, weight="bold"))
    p, _ = para(x + 26, y + 150, "OR = 0.2 means 20% of the measured robustness lies beyond genuine semantic change — undesirable, stubborn robustness.", size=16, fill=MUTED, width=cw - 52, lh=24)
    b.append(p)
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: GNN + LP
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GREEN, stroke=GREEN, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "The remedy: GNN + label propagation", size=19, fill=TEXT, weight="bold"))
    # pipeline boxes
    def pbox(px, py, pw, txt, col):
        return rect(px, py, pw, 46, fill=CARD2, stroke=col, sw=2) + T(px + pw / 2, py + 29, txt, size=15, fill=TEXT, weight="bold", anchor="middle")
    py = y + 86
    b.append(pbox(x + 26, py, 150, "GNN f", BLUE))
    b.append(T(x + 190, py + 29, "+", size=26, fill=MUTED, anchor="middle"))
    b.append(pbox(x + 210, py, 300, "training-graph labels (propagated)", GREEN))
    b.append(T(x + cw / 2, py + 104, "→  lower over-robustness, same accuracy", size=17, fill=GREEN, anchor="middle", weight="bold"))
    p, _ = para(x + 26, y + 210, "Known labels are fed into inference to cut unwanted over-robustness.", size=15, fill=MUTED, width=cw - 52, lh=22)
    b.append(p)
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_dataset(sid):
    c = chunks(sid); s = [header("DATASET / BENCHMARK", "Contextual Stochastic Block Models", AMAP[sid]["index"])]
    # c1 top-left: CSBM why
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Why CSBMs", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 80, "A controlled generative model whose ground truth is known, so the Bayes-optimal reference can be computed exactly for every node.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(chip(x + 26, y + 196, 240, "exact Bayes reference available", TEAL))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: config KPIs
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Configuration", size=20, fill=TEXT, weight="bold"))
    kpis = [("1,000", "nodes / graph"), ("Cora", "matched edge stats"), ("1,000", "test nodes"), ("10", "graphs averaged")]
    kx, ky = x + 26, y + 70
    for i, (v, l) in enumerate(kpis):
        px = kx + (i % 2) * 262; py = ky + (i // 2) * 88
        b.append(rect(px, py, 246, 76, fill=CARD2, stroke=STROKE))
        b.append(T(px + 18, py + 42, v, size=28, fill=GOLD, weight="bold"))
        b.append(T(px + 18, py + 64, l, size=14, fill=MUTED))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: K sweep axis
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Feature signal strength K", size=20, fill=TEXT, weight="bold"))
    ax0, ax1, ayy = x + 60, x + cw - 60, y + 150
    b.append(line(ax0, ayy, ax1, ayy, stroke=MUTED, sw=2))
    ticks = ["0.1", "0.5", "1", "2", "5"]
    for i, tk in enumerate(ticks):
        tx = ax0 + (ax1 - ax0) * i / (len(ticks) - 1)
        b.append(line(tx, ayy - 6, tx, ayy + 6, stroke=MUTED, sw=2))
        b.append(T(tx, ayy + 26, tk, size=15, fill=TEXT, anchor="middle", weight="bold"))
    b.append(T(ax0, ayy - 18, "features weak,", size=13, fill=RED, anchor="start"))
    b.append(T(ax0, ayy - 2, "structure matters", size=13, fill=RED, anchor="start"))
    b.append(T(ax1, ayy - 18, "features strong,", size=13, fill=GREEN, anchor="end"))
    b.append(T(ax1, ayy - 2, "structure needless", size=13, fill=GREEN, anchor="end"))
    b.append(T(x + 26, y + 232, "K swept from 0.1 to 5 across the regime", size=15, fill=MUTED))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: real-world corroboration
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GREEN, stroke=GREEN, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Corroborated beyond CSBMs", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 80, "The same patterns hold on the real-world Cora-ML graph and on a Barabasi-Albert model with community structure.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(chip(x + 26, y + 188, 130, "Cora-ML", BLUE))
    b.append(chip(x + 168, y + 188, 230, "Barabasi-Albert communities", GOLD))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_keyresult(sid):
    c = chunks(sid); s = [header("KEY RESULT", "Perturbation sets are full of flipped labels", AMAP[sid]["index"])]
    # c1 top-left: framing
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "The finding", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "For a majority of nodes, the standard perturbation sets are full of graphs whose true label has already changed.", size=18, fill=TEXT, width=cw - 52, lh=27)
    b.append(p)
    b.append(chip(x + 26, y + 196, 300, "'small' edit  =/=  semantics preserved", RED))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: 99.4% KPI
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=RED, stroke=RED, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Semantics already changed", size=20, fill=TEXT, weight="bold"))
    b.append(T(x + cw / 2, y + 150, "99.4%", size=76, fill=RED, weight="bold", anchor="middle"))
    b.append(T(x + cw / 2, y + 200, "of target nodes have a perturbed graph", size=16, fill=MUTED, anchor="middle"))
    b.append(T(x + cw / 2, y + 224, "with a changed true label   (K = 1, degree+2 budget)", size=15, fill=MUTED, anchor="middle"))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: every GNN over-robust bars near upper bound
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "Every GNN is over-robust", size=20, fill=TEXT, weight="bold"))
    b.append(T(x + 26, y + 62, "over-robustness at K = 0.1, weak L2 attack", size=13, fill=MUTED))
    # horizontal bars clustering near the 43% MLP upper bound
    bars = [("MLP (perfect-robust ref)", 43, RED), ("GCN", 41, GOLD), ("GAT", 40, GOLD), ("APPNP", 39, GOLD)]
    bx0, maxw, bh = x + 210, 300, 26
    scale = maxw / 50.0
    for i, (lab, val, col) in enumerate(bars):
        by = y + 92 + i * 38
        b.append(T(x + 26, by + 18, lab, size=14, fill=TEXT))
        b.append(rect(bx0, by, maxw, bh, fill=CARD2, stroke=STROKE, sw=1, rx=6))
        b.append(rect(bx0, by, val * scale, bh, fill=col, stroke=col, sw=0, rx=6))
        b.append(T(bx0 + val * scale + 8, by + 18, f"{val}%", size=14, fill=col, weight="bold"))
    # upper-bound dashed line at 43
    ubx = bx0 + 43 * scale
    b.append(line(ubx, y + 88, ubx, y + 240, stroke=RED, sw=1.5, dash="4 3"))
    b.append(T(ubx, y + 248, "upper bound", size=12, fill=RED, anchor="middle"))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: interpretation
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "What 43% means", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "Even a perfectly robust reference (an MLP) shows 43% over-robustness: 43% of its measured adversarial robustness is undesirable — robustness beyond genuine semantic change. All GNNs cluster close to that bound.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_ablation(sid):
    c = chunks(sid); s = [header("ABLATION STUDY", "Label propagation cuts over-robustness — for free", AMAP[sid]["index"])]
    # c1 top-left: framing
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "The key ablation", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "Applying label propagation on top of a GNN sharply lowers over-robustness — and LP on its own achieves the lowest over-robustness of any method.", size=18, fill=TEXT, width=cw - 52, lh=27)
    b.append(p)
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: bar chart K=0.5
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GREEN, stroke=GREEN, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "Over-robustness at K = 0.5", size=20, fill=TEXT, weight="bold"))
    bars = [("GCN + LP", 21, GOLD), ("LP only", 14, GREEN)]
    base = y + 220; maxh = 120; scale = maxh / 45.0
    bw = 150
    for i, (lab, val, col) in enumerate(bars):
        bxx = x + 90 + i * 220
        bh = val * scale
        b.append(rect(bxx, base - bh, bw, bh, fill=col, stroke=col, sw=0, rx=6))
        b.append(T(bxx + bw / 2, base - bh - 12, f"{val}%", size=22, fill=col, weight="bold", anchor="middle"))
        b.append(T(bxx + bw / 2, base + 24, lab, size=15, fill=TEXT, anchor="middle", weight="bold"))
    b.append(line(x + 60, base, x + cw - 40, base, stroke=STROKE, sw=1.5))
    b.append(T(x + 26, y + 70, "lower = less stubborn robustness", size=13, fill=MUTED))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: comes for free
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "And it comes for free", size=20, fill=TEXT, weight="bold"))
    rows = [("test accuracy", "no drop", GREEN), ("adversarial robustness", "often improves", GREEN), ("structure still matters", "preserved", GREEN)]
    ry = y + 84
    for lab, tag, col in rows:
        b.append(f'<circle cx="{x+38}" cy="{ry-5}" r="6" fill="{col}"/>')
        b.append(T(x + 56, ry, lab, size=17, fill=TEXT))
        b.append(T(x + cw - 26, ry, tag, size=16, fill=col, anchor="end", weight="bold"))
        ry += 46
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: stronger attacks Nettack
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=RED, stroke=RED, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "Robust to stronger attacks", size=20, fill=TEXT, weight="bold"))
    b.append(T(x + 26, y + 62, "under Nettack, some over-robustness always remains", size=13, fill=MUTED))
    bars = [("GCN", 11.4, GOLD), ("MLP", 19.2, RED)]
    bx0, maxw, bh = x + 130, 300, 34
    scale = maxw / 25.0
    for i, (lab, val, col) in enumerate(bars):
        by = y + 100 + i * 60
        b.append(T(x + 26, by + 23, lab, size=16, fill=TEXT, weight="bold"))
        b.append(rect(bx0, by, maxw, bh, fill=CARD2, stroke=STROKE, sw=1, rx=6))
        b.append(rect(bx0, by, val * scale, bh, fill=col, stroke=col, sw=0, rx=6))
        b.append(T(bx0 + val * scale + 8, by + 23, f"{val}%", size=16, fill=col, weight="bold"))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_headline(sid):
    c = chunks(sid); s = [header("HEADLINE NUMBERS", "The impact in four numbers", AMAP[sid]["index"])]
    # c1 top strip: intro
    x, y, cw = 64, 122, 1152
    b = [rect(x, y, cw, 70, fill=CARD), rect(x, y, 6, 70, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 28, y + 44, "A semantics-aware lens reframes robustness in graph ML — the headline numbers:", size=20, fill=TEXT, weight="bold"))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # three big KPI tiles (c2,c3,c4)
    tiles = [
        ("99.4%", "of target nodes get a perturbation that changes the true label (common threat model)", RED),
        ("43%", "over-robustness even for a perfectly robust classifier at low signal strength", GOLD),
        ("~21%", "GCN over-robustness after label propagation; ~11-19% remains even under Nettack", GREEN),
    ]
    tw, gap = 368, 24
    for i, ch in enumerate(c[1:]):
        x = 64 + i * (tw + gap); y = 214
        v, l, col = tiles[i]
        b = [rect(x, y, tw, 420, fill=CARD)]
        b.append(rect(x, y, tw, 8, fill=col, stroke=col, sw=0, rx=4))
        b.append(T(x + tw / 2, y + 200, v, size=90, fill=col, weight="bold", anchor="middle"))
        p, _ = para(x + 34, y + 268, l, size=19, fill=TEXT, width=tw - 68, lh=28)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_takeaway(sid):
    c = chunks(sid); s = [header("TAKEAWAY", "Not fragile — over-robust", AMAP[sid]["index"])]
    tiles = [
        ("GNNs are over-robust, not just fragile", "A large part of their measured robustness is stubborn robustness that persists after a node's true meaning has already changed — which conventional evaluations wrongly credit as good behaviour.", RED),
        ("Label propagation is a free fix", "Bringing the training graph's label structure into inference reduces over-robustness while improving accuracy and real adversarial robustness.", GREEN),
        ("No inductive tradeoff", "With a semantics-aware definition, classifying a newly added node carries no robustness-accuracy tradeoff at all — changing how robustness in graph ML ought to be measured.", TEAL),
    ]
    tw, gap = 368, 24
    for i, ch in enumerate(c):
        x = 64 + i * (tw + gap); y = 140
        head, body, col = tiles[i]
        b = [rect(x, y, tw, 470, fill=CARD)]
        b.append(rect(x, y, tw, 8, fill=col, stroke=col, sw=0, rx=4))
        b.append(f'<circle cx="{x+42}" cy="{y+58}" r="18" fill="{col}"/>')
        b.append(T(x + 42, y + 65, str(i + 1), size=20, fill="#08131F", weight="bold", anchor="middle"))
        hp, hy = para(x + 74, y + 52, head, size=21, fill=TEXT, width=tw - 100, lh=27, weight="bold")
        b.append(hp)
        p, _ = para(x + 34, y + 168, body, size=18, fill=MUTED, width=tw - 68, lh=27)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    s.append(T(64, 682, "Revisiting Robustness in Graph Machine Learning  ·  ICLR 2023  ·  arxiv.org/abs/2305.00851", size=15, fill=MUTED))
    return svg_wrap("\n".join(s))

BUILDERS = {
    "title": s_title, "problem": s_problem, "motivation": s_motivation,
    "contribution": s_contribution, "method": s_method, "dataset-benchmark": s_dataset,
    "key-result": s_keyresult, "ablation-study": s_ablation,
    "headline-numbers": s_headline, "takeaway": s_takeaway,
}

order = sorted(AMAP.items(), key=lambda kv: kv[1]["index"])
for sid, meta in order:
    svg = BUILDERS[sid](sid)
    fn = f"{meta['index']:02d}_{sid}.svg"
    open(os.path.join(OUT, fn), "w").write(svg)
    print("wrote", fn)
print("done ->", OUT)
