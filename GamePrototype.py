# Imports needed:
import numpy as np
import sys
import os
import pygame

from Board import Board
from Button import Button

from typing import List

# Colours used in the game:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
LIGHTBLUE = (204, 204, 255)


class Game:
    """
    This class runs Connect 2^2 for the user in a pyGame window.

    To do this the class begins by:

    1. Initializing the main menu of the game and displaying it on screen.
    2. Launching a HumanVsHuman or HumanVsCPU game depending on what the user clicks.

    From there, the main game loop:

    3. Loads up an empty Board.
    4. Let's the user pick a move depending on who's turn it is in the game.
    5. Updates the board after every move.

    The Board class is responsible for checking the winning condition, but once that condition is met, this Game class
    displays a game over screen.

    === Public Attributes ===
    board: The matrix representation of our board in the console.
    window: The pyGame window running the Connect 2^2 game.

    === Private Attributes ===
    _all_screens: Every screen in our Connect 2^2 game.
    _current_screen: The current screen that we are at in the game.
    _game_over: Shows whether or not the game is over.
    """

    board: Board
    window: pygame.Surface
    _all_screens: List[str]
    _current_screen: str
    _game_over: bool

    def __init__(self) -> None:
        """
        Initializes the main game loop in pyGame.
        """

        # Initializes the main pyGame window.
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # starts the game window centered to window screen
        pygame.display.set_caption("connect 2^2")
        self.window = pygame.display.set_mode((800, 600))

        # Sets attribute to keep track of what scene we are at in the game.
        self._all_screens = ["mainMenu", "game", "endScreen", "aboutGame"]
        self._current_screen = self._all_screens[0]

        self._game_over = False
        has_not_rendered = True
        while not self._game_over:

            for event in pygame.event.get():

                # if the user X's out, the game ends.
                if event.type == pygame.QUIT:
                    sys.exit()

                # else start by displaying the main menu.
                if self._current_screen == "mainMenu":
                    self.show_menu(event)
                    pygame.display.flip()

                # if the user has already clicked start game in the menu, start the game.
                elif self._current_screen == "game":

                    if has_not_rendered:
                        self.play_game(event)
                        # Since the game has now started, has_not_rendered
                        # is set to False so that the game doesn't restart.
                        has_not_rendered = False

    def show_menu(self, event) -> None:
        """
        Displays the Connect 2^2's menu screen in pyGame for the user.
        :param event: the latest event in the main pyGame loop.
        :return: None
        """

        # This adds a frame to the menu screen.
        # We are still deciding whether or not we will keep this.
        # pygame.draw.rect(self.window, GREY, (50, 50, 400, 300))

        # Adds the Connect 2^2 title at the middle of the screen.
        font = pygame.font.SysFont('gloucesterextracondensed', 75)
        title = font.render("connect 2^2", 2, LIGHTBLUE)
        self.window.blit(title, (200, 200))

        # Creates the buttons in the main menu screen.
        start_game = Button(BLACK, 190, 350, 50, 100, "start.")
        quit_game = Button(BLACK, 390, 350, 50, 100, "quit.")
        start_game.draw(self.window)
        quit_game.draw(self.window)

        # Updates the screen with these buttons.
        pygame.display.flip()

        # Checks which button the players clicks and acts accordingly.
        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self._current_screen == "mainMenu":
                if start_game.is_hover(mouse_position):
                    # Switch to the game screen.
                    self._current_screen = "game"

                if quit_game.is_hover(mouse_position):
                    self._game_over = True
                    sys.exit()

    def play_game(self, event) -> None:
        """
        Starts a Connect 2^2 game for the user.
        :param event: the latest event in the main pyGame loop.
        :return: None
        """

        # Clears the screen in the game loop.
        self.window.fill(BLACK)
        pygame.display.flip()

        # Initializes the matrix board that we will refer to in the Connect 2^2 game.
        board = Board()

        # The dimensions of our board in pyGame.
        SLOTSIZE = 75
        HOLE_SIZE = int(SLOTSIZE/2) - 10
        NUMBEROFCOLUMNS = board.get_grid_size()[1]
        NUMBEROFROWS = board.get_grid_size()[0]

        # Creates the pyGame Board with corresponding slots and holes from the matrix board representation.
        # This strategy for creating the board was inspired by a tutorial on freeCodeCamp.org.
        #   Video URL: https://www.youtube.com/watch?v=XpYz-q1lxu8
        for column in range(NUMBEROFCOLUMNS):
            for row in range(NUMBEROFROWS):
                pygame.draw.rect(self.window, LIGHTBLUE, (125+column*SLOTSIZE, 75+row*SLOTSIZE, SLOTSIZE, SLOTSIZE))
                pygame.draw.circle(self.window, BLACK, (160+column*SLOTSIZE, 110+row*SLOTSIZE), HOLE_SIZE)

        # Renders the board on screen after creating it.
        pygame.display.flip()


if __name__ == "__main__":

    # This simply starts running our Connect 2^2 game.
    game = Game()

