import pygame
from State import STATE
from Button import Button
import Game

WHITE = (255, 255, 255)

class Menu:
    """
    This class handles the different game screens of Connect 2^2 depending on
    the current game gamestate.

    ===Private Attributes===

    _game: reference of the Game class so that Menu can update the game

    ===Public Attributes===

    play: a Button with the label "PLAY"

    option: a Button with the label "OPTION"

    quit: a Button with the label "QUIT"

    back: a Button with the label "BACK"

    """
    # Private Instance Attributes
    _game: Game

    # Public Instance Attributes
    play: Button
    option: Button
    quit: Button
    back: Button

    def __init__(self, game):
        """
        Initializes a Menu that has the game, and buttons.

        :param game: the main game class
        """
        self._game = game
        self._xpos = 0
        self.sound = pygame.mixer.Sound("./Assets/audio/sfx/click.wav")
        self.trackname = "track_" + str(self._game.currtrack)

        # Creates reusable assets

        # Instantiates a translucent background
        self.transbg = pygame.Surface((700, 400))
        self.transbg.set_alpha(100)
        self.transbg.fill((0, 0, 0))

        # Instantiates the buttons
        # will need to split dictionary to specified screens
        self.buttons = {
            "play": Button((0, 0, 0), 350, 250, 50, 120, "PLAY", 20, True),
            "option": Button((0, 0, 0), 350, 350, 50, 120, "OPTION", 20, True),
            "quit": Button((0, 0, 0), 350, 450, 50, 120, "QUIT", 20, True),
            "back": Button((0, 0, 0), 650, 525, 50, 120, "BACK", 20, True),
            "arrowl": Button((0, 0, 0), 350, 115, 50, 50, " < ", 40, False),
            "arrowr": Button((0, 0, 0), 655, 115, 50, 50, " > ", 40, False),
            "arrow_bgm_l": Button((0, 0, 0), 350, 190, 50, 50, " < ", 40, False),
            "arrow_bgm_r": Button((0, 0, 0), 655, 190, 50, 50, " > ", 40, False),
            "arrow_sfx_l": Button((0, 0, 0), 350, 265, 50, 50, " < ", 40, False),
            "arrow_sfx_r": Button((0, 0, 0), 655, 265, 50, 50, " > ", 40, False),
            "return": Button((0, 0, 0), 350, 450, 50, 120, "RETURN", 20, True),
        }

    def on_click(self, mouse_press):
        """
        React to the given <mousepress> position to as appropriate to change
        the game state or to exit the game.
        """
        pos = mouse_press.get_pos()

        if self._game.gamestate == STATE.Menu:
            if self.buttons["play"].is_hover(pos):
                self.sound.play()
                self._game.gamestate = STATE.Game

                # call the game board here once
                # the game board is fully functional

            if self.buttons["option"].is_hover(pos):
                self.sound.play()
                self._game.gamestate = STATE.Option

            if self.buttons["quit"].is_hover(pos):
                self.sound.play()
                self._game.running = False

        elif self._game.gamestate == STATE.Option:

            if self.buttons["arrow_bgm_l"].is_hover(pos):
                self.sound.play()
                reduce_vol = -0.1
                curr_vol = pygame.mixer_music.get_volume() + reduce_vol
                if curr_vol <= 0:
                    pygame.mixer_music.set_volume(0)
                elif curr_vol > 0:
                    pygame.mixer_music.set_volume(curr_vol)

            if self.buttons["arrow_bgm_r"].is_hover(pos):
                self.sound.play()
                pygame.mixer_music.set_volume(pygame.mixer_music.get_volume() + 0.1)

            if self.buttons["arrow_sfx_l"].is_hover(pos):
                self.sound.play()
                reduce_vol = -0.1
                curr_vol = self.sound.get_volume() + reduce_vol
                if curr_vol <= 0:
                    self.sound.set_volume(0)
                elif curr_vol > 0:
                    self.sound.set_volume(curr_vol)

            if self.buttons["arrow_sfx_r"].is_hover(pos):
                self.sound.play()
                self.sound.set_volume(self.sound.get_volume() + 0.1)

            if self.buttons["arrowl"].is_hover(pos):
                self.sound.play()
                if self._game.currtrack > 0:
                    self._game.set_bgm(self._game.tracks[self._game.currtrack - 1],
                                       self._game.currtrack - 1)
                elif self._game.currtrack == 0:
                    self._game.set_bgm(self._game.tracks[-1],
                                       len(self._game.tracks) - 1)
                self.trackname = self.trackname[:-1] + str(self._game.currtrack)

            if self.buttons["arrowr"].is_hover(pos):
                self.sound.play()
                if self._game.currtrack < len(self._game.tracks) - 1:
                    self._game.set_bgm(self._game.tracks[self._game.currtrack + 1],
                                       self._game.currtrack + 1)
                elif self._game.currtrack == len(self._game.tracks) - 1:
                    self._game.set_bgm(self._game.tracks[0], 0)
                self.trackname = self.trackname[:-1] + str(self._game.currtrack)

            if self.buttons["back"].is_hover(pos):
                self.sound.play()
                self._game.gamestate = STATE.Menu

        elif self._game.gamestate == STATE.End:
            if self.buttons["return"].is_hover(pos):
                self.sound.play()
                self._game.gamestate = STATE.Menu

    def tick(self):
        """
        Animates the Menu given a pygame mouse event.
        If the pygame.event == MOUSEBUTTONDOWN, then
        animate accordingly.
        """
        for event in self._game.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.on_click(pygame.mouse)

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
            self.buttons["play"].draw(screen)
            self.buttons["option"].draw(screen)
            self.buttons["quit"].draw(screen)

        if self._game.gamestate == STATE.Option:
            # Create the font
            font = pygame.font.Font("./Assets/joystix_monospace.ttf", 40)
            font2 = pygame.font.Font("./Assets/joystix_monospace.ttf", 25)

            # Instantiate the text and other objects
            options = font.render("OPTION", 1, WHITE)
            bgm = font2.render("SELECT BGM", 1, WHITE)
            trknm = font2.render(self.trackname, 1, WHITE)
            bgm_vol = font2.render("BGM VOLUME", 1, WHITE)
            bgm_vol_num = font2.render(str(round(pygame.mixer_music.get_volume() * 10)), 1, WHITE)
            sfx_vol = font2.render("SFX VOLUME", 1, WHITE)
            sfx_vol_num = font2.render(str(round(self.sound.get_volume() * 10)), 1, WHITE)

            # Display the title and other objects
            screen.blit(self.transbg, (50, 100))
            pygame.draw.rect(screen, (255, 255, 255), (50, 100, 700, 400), 3)
            screen.blit(options, ((self._game.width/2 - options.get_width()/2), 40))
            screen.blit(bgm, (75, 125))
            screen.blit(trknm, ((655 + 350 + 50)/2 - trknm.get_width()/2, 125))  #around 450
            screen.blit(bgm_vol, (75, 200))
            screen.blit(bgm_vol_num, ((655 + 350 + 165)/2 - trknm.get_width()/2, 200))
            screen.blit(sfx_vol, (75, 275))
            screen.blit(sfx_vol_num, ((655 + 350 + 165)/2 - trknm.get_width()/2, 275))

            # Draw button
            self.buttons["back"].draw(screen)
            self.buttons["arrowl"].draw(screen)
            self.buttons["arrowr"].draw(screen)
            self.buttons["arrow_bgm_r"].draw(screen)
            self.buttons["arrow_bgm_l"].draw(screen)
            self.buttons["arrow_sfx_r"].draw(screen)
            self.buttons["arrow_sfx_l"].draw(screen)

        if self._game.gamestate == STATE.End:
            font = pygame.font.Font("./Assets/joystix_monospace.ttf", 50)
            font2 = pygame.font.Font("./Assets/joystix_monospace.ttf", 30)
            gameover = font.render("GAME OVER", 1, WHITE)

            winner = font2.render("Player " + self._game.get_winner()  + " WON", 1, WHITE)
            screen.blit(gameover, ((self._game.width/2 - gameover.get_width()/2), 70))
            screen.blit(winner, ((self._game.width/2 - winner.get_width()/2), 275))

            self.buttons["return"].draw(screen)



