from Classes.Reservations import Reservation
from Menus.ClientsMenu import ClientsMenu
from Menus.BedroomsMenu import BedroomsMenu
from Utils.Colors import Colors
from Utils.Clear import Clear
from Utils.Json import JSON
from datetime import datetime as dt
import re
import time

class ReservationsMenu:
    def AddReservation():
        reservation = ReservationsMenu.CreateReservationInstance()
        if reservation == None:
            time.sleep(3)
            return

        Reservation.add(reservation)
        print(Colors.green("Reservation created."))
        time.sleep(1)


    def RemoveReservation():
        id = ReservationsMenu.ListChoice()
        if id == None:
            return

        Reservation.remove(id=id)
        print(Colors.green("Reservation removed."))
        time.sleep(1)


    def UpdateReservation():
        id = ReservationsMenu.ListChoice()
        if id == None:
            return
        
        updatedReservation = ReservationsMenu.CreateReservationInstance()
        if updatedReservation == None:
            time.sleep(3)
            return

        updatedReservation.id = id

        Reservation.update(id, updatedReservation)
        print(Colors.green("Reservation updated."))
        time.sleep(1)


    def PrintAll():
        reservations = Reservation.getAll()

        if reservations == []:
            print(Colors.yellow("There is no Reservations."))
            time.sleep(1)
        else:
            print("\nList of Reservations: ")
            for reservation in reservations:
                print(str(reservation['dateStart'])+", "+str(reservation['dateEnd'])+", "+reservation['payment'])

            time.sleep(5)


    def ExportToCsv():
        Clear.ClearTerminal()
        print(Colors.blue("**** Export To Csv ****"))

        dateRegex = re.compile(r'^\d{2}/\d{2}/\d{4}$')

        inputStartDate = input("Date start (dd/mm/yyyy): ")
        if inputStartDate == "" or not (dateRegex.match(inputStartDate) or ReservationsMenu.verifyDateFormat(inputStartDate)):
            print(Colors.red("Incorrect date start!"))
            return None
        
        inputEndDate = input("Date end (dd/mm/yyyy): ")
        if inputEndDate == "" or not (dateRegex.match(inputEndDate) or ReservationsMenu.verifyDateFormat(inputEndDate)):
            print(Colors.red("Incorrect date end!"))
            return None

        dtStart = dt.strptime(inputStartDate, '%d/%m/%Y')
        dtEnd = dt.strptime(inputEndDate, '%d/%m/%Y')

        if dtStart >= dtEnd:
            print(Colors.red("Start date cannot be after or the same as end date!"))
            return None
        
        filteredReservations = Reservation.getAvailableBedRooms(dtStart, dtEnd)

        if not filteredReservations:
            print(Colors.yellow("Aucune réservation pour la période spécifiée."))
            return None
        
        dateStartOnly = str(dtStart.isoformat().split("T")[0])
        dateEndOnly = str(dtEnd.isoformat().split("T")[0])
        csv_filename = f"reservations_{dateStartOnly}_{dateEndOnly}.csv"

        JSON.exportCsv(csv_filename, filteredReservations)

        print(Colors.green(f"Reservations from {inputStartDate} to {inputEndDate} has been exported in {csv_filename}."))


    def CreateReservationInstance() -> Reservation:
        Clear.ClearTerminal()
        print(Colors.blue("**** Reservation Instance ****"))

        print("Which client: ")
        clientId = ClientsMenu.ListChoice()
        if clientId == None:
            return

        print("Which room: ")
        bedroomId = BedroomsMenu.ListChoice()
        if bedroomId == None:
            return

        dateRegex = re.compile(r'^\d{2}/\d{2}/\d{4}$')

        dateStart = input("Date start (dd/mm/yyyy): ")
        if dateStart == '' or not (dateRegex.match(dateStart) or ReservationsMenu.verifyDateFormat(dateStart)):
            print(Colors.red("Incorrect date end!"))
            return None
        
        dateStartSplitted = dateStart.split("/")
        dtStart = dt(int(dateStartSplitted[2]), int(dateStartSplitted[1]), int(dateStartSplitted[0]))
        
        dateEnd = input("Date end (dd/mm/yyyy): ")
        if dateEnd == '' or not (dateRegex.match(dateEnd) or ReservationsMenu.verifyDateFormat(dateEnd)):
            print(Colors.red("Incorrect date end!"))
            return None
        
        dateEndSplitted = dateEnd.split("/")
        dtEnd = dt(int(dateEndSplitted[2]), int(dateEndSplitted[1]), int(dateEndSplitted[0]))

        for reservation in Reservation.getAll():
            if reservation['bedroomId'] == bedroomId:
                if reservation['dateStart'] <= dtStart and dtStart <= reservation['dateEnd']:
                    print(Colors.yellow("There is already a reservation for this bedroom at this moment."))
                    return None
        
        paymentMethod = input("Payment method (Carte / Paypal / Espece): ")
        if paymentMethod not in ["Carte", "Paypal", "Espece"]:
            print(Colors.red("Incorrect payment  method!"))
            return None

        return Reservation(dtStart, dtEnd, paymentMethod, clientId, bedroomId)
    

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
        Clear.ClearTerminal()
        print(Colors.blue("**** Reservations List ****"))

        reservations = Reservation.getAll()
        if len(reservations) < 1:
            print(Colors.yellow("There is no Reservations."))
            time.sleep(1)
            return None

        for i, reservation in enumerate(reservations):
            print(f"({str(i+1)}) {str(reservation['dateStart'])}, {str(reservation['dateEnd'])}, {reservation['payment']}")
        
        print("(0) Go back")

        while(True):
            while(True):
                userInput = input(Colors.magenta("Id: "))

                if userInput.isdigit():
                    break

                print(Colors.red("You can only enter integer to choose!"))

            userInput = int(userInput)

            if userInput >= 0 and userInput <= len(reservations):
                break

            print(Colors.cyan(f"Enter a number between 0 and {str(len(reservations))} !"))

        if userInput == 0:
            return None

        return str(reservations[userInput-1]['id'])