import pytest
from Board import *


board = Board()


@pytest.mark.board
def test_initial_board():
    """
    Test the initial state of the board, which should be empty
    :return:
    """

    for i in range(board.get_grid_size()[0]):
        for j in range(board.get_grid_size()[1]):
            assert board.get_token(i, j) == Board.EMPTY


@pytest.mark.move
def test_move():
    """
    """
    pass


@pytest.mark.get_token
def test_get_token():
    pass




@pytest.mark.winner
def test_get_winner():
    pass


@pytest.mark.valid_move
def test_valid_move():
    pass


@pytest.mark.load
def test_load():
    pass
