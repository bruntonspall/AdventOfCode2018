import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(4, puzzle.solve("dabAcCaCBAcCcaDA"))
        # self.assertEqual(0, puzzle.solve("a"*5000+"A"*5000))
        self.assertEqual(0, puzzle.solve("abBA"))


    def test_pass(self):
        data = file("input.txt").read(500000).strip()
        answer = puzzle.solve(data)
        self.assertEqual(0, answer)


if __name__ == '__main__':
    unittest.main()
