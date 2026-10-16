"""Negative controls for the public release-content scanner."""
import gzip
import io
import unittest

from privacy_check import payload_findings, text_findings


class PrivacyControls(unittest.TestCase):
    def test_home_paths(self):
        windows = 'C:' + chr(92) + 'Users' + chr(92) + 'Example' + chr(92) + 'proof.py'
        unix = '/' + 'home' + '/' + 'example' + '/proof.py'
        self.assertTrue(text_findings('fixture', windows))
        self.assertTrue(text_findings('fixture', unix))

    def test_email_and_unicode_escape(self):
        address = 'example' + '@' + 'example.invalid'
        encoded = address.replace('@', chr(92) + 'u0040')
        self.assertTrue(text_findings('fixture', address))
        self.assertTrue(text_findings('fixture', encoded))

    def test_compressed_personal_data(self):
        text = ('example' + '@' + 'example.invalid').encode()
        self.assertTrue(payload_findings('fixture.gz', gzip.compress(text), True))

    def test_gzip_original_filename(self):
        address = 'example' + '@' + 'example.invalid'
        output = io.BytesIO()
        with gzip.GzipFile(filename=address, mode='wb', fileobj=output, mtime=0) as stream:
            stream.write(b'clean payload')
        self.assertTrue(payload_findings('fixture.gz', output.getvalue(), True))

    def test_credentials(self):
        candidates = ['gh' + 'p_' + 'a' * 36, 'sk' + '-proj-' + 'b' * 32,
                      'AK' + 'IA' + 'X' * 16,
                      '-----BEGIN ' + 'PRIVATE KEY-----']
        self.assertTrue(all(text_findings('fixture', text) for text in candidates))

    def test_mathematical_data_is_accepted(self):
        self.assertEqual(text_findings('fixture', '2N >= 495; N <= 247; sha256=' + 'a' * 64), [])


if __name__ == '__main__':
    unittest.main()
