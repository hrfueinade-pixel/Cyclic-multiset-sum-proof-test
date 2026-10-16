"""Probe a fixed-injective arithmetic shortcut for the four-fiber cover.

Edges join H forms whose difference is a unit multiple of a balanced
forbidden relation. A proper coloring bounds all cliques and therefore
the size of any fixed family certified injective by this edge rule.
"""

import argparse
import json
from math import gcd
from pathlib import Path
from time import monotonic

from stage3_four_fiber_search import forbidden_forms
from stage3_search import bits


def investigate(modulus, seconds, checkpoint):
    start = monotonic()
    balanced, forms = forbidden_forms(modulus)
    units = [u for u in range(1, modulus) if gcd(u,modulus)==1]
    differences = {tuple(u*x % modulus for x in vector)
                   for vector in balanced for u in units}
    adjacency = [0]*len(forms)
    edges = 0
    for i,(a,b,c) in enumerate(forms):
        if monotonic()-start >= seconds:
            result={"status":"TIMEOUT","N":modulus,"seconds_limit":seconds,
                    "elapsed_seconds":monotonic()-start,"completed_rows":i,
                    "forms":len(forms),"complete_graph":False}
            Path(checkpoint).write_text(json.dumps(result,indent=2)+"\n",encoding="ascii")
            return result
        for j in range(i):
            d,e,f=forms[j]
            if ((a-d)%modulus,(b-e)%modulus,(c-f)%modulus) in differences:
                adjacency[i]|=1<<j
                adjacency[j]|=1<<i
                edges+=1
    order=sorted(range(len(forms)),key=lambda i:adjacency[i].bit_count(),reverse=True)
    colors=[-1]*len(forms)
    classes=[]
    for i in order:
        for color,members in enumerate(classes):
            if not adjacency[i]&members:
                colors[i]=color
                classes[color]|=1<<i
                break
        else:
            colors[i]=len(classes)
            classes.append(1<<i)
    assert all(colors[i]!=colors[j] for i in range(len(forms)) for j in bits(adjacency[i]) if j<i)
    best=[]
    for seed in order[:100]:
        clique=[seed]
        available=adjacency[seed]
        while available:
            chosen=max(bits(available),key=lambda i:(adjacency[i]&available).bit_count())
            clique.append(chosen)
            available&=adjacency[chosen]
        if len(clique)>len(best):
            best=clique
    result={"status":"COMPLETE","N":modulus,"seconds_limit":seconds,
            "elapsed_seconds":monotonic()-start,"forms":len(forms),
            "balanced_unit_multiple_differences":len(differences),
            "graph_edges":edges,"proper_coloring_count":len(classes),
            "greedy_clique_count":len(best),"clique_form_indices":best,
            "form_colors":colors,"complete_graph":True,
            "max_clique_computed":False}
    Path(checkpoint).write_text(json.dumps(result,indent=2)+"\n",encoding="ascii")
    return {k:v for k,v in result.items() if k not in ("form_colors","clique_form_indices")}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--N",type=int,default=247)
    parser.add_argument("--seconds",type=float,default=60)
    parser.add_argument("--checkpoint",default="stage3_four_fiber_cover_247.json")
    args=parser.parse_args()
    print(json.dumps(investigate(args.N,args.seconds,args.checkpoint),indent=2))
