import unittest
from two_characters import alternate

class TestTwoCharacters(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_all_same(self):
        self.assertEqual(alternate("aaaa"), 0)

    def test_perfect_alternating(self):
        self.assertEqual(alternate("ababab"), 6)

    def test_two_chars_only(self):
        self.assertEqual(alternate("ab"), 2)

    def test_multiple_choices(self):
        self.assertEqual(alternate("abcabc"), 4)

    def test_single_char(self):
        self.assertEqual(alternate("a"), 0)

if __name__ == "__main__":
    unittest.main()