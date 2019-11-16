from __future__ import annotations
import pygame
import Board
from GameObject import GameObject


class Player(GameObject):
    """
    This class represents one of the two players that will play
    the Connect 2^2 game.

    ===Public Attributes===

    """

    disc: str
    icon: pygame.Surface
    x: int
    y: int
    offset_x: int

    def __init__(self, turn: int, x: int, y: int) -> None:
        """
        Instantiate a Player object, with their respective
        """
        # self.icon = pygame.image.load(icon_file)
        super().__init__(x, y)
        self.offset_x = -25
        self.turn = turn
        self.vel_y = 30

    def make_move(self, board: Board, col: int) -> bool:
        """
        Let self make a move at column <col>.

        :param board: the board to make a move on.:
        :param col: a column in the game board.:
        :return: Whether the move was successfully made at <col>.:
        """
        return board.move(self, col)

    def has_won(self, board: Board) -> bool:
        """
        Determine whether the player has won the game.

        :param board: the board to check whether self has won
        :return: True or false based on whether the player has won the game
        """
        return board.get_winner() == self.disc

    def tick(self):
        self.y += self.vel_y

    def render(self, screen: pygame.Surface):

        pygame.draw.rect(screen, (255, 255, 255), (self.x + self.offset_x, self.y, 50, 50))
        return None

    def collisions(self):
        return None
