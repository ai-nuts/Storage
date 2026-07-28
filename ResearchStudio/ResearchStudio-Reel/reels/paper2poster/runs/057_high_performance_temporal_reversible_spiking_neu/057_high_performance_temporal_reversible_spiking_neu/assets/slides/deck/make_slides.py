#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 057 (T-RevSNN, ICML 2024).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_...">
card with a <title> holding the cue keywords, so the strict --require-pptx-anchors
cue pass resolves every anchor from PPTX geometry. Zero <image>, zero gradients,
ASCII mono equations only. Adapted from run097 make_slides.py."""
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
            T(x-12,y+h*0.72,label,14,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.72,valtxt,14,color,"800"))

def kpi(x,y,num,lbl,col,w=168,h=100):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+56,num,30,col,"800",anchor="middle")+
            T(x+w/2,y+82,lbl,12.5,SEC,"600",anchor="middle"))

def ministat(x,y,num,lbl,col,w,h=66):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=10)+
            T(x+w/2,y+34,num,22,col,"800",anchor="middle")+
            T(x+w/2,y+55,lbl,11.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---------- SLIDE 1: TITLE (3 chunks) ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Peking University  ·  Institute of Automation, CAS",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,152,"High-Performance Temporal Reversible",39,WHITE,"800")
    b+=T(64,198,"Spiking Neural Networks",39,ACCENT,"800")
    b+=T(64,236,"O(L) Training Memory   ·   O(1) Inference Cost",22,TEAL,"800")
    b+=T(64,272,"Jiakui Hu, Man Yao, Xuerui Qiu, ... Guoqi Li   —   Peking University & Institute of Automation, CAS",15,SEC,"500")
    # three concept cards (1x3) = anchors
    cw=365; gap=28; x0=64; x1=x0+cw+gap; x2=x1+cw+gap; cy=316; chh=214
    data=[
        (ch[0],GOLD,x0,"The steep cost of spiking nets","Spiking networks promise low-power AI, but they are simulated over many timesteps: training memory grows with L times T, and inference repeats work at every step."),
        (ch[1],ACCENT,x1,"T-RevSNN","Turn off the temporal dynamics of most spiking neurons, and make the few remaining temporal connections reversible."),
        (ch[2],GREEN,x2,"The payoff","O(L) training memory and O(1) inference cost, state-of-the-art accuracy among CNN-based SNNs on ImageNet, up to 8.6x better memory."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              T(x+26,cy+48,ti,18.5,TEXT,"800"))
        body+=para(x+26,cy+82,tx,14,SEC,42,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,566,1216,566,STROKE,1)
    b+=T(64,602,"arXiv:2405.16466",14,ACCENT,"700")
    b+=T(300,602,"You do not need full temporal dynamics everywhere to build a capable spiking network.",14,SEC,"600")
    b+=T(64,648,"github.com/BICLab/T-RevSNN",13,TER,"600")
    return svg(b)

# ---------- SLIDE 2: PROBLEM (4 chunks) ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","A training-memory and inference-energy dilemma")
    # c1 what makes SNNs appealing but costly (left tall card)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"Appealing, but simulated over time",18,TEXT,"800")+
        para(92,240,"SNNs promise brain-inspired, low-power computation. But to work well they are unfolded over many timesteps, and that comes at a steep cost.",15,SEC,42,24)[0]+
        # mini unrolled-timesteps glyph
        rect(92,352,344,118,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,378,"one input, unrolled over T steps",12.5,TER,"600")+
        circle(126,424,10,fill=ACCENT)+circle(186,424,10,fill=ACCENT)+circle(246,424,10,fill=ACCENT)+circle(306,424,10,fill=ACCENT)+
        line(136,424,176,424,STROKE,2)+line(196,424,236,424,STROKE,2)+line(256,424,296,424,STROKE,2)+
        T(126,452,"t1",11,SEC,"600",anchor="middle")+T(186,452,"t2",11,SEC,"600",anchor="middle")+
        T(246,452,"t3",11,SEC,"600",anchor="middle")+T(306,452,"t4",11,SEC,"600",anchor="middle")+
        T(360,430,"...",16,SEC,"800")+
        T(92,510,"Cost grows with every timestep.",13.5,ACCENT,"700"))
    # right: three stacked pressures
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,120,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,120,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"Training: memory blows up",16.5,RED,"800")+
        para(fx+28,226,"Memory grows with both the number of layers and the number of timesteps.",14.5,SEC,58,22)[0]+
        eqbox(fx+430,196,258,"train mem ~ O(L * T)",14.5,h=40))
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,290,fw,96,fill=PANEL,stroke=STROKE)+
        rect(fx,290,6,96,fill=GOLD,rx=6,sw=0)+
        T(fx+28,328,"Inference: energy scales with T",16.5,GOLD,"800")+
        para(fx+28,356,"Repeating the input over T steps makes inference energy scale with T too.",14.5,SEC,50,22)[0]+
        eqbox(fx+470,318,218,"infer energy ~ O(T)",13.5,h=40))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,398,fw,152,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,398,6,152,fill=RED,rx=6,sw=0)+
        T(fx+28,438,"The dilemma",16,RED,"800")+
        para(fx+28,468,"Current training methods can relieve one of these pressures, but not the other at the same time, leaving SNNs stuck.",14.5,TEXT,74,22)[0]+
        T(fx+28,540,"save memory  XOR  save energy   =   pick one",15,RED,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 3: MOTIVATION (4 chunks) ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Most temporal gradients barely matter")
    # c1 key insight + gradient-magnitude glyph (left)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=TEAL,rx=6,sw=0)+
        T(92,198,"A surprisingly simple observation",18,TEAL,"800")+
        para(92,230,"Examining the gradients that flow backward through time, the authors find that for most neurons those temporal gradients barely matter.",14.5,SEC,50,22)[0]+
        T(92,332,"Temporal gradient magnitude per neuron",13,TER,"700")+
        _gradbars(112,348,486,150)+
        T(92,532,"Only a few positions carry real temporal signal.",13.5,TEAL,"700"))
    # right: three stacked
    rx=648; rw=568
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(rx,158,rw,116,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,116,fill=ACCENT,rx=6,sw=0)+
        T(rx+28,196,"So why pay the full temporal cost?",16,ACCENT,"800")+
        para(rx+28,226,"If only neurons at a few key positions carry important temporal information, most neurons need not pay for it at all.",14.5,SEC,60,22)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,286,rw,120,fill=PANEL,stroke=STROKE)+
        rect(rx,286,6,120,fill=GOLD,rx=6,sw=0)+
        T(rx+28,324,"Prior methods each solve half",16,GOLD,"800")+
        para(rx+28,352,"Decouple training from the timestep to save memory, or shrink inference steps to save energy, but not both.",14.5,SEC,60,22)[0]+
        T(rx+28,394,"memory  OR  energy  (never both)",13.5,GOLD,"800",ff=MONO))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,418,rw,132,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rx,418,6,132,fill=GREEN,rx=6,sw=0)+
        T(rx+28,456,"This paper's question",16,GREEN,"800")+
        para(rx+28,486,"Can both halves, training memory and inference energy, be solved together?",14.5,TEXT,58,22)[0]+
        T(rx+28,534,"memory  AND  energy  ->  together",14,GREEN,"800",ff=MONO))
    return svg(b)

def _gradbars(x,y,w,h):
    # many tiny bars, a few tall (the key positions)
    vals=[0.10,0.08,0.12,0.07,0.90,0.09,0.11,0.06,0.08,0.10,0.82,0.07,0.12,0.09,0.10,0.75,0.08,0.11]
    n=len(vals); bw=int((w-(n-1)*6)/n); box=rect(x-8,y-8,w+16,h+16,fill="#0E2334",stroke=STROKE,rx=8)
    bars=""
    for i,v in enumerate(vals):
        bh=max(3,int(v*(h-8))); bx=x+i*(bw+6); col=TEAL if v>0.5 else STROKE
        bars+=rect(bx,y+h-bh,bw,bh,fill=col,rx=2,sw=0)
    return box+bars+T(x,y+h+2,"neurons ->",11,TER,"600")

# ---------- SLIDE 4: CONTRIBUTION (4 chunks) ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","One architecture, both costs solved")
    cards=[
        (ch[0],ACCENT,"1","Turn off most temporal dynamics","Keep temporal dynamics on only at a few key positions, where the temporal connections are made reversible."),
        (ch[1],TEAL,"2","Reversible -> O(L) memory","Reversibility lets the network recompute activations in the backward pass instead of storing them, cutting training memory to order L."),
        (ch[2],GOLD,"3","Encode once -> O(1) inference","Encode the image only once and split features and network into independent sub-networks, so inference cost becomes constant."),
        (ch[3],GREEN,"4","ConvNeXt block + scaled residual","Redesign the basic SNN block in a ConvNeXt style and add a scaled residual so the sparse temporal design still trains well."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+76,num,28,col,"800",anchor="middle"))
        yy=cy+134
        tl=wrap(ti,19)
        for j,ln in enumerate(tl):
            body+=T(x+24,yy+j*24,ln,16.5,TEXT,"800")
        yy+=24*len(tl)+14
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,584,"Sparse temporal dynamics + reversibility  =  low memory and low inference cost at once.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD (4 chunks) ----------
def s_method():
    ch=chunks("method"); b=header("Method","Encode once, split by time, reverse the key links")
    # LEFT: encode-once split (c1) + sub-network sharing (c2)
    lx=64; lw=568
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,200,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,200,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Encode once, one group per step",16.5,ACCENT,"800")+
        para(lx+28,226,"Instead of feeding the same image at every timestep, T-RevSNN encodes it once and divides the features into T groups, one per step.",14,SEC,58,21)[0]+
        _encode_glyph(lx+28,300,lw-56,48))
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,374,lw,176,fill=PANEL,stroke=STROKE)+
        rect(lx,374,6,176,fill=TEAL,rx=6,sw=0)+
        T(lx+28,412,"Split into T sub-networks",16,TEAL,"800")+
        para(lx+28,442,"The network is split into T sub-networks that share parameters and exchange temporal information only at the key, turned-on neurons.",14,SEC,58,21)[0]+
        T(lx+28,528,"temporal info exchanged only at key neurons",13.5,TEAL,"800",ff=MONO))
    # RIGHT: reversible rule (c3) + memory collapse (c4)
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,200,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,200,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Multi-level temporal-reversible rule",16.5,GOLD,"800")+
        para(rxx+28,226,"The membrane potential at one timestep can be exactly reconstructed from the next timestep's state and the incoming spikes.",14,SEC,56,21)[0]+
        eqbox(rxx+28,314,rw-56,"u[t] = h( u[t+1], s[t] )   (exact)",15))
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,374,rw,176,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rxx,374,6,176,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,412,"Backward needs only the last step",16,GREEN,"800")+
        para(rxx+28,442,"A reversible forward pass means the backward pass stores no intermediate activations, only the final-step potentials.",14,SEC,56,21)[0]+
        eqbox(rxx+28,502,rw-56,"store u[T] only   ->   O(L*T) -> O(L)",14.5))
    return svg(b)

def _encode_glyph(x,y,w,h):
    # image -> encoder -> T feature groups
    g=rect(x,y,72,h,fill=PANEL2,stroke=STROKE,rx=8)+T(x+36,y+h/2+5,"image",12.5,TEXT,"700",anchor="middle")
    g+=T(x+92,y+h/2+6,"->",16,SEC,"800")
    g+=rect(x+118,y,86,h,fill=PANEL2,stroke=ACCENT,rx=8,sw=1.5)+T(x+161,y+h/2+5,"encode",12.5,ACCENT,"800",anchor="middle")
    g+=T(x+214,y+h/2+6,"->",16,SEC,"800")
    gx=x+244; gw=(w-(gx-x)-0)/4
    cols=[ACCENT,TEAL,GOLD,GREEN]
    for i in range(4):
        bx=gx+i*(gw)
        g+=rect(bx+2,y,gw-6,h,fill="#0E2334",stroke=cols[i],rx=6,sw=1.5)+T(bx+2+(gw-6)/2,y+h/2+5,"t%d"%(i+1),12.5,cols[i],"800",anchor="middle")
    return g

# ---------- SLIDE 6: DATASET (4 chunks) ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Static and neuromorphic vision, measured on real cost")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,58,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,58,fill=ACCENT,rx=6,sw=0)+
        T(92,193,"Static images: ImageNet-1K at 224 by 224 resolution, the main large-scale benchmark.",16,TEXT,"600"))
    # c2 event-based
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,240,6,150,fill=TEAL,rx=6,sw=0)+
        T(92,282,"Event-based / neuromorphic",19,TEAL,"800")+
        para(92,316,"Spiking, event-driven vision datasets that stress temporal processing directly.",14.5,SEC,58,22)[0]+
        chip(92,350,"CIFAR10-DVS   ·   DVS128 Gesture",TEAL,w=468,h=30))
    # c3 measure real cost
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,240,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,240,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,282,"Not just accuracy: real cost",17,GOLD,"800")+
        para(684,316,"Peak GPU memory per image and per-epoch time, on six A100 GPUs under mixed precision.",14.5,SEC,58,22)[0]+
        chip(684,350,"6x NVIDIA A100   ·   mixed precision",GOLD,w=468,h=30))
    # c4 baselines
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,410,1152,140,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,410,6,140,fill=GOLD,rx=6,sw=0)+
        T(92,448,"Compared against a broad set of baselines",17,GOLD,"800")+
        para(92,480,"Spiking ResNets and spiking Transformers, plus training-optimization methods, so the memory and speed gains are measured against strong prior work.",14.5,TEXT,110,23)[0]+
        T(92,536,"OTTT   ·   SLTT   ·   spatially-reversible S-RevSNN",14,GOLD,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT (4 chunks) ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","State-of-the-art accuracy at the lowest cost")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,150,1152,86,fill=PANEL,stroke=STROKE)+
        rect(64,150,6,86,fill=GREEN,rx=6,sw=0)+
        T(92,182,"ImageNet-1K  ·  ~30M params, T=4",15.5,GREEN,"800")+
        ministat(360,160,"73.2%","top-1 accuracy",GREEN,196)+
        ministat(572,160,"85.7 MB","memory / image",TEAL,196)+
        ministat(784,160,"2.8 mJ","inference energy",ACCENT,196)+
        T(998,182,"best-in-class",14,GOLD,"800")+T(998,206,"CNN-based SNN",12.5,SEC,"600"))
    # c2 best in class (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,252,560,226,fill=PANEL,stroke=STROKE)+
        rect(64,252,6,226,fill=TEAL,rx=6,sw=0)+
        T(92,290,"Best among convolutional spiking ResNets",15.5,TEAL,"800")+
        para(92,320,"Highest accuracy in its class, and it arrives with the lowest training memory, fastest training, and lowest inference energy.",14.5,SEC,58,22)[0]+
        chip(92,392,"lowest training memory",TEAL,w=504,h=26)+
        chip(92,424,"fastest training time",TEAL,w=504,h=26)+
        chip(92,456,"lowest inference energy",TEAL,w=504,h=26,))
    # c3 vs spiking transformer (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,252,560,226,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,252,6,226,fill=GOLD,rx=6,sw=0)+
        T(684,290,"vs a leading spiking Transformer",15.5,GOLD,"800")+
        T(684,314,"at similar accuracy",13,SEC,"600")+
        kpi(684,330,"8.6x","less memory",GOLD,w=166,h=104)+
        kpi(866,330,"2.0x","faster training",GOLD,w=166,h=104)+
        kpi(1048,330,"1.6x","less energy",GOLD,w=166,h=104))
    # c4 lighter version strip
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,492,1152,116,fill=PANEL,stroke=STROKE)+
        rect(64,492,6,116,fill=ACCENT,rx=6,sw=0)+
        T(92,526,"A lighter model",16,ACCENT,"800")+
        para(92,556,"A 15 million parameter version still reaches nearly 70 percent top-1 accuracy, at under 60 megabytes of memory per image.",14.5,SEC,74,22)[0]+
        kpi(940,506,"~70%","15M params",ACCENT,w=126,h=88)+
        kpi(1082,506,"<60 MB","per image",TEAL,w=126,h=88))
    b+=T(64,648,"Best accuracy, lowest memory, fastest training, lowest energy: all at the same time.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 8: ABLATION (4 chunks) ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Each design choice earns its place")
    # c1 temporal reversibility on MS-ResNet-34 (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,262,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,262,fill=TEAL,rx=6,sw=0)+
        T(92,196,"Temporal reversibility alone",16.5,TEAL,"800")+
        para(92,224,"Adding temporal reversibility to a standard MS-ResNet-34, at a cost of only about 1.5 accuracy points:",14,SEC,58,21)[0]+
        T(112,286,"Training memory per image  ·  lower is better",13,TER,"700")+
        bar(300,300,236,267,267,RED,"baseline","267 MB",h=24)+
        bar(300,332,236,88,267,TEAL,"+ reversible","88 MB",h=24)+
        T(92,392,"Epoch time:",14,TER,"700")+
        T(200,392,"11.2 min  ->  7.4 min",15,TEAL,"800",ff=MONO)+
        T(430,392,"(-1.5 acc pts)",13,SEC,"600"))
    # c2 multi-level fusion (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,436,560,114,fill=PANEL,stroke=STROKE)+
        rect(64,436,6,114,fill=ACCENT,rx=6,sw=0)+
        T(92,472,"Multi-level temporal fusion",16,ACCENT,"800")+
        para(92,500,"Fusing temporal information between stages is worth roughly 1.2 accuracy points on its own.",14,SEC,56,21)[0]+
        T(544,486,"+1.2",26,ACCENT,"800",anchor="end")+T(544,508,"pts",12,SEC,"600",anchor="end"))
    # c3 scaled residual + timesteps (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,192,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,192,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Scaled residual speeds convergence",15.5,GOLD,"800")+
        para(684,226,"Varying the number of timesteps trades accuracy against cost; the scaled residual reaches 60% accuracy in fewer epochs.",14,SEC,58,21)[0]+
        T(684,288,"epochs to reach 60% accuracy  ·  fewer is better",12.5,TER,"700")+
        bar(830,300,300,32,32,RED,"no scale","32 ep",h=20)+
        bar(830,326,300,25,32,GOLD,"scaled res","25 ep",h=20))
    # c4 orthogonality (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,366,560,184,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,366,6,184,fill=GREEN,rx=6,sw=0)+
        T(684,404,"Temporal and spatial are orthogonal",15.5,GREEN,"800")+
        para(684,434,"Temporal and spatial reversibility are independent and can be stacked together for even greater savings.",14,TEXT,56,21)[0]+
        chip(684,500,"temporal + spatial reversibility  ->  stackable",GREEN,w=504,h=34))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS (3 chunks) ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The results in one place")
    # c1 the three multipliers (top wide)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,168,1152,182,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,168,6,182,fill=GOLD,rx=6,sw=0)+
        T(92,208,"vs a leading spiking Transformer, at comparable accuracy",17,GOLD,"800")+
        kpi(120,232,"8.6x","better memory efficiency",GOLD,w=336,h=98)+
        kpi(472,232,"2.0x","faster training",GOLD,w=336,h=98)+
        kpi(824,232,"1.6x","lower inference energy",GOLD,w=336,h=98))
    # c2 imagenet numbers (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,560,184,fill=PANEL,stroke=STROKE)+
        rect(64,366,6,184,fill=GREEN,rx=6,sw=0)+
        T(92,404,"ImageNet-1K",16.5,GREEN,"800")+
        kpi(92,424,"73.2%","top-1 accuracy",GREEN,w=164,h=104)+
        kpi(272,424,"85.7 MB","memory / image",TEAL,w=164,h=104)+
        kpi(452,424,"2.8 mJ","per inference",ACCENT,w=156,h=104))
    # c3 complexity (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,366,560,184,fill=PANEL,stroke=STROKE)+
        rect(656,366,6,184,fill=ACCENT,rx=6,sw=0)+
        T(684,404,"And the complexity that makes it possible",15.5,ACCENT,"800")+
        eqbox(684,432,504,"training memory   =   O(L)",16,h=48)+
        eqbox(684,492,504,"inference cost   =   O(1)",16,h=48))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY (3 chunks) ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","You don't need full temporal dynamics everywhere")
    cards=[
        (ch[0],ACCENT,"Drop the assumption","You do not need full temporal dynamics at every neuron to build a capable spiking network."),
        (ch[1],TEAL,"Switch off most, reverse a few","Because most temporal gradients are unimportant, turning off most temporal dynamics and making the few remaining connections reversible gives O(L) memory and O(1) inference, with almost no accuracy loss."),
        (ch[2],GREEN,"A path to practical brain-inspired AI","By removing the memory and training-time bottleneck, T-RevSNN opens a path toward larger, more practical, more energy-efficient spiking models."),
    ]
    y=176
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,116,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,116,fill=col,rx=6,sw=0)+
              circle(112,y+58,10,fill=col)+
              T(150,y+46,ti,19,TEXT,"800"))
        body+=para(150,y+78,tx,15,SEC,92,24)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=132
    b+=line(64,596,1216,596,STROKE,1)
    b+=T(64,632,"High-Performance Temporal Reversible Spiking Neural Networks",15.5,TEXT,"700")
    b+=T(64,660,"ICML 2024  ·  Hu, Yao, Qiu, ... Li  ·  arXiv:2405.16466  ·  github.com/BICLab/T-RevSNN",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
