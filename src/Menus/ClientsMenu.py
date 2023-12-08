from Classes.Clients import Client
from Utils.Colors import Colors
from Utils.Clear import Clear
import re
import time

class ClientsMenu:
    def AddClient():
        client = ClientsMenu.CreateClientInstance()
        if client == None:
            time.sleep(3)
            return

        Client.add(client)
        print(Colors.green("Client created."))
        time.sleep(1)


    def RemoveClient():
        id = ClientsMenu.ListChoice()
        if id == None:
            return

        Client.remove(id=id)
        print(Colors.green("Client removed."))
        time.sleep(1)


    def UpdateClient():
        id = ClientsMenu.ListChoice()
        if id == None:
            return
        
        updatedClient = ClientsMenu.CreateClientInstance()
        if updatedClient == None:
            time.sleep(3)
            return

        updatedClient.id = id

        Client.update(id, updatedClient)
        print(Colors.green("Client updated."))
        time.sleep(1)


    def PrintAll():
        clients = Client.getAll()

        if clients == []:
            print(Colors.yellow("There is no clients."))
            time.sleep(1)
        else:
            print("\nList of clients: ")
            for client in clients:
                print(f"{client['lastname']}, {client['firstname']}, {client['phoneNumber']}")
        
            time.sleep(5)


    def CreateClientInstance() -> Client:
        Clear.ClearTerminal()
        print(Colors.blue("**** Client Instance ****"))

        namesRegex = re.compile(r'^[a-zA-Z]+$')

        lastname = input("Lastname: ")
        if not namesRegex.match(lastname):
            print(Colors.red("Incorrect Lastname!"))
            return None

        firstname = input("Firstname: ")
        if not namesRegex.match(firstname):
            print(Colors.red("Incorrect Firstname!"))
            return None

        birthday = input("Birthday (dd/mm/yyyy): ")
        birthdayRegex = re.compile(r'^\d{2}/\d{2}/\d{4}$')
        if not birthdayRegex.match(birthday):
            print(Colors.red("Incorrect birthday date!"))
            return None

        date = birthday.split("/")
        if not int(date[0]) > 0 or not int(date[0]) < 32:
            print(Colors.red("Incorrect birthday date!"))
            return None
        if not int(date[1]) > 0 or not int(date[1]) < 13:
            print(Colors.red("Incorrect birthday date!"))
            return None
        if not int(date[2]) > 0 or not int(date[2]) < 9999:
            print(Colors.red("Incorrect birthday date!"))
            return None

        phoneNumber = input("Phone number: ")
        phoneNumberRegex = re.compile(r'[0-9]{10}')
        if not phoneNumberRegex.match(phoneNumber):
            print(Colors.red("Incorrect phone number!"))
            return None

        return Client(lastname, firstname, birthday, phoneNumber)
    
    
    def ListChoice():
        Clear.ClearTerminal()
        print(Colors.blue("**** Clients List ****"))

        clients = Client.getAll()
        if len(clients) < 1:
            print(Colors.yellow("There is no clients."))
            time.sleep(1)
            return None

        for i, client in enumerate(clients):
            print(f"({str(i+1)}) {client['lastname']}, {client['firstname']}, {client['phoneNumber']}")
        
        print("(0) Go back")

        while(True):
            while(True):
                userInput = input(Colors.magenta("Id: "))

                if userInput.isdigit():
                    break

                print(Colors.red("You can only enter integer to choose!"))

            userInput = int(userInput)

            if userInput >= 0 and userInput <= len(clients):
                break

            print(Colors.cyan(f"Enter a number between 0 and {str(len(clients))} !"))

        if userInput == 0:
            return None

        return str(clients[userInput-1]['id'])