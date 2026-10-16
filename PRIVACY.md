# Release privacy review

This release starts with fresh Git history and neutral author and committer
details. The original repository history, local Git configuration, private
review files, credentials and machine-specific artifacts are not included.

The private review checked all 463 source files and the decompressed contents
of 29 logical certificate archives, including the two reconstructed multipart
archives. It checked known personal names and account identifiers, email
addresses, home-directory paths and common credential formats. JSON string
values were checked after decoding. Historical source commit references were
removed from prose and optional Git provenance fields were removed from the
package manifest. Required SHA256 integrity hashes are preserved.

Two comments using a mathematical term that coincided with a private name
were reworded. The executable statements of all 152 original Python programs
are unchanged, and all certificate archive and multipart bytes are unchanged.
Documentation changes are reflected in the proof-package integrity manifest.

The release also includes a generic content scanner and six negative-control
tests. These detect common patterns, compressed personal-data fixtures,
Unicode-escaped identifiers and gzip header filenames. The private list of
identifiers used during review is intentionally excluded from this release.
No finite pattern scan guarantees the absence of every possible identifier.

Repository ownership, the account profile and pull-request activity remain
visible through the hosting service. Service-generated metadata is separate
from uploaded commit metadata. The research itself can be recognizable; this
release is not presented as anonymous.

The privacy review does not establish the mathematical theorem. The existing
proof's computer-assisted scope and human-review limitations remain explicit
in the proof and audit documents.
