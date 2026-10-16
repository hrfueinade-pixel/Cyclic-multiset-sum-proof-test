"""Four fixed models for a fiber with three ordinary quintic words.

Their private centers have tails on the other five labels. Complements of
these tails are three distinct edges on five vertices: four graph types.
Positive certificates only; no parameter/modulus search.
"""
import argparse
import json
from pathlib import Path

from stage43_relation_growth import run


EDGES = {'triangle':((0,1),(0,2),(1,2)),
         'star':((0,1),(0,2),(0,3)),
         'path':((0,1),(1,2),(2,3)),
         'split':((0,1),(1,2),(3,4))}


def models():
    tails = ((0,0,0,0,0),(2,0,0,0,0),(0,2,0,0,0),(0,0,2,0,0),(0,0,0,2,0))
    result = []
    for name,edges in EDGES.items():
        centers = []
        for i,j in edges:
            centers.append(tuple((tails[i][k]+tails[j][k])//2 for k in range(4))+(1,))
        result.append({'id':'q3_'+name,'rows':tails+tuple(centers),
                       'direction':[], 'torsion_rows':(0,)*8, 'torsion_order':1,
                       'edges':edges,
                       'parameterization':'Five tails 0,2u,2v,2w,2t; center=z+half the omitted edge sum.'})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--degree',type=int,default=4)
    parser.add_argument('--target',type=int,default=89)
    args = parser.parse_args()
    results = []
    for model in models():
        result = run(model,args.degree,args.target,[2])
        results.append(result)
        print(json.dumps(result),flush=True)
    Path(f'stage43_three_quintics_degree{args.degree}_results.json').write_text(json.dumps({
        'models':models(), 'results':results,
        'boundary':'Four fixed quintic-tail graph types. Only retained positive bounds are claimed, not absence from incomplete discovery.'},indent=2)+'\n',encoding='utf-8')


if __name__ == '__main__':
    main()
