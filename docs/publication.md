# Typeset manuscript and versioned review releases

The PDF is generated from `PROOF.md`, its six supporting chapters, the
certificate contracts and the references. There is no separately maintained
LaTeX proof. The build creates a contents page, bookmarks, internal chapter
links and links to the canonical numbered lemmas. Code and certificate links
point to the exact source commit.

## Build the PDF

Install Pandoc, XeLaTeX and Poppler (`pdftotext` and `pdfinfo`). On Ubuntu:

```sh
sudo apt-get install pandoc texlive-xetex texlive-latex-extra poppler-utils
python -m verification.book
```

The output is `.verification/publication/proof.pdf`, accompanied by its build
log and a JSON report binding the PDF to the commit, source manifest and
individual Markdown inputs. `--allow-dirty` permits a local preview and marks
it as such; a preview cannot be used in a review release. Assertions are not
used to excuse missing build tools or failed TeX runs. Missing glyphs or
overfull boxes exceeding five TeX points fail the build. A successful build
is a typesetting check, not mathematical certification.

## Build a complete review bundle

Start from a clean full Git clone, with Python 3.12 or later and the PDF
tools above. Use a fresh output directory for archive recovery and release
packaging. The selected version is in [release.json](release.json).

```sh
mkdir -p .verification/publication
python verify.py --seconds-per-order 300 > .verification/publication/console.log 2>&1
python -m verification.evidence --console .verification/publication/console.log --exit-code 0 --output .verification/publication/verification.json.gz
python -m verification.book
python -m verification.regeneration recover --programs
python -m verification.regeneration generate --recipe all
python -m verification.release build --version v0.1.0-review.1
```

Export exit code zero only after the verification command actually succeeds;
the CI workflow captures the real exit code and retains incomplete runs.
Release packaging requires a completed fresh full run, zero reused orders,
a clean source commit and a PDF from that same commit and manifest.

The release directory contains the PDF, complete verification evidence,
`release.json`, `SHA256SUMS` and one self-contained `.tar.gz` review bundle.
The bundle includes the source tree and certificates, the PDF build report,
all generator logs and positive certificates, and the recovered historical
programs. Its metadata pins the source commit, Git tree, source manifest,
every certificate and every bundled file. Public text and extracted PDF
text are checked by the privacy scanner before packaging succeeds.

Check a downloaded bundle against the commit shown on its release page:

```sh
python -m verification.release verify cyclic-multiset-sums-v0.1.0-review.1.tar.gz --commit COMMIT_SHA
```

This checks artifact integrity and cross-file binding. Re-run `verify.py`
inside the bundled `source/` directory to check mathematical certificates.
The archive contains no Git database; offline early-certificate discovery
uses its hash-checked recovered programs:

```sh
cd source
python -m verification.regeneration generate --recipe all --programs ../regeneration/programs
```

## Automation and publication

The verification workflow builds a package for pull requests and `main`.
It retains the PDF/package and complete logs as separate workflow artifacts.
Only a push to `review/releases/VERSION`, matching `docs/release.json`,
publishes a **review prerelease**, after every build and verification step
succeeds. That job alone receives repository-content write permission.
Existing versions are never overwritten. A release is pinned to the pushed
commit; publication does not merge its branch.

The review status remains explicit: AI assistance and computational checks
are distinct from external human review and proof-assistant certification.
Discovery is reproducible for seven named positive-certificate files;
[the generation catalog](generation.json) lists the unresolved families.
