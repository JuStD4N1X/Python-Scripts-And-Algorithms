import unittest
from main import encrypt


class TestCaesarCipher(unittest.TestCase):

    def test_basic_encryption(self):
        self.assertEqual(encrypt("abc", 3), "def")

    def test_alphabet_wrap(self):
        self.assertEqual(encrypt("xyz", 3), "abc")

    def test_decryption(self):
        self.assertEqual(encrypt("def", -3), "abc")

    def test_key_larger_than_alphabet(self):
        self.assertEqual(encrypt("abc", 29), "def")

    def test_text_with_spaces(self):
        self.assertEqual(encrypt("ab cd", 2), "cd ef")


if __name__ == '__main__':
    unittest.main()