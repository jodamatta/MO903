import csv, sys
from collections import Counter
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=list(csv.DictReader(open(sys.argv[1])))
out=sys.argv[2]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9})
INK='#0b0b0b'; INK2='#52514e'; GRID='#e4e3df'; SURF='white'
C={'P':'#2a78d6','R':'#eb6834','O':'#1baf7a'}
LAB={'P':'Entrada/contexto','R':'Representações internas','O':'Saída/decodificação'}
order=['P','R','O']
# Fig A: year stacked
years=['2021','2022','2023','2024','2025','2026']
cnt=Counter((r['ano'],r['ponto']) for r in R)
fig,ax=plt.subplots(figsize=(6.2,2.6),dpi=200)
w=0.62
for i,y in enumerate(years):
    base=0
    for k in order:
        v=cnt[(y,k)]
        if v==0: continue
        ax.bar(i,v,w,bottom=base,color=C[k],edgecolor=SURF,linewidth=1.2)
        if v>=2: ax.text(i,base+v/2,str(v),ha='center',va='center',fontsize=7.5,color='white' if k!='O' else INK,fontweight='bold')
        base+=v
    ax.text(i,base+0.6,str(base),ha='center',va='bottom',fontsize=8,color=INK)
ax.set_xticks(range(len(years))); ax.set_xticklabels(years[:-1]+['2026*'],color=INK2)
ax.set_ylabel('Estudos incluídos',color=INK2)
ax.set_ylim(0,33)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(GRID)
ax.yaxis.grid(True,color=GRID,linewidth=0.6); ax.set_axisbelow(True)
ax.tick_params(axis='y',colors=INK2,length=0); ax.tick_params(axis='x',length=0)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=C[k],label=LAB[k]) for k in order],frameon=False,loc='upper left',fontsize=8)
fig.tight_layout(); fig.savefig(out+'/fig_anos.pdf'); fig.savefig(out+'/fig_anos.png')
# Fig B: attribute access by intervention point (horizontal stacked, sequential ramp)
A={'N':'Não usa','F':'Só offline (construção/calibração)','I':'Exige na inferência'}
S={'N':'#a9cbf2','F':'#5b97e0','I':'#1f4f9a'}
fig,ax=plt.subplots(figsize=(6.2,1.9),dpi=200)
c2=Counter((r['ponto'],r['atributo']) for r in R)
for j,k in enumerate(reversed(order)):
    left=0; tot=sum(c2[(k,a)] for a in 'NFI')
    for a in 'NFI':
        v=c2[(k,a)]
        if v==0: continue
        ax.barh(j,v,0.6,left=left,color=S[a],edgecolor=SURF,linewidth=1.2)
        ax.text(left+v/2,j,str(v),ha='center',va='center',fontsize=7.5,color=INK if a=='N' else 'white',fontweight='bold')
        left+=v
    ax.text(left+0.4,j,f'n={tot}',va='center',fontsize=8,color=INK2)
ax.set_yticks(range(3)); ax.set_yticklabels([LAB[k] for k in reversed(order)],color=INK)
ax.set_xlabel('Número de estudos',color=INK2); ax.set_xlim(0,38)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(GRID); ax.tick_params(length=0,colors=INK2)
ax.xaxis.grid(True,color=GRID,linewidth=0.6); ax.set_axisbelow(True)
ax.legend(handles=[Patch(color=S[a],label=A[a]) for a in 'NFI'],frameon=False,ncol=3,fontsize=7.5,loc='lower center',bbox_to_anchor=(0.42,1.0))
fig.tight_layout(); fig.savefig(out+'/fig_atributo.pdf'); fig.savefig(out+'/fig_atributo.png')
