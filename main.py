import os

# Allow colors on windows sytems.
os.system('color')


class Color:
    """
    Color Class: Store text color/style ANSI escapes sequences.
    """
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


class Menu():
    """
    Menu Class: handles the HackerSchool's App screen
    """

    def __init__(self):
        self.mainmenu()

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

    def displaylogo(self):
        """
        Displays the HackerSchool logo.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        logo = \
            f"""{Color.BOLD}{Color.GREEN}
 _   _            _               ____       _                 _
| | | | __ _  ___| | _____ _ __  / ___|  ___| |__   ___   ___ | |
| |_| |/ _` |/ __| |/ / _ \ '__| \___ \ / __| '_ \ / _ \ / _ \| |
|  _  | (_| | (__|   <  __/ |     ___) | (__| | | | (_) | (_) | |
|_| |_|\__,_|\___|_|\_\___|_|    |____/ \___|_| |_|\___/ \___/|_|
                {Color.END}
        """
        print(logo)

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
        self.clearscreen()
        self.displaylogo()
        print("    Login                  Register                  Exit ")
        print("   type(L)                  type(R)                 type(E)")
        print("\n")
        self.getoption()

    def getoption(self):
        """
        Gets the user option.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        option = input("Option: ")
        self.handleoption(option)

    def handleoption(self, option):
        """
        Handles the user option. If it's an invalid option,
        ask user again for a valid option.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # Login option.
        if (option in ('L', 'l')):
            self.loginmenu()
        # Register option.
        elif (option in ('R', 'r')):
            pass
        # Exit option.
        elif (option in ('E', 'e')):
            quit()
        # Invalid option.
        else:
            print("Please type a valid option! ")
            self.getoption()

    def loginmenu(self):
        """
        Displays the login Menu.
        Parameters
        ----------
        None

        Returns
        -------
        None
         """
        self.clearscreen()
        self.displaylogo()
        print(f"{Color.BOLD}                           Welcome back!\n\n")
        username = input("                     username: ")
        password = input("                     password: ")
        


mymenu = Menu()
