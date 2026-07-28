#!/usr/bin/env python3
"""All-native SVG deck builder for paper2video run 010
(Flexible Attention-Based Multi-Policy Fusion for Efficient Deep RL / KIAN, KGRL
- NeurIPS 2023, UC San Diego / UC Santa Barbara).
Reads _anchor_map.json; wraps each narration chunk in its own <g id="cue_...">
card with a <title> holding the cue keywords, so the strict
--require-pptx-anchors cue pass resolves every anchor from PPTX geometry.
Zero <image>, zero gradients, ASCII mono equations only.
Theme motif: an inner self-learned policy fused with external knowledge policies
through query-key attention; each policy is an independent, swappable key."""
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
def kianfig(cx,cy,scale=1.0):
    """Inner policy fused with external knowledge policies via attention:
    a central fused-action node ringed by independent policy keys."""
    r=int(60*scale)
    pts=[(-1,-0.85,TEAL,"k_in"),(-1,0.95,ACCENT,"k_g1"),
         (1,-0.85,GOLD,"k_g2"),(1,0.95,RED,"k_g3")]
    out=""
    for dx,dy,col,_ in pts:
        out+=line(cx,cy,cx+dx*r,cy+dy*r,STROKE,1.6)
    for dx,dy,col,nm in pts:
        kx,ky=cx+dx*r,cy+dy*r
        out+=circle(kx,ky,9,fill=col)
    out+=circle(cx,cy,18,fill="none",stroke=WHITE,sw=2.4)
    out+=circle(cx,cy,7,fill=WHITE)
    out+=T(cx,cy-r-14,"keys = policies",11,TEAL,"800",anchor="middle")
    out+=T(cx,cy+r+24,"attention fusion",11.5,SEC,"800",anchor="middle")
    return out

def attention_engine(x,y,w,h):
    """The KIAN core: a state-dependent query is compared to every policy key by
    a dot product, softmax gives fusion weights, and the policies are combined
    into one fused policy that samples the action."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    qcx=x+34; qcy=y+h/2
    out+=circle(qcx,qcy,15,fill=ACCENT)
    out+=T(qcx,qcy+5,"q",13,BG,"800",anchor="middle",ff=MONO)
    out+=T(qcx,qcy-24,"query",9.5,SEC,"700",anchor="middle")
    out+=T(qcx,qcy+30,"Phi(s)",9.5,SEC,"700",anchor="middle")
    kx=x+w*0.33
    keys=[("k_in",TEAL),("k_g1",GOLD),("k_g2",RED)]
    kcen=[]
    for i,(nm,col) in enumerate(keys):
        ky=y+22+i*((h-44)/2.0)
        kcen.append((ky+10,col))
        out+=line(qcx+16,qcy,kx-6,ky+10,STROKE,1.2)
        out+=T(kx-16,ky+15,"·",15,SEC,"800",anchor="middle")
        out+=rect(kx,ky,58,20,fill=PANEL2,stroke=col,rx=5,sw=1.3)
        out+=T(kx+29,ky+14,nm,10.5,col,"800",anchor="middle",ff=MONO)
    wx=x+w*0.585
    out+=T(wx+44,y+15,"softmax w^",10,ACCENT,"800",anchor="middle")
    ww=[(0.52,TEAL),(0.30,GOLD),(0.18,RED)]
    wend=[]
    for i,((val,col),(kcy,_)) in enumerate(zip(ww,kcen)):
        by=y+24+i*((h-46)/2.0)
        bw=int(96*val)+8
        out+=line(kx+58,kcen[i][0],wx-4,by+8,STROKE,1.0)
        out+=rect(wx,by,bw,16,fill=col,rx=4,sw=0)
        wend.append((wx+bw,by+8))
    px=x+w-46
    out+=arrow(wx+112,qcy,px-20,qcy,STROKE,1.4,7)
    out+=circle(px,qcy,20,fill="none",stroke=GREEN,sw=2.4)
    out+=T(px,qcy+6,"pi",15,GREEN,"800",anchor="middle",ff=MONO)
    out+=T(px,qcy-28,"fused",9.5,GREEN,"800",anchor="middle")
    out+=T(px,qcy+36,"sample a",9,SEC,"600",anchor="middle")
    return out

def keymodule(x,y,w,h):
    """Each policy is an independent key, so the knowledge set can be freely
    rearranged, added to, or swapped without retraining the rest of KIAN."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    out+=T(x+14,y+18,"add · swap · reorder",10,SEC,"700")
    chips=[("k_in",TEAL,False),("k_g1",GOLD,False),("k_g2",RED,False),("+ new",GREEN,True)]
    n=len(chips); gap=8; cw=(w-28-(n-1)*gap)/n
    cy=y+h/2+9
    for i,(nm,col,dashed) in enumerate(chips):
        cx=x+14+i*(cw+gap)
        fill="none" if dashed else PANEL2
        out+=rect(cx,cy-15,cw,30,fill=fill,stroke=col,rx=7,sw=1.4)
        out+=T(cx+cw/2,cy+4,nm,10.5,col,"800",anchor="middle",ff=MONO)
    return out

def entropybars(x,y,w,h,collapse=True,title="",col=ACCENT):
    """Fusion-weight distribution over policies: entropy imbalance collapses
    weight onto a single policy; the fix restores a balanced spread."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    if title: out+=T(x+14,y+20,title,11.5,col,"800")
    vals=[0.88,0.07,0.05] if collapse else [0.40,0.34,0.26]
    labels=["pi_in","pi_g1","pi_g2"]
    cols=[TEAL,GOLD,RED]
    bx=x+58; bw=w-84; ay0=y+h-18
    slot=(h-46)/3.0
    for i,(v,lb,c) in enumerate(zip(vals,labels,cols)):
        by=y+34+i*slot
        out+=T(bx-10,by+11,lb,10,c,"800",anchor="end",ff=MONO)
        out+=rect(bx,by,bw,14,fill="#0A1A2C",stroke=STROKE,rx=4,sw=0.8)
        out+=rect(bx,by,max(4,int(bw*v)),14,fill=c,rx=4,sw=0)
        out+=T(bx+int(bw*v)+8,by+11,f"{v:.2f}",9.5,c,"800")
    return out

def gridworld(x,y,s=1.0):
    """A MiniGrid door-key puzzle: agent, key, door, and goal on a grid."""
    n=5; cell=int(20*s); gx=x; gy=y
    out=rect(gx-4,gy-4,n*cell+8,n*cell+8,fill="#0E223A",stroke=STROKE,rx=6)
    for i in range(n+1):
        out+=line(gx,gy+i*cell,gx+n*cell,gy+i*cell,STROKE,0.7)
        out+=line(gx+i*cell,gy,gx+i*cell,gy+n*cell,STROKE,0.7)
    # agent (triangle) bottom-left
    ax,ay=gx+cell*0.5,gy+cell*4.5
    out+=polygon([(ax-6,ay+5),(ax+6,ay+5),(ax,ay-6)],fill=ACCENT)
    # key
    kx,ky=gx+cell*2.5,gy+cell*3.5
    out+=circle(kx,ky-3,4,fill="none",stroke=GOLD,sw=1.6)+line(kx,ky,kx,ky+6,GOLD,1.6)
    # door (a wall gap) col 3
    out+=rect(gx+cell*3,gy,cell*0.28,n*cell,fill=STROKE,rx=0,sw=0)
    out+=rect(gx+cell*3-1,gy+cell*2,cell*0.5,cell,fill=RED,rx=2,sw=0)
    # goal
    out+=rect(gx+cell*4.2,gy+cell*0.2,cell*0.6,cell*0.6,fill=GREEN,rx=2,sw=0)
    return out

def envrow(x,y,w,items):
    gap=14; bw=(w-(len(items)-1)*gap)/len(items); out=""
    for i,(nm,col,sub) in enumerate(items):
        bx=x+i*(bw+gap)
        out+=rect(bx,y,bw,60,fill=PANEL2,stroke=col,rx=10,sw=1.5)
        out+=rect(bx,y,bw,5,fill=col,rx=3,sw=0)
        out+=T(bx+bw/2,y+32,nm,14.5,TEXT,"800",anchor="middle")
        out+=T(bx+bw/2,y+50,sub,11,SEC,"600",anchor="middle")
    return out

def curvecompare(x,y,w,h,hi=0.93,lo=0.53,hilab="KIAN",lolab="best baseline"):
    """Sample-efficiency learning curves: KIAN climbs high and fast while the
    strongest baseline stalls at a lower reward."""
    out=rect(x,y,w,h,fill="#0E223A",stroke=STROKE,rx=8)
    ax0=x+34; ax1=x+w-14; ay0=y+h-24; ay1=y+16
    out+=line(ax0,ay0,ax1,ay0,STROKE,1.2)
    out+=line(ax0,ay0,ax0,ay1,STROKE,1.2)
    def curve(final,k):
        pts=[]
        for t in range(0,101,5):
            u=t/100.0
            val=final*(1-math.exp(-k*u))
            pts.append((ax0+u*(ax1-ax0), ay0-val*(ay0-ay1)))
        return pts
    out+=poly(curve(lo,2.2),stroke=SEC,sw=2.4,dash="6 5")
    out+=poly(curve(hi,4.5),stroke=TEAL,sw=2.8)
    out+=T(ax1,ay0-hi*(ay0-ay1)-6,f"{hilab} {hi:.2f}",10.5,TEAL,"800",anchor="end")
    out+=T(ax1,ay0-lo*(ay0-ay1)+16,f"{lolab} {lo:.2f}",10,SEC,"700",anchor="end")
    out+=T(ax0-4,ay1+2,"reward",9.5,TER,"600",anchor="end")
    out+=T(ax1,ay0+15,"samples ->",9.5,TER,"600",anchor="end")
    return out

def vsbars(x,y,w,h,title,kian,base,baselab):
    """Two-bar comparison: KIAN vs the strongest baseline on one transfer."""
    out=rect(x,y,w,h,fill=PANEL2,stroke=STROKE,rx=10)
    ay0=y+h-24; top=y+30; span=ay0-top
    pairs=[("KIAN",kian,GREEN),(baselab,base,SEC)]
    slot=(w-40)/2.0
    for i,(lb,v,c) in enumerate(pairs):
        cx=x+20+slot*i+slot/2
        bh=max(6,span*v)
        out+=rect(cx-36,ay0-bh,72,bh,fill=c,rx=5,sw=0)
        out+=T(cx,ay0-bh-8,f"{v:.2f}",14,c,"800",anchor="middle")
        out+=T(cx,ay0+16,lb,11,SEC,"700",anchor="middle")
    return out

def propchips(x,y,w,items):
    """The five properties of efficient, flexible human learning."""
    gap=10; bw=(w-(len(items)-1)*gap)/len(items); out=""
    for i,(nm,col,on) in enumerate(items):
        bx=x+i*(bw+gap)
        stroke=col if on else STROKE
        out+=rect(bx,y,bw,52,fill=PANEL2,stroke=stroke,rx=9,sw=1.5)
        mark="check" if on else "~"
        out+=circle(bx+bw/2,y+18,7,fill=col if on else "#20364E")
        for j,ln in enumerate(wrap(nm,13)):
            out+=T(bx+bw/2,y+38+j*13,ln,10.5,TEXT if on else SEC,"700",anchor="middle")
    return out

# ---------- SLIDE 1: TITLE ----------
def s_title():
    ch=chunks("title"); b=""
    b+=T(64,72,"NeurIPS 2023",14,ACCENT,"800",ls="2")
    b+=T(1216,72,"Knowledge-Grounded RL  ·  Attention-Based Policy Fusion",13.5,SEC,"600",anchor="end")
    b+=line(64,88,1216,88,STROKE,1)
    b+=T(64,150,"KIAN",44,WHITE,"800")
    b+=T(64,196,"Flexible Attention-Based Multi-Policy Fusion",23,ACCENT,"800")
    b+=T(64,224,"for Efficient Deep Reinforcement Learning",23,ACCENT,"800")
    b+=kianfig(1112,182,1.0)
    b+=T(64,258,"Zih-Yun Chiu · Yi-Lin Tuan · William Yang Wang · Michael C. Yip",13.5,SEC,"500")
    b+=T(64,280,"UC San Diego   ·   UC Santa Barbara",12.5,TER,"600")
    cw=368; gap=24; x0=64; cy=306; chh=224
    data=[
        (ch[0],ACCENT,x0,"Humans reuse strategies",
         "Reinforcement learning agents still learn far less efficiently than humans, who freely borrow strategies from many sources and rearrange them at will."),
        (ch[1],TEAL,x0+cw+gap,"KGRL + the KIAN actor",
         "Presented at NeurIPS 2023, this work introduces Knowledge-Grounded RL, fusing many external knowledge policies, and a new actor, the Knowledge-Inclusive Attention Network."),
        (ch[2],GREEN,x0+2*(cw+gap),"Add, drop, recombine",
         "KIAN lets an agent add, remove, and recombine knowledge policies without retraining, fixes an exploration pathology called entropy imbalance, and learns more efficiently."),
    ]
    for c,col,x,ti,tx in data:
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+28,cy+44,7,fill=col))
        body+=para(x+46,cy+50,ti,17.5,TEXT,26,22,"800")[0]
        body+=para(x+26,cy+100,tx,13.5,SEC,42,20)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,556,1216,556,STROKE,1)
    b+=T(64,592,"arXiv:2210.03729",14,ACCENT,"700")
    b+=T(310,592,"github.com/Pascalson/KGRL",13.5,SEC,"600")
    b+=T(1216,592,"Modular knowledge for sample-efficient RL.",14,SEC,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 2: PROBLEM ----------
def s_problem():
    ch=chunks("problem"); b=header("Problem","Agents can't freely reuse what they know")
    # c1 left tall: sample inefficiency
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,404,392,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,392,fill=ACCENT,rx=6,sw=0)+
        T(92,202,"RL is sample-hungry",17.5,TEXT,"800")+
        para(92,238,"Reinforcement learning has succeeded across physics and robotics, yet agents still need enormous numbers of samples to solve tasks that humans master quickly.",14,SEC,42,22)[0]+
        rect(92,360,344,138,fill=PANEL2,stroke=STROKE,rx=10)+
        T(112,390,"the efficiency gap",12.5,TER,"700")+
        eqbox(112,406,304,"agent samples  >>  human samples",12.5,h=40,col=RED)+
        T(112,486,"tasks humans master quickly",12,SEC,"600"))
    fx=500; fw=716
    # c2 humans reuse & combine
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(fx,158,fw,150,fill=PANEL,stroke=STROKE)+
        rect(fx,158,6,150,fill=TEAL,rx=6,sw=0)+
        T(fx+28,196,"Humans reuse, combine, and swap",16.5,TEAL,"800")+
        para(fx+28,226,"Part of the gap is that humans learn by observing others and freely reuse, combine, and swap the strategies they already know.",14,SEC,50,21)[0]+
        keymodule(fx+404,214,290,84))
    # c3 prior methods too rigid
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(fx,324,fw,104,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(fx,324,6,104,fill=GOLD,rx=6,sw=0)+
        T(fx+28,362,"Prior knowledge-guided RL was rigid",16,GOLD,"800")+
        para(fx+28,392,"Earlier methods did inject external knowledge policies to improve efficiency, but they made arbitrary combinations and replacements of those policies hard.",14.5,TEXT,88,24)[0])
    # c4 the property to fix
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(fx,444,fw,106,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(fx,444,6,106,fill=GREEN,rx=6,sw=0)+
        T(fx+28,482,"This paper fixes that rigidity",16,GREEN,"800")+
        para(fx+28,512,"The goal is an actor whose knowledge policies can be freely rearranged, added, or replaced. That rigidity is exactly what this work set out to fix.",14.5,SEC,88,24)[0])
    return svg(b)

# ---------- SLIDE 3: MOTIVATION ----------
def s_motivation():
    ch=chunks("motivation"); b=header("Motivation","Five properties of flexible learning")
    # c1 left top: five properties
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,204,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,204,fill=ACCENT,rx=6,sw=0)+
        T(92,196,"What efficient human learning needs",16,ACCENT,"800")+
        para(92,224,"The authors distill five properties of efficient, flexible human learning.",13.5,SEC,58,20)[0]+
        propchips(92,264,504,[("acquirable",ACCENT,True),("efficient",TEAL,True),
                              ("generalizable",GREEN,True),("compositional",GOLD,True),("incremental",VIOLET,True)])+
        T(92,344,"existing methods satisfy some, but stumble on flexibility",12,SEC,"600"))
    # c2 left bottom: rigidity of fusion
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,378,560,172,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,378,6,172,fill=GOLD,rx=6,sw=0)+
        T(92,414,"Fusion tied to number & ordering",15,GOLD,"800")+
        para(92,442,"When fusion depends on the count or ordering of external policies, rearranging the set or swapping a policy means rebuilding or retraining large parts of the model.",13.5,TEXT,58,20)[0])
    # c3 right top: rigidity illustrated
    rxx=648; rw=568
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,158,rw,204,fill=PANEL,stroke=STROKE)+
        rect(rxx,158,6,204,fill=RED,rx=6,sw=0)+
        T(rxx+28,196,"Swapping a policy breaks the model",16,RED,"800")+
        para(rxx+28,226,"Prior actors such as KoGuN and A2T tie fusion to fixed input orderings or per-policy parameters, so adding or removing one policy forces architectural changes.",13.5,SEC,60,20)[0]+
        eqbox(rxx+28,312,rw-56,"add / remove policy  =>  retrain",13.5,h=40,col=RED))
    # c4 right bottom: the design goal
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,378,rw,172,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rxx,378,6,172,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,414,"Design goal: a reorderable actor",15.5,GREEN,"800")+
        para(rxx+28,442,"Design an actor whose structure lets knowledge policies be freely rearranged, added, or replaced, so one trained agent can carry its skills into new tasks.",13.5,TEXT,60,20)[0]+
        T(rxx+28,524,"one trained agent  ->  many new tasks",13,GREEN,"800",ff=MONO))
    return svg(b)

# ---------- SLIDE 4: CONTRIBUTION ----------
def s_contribution():
    ch=chunks("contribution"); b=header("Contribution","One paradigm, one actor, one fix")
    cards=[
        (ch[0],ACCENT,"KGRL","Knowledge-Grounded RL: a paradigm that fuses an inner, self-learned policy with multiple external knowledge policies."),
        (ch[1],TEAL,"KIAN","The Knowledge-Inclusive Attention Network, whose embedding-based attention lets policies be freely rearranged, added, or replaced without touching the rest of the network."),
        (ch[2],GOLD,"Entropy imbalance","A newly uncovered problem when maximizing entropy for exploration; the paper proves when it happens and proposes modified policy distributions that fix it."),
        (ch[3],GREEN,"Efficient & modular","Together these give an agent that is efficient, generalizable, and truly modular in its use of external knowledge."),
    ]
    cw=272; gap=24; x0=64; cy=180; chh=372
    tags=["1","2","3","+"]
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
    b+=T(64,586,"An agent that is efficient, generalizable, and modular in how it reuses knowledge.",15.5,TEAL,"700")
    return svg(b)

# ---------- SLIDE 5: METHOD ----------
def s_method():
    ch=chunks("method"); b=header("Method","Query-key attention over policies")
    # c1 full-width top: the attention engine + eq
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,182,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,182,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"KIAN = inner actor + keys + query",16.5,TEXT,"800")+
        para(92,220,"An inner learnable actor lets the agent form its own strategy, so even if every external policy is useless it can still solve the task.",13,SEC,58,19)[0]+
        eqbox(92,286,536,"w_i = Phi(s).k_i / c_i    ;    pi = sum_i softmax(w)_i * pi_i",12.5,h=40)+
        attention_engine(652,196,564,128))
    # c2 keys are independent embeddings
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,356,560,194,fill=PANEL,stroke=STROKE)+
        rect(64,356,6,194,fill=TEAL,rx=6,sw=0)+
        T(92,394,"Every policy gets a learnable key",16.5,TEAL,"800")+
        para(92,424,"Each knowledge policy, including the inner one, is given a learnable embedding vector, its key, which represents the whole policy independent of any state or action.",13.5,TEXT,58,20)[0]+
        eqbox(92,508,504,"key k_i : one vector per policy",13,h=30))
    # c3 query -> softmax -> fuse
    rxx=656; rw=560
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(rxx,356,rw,90,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(rxx,356,6,90,fill=GOLD,rx=6,sw=0)+
        T(rxx+28,388,"Query, dot-product, softmax, fuse",15.5,GOLD,"800")+
        para(rxx+28,414,"A state-dependent query meets each key by a dot product; softmax turns the scores into fusion weights over the policies.",12.5,SEC,82,18)[0])
    # c4 keys independent -> swappable
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(rxx,462,rw,88,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(rxx,462,6,88,fill=GREEN,rx=6,sw=0)+
        T(rxx+28,494,"Independent keys => swappable",15.5,GREEN,"800")+
        para(rxx+28,520,"Each key is independent, so policies are unordered and any one is swapped just by replacing its key, no retraining needed.",12.5,SEC,82,18)[0])
    return svg(b)

# ---------- SLIDE 6: DATASET ----------
def s_dataset():
    ch=chunks("dataset-benchmark"); b=header("Dataset / Benchmark","Grid-worlds and robotic control")
    # c1 full-width top: two suites
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,160,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,160,fill=ACCENT,rx=6,sw=0)+
        T(92,192,"Two families of environments",16,TEXT,"800")+
        T(96,224,"MiniGrid  ·  discrete",12.5,ACCENT,"800")+
        envrow(96,234,540,[("Empty",ACCENT,"rooms"),("DoorKey",TEAL,"puzzle"),
                           ("Dyn-Obst",GOLD,"moving"),("MultiRoom",RED,"maze")])+
        T(660,224,"OpenAI-Robotics  ·  continuous",12.5,TEAL,"800")+
        envrow(660,234,556,[("Push",ACCENT,"manip"),("Slide",TEAL,"manip"),
                            ("Pick&Place",GOLD,"manip"),("Reach",GREEN,"manip")]))
    # c2 minigrid detail
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,334,560,124,fill=PANEL,stroke=STROKE)+
        rect(64,334,6,124,fill=TEAL,rx=6,sw=0)+
        T(92,370,"Increasing grid-world difficulty",15,TEAL,"800")+
        para(92,398,"From empty rooms to door-key puzzles, dynamic obstacles, lava crossings, multi-room mazes, and key corridors.",13.5,SEC,44,20)[0]+
        gridworld(474,352,1.0))
    # c3 shared sub-optimal knowledge
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,334,560,124,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(656,334,6,124,fill=GOLD,rx=6,sw=0)+
        T(684,370,"Same sub-optimal knowledge set",15.5,GOLD,"800")+
        para(684,398,"Every method starts from the same if-else programs, deliberately sub-optimal and unable to complete any task on their own.",13.5,TEXT,60,20)[0])
    # c4 full-width callout: protocol stats
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(64,474,1152,76,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,474,6,76,fill=GREEN,rx=6,sw=0)+
        T(92,506,"A rigorous protocol",15.5,GREEN,"800")+
        stat(560,482,168,60,"2","benchmark suites",ACCENT)+
        stat(742,482,168,60,"10","random seeds",TEAL)+
        stat(924,482,168,60,"95%","conf. intervals",GOLD)+
        T(92,532,"learning curves averaged with error bands",12.5,SEC,"600"))
    return svg(b)

# ---------- SLIDE 7: KEY RESULT ----------
def s_result():
    ch=chunks("key-result"); b=header("Key Result","The only method that works everywhere")
    # c1 headline strip with learning curve
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,1152,162,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,158,6,162,fill=GREEN,rx=6,sw=0)+
        T(92,196,"KIAN succeeds in every environment",16.5,GREEN,"800")+
        rect(92,214,470,88,fill=PANEL2,stroke=STROKE,rx=12)+
        para(112,244,"From sub-optimal knowledge, KIAN is the only method to succeed across all tasks, and its sample-efficiency lead grows as tasks get harder.",13,SEC,52,20)[0]+
        curvecompare(584,214,632,90,0.93,0.53))
    # c2 zero-shot generalization
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,336,368,214,fill=PANEL,stroke=STROKE)+
        rect(64,336,6,214,fill=TEAL,rx=6,sw=0)+
        T(92,372,"Best zero-shot transfer",16,TEAL,"800")+
        para(92,400,"Train on one task, test on another: KIAN beats all baselines in most transfers, with noticeably smaller variance.",13.5,SEC,42,20)[0]+
        chip(92,502,"outperforms all  ·  lower variance",TEAL,w=312,h=32))
    # c3 hardest grid number
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,336,368,214,fill=PANEL,stroke=STROKE)+
        rect(456,336,6,214,fill=ACCENT,rx=6,sw=0)+
        T(484,372,"Hardest simple-to-complex grid",15,ACCENT,"800")+
        para(484,400,"On the toughest transfer, KIAN reaches a reward near 0.93 while the strongest baseline stalls around 0.53.",13.5,SEC,42,20)[0]+
        vsbars(484,452,312,84,"reward",0.93,0.53,"baseline"))
    # c4 continuous control
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(848,336,368,214,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(848,336,6,214,fill=GOLD,rx=6,sw=0)+
        T(876,372,"Continuous control holds up",15.5,GOLD,"800")+
        para(876,402,"In continuous control, competing methods that ignore the exploration issue collapse, whereas KIAN keeps learning efficiently.",13.5,TEXT,42,20)[0]+
        chip(876,504,"baselines collapse  ·  KIAN keeps learning",GOLD,w=316,h=32))
    return svg(b)

# ---------- SLIDE 8: ABLATION ----------
def s_ablation():
    ch=chunks("ablation-study"); b=header("Ablation Study","The entropy-imbalance fix matters")
    # c1 left top: original fusion collapses
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,158,560,204,fill=PANEL,stroke=STROKE)+
        rect(64,158,6,204,fill=RED,rx=6,sw=0)+
        T(92,196,"Original fusion collapses",16,RED,"800")+
        para(92,224,"With the original policy fusion, an agent maximizing entropy for exploration collapses onto a single policy and struggles.",13.5,SEC,44,20)[0]+
        entropybars(360,206,244,140,collapse=True,title="weights collapse",col=RED))
    # c2 left bottom: worst on hard tasks
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,378,560,172,fill="#2A2417",stroke=GOLD,rx=14,sw=1.5)+
        rect(64,378,6,172,fill=GOLD,rx=6,sw=0)+
        T(92,414,"Worst on the demanding tasks",15,GOLD,"800")+
        para(92,442,"The collapse bites hardest on dynamic obstacles, multi-room mazes, and the robotic manipulation tasks like Push, Slide, and Pick-and-Place.",13.5,TEXT,58,20)[0])
    # c3 right top: the fix restores exploration
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(656,158,560,204,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(656,158,6,204,fill=GREEN,rx=6,sw=0)+
        T(684,196,"Modified distributions fix it",16,GREEN,"800")+
        para(684,224,"Switching on the modified policy distributions restores efficient exploration and recovers strong performance.",13.5,TEXT,40,20)[0]+
        entropybars(972,206,232,140,collapse=False,title="weights balanced",col=GREEN))
    # c4 right bottom: modular reuse pays off
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(656,378,560,172,fill=PANEL,stroke=STROKE)+
        rect(656,378,6,172,fill=TEAL,rx=6,sw=0)+
        T(684,414,"Modular reuse pays off",15.5,TEAL,"800")+
        para(684,442,"Compositional and incremental experiments confirm KIAN reuses its keys and inner policy to acquire new tasks sequentially with fewer samples than training from scratch.",13.5,SEC,58,20)[0])
    return svg(b)

# ---------- SLIDE 9: HEADLINE NUMBERS ----------
def s_headline():
    ch=chunks("headline-numbers"); b=header("Headline Numbers","The gains in three transfers")
    # c1 full-width strip: only method everywhere
    b+=anchor(ch[0]["aid"],ch[0]["kw"],
        rect(64,166,1152,120,fill="#0F2E2B",stroke=GREEN,rx=14,sw=1.5)+
        rect(64,166,6,120,fill=GREEN,rx=6,sw=0)+
        T(92,202,"KIAN is the only method that succeeds everywhere",16.5,GREEN,"800")+
        stat(92,214,300,60,"only method","succeeds in all envs",GREEN)+
        rect(410,214,806,60,fill=PANEL2,stroke=STROKE,rx=12)+
        para(430,240,"A few numbers capture the gains from a sub-optimal initial knowledge set across two benchmark suites.",13.5,SEC,96,20)[0])
    # c2 empty-random transfer
    b+=anchor(ch[1]["aid"],ch[1]["kw"],
        rect(64,302,368,162,fill=PANEL,stroke=STROKE)+
        rect(64,302,6,162,fill=ACCENT,rx=6,sw=0)+
        T(92,334,"Empty-Random 16x16",14.5,ACCENT,"800")+
        T(92,356,"zero-shot simple-to-complex",11.5,SEC,"600")+
        vsbars(92,366,312,90,"reward",0.93,0.53,"KoGuN"))
    # c3 pick-and-place transfer
    b+=anchor(ch[2]["aid"],ch[2]["kw"],
        rect(456,302,368,162,fill=PANEL,stroke=STROKE)+
        rect(456,302,6,162,fill=GOLD,rx=6,sw=0)+
        T(484,334,"Pick-and-Place  10x range",14.5,GOLD,"800")+
        T(484,356,"zero-shot, larger goal range",11.5,SEC,"600")+
        vsbars(484,366,312,90,"success",0.72,0.30,"RL+BC"))
    # c4 doorkey -> reach transfer
    b+=anchor(ch[3]["aid"],ch[3]["kw"],
        rect(848,302,368,162,fill=PANEL,stroke=STROKE)+
        rect(848,302,6,162,fill=TEAL,rx=6,sw=0)+
        T(876,334,"DoorKey-8x8 -> Reach",14.5,TEAL,"800")+
        T(876,356,"complex-to-simple transfer",11.5,SEC,"600")+
        vsbars(876,366,312,90,"success",1.00,0.80,"RL / RL+BC"))
    # footer scope strip (shared, not an anchor)
    b+=rect(64,480,1152,70,fill=PANEL2,stroke=STROKE,rx=12)
    b+=T(92,510,"Measured across",13.5,SEC,"600")
    b+=T(230,510,"2 suites  ·  5 baselines  ·  10 seeds  ·  95% CI",14,TEXT,"800",ff=MONO)
    b+=T(1192,510,"KIAN wins or ties every transfer",13.5,GREEN,"800",anchor="end")
    b+=T(1192,534,"higher reward / success is better",12,TER,"600",anchor="end")
    return svg(b)

# ---------- SLIDE 10: TAKEAWAY ----------
def s_takeaway():
    ch=chunks("takeaway"); b=header("Takeaway","Knowledge as modular building blocks")
    cards=[
        (ch[0],ACCENT,"Each policy is a key","Treating each knowledge policy as an independent, attention-addressable key turns external knowledge into truly modular building blocks."),
        (ch[1],TEAL,"Add, drop, reorder freely","An agent can add, drop, or reorder its policies at any time without retraining the network, and the entropy-imbalance fix keeps exploration efficient when many are fused."),
        (ch[2],GREEN,"Faster, more flexible RL","The result is an RL actor that learns faster, generalizes better, and stays flexible, moving agents closer to the efficiency and adaptability of human learning."),
    ]
    cw=368; gap=24; x0=64; cy=176; chh=360
    for i,(c,col,ti,tx) in enumerate(cards):
        x=x0+i*(cw+gap)
        body=(rect(x,cy,cw,chh,fill=PANEL,stroke=STROKE)+
              rect(x,cy,cw,6,fill=col,rx=6,sw=0)+
              circle(x+34,cy+54,11,fill=col))
        yy=cy+100
        for j,ln in enumerate(wrap(ti,20)):
            body+=T(x+28,yy+j*26,ln,19,TEXT,"800")
        yy+=26*len(wrap(ti,20))+16
        body+=para(x+28,yy,tx,14,SEC,32,22)[0]
        b+=anchor(c["aid"],c["kw"],body)
    b+=line(64,566,1216,566,STROKE,1)
    b+=kianfig(120,624,0.42)
    b+=T(1216,624,"KIAN  ·  Attention-Based Multi-Policy Fusion  ·  NeurIPS 2023",14,SEC,"600",anchor="end")
    return svg(b)

SLIDES=[("01_title",s_title),("02_problem",s_problem),("03_motivation",s_motivation),
        ("04_contribution",s_contribution),("05_method",s_method),("06_dataset",s_dataset),
        ("07_key_result",s_result),("08_ablation",s_ablation),("09_headline",s_headline),
        ("10_takeaway",s_takeaway)]

for name,fn in SLIDES:
    open(os.path.join(OUT,name+".svg"),"w").write(fn())
    print("wrote",name)
print("DONE",len(SLIDES))
