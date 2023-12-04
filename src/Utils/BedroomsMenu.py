import Classes.bedrooms as Bedrooms
import re

class BedroomsMenu:
    def AddBedroom():
        Bedroom = BedroomsMenu.CreateBedroomInstance()
        if Bedroom == None:
            return

        Bedrooms.Bedroom.add(Bedroom)
        print("Bedroom created.")

    def RemoveBedroom():
        id = input("Id: ")

        Bedrooms.Bedroom.remove(id=id)
        print("Bedroom removed.")

    def UpdateBedroom():
        id = input("Id: ")
        updatedBedroom = BedroomsMenu.CreateBedroomInstance()
        if updatedBedroom == None:
            return

        updatedBedroom.id = id

        Bedrooms.Bedroom.update(id, updatedBedroom)
        print("Bedroom updated.")

    def PrintAll():
        bedrooms = Bedrooms.Bedroom.getAll()
        print(bedrooms)


    def CreateBedroomInstance() -> Bedrooms.Bedroom:
        type = input("Type (simple / double / suite): ")
        if type not in ["simple", "double", "suite"]:
            print("Incorrect Type!")
            return None

        price = input("Price: ")
        priceRegex = re.compile(r'^\d+$')
        if not priceRegex.match(price):
            print("Incorrect Price!")
            return None

        return Bedrooms.Bedroom(type, price)