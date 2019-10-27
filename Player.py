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

    def __init__(self, disc: str, icon_file: str):
        """
        Instantiate a Player object, with their respective
        """
        self.disc = disc
<<<<<<< HEAD

    def make_move(self, col: int):
        """
        Let self make a move at column <col>.

        :param col: a column in the game board.:
        :return:
        """
        raise NotImplementedError
=======
        self.icon = pygame.image.load(icon_file)
>>>>>>> 952aa4def8970681095c6fa1efb8ab65e67b249b
