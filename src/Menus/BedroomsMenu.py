from Classes.Bedrooms import Bedroom
from Utils.Colors import Colors
from Utils.Clear import Clear
import re
import time

class BedroomsMenu:
    def AddBedroom():
        bedroom = BedroomsMenu.CreateBedroomInstance()
        if bedroom == None:
            time.sleep(3)
            return

        bedroom.add()
        print(Colors.green("Bedroom created."))
        time.sleep(1)


    def RemoveBedroom():
        bedroom = BedroomsMenu.ListChoice()
        if bedroom == None:
            return

        bedroom.remove()
        print(Colors.green("Bedroom removed."))
        time.sleep(1)


    def UpdateBedroom():
        bedroom = BedroomsMenu.ListChoice()
        if bedroom == None:
            return

        updatedBedroom = BedroomsMenu.CreateBedroomInstance()
        if updatedBedroom == None:
            time.sleep(3)
            return

        updatedBedroom.id = bedroom.id

        updatedBedroom.update()
        print(Colors.green("Bedroom updated."))
        time.sleep(1)


    def PrintAll():
        bedrooms = Bedroom.getAll()
        if bedrooms == []: 
            print(Colors.yellow("There is no bedrooms."))
            time.sleep(1)
        else: 
            print("\nList of bedrooms: ")
            for bedroom in bedrooms:
                print(f"{bedroom['type']}, {str(bedroom['price'])}")

            Clear.askToExit()


    def CreateBedroomInstance() -> Bedroom:
        Clear.ClearTerminal()
        print(Colors.blue("**** Bedroom Instance ****"))

        type = input("Type (simple / double / suite): ")
        if type not in ["simple", "double", "suite"]:
            print(Colors.red("Incorrect Type!"))
            return None

        price = input("Price: ")
        if price == "" or not price.isdigit():
            print(Colors.red("Incorrect Price!"))
            return None
        
        priceRegex = re.compile(r'^\d+$')
        if not priceRegex.match(price):
            print(Colors.red("Incorrect Price!"))
            return None

        return Bedroom(type, price)
    

    def ListChoice():
        Clear.ClearTerminal()
        print(Colors.blue("**** Bedrooms List ****"))

        bedrooms = Bedroom.getAll()
        if len(bedrooms) < 1:
            print(Colors.yellow("There is no bedrooms."))
            time.sleep(1)
            return None

        for i, bedroom in enumerate(bedrooms):
            print(f"({str(i+1)}) {bedroom['type']}, {str(bedroom['price'])}")
        
        print("(0) Go back")

        while(True):
            while(True):
                userInput = input(Colors.magenta("Id: "))

                if userInput.isdigit():
                    break

                print(Colors.red("You can only enter integer to choose!"))

            userInput = int(userInput)

            if userInput >= 0 and userInput <= len(bedrooms):
                break

            print(Colors.cyan(f"Enter a number between 0 and {str(len(bedrooms))} !"))

        if userInput == 0:
            return None
        
        selected = bedrooms[userInput-1]
        bedroom = Bedroom(selected['type'], selected['price'])
        bedroom.id = selected['id']

        return bedroom