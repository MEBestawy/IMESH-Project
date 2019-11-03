import multiprocessing
import csv
import GameStorage
from Board import Board


class GameStorage:
    """


    """
    __instance = None

    def __init__(self):
        try:
            if self.__instance and not self.data_dict:
                self.data_dict = {}
        except AttributeError:
            self.data_dict = None

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
                 "Board": load_board(line.get("Board"))}


def load_board(str_board: str) -> Board:
    """

    :param str_board:
    :return:
    """
    board_list = str_board.split("/")
    board = Board(len(board_list), len(board_list[0]))
    board.load(board_list)
    return board


if __name__ == "__main__":
    a1 = GameStorage.get_storage()
    a2 = GameStorage.get_storage()
    a3 = GameStorage.get_storage()
    print(a1.data_dict)

    a1.read("./Assets/History.csv")
    print(a3.data_dict)
    print(a2.data_dict[0]['Board'])
    print(a1 == a2 == a3)

