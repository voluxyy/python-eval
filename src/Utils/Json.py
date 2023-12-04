import json
import os

class JSON:
    file_path = "clients.json"
    def save_clients_to_json(data):
        with open(JSON.file_path, "+w") as f:
            json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)

    def open_clients_json() -> []:
        if os.path.exists(JSON.file_path) and os.stat(JSON.file_path).st_size > 0:
            with open(JSON.file_path, '+r') as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        return existing_data