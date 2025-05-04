def find_object_by_key(data: dict, first_char: str, key: str):
    for item in data[first_char]:
        if item["name"] == key:
            return item
