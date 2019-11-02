import pygame
from pygame import mouse
import os
import Handler
import Menu
import DisplayBoard
import Board
from State import STATE
from typing import Tuple, Optional


class Game:
    """
    This class represents the main game.

    ===Public Attributes===

    width: the width of the game screen

    height: the height of the game screen

    size: the size of the game screen in terms of width by height

    running: whether the game is still being played or has ended

    has_winner: if a player has won the game

    screen: the display window of the game

    board: The matrix representation of our board in the console.

    handler: the game object handler

    menu: the game menu

    displayboard: the Connect 2^2 play screen

    gamestate: the state of the game

    """

    # Public Instance Attributes
    width: int
    height: int
    running: bool
    has_winner: bool
    size: Tuple[int, int]
    screen: Optional[pygame.Surface]
    board: Board
    handler: Handler
    menu: Menu
    displayboard: DisplayBoard
    gamestate: STATE

    def __init__(self):
        """
        Initializes the necessary variables and classes that the game
        requires to run.
        """
        # Initializes variables for the game screen and for the game to run
        # By default the game is set to run
        self.width, self.height = 800, 600
        self.running = False
        self.has_winner = False
        self.size = (self.width, self.height)
        self.screen = None

        # Initializes the classes for that the game requires to run and update
        # the game.
        self.board = Board.Board()
        self.handler = Handler.Handler()
        self.menu = Menu.Menu(self, self.handler)
        self.displayboard = DisplayBoard.DisplayBoard(self, self.handler, self.board)

        # Sets the game state.
        # By default, the game state starts with the menu state.
        self.gamestate = STATE.Menu

        # Run the game
        self.run_game()

    def set_bgm(self, track):
        """
        Sets the current game background music to a <track>
        """
        pass

    def on_init(self):
        """
        Initializes the game screen and runs the game.
        """
        pygame.init()

        # Starts the game window centered to window screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Connect 2^2")

        # Sets the pygame display screen to self.size
        # and displays with either Hardware Surface or
        # Double Buffer
        self.screen = pygame.display.set_mode\
            (self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

    def on_event(self, event: pygame.event):
        """
        React to the given pygame event as appropriate.
        """
        if event.type == pygame.QUIT:
            self.running = False

    def tick(self):
        """
        Animate all game objects in the game as appropriate to
        the current game state.
        Checks if a player has won, and stops the game if necessary.
        """
        if self.gamestate == STATE.Game:
            self.displayboard.tick()
            self.handler.tick()

            if self.has_winner:
                self.gamestate = STATE.End

        elif self.gamestate == STATE.Menu or \
                self.gamestate == STATE.End or \
                self.gamestate == STATE.About:
            self.handler.tick()
            self.menu.tick()

    def render(self):
        """
        Renders all the game elements onto the game screen as
        appropriate to the current game state.
        """
        if self.gamestate == STATE.Game:
            self.displayboard.render(self.screen)
            self.handler.render(self.screen)

        elif self.gamestate == STATE.Menu or \
                self.gamestate == STATE.End or \
                self.gamestate == STATE.About:
            self.handler.render(self.screen)
            self.menu.render(self.screen)

        pygame.display.flip()

    def run_game(self):
        """
        Runs the Connect 2^2 game until the game ends.
        """
        self.on_init()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.tick()
            self.render()
        
        pygame.quit()
        
        # Have to add this line here to properly close the window w/ Macs
        exit()


if __name__ == "__main__":
    game = Game()

