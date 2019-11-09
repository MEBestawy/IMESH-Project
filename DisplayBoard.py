import pygame
from State import STATE
from Button import Button
from Board import Board


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
LIGHTBLUE = (183, 208, 218)
BLUE = (65, 105, 225)
GREY = (100, 118, 141)
LIGHTERBLUE = (217, 233, 239)
NAVY = (0, 76, 153)


class DisplayBoard:
    """
    Connect 2^2 main game visualizer.
    Acts as the controller to Board.py, and updates Game.py.
    """
    def __init__(self, game, handler, board):
        self.game = game
        
        self.board = Board()
        
        self.handler = handler
        self.buttons = []
        
        # Who's turn it is in the game:
        self.turn = 0

    def on_event(self, mousepress):
        # print(pygame.mouse.get_pos())
        selected_column = self.get_column(mousepress)

        self.move_next(selected_column)
        

    def tick(self):
        for event in self.game.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.on_event(pygame.mouse)

    def render(self, display):
        
        self.start_game(display)

        
    def start_game(self, display):
        # CHANGING THE GAME BACKGROUND
        display.fill((255, 255, 255))


        SLOTSIZE = 75
        HOLE_SIZE = int(SLOTSIZE / 2) - 10

        NUMBEROFCOLUMNS = self.board.get_grid_size()[1]
        NUMBEROFROWS = self.board.get_grid_size()[0]

        # Adding a Background
        board_background = pygame.image.load('./Assets/BOARD.png').convert()
        display.blit(board_background, (0, 0))
        
        # The matrix representation of the grid
        grid = self.board.get_grid()

        # Creates the pyGame Board with corresponding slots and holes from the matrix board representation.
        # This strategy for creating the board was inspired by a tutorial on freeCodeCamp.org.
        # Video URL: https://www.youtube.com/watch?v=XpYz-q1lxu8

        for column in range(NUMBEROFCOLUMNS):

            for row in range(NUMBEROFROWS):
                
                if grid[row][column] == 'X':
                    pygame.draw.circle(display,
                                       BLACK,
                                       (190 + (column * (SLOTSIZE-5)), 122 + (row * (SLOTSIZE-5))),
                                        HOLE_SIZE)
                    
                elif grid[row][column] == 'O':
                    
                    pygame.draw.circle(display,
                                       NAVY,
                                       (190 + (column * (SLOTSIZE-5)), 122 + (row * (SLOTSIZE-5))),
                                        HOLE_SIZE)
 
                else:
                    pygame.draw.circle(display,
                                       LIGHTERBLUE,
                                       (190 + (column * (SLOTSIZE-5)), 122 + (row * (SLOTSIZE-5))),
                                        HOLE_SIZE)
                
        font = pygame.font.Font("./Assets/joystix_monospace.ttf", 20)
        
        
        if self.turn == 0:
            text = font.render("Player 1's Turn.", True, WHITE, BLACK)
        elif self.turn == 1:
            text = font.render("Player 2's Turn.", True, WHITE, BLACK)
            
            
        textBox = text.get_rect(center=(400,560))

        display.blit(text, textBox)
        
        pygame.display.flip()
        

    def move_next(self, column: int) -> None:
        """
        Makes a move depending on who's turn it is. Doesn't change the turn
        if the player's input was invalid.
        """
        
        if self.turn == 0:
            
            if self.board.move(self.board.P1, column):
                self.turn += 1
            
        elif self.turn == 1:
            
            if self.board.move(self.board.P2, column):
                self.turn -= 1
                
    
    def get_column(self, mousepress):
        # Will need to refactor this.
        position = mousepress.get_pos()[0]
        
        if 161 <= position <= 217:
            return 0

        elif 231 <= position <= 287:
            return 1

        elif 302 <= position <= 358:
            return 2

        elif 371 <= position <= 427:
            return 3

        elif 441 <= position <= 497:
            return 4

        elif 511 <= position <= 567:
            return 5

        elif 581 <= position <= 637:
            return 6

        else:
            return -1









