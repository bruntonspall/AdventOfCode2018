import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_has_pair(self):
        self.assertTrue(puzzle.has_pair("abBA"))
        self.assertTrue(puzzle.has_pair("aA"))
        self.assertTrue(puzzle.has_pair("bB"))
        self.assertTrue(puzzle.has_pair("dabAcCaCBAcCcaDA"))
        self.assertTrue(puzzle.has_pair("dabAaCBAcCcaDA"))
        self.assertTrue(puzzle.has_pair("dabCBAcCcaDA"))

        self.assertFalse(puzzle.has_pair("dabCBAcaDA"))
        self.assertFalse(puzzle.has_pair("abAB"))
        self.assertFalse(puzzle.has_pair("aabAAB"))

    def test_reduce(self):
        self.assertEqual("aA", puzzle.do_reduce("abBA"))
        self.assertEqual("", puzzle.do_reduce("aA"))
        self.assertEqual("", puzzle.do_reduce("bB"))
        self.assertEqual("dabAaCBAcCcaDA", puzzle.do_reduce("dabAcCaCBAcCcaDA"))
        self.assertEqual("dabCBAcCcaDA", puzzle.do_reduce("dabAaCBAcCcaDA"))
        self.assertEqual("dabCBAcaDA", puzzle.do_reduce("dabCBAcCcaDA"))

        self.assertEqual("abAB", puzzle.do_reduce("abAB"))

    def test_solve(self):
        self.assertEqual(10, len(puzzle.solve("dabAcCaCBAcCcaDA")))
        self.assertEqual(0, len(puzzle.solve("abBA")))


    def test_pass(self):
        data = file("input.txt").read(500000).strip()
        answer = puzzle.solve(data)
        self.assertEqual(0, len(answer))


if __name__ == '__main__':
    unittest.main()
