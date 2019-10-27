import pygame
from State import STATE
from Button import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
LIGHTBLUE = (204, 204, 255)


class DisplayBoard:
    """
    Connect 2^2 main game visualizer. Acts as the controller to Board.py, and updates Game.py
    """

    def __init__(self, game, handler, board):
        self.game = game
        self.handler = handler
        self.buttons = []
        self.board = board

        for row in range(7):
            self.buttons.append(Button((0, 0, 0), (game.width + 50)/8 * row + 30, 50, 55, 100, " "))


    def on_event(self, mousepress):
        pos = mousepress

        for button in self.buttons:
            if button.is_hover(pos):
                ##does some action with the game
                print("CLICKK")
                pass

    def tick(self):
        if pygame.mouse.get_pressed()[0]:
            self.on_event(pygame.mouse.get_pos())

    def render(self, display):
        display.fill((150, 150, 150))

        for button in self.buttons:
            button.draw(display)

        SLOTSIZE = 75
        HOLE_SIZE = int(SLOTSIZE / 2) - 10
        NUMBEROFCOLUMNS = self.board.get_grid_size()[1]
        NUMBEROFROWS = self.board.get_grid_size()[0]

        # Creates the pyGame Board with corresponding slots and holes from the matrix board representation.
        # This strategy for creating the board was inspired by a tutorial on freeCodeCamp.org.
        #   Video URL: https://www.youtube.com/watch?v=XpYz-q1lxu8
        for column in range(NUMBEROFCOLUMNS):
            for row in range(NUMBEROFROWS):
                pygame.draw.rect(display, LIGHTBLUE, (
                125 + column * SLOTSIZE, 110 + row * SLOTSIZE, SLOTSIZE,
                SLOTSIZE))
                pygame.draw.circle(display, BLACK, (
                160 + column * SLOTSIZE, 145 + row * SLOTSIZE), HOLE_SIZE)

