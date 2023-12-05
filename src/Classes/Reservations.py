import uuid
import Utils.Json as Json

class Reservation:
    def __init__(self, dateStart, dateEnd, payment) -> None:
        self.id = str(uuid.uuid4())
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.payment = payment

    def add(reservation):
        data = Json.JSON.openJson("reservations.json")

        reservationJson = {
            'id': reservation.id,
            'dateStart': reservation.dateStart,
            'dateEnd': reservation.dateEnd,
            'payment': reservation.payment
        }
        
        data.append(reservationJson)

        Json.JSON.saveJson("reservations.json", data)


    def remove(id):
        data = Json.JSON.openJson("reservations.json")

        for reservation in data:
            if reservation['id'] == id:
                data.remove(reservation)
                break

        Json.JSON.saveJson("reservations.json", data)


    def update(id, newReservation):
        Reservation.remove(id)

        reservation = {
            'id': id,
            'dateStart': newReservation.dateStart,
            'dateEnd': newReservation.dateEnd,
            'payment': newReservation.payment
        }

        data = Json.JSON.openJson("reservations.json")
        data.append(reservation)

        Json.JSON.saveJson("reservations.json", data)


    def getAll() -> []:
        return Json.JSON.openJson("reservations.json")
    
    def getAvailableBedRooms():
        return
