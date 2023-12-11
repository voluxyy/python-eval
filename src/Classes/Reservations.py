import uuid
import datetime as dt
from Utils.Json import JSON

class Reservation:
    global filePath
    filePath = "reservations.json"

    def __init__(self, dateStart, dateEnd, payment, clientId, bedroomId) -> None:
        self.id = str(uuid.uuid4())
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.payment = payment
        self.clientId = clientId
        self.bedroomId = bedroomId

    def add(self):
        data = JSON.openJson(filePath)

        reservationJson = {
            'id': self.id,
            'dateStart': str(self.dateStart),
            'dateEnd': str(self.dateEnd),
            'payment': self.payment,
            'clientId': self.clientId,
            'bedroomId': self.bedroomId
        }
        
        data.append(reservationJson)

        JSON.saveJson(filePath, data)


    def remove(self):
        data = JSON.openJson(filePath)

        for reservation in data:
            if reservation['id'] == self.id:
                data.remove(reservation)
                break

        JSON.saveJson(filePath, data)


    def update(self):
        self.remove()
        self.add()
        

    @staticmethod
    def getAll() -> []:
        reservations = JSON.openJson(filePath)
        if not reservations:
            reservations = []

        reservationsFormat = []

        for reservation in reservations:
            dateStartSplitted = reservation['dateStart'].split("-")
            dtStart = dt.datetime(int(dateStartSplitted[0]), int(dateStartSplitted[1]), int(dateStartSplitted[2].split(" ")[0]))

            dateEndSplitted = reservation['dateEnd'].split("-")
            dtEnd = dt.datetime(int(dateEndSplitted[0]), int(dateEndSplitted[1]), int(dateEndSplitted[2].split(" ")[0]))

            reservationsFormat.append({
                'id': reservation['id'],
                'dateStart': dtStart,
                'dateEnd': dtEnd,
                'payment': reservation['payment'],
                'clientId': reservation['clientId'],
                'bedroomId': reservation['bedroomId']
            })

        return reservationsFormat
    
    @staticmethod
    def getReservationByBedroomId(id):
        reservations = JSON.openJson(filePath)
        reservationsContainsId = []
        
        for reservation in reservations:
            if reservation['bedroomId'] == id:
                reservationsContainsId.append(reservation)

        return reservationsContainsId
        
    
    @staticmethod
    def getAvailableBedRooms(date1, date2) -> []:
        reservations = Reservation.getAll()

        available_rooms = []

        for reservation in reservations:
            if reservation['dateStart'] >= date1 and reservation['dateEnd'] <= date2:
                available_rooms.append(reservation)

        return available_rooms

    @staticmethod
    def getAllByClientId(clientId):
        reservations = Reservation.getAll()

        reservedByClientId = [reservation for reservation in reservations if reservation['clientId'] == clientId]

        return reservedByClientId