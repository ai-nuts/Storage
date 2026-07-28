#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 024
(RNA-Protein Interaction Classification via Sequence Embeddings - RPIembeddor / RNAInterAct, ICLR 2024).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card with a
<title> holding the cue keywords, so the strict --require-pptx-anchors cue pass resolves every
anchor from PPTX geometry. Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: a TEAL RNA strand (nucleotide beads) meeting an ACCENT protein chain (residue
nodes) at a binding site - sequence-only prediction of whether RNA and protein interact.
Green = RPIembeddor / positive signal, red = baselines / collapse."""
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
    p=" ".join(f"{x},{y}" for x,y in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{d}/>'

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
def rna_strand(x,y,w,color=TEAL,beads=9,amp=8,sw=2.6):
    """A wavy single-strand RNA with nucleotide beads."""
    pts=[]
    for i in range(41):
        t=i/40.0
        pts.append((x+t*w, y+math.sin(t*math.pi*3.0)*amp))
    out=poly(pts,stroke=color,sw=sw)
    for i in range(beads):
        t=(i+0.5)/beads
        out+=circle(x+t*w, y+math.sin(t*math.pi*3.0)*amp, 3.1, fill=color)
    return out

def protein_chain(x,y,w,color=ACCENT,nodes=7,amp=9,sw=2.6):
    """A folded protein backbone: zig-zag with residue nodes."""
    pts=[]
    for i in range(nodes):
        t=i/(nodes-1)
        pts.append((x+t*w, y+(amp if i%2 else -amp)))
    out=poly(pts,stroke=color,sw=sw)
    for px,py in pts:
        out+=circle(px,py,4.4,fill=PANEL2,stroke=color,sw=2)
    return out

def binding_glyph(x,y,w,rna_col=TEAL,prot_col=ACCENT):
    """RNA strand (top) meeting a protein chain (bottom) at a binding site."""
    out=rna_strand(x,y,w,rna_col,beads=9,amp=7)
    out+=protein_chain(x,y+40,w,prot_col,nodes=7,amp=8)
    # binding link at the center
    cx=x+w*0.5
    out+=line(cx,y+8,cx,y+32,GOLD,2.2,dash="3 3")
    out+=circle(cx,y+20,4.0,fill=GOLD)
    return out

def interact_pill(x,y,pos=True,w=150,h=30):
    """A small pill showing an interaction verdict."""
    col=GREEN if pos else RED
    txt="interact" if pos else "no interact"
    return (rect(x,y,w,h,fill=PANEL2,stroke=col,rx=15,sw=1.5)+
            circle(x+16,y+h/2,5,fill=col)+
            T(x+30,y+h/2+5,txt,13,col,"800"))

def roccurve(x,y,w,h):
    """Small ROC inset: RPIembeddor (green, AUC 0.70) above the diagonal,
    baseline (red, AUC ~0.5) on the diagonal."""
    out=rect(x,y,w,h,fill="#0E2334",stroke=STROKE,rx=8)
    ax0=x+16; ax1=x+w-12; ay0=y+h-16; ay1=y+14
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    out+=line(ax0,ay0,ax1,ay1,RED,1.8,dash="4 4")   # chance diagonal
    good=[]
    for i in range(0,101,5):
        t=i/100.0
        # concave curve bowing toward top-left (AUC ~0.70)
        gv=1-(1-t)**1.9
        good.append((ax0+t*(ax1-ax0), ay0-gv*(ay0-ay1)))
    out+=poly(good,stroke=GREEN,sw=2.6)
    out+=T(ax1-2,ay1+4,"AUC .70",10.5,GREEN,"800",anchor="end")
    out+=T(ax1-2,ay0-4,"chance",10.5,RED,"700",anchor="end")
    out+=T(ax0+2,ay0+13,"FPR ->",10,TER,"600")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"ICLR 2024",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"University of Freiburg  ·  ELLIS Institute Tuebingen  ·  Sequence-only RPI",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"RNA-Protein Interaction Classification",42,WHITE,"800")
    b+=T(64,198,"via Sequence Embeddings   —   RPIembeddor  +  RNAInterAct",24,ACCENT,"800")
    # RNA strand meets protein chain motif near the title
    b+=binding_glyph(946,140,236)
    b+=T(1064,214,"RNA  x  protein  ->  interact?",12,TER,"600",anchor="middle")
    b+=T(64,236,"D. Matus  ·  F. Runge  ·  J. Franke  ·  L. Gerne  ·  M. Uhl  ·  F. Hutter  ·  R. Backofen",14.5,SEC,"500")
    # three concept cards in a row = anchors (title has 3 chunks)
    cw=373; gap=18; x0=64; cy=296; chh=232
    data=[
        (ch[0],RED,x0,"Slow to measure",
         "RNA-protein interactions drive gene regulation, but measuring them in the lab is slow and costly, and existing predictors lean on small, protein-specific datasets.",
         "lab assay"),
        (ch[1],ACCENT,x0+cw+gap,"A dataset + a model",
         "This work releases RNAInterAct, a large curated set of non-coding RNA-protein interactions, and RPIembeddor, a transformer that classifies any RNA-protein pair from sequence alone.",
         "RNAInterAct + RPIembeddor"),
        (ch[2],GREEN,x0+2*(cw+gap),"Two foundation models",
         "Feeding embeddings from RNA-FM for RNA and ESM-2 for proteins into an attention network beats prior state of the art and generalizes to unseen RNA families.",
         "RNA-FM + ESM-2"),
    ]
    for c,col,x,ti,tx,tag in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              T(x+24,cy+48,ti,18,TEXT,"800")+
              para(x+24,cy+82,tx,13.5,SEC,50,20)[0])
        body+=chip(x+24,cy+chh-44,tag,col,w=cw-48,h=30)
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,560,1216,560,STROKE,1)
    b+=T(64,596,"biorxiv.org/content/10.1101/2024.11.08.622607",13.5,ACCENT,"700")
    b+=T(1216,596,"Decide if any RNA and protein interact, from sequence alone.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","No general predictor from sequence alone")
    # c1 left tall: ncRNAs act through protein partners, mapping is slow
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"ncRNAs act through proteins",18,TEXT,"800")+
        para(92,240,"Non-coding RNAs regulate the cell largely through their interactions with proteins, but mapping these interactions experimentally is slow and costly.",14.5,SEC,42,23)[0]+
        rect(92,356,344,150,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,384,"an RNA-protein binding pair",12.5,TER,"700")+
        binding_glyph(112,420,304)+
        T(244,502,"SELEX / CLIP-seq: expensive",11.5,TER,"600",anchor="middle"))
    # right column, three stacked
    fx=500; fw=716
    # c2 one model per protein needs large per-protein data
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"Today: one model per protein",16.5,RED,"800")+
        para(fx+28,226,"Most computational predictors sidestep the general problem by training a separate model for each protein, which needs a large interaction dataset for that specific protein.",14,SEC,58,21)[0]+
        chip(fx+28,278,"protein A -> model A     protein B -> model B     ...",RED,w=fw-56,h=26))
    # c3 datasets exist for only a few hundred RBPs
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,104,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,324,6,104,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"Data covers only a few hundred",16,GOLD,"800")+
        para(fx+28,392,"Such datasets exist for only a few hundred of the roughly two thousand human RNA-binding proteins.",14.5,TEXT,74,22)[0])
    # c4 what is missing (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,444,fw,106,fill=PANEL,stroke=STROKE)+
        rect(fx,444,6,106,fill=TEAL,rx=6,sw=0)+
        T(fx+28,482,"Missing: decide any pair, any sequence",16,TEAL,"800")+
        para(fx+28,512,"What is missing is a method that decides, for any RNA and protein pair, whether they interact using nothing but their sequences.",14.5,SEC,74,22)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Learn across tasks, stand on foundation models")
    # c1 left top: two useful ideas
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,192,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,192,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Two ideas point the way",16.5,ACCENT,"800")+
        para(92,226,"Recent progress suggests two useful ideas that together enable a broad, sequence-only predictor of RNA-protein interaction.",14,SEC,58,21)[0]+
        chip(92,300,"idea 1: learn across many tasks",TEAL,w=248,h=34)+
        chip(348,300,"idea 2: foundation models",GREEN,w=248,h=34))
    # c2 left bottom: learn across many tasks
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,560,184,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,366,6,184,fill=TEAL,rx=6,sw=0)+
        T(92,404,"Learn across many tasks",16,TEAL,"800")+
        para(92,434,"Learning across many interaction types at once, rather than one protein at a time, helps precisely when labeled data is scarce.",14,TEXT,58,21)[0]+
        chip(92,504,"many proteins  ->  one shared model",TEAL,w=468,h=30))
    # c3 right top: foundation models capture hidden signal
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,192,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,192,fill=GREEN,rx=6,sw=0)+
        T(rx+28,196,"Foundation models expose signal",16.5,GREEN,"800")+
        para(rx+28,226,"Foundation models trained on huge unlabeled biological corpora capture structural and functional signal that raw sequences do not expose directly.",14,SEC,56,21)[0]+
        T(rx+28,318,"AUGC... -> RNA-FM -> rich embedding",13.5,GREEN,"800",ff=MONO))
    # c4 right bottom: combine (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,366,rw,184,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rx,366,6,184,fill=GOLD,rx=6,sw=0)+
        T(rx+28,404,"Combine: general rules, unseen types",16,GOLD,"800")+
        para(rx+28,434,"Combined, a single model can learn general rules of RNA-protein binding and apply them to interaction types it has never seen.",14,TEXT,58,21)[0]+
        T(rx+28,522,"general binding rules  ->  unseen RNA families",13.5,GOLD,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","A dataset, a model, and an ablation")
    cards=[
        (ch[0],ACCENT,"Three contributions","One curated dataset, one sequence-only classifier, and an ablation that pins down why it works."),
        (ch[1],TEAL,"1  RNAInterAct","An extensive dataset of non-coding RNA-protein interactions from the RNAInter database, enriched with carefully generated negatives."),
        (ch[2],GREEN,"2  RPIembeddor","A transformer that classifies interactions from sequence embeddings, beating existing tools while generalizing to new data."),
        (ch[3],GOLD,"3  Ablation","It shows the two foundation-model embeddings are not optional add-ons but the core of the model's ability to classify."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    tags=["3x","DB","NET","+/-"]
    for i,(c,col,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+74,tags[i],(17 if i in (1,) else 18),col,"800",anchor="middle"))
        yy=cy+134
        tlines=wrap(ti,18)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,14,SEC,30,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"Build the benchmark, build the model, and prove the embeddings are what make it work.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Two embeddings, symmetric attention, one probability")
    lx=64; lw=568
    # c1 two pre-trained foundation models
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,204,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,204,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"Embed with two foundation models",16.5,ACCENT,"800")+
        para(lx+28,224,"RNA sequences are embedded with RNA-FM, trained on 23M non-coding RNAs; proteins with ESM-2, which predicts folding without multiple sequence alignments.",13.5,SEC,60,20)[0]+
        eqbox(lx+28,304,lw-56,"RNA -> RNA-FM;   protein -> ESM-2 (150M)",13))
    # c2 both N x 640, two parallel FF normalize
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,378,lw,172,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(lx,378,6,172,fill=TEAL,rx=6,sw=0)+
        T(lx+28,416,"Normalize both to a shared size",16,TEAL,"800")+
        para(lx+28,444,"Both produce embeddings of size N by 640. Two parallel feed-forward layers normalize their sizes before the encoders.",13.5,TEXT,60,20)[0]+
        eqbox(lx+28,506,lw-56,"RNA-FM, ESM-2  ->  [N x 640]  -> FF norm",13))
    rxx=656; rw=560
    # c3 symmetric encoder attention
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,204,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,204,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"Process both symmetrically",16.5,GOLD,"800")+
        para(rxx+28,224,"Encoder layers process the RNA and protein embeddings symmetrically, so attention can focus on the parts of each sequence most relevant to interaction and each modality has equal influence.",13.5,SEC,58,20)[0]+
        T(rxx+28,336,"attention over RNA <-> protein positions",13.5,GOLD,"800",ff=MONO))
    # c4 concat -> FF -> sigmoid, 1.4M params (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,378,rw,172,fill=PANEL,stroke=STROKE)+
        rect(rxx,378,6,172,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,416,"Concatenate, then a sigmoid head",16,GREEN,"800")+
        para(rxx+28,444,"Latent representations are concatenated, passed through feed-forward layers, and a linear layer with sigmoid outputs the interaction probability. Just 1.4M parameters.",13.5,TEXT,58,20)[0]+
        eqbox(rxx+28,510,rw-56,"p = sigmoid(W h + b)   |   1.4M params",13))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","RNAInterAct: curated, homology-split")
    # c1 pipeline strip: RNAInter -> sequences -> families
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,132,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,132,fill=ACCENT,rx=6,sw=0)+
        T(92,194,"Built from RNAInter, sequences and families recovered",16,TEXT,"800")+
        _seqchip(112,222,"RNAInter","47M interactions",ACCENT)+
        T(320,250,"->",22,SEC,"800",anchor="middle")+
        _seqchip(348,222,"NCBI / UniProt / Ensembl","sequences",TEAL)+
        T(632,250,"->",22,SEC,"800",anchor="middle")+
        _seqchip(660,222,"Rfam / Pfam","families + clans",GREEN,w=232))
    # c2 biologically meaningful negatives
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,306,560,140,fill=PANEL,stroke=STROKE)+
        rect(64,306,6,140,fill=GREEN,rx=6,sw=0)+
        T(92,342,"Biologically meaningful negatives",16.5,GREEN,"800")+
        para(92,372,"Family and clan annotations let the authors generate negatives that are biologically plausible rather than random.",14,SEC,58,21)[0])
    # c3 122k interactions, 1:2 ratio
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,306,560,140,fill=PANEL,stroke=STROKE)+
        rect(656,306,6,140,fill=TEAL,rx=6,sw=0)+
        T(684,342,"122,217 interactions",16.5,TEAL,"800")+
        stat(684,364,164,72,"122K","interactions",TEAL)+
        stat(864,364,164,72,"1:2","pos : neg",ACCENT)+
        stat(1044,364,144,72,"976","RNA families",GREEN))
    # c4 homology-aware split + external test (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,462,1152,88,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,462,6,88,fill=GOLD,rx=6,sw=0)+
        T(92,498,"Split by RNA family",16,GOLD,"800")+
        para(300,498,"No family appears in both train and test (TRinter / TSfam), and models are also tested on external RPI2825, so the benchmark rewards generalization, not memorization.",14,TEXT,108,23)[0])
    return svg(b)

def _seqchip(x,y,name,tag,col,w=196,h=52):
    return (rect(x,y,w,h,fill=PANEL2,stroke=col,rx=10,sw=1.5)+
            rect(x,y,5,h,fill=col,rx=2,sw=0)+
            T(x+16,y+24,name,13.5,TEXT,"800")+
            T(x+16,y+42,tag,11.5,TER,"600"))

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Real signal where baselines hit chance")
    # c1 headline strip: F1 0.59, acc 0.67 on hardest split
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,152,1152,140,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,152,6,140,fill=GREEN,rx=6,sw=0)+
        T(92,188,"On TSfam, where no RNA family overlaps training",16.5,GREEN,"800")+
        stat(92,204,220,74,"0.586","F1 on TSfam",GREEN)+
        stat(332,204,220,74,"0.667","accuracy",TEAL)+
        roccurve(576,204,300,74)+
        rect(900,204,300,74,fill=PANEL2,stroke=STROKE,rx=12)+
        para(920,232,"Best of all methods on the homology-separated test set.",13,SEC,42,20)[0])
    # c2 ROC AUC 0.70 vs competitors at chance (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,308,560,210,fill=PANEL,stroke=STROKE)+
        rect(64,308,6,210,fill=ACCENT,rx=6,sw=0)+
        T(92,344,"AUC 0.70 vs baselines at chance",16,ACCENT,"800")+
        para(92,372,"Its ROC area under the curve is 0.70, while XRPI and IPMiner sit at 0.48 and 0.50, essentially chance.",13.5,SEC,58,20)[0]+
        bar(300,428,250,0.70,1.0,GREEN,"RPIembeddor","0.70",h=22)+
        bar(300,456,250,0.50,1.0,GOLD,"IPMiner","0.50",h=22)+
        bar(300,484,250,0.48,1.0,RED,"XRPI","0.48",h=22))
    # c3 concrete counts (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,308,560,210,fill=PANEL,stroke=STROKE)+
        rect(656,308,6,210,fill=GOLD,rx=6,sw=0)+
        T(684,344,"Concretely, it separates the classes",16,GOLD,"800")+
        para(684,372,"RPIembeddor correctly labels nearly 3,000 positive interactions and over 5,000 negatives, whereas XRPI predicts almost everything as interacting.",13.5,SEC,58,20)[0]+
        stat(684,452,164,58,"2,971","true positives",GREEN)+
        stat(864,452,164,58,"5,586","true negatives",TEAL)+
        stat(1044,452,144,58,"~91%","XRPI all-pos",RED))
    # c4 learns real signal (footer strip)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,534,1152,64,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,534,6,64,fill=GOLD,rx=6,sw=0)+
        T(92,562,"The verdict",15.5,GOLD,"800")+
        T(210,562,"The model clearly learns real signal that generalizes to unseen RNA families,",13.5,TEXT,"600")+
        T(210,584,"rather than memorizing the families it trained on.",13.5,SEC,"600"))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Both embeddings are the model")
    # c1 setup (left top)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Swap the embeddings out",16.5,ACCENT,"800")+
        para(92,226,"To test whether the two embeddings really matter, the authors retrain after replacing the RNA embedding, the protein embedding, or both, with random vectors or one-hot encodings.",14,SEC,56,21)[0])
    # c2 every variant collapses (left bottom)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,226,fill="#2A1A1A",stroke=RED,rx=14,sw=1.5)+
        rect(64,324,6,226,fill=RED,rx=6,sw=0)+
        T(92,362,"Every variant collapses",16.5,RED,"800")+
        para(92,392,"In every one of these variants the model stops working, predicting only the negative class: F1 falls to zero and accuracy merely reflects the fraction of negatives.",14,TEXT,56,21)[0]+
        bar(300,472,250,0.0,0.7,RED,"F1 (ablated)","0.00",h=24)+
        bar(300,506,250,0.624,1.0,GOLD,"accuracy","0.624 = neg frac",h=24))
    # c3 full model works (right top)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,158,6,150,fill=GREEN,rx=6,sw=0)+
        T(684,196,"Only both together classify",16,GREEN,"800")+
        para(684,226,"Only when both the RNA-FM and ESM-2 embeddings are present does the model classify correctly, at F1 0.605 and accuracy 0.678.",14,TEXT,56,21)[0]+
        chip(684,268,"RNA-FM  +  ESM-2  ->  F1 0.605 / acc 0.678",GREEN,w=504,h=28))
    # c4 what it means (right bottom)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(656,324,6,226,fill=TEAL,rx=6,sw=0)+
        T(684,362,"The embeddings carry the signal",16.5,TEAL,"800")+
        para(684,392,"This confirms the foundation-model embeddings carry the structural and functional information the task depends on; neither can be dropped or simplified.",14,SEC,56,21)[0]+
        chip(684,468,"random / one-hot  ->  breaks the model",RED,w=504,h=30)+
        chip(684,506,"RNA-FM + ESM-2  ->  essential, not add-ons",TEAL,w=504,h=30))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in one place")
    # c1 AUC 0.70 vs 0.50 (big strip)
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,132,fill=PANEL,stroke=STROKE)+
        rect(64,166,6,132,fill=GREEN,rx=6,sw=0)+
        T(92,202,"ROC AUC on the homology-separated test set",16.5,GREEN,"800")+
        stat(92,220,250,66,"0.70","RPIembeddor AUC",GREEN)+
        stat(360,220,250,66,"0.50","best competitor",RED)+
        rect(630,220,586,66,fill=PANEL2,stroke=STROKE,rx=12)+
        para(650,248,"Real generalization to unseen RNA families, where prior tools land at chance.",13.5,SEC,74,20)[0])
    # c2 F1 and accuracy lead (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,314,560,150,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,314,6,150,fill=GREEN,rx=6,sw=0)+
        T(92,352,"Best F1 and accuracy",16.5,GREEN,"800")+
        stat(92,368,220,80,"0.586","F1 on TSfam",GREEN)+
        stat(332,368,228,80,"0.667","accuracy",TEAL))
    # c3 dataset scale (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,314,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,314,6,150,fill=ACCENT,rx=6,sw=0)+
        T(684,352,"RNAInterAct scale",16.5,ACCENT,"800")+
        stat(684,368,250,80,"122K","interactions",ACCENT)+
        stat(958,368,250,80,"976","RNA families",TEAL))
    # c4 compact model on two foundation models (bottom strip)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,480,1152,70,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,480,6,70,fill=GOLD,rx=6,sw=0)+
        T(92,510,"A compact model, big backbones",15.5,GOLD,"800")+
        T(92,534,"All of it runs in a small attention network on two foundation models.",13.5,SEC,"600")+
        eqbox(792,492,424,"1.4M params  |  RNA-FM + ESM-2",14,h=46))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Sequence-only, general, and reproducible")
    cards=[
        (ch[0],ACCENT,"General prediction is achievable","General RNA-protein interaction prediction from sequence alone is achievable when you stand on the shoulders of foundation models."),
        (ch[1],GREEN,"Small net beats specialists","A compact attention network fed RNA-FM and ESM-2 embeddings outperforms specialized tools and, unlike them, generalizes to RNA families it has never seen."),
        (ch[2],TEAL,"A fair, homology-aware benchmark","The companion RNAInterAct dataset, split to remove homology bias, gives the community a fair benchmark to drive further progress."),
        (ch[3],GOLD,"Both embeddings, then structure next","Both embeddings are essential, and the authors point toward adding RNA-structure models and longer sequences next."),
    ]
    y=170
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,86,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,86,fill=col,rx=6,sw=0)+
              circle(108,y+43,9,fill=col)+
              T(140,y+34,ti,17.5,TEXT,"800"))
        body+=para(140,y+62,tx,14,SEC,110,20)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=98
    b+=line(64,584,1216,584,STROKE,1)
    b+=binding_glyph(64,600,200)
    b+=T(1216,624,"RPIembeddor  ·  RNAInterAct  ·  RNA-Protein Interaction from Sequence  ·  ICLR 2024",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
