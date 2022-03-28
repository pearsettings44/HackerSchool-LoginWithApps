class Tittactoe():
    """
    A class to represent a Tic Tac Toe game.
    """
    def __init__(self):
        pass

    def createboard(self):
        """
        Creates the game board
        Parameters
        ----------
        None

        Returns
        -------
        board : list
        """
        board = [['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-']]
        return board
    
    def displayboard(self, board):
        """
        Displays the game board.
        Parameters
        ----------
        board : list

        Returns
        -------
        None
        """
        for row in board:
            for collum in row:
                print(collum, end= ' ')
            print("\n", end= "")

my = Tittactoe()
board = my.createboard()
my.displayboard(board)
