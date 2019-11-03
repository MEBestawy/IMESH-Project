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

    option: a Button with the label "OPTION"

    quit: a Button with the label "QUIT"

    back: a Button with the label "BACK"

    """
    # Private Instance Attributes
    _game: Game
    _handler: Handler

    # Public Instance Attributes
    play: Button
    option: Button
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
        self._xpos = 0
        self.sound = pygame.mixer.Sound("./Assets/audio/sfx/click.wav")

        self.play = Button((0, 0, 0), 350, 250, 50, 120, "PLAY")
        self.option = Button((0, 0, 0), 350, 350, 50, 120, "OPTION")
        self.quit = Button((0, 0, 0), 350, 450, 50, 120, "QUIT")
        self.back = Button((0, 0, 0), 650, 525, 50, 120, "BACK")

    def on_event(self, mouse_press):
        """
        React to the given <mousepress> position to as appropriate to change
        the game state or to exit the game.
        """
        pos = mouse_press.get_pos()

        if self._game.gamestate == STATE.Menu:
            if self.play.is_hover(pos):
                self.sound.play()
                self._game.gamestate = STATE.Game
                # Clear the screen of game objects
                self._handler.clear_all()

                # call the game board here once
                # the game board is fully functional

            if self.option.is_hover(pos):
                self.sound.play()
                self._game.gamestate = STATE.Option

            if self.quit.is_hover(pos):
                self.sound.play()
                self._game.running = False

        if self._game.gamestate == STATE.Option:
            if self.back.is_hover(pos):
                self.sound.play()
                self._game.gamestate = STATE.Menu

    def tick(self):
        """
        Animates the Menu given a pygame mouse event.
        If the pygame.event == MOUSEBUTTONDOWN, then
        animate accordingly.
        """
        if pygame.mouse.get_pressed()[0]:
            self.on_event(pygame.mouse)

    def render(self, screen: pygame.Surface):
        """
        Renders the game screen depending on the
        current game state.
        """
        # Draws the background
        background = pygame.image.load("./Assets/BACKGROUND.png").convert()

        screen.fill((0, 0, 0))
        rel_x = self._xpos % background.get_rect().width
        screen.blit(background, (rel_x - background.get_rect().width, 0))
        if rel_x < screen.get_width():
            screen.blit(background, (rel_x, 0))
        self._xpos -= 1
        if self._game.gamestate == STATE.Menu:

            # Set the text
            title = pygame.image.load("./Assets/title.png").convert()
            title.set_colorkey((85, 255, 0))
            screen.blit(title, ((self._game.width/2 - title.get_width()/2), 75))

            # Draw the Buttons
            self.play.draw(screen)
            self.option.draw(screen)
            self.quit.draw(screen)

        if self._game.gamestate == STATE.Option:
            self.back.draw(screen)

        if self._game.gamestate == STATE.End:
            screen.fill((0, 0, 0))



