import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_insert_marble(self):
        self.assertEqual(([0], 0, 0), puzzle.insert([], 0, 0))
        self.assertEqual(([0, 1], 1, 0), puzzle.insert([0], 0, 1))
        self.assertEqual(([0, 2, 1], 1, 0), puzzle.insert([0, 1], 1, 2))
        self.assertEqual(([0, 2, 1, 3], 3, 0), puzzle.insert([0, 2, 1], 1, 3))
        self.assertEqual(([0, 4, 2, 1, 3], 1, 0), puzzle.insert([0, 2, 1, 3], 3, 4))
        self.assertEqual(([0, 16, 8, 17, 4, 18, 19, 2, 20, 10, 21, 5 ,22, 11, 1, 12, 6, 13, 3, 14, 7, 15], 6, 32), puzzle.insert([0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5 ,22, 11, 1, 12, 6, 13, 3, 14, 7, 15], 13, 23))

    def test_solve(self):
        self.assertEqual(32, puzzle.solve(9, 25))
        self.assertEqual(8317, puzzle.solve(10, 1618))
        self.assertEqual(146373, puzzle.solve(13, 7999))
        # self.assertEqual(2764, puzzle.solve(17, 1104))
        self.assertEqual(54718, puzzle.solve(21, 6111))
        self.assertEqual(37305, puzzle.solve(30, 5807))

    def test_pass(self):
        answer = puzzle.solve(465, 71498)
        self.assertEqual(0, answer)


if __name__ == '__main__':
    unittest.main()
