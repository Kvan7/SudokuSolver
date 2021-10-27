import unittest
import simple_solver
import numpy as np


class TestSimpleSolver(unittest.TestCase):
    def test_no_blanks(self):
        area = np.array([[1, 2, 3], [4, 5, 6]])
        self.assertTrue(simple_solver.get_first_blank(area) is None)

    def test_find_blank(self):
        area = np.array([[1, 0, 3], [4, 5, 6]])
        self.assertTrue(simple_solver.get_first_blank(area) == (0, 1))

    def test_find_first_blank(self):
        area = np.array([[1, 0, 0], [4, 5, 6]])
        self.assertTrue(simple_solver.get_first_blank(area) == (0, 1))

    def test_find_blank_second_row(self):
        area = np.array([[1, 4, 3], [0, 5, 0]])
        self.assertTrue(simple_solver.get_first_blank(area) == (1, 0))

    def test_valid_numbers(self):
        area = np.array([[1, 4, 3], [0, 5, 0], [7, 2, 9]])
        valid = simple_solver.get_valid_numbers((1, 0), area)
        self.assertTrue(valid == {6, 8})

    def test_valid_numbers_all(self):
        area = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        valid = simple_solver.get_valid_numbers((1, 0), area)
        self.assertTrue(valid == {1, 2, 3, 4, 5, 6, 7, 8, 9})


if __name__ == '__main__':
    unittest.main()
