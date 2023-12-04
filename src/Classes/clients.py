import uuid
import os
import json
import Utils.Json as Json

class Client:
    def __init__(self, lastname, firstname, birthday, phoneNumber) -> None:
        self.id = str(uuid.uuid4())
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.phoneNumber = phoneNumber
        

    def add(client):
        data = Json.JSON.open_clients_json()

        clientJson = {
            'id': client.id,
            'lastname': client.lastname,
            'firstname': client.firstname,
            'birthday': str(client.birthday),
            'phoneNumber': client.phoneNumber
        }
        
        data.append(clientJson)

        Json.JSON.save_clients_to_json(data)


    def remove(id):
        data = Json.JSON.open_clients_json()

        for client in data:
            if client['id'] == id:
                data.remove(client)
                break

        Json.JSON.save_clients_to_json(data)


    def update(id, new_client):
        Client.remove(id)

        client = {
            'id': id,
            'lastname': new_client.lastname,
            'firstname': new_client.firstname,
            'birthday': str(new_client.birthday),
            'phoneNumber': new_client.phoneNumber
        }

        data = Json.JSON.open_clients_json()
        data.append(client)

        Json.JSON.save_clients_to_json(data)


    def getAll() -> []:
        return Json.JSON.open_clients_json()
