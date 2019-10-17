from __future__ import annotations
import pygame
from settings import *
from game import *


class Actor:
    """
    A class to represent all the game's actors. This class includes any
    attributes/methods that every actor in the game must have.

    This is an abstract class. Only subclasses should be instantiated.

    === Public Attributes ===
    x:
        x coordinate of this actor's location on the stage
    y:
        y coordinate of this actor's location on the stage
    icon:
        the image representing this actor
    """
    x: int
    y: int
    icon: pygame.Surface

    def __init__(self, icon_file, x, y):
        """Initialize an actor with the given image <icon_file> and the
        given <x> and <y> position on the game's stage.
        """

        self.x, self.y = x, y
        self.icon = pygame.image.load(icon_file)

    def move(self, game: 'Game') -> None:
        """Move this actor by taking one step of its animation."""

        raise NotImplementedError


class Player(Actor):
    """
    A class to represent a Player in the game.
    """
    # === Private Attributes ===
    # _stars_collected:
    #       the number of stars the player has collected so far
    x: int
    y: int
    icon: pygame.Surface
    _stars_collected: int

    def __init__(self, icon_file: str, x: int, y: int) -> None:
        """Initalize a Player with the given image <icon_file> at the position
        <x> and <y> on the stage."""

        super().__init__(icon_file, x, y)
        self._stars_collected = 0

    def move(self, game: Game) -> None:
        """
        Move the player on the <game>'s stage based on keypresses.
        """

        new_x, new_y = self.x, self.y
        if game.keys_pressed[pygame.K_LEFT]:
            new_x -= 1
        elif game.keys_pressed[pygame.K_RIGHT]:
            new_x += 1
        elif game.keys_pressed[pygame.K_UP]:
            new_y -= 1
        elif game.keys_pressed[pygame.K_DOWN]:
            new_y += 1
        elif game.keys_pressed[pygame.K_w]:
            new_y -= 1
        elif game.keys_pressed[pygame.K_a]:
            new_x -= 1
        elif game.keys_pressed[pygame.K_s]:
            new_y += 1
        elif game.keys_pressed[pygame.K_d]:
            new_x += 1

        if isinstance(game.get_actor(new_x, new_y), Star):
            self._stars_collected += 1
            game.remove_actor(game.get_actor(new_x, new_y))

        if not isinstance(game.get_actor(new_x, new_y), Wall):
            self.x, self.y = new_x, new_y

    def has_won(self, game: 'Game') -> bool:
        """Return True iff the game has been won."""

        if game.goal_stars == self._stars_collected:
            return True
        return False



class Chaser(Actor):
    """
    A class to represent a Chaser in the game who chases the Player.
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        Move the chaster on the <game>'s stage based on the player's location.
        """

        if game.player.x > self.x:
            self.x += 0.5
        elif game.player.x < self.x:
            self.x -= 0.5
        elif game.player.y > self.y:
            self.y += 0.5
        elif game.player.y < self.y:
            self.y -= 0.5

        if isinstance(game.get_actor(self.x, self.y), Player):
            game.game_over()


class Star(Actor):
    """
    A class to represent a Star in the game.
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A Star cannot move, so do nothing.
        """

        pass


class Wall(Actor):
    """
    A class to represent a Wall in the game.
    """
    x: int
    y: int
    icon: pygame.Surface

    def move(self, game: 'Game') -> None:
        """
        A Wall cannot move, so do nothing.
        """

        pass


