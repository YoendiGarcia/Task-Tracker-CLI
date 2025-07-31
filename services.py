import json
from schemas import Task,Status
from main import DB_PATH


class DBService:

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


class TaskService:

    def add_task(description: str):
       
       task = Task(description=description)

       task_dict = task.to_dict()

       tasks = DBService.load_database(DB_PATH)

       tasks[task.id] = task_dict

       DBService.save_database(tasks,DB_PATH)

       return task_dict

    def update_task(id: int, description: str):
       
       tasks = DBService.load_database(DB_PATH)

       if tasks[id]:

        tasks[id]["description"] = description

        DBService.save_database(tasks,DB_PATH)

        return tasks[id]
       
       raise Exception("Task not exists")

    def change_status(id: int, new_status: Status):

        tasks = DBService.load_database(DB_PATH)

        if tasks[id]:

         tasks[id]["status"] = str(new_status)

         DBService.save_database(tasks,DB_PATH)

         return tasks[id]
       
        raise Exception("Task not exists")
    
    def list_tasks(which: Status = None):
       
       tasks = DBService.load_database(DB_PATH)

       if which:
          
          tasks_filter = [task for task in tasks if task['status'] == str(which)]
          
          return tasks_filter
       
       return tasks

    def delete_task(id: int):
       
        tasks = DBService.load_database(DB_PATH)

        if tasks[id]:

            del tasks[id]

            DBService.save_database(tasks,DB_PATH)

            return tasks[id]
       
        raise Exception("Task not exists")



