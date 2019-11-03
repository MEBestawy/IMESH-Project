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
        self.trackname = "track_" + str(self._game.currtrack)

        # Creates reusable assets

        # Instantiates a translucent background
        self.transbg = pygame.Surface((700, 400))
        self.transbg.set_alpha(100)
        self.transbg.fill((0, 0, 0))

        # Instantiates the buttons
        self.play = Button((0, 0, 0), 350, 250, 50, 120, "PLAY", 20, True)
        self.option = Button((0, 0, 0), 350, 350, 50, 120, "OPTION", 20, True)
        self.quit = Button((0, 0, 0), 350, 450, 50, 120, "QUIT", 20, True)
        self.back = Button((0, 0, 0), 650, 525, 50, 120, "BACK", 20, True)
        self.arrowl = Button((0, 0, 0), 350, 115, 50, 50, " < ", 40, False)
        self.arrowr = Button((0, 0, 0), 655, 115, 50, 50, " > ", 40, False)

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

        elif self._game.gamestate == STATE.Option:

            if self.arrowl.is_hover(pos):
                self.sound.play()
                if self._game.currtrack > 0:
                    self._game.set_bgm(self._game.tracks[self._game.currtrack - 1],
                                       self._game.currtrack - 1)
                elif self._game.currtrack == 0:
                    self._game.set_bgm(self._game.tracks[-1],
                                       len(self._game.tracks) - 1)
                self.trackname = self.trackname[:-1] + str(self._game.currtrack)

            if self.arrowr.is_hover(pos):
                self.sound.play()
                if self._game.currtrack < len(self._game.tracks) - 1:
                    self._game.set_bgm(self._game.tracks[self._game.currtrack + 1],
                                       self._game.currtrack + 1)
                elif self._game.currtrack == len(self._game.tracks) - 1:
                    self._game.set_bgm(self._game.tracks[0], 0)
                self.trackname = self.trackname[:-1] + str(self._game.currtrack)

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
            if not self._game.pressed:
                self.on_event(pygame.mouse)
                self._game.pressed = True

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
            # Create the font
            font = pygame.font.Font("./Assets/joystix_monospace.ttf", 40)
            font2 = pygame.font.Font("./Assets/joystix_monospace.ttf", 25)

            # Instantiate the text and other objects
            options = font.render("OPTIONS", 1, (255, 255, 255))
            bgm = font2.render("SELECT BGM", 1, (255, 255, 255))
            trknm = font2.render(self.trackname, 1, (255, 255, 255))


            # Display the title and other objects
            screen.blit(self.transbg, (50, 100))
            pygame.draw.rect(screen, (255, 255, 255), (50, 100, 700, 400), 3)
            screen.blit(options, ((self._game.width/2 - options.get_width()/2), 40))
            screen.blit(bgm, (75, 125))
            screen.blit(trknm, ((655 + 350 + 50)/2 - trknm.get_width()/2, 125))  #around 450

            # Draw button
            self.back.draw(screen)
            self.arrowl.draw(screen)
            self.arrowr.draw(screen)

        if self._game.gamestate == STATE.End:
            screen.fill((0, 0, 0))



