import uuid
import datetime as dt
import Utils.Json as Json

class Reservation:
    def __init__(self, dateStart, dateEnd, payment, clientId, bedroomId) -> None:
        self.id = str(uuid.uuid4())
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.payment = payment
        self.clientId = clientId
        self.bedroomId = bedroomId

    def add(reservation):
        data = Json.JSON.openJson("reservations.json")

        reservationJson = {
            'id': reservation.id,
            'dateStart': str(reservation.dateStart),
            'dateEnd': str(reservation.dateEnd),
            'payment': reservation.payment,
            'clientId': reservation.clientId,
            'bedroomId': reservation.bedroomId
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
            'id': newReservation.id,
            'dateStart': str(newReservation.dateStart),
            'dateEnd': str(newReservation.dateEnd),
            'payment': newReservation.payment,
            'clientId': newReservation.clientId,
            'bedroomId': newReservation.bedroomId
        }

        data = Json.JSON.openJson("reservations.json")
        data.append(reservation)

        Json.JSON.saveJson("reservations.json", data)


    def getAll() -> []:
        reservations = Json.JSON.openJson("reservations.json")
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
    

    def getReservationByBedroomId(id):
        reservations = Json.JSON.openJson("reservations.json")
        reservationsContainsId = []
        
        for reservation in reservations:
            if reservation['bedroomId'] == id:
                reservationsContainsId.append(reservation)

        return reservationsContainsId
        
    
    @staticmethod
    def getAvailableBedRooms(date1, date2):
        reservations = Reservation.getAll()

        date1 = dt.strptime(date1, '%Y-%m-%d')
        date2 = dt.strptime(date2, '%Y-%m-%d')

        available_rooms = []

        for reservation in reservations:
            dateStart = dt.strptime(reservation['dateStart'], '%Y-%m-%dT%H:%M:%S')
            dateEnd = dt.strptime(reservation['dateEnd'], '%Y-%m-%dT%H:%M:%S')

            if not (date2 < dateStart or date1 > dateEnd):
                break
            else:
                available_rooms.append(reservation)

        return available_rooms
