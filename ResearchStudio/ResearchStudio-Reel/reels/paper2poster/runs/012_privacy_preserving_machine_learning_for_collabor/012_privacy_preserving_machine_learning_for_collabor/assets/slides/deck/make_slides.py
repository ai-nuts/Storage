#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 012
(Privacy-Preserving Machine Learning for Collaborative Data Sharing via
Auto-encoder Latent Space Embeddings, NeurIPS 2022).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_..."> card
with a <title> holding the cue keywords, so the strict --require-pptx-anchors cue pass
resolves every anchor from PPTX geometry. Zero <image>, zero gradients, ASCII mono equations.
Theme motif: an autoencoder hourglass N->M->N whose bottleneck z is a locked, obfuscated
latent embedding two peers share instead of their raw features."""
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

def polygon(pts,fill=PANEL2,stroke=None,sw=1.5,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o=f' opacity="{opacity}"' if opacity is not None else ""
    p=" ".join(f"{x},{y}" for x,y in pts)
    return f'<polygon points="{p}" fill="{fill}"{st}{o}/>'

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
            T(x-12,y+h*0.70+2,label,13,lblcolor,"600",anchor="end")+
            T(x+bw+10,y+h*0.70+2,valtxt,13,color,"800"))

def stat(x,y,w,h,num,lbl,col):
    ns=min(30,h*0.36)
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=12)+
            T(x+w/2,y+h*0.52,num,ns,col,"800",anchor="middle")+
            T(x+w/2,y+h*0.82,lbl,12,SEC,"600",anchor="middle"))

def chip(x,y,text,col,w=512,h=34):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            circle(x+18,y+h/2,5,fill=col)+
            T(x+34,y+h/2+6,text,14,TEXT,"600"))

def eqbox(x,y,w,expr,size=16,h=44):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=8)+
            T(x+w/2,y+h/2+6,expr,size,TEXT,"800",anchor="middle",ff=MONO))

# ---- theme glyphs -------------------------------------------------------
def lock(x,y,s=16,col=TEAL):
    """Small padlock, top-left at (x,y). Body s wide, shackle above."""
    bx=x; by=y+s*0.42; bw=s; bh=s*0.62
    body=rect(bx,by,bw,bh,fill=col,rx=2.5,sw=0)
    shackle=(f'<path d="M {bx+s*0.24} {by} v -{s*0.24} '
             f'a {s*0.26} {s*0.26} 0 0 1 {s*0.52} 0 v {s*0.24}" '
             f'fill="none" stroke="{col}" stroke-width="2.2"/>')
    hole=circle(bx+bw/2,by+bh*0.5,s*0.11,fill=BG)
    return shackle+body+hole

def aefunnel(x,y,w,h,col=ACCENT,zcol=TEAL,locked=True,labels=True):
    """Autoencoder hourglass: encoder trapezoid narrows N->M, decoder widens M->N,
    bottleneck latent z highlighted (optionally locked). Fits inside (x,y,w,h)."""
    cx=x+w/2; midh=max(10,h*0.16); top=y; bot=y+h
    zt=y+h/2-midh/2; zb=y+h/2+midh/2
    out=polygon([(x,top),(cx-8,zt),(cx-8,zb),(x,bot)],fill="#123049",stroke=col,sw=1.6)
    out+=polygon([(x+w,top),(cx+8,zt),(cx+8,zb),(x+w,bot)],fill="#123049",stroke=col,sw=1.6)
    out+=rect(cx-8,zt,16,midh,fill=zcol,rx=3,sw=0)
    if locked:
        out+=lock(cx-8,zt-24,15,zcol)
    if labels:
        out+=T(x,bot+15,"N",12.5,SEC,"800",anchor="middle")
        out+=T(x+w,bot+15,"N",12.5,SEC,"800",anchor="middle")
        out+=T(cx,zb+15,"z (M)",11.5,zcol,"800",anchor="middle")
        out+=T(x+w*0.27,top-6,"encoder f",10.5,TER,"700",anchor="middle")
        out+=T(x+w*0.73,top-6,"decoder g",10.5,TER,"700",anchor="middle")
    return out

def peerbox(x,y,w,h,label,col,rows):
    out=rect(x,y,w,h,fill=PANEL2,stroke=col,rx=10,sw=1.5)+rect(x,y,5,h,fill=col,rx=2,sw=0)
    out+=T(x+16,y+22,label,13.5,TEXT,"800")
    for i,r in enumerate(rows):
        out+=T(x+16,y+42+i*16,r,11,SEC,"600")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"NeurIPS 2022",14,ACCENT,"800",ls="3")
    b+=T(1216,72,"Los Andes University  ·  Rappi  ·  Amazon",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"Privacy-Preserving Machine Learning",40,WHITE,"800")
    b+=T(64,196,"for Collaborative Data Sharing",40,WHITE,"800")
    b+=T(64,238,"via Auto-encoder Latent Space Embeddings",22,ACCENT,"800")
    # autoencoder motif near title, right
    b+=aefunnel(958,132,224,96,col=ACCENT,zcol=TEAL)
    b+=T(64,272,"Ana Maria Quintero Ossa  ·  Jesus Solano  ·  Hernan Garcia  ·  David Zarruk  ·  Alejandro Correa-Bahnsen  ·  Carlos Valencia",13.5,SEC,"500")
    # four concept cards in a row = anchors
    cw=276; gap=16; x0=64; cy=300; chh=228
    data=[
        (ch[0],GOLD,x0,"Pooling data is blocked",
         "Organizations want to pool data for better models, but privacy and IP laws make raw sharing impossible."),
        (ch[1],ACCENT,x0+cw+gap,"Autoencoder embeddings",
         "A framework uses autoencoders to turn sensitive tabular data into obfuscated latent-space embeddings."),
        (ch[2],TEAL,x0+2*(cw+gap),"Share codes, not features",
         "Peers share only these encoded representations, then join them to train a shared downstream model."),
        (ch[3],GREEN,x0+3*(cw+gap),"Under 10 pp drop",
         "Across three public benchmarks, encoded data preserves predictive power while the raw features stay hidden."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0))
        if col==TEAL:
            body+=aefunnel(x+26,cy+34,120,52,col=col,zcol=TEAL,labels=False)
        elif col==GREEN:
            body+=T(x+24,cy+72,"< 10 pp",30,GREEN,"800")
        elif col==ACCENT:
            body+=lock(x+26,cy+38,26,ACCENT)
        else:
            body+=T(x+24,cy+72,"raw  ✕",26,GOLD,"800")
        body+=para(x+24,cy+112,ti,17,TEXT,26,22,"800")[0]
        body+=para(x+24,cy+162,tx,12.5,SEC,34,18)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,562,1216,562,STROKE,1)
    b+=T(64,598,"arXiv:2211.05717",14,ACCENT,"700")
    b+=T(1216,598,"Share the latent embedding, keep the raw data private.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Complementary data that cannot be combined")
    # c1 left tall: two peers, same users, different variables
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"Two peers, one user base",18,TEXT,"800")+
        para(92,240,"Two companies each hold a different set of variables about the same users. Combining features would predict a shared target far more accurately.",14,SEC,42,22)[0]+
        peerbox(92,350,168,110,"Peer A",TEAL,["age, income,","spend history,","location ..."])+
        peerbox(268,350,168,110,"Peer B",GOLD,["app usage,","device, tenure,","credit ..."])+
        T(264,494,"same users  ->  richer target prediction",12.5,SEC,"700",anchor="middle"))
    # right column, three stacked
    fx=500; fw=716
    # c2 sensitive: laws forbid raw sharing
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=RED,rx=6,sw=0)+
        T(fx+28,196,"But the raw data is sensitive",16.5,RED,"800")+
        para(fx+28,226,"Privacy policies and intellectual property laws forbid handing over the raw features, even when the channel between peers is secure.",14,SEC,64,21)[0]+
        T(fx+28,296,"secure channel is not enough  ->  raw features stay locked away",13,RED,"800",ff=MONO))
    # c3 collaboration cancelled (callout)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,104,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,324,6,104,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"So the collaboration is cancelled",16,GOLD,"800")+
        para(fx+28,392,"Without a way to share, the partnership stops and the potential boost in model performance is lost.",14.5,TEXT,74,22)[0])
    # c4 core question
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,444,fw,106,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(fx,444,6,106,fill=TEAL,rx=6,sw=0)+
        T(fx+28,482,"The core question",16,TEAL,"800")+
        para(fx+28,512,"How can peers share their information and keep the predictive power of the original features, without ever exposing the raw data?",14.5,TEXT,74,22)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Existing privacy tools each fall short")
    # c1 left top: encryption strong but heavy
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,192,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,192,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Encryption: strong but heavy",16.5,ACCENT,"800")+
        para(92,226,"Encryption approaches like homomorphic encryption offer strong security, yet are hard to deploy in real settings because of their technology requirements.",14,SEC,58,21)[0]+
        eqbox(92,308,504,"strong security  vs  hard, costly deployment",13.5,h=30))
    # c2 left bottom: federated learning assumes same features
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,366,560,184,fill=PANEL,stroke=STROKE)+
        rect(64,366,6,184,fill=RED,rx=6,sw=0)+
        T(92,404,"Federated learning: same features only",15.5,RED,"800")+
        para(92,434,"Federated learning decentralizes training across devices, but assumes every peer holds the same kind of information, so it cannot handle peers with different features.",14,SEC,58,21)[0]+
        T(92,528,"different feature sets  ->  federated setup breaks",13,RED,"800",ff=MONO))
    # c3 right top: DP + PCA distort
    rx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rx,158,rw,192,fill=PANEL,stroke=STROKE)+
        rect(rx,158,6,192,fill=GOLD,rx=6,sw=0)+
        T(rx+28,196,"Noise and linear projection distort",16,GOLD,"800")+
        para(rx+28,226,"Differential privacy masks values by adding noise, which can significantly reduce data utility.",14,SEC,56,21)[0]+
        chip(rx+28,272,"Differential privacy: noise cuts utility",GOLD,w=rw-56,h=30)+
        chip(rx+28,308,"PCA: linear, loses nonlinear relationships",GOLD,w=rw-56,h=30))
    # c4 right bottom: deep representation learning (callout)
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rx,366,rw,184,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(rx,366,6,184,fill=TEAL,rx=6,sw=0)+
        T(rx+28,404,"The opening: deep representations",16,TEAL,"800")+
        para(rx+28,434,"These gaps motivate a new approach: use deep representation learning to encode the data while keeping its predictive structure intact.",14,TEXT,56,21)[0]+
        aefunnel(rx+28,506,150,40,col=TEAL,zcol=TEAL,locked=False,labels=False)+
        T(rx+196,530,"nonlinear encoder preserves structure",13,TEAL,"800"))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","One survey, one framework, broad tests")
    cards=[
        (ch[0],ACCENT,"3","Three contributions","The paper makes three main contributions toward practical privacy-preserving collaboration."),
        (ch[1],GOLD,"1","Survey the gaps","Reviews existing privacy-preserving machine learning approaches to expose their limitations and the room to improve."),
        (ch[2],TEAL,"2","The framework","Each peer trains an autoencoder, shares only the latent representation, and joins the embeddings to train a shared supervised model."),
        (ch[3],GREEN,"3","Broad validation","Validated on three public datasets, spanning regression and classification, across five scenarios up to non-naive multitask autoencoders."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    for i,(c,col,tag,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+50,cy+66,26,fill="none",stroke=col,sw=2.5)+
              T(x+50,cy+75,tag,26,col,"800",anchor="middle"))
        yy=cy+134
        tlines=wrap(ti,18)
        for j,ln in enumerate(tlines):
            body+=T(x+24,yy+j*26,ln,17.5,TEXT,"800")
        yy+=26*len(tlines)+12
        body+=para(x+24,yy,tx,13.5,SEC,31,21)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=T(64,586,"Encode with an autoencoder, share only the code, then join and train, no raw features ever leave a peer.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Encode, share the code, then join and train")
    lx=64; lw=568
    # c1 one extra step: encode before sharing
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(lx,158,lw,204,fill=PANEL,stroke=STROKE)+
        rect(lx,158,6,204,fill=ACCENT,rx=6,sw=0)+
        T(lx+28,196,"One extra step before sharing",16.5,ACCENT,"800")+
        para(lx+28,224,"Instead of merging raw datasets, each peer first passes its features through an autoencoder to obtain an obfuscated latent representation, ready to share.",13.5,SEC,60,20)[0]+
        aefunnel(lx+28,300,180,52,col=ACCENT,zcol=TEAL)+
        eqbox(lx+240,306,lw-268,"z = f(x)   share z, not x",13,h=40))
    # c2 join by shared ID, train one model
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(lx,378,lw,172,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(lx,378,6,172,fill=TEAL,rx=6,sw=0)+
        T(lx+28,416,"Join by a shared ID, train once",16,TEAL,"800")+
        para(lx+28,444,"Peers join their representations by a shared observation ID and train a single supervised model on the combined embeddings to predict the target.",13.5,TEXT,60,20)[0]+
        eqbox(lx+28,506,lw-56,"[ z_A | z_B ]  ->  one shared predictor",13.5,h=36))
    rxx=656; rw=560
    # c3 the fixed autoencoder
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,204,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,204,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,196,"A single fixed autoencoder",16.5,GOLD,"800")+
        para(rxx+28,224,"The same autoencoder is used across every experiment, so conclusions reflect the framework, not network tuning: a four-layer encoder down to size M, mirrored back to N.",13.5,SEC,58,20)[0]+
        eqbox(rxx+28,312,rw-56,"N -> 128 -> 64 -> 40 -> M  ->  40 -> 64 -> 128 -> N",13.5,h=38))
    # c4 training recipe + non-naive
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,378,rw,172,fill=PANEL,stroke=STROKE)+
        rect(rxx,378,6,172,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,414,"Training recipe, and a non-naive twist",15,GREEN,"800")+
        para(rxx+28,442,"ReLU layers, Mean Absolute Error loss, Adam. In non-naive scenarios the autoencoder is multitask, also predicting the target, so encoding is task-guided.",13,SEC,60,19)[0]+
        eqbox(rxx+28,510,rw-56,"min (1/n) sum ||x - g(f(x))||_1   ReLU · MAE · Adam 1e-4",12,h=34))
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def _dstat(x,y,w,name,obs,feats,task,col,h=70):
    out=rect(x,y,w,h,fill=PANEL2,stroke=col,rx=10,sw=1.5)+rect(x,y,5,h,fill=col,rx=2,sw=0)
    out+=T(x+18,y+25,name,14,TEXT,"800")
    out+=T(x+18,y+45,obs,12.5,SEC,"600")
    out+=T(x+18,y+63,feats,12.5,SEC,"600")
    out+=T(x+w-16,y+25,task,12,col,"800",anchor="end")
    return out

def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Three public sets, two task types")
    # c1 left: House Pricing
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,212,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,212,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"Three public datasets",16.5,ACCENT,"800")+
        para(92,224,"Chosen to test the framework under realistic and varied conditions. First, House Pricing predicts house price in US dollars.",14,SEC,58,21)[0]+
        _dstat(92,286,504,"House Pricing","21,613 observations","12 features","regression",ACCENT))
    # c2 right: MNIST + Buzz
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(656,158,560,212,fill=PANEL,stroke=STROKE)+
        rect(656,158,6,212,fill=TEAL,rx=6,sw=0)+
        T(684,196,"A large-feature and a large-sample set",15.5,TEAL,"800")+
        _dstat(684,214,504,"MNIST Numbers","35,000 observations","784 features (tabular)","10-class",TEAL)+
        _dstat(684,292,504,"Buzz in Social Media","87,488 observations","77 features","regression",GOLD))
    # c3 coverage strip
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(64,388,1152,74,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,388,6,74,fill=TEAL,rx=6,sw=0)+
        T(92,418,"Deliberately varied",15.5,TEAL,"800")+
        para(238,412,"Together they cover regression and classification, small and large feature sets, and different feature types, probing how robust and scalable the encoding is.",13.5,TEXT,96,21)[0])
    # c4 compute callout
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,478,1152,72,fill=PANEL,stroke=STROKE)+
        rect(64,478,6,72,fill=SEC,rx=6,sw=0)+
        T(92,512,"A modest compute setup",15,TEXT,"800")+
        T(92,536,"2-core Intel Xeon @ 2.3 GHz",13,SEC,"600")+
        T(430,536,"·  Nvidia K80 / T4, 12 GB",13,SEC,"600")+
        T(760,536,"·  12 GB RAM",13,SEC,"600"))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","Obfuscate the data, keep the accuracy")
    # c1 headline strip
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,110,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,110,fill=GREEN,rx=6,sw=0)+
        T(92,194,"Encoded representations barely hurt performance",16.5,GREEN,"800")+
        stat(92,204,240,52,"< 10 pp","drop vs raw features",GREEN)+
        rect(352,204,864,52,fill=PANEL2,stroke=STROKE,rx=12)+
        para(372,232,"The central finding: sharing encoded representations instead of raw features barely changes downstream accuracy, while the data stays obfuscated.",13,SEC,92,20)[0])
    # c2 House Pricing bars
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,284,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,284,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,320,"House Pricing: an almost negligible drop",15,ACCENT,"800")+
        bar(300,346,250,90.29,100,GREEN,"raw baseline","90.29% R2",h=22)+
        bar(300,378,250,89.33,100,TEAL,"two AEs (Sc. 2)","89.33% R2",h=22)+
        T(300,414,"obfuscated data, near-identical R-squared",12,TER,"600"))
    # c3 Buzz + MNIST bars
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,284,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,284,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,318,"Buzz and MNIST hold up too",15,GOLD,"800")+
        bar(864,338,300,96.19,100,SEC,"Buzz raw R2","96.19%",h=18)+
        bar(864,362,300,91.0,100,TEAL,"Buzz encoded","~89-91%",h=18)+
        bar(864,386,300,92.0,100,SEC,"MNIST raw acc","92%",h=18)+
        bar(864,410,300,85.0,100,GOLD,"MNIST encoded","mid-80s",h=18))
    # c4 non-naive recovers the gap
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,450,1152,100,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,450,6,100,fill=GOLD,rx=6,sw=0)+
        T(92,486,"Guiding the latent space recovers much of the gap",16,GOLD,"800")+
        para(92,516,"The non-naive multitask scenarios, where the autoencoder is guided by the target variable, recover most of the small loss, showing task-shaped codes help.",14,TEXT,110,22)[0])
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def _scen(x,y,w,tag,text,col,h=30):
    return (rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=7)+
            rect(x,y,34,h,fill=col,rx=7,sw=0)+
            T(x+17,y+h/2+5,tag,13,BG,"800",anchor="middle")+
            T(x+44,y+h/2+5,text,12.5,TEXT,"600"))

def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","Five scenarios isolate each choice")
    # c1 top-left: five scenarios framing
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"An ablation over five scenarios",16.5,ACCENT,"800")+
        para(92,226,"The experiments are organized as an ablation across five scenarios that isolate each design decision, from no privacy to task-guided encoding.",14,SEC,58,21)[0]+
        chip(92,272,"Scenario 0  ->  Scenario 4",ACCENT,w=468,h=28))
    # c2 bottom-left: naive scenarios 0-2
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,324,560,226,fill=PANEL,stroke=STROKE)+
        rect(64,324,6,226,fill=TEAL,rx=6,sw=0)+
        T(92,360,"Naive scenarios 0 to 2",16.5,TEAL,"800")+
        _scen(92,384,504,"S0","Raw-data baseline, no privacy protection",SEC)+
        _scen(92,422,504,"S1","Single shared autoencoder on one combined set",ACCENT)+
        _scen(92,460,504,"S2","Two peers, individual AEs, embeddings joined",TEAL)+
        T(92,516,"each step adds obfuscation while sharing latent codes",12,TER,"600"))
    # c3 top-right: non-naive 3 & 4
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,150,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,158,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,196,"Non-naive scenarios 3 and 4",16,GOLD,"800")+
        para(684,226,"Scenarios 3 and 4 repeat 1 and 2 but make the autoencoder multitask, also predicting the objective. The non-naive variants beat their naive counterparts.",13.5,TEXT,60,21)[0])
    # c4 bottom-right: the gains, bars
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,324,560,226,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,324,6,226,fill=GREEN,rx=6,sw=0)+
        T(684,360,"Task-guided codes lift the numbers",15.5,GREEN,"800")+
        para(684,388,"Guiding the latent space with the target clearly helps across datasets.",13.5,TEXT,60,20)[0]+
        bar(892,436,300,91.55,100,SEC,"Buzz R2 (S1)","91.55%",h=20)+
        bar(892,466,300,94.03,100,GREEN,"Buzz R2 (S3)","94.03%",h=20)+
        bar(892,496,300,91.0,100,TEAL,"MNIST acc S1->S3","88% -> 91%",h=20))
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The impact in one place")
    # c1 big strip: <10pp + 5-11% recon error
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,132,fill=PANEL,stroke=STROKE)+
        rect(64,166,6,132,fill=GREEN,rx=6,sw=0)+
        T(92,202,"Predictive power kept, data obfuscated",16.5,GREEN,"800")+
        stat(92,220,250,66,"< 10 pp","performance drop vs raw",GREEN)+
        stat(360,220,250,66,"5-11%","autoencoder recon. error",TEAL)+
        rect(630,220,586,66,fill=PANEL2,stroke=STROKE,rx=12)+
        para(650,248,"Across every use case, swapping raw features for shared latent codes cost under ten points of performance.",13,SEC,74,20)[0])
    # c2 House Pricing R2 (left)
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,314,560,150,fill=PANEL,stroke=STROKE)+
        rect(64,314,6,150,fill=ACCENT,rx=6,sw=0)+
        T(92,350,"House Pricing R-squared",16.5,ACCENT,"800")+
        stat(92,368,220,80,"90.29%","raw baseline",SEC)+
        T(324,414,"->",26,SEC,"800",anchor="middle")+
        stat(370,368,220,80,"89.33%","two individual AEs",TEAL))
    # c3 Buzz R2 (right)
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,314,560,150,fill=PANEL,stroke=STROKE)+
        rect(656,314,6,150,fill=GOLD,rx=6,sw=0)+
        T(684,350,"Buzz in Social Media R-squared",16,GOLD,"800")+
        stat(684,368,220,80,"96.19%","raw baseline",SEC)+
        T(916,414,"->",26,SEC,"800",anchor="middle")+
        stat(962,368,220,80,"94.03%","non-naive shared AE",GREEN))
    # c4 recon accuracy callout
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,480,1152,70,fill="#0F2E2B",stroke=TEAL,rx=14,sw=1.5)+
        rect(64,480,6,70,fill=TEAL,rx=6,sw=0)+
        T(92,510,"Faithful reconstructions",15.5,TEAL,"800")+
        T(92,534,"Shared autoencoders correctly estimate 96-98% of observations per feature, so the embeddings retain the data's core structure.",13.5,SEC,"600"))
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Share the code, keep the data private")
    cards=[
        (ch[0],ACCENT,"Share codes, not raw data","Instead of exchanging raw sensitive data, collaborating organizations can share the latent-space embeddings produced by autoencoders."),
        (ch[1],TEAL,"Private, yet still accurate","This keeps the original features private while preserving most of the predictive power, dropping under ten points across three benchmarks."),
        (ch[2],GREEN,"Make the encoder task-aware","Making the autoencoder aware of the downstream task, the non-naive variant, narrows the small remaining gap even further."),
        (ch[3],GOLD,"What comes next","Custom per-dataset autoencoders and formal measures of privacy strength are the next steps toward real organizational deployment."),
    ]
    y=170
    for c,col,ti,tx in cards:
        body=(rect(64,y,1152,90,fill=PANEL,stroke=STROKE)+
              rect(64,y,6,90,fill=col,rx=6,sw=0)+
              circle(112,y+45,10,fill=col)+
              T(150,y+38,ti,18,TEXT,"800"))
        body+=para(150,y+64,tx,14,SEC,96,20)[0]
        b+=anchor(c["aid"],c["kw"],body)
        y+=102
    b+=line(64,596,1216,596,STROKE,1)
    b+=aefunnel(84,612,140,44,col=TEAL,zcol=TEAL,labels=False)
    b+=T(1216,632,"Privacy-Preserving ML via Auto-encoder Latent Embeddings  ·  NeurIPS 2022",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
