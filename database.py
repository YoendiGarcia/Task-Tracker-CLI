import json


def load_database(path: str) -> dict[int,dict]:

    try:
        with open(path) as f:
            database = json.load(f)
    except FileNotFoundError:
        database = {}
    return database


def save_database(database: dict[int, dict], path: str) -> None:
    with open(path, "w") as f:
        json.dump(database, f)