import Utils.ClientsMenu as ClientsMenu

def mainMenu():
    while(True):
        print("**** Main Menu ****\n"
              "(1) Manage Clients\n"
              "(2) Manage Rooms\n"
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
            clientsMenu()
        elif userInput == 2:
            roomsMenu()
        elif userInput == 3:
            reservationsMenu()

def clientsMenu():
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
        return
    elif userInput == 1:
        ClientsMenu.AddClient()
    elif userInput == 2:
        ClientsMenu.UpdateClient()
    elif userInput == 3:
        ClientsMenu.RemoveClient()
    elif userInput == 4:
        ClientsMenu


def roomsMenu():
    print("**** Rooms Menu ****\n"
          "(1) Add\n"
          "(2) Update\n"
          "(3) Remove\n"
          "(4) Print all\n"
          "(0) Go back")
    
    userInput = 0
    while(True):
        userInput = int(input("Enter number:"))

        if userInput >= 0 and userInput <= 3:
            break

        print("Enter a number between 0 and 3 !")


def reservationsMenu():
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