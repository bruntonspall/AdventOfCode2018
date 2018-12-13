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

    def test_find_next_with_in_use(self):
        data = {
            "A": set(["C"]),
            "B": set(["A"]),
            "C": set(),
            "D": set(["A"]),
            "E": set(["B", "D", "F"]),
            "F": set(["C"])
        }
        self.assertEqual("A", puzzle.find_next(data, set("C"), set()))
        self.assertEqual("F", puzzle.find_next(data, set("C"), set('A')))
        self.assertEqual(None, puzzle.find_next(data, set("C"), set(['A', 'F'])))
        self.assertEqual("B", puzzle.find_next(data, set(["C", "A"]), set('F')))
        self.assertEqual("D", puzzle.find_next(data, set(["C", "A"]), set(['F', "B"])))

    def test_traverse(self):
        data = {
            "A": set(["C"]),
            "B": set(["A"]),
            "C": set(),
            "D": set(["A"]),
            "E": set(["B", "D", "F"]),
            "F": set(["C"])
        }
        answer = puzzle.traverse(data, 2, 0)
        self.assertEqual("CABFDE", "".join(answer[0]))
        self.assertEqual(15, answer[1])

    def test_pass(self):
        data = puzzle.parse(file("input.txt").readlines())
        answer, t = puzzle.traverse(data, 5, 60)
        self.assertEqual(0, t)


if __name__ == '__main__':
    unittest.main()
