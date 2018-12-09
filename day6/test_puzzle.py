import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(0, puzzle.distance((0, 0), (0, 0)))
        self.assertEqual(1, puzzle.distance((0, 0), (1, 0)))
        self.assertEqual(2, puzzle.distance((0, 0), (2, 0)))
        self.assertEqual(1, puzzle.distance((0, 0), (0, 1)))
        self.assertEqual(2, puzzle.distance((0, 0), (0, 2)))
        self.assertEqual(2, puzzle.distance((0, 0), (1, 1)))
        self.assertEqual(2, puzzle.distance((1, 2), (2, 3)))
        self.assertEqual(2, puzzle.distance((2, 2), (1, 1)))
        self.assertEqual(4, puzzle.distance((4, 0), (2, 2)))
        self.assertEqual(4, puzzle.distance((2, 2), (4, 0)))

    def test_find_closest_point(self):
        test_points = [(0, 0), (4, 0), (2, 2), (0, 4), (4, 4)]
        self.assertEqual(0, puzzle.find_closest_point(test_points, (0, 0)))
        self.assertEqual(0, puzzle.find_closest_point(test_points, (1, 0)))
        self.assertEqual(0, puzzle.find_closest_point(test_points, (0, 1)))
        self.assertEqual(2, puzzle.find_closest_point(test_points, (2, 2)))
        self.assertEqual(2, puzzle.find_closest_point(test_points, (1, 2)))
        self.assertEqual(2, puzzle.find_closest_point(test_points, (2, 3)))
        self.assertEqual(4, puzzle.find_closest_point(test_points, (4, 4)))
        self.assertEqual(4, puzzle.find_closest_point(test_points, (3, 4)))
        self.assertEqual(None, puzzle.find_closest_point(test_points, (2, 0)))
        self.assertEqual(2, puzzle.find_closest_point(test_points, (2, 1)))

    def test_find_valid_points(self):
        test_points = [(0, 0), (4, 0), (2, 2), (0, 4), (4, 4)]
        self.assertEqual({0: False, 1: False, 2: True, 3: False, 4: False}, puzzle.find_valid_points(test_points))
        test_points = [(1, 1), (1, 6), (8, 3), (3, 4),  (5, 5), (8, 9)]
        self.assertEqual({0: False, 1: False, 2: False, 3: True, 4: True, 5: False}, puzzle.find_valid_points(test_points))

    def test_count_nearest(self):
        test_points = [(0, 0), (4, 0), (2, 2), (0, 4), (4, 4)]
        self.assertEqual({2: 5}, puzzle.count(test_points))
        test_points = [(1, 1), (1, 6), (8, 3), (3, 4),  (5, 5), (8, 9)]
        self.assertEqual({3: 9, 4: 17}, puzzle.count(test_points))

    def test_pass(self):
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(3660, answer)


if __name__ == '__main__':
    unittest.main()
