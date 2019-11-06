import multiprocessing
import csv
import GameStorage
from Board import Board


class GameStorage:
    """


    """
    __instance = None
    data_dict = {}

    @classmethod
    def get_storage(cls) -> GameStorage:
        """

        :return:
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

        :param url:
        :return:
        """
        opened = open(url)
        file = csv.DictReader(opened)
        self.data_dict = {}

        for line in file:
            self.data_dict[int(line.get("ID"))] = \
                {"CurrentTurn": line.get("CurrentTurn"),
                 "BGM": line.get("BGM"),
                 "Board": _load_board(line.get("Board"))}

    def save_game(self) -> None:
        """

        :return:
        """
        # TODO: Ask about this!!!


def _convert_board_to_format(board: Board) -> str:
    """

    :param board:
    :return:
    """
    shape = board.get_grid_size()
    result = ""

    # Going row by row
    for i in range(shape[0]):
        for j in range(shape[1]):
            result += board.get_token(j, i)

        if i < shape[0] - 1:
            result += "/"
    print(board, result)
    return result


def _load_board(str_board: str) -> Board:
    """

    :param str_board:
    :return:
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
    _convert_board_to_format(a2.data_dict[0]['Board'])
    print(a1 == a2 == a3)

