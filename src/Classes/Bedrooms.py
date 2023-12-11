import uuid
from Utils.Json import JSON

class Bedroom:
    global filePath
    filePath = "bedrooms.json"
    def __init__(self, type :str, price :int) -> None:
        self.id = str(uuid.uuid4())
        self.type = type
        self.price = int(price)
        

    def add(self):
        data = JSON.openJson(filePath)

        bedroomJson = {
            'id': self.id,
            'type': self.type,
            'price': int(self.price)
        }
        
        data.append(bedroomJson)

        JSON.saveJson(filePath, data)


    def remove(self):
        bedrooms = JSON.openJson(filePath)

        for bedroom in bedrooms:
            if bedroom['id'] == self.id:
                bedrooms.remove(bedroom)
                break
            
        JSON.saveJson(filePath, bedrooms)

        reservations = JSON.openJson("reservations.json")

        for reservation in reservations:
            if reservation['bedroomId'] == self.id:
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
        for bedroom in JSON.openJson(filePath):
            if bedroom['id'] == id:
                break

        reBedroom = Bedroom(bedroom['type'], bedroom['price'])
        reBedroom.id == id

        return reBedroom