import pygame


class GameObject:
    """
    This abstract class represents the game objects in the Connect 2^2 game.

    ===Public Attributes===
    x: the x coordinate of the game object on the pygame screen.

    y: the y coordinate of the game object on the pygame screen.

    """
    # Public Instance Attributes
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """
        Initializes a game object with the given (x, y) coordinates.
        """
        self.x = x
        self.y = y

    def tick(self):
        """
        Abstract method: this method animates the game object
        """
        raise NotImplemented

    def render(self, display: pygame.Surface):
        """
        Abstract method: this method renders the game object
        """
        raise NotImplemented

    # Getter and setter methods for game object
    def set_x(self, x: float):
        """
        Sets the x-coordinate of the game object
        """
        self.x = x

    def set_y(self, y: float):
        """
        Sets the y-coordinate of the game object
        """
        self.y = y

    def get_x(self) -> float:
        """
        :return: the x-coordinate of the game object
        """
        return self.x

    def get_y(self) -> float:
        """
        :return: the y-coordinate of the game object
        """
        return self.y

