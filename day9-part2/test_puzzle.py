import unittest
import puzzle
import collections


class TestBasic(unittest.TestCase):
    def test_insert_marble(self):
        marbles = puzzle.create()
        marbles, score = puzzle.insert(marbles, 1)
        self.assertEqual(0, score)
        self.assertEqual([0, 1], list(marbles))

        marbles, score = puzzle.insert(marbles, 2)
        self.assertEqual(0, score)
        self.assertEqual([1, 0, 2], list(marbles))

        marbles, score = puzzle.insert(marbles, 3)
        self.assertEqual(0, score)
        self.assertEqual([0, 2, 1, 3], list(marbles))

        marbles, score = puzzle.insert(marbles, 4)
        self.assertEqual(0, score)
        self.assertEqual([2, 1, 3, 0, 4], list(marbles))

        marbles, score = puzzle.insert(marbles, 5)
        self.assertEqual(0, score)
        self.assertEqual([1, 3, 0, 4, 2, 5], list(marbles))

    def test_insert_marble_23(self):
        marbles = collections.deque([11, 1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22])
        marbles, score = puzzle.insert(marbles, 23)
        self.assertEqual(32, score)
        self.assertEqual([2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18, 19], list(marbles))

    def test_solve(self):
        self.assertEqual(32, puzzle.solve(9, 25))
        self.assertEqual(8317, puzzle.solve(10, 1618))
        self.assertEqual(146373, puzzle.solve(13, 7999))
        # self.assertEqual(2764, puzzle.solve(17, 1104))
        self.assertEqual(54718, puzzle.solve(21, 6111))
        self.assertEqual(37305, puzzle.solve(30, 5807))

    def test_pass(self):
        answer = puzzle.solve(465, 7149800)
        self.assertEqual(0, answer)


if __name__ == '__main__':
    unittest.main()
