import Utils.ClientsMenu as ClientsMenu
import Utils.BedroomsMenu as BedroomsMenu

class Menu:
    def mainMenu():
        while(True):
            print("**** Main Menu ****\n"
                  "(1) Manage Clients\n"
                  "(2) Manage Bedrooms\n"
                  "(3) Manage Reservations\n"
                  "(0) Exit")
    
            userInput = 0
            while(True):
                userInput = int(input("Enter number:"))
    
                if userInput >= 0 and userInput <= 3:
                    break
                
                print("Enter a number between 0 and 3 !")
    
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
            print("**** Clients Menu ****\n"
                  "(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) List all\n"
                  "(0) Go back")
    
            userInput = 0
            while(True):
                userInput = int(input("Enter number:"))
    
                if userInput >= 0 and userInput <= 4:
                    break
                
                print("Enter a number between 0 and 4 !")
    
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
            print("**** Bedrooms Menu ****\n"
                  "(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) Print all\n"
                  "(0) Go back")
    
            userInput = 0
            while(True):
                userInput = int(input("Enter number:"))
    
                if userInput >= 0 and userInput <= 4:
                    break
                
                print("Enter a number between 0 and 4 !")

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
            print("**** Reservations Menu ****\n"
                  "(1) Add\n"
                  "(2) Update\n"
                  "(3) Remove\n"
                  "(4) List all\n"
                  "(0) Go back")
    
            userInput = 0
            while(True):
                userInput = int(input("Enter number:"))
    
                if userInput >= 0 and userInput <= 3:
                    break
                
                print("Enter a number between 0 and 3 !")