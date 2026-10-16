"""Discovery check of necessary signed-orbit unions at H<248, not A-set search."""
from math import gcd,lcm
import json
from pathlib import Path
from time import monotonic

def main():
    start=monotonic(); records=[]; complete=True
    for n in range(187,248,2):
        if monotonic()-start>5:
            complete=False; break
        unused=set(range(1,n)); blocks=[]
        while unused:
            r=min(unused); orbit=set(); x=r
            while x not in orbit:
                orbit.add(x); orbit.add((-x)%n); x=2*x%n
            unused-=orbit
            blocks.append({'representative':r,'order':n//gcd(n,r),'residues':sorted(orbit)})
        usable=[b for b in blocks if len(b['residues'])<=56 and b['order']!=3]
        dp={(0,1):[]}
        for b in usable:
            add={}
            for (size,order),witness in dp.items():
                newsize=size+len(b['residues'])
                if newsize<=56:
                    key=newsize,lcm(order,b['order'])
                    if key not in dp and key not in add:
                        add[key]=witness+[b['representative']]
            dp.update(add)
        witness=dp.get((56,n))
        records.append({'H':n,'blocks':blocks,'selected_representatives':witness,
                        'necessary_orbit_union_exists':witness is not None})
    data={'completion':'COMPLETE' if complete else 'TIMEOUT','seconds_limit':5,
          'elapsed_seconds':monotonic()-start,'scope':'Necessary 56-residue signed doubling orbit unions at odd H=187..247; no actual sets',
          'records':records}
    Path('stage26_small_h0_orbit_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(data['completion'],data['elapsed_seconds'])
    print('surviving orders:',[r['H'] for r in records if r['necessary_orbit_union_exists']])

if __name__=='__main__': main()
