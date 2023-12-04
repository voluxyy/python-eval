import Classes.clients as Clients

def AddClient():
    Clients.Client.add(CreateClientInstance())

def RemoveClient():
    id = input("Id: ")

    Clients.Client.remove(id=id)

def UpdateClient():
    id = input("Id: ")
    updatedClient = CreateClientInstance()
    updatedClient.id = id

    Clients.Client.update(id, updatedClient)

def PrintAll():
    clients = Clients.Client.getAll()
    print(clients)


def CreateClientInstance() -> Clients.Client:
    lastname = input("Lastname: ")
    firstname = input("Firstname: ")
    birthday = input("Birthday (dd/mm/yyyy): ")
    phoneNumber = input("Phone number: ")

    return Clients.Client(lastname, firstname, birthday, phoneNumber)