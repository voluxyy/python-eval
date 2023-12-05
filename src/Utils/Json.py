import json
import os

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