import pygame
from typing import Tuple


class Button:
    """
    This class creates a Button to be used in the Connect 2^2 pygame screen whereby
    Users are able to interact with the button by clicking on it.

    The Button is customizable with a given colour, x and y coordinates, height, width,
    and label

    ===Public Attributes===

    colour: the colour of the Button

    x: the x coordinate of the Button on the pygame screen

    y: the y coordinate of the Button on the pygame screen

    height: the height of the Button

    width: the width of the Button

    label: the description of the Button

    """

    # Public Instance Attributes
    colour: Tuple[int]
    x: int
    y: int
    height: int
    width: int
    label: str

    def __init__(self, colour, x, y, height, width, label, fontsize, visible):
        """
        Initializes a Button with the given colour, at coordinates (x,y), with the given
        sizes width and height, and a label that describes the Button
        """
        self.colour = colour
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.label = label
        self.fontsize = fontsize
        self.visible = visible

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def draw(self, screen) -> None:
        """
        Draws the Button on the given pygame display.
        :param screen: pygame display
        :return: None
        """
        font = pygame.font.Font("./Assets/joystix_monospace.ttf", self.fontsize)
        label = font.render(self.label, 1, (255, 255, 255))
        screen.blit(label, (self.x + (self.width / 2 - label.get_width() / 2),
                            self.y + (
                                        self.height / 2 - label.get_height() / 2)))
        if self.visible:
            button = pygame.image.load("./Assets/button.png").convert()
            button.set_colorkey((85, 255, 0))
            screen.blit(button, (self.x, self.y))

    def is_hover(self, position) -> bool:
        """
        Checks if the mouse position on the pygame screen is hovering above the Button.

        :param position: mouse position on the pygame screen
        :return: True if the position is within the bounds of the Button, False otherwise
        """
        if self.x < position[0] < self.x + self.width:
            if self.y < position[1] < self.y + self.height:
                return True
        return False
