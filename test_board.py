import pytest
from Board import *


@pytest.mark.board_test
def test_initial_board():
    """
    Test the initial state of the board, which should be empty
    :return:
    """
    board = Board()

    for i in range(board.get_grid_size()[0]):
        for j in range(board.get_grid_size()[1]):
            assert board.get_token(i, j) == Board.EMPTY


@pytest.mark.valid_move
def test_valid_move():
    """
    Test whether or not a possible move is indeed valid or not
    :return:
    """

    board = Board()

    # a col outside the width of the board should be false
    assert board.valid_move(board.get_grid_size()[1] + 1) is False

    # only positive cols should be considered for a move
    assert board.valid_move(-2) is False

    # since board is empty all cols should have moves
    for i in range(board.get_grid_size()[1]):
        assert board.valid_move(i) is True

    # if a col is full no move can be made
    for i in range(board.get_grid_size()[1]):
        if i % 2 == 0:
            board.move(board.P1, 0)
        else:
            board.move(board.P2, 0)

    """
    board now looks like this...
    
      0 1 2 3 4 5 6 
     +-+-+-+-+-+-+-+
    0|O|-|-|-|-|-|-|0
     +-+-+-+-+-+-+-+
    1|X|-|-|-|-|-|-|1
     +-+-+-+-+-+-+-+
    2|O|-|-|-|-|-|-|2
     +-+-+-+-+-+-+-+
    3|X|-|-|-|-|-|-|3
     +-+-+-+-+-+-+-+
    4|O|-|-|-|-|-|-|4
     +-+-+-+-+-+-+-+
    5|X|-|-|-|-|-|-|5
     +-+-+-+-+-+-+-+
      0 1 2 3 4 5 6 

    """
    assert board.valid_move(0) is False


@pytest.mark.move
def test_move():
    """
    Test whether a move is made correctly.
    :return:
    """

    board = Board()

    # invalid moves: out of board boundaries
    assert board.move(board.P1, 100) is False
    assert board.move(board.P2, -2) is False

    print(board)

    # valid moves
    assert board.move(board.P1, 0) is True
    assert board.move(board.P2, 3) is True

    assert board.move(board.P1, 4) is True
    assert board.move(board.P2, 3) is True

    assert board.move(board.P1, 3) is True
    assert board.move(board.P2, 4) is True

    assert board.move(board.P1, 2) is True
    assert board.move(board.P2, 4) is True

    assert board.move(board.P1, 2) is True
    assert board.move(board.P2, 2) is True

    assert board.move(board.P1, 1) is True
    assert board.move(board.P2, 4) is True

    """
    BEFORE:
    
      0 1 2 3 4 5 6 
     +-+-+-+-+-+-+-+
    0|-|-|-|-|-|-|-|0
     +-+-+-+-+-+-+-+
    1|-|-|-|-|-|-|-|1
     +-+-+-+-+-+-+-+
    2|-|-|-|-|-|-|-|2
     +-+-+-+-+-+-+-+
    3|-|-|-|-|-|-|-|3
     +-+-+-+-+-+-+-+
    4|-|-|-|-|-|-|-|4
     +-+-+-+-+-+-+-+
    5|-|-|-|-|-|-|-|5
     +-+-+-+-+-+-+-+
      0 1 2 3 4 5 6 
    
    AFTER:
    
      0 1 2 3 4 5 6 
     +-+-+-+-+-+-+-+
    0|-|-|-|-|-|-|-|0
     +-+-+-+-+-+-+-+
    1|-|-|-|-|-|-|-|1
     +-+-+-+-+-+-+-+
    2|-|-|-|-|O|-|-|2
     +-+-+-+-+-+-+-+
    3|-|-|O|X|O|-|-|3
     +-+-+-+-+-+-+-+
    4|-|-|X|O|O|-|-|4
     +-+-+-+-+-+-+-+
    5|X|X|X|O|X|-|-|5
     +-+-+-+-+-+-+-+
      0 1 2 3 4 5 6 
    
    """

    print(board)


@pytest.mark.get_token
def test_get_token():
    """
    Test whether board is able to identify the winner of the game
    :return:
    """

    board = Board()

    # invalid row
    assert board.get_token(-1, 1) == board.EMPTY

    # invalid col
    assert board.get_token(1, -1) == board.EMPTY

    # setup board
    board.move(board.P1, 0)
    board.move(board.P2, 3)

    board.move(board.P1, 4)
    board.move(board.P2, 3)

    board.move(board.P1, 3)
    board.move(board.P2, 4)

    board.move(board.P1, 2)
    board.move(board.P2, 4)

    board.move(board.P1, 2)
    board.move(board.P2, 2)

    board.move(board.P1, 1)
    board.move(board.P2, 4)

    # valid
    assert board.get_token(5, 3) == board.P2
    assert board.get_token(5, 6) == board.EMPTY
    assert board.get_token(3, 3) == board.P1


@pytest.mark.winner
def test_get_winner():
    """
    Test whether a winner is returned and if so is it the correct  winner
    """

    board = Board()
    board1 = Board()
    board2 = Board()

    # board is empty
    for i in range(board.get_grid_size()[1]):
        assert board.get_winner(i) == board.EMPTY

    # vertical win
    for i in range(4):
        board.move(Board.P1, 1)

    for i in range(3):
        board.move(Board.P2, 2)

    assert board.get_winner(1) == board.P1

    # horizontal win
    for i in range(4):
        board1.move(Board.P2, i)
    for i in range(3):
        board1.move(Board.P1, 1)

    assert board1.get_winner(0) == board.P2

    # diagonal win

    board2.move(Board.P1, 1)
    board2.move(Board.P2, 2)

    board2.move(Board.P1, 2)
    board2.move(Board.P2, 3)

    board2.move(Board.P1, 4)
    board2.move(Board.P2, 3)

    board2.move(Board.P1, 3)
    board2.move(Board.P2, 5)

    board2.move(Board.P1, 4)
    board2.move(Board.P2, 4)

    board2.move(Board.P1, 4)

    assert board2.get_winner(1) == board.P1


@pytest.mark.load
def test_load():
    pass


if __name__ == "__main__":
    import pytest
    pytest.main(["test_board.py"])
