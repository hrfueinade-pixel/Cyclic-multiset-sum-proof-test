"""Fixed symbolic inventory of a companion avoiding a star's added label.

No moduli, group elements or historical searches are enumerated. Label order
is a,b,c,u,v,x,y,z. Normalize the quartic triangle value to zero, and write
(a,b,c,v)=(2p,2q,2r,2t). A mixed quintic M on a,b,c,v forces u=value(M).
This is an exact four-parameter model over every odd group, with no odd unit
cancellation. Formal absence of a rival is a diagnostic, never an exclusion.
"""
import itertools
import json
from pathlib import Path


def count_words(n, degree):
    for indices in itertools.combinations_with_replacement(range(n), degree):
        yield tuple(indices.count(i) for i in range(n))


def value(word, rows):
    return tuple(sum(n * row[j] for n, row in zip(word, rows)) for j in range(4))


def main():
    results = []
    for word in count_words(4, 5):
        # Exactly the five nonordinary repeated shapes, excluding ordinary 2111.
        shape = tuple(sorted((n for n in word if n), reverse=True))
        if shape == (2, 1, 1, 1):
            continue
        rows = [(2,0,0,0),(0,2,0,0),(0,0,2,0),
                tuple(2*n for n in word),(0,0,0,2),
                (0,-1,-1,0),(-1,0,-1,0),(-1,-1,0,0)]
        target = value((1,)*8, rows)
        rivals = [w for w in count_words(8,8)
                  if w != (1,)*8 and value(w, rows) == target]
        fibers = []
        for degree, destination in [(4,(0,0,0,0)),(5,rows[3]),(5,rows[4])]:
            fibers.append([w for w in count_words(8,degree)
                           if value(w,rows)==destination])
        results.append({'word_abcv':word,'shape':shape,'rows':rows,
                        'direct_rivals':rivals,'formal_fibers':fibers})
    assert len(results) == 52
    orbits = {}
    for item in results:
        w=item['word_abcv']
        key=tuple(sorted(w[:3],reverse=True))+(w[3],)
        orbits.setdefault(key,[]).append(item)
    summary={'assignments':len(results),'s3_orbits':len(orbits),
             'direct_rival_assignments':sum(bool(x['direct_rivals']) for x in results),
             'surviving_assignments':sum(not x['direct_rivals'] for x in results),
             'orbit_summary':[{'word_abcv':key,'orbit_size':len(items),
                              'direct_rivals':len(items[0]['direct_rivals']),
                              'quartic_words':len(items[0]['formal_fibers'][0]),
                              'star_u_words':len(items[0]['formal_fibers'][1]),
                              'star_v_words':len(items[0]['formal_fibers'][2])}
                             for key,items in orbits.items()]}
    Path('stage47_star_avoid_results.json').write_text(
        json.dumps({'scope':'Fixed symbolic models, no residue search.',
                    'summary':summary,'models':results},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
