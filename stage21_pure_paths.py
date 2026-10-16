"""One bounded closure layer for the two residual pure three-path shapes."""
import argparse
import json
from pathlib import Path
from time import monotonic
from stage19_cycle_roles import e, lin, compositions, find

def cases():
    F=lin((4,e(0)))
    O=lin((2,e(2)),(1,e(0)),(1,e(1)))
    for shape,last in [('FOO',lin((2,e(3)),(1,e(1)),(1,e(4)))),
                       ('FOP',lin((3,e(3)),(1,e(1))))]:
        base=[lin((1,O),(-1,F)),lin((1,last),(-1,F))]
        if shape=='FOO':
            for a in range(8):
                for b in range(8):
                    if a!=b:
                        yield shape,[a,b],base+[lin((2,e(1)),(-2,e(0)),(-1,e(a)),(1,e(b)))]
        else:
            # Stage 8 Lemma 2.3: 4z=3a+b forces E=6z-5a in A.
            for a in range(8):
                yield shape,[a],base+[lin((6,e(0)),(-5,e(3)),(-1,e(a)))]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seconds',type=float,default=30)
    args=ap.parse_args(); start=monotonic()
    candidates=tuple(c for c in compositions(8,8) if c!=(1,)*8)
    records=[]; complete=True
    for shape,roles,rows in cases():
        if monotonic()-start>args.seconds:
            complete=False; break
        records.append({'shape':shape,'roles':roles,'rows':rows,'certificate':find(rows,candidates)})
    data={'completion':'COMPLETE' if complete else 'TIMEOUT','seconds_limit':args.seconds,
          'elapsed_seconds':monotonic()-start,'records':records}
    Path('stage21_pure_path_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(data['completion'],data['elapsed_seconds'])
    for shape in ('FOO','FOP'):
        local=[r for r in records if r['shape']==shape]
        print(shape,len(local),'roles;',sum(r['certificate'] is None for r in local),'uncertified')

if __name__=='__main__': main()
