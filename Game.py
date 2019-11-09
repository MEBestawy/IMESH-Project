import pygame
from pygame import mouse
import os
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
        self.events = None
        self.tracks = [
            "./Assets/audio/bgm/louie_zong_cat_toy.wav",
            "./Assets/audio/bgm/ffxv_ost_crystalline_chill.wav",
            "./Assets/audio/bgm/jayswanzone_musicpg.wav",
            "./Assets/audio/bgm/nearstheme_deathnote.wav",
            "./Assets/audio/bgm/snailshouse_ramune.wav"
        ]

        self.winner = "1"
        self.currtrack = 0
        # Initializes the classes for that the game requires to run and update
        # the game.
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init(44100, -16, 2, 512)

        self.board = Board.Board()
        self.menu = Menu.Menu(self)
        self.displayboard = DisplayBoard.DisplayBoard(self, self.board)

        # Sets the game state.
        # By default, the game state starts with the menu state.
        self.gamestate = STATE.Menu

        # Run the game
        self.run_game()

    def set_bgm(self, track, tracknum):
        """
        Sets the current game background music to a <track>
        """
        self.currtrack = tracknum
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(-1)

    def on_init(self):
        """
        Initializes the game screen and runs the game.
        """
        pygame.init()

        # Starts the game window centered to window screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Connect 2^2")

        # Starts the game audio
        self.set_bgm(self.tracks[0], 0)

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

    def get_winner(self):
        """
        Get the winner of the game.
        """
        return self.winner

    def set_winner(self, winner):
        self.winner = winner


    def tick(self):
        """
        Animate all game objects in the game as appropriate to
        the current game state.
        Checks if a player has won, and stops the game if necessary.
        """
        if self.gamestate == STATE.Game:
            self.displayboard.tick()
            if self.has_winner:
                self.gamestate = STATE.End
        elif self.gamestate == STATE.Menu or \
                self.gamestate == STATE.End or \
                self.gamestate == STATE.Option:
            self.menu.tick()

    def render(self):
        """
        Renders all the game elements onto the game screen as
        appropriate to the current game state.
        """
        if self.gamestate == STATE.Game:
            self.displayboard.render(self.screen)
        elif self.gamestate == STATE.Menu or \
                self.gamestate == STATE.End or \
                self.gamestate == STATE.Option:
            self.menu.render(self.screen)

        pygame.display.flip()

    def run_game(self):
        """
        Runs the Connect 2^2 game until the game ends.
        """
        self.on_init()

        while self.running:
            self.events = pygame.event.get()
            for event in self.events:
                self.on_event(event)
            self.tick()
            self.render()
        pygame.quit()

        # Have to add this line here to properly close the window w/ Macs
        exit()


if __name__ == "__main__":
    game = Game()

