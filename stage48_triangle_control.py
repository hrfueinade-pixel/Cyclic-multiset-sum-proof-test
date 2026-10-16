"""One declared positive control for a proposed global triangle inequality.

No modulus, parameter or set search. Standard-library count enumeration checks
the fixed example, full validity and exact ordinary graph classifications.
"""
import itertools
import json
from collections import Counter,defaultdict
from pathlib import Path


def counts(total,width):
    if width==1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in counts(total-first,width-1):yield(first,)+rest


def main():
    a=(0,101,303,707,1515,3131,6363,1);n=12827
    target=sum(a)%n
    hits=[c for c in counts(8,8)if sum(x*y for x,y in zip(a,c))%n==target]
    assert hits==[(1,)*8]
    shape_names={(2,2,2):'triangle',(3,1,1,1):'star',
                 (2,2,1,1):'path',(2,1,1,1,1):'split'}
    output={};T={};caps={};C3=0;F4=0;R3=0
    for degree in(3,4,5):
        repeated=defaultdict(list);ordinary=defaultdict(list)
        for c in counts(degree,8):
            value=sum(x*y for x,y in zip(a,c))%n
            if max(c)>1:repeated[value].append(c)
            if sorted(x for x in c if x)==[1]*(degree-2)+[2]:ordinary[value].append(c)
        T[degree]=len(repeated)
        caps[degree]={'total':max(map(len,repeated.values())),
                      'ordinary':max(map(len,ordinary.values()))}
        if degree==3:
            C3=sum(len(w)==3 for w in ordinary.values())
            R3=sum((len(w)-1)*(len(w)-2)//2 for w in repeated.values())
            continue
        triples=[];disjoint=[]
        for value,words in ordinary.items():
            if len(words)==2 and degree==4:
                tails=[{i for i,c in enumerate(w)if c==1}for w in words]
                if not tails[0]&tails[1]:disjoint.append({'value':value,'words':words})
            if len(words)!=3:continue
            centers={next(i for i,c in enumerate(w)if c==2)for w in words}
            b=set(range(8))-centers
            tails=[{i for i,c in enumerate(w)if c==1}for w in words]
            edges=tails if degree==4 else[b-tail for tail in tails]
            degrees=Counter(i for edge in edges for i in edge)
            shape=shape_names[tuple(sorted(degrees.values(),reverse=True))]
            triples.append({'value':value,'shape':shape,'words':words})
        output[degree]={'triples':triples,'shapes':dict(Counter(t['shape']for t in triples))}
        if degree==4:F4=len(disjoint);output[degree]['disjoint_two_ordinary_values']=disjoint
    delta={(x-y)%n for x in a for y in a if x!=y}
    assert len(delta)==56
    h=sum((2*d)%n not in delta for d in delta)//2;k=h+R3
    C4tri=output[4]['shapes'].get('triangle',0)
    C4split=output[4]['shapes'].get('split',0)
    C5split=output[5]['shapes'].get('split',0)
    lhs=5*C4tri+4*C5split;rhs=2*k+2*C3+5*C4split+F4
    assert(T,h,R3,C4tri,C5split,C3,C4split,F4,lhs,rhs)==(
        {3:43,4:127,5:260},7,0,7,0,0,0,7,35,21)
    assert caps[3]['total']==2 and caps[4]['ordinary']==3 and caps[5]['ordinary']==3
    result={'status':'PASS','scope':'One fixed counterexample; no small-order conclusion.',
            'set':a,'modulus':n,'full_valid':True,'checked_eight_term_words':6435,
            'T':T,'h':h,'R3':R3,'caps':caps,'C4triangle':C4tri,'C5split':C5split,
            'C3ordinary':C3,'C4split':C4split,'F4disjoint_two_ordinary':F4,
            'proposed_inequality':{'left':lhs,'right':rhs,'satisfied':lhs<=rhs},
            'ordinary_graph_records':output,
            'boundary':'Refutes the unrestricted inequality under full validity and local caps; T4<=88 remains untested by this example.'}
    Path('stage48_triangle_control_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='ordinary_graph_records'},indent=2))


if __name__=='__main__':main()
