import unittest
from funny_string import funnyString

class TestFunnyString(unittest.TestCase):

    def test_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_single_char(self):
        self.assertEqual(funnyString("a"), "Funny")

    def test_same_char(self):
        self.assertEqual(funnyString("aa"), "Funny")

    def test_middle_fail(self):
        self.assertEqual(funnyString("abc"), "Not Funny")

if __name__ == "__main__":
    unittest.main()