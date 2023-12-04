import Classes.clients as Clients
import re

class ClientsMenu:
    def AddClient():
        client = ClientsMenu.CreateClientInstance()
        if client == None:
            return

        Clients.Client.add(client)
        print("Client created.")

    def RemoveClient():
        id = input("Id: ")

        Clients.Client.remove(id=id)
        print("Client removed.")

    def UpdateClient():
        id = input("Id: ")
        updatedClient = ClientsMenu.CreateClientInstance()
        updatedClient.id = id

        Clients.Client.update(id, updatedClient)
        print("Client updated.")

    def PrintAll():
        clients = Clients.Client.getAll()
        print(clients)


    def CreateClientInstance() -> Clients.Client:
        namesRegex = re.compile(r'^[a-zA-Z]+$')

        lastname = input("Lastname: ")
        if not namesRegex.match(lastname):
            print("Incorrect Lastname!")
            return None

        firstname = input("Firstname: ")
        if not namesRegex.match(firstname):
            print("Incorrect Firstname!")
            return None

        birthday = input("Birthday (dd/mm/yyyy): ")
        birthdayRegex = re.compile(r'^\d{2}/\d{2}/\d{4}$')
        if not birthdayRegex.match(birthday):
            print("Incorrect birthday date!")
            return None

        date = birthday.split("/")
        if not int(date[0]) > 0 or not int(date[0]) < 32:
            print("Incorrect birthday date!")
            return None
        if not int(date[1]) > 0 or not int(date[1]) < 13:
            print("Incorrect birthday date!")
            return None
        if not int(date[2]) > 0 or not int(date[2]) < 9999:
            print("Incorrect birthday date!")
            return None

        phoneNumber = input("Phone number: ")
        phoneNumberRegex = re.compile(r'[0-9]{10}')
        if not phoneNumberRegex.match(phoneNumber):
            print("Incorrect phone number!")
            return None

        return Clients.Client(lastname, firstname, birthday, phoneNumber)