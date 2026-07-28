#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 009.
Collective Certified Robustness against Graph Injection Attacks (ICML 2024, HK PolyU).
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

def poly(pts, stroke=TEAL, sw=3, fill="none", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def circ(cx, cy, r, fill, stroke=BG, sw=2):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

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
    s.append(T(86, 66, "ICML 2024  ·  THE HONG KONG POLYTECHNIC UNIVERSITY", size=16, fill=TEAL, weight="bold", spacing="2"))
    s.append(T(84, 150, "Collective Certified Robustness", size=54, fill=TEXT, weight="bold"))
    s.append(T(84, 210, "against Graph Injection Attacks", size=54, fill=TEXT, weight="bold"))
    s.append(T(84, 252, "Certify a whole target set at once — 0% becomes 80%+", size=22, fill=GOLD))
    s.append(T(84, 292, "Yuni Lai · Bailin Pan · Kaihuang Chen · Yancheng Yuan · Kai Zhou", size=18, fill=MUTED))
    labels = [
        ("THE VULNERABILITY", "GNNs power citation search and recommendation — yet a few injected malicious nodes can fool them."),
        ("THE PAPER", "The first collective certified robustness scheme against graph injection attacks."),
        ("THE IDEA", "Certify a whole set of target nodes jointly: cast the worst-case attacker as an integer program, relax it to a linear program that solves in about a minute."),
        ("THE PAYOFF", "On Citeseer the certified ratio jumps from zero percent to over eighty percent."),
    ]
    accents = [RED, BLUE, TEAL, GREEN]
    x0, y0, cw, gap = 64, 356, 278, 18
    for i, ch in enumerate(c):
        x = x0 + i * (cw + gap)
        b = [rect(x, y0, cw, 250, fill=CARD)]
        b.append(rect(x, y0, cw, 6, fill=accents[i], stroke=accents[i], sw=0, rx=3))
        b.append(T(x + 20, y0 + 44, labels[i][0], size=14, fill=accents[i], weight="bold", spacing="1"))
        p, _ = para(x + 20, y0 + 76, labels[i][1], size=16, fill=TEXT, width=cw - 40, lh=24)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    s.append(T(84, 648, "arxiv.org/abs/2403.01423   ·   github.com/Yuni-Lai/CollectiveLPCert", size=16, fill=MUTED))
    return svg_wrap("\n".join(s))

def s_problem(sid):
    c = chunks(sid); s = [header("PROBLEM", "Node-by-node certificates certify almost nothing", AMAP[sid]["index"])]
    # c1 top-left: injection attack diagram
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Graph injection attack", size=20, fill=TEXT, weight="bold"))
    b.append(T(x + 26, y + 66, "A handful of malicious nodes slip into the graph:", size=14, fill=MUTED))
    # clean cluster + injected red nodes
    cx, cy = x + 150, y + 168
    clean = [(cx, cy), (cx - 46, cy + 30), (cx + 44, cy + 34), (cx - 28, cy - 40), (cx + 34, cy - 32)]
    for i in range(len(clean)):
        for j in range(i + 1, len(clean)):
            if (i + j) % 2 == 0:
                b.append(line(*clean[i], *clean[j], stroke=STROKE, sw=1.5))
    for p in clean:
        b.append(circ(p[0], p[1], 13, BLUE))
    inj = [(x + 400, y + 120), (x + 452, y + 176)]
    for p in inj:
        b.append(line(p[0], p[1], cx + 44, cy + 34, stroke=RED, sw=2, dash="4 3"))
        b.append(line(p[0], p[1], cx, cy, stroke=RED, sw=2, dash="4 3"))
        b.append(circ(p[0], p[1], 14, RED))
    b.append(T(x + 426, y + 232, "injected malicious nodes", size=13, fill=RED, anchor="middle"))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: want certified robustness
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "We want certified robustness", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 80, "A mathematical guarantee that a model's predictions stay stable no matter how the attacker spends the budget.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(rect(x + 26, y + 182, cw - 52, 48, fill=CARD2, stroke=STROKE))
    b.append(T(x + 42, y + 212, "prediction( attacked graph )  =  prediction( clean )", size=15, fill=TEAL, ff=MONO, weight="bold"))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: sample-wise = node by node
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Every existing certificate is sample-wise", size=19, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 80, "For injection attacks, all prior certificates work node by node, certifying each target node in complete isolation.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(chip(x + 26, y + 196, 300, "one certificate  ·  one target node", GOLD))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: too pessimistic -> 0%
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=RED, stroke=RED, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Too pessimistic in practice", size=20, fill=TEXT, weight="bold"))
    b.append(T(x + cw / 2, y + 148, "0%", size=76, fill=RED, weight="bold", anchor="middle"))
    b.append(T(x + cw / 2, y + 196, "certified once the attacker gets", size=16, fill=MUTED, anchor="middle"))
    b.append(T(x + cw / 2, y + 220, "a modest injection budget", size=16, fill=MUTED, anchor="middle"))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_motivation(sid):
    c = chunks(sid); s = [header("MOTIVATION", "One graph must fool the whole target set", AMAP[sid]["index"])]
    pos = [(64, 122), (656, 122), (64, 400), (656, 400)]
    cw, chh = 560, 258
    accents = [TEAL, BLUE, GREEN, GOLD]
    heads = ["The key insight", "One shared perturbed graph", "So certify the set jointly", "Prior collective methods do not carry over"]
    bodies = [
        "In the real world an attacker cannot conjure a different graph for every node they want to fool.",
        "They inject a single perturbed graph, and that one graph has to disrupt the entire set of target nodes at the same time.",
        "If we certify the whole target set jointly instead of one node at a time, the guarantee becomes much stronger.",
        "Collective methods existed for edge-modification attacks, but they assume a fixed receptive field and do not carry over to injection, which expands the receptive field by adding new edges.",
    ]
    for i, ch in enumerate(c):
        x, y = pos[i]
        b = [rect(x, y, cw, chh, fill=CARD)]
        b.append(rect(x, y, 6, chh, fill=accents[i], stroke=accents[i], sw=0, rx=3))
        b.append(T(x + 26, y + 42, heads[i], size=20, fill=TEXT, weight="bold"))
        b.append(line(x + 26, y + 56, x + cw - 26, y + 56, stroke=STROKE, sw=1))
        p, _ = para(x + 26, y + 90, bodies[i], size=17, fill=MUTED, width=cw - 52, lh=26)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_contribution(sid):
    c = chunks(sid); s = [header("CONTRIBUTION", "The first collective certificate for injection", AMAP[sid]["index"])]
    tw, gap = 368, 24
    nums = ["1", "2", "3"]
    accents = [TEAL, BLUE, GREEN]
    heads = ["First collective scheme", "A customized linearization", "Almost model-agnostic"]
    bodies = [
        "The first collective certified robustness scheme for graph neural networks against graph injection attacks.",
        "Cast certification as a worst-case optimization: a binary integer quadratic constrained linear program, then relax that hard program into an ordinary linear program that solves efficiently.",
        "It works for any message-passing GNN and buys huge gains in certified performance at very little computational cost.",
    ]
    for i, ch in enumerate(c):
        x = 64 + i * (tw + gap); y = 140
        b = [rect(x, y, tw, 470, fill=CARD)]
        b.append(rect(x, y, tw, 8, fill=accents[i], stroke=accents[i], sw=0, rx=4))
        b.append(circ(x + 44, y + 62, 20, accents[i], stroke=CARD, sw=0))
        b.append(T(x + 44, y + 69, nums[i], size=22, fill="#08131F", weight="bold", anchor="middle"))
        hp, _ = para(x + 76, y + 56, heads[i], size=21, fill=TEXT, width=tw - 110, lh=27, weight="bold")
        b.append(hp)
        p, _ = para(x + 34, y + 148, bodies[i], size=18, fill=MUTED, width=tw - 68, lh=27)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_method(sid):
    c = chunks(sid); s = [header("METHOD", "Node-aware bi-smoothing, then a relaxed LP", AMAP[sid]["index"])]
    # c1 top-left: bi-smoothing + locality
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Node-aware bi-smoothing", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 76, "Randomized smoothing that randomly deletes edges and nodes to blur the attacker's influence. Locality: an injected node harms a target only if a message-passing path survives.", size=16, fill=MUTED, width=cw - 52, lh=24)
    b.append(p)
    # tiny path diagram: injected -> ... -> target, one dashed surviving path
    py = y + 214
    b.append(circ(x + 60, py, 12, RED)); b.append(T(x + 60, py + 30, "injected", size=12, fill=RED, anchor="middle"))
    b.append(circ(x + 190, py, 10, MUTED)); b.append(circ(x + 320, py, 10, MUTED))
    b.append(circ(x + 450, py, 12, TEAL)); b.append(T(x + 450, py + 30, "target", size=12, fill=TEAL, anchor="middle"))
    b.append(line(x + 72, py, x + 180, py, stroke=GOLD, sw=2, dash="4 3"))
    b.append(line(x + 200, py, x + 310, py, stroke=GOLD, sw=2, dash="4 3"))
    b.append(line(x + 330, py, x + 438, py, stroke=GOLD, sw=2, dash="4 3"))
    b.append(T(x + 255, py - 14, "surviving message path", size=12, fill=GOLD, anchor="middle"))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: worst-case attacker BIQP -> LP
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Worst-case attacker as a program", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 76, "Upper-bound the message-interference probability into a certifying condition, then model an attacker maximizing non-robust nodes under a budget on injected nodes and edges.", size=16, fill=MUTED, width=cw - 52, lh=24)
    b.append(p)
    b.append(rect(x + 26, y + 190, 250, 44, fill=CARD2, stroke=RED))
    b.append(T(x + 151, y + 217, "integer program (NP-hard)", size=14, fill=RED, anchor="middle", weight="bold"))
    b.append(T(x + 296, y + 218, "→", size=26, fill=GOLD, anchor="middle"))
    b.append(rect(x + 316, y + 190, 218, 44, fill=CARD2, stroke=GREEN))
    b.append(T(x + 425, y + 217, "linear program", size=14, fill=GREEN, anchor="middle", weight="bold"))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: Collective-LP-2 variable reduction
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Collective-LP-2: fewer variables", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 76, "The customized reformulation collapses a quadratic term into a single vector, cutting the extra variables and improving both quality and speed.", size=16, fill=MUTED, width=cw - 52, lh=24)
    b.append(p)
    b.append(rect(x + 26, y + 190, cw - 52, 48, fill=CARD2, stroke=STROKE))
    b.append(T(x + 42, y + 220, "extra variables:   O(rho^2)  →  O(rho)", size=18, fill=GOLD, ff=MONO, weight="bold"))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: sound lower bound
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GREEN, stroke=GREEN, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "A sound lower bound", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 80, "The linear program has a larger feasible region than the integer one, so its optimum is always a valid lower bound on the true certified ratio.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(chip(x + 26, y + 196, 300, "LP answer  <=  true certified ratio", GREEN))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_dataset(sid):
    c = chunks(sid); s = [header("DATASET / BENCHMARK", "Two citation graphs, two GNN backbones", AMAP[sid]["index"])]
    tw, gap = 368, 24
    accents = [TEAL, BLUE, GOLD]
    # c1: datasets + backbones
    x = 64; y = 140
    b = [rect(x, y, tw, 470, fill=CARD), rect(x, y, tw, 8, fill=TEAL, stroke=TEAL, sw=0, rx=4)]
    b.append(T(x + 30, y + 52, "Graphs & backbones", size=20, fill=TEXT, weight="bold"))
    b.append(chip(x + 30, y + 84, 150, "Cora-ML", BLUE))
    b.append(chip(x + 190, y + 84, 150, "Citeseer", BLUE))
    b.append(T(x + 30, y + 148, "two standard citation graphs,", size=16, fill=MUTED))
    b.append(T(x + 30, y + 172, "a few thousand nodes each", size=16, fill=MUTED))
    b.append(line(x + 30, y + 200, x + tw - 30, y + 200, stroke=STROKE, sw=1))
    b.append(chip(x + 30, y + 226, 120, "GCN", TEAL))
    b.append(chip(x + 162, y + 226, 120, "GAT", TEAL))
    b.append(T(x + 30, y + 290, "two representative message-", size=16, fill=MUTED))
    b.append(T(x + 30, y + 314, "passing backbones", size=16, fill=MUTED))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2: attacker budget sweep
    x = 64 + (tw + gap); y = 140
    b = [rect(x, y, tw, 470, fill=CARD), rect(x, y, tw, 8, fill=BLUE, stroke=BLUE, sw=0, rx=4)]
    b.append(T(x + 30, y + 52, "Attacker budget", size=20, fill=TEXT, weight="bold"))
    b.append(T(x + tw / 2, y + 150, "20 → 160", size=52, fill=BLUE, weight="bold", anchor="middle"))
    b.append(T(x + tw / 2, y + 190, "injected nodes swept", size=16, fill=MUTED, anchor="middle"))
    b.append(rect(x + 30, y + 236, tw - 60, 70, fill=CARD2, stroke=STROKE))
    b.append(T(x + tw / 2, y + 268, "per-node edge limit", size=15, fill=MUTED, anchor="middle"))
    b.append(T(x + tw / 2, y + 292, "= graph average degree", size=16, fill=GOLD, anchor="middle", weight="bold"))
    b.append(T(x + 30, y + 360, "Budget spans light to heavy", size=15, fill=MUTED))
    b.append(T(x + 30, y + 384, "injection attacks.", size=15, fill=MUTED))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3: estimation + solver
    x = 64 + 2 * (tw + gap); y = 140
    b = [rect(x, y, tw, 470, fill=CARD), rect(x, y, tw, 8, fill=GOLD, stroke=GOLD, sw=0, rx=4)]
    b.append(T(x + 30, y + 52, "Estimation & solver", size=20, fill=TEXT, weight="bold"))
    kpis = [("100,000", "Monte Carlo samples"), ("1%", "confidence level")]
    ky = y + 84
    for i, (v, l) in enumerate(kpis):
        py = ky + i * 96
        b.append(rect(x + 30, py, tw - 60, 82, fill=CARD2, stroke=STROKE))
        b.append(T(x + 48, py + 46, v, size=30, fill=GOLD, weight="bold"))
        b.append(T(x + 48, py + 68, l, size=14, fill=MUTED))
    b.append(line(x + 30, y + 292, x + tw - 30, y + 292, stroke=STROKE, sw=1))
    b.append(T(x + 30, y + 330, "Every linear program solved with", size=15, fill=MUTED))
    b.append(chip(x + 30, y + 352, 150, "MOSEK", GREEN))
    b.append(T(x + 190, y + 370, "via CVXPY", size=15, fill=MUTED))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_keyresult(sid):
    c = chunks(sid); s = [header("KEY RESULT", "Sample-wise collapses to zero; collective holds", AMAP[sid]["index"])]
    # c1 top-left: framing
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "A night-and-day improvement", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 84, "Under graph injection attacks, sample-wise certification is useless while the collective certificates stay strong.", size=18, fill=TEXT, width=cw - 52, lh=27)
    b.append(p)
    b.append(chip(x + 26, y + 196, 320, "collective  >>  sample-wise", TEAL))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: line chart certified vs injected nodes
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "Certified ratio vs injected nodes", size=19, fill=TEXT, weight="bold"))
    ox, oy, aw, ah = x + 74, y + 210, 420, 130
    b.append(line(ox, oy, ox + aw, oy, stroke=MUTED, sw=2))
    b.append(line(ox, oy, ox, oy - ah, stroke=MUTED, sw=2))
    b.append(T(ox - 10, oy - ah, "100%", size=12, fill=MUTED, anchor="end"))
    b.append(T(ox - 10, oy + 4, "0%", size=12, fill=MUTED, anchor="end"))
    b.append(T(ox + aw / 2, oy + 30, "injected nodes  20 → 160", size=13, fill=MUTED, anchor="middle"))
    xs = [0.0, 0.25, 0.5, 0.75, 1.0]
    coll = [0.92, 0.90, 0.86, 0.83, 0.79]
    samp = [0.30, 0.12, 0.03, 0.0, 0.0]
    pc = [(ox + xx * aw, oy - vv * ah) for xx, vv in zip(xs, coll)]
    ps = [(ox + xx * aw, oy - vv * ah) for xx, vv in zip(xs, samp)]
    b.append(poly(pc, stroke=GREEN, sw=3))
    b.append(poly(ps, stroke=RED, sw=3))
    for p in pc: b.append(circ(p[0], p[1], 4, GREEN, stroke=CARD, sw=1))
    for p in ps: b.append(circ(p[0], p[1], 4, RED, stroke=CARD, sw=1))
    b.append(T(ox + aw, pc[-1][1] - 8, "collective", size=13, fill=GREEN, anchor="end", weight="bold"))
    b.append(T(ox + aw, oy - 8, "sample-wise", size=13, fill=RED, anchor="end", weight="bold"))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: bars 0 / 73 / 81.2 on Citeseer 140
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GOLD, stroke=GOLD, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "Citeseer, 140 injected nodes", size=20, fill=TEXT, weight="bold"))
    bars = [("sample-wise", 0.0, RED), ("collective (standard)", 73.0, BLUE), ("collective (customized)", 81.2, GREEN)]
    base = y + 226; maxh = 120; scale = maxh / 100.0; bw = 120
    for i, (lab, val, col) in enumerate(bars):
        bxx = x + 70 + i * 165
        bh = max(val * scale, 2)
        b.append(rect(bxx, base - bh, bw, bh, fill=col, stroke=col, sw=0, rx=6))
        b.append(T(bxx + bw / 2, base - bh - 12, f"{val:.0f}%" if val == int(val) else f"{val:.1f}%", size=20, fill=col, weight="bold", anchor="middle"))
        p, _ = para(bxx + bw / 2 - 60, base + 22, lab, size=13, fill=TEXT, width=120, lh=16)
        # center the label
        for ln, yy in [(l2, base + 22 + k * 16) for k, l2 in enumerate(wrap(lab, 16))]:
            b.append(T(bxx + bw / 2, yy, ln, size=13, fill=TEXT, anchor="middle"))
    b.append(line(x + 60, base, x + cw - 30, base, stroke=STROKE, sw=1.5))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: customized dominates
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GREEN, stroke=GREEN, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Customized Collective-LP-2 dominates", size=19, fill=TEXT, weight="bold"))
    rows = [("matches or beats standard", "always", GREEN),
            ("relative gain in one setting", "+216%", GOLD),
            ("solves the largest budgets in", "~1 min", TEAL)]
    ry = y + 92
    for lab, tag, col in rows:
        b.append(circ(x + 38, ry - 5, 6, col, stroke=CARD, sw=0))
        b.append(T(x + 56, ry, lab, size=16, fill=TEXT))
        b.append(T(x + cw - 26, ry, tag, size=17, fill=col, anchor="end", weight="bold"))
        ry += 50
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_ablation(sid):
    c = chunks(sid); s = [header("ABLATION STUDY", "The relaxation costs little, and stays fast", AMAP[sid]["index"])]
    # c1 top-left: the question
    x, y, cw = 64, 122, 560
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=TEAL, stroke=TEAL, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "How much does relaxation cost?", size=20, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 84, "The linear relaxation trades exactness for tractability. So how much certified ratio do we actually give up?", size=18, fill=TEXT, width=cw - 52, lh=27)
    b.append(p)
    b.append(chip(x + 26, y + 196, 300, "relaxed LP  vs  exact integer", TEAL))
    s.append(group(c[0]["aid"], c[0]["kw"], "\n".join(b)))
    # c2 top-right: compare vs exact integer
    x, y = 656, 122
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=BLUE, stroke=BLUE, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "Benchmark: the exact integer program", size=19, fill=TEXT, weight="bold"))
    p, _ = para(x + 26, y + 82, "The exact binary integer program is only tractable for very small attack budgets, giving a reference upper bound to compare the relaxation against.", size=17, fill=MUTED, width=cw - 52, lh=25)
    b.append(p)
    b.append(chip(x + 26, y + 196, 320, "exact = ground-truth reference", BLUE))
    s.append(group(c[1]["aid"], c[1]["kw"], "\n".join(b)))
    # c3 bottom-left: gap small ~5%
    x, y = 64, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=GREEN, stroke=GREEN, sw=0, rx=3)]
    b.append(T(x + 26, y + 42, "The gap is small", size=20, fill=TEXT, weight="bold"))
    b.append(T(x + cw / 2, y + 150, "~5%", size=72, fill=GREEN, weight="bold", anchor="middle"))
    b.append(T(x + cw / 2, y + 196, "certified ratio lost vs the exact program", size=16, fill=MUTED, anchor="middle"))
    b.append(T(x + cw / 2, y + 222, "— also why collective can trail at tiny budgets", size=14, fill=MUTED, anchor="middle"))
    s.append(group(c[2]["aid"], c[2]["kw"], "\n".join(b)))
    # c4 bottom-right: runtime chart standard blows up
    x, y = 656, 400
    b = [rect(x, y, cw, 258, fill=CARD), rect(x, y, 6, 258, fill=RED, stroke=RED, sw=0, rx=3)]
    b.append(T(x + 26, y + 40, "Runtime: customized stays near a minute", size=18, fill=TEXT, weight="bold"))
    ox, oy, aw, ah = x + 70, y + 214, 430, 120
    b.append(line(ox, oy, ox + aw, oy, stroke=MUTED, sw=2))
    b.append(line(ox, oy, ox, oy - ah, stroke=MUTED, sw=2))
    b.append(T(ox - 10, oy - ah, "1000s", size=12, fill=MUTED, anchor="end"))
    b.append(T(ox - 10, oy + 4, "0", size=12, fill=MUTED, anchor="end"))
    b.append(T(ox + aw / 2, oy + 26, "attack budget →", size=13, fill=MUTED, anchor="middle"))
    xs = [0.0, 0.33, 0.66, 1.0]
    std = [0.08, 0.30, 0.66, 1.0]
    cus = [0.05, 0.06, 0.06, 0.07]
    pstd = [(ox + xx * aw, oy - vv * ah) for xx, vv in zip(xs, std)]
    pcus = [(ox + xx * aw, oy - vv * ah) for xx, vv in zip(xs, cus)]
    b.append(poly(pstd, stroke=RED, sw=3))
    b.append(poly(pcus, stroke=GREEN, sw=3))
    b.append(T(ox + aw, pstd[-1][1] + 4, "standard", size=13, fill=RED, anchor="end", weight="bold"))
    b.append(T(ox + aw, pcus[-1][1] - 8, "customized ~1 min", size=13, fill=GREEN, anchor="end", weight="bold"))
    s.append(group(c[3]["aid"], c[3]["kw"], "\n".join(b)))
    return svg_wrap("\n".join(s))

def s_headline(sid):
    c = chunks(sid); s = [header("HEADLINE NUMBERS", "The impact in four numbers", AMAP[sid]["index"])]
    # 4 KPI tiles across
    tiles = [
        ("0 → 81.2%", "certified ratio on Citeseer at 140 injected nodes — sample-wise vs customized collective", GREEN),
        ("~1 min", "the collective linear program solves even the largest attack budgets", TEAL),
        ("+216%", "relative improvement of the customized relaxation over the standard one", GOLD),
        ("~5%", "how far the relaxation sits below the exact but far slower integer solution", BLUE),
    ]
    tw, gap = 272, 20
    for i, ch in enumerate(c):
        x = 64 + i * (tw + gap); y = 150
        v, l, col = tiles[i]
        b = [rect(x, y, tw, 460, fill=CARD)]
        b.append(rect(x, y, tw, 8, fill=col, stroke=col, sw=0, rx=4))
        sz = 54 if len(v) > 6 else 66
        b.append(T(x + tw / 2, y + 190, v, size=sz, fill=col, weight="bold", anchor="middle"))
        p, _ = para(x + 26, y + 258, l, size=17, fill=TEXT, width=tw - 52, lh=25)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    s.append(T(64, 646, "Injecting five percent of the graph, the certified ratio climbs from zero to over eighty percent on both datasets.", size=15, fill=MUTED))
    return svg_wrap("\n".join(s))

def s_takeaway(sid):
    c = chunks(sid); s = [header("TAKEAWAY", "Certify the set, not one node at a time", AMAP[sid]["index"])]
    pos = [(64, 122), (656, 122), (64, 400), (656, 400)]
    cw, chh = 560, 258
    accents = [TEAL, GREEN, BLUE, GOLD]
    heads = ["The lesson", "Collective certification transforms the guarantee", "Kept tractable", "Practical, and composable"]
    bodies = [
        "Simple but powerful: how you frame the certification question changes everything.",
        "Certifying a whole set of nodes together, instead of one at a time, turns a near-useless zero percent guarantee into an eighty percent certified ratio against graph injection attacks.",
        "A customized linear relaxation keeps this efficient, solving in about a minute even for large attacks.",
        "A concrete step toward practical provable defenses. Because it shares the same smoothed model, it plugs in alongside existing sample-wise certificates to stay strong across every attack budget.",
    ]
    for i, ch in enumerate(c):
        x, y = pos[i]
        b = [rect(x, y, cw, chh, fill=CARD)]
        b.append(rect(x, y, 6, chh, fill=accents[i], stroke=accents[i], sw=0, rx=3))
        b.append(circ(x + 40, y + 44, 18, accents[i], stroke=CARD, sw=0))
        b.append(T(x + 40, y + 51, str(i + 1), size=20, fill="#08131F", weight="bold", anchor="middle"))
        hp, hy = para(x + 72, y + 40, heads[i], size=20, fill=TEXT, width=cw - 104, lh=26, weight="bold")
        b.append(hp)
        p, _ = para(x + 26, y + (108 if hy - y < 90 else 128), bodies[i], size=17, fill=MUTED, width=cw - 52, lh=25)
        b.append(p)
        s.append(group(ch["aid"], ch["kw"], "\n".join(b)))
    s.append(T(64, 690, "Collective Certified Robustness against Graph Injection Attacks  ·  ICML 2024  ·  arxiv.org/abs/2403.01423", size=14, fill=MUTED))
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
