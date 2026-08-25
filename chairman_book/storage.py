import json
from pathlib import Path


DATA_FILE = Path("data.json")


def load_data():
    if not DATA_FILE.exists():
        return {
            "members": [],
            "payments": []
        }

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Sorry, the saved data appears to be corrupted.")
        return {
            "members": [],
            "payments": []
        }


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)