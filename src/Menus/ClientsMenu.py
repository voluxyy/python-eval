from Classes.Clients import Client
from Utils.Colors import Colors
import re

class ClientsMenu:
    def AddClient():
        client = ClientsMenu.CreateClientInstance()
        if client == None:
            return

        Client.add(client)
        print(Colors.green("Client created."))


    def RemoveClient():
        id = ClientsMenu.ListChoice()
        if id == None:
            return

        Client.remove(id=id)
        print(Colors.green("Client removed."))


    def UpdateClient():
        id = ClientsMenu.ListChoice()
        if id == None:
            return
        
        updatedClient = ClientsMenu.CreateClientInstance()
        if updatedClient == None:
            return

        updatedClient.id = id

        Client.update(id, updatedClient)
        print(Colors.green("Client updated."))


    def PrintAll():
        clients = Client.getAll()

        if clients == []:
            print(Colors.yellow("There is no clients."))
        else:
            print("\nList of clients: ")
            for client in clients:
                print(f"{client['lastname']}, {client['firstname']}, {client['phoneNumber']}")


    def CreateClientInstance() -> Client:
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
        clients = Client.getAll()
        if len(clients) < 1:
            print(Colors.yellow("There is no clients."))
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