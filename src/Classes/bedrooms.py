import uuid
import Utils.Json as Json

class Bedroom:
    def __init__(self, type, price) -> None:
        self.id = str(uuid.uuid4())
        self.type = type
        self.price = int(price)
        

    def add(bedroom):
        data = Json.JSON.open_clients_json("bedrooms.json")

        bedroomJson = {
            'id': bedroom.id,
            'type': bedroom.type,
            'price': int(bedroom.price)
        }
        
        data.append(bedroomJson)

        Json.JSON.save_clients_to_json("bedrooms.json", data)


    def remove(id):
        data = Json.JSON.open_clients_json("bedrooms.json")

        for bedroom in data:
            if bedroom['id'] == id:
                data.remove(bedroom)
                break

        Json.JSON.save_clients_to_json("bedrooms.json", data)


    def update(id, new_bedroom):
        Bedroom.remove(id)

        bedroom = {
            'id': id,
            'type': new_bedroom.type,
            'price': int(new_bedroom.price)
        }

        data = Json.JSON.open_clients_json("bedrooms.json")
        data.append(bedroom)

        Json.JSON.save_clients_to_json("bedrooms.json", data)


    def getAll() -> []:
        return Json.JSON.open_clients_json("bedrooms.json")
