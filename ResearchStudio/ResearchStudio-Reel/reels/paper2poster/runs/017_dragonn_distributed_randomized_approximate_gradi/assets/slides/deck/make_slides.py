#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 017 (DRAGONN, ICML 2022).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue
pass resolves every anchor from PPTX geometry. Zero <image>, zero gradients, ASCII
mono equations only."""
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
    p=" ".join(f"{px},{py}" for px,py in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

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

def kpi(x,y,num,lbl,col,w=168,h=100,ns=30):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,ns,col,"800",anchor="middle")+
            T(x+w/2,y+h-16,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICML 2022",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Rice University  ·  ThirdAI Corp",14,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,158,"DRAGONN",46,WHITE,"800")
    b+=T(64,204,"Distributed Randomized Approximate",30,ACCENT,"800")
    b+=T(64,242,"Gradients of Neural Networks",30,ACCENT,"800")
    b+=T(64,282,"Zhuang Wang · Zhaozhuo Xu · Xinyu Crystal Wu · Anshumali Shrivastava · T. S. Eugene Ng",15,SEC,"500")
    # three concept cards (top row wide + two below) = anchors
    cw=560; chh=118; gap=32; x0=64; x1=x0+cw+gap; cy0=320; cy1=cy0+chh+22
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(x0,cy0,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x0,cy0,6,chh,fill=ACCENT,rx=6,sw=0)+
        T(x0+28,cy0+36,"A randomized hashing compressor",18,TEXT,"800")+
        para(x0+28,cy0+62,"DRAGONN sparsifies gradients by direct hashing instead of exact top-k selection, for data-parallel distributed training.",14,SEC,66,21)[0])
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(x1,cy0,cw,chh,fill=PANEL,stroke=STROKE)+
        rect(x1,cy0,6,chh,fill=GOLD,rx=6,sw=0)+
        T(x1+28,cy0+36,"The moving bottleneck",18,TEXT,"800")+
        para(x1+28,cy0+62,"Synchronizing gradients across GPUs dominates cost; sparsification was meant to help, but its compression overhead became the new bottleneck.",14,SEC,66,21)[0])
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(x0,cy1,cw*2+gap,chh,fill="#0F2E2B",stroke=TEAL,sw=1.5)+
        rect(x0,cy1,6,chh,fill=TEAL,rx=6,sw=0)+
        T(x0+28,cy1+36,"The payoff",18,TEAL,"800")+
        para(x0+28,cy1+62,"Replacing exact parallel-prefix-sum with direct hashing cuts compression time by up to 70% and speeds up total training by up to 3.5x.",14.5,TEXT,140,21)[0])
    b+=line(64,616,1216,616,STROKE,1)
    b+=T(64,650,"github.com/zhuangwang93/dragonn",14,ACCENT,"700")
    b+=T(420,650,"Sparsification only needs an approximate set of top gradients — so it should not pay for an exact one.",14,SEC,"600")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","When compression costs more than it saves")
    # c1 setup (left tall card)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"The dominant cost",18,TEXT,"800")+
        para(92,240,"Data-parallel training is the standard way to scale deep learning across many GPUs, but synchronizing gradients between workers is the single largest cost.",15,SEC,42,24)[0]+
        # mini all-reduce glyph
        rect(92,360,344,150,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,388,"gradient all-reduce",12.5,TER,"700")+
        circle(150,446,15,fill=ACCENT)+circle(230,446,15,fill=ACCENT)+circle(310,446,15,fill=ACCENT)+circle(390,446,15,fill=ACCENT)+
        T(150,451,"g0",11,BG,"800",anchor="middle")+T(230,451,"g1",11,BG,"800",anchor="middle")+
        T(310,451,"g2",11,BG,"800",anchor="middle")+T(390,451,"g3",11,BG,"800",anchor="middle")+
        line(165,446,215,446,GOLD,2)+line(245,446,295,446,GOLD,2)+line(325,446,375,446,GOLD,2)+
        T(264,492,"sync every step  =  communication bottleneck",12.5,GOLD,"700",anchor="middle"))
    # c2 promise vs reality (right top)
    fx=500; fw=716
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=GOLD,rx=6,sw=0)+
        T(fx+28,196,"Gradient sparsification: promise vs reality",17,GOLD,"800")+
        rect(fx+28,216,332,72,fill=PANEL2,stroke=STROKE,rx=8)+circle(fx+52,240,6,fill=TEAL)+T(fx+70,245,"Promise",13.5,TEAL,"800")+
        para(fx+70,266,"send only a small subset of gradients",12.5,SEC,40,16)[0]+
        rect(fx+380,216,308,72,fill=PANEL2,stroke=STROKE,rx=8)+circle(fx+404,240,6,fill=RED)+T(fx+422,245,"Reality",13.5,RED,"800")+
        para(fx+422,266,"compression time cancels the savings",12.5,SEC,36,16)[0])
    # c3 crossover chart (right bottom)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,326,fw,224,fill="#2A1720",stroke=RED,rx=14,sw=1.5)+
        rect(fx,326,6,224,fill=RED,rx=6,sw=0)+
        T(fx+28,362,"Compression overhead dominates past ~16 MB (2^24 bytes)",15.5,RED,"800")+
        _overhead_chart(fx+300,378,388,150)+
        para(fx+28,398,"Above the crossover, compression is the single largest efficiency bottleneck.",13.5,SEC,34,21)[0]+
        para(fx+28,470,"For small tensors, sparsification can even be slower than sending everything.",13.5,TER,34,21)[0])
    return svg(b)

def _overhead_chart(x,y,w,h):
    # bars: at 3 tensor sizes, compression fraction rises
    box=rect(x,y,w,h,fill="#1A1016",stroke=STROKE,rx=8)
    base=y+h-26; bw=60; gap=48; x0=x+40
    sizes=[("1 MB",0.28,GOLD),("16 MB",0.62,GOLD),(">16 MB",0.9,RED)]
    out=box+line(x0-10,base,x+w-14,base,STROKE,1.2)
    out+=T(x0-16,y+16,"compression share",10.5,TER,"600")+T(x+w-14,y+16,"tensor size ->",10.5,TER,"600",anchor="end")
    for i,(lbl,frac,col) in enumerate(sizes):
        bx=x0+i*(bw+gap); bh=int((h-52)*frac)
        out+=rect(bx,base-bh,bw,bh,fill=col,rx=4,sw=0)
        out+=T(bx+bw/2,base-bh-6,f"{int(frac*100)}%",11.5,col,"800",anchor="middle")
        out+=T(bx+bw/2,base+16,lbl,11,SEC,"600",anchor="middle")
    return out

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","An exact algorithm doing an approximate job")
    # c1 DGC selects above threshold (approximate) - left
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,180,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,180,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"How Deep Gradient Compression (DGC) works",16.5,ACCENT,"800")+
        para(92,226,"DGC keeps gradients whose magnitude clears an estimated threshold — an inherently approximate selection.",14.5,SEC,58,22)[0]+
        rect(92,290,504,34,fill=PANEL2,stroke=STROKE,rx=8)+
        T(344,312,"select  |g| > threshold   (approximate top-k)",14,ACCENT,"800",anchor="middle",ff=MONO))
    # c2 prefix sum exact + 7x bar - left bottom
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,354,560,196,fill=PANEL,stroke=STROKE)+
        rect(64,354,6,196,fill=RED,rx=6,sw=0)+
        T(92,392,"...but placement uses exact parallel prefix sum",16,RED,"800")+
        para(92,420,"To pack kept gradients without conflicts, DGC builds a balanced binary tree, runs O(log d) sequential steps, and touches memory ~7x more than the lower bound.",13.5,SEC,58,20)[0]+
        _memaccess_bar(340,470,240,58))
    # c3 exact-approximate mismatch - right
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,392,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,158,6,392,fill=GOLD,rx=6,sw=0)+
        T(684,200,"The exact-approximate mismatch",19,GOLD,"800")+
        # two-column glyph: need vs use
        rect(684,232,246,150,fill=PANEL2,stroke=STROKE,rx=10)+
        T(807,262,"What is needed",13,TEAL,"800",anchor="middle")+
        T(807,300,"approximate",20,TEAL,"800",anchor="middle")+
        T(807,326,"set of top gradients",13,SEC,"600",anchor="middle")+
        T(807,360,"cheap is fine",12.5,TER,"600",anchor="middle")+
        rect(942,232,246,150,fill=PANEL2,stroke=STROKE,rx=10)+
        T(1065,262,"What DGC uses",13,RED,"800",anchor="middle")+
        T(1065,300,"exact",20,RED,"800",anchor="middle")+
        T(1065,326,"prefix-sum placement",13,SEC,"600",anchor="middle")+
        T(1065,360,"expensive & sequential",12.5,TER,"600",anchor="middle")+
        para(684,420,"Paying for an exact selection algorithm when only an approximate result is required is wasted effort.",14.5,TEXT,58,23)[0]+
        T(684,512,"Idea: match the algorithm's exactness to the task.",14.5,GOLD,"800"))
    return svg(b)

def _memaccess_bar(x,y,w,h):
    return (T(x-12,y+16,"memory accesses vs lower bound",11,TER,"600",anchor="end")+
            bar(x,y+26,w,1,7,TEAL,"lower bound","1x",h=13)+
            bar(x,y+46,w,7,7,RED,"prefix sum","~7x",h=13))

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","Three contributions")
    # c1 intro strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,56,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,56,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"The paper contributes one new algorithm, two system-level optimizations, and a broad empirical study.",16,TEXT,"600"))
    cards=[
        (ch[1],ACCENT,"1","DRAGONN algorithm","A hashing-based sparsifier that slashes compression overhead while keeping the same per-iteration convergence, with theoretical bounds on compression and generalization error."),
        (ch[2],GOLD,"2","Two system optimizations","Efficiency-aware tensor selection compresses only where it pays off; sparse decoding keeps decode cost from growing with the number of GPUs."),
        (ch[3],GREEN,"3","Broad evaluation","Tested across vision and recommendation models, demonstrating large, consistent end-to-end training speedups."),
    ]
    cw=368; gap=24; x0=64; cy=240; chh=310
    for i,(c,col,num,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+56,cy+72,28,fill="none",stroke=col,sw=2.5)+
              T(x+56,cy+83,num,30,col,"800",anchor="middle"))
        yy=cy+148
        for j,ln in enumerate(wrap(ti,22)):
            body+=T(x+28,yy+j*28,ln,19,TEXT,"800")
        yy+=28*len(wrap(ti,22))+14
        body+=para(x+28,yy,tx,14.5,SEC,40,23)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,588,"One idea — hash, do not sort — unlocks all three.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Hash gradients straight into a buffer")
    # LEFT top: c1 hash directly
    lx=64; lw=560
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,232,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,232,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Pre-allocate, then hash-and-write",16.5,ACCENT,"800")+
        para(lx+28,226,"Allocate a small buffer sized to the compression ratio. For each gradient whose |value| clears the threshold, hash its index directly to a slot and write it — no scan for nonzero positions.",13.5,SEC,64,20)[0]+
        _hashtable(lx+28,306,lw-56))
    # LEFT bottom: c2 collisions
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,404,lw,146,fill=PANEL,stroke=STROKE)+
        rect(lx,404,6,146,fill=GOLD,rx=6,sw=0)+
        T(lx+28,440,"Collisions are cheap by design",16,GOLD,"800")+
        para(lx+28,470,"If two indices hash to the same slot, the later write overwrites the earlier one; any slot left empty maps to zero.",14,SEC,60,20)[0]+
        eqbox(lx+28,508,lw-56,"collision -> overwrite      empty slot (-1) -> 0",13.5,h=36))
    # RIGHT top: c3 atomic parallel + cost
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,214,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(rxx,158,6,214,fill=TEAL,rx=6,sw=0)+
        T(rxx+28,196,"Embarrassingly parallel on the GPU",16.5,TEAL,"800")+
        para(rxx+28,226,"Because GPU memory writes are atomic, many threads hash and write at once with no ordering dependency, so the whole compression needs only d comparisons plus l hashes.",13.5,SEC,56,20)[0]+
        eqbox(rxx+28,308,rw-56,"cost = d comparisons + l hashes  ~ lower bound",14))
    # RIGHT bottom: c4 two deploy tricks
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,388,rw,162,fill=PANEL,stroke=STROKE)+
        rect(rxx,388,6,162,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,424,"Two tricks for real deployment",16,GREEN,"800")+
        rect(rxx+28,440,252,92,fill=PANEL2,stroke=STROKE,rx=8)+
        T(rxx+44,466,"Tensor selection",13.5,GREEN,"800")+
        para(rxx+44,488,"compress a tensor only when it saves more than it costs",12,SEC,32,16)[0]+
        rect(rxx+296,440,236,92,fill=PANEL2,stroke=STROKE,rx=8)+
        T(rxx+312,466,"Sparse decoding",13.5,GREEN,"800")+
        para(rxx+312,488,"batch all received tensors into one decode; cost ~ constant in GPUs",12,SEC,30,16)[0])
    return svg(b)

def _hashtable(x,y,w):
    # two stacked index chips -> hash pill -> buffer slots; two collide into slot 3
    out=T(x,y-2,"two indices hash to one slot — the later write wins",11,TER,"700")
    cy=y+10
    out+=(rect(x,cy,58,20,fill=PANEL2,stroke=TEAL,rx=6,sw=1.4)+T(x+29,cy+14,"i=9",11.5,TEAL,"800",anchor="middle")+
          rect(x,cy+26,58,20,fill=PANEL2,stroke=GOLD,rx=6,sw=1.4)+T(x+29,cy+40,"i=17",11.5,GOLD,"800",anchor="middle"))
    hx=x+94
    out+=rect(hx,cy+13,54,20,fill="#0E2334",stroke=ACCENT,rx=10,sw=1.2)+T(hx+27,cy+27,"hash",11.5,ACCENT,"800",anchor="middle")
    out+=line(x+58,cy+10,hx,cy+21,TEAL,1.5,dash="3 3")+line(x+58,cy+36,hx,cy+25,GOLD,1.5,dash="3 3")
    sw_=30; ns=6; gap=6; tot=ns*(sw_+gap)-gap
    sx=x+w-tot; sy=cy+13
    out+=T(sx,sy-8,"buffer",10.5,TER,"700")
    for s in range(ns):
        hit=(s==3)
        out+=rect(sx+s*(sw_+gap),sy,sw_,26,fill="#2A2417" if hit else PANEL2,
                  stroke=GOLD if hit else STROKE,rx=5,sw=1.4 if hit else 1)
        if hit: out+=T(sx+3*(sw_+gap)+sw_/2,sy+18,"17",12,GOLD,"800",anchor="middle")
    out+=line(hx+54,cy+23,sx+3*(sw_+gap),sy+13,ACCENT,1.5,dash="3 3")
    return out

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Vision and recommendation workloads")
    # c1 four models (left wide)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,700,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,200,"Four models, two domains",18,TEXT,"800")+
        _modelrow(92,232,"ResNet50","ImageNet-1K",ACCENT,"vision · CNN")+
        _modelrow(92,312,"Vision Transformer","Cifar10  (ImageNet-21k pretrain)",TEAL,"vision · fine-tune")+
        _modelrow(92,392,"MLP-Mixer","Cifar10  (ImageNet-21k pretrain)",GOLD,"vision · fine-tune")+
        _modelrow(92,472,"XML classifier","Wiki10-31K",GREEN,"extreme multi-label"))
    # c2 testbed (right)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(788,158,428,392,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(788,158,6,392,fill=TEAL,rx=6,sw=0)+
        T(816,200,"Testbed",18,TEAL,"800")+
        kpi(816,224,"16","V100-32GB GPUs",TEAL,w=180,h=92,ns=32)+
        kpi(1012,224,"25 Gbps","network",TEAL,w=180,h=92,ns=24)+
        kpi(816,332,"2 x 8","two machines",ACCENT,w=180,h=92,ns=28)+
        kpi(1012,332,"NCCL","+ Horovod",ACCENT,w=180,h=92,ns=26)+
        rect(816,440,400,92,fill=PANEL2,stroke=STROKE,rx=10)+
        T(836,468,"Software & accuracy",13,SEC,"800")+
        para(836,490,"PyTorch 1.8 · CUDA 11.0 · memory-momentum error feedback preserves accuracy for every method.",13,SEC,52,19)[0])
    return svg(b)

def _modelrow(x,y,name,data,col,tag):
    return (rect(x,y,644,66,fill=PANEL2,stroke=STROKE,rx=10)+
            rect(x,y,5,66,fill=col,rx=3,sw=0)+
            T(x+24,y+30,name,16,TEXT,"800")+
            T(x+24,y+52,data,13,SEC,"600")+
            T(x+624,y+30,tag,12.5,col,"700",anchor="end"))

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Compression cut, throughput multiplied")
    # c1 compression time headline (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=TEAL,rx=6,sw=0)+
        T(92,196,"Compression time",16.5,TEAL,"800")+
        kpi(92,214,"-70%","vs best existing GS",TEAL,w=180,h=78,ns=32)+
        para(292,236,"DRAGONN cuts compression time by up to seventy percent compared with the best prior sparsification methods.",13.5,SEC,42,20)[0])
    # c2 throughput bars (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,226,fill=GREEN,rx=6,sw=0)+
        T(92,360,"Total training throughput at equal convergence",15,TEXT,"800")+
        bar(300,384,240,1,36,SEC,"FULL sync","1x",h=26)+
        bar(300,420,240,10.2,36,ACCENT,"DGC","~10x",h=26)+
        bar(300,456,240,36,36,GREEN,"DRAGONN","up to 35.9x",h=26)+
        rect(92,496,504,42,fill="#0F2E2B",stroke=GREEN,rx=10,sw=1.5)+
        T(112,522,"Up to 3.52x over DGC — and it matches FULL's test accuracy",14,GREEN,"800"))
    # c3 scalability (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,392,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,158,6,392,fill=GOLD,rx=6,sw=0)+
        T(684,200,"The lead grows with scale",18,GOLD,"800")+
        para(684,232,"DRAGONN's advantage over DGC widens as more GPUs are added — evidence of strong scalability.",14.5,SEC,56,22)[0]+
        _scale_chart(684,296,504,190))
    b+=T(64,650,"Faster networks would tilt the balance further toward compression — widening the gains.",14,SEC,"600")
    return svg(b)

def _scale_chart(x,y,w,h):
    box=rect(x,y,w,h,fill="#1A1608",stroke=STROKE,rx=10)
    base=y+h-30; left=x+44
    out=box+line(left,y+18,left,base,STROKE,1.2)+line(left,base,x+w-20,base,STROKE,1.2)
    out+=T(left-8,y+16,"speedup vs DGC",10.5,TER,"600",anchor="end") if False else ""
    out+=T(x+20,y+30,"speedup",10.5,TER,"700")+T(x+w-20,base+20,"# GPUs ->",11,TER,"700",anchor="end")
    gpus=[(4,1.6),(8,2.3),(16,3.52)]
    xs=[left+40,left+180,left+340]
    pts=[]
    for (g,v),px in zip(gpus,xs):
        py=base-int((v/4.0)*(h-56))
        pts.append((px,py))
        out+=T(px,base+18,str(g),11,SEC,"700",anchor="middle")
        out+=circle(px,py,5,fill=GOLD)+T(px,py-12,f"{v:.2f}x",12,GOLD,"800",anchor="middle")
    out+=poly(pts,stroke=GOLD,sw=2.6)
    return out

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Each component adds speedup")
    # c1 intro strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,54,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,54,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"A component ablation isolates the three parts of DRAGONN, added one at a time.",16,TEXT,"600"))
    # c2 staircase bars (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,230,560,320,fill=PANEL,stroke=STROKE)+
        rect(64,230,6,320,fill=TEAL,rx=6,sw=0)+
        T(92,268,"Speedup builds up (one model)",16,TEAL,"800")+
        _stair(120,296,440,232))
    # c3 sparse decoding exceeds K (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,230,560,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,230,6,150,fill=GREEN,rx=6,sw=0)+
        T(684,268,"Why the gain exceeds the worker count",15.5,GREEN,"800")+
        para(684,298,"Sparse decoding removes the decode cost that otherwise grows linearly with the number of GPUs, so its benefit can exceed K-fold.",14,SEC,58,22)[0])
    # c4 micro-benchmarks (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,396,560,154,fill=PANEL,stroke=STROKE)+
        rect(656,396,6,154,fill=GOLD,rx=6,sw=0)+
        T(684,432,"Micro-benchmarks confirm it",15.5,GOLD,"800")+
        chip(684,448,"Lowest encoding time across all tensor sizes",GOLD,w=504,h=32)+
        _decode_lines(684,494,504,46))
    return svg(b)

def _stair(x,y,w,h):
    base=y+h-26; bw=110; gap=40; x0=x+10
    steps=[("hashing\nonly",1.0,ACCENT,"1.0x"),("+ tensor\nselection",1.92,TEAL,"1.92x"),("+ sparse\ndecoding",4.33,GREEN,"4.33x")]
    out=line(x0-6,base,x+w-6,base,STROKE,1.2)+T(x-2,y+12,"speedup",10.5,TER,"700")
    for i,(lbl,v,col,vt) in enumerate(steps):
        bx=x0+i*(bw+gap); bh=int((h-56)*v/4.33)
        out+=rect(bx,base-bh,bw,bh,fill=col,rx=5,sw=0)
        out+=T(bx+bw/2,base-bh-8,vt,14,col,"800",anchor="middle")
        for j,ln in enumerate(lbl.split("\n")):
            out+=T(bx+bw/2,base+16+j*15,ln,11,SEC,"600",anchor="middle")
    return out

def _decode_lines(x,y,w,h):
    out=T(x,y-2,"decode time as GPUs grow:",11.5,TER,"700")
    # dense grows linear (red), sparse flat (green)
    x0=x+220; base=y+h-8; span=w-236
    out+=line(x0,base,x0+span,base-32,RED,2.2)+T(x0+span,base-34,"dense (linear)",10.5,RED,"800",anchor="end")
    out+=line(x0,base-2,x0+span,base-4,GREEN,2.2)+T(x0+span,base-8,"sparse (flat)",10.5,GREEN,"800",anchor="end")
    return out

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The results in one place")
    body =rect(64,166,1152,384,fill=PANEL,stroke=STROKE)
    body+=rect(64,166,6,384,fill=GREEN,rx=6,sw=0)
    body+=T(92,206,"DRAGONN vs the state of the art",17,GREEN,"800")
    # top KPI row
    body+=kpi(92,226,"-70%","compression time vs SOTA GS",TEAL,w=352,h=104,ns=34)
    body+=kpi(464,226,"3.52x","total speedup over DGC",GREEN,w=352,h=104,ns=34)
    body+=kpi(836,226,"35.9x","over FULL synchronization",GOLD,w=352,h=104,ns=34)
    # per-model bars
    body+=T(92,364,"Per-model speedup over DGC (Table 2)",14.5,TEXT,"800")
    body+=bar(300,384,300,1.42,3.52,ACCENT,"ResNet50","1.42x",h=24)
    body+=bar(300,416,300,2.15,3.52,ACCENT,"ViT","2.15x",h=24)
    body+=bar(300,448,300,1.72,3.52,ACCENT,"MLP-Mixer","1.72x",h=24)
    body+=bar(300,480,300,3.52,3.52,GREEN,"XML","3.52x",h=24)
    # right callout
    body+=rect(700,376,488,150,fill=PANEL2,stroke=STROKE,rx=12)
    body+=T(724,406,"And the decode overhead",14.5,GOLD,"800")
    body+=T(724,452,"linear in #GPUs",20,RED,"800")
    body+=T(724,478,"->",22,SEC,"800")+T(770,478,"nearly constant",20,GREEN,"800")
    body+=T(724,510,"thanks to sparse decoding",13,SEC,"600")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],body)
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Match the algorithm to the task")
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,176,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,176,6,150,fill=ACCENT,rx=6,sw=0)+
        circle(112,232,10,fill=ACCENT)+
        T(150,224,"Do not pay for exactness you do not need",19,TEXT,"800")+
        para(150,256,"Gradient sparsification only ever needs an approximate set of top gradients, so using an expensive exact selection algorithm to place them is wasted effort.",15.5,SEC,92,24)[0])
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,342,1152,150,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,342,6,150,fill=TEAL,rx=6,sw=0)+
        circle(112,398,10,fill=TEAL)+
        T(150,390,"Hashing makes sparsification finally pay off",19,TEXT,"800")+
        para(150,422,"Swapping exact prefix sum for direct randomized hashing turns a sequential, dependency-heavy step into an embarrassingly parallel one; with tensor selection and sparse decoding it delivers scalable speedups without hurting accuracy.",15.5,SEC,96,24)[0])
    b+=line(64,536,1216,536,STROKE,1)
    b+=T(64,572,"DRAGONN: Distributed Randomized Approximate Gradients of Neural Networks",15.5,TEXT,"700")
    b+=T(64,600,"ICML 2022  ·  Rice University & ThirdAI  ·  github.com/zhuangwang93/dragonn",13.5,SEC,"600")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
