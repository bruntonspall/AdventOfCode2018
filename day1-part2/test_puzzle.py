import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_basic_parse(self):
        data = puzzle.parse('''+1
        +13
        +2'''.split())
        self.assertEqual([1, 13, 2], data)

    def test_basic_solve(self):
        data = [1, -2, 3, 1]
        self.assertEqual(2, puzzle.solve(data))
        data = [+3, +3, +4, -2, -4]
        self.assertEqual(10, puzzle.solve(data))
        data = [+1, -1]
        self.assertEqual(0, puzzle.solve(data))
        data = [-6, +3, +8, +5, -6]
        self.assertEqual(5, puzzle.solve(data))
        data = [+7, +7, -2, -7, -4]
        self.assertEqual(14, puzzle.solve(data))

    def test_pass(self):
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(0, answer)


if __name__ == '__main__':
    unittest.main()
