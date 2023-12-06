import Menus.ClientsMenu as ClientsMenu
import Menus.BedroomsMenu as BedroomsMenu
import Menus.ReservationsMenu as ReservationsMenu
import Utils.Colors as Colors

class Menu:
    def mainMenu():
        while(True):
            print(Colors.Colors.blue("\n**** Main Menu ****"))
            print("(1) Manage Clients\n"
                  "(2) Manage Bedrooms\n"
                  "(3) Manage Reservations\n"
                  "(0) Exit")
    
            userInput = 0
            while(True):
                while(True):
                    userInput = input(Colors.Colors.magenta("Enter number:"))

                    if userInput.isdigit():
                        break

                    print(Colors.Colors.red("You can only enter integer to choose!"))
                    
                userInput = int(userInput)

                if userInput >= 0 and userInput <= 3:
                    break
                
                print(Colors.Colors.red("Enter a number between 0 and 3 !"))
    
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
            print(Colors.Colors.blue("\n**** Clients Menu ****"))
            print("(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) List all\n"
                  "(0) Go back")
    
            userInput = 0
            while(True):
                while(True):
                    userInput = input(Colors.Colors.magenta("Enter number:"))

                    if userInput.isdigit():
                        break

                    print(Colors.Colors.red("You can only enter integer to choose!"))
                    
                userInput = int(userInput)

                if userInput >= 0 and userInput <= 4:
                    break
                
                print(Colors.Colors.red("Enter a number between 0 and 4 !"))
    
            if userInput == 0:
                break
            elif userInput == 1:
                ClientsMenu.ClientsMenu.AddClient()
            elif userInput == 2:
                ClientsMenu.ClientsMenu.UpdateClient()
            elif userInput == 3:
                ClientsMenu.ClientsMenu.RemoveClient()
            elif userInput == 4:
                ClientsMenu.ClientsMenu.PrintAll()
    
    
    def bedroomsMenu():
        while(True):
            print(Colors.Colors.blue("\n**** Bedrooms Menu ****"))
            print("(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) Print all\n"
                  "(0) Go back")
    
            userInput = 0
            while(True):
                while(True):
                    userInput = input(Colors.Colors.magenta("Enter number:"))

                    if userInput.isdigit():
                        break

                    print(Colors.Colors.red("You can only enter integer to choose!"))
                    
                userInput = int(userInput)

                if userInput >= 0 and userInput <= 4:
                    break
                
                print(Colors.Colors.red("Enter a number between 0 and 4 !"))

            if userInput == 0:
                break
            elif userInput == 1:
                BedroomsMenu.BedroomsMenu.AddBedroom()
            elif userInput == 2:
                BedroomsMenu.BedroomsMenu.UpdateBedroom()
            elif userInput == 3:
                BedroomsMenu.BedroomsMenu.RemoveBedroom()
            elif userInput == 4:
                BedroomsMenu.BedroomsMenu.PrintAll()
    
    
    def reservationsMenu():
        while(True):
            print(Colors.Colors.blue("\n**** Reservations Menu ****"))
            print("(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) List all\n"
                  "(5) Export to csv\n"
                  "(0) Go back")
    
            userInput = 0
            while(True):
                while(True):
                    userInput = input(Colors.Colors.magenta("Enter number:"))

                    if userInput.isdigit():
                        break

                    print(Colors.Colors.red("You can only enter integer to choose!"))
                    
                userInput = int(userInput)

                if userInput >= 0 and userInput <= 5:
                    break
                
                print(Colors.Colors.red("Enter a number between 0 and 4 !"))

            if userInput == 0:
                break
            elif userInput == 1:
                ReservationsMenu.ReservationsMenu.AddReservation()
            elif userInput == 2:
                ReservationsMenu.ReservationsMenu.UpdateReservation()
            elif userInput == 3:
                ReservationsMenu.ReservationsMenu.RemoveReservation()
            elif userInput == 4:
                ReservationsMenu.ReservationsMenu.PrintAll()
            elif userInput == 5:
                ReservationsMenu.ReservationsMenu.ExportToCsv()