import unittest
from caesar_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_full_rotation(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")

    def test_upper_wrap(self):
        self.assertEqual(caesarCipher("Z", 1), "A")

    def test_lower_wrap(self):
        self.assertEqual(caesarCipher("z", 1), "a")

    def test_with_symbol(self):
        self.assertEqual(caesarCipher("Hello-World", 4), "Lipps-Asvph")

    def test_zero_shift(self):
        self.assertEqual(caesarCipher("A", 0), "A")

if __name__ == "__main__":
    unittest.main()