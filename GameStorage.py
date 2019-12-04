import multiprocessing
import csv
import GameStorage
from Board import Board


class GameStorage:
    """
    NOTE: This class is incomplete and is not currently used anywhere within
    the program.

    An object of this class is responsible for saving and loading information
    about Connect2^2 games. The information is designed to be saved in CSV
    format in the following order:
        ID,     CurrentTurn,     BGM,     Board
    where the ID entry is unique to each line, and thus unique to each saved
    game.

    This CSV is expected to be read and stored into a dictionary (data_dict)

    This class implements the singleton design pattern to insure no issues
    arise from multiple objects saving and loading information from and into
    files.

    ===Private Static Variables===
    __instance: The initialized instance of this class.
    __data_dict: The dictionary containing information about saved Connect2^2
                 games. This nested dictionary maps the ID for each saved game
                 to a dictionary containing the information about the saved
                 games. These internal dictionaries would have keys mapping
                 directly to a property of the saved game.

                 For example, "Board" would map to the board of a saved game.
    """
    __instance = None
    __data_dict = {}

    @classmethod
    def get_storage(cls) -> GameStorage:
        """
        This method acts as the constructor of objects of this class.

        :return: The current instance of this class.
        """
        if not cls.__instance:
            lock = multiprocessing.Lock()
            lock.acquire()

            if not cls.__instance:
                cls.__instance = GameStorage()
                cls.__instance = GameStorage()
            lock.release()
        return cls.__instance

    def read(self, url: str) -> None:
        """
        Read the file at the given url, and construct the __data_dict based on
        the information found there.
        :param url: The url to the file to be read.
        """
        # Preparing to read the file
        opened = open(url)
        file = csv.DictReader(opened)
        self.__data_dict = {}

        # Reading file
        for line in file:
            self.__data_dict[int(line.get("ID"))] = \
                {"CurrentTurn": line.get("CurrentTurn"),
                 "BGM": line.get("BGM"),
                 "Board": _load_board(line.get("Board"))}
        # Closing file
        opened.close()

    def save_game(self) -> None:
        """
        This method saves the current game of Connect 2^2 to file.
        """
        pass


def _convert_board_to_format(board: Board) -> str:
    """
    This function takes a board and returns a string that stands as a one line
    string representation of the board.

    :param board: The board to be saved.
    :return: A one line string representation of the board of current game.
    """
    shape = board.get_grid_size()
    result = ""

    # Going row by row
    for i in range(shape[0]):
        for j in range(shape[1]):
            result += board.get_token(j, i)

        if i < shape[0] - 1:
            result += "/"
    return result


def _load_board(str_board: str) -> Board:
    """
    Read a one line string and return a board that is supposed to be represented
    by the string.

    Precondition: str_board does represent some board.

    :param str_board: A one line string representation of some board.
    :return: The board represented by str_board.
    """
    board_list = str_board.split("/")
    board = Board(len(board_list), len(board_list[0]))
    board.load(board_list)
    return board


if __name__ == "__main__":
    a4 = GameStorage()
    a1 = GameStorage.get_storage()
    a2 = GameStorage.get_storage()
    a3 = GameStorage.get_storage()
#    print(a1.data_dict)
    print(a4 is a1)
    print(a1 is a2 is a3)

    a1.read("./Assets/History.csv")
    #print(a3.data_dict)
   # _convert_board_to_format(a2.data_dict[0]['Board'])
    print(a1 == a2 == a3)

