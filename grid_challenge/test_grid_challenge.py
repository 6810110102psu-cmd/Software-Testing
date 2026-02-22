import unittest
from grid_challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):

    def test_example_yes(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_example_no(self):
        grid = ["mpxz", "abcd", "wlmf"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_simple_yes(self):
        grid = ["abc", "ade", "efg"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_single_cell(self):
        grid = ["z"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_column_fail(self):
        grid = ["ba", "aa"]
        self.assertEqual(gridChallenge(grid), "NO")

if __name__ == "__main__":
    unittest.main()