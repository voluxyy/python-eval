import uuid
from Utils.Json import JSON

class Client:
    global filePath 
    filePath = "clients.json"

    def __init__(self, lastname, firstname, birthday, phoneNumber) -> None:
        self.id = str(uuid.uuid4())
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.phoneNumber = phoneNumber
        

    def add(client):
        data = JSON.openJson(filePath)

        clientJson = {
            'id': client.id,
            'lastname': client.lastname,
            'firstname': client.firstname,
            'birthday': str(client.birthday),
            'phoneNumber': client.phoneNumber
        }
        
        data.append(clientJson)

        JSON.saveJson(filePath, data)


    def remove(id):
        clients = JSON.openJson(filePath)

        for client in clients:
            if client['id'] == id:
                clients.remove(client)
                break

        JSON.saveJson(filePath, clients)

        reservations = JSON.openJson("reservations.json")

        for reservation in reservations:
            if reservation['clientId'] == id:
                reservations.remove(reservation)

        JSON.saveJson("reservations.json", reservations)


    def update(id, newClient):
        Client.remove(id)

        client = {
            'id': id,
            'lastname': newClient.lastname,
            'firstname': newClient.firstname,
            'birthday': str(newClient.birthday),
            'phoneNumber': newClient.phoneNumber
        }

        data = JSON.openJson(filePath)
        data.append(client)

        JSON.saveJson(filePath, data)


    def getAll() -> []:
        return JSON.openJson(filePath)
