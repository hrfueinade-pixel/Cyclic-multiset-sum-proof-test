"""All regular paths on >=4 vertices within eight support points."""
import argparse
from itertools import product
import json
from pathlib import Path
from time import monotonic
from stage19_cycle_roles import e, lin, compositions, find

def models():
    for L in range(4,9):
        for letters in product('FQPO',repeat=L):
            word=''.join(letters)
            if word>word[::-1] or word.count('F')>1 or word.count('Q')>1 or word.count('P')>2:
                continue
            if any(word[i]=='F' for i in range(1,L-1)):
                continue
            if 'F' in word and ('Q' in word or (word[1]!='O' if word[0]=='F' else word[-2]!='O')):
                continue
            if 'Q' in word and any(abs(i-word.index('Q'))!=1 for i,t in enumerate(word) if t=='P'):
                continue
            support=L-1+word.count('O')+sum(word[i]!='F' for i in (0,L-1))
            if support>8:
                continue
            ps=[i for i,t in enumerate(word) if t=='P' and 0<i<L-1]
            for orientation in product((0,1),repeat=len(ps)):
                private=L-1; centers={}; vertices=[]
                for i,t in enumerate(word):
                    left=i-1 if i else None
                    right=i if i<L-1 else None
                    incident=[x for x in (left,right) if x is not None]
                    if t=='F':
                        vertices.append(lin((4,e(incident[0])))); continue
                    if len(incident)==1:
                        incident.append(private); private+=1
                    if t=='Q':
                        vertices.append(lin((2,e(incident[0])),(2,e(incident[1])))); continue
                    if t=='O' or i in (0,L-1):
                        centers[i]=private; private+=1
                    else:
                        centers[i]=incident[orientation[ps.index(i)]]
                    if t=='P' and i in (0,L-1):
                        # An endpoint's pure deletion is paired, so its sole
                        # shared point is its singleton. Its center is private.
                        centers[i]=incident[1]; private-=1
                        vertices.append(lin((3,e(centers[i])),(1,e(incident[0]))))
                    else:
                        vertices.append(lin((2,e(centers[i])),(1,e(incident[0])),(1,e(incident[1]))))
                assert private==support
                supports=[{j for j,x in enumerate(v) if x} for v in vertices]
                if any(bool(supports[i]&supports[j])!=(i==j+1) for i in range(L) for j in range(i)):
                    continue
                if any(centers[i] in supports[j] for i,t in enumerate(word) if t=='P' for j,s in enumerate(word) if s=='Q'):
                    continue
                base=[lin((1,v),(-1,vertices[0])) for v in vertices[1:]]
                domains=[]; pairs=[]
                for i in range(L):
                    for j in range(i):
                        if word[i] not in 'OP' or word[j] not in 'OP' or supports[i]&supports[j]:
                            continue
                        a,c=centers[i],centers[j]
                        if word[i]==word[j]=='P':
                            base.append(lin((5,e(a)),(-5,e(c)))); continue
                        roles=product(sorted(supports[i]-{a}),sorted(supports[j]-{c}))
                        domains.append([(r,lin((2,e(a)),(-2,e(c)),(-1,e(r[0])),(1,e(r[1])))) for r in roles])
                        pairs.append([i,j])
                yield word,orientation,vertices,support,base,domains,pairs

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seconds',type=float,default=60)
    args=ap.parse_args(); start=monotonic()
    candidates=tuple(c for c in compositions(8,8) if c!=(1,)*8)
    records=[]; complete=True
    for word,orientation,vertices,support,base,domains,pairs in models():
        for options in product(*domains):
            if monotonic()-start>args.seconds:
                complete=False; break
            rows=base+[r for _,r in options]
            records.append({'word':word,'orientation':orientation,'vertices':vertices,
                            'support_size':support,'domain_pairs':pairs,
                            'roles':[r for r,_ in options],'rows':rows,'certificate':find(rows,candidates)})
        if not complete: break
    result={'completion':'COMPLETE' if complete else 'TIMEOUT','seconds_limit':args.seconds,
            'elapsed_seconds':monotonic()-start,'records':records}
    Path('stage20_path_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['completion'],result['elapsed_seconds'],len(records),'branches')
    print('uncertified:',sum(r['certificate'] is None for r in records))
    print('surviving words:',sorted({r['word'] for r in records if r['certificate'] is None}))

if __name__=='__main__': main()
