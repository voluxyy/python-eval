import uuid
from Utils.Json import JSON

class Bedroom:
    def __init__(self, type, price) -> None:
        self.id = str(uuid.uuid4())
        self.type = type
        self.price = int(price)
        

    def add(bedroom):
        data = JSON.openJson("bedrooms.json")

        bedroomJson = {
            'id': bedroom.id,
            'type': bedroom.type,
            'price': int(bedroom.price)
        }
        
        data.append(bedroomJson)

        JSON.saveJson("bedrooms.json", data)


    def remove(id):
        bedrooms = JSON.openJson("bedrooms.json")

        for bedroom in bedrooms:
            if bedroom['id'] == id:
                bedrooms.remove(bedroom)
                break
            
        JSON.saveJson("bedrooms.json", bedrooms)

        reservations = JSON.openJson("reservations.json")

        for reservation in reservations:
            if reservation['bedroomId'] == id:
                reservations.remove(reservation)

        JSON.saveJson("reservations.json", reservations)


    def update(id, newBedroom):
        Bedroom.remove(id)

        bedroom = {
            'id': id,
            'type': newBedroom.type,
            'price': int(newBedroom.price)
        }

        data = JSON.openJson("bedrooms.json")
        data.append(bedroom)

        JSON.saveJson("bedrooms.json", data)


    def getAll() -> []:
        return JSON.openJson("bedrooms.json")
