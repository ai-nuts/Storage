#!/usr/bin/env python3
"""Native SVG deck builder for RetoMaton (ICML 2022) paper2video.
Each of the 38 narration chunks becomes its own <g id="cue_..."> card with a
<title> holding the cue keywords, so the strict --require-pptx-anchors cue pass
resolves 100% from PPTX geometry. All-native (no <image> except one code QR)."""
import json, os, base64, html

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CONTRACT = json.load(open(os.path.join(BUNDLE, "assets/meta/visual_anchor_contract.json")))
QR_B64 = open(os.path.join(HERE, "_qr_code_b64.txt")).read().strip()

W, H = 1280, 720
BG="#0d1526"; PANEL="#172038"; PANEL2="#1e2b4a"; STROKE="#2c3d63"
ACCENT="#4da3ff"; TEAL="#2dd4bf"; GOLD="#f5b642"; GREEN="#34d399"; RED="#f87171"
TEXT="#e9eef8"; MUTED="#9fb0cc"; INK="#0d1526"

# map slide id -> {index, chunks:[{anchor_id, keywords}]}
SL = {s["id"]: s for s in CONTRACT["slides"]}

def esc(s): return html.escape(str(s), quote=True)

def anchor(sid, ci):
    """Return (anchor_id, title_text) for slide id `sid` chunk index ci(1-based)."""
    ch = SL[sid]["chunks"][ci-1]
    kw = " ".join(ch.get("cue_keywords", ch.get("keywords", [])))
    return ch["anchor_id"], kw

def T(x,y,s,size=18,fill=TEXT,weight="normal",anchor_="start",family="Inter, Segoe UI, sans-serif",spacing=None,style=""):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor_}"{ls} style="{style}">{esc(s)}</text>')

def rect(x,y,w,h,fill=PANEL,rx=14,stroke=STROKE,sw=1.5,opacity=1.0):
    so = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}"{so} opacity="{opacity}"/>'

def line(x1,y1,x2,y2,stroke=STROKE,sw=2,dash=None,cap="round"):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d} stroke-linecap="{cap}"/>'

def circle(cx,cy,r,fill,stroke=None,sw=2):
    so=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"{so}/>'

def arrow(x1,y1,x2,y2,color=GOLD,sw=2.4,dash=None):
    import math
    ang=math.atan2(y2-y1,x2-x1); L=9
    a1=ang+math.radians(152); a2=ang-math.radians(152)
    hx1=x2+L*math.cos(a1); hy1=y2+L*math.sin(a1)
    hx2=x2+L*math.cos(a2); hy2=y2+L*math.sin(a2)
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return (line(x1,y1,x2,y2,color,sw,dash)+
            f'<polyline points="{hx1:.1f},{hy1:.1f} {x2:.1f},{y2:.1f} {hx2:.1f},{hy2:.1f}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')

def header(num, title, accent=ACCENT):
    o=[]
    # inset accent bar (NOT full-bleed: starts below top band, off L/R edges)
    o.append(rect(64,44,6,34,fill=accent,rx=3,stroke=None))
    o.append(T(88,60,f"{num:02d}",size=15,fill=accent,weight="700",spacing="2"))
    o.append(T(88,80,title,size=30,fill=TEXT,weight="700"))
    o.append(line(64,96,1216,96,stroke=STROKE,sw=1.2))
    return "".join(o)

def footer(right="RetoMaton · ICML 2022"):
    return T(1216,694,right,size=12,fill=MUTED,anchor_="end")

def card_open(anchor_id, kw):
    return f'<g id="{anchor_id}"><title>{esc(kw)}</title>'
def card_close(): return '</g>'

def svg_wrap(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="none"/>'
            + body + '</svg>')

def chip(x,y,w,h,label,color):
    return rect(x,y,w,h,fill="none",rx=9,stroke=color,sw=1.5)+T(x+14,y+h/2+5,label,size=14,fill=color,weight="600")

def datastore_row(x,y,w,k,v,ptr,kcol=TEAL,vcol=TEXT,pcol=GOLD,h=30):
    o=[rect(x,y,w,h,fill=PANEL2,rx=7,stroke=STROKE,sw=1)]
    o.append(rect(x+6,y+6,52,h-12,fill="none",rx=5,stroke=kcol,sw=1.3))
    o.append(T(x+32,y+h/2+5,k,size=13,fill=kcol,anchor_="middle",weight="600"))
    o.append(T(x+70,y+h/2+5,v,size=14,fill=vcol,weight="600"))
    o.append(T(x+w-14,y+h/2+5,ptr,size=13,fill=pcol,anchor_="end",weight="600"))
    return "".join(o)

def state_node(cx,cy,r,label,color=ACCENT,fill=PANEL):
    return circle(cx,cy,r,fill,stroke=color,sw=2.4)+T(cx,cy+5,label,size=15,fill=color,anchor_="middle",weight="700")

# ---------------------------------------------------------------- slides
def s_title():
    o=[]
    o.append(rect(64,40,6,62,fill=ACCENT,rx=3,stroke=None))
    o.append(T(88,62,"ICML 2022  ·  Neuro-Symbolic Language Modeling",size=15,fill=ACCENT,weight="600",spacing="1"))
    o.append(T(88,110,"RetoMaton: Automaton-Augmented",size=44,fill=TEXT,weight="800"))
    o.append(T(88,156,"Retrieval for Language Models",size=44,fill=TEXT,weight="800"))
    o.append(T(88,192,"Uri Alon · Frank F. Xu · Junxian He · S. Sengupta · Dan Roth · Graham Neubig",size=15,fill=MUTED))
    o.append(T(88,214,"Carnegie Mellon University  ·  Amazon AWS  ·  AWS AI Labs",size=14,fill=MUTED))
    qs=182
    o.append(rect(1216-qs-24,42,qs+24,qs+42,fill=PANEL,rx=12,stroke=STROKE,sw=1.4))
    o.append(f'<image x="{1216-qs-12}" y="54" width="{qs}" height="{qs}" xlink:href="data:image/png;base64,{QR_B64}"/>')
    o.append(T(1216-qs/2-12,54+qs+24,"Code · github.com/neulab/retomaton",size=11,fill=MUTED,anchor_="middle"))
    ax=64; ay=274; cw=(1152-3*18)/4; chh=342
    a1,k1=anchor("title",1); a2,k2=anchor("title",2); a3,k3=anchor("title",3); a4,k4=anchor("title",4)
    def frame(x,col,ttl,lines,tag):
        r=[rect(x,ay,cw,chh,fill=PANEL,rx=14,stroke=STROKE,sw=1.4),
           rect(x,ay,cw,5,fill=col,rx=2,stroke=None),
           circle(x+22,ay+36,7,col), T(x+40,ay+42,ttl,size=18,fill=TEXT,weight="700")]
        for j,ln in enumerate(lines): r.append(T(x+20,ay+76+j*23,ln,size=13.5,fill=MUTED))
        r.append(T(x+20,ay+chh-18,tag,size=12.5,fill=col,weight="600"))
        return r
    # card 1 retrieval LMs + datastore stack
    x=ax+0*(cw+18); o.append(card_open(a1,k1)); o.extend(frame(x,TEAL,"Retrieval LMs",
        ["Sharpen predictions by","pulling examples from a","huge external datastore","at test time."],"external datastore"))
    for i in range(3): o.append(datastore_row(x+20,ay+186+i*34,cw-40,"k","w"+str(i+1),"→",h=28))
    o.append(card_close())
    # card 2 automaton
    x=ax+1*(cw+18); o.append(card_open(a2,k2)); o.extend(frame(x,ACCENT,"RetoMaton",
        ["Builds a weighted finite","automaton on top of the","datastore, a retrieval","automaton."],"weighted finite automaton"))
    o.append(state_node(x+60,ay+250,24,"q1",TEAL)); o.append(state_node(x+cw/2+6,ay+218,24,"q2",ACCENT)); o.append(state_node(x+cw-60,ay+250,24,"q3",GOLD))
    o.append(arrow(x+82,ay+244,x+cw/2-14,ay+224,GOLD,2)); o.append(arrow(x+cw/2+28,ay+224,x+cw-82,ay+244,GOLD,2))
    o.append(card_close())
    # card 3 pointers + states
    x=ax+2*(cw+18); o.append(card_open(a3,k3)); o.extend(frame(x,GOLD,"Pointers + States",
        ["Saves pointers between","consecutive entries and","clusters entries into","automaton states."],"pointers · clusters"))
    for i in range(4):
        cx=x+38+i*58
        o.append(circle(cx,ay+218,10,TEAL if i==0 else PANEL2,stroke=TEAL,sw=1.5))
        if i<3: o.append(arrow(cx+11,ay+218,cx+47,ay+218,GOLD,2))
    o.append(f'<ellipse cx="{x+cw/2}" cy="{ay+272}" rx="70" ry="20" fill="none" stroke="{GOLD}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    o.append(T(x+cw/2,ay+277,"one state",size=12,fill=GOLD,anchor_="middle"))
    o.append(card_close())
    # card 4 result big number
    x=ax+3*(cw+18); o.append(card_open(a4,k4)); o.extend(frame(x,GREEN,"The Result",
        ["Up to 83% fewer","nearest-neighbor searches","with no perplexity loss, or","1.85 lower perplexity."],"83% fewer searches"))
    o.append(T(x+cw/2,ay+250,"83%",size=54,fill=GREEN,anchor_="middle",weight="800"))
    o.append(T(x+cw/2,ay+280,"fewer searches",size=13,fill=MUTED,anchor_="middle"))
    o.append(card_close())
    o.append(footer("arXiv:2201.12431"))
    return svg_wrap("".join(o))

def s_problem():
    o=[header(2,"The Problem: Search Dominates Inference",RED)]
    a1,k1=anchor("problem",1)
    o.append(card_open(a1,k1))
    o.append(rect(64,118,564,300,fill=PANEL,rx=14)); o.append(rect(64,118,6,300,fill=TEAL,rx=3,stroke=None))
    o.append(T(90,150,"Retrieval-based LM",size=20,fill=TEAL,weight="700"))
    o.append(T(90,180,"Fetches nearest-neighbor examples from an",size=15,fill=MUTED))
    o.append(T(90,202,"external datastore and blends them into the",size=15,fill=MUTED))
    o.append(T(90,224,"prediction. Better quality than a plain LM.",size=15,fill=MUTED))
    o.append(state_node(150,320,34,"LM",ACCENT))
    o.append(arrow(188,320,262,320,MUTED))
    o.append(rect(262,290,132,60,fill=PANEL2,rx=9,stroke=TEAL,sw=1.6))
    o.append(T(328,316,"Datastore",size=15,fill=TEAL,anchor_="middle",weight="600")); o.append(T(328,336,"search",size=12,fill=MUTED,anchor_="middle"))
    o.append(arrow(394,320,470,320,MUTED))
    o.append(rect(470,290,132,60,fill=PANEL2,rx=9,stroke=STROKE,sw=1.4))
    o.append(T(536,316,"blended",size=15,fill=TEXT,anchor_="middle",weight="600")); o.append(T(536,336,"prediction",size=12,fill=MUTED,anchor_="middle"))
    o.append(T(90,392,"Accuracy, domain-adaptability and provenance benefits.",size=13,fill=MUTED))
    o.append(card_close())
    a2,k2=anchor("problem",2)
    o.append(card_open(a2,k2))
    o.append(rect(652,118,564,300,fill=PANEL,rx=14)); o.append(rect(652,118,6,300,fill=RED,rx=3,stroke=None))
    o.append(T(678,150,"The catch is cost",size=20,fill=RED,weight="700"))
    o.append(T(678,180,"That datastore search can fire at every single",size=15,fill=MUTED))
    o.append(T(678,202,"time step, and it is far slower than the model's",size=15,fill=MUTED))
    o.append(T(678,224,"own forward pass.",size=15,fill=MUTED))
    o.append(T(678,266,"Relative cost per token",size=13,fill=MUTED))
    o.append(rect(678,280,96,26,fill=ACCENT,rx=6,stroke=None)); o.append(T(784,298,"LM forward pass",size=12,fill=TEXT))
    o.append(rect(678,316,510,26,fill=RED,rx=6,stroke=None)); o.append(T(1176,334,"kNN datastore search",size=12,fill=INK,anchor_="end",weight="600"))
    o.append(T(678,384,"Search runs as often as every time step.",size=13,fill=MUTED))
    o.append(card_close())
    a3,k3=anchor("problem",3)
    o.append(card_open(a3,k3))
    o.append(rect(64,436,1152,180,fill=PANEL2,rx=14,stroke=RED,sw=1.6))
    o.append(circle(128,526,26,"none",stroke=RED,sw=2.6)); o.append(T(128,536,"!",size=32,fill=RED,anchor_="middle",weight="800"))
    o.append(T(180,502,"Frequent search is the single most critical bottleneck",size=24,fill=TEXT,weight="800"))
    o.append(T(180,540,"It is the dominant computational cost at inference, and it keeps these otherwise powerful",size=15,fill=MUTED))
    o.append(T(180,564,"retrieval LMs out of practical, deployable settings despite their accuracy benefits.",size=15,fill=MUTED))
    o.append(card_close())
    o.append(footer())
    return svg_wrap("".join(o))

def s_motivation():
    o=[header(3,"Motivation: A Flat Datastore Throws Away Structure",GOLD)]
    a1,k1=anchor("motivation",1)
    o.append(card_open(a1,k1))
    o.append(rect(64,116,1152,86,fill=PANEL2,rx=14,stroke=GOLD,sw=1.5))
    o.append(T(90,148,"Key observation",size=16,fill=GOLD,weight="700"))
    o.append(T(90,178,"kNN-LM treats the datastore as a flat list and searches it token by token, ignoring that consecutive",size=16,fill=TEXT))
    o.append(T(90,198,"retrieved entries are highly correlated in time and that nearby keys behave alike.",size=16,fill=TEXT))
    o.append(card_close())
    a2,k2=anchor("motivation",2)
    o.append(card_open(a2,k2))
    o.append(rect(64,220,564,192,fill=PANEL,rx=14))
    o.append(T(90,252,"1 · Temporal correlation",size=17,fill=TEAL,weight="700"))
    o.append(T(90,280,"If a retrieved entry is useful now, the entry",size=14.5,fill=MUTED))
    o.append(T(90,301,"that follows it in the original text is very",size=14.5,fill=MUTED))
    o.append(T(90,322,"likely useful next.",size=14.5,fill=MUTED))
    for i in range(4):
        cx=120+i*130
        o.append(circle(cx,376,13,TEAL if i==0 else PANEL2,stroke=TEAL,sw=1.7))
        o.append(T(cx,381,"e"+str(i+1),size=12,fill=TEAL,anchor_="middle"))
        if i<3: o.append(arrow(cx+15,376,cx+115,376,GOLD,2.2))
    o.append(card_close())
    a3,k3=anchor("motivation",3)
    o.append(card_open(a3,k3))
    o.append(rect(652,220,564,192,fill=PANEL,rx=14))
    o.append(T(678,252,"2 · Key-vector locality",size=17,fill=ACCENT,weight="700"))
    o.append(T(678,280,"Entries whose key vectors are close tend to",size=14.5,fill=MUTED))
    o.append(T(678,301,"be followed by the same token, so they can",size=14.5,fill=MUTED))
    o.append(T(678,322,"share their outgoing pointers.",size=14.5,fill=MUTED))
    import math
    for i in range(6):
        cx=760+46*math.cos(i*1.1); cy=376+18*math.sin(i*1.9)
        o.append(circle(cx,cy,8,ACCENT if i<4 else PANEL2,stroke=ACCENT,sw=1.5))
    o.append(f'<ellipse cx="770" cy="374" rx="74" ry="26" fill="none" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    o.append(T(1010,381,"same next token",size=13,fill=ACCENT,weight="600"))
    o.append(card_close())
    a4,k4=anchor("motivation",4)
    o.append(card_open(a4,k4))
    o.append(rect(64,430,1152,186,fill=PANEL,rx=14,stroke=RED,sw=1.4))
    o.append(T(90,462,"Prior work · Adaptive Retrieval (AdaptRet)",size=18,fill=RED,weight="700"))
    o.append(T(90,494,"Trains an MLP to learn when to skip the search. But on a skip it backs off to the base LM alone,",size=15.5,fill=MUTED))
    o.append(T(90,517,"discarding the retrieval distribution exactly where it helps most, in domains where the base is weak.",size=15.5,fill=MUTED))
    o.append(state_node(150,576,24,"LM",ACCENT)); o.append(arrow(174,576,300,576,RED,2.4,dash="6 5"))
    o.append(T(240,566,"skip = lose retrieval",size=12,fill=RED,anchor_="middle"))
    o.append(rect(324,554,150,44,fill="none",rx=9,stroke=RED,sw=1.5)); o.append(T(399,581,"base LM only",size=14,fill=RED,anchor_="middle",weight="600"))
    o.append(T(520,582,"RetoMaton instead keeps the retrieval signal while still skipping the search.",size=14,fill=MUTED))
    o.append(card_close())
    o.append(footer())
    return svg_wrap("".join(o))

def s_contribution():
    o=[header(4,"Contribution: Two Changes Build the Automaton",ACCENT)]
    a1,k1=anchor("contribution",1)
    o.append(card_open(a1,k1))
    o.append(rect(64,116,564,190,fill=PANEL,rx=14)); o.append(rect(64,116,6,190,fill=GOLD,rx=3,stroke=None))
    o.append(T(96,148,"Change 1 · Pointers",size=19,fill=GOLD,weight="700"))
    o.append(T(96,178,"Save a pointer from every entry to the entry",size=15,fill=MUTED))
    o.append(T(96,200,"that came right after it in the text.",size=15,fill=MUTED))
    for i in range(4):
        x=110+i*118
        o.append(rect(x,240,66,34,fill=PANEL2,rx=6,stroke=STROKE,sw=1)); o.append(T(x+33,262,f"e{i+1}",size=14,fill=TEAL,anchor_="middle",weight="600"))
        if i<3: o.append(arrow(x+68,257,x+108,257,GOLD,2.4))
    o.append(card_close())
    a2,k2=anchor("contribution",2)
    o.append(card_open(a2,k2))
    o.append(rect(652,116,564,190,fill=PANEL,rx=14)); o.append(rect(652,116,6,190,fill=ACCENT,rx=3,stroke=None))
    o.append(T(684,148,"Change 2 · Clustering",size=19,fill=ACCENT,weight="700"))
    o.append(T(684,178,"Cluster entries with similar key vectors into",size=15,fill=MUTED))
    o.append(T(684,200,"states; states share their outgoing pointers.",size=15,fill=MUTED))
    for i in range(6):
        cx=730+(i%3)*16; cy=248+(i//3)*18
        o.append(circle(cx,cy,7,ACCENT,stroke=None))
    o.append(f'<ellipse cx="746" cy="257" rx="38" ry="26" fill="none" stroke="{ACCENT}" stroke-width="1.7"/>')
    o.append(T(806,262,"= one state  →  shared pointers",size=14.5,fill=MUTED))
    o.append(card_close())
    a3,k3=anchor("contribution",3)
    o.append(card_open(a3,k3))
    o.append(rect(64,324,764,292,fill=PANEL2,rx=14,stroke=ACCENT,sw=1.6))
    o.append(T(90,358,"Together → a weighted finite automaton",size=19,fill=ACCENT,weight="700"))
    o.append(state_node(200,470,38,"q1",TEAL)); o.append(state_node(430,430,38,"q2",ACCENT))
    o.append(state_node(430,540,32,"q3",GOLD)); o.append(state_node(680,470,38,"q4",GREEN))
    o.append(arrow(238,462,392,438,GOLD,2.6)); o.append(arrow(232,486,398,532,GOLD,2.6))
    o.append(arrow(468,436,642,462,GOLD,2.6)); o.append(arrow(462,534,648,482,GOLD,2.6))
    o.append(T(90,596,"States are clusters · edges are shared pointers · traversed in parallel with LM inference.",size=14,fill=MUTED))
    o.append(card_close())
    a4,k4=anchor("contribution",4)
    o.append(card_open(a4,k4))
    o.append(rect(852,324,364,292,fill=PANEL,rx=14,stroke=GREEN,sw=1.5))
    o.append(T(878,358,"Fully unsupervised",size=18,fill=GREEN,weight="700"))
    for j,ln in enumerate(["No extra training data","Built from the training","corpus, or a new domain","Model-agnostic","Approximates the next","nearest neighbors so most","searches are skipped"]):
        o.append(circle(886,394+j*30,4,GREEN)); o.append(T(900,399+j*30,ln,size=14,fill=MUTED))
    o.append(card_close())
    o.append(footer())
    return svg_wrap("".join(o))

def s_method():
    o=[header(5,"Method: Traverse the Automaton Alongside the LM",ACCENT)]
    a1,k1=anchor("method",1)
    o.append(card_open(a1,k1))
    o.append(rect(64,116,564,238,fill=PANEL,rx=14))
    o.append(T(90,148,"Entry = (key, value, pointer)",size=18,fill=TEAL,weight="700"))
    o.append(datastore_row(90,168,448,"kᵢ","value wᵢ","→ successor",h=34))
    o.append(datastore_row(90,210,448,"kⱼ","value wⱼ","→ successor",h=34))
    o.append(datastore_row(90,252,448,"kₗ","value wₗ","→ successor",h=34))
    o.append(T(90,318,"The pointer references the entry that followed it in the corpus.",size=13.5,fill=MUTED))
    o.append(card_close())
    a2,k2=anchor("method",2)
    o.append(card_open(a2,k2))
    o.append(rect(652,116,564,238,fill=PANEL,rx=14))
    o.append(T(678,148,"Keep a small set of active states",size=18,fill=ACCENT,weight="700"))
    o.append(T(678,176,"Close-key entries are clustered into a state; the",size=14.5,fill=MUTED))
    o.append(T(678,197,"state inherits all pointers of its members.",size=14.5,fill=MUTED))
    o.append(state_node(730,270,30,"S₁",ACCENT)); o.append(state_node(850,270,30,"S₂",TEAL)); o.append(state_node(970,270,30,"S₃",GOLD))
    o.append(arrow(760,270,820,270,GOLD,2)); o.append(arrow(880,270,940,270,GOLD,2))
    o.append(T(678,330,"Traversed in parallel with LM inference, visiting a set of states each step.",size=13.5,fill=MUTED))
    o.append(card_close())
    a3,k3=anchor("method",3)
    o.append(card_open(a3,k3))
    o.append(rect(64,372,564,244,fill=PANEL2,rx=14,stroke=GOLD,sw=1.5))
    o.append(T(90,404,"Move forward = follow pointers",size=18,fill=GOLD,weight="700"))
    o.append(T(90,434,"Follow the pointers of entries whose value",size=14.5,fill=MUTED))
    o.append(T(90,455,"matches the generated token. Essentially free.",size=14.5,fill=MUTED))
    o.append(state_node(150,520,30,"S",ACCENT)); o.append(arrow(180,520,360,520,GREEN,3))
    o.append(T(270,508,"free transition",size=13,fill=GREEN,anchor_="middle")); o.append(state_node(390,520,30,"S′",TEAL))
    o.append(T(90,586,"No search needed while valid transitions remain.",size=13.5,fill=MUTED))
    o.append(card_close())
    a4,k4=anchor("method",4)
    o.append(card_open(a4,k4))
    o.append(rect(652,372,564,244,fill=PANEL,rx=14,stroke=RED,sw=1.4))
    o.append(T(678,404,"Search only when transitions < τ",size=18,fill=RED,weight="700"))
    o.append(T(678,434,"A full kNN search is triggered, and restarts the",size=14.5,fill=MUTED))
    o.append(T(678,455,"traversal, only when valid onward transitions",size=14.5,fill=MUTED))
    o.append(T(678,476,"drop below threshold τ.",size=14.5,fill=MUTED))
    o.append(T(678,510,"Transition weights are dynamic (hidden-state",size=14,fill=MUTED))
    o.append(T(678,531,"distances), interpolated with the base LM by λ:",size=14,fill=MUTED))
    o.append(rect(678,548,510,34,fill=PANEL2,rx=8,stroke=STROKE,sw=1))
    o.append(T(688,570,"p = λ · p_auto(w | c,S) + (1−λ) · p_LM(w | c)",size=15,fill=TEXT,weight="600"))
    o.append(T(678,606,"τ trades accuracy (more searches) against speed (fewer).",size=13,fill=GOLD))
    o.append(card_close())
    o.append(footer())
    return svg_wrap("".join(o))

def s_dataset():
    o=[header(6,"Datasets: In-Domain and Domain Adaptation",TEAL)]
    a1,k1=anchor("dataset-benchmark",1)
    o.append(card_open(a1,k1))
    o.append(rect(64,116,1152,72,fill=PANEL2,rx=12,stroke=TEAL,sw=1.4))
    o.append(T(90,148,"Two settings",size=15,fill=TEAL,weight="700"))
    o.append(T(230,148,"in-domain language modeling, and cross-domain adaptation to a new law corpus.",size=16,fill=TEXT))
    o.append(card_close())
    a2,k2=anchor("dataset-benchmark",2)
    o.append(card_open(a2,k2))
    o.append(rect(64,204,564,244,fill=PANEL,rx=14)); o.append(rect(64,204,6,244,fill=ACCENT,rx=3,stroke=None))
    o.append(T(96,238,"In-domain · WikiText-103",size=19,fill=ACCENT,weight="700"))
    stats=[("103M","training tokens"),("247M","param base LM"),("103M","datastore entries"),("1M","clustered states")]
    for i,(v,l) in enumerate(stats):
        x=96+(i%2)*252; y=290+(i//2)*74
        o.append(T(x,y,v,size=30,fill=TEAL,weight="800")); o.append(T(x,y+22,l,size=13,fill=MUTED))
    o.append(T(96,438,"Wikipedia benchmark · 250K val/test tokens · avg cluster ≈ 100",size=12.5,fill=MUTED))
    o.append(card_close())
    a3,k3=anchor("dataset-benchmark",3)
    o.append(card_open(a3,k3))
    o.append(rect(652,204,564,244,fill=PANEL,rx=14)); o.append(rect(652,204,6,244,fill=GOLD,rx=3,stroke=None))
    o.append(T(684,238,"Domain adaptation · Law-MT",size=19,fill=GOLD,weight="700"))
    stats2=[("19M","tokens (English)"),("656M","param base LM"),("200K","clustered states"),("≈100","avg cluster size")]
    for i,(v,l) in enumerate(stats2):
        x=684+(i%2)*252; y=290+(i//2)*74
        o.append(T(x,y,v,size=30,fill=GOLD,weight="800")); o.append(T(x,y+22,l,size=13,fill=MUTED))
    o.append(T(684,438,"Law-domain corpus · automaton built for a brand-new domain",size=12.5,fill=MUTED))
    o.append(card_close())
    a4,k4=anchor("dataset-benchmark",4)
    o.append(card_open(a4,k4))
    o.append(rect(64,464,1152,152,fill=PANEL,rx=14,stroke=STROKE,sw=1.3))
    o.append(T(90,500,"Baselines compared throughout",size=17,fill=RED,weight="700"))
    o.append(rect(90,522,300,66,fill=PANEL2,rx=10,stroke=RED,sw=1.5))
    o.append(T(110,552,"kNN-LM",size=20,fill=RED,weight="700")); o.append(T(110,576,"the original retrieval LM",size=13,fill=MUTED))
    o.append(rect(410,522,300,66,fill=PANEL2,rx=10,stroke=RED,sw=1.5))
    o.append(T(430,552,"AdaptRet",size=20,fill=RED,weight="700")); o.append(T(430,576,"Adaptive Retrieval (MLP skip)",size=13,fill=MUTED))
    o.append(rect(730,522,486,66,fill=PANEL2,rx=10,stroke=GREEN,sw=1.5))
    o.append(T(750,552,"RetoMaton",size=20,fill=GREEN,weight="700")); o.append(T(750,576,"pointer + cluster automaton over the same datastore",size=13,fill=MUTED))
    o.append(card_close())
    o.append(footer())
    return svg_wrap("".join(o))

def _fosscurve(x,y,w,h,title,knn_pts,reto_pts,ymax,ymin,note,color_reto=GREEN):
    o=[rect(x,y,w,h,fill=PANEL,rx=14)]
    o.append(T(x+22,y+32,title,size=17,fill=TEXT,weight="700"))
    px,py=x+58,y+56; pw,ph=w-92,h-118
    def X(f): return px+f*pw
    def Y(v): return py+ph-((v-ymin)/(ymax-ymin))*ph
    o.append(line(px,py,px,py+ph,MUTED,1.2)); o.append(line(px,py+ph,px+pw,py+ph,MUTED,1.2))
    o.append(T(px-10,py+ph+4,f"{ymin:.0f}",size=10,fill=MUTED,anchor_="end")); o.append(T(px-10,py+8,f"{ymax:.0f}",size=10,fill=MUTED,anchor_="end"))
    o.append(T(px+pw/2,y+h-12,"Fraction of Saved Searches (FoSS) →",size=11.5,fill=MUTED,anchor_="middle"))
    o.append(f'<text x="{x+18}" y="{py+ph/2}" font-family="Inter" font-size="11" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 {x+18} {py+ph/2})">Perplexity</text>')
    for pts,col in [(knn_pts,RED),(reto_pts,color_reto)]:
        pl=" ".join(f"{X(f):.1f},{Y(v):.1f}" for f,v in pts)
        o.append(f'<polyline points="{pl}" fill="none" stroke="{col}" stroke-width="2.8" stroke-linejoin="round"/>')
        for f,v in pts: o.append(circle(X(f),Y(v),3.2,col))
    o.append(rect(x+w-152,y+44,14,4,fill=RED,rx=2,stroke=None)); o.append(T(x+w-134,y+49,"kNN-LM",size=11,fill=MUTED))
    o.append(rect(x+w-152,y+62,14,4,fill=color_reto,rx=2,stroke=None)); o.append(T(x+w-134,y+67,"RetoMaton",size=11,fill=MUTED))
    o.append(T(x+22,y+h-30,note,size=12,fill=color_reto,weight="600"))
    return "".join(o)

def s_keyresult():
    o=[header(7,"Key Result: Fewer Searches, Lower Perplexity",GREEN)]
    a1,k1=anchor("key-result",1)
    o.append(card_open(a1,k1))
    o.append(rect(64,116,1152,58,fill=PANEL2,rx=12,stroke=GREEN,sw=1.4))
    o.append(T(90,150,"Results are strong in both regimes, matching or beating kNN-LM at a fraction of the search cost.",size=17,fill=TEXT))
    o.append(card_close())
    a2,k2=anchor("key-result",2)
    o.append(card_open(a2,k2))
    o.append(_fosscurve(64,188,564,286,"WikiText-103",
        [(0,16.65),(0.4,17.1),(0.7,18.2),(0.9,20.5)],
        [(0,16.08),(0.4,16.2),(0.7,16.6),(0.81,16.65),(0.9,17.2)],
        21,16,"Matches kNN-LM while skipping 81% of searches"))
    o.append(card_close())
    a3,k3=anchor("key-result",3)
    o.append(card_open(a3,k3))
    o.append(_fosscurve(652,188,564,286,"Law-MT (domain adaptation)",
        [(0,12.34),(0.3,14.0),(0.6,18.5),(0.8,26.0)],
        [(0,10.49),(0.3,10.9),(0.6,11.8),(0.8,13.2)],
        27,10,"12.34 → 10.49 at FoSS=0; degrades only gently"))
    o.append(card_close())
    a4,k4=anchor("key-result",4)
    o.append(card_open(a4,k4))
    o.append(rect(64,490,1152,126,fill=PANEL,rx=14,stroke=GREEN,sw=1.5))
    o.append(T(90,522,"Overall: two ways to spend the automaton's advantage",size=17,fill=GREEN,weight="700"))
    o.append(T(150,584,"−1.85",size=34,fill=GREEN,weight="800")); o.append(T(270,572,"lower perplexity",size=15,fill=TEXT)); o.append(T(270,594,"when the search budget is kept",size=13,fill=MUTED))
    o.append(line(560,540,560,600,STROKE,1.4))
    o.append(T(640,584,"83%",size=34,fill=GREEN,weight="800")); o.append(T(730,572,"searches saved",size=15,fill=TEXT)); o.append(T(730,594,"with no loss in perplexity",size=13,fill=MUTED))
    o.append(line(978,540,978,600,STROKE,1.4))
    o.append(T(996,566,"WikiText 16.65 → 16.08",size=12.5,fill=MUTED)); o.append(T(996,592,"kNN-LM ppl rises sharply",size=12.5,fill=MUTED))
    o.append(card_close())
    o.append(footer())
    return svg_wrap("".join(o))

def s_ablation():
    o=[header(8,"Ablation: Pointers vs. Clustering",GOLD)]
    a1,k1=anchor("ablation-study",1)
    o.append(card_open(a1,k1))
    o.append(rect(64,116,1152,56,fill=PANEL2,rx=12,stroke=GOLD,sw=1.3))
    o.append(T(90,150,"The ablation teases apart the two ingredients that make RetoMaton work: pointers and clustering.",size=16,fill=TEXT))
    o.append(card_close())
    a2,k2=anchor("ablation-study",2)
    o.append(card_open(a2,k2))
    o.append(rect(64,186,564,208,fill=PANEL,rx=14)); o.append(rect(64,186,6,208,fill=GOLD,rx=3,stroke=None))
    o.append(T(96,220,"Pointers alone (no clustering)",size=17,fill=GOLD,weight="700"))
    o.append(T(96,248,"Already beats every baseline and matches",size=14.5,fill=MUTED))
    o.append(T(96,269,"kNN-LM. Pointers drive most of the gain.",size=14.5,fill=MUTED))
    o.append(T(96,326,"16.12",size=32,fill=GREEN,weight="800")); o.append(T(210,318,"perplexity",size=14,fill=TEXT)); o.append(T(210,338,"at FoSS = 0",size=12,fill=MUTED))
    o.append(T(96,378,">60%",size=28,fill=GREEN,weight="800")); o.append(T(210,378,"searches saved at matched perplexity",size=13,fill=MUTED))
    o.append(card_close())
    a3,k3=anchor("ablation-study",3)
    o.append(card_open(a3,k3))
    o.append(rect(652,186,564,208,fill=PANEL,rx=14)); o.append(rect(652,186,6,208,fill=ACCENT,rx=3,stroke=None))
    o.append(T(684,220,"Clustering helps at high saving",size=17,fill=ACCENT,weight="700"))
    o.append(T(684,248,"Contributes mainly from ≈70% saved searches",size=14.5,fill=MUTED))
    o.append(T(684,269,"onward, enabling longer search-free runs.",size=14.5,fill=MUTED))
    for i,(f,hh) in enumerate([("0.3",18),("0.5",34),("0.7",64),("0.9",92)]):
        x=700+i*96
        o.append(rect(x,380-hh,56,hh,fill=ACCENT,rx=5,stroke=None))
        o.append(T(x+28,394,f,size=12,fill=MUTED,anchor_="middle"))
    o.append(T(1130,306,"cluster",size=12,fill=ACCENT,anchor_="end")); o.append(T(1130,322,"benefit ↑",size=12,fill=ACCENT,anchor_="end"))
    o.append(card_close())
    a4,k4=anchor("ablation-study",4)
    o.append(card_open(a4,k4))
    o.append(rect(64,412,1152,204,fill=PANEL,rx=14,stroke=STROKE,sw=1.3))
    o.append(T(90,446,"Clustering granularity (WikiText-103)",size=17,fill=TEXT,weight="700"))
    for i,(k,verdict,col) in enumerate([("k = 100K","too coarse",RED),("k = 500K","good",GREEN),("k = 1M","good (similar to 500K)",GREEN)]):
        x=90+i*372
        o.append(rect(x,470,348,72,fill=PANEL2,rx=10,stroke=col,sw=1.5))
        o.append(T(x+20,510,k,size=22,fill=TEXT,weight="700")); o.append(T(x+20,534,verdict,size=14,fill=col,weight="600"))
    o.append(T(90,584,"The cheaper greedy merge wins at FoSS = 0 but degrades as FoSS grows.",size=14,fill=MUTED))
    o.append(T(1190,584,"98% of val tokens fall in n>1 automaton-continued n-grams",size=13,fill=GOLD,anchor_="end"))
    o.append(card_close())
    o.append(footer())
    return svg_wrap("".join(o))

def s_headline():
    o=[header(9,"Headline Numbers",GREEN)]
    a1,k1=anchor("headline-numbers",1)
    o.append(card_open(a1,k1))
    o.append(rect(64,116,1152,54,fill=PANEL2,rx=12,stroke=GREEN,sw=1.3))
    o.append(T(90,150,"Simple to remember: two ways to spend the automaton's savings, and a big domain-adaptation win.",size=16,fill=TEXT))
    o.append(card_close())
    a2,k2=anchor("headline-numbers",2)
    o.append(card_open(a2,k2))
    o.append(rect(64,186,564,196,fill=PANEL,rx=14,stroke=GREEN,sw=1.5))
    o.append(T(90,220,"Save compute",size=16,fill=GREEN,weight="700"))
    o.append(T(90,300,"83%",size=64,fill=GREEN,weight="800"))
    o.append(T(280,282,"fewer nearest-neighbor",size=16,fill=TEXT)); o.append(T(280,308,"searches, no perplexity loss",size=16,fill=TEXT))
    o.append(T(90,352,"or lower perplexity by up to 1.85 when the budget is kept.",size=13.5,fill=MUTED))
    o.append(card_close())
    a3,k3=anchor("headline-numbers",3)
    o.append(card_open(a3,k3))
    o.append(rect(652,186,564,196,fill=PANEL,rx=14,stroke=ACCENT,sw=1.5))
    o.append(T(678,220,"WikiText-103",size=16,fill=ACCENT,weight="700"))
    o.append(T(678,300,"81%",size=64,fill=ACCENT,weight="800"))
    o.append(T(868,282,"of searches skipped",size=16,fill=TEXT)); o.append(T(868,308,"while matching kNN-LM",size=16,fill=TEXT))
    o.append(T(678,352,"pointers-only already saves >60% at matched perplexity.",size=13.5,fill=MUTED))
    o.append(card_close())
    a4,k4=anchor("headline-numbers",4)
    o.append(card_open(a4,k4))
    o.append(rect(64,400,1152,216,fill=PANEL2,rx=14,stroke=GOLD,sw=1.5))
    o.append(T(90,436,"Fine-tuned Law-domain model",size=18,fill=GOLD,weight="700"))
    o.append(T(170,524,"8.61",size=52,fill=RED,weight="800")); o.append(T(170,552,"base LM perplexity",size=13,fill=MUTED))
    o.append(arrow(300,506,430,506,GREEN,3.4))
    o.append(T(470,524,"7.10",size=52,fill=GREEN,weight="800")); o.append(T(470,552,"+ RetoMaton",size=13,fill=MUTED))
    o.append(rect(650,486,330,52,fill="none",rx=10,stroke=GREEN,sw=1.8))
    o.append(T(815,519,"−17.5% relative perplexity",size=21,fill=GREEN,anchor_="middle",weight="700"))
    o.append(T(650,566,"The automaton compounds with fine-tuning, not just base models.",size=13.5,fill=MUTED))
    o.append(T(1030,470,"Reduces perplexity",size=13,fill=MUTED,anchor_="end")); o.append(T(1190,470,"by up to 1.85",size=13,fill=GOLD,anchor_="end",weight="600"))
    o.append(card_close())
    o.append(footer())
    return svg_wrap("".join(o))

def s_takeaway():
    o=[header(10,"Takeaway",ACCENT)]
    a1,k1=anchor("takeaway",1)
    o.append(card_open(a1,k1))
    o.append(rect(64,120,1152,124,fill=PANEL2,rx=16,stroke=ACCENT,sw=1.6))
    o.append(T(96,172,"A retrieval datastore has structure worth exploiting.",size=28,fill=TEXT,weight="800"))
    o.append(T(96,208,"Pointers link consecutive entries and clusters group similar ones, so the model carries retrieval",size=15.5,fill=MUTED))
    o.append(T(96,230,"forward in time instead of searching from scratch at every token.",size=15.5,fill=MUTED))
    o.append(card_close())
    a2,k2=anchor("takeaway",2)
    o.append(card_open(a2,k2))
    o.append(rect(64,264,564,232,fill=PANEL,rx=14))
    o.append(T(90,298,"The mechanism",size=17,fill=GOLD,weight="700"))
    o.append(state_node(150,380,30,"q",TEAL)); o.append(arrow(180,380,300,380,GOLD,2.6)); o.append(T(240,368,"pointer",size=12,fill=GOLD,anchor_="middle"))
    o.append(state_node(330,380,30,"q′",ACCENT)); o.append(arrow(360,380,480,380,GREEN,2.6)); o.append(T(420,368,"skip search",size=12,fill=GREEN,anchor_="middle"))
    o.append(state_node(510,380,30,"q″",GREEN))
    o.append(T(90,446,"Link consecutive entries · group similar ones into states.",size=14,fill=MUTED))
    o.append(T(90,470,"A full search fires only when transitions drop below τ.",size=14,fill=MUTED))
    o.append(card_close())
    a3,k3=anchor("takeaway",3)
    o.append(card_open(a3,k3))
    o.append(rect(652,264,564,232,fill=PANEL,rx=14))
    o.append(T(678,298,"Why it matters",size=17,fill=GREEN,weight="700"))
    for j,ln in enumerate(["Unsupervised, works with any base model","Transfers across domains",
                           "Unifies token, chunk and sequence retrieval","Cuts the dominant cost of retrieval LMs",
                           "Up to 83% fewer searches, or 1.85 lower ppl"]):
        o.append(circle(686,330+j*32,4,GREEN)); o.append(T(700,335+j*32,ln,size=14.5,fill=MUTED))
    o.append(card_close())
    o.append(rect(64,516,1152,72,fill=PANEL,rx=12,stroke=STROKE,sw=1.2))
    o.append(T(90,560,"RetoMaton · Alon, Xu, He, Sengupta, Roth, Neubig · ICML 2022",size=15,fill=MUTED))
    o.append(T(1190,560,"github.com/neulab/retomaton",size=14,fill=ACCENT,anchor_="end",weight="600"))
    o.append(footer(""))
    return svg_wrap("".join(o))
SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_keyresult",s_keyresult),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

def main():
    od=os.path.join(HERE,"svg_output"); os.makedirs(od,exist_ok=True)
    for name,fn in SLIDES:
        svg=fn()
        open(os.path.join(od,name+".svg"),"w").write(svg)
        print("wrote",name,len(svg),"bytes")

if __name__=="__main__":
    main()
