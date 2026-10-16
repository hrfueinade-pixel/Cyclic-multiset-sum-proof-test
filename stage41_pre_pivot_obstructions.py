"""Two fixed proof-step obstructions, not an exclusion search."""
import itertools
import json


def multiply(a,b):
    # F4=F2[t]/(t^2+t+1), with elements encoded by their two coefficients.
    a0,a1=a&1,a>>1
    b0,b1=b&1,b>>1
    return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1)


def main():
    n=255
    a=(0,1,3,7,15,31,63,127)
    copies=[]
    for origin in a:
        for point in a:
            if point==origin:
                continue
            direction=(point-origin)%n
            other=[(x-origin)%n for x in a if x not in (origin,point)]
            cube={sum(other[i] for i in range(6) if mask>>i&1)%n for mask in range(64)}
            union={(x+k*direction)%n for x in cube for k in range(4)}
            copies.append({'origin':origin,'point':point,'union_size':len(union)})
    vectors=[(1,0,0),(0,1,0),(0,0,1),(1,2,2),(2,1,2),(2,2,1)]
    entries=[]
    for indices in itertools.product(range(3),repeat=3):
        value=0
        for v in vectors:
            term=2  # coefficient omega
            for i in indices:
                term=multiply(term,v[i])
            value ^=term
        assert value==int(len(set(indices))==3)
        entries.append([indices,value])
    result={'four_copy_cube_binary_control':{'N':n,'A':a,
             'origin_direction_pairs':len(copies),'maximum_union_size':max(x['union_size'] for x in copies),
             'pairs':copies,'boundary':'Historical valid N=255 control; refutes a universal 248-point packing claim, not the conditional small-order theorem.'},
            'characteristic_two_symmetric_decomposition':{'field':'F4, omega^2=omega+1','coefficient':2,
             'vectors':vectors,'tensor_entries':entries,'terms':6,
             'boundary':'Refutes the proposed general bound symmetric_rank(det_n)>=2^n-1 at n=3. It does not refute an n=8 bound or give a cyclic counterexample.'}}
    with open('stage41_pre_pivot_obstructions_results.json','w',encoding='utf-8') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print(json.dumps({'four_copy_maximum':max(x['union_size'] for x in copies),
                      'F4_six_term_identity_entries_checked':len(entries)},indent=2))


if __name__=='__main__':
    main()
