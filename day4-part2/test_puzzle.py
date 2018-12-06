import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_parse(self):
        contents = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
        expected = {
                (10, 11, 1, 5): 20,
                (10, 11, 1, 30): 25,
                (99, 11, 2, 40): 10,
                (10, 11, 3, 24): 5,
                (99, 11, 4, 36): 10,
                (99, 11, 5, 45): 10}
        # self.assertEqual(expected, puzzle.parse(contents.split('\n')))

    def test_parse_out_of_order(self):
        contents = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:30] falls asleep
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:29] wakes up
[1518-11-01 00:25] wakes up
[1518-11-01 00:55] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
        expected = {
            (10, 11, 1, 5): 20,
            (10, 11, 1, 30): 25,
            (99, 11, 2, 40): 10,
            (10, 11, 3, 24): 5,
            (99, 11, 4, 36): 10,
            (99, 11, 5, 45): 10}
        self.assertEqual(expected, puzzle.parse(contents.split('\n')))

    def test_most_asleep(self):
        data = {
            (10, 11, 1, 5): 20,
            (10, 11, 1, 30): 25,
            (99, 11, 2, 40): 10,
            (10, 11, 3, 24): 5,
            (99, 11, 4, 36): 10,
            (99, 11, 5, 45): 10}
        answer = puzzle.most_asleep(data)
        self.assertEqual(10, answer)
        pass

    def test_most_asleep_during(self):
        data = {
            (10, 11, 1, 5): 20,
            (10, 11, 1, 30): 25,
            (99, 11, 2, 40): 10,
            (10, 11, 3, 24): 5,
            (99, 11, 4, 36): 10,
            (99, 11, 5, 45): 10}
        answer = puzzle.most_asleep_during(data, 10)
        self.assertEqual(24, answer)
        pass

    def test_asleep_at(self):
        data = {
            (10, 11, 1, 5): 20,
            (10, 11, 1, 30): 25,
            (99, 11, 2, 40): 10,
            (10, 11, 3, 24): 5,
            (99, 11, 4, 36): 10,
            (99, 11, 5, 45): 10,
            (10, 11, 6, 5): 2,
            (10, 11, 6, 15): 3
            }
        # Which minutes was guard 10 asleep at on the 3rd?
        self.assertEqual([24, 25, 26, 27, 28], puzzle.asleep_at(data, 10, 3))
        self.assertEqual([36, 37, 38, 39, 40, 41, 42, 43, 44, 45], puzzle.asleep_at(data, 99, 4))
        self.assertEqual([5, 6, 15, 16, 17], puzzle.asleep_at(data, 10, 6))

    def test_asleep_minutes(self):
        data = {
            (10, 11, 6, 5): 2,
            (10, 11, 6, 15): 3,
            (99, 11, 6, 6): 3,
            (99, 11, 6, 22): 3,
            (10, 10, 6, 31): 1,
            (99, 10, 6, 24): 1
            }
        self.assertEqual({10: [5, 6, 31, 15, 16, 17], 99: [24, 6, 7, 8, 22, 23, 24]}, puzzle.asleep_minutes(data))
        self.assertEqual((99, 24), puzzle.most_asleep_minute(data))

        data = {
            (10, 11, 1, 5): 20,
            (10, 11, 1, 30): 25,
            (99, 11, 2, 40): 10,
            (10, 11, 3, 24): 5,
            (99, 11, 4, 36): 10,
            (99, 11, 5, 45): 10}
        self.assertEqual((99, 45), puzzle.most_asleep_minute(data))


    def test_solve(self):
        data = {
            (10, 11, 1, 5): 20,
            (10, 11, 1, 30): 25,
            (99, 11, 2, 40): 10,
            (10, 11, 3, 24): 5,
            (99, 11, 4, 36): 10,
            (99, 11, 5, 45): 10}
        answer = puzzle.solve(data)
        self.assertEqual(4455, answer)
        pass

    def test_pass(self):
        pass
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(38813, answer)


if __name__ == '__main__':
    unittest.main()
