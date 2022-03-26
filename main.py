
import os

# Clear the terminal's screen, using the cls command on Windows, or
# the clear command on UNIX systems.
os.system('cls' if os.name == 'nt' else 'clear')

class Menu():
    """
    Menu Class: handles the HackerSchool's App screen
    """

    def __init__(self):
        pass

    def mainmenu(self):
        """
        Displays the main menu.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        print("_   _            _               ____       _                 _ ")
        print("| | | | __ _  ___| | _____ _ __  / ___|  ___| |__   ___   ___ | |")
        print("| |_| |/ _` |/ __| |/ / _ \ '__| \___ \ / __| '_ \ / _ \ / _ \| |")
        print("|  _  | (_| | (__|   <  __/ |     ___) | (__| | | | (_) | (_) | |")
        print("|_| |_|\__,_|\___|_|\_\___|_|    |____/ \___|_| |_|\___/ \___/|_|")
        print("\n\n")
        print("    Login                  Register                  Exit ")
        print("   type(L)                  type(R)                 type(E)")
        print("\n")

    def getoption(self):
        """
        Gets the user option.
        Parameters
        ----------
        None

        Returns
        -------
        str
        """
        option = input("Option: ")
        return option


