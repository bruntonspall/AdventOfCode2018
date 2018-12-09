import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_count_nearest(self):
        test_points = [(1, 1), (1, 6), (8, 3), (3, 4),  (5, 5), (8, 9)]
        self.assertEqual(16, puzzle.count(test_points, 32))

    def test_pass(self):
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(35928, answer)


if __name__ == '__main__':
    unittest.main()
