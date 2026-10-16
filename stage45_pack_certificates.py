"""Pack saved mixed-fiber evidence, without repeating discovery."""
import gzip
import json
from pathlib import Path


def main():
    counter = json.loads(Path('stage45_counterexample_results.json').read_text())
    packed = {
        'inventory': json.loads(gzip.decompress(Path('stage45_five_label_311_inventory.json.gz').read_bytes())),
        'counterexample': counter,
        'growth_certificate': json.loads(gzip.decompress(Path(counter['growth']['certificate']).read_bytes())),
        'embedding_diagnostic': json.loads(Path('stage45_residual_embeddings_results.json').read_text()),
    }
    path = Path('stage45_certificates.json.gz')
    path.write_bytes(gzip.compress(json.dumps(packed, separators=(',', ':')).encode(), mtime=0))
    print(json.dumps({'file': path.name, 'bytes': path.stat().st_size}))


if __name__ == '__main__':
    main()
