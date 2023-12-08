from Utils.Colors import Colors
from Utils.Clear import Clear
from Menus.ClientsMenu import ClientsMenu
from Menus.BedroomsMenu import BedroomsMenu
from Menus.ReservationsMenu import ReservationsMenu

class Menu:
    def mainMenu():
        while(True):
            Clear.ClearTerminal()
            print(Colors.blue("**** Main Menu ****"))
            print("(1) Manage Clients\n"
                  "(2) Manage Bedrooms\n"
                  "(3) Manage Reservations\n"
                  "(0) Exit")
    
            userInput = Menu.Input("Enter number: ", 0, 3)

            if userInput == 0:
                break
            elif userInput == 1:
                Menu.clientsMenu()
            elif userInput == 2:
                Menu.bedroomsMenu()
            elif userInput == 3:
                Menu.reservationsMenu()
    

    def clientsMenu():
        while(True):
            Clear.ClearTerminal()
            print(Colors.blue("**** Clients Menu ****"))
            print("(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) List all\n"
                  "(0) Go back")
    
            userInput = Menu.Input("Enter number: ", 0, 4)
    
            if userInput == 0:
                break
            elif userInput == 1:
                ClientsMenu.AddClient()
            elif userInput == 2:
                ClientsMenu.UpdateClient()
            elif userInput == 3:
                ClientsMenu.RemoveClient()
            elif userInput == 4:
                ClientsMenu.PrintAll()
    
    
    def bedroomsMenu():
        while(True):
            Clear.ClearTerminal()
            print(Colors.blue("**** Bedrooms Menu ****"))
            print("(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) Print all\n"
                  "(0) Go back")
    
            userInput = Menu.Input("Enter number: ", 0, 4)

            if userInput == 0:
                break
            elif userInput == 1:
                BedroomsMenu.AddBedroom()
            elif userInput == 2:
                BedroomsMenu.UpdateBedroom()
            elif userInput == 3:
                BedroomsMenu.RemoveBedroom()
            elif userInput == 4:
                BedroomsMenu.PrintAll()
    
    
    def reservationsMenu():
        while(True):
            Clear.ClearTerminal()
            print(Colors.blue("**** Reservations Menu ****"))
            print("(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) List all\n"
                  "(5) Export to csv\n"
                  "(0) Go back")
    
            userInput = Menu.Input("Enter number: ", 0, 5)

            if userInput == 0:
                break
            elif userInput == 1:
                ReservationsMenu.AddReservation()
            elif userInput == 2:
                ReservationsMenu.UpdateReservation()
            elif userInput == 3:
                ReservationsMenu.RemoveReservation()
            elif userInput == 4:
                ReservationsMenu.PrintAll()
            elif userInput == 5:
                ReservationsMenu.ExportToCsv()

    def Input(str, min, max):
        while(True):
            try:
                userInput = int(input(Colors.magenta(str)))
                
                if userInput >= min and userInput <= max:
                    break
                else:
                    raise Exception(2)
            except Exception as error:
                    if error.args[0] == 2:
                        print(Colors.red(f"Enter a number between {min} and {max} !"))
                    else:
                        print(Colors.red("You can only enter integer to choose!"))

        return userInput