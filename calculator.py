import main as c

class Calculator():
    """
    Calculator Class: Represents a calculator.
    """
    def __init__(self):
        self.displaylogo()
    def displaylogo(self):
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

my = Calculator()