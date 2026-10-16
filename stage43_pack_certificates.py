"""Package already discovered positive witnesses without repeating discovery."""
import gzip
import json
from pathlib import Path


def main():
    certificates = {path.name:json.loads(gzip.decompress(path.read_bytes()))
                    for path in sorted(Path('.').glob('stage43_*_certificate.json.gz'))}
    assert certificates
    data = json.dumps({'certificates':certificates},separators=(',',':')).encode()
    target = Path('stage43_certificates.json.gz')
    target.write_bytes(gzip.compress(data,mtime=0))
    print(json.dumps({'certificates':len(certificates),'compressed_bytes':target.stat().st_size}))


if __name__ == '__main__':
    main()
