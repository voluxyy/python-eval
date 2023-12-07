from Utils.Colors import Colors
from Menus.ClientsMenu import ClientsMenu
from Menus.BedroomsMenu import BedroomsMenu
from Menus.ReservationsMenu import ReservationsMenu

class Menu:
    def mainMenu():
        while(True):
            print(Colors.blue("\n**** Main Menu ****"))
            print("(1) Manage Clients\n"
                  "(2) Manage Bedrooms\n"
                  "(3) Manage Reservations\n"
                  "(0) Exit")
    
            userInput = 0
            while(True):
                while(True):
                    userInput = input(Colors.magenta("Enter number:"))

                    if userInput.isdigit():
                        break

                    print(Colors.red("You can only enter integer to choose!"))
                    
                userInput = int(userInput)

                if userInput >= 0 and userInput <= 3:
                    break
                
                print(Colors.red("Enter a number between 0 and 3 !"))
    
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
            print(Colors.blue("\n**** Clients Menu ****"))
            print("(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) List all\n"
                  "(0) Go back")
    
            userInput = 0
            while(True):
                while(True):
                    userInput = input(Colors.magenta("Enter number:"))

                    if userInput.isdigit():
                        break

                    print(Colors.red("You can only enter integer to choose!"))
                    
                userInput = int(userInput)

                if userInput >= 0 and userInput <= 4:
                    break
                
                print(Colors.red("Enter a number between 0 and 4 !"))
    
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
            print(Colors.blue("\n**** Bedrooms Menu ****"))
            print("(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) Print all\n"
                  "(0) Go back")
    
            userInput = 0
            while(True):
                while(True):
                    userInput = input(Colors.magenta("Enter number:"))

                    if userInput.isdigit():
                        break

                    print(Colors.red("You can only enter integer to choose!"))
                    
                userInput = int(userInput)

                if userInput >= 0 and userInput <= 4:
                    break
                
                print(Colors.red("Enter a number between 0 and 4 !"))

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
            print(Colors.blue("\n**** Reservations Menu ****"))
            print("(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) List all\n"
                  "(5) Export to csv\n"
                  "(0) Go back")
    
            userInput = 0
            while(True):
                while(True):
                    userInput = input(Colors.magenta("Enter number:"))

                    if userInput.isdigit():
                        break

                    print(Colors.red("You can only enter integer to choose!"))
                    
                userInput = int(userInput)

                if userInput >= 0 and userInput <= 5:
                    break
                
                print(Colors.red("Enter a number between 0 and 4 !"))

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