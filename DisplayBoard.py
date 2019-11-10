import pygame
from State import STATE
from Board import Board

# GLOBAL variables for RGB of colours on the board
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
LIGHTBLUE = (183, 208, 218)
BLUE = (65, 105, 225)
GREY = (100, 118, 141)
LIGHTERBLUE = (217, 233, 239)
NAVY = (71, 124, 163)
DARKGREY = (50, 50, 50)


class DisplayBoard:
    """
    The main Connect 2^2 game visualizer.
    
    This is where each player can play the game, until someone wins.  
    
    The class acts as the controller to Board.py, and updates Game.py.
    
    === Public Attributes ===
    
    board: The board where the Connect 2^2 game is being played. 
    
    turn: Who's turn it is in the game. The first player is represented with 
    a 0, and the 2nd with a 1. 
    
    === Private Attributes === 
    _game: This represents the main game loop. In other words, this is the 
    pyGame window that contains the main menu, this gameBoard and our endscreen. 
    
    """
    def __init__(self, game, board):
        """
        Initializes the game with a board and displays this in pyGame.
        """
        self._game = game

        self.board = Board()

        self.turn = 0
        

    def on_event(self, mousepress) -> None:
        """
        After each mousepress, this method handles what to do. 
        """
        selected_column = self.get_column(mousepress)
        self.move_next(selected_column)

    def tick(self):
        """
        This method detects any mouse clicks on the pyGame window. 
        """
        for event in self._game.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.on_event(pygame.mouse)
                pygame.mixer.Sound("./Assets/audio/sfx/click.wav").play()

    def render(self, display: pygame.Surface)-> None:
        """
        Renders the changes on the display after each event.
        """

        self.update_board(display)


    def update_board(self, display: pygame.Surface)-> None:
        """
        This continously updates the board after every move in the Connect 
        2^2 game.
        """

        # Adding the board background to the game
        board_background = pygame.image.load('./Assets/BOARD2.png').convert()
        display.blit(board_background, (0,0))
        
        """
        Grid coordinates of the Board in BOARD2.png:
            
        topLeft = (138, 75)
        bottomLeft = (138, 525)
        
        topRight = (663, 75)
        bottomRight = (663, 525)
        """
        
         # The size of each slot of the board
        SLOT_SIZE = 75
        HOLE_SIZE = 25

        NUMBEROFCOLUMNS = self.board.get_grid_size()[1]
        NUMBEROFROWS = self.board.get_grid_size()[0]

        # The matrix representation of the grid
        grid = self.board.get_grid()

        # If there is a winner, switch to the end screen
        if self.board.get_winner() != '-':
            
            self._game.set_winner(self.board.get_winner())
            self.reset_board()
            self._game.gamestate = STATE.End

        # Creates the slots and holes on the board,
        # then updates the board from the matrix board representation.
        # This strategy for creating the board was inspired by a tutorial on freeCodeCamp.org.
        # Video URL: https://www.youtube.com/watch?v=XpYz-q1lxu8
        for column in range(NUMBEROFCOLUMNS):
            
            for row in range(NUMBEROFROWS):
                
                if grid[row][column] == 'X':
                    pygame.draw.circle(display,
                                       DARKGREY,
                                       (138 + (SLOT_SIZE//2) + column*(SLOT_SIZE), 75 + (SLOT_SIZE//2) + row*(SLOT_SIZE)),
                                       HOLE_SIZE)
                    
                    
                elif grid[row][column] == 'O':                
                    pygame.draw.circle(display,
                                       NAVY,
                                       (138 + (SLOT_SIZE//2) + column*(SLOT_SIZE), 75 + (SLOT_SIZE//2) + row*(SLOT_SIZE)),
                                       HOLE_SIZE)
                    
                    
                else:    
                    pygame.draw.circle(display,
                                       LIGHTBLUE,
                                       (138 + (SLOT_SIZE//2) + column*(SLOT_SIZE), 75 + (SLOT_SIZE//2) + row*(SLOT_SIZE)),
                                       HOLE_SIZE)
                                       
        
        #Displays who's turn it is in the game
        font = pygame.font.Font("./Assets/joystix_monospace.ttf", 20)

        if self.turn == 0:
            text = font.render("Player 1's Turn. Pick Where to Drop Disc.", True, WHITE, BLACK)
        elif self.turn == 1:
            text = font.render("Player 2's Turn. Pick Where to Drop Disc.", True, WHITE, BLACK)
            
        goal = font.render("Connect 2^2 Discs in a Row.", True, WHITE, BLACK)
        goalBox = goal.get_rect(center=(400, 35))
        textBox = text.get_rect(center=(400,560))
        
        display.blit(text, textBox)
        display.blit(goal, goalBox)

        pygame.display.flip()


    def move_next(self, column: int) -> bool:
        """
        Makes a move depending on who's turn it is. Doesn't change the turn
        if the player's input was invalid.
        """

        if self.turn == 0:

            if self.board.move(self.board.P1, column):
                self.turn += 1
                return True

        elif self.turn == 1:

            if self.board.move(self.board.P2, column):
                self.turn -= 1
                return True
        return False


    def get_column(self, mousepress) -> int:
        
        """
        Returns which column the player picked, or -1 if they picked an invalid
        move.
        
        """
        
        x_position = mousepress.get_pos()[0]
        y_position = mousepress.get_pos()[1]
        
        # Invalid Y Coordinates on the Board
        if y_position > 500:
            return -1
        
        # Valid X Coordinates of the Board
        if 138 <= x_position <= 663:
            
            width = 663-138
            
            width_of_columns = width // 7
            
            # return which column was picked w/ a simple calculation
            return (x_position-138)//width_of_columns
          
        # Invalid X Coordinate
        else:
            return -1
        
        
    def reset_board(self) -> None:
        """
        This class resets the board, so that we can play again, if the
        player chooses to.
        """
        
        # Clear Board to a new Board
        self.board = Board()
        
        # Reset Turn
        self.turn = 0
        








