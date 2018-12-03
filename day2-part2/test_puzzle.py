import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(2, puzzle.distance("abcde", "axcye"))
        self.assertEqual(1, puzzle.distance("fghij", "fguij"))

    def test_differs_by_one(self):
        self.assertEqual(False, puzzle.differs_by_one("abcde", "axcye"))
        self.assertEqual(True, puzzle.differs_by_one("fghij", "fguij"))
        self.assertEqual(False, puzzle.differs_by_one("abcde", "edcbz"))
        self.assertEqual(True, puzzle.differs_by_one("abcde", "zbcde"))

    def test_sameletters(self):
        self.assertEqual("fgij", puzzle.sameletters("fghij", "fguij"))
        self.assertEqual("bcde", puzzle.sameletters("abcde", "zbcde"))

    def test_solve(self):
        lines = """abcde
        abcef
fghij
klmno
pqrst
fguij
axcye
wvxyz"""
        data = puzzle.parse(lines.split())
        answer = puzzle.solve(data)
        self.assertEqual("fgij", answer)

    def test_pass(self):
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(0, answer)


if __name__ == '__main__':
    unittest.main()
