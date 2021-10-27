"""
Solves sudokus
:author: kvan
"""
import pprint
import numpy as np

SUDOKU_SIZE = 9


def is_valid_area(area: list) -> bool:
    """ :DEPRECATED: Check if list of numbers is valid for a sudoku
    :param area: list of numbers to check, length of 9, empty cells represented by zeros
    :returns: bool, if valid or not, based on if it contains a duplicate value
    """
    # ignore empty cells
    nat_number_list = list(filter(lambda x: 0 < x <= SUDOKU_SIZE, area))
    # make set
    number_set = list(set(nat_number_list))
    # check for no duplicates and that size of area is correct
    return nat_number_list == number_set and len(area) == SUDOKU_SIZE


def get_area_list(pos: tuple, board: np.ndarray) -> list:
    """ Gets the 3x3 area around the position cell
    :param pos: tuple, (row,column) of cell to get group from
    :param board: 2D list, current position of board to get group from
    :returns: list, of cells in the group
    """
    # find starting cell position
    start_cell = (pos[0]//3*3, pos[1]//3*3)
    # generate group by getting all cells in 3x3 from starting cell position
    group = [board[i, j] for j in range(
        start_cell[1], start_cell[1]+3) for i in range(start_cell[0], start_cell[0]+3)]
    return group


def is_valid(pos: tuple, board: np.ndarray, num: int) -> bool:
    """:DEPRECATED: Checks if a cell is valid in the current board position
    :param pos: tuple, (row,column) of cell to check
    :param board: 2D list, current position of board to check
    :returns: bool, if cell is valid
    """
    # Get all areas to check: row, column, and 3x3 area
    check_row = num not in board[pos[0]].to_list()
    check_column = num not in board[:, pos[1]].to_list()
    check_group = num not in get_area_list(pos, board)
    # Make sure all are valid
    return check_column and check_group and check_row


def is_solved(board: np.ndarray) -> bool:
    """ :DEPRECATED:Checks if the board is in a solved position
    :param board: 2D list, current board position
    :returns: bool, if sudoku board is solved or not
    """
    # any unfilled cells => unable to be in solved state
    if 0 in board:
        return False
    # check each row, column and cell group
    # check rows
    for row_index in range(0, 9):
        if not is_valid_area(board[row_index]):
            return False
    # check columns
    for column_index in range(0, 9):
        if not is_valid_area(board[:, column_index]):
            return False
    # generate group starting positions
    group = [(i*3, j*3) for i in range(0, 3) for j in range(0, 3)]
    # check group areas
    for start in group:
        if not is_valid_area(get_area_list(start, board)):
            return False
    return True


def get_valid_numbers(pos: tuple, board: np.ndarray) -> set:
    """ Get valid number options for a position
    :param pos: tuple, (row,column) of cell to get numbers for
    :param board: 2D list, current position of board to get numbers for
    :returns: set, of valid numbers
    """
    row_set = set(filter(lambda x: x > 0, board[pos[0]]))
    col_set = set(filter(lambda x: x > 0, board[:, pos[1]]))
    area_set = set(filter(lambda x: x > 0, get_area_list(pos, board)))
    not_set = row_set.union(col_set).union(area_set)
    valid_numbers = set(x+1 for x in range(SUDOKU_SIZE))
    valid_numbers = valid_numbers.difference(not_set)
    return valid_numbers


def get_first_blank(board: np.ndarray) -> tuple or None:
    """ first position of zero in board
    :param board: 2D list, current board position
    :returns: tuple, position of zero, or None if no zeros
    """
    if 0 not in board:
        return None
    index = np.where(board == 0)
    index = (index[0][0], index[1][0])
    return index


def solver(board: np.ndarray) -> bool:
    """ Solves a sudoku board
    :param board: 2D list, contains starting board position for solver(zeros for empty cells)
    :returns: boolean, if board is solved
    """
    find = get_first_blank(board)
    if not find:
        return True
    row, col = find
    for i in get_valid_numbers(find, board):
        board[row][col] = i
        if solver(board):
            return True
        board[row][col] = 0
    return False


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
solver(sudoku_board)
pprint.pprint(sudoku_board)
