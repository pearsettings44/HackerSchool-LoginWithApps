import main as c

class Calculator():
    """
    Calculator Class: Represents a calculator.
    """
    def __init__(self):
        self.mainmenu()
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
            self.docalculation()
        else:
            print("Please type a valid option! ")
            self.getoption()
    
    def docalculation():
        
