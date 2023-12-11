import os
from Utils.Colors import Colors

class Clear:
    def ClearTerminal():        
        os.system('cls' if os.name == 'nt' else 'clear')

    def askToExit():
        while(True):
            try:
                userInput = int(input(Colors.magenta("Enter 0 to leave: ")))
                
                if userInput == 0:
                    break
                else:
                    raise Exception(2)
            except Exception as error:
                    if error.args[0] == 2:
                        print(Colors.red(f"Only 0 is possible to leave!"))
                    else:
                        print(Colors.red("You can only enter integer to choose!"))
