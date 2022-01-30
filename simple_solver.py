"""
Solves sudokus
:author: kvan
"""
import pprint
import numpy as np

SUDOKU_SIZE = 9


def is_valid_set(arr: np.ndarray) -> bool:
    no_zeros = arr[arr != 0]
    return len(no_zeros) == len(set(no_zeros))


def is_valid(board: np.ndarray) -> bool:
    for row in board:
        if not is_valid_set(row):
            return False
    for col in enumerate(board):
        if not is_valid_set(board[:, col[0]]):
            return False
    for grid in enumerate(board):
        if not is_valid_set(board[grid[0]:3, grid[0]:3]):
            return False
    return True


def is_solved(board: np.ndarray) -> tuple:
    for row in enumerate(board):
        for col in enumerate(row[1]):
            if board[row[0]][col[0]] == 0:
                return (row[0], col[0])
    return (None, None)


def solver(board: np.ndarray) -> tuple:
    """Solves given sudoku board that is passed in

    Args:
      board (np.ndarray): the board to solve
    """
    (row, col) = is_solved(board)
    if row is None and col is None:
        return (True, board)
    for test_number in range(1, len(board)+1):
        board[row][col] = test_number
        # pprint.pprint(board)
        if is_valid(board):
            solved, next_board = solver(np.copy(board))
            if solved:
                return (True, next_board)
        # if(is_valid(board) and solver(np.copy(board))[0]):
        #     return (True, board)
    return (False, board)


def solve_sudoku(board: np.ndarray) -> np.ndarray:
    _, solved_board = solver(board)
    return solved_board


sudoku_board = np.array([[5, 6, 1, 0, 0, 0, 7, 4, 9],
                         [8, 0, 9, 0, 0, 6, 2, 1, 3],
                         [0, 0, 0, 0, 9, 0, 6, 0, 0],
                         [7, 1, 4, 6, 0, 0, 8, 3, 0],
                         [0, 2, 0, 0, 0, 4, 0, 6, 7],
                         [6, 3, 8, 7, 0, 1, 5, 9, 4],
                         [0, 0, 0, 4, 0, 3, 0, 2, 5],
                         [0, 9, 0, 0, 0, 5, 0, 0, 6],
                         [4, 0, 7, 0, 0, 2, 0, 0, 0]])

pprint.pprint(sudoku_board)
sudoku_board = solve_sudoku(sudoku_board)
pprint.pprint(sudoku_board)
