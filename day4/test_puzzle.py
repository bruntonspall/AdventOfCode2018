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

    def test_solve(self):
        data = {
            (10, 11, 1, 5): 20,
            (10, 11, 1, 30): 25,
            (99, 11, 2, 40): 10,
            (10, 11, 3, 24): 5,
            (99, 11, 4, 36): 10,
            (99, 11, 5, 45): 10}
        answer = puzzle.solve(data)
        self.assertEqual(240, answer)
        pass

    def test_pass(self):
        pass
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(38813, answer)


if __name__ == '__main__':
    unittest.main()
