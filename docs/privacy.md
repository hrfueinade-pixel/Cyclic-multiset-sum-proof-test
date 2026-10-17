# Privacy of the release

The release excludes local logs, temporary work, account profiles, and the
original Git history. The public scanner checks plain and compressed text,
escaped JSON strings, gzip original-file headers, common credentials, email
addresses, and computer home paths. Its tests include deliberate negative
controls. The private review also uses a local identifier list; that list is
not published.

This is a content review, not a promise of anonymity. Repository ownership,
pull-request activity, platform-generated merge metadata, timestamps, and the
recognizable mathematics can link the work to its account. That account
visibility was accepted for this release. Neutral uploaded commit identity
does not hide the repository owner. Hashes in the source map identify file
contents and may link matching public copies.

Run `python privacy_check.py` to repeat the public content checks. Generated
`.verification/` output is excluded from publication and should remain local.
