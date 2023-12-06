import uuid
import Utils.Json as Json

class Bedroom:
    def __init__(self, type, price) -> None:
        self.id = str(uuid.uuid4())
        self.type = type
        self.price = int(price)
        

    def add(bedroom):
        data = Json.JSON.openJson("bedrooms.json")

        bedroomJson = {
            'id': bedroom.id,
            'type': bedroom.type,
            'price': int(bedroom.price)
        }
        
        data.append(bedroomJson)

        Json.JSON.saveJson("bedrooms.json", data)


    def remove(id):
        bedrooms = Json.JSON.openJson("bedrooms.json")

        for bedroom in bedrooms:
            if bedroom['id'] == id:
                bedrooms.remove(bedroom)
                break
            
        Json.JSON.saveJson("bedrooms.json", bedrooms)

        reservations = Json.JSON.openJson("reservations.json")

        for reservation in reservations:
            if reservation['bedroomId'] == id:
                reservations.remove(reservation)

        Json.JSON.saveJson("reservations.json", reservations)


    def update(id, newBedroom):
        Bedroom.remove(id)

        bedroom = {
            'id': id,
            'type': newBedroom.type,
            'price': int(newBedroom.price)
        }

        data = Json.JSON.openJson("bedrooms.json")
        data.append(bedroom)

        Json.JSON.saveJson("bedrooms.json", data)


    def getAll() -> []:
        return Json.JSON.openJson("bedrooms.json")
