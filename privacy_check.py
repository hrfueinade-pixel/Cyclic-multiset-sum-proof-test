"""Check release files and gzip payloads for common personal-data patterns.

Run from a clean checkout with Python 3. This is a file-content check;
hosting-account identity and service-generated metadata are outside its scope.
"""
from __future__ import annotations

import gzip
import json
from pathlib import Path
import re
import sys

PATTERNS = {
    'email': r'(?i)\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b',
    'windows_home': r'(?i)\b[A-Z]:[\\/]+Users[\\/]+[^\s"<>|]+',
    'unix_home': r'/(?:home|Users)/[^\s"<>|]+',
    'private_key': r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',
    'github_token': r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b',
    'provider_key': r'\bsk-(?:proj-|or-v1-)?[A-Za-z0-9_\-]{24,}\b',
    'aws_key': r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
}
EXCLUDED = {'.git', '__pycache__', '.venv', 'venv'}


def text_findings(name: str, text: str) -> list[dict]:
    # Expand JSON Unicode escapes and escaped slashes without interpreting
    # arbitrary source text as executable code or needing a large object tree.
    expanded = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m[1], 16)), text)
    expanded = expanded.replace('\\/', '/')
    return [
        {'file': name, 'line': expanded.count('\n', 0, m.start()) + 1, 'kind': kind}
        for kind, pattern in PATTERNS.items()
        for m in re.finditer(pattern, expanded)
    ]


def gzip_header_text(raw: bytes) -> str:
    if raw[:3] != b'\x1f\x8b\x08' or len(raw) < 10:
        raise ValueError('Invalid gzip header')
    flags = raw[3]
    pos = 10
    if flags & 4:
        size = int.from_bytes(raw[pos:pos + 2], 'little')
        pos += 2 + size
    fields = []
    for flag in (8, 16):
        if flags & flag:
            end = raw.index(b'\0', pos)
            fields.append(raw[pos:end].decode('latin-1'))
            pos = end + 1
    return '\n'.join(fields)


def payload_findings(name: str, raw: bytes, compressed: bool = False) -> list[dict]:
    findings = []
    if compressed:
        findings += text_findings(name + '::gzip-header', gzip_header_text(raw))
        raw = gzip.decompress(raw)
    return findings + text_findings(name, raw.decode('utf-8-sig'))


def scan(root: Path) -> dict:
    paths = sorted(p for p in root.rglob('*') if p.is_file()
                   and not any(part in EXCLUDED for part in p.relative_to(root).parts))
    relative = {p.relative_to(root).as_posix(): p for p in paths}
    findings = []
    archives = 0
    for name, path in relative.items():
        findings += text_findings(name, name)
        if '.gz.part' in name:
            continue
        try:
            findings += payload_findings(name, path.read_bytes(), name.endswith('.gz'))
        except (UnicodeDecodeError, ValueError, OSError, EOFError):
            findings.append({'file': name, 'line': 0, 'kind': 'uninspected_payload'})
        archives += name.endswith('.gz')
    for base in sorted({name.split('.part')[0] for name in relative if '.gz.part' in name}):
        parts = sorted(name for name in relative if name.startswith(base + '.part'))
        expected = [base + '.part' + str(i).zfill(3) for i in range(len(parts))]
        if parts != expected:
            findings.append({'file': base, 'line': 0, 'kind': 'missing_archive_part'})
            continue
        try:
            raw = b''.join(relative[name].read_bytes() for name in parts)
            findings += payload_findings(base + '::reconstructed', raw, True)
        except (UnicodeDecodeError, ValueError, OSError, EOFError):
            findings.append({'file': base, 'line': 0, 'kind': 'uninspected_archive'})
        archives += 1
    return {'files_checked': len(paths), 'logical_gzip_archives': archives,
            'findings': findings, 'scope': 'Common file-content patterns; not an anonymity guarantee.'}


def main() -> int:
    result = scan(Path(__file__).resolve().parent)
    print(json.dumps(result, indent=2))
    return 1 if result['findings'] else 0


if __name__ == '__main__':
    sys.exit(main())
