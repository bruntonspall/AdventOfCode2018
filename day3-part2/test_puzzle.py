import unittest
import puzzle


class TestBasic(unittest.TestCase):

    def test_parseline(self):
        self.assertEqual(('#1', {'id': '#1', 'x': 1, 'y': 3, 'width': 4, 'height': 4}), puzzle.parse_line('#1 @ 1,3: 4x4'))

    def test_parse(self):
        words = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2""".split('\n')
        data = puzzle.parse(words)
        self.assertEqual(data['#1'], {'id': '#1', 'x': 1, 'y': 3, 'width': 4, 'height': 4})
        self.assertEqual(data['#2'], {'id': '#2', 'x': 3, 'y': 1, 'width': 4, 'height': 4})
        self.assertEqual(data['#3'], {'id': '#3', 'x': 5, 'y': 5, 'width': 2, 'height': 2})

    def test_apply(self):
        data = [{'id': '#1', 'x': 1, 'y': 3, 'width': 4, 'height': 4}]
        map = {}
        self.assertEqual(
            {(1, 3): ['#1'], (2, 3): ['#1'], (3, 3): ['#1'], (4, 3): ['#1'],
             (1, 4): ['#1'], (2, 4): ['#1'], (3, 4): ['#1'], (4, 4): ['#1'],
             (1, 5): ['#1'], (2, 5): ['#1'], (3, 5): ['#1'], (4, 5): ['#1'],
             (1, 6): ['#1'], (2, 6): ['#1'], (3, 6): ['#1'], (4, 6): ['#1']},
            puzzle.apply(map, data)
        )

    def test_solve(self):
        data = {'#1': {'id': '#1', 'x': 1, 'y': 3, 'width': 4, 'height': 4},
                '#2': {'id': '#2', 'x': 3, 'y': 1, 'width': 4, 'height': 4},
                '#3': {'id': '#3', 'x': 5, 'y': 5, 'width': 2, 'height': 2}}
        self.assertEqual('#3', puzzle.solve(data))

    def test_pass(self):
        data = puzzle.parse(file("input.txt").readlines())
        answer = puzzle.solve(data)
        self.assertEqual('#504', answer)


if __name__ == '__main__':
    unittest.main()
