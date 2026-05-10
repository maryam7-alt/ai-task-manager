import json
import os

FILE_PATH = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("⚠️ Corrupted file. Resetting tasks.")
        return []


def save_tasks(tasks):
    temp_path = FILE_PATH + ".tmp"

    with open(temp_path, "w") as file:
        json.dump(tasks, file, indent=4)

    os.replace(temp_path, FILE_PATH)