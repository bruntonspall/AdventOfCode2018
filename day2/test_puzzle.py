import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_boxids(self):
        self.assertEqual((0, 0), puzzle.count_boxids("abcdef"))
        self.assertEqual((1, 1), puzzle.count_boxids("bababc"))
        self.assertEqual((1, 0), puzzle.count_boxids("abbcde"))
        self.assertEqual((0, 1), puzzle.count_boxids("abcccd"))
        self.assertEqual((1, 0), puzzle.count_boxids("aabcdd"))
        self.assertEqual((1, 0), puzzle.count_boxids("abcdee"))
        self.assertEqual((0, 1), puzzle.count_boxids("ababab"))

    def test_checksum(self):
        self.assertEqual(12, puzzle.checksum([(0, 0), (1, 1), (1, 0), (0, 1), (1, 0), (1, 0), (0, 1)]))

    def test_solve(self):
        lines = """abcdef
        bababc
        abbcde
        abcccd
        aabcdd
        abcdee
        ababab"""
        data = puzzle.parse(lines.split())
        answer = puzzle.solve(data)
        self.assertEqual(12, answer)

    def test_pass(self):
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(0, answer)


if __name__ == '__main__':
    unittest.main()
