import unittest
from main import encrypt

class TestGaderypolukiCipher(unittest.TestCase):

    def test_encryption_works(self):
        result = encrypt("ROMEO")
        self.assertEqual(result, "YPMDP")


if __name__ == '__main__':
    unittest.main()
