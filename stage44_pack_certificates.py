"""Package saved shared-center evidence without restarting discovery."""
import gzip
import json
from pathlib import Path


def main():
    inventory = json.loads(Path('stage44_same_centers_results.json').read_text())
    growth = json.loads(Path('stage44_shared_growth_results.json').read_text())
    certificates = {}
    for result in growth['results']:
        name = result['certificate']
        certificates[name] = json.loads(gzip.decompress(Path(name).read_bytes()))
    packed = {'inventory': inventory, 'growth': growth, 'certificates': certificates}
    data = json.dumps(packed, separators=(',', ':')).encode()
    path = Path('stage44_certificates.json.gz')
    path.write_bytes(gzip.compress(data, mtime=0))
    print(json.dumps({'file': path.name, 'bytes': path.stat().st_size,
                      'symbolic_patterns': 2880, 'residual_certificates': len(certificates)}))


if __name__ == '__main__':
    main()
