#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 011
(G2N2: Weisfeiler and Lehman Go Grammatical - ICLR 2024,
LITIS Rouen Normandy / LIFAT Tours).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_...">
card with a <title> holding the cue keywords, so the strict
--require-pptx-anchors cue pass resolves every anchor from PPTX geometry.
Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: an expressive matrix-language fragment ML(L3) becomes a
context-free grammar, the grammar is reduced, and its rules become the
layers of a provably 3-WL graph neural network."""
import json, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
META = os.environ["VIDEO_META"]
OUT  = os.path.join(HERE, "svg_output")
os.makedirs(OUT, exist_ok=True)
AM = json.load(open(os.path.join(META, "_anchor_map.json")))

W, H = 1280, 720
BG="#0B1A2B"; PANEL="#122A42"; PANEL2="#173453"; STROKE="#2A4D6E"
ACCENT="#3E9BFF"; TEAL="#33D6C0"; GOLD="#F4C24C"; RED="#F2685C"; GREEN="#46C98B"
VIOLET="#9C86F0"
TEXT="#EAF2FB"; SEC="#9DB3C8"; TER="#6E869C"; WHITE="#FFFFFF"
GLYPH_BG="#0E223A"; TRACK="#0A1A2C"
WARM="#2A2417"; SUCCESS_T="#0F2E2B"
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
    p=" ".join(f"{x},{y}" for x,y in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{d}/>'

def polygon(pts,fill=ACCENT,stroke=None,sw=1.0):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    p=" ".join(f"{x},{y}" for x,y in pts)
    return f'<polygon points="{p}" fill="{fill}"{st}/>'

def arrow(x1,y1,x2,y2,color=STROKE,sw=1.5,head=6):
    ang=math.atan2(y2-y1,x2-x1)
    hx,hy=x2-head*math.cos(ang),y2-head*math.sin(ang)
    p1=(hx-head*math.cos(ang-0.5),hy-head*math.sin(ang-0.5))
    p2=(hx-head*math.cos(ang+0.5),hy-head*math.sin(ang+0.5))
    return (line(x1,y1,x2,y2,color,sw)+
            polygon([(x2,y2),p1,p2],fill=color))

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

def stat(x,y,w,h,num,lbl,col):
    ns=min(30,h*0.34)
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,ns,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.80,lbl,12.5,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14.5,TEXT,"600"))

def eqbox(x,y,w,expr,size=17,h=44,col=TEXT):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,col,"800",anchor="middle",ff=MONO))

# ---- theme glyphs -------------------------------------------------------
def pipefig(cx,cy,scale=1.0):
    """Grammar-to-network motif: expressive language fragment -> grammar ->
    provably 3-WL network. Three boxes joined by arrows."""
    bw=int(80*scale); bh=int(38*scale); gap=int(28*scale)
    total=3*bw+2*gap
    x0=cx-total/2; y=cy-bh/2
    labels=[("ML(L3)",ACCENT),("grammar",GOLD),("G2N2",GREEN)]
    out=""; xs=[]
    for i,(lb,col) in enumerate(labels):
        bx=x0+i*(bw+gap)
        xs.append((bx,bx+bw))
        out+=rect(bx,y,bw,bh,fill=PANEL2,stroke=col,rx=8,sw=1.6)
        out+=T(bx+bw/2,y+bh/2+5,lb,12*scale,col,"800",anchor="middle",ff=MONO)
    for i in range(2):
        out+=arrow(xs[i][1]+3,cy,xs[i+1][0]-3,cy,STROKE,1.6,7)
    out+=T(cx,y-12,"expressive language",10.5*scale,SEC,"700",anchor="middle")
    out+=T(cx,y+bh+18,"provably 3-WL network",10.5*scale,SEC,"700",anchor="middle")
    return out

def opset(x,y,w):
    """The operation set L3 that seeds the grammar."""
    ops=[("MatMul",ACCENT),("Transpose",TEAL),("All-ones",GOLD),
         ("Diagonal",VIOLET),("Hadamard",GREEN)]
    gap=10; bw=(w-(len(ops)-1)*gap)/len(ops); out=""
    for i,(nm,col) in enumerate(ops):
        bx=x+i*(bw+gap)
        out+=rect(bx,y,bw,30,fill=PANEL2,stroke=col,rx=7,sw=1.3)
        out+=circle(bx+13,y+15,4,fill=col)
        out+=T(bx+bw/2+6,y+19,nm,11.5,TEXT,"700",anchor="middle")
    return out

def grammar_engine(x,y,w,h):
    """Exhaustive grammar G(L3) reduced to a compact grammar r-G(L3); the
    reduced rules become inputs and layers. Compact, fits within (x,y,w,h)."""
    out=rect(x,y,w,h,fill=GLYPH_BG,stroke=STROKE,rx=8)
    py=y+22; ph=h-40
    # left panel: exhaustive grammar (4 rule bars)
    lw=int(w*0.28); lx=x+18
    out+=T(lx+lw/2,y+16,"G(L3) exhaustive",9.5,SEC,"800",anchor="middle")
    out+=rect(lx,py,lw,ph,fill=PANEL,stroke=ACCENT,rx=6,sw=1.0)
    for i in range(4):
        out+=rect(lx+8,py+6+i*((ph-10)/4.0),lw-16,3.5,fill=ACCENT,rx=2,sw=0)
    # reduce arrow
    ax0=lx+lw+12; ax1=ax0+int(w*0.20)
    my=py+ph/2
    out+=T((ax0+ax1)/2,y+14,"reduce",10,GOLD,"800",anchor="middle")
    out+=arrow(ax0,my,ax1,my,GOLD,2.0,8)
    out+=T((ax0+ax1)/2,my+18,"keep 3-WL",8.5,GOLD,"700",anchor="middle")
    # right panel: reduced grammar (2 rule bars, highlighted)
    rw=int(w*0.30); rx0=ax1+14
    out+=T(rx0+rw/2,y+16,"r-G(L3) reduced",9.5,GREEN,"800",anchor="middle")
    out+=rect(rx0,py,rw,ph,fill=PANEL,stroke=GREEN,rx=6,sw=1.2)
    for i in range(2):
        out+=rect(rx0+8,py+8+i*((ph-14)/2.0),rw-16,5,fill=GREEN,rx=2,sw=0)
    # far right: what the reduced grammar yields
    cx=rx0+rw+16
    out+=T(cx,my-4,"inputs",10.5,TEAL,"800",ff=MONO)
    out+=T(cx,my+13,"& layers",10.5,TEAL,"800",ff=MONO)
    return out

def layerfig(x,y,w,h):
    """One G2N2 layer: edge memory C and node memory H, reduced rules, MLPs.
    Self-contained within (x,y,w,h); grid sized so nothing pokes past the box."""
    out=rect(x,y,w,h,fill=GLYPH_BG,stroke=STROKE,rx=8)
    gs=10; cy=y+h/2+4
    # C : 3x3 matrix grid
    gx=x+20
    out+=T(gx+1.5*gs,y+16,"C",10,ACCENT,"800",anchor="middle")
    for r in range(3):
        for c in range(3):
            out+=rect(gx+c*gs,cy-1.5*gs+r*gs,gs-2,gs-2,fill=PANEL2,stroke=ACCENT,rx=2,sw=0.7)
    # H : vector column
    hx=gx+3*gs+16
    out+=T(hx+4,y+16,"H",10,TEAL,"800",anchor="middle")
    for r in range(3):
        out+=rect(hx,cy-1.5*gs+r*gs,gs-2,gs-2,fill=PANEL2,stroke=TEAL,rx=2,sw=0.7)
    # rules chips
    rcx=hx+40
    out+=arrow(rcx-13,cy,rcx-2,cy,STROKE,1.4,6)
    rules=[("M*M",ACCENT),("M o M",GOLD),("diag",VIOLET)]
    for i,(nm,col) in enumerate(rules):
        by=cy-22+i*15
        out+=rect(rcx,by,70,12,fill=PANEL2,stroke=col,rx=4,sw=1.0)
        out+=T(rcx+35,by+10,nm,9,col,"800",anchor="middle",ff=MONO)
    # MLP box
    mx=rcx+86
    out+=arrow(mx-12,cy,mx-2,cy,STROKE,1.4,6)
    out+=rect(mx,cy-19,48,38,fill=PANEL2,stroke=WHITE,rx=6,sw=1.4)
    out+=T(mx+24,cy+4,"MLP",10.5,WHITE,"800",anchor="middle",ff=MONO)
    # outputs
    ox=mx+48
    out+=arrow(ox+2,cy,ox+20,cy,STROKE,1.4,6)
    out+=T(ox+40,cy-3,"C'",12,ACCENT,"800",anchor="middle",ff=MONO)
    out+=T(ox+40,cy+15,"H'",12,TEAL,"800",anchor="middle",ff=MONO)
    return out

def wlladder(x,y,w,h):
    """The WL/MATLANG bridge: 1-WL <-> ML(L1), 3-WL <-> ML(L3)."""
    out=rect(x,y,w,h,fill=GLYPH_BG,stroke=STROKE,rx=8)
    rows=[("1-WL","ML(L1)",TEAL),("3-WL","ML(L3)",ACCENT)]
    bw=int(w*0.30); bh=34
    lx=x+24; rx0=x+w-24-bw
    for i,(wl,ml,col) in enumerate(rows):
        ry=y+22+i*((h-40)/2.0)
        out+=rect(lx,ry,bw,bh,fill=PANEL2,stroke=col,rx=7,sw=1.4)
        out+=T(lx+bw/2,ry+bh/2+5,wl,13,col,"800",anchor="middle",ff=MONO)
        out+=rect(rx0,ry,bw,bh,fill=PANEL2,stroke=col,rx=7,sw=1.4)
        out+=T(rx0+bw/2,ry+bh/2+5,ml,13,col,"800",anchor="middle",ff=MONO)
        # double arrow (equivalence)
        my=ry+bh/2
        out+=line(lx+bw+8,my,rx0-8,my,col,1.6)
        out+=polygon([(lx+bw+8,my),(lx+bw+16,my-4),(lx+bw+16,my+4)],fill=col)
        out+=polygon([(rx0-8,my),(rx0-16,my-4),(rx0-16,my+4)],fill=col)
        out+=T((lx+bw+rx0)/2,my-8,"same value",8.5,SEC,"700",anchor="middle")
    return out

def arenarow(x,y,w,items):
    gap=16; bw=(w-(len(items)-1)*gap)/len(items); out=""
    for i,(nm,col,sub) in enumerate(items):
        bx=x+i*(bw+gap)
        out+=rect(bx,y,bw,58,fill=PANEL2,stroke=col,rx=10,sw=1.5)
        out+=rect(bx,y,bw,5,fill=col,rx=3,sw=0)
        out+=T(bx+bw/2,y+31,nm,14,TEXT,"800",anchor="middle")
        out+=T(bx+bw/2,y+49,sub,10.5,SEC,"600",anchor="middle")
    return out

def tudrow(x,y,w,items,col=GOLD):
    gap=8; bw=(w-(len(items)-1)*gap)/len(items); out=""
    for i,nm in enumerate(items):
        bx=x+i*(bw+gap)
        out+=rect(bx,y,bw,26,fill=PANEL2,stroke=col,rx=6,sw=1.1)
        out+=T(bx+bw/2,y+17,nm,10.5,TEXT,"700",anchor="middle")
    return out

def cmpbars(x,y,w,h,g,p,glab,plab,fmt="{:.2f}",lower_better=True,ratio=None):
    """Two-bar comparison G2N2 vs PPGN. Bars proportional to value; the winner
    (lower for MAE / higher for R2) is green, the other muted."""
    out=rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=10)
    ay0=y+h-24; top=y+34; span=ay0-top
    mx=max(g,p) if max(g,p)>0 else 1.0
    g_win = (g<p) if lower_better else (g>p)
    pairs=[("G2N2",g,GREEN if g_win else SEC),(plab,p,GREEN if not g_win else SEC)]
    slot=(w-40)/2.0
    for i,(lb,v,c) in enumerate(pairs):
        cx=x+20+slot*i+slot/2
        bh=max(6,span*(v/mx))
        out+=rect(cx-38,ay0-bh,76,bh,fill=c,rx=5,sw=0)
        out+=T(cx,ay0-bh-8,fmt.format(v),14,c,"800",anchor="middle")
        out+=T(cx,ay0+16,lb,11,SEC,"700",anchor="middle")
    if ratio:
        out+=rect(x+w/2-52,y+8,104,20,fill=SUCCESS_T,stroke=GREEN,rx=7,sw=1.1)
        out+=T(x+w/2,y+22,ratio,11,GREEN,"800",anchor="middle")
    return out

def spectralcurve(x,y,w,h):
    """Spectral band-pass test: G2N2 tracks the target band-pass response,
    PPGN stays flat and low."""
    out=rect(x,y,w,h,fill=GLYPH_BG,stroke=STROKE,rx=8)
    ax0=x+34; ax1=x+w-14; ay0=y+h-24; ay1=y+18
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    def band(t):  # band-pass bump peaked at t=0.5
        return math.exp(-((t-0.5)**2)/(2*0.10**2))
    tgt=[]; g2=[]
    for k in range(0,101,4):
        u=k/100.0
        tgt.append((ax0+u*(ax1-ax0), ay0-band(u)*(ay0-ay1)))
        # G2N2 tracks target closely with tiny wobble
        val=band(u)*0.94
        g2.append((ax0+u*(ax1-ax0), ay0-val*(ay0-ay1)))
    out+=poly(tgt,stroke=SEC,sw=1.8,dash="5 5")
    out+=poly(g2,stroke=GREEN,sw=2.8)
    # PPGN flat low
    out+=poly([(ax0,ay0-0.10*(ay0-ay1)),(ax1,ay0-0.10*(ay0-ay1))],stroke=RED,sw=2.2,dash="2 4")
    out+=T(ax1,ay1+4,"G2N2  R2 0.82",10,GREEN,"800",anchor="end")
    out+=T(ax1,ay0-0.10*(ay0-ay1)-6,"PPGN  0.10",9.5,RED,"800",anchor="end")
    out+=T(ax0-4,ay1-2,"gain",9,TER,"600",anchor="end")
    out+=T(ax1,ay0+15,"frequency ->",9,TER,"600",anchor="end")
    return out

def reductionbars(x,y,w,h):
    """Grammar-reduction ablation on QM9 R2: full G, intermediate, reduced
    r-G(L3) reach the same low error; over-reducing spikes the error up."""
    out=rect(x,y,w,h,fill=GLYPH_BG,stroke=STROKE,rx=8)
    ax0=x+30; ax1=x+w-16; ay0=y+h-30; ay1=y+30
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    bars=[("G(L3)",0.30,TEAL),("interm.",0.30,TEAL),("r-G(L3)",0.31,GREEN),("over-red.",0.86,RED)]
    n=len(bars); slot=(ax1-ax0)/n
    for i,(lb,v,c) in enumerate(bars):
        cx=ax0+slot*i+slot/2
        bh=v*(ay0-ay1)
        out+=rect(cx-slot*0.30,ay0-bh,slot*0.60,bh,fill=c,rx=4,sw=0)
        out+=T(cx,ay0+15,lb,9.5,SEC,"700",anchor="middle")
    out+=T(ax0-2,ay1-6,"QM9 R2 error (lower better)",9,TER,"600")
    out+=T(ax0+slot*1.5,ay0-0.30*(ay0-ay1)-8,"same error",9.5,GREEN,"800",anchor="middle")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICLR 2024",14,ACCENT,"800",ls="2")
    b+=T(1216,72,"Provable Expressiveness  ·  Grammar-Built GNN",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,152,"G2N2",46,WHITE,"800")
    b+=T(210,152,"Grammatical Graph Neural Network",21,ACCENT,"800")
    b+=T(64,196,"Weisfeiler and Lehman Go Grammatical",23,TEAL,"800")
    b+=pipefig(1030,168,1.0)
    b+=T(64,242,"J. Piquenot · A. Moscatelli · M. Berar · P. Heroux · J.-Y. Ramel · R. Raveaux · S. Adam",13,SEC,"500")
    b+=T(64,266,"LITIS Lab, University of Rouen Normandy   ·   LIFAT Lab, University of Tours",12.5,TER,"600")
    cw=273; gap=20; x0=64; cy=298; chh=232
    data=[
        (ch[0],ACCENT,"A question of expressiveness",
         "Can we design a graph neural network whose expressive power is guaranteed by construction, rather than proved after the fact?"),
        (ch[1],TEAL,"The answer is a recipe",
         "Instead of a one-off, hand-crafted proof, the authors give a single repeatable recipe."),
        (ch[2],GOLD,"Grammar becomes layers",
         "Take a matrix-language fragment matched to 3-W-L, write it as a context-free grammar, prune it to essential rules, and translate those rules into network layers."),
        (ch[3],GREEN,"Provably 3-WL, and faster",
         "The result is a provably three-W-L graph neural network that is, in practice, both faster and more accurate than its competitors."),
    ]
    for i,(c,col,ti,tx) in enumerate(data):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+42,7,fill=col))
        body+=para(x+44,cy+48,ti,16,TEXT,24,21,"800")[0]
        body+=para(x+24,cy+100,tx,13,SEC,32,19)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,552,1216,552,STROKE,1)
    b+=T(64,588,"arXiv:2303.01590",14,ACCENT,"700")
    b+=T(316,588,"github.com/JPiquenot/Wesfeiler-and-Lehman-go-grammatical",13,SEC,"600")
    b+=T(1216,588,"Expressiveness guaranteed by construction.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Expressiveness proved after the fact")
    # c1 left tall
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"The Weisfeiler-Lehman yardstick",16.5,TEXT,"800")+
        para(92,238,"For years the field has measured a graph network's power on the Weisfeiler-Lehman hierarchy. The gold standard: design a model, then prove it matches, say, the third-order test.",13.5,SEC,42,21)[0]+
        rect(92,368,344,130,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,398,"the usual workflow",12.5,TER,"700")+
        eqbox(112,414,304,"design model  ->  then prove k-WL",12.5,h=40,col=ACCENT)+
        T(112,486,"the proof trails the design",12,SEC,"600"))
    fx=500; fw=716
    # c2 proof is an afterthought
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,110,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,158,6,110,fill=GOLD,rx=6,sw=0)+
        T(fx+28,196,"The proof is an afterthought",16.5,GOLD,"800")+
        para(fx+28,226,"Expressiveness is established after the design, almost as an afterthought, never as the thing that drives the architecture.",14,TEXT,74,22)[0])
    # c3 the missing reverse direction
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,284,fw,158,fill=PANEL,stroke=STROKE)+
        rect(fx,284,6,158,fill=TEAL,rx=6,sw=0)+
        T(fx+28,322,"Missing: the reverse direction",16.5,TEAL,"800")+
        para(fx+28,352,"What has been missing is a systematic way to go the other way: start from a language we already know is exactly as powerful as 3-W-L, and mechanically build a network that inherits that power.",13.5,SEC,64,21)[0]+
        eqbox(fx+28,404,fw-56,"language known = 3-WL   =>   build the network",13,h=30,col=TEAL))
    # c4 every architecture a fresh proof
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,458,fw,92,fill="#3A2020",stroke=RED,rx=14,sw=1.5)+
        rect(fx,458,6,92,fill=RED,rx=6,sw=0)+
        T(fx+28,494,"Otherwise: reinvent the proof each time",15.5,RED,"800")+
        para(fx+28,522,"Without such a recipe, every expressive architecture is a fresh, hand-crafted proof.",13.5,TEXT,86,20)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","A bridge from combinatorics to algebra")
    # c1 left top: WL as MATLANG fragments
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,214,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,214,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"WL tests are MATLANG fragments",16,ACCENT,"800")+
        para(92,224,"A groundbreaking observation: the 1-W-L and 3-W-L tests can each be rewritten as a fragment of a matrix language called MATLANG.",13.5,SEC,60,20)[0]+
        wlladder(92,286,504,74))
    # c2 left bottom: the bridge
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,388,560,162,fill=PANEL,stroke=STROKE)+
        rect(64,388,6,162,fill=TEAL,rx=6,sw=0)+
        T(92,424,"Equal on every sentence",15.5,TEAL,"800")+
        para(92,452,"Two graphs look the same to 3-W-L exactly when every sentence of the fragment ML-of-L-three gives them the same value: a beautiful bridge between combinatorics and algebra. But a bridge is not a road.",13.5,SEC,58,20)[0])
    # c3 right top: only case by case
    rxx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,214,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rxx,158,6,214,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Built only case by case",16,GOLD,"800")+
        para(rxx+28,226,"Turning one of these fragments into an actual, trainable network had been done only case by case, and the resulting models could not claim the full 3-W-L guarantee.",13.5,TEXT,60,20)[0]+
        eqbox(rxx+28,320,rw-56,"hand-built fragment  =>  no full 3-WL claim",13,h=38,col=GOLD))
    # c4 right bottom: pave the road
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,388,rw,162,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rxx,388,6,162,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,424,"Goal: pave the road once",15.5,GREEN,"800")+
        para(rxx+28,452,"The motivation is to replace the case-by-case craft with one general procedure that turns an expressive fragment into a matching network, once and for all.",13.5,TEXT,60,20)[0]+
        T(rxx+28,532,"one procedure  ->  every fragment",13,GREEN,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","One framework, one network")
    cards=[
        (ch[0],ACCENT,"Generic framework","A generic procedure that turns any fragment of an algebraic language into a graph neural network through context-free grammars."),
        (ch[1],TEAL,"G2N2","Run the framework on the ML-of-L-three fragment and out comes G2N2, a network that is provably 3-W-L."),
        (ch[2],GOLD,"Rule set validated","Experiments confirm the grammar reduction keeps expressiveness while trimming redundant rules."),
        (ch[3],GREEN,"Beats prior 3-WL","Across a broad battery of downstream tasks, G2N2 beats existing 3-W-L networks, often while running faster."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    tags=["1","2","3","4"]
    for i,(c,col,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+75,tags[i],26,col,"800",anchor="middle"))
        yy=cy+134
        tlines=wrap(ti,18)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,13.5,SEC,29,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"From an expressive language to a provably expressive network - by construction.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","From operations to grammar to layers")
    # c1 full-width top: ops + exhaustive grammar
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"Move 1: pick the operations, write the grammar",16.5,TEXT,"800")+
        para(92,220,"Start from the operation set L-three, then write an exhaustive grammar whose sentences are exactly the fragment ML-of-L-three.",12.5,SEC,66,18)[0]+
        opset(92,262,700)+
        T(812,262,"exhaustive grammar",11,ACCENT,"800")+
        eqbox(812,278,404,"sentences  =  ML(L3)",12.5,h=26,col=ACCENT))
    # c2 left: reduce, read off network
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,322,560,228,fill=PANEL,stroke=STROKE)+
        rect(64,322,6,228,fill=TEAL,rx=6,sw=0)+
        T(92,358,"Move 2: reduce, then read off the net",15.5,TEAL,"800")+
        para(92,386,"Strip away redundant rules and variables until only the essential productions remain - proving each step keeps the 3-W-L guarantee. The surviving variables become the network inputs; each surviving rule becomes a piece of a layer.",12.5,SEC,62,18)[0]+
        grammar_engine(92,478,504,64))
    # c3 right top: the layer
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,322,rw,160,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rxx,322,6,160,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,354,"Move 3: rules become one layer",15.5,GOLD,"800")+
        para(rxx+28,380,"A layer carries edge memory C and node memory H; linear blocks combine slices, the reduced rules are computed, and two MLPs merge them.",12,TEXT,74,17)[0]+
        layerfig(rxx+28,422,rw-56,52))
    # c4 right bottom: stack -> G2N2
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,494,rw,56,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rxx,494,6,56,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,520,"Stack + equivariant readouts = G2N2",15,GREEN,"800")+
        T(rxx+28,540,"permutation-equivariant readouts on H and on C",11.5,SEC,"600"))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Three very different arenas")
    # c1 full-width top: three arenas + QM9 focus
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"Regression, classification, and a spectral stress test",16,TEXT,"800")+
        arenarow(92,208,700,[("QM9",ACCENT,"regression"),("TUD",GOLD,"classification"),("Spectral",GREEN,"band-pass")])+
        rect(812,208,404,58,fill=PANEL2,stroke=STROKE,rx=10)+
        T(832,232,"QM9: 130K molecules",12.5,ACCENT,"800")+
        T(832,252,"12 targets · R-squared is hardest",11.5,SEC,"600")+
        T(92,296,"together they probe accuracy, generality, and a subtle spectral ability",11.5,SEC,"600"))
    # c2 left: TUD
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,132,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,324,6,132,fill=GOLD,rx=6,sw=0)+
        T(92,360,"TUD: six classic datasets",15.5,GOLD,"800")+
        para(92,388,"From molecules like MUTAG and PTC to social graphs like IMDB.",13,TEXT,60,19)[0]+
        tudrow(92,414,504,["MUTAG","PTC","Proteins","NCI1","IMDB-B","IMDB-M"]))
    # c3 right: spectral
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,324,560,132,fill=PANEL,stroke=STROKE)+
        rect(656,324,6,132,fill=GREEN,rx=6,sw=0)+
        T(684,360,"Spectral stress test",15.5,GREEN,"800")+
        para(684,388,"A node-regression task on nine-hundred-node graphs: can the model act as a band-pass filter?",13,SEC,44,19)[0]+
        T(684,442,"900-node graphs · band-pass target",11.5,GREEN,"700"))
    # c4 full-width callout: probe
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,472,1152,78,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,472,6,78,fill=GREEN,rx=6,sw=0)+
        T(92,504,"One suite for three abilities",15.5,GREEN,"800")+
        stat(560,480,168,62,"accuracy","QM9 regression",ACCENT)+
        stat(742,480,168,62,"generality","TUD classes",GOLD)+
        stat(924,480,168,62,"spectral","band-pass filter",GREEN)+
        T(92,532,"a subtle spectral ability trips up other 3-WL models",12,SEC,"600"))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Dominates in practice")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,194,"Best QM9 error on every target - and faster than PPGN",16.5,GREEN,"800")+
        rect(92,210,640,82,fill=PANEL2,stroke=STROKE,rx=12)+
        para(112,238,"G2N2 does not just match the theory. Learning QM9 targets one at a time, it posts the best error on every single target while training faster than PPGN.",13,SEC,72,20)[0]+
        stat(760,210,214,82,"12 / 12","best QM9 targets",GREEN)+
        stat(994,210,222,82,"faster","than PPGN / epoch",ACCENT))
    # c2 hardest R2
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,368,226,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,226,fill=ACCENT,rx=6,sw=0)+
        T(92,358,"The hardest target: R-squared",14.5,ACCENT,"800")+
        para(92,382,"Error drops to 0.342 where PPGN sits at 3.78 - a ten-fold-plus improvement; the gap widens further when all twelve targets are learned at once.",12.5,SEC,44,18)[0]+
        cmpbars(92,452,312,90,0.342,3.78,"G2N2","PPGN",fmt="{:.3f}",lower_better=True,ratio="~11x lower MAE"))
    # c3 TUD classification
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,324,368,226,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(456,324,6,226,fill=GOLD,rx=6,sw=0)+
        T(484,358,"Graph classification",14.5,GOLD,"800")+
        para(484,382,"On the TUD suite, G2N2 beats the second-best network on five of the six datasets.",12.5,TEXT,46,18)[0]+
        stat(484,444,150,90,"5 / 6","TUD datasets",GOLD)+
        stat(646,444,150,90,"92.5%","MUTAG accuracy",TEAL))
    # c4 spectral
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(848,324,368,226,fill=PANEL,stroke=STROKE)+
        rect(848,324,6,226,fill=GREEN,rx=6,sw=0)+
        T(876,358,"Spectral band-pass",14.5,GREEN,"800")+
        para(876,382,"It cleanly learns band-pass filters where PPGN, starved of memory, essentially fails.",12.5,SEC,46,18)[0]+
        spectralcurve(876,442,312,96))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Grammar reduction keeps the power")
    # c1 left top: compare the grammars
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,214,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,214,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Compare full, intermediate, reduced",15.5,ACCENT,"800")+
        para(92,224,"The key experiment compares the full grammar, an intermediate one, and the reduced grammar r-G-of-L-three on the QM9 R-squared target.",13,SEC,58,19)[0]+
        reductionbars(340,280,264,84))
    # c2 left bottom: same error => only redundancy
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,388,560,162,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,388,6,162,fill=GREEN,rx=6,sw=0)+
        T(92,424,"Same error => only redundancy removed",15,GREEN,"800")+
        para(92,452,"Their errors are essentially the same, which confirms that the reduction throws away redundancy without ever touching expressive power.",13.5,TEXT,58,20)[0])
    # c3 right top: delete essentials => degrade
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,214,fill="#3A2020",stroke=RED,rx=14,sw=1.5)+
        rect(656,158,6,214,fill=RED,rx=6,sw=0)+
        T(684,196,"Delete essentials => it degrades",15.5,RED,"800")+
        para(684,224,"But push past the reduced grammar and start deleting essential rules, and performance degrades in a clear, measurable way.",13.5,TEXT,58,20)[0]+
        eqbox(684,312,504,"remove essential rule  ->  error rises",13,h=40,col=RED))
    # c4 right bottom: degradation is useful
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,388,560,162,fill=PANEL,stroke=STROKE)+
        rect(656,388,6,162,fill=VIOLET,rx=6,sw=0)+
        T(684,424,"Degradation is useful signal",15.5,VIOLET,"800")+
        para(684,452,"That degradation is information: it shows how much each operation contributes, so you can prune the model deliberately when a task does not demand full 3-W-L strength.",13.5,SEC,60,20)[0])
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The gains, in numbers")
    # c1 full-width strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,110,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,166,6,110,fill=GREEN,rx=6,sw=0)+
        T(92,202,"A few numbers capture the impact",16.5,GREEN,"800")+
        stat(560,196,214,58,"~11x","lower QM9 R2 error",GREEN)+
        rect(792,196,424,58,fill=PANEL2,stroke=STROKE,rx=12)+
        para(812,222,"Provable 3-WL power turns into concrete wins across regression, classification, and spectral tasks.",12.5,SEC,58,18)[0])
    # c2 QM9 R2 + epoch time
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,300,368,164,fill=PANEL,stroke=STROKE)+
        rect(64,300,6,164,fill=ACCENT,rx=6,sw=0)+
        T(92,332,"QM9 R-squared target",14.5,ACCENT,"800")+
        cmpbars(92,344,180,110,0.342,3.78,"G2N2","PPGN",fmt="{:.3f}",lower_better=True)+
        cmpbars(288,344,132,110,98,129,"G2N2","PPGN",fmt="{:.0f}s",lower_better=True))
    # c3 spectral band-pass
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,300,368,164,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(456,300,6,164,fill=GREEN,rx=6,sw=0)+
        T(484,332,"Spectral band-pass R-squared",14.5,GREEN,"800")+
        cmpbars(484,344,312,110,0.82,0.10,"G2N2","PPGN",fmt="{:.2f}",lower_better=False,ratio="8x higher R2"))
    # c4 TUD
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(848,300,368,164,fill=PANEL,stroke=STROKE)+
        rect(848,300,6,164,fill=GOLD,rx=6,sw=0)+
        T(876,332,"TUD classification",14.5,GOLD,"800")+
        T(876,354,"better than 2nd place",11.5,SEC,"600")+
        stat(876,368,150,84,"5 / 6","datasets",GOLD)+
        stat(1038,368,150,84,"92.5%","MUTAG",TEAL))
    # footer scope strip
    b+=rect(64,480,1152,70,fill=PANEL2,stroke=STROKE,rx=12)
    b+=T(92,510,"Measured across",13.5,SEC,"600")
    b+=T(230,510,"QM9 (12 targets)  ·  TUD (6 sets)  ·  spectral (900-node)",14,TEXT,"800",ff=MONO)
    b+=T(1192,510,"lower error / higher R2 is better",13.5,GREEN,"800",anchor="end")
    b+=T(1192,534,"G2N2 wins on every arena",12,TER,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Expressiveness by construction")
    # c1 full-width lead strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,74,fill=PANEL,stroke=STROKE)+
        rect(64,166,6,74,fill=ACCENT,rx=6,sw=0)+
        T(92,198,"The lasting message is a change of workflow",17,TEXT,"800")+
        T(92,224,"stop proving expressiveness after the fact - build it in from the start",13,SEC,"600"))
    cards=[
        (ch[1],TEAL,"Read the network off the grammar","Start from a language whose expressive power you already know, reduce it to a clean grammar, and read the network's inputs and layers straight off the surviving rules."),
        (ch[2],GREEN,"G2N2 is the payoff","G2N2 is the concrete result: a provably 3-W-L model that is also faster and more accurate than its predecessors."),
        (ch[3],GOLD,"A generic route","Because the framework is generic, the same grammatical route could turn other algebraic fragments into other networks, each carrying its expressive power by design."),
    ]
    cw=368; gap=24; x0=64; cy=264; chh=278
    for i,(c,col,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+34,cy+52,11,fill=col))
        yy=cy+96
        for j,ln in enumerate(wrap(ti,26)):
            body+=T(x+28,yy+j*24,ln,17,TEXT,"800")
        yy+=24*len(wrap(ti,26))+14
        body+=para(x+28,yy,tx,13.5,SEC,34,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,560,1216,560,STROKE,1)
    b+=pipefig(150,616,0.44)
    b+=T(1216,620,"G2N2  ·  Weisfeiler and Lehman Go Grammatical  ·  ICLR 2024",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
