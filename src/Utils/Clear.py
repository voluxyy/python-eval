import os

class Clear:
    def ClearTerminal():
        os.system('cls' if os.name == 'nt' else 'clear')