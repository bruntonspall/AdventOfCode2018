import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_parse(self):
        contents = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:08] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:35] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:42] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:34] falls asleep
[1518-11-03 00:35] wakes up"""
        # instead of (guardid, month, day, minute), I only ever use minute and guardid
        # So what if I parse into guard/minute pairs, for each minute asleep?
        expected = [(10, 5), (10, 6), (10, 7),
                    (10, 30), (10, 31), (10, 32), (10, 33), (10, 34),
                    (99, 40), (99, 41),
                    (10, 34)]
        self.assertEqual(expected, puzzle.parse(contents.split('\n')))

    def test_asleep_minutes(self):
        data = [(10, 5), (10, 6), (10, 7),
                (10, 30), (10, 31), (10, 32), (10, 33), (10, 34),
                (99, 40), (99, 41),
                (10, 34)]
        self.assertEqual((10, 34), puzzle.most_asleep_minute(data))

    def test_solve(self):
        data = [(10, 5), (10, 6), (10, 7),
                (10, 30), (10, 31), (10, 32), (10, 33), (10, 34),
                (99, 40), (99, 41),
                (10, 34)]
        answer = puzzle.solve(data)
        self.assertEqual(10*34, answer)
        pass

    def test_pass(self):
        pass
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(141071, answer)


if __name__ == '__main__':
    unittest.main()
