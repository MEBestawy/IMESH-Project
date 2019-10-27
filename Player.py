class Player:
    """
    This class represents one of the two players that will play
    the Connect 2^2 game.

    ===Public Attributes===

    disc: the disc that Player uses when making a move.

    """

    disc: str

    def __init__(self, disc):
        """
        Instantiate a Player object.
        """
        self.disc = disc

    def make_move(self, col: int):
        """
        Let self make a move at column <col>.

        :param col: a column in the game board.:
        :return:
        """
        raise NotImplementedError
