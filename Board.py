import numpy as np
from typing import Dict, Tuple, List


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


    ===Private Attributes===
    __grid: A 2D numpy array responsible for holding the information about the
            state of the board throughout the game.
    __avail_pos: A dictionary containing which rows a player can place a token
                 depending on the column. This dictionary maps column indices
                 as keys to values of rows of potential next moves.
    __winner: The winner of the game. Takes on a value of a player or empty

    ===Static Variables===
    P1: The string representation of the first player.
    P2: The string representation of the second player.
    EMPTY: The string representation of an empty slot on the board.

    """
    # Static variables for board info
    P1 = "X"
    P2 = "O"
    EMPTY = "-"

    # Private Attributes
    __grid: np.ndarray
    __avail_pos: Dict[int, int]

    def __init__(self, length=6, width=7):
        """
        Instantiate a board object.

        :param length: The length (vertical) size of board
        :param width: The width (horizontal) size of board
        """
        self.__winner = Board.EMPTY
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
        if self.valid_move(col):
            if player == Board.P1 or player == Board.P2:
                self.__grid[self.get_avail_row(col)][col] = player
                self.__avail_pos[col] -= 1
                self.find_winner(col)
                return True
        return False

    def get_winner(self) -> str:
        """

        :return:
        """
        return self.__winner

    def find_winner(self, col: int) -> None:
        """
        After a player has moved, this method finds the winner, if a winner
        exists.

        Precondition:
        A win would only be possible using the top-most disc of inputted col,
        nowhere else on the board should a win condition be possible.

        :param col: The column where the move was just made
        """
        x, y = self.get_avail_row(col) + 1, col
        if self.get_token(x, y) == Board.EMPTY:
            self.__winner = Board.EMPTY
            return
        player = self.get_token(x, y)  # player who just moved
        count = 1  # occurrences of player in a row
        directions = [(1, -1), (1, 0), (1, 1), (0, 1)]
        for d in directions:
            drow, dcol = d
            switched = False
            while count < 4:
                if 0 <= x + drow < self.__grid.shape[0] and \
                        0 <= y + dcol < self.__grid.shape[1] and \
                        self.get_token(x + drow, y + dcol) == player:
                    count += 1
                    x += drow
                    y += dcol
                else:
                    if not switched:
                        x, y = self.get_avail_row(col) + 1, col
                        drow, dcol = -drow, -dcol
                        switched = True
                    else:
                        count = 1
                        break
            if count == 4:
                self.__winner = player
                return
        self.__winner = Board.EMPTY

    def valid_move(self, col: int) -> bool:
        """
        Checks if there is a valid move at the inputted column.

        :param col: A column of the board.
        :return: Whether a move on this column is possible.
        """
        # Checking if the column is in the board, and has available moves.
        return 0 <= self.get_avail_row(col) <= self.__grid.shape[1]

    def get_avail_row(self, col: int) -> int:
        """
        Method checks which row a token would be positioned at if it were to be
        dropped at column col.

        :param col: The column to be checked.
        :return: The row where a token would be dropped if place, -1 if no move
        possible.
        """
        return self.__avail_pos.get(col, -1)

    def get_grid_size(self) -> Tuple[int, int]:
        """
        Method that returns the size of the matrix board representation.
        :return: the size of the matrix board representation.
        """
        return self.__grid.shape

    def get_token(self, row: int, col: int) -> str:
        """
        Return the token at row, col in the board

        :param row: specified row to look in
        :param col: specified col to look in
        :return: either Board.EMPTY, Board.P1, or Board.P2
        """
        if (0 <= col < self.__grid.shape[1]) and (0 <= row < self.__grid.shape[0]):
            return self.__grid[row][col]
        else:
            return Board.EMPTY

    def load(self, board_lst: List) -> None:
        """

        :param board_lst:
        """
        # Loading the board from the list
        for row in range(len(board_lst)):
            for col in range(len(board_lst[row])):
                self.__grid[row][col] = board_lst[row][col]

        # Adjusting moves dictionary
        for i in range(self.__grid.shape[1]):
            j = self.__grid.shape[0] - 1
            while j > -1 and self.__grid[j][i] != Board.EMPTY:
                j -= 1
            self.__avail_pos[i] = j

    def __str__(self):
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
    print(board.get_winner())
    b2 = Board()
    print(board == b2)
    board.move(Board.P1, 3)
    board.move(Board.P2, 3)
    board.move(Board.P1, 3)
    board.move(Board.P2, 3)
    board.move(Board.P1, 0)
    print(board.get_winner())
    print(board.get_winner())
    board.move("R", 3)
    board.move(Board.P2, 3)
    board.move(Board.P1, 3)
    print(board.move(Board.P1, 3))
    print(board.move(Board.P1, -1))
    print(board.move(Board.P1, 6))
    print(board.move(Board.P1, 7))
    print(board)
    board.load(["-------","-------","-------","XXXXXXX","XXXXXXX","XXXXXXX"])
    print(board)
    print(board.move(Board.P1, 5))
    print(board.get_winner())
    print(board)

