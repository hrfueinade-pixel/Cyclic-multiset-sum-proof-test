"""Audit regression controls: exclusion strength and incomplete-run exits.

Quartic controls use genuine certificate identities. Parity controls replace
only the run function in temporary copies to exercise exit/status behavior;
their synthetic complete reports are NOT mathematical exclusion evidence.
Run with assertions enabled. Canonical archives/results are not changed.
"""
from pathlib import Path
from itertools import combinations
import ast,contextlib,gzip,importlib.util,io,json,os,shutil,subprocess,sys,tempfile


def main():
    if not __debug__:raise RuntimeError('Assertions must be enabled for proof verification.')
    root=Path(__file__).resolve().parent
    spec=importlib.util.spec_from_file_location('stage42_hardened',root/'stage42_certificate_check.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    certificates=sorted(root.glob('stage42_*_certificate.json.gz'));assert certificates
    quartic=[];parity=[]
    with tempfile.TemporaryDirectory(prefix='.stage64-check-',dir=root)as name:
        work=Path(name).resolve();assert work.is_relative_to(root)
        for target in(87,88,89,94):
            case=work/str(target);case.mkdir();found=0
            for path in certificates:
                data=json.loads(gzip.decompress(path.read_bytes()))
                if data['model']=='exception3'and data['degree']==4:
                    found+=1;n=len(data['words']);assert n==94
                    data['pairs']=[w for(i,j),w in zip(combinations(range(n),2),data['pairs'])if j<target]
                    data['words']=data['words'][:target]
                    (case/path.name).write_bytes(gzip.compress(json.dumps(data).encode()))
                else:shutil.copyfile(path,case/path.name)
            assert found==1;before=Path.cwd();accepted=False
            try:
                os.chdir(case)
                with contextlib.redirect_stdout(io.StringIO()):
                    try:module.main();accepted=True
                    except AssertionError:pass
            finally:os.chdir(before)
            assert accepted==(target>=89)
            quartic.append({'values':target,'accepted':accepted,'bound':71+2*target})
        for stage in(32,34):
            file=root/('stage32_even_independent.py'if stage==32 else 'stage34_seven_sum_independent.py')
            for incomplete in(False,True):
                case=work/(str(stage)+('_incomplete'if incomplete else '_complete'));case.mkdir()
                if stage==32:
                    reports=[{'M':m,'counts':{'B_blocks':0,'proper_saturated':0,'C_shapes':0}}for m in range(94,124)]
                    (case/'stage32_high_orders_results.json').write_text(json.dumps({'reports':reports}))
                    (case/'stage32_lower_orders_results.json').write_text(json.dumps({'reports':[]}))
                    body="return {'M':m,'completion':'COMPLETE','counts':{'B_blocks':0,'proper_saturated':0,'C_shapes':0}}"
                    output='stage32_even_independent_results.json'
                else:
                    (case/'stage34_combined_results.json').write_text(json.dumps({'completion':'COMPLETE','survivors':[]}))
                    body="return {'M':m,'completion':'COMPLETE','prefix_counts':[0],'survivors':0}"
                    output='stage34_seven_sum_independent_results.json'
                tree=ast.parse(file.read_text());replacements=0
                for node in tree.body:
                    if isinstance(node,ast.FunctionDef)and node.name=='run':
                        node.body=ast.parse('raise TimeoutError()'if incomplete else body).body;replacements+=1
                assert replacements==1
                target=case/file.name;target.write_text(ast.unparse(ast.fix_missing_locations(tree))+'\n')
                result=subprocess.run([sys.executable,'-B',str(target)],cwd=case,capture_output=True,text=True,timeout=15)
                status=json.loads((case/output).read_text())
                assert result.returncode==(2 if incomplete else 0),(result.returncode,result.stderr)
                assert status['completion']==('TIMEOUT/incomplete'if incomplete else 'COMPLETE')
                expected=[]if incomplete else list(range(123,93,-1))if stage==32 else list(range(64,124))
                assert status['completed_orders']==expected
                parity.append({'stage':stage,'synthetic_control':'timeout'if incomplete else 'complete',
                               'exit_code':result.returncode,'completion':status['completion']})
    out={'quartic_threshold_controls':quartic,'parity_exit_controls':parity,
         'scope':'Genuine positive quartic certificates; synthetic parity exit-path controls, not new parity exclusions.'}
    (root/'stage64_verifier_hardening_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':main()
