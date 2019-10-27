<<<<<<< HEAD

=======
import numpy as np
from Slot import Slot
from Disc import Disc


class Board:
    """

    """

    def __init__(self, length=6, width=7):
        """

        :param length:
        :param width:
        """
        self.grid = np.zeros(shape=(length, width), dtype=object)

        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                self.grid[row][col] = Slot()

    def __str__(self):
        """
        :return: The string representation of the board.
        """
        # Showing the col index numbers
        result = "  "
        for col in range(self.grid.shape[1]):
            result += str(col) + " "
        result += "\n"

        # Adding the top level of board
        result += " +"
        for col in range(self.grid.shape[1]):
            result += "-+"
        result += '\n'

        # Adding each row of the board
        for row in range(self.grid.shape[0]):
            result += str(row) + "|"
            # Adding each col of the board
            for col in range(self.grid.shape[1]):
                result += str(self.grid[row][col]) + "|"
            result += str(row) + "\n"

            # End of row
            result += " +"
            for col in range(self.grid.shape[1]):
                result += "-+"
            result += '\n'

        # Showing the index numbers on the bottom
        result += "  "
        for col in range(self.grid.shape[1]):
            result += str(col) + " "
        result += '\n'

        # Return the result
        return result


if __name__ == "__main__":
    board = Board()
    print(board)
>>>>>>> parent of 75156d9... Update Board class to agreed upon design
