import unittest
import re
from pypassword import Password
from passlib.hash import sha512_crypt
class TestPassword(unittest.TestCase):

    def test_default_car(self):
        """Return true if password lenght = 16
        """
        pw = Password()
        pw.generate()
        self.assertEqual(len(pw.getpass_plain_text()), 16)

    def test_custom_lenght(self):
        """Return true if password lenght = 16
        """
        lenght = 30
        pw = Password(lenght)
        pw.generate()
        self.assertEqual(len(pw.getpass_plain_text()), 30)

    def test_check_var_type(self):
        """Return true if type are correct
        """
        pw = Password()
        pw.generate()
        self.assertEqual(type(pw.getpass()), dict, "Should be a dict")
        self.assertEqual(type(pw.getpass_plain_text()), str, "Should be a string")
        self.assertEqual(type(pw.getpass_md5()), str, "Should be a string")
        self.assertEqual(type(pw.getpass_sha256()), str, "Should be a string")

    def test_get_md5(self):
        """Return true if getpass_md5() is matching regex '^[0-9a-fA-F]{32}$'
        """
        pw = Password()
        pw.generate()
        regex_match = re.match("^[0-9a-fA-F]{32}$", pw.getpass_md5())
        self.assertEqual(pw.getpass_md5(), regex_match.group(), "Did not match '^[0-9a-fA-F]{32}$' regex")

    def test_get_sha256(self):
        """Return true if getpass_sha256() is matching regex '^[A-Fa-f0-9]{64}$'
        """
        pw = Password()
        pw.generate()
        regex_match = re.match("^[A-Fa-f0-9]{64}$", pw.getpass_sha256())
        self.assertEqual(pw.getpass_sha256(), regex_match.group(), "Did not match '^[A-Fa-f0-9]{64}$' regex")

    def test_get_sha512_crypt(self):
        """Return true if getpass_sha512_crypt() is correctly encrypted
        """
        pw = Password()
        pw.generate()
        self.assertTrue(sha512_crypt.identify(pw.getpass_sha512_crypt()), "Is not a sha512 encrypted password")
if __name__ == "__main__":
    unittest.main(verbosity=2)