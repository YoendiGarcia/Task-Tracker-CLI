import json



class DBService:

    def load_database(path: str) -> dict[str,dict]:

        try:
            with open(path) as f:
                database = json.load(f)
        except FileNotFoundError:
            database = {}
        return database


    def save_database(database: dict[str, dict], path: str) -> None:
        with open(path, "w") as f:
            json.dump(database, f)


class TaskService:

   pass

