#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 076
(TimeSiam: A Pre-Training Framework for Siamese Time-Series Modeling, ICML 2024).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card with a
<title> holding the cue keywords, so the strict --require-pptx-anchors cue pass resolves every
anchor from PPTX geometry. Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: paired time-series windows - a TEAL past subseries and a BLUE current subseries
whose masked span is a GOLD band, echoing 'reconstruct the current from the past'."""
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
def _tspts(x,y,w,h,phase,rough=0.0):
    pts=[]; n=64
    for i in range(n+1):
        t=i/n
        val=0.5+0.30*math.sin(t*math.pi*3.0+phase)+0.13*math.sin(t*math.pi*7.0+phase*1.7)
        val+=rough*0.10*math.sin(t*math.pi*19.0+phase*3.1)
        val=min(0.98,max(0.02,val))
        px=x+8+t*(w-16); py=y+h-8-val*(h-16)
        pts.append((px,py))
    return pts

def tsline(x,y,w,h,color,phase=0.0,mask=None,sw=2.6,bg=True,rough=0.0):
    """A time-series curve in a boxed axis. mask=(t0,t1) draws a gold masked span."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8) if bg else ""
    if mask:
        m0,m1=mask; bx=x+8+m0*(w-16); bw=(m1-m0)*(w-16)
        out+=rect(bx,y+6,bw,h-12,fill=GOLD,rx=4,opacity=0.20,sw=0)
        out+=line(bx,y+6,bx,y+h-6,GOLD,1.2,dash="3 3")
        out+=line(bx+bw,y+6,bx+bw,y+h-6,GOLD,1.2,dash="3 3")
    out+=poly(_tspts(x,y,w,h,phase,rough),stroke=color,sw=sw)
    return out

def siamese_arch(x,y,w,h):
    """Compact TimeSiam schematic: past window + masked current window ->
    two shared-weight encoders -> cross-attention decoder -> reconstructed current."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=10)
    winw=150; winh=54
    # inputs (left)
    px=x+22; pcy=y+40; ccy=y+120
    out+=tsline(px,pcy,winw,winh,TEAL,phase=0.2,bg=True)
    out+=T(px,pcy-8,"past subseries",11.5,TEAL,"700")
    out+=tsline(px,ccy,winw,winh,ACCENT,phase=2.1,mask=(0.55,0.85),bg=True)
    out+=T(px,ccy-8,"current subseries (masked)",11.5,ACCENT,"700")
    # encoders (shared weights)
    ex=px+winw+40; ew=92; eh=52
    e1y=pcy+1; e2y=ccy+1
    out+=rect(ex,e1y,ew,eh,fill=PANEL2,stroke=TEAL,rx=8,sw=1.5)+T(ex+ew/2,e1y+eh/2+5,"Encoder",13,TEXT,"800",anchor="middle")
    out+=rect(ex,e2y,ew,eh,fill=PANEL2,stroke=ACCENT,rx=8,sw=1.5)+T(ex+ew/2,e2y+eh/2+5,"Encoder",13,TEXT,"800",anchor="middle")
    out+=arrow(px+winw+4,pcy+winh/2,ex-4,e1y+eh/2,TEAL,2.0)
    out+=arrow(px+winw+4,ccy+winh/2,ex-4,e2y+eh/2,ACCENT,2.0)
    # shared-weight tie
    out+=line(ex+ew/2,e1y+eh,ex+ew/2,e2y,GOLD,1.6,dash="4 3")
    out+=T(ex+ew/2+6,(e1y+eh+e2y)/2+4,"shared weights",10.5,GOLD,"700")
    # decoder (cross-attention)
    dx=ex+ew+46; dw=118; dh=110; dyy=y+40
    out+=rect(dx,dyy,dw,dh,fill=PANEL2,stroke=GOLD,rx=8,sw=1.5)
    out+=T(dx+dw/2,dyy+38,"Decoder",13.5,TEXT,"800",anchor="middle")
    out+=T(dx+dw/2,dyy+58,"cross-attn",12,GOLD,"700",anchor="middle")
    out+=T(dx+dw/2,dyy+82,"+ lineage",11.5,SEC,"700",anchor="middle")
    out+=arrow(ex+ew+4,e1y+eh/2,dx-4,dyy+34,TEAL,2.0)
    out+=arrow(ex+ew+4,e2y+eh/2,dx-4,dyy+74,ACCENT,2.0)
    # output reconstructed current
    ox=dx+dw+40; oy=y+68
    out+=tsline(ox,oy,winw,winh,GREEN,phase=2.1,bg=True)
    out+=T(ox,oy-8,"reconstructed current",11.5,GREEN,"700")
    out+=arrow(dx+dw+4,dyy+dh/2,ox-4,oy+winh/2,GREEN,2.0)
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Tsinghua University  ·  Self-Supervised Time-Series Pre-Training",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"TimeSiam",42,WHITE,"800")
    b+=T(64,198,"A Pre-Training Framework for Siamese Time-Series Modeling",25,ACCENT,"800")
    # past vs current window motif near the title
    b+=tsline(946,116,266,52,TEAL,phase=0.2,bg=True); b+=T(946,110,"past",11,TER,"700")
    b+=tsline(946,182,266,52,ACCENT,phase=2.1,mask=(0.55,0.85),bg=True); b+=T(946,176,"current (masked)",11,TER,"700")
    b+=T(64,236,"Jiaxiang Dong · Haixu Wu · Yuxuan Wang · Yunzhong Qiu · Li Zhang · Jianmin Wang · Mingsheng Long",14.5,SEC,"500")
    # four concept cards in a row = anchors
    cw=276; gap=16; x0=64; cy=296; chh=236
    data=[
        (ch[0],ACCENT,x0,"Pre-training, borrowed recipes fall short",
         "Time series pre-training promises to cut labeling costs and boost downstream tasks, but recipes from vision and language fall short."),
        (ch[1],RED,x0+cw+gap,"Masking distorts temporal structure",
         "Random masking or series-wise similarity distorts or ignores the temporal correlations that make time series meaningful."),
        (ch[2],TEAL,x0+2*(cw+gap),"Reconstruct current from past",
         "TimeSiam samples a past and a current subseries and trains Siamese encoders to reconstruct the masked current from the past."),
        (ch[3],GREEN,x0+3*(cw+gap),"Lineage embeddings, new SOTA",
         "Learnable lineage embeddings span many time distances; across 13 benchmarks and 2 tasks it sets a new state of the art."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              tsline(x+22,cy+30,cw-44,44,col,phase=1.1,
                     mask=((0.55,0.85) if col in (RED,) else None))+
              para(x+24,cy+108,ti,17,TEXT,25,23,"800")[0])
        body+=para(x+24,cy+160,tx,12.8,SEC,35,18)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,562,1216,562,STROKE,1)
    b+=T(64,598,"arXiv:2402.02475",14,ACCENT,"700")
    b+=T(280,598,"github.com/thuml/TimeSiam",13.5,SEC,"600")
    b+=T(1216,598,"Learn temporal correlation the world's sensors already give away.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Vision-and-language recipes don't fit time series")
    # c1 left tall: borrowed tools, awkward fit
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"Borrowed tools, an awkward fit",18,TEXT,"800")+
        para(92,240,"Self-supervised pre-training transformed vision and language, so researchers reached for the same tools on time series. But the fit is awkward.",14.5,SEC,42,23)[0]+
        rect(92,360,344,138,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,388,"smooth signal vs shattered mask",12.5,TER,"700")+
        tsline(112,402,320,40,TEAL,phase=0.4)+
        tsline(112,452,320,40,RED,phase=0.4,mask=(0.30,0.42),rough=1.0))
    # right column, three stacked
    fx=500; fw=716
    # c2 masking shatters structure
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"Random masking shatters structure",16.5,RED,"800")+
        para(fx+28,226,"Masking points across a series can shatter the smooth temporal structure the signal depends on, making reconstruction so hard the model learns little.",14,SEC,58,21)[0]+
        T(fx+28,300,"masked-point recovery  ->  little signal learned",13.5,RED,"800",ff=MONO))
    # c3 contrastive ignores fine detail
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,132,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,324,6,132,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"Contrastive ignores fine-grained detail",16,GOLD,"800")+
        para(fx+28,392,"Comparing whole series for similarity ignores the fine-grained correlations inside them, and hinges on augmentations that are hard to design for temporal data.",14.5,TEXT,74,22)[0])
    # c4 the gap (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,472,fw,78,fill=PANEL,stroke=STROKE)+
        rect(fx,472,6,78,fill=TEAL,rx=6,sw=0)+
        T(fx+28,504,"The gap this paper addresses",16,TEAL,"800")+
        para(fx+28,532,"Existing recipes fail to emphasize the temporal correlations that make time series what they are.",14.5,SEC,80,20)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Unlabeled series, and a discarded prior")
    # c1 left top: flood of unlabeled series
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,192,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,192,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"A flood of unlabeled series",16.5,ACCENT,"800")+
        para(92,226,"Every day, sensors, wearables, and industrial systems pour out staggering volumes of unlabeled time series through the Internet of Things.",14,SEC,58,21)[0]+
        tsline(92,300,504,38,ACCENT,phase=0.9))
    # c2 left bottom: gold mine if unlabeled learning
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,560,184,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,366,6,184,fill=GOLD,rx=6,sw=0)+
        T(92,404,"A gold mine, if we skip labels",16,GOLD,"800")+
        para(92,434,"That data is a gold mine, but only if we can learn from it without hand labeling.",14,TEXT,58,21)[0]+
        eqbox(92,486,504,"value  =  unlabeled data  x  self-supervision",13.5))
    # c3 right top: the discarded prior
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,192,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(rx,158,6,192,fill=TEAL,rx=6,sw=0)+
        T(rx+28,196,"The prior prior methods throw away",16.5,TEAL,"800")+
        para(rx+28,226,"The key insight: time series carry a special information prior methods discard, the correlation between what happened in the past and what is happening now.",14,TEXT,56,21)[0]+
        T(rx+28,326,"past  ~~>  now :  correlation across time",13.5,TEAL,"800",ff=MONO))
    # c4 right bottom: relate distant moments
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,366,rw,184,fill=PANEL,stroke=STROKE)+
        rect(rx,366,6,184,fill=GREEN,rx=6,sw=0)+
        T(rx+28,404,"So relate distant moments directly",16,GREEN,"800")+
        para(rx+28,434,"Instead of treating each window in isolation, build a pre-training task that explicitly asks the model to relate distant moments in time to each other.",14,SEC,56,21)[0]+
        tsline(rx+28,494,rw-56,40,GREEN,phase=1.7,mask=(0.62,0.9)))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","One framework, three contributions")
    cards=[
        (ch[0],ACCENT,"TimeSiam framework","A simple but effective pre-training framework that uses Siamese networks to capture correlations among temporally distanced subseries."),
        (ch[1],TEAL,"Lineage embeddings","Learnable lineage embeddings: a lightweight mechanism that lets one model represent many different past-to-current time distances."),
        (ch[2],GREEN,"SOTA on both tasks","Extensive experiments show consistent state-of-the-art when fine-tuned on forecasting and classification, in-domain and cross-domain."),
        (ch[3],GOLD,"Backbone-agnostic","The framework drops cleanly onto modern encoders like iTransformer, PatchTST, and TCN."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    tags=["TS","L","*","+"]
    for i,(c,col,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+74,tags[i],24,col,"800",anchor="middle"))
        yy=cy+134
        tlines=wrap(ti,18)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"Pose pre-training as past-to-current reconstruction, span time distances, and stay backbone-agnostic.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Siamese subseries, reconstruct current from past")
    # c1 sample Siamese subseries (left top)
    lx=64; lw=560
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,168,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,168,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Sample two windows: Siamese subseries",16,ACCENT,"800")+
        para(lx+28,224,"From a single series, randomly sample a past and a current window, together the Siamese subseries; the current is lightly corrupted by masking.",13.5,SEC,60,20)[0]+
        tsline(lx+28,296,lw-56,30,ACCENT,phase=1.0,mask=(0.6,0.85)))
    # right c3 lineage embeddings
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,168,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rxx,158,6,168,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Lineage embeddings by distance",16,GOLD,"800")+
        para(rxx+28,224,"Past and current windows can be near or far apart, so TimeSiam adds learnable lineage embeddings indexed by that relative distance.",13.5,TEXT,60,20)[0]+
        eqbox(rxx+28,286,rw-56,"lineage(d):  one model, many temporal gaps d",12.5,h=30))
    # c2 shared encoders + cross-attention decoder (wide schematic bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,344,732,206,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,344,6,206,fill=TEAL,rx=6,sw=0)+
        T(92,378,"Shared encoders, cross-attention decoder",16,TEAL,"800")+
        siamese_arch(92,392,676,146))
    # c4 objective (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(820,344,396,206,fill=PANEL,stroke=STROKE)+
        rect(820,344,6,206,fill=GREEN,rx=6,sw=0)+
        T(848,378,"Objective",16.5,GREEN,"800")+
        para(848,408,"Simply the squared reconstruction error between the true and predicted current series.",13.5,SEC,40,20)[0]+
        eqbox(848,486,368,"L = || current - recon ||^2",14,h=42))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Thirteen benchmarks, plus two new corpora")
    # c1 breadth strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,96,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,96,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"A deliberately broad evaluation",16.5,TEXT,"800")+
        para(92,224,"The study spans thirteen benchmarks and two mainstream tasks: forecasting and classification.",14,SEC,110,20)[0]+
        stat(980,168,110,76,"13","benchmarks",ACCENT)+
        stat(1100,168,110,76,"2","tasks",TEAL))
    # c2 forecasting + classification sets
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,270,560,152,fill=PANEL,stroke=STROKE)+
        rect(64,270,6,152,fill=TEAL,rx=6,sw=0)+
        T(92,306,"Established benchmarks",16.5,TEAL,"800")+
        para(92,336,"Forecasting: four ETT subsets, Weather, Electricity, Traffic, Exchange. Classification: EEG (AD, TDBrain) and ECG (PTB).",13.5,SEC,56,20)[0]+
        chip(92,398,"forecasting  +  classification  =  11 established",TEAL,w=504,h=26))
    # c3 two new datasets
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,270,560,152,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,270,6,152,fill=GREEN,rx=6,sw=0)+
        T(684,306,"Two new multi-domain corpora",16.5,GREEN,"800")+
        para(684,336,"On top of the eleven established benchmarks, the authors construct two new large-scale, multi-domain datasets.",13.5,TEXT,58,20)[0]+
        chip(684,392,"TSLD-500M    and    TSLD-1G",GREEN,w=504,h=26))
    # c4 scale / cross-domain (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,438,1152,112,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,438,6,112,fill=GOLD,rx=6,sw=0)+
        T(92,474,"TSLD-1G: built for cross-domain stress tests",16,GOLD,"800")+
        para(92,504,"The larger corpus packs nearly fourteen million examples from diverse, non-overlapping domains, so pre-training and fine-tuning data can come from entirely different sources.",14,TEXT,86,22)[0]+
        stat(980,452,230,84,"~14M","examples, TSLD-1G",GOLD))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Consistent SOTA on forecasting and classification")
    # c1 headline strip: consistent and strong
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,116,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,116,fill=GREEN,rx=6,sw=0)+
        T(92,196,"The results are consistent and strong",16.5,GREEN,"800")+
        para(92,226,"State-of-the-art in both in-domain and cross-domain settings, on two mainstream tasks.",14,SEC,74,20)[0]+
        stat(720,172,236,88,"SOTA","in- & cross-domain",GREEN)+
        stat(970,172,246,88,"8 / 8","beats SSL baselines",TEAL))
    # c2 in-domain forecasting (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,290,560,258,fill=PANEL,stroke=STROKE)+
        rect(64,290,6,258,fill=ACCENT,rx=6,sw=0)+
        T(92,326,"In-domain forecasting: lower MSE",16,ACCENT,"800")+
        para(92,354,"TimeSiam cuts average mean squared error on strong backbones that already forecast well from scratch.",13.5,SEC,58,20)[0]+
        bar(300,432,240,5.7,7,GREEN,"PatchTST","-5.7%",h=26)+
        bar(300,470,240,2.5,7,TEAL,"iTransformer","-2.5%",h=26)+
        T(92,522,"average MSE reduction vs training from scratch",12.5,TER,"600"))
    # c3 classification + baselines (right top) / c4 cross-domain (right bottom)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,290,560,120,fill=PANEL,stroke=STROKE)+
        rect(656,290,6,120,fill=TEAL,rx=6,sw=0)+
        T(684,326,"In-domain classification: +11.5% acc",16,TEAL,"800")+
        para(684,356,"Average accuracy rises 11.5% over random initialization, beating eight strong self-supervised baselines.",13.5,SEC,58,20)[0]+
        T(684,398,"+11.5% over random init  ·  beats 8 SSL baselines",13,TEAL,"800",ff=MONO))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,426,560,122,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,426,6,122,fill=GOLD,rx=6,sw=0)+
        T(684,462,"Cross-domain can beat in-domain",16,GOLD,"800")+
        para(684,492,"The most striking finding: pre-training on the large, diverse TSLD-1G and fine-tuning elsewhere sometimes beats even in-domain pre-training.",13.5,TEXT,58,20)[0])
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Which design choices carry the weight")
    # c1 setup (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Controlled study on Traffic",16.5,ACCENT,"800")+
        para(92,226,"Careful ablations on the Traffic benchmark isolate which design choices actually matter for TimeSiam.",14,SEC,56,21)[0]+
        chip(92,268,"Traffic benchmark  ·  one factor at a time",ACCENT,w=468,h=28))
    # c2 past-recon beats self-recon (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,226,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,324,6,226,fill=GREEN,rx=6,sw=0)+
        T(92,362,"Past-to-current beats self-recon",16.5,GREEN,"800")+
        para(92,392,"Reconstructing the current window from a past one clearly beats plain self-reconstruction, validating the core Siamese idea.",14,TEXT,56,21)[0]+
        bar(320,472,220,9.0,10,GREEN,"past -> current","best",h=24)+
        bar(320,506,220,5.5,10,RED,"self-recon","worse",h=24))
    # c3 masking sweet spot (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,150,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,158,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Masking ratio sweet spot ~25%",16,GOLD,"800")+
        para(684,226,"Masking only 15% makes the task too easy to teach anything; masking 75% makes it too hard. Around 25% is best.",14,TEXT,56,21)[0]+
        T(684,296,"15% too easy   |   25% best   |   75% too hard",13,GOLD,"800",ff=MONO))
    # c4 lineage embeddings help (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(656,324,6,226,fill=TEAL,rx=6,sw=0)+
        T(684,362,"More lineage embeddings, more gain",16.5,TEAL,"800")+
        para(684,392,"Lineage embeddings deliver consistent gains over random initialization, and adding more keeps improving Electricity and Traffic up to a point.",14,SEC,56,21)[0]+
        bar(884,472,300,4.0,10,SEC,"random init","base",h=24)+
        bar(884,506,300,8.5,10,TEAL,"+ lineage embeds","better",h=24))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in one place")
    # c1 the numbers strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,166,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,202,"Error down, accuracy up, all vs from scratch",16.5,GREEN,"800")+
        stat(92,220,270,80,"-5.7%","forecast MSE, PatchTST",GREEN)+
        stat(382,220,270,80,"-2.5%","forecast MSE, iTransformer",TEAL)+
        stat(672,220,270,80,"+11.5%","in-domain accuracy",ACCENT)+
        rect(962,220,254,80,fill=PANEL2,stroke=STROKE,rx=12)+
        para(982,250,"All relative to training the backbone from scratch.",13,SEC,30,19)[0])
    # c2 breadth + baselines
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,332,560,218,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,332,6,218,fill=TEAL,rx=6,sw=0)+
        T(92,368,"Broad, and ahead of the field",16.5,TEAL,"800")+
        para(92,398,"Across thirteen benchmarks covering forecasting and classification, in both in-domain and cross-domain settings.",13.5,TEXT,56,20)[0]+
        stat(92,470,236,64,"13","benchmarks",TEAL)+
        stat(348,470,236,64,"8","SSL baselines beaten",GREEN))
    # c3 TSLD-1G
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,332,560,218,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,332,6,218,fill=GOLD,rx=6,sw=0)+
        T(684,368,"The corpus behind cross-domain",16.5,GOLD,"800")+
        para(684,398,"Backing the cross-domain story is TSLD-1G, a newly built pre-training dataset spanning multiple domains.",13.5,TEXT,58,20)[0]+
        stat(684,470,504,64,"~14M","examples across diverse domains",GOLD))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Reconstruct the past into the present")
    cards=[
        (ch[0],ACCENT,"A reframing of the task","The lasting takeaway is a reframing of how time series pre-training should be posed."),
        (ch[1],TEAL,"Past-to-current between Siamese subseries","Posing pre-training as past-to-current reconstruction between Siamese subseries, with learnable lineage embeddings, captures the correlations masking and contrastive methods leave on the table."),
        (ch[2],GREEN,"Simple, general, and state of the art","The payoff is a simple, general framework that drops onto modern backbones, scales with larger and more diverse data, and sets a new state of the art across tasks and domains."),
    ]
    y=176
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,116,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,116,fill=col,rx=6,sw=0)+
              circle(112,y+58,10,fill=col)+
              T(150,y+46,ti,19,TEXT,"800"))
        body+=para(150,y+78,tx,15.5,SEC,88,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=132
    b+=line(64,596,1216,596,STROKE,1)
    b+=tsline(64,612,150,40,TEAL,phase=0.2)
    b+=tsline(232,612,150,40,ACCENT,phase=2.1,mask=(0.55,0.85))
    b+=T(1216,636,"TimeSiam  ·  Siamese Time-Series Pre-Training  ·  ICML 2024",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
