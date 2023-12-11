import json
import csv
from Utils.Colors import Colors

class JSON:
    def saveJson(file_path, data):
        try:
            with open(file_path, "+w") as f:
                json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)
        except Exception as error:
            print(Colors.red(f"An error has been encountered while trying to save in json file. This is the error: {error.args[1]}"))


    def openJson(file_path) -> []:
        try:
            with open(file_path, '+r') as f:
                existing_data = json.load(f)
        except Exception as error:
            print(Colors.red(f"An error has been encountered while trying to open json file. This is the error: {error.args[1]}"))
            existing_data = []

        if file_path == "reservations.json":
            print(f"{file_path}: {existing_data}")
            
        return existing_data
    
    def exportCsv(csv_filename, filteredReservations):
        try:
            with open(csv_filename, '+w') as csvfile:
                fieldnames = ['Reservation ID', 'Date Start', 'Date End', 'Payment', 'Client ID', 'Bedroom ID']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for reservation in filteredReservations:
                    writer.writerow({
                        'Reservation ID': reservation['id'],
                        'Date Start': reservation['dateStart'],
                        'Date End': reservation['dateEnd'],
                        'Payment': reservation['payment'],
                        'Client ID': reservation['clientId'],
                        'Bedroom ID': reservation['bedroomId']
                    })
        except Exception as error:
            print(Colors.red(f"An error has been encountered while trying to save csv. This is the error: {error.args[1]}"))