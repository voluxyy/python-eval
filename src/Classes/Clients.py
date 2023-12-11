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
        self.points = 0


    def add(self):
        data = JSON.openJson(filePath)

        clientJson = {
            'id': self.id,
            'lastname': self.lastname,
            'firstname': self.firstname,
            'birthday': str(self.birthday),
            'phoneNumber': self.phoneNumber,
            'points': self.points
        }
        
        data.append(clientJson)

        JSON.saveJson(filePath, data)


    def remove(self):
        clients = JSON.openJson(filePath)

        for client in clients:
            if client['id'] == self.id:
                clients.remove(client)
                break

        JSON.saveJson(filePath, clients)

        reservations = JSON.openJson("reservations.json")

        for reservation in reservations:
            if reservation['clientId'] == self.id:
                reservations.remove(reservation)

        JSON.saveJson("reservations.json", reservations)


    def update(self):
        self.remove()
        self.add()


    @staticmethod
    def getAll() -> []:
        return JSON.openJson(filePath)
    
    
    @staticmethod
    def getById(id):
        for client in JSON.openJson(filePath):
            if client['id'] == id:
                break

        reClient = Client(client['lastname'], client['firstname'], client['birthday'], client['phoneNumber'])
        reClient.id = client['id']
        reClient.points = client['points']

        return reClient


    def addFidelityPoints(self, points):
        self.points += int(points)
        return self
    
    
    def removeFidelityPoints(self):
        self.points = 0
        return self