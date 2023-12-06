import Classes.Bedrooms as Bedrooms
import Utils.Colors as Colors
import re

class BedroomsMenu:
    def AddBedroom():
        Bedroom = BedroomsMenu.CreateBedroomInstance()
        if Bedroom == None:
            return

        Bedrooms.Bedroom.add(Bedroom)
        print(Colors.Colors.green("Bedroom created."))


    def RemoveBedroom():
        id = BedroomsMenu.ListChoice()
        if id == None:
            return

        Bedrooms.Bedroom.remove(id=id)
        print(Colors.Colors.green("Bedroom removed."))


    def UpdateBedroom():
        id = BedroomsMenu.ListChoice()
        if id == None:
            return

        updatedClient = BedroomsMenu.CreateBedroomInstance()
        if updatedClient == None:
            return

        updatedClient.id = id

        Bedrooms.Bedroom.update(id, updatedClient)
        print(Colors.Colors.green("Bedroom updated."))


    def PrintAll():
        bedrooms = Bedrooms.Bedroom.getAll()
        if bedrooms == []: 
            print(Colors.Colors.yellow("There is no bedrooms.")) 
        else: 
            print("\nList of bedrooms: ")
            for bedroom in bedrooms:
                print(f"{bedroom['type']}, {str(bedroom['price'])}")


    def CreateBedroomInstance() -> Bedrooms.Bedroom:
        type = input("Type (simple / double / suite): ")
        if type not in ["simple", "double", "suite"]:
            print(Colors.Colors.red("Incorrect Type!"))
            return None

        price = input("Price: ")
        priceRegex = re.compile(r'^\d+$')
        if not priceRegex.match(price):
            print(Colors.Colors.red("Incorrect Price!"))
            return None

        return Bedrooms.Bedroom(type, price)
    

    def ListChoice():
        bedrooms = Bedrooms.Bedroom.getAll()
        if len(bedrooms) < 1:
            print(Colors.Colors.yellow("There is no bedrooms."))
            return None

        for i, bedroom in enumerate(bedrooms):
            print(f"({str(i+1)}) {bedroom['type']}, {str(bedroom['price'])}")
        
        print("(0) Go back")

        while(True):
            userInput = int(input("Id: "))

            if userInput >= 0 and userInput <= len(bedrooms):
                break

            print(Colors.Colors.cyan(f"Enter a number between 0 and {str(len(bedrooms))} !"))

        if userInput == 0:
            return None

        return str(bedrooms[userInput-1]['id'])