import uuid
import Utils.Json as Json

class Client:
    def __init__(self, lastname, firstname, birthday, phoneNumber) -> None:
        self.id = str(uuid.uuid4())
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.phoneNumber = phoneNumber
        

    def add(client):
        data = Json.JSON.openJson("clients.json")

        clientJson = {
            'id': client.id,
            'lastname': client.lastname,
            'firstname': client.firstname,
            'birthday': str(client.birthday),
            'phoneNumber': client.phoneNumber
        }
        
        data.append(clientJson)

        Json.JSON.saveJson("clients.json", data)


    def remove(id):
        data = Json.JSON.openJson("clients.json")

        for client in data:
            if client['id'] == id:
                data.remove(client)
                break

        Json.JSON.saveJson("clients.json", data)


    def update(id, newClient):
        Client.remove(id)

        client = {
            'id': id,
            'lastname': newClient.lastname,
            'firstname': newClient.firstname,
            'birthday': str(newClient.birthday),
            'phoneNumber': newClient.phoneNumber
        }

        data = Json.JSON.openJson("clients.json")
        data.append(client)

        Json.JSON.saveJson("clients.json", data)


    def getAll() -> []:
        return Json.JSON.openJson("clients.json")
