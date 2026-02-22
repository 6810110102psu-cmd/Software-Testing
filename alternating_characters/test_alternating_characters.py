import unittest
from alternating_characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):

    def test_all_same_A(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_all_same_B(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)

    def test_alternating(self):
        self.assertEqual(alternatingCharacters("ABABAB"), 0)

    def test_grouped(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_single_char(self):
        self.assertEqual(alternatingCharacters("A"), 0)

    def test_middle_duplicate(self):
        self.assertEqual(alternatingCharacters("ABBA"), 1)

if __name__ == "__main__":
    unittest.main()