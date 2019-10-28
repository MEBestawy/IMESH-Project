from __future__ import annotations
import pygame


class Player:
    """
    This class represents one of the two players that will play
    the Connect 2^2 game.

    ===Public Attributes===

    disc: the disc that Player uses when making a move.

    icon: the image representing this player

    """

    disc: str
    icon: pygame.Surface
    win_count: int

    def __init__(self, disc: str, icon_file: str) -> None:
        """
        Instantiate a Player object, with their respective
        """
        self.disc = disc
        self.icon = pygame.image.load(icon_file)

    def make_move(self, col: int) -> None:
        """
        Let self make a move at column <col>.

        :param col: a column in the game board.:
        :return:
        """
        raise NotImplementedError

    def has_won(self) -> bool:
        """
        Determine whether the player has won the game
        :return: True or false based on whether the player has won the game
        """
        raise NotImplementedError