from Classes.Bedrooms import Bedroom
from Utils.Colors import Colors
import re

class BedroomsMenu:
    def AddBedroom():
        bedroom = BedroomsMenu.CreateBedroomInstance()
        if bedroom == None:
            return

        Bedroom.add(bedroom)
        print(Colors.green("Bedroom created."))


    def RemoveBedroom():
        id = BedroomsMenu.ListChoice()
        if id == None:
            return

        Bedroom.remove(id=id)
        print(Colors.green("Bedroom removed."))


    def UpdateBedroom():
        id = BedroomsMenu.ListChoice()
        if id == None:
            return

        updatedClient = BedroomsMenu.CreateBedroomInstance()
        if updatedClient == None:
            return

        updatedClient.id = id

        Bedroom.update(id, updatedClient)
        print(Colors.green("Bedroom updated."))


    def PrintAll():
        bedrooms = Bedroom.getAll()
        if bedrooms == []: 
            print(Colors.yellow("There is no bedrooms.")) 
        else: 
            print("\nList of bedrooms: ")
            for bedroom in bedrooms:
                print(f"{bedroom['type']}, {str(bedroom['price'])}")


    def CreateBedroomInstance() -> Bedroom:
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
        bedrooms = Bedroom.getAll()
        if len(bedrooms) < 1:
            print(Colors.yellow("There is no bedrooms."))
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

        return str(bedrooms[userInput-1]['id'])