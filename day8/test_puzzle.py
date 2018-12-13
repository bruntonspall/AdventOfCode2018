import unittest
import puzzle


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(file("input.txt").read())
        answer = puzzle.solve(data)
        self.assertEqual(0, answer)

    def test_simple_parse(self):
        self.assertEqual(({"metadata": [], "children": []}, ''), puzzle.parse_node("0 0"))
        self.assertEqual(({"metadata": [1], "children": []}, ''), puzzle.parse_node("0 1 1"))
        self.assertEqual(({"metadata": [7], "children": []}, ''), puzzle.parse_node("0 1 7"))
        self.assertEqual(({"metadata": [7, 2], "children": []}, ''), puzzle.parse_node("0 2 7 2"))

    def test_parse(self):
        expected = {
            "metadata": [1, 1, 2],
            "children": [
                {
                    "metadata": [10, 11, 12],
                    "children": []
                },
                {
                    "metadata": [2],
                    "children": [
                        {
                            "metadata": [99],
                            "children": []
                        }
                    ]
                }
            ]
        }
        data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        self.assertEqual(expected, puzzle.parse(data))

    def test_simple_solve(self):
        self.assertEqual(9, puzzle.solve({"metadata": [7, 2], "children": []}))
        self.assertEqual(15, puzzle.solve({"metadata": [7, 2], "children": [
            {"metadata": [2, 2], "children": []},
            {"metadata": [1, 1], "children": []}
        ]}))

    def test_solve(self):
        data = {
            "metadata": [1, 1, 2],
            "children": [
                {
                    "metadata": [10, 11, 12],
                    "children": []
                },
                {
                    "metadata": [2],
                    "children": [
                        {
                            "metadata": [99],
                            "children": []
                        }
                    ]
                }
            ]
        }
        self.assertEqual(138, puzzle.solve(data))

if __name__ == '__main__':
    unittest.main()
