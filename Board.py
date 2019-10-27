import numpy as np


class Board:
    """
    The Connect2^2 representation of the game board. Contains all of the
    information regarding a connect game board, and controls game mechanics.

    This class holds information about each piece on the board using static
    variables: P1, P2, EMPTY.

    Instances of this class also have a 2D array containing information about
    the positions of each token.

    Code for __str__() method was inspired by CSC207 Assignment 1:
        Assignment URL:
            https://axiom.utm.utoronto.ca/~207/19f/assignments/a1/index.shtml
    """
    # Static variables for board info
    P1 = "X"
    P2 = "O"
    EMPTY = "_"

    def __init__(self, length=6, width=7):
        """
        Instantiate a board object.

        :param length: The length (vertical) size of board
        :param width: The width (horizontal) size of board
        """
        self.__grid = np.full(shape=(length, width), fill_value=Board.EMPTY)

        # Initializing the dictionary containing where moves could be made.
        self.__avail_pos = {}
        for i in range(width):
            self.__avail_pos[i] = length - 1

    def move(self, player: str, col: int) -> bool:
        """
        When called, this method attempts to place a player's token down the
        inputted column. This method will mutate the board's grid, as well as
        update the dictionary associated with available moves on the board.

        :param player: A string representing the player making a move.
        :param col: The column on the board the player wants to move.
        :return: Whether the move was successfully done.
        """
        # TODO: Build is method.
        raise NotImplementedError

    def get_winner(self, col: int) -> str:
        """

        :param col: The column that
        :return: The winner, either P1, P2, or EMPTY if there is no winner yet.
        """
        # TODO: Build is method.
        raise NotImplementedError

    def valid_move(self, col: int) -> bool:
        """
        Checks if there is a valid move at the inputted column.

        :param col: A column of the baord.
        :return: Whether a move on this column is possible.
        """
        # Checking if the column is in the board, and has available moves.
        if 0 <= col <= self.__grid.shape[1]:
            return self.get_avail_row(col) >= 0
        return False

    def get_avail_row(self, col: int):
        """
        Method checks which row a token would be positioned at if it were to be
        dropped at column col.

        :param col: The column to be checked.
        :return: The row where a token would be dropped if place, -1 if no move
        possible.
        """
        return self.__avail_pos.get(col, -1)

    def __str__(self) -> str:
        """
        :return: The string representation of the board.
        """
        # Showing the col index numbers
        result = "\n  "
        for col in range(self.__grid.shape[1]):
            result += str(col) + " "
        result += "\n"

        # Adding the top level of board
        result += " +"
        for col in range(self.__grid.shape[1]):
            result += "-+"
        result += '\n'

        # Adding each row of the board
        for row in range(self.__grid.shape[0]):
            result += str(row) + "|"
            # Adding each col of the board
            for col in range(self.__grid.shape[1]):
                result += str(self.__grid[row][col]) + "|"
            result += str(row) + "\n"

            # End of row
            result += " +"
            for col in range(self.__grid.shape[1]):
                result += "-+"
            result += '\n'

        # Showing the index numbers on the bottom
        result += "  "
        for col in range(self.__grid.shape[1]):
            result += str(col) + " "
        result += '\n'

        # Return the result
        return result


if __name__ == "__main__":
    board = Board()
    print(board)
    print(board.valid_move(3))
