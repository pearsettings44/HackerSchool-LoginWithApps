import main as c
import os

class Tittactoe():
    """
    A class to represent a Tic Tac Toe game.
    """
    def __init__(self):
        self.createboard()

    def clearscreen(self):
            """
            Clear the terminal's screen, using the cls command on Windows, or
            the clear command on UNIX systems.
            Parameters
            ----------
            None

            Returns
            -------
            None
            """
            os.system('cls' if os.name == 'nt' else 'clear')
    
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
        self.displayboard(board)
    
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
