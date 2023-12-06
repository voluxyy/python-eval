import Classes.Reservations as Reservations
from Menus import ClientsMenu, BedroomsMenu
import Utils.Colors as Colors
import Utils.Json as Json
import datetime as dt
import re

class ReservationsMenu:
    def AddReservation():
        reservation = ReservationsMenu.CreateReservationInstance()
        if reservation == None:
            return

        Reservations.Reservation.add(reservation)
        print(Colors.Colors.green("Reservation created."))


    def RemoveReservation():
        id = ReservationsMenu.ListChoice()
        if id == None:
            return

        Reservations.Reservation.remove(id=id)
        print(Colors.Colors.green("Reservation removed."))


    def UpdateReservation():
        id = ReservationsMenu.ListChoice()

        if id == None:
            return
        
        updatedReservation = ReservationsMenu.CreateReservationInstance()
        if updatedReservation == None:
            return

        updatedReservation.id = id

        Reservations.Reservation.update(id, updatedReservation)
        print(Colors.Colors.green("Reservation updated."))


    def PrintAll():
        reservations = Reservations.Reservation.getAll()

        if reservations == []:
            print(Colors.Colors.yellow("There is no Reservations."))
        else:
            print("\nList of Reservations: ")
            for reservation in reservations:
                print(str(reservation['dateStart'])+", "+str(reservation['dateEnd'])+", "+reservation['payment'])


    def ExportToCsv():
        dateRegex = re.compile(r'^\d{2}/\d{2}/\d{4}$')

        inputStartDate = input("Date start (dd/mm/yyyy): ")
        if not dateRegex.match(inputStartDate) or not ReservationsMenu.verifyDateFormat(inputStartDate):
            print(Colors.Colors.red("Incorrect date start!"))
            return None
        
        inputEndDate = input("Date end (dd/mm/yyyy): ")
        if not dateRegex.match(inputEndDate) or not ReservationsMenu.verifyDateFormat(inputEndDate):
            print(Colors.Colors.red("Incorrect date end!"))
            return None

        dtStart = dt.datetime.strptime(inputStartDate, '%d/%m/%Y')
        dtEnd = dt.datetime.strptime(inputEndDate, '%d/%m/%Y')

        if dtStart >= dtEnd:
            print(Colors.Colors.red("Start date cannot be after or the same as end date!"))
            return None
        
        filteredReservations = Reservations.Reservation.getAvailableBedRooms(dtStart, dtEnd)

        if not filteredReservations:
            print(Colors.Colors.yellow("Aucune réservation pour la période spécifiée."))
            return None
        
        dateStartOnly = str(dtStart.isoformat().split("T")[0])
        dateEndOnly = str(dtEnd.isoformat().split("T")[0])
        csv_filename = f"reservations_{dateStartOnly}_{dateEndOnly}.csv"

        Json.JSON.exportCsv(csv_filename, filteredReservations)

        print(Colors.Colors.green(f"Reservations from {inputStartDate} to {inputEndDate} has been exported in {csv_filename}."))


    def CreateReservationInstance() -> Reservations.Reservation:
        print("Which client: ")
        clientId = ClientsMenu.ClientsMenu.ListChoice()
        if clientId == None:
            return

        print("Which room: ")
        bedroomId = BedroomsMenu.BedroomsMenu.ListChoice()
        if bedroomId == None:
            return

        dateRegex = re.compile(r'^\d{2}/\d{2}/\d{4}$')

        dateStart = input("Date start (dd/mm/yyyy): ")
        if not dateRegex.match(dateStart) or not ReservationsMenu.verifyDateFormat(dateStart):
            print(Colors.Colors.red("Incorrect date end!"))
            return None
        
        # Todo: add condition if there is already a reservation on this date
        
        dateStartSplitted = dateStart.split("/")
        dtStart = dt.datetime(int(dateStartSplitted[2]), int(dateStartSplitted[1]), int(dateStartSplitted[0]))
        
        dateEnd = input("Date end (dd/mm/yyyy): ")
        if not dateRegex.match(dateEnd) or not ReservationsMenu.verifyDateFormat(dateEnd):
            print(Colors.Colors.red("Incorrect date end!"))
            return None
        
        dateEndSplitted = dateEnd.split("/")
        dtEnd = dt.datetime(int(dateEndSplitted[2]), int(dateEndSplitted[1]), int(dateEndSplitted[0]))
        
        paymentMethod = input("Payment method (Carte / Paypal / Espece): ")
        if paymentMethod not in ["Carte", "Paypal", "Espece"]:
            print(Colors.Colors.red("Incorrect payment  method!"))
            return None

        return Reservations.Reservation(dtStart, dtEnd, paymentMethod, clientId, bedroomId)
    

    def verifyDateFormat(date) -> bool:
        dateStartSplited = date.split("/")

        if not int(dateStartSplited[0]) > 0 or not int(dateStartSplited[0]) < 32:
            return False
        
        if not int(dateStartSplited[1]) > 0 or not int(dateStartSplited[1]) < 13:
            return False
        
        if not int(dateStartSplited[2]) > 0 or not int(dateStartSplited[2]) < 9999:
            return False
        
        return True


    def verifyDate() -> bool:
        return False

    def ListChoice():
        reservations = Reservations.Reservation.getAll()
        if len(reservations) < 1:
            print(Colors.Colors.yellow("There is no Reservations."))
            return None

        for i, reservation in enumerate(reservations):
            print(f"({str(i+1)}) {str(reservation['dateStart'])}, {str(reservation['dateEnd'])}, {reservation['payment']}")
        
        print("(0) Go back")

        while(True):
            userInput = int(input("Id: "))

            if userInput >= 0 and userInput <= len(reservations):
                break

            print(Colors.Colors.cyan(f"Enter a number between 0 and {str(len(reservations))} !"))

        if userInput == 0:
            return None

        return str(reservations[userInput-1]['id'])