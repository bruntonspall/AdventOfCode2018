import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(10, len(puzzle.solve("dabAcCaCBAcCcaDA")))
        self.assertEqual(0, len(puzzle.solve("a"*5000+"A"*5000)))
        self.assertEqual(0, len(puzzle.solve("abBA")))


    def test_pass(self):
        data = file("input.txt").read(500000).strip()
        answer = puzzle.solve(data)
        self.assertEqual(0, len(answer))


if __name__ == '__main__':
    unittest.main()
