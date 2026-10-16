"""Independent arithmetic for the regular-branch contradiction."""
import json
from pathlib import Path
from time import monotonic

def parts(n,cap):
    if n==0: yield ()
    for x in range(1,min(n,cap)+1):
        for tail in parts(n-x,x): yield (x,)+tail

def main():
    start=monotonic()
    partitions=list(parts(7,5))
    assert monotonic()-start<10
    values=[sum(x*(x-1)//2 for x in p) for p in partitions]
    assert max(values)==11
    table=[]
    for c in range(5):
        lower=(152+2*c+2)//3; upper=29+20+c
        assert lower>upper
        assert 152+2*c-(147+3*c)==5-c>0
        table.append({'c2':c,'minimum_C_from_short_paths':lower,
                      'maximum_C_outside_affine_family':upper,'contradiction':True})
    data={'completion':'COMPLETE','seconds_limit':10,'elapsed_seconds':monotonic()-start,
          'partitions':partitions,'incoming_pair_maximum':11,'cases':table,
          'scope':'Integer arithmetic only; structural premises are proved in the report.'}
    Path('stage24_arithmetic_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='partitions'},indent=2))

if __name__=='__main__': main()
