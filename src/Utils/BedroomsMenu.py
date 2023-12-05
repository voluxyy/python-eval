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
        id = BedroomsMenu.ListChoice()
        if id == None:
            return

        updatedClient = BedroomsMenu.CreateBedroomInstance()
        if updatedClient == None:
            return

        updatedClient.id = id

        Bedrooms.Bedroom.update(id, updatedClient)
        print("Client updated.")

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
    
    def ListChoice():
        bedrooms = Bedrooms.Bedroom.getAll()
        if len(bedrooms) < 1:
            print("There is no bedrooms.")
            return None

        for i, bedroom in enumerate(bedrooms):
            print("("+str(i+1)+") "+bedroom['lastname']+", "+bedroom['firstname']+", "+bedroom['phoneNumber'])
        
        print("(0) Go back")

        while(True):
            userInput = int(input("Id: "))

            if userInput >= 0 and userInput <= len(bedrooms):
                break

            print("Enter a number between 0 and "+str(len(bedrooms))+" !")

        if userInput == 0:
            return None

        return str(bedrooms[userInput-1]['id'])