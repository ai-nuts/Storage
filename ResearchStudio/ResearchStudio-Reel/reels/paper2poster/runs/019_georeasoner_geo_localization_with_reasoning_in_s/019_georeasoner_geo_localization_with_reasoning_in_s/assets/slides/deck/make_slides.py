#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 019
(GeoReasoner: Geo-localization with Reasoning in Street Views using a Large VLM, ICML 2024).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card with a
<title> holding the cue keywords, so the strict --require-pptx-anchors cue pass resolves every
anchor from PPTX geometry. Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: street-view geo-localization - a stylized street-view frame with a GREEN location
pin (high-locatability) vs a RED blank frame (no clues), GOLD human game clues, and a
locatability gauge with a 0.4 threshold."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0B1B2B"; PANEL="#12293D"; PANEL2="#16324A"; STROKE="#26455F"
ACCENT="#4C9BE8"; TEAL="#34D3C0"; GOLD="#F2C14E"; RED="#F2685C"; GREEN="#48C78E"
TEXT="#EAF2FB"; SEC="#9DB3C8"; TER="#6E869C"; WHITE="#FFFFFF"
SANS="Arial, 'Helvetica Neue', Helvetica, sans-serif"
MONO="'DejaVu Sans Mono', Consolas, monospace"

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
            .replace('"',"&quot;"))

def T(x,y,s,size,fill=TEXT,weight="400",anchor="start",ff=SANS,ls=None,opacity=None):
    a=f' letter-spacing="{ls}"' if ls is not None else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<text x="{x}" y="{y}" font-family="{ff}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"{a}{o}>{esc(s)}</text>')

def rect(x,y,w,h,fill=PANEL,stroke=None,rx=14,sw=1.5,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}{o}/>'

def line(x1,y1,x2,y2,stroke=STROKE,sw=1.5,dash=None,cap="round"):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>'

def circle(cx,cy,r,fill=ACCENT,stroke=None,sw=1.5,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}{o}/>'

def poly(pts,fill="none",stroke=ACCENT,sw=2.5,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{d}/>'

def polygon(pts,fill=PANEL2,stroke=None,sw=1.0):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    p=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    return f'<polygon points="{p}" fill="{fill}"{st}/>'

def arrow(x1,y1,x2,y2,stroke=SEC,sw=2.2):
    ang=math.atan2(y2-y1,x2-x1); a=10
    xa=x2-a*math.cos(ang-0.45); ya=y2-a*math.sin(ang-0.45)
    xb=x2-a*math.cos(ang+0.45); yb=y2-a*math.sin(ang+0.45)
    return (line(x1,y1,x2,y2,stroke,sw)+
            f'<polyline points="{xa:.1f},{ya:.1f} {x2},{y2} {xb:.1f},{yb:.1f}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')

def wrap(text,maxc):
    words=text.split(); lines=[]; cur=""
    for w in words:
        if len(cur)+len(w)+1<=maxc: cur=(cur+" "+w).strip()
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines

def para(x,y,text,size,fill,maxc,lh,weight="400"):
    ls=wrap(text,maxc); out=[T(x,y+i*lh,l,size,fill,weight) for i,l in enumerate(ls)]
    return "".join(out), y+len(ls)*lh

def anchor(aid,kw,body):
    return f'<g id="{aid}"><title>{esc(" ".join(kw))}</title>{body}</g>'

def eyebrow(label):
    return (rect(64,52,5,26,fill=ACCENT,rx=2,sw=0)+
            T(82,72,label.upper(),15,SEC,"700",ls="2.5"))

def header(label,title,tsize=30):
    return eyebrow(label)+T(64,110,title,tsize,TEXT,"800")

def chunks(slide_id):
    return AM[slide_id]["chunks"]

def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" font-family="{SANS}">'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>'
            f'{body}</svg>')

def bar(x,y,w,val,vmax,color,label,valtxt,lblcolor=SEC,h=26):
    bw=max(2,int(w*val/vmax))
    return (rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=6,sw=1)+
            rect(x,y,bw,h,fill=color,rx=6,sw=0)+
            T(x-12,y+h*0.70+2,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.70+2,valtxt,14,color,"800"))

def stat(x,y,w,h,num,lbl,col):
    ns=min(32,h*0.34)
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,ns,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.80,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---- theme glyphs -------------------------------------------------------
def pin(cx,cy,r,color=GREEN):
    """Map location pin: filled circle head with a hole + downward point."""
    tri=polygon([(cx-r*0.60,cy+r*0.42),(cx+r*0.60,cy+r*0.42),(cx,cy+r*1.75)],fill=color)
    return tri+circle(cx,cy,r,fill=color)+circle(cx,cy,r*0.40,fill=BG)

def sv_frame(x,y,w,h,located=True):
    """Stylized street-view thumbnail. located=True -> buildings/road + green pin;
    located=False -> blank/tunnel frame with a red 'no clue' mark."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    if located:
        out+=rect(x+5,y+5,w-10,h*0.40,fill="#1C3A54",rx=4,sw=0)      # sky
        gy=y+h*0.44
        out+=rect(x+w*0.10,gy-h*0.10,w*0.20,h*0.50,fill="#24506E",rx=2,sw=0)  # building L
        out+=rect(x+w*0.34,gy-h*0.22,w*0.16,h*0.62,fill="#2C5C80",rx=2,sw=0)  # building tall
        out+=rect(x+w*0.72,gy-h*0.06,w*0.18,h*0.46,fill="#24506E",rx=2,sw=0)  # building R
        out+=polygon([(x+w*0.40,y+h-6),(x+w*0.60,y+h-6),(x+w*0.55,gy),(x+w*0.45,gy)],fill="#33597A")  # road
        out+=pin(x+w*0.62,y+h*0.34,7,GREEN)
    else:
        out+=rect(x+5,y+5,w-10,h-10,fill="#161E28",rx=4,sw=0)         # blank/tunnel
        cx,cy=x+w/2,y+h/2
        out+=line(cx-12,cy-12,cx+12,cy+12,RED,3.0)
        out+=line(cx-12,cy+12,cx+12,cy-12,RED,3.0)
    return out

def locgauge(x,y,w,val,color=GREEN,thr=0.4,h=22,lbl=None):
    """Locatability meter 0..1 with a dashed 0.4 threshold and a value fill."""
    bw=max(2,w*val)
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=6,sw=1)
    out+=rect(x,y,bw,h,fill=color,rx=6,sw=0)
    tx=x+w*thr
    out+=line(tx,y-6,tx,y+h+6,GOLD,1.6,dash="4 3")
    out+=T(tx,y-10,f"threshold {thr}",11,GOLD,"700",anchor="middle")
    if lbl: out+=T(x,y+h+16,lbl,12,SEC,"600")
    out+=T(x+w+8,y+h*0.70+2,f"{val:.2f}",13,color,"800")
    return out

def segbars(x,y,w,rowh=13,barh=9,n=4):
    """MaskFormer class-area ratio bars for a street view (compact)."""
    rows=[("building",0.72,ACCENT),("sky",0.55,TEAL),("road",0.40,SEC),
          ("vehicle",0.30,GOLD),("vegetation",0.18,GREEN)][:n]
    out=T(x,y-6,"MaskFormer class-area ratios",11.5,TER,"700")
    for i,(nm,v,c) in enumerate(rows):
        yy=y+i*rowh
        out+=T(x,yy+barh-1,nm,10.5,SEC,"600")
        bx=x+80; bw=(w-80)
        out+=rect(bx,yy,bw,barh,fill="#0E2334",stroke=STROKE,rx=3,sw=0.8)
        out+=rect(bx,yy,bw*v,barh,fill=c,rx=3,sw=0)
    return out

def two_stage_arch(x,y,w,h):
    """Qwen-VL backbone (Vision Encoder -> VL Adapter -> Pre-trained LLM) with two
    stacked LoRA fine-tuning stages: reasoning tuning (country) then location tuning (city)."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=10)
    # input street view
    ix=x+18; iy=y+30
    out+=sv_frame(ix,iy,86,58,located=True)
    out+=T(ix,iy-8,"street view",11,TER,"700")
    # three backbone modules
    mods=[("Vision\nEncoder",ACCENT),("VL\nAdapter",TEAL),("Pre-trained\nLLM",ACCENT)]
    mx=ix+86+30; mw=118; mh=58; gap=34; my=iy
    boxes=[]
    for i,(nm,col) in enumerate(mods):
        bx=mx+i*(mw+gap)
        boxes.append((bx,col))
        out+=rect(bx,my,mw,mh,fill=PANEL2,stroke=col,rx=8,sw=1.5)
        for j,ln in enumerate(nm.split("\n")):
            out+=T(bx+mw/2,my+mh/2-4+j*17,ln,12.5,TEXT,"800",anchor="middle")
    out+=arrow(ix+86+2,iy+29,mx-4,my+mh/2,SEC,2.0)
    for i in range(len(boxes)-1):
        out+=arrow(boxes[i][0]+mw+2,my+mh/2,boxes[i+1][0]-4,my+mh/2,SEC,2.0)
    # output: reasoning + city
    ox=boxes[-1][0]+mw+30
    out+=arrow(boxes[-1][0]+mw+2,my+mh/2,ox-4,my+mh/2,GREEN,2.0)
    out+=T(ox,my+mh/2+5,"reasoning + city",12.5,GREEN,"800")
    # two LoRA stages under the LLM (non-overlapping)
    ly=my+mh+18
    sw1=250
    out+=rect(mx,ly,sw1,44,fill="#2A2417",stroke=GOLD,rx=8,sw=1.2)
    out+=T(mx+14,ly+18,"Stage 1  LoRA: Reasoning tuning",11.5,GOLD,"800")
    out+=T(mx+14,ly+35,"3K game clue pairs  ->  country",10.5,SEC,"600")
    sx=mx+sw1+16
    out+=rect(sx,ly,sw1,44,fill="#0F2E2B",stroke=GREEN,rx=8,sw=1.2)
    out+=T(sx+14,ly+18,"Stage 2  LoRA: Location tuning",11.5,GREEN,"800")
    out+=T(sx+14,ly+35,"70K street views  ->  city",10.5,SEC,"600")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"HKUST (GZ) · Tongji · Info. Eng. University",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"GeoReasoner",42,WHITE,"800")
    b+=T(64,196,"Geo-localization with Reasoning in Street Views via a Large VLM",23,ACCENT,"800")
    # street-view motif near the title: located frame + reasoning to a pin
    b+=sv_frame(980,108,150,86,located=True); b+=T(980,104,"high-locatability",11,TER,"700")
    b+=arrow(1134,150,1176,150,GOLD,2.0); b+=pin(1196,150,10,GREEN)
    b+=T(64,232,"Ling Li · Yu Ye · Yao Zhou · Bingchuan Jiang · Wei Zeng",14.5,SEC,"500")
    # four concept cards in a row = anchors
    cw=276; gap=16; x0=64; cy=290; chh=246
    data=[
        (ch[0],ACCENT,x0,"Where the photo was taken - and how",
         "GeoReasoner not only predicts the country and city of a street photo, it explains the visual clues behind each guess."),
        (ch[1],RED,x0+cw+gap,"Two long-standing obstacles",
         "Street-view training data is full of low-quality images with no visual clues, and existing localization models are opaque black boxes."),
        (ch[2],GOLD,x0+2*(cw+gap),"Locatability + human game clues",
         "It quantifies how locatable each image is, borrows human inference knowledge from geo-games, and fine-tunes in two stages."),
        (ch[3],GREEN,x0+3*(cw+gap),"+25% country, +38% city",
         "Beats comparable vision-language models by over 25% at country and 38% at city level, matching a specialist trained on 15x more data."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              para(x+24,cy+50,ti,17,TEXT,25,23,"800")[0])
        body+=para(x+24,cy+128,tx,12.8,SEC,35,18)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,566,1216,566,STROKE,1)
    b+=T(64,600,"arXiv:2406.18572",14,ACCENT,"700")
    b+=T(280,600,"github.com/lingli1996/GeoReasoner",13.5,SEC,"600")
    b+=T(1216,600,"Interpretable geo-localization with a fraction of the data.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Bad training data, and models that can't explain")
    # c1 left tall: why it matters
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"Predicting where a photo was taken",18,TEXT,"800")+
        para(92,240,"Locating a street-view photo is useful for urban planning, navigation, and social studies. But today's approaches have two blind spots.",14.5,SEC,42,23)[0]+
        chip(92,360,"urban planning",ACCENT,w=176,h=30)+
        chip(280,360,"navigation",TEAL,w=156,h=30)+
        chip(92,402,"social studies",GREEN,w=176,h=30)+
        chip(280,402,"two blind spots",RED,w=156,h=30)+
        T(92,472,"useful, yet held back by data and opacity",12.8,TER,"700"))
    # right column, three stacked
    fx=500; fw=716
    # c2 the data problem: no visual clues
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,164,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,164,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"1. The data problem: no visual clues",16.5,RED,"800")+
        para(fx+28,226,"Street-view datasets are stuffed with images captured in tunnels, against blank walls, or of generic vegetation - none carrying clues a model could use to locate them.",14,SEC,58,21)[0]+
        sv_frame(fx+28,290,60,22,located=False)+
        T(fx+300,296,"tunnels · blank walls · vegetation  ->  no signal",12.5,RED,"800",ff=MONO))
    # c3 the reasoning problem: black boxes
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,338,fw,120,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,338,6,120,fill=GOLD,rx=6,sw=0)+
        T(fx+28,376,"2. The reasoning problem: black boxes",16,GOLD,"800")+
        para(fx+28,406,"Retrieval and classification models hand back a coordinate with no explanation a person could inspect or trust.",14.5,TEXT,74,22)[0])
    # c4 the argument (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,472,fw,78,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(fx,472,6,78,fill=TEAL,rx=6,sw=0)+
        T(fx+28,504,"Both must be fixed together",16,TEAL,"800")+
        para(fx+28,532,"This paper argues that data quality and interpretability cannot be solved in isolation.",14.5,SEC,80,20)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","LVLMs that reason, plus a wealth of game clues")
    # c1 left top: why now
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Why now, and why this approach?",16.5,ACCENT,"800")+
        para(92,226,"Two trends converge to make interpretable, knowledge-driven geo-localization newly feasible.",14,SEC,58,21)[0]+
        chip(92,266,"capable LVLMs  +  untapped human clues",ACCENT,w=468,h=30))
    # c2 left bottom: LVLMs fuse image+text and reason
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,226,fill=TEAL,rx=6,sw=0)+
        T(92,362,"LVLMs fuse image + text, and reason",16.5,TEAL,"800")+
        para(92,392,"Large vision-language models can jointly process images and text and follow step-by-step reasoning, and prior work shows a reasoning process makes language models stronger.",14,SEC,56,21)[0]+
        eqbox(92,486,504,"image + text + reasoning  ->  stronger model",13.5,h=40))
    # c3 right top: untapped resource - geo-games
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,192,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rx,158,6,192,fill=GOLD,rx=6,sw=0)+
        T(rx+28,196,"A huge untapped resource",16.5,GOLD,"800")+
        para(rx+28,226,"Communities behind geo-localization games have spent years assembling textual clues that pinpoint countries and cities from subtle visual details.",14,TEXT,56,21)[0]+
        chip(rx+28,306,"GeoGuessr  +  Tuxun  ->  human inference knowledge",GOLD,w=rw-56,h=30))
    # c4 right bottom: the insight
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,366,rw,184,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rx,366,6,184,fill=GREEN,rx=6,sw=0)+
        T(rx+28,404,"The insight: harvest and pair",16,GREEN,"800")+
        para(rx+28,434,"Harvest that human inference knowledge and pair it with high-quality street views, so the model learns not just to guess a location but to justify it.",14,TEXT,56,21)[0]+
        T(rx+28,528,"guess a location  ->  justify it",13.5,GREEN,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","One paradigm, three contributions")
    cards=[
        (ch[0],ACCENT,"Three contributions","GeoReasoner brings together a new paradigm, a new metric, and a new interpretable model for street-view geo-localization.","3"),
        (ch[1],GOLD,"New paradigm: LVLM + human clues","Leverages a large vision-language model together with external human reasoning knowledge learned from online games, enabling geo-localization with explanation.","P"),
        (ch[2],TEAL,"Locatability metric","Defines locatability - a metric for how findable an image's location is - and builds a CLIP-based network to compute it and curate clean data.","L"),
        (ch[3],GREEN,"GeoReasoner model","Delivers GeoReasoner itself: a model that beats existing geo-localization systems while offering detailed reasoning for every prediction.","G"),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    for i,(c,col,ti,tx,tag) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+74,tag,24,col,"800",anchor="middle"))
        yy=cy+134
        tlines=wrap(ti,18)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"Pair an LVLM with human reasoning knowledge, quantify locatability, and explain every prediction.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Curate locatable data, then fine-tune in two stages")
    # c1 left top: locatability metric via MaskFormer
    lx=64; lw=560
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,168,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,168,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,194,"Step 1: a locatability metric",16,ACCENT,"800")+
        para(lx+28,218,"MaskFormer segments each street view into semantic classes, producing a vector of class-area ratios.",13.5,SEC,64,19)[0]+
        segbars(lx+28,268,300,rowh=13,barh=9,n=4))
    # c2 right top: Sentence-BERT relevance weights
    rxx=656; rw=560
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(rxx,158,rw,168,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rxx,158,6,168,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,194,"Step 2: weight classes by relevance",16,GOLD,"800")+
        para(rxx+28,220,"Sentence-BERT measures how relevant each class is to the textual clues mined from geo-games, producing an importance weight vector w_loc.",13.5,TEXT,62,19)[0]+
        eqbox(rxx+28,286,rw-56,"Sentence-BERT( class, clues )  ->  w_loc",12.5,h=30))
    # c4 wide bottom schematic: Qwen-VL + two-stage LoRA
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,344,732,206,fill=PANEL,stroke=STROKE)+
        rect(64,344,6,206,fill=GREEN,rx=6,sw=0)+
        T(92,378,"The model: Qwen-VL + two LoRA stages",16,GREEN,"800")+
        two_stage_arch(92,388,676,158))
    # c3 right bottom: locatability equation + threshold
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(820,344,396,206,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(820,344,6,206,fill=TEAL,rx=6,sw=0)+
        T(848,378,"Locatability = weighted sum",16.5,TEAL,"800")+
        eqbox(848,398,368,"loc = sum_k  I_seg(k) * w_k^loc",13,h=38)+
        para(848,462,"Keep images scoring above 0.4; this filters 130K raw down to 70K.",13,SEC,44,19)[0]+
        locgauge(848,516,300,0.62,GREEN,thr=0.4,h=18))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Built from scratch: 130K street views + 3K clues")
    # c1 breadth strip: OSM + GSV sampling
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,96,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,96,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"Sampled from OpenStreetMap + Google Street View",16.5,TEXT,"800")+
        para(92,224,"Sample points every 4000 m across top global cities, collecting geo-tagged street views.",14,SEC,80,20)[0]+
        stat(980,168,110,76,"72","cities",ACCENT)+
        stat(1100,168,110,76,"48","countries",TEAL))
    # c2 locatability filter 130K -> 70K
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,270,560,152,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,270,6,152,fill=GREEN,rx=6,sw=0)+
        T(92,306,"Filter at locatability 0.4",16.5,GREEN,"800")+
        para(92,336,"Applying the locatability filter yields roughly 70K high-quality images.",13.5,TEXT,58,20)[0]+
        stat(92,368,236,40,"130K+","raw GSV images",SEC)+
        T(340,394,"->",22,GREEN,"800")+
        stat(380,368,236,40,"~70K","high-locatability",GREEN))
    # c3 two new datasets - 3K game clues
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,270,560,152,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,270,6,152,fill=GOLD,rx=6,sw=0)+
        T(684,306,"3K reasoned text-image clues",16.5,GOLD,"800")+
        para(684,336,"Scrape 3K+ textual clues from two geo-games, clean them with a BERT-based entity recognizer, and pair each with a street view.",13.5,TEXT,58,20)[0]+
        chip(684,392,"GeoGuessr  +  Tuxun  ·  BERT-NER cleaned",GOLD,w=504,h=26))
    # c4 evaluation (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,438,1152,112,fill=PANEL,stroke=STROKE)+
        rect(64,438,6,112,fill=TEAL,rx=6,sw=0)+
        T(92,474,"Evaluation: held-out set + open benchmarks",16,TEAL,"800")+
        para(92,504,"A held-out set of 1K images measures country/city accuracy; the open Im2GPS and Im2GPS3k Flickr benchmarks test generalization.",14,SEC,86,22)[0]+
        stat(980,452,230,84,"Im2GPS","+ Im2GPS3k",TEAL))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Beats VLMs by wide margins, rivals a 15x specialist")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,110,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,110,fill=GREEN,rx=6,sw=0)+
        T(92,196,"The headline result is decisive",16.5,GREEN,"800")+
        para(92,226,"State-of-the-art F1 at both country and city level, with a fraction of the training data.",14,SEC,74,20)[0]+
        stat(720,170,236,84,"0.90","country F1",GREEN)+
        stat(970,170,246,84,"0.86","city F1",TEAL))
    # c2 F1 vs Qwen-VL (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,284,560,264,fill=PANEL,stroke=STROKE)+
        rect(64,284,6,264,fill=ACCENT,rx=6,sw=0)+
        T(92,320,"F1: beats Qwen-VL by +25% / +39%",16,ACCENT,"800")+
        para(92,348,"Against the strongest comparable VLM, GeoReasoner lifts F1 at both levels.",13.5,SEC,60,20)[0]+
        bar(300,404,240,0.72,1.0,SEC,"Qwen-VL country","0.72",h=24)+
        bar(300,440,240,0.90,1.0,GREEN,"GeoReasoner ctry","0.90",h=24)+
        bar(300,480,240,0.53,1.0,SEC,"Qwen-VL city","0.53",h=24)+
        bar(300,516,240,0.86,1.0,TEAL,"GeoReasoner city","0.86",h=24))
    # c3 vs StreetCLIP (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,284,560,120,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,284,6,120,fill=GOLD,rx=6,sw=0)+
        T(684,320,"Edges out StreetCLIP - on 15x less data",16,GOLD,"800")+
        para(684,350,"Surpasses a geo-specialist trained on 1.1M street views.",13.5,TEXT,64,20)[0]+
        T(684,392,"70K images  vs  1.1M  ·  and still wins",13,GOLD,"800",ff=MONO))
    # c4 quality sweep (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,420,560,128,fill=PANEL,stroke=STROKE)+
        rect(656,420,6,128,fill=TEAL,rx=6,sw=0)+
        T(684,454,"More high-locatability data -> higher acc.",15.5,TEAL,"800")+
        para(684,482,"As the fraction of high-locatability images rises 0% -> 100%, accuracy climbs steadily: quality, not quantity, drives the gains.",13.5,SEC,62,19)[0]+
        T(684,540,"country 0.63->0.72   city 0.47->0.51",12.8,TEAL,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Two fine-tuning stages, each pulling its weight")
    # c1 setup + reasoning-only (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"From baseline, add reasoning tuning",16.5,ACCENT,"800")+
        para(92,226,"Starting at the Qwen-VL baseline (0.72 / 0.53 F1), reasoning tuning alone lifts both levels modestly to 0.82 / 0.58.",14,SEC,58,21)[0]+
        chip(92,268,"baseline 0.72/0.53  ->  +reasoning 0.82/0.58",ACCENT,w=468,h=28))
    # c2 location-only: the big jump (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,226,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,324,6,226,fill=GREEN,rx=6,sw=0)+
        T(92,362,"Location tuning: the big city-level jump",16,GREEN,"800")+
        para(92,392,"Adding location tuning alone produces a much larger jump, especially at the fine-grained city level - essential for pinpointing cities.",14,TEXT,56,21)[0]+
        bar(320,472,220,0.53,1.0,SEC,"baseline city","0.53",h=24)+
        bar(320,506,220,0.83,1.0,GREEN,"+location city","0.83",h=24))
    # c3 full model best (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,150,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,158,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Both stages stacked = strongest",16,GOLD,"800")+
        para(684,226,"The full two-stage model is best of all, reaching country F1 0.90 and city F1 0.86.",14,TEXT,58,21)[0]+
        T(684,296,"full model  ->  0.90 country · 0.86 city",13,GOLD,"800",ff=MONO))
    # c4 complementary: progression chart (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(656,324,6,226,fill=TEAL,rx=6,sw=0)+
        T(684,362,"The two stages are complementary",16.5,TEAL,"800")+
        para(684,390,"Location tuning supplies precision; reasoning tuning supplies explanations and a further lift.",13.5,SEC,60,19)[0]+
        bar(852,442,300,0.53,1.0,SEC,"baseline","0.53",h=20)+
        bar(852,472,300,0.58,1.0,ACCENT,"+reason","0.58",h=20)+
        bar(852,502,300,0.83,1.0,GREEN,"+location","0.83",h=20)+
        bar(852,532,300,0.86,1.0,TEAL,"full model","0.86",h=20))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in one place")
    # c1 the margins strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,166,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,202,"Margins over the best comparable VLM (Qwen-VL), in F1",16.5,GREEN,"800")+
        stat(92,220,300,80,"+25.02%","country-level F1",GREEN)+
        stat(412,220,300,80,"+38.61%","city-level F1",TEAL)+
        rect(732,220,484,80,fill=PANEL2,stroke=STROKE,rx=12)+
        para(752,250,"Full-model F1: 0.9033 country, 0.8585 city - a new state of the art.",13,SEC,52,19)[0])
    # c2 data efficiency
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,332,560,218,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,332,6,218,fill=TEAL,rx=6,sw=0)+
        T(92,368,"State of the art on far less data",16.5,TEAL,"800")+
        para(92,398,"Just 70K training images versus the 1.1M used by StreetCLIP, which GeoReasoner nonetheless surpasses.",13.5,TEXT,56,20)[0]+
        stat(92,470,236,64,"70K","GeoReasoner images",TEAL)+
        stat(348,470,236,64,"1.1M","StreetCLIP images",SEC))
    # c3 the underlying data
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,332,560,218,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,332,6,218,fill=GOLD,rx=6,sw=0)+
        T(684,368,"The data behind it",16.5,GOLD,"800")+
        para(684,398,"130K+ raw street views across 72 cities and 48 countries, filtered to 70K, plus 3K human-written reasoning clues.",13.5,TEXT,58,20)[0]+
        stat(684,470,160,64,"130K+","raw views",GOLD)+
        stat(858,470,160,64,"72 / 48","cities / ctys",ACCENT)+
        stat(1032,470,156,64,"3K","game clues",GREEN))
    # c4 Im2GPS efficiency footer
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,566,1152,54,fill=PANEL,stroke=STROKE,rx=10)+
        rect(64,566,6,54,fill=ACCENT,rx=6,sw=0)+
        T(92,599,"On open Im2GPS benchmarks, only 10K Flickr images rival models trained on millions.",14.5,TEXT,"700"))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","The right images and the right knowledge")
    cards=[
        (ch[0],GREEN,64,"You don't need millions of images",
         "You do not need millions of street-view images to build a state-of-the-art geo-localization model."),
        (ch[1],ACCENT,646,"The right images + the right knowledge",
         "What you need instead is the right images and the right reasoning knowledge to interpret them."),
        (ch[2],GOLD,64,"Locatability + geo-game reasoning",
         "By quantifying which street views are actually locatable and borrowing the reasoning strategies humans use to win geo-games, GeoReasoner matches or beats specialists - and explains every prediction."),
        (ch[3],TEAL,646,"Quality can stand in for scale",
         "A case study in how data quality and human inference knowledge substitute for brute-force scale, opening a path to interpretable, resource-efficient geo-localization."),
    ]
    cw=570
    ys=[176,176,340,340]
    hs=[148,148,210,210]
    for (c,col,x,ti,tx),y,hh in zip(cards,ys,hs):
        body=(rect(x,y,cw,hh,fill=PANEL,stroke=STROKE)+
              rect(x,y,6,hh,fill=col,rx=6,sw=0)+
              circle(x+40,y+40,10,fill=col)+
              T(x+64,y+46,ti,17.5,TEXT,"800"))
        body+=para(x+28,y+82,tx,14,SEC,60,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,576,1216,576,STROKE,1)
    b+=pin(84,600,10,GREEN)
    b+=T(104,606,"Interpretable, resource-efficient geo-localization",13.5,SEC,"600")
    b+=T(1216,606,"GeoReasoner · Geo-localization with Reasoning · ICML 2024",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
