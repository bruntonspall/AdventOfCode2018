import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_parse(self):
        input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""
        expected = {
            "A": set(["C"]),
            "B": set(["A"]),
            "C": set(),
            "D": set(["A"]),
            "E": set(["B", "D", "F"]),
            "F": set(["C"])
        }
        self.assertEqual(expected, puzzle.parse(input.split("\n")))

    def test_find_next(self):
        data = {
            "A": set(["C"]),
            "B": set(["A"]),
            "C": set(),
            "D": set(["A"]),
            "E": set(["B", "D", "F"]),
            "F": set(["C"])
        }
        self.assertEqual("C", puzzle.find_next(data, set()))
        self.assertEqual("A", puzzle.find_next(data, set("C")))
        self.assertEqual("B", puzzle.find_next(data, set(["C", "A"])))
        self.assertEqual("D", puzzle.find_next(data, set(["C", "A", "B"])))
        self.assertEqual("F", puzzle.find_next(data, set(["C", "A", "B", "D"])))
        self.assertEqual("E", puzzle.find_next(data, set(["C", "A", "B", "D", "F"])))
        self.assertEqual(None, puzzle.find_next(data, set(["C", "A", "B", "D", "F", "E"])))

    def test_traverse(self):
        data = {
            "A": set(["C"]),
            "B": set(["A"]),
            "C": set(),
            "D": set(["A"]),
            "E": set(["B", "D", "F"]),
            "F": set(["C"])
        }
        self.assertEqual("CABDFE", "".join(puzzle.traverse(data)))

    def test_pass(self):
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.traverse(data)
        self.assertEqual(0, "".join(answer))


if __name__ == '__main__':
    unittest.main()
