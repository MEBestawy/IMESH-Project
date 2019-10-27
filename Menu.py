import pygame
from State import STATE
from Button import Button
import Game
import Handler


class Menu:
    """
    This class handles the different game screens of Connect 2^2 depending on
    the current game gamestate.

    ===Private Attributes===

    _game: reference of the Game class so that Menu can update the game

    _handler: reference of the Handler class so that Menu can call the Handler

    ===Public Attributes===

    play: a Button with the label "PLAY"

    about: a Button with the label "ABOUT"

    quit: a Button with the label "QUIT"

    back: a Button with the label "BACK"

    """
    # Private Instance Attributes
    _game: Game
    _handler: Handler

    # Public Instance Attributes
    play: Button
    about: Button
    quit: Button
    back: Button

    def __init__(self, game, handler):
        """
        Initializes a Menu that has the game, handler, and buttons.

        :param game: the main game class
        :param handler: the handler
        """
        self._game = game
        self._handler = handler

        self.play = Button((0, 0, 0), 350, 250, 50, 120, "PLAY")
        self.about = Button((0, 0, 0), 350, 350, 50, 120, "ABOUT")
        self.quit = Button((0, 0, 0), 350, 450, 50, 120, "QUIT")
        self.back = Button((0, 0, 0), 600, 450, 50, 120, "BACK")

    def on_event(self, mouse_press):
        """
        React to the given <mousepress> position to as appropriate to change
        the game state or to exit the game.
        """
        pos = mouse_press.get_pos()

        if self._game.gamestate == STATE.Menu:
            if self.play.is_hover(pos):
                self._game.gamestate = STATE.Game
                # Clear the screen of game objects
                self._handler.clear_all()

                # call the game board here once
                # the game board is fully functional

            if self.about.is_hover(pos):
                self._game.gamestate = STATE.About

            if self.quit.is_hover(pos):
                self._game.running = False

        if self._game.gamestate == STATE.About:
            if self.back.is_hover(pos):
                self._game.gamestate = STATE.Menu

    def tick(self):
        """
        Animates the Menu given a pygame mouse event.
        If the pygame.event == MOUSEBUTTONDOWN, then
        animate accordingly.
        """
        if pygame.mouse.get_pressed()[0]:
            self.on_event(pygame.mouse)

    def render(self, display: pygame.Surface):
        """
        Renders the game screen depending on the
        current game state.
        """
        if self._game.gamestate == STATE.Menu:
            # Draws the background
            display.fill((0, 0, 0))
            pygame.draw.rect(display, (150, 150, 150), (50, 50, 700, 500))

            # Set the text
            font = pygame.font.SysFont('comicsansms', 75)
            title = font.render("connect 2^2", 1, (255, 255, 255))
            display.blit(title, ((self._game.width/2 - title.get_width()/2), 75))

            # Draw the Buttons
            self.play.draw(display)
            self.about.draw(display)
            self.quit.draw(display)

        if self._game.gamestate == STATE.About:
            pygame.draw.rect(display, (255, 100, 100), (0, 0, 800, 600))
            self.back.draw(display)

        if self._game.gamestate == STATE.End:
            display.fill((0, 0, 0))



