import Classes.Clients as Clients
import Utils.Colors as Colors
import re

class ClientsMenu:
    def AddClient():
        client = ClientsMenu.CreateClientInstance()
        if client == None:
            return

        Clients.Client.add(client)
        print(Colors.Colors.green("Client created."))


    def RemoveClient():
        id = input("Id: ")

        Clients.Client.remove(id=id)
        print(Colors.Colors.green("Client removed."))


    def UpdateClient():
        id = ClientsMenu.ListChoice()

        if id == None:
            return
        
        updatedClient = ClientsMenu.CreateClientInstance()
        if updatedClient == None:
            return

        updatedClient.id = id

        Clients.Client.update(id, updatedClient)
        print(Colors.Colors.green("Client updated."))


    def PrintAll():
        clients = Clients.Client.getAll()

        if clients == []:
            print(Colors.Colors.yellow("There is no clients."))
        else:
            print("\nList of clients: ")
            for client in clients:
                print(client['lastname']+", "+client['firstname']+", "+client['phoneNumber'])


    def CreateClientInstance() -> Clients.Client:
        namesRegex = re.compile(r'^[a-zA-Z]+$')

        lastname = input("Lastname: ")
        if not namesRegex.match(lastname):
            print(Colors.Colors.red("Incorrect Lastname!"))
            return None

        firstname = input("Firstname: ")
        if not namesRegex.match(firstname):
            print(Colors.Colors.red("Incorrect Firstname!"))
            return None

        birthday = input("Birthday (dd/mm/yyyy): ")
        birthdayRegex = re.compile(r'^\d{2}/\d{2}/\d{4}$')
        if not birthdayRegex.match(birthday):
            print(Colors.Colors.red("Incorrect birthday date!"))
            return None

        date = birthday.split("/")
        if not int(date[0]) > 0 or not int(date[0]) < 32:
            print(Colors.Colors.red("Incorrect birthday date!"))
            return None
        if not int(date[1]) > 0 or not int(date[1]) < 13:
            print(Colors.Colors.red("Incorrect birthday date!"))
            return None
        if not int(date[2]) > 0 or not int(date[2]) < 9999:
            print(Colors.Colors.red("Incorrect birthday date!"))
            return None

        phoneNumber = input("Phone number: ")
        phoneNumberRegex = re.compile(r'[0-9]{10}')
        if not phoneNumberRegex.match(phoneNumber):
            print(Colors.Colors.red("Incorrect phone number!"))
            return None

        return Clients.Client(lastname, firstname, birthday, phoneNumber)
    
    
    def ListChoice():
        clients = Clients.Client.getAll()
        if len(clients) < 1:
            print(Colors.Colors.yellow("There is no clients."))
            return None

        for i, client in enumerate(clients):
            print("("+str(i+1)+") "+client['lastname']+", "+client['firstname']+", "+client['phoneNumber'])
        
        print("(0) Go back")

        while(True):
            userInput = int(input("Id: "))

            if userInput >= 0 and userInput <= len(clients):
                break

            print(Colors.Colors.cyan("Enter a number between 0 and "+str(len(clients))+" !"))

        if userInput == 0:
            return None

        return str(clients[userInput-1]['id'])