import os
import time

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
        if option in ('L', 'l'):
            self.loginmenu()
        # Register option.
        elif option in ('R', 'r'):
            self.registermenu()
        # Exit option.
        elif option in ('E', 'e'):
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
        print(f"{Color.BOLD}\t\t\t  Welcome back!\n\n{Color.END}")

        username = input("\t\t\t  username: ")
        password = input("\t\t\t  password: ")
        auth = self.verifyuser(username, password)

        # Case invalid user.
        if auth == -2:
            print(f"\n\n{Color.RED}Theres no user{Color.END} "
                  f"{Color.BOLD}{username}{Color.END} "
                  f"{Color.BOLD}{Color.RED}registered"
                  "in our database{Color.END}")
            # Wait 2 seconds and return to the main menu.
            time.sleep(2)
            self.mainmenu()

        # Case invalid password.
        elif auth == -1:
            print(f"\n\n{Color.BOLD}{Color.RED}Wrong password!{Color.END}")
            # Wait 2 seconds and return to the main menu.
            time.sleep(2)
            self.mainmenu()
        else:
            print(f"\n\n\t\t\t"
                  f"{Color.BOLD}{Color.GREEN}SUCCESSFUL LOGIN!{Color.END}")
            # Wait 0.2 seconds and return to the main menu.
            time.sleep(0.2)
            self.clearscreen()
            self.loadingscreen("SUCCESSFUL LOGIN")
            self.usermenu(username)

    def verifyuser(self, username, password):
        """
        Check if the username and password are valid.
        Parameters
        ----------
        username: str
        password: str

        Returns
        -------
        int
        """
        # Open the database file.
        database = open("password.txt", "r")
        for line in database:
            # Get user and password (using split), and remove then \n at the
            # the end (using rstrip()).
            user_pass = line.rstrip().split(":")
            # Search for a matching username.
            if username == user_pass[0]:
                # Check if the password matches the username.
                if password != user_pass[1]:
                    database.close()
                    return -1
                database.close()
                return
        database.close()
        return -2

    def loadingscreen(self, message):
        """
        Displays the loading screen, with the specified message.
        Parameters
        ----------
        message: str

        Returns
        -------
        None
        """
        print(f"\n\n\t\t\t"
              f"{Color.BOLD}{Color.GREEN}{message}{Color.END}")
        print("\t\t\t   Loading…")
        print("\t\t\t   █▒▒▒▒▒▒▒▒▒""")
        self.clearscreen()
        print(f"\n\n\t\t\t"
              f"{Color.BOLD}{Color.GREEN}{message}{Color.END}")
        print("\t\t\t   25%")
        print("\t\t\t   ███▒▒▒▒▒▒▒")
        time.sleep(0.75)
        self.clearscreen()
        print(f"\n\n\t\t\t"
              f"{Color.BOLD}{Color.GREEN}{message}{Color.END}")
        print("\t\t\t   50%")
        print("\t\t\t   █████▒▒▒▒▒")
        time.sleep(0.75)
        self.clearscreen()
        print(f"\n\n\t\t\t"
              f"{Color.BOLD}{Color.GREEN}{message}{Color.END}")
        print("\t\t\t   75%")
        print("\t\t\t   ███████▒▒▒")
        time.sleep(0.75)
        self.clearscreen()
        print(f"\n\n\t\t\t"
              f"{Color.BOLD}{Color.GREEN}{message}{Color.END}")
        print("\t\t\t   100%")
        print("\t\t\t   ██████████")
        self.clearscreen()

    def registermenu(self):
        """
        Displays the register Menu.
        Parameters
        ----------
        None

        Returns
        -------
        None
         """
        self.clearscreen()
        self.displaylogo()
        print(f"{Color.BOLD}\t\t\t  Welcome!\n\n{Color.END}")
        print(f"{Color.BOLD}\t\t\t  Enter your credentials!\n\n{Color.END}")

        username = input("\t\t\t  username: ")
        password = input("\t\t\t  password: ")
        # Add user to the data base.
        self.registeruser(username, password)
        time.sleep(0.2)
        self.clearscreen()
        self.loadingscreen(f"Registering user {username}")
        self.clearscreen()
        # Go back to the main menu.
        self.mainmenu()

    def registeruser(self, username, password):
        """
        Adds a new user to the database
        Parameters
        ----------
        username: str
        password: str

        Returns
        -------
        None
        """
        database = open("password.txt", "a")
        # Write the credentials at the end of the database file.
        database.write(f"\n{username}:{password}")
        database.close()

    def usermenu(self, username):
        """
        Displays the user menu, with option to use an app,
        change the user password and log out.
        Parameters
        ----------
        username : str
        
        Returns
        -------
        None
        
        """
        self.displaylogo()
        print(f"\n\t\t\t  {Color.BOLD}{Color.CYAN}Welcome back "
              f"{username}{Color.END}\n\n")
        print("\t\t\t  1) Use the calculator\n")
        print("\t\t\t  2) Change your password\n")
        print("\t\t\t  3) Logout\n\n")
        self.getuseroption()

    def getuseroption(self):
        """
        Gets the user option.
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        option = input("\t\t\t  option:")
        self.handleuseroption(option)
    
    def handleuseroption(self, option):
        """
        Handles the user option.
        Parameters
        ----------
        option : str
        
        Returns
        -------
        None
        """
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            self.clearscreen()
            self.loadingscreen("Loging out . . .")
            self.mainmenu()
        else:
            print("Please type a valid option! ")
            self.getuseroption()
        
mymenu = Menu()
