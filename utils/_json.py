import json


def read_json(file_path: str):
    with open(file_path, mode="r", encoding="utf-8") as file:
        content = json.load(file)
    return content
