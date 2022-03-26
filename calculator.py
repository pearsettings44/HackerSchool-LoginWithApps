import main as c
import os


class Calculator():
    """
    Calculator Class: Represents a calculator.
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
        Displays the calculator logo.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        logo = \
            f"""{c.Color.BOLD}{c.Color.GREEN}
 _____   ___   _     _____ _   _ _       ___ _____ ___________ 
/  __ \ / _ \ | |   /  __ \ | | | |     / _ \_   _|  _  | ___ \\
| /  \// /_\ \| |   | /  \/ | | | |    / /_\ \| | | | | | |_/ /
| |    |  _  || |   | |   | | | | |    |  _  || | | | | |    / 
| \__/\| | | || |___| \__/\ |_| | |____| | | || | \ \_/ / |\ \ 
 \____/\_| |_/\_____/\____/\___/\_____/\_| |_/\_/  \___/\_| \_|
        {c.Color.END}"""
        print(logo)

    def mainmenu(self):
        """
        Displays the main menu
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.displaylogo
        print("1 )Solve basic calculations.")
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
        # Basic calculation option
        if option == '1':
            self.clearscreen()
            self.docalculation()
        else:
            print("Please type a valid option! ")
            self.getoption()

    def docalculation(self):
        """
        Uses eval to get the result of the expression given by the user.
        Parameters
        ----------
        None
        
        Results
        -------
        None
        """
        self.displaylogo()
        print(f"\t{c.Color.BOLD}                   Please use:{c.Color.END}")
        print(f"\t  ({c.Color.BOLD}{c.Color.GREEN}+{c.Color.END})"
              f"for adition              ({c.Color.BOLD}{c.Color.GREEN}-"
              f"{c.Color.END}) for subtraction:")
        print(f"\t  ({c.Color.BOLD}{c.Color.GREEN}*{c.Color.END})"
              f"for multiplication       ({c.Color.BOLD}{c.Color.GREEN}/"
              f"{c.Color.END}) for division")
        print(f"\t  ({c.Color.BOLD}{c.Color.GREEN}**{c.Color.END})"
              f"for exponent            ({c.Color.BOLD}{c.Color.GREEN}%"
              f"{c.Color.END}) for rest of")

        expression = input("\n\n\t  Enter your expression here -> ")
        result = eval(expression)
        print(f"\n\t                   {c.Color.GREEN}result: {c.Color.END}"
              f"{result}")
