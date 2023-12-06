import Classes.Reservations as Reservations
from Menus import ClientsMenu, BedroomsMenu
import Utils.Colors as Colors
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


    def CreateReservationInstance() -> Reservations.Reservation:
        dateRegex = re.compile(r'^\d{2}/\d{2}/\d{4}$')

        dateStart = input("Date start (dd/mm/yyyy): ")
        if not dateRegex.match(dateStart) or not ReservationsMenu.verifyDate(dateStart):
            print(Colors.Colors.red("Incorrect date end!"))
            return None
        
        dateStartSplitted = dateStart.split("/")
        dtStart = dt.datetime(int(dateStartSplitted[2]), int(dateStartSplitted[1]), int(dateStartSplitted[0]))
        
        dateEnd = input("Date end (dd/mm/yyyy): ")
        if not dateRegex.match(dateEnd) or not ReservationsMenu.verifyDate(dateEnd):
            print(Colors.Colors.red("Incorrect date end!"))
            return None
        
        dateEndSplitted = dateEnd.split("/")
        dtEnd = dt.datetime(int(dateEndSplitted[2]), int(dateEndSplitted[1]), int(dateEndSplitted[0]))
        
        paymentMethod = input("Payment method (Carte / Paypal / Espece): ")
        if paymentMethod not in ["Carte", "Paypal", "Espece"]:
            print(Colors.Colors.red("Incorrect payment  method!"))
            return None
        
        print("Which client: ")
        clientId = ClientsMenu.ClientsMenu.ListChoice()

        print("Which room: ")
        bedroomId = BedroomsMenu.BedroomsMenu.ListChoice()

        return Reservations.Reservation(dtStart, dtEnd, paymentMethod, clientId, bedroomId)
    

    def verifyDate(date) -> bool:
        dateStartSplited = date.split("/")

        if not int(dateStartSplited[0]) > 0 or not int(dateStartSplited[0]) < 32:
            return False
        
        if not int(dateStartSplited[1]) > 0 or not int(dateStartSplited[1]) < 13:
            return False
        
        if not int(dateStartSplited[2]) > 0 or not int(dateStartSplited[2]) < 9999:
            return False
        
        return True


    def ListChoice():
        reservations = Reservations.Reservation.getAll()
        if len(reservations) < 1:
            print(Colors.Colors.yellow("There is no Reservations."))
            return None

        for i, reservation in enumerate(reservations):
            print("("+str(i+1)+") "+str(reservation['dateStart'])+", "+str(reservation['dateEnd'])+", "+reservation['payment'])
        
        print("(0) Go back")

        while(True):
            userInput = int(input("Id: "))

            if userInput >= 0 and userInput <= len(reservations):
                break

            print(Colors.Colors.cyan("Enter a number between 0 and "+str(len(reservations))+" !"))

        if userInput == 0:
            return None

        return str(reservations[userInput-1]['id'])