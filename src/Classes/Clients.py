import uuid
from Utils.Json import JSON

class Client:
    def __init__(self, lastname, firstname, birthday, phoneNumber) -> None:
        self.id = str(uuid.uuid4())
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.phoneNumber = phoneNumber
        

    def add(client):
        data = JSON.openJson("clients.json")

        clientJson = {
            'id': client.id,
            'lastname': client.lastname,
            'firstname': client.firstname,
            'birthday': str(client.birthday),
            'phoneNumber': client.phoneNumber
        }
        
        data.append(clientJson)

        JSON.saveJson("clients.json", data)


    def remove(id):
        clients = JSON.openJson("clients.json")

        for client in clients:
            if client['id'] == id:
                clients.remove(client)
                break

        JSON.saveJson("clients.json", clients)

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

        data = JSON.openJson("clients.json")
        data.append(client)

        JSON.saveJson("clients.json", data)


    def getAll() -> []:
        return JSON.openJson("clients.json")
