import json
import os
import csv

class JSON:
    def saveJson(file_path, data):
        with open(file_path, "+w") as f:
            json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)


    def openJson(file_path) -> []:
        if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
            with open(file_path, '+r') as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        return existing_data
    
    def exportCsv(csv_filename, filteredReservations):
        with open(csv_filename, '+w') as csvfile:
            fieldnames = ['Reservation ID', 'Date Start', 'Date End', 'Payment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for reservation in filteredReservations:
                writer.writerow({
                    'Reservation ID': reservation['id'],
                    'Date Start': reservation['dateStart'],
                    'Date End': reservation['dateEnd'],
                    'Payment': reservation['payment']
                })