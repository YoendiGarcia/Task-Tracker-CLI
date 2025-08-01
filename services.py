from schemas import Task,Status
from database import load_database,save_database


DB_PATH = "./tasks.json"


class TaskService:

    def add_task(description: str):
       
       task = Task(description=description)

       task_dict = task.to_dict()

       tasks = load_database(DB_PATH)

       tasks[task.id] = task_dict

       save_database(tasks,DB_PATH)


    def update_task(id: int, description: str):
       
        tasks = load_database(DB_PATH)

        tasks[id]["description"] = description

        save_database(tasks,DB_PATH)


    def change_status(id: int, new_status: Status):

        tasks = load_database(DB_PATH)

        tasks[id]["status"] = new_status.value

        save_database(tasks,DB_PATH)

        
    def mark_as_in_progress(id: int):
       
       TaskService.change_status(id,Status.IN_PROGRESS)
    
    def mark_as_done(id: int):
       
       TaskService.change_status(id,Status.DONE)
       
    
    def list_tasks(status: Status = "all"):
       
        tasks = load_database(DB_PATH)

        if status != "all":
          
            tasks = dict([(key,value) for key,value in tasks.items() if value['status'] == status])
       
        for key in tasks.keys():
          
            print(f"ID: {key}")
            print(f"Description: {tasks[key]["description"]}")
            print(f"Status: {tasks[key]["status"]}")
            print(f"Created at: {tasks[key]["created_at"]}")
            print(f"Updated at: {tasks[key]["updated_at"]}")
            print("-----------------------------------------")
       

    def delete_task(id: int):
       
        tasks = load_database(DB_PATH)

        del tasks[id]

        save_database(tasks,DB_PATH)

       



