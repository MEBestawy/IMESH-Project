from Board import Board 

class playInConsole:
    
    """
    
    The Connect2^2 game in the console. Used to faciliate the implementation 
    of the game in pyGame.
    
    ===Public Attributes===
    board: The board we are playing the Connect 2^2 game in.
    turn: Who's turn it is in the game.
    """
    
    board: Board
    turn: int
    
    def __init__(self) -> None:
        """
        Initializes the game in the console.
        """
        self.board = Board()
        
        #Set the first player's turn
        self.turn = 0
        
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
            
    def play(self) -> None:
        
        """
        The game loop in the console.
        """
        
        game_over = self.board.get_winner() != self.board.EMPTY
        
        while not game_over:
        
            print(self.board)
            
            if self.turn == 0:
                print(self.board.P1 + " Moves Next.")
            elif self.turn == 1:
                print(self.board.P2 + " Moves Next.")
                
            column = input("Pick a Column to Move to: ")
            self.move_next(int(column))
            
            game_over = self.board.get_winner() != self.board.EMPTY
                
        print("")
        print(self.board.get_winner() + "Won!")
        return
        
        
if __name__ == "__main__":
    game = playInConsole()
    game.play()